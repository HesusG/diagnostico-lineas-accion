# Semana 2: Pruebas Estadísticas Avanzadas

## 📚 Módulo 1 - Parte 2

### 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:
- Realizar pruebas Ji-cuadrada de independencia
- Aplicar ANOVA para comparar múltiples medias
- Implementar regresión lineal simple
- Calcular y interpretar correlaciones
- Integrar todas las técnicas estadísticas en Python

---

## 📋 Contenidos

### 1. Prueba Ji-Cuadrada (χ²)
- Prueba de independencia entre variables categóricas
- Tablas de contingencia
- Interpretación de resultados
- Aplicación: ¿El área de servicio influye en la satisfacción?

### 2. ANOVA (Análisis de Varianza)
- Comparación de 3 o más medias
- Supuestos y verificación
- Pruebas post-hoc (Tukey, Bonferroni)
- Aplicación: Comparar satisfacción entre múltiples departamentos

### 3. Regresión Lineal y Correlación
- Correlación de Pearson
- Modelo de regresión lineal simple
- Interpretación de coeficientes (R², pendiente)
- Predicción
- Aplicación: Predecir satisfacción basada en tiempo de servicio

### 4. Estadística No Paramétrica
- Prueba de Mann-Whitney U
- Kruskal-Wallis (alternativa a ANOVA)
- Cuándo usar pruebas no paramétricas

---

## 📁 Estructura de la Semana

```
Semana2/
├── README.md
├── notebooks/
│   ├── 01_ji_cuadrada.ipynb
│   ├── 02_anova.ipynb
│   ├── 03_regresion_correlacion.ipynb
│   └── 04_integracion_estadistica.ipynb
├── ejercicios/
│   ├── workshop1_plantilla.ipynb
│   └── workshop2_plantilla.ipynb
├── scripts/
│   ├── analisis_descriptivo.py
│   └── pruebas_hipotesis.py
├── guias/
│   ├── guia_ji_cuadrada.md
│   ├── guia_anova.md
│   └── guia_regresion.md
└── datos/
    └── (reutiliza datos de Semana1/)
```

---

## 🔧 Herramientas Python

```python
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, f_oneway, pearsonr
```

---

## 📝 Actividades de la Semana

| Día | Actividad | Tipo | Tiempo |
|-----|-----------|------|--------|
| D1 | Ji-cuadrada: Teoría y práctica | Clase | 2h |
| D1 | Ejercicios Ji-cuadrada | Tarea | 3h |
| D2 | ANOVA: Teoría y práctica | Clase | 1h |
| D2 | Ejercicios ANOVA | Clase | 1h |
| D2 | Ejercicios ANOVA (continuación) | Tarea | 3h |
| D3 | Regresión y Correlación | Clase | 2h |
| D3 | Workshop 2 | Tarea | 3h |
| D4 | **Examen Módulo 1** | Clase | 2h |

---

## 📊 Entregables

### Workshop 2: Pruebas Estadísticas Avanzadas
**Fecha límite:** Miércoles de Semana 2

**Contenido:**
1. Prueba Ji-Cuadrada de Independencia (25 puntos)
   - Tabla de contingencia
   - Análisis de relación entre variables categóricas
   - Interpretación de resultados
2. ANOVA (35 puntos)
   - Comparación de múltiples grupos
   - Prueba post-hoc (Tukey)
   - Visualización comparativa
3. Regresión Lineal Simple (40 puntos)
   - Correlación de Pearson
   - Modelo de regresión
   - Interpretación de R² y coeficientes
   - Predicciones

**Formato:** Jupyter Notebook (.ipynb)
**Dataset:** student-alcohol-consumption.csv
**Valor:** 10% de la calificación final

**Archivo:** [workshop2_plantilla.ipynb](ejercicios/workshop2_plantilla.ipynb)

---

### Examen Módulo 1
**Fecha:** Viernes de Semana 2

**Duración:** 2 horas (1h teoría + 1h práctica)

**Contenido:**
- Medidas de tendencia central y dispersión (15%)
- Pruebas t para 1 y 2 muestras (20%)
- Prueba Ji-cuadrada (20%)
- ANOVA (25%)
- Regresión lineal y correlación (20%)

**Formato:** Mixto
- Parte 1: Preguntas teóricas (50%)
- Parte 2: Ejercicio práctico en Jupyter (50%)

**Valor:** 5% de la calificación final

---

## 💡 Tips de Estudio

### Para Ji-Cuadrada:
1. Siempre verifica que las frecuencias esperadas sean > 5
2. Usa tablas de contingencia para visualizar relaciones
3. Interpreta el p-value en contexto

### Para ANOVA:
1. Verifica supuestos: normalidad y homogeneidad de varianzas
2. Si rechazas H₀, usa pruebas post-hoc para identificar diferencias
3. Complementa con boxplots

### Para Regresión:
1. Siempre grafica los datos primero (scatter plot)
2. Verifica linealidad antes de ajustar el modelo
3. No extrapoles más allá del rango de tus datos
4. R² no lo es todo: interpreta la pendiente

---

## 📚 Lectura Recomendada

**Libro de texto:**
- Levin & Rubin. Capítulos 10-12

**Complementaria:**
- Keller, Gerald. "Statistics for management and economics"
- Newbold, Paul. "Estadística para administración y economía"

---

## 🎓 Preparación para el Reto

Esta semana es crucial porque aplicarás TODAS estas técnicas en tu proyecto final:

1. **Ji-cuadrada:** ¿El departamento influye en la satisfacción?
2. **ANOVA:** Comparar satisfacción entre múltiples áreas de la ONG
3. **Regresión:** Predecir calidad del servicio basado en variables clave
4. **Correlación:** Identificar relaciones entre variables

---

## ❓ Preguntas Frecuentes

**P: ¿Cuándo usar ANOVA vs múltiples pruebas t?**
R: ANOVA es preferible cuando comparas 3+ grupos porque controla el error Tipo I. Múltiples pruebas t inflan la probabilidad de falsos positivos.

**P: ¿Qué hacer si los supuestos de ANOVA no se cumplen?**
R: Usa la alternativa no paramétrica Kruskal-Wallis o transforma tus datos (log, raíz cuadrada).

**P: ¿Cómo interpreto un R² bajo en regresión?**
R: R² bajo significa que tu modelo explica poca varianza. Puede ser normal si hay muchos factores no medidos que influyen en Y.

---

**Próxima semana:** Módulo 2 - Ética, Compromiso Social y Diagnóstico Estratégico
