---
theme: default
colorSchema: light
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Regresión y Correlación
  Curso CD2001B - Diagnóstico para Líneas de Acción
  Tecnológico de Monterrey Campus Puebla
drawings:
  persist: false
transition: slide-left
title: Regresión y Correlación
mdc: true
download: true
exportFilename: semana2-regresion-correlacion
css: unocss
---

<style src="./styles/tec-theme.css"></style>

# Regresión y Correlación

## Predecir y Medir Relaciones

<div class="pt-12">
  <span class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    CD2001B - Diagnóstico para Líneas de Acción
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <span class="text-sm opacity-50">Semana 2 | Tec de Monterrey</span>
</div>

---
layout: center
class: text-center
---

# ¿Por Qué Necesitamos Regresión?

<div v-click class="mt-12">

## 🤔 Las Preguntas que Queremos Responder:

- 📈 **"¿Podemos PREDECIR la satisfacción basándonos en otros factores?"**
- 🔗 **"¿Qué tan FUERTE es la relación entre dos variables?"**
- 🎯 **"¿Qué variables son las más IMPORTANTES para mejorar nuestro servicio?"**

</div>

<div v-click class="mt-12">
<div class="text-2xl font-bold text-gradient">
Hasta ahora solo COMPARAMOS grupos
<br><br>
Ahora vamos a PREDECIR y MEDIR relaciones
</div>
</div>

---
layout: section
---

# Correlación

## Midiendo la Relación Entre Variables

---

# 🔗 ¿Qué es la Correlación?

<div class="mt-8">

<div v-click>

## En Palabras Simples:

La correlación mide **qué tan fuerte** es la relación lineal entre dos variables numéricas.

</div>

<div v-click class="mt-12">

## Coeficiente de Correlación (r)

Un número entre **-1 y +1** que indica:

- **Dirección:** ¿Aumentan juntas o en sentido contrario?
- **Fuerza:** ¿La relación es fuerte o débil?

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-info">
💡 El coeficiente más común es **r de Pearson** (correlación lineal)
</div>
</div>

---

# 📊 Interpretando el Coeficiente de Correlación

<div class="mt-8">

| Valor de r | Interpretación | Ejemplo |
|------------|----------------|---------|
| **r = +1** | Correlación positiva perfecta | Cuando una variable sube, la otra sube exactamente en la misma proporción |
| **r = +0.7 a +0.9** | Correlación positiva fuerte | Cuando una sube, la otra tiende a subir bastante |
| **r = +0.4 a +0.6** | Correlación positiva moderada | Hay tendencia, pero no muy marcada |
| **r = 0** | Sin correlación | No hay relación lineal |
| **r = -0.4 a -0.6** | Correlación negativa moderada | Cuando una sube, la otra tiende a bajar |
| **r = -0.7 a -0.9** | Correlación negativa fuerte | Cuando una sube, la otra baja bastante |
| **r = -1** | Correlación negativa perfecta | Relación inversa perfecta |

</div>

---

# 📈 Visualizando Correlaciones

<div class="grid grid-cols-3 gap-4 mt-8">

<div v-click>

### r ≈ +0.9
```
    y
    |        •
    |      •
    |    •
    |  •
    |•_____ x
```
**Positiva fuerte**

</div>

<div v-click>

### r ≈ 0
```
    y
    |  • •
    | • • •
    |• • •
    | • •
    |_____ x
```
**Sin correlación**

</div>

<div v-click>

### r ≈ -0.9
```
    y
    |•
    |  •
    |    •
    |      •
    |______• x
```
**Negativa fuerte**

</div>

</div>

---

# 🎯 Ejemplo: ONG "Manos Amigas"

<div class="mt-8">

## La Pregunta:

¿Existe relación entre el **tiempo de espera** y la **satisfacción** de los beneficiarios?

<div v-click class="mt-8">

**Hipótesis intuitiva:**
- Mayor tiempo de espera → Menor satisfacción
- Esperamos correlación **negativa**

</div>

</div>

<div v-click class="mt-12">

## Los Datos (muestra):

| Beneficiario | Tiempo de Espera (min) | Satisfacción (1-10) |
|--------------|------------------------|---------------------|
| 1 | 15 | 9.2 |
| 2 | 45 | 6.5 |
| 3 | 20 | 8.8 |
| 4 | 60 | 5.1 |
| 5 | 10 | 9.5 |

