# Semana 4: Visualización de Datos con Looker Studio

## 📚 Módulo 2 - Parte 2

### 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:
- Crear dashboards interactivos en Looker Studio (Google Data Studio)
- Diseñar visualizaciones efectivas para comunicar insights
- Conectar fuentes de datos (Google Sheets, CSV, BigQuery)
- Aplicar principios de storytelling con datos
- Construir reportes dinámicos para stakeholders

---

## 📋 Contenidos

### 1. Fundamentos de Visualización de Datos (1 hora)
- **Principios de Diseño Visual**
  - Teoría del color aplicada a datos
  - Jerarquía visual
  - Accesibilidad (color blindness, WCAG)

- **Tipos de Gráficos y Cuándo Usarlos**
  - Comparación: Barras, columnas
  - Tendencias: Líneas, áreas
  - Distribución: Histogramas, boxplots
  - Relación: Scatter plots, heatmaps
  - Composición: Pie charts, treemaps

- **Anti-patterns en Visualización**
  - Gráficos de pie con muchas categorías
  - Ejes Y truncados
  - 3D innecesario
  - Uso excesivo de colores

### 2. Introducción a Looker Studio (2 horas)
- **Primeros Pasos**
  - Interfaz de Looker Studio
  - Conectar fuentes de datos
  - Tipos de conectores (Sheets, CSV, SQL)

- **Componentes Básicos**
  - Tablas y scorecards
  - Gráficos de barras y líneas
  - Mapas geográficos
  - Filtros y controles interactivos

- **Configuración de Visualizaciones**
  - Dimensiones vs métricas
  - Agregaciones (SUM, AVG, COUNT)
  - Campos calculados
  - Formato condicional

### 3. Dashboards Avanzados (2 horas)
- **Diseño de Dashboard**
  - Layout y composición
  - Uso de colores corporativos
  - Temas y estilos

- **Interactividad**
  - Filtros de fecha
  - Filtros por categoría
  - Drill-down
  - Parámetros dinámicos

- **Storytelling con Datos**
  - Estructura narrativa
  - Insights accionables
  - Audiencia objetivo

### 4. Integración con Python (1 hora)
- **Preparación de Datos**
  - Exportar datos desde Python
  - Conectar Google Sheets API
  - Automatización con scripts

---

## 📁 Estructura de la Semana

```
Semana4/
├── README.md
├── notebooks/
│   ├── 01_preparacion_datos_looker.ipynb
│   └── 02_visualizacion_python.ipynb
├── plantillas/
│   ├── plantilla_dashboard_ong.md
│   └── checklist_visualizacion.md
├── guias/
│   ├── guia_looker_studio_basico.md
│   ├── guia_storytelling_datos.md
│   └── guia_tipos_graficos.md
├── ejemplos/
│   ├── dashboard_ejemplo_ong.pdf
│   └── dashboard_ejemplo_kpis.pdf
└── datos/
    └── datos_procesados_para_looker.csv
```

---

## 🔧 Herramientas

### Looker Studio
- **Acceso:** https://lookerstudio.google.com
- **Requisitos:** Cuenta de Google
- **Conectores:** Google Sheets, CSV Upload, BigQuery

