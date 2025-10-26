# Guía: Pruebas de Hipótesis

## 🎯 ¿Qué es una Prueba de Hipótesis?

Una prueba de hipótesis es un procedimiento estadístico que nos permite **tomar decisiones** basadas en datos de muestra sobre características de una población.

**Ejemplo de negocio:**
> Una ONG afirma que su nivel promedio de satisfacción es de 8.5/10. ¿Los datos respaldan esta afirmación?

---

## 📋 Pasos para una Prueba de Hipótesis

### 1. Plantear las Hipótesis

**Hipótesis Nula (H₀):**
- Es la afirmación que asumimos como verdadera
- Generalmente incluye =, ≤, o ≥
- Ejemplo: H₀: μ = 8.5

**Hipótesis Alternativa (H₁ o Hₐ):**
- Es lo que queremos probar
- Incluye ≠, <, o >
- Ejemplo: H₁: μ ≠ 8.5

**Tipos de pruebas:**
- **Bilateral (dos colas):** H₁: μ ≠ μ₀
- **Unilateral derecha:** H₁: μ > μ₀
- **Unilateral izquierda:** H₁: μ < μ₀

---

### 2. Seleccionar el Nivel de Significancia (α)

**Nivel de significancia α:**
- Probabilidad de rechazar H₀ cuando es verdadera (Error Tipo I)
- Valores comunes: 0.05 (5%), 0.01 (1%), 0.10 (10%)

```python
alpha = 0.05  # Nivel de confianza del 95%
```

---

### 3. Calcular el Estadístico de Prueba

**Selección de prueba:**

| Condición | Estadístico | Distribución |
|-----------|-------------|--------------|
| σ conocida, n > 30 | Z | Normal |
| σ desconocida, n < 30 | t | t-Student |
| σ desconocida, n ≥ 30 | Z o t | Aproximadamente normal |

---

### 4. Calcular el p-value

**p-value:**
- Probabilidad de obtener resultados tan extremos como los observados, asumiendo que H₀ es verdadera
- Si p-value < α → Rechazamos H₀
- Si p-value ≥ α → No rechazamos H₀

---

### 5. Tomar la Decisión

**Regla de decisión:**
```
SI p-value < α:
    Rechazar H₀
SINO:
    No rechazar H₀
```

---

## 🔬 Prueba de Hipótesis para UNA Muestra

### Prueba t para la Media (σ desconocida)

**Hipótesis:**
- H₀: μ = μ₀
- H₁: μ ≠ μ₀ (bilateral)

**En Python:**

```python
from scipy import stats
import numpy as np

# Datos de muestra
datos = [8, 9, 7, 10, 8, 9, 6, 8, 9, 7, 8, 5, 9, 10, 8]

# Valor poblacional hipotético
mu_0 = 8.5

# Prueba t de una muestra
t_stat, p_value = stats.ttest_1samp(datos, mu_0)

print(f"Estadístico t: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

# Decisión
alpha = 0.05
if p_value < alpha:
    print("Rechazamos H₀")
else:
    print("No rechazamos H₀")
```

**Interpretación:**
```python
# Ejemplo de output
Estadístico t: -0.5234
p-value: 0.6082

# p-value = 0.6082 > 0.05
# Conclusión: No hay evidencia suficiente para rechazar que μ = 8.5
```

---

### Prueba Z para la Media (σ conocida)

**En Python:**

```python
from scipy import stats
import numpy as np

# Datos
datos = [8, 9, 7, 10, 8, 9, 6, 8, 9, 7]
mu_0 = 8.5
sigma = 1.2  # Desviación estándar poblacional conocida

# Calcular Z manualmente
n = len(datos)
x_bar = np.mean(datos)
z_stat = (x_bar - mu_0) / (sigma / np.sqrt(n))

# Calcular p-value (bilateral)
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print(f"Estadístico Z: {z_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

---

## 🔬🔬 Prueba de Hipótesis para DOS Muestras

### 1. Muestras Independientes (t-test)

**Contexto:** Comparar dos grupos independientes
**Ejemplo:** Satisfacción entre beneficiarios del Área A vs Área B

**Hipótesis:**
- H₀: μ₁ = μ₂ (las medias son iguales)
- H₁: μ₁ ≠ μ₂ (las medias son diferentes)

**En Python:**

```python
from scipy import stats

# Datos de dos grupos independientes
area_A = [8, 9, 7, 10, 8, 9, 8, 9, 10]
area_B = [6, 7, 5, 8, 6, 7, 6, 5, 7]

# Prueba t para muestras independientes
t_stat, p_value = stats.ttest_ind(area_A, area_B)