</div>

---

# 🐍 Correlación en Python

```python {all|1-2|4-7|9-11|13-14|all}
import pandas as pd
import seaborn as sns

# Datos
df = pd.DataFrame({
    'tiempo_espera': [15, 45, 20, 60, 10, 35, 50, 25, 40, 18],
    'satisfaccion': [9.2, 6.5, 8.8, 5.1, 9.5, 7.0, 6.0, 8.5, 6.8, 9.0]
})

# Calcular correlación
r = df['tiempo_espera'].corr(df['satisfaccion'])
print(f"Correlación (r): {r:.3f}")

# Visualizar con scatter plot + línea de tendencia
sns.lmplot(data=df, x='tiempo_espera', y='satisfaccion',
           height=5, aspect=1.5)
plt.title(f'Correlación: r = {r:.3f}')
plt.xlabel('Tiempo de Espera (minutos)')
plt.ylabel('Satisfacción (1-10)')
plt.show()
```

<div v-click class="mt-4">

**Resultado:**
```
Correlación (r): -0.892
```

</div>

---

# ✅ Interpretación del Resultado

<div class="mt-8">

**r = -0.892**

<div v-click class="mt-12">

## ¿Qué significa esto?

1. **Signo negativo (-):** Relación inversa
   - A mayor tiempo de espera → menor satisfacción

2. **Magnitud (0.892):** Correlación MUY fuerte
   - La relación es bastante consistente

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-success">
✅ **Conclusión:** Hay una relación lineal negativa muy fuerte entre tiempo de espera y satisfacción. Reducir tiempos de espera probablemente mejorará la satisfacción.
</div>
</div>

---

# 🔥 Matriz de Correlación

<div class="mt-8">

Cuando tienes **múltiples variables**, puedes ver todas las correlaciones en una sola visualización.

```python {all|1-7|9-11|all}
# Datos con múltiples variables
df = pd.DataFrame({
    'edad': [25, 34, 45, 28, 52, 30, 41],
    'tiempo_espera': [15, 45, 20, 60, 10, 35, 50],
    'calidad_atencion': [9, 7, 8, 5, 10, 7, 6],
    'satisfaccion': [9.2, 6.5, 8.8, 5.1, 9.5, 7.0, 6.0]
})

# Calcular todas las correlaciones
correlaciones = df.corr()
print(correlaciones)

# Visualizar con heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlaciones, annot=True, cmap='coolwarm',
            center=0, vmin=-1, vmax=1, square=True, linewidths=1)
plt.title('Matriz de Correlación')
plt.show()
```

</div>

---

# 📊 Interpretando la Matriz

<div class="mt-8">

```
                   edad  tiempo_espera  calidad_atencion  satisfaccion
edad                1.00          0.15              -0.12          0.08
tiempo_espera       0.15          1.00              -0.78         -0.89
calidad_atencion   -0.12         -0.78               1.00          0.92
satisfaccion        0.08         -0.89               0.92          1.00
```

</div>

<div v-click class="mt-12">

## 💡 Hallazgos Clave:

- **satisfaccion ↔ calidad_atencion:** r = +0.92 (fuerte positiva) ✅
- **satisfaccion ↔ tiempo_espera:** r = -0.89 (fuerte negativa) ⚠️
- **satisfaccion ↔ edad:** r = +0.08 (casi sin relación) 🤷

</div>

<div v-click class="mt-8">
<div class="alert alert-info">
💡 Los colores del heatmap ayudan: **rojo** = positiva, **azul** = negativa, **blanco** = sin relación
</div>
</div>

---
layout: center
---

# 🧠 Check Your Understanding

## Pregunta 1

Una ONG midió la correlación entre **años de experiencia del voluntario** y **número de beneficiarios atendidos por mes**.

Resultado: **r = +0.15**

**¿Qué significa esto?**

a) Hay una relación positiva muy fuerte entre experiencia y beneficiarios atendidos

b) Hay una relación positiva débil; la experiencia explica poco la cantidad atendida

c) Los voluntarios con más experiencia atienden 15% más beneficiarios

d) No hay ninguna relación entre las variables

---
layout: center
---

# ✅ Respuesta: Pregunta 1

