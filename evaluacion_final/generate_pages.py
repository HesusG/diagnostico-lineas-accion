#!/usr/bin/env python3
"""
Generador de páginas HTML para GitHub Pages.
Convierte los feedbacks de Markdown a HTML con estilo institucional.
"""

import json
import re
from pathlib import Path
from datetime import datetime

# Template HTML para el índice
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Evaluaciones - CD2001B</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Evaluaciones Finales</h1>
            <p class="subtitle">CD2001B - Diagnóstico para Líneas de Acción</p>
            <p class="date">Generado: {fecha}</p>
        </header>

        <section class="summary">
            <h2>Resumen del Grupo</h2>
            <div class="stats">
                <div class="stat-card">
                    <span class="stat-number">{total_estudiantes}</span>
                    <span class="stat-label">Estudiantes</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">{promedio:.1f}</span>
                    <span class="stat-label">Promedio</span>
                </div>
                <div class="stat-card destacado">
                    <span class="stat-number">{destacados}</span>
                    <span class="stat-label">Destacados</span>
                </div>
            </div>
        </section>

        <section class="students">
            <h2>Evaluaciones Individuales</h2>
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Estudiante</th>
                        <th>Nota</th>
                        <th>Nivel</th>
                        <th>Feedback</th>
                    </tr>
                </thead>
                <tbody>
                    {filas_estudiantes}
                </tbody>
            </table>
        </section>

        <footer>
            <p>Evaluación realizada con sistema multi-agente y consenso Wide-Band Delphi</p>
            <p>Tecnológico de Monterrey - {año}</p>
        </footer>
    </div>
</body>
</html>
"""

# Template HTML para cada estudiante
STUDENT_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Feedback - {nombre}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <div class="container">
        <header>
            <a href="../index.html" class="back-link">← Volver al índice</a>
            <h1>{nombre}</h1>
            <div class="nota-final {nivel_class}">
                <span class="nota">{nota}</span>
                <span class="nivel">{nivel}</span>
            </div>
        </header>

        <section class="resumen-subcompetencias">
            <h2>Resumen por Subcompetencia</h2>
            <div class="subcompetencias-grid">
                {cards_subcompetencias}
            </div>
        </section>

        <section class="detalle">
            <h2>Detalle de Evaluación</h2>
            {detalle_html}
        </section>

        {observaciones_profesor}

        <footer>
            <p>Evaluación generada: {fecha}</p>
            <p><a href="../index.html">← Volver al índice</a></p>
        </footer>
    </div>
</body>
</html>
"""

