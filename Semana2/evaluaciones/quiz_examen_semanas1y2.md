# 📝 Quiz: Semanas 1 y 2 - Análisis Estadístico

**Curso:** CD2001B - Diagnóstico para Líneas de Acción
**Tec de Monterrey - Campus Puebla**

---

## 📋 Instrucciones

- **Total de preguntas:** 20 (valor: 100 puntos)
- **Formato:** Opción múltiple (4 opciones por pregunta)
- **Secciones:**
  - Preguntas 1-5: Semana 1 (Medidas Descriptivas y Pruebas de Hipótesis)
  - Preguntas 6-10: Semana 2 (Chi-Cuadrada y ANOVA)
  - Preguntas 11-15: Funciones Python
  - Preguntas 16-18: Correlación y Regresión Lineal
  - Preguntas 19-20: Casos de Código (Análisis Crítico)

---

## 🟦 SECCIÓN 1: SEMANA 1 (Medidas Descriptivas y Pruebas de Hipótesis)

### Pregunta 1 (6 puntos)
**¿Cuándo es preferible usar la MEDIANA en lugar de la MEDIA?**

a) Cuando los datos son simétricos y no tienen valores extremos
b) Cuando tenemos datos categóricos como género o preferencias
c) Cuando hay valores extremos (outliers) que podrían sesgar el promedio
d) Cuando queremos saber el valor más frecuente en el dataset

---

### Pregunta 2 (6 puntos)
**Una ONG midió la satisfacción de 100 beneficiarios y obtuvo p-value = 0.042. ¿Qué significa esto con α = 0.05?**

a) Hay 4.2% de probabilidad de que H₁ sea verdadera
b) Hay evidencia suficiente para rechazar H₀ porque p < 0.05
c) No hay evidencia suficiente para rechazar H₀ porque p está cerca de 0.05
d) H₀ es verdadera en el 4.2% de los casos

---

### Pregunta 3 (6 puntos)
**¿Qué representa el RANGO INTERCUARTÍLICO (IQR)?**

a) La distancia entre el valor mínimo y máximo del dataset
b) La diferencia entre el cuartil 3 (75%) y el cuartil 1 (25%)
c) La diferencia entre el cuartil 2 (50%) y el cuartil 1 (25%)
d) El promedio de todos los valores que están dentro del rango normal

---

### Pregunta 4 (6 puntos)
**Una prueba t arroja p-value = 0.18. ¿Cuál es la interpretación CORRECTA?**

a) Rechazamos H₀ porque hay 18% de confianza en los datos
b) No rechazamos H₀ porque p > 0.05, no hay evidencia suficiente
c) Aceptamos H₀ como verdadera con 18% de significancia
d) El efecto observado tiene 18% de magnitud estadística

---

### Pregunta 5 (6 puntos)
**¿Qué tipo de prueba t usarías para comparar el peso promedio de un grupo de niños ANTES y DESPUÉS de un programa nutricional?**

a) Prueba t de una muestra, porque solo hay un grupo de niños
b) Prueba t independiente, porque hay dos momentos diferentes
c) Prueba t pareada, porque se mide a las mismas personas en dos momentos
d) Prueba t de dos muestras, porque hay mediciones antes y después

---

## 🟩 SECCIÓN 2: SEMANA 2 (Chi-Cuadrada y ANOVA)

### Pregunta 6 (8 puntos)
**¿Cuándo usarías la prueba de Chi-Cuadrada en lugar de una prueba t?**

a) Cuando quieres comparar promedios de 3 o más grupos
b) Cuando ambas variables son categóricas (género, región, programa)
c) Cuando tienes variables numéricas y quieres ver si están correlacionadas
d) Cuando quieres comparar la media de un grupo contra un valor conocido

---

### Pregunta 7 (8 puntos)
**Una ONG obtiene χ² = 15.3 con p-value = 0.002 al analizar género × programa. ¿Qué concluyes?**

a) No hay relación entre género y programa porque χ² es alto
b) Hay relación significativa, las variables NO son independientes
c) El 0.2% de los beneficiarios no tienen género definido
d) Hay relación significativa, las variables son independientes

---

### Pregunta 8 (8 puntos)
**¿Por qué NO deberías hacer múltiples pruebas t en lugar de usar ANOVA cuando comparas 5 grupos?**

