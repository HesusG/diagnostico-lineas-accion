# Guía: Prueba Ji-Cuadrada (χ²)

## 🎯 ¿Qué es la Prueba Ji-Cuadrada?

La prueba **Ji-cuadrada (χ²)** es una prueba estadística para determinar si existe una **relación o asociación** entre dos **variables categóricas**.

**Ejemplo de negocio:**
> ¿El área de servicio (Norte, Sur, Este, Oeste) influye en el nivel de satisfacción (Baja, Media, Alta)?

---

## 📋 Cuándo Usar Ji-Cuadrada

✅ **Usar cuando:**
- Ambas variables son **categóricas** (nominales u ordinales)
- Quieres probar independencia entre variables
- Tienes datos de frecuencias/conteos

❌ **NO usar cuando:**
- Variables son numéricas continuas (usar correlación o regresión)
- Frecuencias esperadas < 5 en más del 20% de celdas

---

## 🧮 Tipos de Pruebas Ji-Cuadrada

### 1. Prueba de Independencia
Determina si dos variables categóricas son independientes.

**Ejemplo:** ¿El género es independiente de la satisfacción?

### 2. Prueba de Bondad de Ajuste
Verifica si una distribución observada se ajusta a una distribución esperada.

**Ejemplo:** ¿Los beneficiarios se distribuyen uniformemente entre áreas?

---

## 📊 Prueba Ji-Cuadrada de Independencia

### Paso 1: Plantear Hipótesis

- **H₀:** Las variables son independientes (no hay relación)
- **H₁:** Las variables NO son independientes (sí hay relación)

### Paso 2: Crear Tabla de Contingencia

Tabla que cruza las dos variables categóricas:

|            | Satisfacción Baja | Satisfacción Media | Satisfacción Alta | **Total** |
|------------|-------------------|---------------------|-------------------|-----------|
| Norte      | 5                 | 15                  | 30                | 50        |
| Sur        | 10                | 20                  | 20                | 50        |
| Este       | 3                 | 10                  | 37                | 50        |
| Oeste      | 20                | 25                  | 5                 | 50        |
| **Total**  | 38                | 70                  | 92                | **200**   |

### Paso 3: Calcular Frecuencias Esperadas

Frecuencia esperada = (Total fila × Total columna) / Total general

**Ejemplo:**
```
E(Norte, Baja) = (50 × 38) / 200 = 9.5
```

### Paso 4: Calcular Estadístico χ²

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

Donde:
- O = Frecuencia observada
- E = Frecuencia esperada

### Paso 5: Comparar con Valor Crítico

Grados de libertad: `df = (filas - 1) × (columnas - 1)`

Si **χ² > valor crítico** → Rechazar H₀

---

## 💻 Implementación en Python

### Ejemplo Completo

```python
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('datos_satisfaccion.csv')

# Crear variable categórica de satisfacción
df['satisfaccion_cat'] = pd.cut(df['satisfaccion'],
                                  bins=[0, 6, 8, 10],
                                  labels=['Baja', 'Media', 'Alta'])

# Paso 1: Crear tabla de contingencia
tabla_contingencia = pd.crosstab(df['area'], df['satisfaccion_cat'])
print("Tabla de Contingencia:")
print(tabla_contingencia)

# Paso 2: Realizar prueba ji-cuadrada
chi2, p_value, dof, expected = chi2_contingency(tabla_contingencia)

# Resultados
print(f"\nEstadístico χ²: {chi2:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Grados de libertad: {dof}")

# Decisión
alpha = 0.05
if p_value < alpha:
    print(f"\n✗ Rechazamos H₀ (p={p_value:.4f} < {alpha})")
    print("Conclusión: SÍ existe relación entre área y satisfacción")
else:
    print(f"\n✓ No rechazamos H₀ (p={p_value:.4f} ≥ {alpha})")
    print("Conclusión: NO hay evidencia de relación")

# Frecuencias esperadas
print("\nFrecuencias Esperadas:")
print(pd.DataFrame(expected,
                   index=tabla_contingencia.index,
                   columns=tabla_contingencia.columns))
```

---

## 📈 Visualización de Resultados

### Heatmap de Frecuencias Observadas

```python
plt.figure(figsize=(10, 6))
sns.heatmap(tabla_contingencia, annot=True, fmt='d', cmap='Blues', cbar_kws={'label': 'Frecuencia'})
plt.title('Tabla de Contingencia: Área vs Satisfacción', fontsize=14, fontweight='bold')
plt.xlabel('Nivel de Satisfacción')
plt.ylabel('Área')
plt.tight_layout()
plt.show()
```

### Gráfico de Barras Apiladas

```python
tabla_contingencia.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.title('Distribución de Satisfacción por Área', fontsize=14, fontweight='bold')
plt.xlabel('Área')
plt.ylabel('Frecuencia')
plt.legend(title='Satisfacción', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```

### Tabla de Proporciones

```python
# Proporciones por fila (% dentro de cada área)
tabla_proporciones = tabla_contingencia.div(tabla_contingencia.sum(axis=1), axis=0) * 100
print("\nProporciones por Área (%):")
print(tabla_proporciones.round(2))
```

---

## 🔍 Interpretación de Resultados

### Caso 1: p-value < 0.05

```
χ² = 45.32, p-value = 0.0001

✗ Rechazamos H₀

Conclusión: Existe una relación significativa entre el área y la satisfacción.
Al observar la tabla, vemos que:
- Área Norte y Este tienen mayor proporción de satisfacción alta
- Área Oeste tiene mayor proporción de satisfacción baja
```

