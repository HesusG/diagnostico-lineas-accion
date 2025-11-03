# 📈 Semana 2: Pruebas Estadísticas Avanzadas

## 📚 Módulo 1 - Parte 2

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:
- ✅ Realizar pruebas Ji-cuadrada para variables categóricas
- ✅ Aplicar ANOVA para comparar 3+ medias simultáneamente
- ✅ Implementar regresión lineal simple y predecir valores
- ✅ Calcular e interpretar correlaciones de Pearson
- ✅ Decidir cuál prueba estadística usar según tipo de datos
- ✅ Integrar todas las técnicas en análisis completos

---

## 📅 Plan Detallado de Clases

Para el **plan detallado día por día** con agendas completas, actividades de equipo opcionales, y notas para el profesor, consulta:

👉 **[PLAN_CLASES.md](PLAN_CLASES.md)** - Plan completo de 4 clases × 2 horas

**Resumen de las 4 clases:**
1. **Clase 1:** Prueba Ji-Cuadrada (χ²) para variables categóricas
2. **Clase 2:** ANOVA para comparar 3+ medias
3. **Clase 3:** Regresión Lineal y Correlación (predicción)
4. **Clase 4:** Integración y Workshop 2 (trabajo en clase)

---

## 📁 Estructura de la Semana

```
Semana2/
├── README.md                                 # Este archivo
├── notebooks/
│   ├── 01_ji_cuadrada.ipynb                 # Clase 1: Variables categóricas
│   ├── 02_anova.ipynb                       # Clase 2: Comparar 3+ grupos
│   ├── 03_regresion_correlacion.ipynb       # Clase 3: Predicción
│   └── 04_integracion_estadistica.ipynb     # Clase 3-4: Árbol de decisión
├── ejercicios/
│   └── workshop2_plantilla.ipynb            # ⭐ ENTREGABLE - 10% calificación
├── ejercicios_extra/
│   ├── practica_ong_estadistica_avanzada.ipynb  # Práctica adicional
│   └── textbook_exercises.ipynb             # Ejercicios de libro
└── datos/
    └── (reutiliza datos de Semana1/)
```

---

## 📊 Entregables de la Semana

### **🎯 Workshop 2: Análisis Estadístico Avanzado**

**Archivo:** [workshop2_plantilla.ipynb](ejercicios/workshop2_plantilla.ipynb)
**Dataset:** `fundacion_esperanza_donadores.csv` (ONG - 1000 donadores)
**Valor:** 10% de la calificación final
**Fecha límite:** Ver calendario del curso

**Contenido del Workshop:**

| Sección | Descripción | Puntos |
|---------|-------------|--------|
| **Parte 1: Chi-cuadrada** | ¿Tipo de donante afecta retención? | 25 pts |
| **Parte 2: ANOVA** | Comparar satisfacción por canal de donación | 30 pts |
| **Parte 3: Regresión** | Predecir satisfacción con años como donante | 25 pts |
| **Parte 4: Integración** | Análisis completo + recomendaciones | 20 pts |
| **BONUS: Reflexión MEAL** | Análisis académico comparativo (Semana 1 vs 2) | +10 pts |
| **TOTAL** | | **100 pts** (+10 bonus) |

---

## 🔧 Herramientas Python

### **Librerías principales:**
```python
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency, f_oneway, pearsonr
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
```

### **Comandos clave:**

**Chi-cuadrada:**
```python
from scipy.stats import chi2_contingency

# Crear tabla de contingencia
tabla = pd.crosstab(df['var1'], df['var2'])

# Prueba chi-cuadrada
chi2, p_value, dof, expected = chi2_contingency(tabla)
```

**ANOVA:**
```python
from scipy.stats import f_oneway

# ANOVA de un factor
f_stat, p_value = f_oneway(grupo1, grupo2, grupo3)

# Post-hoc (Tukey)
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(df['variable'], df['grupo'])
```

**Regresión:**
```python
from scipy.stats import pearsonr

# Correlación
r, p_value = pearsonr(df['x'], df['y'])

# Regresión lineal simple
from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Predicción
y_pred = slope * x_nuevo + intercept
```

---

## 💡 Tips de Estudio

1. **🗺️ Usa el árbol de decisión:**
   - Antes de cada análisis: ¿Qué tipo de variables tengo?
   - Categórica vs categórica → Chi-cuadrada
   - Numérica con 3+ grupos → ANOVA
   - 2 numéricas para predecir → Regresión

2. **📊 SIEMPRE visualiza primero:**
   - Chi-cuadrada → Gráfico de barras agrupadas
   - ANOVA → Boxplots por grupo
   - Regresión → Scatter plot con línea de tendencia

