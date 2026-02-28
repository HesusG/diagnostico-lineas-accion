"""
Generador de ejemplos MALOS de visualización
Basado en "Storytelling with Data" de Cole Nussbaumer Knaflic

Estos ejemplos ilustran anti-patterns comunes:
- Clutter excesivo (Cap. 3)
- Visual incorrecto para el dato (Cap. 2)
- Falta de enfoque en la atención (Cap. 4)
- Títulos descriptivos vs. insight (Cap. 5)
"""

import matplotlib.pyplot as plt
import numpy as np

# Configuración para guardar SVG
plt.rcParams['svg.fonttype'] = 'none'

# =============================================================================
# EJEMPLO 1: Gráfico 3D con clutter excesivo
# Anti-pattern: 3D distorsiona percepción + demasiados elementos decorativos
# =============================================================================

def bad_example_3d_clutter():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    categorias = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
    valores = [8.5, 7.8, 9.1, 7.2, 8.0]
    colores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']

    xpos = np.arange(len(categorias))
    ypos = np.zeros(len(categorias))
    zpos = np.zeros(len(categorias))

    dx = dy = 0.8
    dz = valores

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colores, alpha=0.8,
             edgecolor='black', linewidth=2)

    # Agregar clutter: grid excesivo, título largo, etiquetas redundantes
    ax.set_xlabel('CATEGORÍAS DE REGIÓN GEOGRÁFICA', fontsize=10, fontweight='bold')
    ax.set_ylabel('', fontsize=10)
    ax.set_zlabel('PUNTUACIÓN DE SATISFACCIÓN (ESCALA 1-10)', fontsize=10, fontweight='bold')
    ax.set_xticks(xpos + 0.4)
    ax.set_xticklabels(categorias, fontsize=9)

    # Título excesivamente largo y descriptivo (no insight)
    plt.title('GRÁFICO DE BARRAS 3D MOSTRANDO LA SATISFACCIÓN\n'
              'POR REGIÓN GEOGRÁFICA EN ESCALA DEL 1 AL 10\n'
              '(Datos del Q4 2024 - Fundación Teletón México)',
              fontsize=12, fontweight='bold', pad=20)

    # Agregar leyenda innecesaria
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=c, label=cat) for c, cat in zip(colores, categorias)]
    ax.legend(handles=legend_elements, loc='upper left', title='Regiones:')

    plt.tight_layout()
    plt.savefig('/mnt/c/Users/HG_Co/OneDrive/Documents/Github/diagnostico-lineas-accion/semana3_reduced_localized/bad_examples_svg/01_bad_3d_clutter.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ Generado: 01_bad_3d_clutter.svg")


# =============================================================================
# EJEMPLO 2: Pie chart con demasiadas categorías
# Anti-pattern: Más de 5 rebanadas = imposible comparar
# =============================================================================

def bad_example_pie_many_categories():
    fig, ax = plt.subplots(figsize=(10, 8))

    categorias = ['Alimentación', 'Salud', 'Educación', 'Vivienda', 'Empleo',
                  'Legal', 'Psicológico', 'Deportes', 'Cultura', 'Transporte', 'Otros']
    valores = [15, 12, 11, 10, 9, 8, 7, 6, 5, 4, 13]
    colores = plt.cm.Set3(np.linspace(0, 1, len(categorias)))

    # Pie con efecto "explode" innecesario
    explode = [0.05] * len(categorias)

    wedges, texts, autotexts = ax.pie(valores, labels=categorias, autopct='%1.1f%%',
                                       colors=colores, explode=explode,
                                       shadow=True,  # Sombra = clutter
                                       startangle=90)

    # Etiquetas pequeñas e ilegibles
    for text in texts:
        text.set_fontsize(8)
    for autotext in autotexts:
        autotext.set_fontsize(7)

    # Título descriptivo (no insight)
    plt.title('DISTRIBUCIÓN PORCENTUAL DE PROGRAMAS\n'
              '(Gráfico Circular con 11 Categorías)',
              fontsize=14, fontweight='bold')

    # Agregar borde decorativo
    circle = plt.Circle((0, 0), 0.7, fc='white', ec='gray', linewidth=3)
    # No agregamos el círculo para que sea pie completo pero con sombra

    plt.tight_layout()
    plt.savefig('/mnt/c/Users/HG_Co/OneDrive/Documents/Github/diagnostico-lineas-accion/semana3_reduced_localized/bad_examples_svg/02_bad_pie_many_categories.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ Generado: 02_bad_pie_many_categories.svg")


# =============================================================================
# EJEMPLO 3: Eje Y truncado que exagera diferencias
# Anti-pattern: Manipulación visual que engaña
# =============================================================================

def bad_example_truncated_axis():
    fig, ax = plt.subplots(figsize=(10, 6))

    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
    satisfaccion = [8.0, 8.1, 8.2, 8.3, 8.4, 8.5]

    ax.plot(meses, satisfaccion, marker='o', linewidth=3, markersize=12,
            color='#E74C3C', markerfacecolor='#E74C3C')

    # EJE TRUNCADO: Inicia en 7.9 para exagerar el cambio
    ax.set_ylim(7.9, 8.6)

    # Grid pesado
    ax.grid(True, linestyle='-', linewidth=1.5, alpha=0.7)
    ax.set_axisbelow(True)

    # Fondo coloreado (clutter)
    ax.set_facecolor('#F5F5F5')

    # Título que NO advierte sobre el eje truncado
    plt.title('¡INCREÍBLE MEJORA EN SATISFACCIÓN!\n'
              '(Crecimiento Sostenido Mes a Mes)',
              fontsize=14, fontweight='bold', color='#E74C3C')

    ax.set_xlabel('Mes (2024)', fontsize=12)
    ax.set_ylabel('Satisfacción', fontsize=12)

    # Agregar anotación engañosa
    ax.annotate('¡+6.25% de mejora!', xy=(5, 8.5), fontsize=14,
                fontweight='bold', color='green',
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('/mnt/c/Users/HG_Co/OneDrive/Documents/Github/diagnostico-lineas-accion/semana3_reduced_localized/bad_examples_svg/03_bad_truncated_axis.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ Generado: 03_bad_truncated_axis.svg")


# =============================================================================
# EJEMPLO 4: Demasiados colores sin significado (rainbow vomit)
# Anti-pattern: Color como decoración, no como información
# =============================================================================

def bad_example_rainbow_colors():
    fig, ax = plt.subplots(figsize=(10, 6))

    areas = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro', 'Noreste']
    valores = [8.5, 7.8, 9.1, 7.2, 8.0, 8.3]

    # Colores arcoíris sin significado
    colores = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#8B00FF']

    bars = ax.bar(areas, valores, color=colores, edgecolor='black', linewidth=2)

    # Agregar patrones diferentes a cada barra (más clutter)
    patterns = ['/', '\\', 'x', 'o', '.', '*']
    for bar, pattern in zip(bars, patterns):
        bar.set_hatch(pattern)

    # Grid horizontal y vertical
    ax.grid(True, axis='both', linestyle='--', linewidth=1, alpha=0.5)

    # Título sin insight
    plt.title('DATOS DE SATISFACCIÓN POR ÁREA\n'
              '(Gráfico de Barras con Colores)',
              fontsize=14, fontweight='bold')

    ax.set_xlabel('Área Geográfica', fontsize=12)
    ax.set_ylabel('Puntuación (1-10)', fontsize=12)

    # Leyenda redundante (los colores no significan nada)
    ax.legend(bars, areas, title='Áreas:', loc='upper right')

    # Valores en las barras con formato inconsistente
    for bar, val in zip(bars, valores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{val}pts', ha='center', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig('/mnt/c/Users/HG_Co/OneDrive/Documents/Github/diagnostico-lineas-accion/semana3_reduced_localized/bad_examples_svg/04_bad_rainbow_colors.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ Generado: 04_bad_rainbow_colors.svg")


# =============================================================================
# EJEMPLO 5: Doble eje Y confuso
# Anti-pattern: Escalas independientes que sugieren correlación falsa
# =============================================================================

def bad_example_dual_axis():
    fig, ax1 = plt.subplots(figsize=(10, 6))

    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
    beneficiarios = [1500, 1800, 2100, 2400, 2200, 2600]
    satisfaccion = [7.5, 7.8, 8.0, 7.9, 8.2, 8.1]

    # Eje 1: Beneficiarios
    color1 = '#3498DB'
    ax1.set_xlabel('Mes (2024)', fontsize=12)
    ax1.set_ylabel('Beneficiarios', color=color1, fontsize=12)
    line1 = ax1.plot(meses, beneficiarios, color=color1, linewidth=3,
                     marker='s', markersize=10, label='Beneficiarios')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(1000, 3000)  # Escala manipulada

    # Eje 2: Satisfacción
    ax2 = ax1.twinx()
    color2 = '#E74C3C'
    ax2.set_ylabel('Satisfacción', color=color2, fontsize=12)
    line2 = ax2.plot(meses, satisfaccion, color=color2, linewidth=3,
                     marker='o', markersize=10, label='Satisfacción')
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(7.0, 8.5)  # Escala manipulada para que "coincidan"

    # Título que sugiere correlación
    plt.title('MÁS BENEFICIARIOS = MÁS SATISFACCIÓN\n'
              '(Relación Directa Observada)',
              fontsize=14, fontweight='bold')

    # Leyenda
    lines = line1 + line2
    labels = ['Beneficiarios', 'Satisfacción']
    ax1.legend(lines, labels, loc='upper left')

    # Anotación engañosa
    ax1.annotate('¡Correlación\nperfecta!', xy=(4, 2200), fontsize=12,
                 fontweight='bold', color='green',
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

    plt.tight_layout()
    plt.savefig('/mnt/c/Users/HG_Co/OneDrive/Documents/Github/diagnostico-lineas-accion/semana3_reduced_localized/bad_examples_svg/05_bad_dual_axis.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ Generado: 05_bad_dual_axis.svg")


# =============================================================================
# EJEMPLO 6: Visual incorrecto para el tipo de dato
# Anti-pattern: Usar líneas para datos categóricos (no hay orden temporal)
# =============================================================================

def bad_example_wrong_chart_type():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Categorías SIN orden (no son temporales)
    programas = ['Salud', 'Educación', 'Empleo', 'Legal', 'Vivienda']
    satisfaccion = [8.5, 7.8, 9.1, 7.2, 8.0]

    # ERROR: Usar gráfico de líneas para datos categóricos
    ax.plot(programas, satisfaccion, marker='o', linewidth=3, markersize=15,
            color='#9B59B6', linestyle='-')

    # Área bajo la curva (aún más confuso)
    ax.fill_between(programas, satisfaccion, alpha=0.3, color='#9B59B6')

    ax.set_ylim(0, 10)
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)

    # Título descriptivo
    plt.title('SATISFACCIÓN POR PROGRAMA\n'
              '(Gráfico de Líneas)',
              fontsize=14, fontweight='bold')

    ax.set_xlabel('Programa', fontsize=12)
    ax.set_ylabel('Satisfacción (1-10)', fontsize=12)

    plt.tight_layout()
    plt.savefig('/mnt/c/Users/HG_Co/OneDrive/Documents/Github/diagnostico-lineas-accion/semana3_reduced_localized/bad_examples_svg/06_bad_wrong_chart_type.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ Generado: 06_bad_wrong_chart_type.svg")


# =============================================================================
# EJEMPLO 7: Sin jerarquía visual - todo igual
# Anti-pattern: No hay enfoque, todo compite por atención
# =============================================================================

def bad_example_no_hierarchy():
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Todos los gráficos con mismo tamaño, color y prominencia
    datos = {
        'NPS': ['+40'],
        'Satisfacción': ['77%'],
        'Calidad': ['73%'],
        'Responsiveness': ['3.60']
    }

    colores = ['#3498DB', '#3498DB', '#3498DB', '#3498DB']  # Todos iguales

    for ax, (titulo, valor), color in zip(axes.flat, datos.items(), colores):
        ax.bar([titulo], [float(valor[0].replace('%', '').replace('+', ''))],
               color=color, edgecolor='black')
        ax.set_title(titulo, fontsize=12)
        ax.set_ylim(0, 100)

        # Grid idéntico en todos
        ax.grid(True, axis='y', linestyle='--', alpha=0.5)

        # Etiqueta idéntica
        ax.text(0, float(valor[0].replace('%', '').replace('+', '')) + 2,
                valor[0], ha='center', fontsize=14)

    # Título general sin insight
    fig.suptitle('MÉTRICAS DEL DASHBOARD\n(Cuatro Indicadores)',
                 fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.savefig('/mnt/c/Users/HG_Co/OneDrive/Documents/Github/diagnostico-lineas-accion/semana3_reduced_localized/bad_examples_svg/07_bad_no_hierarchy.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ Generado: 07_bad_no_hierarchy.svg")


# =============================================================================
# EJEMPLO 8: Título descriptivo vs. título con insight
# Anti-pattern: El título no comunica el mensaje clave
# =============================================================================

def bad_example_bad_title():
    fig, ax = plt.subplots(figsize=(10, 6))

    regiones = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
    nps = [51, 48, 44, 30, 31]

    # Ordenar de mayor a menor sería mejor, pero no lo hacemos
    bars = ax.bar(regiones, nps, color='#95A5A6', edgecolor='black')

    ax.axhline(y=40, color='gray', linestyle='--', linewidth=1, label='Promedio')

    ax.set_ylim(0, 60)
    ax.grid(True, axis='y', linestyle='--', alpha=0.3)

    # TÍTULO MALO: Descriptivo, no insight
    plt.title('NPS POR REGIÓN\n'
              '(Net Promoter Score - Datos 2024)',
              fontsize=14, fontweight='bold')

    # Subtítulo que debería ser el título
    ax.text(0.5, -0.15, 'Nota: Centro y Occidente requieren atención',
            transform=ax.transAxes, fontsize=10, style='italic',
            ha='center')

    ax.set_xlabel('Región', fontsize=12)
    ax.set_ylabel('NPS', fontsize=12)

    plt.tight_layout()
    plt.savefig('/mnt/c/Users/HG_Co/OneDrive/Documents/Github/diagnostico-lineas-accion/semana3_reduced_localized/bad_examples_svg/08_bad_title_no_insight.svg', format='svg', bbox_inches='tight')
    plt.close()
    print("✓ Generado: 08_bad_title_no_insight.svg")


# =============================================================================
# GENERAR TODOS LOS EJEMPLOS
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("Generando ejemplos MALOS de visualización...")
    print("Basado en 'Storytelling with Data' - Cole Nussbaumer Knaflic")
    print("="*60 + "\n")

    bad_example_3d_clutter()
    bad_example_pie_many_categories()
    bad_example_truncated_axis()
    bad_example_rainbow_colors()
    bad_example_dual_axis()
    bad_example_wrong_chart_type()
    bad_example_no_hierarchy()
    bad_example_bad_title()

    print("\n" + "="*60)
    print("¡Todos los ejemplos generados!")
    print("Ubicación: semana3_reduced_localized/bad_examples_svg/")
    print("="*60 + "\n")
