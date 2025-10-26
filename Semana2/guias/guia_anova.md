# Guía: ANOVA (Análisis de Varianza)

## 🎯 ¿Qué es ANOVA?

**ANOVA (Analysis of Variance)** es una prueba estadística para comparar las **medias de 3 o más grupos** simultáneamente.

**Ejemplo de negocio:**
> ¿La satisfacción promedio es diferente entre las 4 áreas de servicio (Norte, Sur, Este, Oeste)?

---

## 📋 ¿Por qué ANOVA y no múltiples pruebas t?

### Problema con múltiples pruebas t:

Si tienes 4 grupos y quieres compararlos todos:
- Norte vs Sur
- Norte vs Este
- Norte vs Oeste
- Sur vs Este
- Sur vs Oeste
- Este vs Oeste

**Total: 6 pruebas t**

**Problema:** Cada prueba tiene 5% de probabilidad de Error Tipo I (α=0.05). Con múltiples pruebas, la probabilidad acumulada de cometer al menos un error aumenta significativamente.

**Solución:** ANOVA controla el error Tipo I al hacer UNA sola prueba para todos los grupos.

---

## 🧮 ANOVA de Un Factor (One-Way ANOVA)

### Hipótesis:

- **H₀:** μ₁ = μ₂ = μ₃ = ... = μₖ (Todas las medias son iguales)
- **H₁:** Al menos una media es diferente

### Paso 1: Verificar Supuestos

#### 1. Independencia de observaciones
Cada observación es independiente de las demás.

#### 2. Normalidad
Los datos de cada grupo siguen una distribución normal.

**Prueba de Shapiro-Wilk:**
```python
from scipy.stats import shapiro

for area in df['area'].unique():
    datos = df[df['area'] == area]['satisfaccion']
    stat, p = shapiro(datos)
    print(f"{area}: W={stat:.4f}, p={p:.4f}")
    if p > 0.05:
        print("  ✓ Normal")
    else:
        print("  ✗ No normal")
```

#### 3. Homogeneidad de varianzas (Homocedasticidad)
Las varianzas de los grupos son similares.

**Prueba de Levene:**
```python
from scipy.stats import levene

grupos = [df[df['area'] == area]['satisfaccion'] for area in df['area'].unique()]
stat, p = levene(*grupos)

print(f"Test de Levene: W={stat:.4f}, p={p:.4f}")
if p > 0.05:
    print("✓ Varianzas homogéneas")
else:
    print("✗ Varianzas NO homogéneas (considerar Welch's ANOVA)")
```

---

## 💻 Implementación en Python

### Opción 1: Usando scipy

```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv('datos_satisfaccion.csv')

# Separar datos por grupo
norte = df[df['area'] == 'Norte']['satisfaccion']
sur = df[df['area'] == 'Sur']['satisfaccion']
este = df[df['area'] == 'Este']['satisfaccion']
oeste = df[df['area'] == 'Oeste']['satisfaccion']

# Realizar ANOVA
f_stat, p_value = stats.f_oneway(norte, sur, este, oeste)

print("="*60)
print("ANOVA DE UN FACTOR")
print("="*60)
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_value:.4f}")

# Decisión
alpha = 0.05
if p_value < alpha:
    print(f"\n✗ Rechazamos H₀ (p={p_value:.4f} < {alpha})")
    print("Conclusión: Al menos una media es diferente")
    print("Siguiente paso: Pruebas post-hoc para identificar cuál(es)")
else:
    print(f"\n✓ No rechazamos H₀ (p={p_value:.4f} ≥ {alpha})")
    print("Conclusión: No hay diferencia significativa entre las medias")
```

### Opción 2: Usando statsmodels (con tabla ANOVA completa)

```python
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Ajustar modelo ANOVA
modelo = ols('satisfaccion ~ C(area)', data=df).fit()

# Tabla ANOVA
tabla_anova = sm.stats.anova_lm(modelo, typ=2)
print("\nTabla ANOVA:")
print(tabla_anova)

# Explicación de la tabla:
# sum_sq: Suma de cuadrados
# df: Grados de libertad
# F: Estadístico F
# PR(>F): p-value
```

