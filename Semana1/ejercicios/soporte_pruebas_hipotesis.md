# 📘 Guía de Soporte: Pruebas de Hipótesis

> **Para:** Ejercicio Práctico de Pruebas de Hipótesis
> **Usa este documento como referencia** mientras trabajas en el ejercicio

---

## 🎯 ¿Qué es una Prueba de Hipótesis?

Es un método para **tomar decisiones basadas en datos**. Básicamente respondes la pregunta:

> *"¿Lo que veo en mis datos es real, o solo fue casualidad?"*

**Ejemplo del día a día:**
- Lanzas una moneda 10 veces y sale **8 veces cara**
- **Pregunta:** ¿La moneda está trucada o solo tuve suerte?
- **Respuesta:** Una prueba de hipótesis te ayuda a decidir

---

## 📋 Los 6 Pasos (Siempre los Mismos)

### Paso 1: Plantear las Hipótesis

Siempre hay **DOS hipótesis**:

**H₀ (Hipótesis Nula)** = "No pasa nada especial" / "Todo es normal"
- Es como la "posición escéptica"
- Ejemplo: "La satisfacción promedio ES 8.0"

**H₁ (Hipótesis Alternativa)** = "Sí pasa algo" / "Hay un efecto"
- Es lo que queremos probar
- Ejemplo: "La satisfacción promedio NO ES 8.0"

**💡 Tip:** Siempre empieza asumiendo que H₀ es verdadera (como "inocente hasta que se pruebe lo contrario")

---

### Paso 2: Establecer el Nivel de Significancia (α)

**α = 0.05** (esto es estándar)

Significa: "Acepto un 5% de riesgo de equivocarme"

**En palabras simples:** Si hago esta prueba 100 veces, me equivocaré máximo 5 veces.

---

### Paso 3: Calcular el Estadístico de Prueba

Aquí es donde Python hace el trabajo pesado. Usarás funciones como:

```python
stats.ttest_1samp(datos, valor_a_comparar)  # Para 1 muestra
stats.ttest_ind(grupo1, grupo2)             # Para 2 grupos
```

Estas funciones calculan un número llamado **t-statistic**. No te preocupes por la fórmula, Python lo hace por ti.

---

### Paso 4: Obtener el p-value

El **p-value** es EL NÚMERO MÁS IMPORTANTE. Te dice:

> *"¿Qué tan probable es obtener estos datos si H₀ fuera cierta?"*

**Regla de oro:**
- **p-value < 0.05** → Los datos son muy raros si H₀ es cierta → **Rechazamos H₀**
- **p-value ≥ 0.05** → Los datos son normales bajo H₀ → **NO rechazamos H₀**

---

### Paso 5: Tomar la Decisión

```python
if p_value < 0.05:
    print("Rechazamos H₀")
else:
    print("No rechazamos H₀")
```

**⚠️ IMPORTANTE:**
- NO digas "aceptamos H₀"
- Di "NO rechazamos H₀" (no es lo mismo)

**Analogía:** Es como un juicio. "No culpable" ≠ "Inocente"

---

### Paso 6: Interpretar en Contexto

**Este es el paso más importante para la ONG.**

No basta con decir "rechazamos H₀". Debes explicar:
- ¿Qué significa esto para la organización?
- ¿Qué acciones deben tomar?

**Ejemplo:**
❌ Malo: "Rechazamos H₀"
✅ Bueno: "Rechazamos H₀. La satisfacción promedio (7.2) es significativamente menor que la meta (8.0). Recomendamos investigar las causas y diseñar mejoras en el servicio."

---

## 🔍 Tipos de Pruebas t

### 1️⃣ Prueba t de Una Muestra

**¿Cuándo usarla?**
- Tienes UN GRUPO de datos
- Quieres compararlo con un VALOR CONOCIDO

**Ejemplo:**
- Tengo 200 encuestas de satisfacción
- La meta de la ONG es 8.0
- **Pregunta:** ¿Mi promedio es diferente de 8.0?

**Código:**
```python
from scipy import stats

t_stat, p_value = stats.ttest_1samp(df['satisfaccion'], 8.0)
```

**Hipótesis:**
- H₀: μ = 8.0
- H₁: μ ≠ 8.0

---

### 2️⃣ Prueba t de Dos Muestras Independientes

**¿Cuándo usarla?**
- Tienes DOS GRUPOS DIFERENTES de personas
- Quieres comparar sus promedios

**Ejemplo:**
- Grupo 1: Hombres
- Grupo 2: Mujeres
- **Pregunta:** ¿Su satisfacción promedio es diferente?

**Código:**
```python
grupo1 = df[df['genero'] == 'Masculino']['satisfaccion']
grupo2 = df[df['genero'] == 'Femenino']['satisfaccion']

t_stat, p_value = stats.ttest_ind(grupo1, grupo2)
```

