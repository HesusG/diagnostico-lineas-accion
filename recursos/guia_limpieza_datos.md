# Guía de Limpieza de Datos con Python

## 📋 Índice

1. [Introducción](#introducción)
2. [Paso 1: Exploración Inicial](#paso-1-exploración-inicial)
3. [Paso 2: Valores Faltantes](#paso-2-valores-faltantes)
4. [Paso 3: Detección de Outliers](#paso-3-detección-de-outliers)
5. [Paso 4: Normalización de Formatos](#paso-4-normalización-de-formatos)
6. [Paso 5: Validación de Tipos de Datos](#paso-5-validación-de-tipos-de-datos)
7. [Paso 6: Documentación de Transformaciones](#paso-6-documentación-de-transformaciones)
8. [Checklist de Limpieza](#checklist-de-limpieza)

---

## Introducción

La limpieza de datos es un paso **crítico** en cualquier análisis. Datos sucios pueden llevar a conclusiones erróneas. Esta guía te proporciona un proceso sistemático para preparar tus datos.

### ¿Por qué es importante?

- 80% del tiempo de análisis se invierte en limpieza de datos
- Datos limpios = Resultados confiables
- Evita sesgos y errores en visualizaciones
- Facilita análisis estadísticos válidos

---

## Paso 1: Exploración Inicial

### 1.1 Cargar y Visualizar Datos

```python
import pandas as pd
import numpy as np

# Cargar dataset
df = pd.read_csv('datos.csv')

# Vista rápida
print("📊 Primeras filas:")
print(df.head())

print("\n📏 Dimensiones:")
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

print("\n🔍 Información general:")
print(df.info())
```

### 1.2 Entender la Estructura

```python
# Tipos de datos
print("\n📋 Tipos de datos:")
print(df.dtypes)

# Nombres de columnas
print("\n📝 Columnas:")
print(df.columns.tolist())

# Estadísticas descriptivas
print("\n📈 Resumen estadístico:")
print(df.describe())
```

### 1.3 Identificar Problemas

```python
# Valores únicos por columna
print("\n🔢 Valores únicos:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} valores únicos")

# Duplicados
duplicados = df.duplicated().sum()
print(f"\n⚠️ Filas duplicadas: {duplicados}")
```

---

## Paso 2: Valores Faltantes

### 2.1 Detectar Valores Faltantes

```python
# Conteo de valores faltantes
print("\n🔍 Valores faltantes por columna:")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100

missing_df = pd.DataFrame({
    'Columna': missing.index,
    'Faltantes': missing.values,
    'Porcentaje': missing_pct.values
})
print(missing_df[missing_df['Faltantes'] > 0])

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=True, yticklabels=False, cmap='viridis')
plt.title('Mapa de Valores Faltantes')
plt.show()
```

### 2.2 Estrategias de Tratamiento

#### Opción A: Eliminar

```python
# Eliminar filas con cualquier valor faltante
df_clean = df.dropna()

# Eliminar filas donde TODAS las columnas son nulas
df_clean = df.dropna(how='all')

# Eliminar columnas con más de 50% de datos faltantes
threshold = 0.5
df_clean = df.dropna(thresh=int(threshold * len(df)), axis=1)
```

#### Opción B: Imputar

```python
# Imputar con la media (variables numéricas)
df['edad'].fillna(df['edad'].mean(), inplace=True)

# Imputar con la mediana (mejor para datos con outliers)
df['salario'].fillna(df['salario'].median(), inplace=True)

# Imputar con la moda (variables categóricas)
df['departamento'].fillna(df['departamento'].mode()[0], inplace=True)

# Imputar con valor específico
df['comentarios'].fillna('Sin comentario', inplace=True)

# Forward fill (usar valor anterior)
df['temperatura'].fillna(method='ffill', inplace=True)

# Backward fill (usar valor siguiente)
df['temperatura'].fillna(method='bfill', inplace=True)
```

#### Opción C: Interpolación

```python
# Interpolación lineal (buena para series temporales)
df['ventas'] = df['ventas'].interpolate(method='linear')

# Interpolación polinomial
df['ventas'] = df['ventas'].interpolate(method='polynomial', order=2)
```

### 2.3 Decisión Informada

```python
# Función para decidir estrategia
def decidir_imputacion(columna, df):
    missing_pct = (df[columna].isnull().sum() / len(df)) * 100

    if missing_pct > 50:
        return f"❌ ELIMINAR columna '{columna}' (>{50}% faltantes)"
    elif missing_pct > 20:
        return f"⚠️ Revisar '{columna}' ({missing_pct:.1f}% faltantes)"
    elif df[columna].dtype in ['int64', 'float64']:
        return f"✓ Imputar '{columna}' con mediana"
    else:
        return f"✓ Imputar '{columna}' con moda"

# Aplicar
for col in df.columns:
    if df[col].isnull().sum() > 0:
        print(decidir_imputacion(col, df))
```

---

## Paso 3: Detección de Outliers

### 3.1 Método del Rango Intercuartílico (IQR)

```python
def detectar_outliers_iqr(df, columna):
    """
    Detecta outliers usando el método IQR
    """
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[columna] < lower_bound) | (df[columna] > upper_bound)]

    print(f"\n📊 Columna: {columna}")
    print(f"Límite inferior: {lower_bound:.2f}")
    print(f"Límite superior: {upper_bound:.2f}")
    print(f"Outliers detectados: {len(outliers)} ({len(outliers)/len(df)*100:.1f}%)")

    return outliers

# Ejemplo
outliers_edad = detectar_outliers_iqr(df, 'edad')
```

### 3.2 Método Z-Score

```python
from scipy import stats

def detectar_outliers_zscore(df, columna, threshold=3):
    """
    Detecta outliers usando Z-score
    Z > 3 o Z < -3 se consideran outliers
    """
    z_scores = np.abs(stats.zscore(df[columna].dropna()))
    outliers_idx = np.where(z_scores > threshold)[0]

    print(f"\n📊 Columna: {columna}")
    print(f"Outliers (|Z| > {threshold}): {len(outliers_idx)}")

    return df.iloc[outliers_idx]

# Ejemplo
outliers_salario = detectar_outliers_zscore(df, 'salario')
```

### 3.3 Visualización de Outliers

```python
# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['edad', 'salario', 'satisfaccion']])
plt.title('Detección Visual de Outliers')
plt.xticks(rotation=45)
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df.index, df['edad'], alpha=0.6)
plt.axhline(y=df['edad'].mean() + 3*df['edad'].std(), color='r', linestyle='--', label='Límite superior')
plt.axhline(y=df['edad'].mean() - 3*df['edad'].std(), color='r', linestyle='--', label='Límite inferior')
plt.title('Outliers en Edad')
plt.legend()
plt.show()
```

### 3.4 Tratamiento de Outliers

```python
# Opción 1: Eliminar
df_sin_outliers = df[df['edad'] <= upper_bound]

# Opción 2: Reemplazar con límite (capping)
df['edad_capped'] = df['edad'].clip(lower=lower_bound, upper=upper_bound)

# Opción 3: Transformación logarítmica
df['salario_log'] = np.log1p(df['salario'])

# Opción 4: Winsorización (reemplazar extremos con percentiles)
from scipy.stats.mstats import winsorize
df['edad_winsorized'] = winsorize(df['edad'], limits=[0.05, 0.05])
```

---

## Paso 4: Normalización de Formatos

### 4.1 Texto

```python
# Convertir a minúsculas
df['departamento'] = df['departamento'].str.lower()

# Eliminar espacios extra
df['nombre'] = df['nombre'].str.strip()

# Reemplazar valores
df['genero'] = df['genero'].replace({
    'M': 'Masculino',
    'F': 'Femenino',
    'H': 'Masculino',
    'M': 'Femenino'
})

# Estandarizar categorías
df['ciudad'] = df['ciudad'].str.title()  # Primera letra mayúscula
```

### 4.2 Fechas

```python
# Convertir a datetime
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'], format='%Y-%m-%d', errors='coerce')

# Extraer componentes
df['año'] = df['fecha_ingreso'].dt.year
df['mes'] = df['fecha_ingreso'].dt.month
df['dia_semana'] = df['fecha_ingreso'].dt.day_name()

# Calcular diferencias
df['antiguedad_dias'] = (pd.Timestamp.now() - df['fecha_ingreso']).dt.days
```

### 4.3 Números

```python
# Eliminar caracteres no numéricos
df['salario'] = df['salario'].str.replace('$', '').str.replace(',', '').astype(float)

# Redondear
df['calificacion'] = df['calificacion'].round(2)

# Convertir a enteros
df['edad'] = df['edad'].astype(int)
```

---

## Paso 5: Validación de Tipos de Datos

### 5.1 Verificar Tipos Correctos

```python
# Diccionario de tipos esperados
tipos_esperados = {
    'id_empleado': 'int64',
    'nombre': 'object',
    'edad': 'int64',
    'salario': 'float64',
    'fecha_ingreso': 'datetime64[ns]',
    'activo': 'bool'
}

# Verificar
for col, tipo in tipos_esperados.items():
    if col in df.columns:
        tipo_actual = str(df[col].dtype)
        if tipo_actual != tipo:
            print(f"⚠️ {col}: esperado {tipo}, actual {tipo_actual}")
        else:
            print(f"✓ {col}: {tipo}")
```

### 5.2 Convertir Tipos

```python
# A categórico (ahorra memoria)
df['departamento'] = df['departamento'].astype('category')

# A booleano
df['activo'] = df['activo'].map({'Sí': True, 'No': False})

# A numérico (forzando errores a NaN)
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
```

### 5.3 Rangos Válidos

```python
# Función de validación
def validar_rangos(df, columna, min_val, max_val):
    invalidos = df[(df[columna] < min_val) | (df[columna] > max_val)]

    if len(invalidos) > 0:
        print(f"⚠️ {len(invalidos)} valores fuera de rango en '{columna}'")
        print(f"   Rango válido: [{min_val}, {max_val}]")
        print(f"   Valores inválidos: {invalidos[columna].tolist()}")
    else:
        print(f"✓ '{columna}' dentro de rango [{min_val}, {max_val}]")

# Aplicar
validar_rangos(df, 'edad', 18, 100)
validar_rangos(df, 'satisfaccion', 1, 10)
```

---

## Paso 6: Documentación de Transformaciones

### 6.1 Registro de Cambios

```python
import datetime

# Crear log de transformaciones
log_transformaciones = []

def registrar_transformacion(descripcion):
    """Registra cada transformación aplicada"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_transformaciones.append({
        'timestamp': timestamp,
        'transformacion': descripcion
    })
    print(f"📝 [{timestamp}] {descripcion}")

# Ejemplo de uso
registrar_transformacion("Eliminadas 15 filas duplicadas")
registrar_transformacion("Imputada columna 'edad' con mediana (28 años)")
registrar_transformacion("Detectados y eliminados 7 outliers en 'salario'")

# Exportar log
log_df = pd.DataFrame(log_transformaciones)
log_df.to_csv('log_limpieza_datos.csv', index=False)
```

### 6.2 Comparación Antes/Después

```python
# Función de resumen
def resumen_limpieza(df_original, df_limpio):
    """
    Compara dataset original vs limpio
    """
    print("=" * 60)
    print("📊 RESUMEN DE LIMPIEZA DE DATOS")
    print("=" * 60)

    print(f"\n🔢 Dimensiones:")
    print(f"   Original: {df_original.shape}")
    print(f"   Limpio:   {df_limpio.shape}")
    print(f"   Filas eliminadas: {df_original.shape[0] - df_limpio.shape[0]}")
    print(f"   Columnas eliminadas: {df_original.shape[1] - df_limpio.shape[1]}")

    print(f"\n❓ Valores faltantes:")
    print(f"   Original: {df_original.isnull().sum().sum()}")
    print(f"   Limpio:   {df_limpio.isnull().sum().sum()}")

    print(f"\n🔁 Duplicados:")
    print(f"   Original: {df_original.duplicated().sum()}")
    print(f"   Limpio:   {df_limpio.duplicated().sum()}")

    print("\n" + "=" * 60)

# Usar antes de guardar
resumen_limpieza(df_original, df_clean)
```

---

## Checklist de Limpieza

Use esta lista para verificar que todos los pasos se han completado:

### ✅ Pre-Limpieza
- [ ] Dataset cargado correctamente
- [ ] Exploración inicial completada
- [ ] Copia de respaldo creada (`df_original = df.copy()`)

### ✅ Valores Faltantes
- [ ] Identificados valores faltantes
- [ ] Estrategia de imputación decidida
- [ ] Transformaciones aplicadas y documentadas

### ✅ Outliers
- [ ] Outliers detectados (IQR o Z-score)
- [ ] Visualizaciones creadas
- [ ] Decisión tomada (eliminar/transformar/mantener)

### ✅ Formatos
- [ ] Texto normalizado (mayúsculas/minúsculas)
- [ ] Fechas convertidas a datetime
- [ ] Números limpiados de caracteres especiales

### ✅ Tipos de Datos
- [ ] Tipos verificados
- [ ] Conversiones aplicadas
- [ ] Rangos validados

### ✅ Duplicados
- [ ] Duplicados identificados
- [ ] Duplicados eliminados (si aplica)

### ✅ Documentación
- [ ] Log de transformaciones creado
- [ ] Comparación antes/después generada
- [ ] Dataset limpio exportado

### ✅ Post-Limpieza
- [ ] Verificación final de estructura
- [ ] Dataset guardado (`df_clean.to_csv('datos_limpios.csv', index=False)`)
- [ ] Notebook/script documentado con comentarios

---

## 📚 Recursos Adicionales

**Libros:**
- "Python for Data Analysis" - Wes McKinney
- "Data Cleaning" - Ihab Ilyas & Xu Chu

**Documentación:**
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Pandas Missing Data](https://pandas.pydata.org/docs/user_guide/missing_data.html)

**Tutoriales:**
- [Real Python: Data Cleaning](https://realpython.com/python-data-cleaning-numpy-pandas/)
- [Kaggle Learn: Data Cleaning](https://www.kaggle.com/learn/data-cleaning)

---

## 💡 Consejos Finales

1. **Siempre haz una copia:** `df_clean = df.copy()` antes de modificar
2. **Documenta TODO:** Cada decisión debe estar justificada
3. **Visualiza primero:** Gráficas revelan patrones que números no muestran
4. **No elimines automáticamente:** Analiza por qué faltan datos
5. **Valida con experto del dominio:** La limpieza requiere contexto del negocio
6. **Prueba diferentes estrategias:** Compara resultados de imputación vs eliminación
7. **Mantén versiones:** `datos_v1.csv`, `datos_v2_limpio.csv`

---

**Última actualización:** Enero 2025
**Curso:** CD2001B - Diagnóstico para Líneas de Acción
**Autor:** Tecnológico de Monterrey