a) Porque ANOVA es más rápida de calcular en Python
b) Porque cada prueba t aumenta el riesgo de Error Tipo I (falsos positivos)
c) Porque ANOVA te dice exactamente qué grupos son diferentes entre sí
d) Porque las pruebas t solo funcionan con exactamente 2 grupos

---

### Pregunta 9 (8 puntos)
**Una ONG compara satisfacción en 4 áreas y ANOVA arroja p-value = 0.03. ¿Qué significa?**

a) Al menos una área tiene media diferente; necesitas post-hoc para saber cuál
b) Las 4 áreas tienen exactamente la misma satisfacción promedio
c) Exactamente 3% de las áreas tienen satisfacción diferente
d) Todas las áreas son significativamente diferentes entre sí

---

### Pregunta 10 (8 puntos)
**¿Qué limitación tiene la prueba Chi-Cuadrada?**

a) No funciona con más de 2 variables categóricas simultáneamente
b) Te dice SI hay relación, pero NO qué tan fuerte ni en qué dirección
c) Solo funciona si ambas variables tienen exactamente 2 categorías
d) Te dice la dirección de la relación, pero no si es estadísticamente significativa

---

## 🟨 SECCIÓN 3: FUNCIONES PYTHON

### Pregunta 11 (6 puntos)
**¿Qué hace la función `df.describe()` en pandas?**

a) Muestra solo los primeros 5 registros del dataset
b) Calcula estadísticas descriptivas (media, std, min, max, cuartiles) de columnas numéricas
c) Describe el tipo de datos de cada columna sin calcular estadísticas
d) Calcula estadísticas descriptivas solo de la media y mediana

---

### Pregunta 12 (6 puntos)
**¿Para qué sirve `stats.ttest_ind(grupo1, grupo2)` en scipy?**

a) Compara las medias de dos grupos independientes (diferentes individuos)
b) Compara las medias del mismo grupo en dos momentos diferentes
c) Calcula la independencia estadística entre dos variables categóricas
d) Compara las medias de dos grupos pareados (mismos individuos)

---

### Pregunta 13 (6 puntos)
**¿Qué mide el estadístico Chi-cuadrado (χ²)?**

a) La diferencia entre las frecuencias observadas y las esperadas si no hubiera relación
b) La correlación lineal entre dos variables categóricas en una escala de -1 a 1
c) El porcentaje de casos que están en cada categoría de la tabla
d) La probabilidad de que dos variables categóricas sean independientes

---

### Pregunta 14 (6 puntos)
**¿Cuál es la diferencia entre `df['edad'].mean()` y `df['edad'].median()` en pandas?**

a) `.mean()` es afectado por outliers, `.median()` es resistente a outliers
b) `.mean()` solo funciona con datos simétricos, `.median()` con asimétricos
c) `.mean()` calcula el valor más frecuente, `.median()` el valor central
d) `.mean()` es resistente a outliers, `.median()` es afectado por outliers

---

### Pregunta 15 (6 puntos)
**¿Para qué usas `sns.boxplot(data=df, x='grupo', y='calificacion')` de seaborn?**

a) Para crear un gráfico de barras que muestra frecuencias por grupo
b) Para visualizar la distribución, mediana, cuartiles y outliers de una variable numérica por grupos
c) Para crear un heatmap que muestra correlaciones entre variables
d) Para visualizar la distribución y mediana de una variable, pero sin mostrar outliers

---

## 🟧 SECCIÓN 4: CORRELACIÓN Y REGRESIÓN LINEAL

### Pregunta 16 (5 puntos)
**Una ONG encuentra que r = 0.85 entre años de educación y salario. ¿Qué significa esto?**

a) Hay una correlación positiva fuerte; a mayor educación, mayor salario
b) La educación causa directamente el 85% del aumento en salario
c) El 85% de las personas con más educación tienen mayor salario
d) Hay una correlación negativa moderada entre educación y salario

---

### Pregunta 17 (5 puntos)
**Creaste un modelo de regresión lineal con R² = 0.45 prediciendo donaciones futuras basadas en años como donador. ¿Qué significa R²?**

a) El modelo predice correctamente el 45% de los donadores
b) Hay 45% de probabilidad de que el modelo sea estadísticamente significativo
c) El 45% de la variabilidad en donaciones futuras es explicada por años como donador
d) El modelo tiene 45% de error en sus predicciones

---