---

## 📊 Visualización de Resultados

### Boxplot por Grupos

```python
plt.figure(figsize=(10, 6))
df.boxplot(column='satisfaccion', by='area', grid=False, patch_artist=True)
plt.suptitle('')
plt.title('Distribución de Satisfacción por Área', fontsize=14, fontweight='bold')
plt.xlabel('Área', fontsize=12)
plt.ylabel('Satisfacción', fontsize=12)
plt.tight_layout()
plt.show()
```

### Gráfico de Medias con Intervalos de Confianza

```python
# Calcular estadísticos por grupo
medias = df.groupby('area')['satisfaccion'].mean()
std_errors = df.groupby('area')['satisfaccion'].sem()

plt.figure(figsize=(10, 6))
medias.plot(kind='bar', yerr=std_errors*1.96, capsize=5, color='steelblue', edgecolor='black')
plt.title('Media de Satisfacción por Área (IC 95%)', fontsize=14, fontweight='bold')
plt.xlabel('Área', fontsize=12)
plt.ylabel('Satisfacción Promedio', fontsize=12)
plt.xticks(rotation=0)
plt.axhline(y=df['satisfaccion'].mean(), color='red', linestyle='--', label='Media General')
plt.legend()
plt.grid(alpha=0.3, axis='y')
plt.tight_layout()
plt.show()
```

### Violin Plot

```python
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x='area', y='satisfaccion', palette='Set2')
plt.title('Distribución de Satisfacción por Área (Violin Plot)', fontsize=14, fontweight='bold')
plt.xlabel('Área', fontsize=12)
plt.ylabel('Satisfacción', fontsize=12)
plt.grid(alpha=0.3, axis='y')
plt.tight_layout()
plt.show()
```

---

## 🔍 Pruebas Post-Hoc

Si rechazamos H₀ en ANOVA, necesitamos **pruebas post-hoc** para determinar **qué grupos** son diferentes.

### Prueba de Tukey (HSD)

**La más común:** Compara todas las parejas de medias controlando el error familiar.

```python
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Realizar prueba de Tukey
tukey = pairwise_tukeyhsd(endog=df['satisfaccion'], groups=df['area'], alpha=0.05)

print("\nPrueba Post-Hoc de Tukey:")
print(tukey)

# Visualización
tukey.plot_simultaneous(figsize=(10, 6))
plt.title('Intervalos de Confianza 95% - Prueba de Tukey', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Interpretación de la tabla:**
- **reject:** True si hay diferencia significativa
- **meandiff:** Diferencia entre medias
- **lower/upper:** Intervalo de confianza de la diferencia
- **p-adj:** p-value ajustado

### Otras Pruebas Post-Hoc

#### Bonferroni (más conservadora)

```python
from statsmodels.stats.multicomp import MultiComparison

mc = MultiComparison(df['satisfaccion'], df['area'])
resultado_bonferroni = mc.allpairtest(stats.ttest_ind, method='bonf')
print(resultado_bonferroni[0])
```

#### Scheffé (más flexible)

Útil cuando se planean comparaciones complejas (no solo pares).

---

## 📈 Estadísticos Descriptivos por Grupo

```python
# Resumen por grupo
resumen = df.groupby('area')['satisfaccion'].agg([
    ('n', 'count'),
    ('Media', 'mean'),
    ('Mediana', 'median'),
    ('Desv.Std', 'std'),
    ('Mínimo', 'min'),
    ('Máximo', 'max')
]).round(2)

print("\nEstadísticos Descriptivos por Área:")
print(resumen)

# Visualizar en tabla
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
tabla = ax.table(cellText=resumen.values,
                 rowLabels=resumen.index,
                 colLabels=resumen.columns,
                 cellLoc='center',
                 loc='center')
