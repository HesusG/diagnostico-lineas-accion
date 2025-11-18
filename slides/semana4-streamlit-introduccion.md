---
theme: default
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Streamlit: Dashboards Interactivos con Python
  Curso CD2001B - Diagnóstico para Líneas de Acción
  Tecnológico de Monterrey Campus Puebla
drawings:
  persist: false
transition: slide-left
title: Introducción a Streamlit
mdc: true
download: true
exportFilename: semana4-streamlit-introduccion
css: unocss
---

<style src="./styles/tec-theme.css"></style>

# Streamlit: Dashboards con Python

## Alternativa Poderosa a Looker Studio

<div class="pt-12">
  <span class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    CD2001B - Semana 4 | Módulo 2
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <span class="text-sm opacity-50">Tec de Monterrey Campus Puebla</span>
</div>

---
layout: center
class: text-center
---

# ¿Qué es Streamlit?

<div class="grid grid-cols-2 gap-8 mt-12">
<div v-click>

### 🐍 Framework de Python

**Convierte scripts Python en apps web interactivas**

```python
# Esto es TODO el código para un dashboard:
import streamlit as st
import pandas as pd

df = pd.read_csv('teleton_benefactores.csv')

st.title('Dashboard Teletón')
st.metric("Satisfacción", df['satisfaccion'].mean())
st.bar_chart(df.groupby('giro')['satisfaccion'].mean())
```

**Resultado:** Dashboard web completo

</div>
<div v-click>

### 🆚 Looker Studio vs Streamlit

| Característica | Looker Studio | Streamlit |
|----------------|---------------|-----------|
| **Código** | ❌ No-code | ✅ Python |
| **Flexibilidad** | 🟡 Media | 🟢 Total |
| **Curva aprendizaje** | 🟢 Fácil | 🟡 Media |
| **ML/AI** | ❌ No | ✅ Sí |
| **Costo** | 🟢 Gratis | 🟢 Gratis |
| **Hosting** | ☁️ Google | ☁️ Streamlit Cloud |

</div>
</div>

<div v-click class="mt-12 text-xl font-bold text-gradient">
Streamlit = Looker Studio + Superpoderes de Python
</div>

---
layout: section
---

# Parte 1: Primer Dashboard en 10 Minutos

## De Cero a Deployed

---

# Instalación y Setup

<div class="grid grid-cols-2 gap-8">
<div>

## Paso 1: Instalar Streamlit

**En terminal o Jupyter:**

```bash
pip install streamlit
```

**Verificar instalación:**

```bash
streamlit --version
# Output: Streamlit version 1.30.0
```

## Paso 2: Crear Archivo Python

**Crear:** `dashboard_teleton.py`

```python
import streamlit as st

st.title("Mi Primer Dashboard")
st.write("Hola, Teletón!")
```

</div>
<div v-click>

## Paso 3: Ejecutar

**En terminal:**

```bash
streamlit run dashboard_teleton.py
```

**Se abrirá automáticamente en navegador:**
- URL: `http://localhost:8501`
- Hot-reload: Cambios en código → Actualiza automáticamente

## Paso 4: Ver Resultado

<div class="p-6 bg-white rounded shadow text-left">
  <h1 class="text-3xl font-bold">Mi Primer Dashboard</h1>
  <p class="mt-4">Hola, Teletón!</p>
</div>

<div v-click class="mt-6 p-4 bg-blue-500 bg-opacity-10 rounded text-sm">

**¡Listo!** Ya tienes una app web corriendo

</div>

</div>
</div>

---

# Componentes Básicos de Streamlit

<div class="grid grid-cols-3 gap-4 text-xs">

<div>

### Texto y Títulos

```python
st.title("Dashboard Teletón")
st.header("Sección de KPIs")
st.subheader("Satisfacción")
st.text("Texto simple")
st.markdown("**Negrita** *cursiva*")
st.caption("Nota pequeña")
```

**Resultado:**
<div class="p-4 bg-white rounded shadow text-left">
  <h1 class="text-2xl font-bold">Dashboard Teletón</h1>
  <h2 class="text-xl font-semibold mt-2">Sección de KPIs</h2>
  <h3 class="text-lg mt-1">Satisfacción</h3>
  <p class="mt-1">Texto simple</p>
  <p class="mt-1"><strong>Negrita</strong> <em>cursiva</em></p>
  <p class="text-sm opacity-60 mt-1">Nota pequeña</p>
