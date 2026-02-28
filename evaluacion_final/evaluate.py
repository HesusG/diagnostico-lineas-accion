#!/usr/bin/env python3
"""
Sistema de Evaluación Multi-Agente con Wide-Band Delphi y Revisión Humana.
Usa Together.ai (DeepSeek) para las evaluaciones.
"""

import os
import sys
import json
import re
import time
from pathlib import Path
from datetime import datetime

import requests
from dotenv import load_dotenv

from rubrics import RUBRICAS, PONDERACIONES, get_rubric_prompt, calcular_nota_final, NIVELES

# Cargar variables de entorno
load_dotenv(Path(__file__).parent.parent / ".env")

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
MODEL = "deepseek-ai/DeepSeek-V3"  # Modelo de DeepSeek en Together.ai


def call_together_api(prompt: str, student_text: str, max_retries: int = 3) -> dict:
    """
    Llama a la API de Together.ai con DeepSeek.
    Maneja JSON malformado con fallbacks.
    """
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"## Trabajo del Estudiante:\n\n{student_text[:15000]}"}  # Limitar texto
    ]

    payload = {
        "model": MODEL,
        "messages": messages,
        "max_tokens": 1000,
        "temperature": 0.3,
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(TOGETHER_API_URL, headers=headers, json=payload, timeout=60)
            response.raise_for_status()

            result = response.json()
            content = result["choices"][0]["message"]["content"]

            # Intentar parsear JSON
            return parse_json_response(content)

        except requests.exceptions.RequestException as e:
            print(f"    Error API (intento {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            continue

        except Exception as e:
            print(f"    Error inesperado: {e}")
            continue

    # Si todo falla, retornar evaluación por defecto
    return {
        "nivel": "Básico",
        "puntos": 75,
        "evidencias": ["No se pudo evaluar automáticamente"],
        "fortalezas": [],
        "areas_mejora": ["Requiere revisión manual"],
        "retroalimentacion": "Evaluación pendiente de revisión manual.",
        "error": True
    }


def parse_json_response(content: str) -> dict:
    """
    Parsea la respuesta JSON con múltiples estrategias de fallback.
    """
    # Estrategia 1: JSON directo
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        pass

    # Estrategia 2: Extraer JSON con regex
    json_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
    matches = re.findall(json_pattern, content, re.DOTALL)
    for match in matches:
        try:
            return json.loads(match)
        except json.JSONDecodeError:
            continue

    # Estrategia 3: Buscar campos específicos con regex
    nivel_match = re.search(r'"nivel"\s*:\s*"([^"]+)"', content)
    puntos_match = re.search(r'"puntos"\s*:\s*(\d+)', content)

    if nivel_match and puntos_match:
        nivel = nivel_match.group(1)
        puntos = int(puntos_match.group(1))

        # Validar nivel
        niveles_validos = ["Destacado", "Sólido", "Básico", "Incipiente", "Sin evidencia"]
        if nivel not in niveles_validos:
            nivel = "Básico"
            puntos = 75

        return {
            "nivel": nivel,
            "puntos": puntos,
            "evidencias": ["Extraído de respuesta parcial"],
            "fortalezas": [],
            "areas_mejora": [],
            "retroalimentacion": content[:500],
            "parsed_fallback": True
        }

    # Estrategia 4: Valor por defecto
    return {
        "nivel": "Básico",
        "puntos": 75,
        "evidencias": [],
        "fortalezas": [],
        "areas_mejora": [],
        "retroalimentacion": content[:500] if content else "Sin respuesta",
        "parse_failed": True
    }


def evaluate_student_round1(student_name: str, student_text: str) -> dict:
    """
    Ronda 1: Evaluación independiente por cada agente.
    """
    print(f"\n  Ronda 1 - Evaluación independiente...")
    evaluaciones = {}

    for codigo in RUBRICAS.keys():
        print(f"    Evaluando {codigo}...", end=" ", flush=True)
        prompt = get_rubric_prompt(codigo)
        resultado = call_together_api(prompt, student_text)
        evaluaciones[codigo] = resultado
        print(f"{resultado['nivel']} ({resultado['puntos']})")
        time.sleep(1)  # Rate limiting

    return evaluaciones


def evaluate_student_round2(student_name: str, student_text: str, eval_round1: dict) -> dict:
    """
    Ronda 2: Revisión con contexto cruzado.
    Cada agente ve el resumen de otras evaluaciones.
    """
    print(f"\n  Ronda 2 - Revisión con contexto cruzado...")

    # Crear resumen de Ronda 1
    resumen = "## Resumen de evaluaciones previas:\n"
    for codigo, eval_data in eval_round1.items():
        nombre = RUBRICAS[codigo]["nombre"]
        resumen += f"- {codigo} ({nombre}): {eval_data['nivel']} ({eval_data['puntos']} pts)\n"

    evaluaciones = {}

    for codigo in RUBRICAS.keys():
        print(f"    Revisando {codigo}...", end=" ", flush=True)

        prompt_base = get_rubric_prompt(codigo)
        prompt_r2 = f"""{prompt_base}

## CONTEXTO ADICIONAL (Ronda 2 Delphi):
Otros evaluadores han dado las siguientes calificaciones a este trabajo:
{resumen}

Considera si tu evaluación es consistente con las demás.
Si hay discrepancias mayores a 15 puntos, justifica tu posición.
Puedes ajustar tu evaluación si encuentras nuevas evidencias.
"""
        resultado = call_together_api(prompt_r2, student_text)
        evaluaciones[codigo] = resultado

        # Detectar cambios significativos
        cambio = resultado['puntos'] - eval_round1[codigo]['puntos']
        indicador = ""
        if abs(cambio) > 10:
            indicador = f" (cambió {cambio:+d})"

        print(f"{resultado['nivel']} ({resultado['puntos']}){indicador}")
        time.sleep(1)

    return evaluaciones


def identificar_puntos_criticos(eval_r1: dict, eval_r2: dict) -> dict:
    """
    Identifica puntos críticos y discrepancias entre rondas.
    """
    criticos = {
        "discrepancias": [],
        "areas_debiles": [],
        "areas_fuertes": [],
        "requiere_atencion": []
    }

    for codigo in RUBRICAS.keys():
        nombre = RUBRICAS[codigo]["nombre"]
        p1 = eval_r1[codigo]["puntos"]
        p2 = eval_r2[codigo]["puntos"]
        promedio = (p1 + p2) / 2

        # Discrepancias entre rondas
        if abs(p1 - p2) > 10:
            criticos["discrepancias"].append({
                "codigo": codigo,
                "nombre": nombre,
                "ronda1": p1,
                "ronda2": p2,
                "diferencia": abs(p1 - p2)
            })

        # Áreas débiles (promedio < 75)
        if promedio < 75:
            criticos["areas_debiles"].append({
                "codigo": codigo,
                "nombre": nombre,
                "promedio": promedio,
                "evidencias": eval_r2[codigo].get("evidencias", []),
                "areas_mejora": eval_r2[codigo].get("areas_mejora", [])
            })

        # Áreas fuertes (promedio >= 90)
        if promedio >= 90:
            criticos["areas_fuertes"].append({
                "codigo": codigo,
                "nombre": nombre,
                "promedio": promedio,
                "fortalezas": eval_r2[codigo].get("fortalezas", [])
            })

        # Requiere atención especial
        if eval_r2[codigo].get("error") or eval_r2[codigo].get("parse_failed"):
            criticos["requiere_atencion"].append({
                "codigo": codigo,
                "nombre": nombre,
                "razon": "Evaluación automática falló - requiere revisión manual"
            })

    return criticos


def mostrar_resumen_para_revision(student_name: str, eval_r1: dict, eval_r2: dict, criticos: dict):
    """
    Muestra el resumen para revisión humana antes de Ronda 3.
    """
    print("\n" + "=" * 70)
    print(f"  REVISIÓN HUMANA: {student_name}")
    print("=" * 70)

    # Tabla de evaluaciones
    print("\n  Evaluaciones por subcompetencia:")
    print("  " + "-" * 60)
    print(f"  {'Subcompetencia':<30} {'R1':>8} {'R2':>8} {'Prom':>8}")
    print("  " + "-" * 60)

    for codigo in RUBRICAS.keys():
        nombre = RUBRICAS[codigo]["nombre"][:28]
        p1 = eval_r1[codigo]["puntos"]
        p2 = eval_r2[codigo]["puntos"]
        prom = (p1 + p2) / 2
        print(f"  {nombre:<30} {p1:>8} {p2:>8} {prom:>8.1f}")

    # Nota preliminar
    eval_promedio = {c: (eval_r1[c]["puntos"] + eval_r2[c]["puntos"]) / 2 for c in RUBRICAS.keys()}
    nota_prelim, nivel_prelim = calcular_nota_final(eval_promedio)
    print("  " + "-" * 60)
    print(f"  {'NOTA PRELIMINAR':<30} {'':<8} {'':<8} {nota_prelim:>8.1f} ({nivel_prelim})")

    # Puntos críticos
    if criticos["discrepancias"]:
        print("\n  ⚠️  DISCREPANCIAS DETECTADAS:")
        for d in criticos["discrepancias"]:
            print(f"     - {d['nombre']}: R1={d['ronda1']} vs R2={d['ronda2']} (dif: {d['diferencia']})")

    if criticos["areas_debiles"]:
        print("\n  ⚠️  ÁREAS DÉBILES (< 75 pts):")
        for a in criticos["areas_debiles"]:
            print(f"     - {a['nombre']}: {a['promedio']:.1f} pts")
            if a["areas_mejora"]:
                for mejora in a["areas_mejora"][:2]:
                    print(f"       → {mejora[:60]}...")

    if criticos["areas_fuertes"]:
        print("\n  ✓  ÁREAS FUERTES (≥ 90 pts):")
        for a in criticos["areas_fuertes"]:
            print(f"     - {a['nombre']}: {a['promedio']:.1f} pts")

    if criticos["requiere_atencion"]:
        print("\n  ❗ REQUIERE ATENCIÓN MANUAL:")
        for r in criticos["requiere_atencion"]:
            print(f"     - {r['nombre']}: {r['razon']}")


def obtener_input_humano(student_name: str, criticos: dict, auto_mode: bool = False) -> dict:
    """
    Obtiene input del profesor para la Ronda 3.
    Preguntas sencillas y directas.

    Args:
        student_name: Nombre del estudiante
        criticos: Puntos críticos identificados
        auto_mode: Si True, salta las preguntas y usa valores por defecto
    """
    input_humano = {
        "observaciones": [],
        "ajustes": {},
        "comentario_final": ""
    }

    # En modo automático o sin terminal, saltar preguntas
    if auto_mode or not sys.stdin.isatty():
        print("\n  [Modo automático - sin revisión humana]")
        return input_humano

    print("\n" + "-" * 70)
    print("  Por favor, revisa el PDF del estudiante y responde:")
    print("-" * 70)

    # Pregunta 1: Observaciones generales
    print("\n  1. ¿Observaste algo importante que los agentes pudieron pasar por alto?")
    print("     (Escribe tu observación o presiona Enter para omitir)")
    try:
        obs = input("     > ").strip()
        if obs:
            input_humano["observaciones"].append(obs)
    except EOFError:
        pass

    # Pregunta 2: Si hay áreas débiles, preguntar específicamente
    if criticos["areas_debiles"]:
        area = criticos["areas_debiles"][0]
        print(f"\n  2. El área más débil es '{area['nombre']}' ({area['promedio']:.0f} pts).")
        print("     ¿Crees que la calificación es justa? (s/n/ajustar)")
        try:
            resp = input("     > ").strip().lower()

            if resp == "n" or resp == "ajustar":
                print("     ¿Qué puntuación sugieres? (55/75/88/100)")
                try:
                    nueva = int(input("     > ").strip())
                    if nueva in [55, 75, 88, 100]:
                        input_humano["ajustes"][area["codigo"]] = {
                            "puntos_sugeridos": nueva,
                            "razon": "Ajuste del profesor"
                        }
                except ValueError:
                    pass
        except EOFError:
            pass

    # Pregunta 3: Si hay discrepancias
    if criticos["discrepancias"]:
        disc = criticos["discrepancias"][0]
        print(f"\n  3. Hay discrepancia en '{disc['nombre']}' (R1:{disc['ronda1']} vs R2:{disc['ronda2']}).")
        print("     ¿Cuál te parece más acertada? (1/2/otra)")
        try:
            resp = input("     > ").strip()

            if resp == "1":
                input_humano["ajustes"][disc["codigo"]] = {
                    "puntos_sugeridos": disc["ronda1"],
                    "razon": "Profesor prefiere evaluación R1"
                }
            elif resp == "2":
                input_humano["ajustes"][disc["codigo"]] = {
                    "puntos_sugeridos": disc["ronda2"],
                    "razon": "Profesor prefiere evaluación R2"
                }
            elif resp.isdigit():
                input_humano["ajustes"][disc["codigo"]] = {
                    "puntos_sugeridos": int(resp),
                    "razon": "Ajuste manual del profesor"
                }
        except EOFError:
            pass

    # Pregunta 4: Comentario adicional
    print("\n  4. ¿Algún comentario adicional para el feedback del estudiante?")
    print("     (Escribe o presiona Enter para omitir)")
    try:
        comentario = input("     > ").strip()
        if comentario:
            input_humano["comentario_final"] = comentario
    except EOFError:
        pass

    return input_humano


def evaluate_student_round3(student_name: str, student_text: str,
                            eval_r1: dict, eval_r2: dict,
                            input_humano: dict) -> dict:
    """
    Ronda 3: Consenso final incorporando feedback humano.
    """
    print(f"\n  Ronda 3 - Consenso final...")

    evaluaciones_finales = {}

    for codigo in RUBRICAS.keys():
        nombre = RUBRICAS[codigo]["nombre"]

        # Si el profesor hizo un ajuste específico
        if codigo in input_humano.get("ajustes", {}):
            ajuste = input_humano["ajustes"][codigo]
            puntos = ajuste["puntos_sugeridos"]

            # Mapear puntos a nivel
            nivel = "Básico"
            for n, p in NIVELES.items():
                if p == puntos:
                    nivel = n
                    break

            evaluaciones_finales[codigo] = {
                "nivel": nivel,
                "puntos": puntos,
                "evidencias": eval_r2[codigo].get("evidencias", []),
                "fortalezas": eval_r2[codigo].get("fortalezas", []),
                "areas_mejora": eval_r2[codigo].get("areas_mejora", []),
                "retroalimentacion": eval_r2[codigo].get("retroalimentacion", ""),
                "ajuste_profesor": ajuste["razon"]
            }
            print(f"    {codigo}: {nivel} ({puntos}) [AJUSTADO POR PROFESOR]")

        else:
            # Promedio de R1 y R2, redondeado al nivel más cercano
            p1 = eval_r1[codigo]["puntos"]
            p2 = eval_r2[codigo]["puntos"]
            promedio = (p1 + p2) / 2

            # Redondear al nivel más cercano
            niveles_pts = [(100, "Destacado"), (88, "Sólido"), (75, "Básico"), (55, "Incipiente"), (0, "Sin evidencia")]
            puntos_final = min(niveles_pts, key=lambda x: abs(x[0] - promedio))[0]
            nivel_final = [n for p, n in niveles_pts if p == puntos_final][0]

            evaluaciones_finales[codigo] = {
                "nivel": nivel_final,
                "puntos": puntos_final,
                "evidencias": eval_r2[codigo].get("evidencias", []),
                "fortalezas": eval_r2[codigo].get("fortalezas", []),
                "areas_mejora": eval_r2[codigo].get("areas_mejora", []),
                "retroalimentacion": eval_r2[codigo].get("retroalimentacion", ""),
                "promedio_delphi": promedio
            }
            print(f"    {codigo}: {nivel_final} ({puntos_final})")

    # Agregar observaciones del profesor
    if input_humano.get("observaciones"):
        evaluaciones_finales["_observaciones_profesor"] = input_humano["observaciones"]

    if input_humano.get("comentario_final"):
        evaluaciones_finales["_comentario_profesor"] = input_humano["comentario_final"]

    return evaluaciones_finales


def generar_feedback_markdown(student_name: str, evaluaciones: dict) -> str:
    """
    Genera el feedback en formato Markdown.
    """
    # Calcular nota final
    notas = {c: evaluaciones[c]["puntos"] for c in RUBRICAS.keys()}
    nota_final, nivel_final = calcular_nota_final(notas)

    fecha = datetime.now().strftime("%d/%m/%Y")

    md = f"""# Retroalimentación: {student_name}

**Calificación Final: {nota_final}/100 - {nivel_final}**

*Fecha de evaluación: {fecha}*

---

## Resumen por Subcompetencia

| Subcompetencia | Nivel | Puntos |
|----------------|-------|--------|
"""

    for codigo in RUBRICAS.keys():
        nombre = RUBRICAS[codigo]["nombre"]
        eval_data = evaluaciones[codigo]
        md += f"| {codigo} - {nombre} | {eval_data['nivel']} | {eval_data['puntos']} |\n"

    md += f"\n**Nota Final Ponderada: {nota_final}**\n\n---\n\n"

    # Detalle por subcompetencia
    md += "## Detalle por Subcompetencia\n\n"

    for codigo in RUBRICAS.keys():
        nombre = RUBRICAS[codigo]["nombre"]
        eval_data = evaluaciones[codigo]

        md += f"### {codigo} - {nombre}\n\n"
        md += f"**Nivel alcanzado:** {eval_data['nivel']} ({eval_data['puntos']} puntos)\n\n"

        if eval_data.get("evidencias"):
            md += "**Evidencias encontradas:**\n"
            for ev in eval_data["evidencias"][:3]:
                md += f"- {ev}\n"
            md += "\n"

        if eval_data.get("fortalezas"):
            md += "**Fortalezas:**\n"
            for f in eval_data["fortalezas"][:3]:
                md += f"- {f}\n"
            md += "\n"

        if eval_data.get("areas_mejora"):
            md += "**Áreas de mejora:**\n"
            for a in eval_data["areas_mejora"][:3]:
                md += f"- {a}\n"
            md += "\n"

        if eval_data.get("retroalimentacion"):
            md += f"**Retroalimentación:** {eval_data['retroalimentacion']}\n\n"

        if eval_data.get("ajuste_profesor"):
            md += f"*Nota: {eval_data['ajuste_profesor']}*\n\n"

        md += "---\n\n"

    # Observaciones del profesor
    if evaluaciones.get("_observaciones_profesor"):
        md += "## Observaciones del Profesor\n\n"
        for obs in evaluaciones["_observaciones_profesor"]:
            md += f"- {obs}\n"
        md += "\n"

    if evaluaciones.get("_comentario_profesor"):
        md += f"**Comentario final:** {evaluaciones['_comentario_profesor']}\n\n"

    md += "---\n\n"
    md += "*Evaluación generada con sistema multi-agente y consenso Wide-Band Delphi con supervisión humana.*\n"

    return md


def evaluar_estudiante(student_name: str, student_text: str, output_dir: Path, auto_mode: bool = False) -> dict:
    """
    Proceso completo de evaluación para un estudiante.

    Args:
        student_name: Nombre del estudiante
        student_text: Texto extraído del trabajo
        output_dir: Directorio de salida
        auto_mode: Si True, salta la revisión humana
    """
    print(f"\n{'=' * 70}")
    print(f"  EVALUANDO: {student_name}")
    print("=" * 70)

    # Ronda 1
    eval_r1 = evaluate_student_round1(student_name, student_text)

    # Ronda 2
    eval_r2 = evaluate_student_round2(student_name, student_text, eval_r1)

    # Identificar puntos críticos
    criticos = identificar_puntos_criticos(eval_r1, eval_r2)

    # Mostrar resumen para revisión
    mostrar_resumen_para_revision(student_name, eval_r1, eval_r2, criticos)

    # Obtener input humano
    input_humano = obtener_input_humano(student_name, criticos, auto_mode)

    # Ronda 3 - Consenso final
    eval_final = evaluate_student_round3(student_name, student_text, eval_r1, eval_r2, input_humano)

    # Calcular nota final
    notas = {c: eval_final[c]["puntos"] for c in RUBRICAS.keys()}
    nota_final, nivel_final = calcular_nota_final(notas)

    print(f"\n  ✓ NOTA FINAL: {nota_final}/100 - {nivel_final}")

    # Guardar evaluación completa (JSON)
    eval_completa = {
        "estudiante": student_name,
        "fecha": datetime.now().isoformat(),
        "ronda1": eval_r1,
        "ronda2": eval_r2,
        "puntos_criticos": criticos,
        "input_humano": input_humano,
        "evaluacion_final": eval_final,
        "nota_final": nota_final,
        "nivel_final": nivel_final
    }

    json_file = output_dir / "evaluations" / f"{student_name}.json"
    json_file.parent.mkdir(parents=True, exist_ok=True)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(eval_completa, f, ensure_ascii=False, indent=2)

    # Generar feedback Markdown
    feedback_md = generar_feedback_markdown(student_name, eval_final)
    md_file = output_dir / "feedback" / f"{student_name}.md"
    md_file.parent.mkdir(parents=True, exist_ok=True)
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(feedback_md)

    print(f"  ✓ Guardado: {json_file.name}, {md_file.name}")

    return eval_completa


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Sistema de Evaluación Multi-Agente')
    parser.add_argument('--student', '-s', type=int, help='Número del estudiante a evaluar (1-16)')
    parser.add_argument('--from-student', '-f', type=int, help='Continuar desde el estudiante N')
    parser.add_argument('--auto', '-a', action='store_true', help='Modo automático sin revisión humana')
    parser.add_argument('--list', '-l', action='store_true', help='Solo listar estudiantes')
    args = parser.parse_args()

    print("=" * 70)
    print("  SISTEMA DE EVALUACIÓN MULTI-AGENTE")
    print("  Wide-Band Delphi con Revisión Humana")
    print("=" * 70)

    # Verificar API key
    if not TOGETHER_API_KEY:
        print("\nERROR: No se encontró TOGETHER_API_KEY en .env")
        sys.exit(1)

    # Rutas
    base_dir = Path(__file__).parent
    extractions_dir = base_dir / "output" / "extractions"
    output_dir = base_dir / "output"

    # Verificar que existan las extracciones
    if not extractions_dir.exists():
        print(f"\nERROR: No existe el directorio de extracciones: {extractions_dir}")
        print("Ejecuta primero: python extract_text.py")
        sys.exit(1)

    # Listar estudiantes
    students = sorted([f.stem for f in extractions_dir.glob("*.txt")])

    if not students:
        print("\nERROR: No se encontraron archivos de texto extraído.")
        print("Ejecuta primero: python extract_text.py")
        sys.exit(1)

    print(f"\nEstudiantes encontrados: {len(students)}")
    for i, s in enumerate(students, 1):
        print(f"  {i}. {s}")

    # Si solo quiere listar, terminar aquí
    if args.list:
        sys.exit(0)

    # Procesar argumentos de línea de comandos
    if args.student:
        idx = args.student - 1
        if 0 <= idx < len(students):
            students = [students[idx]]
        else:
            print(f"ERROR: Estudiante {args.student} no existe (rango: 1-{len(students)})")
            sys.exit(1)
    elif args.from_student:
        idx = args.from_student - 1
        if 0 <= idx < len(students):
            students = students[idx:]
        else:
            print(f"ERROR: Estudiante {args.from_student} no existe (rango: 1-{len(students)})")
            sys.exit(1)
    elif sys.stdin.isatty():
        # Modo interactivo solo si hay terminal
        print("\n¿Qué deseas hacer?")
        print("  1. Evaluar todos los estudiantes")
        print("  2. Evaluar un estudiante específico")
        print("  3. Continuar desde un estudiante específico")

        opcion = input("\nOpción (1/2/3): ").strip()

        if opcion == "2":
            print("\nIngresa el número del estudiante:")
            try:
                idx = int(input("> ").strip()) - 1
                if 0 <= idx < len(students):
                    students = [students[idx]]
                else:
                    print("Índice inválido")
                    sys.exit(1)
            except ValueError:
                print("Entrada inválida")
                sys.exit(1)

        elif opcion == "3":
            print("\nIngresa el número del estudiante desde donde continuar:")
            try:
                idx = int(input("> ").strip()) - 1
                if 0 <= idx < len(students):
                    students = students[idx:]
                else:
                    print("Índice inválido")
                    sys.exit(1)
            except ValueError:
                print("Entrada inválida")
                sys.exit(1)

    resultados = []

    # Evaluar estudiantes
    for student_name in students:
        # Leer texto extraído
        text_file = extractions_dir / f"{student_name}.txt"
        with open(text_file, 'r', encoding='utf-8') as f:
            student_text = f.read()

        if student_text.startswith("ERROR"):
            print(f"\n⚠️  Saltando {student_name}: {student_text[:100]}")
            continue

        # Evaluar
        resultado = evaluar_estudiante(student_name, student_text, output_dir, auto_mode=args.auto)
        resultados.append(resultado)

        # Preguntar si continuar (solo en modo interactivo)
        if len(students) > 1 and student_name != students[-1] and sys.stdin.isatty() and not args.auto:
            print("\n" + "-" * 70)
            continuar = input("¿Continuar con el siguiente estudiante? (s/n): ").strip().lower()
            if continuar == "n":
                break

    # Resumen final
    print("\n" + "=" * 70)
    print("  RESUMEN FINAL")
    print("=" * 70)

    if resultados:
        print(f"\n  Estudiantes evaluados: {len(resultados)}")
        print("\n  " + "-" * 50)
        print(f"  {'Estudiante':<35} {'Nota':>8} {'Nivel':<12}")
        print("  " + "-" * 50)

        for r in resultados:
            print(f"  {r['estudiante'][:33]:<35} {r['nota_final']:>8.1f} {r['nivel_final']:<12}")

        print("  " + "-" * 50)

        promedio = sum(r['nota_final'] for r in resultados) / len(resultados)
        print(f"  {'PROMEDIO GRUPO':<35} {promedio:>8.1f}")

    print(f"\n  Archivos guardados en: {output_dir}")
    print("\n  Para generar las páginas web, ejecuta: python generate_pages.py")


if __name__ == "__main__":
    main()