### Pregunta 18 (5 puntos)
**En un modelo de regresión lineal simple obtuviste: donacion = 100 + 50 × años. ¿Cómo interpretas el coeficiente 50?**

a) Por cada año adicional como donador, la donación aumenta en promedio $50
b) El 50% del incremento en donaciones se debe a los años como donador
c) Un donador con 50 años de antigüedad donará $100
d) La donación mínima es $50 independientemente de los años

---

## 🟥 SECCIÓN 5: CASOS DE CÓDIGO (Análisis Crítico)

### Pregunta 19 (5 puntos - CASO TRICKY)

**Contexto:** Una ONG quiere predecir el **monto de donación** basándose en la **satisfacción del donador**.

**Código usado:**
```python
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv('donadores.csv')
modelo = LinearRegression()

# Entrenar modelo
X = df[['monto_donacion']]  # Variable independiente
y = df['satisfaccion']       # Variable dependiente

modelo.fit(X, y)
print(f"R² = {modelo.score(X, y):.2f}")
```

**El código ejecuta sin errores y muestra R² = 0.68. ¿Cuál es el problema?**

a) Falta escalar las variables antes de ajustar el modelo
b) Las variables X e Y están invertidas; estamos prediciendo satisfacción en vez de monto
c) El modelo necesita incluir más variables independientes para ser válido
d) Debería usar regresión logística en lugar de regresión lineal

---

### Pregunta 20 (5 puntos - CASO TRICKY)

**Contexto:** Una ONG analiza si hay correlación entre **edad de beneficiarios** (18-80 años) y **nivel de participación** (escala 1-10).

**Código usado:**
```python
from scipy.stats import pearsonr
import pandas as pd

df = pd.read_csv('beneficiarios.csv')

# Calcular correlación
r, p_value = pearsonr(df['edad'], df['participacion'])

print(f"Correlación de Pearson: r = {r:.3f}")
print(f"p-value = {p_value:.4f}")

if p_value < 0.05:
    print("✓ Hay correlación significativa")
else:
    print("✗ No hay correlación significativa")
```

**Resultado:** `r = 0.12, p-value = 0.15`

**La ONG concluye:** *"No hay relación entre edad y participación"*

**Al graficar los datos, observas un patrón de U invertida (participación alta en jóvenes, baja en adultos medios, alta en adultos mayores). ¿Cuál es el problema principal?**

a) El tamaño de muestra es insuficiente para detectar la correlación
b) Pearson solo detecta relaciones lineales; aquí hay una relación no lineal (cuadrática)
c) El código debería usar correlación de Spearman en lugar de Pearson
d) El p-value > 0.05 significa que definitivamente no hay ninguna relación

---

---

## ✅ HOJA DE RESPUESTAS

| # | Respuesta Correcta |
|---|--------------------|
| 1 | c |
| 2 | b |
| 3 | b |
| 4 | b |
| 5 | c |
| 6 | b |
| 7 | b |
| 8 | b |
| 9 | a |
| 10 | b |
| 11 | b |
| 12 | a |
| 13 | a |
| 14 | a |
| 15 | b |
| 16 | a |
| 17 | c |
| 18 | a |
| 19 | b |
| 20 | b |

---

## 📊 JUSTIFICACIONES Y FEEDBACK

### Pregunta 1
**Respuesta correcta: c) Cuando hay valores extremos (outliers) que podrían sesgar el promedio**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (misconception): Cuando los datos son simétricos SIN outliers, la media es preferible
- **b)** INCORRECTO (misconception común): Para datos categóricos se usa la MODA, no mediana ni media
- **d)** INCORRECTO (similar pero error): Eso describe la MODA, no la mediana

---

### Pregunta 2
**Respuesta correcta: b) Hay evidencia suficiente para rechazar H₀ porque p < 0.05**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (misconception común): p-value NO es la probabilidad de que H₁ sea verdadera
- **c)** INCORRECTO (similar pero error): p = 0.042 SÍ es menor que 0.05, por lo que SÍ rechazamos H₀
- **d)** INCORRECTO (misconception): p-value no es la probabilidad de que H₀ sea verdadera

---

### Pregunta 3
**Respuesta correcta: b) La diferencia entre el cuartil 3 (75%) y el cuartil 1 (25%)**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (similar pero error): Eso describe el RANGO, no el IQR
- **c)** INCORRECTO (misconception): Usa cuartiles incorrectos; IQR = Q3 - Q1, no Q2 - Q1
- **d)** INCORRECTO (misconception): IQR no es un promedio, es una diferencia entre cuartiles