### Python para Preparación de Datos
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Para exportar a Google Sheets
from google.oauth2 import service_account
import gspread
```

---

## 📝 Actividades de la Semana

| Día | Actividad | Tipo | Tiempo |
|-----|-----------|------|--------|
| D1 | Fundamentos de visualización | Clase | 1h |
| D1 | Tipos de gráficos y anti-patterns | Clase | 1h |
| D1 | Introducción a Looker Studio | Clase | 1h |
| D2 | Creación de primer dashboard | Taller | 2h |
| D2 | **Actividad #2 (Parte 1): Preparar datos** | Tarea | 2h |
| D3 | Dashboards avanzados e interactividad | Clase | 2h |
| D3 | Storytelling con datos | Clase | 1h |
| D3 | **Actividad #2 (Parte 2): Dashboard Final** | Tarea | 4h |

---

## 📊 Entregables

### Actividad Individual #2 (Parte 1): Preparación de Datos para Dashboard
**Fecha límite:** Mitad Semana 4

**Contenido:**
1. Dataset limpio y procesado de la ONG
2. Variables calculadas (KPI, categorías)
3. Exportación a Google Sheets o CSV
4. Documentación de transformaciones realizadas

**Formato:** Jupyter Notebook (.ipynb) + CSV/Google Sheets

**Valor:** Parte de 6.25% (25% del Módulo 2)

---

### Actividad Individual #2 (Parte 2): Dashboard Interactivo en Looker Studio
**Fecha límite:** Fin Semana 4

**Contenido:**
1. Dashboard con mínimo 5 visualizaciones:
   - Scorecard con KPI principal
   - Gráfico de tendencia temporal
   - Comparación entre categorías
   - Distribución de satisfacción
   - Mapa o gráfico contextual
2. Filtros interactivos funcionales
3. Diseño alineado con identidad de la ONG
4. Insights y recomendaciones en texto

**Formato:**
- Link público a Looker Studio
- PDF exportado del dashboard
- Documento con interpretación (1-2 páginas)

**Valor:** Parte de 6.25% (25% del Módulo 2)

**Rúbrica de Evaluación:**
- **Diseño visual (20%):** Claridad, jerarquía, uso de color
- **Contenido técnico (30%):** Visualizaciones apropiadas, métricas correctas
- **Interactividad (20%):** Filtros funcionales, navegación intuitiva
- **Storytelling (20%):** Narrativa clara, insights accionables
- **Presentación (10%):** Formato profesional, sin errores

---

## 💡 Competencia: Gráficos Dinámicos (SCD0105.B)

**Nivel de dominio B:**
- Crear gráficos dinámicos interactivos
- Comunicar insights de manera efectiva
- Adaptar visualizaciones a la audiencia
- Aplicar principios de diseño de información

**Ejemplo aplicado:**
> "El dashboard muestra que la satisfacción en el Área Norte (8.5/10) supera significativamente al promedio general (7.8/10). El gráfico de tendencia revela que después de la intervención de julio 2023, la satisfacción incrementó 15%. El filtro por departamento permite a los gerentes identificar áreas de oportunidad específicas."

---

## 🎨 Principios de Diseño para Dashboards

### 1. Jerarquía Visual
- **Lo más importante arriba a la izquierda**
- KPIs principales como scorecards grandes
- Visualizaciones de soporte debajo

### 2. Regla del 5-7-9
- Máximo 5-7 visualizaciones por página
- Máximo 9 categorías en un gráfico de barras
- Si tienes más, agrupa o filtra

### 3. Uso de Color
```python
# Paleta recomendada para ONGs
colores_principales = {
    'primario': '#1E88E5',      # Azul confianza
    'secundario': '#43A047',    # Verde éxito
    'alerta': '#FB8C00',        # Naranja advertencia
    'critico': '#E53935'        # Rojo crítico
}
```

### 4. Accesibilidad
- Evitar rojo-verde para daltónicos
- Usar texturas/patrones además de color
- Etiquetas claras en todos los ejes

---

## 📚 Lectura Recomendada

**Obligatoria:**
- Knaflic, C. "Storytelling with Data: A Data Visualization Guide"
  - Capítulos 1-4

**Complementaria:**
- Tufte, E. "The Visual Display of Quantitative Information"
- Cairo, A. "The Truthful Art: Data, Charts, and Maps for Communication"

**Recursos en línea:**
- [Looker Studio Gallery](https://lookerstudio.google.com/gallery) - Inspiración
- [Data Viz Project](https://datavizproject.com/) - Catálogo de tipos de gráficos
- [ColorBrewer](https://colorbrewer2.org/) - Paletas accesibles

---

## 🎯 Conexión con el Reto Final

El dashboard que crees esta semana es PARTE INTEGRAL del reto porque:

1. **Visualización de KPI:** Presentarás los indicadores identificados en Semana 3
2. **Análisis Estadístico:** Integrarás resultados de pruebas de hipótesis (Semanas 1-2)
3. **Comunicación:** El dashboard es tu herramienta para presentar hallazgos
4. **Recomendaciones:** Los insights del dashboard justifican tus líneas de acción

---

## ❓ Preguntas Frecuentes

**P: ¿Puedo usar Tableau o Power BI en lugar de Looker Studio?**
R: La actividad requiere Looker Studio porque es gratuito y accesible. Puedes explorar otras herramientas por tu cuenta.

**P: ¿Cómo conecto mi Jupyter Notebook con Looker Studio?**
R: Exporta tus datos procesados a Google Sheets (usando API) o descárgalos como CSV y súbelos manualmente.

**P: ¿Cuántas páginas debe tener mi dashboard?**
R: 1-2 páginas es ideal. Una página principal con overview y opcionalmente una segunda con detalles.

**P: ¿El dashboard debe ser público?**
R: Para la entrega, configúralo como "Anyone with the link can view". Puedes hacerlo privado después.

---

## 🔗 Recursos Técnicos

### Conectar Google Sheets desde Python

```python
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Configurar credenciales (requiere cuenta de servicio)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
client = gspread.authorize(creds)

# Subir DataFrame a Google Sheets
def subir_a_sheets(df, sheet_name):
    sheet = client.create(sheet_name)
    worksheet = sheet.get_worksheet(0)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    return sheet.url

# Uso
df_limpio = pd.read_csv('datos_procesados.csv')
url = subir_a_sheets(df_limpio, 'Datos ONG - Dashboard')
print(f"Datos subidos: {url}")
```

### Exportar visualizaciones de Python

```python
import plotly.express as px

# Crear gráfico interactivo
fig = px.bar(df, x='area', y='satisfaccion',
             title='Satisfacción por Área')

# Exportar como HTML (embeddable)
fig.write_html('grafico_satisfaccion.html')
```

---

**Próxima semana:** Semana 5 - Integración y Presentación del Reto Final