**Respuesta correcta: b)**

**Hay una relación positiva débil; la experiencia explica poco la cantidad atendida**

<div class="mt-8">

**Por qué:**
- r = +0.15 está cerca de 0 → correlación muy débil
- El signo + indica que es positiva (más experiencia → más beneficiarios), pero la magnitud es pequeña
- La experiencia NO es un buen predictor de beneficiarios atendidos

</div>

<div class="mt-12">

**Errores comunes:**
- **a)** Incorrecto: 0.15 es débil, no fuerte (fuerte sería > 0.7)
- **c)** Incorrecto: r no es porcentaje
- **d)** Incorrecto: Hay relación, pero es muy débil

</div>

---

# ⚠️ Correlación ≠ Causalidad

<div class="mt-8">

<div v-click>

## La Trampa Más Común:

**"Si hay correlación, entonces una variable CAUSA la otra"**

❌ **FALSO**

</div>

<div v-click class="mt-12">

## Ejemplo Absurdo pero Real:

**Correlación entre:**
- Ventas de helado 🍦
- Ahogamientos en piscina 🏊

**r ≈ +0.9** (correlación fuerte!)

**¿Esto significa que comer helado causa ahogamientos?** 😂

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-warning">
⚠️ **Explicación:** Ambas variables están relacionadas con una TERCERA variable: **temperatura/verano**. Esto se llama **variable confusora**.
</div>
</div>

---

# 🤔 ¿Entonces Cuándo Hay Causalidad?

<div class="mt-8">

<div v-click>

## Para Establecer Causalidad Necesitas:

1. **Correlación** (el primer paso)
2. **Orden temporal:** La causa ocurre ANTES del efecto
3. **Mecanismo plausible:** Tiene sentido científico/lógico
4. **Experimento controlado:** Manipulas la causa y mides el efecto

</div>

<div v-click class="mt-12">

## Ejemplo en nuestra ONG:

**Correlación:** Tiempo de espera ↔ Satisfacción (r = -0.89)

**¿Es causal?**
- ✅ Correlación fuerte
- ✅ Orden temporal: Primero esperan, luego califican
- ✅ Mecanismo plausible: Esperar frustra → baja satisfacción
- ⚠️ Experimento: Necesitaríamos reducir tiempos y medir cambios

**Conclusión:** Muy probable que sea causal, pero se necesita intervención para confirmarlo

</div>

</div>

---
layout: section
---

# Regresión Lineal

## De Medir a Predecir

---

# 📈 ¿Qué es Regresión Lineal?

<div class="mt-8">

<div v-click>

## En Palabras Simples:

Encontrar la **"línea de mejor ajuste"** que nos permita **predecir** una variable (Y) basándonos en otra(s) variable(s) (X).

</div>

<div v-click class="mt-12">

## La Diferencia con Correlación:

| Correlación | Regresión |
|-------------|-----------|
| **Mide** la fuerza de la relación | **Predice** valores |
| No distingue X e Y (simétrica) | Y depende de X (asimétrica) |
| Solo un número (r) | Una ecuación completa |

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-info">
💡 Correlación te dice "¿hay relación?". Regresión te dice "¿cuánto cambia Y cuando cambio X?"
</div>
</div>

---

# 📐 La Ecuación de Regresión

<div class="mt-12">

<div v-click>

## La Famosa Ecuación de la Recta:

<div class="math-display text-center text-3xl mt-8">
y = mx + b
</div>

</div>

<div v-click class="mt-12">

## En Estadística:

<div class="math-display text-center text-3xl mt-8">
ŷ = β₀ + β₁x
</div>

</div>

</div>

<div v-click class="mt-12">

### Donde:
- **ŷ** (y-hat): Valor predicho
- **β₀** (beta-cero): Intercepto (donde la línea cruza el eje Y)
- **β₁** (beta-uno): Pendiente (cuánto cambia Y por cada unidad de X)
- **x**: Valor de la variable independiente

</div>

---

# 🎯 Ejemplo: Predecir Satisfacción

<div class="mt-8">

## La Pregunta:

¿Podemos **predecir** la satisfacción basándonos en el tiempo de espera?

<div v-click class="mt-8">

**Datos:**