tabla.auto_set_font_size(False)
tabla.set_fontsize(10)
tabla.scale(1, 2)
plt.title('Resumen Estadístico por Área', fontsize=14, fontweight='bold', pad=20)
plt.show()
```

---

## 🎯 Tamaño del Efecto

El p-value nos dice **SI** hay diferencia, pero no **QUÉ TAN GRANDE** es.

### Eta Cuadrado (η²)

Proporción de varianza en la variable dependiente explicada por la variable independiente.

```python
# Calcular Eta cuadrado
ss_between = sum([len(df[df['area']==a]) * (df[df['area']==a]['satisfaccion'].mean() - df['satisfaccion'].mean())**2
                  for a in df['area'].unique()])

ss_total = sum((df['satisfaccion'] - df['satisfaccion'].mean())**2)

eta_squared = ss_between / ss_total

print(f"\nEta² = {eta_squared:.4f}")

# Interpretación
if eta_squared < 0.01:
    print("Efecto pequeño")
elif eta_squared < 0.06:
    print("Efecto mediano")
else:
    print("Efecto grande")
```

---

## ⚠️ ¿Qué hacer si NO se cumplen los supuestos?

### 1. Si NO hay normalidad:

**Opción A:** Transformar datos
```python
# Transformación logarítmica
df['satisfaccion_log'] = np.log(df['satisfaccion'])

# Transformación raíz cuadrada
df['satisfaccion_sqrt'] = np.sqrt(df['satisfaccion'])
```

**Opción B:** Usar prueba NO paramétrica (Kruskal-Wallis)
```python
from scipy.stats import kruskal

norte = df[df['area'] == 'Norte']['satisfaccion']
sur = df[df['area'] == 'Sur']['satisfaccion']
este = df[df['area'] == 'Este']['satisfaccion']
oeste = df[df['area'] == 'Oeste']['satisfaccion']

h_stat, p_value = kruskal(norte, sur, este, oeste)

print(f"Kruskal-Wallis H: {h_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("✗ Al menos un grupo tiene mediana diferente")
    # Post-hoc: Mann-Whitney U con corrección Bonferroni
else:
    print("✓ No hay diferencia entre medianas")
```

### 2. Si NO hay homogeneidad de varianzas:

**Usar Welch's ANOVA** (no asume varianzas iguales)
```python
# Welch's ANOVA ya está implementada en statsmodels
from scipy.stats import f_oneway

# Para Welch's ANOVA, usar pingouin
import pingouin as pg

welch_result = pg.welch_anova(data=df, dv='satisfaccion', between='area')
print(welch_result)
```

---

## 🎯 Ejemplo Completo: Análisis de ONG

```python
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv('ejemplo_satisfaccion_clientes.csv')

print("="*70)
print("ANÁLISIS ANOVA: SATISFACCIÓN POR ÁREA")
print("="*70)

# Paso 1: Estadísticos descriptivos
print("\nEstadísticos Descriptivos:")
resumen = df.groupby('area')['satisfaccion'].agg(['count', 'mean', 'std'])
print(resumen)

# Paso 2: Verificar supuestos
print("\n" + "="*70)
print("VERIFICACIÓN DE SUPUESTOS")
print("="*70)

# Normalidad (Shapiro-Wilk por grupo)
print("\nPrueba de Normalidad (Shapiro-Wilk):")
for area in df['area'].unique():
    datos = df[df['area'] == area]['satisfaccion']
    stat, p = stats.shapiro(datos)
    resultado = "✓ Normal" if p > 0.05 else "⚠️ No normal"
    print(f"  {area}: p={p:.4f} {resultado}")

# Homogeneidad de varianzas (Levene)
print("\nPrueba de Homogeneidad de Varianzas (Levene):")
grupos = [df[df['area'] == area]['satisfaccion'] for area in df['area'].unique()]
stat, p = stats.levene(*grupos)
print(f"  W={stat:.4f}, p={p:.4f}")
print(f"  {'✓ Varianzas homogéneas' if p > 0.05 else '⚠️ Varianzas NO homogéneas'}")

# Paso 3: ANOVA
print("\n" + "="*70)
print("RESULTADO ANOVA")
print("="*70)

f_stat, p_value = stats.f_oneway(*grupos)
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"\n✗ Rechazamos H₀ (p={p_value:.4f} < {alpha})")
    print("Conclusión: Al menos una área tiene satisfacción diferente")

    # Paso 4: Post-hoc (Tukey)
    print("\n" + "="*70)
    print("PRUEBAS POST-HOC (TUKEY)")
    print("="*70)

    tukey = pairwise_tukeyhsd(endog=df['satisfaccion'], groups=df['area'], alpha=0.05)
    print(tukey)

    # Identificar diferencias
    print("\n📊 Resumen de diferencias significativas:")
    for i, row in enumerate(tukey.summary().data[1:]):
        if row[6]:  # reject column
            print(f"  • {row[0]} vs {row[1]}: diferencia = {row[2]:.2f}, p={row[5]:.4f}")

