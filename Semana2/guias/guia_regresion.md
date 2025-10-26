# Guía: Regresión Lineal y Correlación

## 🎯 ¿Qué es Regresión Lineal?

La **regresión lineal** es un método estadístico para modelar la **relación** entre una variable dependiente (Y) y una o más variables independientes (X).

**Objetivo:** Predecir el valor de Y basándose en X.

**Ejemplo de negocio:**
> ¿Podemos predecir la satisfacción del cliente basándonos en el tiempo de espera?

---

## 📋 Regresión Lineal Simple vs Múltiple

### Regresión Lineal Simple
Una variable independiente (X) predice una variable dependiente (Y).

**Ecuación:**
```
Y = β₀ + β₁X + ε
```

Donde:
- **Y:** Variable dependiente (satisfacción)
- **X:** Variable independiente (tiempo de espera)
- **β₀:** Intercepto (valor de Y cuando X=0)
- **β₁:** Pendiente (cambio en Y por cada unidad de X)
- **ε:** Error (residuo)

### Regresión Lineal Múltiple
Múltiples variables independientes predicen Y.

**Ecuación:**
```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε
```

---

## 📊 Correlación de Pearson

Antes de hacer regresión, es útil calcular la **correlación** para ver qué tan fuerte es la relación lineal.

### Coeficiente de Correlación (r)

**Rango:** -1 a +1

- **r = +1:** Correlación positiva perfecta
- **r = 0:** Sin correlación lineal
- **r = -1:** Correlación negativa perfecta

**Interpretación:**
- |r| < 0.3: Débil
- 0.3 ≤ |r| < 0.7: Moderada
- |r| ≥ 0.7: Fuerte

### Calcular en Python

```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv('datos_satisfaccion.csv')

# Correlación de Pearson
r, p_value = stats.pearsonr(df['tiempo_espera'], df['satisfaccion'])

print(f"Coeficiente de correlación (r): {r:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("✗ La correlación es estadísticamente significativa")
else:
    print("✓ No hay correlación significativa")
```

### Scatter Plot

```python
plt.figure(figsize=(10, 6))
plt.scatter(df['tiempo_espera'], df['satisfaccion'], alpha=0.6, edgecolor='black')
plt.xlabel('Tiempo de Espera (minutos)', fontsize=12)
plt.ylabel('Satisfacción (1-10)', fontsize=12)
plt.title(f'Relación: Tiempo de Espera vs Satisfacción (r={r:.3f})', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 💻 Regresión Lineal Simple en Python

### Opción 1: Usando scipy

```python
from scipy import stats

# Variables
X = df['tiempo_espera']
Y = df['satisfaccion']

# Regresión lineal
pendiente, intercepto, r_value, p_value, std_err = stats.linregress(X, Y)

print("="*60)
print("REGRESIÓN LINEAL SIMPLE")
print("="*60)
print(f"Ecuación: Y = {intercepto:.4f} + ({pendiente:.4f})X")
print(f"R² = {r_value**2:.4f}")
print(f"p-value = {p_value:.4f}")
print(f"Error estándar = {std_err:.4f}")
```

### Opción 2: Usando statsmodels (más completo)

```python
import statsmodels.api as sm

# Preparar datos
X = df['tiempo_espera']
X = sm.add_constant(X)  # Añadir intercepto
Y = df['satisfaccion']

# Ajustar modelo
modelo = sm.OLS(Y, X).fit()

# Resumen completo
print(modelo.summary())
```

**Interpretación del summary:**
- **R-squared:** Proporción de varianza explicada
- **coef:** Coeficientes (β₀ y β₁)
- **P>|t|:** p-value de cada coeficiente
- **[0.025  0.975]:** Intervalo de confianza 95%

---

## 📈 Visualización de la Regresión

### Línea de Regresión

```python
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.regplot(x='tiempo_espera', y='satisfaccion', data=df,
            scatter_kws={'alpha':0.5, 'edgecolor':'black'},
            line_kws={'color':'red', 'linewidth':2})

