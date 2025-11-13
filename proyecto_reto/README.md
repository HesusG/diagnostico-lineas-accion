# 💛 Proyecto Dashboard - Fundación Teletón

Análisis de Satisfacción de Empresas Benefactoras

---

## 📋 Descripción del Proyecto

Este proyecto desarrolla un análisis completo de la encuesta de satisfacción aplicada a empresas benefactoras de Fundación Teletón, implementando **dos rutas de visualización**:

1. **Ruta Programática**: Python → Streamlit (dashboard interactivo con código)
2. **Ruta Visual**: Python → BigQuery → Looker Studio (dashboard sin código)

### Subcompetencias Demostradas

- **SCD0104**: Análisis descriptivo con medidas de tendencia central y dispersión
- **SCD0105**: Creación de gráficos dinámicos interactivos

---

## 📊 Dataset

- **Archivo**: `teleton.xlsx`
- **Descripción**: Encuesta de satisfacción a empresas benefactoras
- **Registros**: 274 empresas
- **Variables**: 21 columnas
  - 13 dimensiones de calidad de servicio (escala Likert 1-5)
  - 4 variables de satisfacción (escala 1-10)
  - 3 variables categóricas (giro, puesto, estado)
  - 1 variable numérica (años como benefactor)
  - 1 variable temporal (fecha)

---

## 🗂️ Estructura del Proyecto

```
proyecto_reto/
│
├── datos/                          # Datos del proyecto
│   ├── teleton.xlsx                # Dataset original
│   └── teleton_limpio.csv          # Dataset procesado (generado por Notebook 1)
│
├── slides/                         # Presentación del proyecto
│   └── proyecto_dashboard_teleton.md  # Slides en Slidev
│
├── jupyter/                        # Notebooks de análisis
│   ├── 01_analisis_exploratorio.ipynb    # EDA completo
│   ├── 02_preparacion_streamlit.ipynb    # Prep. para Streamlit
│   └── 03_preparacion_looker.ipynb       # Prep. para BigQuery/Looker
│
├── streamlit/                      # Dashboard Streamlit (Ruta 1)
│   ├── app.py                      # Aplicación principal
│   ├── teleton_utils.py            # Funciones reutilizables
│   ├── requirements.txt            # Dependencias
│   ├── .streamlit/
│   │   └── config.toml             # Configuración con colores Teletón
│   ├── data/                       # Datos procesados
│   │   ├── agregacion_giro.csv
│   │   ├── agregacion_estado.csv
│   │   ├── agregacion_antiguedad.csv
│   │   ├── segmentos_nps.csv
│   │   └── kpis.csv
│   └── README.md                   # Documentación Streamlit
│
├── looker/                         # BigQuery + Looker Studio (Ruta 2)
│   ├── TUTORIAL_BIGQUERY_LOOKER.md # Tutorial completo paso a paso
│   ├── bigquery_data/              # Datos para BigQuery
│   │   ├── dimensiones.csv
│   │   ├── hechos.csv
│   │   ├── agregaciones.csv
│   │   ├── kpis_globales.csv
│   │   └── teleton_completo.csv
│   ├── bigquery_schemas.json       # Esquemas de tablas
│   └── diccionario_datos.json      # Documentación de datos
│
└── README.md                       # Este archivo
```

---

## 🚀 Guía de Inicio Rápido

### Requisitos Previos

- Python 3.8+
- Jupyter Notebook o JupyterLab
- pip (gestor de paquetes)

### Opción 1: Dashboard con Streamlit

#### Paso 1: Generar Datos Limpios

```bash
cd jupyter
jupyter notebook 01_analisis_exploratorio.ipynb
# Ejecutar todas las celdas (Cell > Run All)
```

Esto creará:
- `datos/teleton_limpio.csv`

#### Paso 2: Preparar Componentes de Streamlit

```bash
jupyter notebook 02_preparacion_streamlit.ipynb
# Ejecutar todas las celdas
```

Esto creará:
- `streamlit/teleton_utils.py`
- Archivos CSV en `streamlit/data/`

#### Paso 3: Ejecutar Dashboard

```bash
cd ../streamlit
pip install -r requirements.txt
streamlit run app.py
```

El dashboard se abrirá en `http://localhost:8501`

**Ver documentación completa**: [`streamlit/README.md`](streamlit/README.md)

---

### Opción 2: Dashboard con Looker Studio

#### Paso 1: Generar Datos para BigQuery

```bash
cd jupyter
jupyter notebook 03_preparacion_looker.ipynb
# Ejecutar todas las celdas
```