else:
    print(f"\n✓ No rechazamos H₀ (p={p_value:.4f} ≥ {alpha})")
    print("Conclusión: No hay diferencia significativa entre áreas")

# Visualización
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Boxplot
df.boxplot(column='satisfaccion', by='area', ax=axes[0], patch_artist=True)
axes[0].set_title('Distribución por Área', fontweight='bold')
axes[0].set_xlabel('Área')
axes[0].set_ylabel('Satisfacción')

# Gráfico de medias
medias = df.groupby('area')['satisfaccion'].mean()
std_errors = df.groupby('area')['satisfaccion'].sem()
medias.plot(kind='bar', yerr=std_errors*1.96, ax=axes[1], capsize=5, color='teal')
axes[1].set_title('Medias con IC 95%', fontweight='bold')
axes[1].set_ylabel('Satisfacción Promedio')
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=0)
axes[1].axhline(y=df['satisfaccion'].mean(), color='red', linestyle='--', label='Media General')
axes[1].legend()
axes[1].grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.show()
```

---

## 💡 Tips Prácticos

### 1. Reportar Resultados

Al escribir resultados en un reporte:

```
Se realizó un ANOVA de un factor para comparar la satisfacción entre las 4 áreas
de servicio (Norte, Sur, Este, Oeste). Se encontró una diferencia significativa
entre los grupos (F(3, 196) = 12.45, p < 0.001, η² = 0.16).

Pruebas post-hoc de Tukey revelaron que:
- Área Norte (M=8.45, SD=0.82) tuvo mayor satisfacción que Área Oeste (M=5.75, SD=0.85), p<0.001
- Área Este (M=9.20, SD=0.65) tuvo mayor satisfacción que Área Oeste, p<0.001
- No hubo diferencia significativa entre Norte y Sur (p=0.42)
```

### 2. Tamaño Muestral

ANOVA requiere mínimo ~20-30 observaciones por grupo para tener poder estadístico adecuado.

### 3. ANOVA vs Regresión

ANOVA es un caso especial de regresión lineal cuando la variable independiente es categórica.

---

## 📚 Referencias

- Levin & Rubin. "Estadística para administradores". Capítulo 10
- Montgomery, D. "Design and Analysis of Experiments"
- SciPy Documentation: `scipy.stats.f_oneway`
- Statsmodels Documentation: `statsmodels.stats.anova`

---

## ✍️ Ejercicios Propuestos

1. **Ejercicio 1:** Compara `calidad_atencion` entre las 4 áreas
2. **Ejercicio 2:** Crea grupos de edad y compara satisfacción entre ellos
3. **Ejercicio 3:** Si algún supuesto no se cumple, aplica Kruskal-Wallis
4. **Ejercicio 4:** Calcula el tamaño del efecto (η²) y explica su significado práctico

