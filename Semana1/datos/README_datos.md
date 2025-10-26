# Datasets - Semana 1

## 📊 Descripción de Datasets

Esta carpeta contiene los datasets para practicar durante la Semana 1 del módulo.

---

## 📁 Archivos Disponibles

### 1. `ejemplo_satisfaccion_clientes.csv`

**Descripción:** Datos ficticios de satisfacción de clientes de una organización sin fines de lucro.

**Variables:**
- `id`: Identificador único del beneficiario
- `area`: Departamento o área de servicio (Norte, Sur, Este, Oeste)
- `edad`: Edad del beneficiario
- `genero`: Género (M, F, Otro)
- `tiempo_servicio`: Meses utilizando el servicio
- `satisfaccion`: Nivel de satisfacción (escala 1-10)
- `recomendaria`: ¿Recomendaría el servicio? (Sí/No)
- `calidad_atencion`: Calificación de atención recibida (1-10)
- `tiempo_espera`: Tiempo de espera promedio (minutos)

**Tamaño:** ~200 registros

**Uso:**
- Práctica de medidas de tendencia central
- Pruebas de hipótesis para una muestra
- Comparación entre áreas (prueba t independiente)

---

### 2. `alcohol_estudiantes.csv` (Para Workshop 1)

**Fuente:** https://www.kaggle.com/uciml/student-alcohol-consumption

**Descripción:** Datos de consumo de alcohol entre estudiantes portugueses.

**Variables seleccionadas:**
- `school`: Escuela (GP o MS)
- `sex`: Género (F o M)
- `age`: Edad
- `studytime`: Tiempo de estudio semanal
- `failures`: Número de reprobaciones pasadas
- `absences`: Número de ausencias
- `G1`, `G2`, `G3`: Calificaciones en diferentes periodos
- `Dalc`: Consumo de alcohol entre semana (1-5)
- `Walc`: Consumo de alcohol en fin de semana (1-5)

**Uso:**
- Workshop 1: Análisis exploratorio completo
- Identificación de correlaciones
- Pruebas de hipótesis múltiples

---

## 🔧 Cómo Cargar los Datos

### En Python con Pandas:

```python
import pandas as pd

# Opción 1: Ruta relativa (desde notebooks/)
df = pd.read_csv('../datos/ejemplo_satisfaccion_clientes.csv')

# Opción 2: Ruta absoluta
df = pd.read_csv('/ruta/completa/ejemplo_satisfaccion_clientes.csv')

# Ver primeras filas
print(df.head())

# Información del dataset
print(df.info())

# Estadísticas descriptivas
print(df.describe())
```

---

## 📝 Notas para Crear tu Propio Dataset

Si deseas generar datos sintéticos adicionales para practicar:

```python
import pandas as pd
import numpy as np

# Semilla para reproducibilidad
np.random.seed(42)

# Generar datos
n = 200
data = {
    'id': range(1, n+1),
    'area': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], n),
    'edad': np.random.randint(18, 70, n),
    'genero': np.random.choice(['M', 'F', 'Otro'], n, p=[0.48, 0.48, 0.04]),
    'satisfaccion': np.random.randint(1, 11, n),
    'calidad_atencion': np.random.randint(1, 11, n),
}

df = pd.DataFrame(data)
df.to_csv('mi_dataset.csv', index=False)
```

---

## ⚠️ Consideraciones Éticas

**Importante:** Todos los datasets de este curso son:
- Ficticios o públicos
- Anonimizados
- Para fines educativos únicamente

Cuando trabajes con datos reales de la ONG:
- Respeta la privacidad de los beneficiarios
- No compartas datos sensibles
- Cumple con regulaciones de protección de datos

---

## 📚 Recursos Adicionales

- [Pandas Cheat Sheet](../../recursos/cheat_sheet_pandas.pdf)
- [Guía de limpieza de datos](../../recursos/guia_limpieza_datos.md)
- [Kaggle Datasets](https://www.kaggle.com/datasets) - Para más práctica

---

**Nota:** Si encuentras errores en los datos o deseas sugerir nuevos datasets, contacta al profesor.
