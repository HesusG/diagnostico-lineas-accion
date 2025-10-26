# Semana 1: Introducción a Estadística y Pruebas de Hipótesis

## 📚 Módulo 1 - Parte 1

### 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:
- Calcular y analizar medidas de tendencia central y dispersión
- Realizar pruebas de hipótesis para una muestra
- Realizar pruebas de hipótesis para dos muestras
- Interpretar resultados estadísticos en el contexto de negocios

---

## 📋 Contenidos

### 1. Medidas de Tendencia Central y Dispersión
- Media, mediana, moda
- Varianza y desviación estándar
- Cuartiles y percentiles
- Interpretación en contexto empresarial

### 2. Prueba de Hipótesis para Una Muestra
- Conceptos fundamentales (H0, H1, nivel de significancia)
- Prueba Z para la media (σ conocida)
- Prueba t para la media (σ desconocida)
- Interpretación de p-values

### 3. Prueba de Hipótesis para Dos Muestras
- Prueba t para muestras independientes
- Prueba t para muestras pareadas
- Comparación de proporciones

---

## 📁 Estructura de la Semana

```
Semana1/
├── README.md                                    # Este archivo
├── notebooks/
│   ├── 01_introduccion_estadistica.ipynb       # Conceptos básicos
│   ├── 02_medidas_tendencia_central.ipynb      # Medidas descriptivas
│   └── 03_pruebas_hipotesis_1_2_muestras.ipynb # Pruebas estadísticas
├── ejercicios/
│   ├── ejercicio_medidas_tendencia.ipynb       # Práctica guiada
│   └── ejercicio_pruebas_hipotesis.ipynb       # Aplicación práctica
├── guias/
│   ├── guia_medidas_tendencia_central.md       # Referencia rápida
│   └── guia_pruebas_hipotesis.md               # Paso a paso
└── datos/
    ├── ejemplo_satisfaccion_clientes.csv       # Dataset práctica
    └── README_datos.md                          # Descripción de datasets
```

---

## 🔧 Herramientas Python

### Librerías principales:
```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 📝 Actividades de la Semana

| Día | Actividad | Tipo | Tiempo |
|-----|-----------|------|--------|
| D1 | Bienvenida y conceptos de estadística | Clase | 1h |
| D1 | Notebook: Medidas de tendencia central | Clase | 2h |
| D1 | Ejercicio: Medidas de tendencia | Tarea | 3h |
| D2 | Prueba de hipótesis 1 muestra | Clase | 1h |
| D2 | Práctica con Python | Clase | 2h |
| D2 | Ejercicio: Prueba de hipótesis | Tarea | 3h |
| D3 | Prueba de hipótesis 2 muestras | Clase | 2h |
| D3 | Workshop 1 | Tarea | 3h |
| D4 | Revisión Workshop 1 | Clase | 2h |
| D4 | **Entregable 1:** Análisis exploratorio | Tarea | 10h |

---

## 📊 Entregables

### Entregable 1: Análisis Exploratorio de Base de Datos
**Fecha límite:** Fin de semana 2

**Requisitos:**
1. Base de datos en Python (archivo .csv o .xlsx)
2. Responder preguntas teóricas en un documento PDF o Word
3. Identificar variables continuas vs discretas
4. Explicar metodología de investigación

**Valor:** Formativo (prepara para el reto)

---

## 💡 Tips de Estudio

1. **Practica con datos reales:** Usa los datasets proporcionados
2. **Interpreta, no solo calcules:** Siempre explica qué significan los números
3. **Visualiza primero:** Antes de hacer pruebas, explora tus datos gráficamente
4. **Verifica supuestos:** Las pruebas estadísticas tienen condiciones de aplicación

---

## 🆘 Recursos de Apoyo

- [Guía de instalación de Python](../recursos/instalacion_python_jupyter.md)
- [Cheat sheet de Pandas](../recursos/cheat_sheet_pandas.pdf)
- [Cheat sheet de SciPy Stats](../recursos/cheat_sheet_scipy_stats.pdf)
- [Bibliografía](../recursos/bibliografia.md)

---

## 📚 Lectura Recomendada

**Libro de texto:**
- Levin, R. I. & Rubin, D. S. "Estadística para administradores" (Capítulos 1-3, 8-9)

**Complementaria:**
- Newbold, Paul. "Estadística para administración y economía" (6ª ed.)

---

## ❓ Preguntas Frecuentes

**P: ¿Puedo usar otra herramienta además de Python?**
R: El curso está diseñado para Python, pero puedes complementar con Excel para verificar resultados.

**P: ¿Qué hago si no tengo experiencia con Python?**
R: Revisa primero la guía de instalación y el notebook de introducción. También hay tutoriales en la carpeta de recursos.

**P: ¿Los ejercicios son obligatorios?**
R: Sí, forman parte de tu calificación y preparan para el reto final.

---

**Próxima semana:** Pruebas estadísticas avanzadas (ANOVA, Ji-cuadrada, Regresión)