print(f"Estadístico t: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

# Decisión
alpha = 0.05
if p_value < alpha:
    print("Las medias son significativamente diferentes")
else:
    print("No hay diferencia significativa entre las medias")
```

**Suposiciones:**
- Independencia de las muestras
- Normalidad (o n > 30)
- Homogeneidad de varianzas (usar Levene test)

**Prueba de Levene (homogeneidad de varianzas):**

```python
# Verificar si las varianzas son iguales
stat, p_levene = stats.levene(area_A, area_B)

if p_levene > 0.05:
    # Varianzas iguales, usar ttest_ind normal
    t_stat, p_value = stats.ttest_ind(area_A, area_B)
else:
    # Varianzas diferentes, usar Welch's t-test
    t_stat, p_value = stats.ttest_ind(area_A, area_B, equal_var=False)
```

---

### 2. Muestras Pareadas (t-test pareado)

**Contexto:** Comparar dos mediciones en el mismo grupo
**Ejemplo:** Satisfacción antes y después de una intervención

**Hipótesis:**
- H₀: μ_diferencia = 0
- H₁: μ_diferencia ≠ 0

**En Python:**

```python
# Datos pareados
antes = [7, 6, 8, 7, 6, 9, 7, 8]
despues = [8, 7, 9, 8, 7, 10, 8, 9]

# Prueba t pareada
t_stat, p_value = stats.ttest_rel(antes, despues)

print(f"Estadístico t: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Hay diferencia significativa entre antes y después")
```

---

## 📊 Comparación de Proporciones

**Contexto:** Comparar porcentajes entre grupos
**Ejemplo:** % de beneficiarios satisfechos (≥8) entre áreas

**En Python:**

```python
from statsmodels.stats.proportion import proportions_ztest

# Datos
count = np.array([45, 38])  # Número de satisfechos en cada grupo
nobs = np.array([50, 50])   # Total en cada grupo

# Prueba Z para proporciones
z_stat, p_value = proportions_ztest(count, nobs)

print(f"Estadístico Z: {z_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

---

## 🎯 Ejemplo Completo: Calidad en el Servicio de ONG

```python
import pandas as pd
import numpy as np
from scipy import stats

# Cargar datos
df = pd.read_csv('datos_satisfaccion_ong.csv')

# 1. Prueba: ¿La satisfacción promedio es 8?
H0 = 8
t_stat, p_value = stats.ttest_1samp(df['satisfaccion'], H0)

print("=" * 50)
print("Prueba 1: Satisfacción promedio vs estándar (8)")
print(f"H₀: μ = {H0}")
print(f"Media muestral: {df['satisfaccion'].mean():.2f}")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Conclusión: La satisfacción promedio ES diferente de 8")
else:
    print("Conclusión: No hay evidencia de que sea diferente de 8")

# 2. Comparar dos áreas
area_norte = df[df['area'] == 'Norte']['satisfaccion']
area_sur = df[df['area'] == 'Sur']['satisfaccion']

t_stat, p_value = stats.ttest_ind(area_norte, area_sur)

print("\n" + "=" * 50)
print("Prueba 2: Comparación entre Área Norte y Sur")
print(f"Media Norte: {area_norte.mean():.2f}")
print(f"Media Sur: {area_sur.mean():.2f}")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Conclusión: HAY diferencia significativa entre áreas")
else:
    print("Conclusión: NO hay diferencia significativa entre áreas")
```

---

## ⚠️ Errores Comunes

### Error Tipo I (α)
- Rechazar H₀ cuando es verdadera
- "Falso positivo"
- Probabilidad = α

### Error Tipo II (β)
- No rechazar H₀ cuando es falsa
- "Falso negativo"
- Poder de la prueba = 1 - β

---

## 💡 Tips Prácticos

1. **Siempre visualiza primero:** Usa histogramas y boxplots
2. **Verifica supuestos:** Normalidad con Q-Q plots o tests
3. **Interpreta el contexto:** Un resultado estadísticamente significativo puede no ser relevante en la práctica
4. **Tamaño del efecto:** Complementa con medidas como Cohen's d

```python
# Tamaño del efecto (Cohen's d)
def cohen_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_std

d = cohen_d(area_norte, area_sur)
print(f"Cohen's d: {d:.4f}")

# Interpretación:
# |d| < 0.2: pequeño
# |d| ~ 0.5: mediano
# |d| > 0.8: grande
```

---

## 📚 Referencias

- Levin & Rubin. "Estadística para administradores". Capítulos 8-9
- SciPy Stats Documentation: https://docs.scipy.org/doc/scipy/reference/stats.html
- Statsmodels: https://www.statsmodels.org/
