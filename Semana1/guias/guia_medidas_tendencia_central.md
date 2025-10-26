# Guía: Medidas de Tendencia Central y Dispersión

## 📊 Medidas de Tendencia Central

### 1. Media (Promedio)
**Definición:** Suma de todos los valores dividida entre el número total de datos.

**Fórmula:**
```
μ = Σx / n
```

**En Python:**
```python
import pandas as pd
import numpy as np

# Con pandas
media = df['columna'].mean()

# Con numpy
media = np.mean(datos)
```

**Cuándo usarla:**
- ✅ Datos sin valores extremos
- ✅ Distribución simétrica
- ❌ Evitar con outliers

---

### 2. Mediana
**Definición:** Valor que divide los datos en dos partes iguales.

**En Python:**
```python
# Con pandas
mediana = df['columna'].median()

# Con numpy
mediana = np.median(datos)
```

**Cuándo usarla:**
- ✅ Datos con valores extremos
- ✅ Distribución asimétrica
- ✅ Variables ordinales

---

### 3. Moda
**Definición:** Valor que aparece con mayor frecuencia.

**En Python:**
```python
# Con pandas
moda = df['columna'].mode()[0]

# Con scipy
from scipy import stats
moda = stats.mode(datos)[0]
```

**Cuándo usarla:**
- ✅ Variables categóricas
- ✅ Identificar valor más común

---

## 📈 Medidas de Dispersión

### 1. Varianza
**Definición:** Promedio de las desviaciones al cuadrado respecto a la media.

**Fórmula (poblacional):**
```
σ² = Σ(x - μ)² / N
```

**Fórmula (muestral):**
```
s² = Σ(x - x̄)² / (n - 1)
```

**En Python:**
```python
# Varianza muestral (ddof=1)
varianza = df['columna'].var()

# Varianza poblacional (ddof=0)
varianza_pob = df['columna'].var(ddof=0)
```

---

### 2. Desviación Estándar
**Definición:** Raíz cuadrada de la varianza. Mide dispersión en las mismas unidades que los datos.

**Fórmula:**
```
σ = √(σ²)
```

**En Python:**
```python
# Desviación estándar muestral
desv_std = df['columna'].std()

# Desviación estándar poblacional
desv_std_pob = df['columna'].std(ddof=0)
```

**Interpretación:**
- **Baja desviación:** Datos concentrados cerca de la media
- **Alta desviación:** Datos muy dispersos

---

### 3. Rango
**Definición:** Diferencia entre el máximo y el mínimo.

**En Python:**
```python
rango = df['columna'].max() - df['columna'].min()
```

---

### 4. Cuartiles y Rango Intercuartílico (IQR)

**Cuartiles:**
- Q1 (25%): 25% de los datos están por debajo
- Q2 (50%): Mediana
- Q3 (75%): 75% de los datos están por debajo

**En Python:**
```python
# Cuartiles
Q1 = df['columna'].quantile(0.25)
Q2 = df['columna'].quantile(0.50)  # Mediana
Q3 = df['columna'].quantile(0.75)

# Rango intercuartílico
IQR = Q3 - Q1
```

**Detección de outliers:**
```python
# Límites para outliers
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Filtrar outliers
outliers = df[(df['columna'] < limite_inferior) | (df['columna'] > limite_superior)]
```

---

## 📋 Resumen Estadístico Completo

**En Python:**
```python
# Resumen de todas las medidas
resumen = df['columna'].describe()

# Incluir más percentiles
resumen_completo = df['columna'].describe(percentiles=[.1, .25, .5, .75, .9])
```

**Output:**
```
count    100.000000  # Número de datos
mean      50.500000  # Media
std       29.011492  # Desviación estándar
min        1.000000  # Mínimo
25%       25.750000  # Q1
50%       50.500000  # Q2 (Mediana)
75%       75.250000  # Q3
max      100.000000  # Máximo
```

---

## 💡 Ejemplo Práctico: Calidad en el Servicio

```python
import pandas as pd
import numpy as np

# Datos de satisfacción del cliente (escala 1-10)
satisfaccion = pd.Series([8, 9, 7, 10, 8, 9, 6, 8, 9, 7, 8, 5, 9, 10, 8])

# Medidas de tendencia central
print(f"Media: {satisfaccion.mean():.2f}")
print(f"Mediana: {satisfaccion.median():.2f}")
print(f"Moda: {satisfaccion.mode()[0]}")

# Medidas de dispersión
print(f"Desviación estándar: {satisfaccion.std():.2f}")
print(f"Varianza: {satisfaccion.var():.2f}")
print(f"Rango: {satisfaccion.max() - satisfaccion.min()}")

# Cuartiles
print(f"Q1: {satisfaccion.quantile(0.25)}")
print(f"Q2 (Mediana): {satisfaccion.quantile(0.50)}")
print(f"Q3: {satisfaccion.quantile(0.75)}")
```

**Interpretación:**
- Si media ≈ mediana → Distribución simétrica
- Si media > mediana → Distribución sesgada a la derecha
- Si media < mediana → Distribución sesgada a la izquierda

---

## 🎯 Aplicación en el Contexto de la ONG

**Preguntas a responder:**
1. ¿Cuál es el nivel promedio de satisfacción de los beneficiarios?
2. ¿Qué tan consistente es la calidad del servicio? (desviación estándar)
3. ¿Existen departamentos con resultados atípicos?
4. ¿El 50% de los encuestados califica con al menos qué valor?

---

## 📚 Referencias

- Levin & Rubin (2004). "Estadística para administradores". Cap. 3
- Pandas Documentation: https://pandas.pydata.org/docs/
- NumPy Statistical Functions: https://numpy.org/doc/stable/reference/routines.statistics.html