Esto creará:
- 5 archivos CSV en `looker/bigquery_data/`
- `looker/bigquery_schemas.json`
- `looker/diccionario_datos.json`

#### Paso 2: Configurar BigQuery y Looker Studio

Sigue el tutorial completo: [`looker/TUTORIAL_BIGQUERY_LOOKER.md`](looker/TUTORIAL_BIGQUERY_LOOKER.md)

Incluye:
1. Crear proyecto en Google Cloud Platform
2. Crear dataset en BigQuery
3. Cargar tablas desde CSV
4. Configurar permisos IAM para @tec.mx
5. Conectar Looker Studio
6. Crear dashboard con colores Teletón

---

## 📈 Indicadores Clave (KPIs)

El proyecto calcula 6 KPIs principales:

| KPI | Descripción | Escala |
|-----|-------------|--------|
| **Satisfacción General** | Promedio de satisfacción general con Teletón | 1-10 |
| **Net Promoter Score (NPS)** | (% Promotores - % Detractores) × 100 | -100 a +100 |
| **Índice Calidad Servicio** | Promedio de 13 dimensiones de calidad | 1-5 |
| **Transparencia** | Promedio de transparencia percibida | 1-10 |
| **Calidad Percibida** | Promedio de calidad general percibida | 1-10 |
| **Antigüedad Promedio** | Años promedio como benefactor | Años |

---

## 🎨 Paleta de Colores Teletón

El proyecto utiliza la paleta oficial de Fundación Teletón:

### Colores Principales

| Color | Hex | Uso |
|-------|-----|-----|
| **Amarillo Teletón** | `#F7C600` | Acentos, highlights, valores positivos |
| **Morado Profundo** | `#4B1F76` | Títulos, gráficos principales |
| **Morado Medio** | `#7E3AA7` | Gráficos secundarios, variaciones |

### Colores de Acento

| Color | Hex | Uso |
|-------|-----|-----|
| **Magenta** | `#D7268F` | Énfasis especial |
| **Azul** | `#1A2A6C` | Mapas geográficos |
| **Verde** | `#2ECC71` | Promotores, indicadores positivos |
| **Naranja** | `#F39C12` | Alertas moderadas |
| **Rojo** | `#E74C3C` | Detractores, indicadores negativos |

### Colores Neutros

| Color | Hex | Uso |
|-------|-----|-----|
| **Blanco** | `#FFFFFF` | Fondos principales |
| **Gris Claro** | `#F5F5F5` | Fondos de tarjetas |
| **Gris Medio** | `#7F8C8D` | Texto secundario |
| **Gris Oscuro** | `#2D3436` | Texto principal |

---

## 📚 Contenido de los Notebooks

### Notebook 1: Análisis Exploratorio

**Archivo**: `jupyter/01_analisis_exploratorio.ipynb`

**Contenido**:
- Carga y validación de datos
- Renombrado de columnas para facilitar análisis
- Tratamiento de valores faltantes
- Función `estadisticas_completas()` con todas las medidas requeridas:
  - **Tendencia Central**: Media aritmética, geométrica, mediana, moda
  - **Dispersión**: Rango, desviación estándar, varianza, IQR, CV
- Análisis de 13 dimensiones de calidad (Likert 1-5)
- Análisis de 4 variables de satisfacción (escala 1-10)
- Cálculo de NPS con segmentación
- Detección de outliers (método IQR)
- Múltiples visualizaciones con paleta Teletón
- Análisis de correlaciones
- Segmentación por antigüedad
- Exportación de dataset limpio

**Output**: `datos/teleton_limpio.csv`

---

### Notebook 2: Preparación Streamlit

**Archivo**: `jupyter/02_preparacion_streamlit.ipynb`

**Contenido**:
- 6 funciones de cálculo de KPIs
- Función de segmentación NPS (promotores/pasivos/detractores)
- 3 funciones de agregación (por giro, estado, antigüedad)
- 8 funciones de visualización con paleta Teletón:
  - Gauge de KPIs
  - Gráfico de distribución NPS
  - Gráfico de 13 dimensiones de calidad
  - Gráfico por giro empresarial
  - Gráfico geográfico por estado
  - Gráfico de tendencia por antigüedad
  - Heatmap de correlaciones
- Exportación de agregaciones
- Creación de módulo `teleton_utils.py`

**Outputs**:
- `streamlit/teleton_utils.py`
- `streamlit/data/*.csv` (5 archivos)

---

### Notebook 3: Preparación Looker

**Archivo**: `jupyter/03_preparacion_looker.ipynb`