**Hipótesis:**
- H₀: μ₁ = μ₂ (los promedios son iguales)
- H₁: μ₁ ≠ μ₂ (los promedios son diferentes)

---

## 🎯 Pruebas Bilaterales vs Unilaterales

### Prueba Bilateral (Two-tailed) ↔️

**¿Cuándo?** Cuando preguntas si algo es **DIFERENTE** (puede ser mayor O menor)

**Palabras clave:** "diferente", "distinto", "no igual"

**Ejemplo:** ¿La satisfacción es diferente de 8.0? (puede ser 7 o 9, no importa)

**Hipótesis:**
- H₀: μ = 8.0
- H₁: μ ≠ 8.0

**Código:** (Python hace esto por defecto)
```python
t_stat, p_value = stats.ttest_1samp(datos, 8.0)
# El p_value ya es bilateral
```

---

### Prueba Unilateral (One-tailed) ↗️ o ↘️

**¿Cuándo?** Cuando preguntas si algo es **MAYOR** o **MENOR** (una dirección específica)

**Palabras clave:** "mayor que", "menor que", "supera", "por debajo de"

**Ejemplo:** ¿El tiempo de espera es MAYOR a 30 minutos? (solo nos importa si excede)

**Hipótesis:**
- H₀: μ ≤ 30
- H₁: μ > 30

**Código:**
```python
t_stat, p_value_bilateral = stats.ttest_1samp(datos, 30)
# Para unilateral, divide entre 2
p_value = p_value_bilateral / 2
```

**⚠️ Extra:** Asegúrate de que t_stat tenga el signo correcto:
- Si preguntas "mayor que", t_stat debe ser positivo
- Si preguntas "menor que", t_stat debe ser negativo

---

## 📊 Verificación de Supuestos

Las pruebas t **asumen** ciertas cosas sobre tus datos. Debes verificarlas.

### Supuesto 1: Normalidad

**¿Qué significa?** Los datos deben tener forma de "campana" (distribución normal)

**¿Cómo verificarlo?**

**Opción A: Prueba de Shapiro-Wilk**
```python
from scipy import stats

stat, p_value = stats.shapiro(df['satisfaccion'])

if p_value > 0.05:
    print("✓ Los datos son normales")
else:
    print("⚠️ Los datos NO son normales")
```

**Hipótesis:**
- H₀: Los datos son normales
- H₁: Los datos NO son normales

**Opción B: Q-Q Plot (visual)**
```python
from scipy.stats import probplot

probplot(df['satisfaccion'], dist="norm", plot=plt)
plt.show()
```

**¿Cómo interpretar el Q-Q Plot?**
- Si los puntos siguen la línea diagonal → **Los datos son normales** ✓
- Si se desvían mucho → **No son normales** ⚠️

**💡 Buena noticia:** Si tu muestra es grande (n > 30), la prueba t es **robusta** aunque los datos no sean perfectamente normales.

---

### Supuesto 2: Homogeneidad de Varianzas

**Solo para pruebas de 2 muestras**

**¿Qué significa?** Los dos grupos deben tener variabilidad similar

**¿Cómo verificarlo?**

**Prueba de Levene:**
```python
stat, p_value = stats.levene(grupo1, grupo2)

if p_value > 0.05:
    print("✓ Las varianzas son iguales")
else:
    print("⚠️ Las varianzas son diferentes")
```

**Hipótesis:**
- H₀: Las varianzas son iguales
- H₁: Las varianzas son diferentes

**Si las varianzas NO son iguales:**
```python
# Usa equal_var=False
t_stat, p_value = stats.ttest_ind(grupo1, grupo2, equal_var=False)
```

---

## 🛠️ Funciones de Python que Necesitas

### Importar librerías
```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
```

### Estadísticas descriptivas
```python
df['columna'].mean()      # Promedio
df['columna'].std()       # Desviación estándar
df['columna'].count()     # Cantidad de datos
len(df)                   # Tamaño del dataframe
```

### Filtrar datos
```python
# Filtrar un grupo
grupo = df[df['columna'] == 'valor']

# Ejemplo
hombres = df[df['genero'] == 'Masculino']
```

### Agrupar y resumir
```python
df.groupby('columna')['otra_columna'].agg(['mean', 'std', 'count'])
```

### Pruebas estadísticas
```python
# Prueba t de 1 muestra
t_stat, p_value = stats.ttest_1samp(datos, valor_a_comparar)

# Prueba t de 2 muestras
t_stat, p_value = stats.ttest_ind(grupo1, grupo2)

# Prueba de normalidad
stat, p_value = stats.shapiro(datos)

# Prueba de homogeneidad de varianzas
stat, p_value = stats.levene(grupo1, grupo2)
```

---

## ❓ Preguntas Frecuentes

### 1. ¿Qué es el t-statistic?

Es un número que mide **qué tan lejos está tu resultado del valor esperado**.

- **t grande** (en valor absoluto) → tu resultado está MUY lejos de H₀ → probablemente rechaces H₀
- **t pequeño** → tu resultado está cerca de H₀ → probablemente NO rechaces H₀