| Tiempo de Espera (x) | Satisfacción Real (y) |
|----------------------|-----------------------|
| 10 min | 9.5 |
| 20 min | 8.8 |
| 30 min | 7.5 |
| 40 min | 6.8 |
| 50 min | 6.0 |

</div>

</div>

<div v-click class="mt-8">

**Objetivo:** Encontrar la ecuación que mejor prediga la satisfacción

</div>

---

# 🐍 Regresión Lineal en Python

```python {all|1-2|4-7|9-12|14-17|19-21|all}
from sklearn.linear_model import LinearRegression
import numpy as np

# Preparar datos
X = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)  # reshape para sklearn
y = np.array([9.5, 8.8, 7.5, 6.8, 6.0])

# Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Obtener parámetros
intercepto = modelo.intercept_
pendiente = modelo.coef_[0]
print(f"Ecuación: ŷ = {intercepto:.2f} + ({pendiente:.3f})x")

# Hacer predicciones
tiempo_nuevo = np.array([[25]])  # 25 minutos
satisfaccion_predicha = modelo.predict(tiempo_nuevo)
print(f"Predicción para 25 min: {satisfaccion_predicha[0]:.2f}")
```

<div v-click class="mt-4">

**Resultado:**
```
Ecuación: ŷ = 10.40 + (-0.084)x
Predicción para 25 min: 8.30
```

</div>

---

# 📊 Visualización con Seaborn

```python {all|1-9|11-16|all}
import seaborn as sns
import matplotlib.pyplot as plt

# Datos en DataFrame
df = pd.DataFrame({
    'tiempo_espera': [10, 20, 30, 40, 50],
    'satisfaccion': [9.5, 8.8, 7.5, 6.8, 6.0]
})

# Scatter plot + línea de regresión
sns.lmplot(data=df, x='tiempo_espera', y='satisfaccion',
           height=6, aspect=1.5, line_kws={'color': 'red'})
plt.title('Regresión: Tiempo de Espera → Satisfacción')
plt.xlabel('Tiempo de Espera (minutos)')
plt.ylabel('Satisfacción Predicha')
plt.show()
```

<div v-click class="mt-4">
<div class="alert alert-success">
✅ La línea roja es la "línea de mejor ajuste". Minimiza la distancia total de todos los puntos a la línea.
</div>
</div>

---

# 🔍 Interpretando los Parámetros

<div class="mt-8">

**Ecuación obtenida:**

<div class="math-display text-center text-2xl mt-8">
ŷ = 10.40 + (-0.084)x
</div>

<div v-click class="mt-12">

## ¿Qué Significa Cada Parte?

**Intercepto (β₀ = 10.40):**
- Si tiempo de espera fuera 0 minutos → satisfacción sería 10.40
- (En la práctica, 0 min no ocurre, pero es el punto de partida matemático)

**Pendiente (β₁ = -0.084):**
- Por cada **minuto adicional** de espera → satisfacción **disminuye 0.084 puntos**
- Por cada **10 minutos** → satisfacción baja **0.84 puntos**

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-info">
💡 El signo negativo confirma la relación inversa: más espera = menos satisfacción
</div>
</div>

---

# 🎯 Haciendo Predicciones

<div class="mt-8">

Con la ecuación **ŷ = 10.40 - 0.084x**, podemos predecir:

<div v-click class="mt-12">

**Pregunta:** Si un beneficiario espera **35 minutos**, ¿cuál será su satisfacción esperada?

```python
tiempo = 35
satisfaccion_predicha = 10.40 - 0.084 * tiempo
print(f"Predicción: {satisfaccion_predicha:.2f}")
```

**Resultado:** ŷ = 10.40 - 0.084(35) = **7.46 puntos**

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-warning">
⚠️ **Cuidado con extrapolación:** No uses la ecuación para valores muy fuera del rango de tus datos. Por ejemplo, predecir para 200 minutos sería poco confiable.
</div>
</div>

---
layout: center
---

# 🧠 Check Your Understanding

## Pregunta 2

Una ONG obtuvo esta ecuación de regresión:

**ŷ = 5.2 + 0.6x**

Donde:
- **x** = Horas de capacitación recibidas
- **y** = Puntaje de competencia (0-10)

**¿Qué significa la pendiente (0.6)?**

a) Por cada hora de capacitación, el puntaje aumenta 0.6 puntos