**Contenido**:
- Optimización de tipos de datos para BigQuery
- Creación de 4 tablas estructuradas:
  - **dimensiones**: Perfil de benefactores
  - **hechos**: Evaluaciones y métricas
  - **agregaciones**: Métricas pre-calculadas
  - **kpis_globales**: KPIs consolidados
- Generación de esquemas BigQuery en JSON
- Exportación de 5 CSVs para importar a BigQuery
- Diccionario de datos completo con:
  - Descripción de tablas y campos
  - 4 métricas calculadas sugeridas para Looker
  - Paleta de colores Teletón

**Outputs**:
- `looker/bigquery_data/*.csv` (5 archivos)
- `looker/bigquery_schemas.json`
- `looker/diccionario_datos.json`

---

## 📊 Comparación: Streamlit vs Looker Studio

| Aspecto | Streamlit | Looker Studio |
|---------|-----------|---------------|
| **Enfoque** | Programático | Visual (sin código) |
| **Control** | Total control del código | Limitado a funciones de Looker |
| **Curva de aprendizaje** | Media (requiere Python) | Baja (interfaz drag-and-drop) |
| **Personalización** | Muy alta | Media-Alta |
| **Hosting** | Requiere servidor Python | Hosting gratuito de Google |
| **Costo** | Gratis (self-hosted) | Gratis (hasta cierto uso) |
| **Compartir** | URL del servidor | URL de Google |
| **Actualización de datos** | Manual (re-ejecutar) | Automática desde BigQuery |
| **Colaboración** | Requiere acceso al código | Fácil compartir con permisos |
| **Escalabilidad** | Limitada por servidor | Alta (infraestructura de Google) |

### Cuándo Usar Cada Opción

**Usa Streamlit si**:
- Necesitas total control del código
- Quieres aprender Python y desarrollo web
- Necesitas visualizaciones muy personalizadas
- Tienes acceso a un servidor para hosting

**Usa Looker Studio si**:
- Prefieres interfaz visual sin código
- Necesitas compartir fácilmente con muchos usuarios
- Quieres actualización automática de datos
- Prefieres hosting en la nube sin mantenimiento

---

## 🎓 Uso Académico

Este proyecto está diseñado para el curso **CD2001B** del Tecnológico de Monterrey.

### Para Profesores

1. **Presentar el proyecto**: Usa los slides en `slides/proyecto_dashboard_teleton.md`
2. **Configurar BigQuery**: Sigue el tutorial en `looker/TUTORIAL_BIGQUERY_LOOKER.md`
3. **Configurar permisos**: Agrega `domain:tec.mx` con rol "Visualizador de datos de BigQuery"
4. **Compartir materiales**: Los alumnos pueden clonar este repositorio

### Para Alumnos

1. **Revisar slides**: Entender los requisitos del proyecto
2. **Ejecutar Notebook 1**: Realizar análisis exploratorio completo
3. **Elegir ruta**:
   - **Ruta 1 (Programática)**: Ejecutar Notebook 2 y crear dashboard Streamlit
   - **Ruta 2 (Visual)**: Ejecutar Notebook 3 y crear dashboard en Looker Studio
4. **Documentar**: Crear reporte con hallazgos y visualizaciones

### Rúbrica de Evaluación

Ver sección **"Rúbrica de Evaluación"** en los slides: `slides/proyecto_dashboard_teleton.md`

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Uso |
|------------|---------|-----|
| **Python** | 3.8+ | Lenguaje principal |
| **Pandas** | 2.0+ | Procesamiento de datos |
| **NumPy** | 1.24+ | Cálculos numéricos |
| **Matplotlib** | 3.7+ | Visualizaciones base |
| **Seaborn** | 0.12+ | Visualizaciones estadísticas |
| **Streamlit** | 1.28+ | Dashboard interactivo |
| **Jupyter** | - | Notebooks de análisis |
| **BigQuery** | - | Data warehouse en la nube |
| **Looker Studio** | - | Visualización sin código |
| **Slidev** | - | Presentaciones (opcional) |

---

## 📖 Recursos Adicionales