**No necesitas interpretarlo directamente, usa el p-value.**

---

### 2. ¿Por qué α = 0.05?

Es una convención. Significa que aceptamos un 5% de riesgo de **Error Tipo I** (rechazar H₀ cuando es verdadera).

**En contextos críticos** (medicina, seguridad) a veces se usa α = 0.01 (más estricto).

---

### 3. ¿Qué significa "estadísticamente significativo"?

Significa que el p-value < 0.05, y por tanto, rechazamos H₀.

**Importante:** "Estadísticamente significativo" NO siempre significa "importante en la práctica".

**Ejemplo:**
- Diferencia de 0.01 puntos puede ser estadísticamente significativa con n=10,000
- Pero 0.01 puntos no es importante para la ONG

---

### 4. ¿Cuándo uso bilateral vs unilateral?

**Bilateral (99% de las veces):** Cuando preguntas "¿es diferente?"
**Unilateral:** Solo cuando tienes una razón específica para preguntar "¿es mayor?" o "¿es menor?"

**Regla práctica:** Si tienes duda, usa bilateral.

---

### 5. ¿Qué hago si los datos no son normales?

**Opciones:**
1. **Si n > 30:** No te preocupes, la prueba t es robusta
2. **Si n < 30:** Considera una prueba no paramétrica (Mann-Whitney U test)
3. **Transformación:** Aplica log o raíz cuadrada a los datos

---

## 📝 Checklist para Cada Prueba

Antes de decir "terminé", verifica:

- [ ] ✅ Planteé H₀ y H₁ claramente
- [ ] ✅ Identifiqué si es bilateral o unilateral
- [ ] ✅ Usé la función correcta de Python
- [ ] ✅ Obtuve t-statistic y p-value
- [ ] ✅ Comparé p-value con α = 0.05
- [ ] ✅ Tomé la decisión correcta (rechazar o no)
- [ ] ✅ Interpreté el resultado en contexto de la ONG
- [ ] ✅ Verifiqué supuestos (normalidad, varianzas)

---

## 🎯 Ejemplo Completo Paso a Paso

### Pregunta: ¿La satisfacción promedio es diferente de 8.0?

**Paso 1: Hipótesis**
```
H₀: μ = 8.0
H₁: μ ≠ 8.0
α = 0.05 (bilateral)
```

**Paso 2: Código**
```python
t_stat, p_value = stats.ttest_1samp(df['satisfaccion'], 8.0)
print(f"t = {t_stat:.4f}, p = {p_value:.4f}")
```

**Paso 3: Decisión**
```python
if p_value < 0.05:
    print("Rechazamos H₀")
else:
    print("No rechazamos H₀")
```

**Paso 4: Interpretación**
```
Supongamos que p = 0.032 (< 0.05)

"Rechazamos H₀. La satisfacción promedio (7.45) es
significativamente diferente de la meta de 8.0 puntos
(p = 0.032). La ONG no está cumpliendo su objetivo.
Recomendamos analizar las causas de insatisfacción
e implementar mejoras en el servicio."
```

---

## 🚨 Errores Comunes a Evitar

### ❌ Error 1: Decir "Aceptamos H₀"
**Correcto:** "No rechazamos H₀"

**Por qué:** No tener evidencia de algo ≠ probar que no existe

---

### ❌ Error 2: Confundir p-value con probabilidad de H₀
**Incorrecto:** "p = 0.03 significa que hay 3% de probabilidad de que H₀ sea cierta"

**Correcto:** "p = 0.03 significa que, si H₀ fuera cierta, habría 3% de probabilidad de obtener estos datos"

---

### ❌ Error 3: No verificar la dirección en pruebas unilaterales
Si preguntas "¿es mayor?" pero t_stat es negativo, NO rechaces H₀ aunque p/2 < 0.05

---

### ❌ Error 4: Olvidar el contexto
No digas solo "rechazamos H₀". Explica qué significa para la ONG.

---

## 📚 Recursos Adicionales

### Si te quedas atorado:

1. **Revisa los slides:** `semana1-pruebas-hipotesis-readable.md`
2. **Consulta la documentación:**
   - [scipy.stats.ttest_1samp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html)
   - [scipy.stats.ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
3. **Foro de Canvas:** Publica tu duda con el código que intentaste

---

## 💡 Consejo Final

> **La estadística no es sobre memorizar fórmulas.**
> **Es sobre pensar críticamente y contar historias con datos.**

Tu trabajo es:
1. Hacer las pruebas correctamente (Python te ayuda)
2. **Interpretar qué significan para la ONG** (esto es TU trabajo)

---

**¡Éxito en tu ejercicio!** 🎉

Si tienes dudas, revisa esta guía. Está aquí para ayudarte, no para darte las respuestas directamente, sino para que entiendas el **POR QUÉ** y el **CÓMO**.