</div>

</div>

<div v-click>

### Datos

```python
import pandas as pd

df = pd.read_csv('teleton.csv')

# Tabla
st.dataframe(df)

# Métrica destacada
st.metric(
    label="Satisfacción Promedio",
    value="8.2",
    delta="+0.3 vs mes anterior"
)

# JSON
st.json({"giro": "Salud", "sat": 8.9})
```

**Resultado:**
<div class="p-4 bg-white rounded shadow text-left">
  <div class="border p-2 mb-2 text-xs">
    <code>[Tabla interactiva con 274 filas]</code>
  </div>
  <div class="border-l-4 border-green-500 p-3 bg-green-50">
    <div class="text-sm opacity-60">Satisfacción Promedio</div>
    <div class="text-3xl font-bold">8.2</div>
    <div class="text-sm text-green-600">↑ +0.3 vs mes anterior</div>
  </div>
</div>

</div>

<div v-click>

### Gráficos

```python
# Gráfico simple
st.line_chart(df['satisfaccion'])

# Con Altair (más control)
import altair as alt
chart = alt.Chart(df).mark_bar().encode(
    x='giro',
    y='mean(satisfaccion)'
)
st.altair_chart(chart)

# Con Plotly (interactivo)
import plotly.express as px
fig = px.bar(df, x='giro', y='satisfaccion')
st.plotly_chart(fig)

# Con Matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(df['giro'], df['satisfaccion'])
st.pyplot(fig)
```

</div>

</div>

---

# Dashboard Teletón: Versión Mínima

<div class="grid grid-cols-2 gap-8">
<div>

## Código Completo (30 líneas)

```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(
    page_title="Dashboard Teletón",
    page_icon="❤️",
    layout="wide"
)

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv('Semana4/datos/teleton_benefactores.csv')

df = load_data()

# Título
st.title("❤️ Dashboard Fundación Teletón")
st.markdown("---")

# KPIs en columnas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Satisfacción Promedio",
              f"{df['satisfaccion'].mean():.1f}/10")

with col2:
    st.metric("Empresas Benefactoras",
              len(df))

with col3:
    meta = (df['satisfaccion'] >= 8).mean() * 100
    st.metric("% Meta Alcanzada",
              f"{meta:.0f}%")

with col4:
    st.metric("Años Promedio",
              f"{df['tiempo_colaboracion'].mean():.1f}")

st.markdown("---")

# Gráficos
col5, col6 = st.columns(2)

with col5:
    st.subheader("Satisfacción por Giro")
    fig1 = px.bar(
        df.groupby('giro')['satisfaccion'].mean().reset_index(),
        x='giro',
        y='satisfaccion',
        color='satisfaccion',
        color_continuous_scale='Tealgrn'
    )
    st.plotly_chart(fig1, use_container_width=True)

with col6:
    st.subheader("Distribución de Satisfacción")
    fig2 = px.histogram(df, x='satisfaccion', nbins=20)
    st.plotly_chart(fig2, use_container_width=True)

# Tabla filtrada
st.subheader("Datos Detallados")
giro_filter = st.multiselect(
    "Filtrar por giro:",
    options=df['giro'].unique(),
    default=df['giro'].unique()
)

df_filtered = df[df['giro'].isin(giro_filter)]
st.dataframe(df_filtered, use_container_width=True)
```

</div>
<div v-click>

## Vista del Dashboard

<img src="./assets/streamlit/dashboard-teleton-basic.png" class="w-full max-h-128 object-contain rounded shadow" />

**Funcionalidades:**
- ✅ 4 KPIs destacados
- ✅ 2 gráficos interactivos (zoom, hover)
- ✅ Tabla con filtro multiselect
- ✅ Layout responsive (2 columnas)
- ✅ Caching de datos (rápido)

**Tiempo de desarrollo:** ~15 minutos

</div>
</div>

---

# Componentes Interactivos (Widgets)

<div class="grid grid-cols-3 gap-6 text-xs">

<div>

### Selectores

```python
# Slider
edad = st.slider(
    "Edad",
    min_value=18,
    max_value=65,
    value=30
)

# Select box
giro = st.selectbox(
    "Giro:",
    options=['Salud', 'Tech', 'Retail']
)

# Multiselect
canales = st.multiselect(
    "Canales:",
    options=['Donación', 'Patrocinio'],
    default=['Donación']
)

# Radio buttons
periodo = st.radio(
    "Periodo:",
    options=['Mensual', 'Trimestral', 'Anual']
)
```