### Documentación de Herramientas

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Looker Studio Help](https://support.google.com/looker-studio)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

### Tutoriales

- [Streamlit Tutorial](https://docs.streamlit.io/library/get-started)
- [BigQuery Quickstart](https://cloud.google.com/bigquery/docs/quickstarts)
- [Looker Studio Tutorial](https://support.google.com/looker-studio/answer/6283323)

### Estadística

- [Measures of Central Tendency](https://www.khanacademy.org/math/statistics-probability)
- [Measures of Dispersion](https://www.khanacademy.org/math/statistics-probability)
- [Net Promoter Score (NPS)](https://www.netpromotersystem.com/about/)

---

## 🐛 Solución de Problemas Comunes

### Problema: "FileNotFoundError: teleton_limpio.csv"

**Solución**: Ejecuta el Notebook 1 primero para generar el archivo.

```bash
cd jupyter
jupyter notebook 01_analisis_exploratorio.ipynb
# Ejecutar todas las celdas
```

### Problema: "ModuleNotFoundError: No module named 'streamlit'"

**Solución**: Instala las dependencias.

```bash
cd streamlit
pip install -r requirements.txt
```

### Problema: Gráficos no se ven en Jupyter

**Solución**: Agrega al inicio del notebook:

```python
%matplotlib inline
```

### Problema: Errores de encoding en CSV

**Solución**: Los archivos están en `utf-8-sig`. Si tienes problemas, usa:

```python
pd.read_csv('archivo.csv', encoding='utf-8-sig')
```

### Problema: No puedo acceder a BigQuery

**Solución**: Verifica que:
1. Estés usando tu cuenta @tec.mx
2. El profesor haya configurado permisos para `domain:tec.mx`
3. Estés en el proyecto correcto de GCP

---

## 📝 Notas Importantes

### Privacidad de Datos

- Los datos de `teleton.xlsx` son ficticios o anonimizados
- **NO compartir** datos sensibles públicamente
- Configurar permisos adecuados en BigQuery (solo @tec.mx)

### Buenas Prácticas

- **Documentar** todo el código con comentarios
- **Versionamiento**: Usar Git para control de versiones
- **Reproducibilidad**: Asegurar que todos los notebooks se puedan ejecutar en orden
- **Validación**: Verificar cálculos manualmente antes de confiar en resultados

### Mejoras Futuras

- [ ] Agregar análisis de series temporales (si hay datos históricos)
- [ ] Implementar modelos predictivos de satisfacción
- [ ] Crear alertas automáticas para NPS bajo
- [ ] Integrar con Google Sheets para actualización en tiempo real
- [ ] Agregar autenticación en Streamlit
- [ ] Crear pruebas unitarias para funciones de cálculo

---

## 👥 Contribuciones

Este proyecto fue desarrollado para Fundación Teletón como parte del curso CD2001B.

### Autor

- **Proyecto Reto CD2001B**
- Tecnológico de Monterrey

### Agradecimientos

- Fundación Teletón por proporcionar el contexto del proyecto
- Empresas benefactoras que respondieron la encuesta

---

## 📄 Licencia

Este proyecto es de uso académico para el Tecnológico de Monterrey.

**Restricciones**:
- No usar con fines comerciales
- No compartir datos de benefactores fuera del contexto académico
- Respetar la privacidad de los datos

---

## 📧 Contacto y Soporte

Para dudas sobre el proyecto:

1. **Revisa primero**:
   - Este README
   - `streamlit/README.md` para Streamlit
   - `looker/TUTORIAL_BIGQUERY_LOOKER.md` para BigQuery/Looker

2. **Consulta la documentación** de las herramientas (enlaces arriba)

3. **Contacta a tu profesor** del curso CD2001B

---

## ✅ Checklist de Completitud del Proyecto

### Análisis Exploratorio
- [ ] Notebook 1 ejecutado completamente
- [ ] Dataset limpio generado (`teleton_limpio.csv`)
- [ ] Todos los KPIs calculados
- [ ] Visualizaciones creadas con paleta Teletón

### Opción Streamlit
- [ ] Notebook 2 ejecutado
- [ ] Módulo `teleton_utils.py` generado
- [ ] Dashboard ejecutándose localmente
- [ ] Todos los filtros funcionando
- [ ] Datos exportables

### Opción Looker Studio
- [ ] Notebook 3 ejecutado
- [ ] 5 CSVs generados para BigQuery
- [ ] Proyecto de GCP creado
- [ ] Dataset en BigQuery creado
- [ ] Tablas cargadas en BigQuery
- [ ] Permisos IAM configurados
- [ ] Looker Studio conectado
- [ ] Dashboard completo con 6 KPIs
- [ ] Filtros interactivos funcionando
- [ ] Dashboard compartido con alumnos

### Documentación
- [ ] README principal leído
- [ ] Slides revisados
- [ ] Reporte de hallazgos escrito (si aplica)

---

**¡Éxito con tu proyecto de Dashboard para Fundación Teletón! 💛**

---

*Última actualización: 2024*