**Recomendación:** Investigar las causas de estas diferencias. ¿Qué hace diferente al Área Norte?

### Caso 2: p-value ≥ 0.05

```
χ² = 8.12, p-value = 0.2301

✓ No rechazamos H₀

Conclusión: No hay evidencia suficiente de relación entre área y satisfacción.
La distribución de satisfacción es similar en todas las áreas.
```

**Recomendación:** La satisfacción es consistente entre áreas, lo cual es positivo para la estandarización del servicio.

---

## 📊 Residuos Estandarizados

Los **residuos estandarizados** indican qué celdas contribuyen más al estadístico χ².

```python
# Calcular residuos estandarizados
residuos = (tabla_contingencia - expected) / np.sqrt(expected)

plt.figure(figsize=(10, 6))
sns.heatmap(residuos, annot=True, fmt='.2f', cmap='RdBu_r', center=0,
            vmin=-3, vmax=3, cbar_kws={'label': 'Residuo Estandarizado'})
plt.title('Residuos Estandarizados', fontsize=14, fontweight='bold')
plt.xlabel('Nivel de Satisfacción')
plt.ylabel('Área')
plt.tight_layout()
plt.show()

# Interpretación
print("\nInterpretación de Residuos:")
print("  |residuo| > 2: Contribución significativa")
print("  |residuo| > 3: Contribución muy significativa")
```

**Residuos positivos:** Más casos observados de lo esperado
**Residuos negativos:** Menos casos observados de lo esperado

---

## ⚠️ Supuestos y Limitaciones

### Supuestos:
1. **Observaciones independientes:** Cada beneficiario aparece solo una vez
2. **Frecuencias esperadas ≥ 5:** Al menos en el 80% de celdas
3. **Muestra aleatoria**

### Verificación de Frecuencias Esperadas:

```python
# Contar celdas con frecuencia esperada < 5
celdas_total = expected.size
celdas_bajas = (expected < 5).sum()
porcentaje = (celdas_bajas / celdas_total) * 100

print(f"Celdas con E < 5: {celdas_bajas} de {celdas_total} ({porcentaje:.1f}%)")

if porcentaje > 20:
    print("⚠️ ADVERTENCIA: Más del 20% de celdas tienen E < 5")
    print("   Considerar combinar categorías o usar Test Exacto de Fisher")
else:
    print("✓ Supuesto cumplido")
```

### ¿Qué hacer si no se cumple?
- **Combinar categorías:** Agrupar niveles con pocas observaciones
- **Test Exacto de Fisher:** Para tablas 2×2 con muestras pequeñas
- **Aumentar tamaño muestral**

---

## 🎯 Ejemplo Aplicado: ONG

### Pregunta de Investigación:
¿El género de los beneficiarios está relacionado con si recomendarían el servicio?

```python
# Crear tabla de contingencia
tabla = pd.crosstab(df['genero'], df['recomendaria'])

print("Tabla de Contingencia: Género vs Recomendación")
print(tabla)
print(f"\nTotal beneficiarios: {tabla.sum().sum()}")

# Prueba ji-cuadrada
chi2, p_value, dof, expected = chi2_contingency(tabla)

print(f"\nχ² = {chi2:.4f}")
print(f"p-value = {p_value:.4f}")

# Interpretación
if p_value < 0.05:
    print("\n✗ Hay relación significativa entre género y recomendación")

    # Analizar proporciones
    prop = tabla.div(tabla.sum(axis=1), axis=0) * 100
    print("\nProporciones (%):")
    print(prop.round(1))
else:
    print("\n✓ No hay relación entre género y recomendación")
    print("   La tasa de recomendación es similar entre géneros")
```

---

## 💡 Tips Prácticos

### 1. Categorización de Variables Numéricas
```python
# Convertir variable numérica a categórica
df['edad_grupo'] = pd.cut(df['edad'],
                          bins=[0, 30, 50, 100],
                          labels=['Joven', 'Adulto', 'Mayor'])
```

### 2. Comparar Múltiples Grupos
```python
# Probar independencia entre 3+ grupos
tabla = pd.crosstab(df['area'], df['satisfaccion_cat'])
chi2, p, dof, exp = chi2_contingency(tabla)
```

### 3. Efecto del Tamaño Muestral
Con muestras muy grandes, diferencias pequeñas pueden ser significativas estadísticamente pero no relevantes en la práctica.

**Medida de asociación (Cramér's V):**
```python
n = tabla.sum().sum()
min_dim = min(tabla.shape[0] - 1, tabla.shape[1] - 1)
cramers_v = np.sqrt(chi2 / (n * min_dim))

print(f"Cramér's V: {cramers_v:.4f}")

if cramers_v < 0.1:
    print("Asociación débil")
elif cramers_v < 0.3:
    print("Asociación moderada")
else:
    print("Asociación fuerte")
```

---

## 📚 Referencias

- Levin & Rubin. "Estadística para administradores". Capítulo 11
- SciPy Documentation: `scipy.stats.chi2_contingency`
- Agresti, A. "Categorical Data Analysis"

---

## ✍️ Ejercicios Propuestos

1. **Ejercicio 1:** Prueba si hay relación entre `area` y `recomendaria`
2. **Ejercicio 2:** Prueba si la distribución de beneficiarios por área es uniforme (bondad de ajuste)
3. **Ejercicio 3:** Crea grupos de edad y prueba relación con satisfacción
4. **Ejercicio 4:** Calcula residuos estandarizados e identifica celdas atípicas