</div>

<div v-click>

### Inputs

```python
# Text input
nombre = st.text_input("Nombre empresa:")

# Number input
monto = st.number_input(
    "Monto:",
    min_value=0,
    max_value=1000000,
    step=1000
)

# Date input
fecha = st.date_input("Fecha de inicio:")

# File uploader
uploaded_file = st.file_uploader(
    "Sube CSV:",
    type=['csv']
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

</div>

<div v-click>

### Botones y Estados

```python
# Button
if st.button("Calcular"):
    resultado = df['satisfaccion'].mean()
    st.success(f"Promedio: {resultado}")

# Checkbox
if st.checkbox("Mostrar datos crudos"):
    st.write(df)

# Mensajes
st.success("✅ Datos cargados")
st.info("ℹ️ Información")
st.warning("⚠️ Advertencia")
st.error("❌ Error")

# Progress bar
import time
progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)
st.success("Completado!")
```

</div>

</div>

---

# Layout Avanzado: Sidebar y Tabs

<div class="grid grid-cols-2 gap-8">
<div>

## Sidebar (Panel Lateral)

```python
import streamlit as st

# Sidebar
with st.sidebar:
    st.image("logo_teleton.png", width=200)
    st.title("Filtros")

    # Filtros en sidebar
    giro = st.selectbox(
        "Giro:",
        options=df['giro'].unique()
    )

    canal = st.multiselect(
        "Canal:",
        options=df['canal_apoyo'].unique(),
        default=df['canal_apoyo'].unique()
    )

    satisfaccion_min = st.slider(
        "Satisfacción mínima:",
        1, 10, 5
    )

    st.markdown("---")
    st.caption("Dashboard v1.0")

# Main area (usa los filtros del sidebar)
df_filtered = df[
    (df['giro'] == giro) &
    (df['canal_apoyo'].isin(canal)) &
    (df['satisfaccion'] >= satisfaccion_min)
]

st.title("Dashboard Principal")
st.metric("Empresas filtradas", len(df_filtered))
```

</div>
<div v-click>

## Tabs (Pestañas)

```python
tab1, tab2, tab3 = st.tabs([
    "📊 Overview",
    "📈 Análisis",
    "📋 Datos"
])

with tab1:
    st.header("Vista General")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("KPI 1", "8.2")
    with col2:
        st.metric("KPI 2", "274")
    with col3:
        st.metric("KPI 3", "62%")

with tab2:
    st.header("Análisis Detallado")
    st.line_chart(df['satisfaccion'])

with tab3:
    st.header("Datos Crudos")
    st.dataframe(df)
```

**Resultado:** Dashboard con navegación por pestañas

</div>
</div>

---

# Caching: Optimización de Performance

<div class="grid grid-cols-2 gap-8">
<div>

## El Problema

**Sin caching:**
```python
import pandas as pd
import streamlit as st

# ❌ Se lee el CSV en CADA interacción
df = pd.read_csv('teleton_benefactores.csv')

# Usuario cambia filtro → recarga TODO
giro = st.selectbox("Giro:", df['giro'].unique())
```

**Consecuencia:**
- Lento con archivos grandes
- Re-procesa datos innecesariamente
- Mala experiencia de usuario

</div>
<div v-click>

## La Solución: @st.cache_data

```python
import pandas as pd
import streamlit as st

# ✅ Se cachea (guarda en memoria)
@st.cache_data
def load_data():
    df = pd.read_csv('teleton_benefactores.csv')
    # Transformaciones pesadas
    df['categoria'] = df['satisfaccion'].apply(categorizar)
    return df

# Solo se ejecuta UNA VEZ
df = load_data()