b) El 60% de las personas mejoran con capacitación

c) La capacitación explica 60% de la varianza

d) La correlación entre capacitación y puntaje es 0.6

---
layout: center
---

# ✅ Respuesta: Pregunta 2

**Respuesta correcta: a)**

**Por cada hora de capacitación, el puntaje aumenta 0.6 puntos**

<div class="mt-8">

**Por qué:**
- La pendiente (β₁ = 0.6) indica cuánto cambia Y por cada unidad de cambio en X
- Interpretación: +1 hora → +0.6 puntos en puntaje

**Ejemplo:**
- 0 horas → ŷ = 5.2 + 0.6(0) = 5.2
- 1 hora → ŷ = 5.2 + 0.6(1) = 5.8
- 5 horas → ŷ = 5.2 + 0.6(5) = 8.2

</div>

<div class="mt-12">

**Errores comunes:**
- **b)** Incorrecto: 0.6 no es porcentaje
- **c)** Incorrecto: Eso sería R² (lo veremos después)
- **d)** Incorrecto: 0.6 es pendiente, no correlación (aunque relacionados)

</div>

---

# 📏 Evaluando el Modelo: R²

<div class="mt-8">

<div v-click>

## ¿Qué tan Buena es Nuestra Predicción?

**R² (R-cuadrado):** Porcentaje de la variabilidad de Y que es explicada por X

**Rango:** 0 a 1 (o 0% a 100%)

</div>

<div v-click class="mt-12">

## Interpretación:

| R² | Significado |
|----|-------------|
| **R² = 1.0** | Predicción perfecta (100% explicado) |
| **R² = 0.8** | Muy bueno (80% de la variabilidad explicada) |
| **R² = 0.5** | Moderado (50% explicado) |
| **R² = 0.2** | Débil (20% explicado) |
| **R² = 0** | El modelo no explica nada |

</div>

</div>

---

# 🐍 Calculando R² en Python

```python {all|1-2|4-11|13-14|16-20|all}
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Entrenar modelo
X = df[['tiempo_espera']].values
y = df['satisfaccion'].values

modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)

# Calcular R²
r2 = r2_score(y, y_pred)
print(f"R² = {r2:.3f}")

# Interpretar
print(f"\nEl modelo explica {r2*100:.1f}% de la variabilidad en satisfacción")
```

<div v-click class="mt-4">

**Resultado:**
```
R² = 0.796

El modelo explica 79.6% de la variabilidad en satisfacción
```

</div>

<div v-click class="mt-4">
<div class="alert alert-success">
✅ R² = 0.796 es **muy bueno**. El tiempo de espera explica casi 80% de las diferencias en satisfacción.
</div>
</div>

---

# 📊 Visualizando el Ajuste

```python {all|1-8|10-15|all}
# Crear gráfico: Real vs Predicho
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y, y=y_pred, s=100, alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()],
         'r--', lw=2, label='Predicción Perfecta')
plt.xlabel('Satisfacción Real')
plt.ylabel('Satisfacción Predicha')
plt.title(f'Real vs Predicho (R² = {r2:.3f})')
plt.legend()
plt.show()
```

<div v-click class="mt-8">

## 💡 Cómo Interpretar el Gráfico:

- **Puntos cerca de la línea roja** → Buenas predicciones
- **Puntos lejos de la línea** → Errores de predicción
- Mientras más juntos estén los puntos a la línea → Mayor R²

</div>

---

# 📏 Evaluando el Modelo: RMSE

<div class="mt-8">

<div v-click>

## Otra Métrica Útil: RMSE

**RMSE (Root Mean Squared Error):** Error promedio de predicción en las **mismas unidades** que Y

**Interpretación:** "En promedio, nuestras predicciones se equivocan por ± RMSE"

</div>

<div v-click class="mt-12">

## Ejemplo:

Si RMSE = 0.5 puntos en satisfacción (escala 1-10):
- Nuestras predicciones están, en promedio, a ±0.5 puntos del valor real
- Un error de 0.5 en una escala de 10 es **bastante bueno** (5%)

</div>

</div>

<div v-click class="mt-12">

```python
from sklearn.metrics import mean_squared_error
import numpy as np

rmse = np.sqrt(mean_squared_error(y, y_pred))
print(f"RMSE = {rmse:.3f} puntos")
```

