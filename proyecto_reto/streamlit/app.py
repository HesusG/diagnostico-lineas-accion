"""
Dashboard Interactivo - Fundación Teletón
Análisis de Satisfacción de Benefactores

Este dashboard presenta visualizaciones interactivas de la encuesta de satisfacción
a empresas benefactoras de Fundación Teletón.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import sys
import os

# Importar módulo de utilidades
from teleton_utils import (
    COLORES_TELETON,
    PALETA_PRINCIPAL,
    calcular_todos_kpis,
    segmentar_nps,
    agregar_por_giro,
    agregar_por_estado,
    agregar_por_antiguedad,
    crear_gauge_kpi,
    crear_grafico_nps,
    crear_grafico_calidad_servicio,
    crear_grafico_por_giro,
    crear_grafico_geografico,
    crear_grafico_antiguedad,
    crear_heatmap_correlacion
)

# ===== CONFIGURACIÓN DE PÁGINA =====
st.set_page_config(
    page_title="Dashboard Teletón | Satisfacción de Benefactores",
    page_icon="💛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== ESTILOS PERSONALIZADOS =====
st.markdown(f"""
<style>
    /* Colores principales Teletón */
    :root {{
        --teleton-amarillo: {COLORES_TELETON['amarillo']};
        --teleton-morado: {COLORES_TELETON['morado_profundo']};
        --teleton-morado-medio: {COLORES_TELETON['morado_medio']};
    }}

    /* Header con colores Teletón */
    .main-header {{
        background: linear-gradient(135deg, {COLORES_TELETON['morado_profundo']} 0%, {COLORES_TELETON['morado_medio']} 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }}

    .main-header h1 {{
        color: {COLORES_TELETON['amarillo']};
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }}

    .main-header p {{
        color: white;
        font-size: 1.2rem;
    }}

    /* Tarjetas de KPI */
    .kpi-card {{
        background-color: white;
        border-left: 5px solid {COLORES_TELETON['amarillo']};
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }}

    .kpi-valor {{
        font-size: 2.5rem;
        font-weight: bold;
        color: {COLORES_TELETON['morado_profundo']};
    }}

    .kpi-label {{
        font-size: 0.9rem;
        color: {COLORES_TELETON['gris_medio']};
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    /* Secciones */
    .section-header {{
        color: {COLORES_TELETON['morado_profundo']};
        border-bottom: 3px solid {COLORES_TELETON['amarillo']};
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }}

    /* Filtros */
    .stSelectbox, .stMultiSelect {{
        margin-bottom: 1rem;
    }}
</style>
""", unsafe_allow_html=True)


# ===== FUNCIONES AUXILIARES =====

@st.cache_data
def cargar_datos():
    """Carga el dataset limpio desde el archivo CSV"""
    try:
        df = pd.read_csv('../datos/teleton_limpio.csv')
        return df
    except FileNotFoundError:
        st.error("❌ Error: No se encontró el archivo teleton_limpio.csv")
        st.info("💡 Por favor, ejecuta primero el Notebook 1: Análisis Exploratorio")
        st.stop()


def formatear_numero(valor, decimales=1, sufijo=""):
    """Formatea números para mostrar en KPIs"""
    return f"{valor:.{decimales}f}{sufijo}"


def crear_kpi_card(titulo, valor, sufijo="", decimales=1):
    """Crea una tarjeta de KPI con estilo personalizado"""
    valor_formateado = formatear_numero(valor, decimales, sufijo)
    return f"""
    <div class="kpi-card">
        <div class="kpi-label">{titulo}</div>
        <div class="kpi-valor">{valor_formateado}</div>
    </div>
    """


# ===== CARGAR DATOS =====
df = cargar_datos()


# ===== SIDEBAR (FILTROS) =====
st.sidebar.image("https://via.placeholder.com/300x100/4B1F76/F7C600?text=Teleton",
                 use_column_width=True)

st.sidebar.markdown("## 🔍 Filtros")

# Filtro por Estado
estados_disponibles = ['Todos'] + sorted(df['estado'].dropna().unique().tolist())
estado_seleccionado = st.sidebar.selectbox(
    "Estado",
    options=estados_disponibles,
    index=0
)

# Filtro por Giro
giros_disponibles = ['Todos'] + sorted(df['giro'].dropna().unique().tolist())
giro_seleccionado = st.sidebar.selectbox(
    "Giro Empresarial",
    options=giros_disponibles,
    index=0
)

# Filtro por Segmento de Antigüedad
segmentos_disponibles = ['Todos'] + df['segmento_antiguedad'].dropna().unique().tolist()
segmento_seleccionado = st.sidebar.selectbox(
    "Segmento de Antigüedad",
    options=segmentos_disponibles,
    index=0
)

# Aplicar filtros
df_filtrado = df.copy()

if estado_seleccionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['estado'] == estado_seleccionado]

if giro_seleccionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['giro'] == giro_seleccionado]

if segmento_seleccionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['segmento_antiguedad'] == segmento_seleccionado]

# Mostrar contador de registros filtrados
st.sidebar.markdown("---")
st.sidebar.metric(
    label="Registros mostrados",
    value=f"{len(df_filtrado)} / {len(df)}",
    delta=f"{len(df_filtrado) - len(df)} desde total"
)

# Información adicional
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Acerca del Dashboard")
st.sidebar.info(
    "Este dashboard presenta el análisis de satisfacción de "
    f"{len(df)} empresas benefactoras de Fundación Teletón.\n\n"
    f"**Última actualización:** {datetime.now().strftime('%d/%m/%Y')}"
)


# ===== HEADER PRINCIPAL =====
st.markdown("""
<div class="main-header">
    <h1>💛 Dashboard de Satisfacción - Fundación Teletón</h1>
    <p>Análisis de Encuesta a Empresas Benefactoras</p>
</div>
""", unsafe_allow_html=True)


# ===== SECCIÓN 1: KPIs PRINCIPALES =====
st.markdown('<h2 class="section-header">📈 Indicadores Clave de Desempeño (KPIs)</h2>',
            unsafe_allow_html=True)

# Calcular KPIs
kpis = calcular_todos_kpis(df_filtrado)

# Mostrar KPIs en 3 columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(crear_kpi_card(
        "Satisfacción General",
        kpis['satisfaccion_general'],
        " / 10",
        decimales=2
    ), unsafe_allow_html=True)

    st.markdown(crear_kpi_card(
        "Calidad Percibida",
        kpis['calidad_percibida'],
        " / 10",
        decimales=2
    ), unsafe_allow_html=True)

with col2:
    st.markdown(crear_kpi_card(
        "Net Promoter Score",
        kpis['nps'],
        "%",
        decimales=1
    ), unsafe_allow_html=True)

    st.markdown(crear_kpi_card(
        "Transparencia",
        kpis['transparencia'],
        " / 10",
        decimales=2
    ), unsafe_allow_html=True)

with col3:
    st.markdown(crear_kpi_card(
        "Índice Calidad de Servicio",
        kpis['indice_calidad_servicio'],
        " / 5",
        decimales=2
    ), unsafe_allow_html=True)

    st.markdown(crear_kpi_card(
        "Antigüedad Promedio",
        kpis['antiguedad_promedio'],
        " años",
        decimales=1
    ), unsafe_allow_html=True)


# ===== SECCIÓN 2: DISTRIBUCIÓN NPS =====
st.markdown('<h2 class="section-header">🎯 Net Promoter Score (NPS)</h2>',
            unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    fig_nps = crear_grafico_nps(df_filtrado)
    st.pyplot(fig_nps)
    plt.close()

with col2:
    st.markdown("### 📊 Interpretación del NPS")

    nps_score = kpis['nps']

    if nps_score > 50:
        categoria_nps = "🌟 Excelente"
        color_nps = COLORES_TELETON['verde']
        mensaje = "Los benefactores son altamente leales y están muy satisfechos."
    elif nps_score > 0:
        categoria_nps = "👍 Bueno"
        color_nps = COLORES_TELETON['amarillo']
        mensaje = "Hay espacio para mejorar la experiencia de los benefactores."
    else:
        categoria_nps = "⚠️ Mejorable"
        color_nps = COLORES_TELETON['rojo']
        mensaje = "Se requiere atención urgente para mejorar la satisfacción."

    st.markdown(f"""
    <div style="background-color: {color_nps}; padding: 1rem; border-radius: 8px; color: white;">
        <h3 style="color: white; margin: 0;">{categoria_nps}</h3>
        <p style="margin: 0.5rem 0 0 0;">{mensaje}</p>
    </div>
    """, unsafe_allow_html=True)

    # Mostrar segmentación
    segmentos = segmentar_nps(df_filtrado)
    st.dataframe(
        segmentos.style.format({'Porcentaje': '{:.1f}%'}),
        use_container_width=True,
        hide_index=True
    )


# ===== SECCIÓN 3: CALIDAD DE SERVICIO =====
st.markdown('<h2 class="section-header">⭐ Evaluación de Calidad de Servicio</h2>',
            unsafe_allow_html=True)

st.markdown("""
Las 13 dimensiones evaluadas miden la calidad del servicio en una escala de 1 a 5.
Los aspectos con menor puntuación representan oportunidades de mejora.
""")

fig_calidad = crear_grafico_calidad_servicio(df_filtrado)
st.pyplot(fig_calidad)
plt.close()


# ===== SECCIÓN 4: PERFIL DE BENEFACTORES =====
st.markdown('<h2 class="section-header">🏢 Perfil de Benefactores</h2>',
            unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Por Giro", "🗺️ Por Estado", "📅 Por Antigüedad"])

with tab1:
    col1, col2 = st.columns([3, 1])

    with col1:
        fig_giro = crear_grafico_por_giro(df_filtrado, metrica='satisfaccion_general', top_n=10)
        st.pyplot(fig_giro)
        plt.close()

    with col2:
        st.markdown("### Top 5 Giros")
        agg_giro = agregar_por_giro(df_filtrado).head(5)
        st.dataframe(
            agg_giro[['giro', 'cantidad', 'satisfaccion_general']].style.format({
                'satisfaccion_general': '{:.2f}'
            }),
            use_container_width=True,
            hide_index=True
        )

with tab2:
    col1, col2 = st.columns([3, 1])

    with col1:
        fig_geo = crear_grafico_geografico(df_filtrado, top_n=10)
        st.pyplot(fig_geo)
        plt.close()

    with col2:
        st.markdown("### Top 5 Estados")
        agg_estado = agregar_por_estado(df_filtrado).head(5)
        st.dataframe(
            agg_estado[['estado', 'cantidad']],
            use_container_width=True,
            hide_index=True
        )

with tab3:
    fig_antiguedad = crear_grafico_antiguedad(df_filtrado)
    st.pyplot(fig_antiguedad)
    plt.close()

    st.markdown("### Estadísticas por Segmento")
    agg_antiguedad = agregar_por_antiguedad(df_filtrado)
    st.dataframe(
        agg_antiguedad.style.format({
            'satisfaccion_general': '{:.2f}',
            'nps': '{:.2f}',
            'indice_calidad_servicio': '{:.2f}',
            'transparencia': '{:.2f}'
        }),
        use_container_width=True,
        hide_index=True
    )


# ===== SECCIÓN 5: CORRELACIONES =====
st.markdown('<h2 class="section-header">🔗 Análisis de Correlaciones</h2>',
            unsafe_allow_html=True)

st.markdown("""
Este análisis muestra las relaciones entre las diferentes métricas de satisfacción y calidad.
Valores cercanos a 1 indican una correlación positiva fuerte.
""")

fig_corr = crear_heatmap_correlacion(df_filtrado)
st.pyplot(fig_corr)
plt.close()


# ===== SECCIÓN 6: DATOS DETALLADOS =====
st.markdown('<h2 class="section-header">📋 Explorador de Datos</h2>',
            unsafe_allow_html=True)

if st.checkbox("Mostrar datos detallados"):
    # Seleccionar columnas a mostrar
    columnas_display = [
        'giro', 'estado', 'anos_benefactor', 'segmento_antiguedad',
        'satisfaccion_general', 'nps', 'nps_categoria',
        'calidad_percibida', 'transparencia', 'indice_calidad_servicio'
    ]

    st.dataframe(
        df_filtrado[columnas_display].style.format({
            'anos_benefactor': '{:.0f}',
            'satisfaccion_general': '{:.2f}',
            'nps': '{:.1f}',
            'calidad_percibida': '{:.2f}',
            'transparencia': '{:.2f}',
            'indice_calidad_servicio': '{:.2f}'
        }),
        use_container_width=True,
        height=400
    )

    # Botón de descarga
    csv = df_filtrado.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 Descargar datos filtrados (CSV)",
        data=csv,
        file_name=f"teleton_filtrado_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )


# ===== FOOTER =====
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: {COLORES_TELETON['gris_medio']}; padding: 2rem;">
    <p><strong>Dashboard de Fundación Teletón</strong> | Desarrollado con Streamlit</p>
    <p>Análisis de {len(df)} encuestas de satisfacción a empresas benefactoras</p>
    <p style="font-size: 0.8rem;">© {datetime.now().year} - Proyecto Reto CD2001B</p>
</div>
""", unsafe_allow_html=True)