# Interacciones rápidas (usa cache)
giro = st.selectbox("Giro:", df['giro'].unique())
```

**Beneficio:**
- ⚡ 10-100x más rápido
- Datos se cargan solo al inicio
- Invalidación automática si archivo cambia

</div>
</div>

<div v-click class="mt-6 p-6 bg-purple-500 bg-opacity-10 rounded text-center">

**Regla:** Cachea todo lo que sea costoso: lectura de CSV, queries a DB, procesamiento de datos

</div>

---

# Caso Práctico: Dashboard Teletón Completo

<div class="grid grid-cols-2 gap-6 text-xs">
<div>

## Estructura del Archivo

```python
# dashboard_teleton_completo.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ============ CONFIGURACIÓN ============
st.set_page_config(
    page_title="Dashboard Teletón",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============ CARGAR DATOS ============
@st.cache_data
def load_data():
    df = pd.read_csv('Semana4/datos/teleton_benefactores.csv')
    # Categorías
    df['categoria_sat'] = df['satisfaccion'].apply(
        lambda x: "Muy Satisfecho" if x >= 9
                  else "Satisfecho" if x >= 7
                  else "Neutral" if x >= 5
                  else "Insatisfecho"
    )
    return df

df = load_data()

# ============ SIDEBAR ============
with st.sidebar:
    st.image("logo_teleton.png", width=150)
    st.title("Filtros de Dashboard")

    # Filtro de giro
    giros = ['Todos'] + list(df['giro'].unique())
    giro_seleccionado = st.selectbox("Giro:", giros)

    # Filtro de canal
    canales = st.multiselect(
        "Canal de Apoyo:",
        options=df['canal_apoyo'].unique(),
        default=df['canal_apoyo'].unique()
    )

    # Filtro de satisfacción
    sat_range = st.slider(
        "Rango de Satisfacción:",
        1, 10, (1, 10)
    )

    # Aplicar filtros
    df_filtered = df.copy()
    if giro_seleccionado != 'Todos':
        df_filtered = df_filtered[
            df_filtered['giro'] == giro_seleccionado
        ]
    df_filtered = df_filtered[
        (df_filtered['canal_apoyo'].isin(canales)) &
        (df_filtered['satisfaccion'].between(
            sat_range[0], sat_range[1]
        ))
    ]

    st.markdown("---")
    st.metric("Empresas Filtradas", len(df_filtered))
```

</div>
<div>

```python
# ============ MAIN DASHBOARD ============
st.title("❤️ Dashboard Fundación Teletón")
st.markdown("### Satisfacción de Empresas Benefactoras 2024")
st.markdown("---")

# KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_sat = df_filtered['satisfaccion'].mean()
    st.metric(
        "Satisfacción Promedio",
        f"{avg_sat:.1f}/10",
        delta=f"{avg_sat - df['satisfaccion'].mean():.1f}",
        help="Promedio de satisfacción filtrado"
    )

with col2:
    st.metric(
        "Empresas",
        len(df_filtered),
        help="Total de empresas en selección"
    )

with col3:
    meta = (df_filtered['satisfaccion'] >= 8).mean() * 100
    st.metric(
        "% Meta Alcanzada",
        f"{meta:.0f}%",
        help="Porcentaje con satisfacción ≥ 8"
    )

with col4:
    st.metric(
        "Años Promedio",
        f"{df_filtered['tiempo_colaboracion'].mean():.1f}",
        help="Promedio de años colaborando"
    )

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Análisis por Giro",
    "📈 Tendencias",
    "🗺️ Distribución",
    "📋 Datos"
])