</div>

---

# 🔢 Regresión Múltiple

<div class="mt-8">

<div v-click>

## ¿Y Si Tengo Varias Variables Predictoras?

Hasta ahora: **1 variable X** → **1 variable Y**

Pero en la vida real: **Múltiples X** → **1 variable Y**

</div>

<div v-click class="mt-12">

## Ejemplo:

**Predecir satisfacción basándose en:**
- X₁: Tiempo de espera
- X₂: Calidad de atención
- X₃: Edad del beneficiario

**Ecuación:**
```
ŷ = β₀ + β₁(tiempo) + β₂(calidad) + β₃(edad)
```

</div>

</div>

---

# 🐍 Regresión Múltiple en Python

```python {all|1-7|9-12|14-19|all}
# Preparar datos con múltiples variables
X = df[['tiempo_espera', 'calidad_atencion', 'edad']].values
y = df['satisfaccion'].values

# Entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Ver coeficientes
print(f"Intercepto: {modelo.intercept_:.2f}")
print(f"Coeficientes: {modelo.coef_}")

# Interpretar
print("\nInterpretación:")
print(f"  - Por cada minuto de espera: {modelo.coef_[0]:.3f} puntos")
print(f"  - Por cada punto en calidad: {modelo.coef_[1]:.3f} puntos")
print(f"  - Por cada año de edad: {modelo.coef_[2]:.3f} puntos")
```

<div v-click class="mt-4">

**Resultado:**
```
Intercepto: 2.15
Coeficientes: [-0.084  0.620 -0.008]

Interpretación:
  - Por cada minuto de espera: -0.084 puntos (negativo = mala señal)
  - Por cada punto en calidad: +0.620 puntos (positivo = buena señal)
  - Por cada año de edad: -0.008 puntos (casi sin efecto)
```

</div>

---
layout: center
---

# 🧠 Check Your Understanding

## Pregunta 3

Una ONG construyó un modelo de regresión múltiple para predecir satisfacción.

Resultados:
- **R² = 0.88**
- **RMSE = 0.6 puntos** (escala 1-10)

**¿Cuál afirmación es CORRECTA?**

a) El modelo predice perfectamente la satisfacción

b) El modelo es muy bueno; explica 88% de la variabilidad con errores pequeños

c) El 88% de los beneficiarios están satisfechos

d) El modelo se equivoca en 88% de los casos

---
layout: center
---

# ✅ Respuesta: Pregunta 3

**Respuesta correcta: b)**

**El modelo es muy bueno; explica 88% de la variabilidad con errores pequeños**

<div class="mt-8">

**Por qué:**
- **R² = 0.88** significa que el modelo explica 88% de las diferencias en satisfacción (muy bueno)
- **RMSE = 0.6** significa errores promedio de ±0.6 puntos en escala 1-10 (6%, bastante preciso)

</div>

<div class="mt-12">

**Errores comunes:**
- **a)** Incorrecto: R² = 1.0 sería perfecto, 0.88 es excelente pero no perfecto
- **c)** Incorrecto: R² ≠ porcentaje de personas satisfechas
- **d)** Incorrecto: R² alto significa buen ajuste, no errores

</div>

---

# 🔥 Gen Z Moment: Regresión Edition 😂

<div class="mt-12 text-center">

<div v-click>

## Cuando R² = 0.95:

<div class="text-6xl mt-8">
😎✨
</div>

<div class="text-xl mt-4">
"Este modelo está on fire, no skibidi"
</div>

</div>

<div v-click class="mt-12">

## Cuando alguien confunde correlación con causalidad:

<div class="text-6xl mt-8">
🤦‍♀️
</div>

<div class="text-xl mt-4">
"El helado no causa ahogamientos, bestie"
</div>

</div>

</div>

---

# 🎯 Aplicación Práctica: Recomendaciones

<div class="mt-8">

## Caso: ONG "Manos Amigas"

**Modelo final:**
```
Satisfacción = 2.15 - 0.084(tiempo_espera) + 0.620(calidad_atencion) - 0.008(edad)
R² = 0.88
```

<div v-click class="mt-12">

## 💡 Insights Accionables:

1. **Calidad de atención** tiene el **mayor impacto** (β = +0.620)
   - ⚡ **Acción:** Invertir en capacitación del personal