---

### Pregunta 4
**Respuesta correcta: b) No rechazamos H₀ porque p > 0.05, no hay evidencia suficiente**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (misconception común): p-value no mide "confianza en los datos"
- **c)** INCORRECTO (similar pero error): NO "aceptamos H₀", solo NO la rechazamos (diferencia clave)
- **d)** INCORRECTO (misconception): p-value no mide "magnitud del efecto"

---

### Pregunta 5
**Respuesta correcta: c) Prueba t pareada, porque se mide a las mismas personas en dos momentos**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (misconception): Aunque es un grupo, hay DOS mediciones (antes/después) en las mismas personas
- **b)** INCORRECTO (similar pero error): "Independiente" implica grupos diferentes; aquí son las MISMAS personas
- **d)** INCORRECTO (misconception): "Dos muestras" típicamente se refiere a prueba independiente, no pareada

---

### Pregunta 6
**Respuesta correcta: b) Cuando ambas variables son categóricas (género, región, programa)**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (similar pero error): Eso describe ANOVA, no Chi-Cuadrada
- **c)** INCORRECTO (misconception): Para variables numéricas correlacionadas usarías regresión o correlación de Pearson
- **d)** INCORRECTO (similar pero error): Eso describe prueba t de 1 muestra

---

### Pregunta 7
**Respuesta correcta: b) Hay relación significativa, las variables NO son independientes**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (misconception común): χ² alto + p-value bajo SÍ indica relación
- **c)** INCORRECTO (misconception): p-value no es un porcentaje de personas
- **d)** INCORRECTO (similar pero error): Si hay relación significativa, entonces NO son independientes

---

### Pregunta 8
**Respuesta correcta: b) Porque cada prueba t aumenta el riesgo de Error Tipo I (falsos positivos)**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (misconception): La velocidad no es la razón estadística principal
- **c)** INCORRECTO (similar pero error): ANOVA NO te dice cuáles son diferentes; necesitas post-hoc para eso
- **d)** INCORRECTO (misconception): Las pruebas t sí funcionan con 2 grupos, el problema es hacer MÚLTIPLES pruebas

---

### Pregunta 9
**Respuesta correcta: a) Al menos una área tiene media diferente; necesitas post-hoc para saber cuál**

**Por qué las otras son incorrectas:**
- **b)** INCORRECTO (misconception): p = 0.03 < 0.05, entonces SÍ hay diferencias
- **c)** INCORRECTO (misconception común): p-value no es un porcentaje de grupos
- **d)** INCORRECTO (similar pero error): ANOVA solo dice que "al menos una" es diferente, no que "todas" lo sean

---

### Pregunta 10
**Respuesta correcta: b) Te dice SI hay relación, pero NO qué tan fuerte ni en qué dirección**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (misconception): Chi-Cuadrada funciona con más de 2 variables (aunque la interpretación se complica)
- **c)** INCORRECTO (misconception): Funciona con cualquier número de categorías (2×3, 3×4, etc.)
- **d)** INCORRECTO (similar pero error): Al revés - SÍ te dice si es significativa, pero NO la dirección directamente

---

### Pregunta 11
**Respuesta correcta: b) Calcula estadísticas descriptivas (media, std, min, max, cuartiles) de columnas numéricas**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (similar pero error): Eso es `df.head()`, no `df.describe()`
- **c)** INCORRECTO (similar pero error): Eso es `df.info()`, no `df.describe()`
- **d)** INCORRECTO (misconception): `describe()` calcula MUCHAS más estadísticas (count, std, min, 25%, 50%, 75%, max)

---

### Pregunta 12
**Respuesta correcta: a) Compara las medias de dos grupos independientes (diferentes individuos)**

**Por qué las otras son incorrectas:**
- **b)** INCORRECTO (similar pero error): Eso es `ttest_rel()` (prueba pareada), no `ttest_ind()`
- **c)** INCORRECTO (misconception): Independencia de variables categóricas se mide con Chi-Cuadrada
- **d)** INCORRECTO (misconception): Grupos pareados usan `ttest_rel()`, no `ttest_ind()`

---

### Pregunta 13
**Respuesta correcta: a) La diferencia entre las frecuencias observadas y las esperadas si no hubiera relación**