with tab1:
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Satisfacción por Giro")
        giro_avg = df_filtered.groupby('giro')[
            'satisfaccion'
        ].mean().sort_values(ascending=True)

        fig1 = go.Figure(go.Bar(
            x=giro_avg.values,
            y=giro_avg.index,
            orientation='h',
            marker=dict(
                color=giro_avg.values,
                colorscale='Tealgrn',
                showscale=True
            )
        ))
        fig1.update_layout(
            xaxis_title="Satisfacción Promedio",
            yaxis_title="Giro"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col6:
        st.subheader("Empresas por Canal")
        canal_count = df_filtered['canal_apoyo'].value_counts()
        fig2 = px.pie(
            values=canal_count.values,
            names=canal_count.index,
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Tealgrn
        )
        st.plotly_chart(fig2, use_container_width=True)
```

</div>
</div>

---

# Dashboard Teletón: Tabs Restantes

<div class="grid grid-cols-2 gap-6 text-xs">
<div>

```python
# Continuación de tabs...

with tab2:
    st.subheader("Satisfacción por Años de Colaboración")

    # Scatter plot
    fig3 = px.scatter(
        df_filtered,
        x='tiempo_colaboracion',
        y='satisfaccion',
        color='giro',
        size='monto_aportado',
        hover_data=['empresa', 'canal_apoyo'],
        title="Relación Tiempo vs Satisfacción"
    )
    fig3.add_hline(
        y=8,
        line_dash="dash",
        line_color="red",
        annotation_text="Meta (8.0)"
    )
    st.plotly_chart(fig3, use_container_width=True)

    # Insights
    corr = df_filtered[[
        'tiempo_colaboracion', 'satisfaccion'
    ]].corr().iloc[0, 1]

    if corr > 0.3:
        st.success(
            f"✅ Correlación positiva ({corr:.2f}): "
            "Más tiempo colaborando → Mayor satisfacción"
        )
    elif corr < -0.3:
        st.warning(
            f"⚠️ Correlación negativa ({corr:.2f}): "
            "Revisar estrategia de retención"
        )
    else:
        st.info(
            f"ℹ️ Correlación débil ({corr:.2f}): "
            "Tiempo no es factor determinante"
        )
```

</div>
<div>

```python
with tab3:
    st.subheader("Distribución de Satisfacción")

    col7, col8 = st.columns(2)

    with col7:
        # Histograma
        fig4 = px.histogram(
            df_filtered,
            x='satisfaccion',
            nbins=20,
            title="Distribución de Satisfacción",
            color_discrete_sequence=['#00A3E0']
        )
        st.plotly_chart(fig4, use_container_width=True)

    with col8:
        # Box plot por giro
        fig5 = px.box(
            df_filtered,
            x='giro',
            y='satisfaccion',
            color='giro',
            title="Variabilidad por Giro"
        )
        st.plotly_chart(fig5, use_container_width=True)

with tab4:
    st.subheader("Datos Detallados")

    # Tabla con formato condicional
    def color_satisfaccion(val):
        if val >= 9:
            color = 'background-color: #d4edda'
        elif val >= 7:
            color = 'background-color: #fff3cd'
        else:
            color = 'background-color: #f8d7da'
        return color

    st.dataframe(
        df_filtered.style.applymap(
            color_satisfaccion,
            subset=['satisfaccion']
        ),
        use_container_width=True
    )

    # Botón de descarga
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar datos filtrados (CSV)",
        data=csv,
        file_name='teleton_filtrado.csv',
        mime='text/csv'
    )
```

</div>
</div>

---

# Deployment: Publicar tu Dashboard

<div class="grid grid-cols-2 gap-8">
<div>

## Opción 1: Streamlit Cloud (Gratis)

**Requisitos:**
- Cuenta GitHub
- Repositorio público con tu código

**Pasos:**

1. **Subir código a GitHub:**
   ```bash
   git add dashboard_teleton.py
   git add requirements.txt
   git commit -m "Add Streamlit dashboard"
   git push
   ```

2. **requirements.txt:**
   ```txt
   streamlit>=1.30.0
   pandas>=2.0.0
   plotly>=5.18.0
   ```

3. **Ir a:** [share.streamlit.io](https://share.streamlit.io)

4. **Deploy:**
   - Conectar GitHub
   - Seleccionar repo y archivo .py
   - Deploy (tarda ~2 minutos)

5. **URL pública:**
   ```
   https://[tu-usuario]-teleton-dashboard.streamlit.app
   ```

</div>
<div v-click>

## Opción 2: Hosting Propio

### Heroku (Básico gratis)

```bash
# Procfile
web: streamlit run dashboard_teleton.py --server.port=$PORT
```

### Docker

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "dashboard_teleton.py"]
```

### Local con Túnel (desarrollo)

```bash
# Opción 1: Streamlit sharing
streamlit run dashboard_teleton.py --server.enableCORS=false

# Opción 2: ngrok (túnel público)
ngrok http 8501
# URL: https://abc123.ngrok.io
```

</div>
</div>

---

# Comparación Final: Looker Studio vs Streamlit

<div class="text-xs">