plt.xlabel('Tiempo de Espera (minutos)', fontsize=12)
plt.ylabel('Satisfacción (1-10)', fontsize=12)
plt.title('Regresión Lineal: Tiempo de Espera vs Satisfacción', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Predicciones vs Valores Reales

```python
# Hacer predicciones
predicciones = intercepto + pendiente * df['tiempo_espera']

plt.figure(figsize=(10, 6))
plt.scatter(df['satisfaccion'], predicciones, alpha=0.6, edgecolor='black')
plt.plot([df['satisfaccion'].min(), df['satisfaccion'].max()],
         [df['satisfaccion'].min(), df['satisfaccion'].max()],
         'r--', linewidth=2, label='Predicción perfecta')
plt.xlabel('Satisfacción Real', fontsize=12)
plt.ylabel('Satisfacción Predicha', fontsize=12)
plt.title('Valores Reales vs Predicciones', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## 🔍 Interpretación de Resultados

### Ejemplo de Output:

```
Ecuación: Y = 10.2345 + (-0.0856)X
R² = 0.6234
p-value < 0.001
```

**Interpretación en contexto de negocio:**

1. **Intercepto (β₀ = 10.23):**
   > Cuando el tiempo de espera es 0 minutos, la satisfacción esperada es 10.23 (teórico)

2. **Pendiente (β₁ = -0.0856):**
   > Por cada minuto adicional de espera, la satisfacción disminuye 0.086 puntos
   > Si el tiempo de espera aumenta de 20 a 30 minutos, la satisfacción baja ~0.86 puntos

3. **R² = 0.6234:**
   > El 62.34% de la variabilidad en satisfacción se explica por el tiempo de espera
   > El 37.66% restante se debe a otros factores no medidos

4. **p-value < 0.001:**
   > La relación es estadísticamente significativa

---

## 📊 R² (Coeficiente de Determinación)

**R²** indica qué proporción de la varianza en Y es explicada por X.

**Interpretación:**
- R² = 0: X no explica nada de Y
- R² = 1: X explica perfectamente Y

**Valores típicos:**
- Ciencias sociales: R² > 0.3 es aceptable
- Ciencias exactas: R² > 0.7 es deseable

### R² Ajustado

Para regresión múltiple, usar **R² ajustado** que penaliza agregar variables innecesarias.

```python
from sklearn.metrics import r2_score

# R² ajustado
n = len(df)  # Número de observaciones
k = 1        # Número de predictores

r2 = r_value**2
r2_ajustado = 1 - ((1 - r2) * (n - 1) / (n - k - 1))

print(f"R² = {r2:.4f}")
print(f"R² ajustado = {r2_ajustado:.4f}")
```

---

## ⚙️ Supuestos de la Regresión Lineal

### 1. Linealidad
La relación entre X e Y es lineal.

**Verificación:** Scatter plot debe mostrar tendencia lineal

### 2. Independencia de Residuos
Los residuos no están correlacionados.

**Verificación:** Gráfico de residuos vs orden temporal

### 3. Homocedasticidad
La varianza de los residuos es constante.

**Verificación:** Gráfico de residuos vs valores ajustados

```python
# Calcular residuos
residuos = df['satisfaccion'] - predicciones

plt.figure(figsize=(10, 6))
plt.scatter(predicciones, residuos, alpha=0.6, edgecolor='black')
plt.axhline(y=0, color='red', linestyle='--', linewidth=2)
plt.xlabel('Valores Ajustados', fontsize=12)
plt.ylabel('Residuos', fontsize=12)
plt.title('Gráfico de Residuos', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

**Patrón ideal:** Puntos dispersos aleatoriamente alrededor de 0

### 4. Normalidad de Residuos
Los residuos siguen distribución normal.

**Verificación:** Q-Q plot

```python
from scipy import stats

stats.probplot(residuos, dist="norm", plot=plt)
plt.title('Q-Q Plot de Residuos', fontsize=14, fontweight='bold')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### 5. No Multicolinealidad (para regresión múltiple)
Las variables independientes no están altamente correlacionadas entre sí.

---

## 🎯 Regresión Lineal Múltiple

### Ejemplo: Predecir Satisfacción con Múltiples Variables

```python
import statsmodels.api as sm

# Seleccionar variables predictoras
X = df[['tiempo_espera', 'calidad_atencion', 'tiempo_servicio']]
X = sm.add_constant(X)  # Añadir intercepto
Y = df['satisfaccion']

# Ajustar modelo
modelo_multiple = sm.OLS(Y, X).fit()

# Resumen
print(modelo_multiple.summary())

# Ecuación resultante
print("\nEcuación de Regresión:")
print(f"Satisfacción = {modelo_multiple.params['const']:.4f}")
for var in ['tiempo_espera', 'calidad_atencion', 'tiempo_servicio']:
    signo = '+' if modelo_multiple.params[var] >= 0 else ''
    print(f"            {signo}{modelo_multiple.params[var]:.4f} * {var}")
```

**Interpretación de coeficientes en regresión múltiple:**

```
β₁ = -0.05 (tiempo_espera)
```
> Manteniendo constantes calidad_atencion y tiempo_servicio, un minuto adicional de espera reduce la satisfacción en 0.05 puntos.

---

## 🔮 Hacer Predicciones

### Predicción para Nuevos Datos

```python
# Datos de un nuevo cliente
nuevo_tiempo_espera = 25  # minutos

# Predicción
satisfaccion_predicha = intercepto + pendiente * nuevo_tiempo_espera

print(f"Si el tiempo de espera es {nuevo_tiempo_espera} minutos:")
print(f"  Satisfacción predicha: {satisfaccion_predicha:.2f}")

# Intervalo de confianza (más complejo, usar statsmodels)
X_nuevo = sm.add_constant([nuevo_tiempo_espera])
prediccion = modelo.predict(X_nuevo)
print(f"  Predicción (statsmodels): {prediccion[0]:.2f}")
```

---

## 📉 Errores Comunes y Soluciones

### Error 1: Extrapolar Más Allá del Rango de Datos

**Problema:** Predecir para X fuera del rango observado

```python
print(f"Rango de tiempo_espera: {df['tiempo_espera'].min()} - {df['tiempo_espera'].max()}")

# ❌ MAL: Predecir para tiempo_espera = 100 (fuera del rango)
# ✅ BIEN: Solo predecir dentro del rango observado
```

### Error 2: Asumir Causalidad

**Recuerda:** Correlación ≠ Causalidad

Aunque tiempo de espera y satisfacción estén correlacionados, no significa que uno **cause** el otro. Puede haber variables confusoras.

### Error 3: Ignorar Outliers

```python
# Identificar outliers usando distancia de Cook
from statsmodels.stats.outliers_influence import OLSInfluence

influence = OLSInfluence(modelo)
cooks_d = influence.cooks_distance[0]

# Puntos con Cook's D > 1 son influyentes
outliers_idx = np.where(cooks_d > 1)[0]
print(f"Outliers influyentes: {outliers_idx}")
```

---

## 💡 Ejemplo Completo: Análisis de ONG

```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Cargar datos
df = pd.read_csv('ejemplo_satisfaccion_clientes.csv')

print("="*70)
print("ANÁLISIS DE REGRESIÓN: TIEMPO DE ESPERA → SATISFACCIÓN")
print("="*70)

# Paso 1: Correlación
r, p_cor = stats.pearsonr(df['tiempo_espera'], df['satisfaccion'])
print(f"\n1. CORRELACIÓN")
print(f"   r = {r:.4f}")
print(f"   p-value = {p_cor:.4f}")

if abs(r) < 0.3:
    fuerza = "débil"
elif abs(r) < 0.7:
    fuerza = "moderada"
else:
    fuerza = "fuerte"

direccion = "negativa" if r < 0 else "positiva"
print(f"   Correlación {fuerza} {direccion}")

# Paso 2: Regresión Lineal Simple
X = sm.add_constant(df['tiempo_espera'])
Y = df['satisfaccion']
modelo = sm.OLS(Y, X).fit()

print(f"\n2. REGRESIÓN LINEAL")
print(f"   Ecuación: Y = {modelo.params['const']:.4f} + ({modelo.params['tiempo_espera']:.4f})X")
print(f"   R² = {modelo.rsquared:.4f}")
print(f"   R² ajustado = {modelo.rsquared_adj:.4f}")
print(f"   p-value = {modelo.f_pvalue:.4f}")

# Interpretación
print(f"\n3. INTERPRETACIÓN")
print(f"   • El {modelo.rsquared*100:.1f}% de la varianza en satisfacción se explica por tiempo de espera")
print(f"   • Por cada minuto adicional de espera, la satisfacción {'disminuye' if modelo.params['tiempo_espera'] < 0 else 'aumenta'} {abs(modelo.params['tiempo_espera']):.4f} puntos")

# Paso 3: Verificar supuestos
residuos = modelo.resid

print(f"\n4. VERIFICACIÓN DE SUPUESTOS")

# Normalidad de residuos (Shapiro-Wilk)
stat_shapiro, p_shapiro = stats.shapiro(residuos)
print(f"   Normalidad (Shapiro-Wilk): p={p_shapiro:.4f} {'✓' if p_shapiro > 0.05 else '⚠️'}")

# Paso 4: Visualizaciones
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Scatter con línea de regresión
axes[0, 0].scatter(df['tiempo_espera'], df['satisfaccion'], alpha=0.6, edgecolor='black')
axes[0, 0].plot(df['tiempo_espera'], modelo.predict(X), color='red', linewidth=2)
axes[0, 0].set_xlabel('Tiempo de Espera (min)')
axes[0, 0].set_ylabel('Satisfacción')
axes[0, 0].set_title(f'Regresión (R²={modelo.rsquared:.3f})', fontweight='bold')
axes[0, 0].grid(alpha=0.3)

# Residuos vs Ajustados
axes[0, 1].scatter(modelo.fittedvalues, residuos, alpha=0.6, edgecolor='black')
axes[0, 1].axhline(y=0, color='red', linestyle='--')
axes[0, 1].set_xlabel('Valores Ajustados')
axes[0, 1].set_ylabel('Residuos')
axes[0, 1].set_title('Residuos vs Ajustados', fontweight='bold')
axes[0, 1].grid(alpha=0.3)

# Q-Q plot
stats.probplot(residuos, dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('Q-Q Plot', fontweight='bold')
axes[1, 0].grid(alpha=0.3)

# Histograma de residuos
axes[1, 1].hist(residuos, bins=20, edgecolor='black', alpha=0.7)
axes[1, 1].set_xlabel('Residuos')
axes[1, 1].set_ylabel('Frecuencia')
axes[1, 1].set_title('Distribución de Residuos', fontweight='bold')
axes[1, 1].grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# Paso 5: Predicción de ejemplo
print(f"\n5. EJEMPLO DE PREDICCIÓN")
tiempo_ejemplo = 25
pred = modelo.params['const'] + modelo.params['tiempo_espera'] * tiempo_ejemplo
print(f"   Si tiempo_espera = {tiempo_ejemplo} min")
print(f"   → Satisfacción predicha = {pred:.2f}")

print("\n" + "="*70)
```

---

## 📚 Referencias

- Levin & Rubin. "Estadística para administradores". Capítulos 12-13
- Montgomery, D. "Introduction to Linear Regression Analysis"
- Statsmodels Documentation: `statsmodels.regression.linear_model`
- Scikit-learn Documentation: `sklearn.linear_model.LinearRegression`

---

## ✍️ Ejercicios Propuestos

1. **Ejercicio 1:** Modela la relación entre `calidad_atencion` y `satisfaccion`
2. **Ejercicio 2:** Crea una regresión múltiple con 3+ variables predictoras
3. **Ejercicio 3:** Identifica outliers usando distancia de Cook
4. **Ejercicio 4:** Compara R² de diferentes modelos y elige el mejor