**Por qué las otras son incorrectas:**
- **b)** INCORRECTO (misconception común): Chi-cuadrada NO mide correlación lineal; eso es para variables numéricas (Pearson). Chi-cuadrada trabaja con variables categóricas y no usa escala -1 a 1
- **c)** INCORRECTO (misconception): Chi-cuadrada NO calcula porcentajes simples; compara observado vs esperado para ver si hay diferencias significativas
- **d)** INCORRECTO (similar pero error): Esto describe el p-value, no el estadístico χ². El estadístico χ² mide qué tan grandes son las diferencias, el p-value te dice la probabilidad

---

### Pregunta 14
**Respuesta correcta: a) `.mean()` es afectado por outliers, `.median()` es resistente a outliers**

**Por qué las otras son incorrectas:**
- **b)** INCORRECTO (misconception): Ambas funcionan con cualquier distribución; la diferencia es la sensibilidad a outliers
- **c)** INCORRECTO (similar pero error): El valor más frecuente es la MODA (`.mode()`), no la media
- **d)** INCORRECTO (similar pero error): Al revés - la media SÍ es afectada, la mediana NO

---

### Pregunta 15
**Respuesta correcta: b) Para visualizar la distribución, mediana, cuartiles y outliers de una variable numérica por grupos**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (similar pero error): Eso es `sns.barplot()` o `sns.countplot()`, no `sns.boxplot()`
- **c)** INCORRECTO (misconception): Eso es `sns.heatmap()`, no `sns.boxplot()`
- **d)** INCORRECTO (similar pero error): El boxplot SÍ muestra outliers (puntos fuera de los bigotes)

---

### Pregunta 16
**Respuesta correcta: a) Hay una correlación positiva fuerte; a mayor educación, mayor salario**

**Por qué las otras son incorrectas:**
- **b)** INCORRECTO (misconception común): Correlación NO implica causalidad. r = 0.85 significa asociación fuerte, no que "causa el 85%"
- **c)** INCORRECTO (misconception): r = 0.85 no es un porcentaje de personas; es el coeficiente de correlación que mide la fuerza de la relación lineal
- **d)** INCORRECTO (error fundamental): r = 0.85 es POSITIVA (no negativa) y FUERTE (no moderada). Valores cercanos a 1 son correlación positiva fuerte

---

### Pregunta 17
**Respuesta correcta: c) El 45% de la variabilidad en donaciones futuras es explicada por años como donador**

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (misconception común): R² no es el porcentaje de predicciones correctas; es la proporción de varianza explicada
- **b)** INCORRECTO (misconception): R² no es una probabilidad de significancia; eso es el p-value
- **d)** INCORRECTO (similar pero error): R² no mide el error; mide qué porcentaje de la variabilidad es explicada por el modelo. El error sería 1 - R² = 55%

---

### Pregunta 18
**Respuesta correcta: a) Por cada año adicional como donador, la donación aumenta en promedio $50**

**Por qué las otras son incorrectas:**
- **b)** INCORRECTO (misconception): El coeficiente 50 no es un porcentaje; es la pendiente que indica cambio en Y por unidad de X
- **c)** INCORRECTO (error de cálculo): Un donador con 50 años donaría: 100 + 50×50 = $2,600, no $100
- **d)** INCORRECTO (confusión de términos): La donación mínima sería el intercepto ($100) cuando años = 0, no $50

---

### Pregunta 19 (CASO TRICKY)
**Respuesta correcta: b) Las variables X e Y están invertidas; estamos prediciendo satisfacción en vez de monto**

**Por qué esta pregunta es "tricky":**
- ✅ El código **SÍ ejecuta sin errores** (sintácticamente correcto)
- ✅ `LinearRegression()` acepta esta configuración
- ✅ Muestra un R² razonable (0.68)
- ❌ **PERO:** El objetivo era predecir **monto** usando **satisfacción**, no al revés
- 🎯 **Error conceptual:** Las variables están invertidas. Debería ser:
  ```python
  X = df[['satisfaccion']]      # Predictor
  y = df['monto_donacion']       # Variable a predecir
  ```

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO: LinearRegression no requiere escalado (no afecta los coeficientes en regresión lineal simple)
- **c)** INCORRECTO: El problema no es falta de variables; es que las variables están invertidas
- **d)** INCORRECTO: Ambas variables son continuas; regresión lineal es apropiada