| Aspecto | Looker Studio | Streamlit | Recomendación |
|---------|---------------|-----------|---------------|
| **Facilidad de uso** | 🟢 Drag & drop, sin código | 🟡 Requiere Python básico | Looker para no programadores |
| **Tiempo de creación** | 🟢 1-2 horas para básico | 🟡 2-4 horas para básico | Looker más rápido inicialmente |
| **Flexibilidad** | 🟡 Limitado a componentes pre-built | 🟢 Control total con Python | Streamlit para customización |
| **Visualizaciones** | 🟡 15-20 tipos estándar | 🟢 Ilimitado (Plotly, Matplotlib, etc.) | Streamlit más opciones |
| **Machine Learning** | ❌ No soporta | ✅ Integración completa | Streamlit para ML/AI |
| **Interactividad** | 🟢 Filtros y drill-down nativos | 🟢 Widgets ilimitados | Empate |
| **Datos en tiempo real** | 🟡 Polling cada N minutos | 🟢 WebSocket, real-time | Streamlit para tiempo real |
| **Colaboración** | 🟢 Compartir link, permisos Google | 🟡 Requiere deployment | Looker más simple |
| **Costo** | 🟢 Gratis (límites Google) | 🟢 Gratis (Cloud o self-host) | Empate |
| **Curva de aprendizaje** | 🟢 1-2 semanas | 🟡 2-4 semanas (si sabes Python) | Looker más accesible |
| **Mantenimiento** | 🟢 Cero (Google lo mantiene) | 🟡 Debes actualizar código | Looker menos mantenimiento |
| **Escalabilidad** | 🟡 Límite 100K filas en Sheets | 🟢 Escala con infraestructura | Streamlit para big data |

</div>

<div v-click class="mt-6 grid grid-cols-2 gap-6">

<div class="p-4 bg-green-500 bg-opacity-10 rounded">

**Usa Looker Studio si:**
- Dashboard para stakeholders no técnicos
- Necesitas rapidez (1-2 horas)
- Datos < 100K filas
- No requieres ML

</div>

<div class="p-4 bg-blue-500 bg-opacity-10 rounded">

**Usa Streamlit si:**
- Audiencia técnica o tú controlas hosting
- Necesitas ML/AI integrado
- Visualizaciones muy customizadas
- Datos > 100K filas
- Quieres aprender Python

</div>

</div>

---

# Casos de Uso Avanzados: Streamlit

<div class="grid grid-cols-3 gap-6 text-xs">

<div>

### 1. Predicción con ML

```python
import streamlit as st
from sklearn.ensemble import RandomForestRegressor

st.title("Predictor de Satisfacción")

# Inputs
giro = st.selectbox("Giro:", giros)
canal = st.selectbox("Canal:", canales)
años = st.number_input("Años:", 1, 20, 5)

# Modelo entrenado
@st.cache_resource
def load_model():
    # Entrenar modelo
    X = df[['giro_encoded', 'canal_encoded',
            'tiempo_colaboracion']]
    y = df['satisfaccion']
    model = RandomForestRegressor()
    model.fit(X, y)
    return model

model = load_model()

if st.button("Predecir"):
    # Encodear inputs
    X_new = encode([giro, canal, años])
    pred = model.predict(X_new)[0]

    st.success(
        f"Satisfacción predicha: {pred:.1f}/10"
    )

    # Feature importance
    st.bar_chart(model.feature_importances_)
```

</div>

<div v-click>

### 2. Upload y Análisis Dinámico

```python
st.title("Analizador de Encuestas")

# Upload
uploaded = st.file_uploader(
    "Sube tu CSV:",
    type=['csv']
)

if uploaded:
    df = pd.read_csv(uploaded)

    # Auto-detect columnas
    num_cols = df.select_dtypes(
        include='number'
    ).columns.tolist()

    cat_cols = df.select_dtypes(
        include='object'
    ).columns.tolist()

    # Selección dinámica
    x = st.selectbox("Eje X:", cat_cols)
    y = st.selectbox("Eje Y:", num_cols)

    # Gráfico automático
    fig = px.bar(
        df.groupby(x)[y].mean().reset_index(),
        x=x, y=y
    )
    st.plotly_chart(fig)

    # Estadísticas
    st.write(df[y].describe())
```

**Uso:** Cliente sube su propio CSV y obtiene insights instantáneos

</div>

<div v-click>

### 3. Dashboard con Autenticación

```python
import streamlit as st
import streamlit_authenticator as stauth

# Configurar usuarios
names = ['Admin', 'Usuario']
usernames = ['admin', 'user']
passwords = ['admin123', 'user123']

# Hashear passwords
hashed = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    names, usernames, hashed,
    'cookie_name', 'signature_key',
    cookie_expiry_days=30
)

# Login
name, auth_status, username = \
    authenticator.login('Login', 'main')

if auth_status:
    st.write(f'Bienvenido *{name}*')

    # Dashboard protegido
    if username == 'admin':
        st.title("Panel de Administrador")
        # Vista completa
    else:
        st.title("Panel de Usuario")
        # Vista limitada

    authenticator.logout('Logout', 'sidebar')

elif auth_status == False:
    st.error('Usuario/contraseña incorrectos')
```