3. **✅ Verifica supuestos:**
   - Chi-cuadrada: Frecuencias esperadas > 5
   - ANOVA: Normalidad (Shapiro), homogeneidad (Levene)
   - Regresión: Linealidad, residuos normales

4. **🤖 Usa IA estratégicamente:**
   - ✅ "Explica cuándo usar ANOVA vs chi-cuadrada"
   - ✅ "Mi ANOVA dio p=0.03, ¿qué significa?"
   - ❌ "Dame todo el código del workshop"

---

## 🆘 Recursos de Apoyo

### **Material del curso:**
- [Semana 1: Estadística Básica](../Semana1/) - Repasar t-test y conceptos base
- [CODEBOOK: Dataset ONG](../Semana1/datos/CODEBOOK_fundacion_esperanza.md)
- [Práctica extra avanzada](ejercicios_extra/practica_ong_estadistica_avanzada.ipynb)

### **Recursos externos:**

**Estadística:**
- [Stat Quest - ANOVA](https://www.youtube.com/watch?v=0Vj2V2qRU10) - Video explicativo
- [Seeing Theory - Regresión](https://seeing-theory.brown.edu/regression-analysis/index.html)

**Python:**
- [SciPy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html) - Todas las pruebas
- [Statsmodels](https://www.statsmodels.org/stable/index.html) - ANOVA y regresión avanzada

---

## ❓ Preguntas Frecuentes

**P: ¿Cuándo uso chi-cuadrada vs ANOVA?**
R:
- **Chi-cuadrada:** Ambas variables son **categóricas** (ej: género × área)
- **ANOVA:** Variable numérica comparada entre **3+ grupos categóricos** (ej: satisfacción × 4 áreas)

**P: ¿Por qué no hacer múltiples t-tests en lugar de ANOVA?**
R: Múltiples t-tests aumentan el error Tipo I (falsos positivos). ANOVA controla este error.

**P: ¿Qué significa R² = 0.65 en regresión?**
R: El modelo explica 65% de la variabilidad en Y. Mientras más cerca de 1, mejor el modelo.

**P: ¿Puedo usar regresión si las variables no están perfectamente relacionadas linealmente?**
R: Depende. Si r < 0.3, la relación es muy débil. Usa scatter plot para verificar linealidad.

**P: ¿Las actividades de equipo opcionales cuentan para calificación?**
R: No, son opcionales y a discreción del profesor. Son para reforzar conceptos de forma interactiva.

---

## 🚀 Próximos Pasos

**Al terminar Semana 2:**
1. ✅ Dominas chi-cuadrada, ANOVA, y regresión
2. ✅ Sabes elegir prueba correcta según tipo de datos
3. ✅ Has completado Workshop 2 (10% de tu calificación)
4. ✅ **Completaste Módulo 1** (estadística completa) 🎉

**Siguiente módulo:**
- [Semana 3: Análisis Estratégico](../Semana3/)
  - Matriz BCG
  - Diamante de Porter
  - Customer Journey Map
  - Selección de ONG para proyecto final

---

## 📝 Checklist de la Semana

**Durante Clase 1 (Chi-cuadrada):**
- [ ] Entendí cuándo usar chi-cuadrada
- [ ] Sé crear tablas de contingencia
- [ ] Puedo interpretar p-value de chi-cuadrada
- [ ] (Opcional) Encontré correlaciones espurias divertidas

**Durante Clase 2 (ANOVA):**
- [ ] Entendí diferencia entre ANOVA y múltiples t-tests
- [ ] Sé interpretar F-statistic y p-value
- [ ] Entiendo para qué sirven pruebas post-hoc
- [ ] (Opcional) Creé analogía clara de ANOVA

**Durante Clase 3 (Regresión):**
- [ ] Puedo calcular correlación de Pearson
- [ ] Sé crear modelo de regresión lineal
- [ ] Entiendo qué significa R²
- [ ] Puedo hacer predicciones con el modelo
- [ ] (Opcional) Competí en Prediction Game

**Durante Clase 4 (Integración):**
- [ ] Uso árbol de decisión para elegir prueba
- [ ] Trabajé en Workshop 2 en clase
- [ ] Resolví dudas con profesor
- [ ] (Opcional) Creé meme estadístico

**Después de Clase 4:**
- [ ] **Entregué Workshop 2 completo** ⭐

---

**¡Felicidades por completar el Módulo 1 de Estadística!** 📊🎉

Ahora tienes un arsenal completo de técnicas estadísticas. En el mundo real, **saber CUÁNDO usar cada prueba** es más importante que memorizar fórmulas. ¡Ya estás listo para el proyecto final!
