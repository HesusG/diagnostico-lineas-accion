# Diagnóstico para Líneas de Acción (CD2001B)

> **Institucion:** Tecnologico de Monterrey
> **Codigo del bloque:** CD2001B
> **Nombre:** Diagnostico para Lineas de Accion
> **Responsable de la adaptacion:** Hesus Garcia Cobos (hesus.garcia@tec.mx)
>
> Este repositorio es la **adaptacion** del profesor de la planificacion institucional proporcionada por el sistema Tec de Monterrey. El manual original del profesor se encuentra en [`data/CD2001B_Manual del Profesor_310125.pdf`](data/CD2001B_Manual%20del%20Profesor_310125.pdf).

## 📋 Descripción del Curso

Este repositorio contiene el material didáctico para el bloque **"Diagnóstico para líneas de acción"** (CD2001B) del Tecnológico de Monterrey. El curso forma parte de la Entrada de Negocios y tiene como objetivo desarrollar competencias en **Analítica Descriptiva**, **Analítica Prescriptiva** y **Compromiso Ético y Ciudadano**.

### 🎯 Objetivo Principal

Medir la calidad en el servicio de una Organización No Gubernamental (ONG) mediante análisis estadístico y visualización de datos, con el fin de generar líneas de acción estratégicas para la mejora organizacional.

---

## 🧩 Estructura del Curso

El bloque está organizado en **2 módulos** distribuidos a lo largo de **5 semanas**:

### **Módulo 1: Prueba de Hipótesis (Estadística para Negocios)**
📅 Semanas 1-2 | ⏱️ 20 horas contacto

**Competencias:**
- **SCD0104.B** - Análisis Descriptivo
- Aplicación de pruebas estadísticas con Python

**Contenidos:**
- Medidas de tendencia central y dispersión
- Prueba de hipótesis (1 y 2 muestras)
- ANOVA (Análisis de varianza)
- Ji-cuadrada
- Regresión lineal y correlación

### **Módulo 2: Diagnóstico Estratégico + Visualización**
📅 Semanas 3-4 | ⏱️ 20 horas contacto

**Competencias:**
- **SCD0105.B** - Gráficos Dinámicos
- **SCD0303.A** - Líneas de Acción Estratégica
- **SEG0401.A** - Reconocimiento y Empatía (Competencia Transversal)

**Contenidos:**
- Ética, derechos humanos y ODS
- Administración estratégica
- Visualización de datos con Looker Studio
- Storytelling con datos

### **Reto Integrador**
📅 Semana 5 | ⏱️ 40 horas

Proyecto completo de diagnóstico y propuesta de mejora para una ONG real.

---

## 📁 Organización del Repositorio

```
diagnostico-lineas-accion/
├── Semana1/          # Introducción y pruebas de hipótesis básicas
├── Semana2/          # Pruebas estadísticas avanzadas
├── Semana3/          # Ética y diagnóstico estratégico
├── Semana4/          # Visualización con Python y Looker Studio
├── Semana5/          # Integración y reto final
└── recursos/         # Bibliografía, guías de instalación, cheat sheets
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Jupyter Notebook / JupyterLab**
- **Pandas** - Manipulación de datos
- **NumPy** - Cálculos numéricos
- **SciPy** - Estadística y pruebas de hipótesis
- **Statsmodels** - Modelos estadísticos
- **Matplotlib & Seaborn** - Visualización de datos
- **Plotly** - Gráficos interactivos
- **Looker Studio** - Dashboards dinámicos

---

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/HesusG/diagnostico-lineas-accion.git
cd diagnostico-lineas-accion
```

### 2. Crear entorno virtual (recomendado)

**Opción A: Con venv**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Opción B: Con conda**
```bash
conda env create -f environment.yml
conda activate diagnostico-analisis
```

### 3. Iniciar Jupyter

```bash
jupyter notebook
```

---

## 📚 Evaluación

| Componente | Porcentaje | Descripción |
|-----------|-----------|-------------|
| **Módulo 1: Análisis Estadístico** | **25%** | Semanas 1-2 |
| Workshop 1 | 10% | Análisis descriptivo + Pruebas t |
| Workshop 2 | 10% | Ji-cuadrada + ANOVA + Regresión |
| Examen Módulo 1 | 5% | Evaluación teórico-práctica |
| **Módulo 2: Diagnóstico Estratégico** | **25%** | Semanas 3-4 |
| Actividad #1 Parte 1 | 6.25% | Contexto social y ético |
| Actividad #1 Parte 2 | 6.25% | Diagnóstico estratégico |
| Actividad #2 Parte 1 | 6.25% | Preparación de datos |
| Actividad #2 Parte 2 | 6.25% | Dashboard Looker Studio |
| **Reto Final** | **50%** | Semana 5 |
| Reporte Escrito | 20% | Documento integrador 10-15 páginas |
| Dashboard Looker Studio | 10% | Dashboard interactivo |
| Presentación Ejecutiva | 15% | Presentación oral 15 minutos |
| Jupyter Notebook | 5% | Código Python completo |

**Detalles completos:** Ver [EVALUACION_DESGLOSE.md](EVALUACION_DESGLOSE.md)

---

## 👤 Modalidad de Trabajo

**Todas las actividades y el reto son INDIVIDUALES**

- Módulo 1: Trabajo individual
- Módulo 2: Trabajo individual
- Reto Final: Trabajo individual

---

## 📖 Recursos Adicionales

- [Guía de instalación de Python](recursos/instalacion_python_jupyter.md)
- [Bibliografía recomendada](recursos/bibliografia.md)
- [Enlaces útiles](recursos/enlaces_utiles.md)
- [Cheat sheets](recursos/)

---

## 👨‍🏫 Información del Profesor

**Responsable de la adaptacion:** Hesus Garcia Cobos
**Email:** hesus.garcia@tec.mx
**Campus:** Puebla

**Diseñadores de la planificacion institucional:**
- Beatriz González
- Ericka Uribe
- Gabriel Héctor Carmona

---

## 📝 Licencia

Este material es de uso académico para el Tecnológico de Monterrey.

---

## 🤝 Contribuciones

Si encuentras errores o tienes sugerencias de mejora, por favor:
1. Abre un issue
2. O contacta directamente al profesor responsable

---

**Última actualización:** Enero 2025
**Versión del curso:** CD2001B