</div>

</div>

---

# Recursos y Aprendizaje Continuo

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Documentación Oficial

**Streamlit Docs:**
- 📘 [docs.streamlit.io](https://docs.streamlit.io)
- API Reference completa
- Tutoriales paso a paso
- Ejemplos de código

**Galería de Demos:**
- 🎨 [streamlit.io/gallery](https://streamlit.io/gallery)
- 100+ apps de ejemplo
- Código fuente disponible
- Filtrar por caso de uso

## Cursos Gratuitos

**Streamlit Official:**
- 30 Days of Streamlit (challenge diario)
- [30days.streamlit.app](https://30days.streamlit.app)

**YouTube:**
- "Streamlit Tutorial for Beginners" (Data Professor)
- "Build 12 Data Apps" (Python Engineer)

</div>
<div v-click>

## Librerías Complementarias

**Visualización:**
```python
pip install plotly       # Gráficos interactivos
pip install altair       # Declarativo
pip install pydeck       # Mapas 3D
```

**Componentes Extra:**
```python
pip install streamlit-aggrid  # Tablas avanzadas
pip install streamlit-option-menu  # Menús
pip install streamlit-authenticator  # Login
pip install streamlit-lottie  # Animaciones
```

**Machine Learning:**
```python
pip install scikit-learn
pip install tensorflow
pip install shap  # Explicabilidad de modelos
```

## Comunidad

- 💬 [Streamlit Community Forum](https://discuss.streamlit.io)
- 🐦 Twitter: @streamlit
- 📺 Streamlit YouTube Channel

</div>
</div>

---

# Actividad Práctica: Mini Dashboard Teletón

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Objetivo

**Crear un dashboard Streamlit básico con datos de Teletón en 30 minutos**

### Requisitos Mínimos

1. **3 KPIs** (métricas destacadas)
2. **2 gráficos:**
   - Barras: Satisfacción por giro
   - Scatter: Tiempo vs Satisfacción
3. **1 filtro** interactivo (selectbox o multiselect)
4. **Tabla** con datos filtrados
5. **Botón de descarga** CSV

### Setup

```bash
# Instalar
pip install streamlit pandas plotly

# Crear archivo
touch dashboard_teleton_mini.py

# Ejecutar
streamlit run dashboard_teleton_mini.py
```

</div>
<div v-click>

## Plantilla Inicial

```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración
st.set_page_config(page_title="Teletón Mini", layout="wide")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv('teleton_benefactores.csv')

df = load_data()

# COMPLETAR AQUÍ:
# 1. Título
st.title("...")

# 2. KPIs en columnas
col1, col2, col3 = st.columns(3)
# ...

# 3. Filtro
giro = st.selectbox("Giro:", ...)

# 4. Gráfico de barras
fig = px.bar(...)
st.plotly_chart(fig)

# 5. Tabla y descarga
st.dataframe(df_filtered)
csv = df_filtered.to_csv(index=False).encode('utf-8')
st.download_button("Descargar", csv, "data.csv")
```

**Tiempo:** 20-30 minutos

</div>
</div>

---
layout: center
class: text-center
---

# Resumen: Streamlit

<div class="grid grid-cols-3 gap-6 mt-12 text-sm">

<div v-click>

### 🚀 Ventajas
- Control total (Python)
- ML/AI integrado
- Componentes ilimitados
- Open source
- Deploy gratis

</div>

<div v-click>

### ⚠️ Consideraciones
- Requiere Python
- Curva de aprendizaje media
- Mantenimiento de código
- Deployment manual

</div>

<div v-click>

### 🎯 Cuándo Usar
- Dashboards técnicos
- Prototipos de ML
- Apps con lógica compleja
- Análisis exploratorio
- Control total requerido

</div>

</div>

<div v-click class="mt-16 text-2xl font-bold text-gradient">
Streamlit = Python + Dashboard Web en minutos
</div>

---
layout: end
class: text-center
---

# ¡Gracias!

## Próxima Semana: Reto Final - Integración Completa

### Actividad: Experimenta con Streamlit (opcional, no evaluado)

<div class="mt-8 opacity-75">
CD2001B - Semana 4<br>
Tec de Monterrey Campus Puebla
</div>