**Lo que un LLM sin contexto diría:**
- "El código es sintácticamente correcto ✓"
- "fit() y score() están bien usados ✓"
- "Muestra resultados ✓"
- Pero **NO detectaría** que se está resolviendo el problema inverso

---

### Pregunta 20 (CASO TRICKY)
**Respuesta correcta: b) Pearson solo detecta relaciones lineales; aquí hay una relación no lineal (cuadrática)**

**Por qué esta pregunta es "tricky":**
- ✅ El código **SÍ ejecuta sin errores** (sintácticamente correcto)
- ✅ `pearsonr()` está bien usado
- ✅ La lógica del if/else es correcta
- ❌ **PERO:** Pearson r = 0.12 solo mide correlación **lineal**
- 🎯 **Error conceptual:** Cuando la relación es en forma de U (cuadrática), Pearson puede dar valores cercanos a 0 aunque SÍ haya relación fuerte

**Ejemplo del problema:**
- Participación alta en jóvenes (edad 20): 9/10
- Participación baja en adultos medios (edad 50): 3/10
- Participación alta en adultos mayores (edad 75): 8/10
- → Patrón de U invertida = Relación **no lineal**
- → Pearson r ≈ 0 porque no hay tendencia lineal ascendente/descendente

**Por qué las otras son incorrectas:**
- **a)** INCORRECTO (podría ser cierto, pero no es el problema PRINCIPAL): Con r = 0.12 y p = 0.15, el tamaño de muestra no es el issue central
- **c)** INCORRECTO (similar pero no resuelve el problema): Spearman detecta relaciones monótonas, pero aquí la relación es en U (no monótona)
- **d)** INCORRECTO (misconception crítico): p > 0.05 significa "no hay evidencia de correlación LINEAL", NO que no haya ninguna relación

**Lo que un LLM sin contexto diría:**
- "El código usa correctamente pearsonr() ✓"
- "La interpretación del p-value es correcta ✓"
- "La lógica estadística es válida ✓"
- Pero **NO detectaría** que Pearson es inapropiado para relaciones no lineales sin ver el gráfico

**Solución correcta:** Graficar primero (scatter plot) para detectar patrones no lineales, o usar regresión polinomial/splines

---

## 📈 Distribución de Puntos

| Sección | Preguntas | Puntos por Pregunta | Total |
|---------|-----------|---------------------|-------|
| Semana 1 (Descriptivos y Pruebas t) | 1-5 | 6 puntos | 30 pts |
| Semana 2 (Chi² y ANOVA) | 6-10 | 8 puntos | 40 pts |
| Python (Funciones) | 11-15 | 6 puntos | 30 pts |
| Correlación y Regresión | 16-18 | 5 puntos | 15 pts |
| Casos Tricky (Código) | 19-20 | 5 puntos | 10 pts |
| **TOTAL** | **20** | - | **125 pts** |

**Nota:** Quiz sobre 125 puntos totales. Se puede ajustar a escala de 100 si es necesario.

---

## 🎯 Temas Evaluados por Pregunta

1. **Medidas de Tendencia Central** (mediana vs media)
2. **Interpretación de p-value** (decisión estadística)
3. **Medidas de Dispersión** (IQR)
4. **Interpretación de p-value** (no rechazo de H₀)
5. **Tipos de pruebas t** (pareada vs independiente)
6. **Chi-Cuadrada** (cuándo usarla)
7. **Chi-Cuadrada** (interpretación de resultados)
8. **ANOVA** (por qué no múltiples pruebas t)
9. **ANOVA** (interpretación y post-hoc)
10. **Chi-Cuadrada** (limitaciones)
11. **Pandas** (df.describe)
12. **Scipy** (ttest_ind)
13. **Chi-Cuadrada** (qué mide el estadístico χ²)
14. **Pandas** (mean vs median)
15. **Seaborn** (boxplot)
16. **Correlación** (interpretación del coeficiente r, correlación ≠ causalidad)
17. **Regresión Lineal** (interpretación de R²)
18. **Regresión Lineal** (interpretación de coeficientes/pendiente)
19. **CASO TRICKY** (Variables invertidas en regresión - error conceptual)
20. **CASO TRICKY** (Correlación de Pearson con relación no lineal - limitación metodológica)

---

**Buena suerte en tu examen!** 🎓📊
