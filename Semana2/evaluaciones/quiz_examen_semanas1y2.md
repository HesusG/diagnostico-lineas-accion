# 📝 Quiz: Semanas 1 y 2 - Análisis Estadístico

**Curso:** CD2001B - Diagnóstico para Líneas de Acción
**Tec de Monterrey - Campus Puebla**

---

## 📋 Instrucciones

- **Total de preguntas:** 15 (valor: 100 puntos)
- **Formato:** Opción múltiple (4 opciones por pregunta)
- **Secciones:**
  - Preguntas 1-5: Semana 1 (Medidas Descriptivas y Pruebas de Hipótesis)
  - Preguntas 6-10: Semana 2 (Chi-Cuadrada y ANOVA)
  - Preguntas 11-15: Funciones Python

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

## 📈 Distribución de Puntos

| Sección | Preguntas | Puntos por Pregunta | Total |
|---------|-----------|---------------------|-------|
| Semana 1 | 1-5 | 6 puntos | 30 pts |
| Semana 2 | 6-10 | 8 puntos | 40 pts |
| Python | 11-15 | 6 puntos | 30 pts |
| **TOTAL** | **15** | - | **100 pts** |

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

---

**Buena suerte en tu examen!** 🎓📊