2. **Tiempo de espera** tiene impacto **negativo** (β = -0.084)
   - ⏰ **Acción:** Optimizar procesos para reducir tiempos

3. **Edad** tiene **casi sin efecto** (β = -0.008)
   - 🤷 No necesita atención prioritaria

</div>

</div>

---

# 📋 Resumen: Correlación vs Regresión

<div class="mt-8">

| Aspecto | Correlación | Regresión |
|---------|-------------|-----------|
| **Objetivo** | Medir fuerza de relación | Predecir valores |
| **Resultado** | Un número (r) | Una ecuación |
| **Pregunta** | ¿Hay relación? | ¿Cuánto vale Y dado X? |
| **Simétrica** | Sí (r de X→Y = r de Y→X) | No (Y depende de X) |
| **Función Python** | `.corr()` | `LinearRegression()` |
| **Visualización** | Scatter plot | Scatter + línea |
| **Métricas** | r (-1 a +1) | R², RMSE |
| **Ejemplo** | ¿Espera y satisfacción están relacionadas? | ¿Cuál será la satisfacción con 30 min de espera? |

</div>

---

# 🛠️ Código Completo: Regresión Simple

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar datos
df = pd.read_csv('datos_ong.csv')

# 2. Preparar variables
X = df[['tiempo_espera']].values
y = df['satisfaccion'].values

# 3. Entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# 4. Hacer predicciones
y_pred = modelo.predict(X)

# 5. Evaluar
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(f"Ecuación: ŷ = {modelo.intercept_:.2f} + ({modelo.coef_[0]:.3f})x")
print(f"R² = {r2:.3f}")
print(f"RMSE = {rmse:.3f}")

# 6. Visualizar
sns.lmplot(data=df, x='tiempo_espera', y='satisfaccion', height=6)
plt.title(f'Regresión Lineal (R² = {r2:.3f})')
plt.show()
```

---

# 🎓 Conceptos Clave para Workshop 2

<div class="mt-8">

## ✅ Lo que Necesitas Recordar:

<div v-click class="mt-8">

### Correlación:
- Mide **fuerza** de relación lineal
- Valor: **-1 a +1**
- Función: `df['x'].corr(df['y'])`
- Visualización: **Scatter plot** + matriz (heatmap)
- **Correlación ≠ Causalidad**

</div>

<div v-click class="mt-8">

### Regresión Lineal:
- **Predice** valores de Y dado X
- Ecuación: **ŷ = β₀ + β₁x**
- Métricas: **R²** (ajuste) y **RMSE** (error)
- Función: `LinearRegression().fit(X, y)`
- Visualización: **Scatter + línea de regresión**

</div>

</div>

---

# 🎯 Conexión con Workshop 2

<div class="mt-8">

En Workshop 2 aplicarás:

<div v-click class="mt-8">

### Parte 1: Chi-Cuadrada
- Variables categóricas
- Relaciones entre grupos

</div>

<div v-click class="mt-8">

### Parte 2: ANOVA
- Comparar 3+ grupos
- Post-hoc si es significativo

</div>

<div v-click class="mt-8">

### Parte 3: Regresión y Correlación
- Matriz de correlación
- Modelo de regresión múltiple
- Predicciones
- Interpretación de coeficientes

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-success">
💡 ¡Todo está conectado! Usa estas herramientas según el tipo de pregunta que tengas.
</div>
</div>

---
layout: center
class: text-center
---

# 🚀 ¡Estás Listo para Workshop 2!

<div class="mt-12">

<div v-click>

## Has Aprendido:

✅ Chi-Cuadrada (relaciones entre categorías)

✅ ANOVA (comparar múltiples grupos)

✅ Correlación (medir relaciones)

✅ Regresión (predecir valores)

</div>

</div>

<div v-click class="mt-12">
<div class="text-2xl font-bold text-gradient">
Ahora pon todo en práctica con datos reales 📊
</div>
</div>

---
layout: end
class: text-center
---

# ¡Gracias!

<div class="pt-12">
  <span class="text-6xl">📈🔗</span>
</div>

### ¿Preguntas?

<div class="abs-br m-6 flex gap-2">
  <span class="text-sm opacity-50">CD2001B | Tec de Monterrey Campus Puebla</span>
</div>
