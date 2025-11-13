# Dashboard Streamlit - Fundación Teletón

Dashboard interactivo para análisis de satisfacción de empresas benefactoras.

## 📋 Descripción

Este dashboard presenta visualizaciones interactivas de la encuesta de satisfacción realizada a empresas benefactoras de Fundación Teletón, incluyendo:

- **KPIs principales**: Satisfacción general, NPS, calidad de servicio, transparencia
- **Análisis NPS**: Distribución de promotores, pasivos y detractores
- **Evaluación de calidad**: 13 dimensiones de calidad de servicio
- **Perfil de benefactores**: Análisis por giro, estado y antigüedad
- **Correlaciones**: Relaciones entre métricas de satisfacción
- **Filtros interactivos**: Por estado, giro y segmento de antigüedad

## 🚀 Instalación

### 1. Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Preparar Datos

Antes de ejecutar el dashboard, debes generar el archivo de datos ejecutando el **Notebook 1: Análisis Exploratorio**:

```bash
# Navega a la carpeta de notebooks
cd ../jupyter

# Ejecuta el notebook (usando Jupyter)
jupyter notebook 01_analisis_exploratorio.ipynb
```

Esto creará el archivo `../datos/teleton_limpio.csv` necesario para el dashboard.

## ▶️ Ejecutar el Dashboard

```bash
streamlit run app.py
```

El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📂 Estructura de Archivos

```
streamlit/
├── app.py                  # Aplicación principal de Streamlit
├── teleton_utils.py        # Módulo con funciones de análisis y visualización
├── requirements.txt        # Dependencias de Python
├── .streamlit/
│   └── config.toml        # Configuración con colores de Teletón
├── data/                  # Datos procesados (generados por Notebook 2)
│   ├── agregacion_giro.csv
│   ├── agregacion_estado.csv
│   ├── agregacion_antiguedad.csv
│   ├── segmentos_nps.csv
│   └── kpis.csv
└── README.md              # Este archivo
```

## 🎨 Paleta de Colores

El dashboard utiliza la paleta oficial de Fundación Teletón:

- **Amarillo Teletón**: `#F7C600` (color principal)
- **Morado Profundo**: `#4B1F76` (gráficos, títulos)
- **Morado Medio**: `#7E3AA7` (acentos)

## 🔧 Configuración

El archivo `.streamlit/config.toml` contiene la configuración de colores y tema del dashboard. Puedes modificarlo para personalizar la apariencia.

## 📊 Funcionalidades

### Filtros Interactivos (Sidebar)

- **Estado**: Filtra benefactores por estado de la República
- **Giro Empresarial**: Filtra por sector empresarial
- **Segmento de Antigüedad**: Filtra por años como benefactor

### Secciones del Dashboard

1. **KPIs Principales**: 6 indicadores clave con tarjetas visuales
2. **Net Promoter Score**: Distribución de promotores/pasivos/detractores
3. **Calidad de Servicio**: 13 dimensiones evaluadas
4. **Perfil de Benefactores**: Análisis por giro, estado y antigüedad (tabs)
5. **Correlaciones**: Matriz de correlación entre métricas
6. **Explorador de Datos**: Tabla interactiva con opción de descarga

### Exportación de Datos

Usa el botón "📥 Descargar datos filtrados" en la sección "Explorador de Datos" para exportar los datos filtrados en formato CSV.

## 🐛 Solución de Problemas

### Error: "No se encontró el archivo teleton_limpio.csv"

**Causa**: No se ha ejecutado el Notebook 1 para generar los datos limpios.

**Solución**:
```bash
cd ../jupyter
jupyter notebook 01_analisis_exploratorio.ipynb
# Ejecuta todas las celdas del notebook
```

### Error: "ModuleNotFoundError: No module named 'streamlit'"

**Causa**: Las dependencias no están instaladas.

**Solución**:
```bash
pip install -r requirements.txt
```

### El dashboard no se abre automáticamente

**Solución**: Abre manualmente tu navegador y visita `http://localhost:8501`

## 📖 Documentación Adicional

- [Documentación de Streamlit](https://docs.streamlit.io/)
- [Guía de visualización con Matplotlib](https://matplotlib.org/stable/users/index.html)
- [Tutorial de Seaborn](https://seaborn.pydata.org/tutorial.html)

## 👥 Subcompetencias Demostradas

Este proyecto demuestra las siguientes subcompetencias:

- **SCD0104**: Análisis descriptivo con medidas de tendencia central y dispersión
- **SCD0105**: Creación de gráficos dinámicos interactivos

## 📝 Notas

- El dashboard se actualiza automáticamente cuando cambias los filtros
- Los datos se cachean para mejorar el rendimiento
- Las visualizaciones usan la paleta de colores oficial de Teletón
- El dashboard es responsive y se adapta a diferentes tamaños de pantalla

---

**Desarrollado para Proyecto Reto CD2001B - Fundación Teletón**