# CSS institucional
CSS_CONTENT = """
:root {
    --tec-blue: #003366;
    --tec-light-blue: #0066cc;
    --destacado: #28a745;
    --solido: #17a2b8;
    --basico: #ffc107;
    --incipiente: #dc3545;
    --bg-light: #f8f9fa;
    --text-dark: #212529;
    --border-color: #dee2e6;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
    line-height: 1.6;
    color: var(--text-dark);
    background-color: var(--bg-light);
}

.container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;
}

header {
    background: linear-gradient(135deg, var(--tec-blue), var(--tec-light-blue));
    color: white;
    padding: 30px;
    border-radius: 10px;
    margin-bottom: 30px;
    text-align: center;
}

header h1 {
    font-size: 2em;
    margin-bottom: 10px;
}

.subtitle {
    opacity: 0.9;
    font-size: 1.1em;
}

.date {
    opacity: 0.7;
    font-size: 0.9em;
    margin-top: 10px;
}

.back-link {
    color: white;
    text-decoration: none;
    display: inline-block;
    margin-bottom: 15px;
    opacity: 0.8;
}

.back-link:hover {
    opacity: 1;
}

/* Nota final */
.nota-final {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    background: rgba(255,255,255,0.2);
    padding: 20px 40px;
    border-radius: 10px;
    margin-top: 20px;
}

.nota-final .nota {
    font-size: 3em;
    font-weight: bold;
}

.nota-final .nivel {
    font-size: 1.2em;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.nota-final.destacado { background: var(--destacado); }
.nota-final.solido { background: var(--solido); }
.nota-final.basico { background: var(--basico); color: var(--text-dark); }
.nota-final.incipiente { background: var(--incipiente); }

/* Stats */
.stats {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
}

.stat-card {
    background: white;
    padding: 20px 30px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.stat-card.destacado {
    border: 2px solid var(--destacado);
}

.stat-number {
    display: block;
    font-size: 2.5em;
    font-weight: bold;
    color: var(--tec-blue);
}

.stat-label {
    color: #666;
    font-size: 0.9em;
}

/* Tabla */
section {
    background: white;
    padding: 25px;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

section h2 {
    color: var(--tec-blue);
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid var(--tec-light-blue);
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
}

th {
    background: var(--tec-blue);
    color: white;
}

tr:hover {
    background: var(--bg-light);
}

.badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: 500;
}

.badge.destacado { background: var(--destacado); color: white; }
.badge.solido { background: var(--solido); color: white; }
.badge.basico { background: var(--basico); color: var(--text-dark); }
.badge.incipiente { background: var(--incipiente); color: white; }

.btn {
    display: inline-block;
    padding: 8px 16px;
    background: var(--tec-light-blue);
    color: white;
    text-decoration: none;
    border-radius: 5px;
    font-size: 0.9em;
}

.btn:hover {
    background: var(--tec-blue);
}

/* Subcompetencias grid */
.subcompetencias-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 15px;
}

.subcomp-card {
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 15px;
    border-left: 4px solid var(--tec-blue);
}

.subcomp-card.destacado { border-left-color: var(--destacado); }
.subcomp-card.solido { border-left-color: var(--solido); }
.subcomp-card.basico { border-left-color: var(--basico); }
.subcomp-card.incipiente { border-left-color: var(--incipiente); }

.subcomp-card h3 {
    font-size: 0.9em;
    color: #666;
    margin-bottom: 5px;
}

.subcomp-card .puntos {
    font-size: 1.5em;
    font-weight: bold;
    color: var(--tec-blue);
}

.subcomp-card .nivel-badge {
    font-size: 0.8em;
    margin-left: 10px;
}

/* Detalle */
.detalle-subcomp {
    margin-bottom: 25px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--border-color);
}

.detalle-subcomp:last-child {
    border-bottom: none;
}

.detalle-subcomp h3 {
    color: var(--tec-blue);
    margin-bottom: 15px;
}

.detalle-subcomp h4 {
    font-size: 0.95em;
    color: #555;
    margin: 10px 0 5px;
}

.detalle-subcomp ul {
    margin-left: 20px;
    color: #666;
}

.detalle-subcomp li {
    margin-bottom: 5px;
}

.retroalimentacion {
    background: var(--bg-light);
    padding: 15px;
    border-radius: 5px;
    margin-top: 10px;
    font-style: italic;
}

.observaciones-profesor {
    background: #fff3cd;
    border: 1px solid #ffc107;
    border-radius: 8px;
    padding: 20px;
    margin-top: 20px;
}

.observaciones-profesor h3 {
    color: #856404;
    margin-bottom: 10px;
}

/* Footer */
footer {
    text-align: center;
    padding: 20px;
    color: #666;
    font-size: 0.9em;
}

footer a {
    color: var(--tec-light-blue);
}

/* Responsive */
@media (max-width: 768px) {
    .container {
        padding: 10px;
    }

    header {
        padding: 20px;
    }

    header h1 {
        font-size: 1.5em;
    }

    .stats {
        flex-direction: column;
        align-items: center;
    }

    table {
        font-size: 0.9em;
    }

    th, td {
        padding: 8px;
    }
}
"""


