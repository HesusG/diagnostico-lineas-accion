#!/usr/bin/env python3
"""
Script para analizar resultados del Quiz Diagnóstico CD2001B
Genera estadísticas descriptivas para ayudar al profesor a entender el nivel del grupo
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Si tienes las respuestas en un CSV exportado de Google Forms/Excel
# El CSV debe tener columnas que correspondan a las preguntas del quiz

def analizar_quiz(archivo_csv):
    """
    Analiza las respuestas del quiz diagnóstico

    Parameters:
    -----------
    archivo_csv : str
        Ruta al archivo CSV con las respuestas

    Returns:
    --------
    DataFrame con resumen de resultados
    """

    # Cargar datos
    df = pd.read_csv(archivo_csv)

    print("="*70)
    print("📊 ANÁLISIS DEL QUIZ DIAGNÓSTICO - CD2001B")
    print("="*70)
    print(f"\nTotal de estudiantes: {len(df)}")

    # SECCIÓN 1: ESTADÍSTICA
    print("\n" + "="*70)
    print("📈 SECCIÓN 1: CONOCIMIENTOS DE ESTADÍSTICA")
    print("="*70)

    # Pregunta 1: Nivel de estadística
    if 'nivel_estadistica' in df.columns:
        print("\n🔍 Nivel actual de conocimiento en estadística:")
        nivel_stats = df['nivel_estadistica'].value_counts()
        print(nivel_stats)
        print(f"\nPorcentajes:")
        print(df['nivel_estadistica'].value_counts(normalize=True) * 100)

    # Pregunta 3: Conceptos estadísticos conocidos
    # (Requiere procesamiento de respuestas múltiples)

    # SECCIÓN 2: PYTHON
    print("\n" + "="*70)
    print("💻 SECCIÓN 2: EXPERIENCIA CON PYTHON")
    print("="*70)

    # Pregunta 7: Nivel de Python
    if 'nivel_python' in df.columns:
        print("\n🐍 Nivel de experiencia con Python:")
        python_stats = df['nivel_python'].value_counts()
        print(python_stats)

    # Pregunta 10: Uso de Google Colab
    if 'uso_colab' in df.columns:
        print("\n☁️ Experiencia con Google Colab:")
        colab_stats = df['uso_colab'].value_counts()
        print(colab_stats)

    # SECCIÓN 3: USO DE IA
    print("\n" + "="*70)
    print("🤖 SECCIÓN 3: USO DE INTELIGENCIA ARTIFICIAL")
    print("="*70)

    # Pregunta 12: Frecuencia de uso de IA
    if 'frecuencia_ia' in df.columns:
        print("\n📊 Frecuencia de uso de IA:")
        ia_freq = df['frecuencia_ia'].value_counts()
        print(ia_freq)

    # Pregunta 15: Uso avanzado (APIs/agentes)
    if 'uso_apis_agentes' in df.columns:
        print("\n🔧 Uso de APIs/agentes de IA:")
        apis_stats = df['uso_apis_agentes'].value_counts()
        print(apis_stats)

        # Calcular porcentaje que ha usado más allá de chat
        total = len(df)
        solo_chat = (df['uso_apis_agentes'] == 'A) No, solo he usado interfaces de chat').sum()
        print(f"\n📌 Estudiantes que solo usan chat: {solo_chat}/{total} ({solo_chat/total*100:.1f}%)")
        print(f"📌 Estudiantes con experiencia en APIs/agentes: {total-solo_chat}/{total} ({(total-solo_chat)/total*100:.1f}%)")

    # RESUMEN EJECUTIVO
    print("\n" + "="*70)
    print("📋 RESUMEN EJECUTIVO PARA EL PROFESOR")
    print("="*70)

    # Clasificar estudiantes en perfiles
    perfiles = {
        'principiantes': 0,
        'intermedios': 0,
        'avanzados': 0
    }

    # Lógica de clasificación (ajustar según columnas reales)
    # Ejemplo básico:
    for idx, row in df.iterrows():
        # Usar Pregunta 20 si existe
        if 'situacion_actual' in df.columns:
            sit = row['situacion_actual']
            if 'A)' in str(sit):
                perfiles['principiantes'] += 1
            elif 'E)' in str(sit):
                perfiles['avanzados'] += 1
            else:
                perfiles['intermedios'] += 1

    print("\n👥 PERFILES DE ESTUDIANTES:")
    print(f"   Principiantes: {perfiles['principiantes']} ({perfiles['principiantes']/len(df)*100:.1f}%)")
    print(f"   Intermedios: {perfiles['intermedios']} ({perfiles['intermedios']/len(df)*100:.1f}%)")
    print(f"   Avanzados: {perfiles['avanzados']} ({perfiles['avanzados']/len(df)*100:.1f}%)")

    print("\n💡 RECOMENDACIONES:")

    if perfiles['principiantes'] > len(df) * 0.5:
        print("   ⚠️  Más del 50% son principiantes - considerar:")
        print("      • Sesiones de nivelación en Python")
        print("      • Material introductorio adicional")
        print("      • Mentorías peer-to-peer")

    if perfiles['avanzados'] > len(df) * 0.3:
        print("   🚀 Hay estudiantes avanzados (>30%) - considerar:")
        print("      • Ejercicios desafiantes opcionales")
        print("      • Roles de TA/mentor en equipos")
        print("      • Proyectos de mayor complejidad")

    # Crear visualizaciones
    crear_visualizaciones(df)

    return df

def crear_visualizaciones(df):
    """Crea gráficos del análisis del quiz"""

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Gráfico 1: Nivel de estadística
    if 'nivel_estadistica' in df.columns:
        df['nivel_estadistica'].value_counts().plot(kind='bar', ax=axes[0, 0], color='steelblue')
        axes[0, 0].set_title('Nivel de Conocimiento en Estadística', fontweight='bold')
        axes[0, 0].set_ylabel('Número de Estudiantes')
        axes[0, 0].tick_params(axis='x', rotation=45)

    # Gráfico 2: Nivel de Python
    if 'nivel_python' in df.columns:
        df['nivel_python'].value_counts().plot(kind='bar', ax=axes[0, 1], color='orange')
        axes[0, 1].set_title('Nivel de Experiencia con Python', fontweight='bold')
        axes[0, 1].set_ylabel('Número de Estudiantes')
        axes[0, 1].tick_params(axis='x', rotation=45)

    # Gráfico 3: Frecuencia de uso de IA
    if 'frecuencia_ia' in df.columns:
        df['frecuencia_ia'].value_counts().plot(kind='bar', ax=axes[1, 0], color='green')
        axes[1, 0].set_title('Frecuencia de Uso de IA', fontweight='bold')
        axes[1, 0].set_ylabel('Número de Estudiantes')
        axes[1, 0].tick_params(axis='x', rotation=45)

    # Gráfico 4: Uso de Google Colab
    if 'uso_colab' in df.columns:
        df['uso_colab'].value_counts().plot(kind='bar', ax=axes[1, 1], color='purple')
        axes[1, 1].set_title('Experiencia con Google Colab', fontweight='bold')
        axes[1, 1].set_ylabel('Número de Estudiantes')
        axes[1, 1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.savefig('analisis_quiz_diagnostico.png', dpi=300, bbox_inches='tight')
    print("\n📊 Gráficos guardados en: analisis_quiz_diagnostico.png")
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    import sys

    print("""
    ╔═══════════════════════════════════════════════════════════════════╗
    ║  ANALIZADOR DE QUIZ DIAGNÓSTICO - CD2001B                         ║
    ║  Diagnóstico para Líneas de Acción                                ║
    ╚═══════════════════════════════════════════════════════════════════╝

    INSTRUCCIONES:

    1. Exporta las respuestas de Google Forms/Microsoft Forms a CSV

    2. Asegúrate de que las columnas tengan estos nombres:
       - nivel_estadistica (Pregunta 1)
       - nivel_python (Pregunta 7)
       - uso_colab (Pregunta 10)
       - frecuencia_ia (Pregunta 12)
       - uso_apis_agentes (Pregunta 15)
       - situacion_actual (Pregunta 20)

    3. Ejecuta este script:
       python analizar_quiz_diagnostico.py ruta/al/archivo.csv

    4. El script generará:
       - Estadísticas en consola
       - Gráficos en analisis_quiz_diagnostico.png

    ═══════════════════════════════════════════════════════════════════
    """)

    if len(sys.argv) > 1:
        archivo = sys.argv[1]
        print(f"📂 Cargando archivo: {archivo}\n")
        try:
            resultados = analizar_quiz(archivo)
            print("\n✅ Análisis completado exitosamente!")
        except Exception as e:
            print(f"\n❌ Error al analizar el archivo: {e}")
            print("\nVerifica que:")
            print("  • El archivo existe")
            print("  • Está en formato CSV")
            print("  • Tiene las columnas correctas")
    else:
        print("❌ Error: No se proporcionó archivo CSV")
        print("\nUso: python analizar_quiz_diagnostico.py respuestas_quiz.csv")