def slugify(text: str) -> str:
    """Convierte un nombre a un slug para URL."""
    text = text.lower()
    text = re.sub(r'[áàäâ]', 'a', text)
    text = re.sub(r'[éèëê]', 'e', text)
    text = re.sub(r'[íìïî]', 'i', text)
    text = re.sub(r'[óòöô]', 'o', text)
    text = re.sub(r'[úùüû]', 'u', text)
    text = re.sub(r'[ñ]', 'n', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text


def nivel_to_class(nivel: str) -> str:
    """Convierte nivel a clase CSS."""
    mapping = {
        "Destacado": "destacado",
        "Sólido": "solido",
        "Básico": "basico",
        "Incipiente": "incipiente",
        "Sin evidencia": "incipiente"
    }
    return mapping.get(nivel, "basico")


def generar_pagina_estudiante(eval_data: dict, output_dir: Path) -> str:
    """Genera la página HTML para un estudiante."""
    nombre = eval_data["estudiante"]
    nota = eval_data["nota_final"]
    nivel = eval_data["nivel_final"]
    eval_final = eval_data["evaluacion_final"]

    # Cards de subcompetencias
    cards = ""
    from rubrics import RUBRICAS
    for codigo in RUBRICAS.keys():
        if codigo.startswith("_"):
            continue
        rubrica = RUBRICAS[codigo]
        ev = eval_final.get(codigo, {})
        puntos = ev.get("puntos", 0)
        nivel_sub = ev.get("nivel", "Sin evidencia")
        nivel_class = nivel_to_class(nivel_sub)

        cards += f"""
        <div class="subcomp-card {nivel_class}">
            <h3>{codigo}</h3>
            <p><strong>{rubrica['nombre']}</strong></p>
            <span class="puntos">{puntos}</span>
            <span class="badge {nivel_class} nivel-badge">{nivel_sub}</span>
        </div>
        """

    # Detalle por subcompetencia
    detalle = ""
    for codigo in RUBRICAS.keys():
        if codigo.startswith("_"):
            continue
        rubrica = RUBRICAS[codigo]
        ev = eval_final.get(codigo, {})

        detalle += f"""
        <div class="detalle-subcomp">
            <h3>{codigo} - {rubrica['nombre']}</h3>
            <p><strong>Nivel:</strong> {ev.get('nivel', 'N/A')} ({ev.get('puntos', 0)} puntos)</p>
        """

        if ev.get("evidencias"):
            detalle += "<h4>Evidencias encontradas:</h4><ul>"
            for e in ev["evidencias"][:3]:
                detalle += f"<li>{e}</li>"
            detalle += "</ul>"

        if ev.get("fortalezas"):
            detalle += "<h4>Fortalezas:</h4><ul>"
            for f in ev["fortalezas"][:3]:
                detalle += f"<li>{f}</li>"
            detalle += "</ul>"

        if ev.get("areas_mejora"):
            detalle += "<h4>Áreas de mejora:</h4><ul>"
            for a in ev["areas_mejora"][:3]:
                detalle += f"<li>{a}</li>"
            detalle += "</ul>"

        if ev.get("retroalimentacion"):
            detalle += f'<div class="retroalimentacion">{ev["retroalimentacion"]}</div>'

        detalle += "</div>"

    # Observaciones del profesor
    obs_html = ""
    if eval_final.get("_observaciones_profesor") or eval_final.get("_comentario_profesor"):
        obs_html = '<section class="observaciones-profesor"><h3>📝 Observaciones del Profesor</h3>'
        if eval_final.get("_observaciones_profesor"):
            obs_html += "<ul>"
            for obs in eval_final["_observaciones_profesor"]:
                obs_html += f"<li>{obs}</li>"
            obs_html += "</ul>"
        if eval_final.get("_comentario_profesor"):
            obs_html += f'<p><strong>Comentario:</strong> {eval_final["_comentario_profesor"]}</p>'
        obs_html += "</section>"

    # Generar HTML
    html = STUDENT_TEMPLATE.format(
        nombre=nombre,
        nota=nota,
        nivel=nivel,
        nivel_class=nivel_to_class(nivel),
        cards_subcompetencias=cards,
        detalle_html=detalle,
        observaciones_profesor=obs_html,
        fecha=eval_data.get("fecha", datetime.now().isoformat())[:10]
    )

    # Guardar
    slug = slugify(nombre)
    filepath = output_dir / "students" / f"{slug}.html"
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    return slug


def generar_indice(evaluaciones: list, output_dir: Path):
    """Genera la página índice con todos los estudiantes."""
    # Calcular estadísticas
    total = len(evaluaciones)
    promedio = sum(e["nota_final"] for e in evaluaciones) / total if total > 0 else 0
    destacados = sum(1 for e in evaluaciones if e["nivel_final"] == "Destacado")

    # Generar filas de la tabla
    filas = ""
    for i, ev in enumerate(sorted(evaluaciones, key=lambda x: x["estudiante"]), 1):
        nombre = ev["estudiante"]
        nota = ev["nota_final"]
        nivel = ev["nivel_final"]
        slug = slugify(nombre)
        nivel_class = nivel_to_class(nivel)

        filas += f"""
        <tr>
            <td>{i}</td>
            <td>{nombre}</td>
            <td><strong>{nota}</strong></td>
            <td><span class="badge {nivel_class}">{nivel}</span></td>
            <td><a href="students/{slug}.html" class="btn">Ver feedback</a></td>
        </tr>
        """

    # Generar HTML
    html = INDEX_TEMPLATE.format(
        fecha=datetime.now().strftime("%d/%m/%Y %H:%M"),
        total_estudiantes=total,
        promedio=promedio,
        destacados=destacados,
        filas_estudiantes=filas,
        año=datetime.now().year
    )

    # Guardar
    with open(output_dir / "index.html", 'w', encoding='utf-8') as f:
        f.write(html)


def main():
    print("=" * 60)
    print("  GENERADOR DE PÁGINAS - GitHub Pages")
    print("=" * 60)

    # Rutas
    base_dir = Path(__file__).parent
    evaluations_dir = base_dir / "output" / "evaluations"
    docs_dir = base_dir / "docs"

    # Verificar que existan evaluaciones
    if not evaluations_dir.exists():
        print(f"\nERROR: No existe el directorio de evaluaciones: {evaluations_dir}")
        print("Ejecuta primero: python evaluate.py")
        return

    json_files = list(evaluations_dir.glob("*.json"))
    if not json_files:
        print("\nERROR: No se encontraron evaluaciones.")
        print("Ejecuta primero: python evaluate.py")
        return

    print(f"\nEvaluaciones encontradas: {len(json_files)}")

    # Crear directorio de salida
    docs_dir.mkdir(parents=True, exist_ok=True)
    (docs_dir / "students").mkdir(exist_ok=True)

    # Guardar CSS
    with open(docs_dir / "style.css", 'w', encoding='utf-8') as f:
        f.write(CSS_CONTENT)
    print("✓ CSS generado")

    # Procesar evaluaciones
    evaluaciones = []
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            eval_data = json.load(f)

        slug = generar_pagina_estudiante(eval_data, docs_dir)
        evaluaciones.append(eval_data)
        print(f"✓ Página generada: {eval_data['estudiante']} → {slug}.html")

    # Generar índice
    generar_indice(evaluaciones, docs_dir)
    print("✓ Índice generado")

    print(f"\n{'=' * 60}")
    print(f"  Páginas generadas en: {docs_dir}")
    print(f"  Total: {len(evaluaciones)} estudiantes")
    print("=" * 60)
    print("\nPara ver las páginas localmente:")
    print(f"  cd {docs_dir}")
    print("  python -m http.server 8000")
    print("  Abre http://localhost:8000 en tu navegador")
    print("\nPara publicar en GitHub Pages:")
    print("  1. Sube la carpeta 'docs' a tu repositorio")
    print("  2. En Settings → Pages, selecciona 'docs' como source")


if __name__ == "__main__":
    main()
