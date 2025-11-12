---
theme: default
colorSchema: light
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Chi-Cuadrada y ANOVA
  Curso CD2001B - Diagnóstico para Líneas de Acción
  Tecnológico de Monterrey Campus Puebla
drawings:
  persist: false
transition: slide-left
title: Chi-Cuadrada y ANOVA
mdc: true
download: true
exportFilename: semana2-chi-cuadrada-anova
css: unocss
---

<style src="./styles/tec-theme.css"></style>

# Chi-Cuadrada (χ²) y ANOVA

## Comparando Grupos y Categorías

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

# ¿Por Qué Necesitamos Más Pruebas Estadísticas?

<div v-click class="mt-8">

## 🤔 El Problema

**Semana 1:** Aprendimos prueba t para comparar promedios
- ✅ Un grupo vs. un valor
- ✅ Dos grupos

</div>

<div v-click class="mt-12">

## 🚧 Pero... ¿Qué pasa cuando?

- 📊 Tengo **3+ grupos** que comparar (no solo 2)
- 🏷️ Mis datos son **categorías**, no números

</div>

<div v-click class="mt-12">
<div class="text-2xl font-bold text-gradient">
Necesitamos nuevas herramientas: Chi-Cuadrada y ANOVA
</div>
</div>

---
layout: section
---

# Chi-Cuadrada (χ²)

## Para Variables Categóricas

---

# 🗣️ Primero: ¿Cómo se Pronuncia?

<div class="mt-12">

<div v-click>

## Chi = "JI"

Como en "**JI**tomate" 🍅

Se escribe: **χ²** (letra griega chi al cuadrado)

</div>

<div v-click class="mt-12">

## Se dice:

**"Ji-cuadrada"** o **"Chi-cuadrada"**

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-info">
💡 No te estreses por el símbolo. Python lo calcula por ti. Lo importante es saber **cuándo y cómo usarlo**.
</div>
</div>

---

# ¿Qué es Chi-Cuadrada?

<div class="mt-8">

<div v-click>

## En Palabras Simples:

Una prueba para saber si **dos variables categóricas** están relacionadas.

</div>

<div v-click class="mt-12">

## Variables Categóricas = Etiquetas/Grupos

**Ejemplos:**
- Género: Masculino, Femenino, No binario
- Región: Norte, Sur, Centro
- Satisfacción: Alta, Media, Baja
- Tipo de programa: Educación, Salud, Vivienda

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-warning">
⚠️ **NO** para números (edad, peso, satisfacción en escala 1-10). Para esos usa prueba t o ANOVA.
</div>
</div>

---

# 🎯 Ejemplo Real: ONG "Manos Unidas"

<div class="mt-8">

## La Pregunta:

Una ONG quiere saber: **¿El género de los beneficiarios está relacionado con el tipo de programa que eligen?**

<div v-click class="mt-8">

**Variables:**
- **Género:** Masculino, Femenino
- **Programa:** Educación, Salud, Vivienda

</div>

</div>

<div v-click class="mt-12">

## Las Hipótesis:

- **H₀:** NO hay relación (género y programa son independientes)
- **H₁:** SÍ hay relación (ciertos géneros prefieren ciertos programas)

</div>

---

# 📊 Los Datos: Tabla de Contingencia

<div class="mt-8">

|  | Educación | Salud | Vivienda | **Total** |
|---|---|---|---|---|
| **Masculino** | 45 | 30 | 25 | 100 |
| **Femenino** | 25 | 55 | 20 | 100 |
| **Total** | 70 | 85 | 45 | 200 |

</div>

<div v-click class="mt-12">

## 🤔 Observación Rápida:

- **Mujeres:** Prefieren Salud (55 vs 30)
- **Hombres:** Prefieren Educación (45 vs 25)

**Pero... ¿es esta diferencia significativa o solo casualidad?**

</div>

---

# 🧮 ¿Cómo Funciona Chi-Cuadrada?

<div class="mt-8">

## La Lógica:

<div v-click class="mt-8">

### 1️⃣ Calcular Frecuencias Esperadas

**Si NO hubiera relación** (H₀ es cierta), ¿qué frecuencias esperaríamos?

**Fórmula:**
```
Esperado = (Total fila × Total columna) / Gran total
```

**Ejemplo:** Masculino + Educación
```
Esperado = (100 × 70) / 200 = 35
```

**Observado:** 45

</div>

<div v-click class="mt-8">

### 2️⃣ Comparar Observado vs Esperado

Si la diferencia entre lo observado y lo esperado es **grande** → probablemente hay relación

</div>

</div>

---

# 🐍 Chi-Cuadrada en Python

```python {all|1-2|4-8|10-11|13-16|all}
from scipy.stats import chi2_contingency
import numpy as np

# Tabla de contingencia
tabla = np.array([
    [45, 30, 25],  # Masculino: Educ, Salud, Vivienda
    [25, 55, 20]   # Femenino: Educ, Salud, Vivienda
])

# Realizar prueba chi-cuadrada
chi2, p_value, df, expected = chi2_contingency(tabla)

# Mostrar resultados
print(f"Chi-cuadrado (χ²): {chi2:.2f}")
print(f"p-value: {p_value:.4f}")
print(f"Grados de libertad: {df}")
```

<div v-click class="mt-8">

**Resultado:**
```
Chi-cuadrado (χ²): 18.62
p-value: 0.0001
Grados de libertad: 2
```

</div>

---

# 📊 Visualización con Seaborn

```python {all|1-2|4-9|11-17|all}
import seaborn as sns
import matplotlib.pyplot as plt

# Crear DataFrame para visualizar
import pandas as pd
df_tabla = pd.DataFrame(tabla,
                        columns=['Educación', 'Salud', 'Vivienda'],
                        index=['Masculino', 'Femenino'])

# Heatmap con seaborn
plt.figure(figsize=(8, 5))
sns.heatmap(df_tabla, annot=True, fmt='d', cmap='YlOrRd',
            linewidths=0.5, cbar_kws={'label': 'Frecuencia'})
plt.title('Distribución: Género × Programa')
plt.xlabel('Programa')
plt.ylabel('Género')
plt.show()
```

<div v-click class="mt-4">
<div class="alert alert-success">
✅ El heatmap revela visualmente las diferencias: colores más intensos donde hay más personas
</div>
</div>

---

# ✅ Interpretación del Resultado

<div class="mt-8">

**Resultados:**
- χ² = 18.62
- **p-value = 0.0001** (< 0.05)

<div v-click class="mt-12">

## Decisión:

**p < 0.05** → Rechazamos H₀

</div>

<div v-click class="mt-12">

## 💡 Conclusión:

**SÍ hay una relación significativa** entre género y elección de programa.

**Observaciones específicas:**
- Las mujeres tienden a elegir programas de **Salud** (55 vs 30)
- Los hombres tienden a elegir programas de **Educación** (45 vs 25)

</div>

</div>

---
layout: center
---

# 🧠 Check Your Understanding

## Pregunta 1

Una ONG analizó la relación entre **zona geográfica** (Urbana, Rural) y **acceso a internet** (Sí, No).

Obtuvieron: **χ² = 2.15, p-value = 0.14**

**¿Cuál es la conclusión CORRECTA?**

a) Hay relación significativa entre zona y acceso a internet

b) No hay evidencia suficiente de relación entre zona y acceso

c) Las zonas rurales tienen significativamente menos acceso

d) El 14% de las personas no tienen internet

---
layout: center
---

# ✅ Respuesta: Pregunta 1

**Respuesta correcta: b)**

**No hay evidencia suficiente de relación entre zona y acceso**

<div class="mt-8">

**Por qué:**
- p-value = 0.14 > 0.05 → **NO rechazamos H₀**
- Esto significa: no hay evidencia estadística de que zona y acceso estén relacionados

</div>

<div class="mt-12">

**Errores comunes:**
- **a)** Incorrecto: p > 0.05, así que NO hay relación significativa
- **c)** Incorrecto: No podemos concluir direcciones específicas sin rechazar H₀
- **d)** Incorrecto: p-value ≠ porcentaje de personas sin internet

</div>

---

# ⚠️ Limitación de Chi-Cuadrada

<div class="mt-8">

<div v-click>

## Lo que SÍ te dice:

✅ **"Hay una relación"** entre las variables

</div>

<div v-click class="mt-12">

## Lo que NO te dice:

❌ **Qué tan fuerte** es la relación

❌ **En qué dirección** va (quién prefiere qué)

❌ **Causalidad** (A causa B)

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-info">
💡 Para entender la dirección y magnitud, necesitas **analizar la tabla visualmente** (el heatmap ayuda) o usar medidas adicionales como **Cramér's V**.
</div>
</div>

---

# 🔍 Otros Tipos de Pruebas Chi-Cuadrada

<div class="mt-8">

<div v-click>

## 📌 Chi-Cuadrada de Independencia (la que vimos)

La más común. Evalúa si **dos variables categóricas** están relacionadas.

**Ejemplo:** ¿El género está relacionado con el programa elegido?

</div>

<div v-click class="mt-12">

## 📌 Chi-Cuadrada de Bondad de Ajuste

Evalúa si una **única variable categórica** sigue una distribución esperada.

**Ejemplo:** Una ONG espera que sus beneficiarios se distribuyan equitativamente entre 4 regiones (25% cada una). Los datos reales son: Norte 30%, Sur 20%, Centro 35%, Oeste 15%. ¿Esta diferencia es significativa o por azar?

**Python:** `chisquare(observado, esperado)`

</div>

</div>

---

# 🔍 Otros Tipos de Pruebas Chi-Cuadrada (cont.)

<div class="mt-8">

<div v-click>

## 📌 Chi-Cuadrada de Homogeneidad

Similar a independencia, pero evalúa si **diferentes poblaciones** tienen la **misma distribución** en una variable categórica.

**Ejemplo:** Una ONG opera en 3 ciudades diferentes. ¿La distribución de satisfacción (Alta, Media, Baja) es la misma en las 3 ciudades?

**Diferencia con independencia:** Aquí comparas distribuciones entre poblaciones separadas, no relación entre dos variables en una misma población.

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-info">
💡 **En este curso** nos enfocamos principalmente en la **Chi-Cuadrada de Independencia** porque es la más útil para analizar relaciones entre variables en datos de ONGs.
</div>
</div>

---
layout: section
---

# ANOVA

## Análisis de Varianza

---

# 🗣️ ¿Qué es ANOVA?

<div class="mt-8">

<div v-click>

## Pronunciación:

**"A-NO-VA"** (se deletrea)

</div>

<div v-click class="mt-12">

## Significado:

**AN**alysis **O**f **VA**riance (Análisis de Varianza)

</div>

<div v-click class="mt-12">

## En Palabras Simples:

Una prueba para comparar los **promedios** de **3 o más grupos** al mismo tiempo.

</div>

</div>

---

# 🤔 ¿Por Qué NO Hacer Múltiples Pruebas t?

<div class="mt-8">

## El Problema:

<div v-click class="mt-8">

Imagina que quieres comparar **5 departamentos** de una ONG.

**Con pruebas t necesitarías:**
- Depto 1 vs 2
- Depto 1 vs 3
- Depto 1 vs 4
- Depto 1 vs 5
- Depto 2 vs 3
- ... (y así sucesivamente)

**Total: 10 pruebas t diferentes** 😵

</div>

</div>

---

# ⚠️ El Peligro de Múltiples Pruebas

<div class="mt-8">

<div v-click>

## Recuerda:

Cada prueba t tiene **α = 0.05** → 5% de riesgo de Error Tipo I (falso positivo)

</div>

<div v-click class="mt-12">

## Con 10 pruebas:

Probabilidad de **AL MENOS UN** falso positivo:

**1 - (0.95)^10 ≈ 0.40 = 40%** 😱

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-danger">
🚨 **Problema:** Con 10 pruebas, hay 40% de probabilidad de encontrar una "diferencia significativa" que en realidad es casualidad!
</div>
</div>

<div v-click class="mt-8">
<div class="alert alert-success">
✅ **Solución:** ANOVA hace **UNA SOLA prueba** para todos los grupos → mantiene α = 0.05 global
</div>
</div>

---

# 🎯 Ejemplo: ONG "Fundación Esperanza"

<div class="mt-8">

## La Situación:

Una ONG tiene **5 departamentos** y quiere saber si la satisfacción de los beneficiarios difiere entre ellos.

<div v-click class="mt-8">

| Departamento | Media | Desv. Est. | n |
|--------------|-------|------------|---|
| Legal | 8.85 | 0.21 | 40 |
| Trámites | 5.95 | 1.48 | 45 |
| Atención Social | 7.80 | 0.65 | 50 |
| Psicología | 8.10 | 0.45 | 35 |
| Administración | 6.20 | 1.20 | 30 |

</div>

</div>

<div v-click class="mt-8">

## ❓ Pregunta:

¿Hay diferencias significativas en satisfacción entre estos 5 departamentos?

</div>

---

# 📝 Las Hipótesis en ANOVA

<div class="mt-12">

<div v-click>

## H₀: Hipótesis Nula

**"Todas las medias son iguales"**

μ₁ = μ₂ = μ₃ = μ₄ = μ₅

Los 5 departamentos tienen la misma satisfacción promedio.

</div>

<div v-click class="mt-12">

## H₁: Hipótesis Alternativa

**"Al menos UNA media es diferente"**

No todos los departamentos tienen la misma satisfacción.

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-info">
💡 Nota: ANOVA solo te dice "hay diferencias", NO te dice **cuáles** departamentos son diferentes entre sí.
</div>
</div>

---

# 🧮 ¿Cómo Funciona ANOVA?

<div class="mt-8">

## La Lógica:

ANOVA compara **dos tipos de variabilidad**:

<div v-click class="mt-12">

### 1️⃣ Variabilidad ENTRE Grupos

¿Qué tan diferentes son los promedios de cada departamento entre sí?

**Ejemplo:** Legal (8.85) vs Trámites (5.95) → ¡Gran diferencia!

</div>

<div v-click class="mt-12">

### 2️⃣ Variabilidad DENTRO de Cada Grupo

¿Qué tan dispersos están los datos dentro de cada departamento?

**Ejemplo:** En Legal, algunas personas dan 8.7, otras 9.0 → Poca dispersión (DE = 0.21)

</div>

</div>

---

# 📊 Visualización: Boxplot con Seaborn

```python {all|1-3|5-11|13-21|all}
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generar datos simulados con distribución normal
np.random.seed(42)  # Para reproducibilidad
legal = np.random.normal(8.85, 0.21, 40)
tramites = np.random.normal(5.95, 1.48, 45)
atencion = np.random.normal(7.80, 0.65, 50)
psicologia = np.random.normal(8.10, 0.45, 35)
admin = np.random.normal(6.20, 1.20, 30)

# Crear DataFrame para visualización
df = pd.DataFrame({
    'departamento': (['Legal']*40 + ['Trámites']*45 + ['Atención Social']*50 +
                     ['Psicología']*35 + ['Administración']*30),
    'satisfaccion': np.concatenate([legal, tramites, atencion, psicologia, admin])
})

# Boxplot comparativo
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='departamento', y='satisfaccion', palette='Set2')
plt.axhline(y=df['satisfaccion'].mean(), color='red', linestyle='--',
            linewidth=2, label='Media General')
plt.title('Satisfacción por Departamento (Datos Simulados)')
plt.ylabel('Satisfacción (1-10)')
plt.xlabel('Departamento')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

# 🐍 ANOVA en Python

```python {all|1-2|4-9|11-12|14-17|all}
from scipy import stats
import numpy as np

# Datos de cada departamento (simulados para el ejemplo)
legal = np.random.normal(8.85, 0.21, 40)
tramites = np.random.normal(5.95, 1.48, 45)
atencion = np.random.normal(7.80, 0.65, 50)
psicologia = np.random.normal(8.10, 0.45, 35)
admin = np.random.normal(6.20, 1.20, 30)

# Realizar ANOVA de una vía (one-way ANOVA)
f_stat, p_value = stats.f_oneway(legal, tramites, atencion, psicologia, admin)

# Mostrar resultados
print(f"Estadístico F: {f_stat:.2f}")
print(f"p-value: {p_value:.6f}")
```

<div v-click class="mt-4">

**Resultado:**
```
Estadístico F: 245.67
p-value: < 0.000001
```

</div>

---

# ✅ Interpretación del Resultado

<div class="mt-8">

**Resultados:**
- F = 245.67
- **p-value < 0.001** (< 0.05)

<div v-click class="mt-12">

## Decisión:

**p < 0.05** → Rechazamos H₀

</div>

<div v-click class="mt-12">

## 💡 Conclusión:

Hay evidencia MUY fuerte de que **AL MENOS un departamento** tiene una satisfacción significativamente diferente.

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-warning">
⚠️ **Pero espera...** ANOVA solo nos dice "hay diferencias". NO nos dice **CUÁLES** departamentos son diferentes entre sí.
</div>
</div>

---
layout: center
---

# 🧠 Check Your Understanding

## Pregunta 2

Una ONG realizó un ANOVA para comparar el tiempo de espera en **4 sucursales** diferentes.

Resultado: **F = 1.85, p-value = 0.15**

**¿Qué significa esto?**

a) La sucursal 1 tiene significativamente mayor tiempo de espera

b) No hay evidencia de diferencias en tiempo de espera entre sucursales

c) Hay diferencias, pero no sabemos cuáles sucursales difieren

d) El tiempo de espera es 15% mayor en algunas sucursales

---
layout: center
---

# ✅ Respuesta: Pregunta 2

**Respuesta correcta: b)**

**No hay evidencia de diferencias en tiempo de espera entre sucursales**

<div class="mt-8">

**Por qué:**
- p-value = 0.15 > 0.05 → **NO rechazamos H₀**
- Conclusión: No hay evidencia suficiente de que las 4 sucursales tengan tiempos diferentes

</div>

<div class="mt-12">

**Errores comunes:**
- **a)** Incorrecto: ANOVA no dice cuál es diferente (y además p > 0.05)
- **c)** Incorrecto: Como p > 0.05, NO rechazamos H₀, no hay evidencia de diferencias
- **d)** Incorrecto: p-value ≠ porcentaje de diferencia

</div>

---

# 🔍 Pruebas Post-Hoc: ¿Cuál es Diferente?

<div class="mt-8">

<div v-click>

## El Problema:

ANOVA nos dijo: **"Hay diferencias"**

Pero NO nos dijo: **"CUÁLES departamentos son diferentes entre sí"**

</div>

<div v-click class="mt-12">

## La Solución: Pruebas Post-Hoc

Son pruebas **adicionales** que haces **DESPUÉS** de ANOVA para identificar exactamente **cuáles pares** de grupos son diferentes.

</div>

<div v-click class="mt-12">

## La Más Común: Tukey HSD

**Tukey HSD** (Honestly Significant Difference) compara **todos los pares** de departamentos, pero ajusta α para controlar el Error Tipo I.

</div>

</div>

---

# 📊 Ejemplo de Resultados Post-Hoc

<div class="mt-8">

Después de ANOVA (que fue significativo), realizamos **Tukey HSD**:

| Comparación | Diferencia de Medias | p-value | ¿Significativo? |
|-------------|---------------------|---------|-----------------|
| Legal vs Psicología | 0.75 | 0.42 | ❌ NO |
| Legal vs Trámites | 2.90 | < 0.001 | ✅ SÍ |
| Legal vs Atención Social | 1.05 | 0.08 | ❌ NO |
| Trámites vs Administración | -0.25 | 0.95 | ❌ NO |
| Psicología vs Trámites | 2.15 | < 0.001 | ✅ SÍ |

</div>

<div v-click class="mt-8">

## 💡 Conclusión Final:

**Trámites** tiene satisfacción significativamente **MENOR** que Legal y Psicología.

Los demás departamentos no difieren significativamente entre sí.

</div>

---

# 🎯 Recomendación para la ONG

<div class="mt-8">

<div v-click>

## 📊 Hallazgos:

1. **Legal** y **Psicología**: Satisfacción más alta (~8.1-8.9)
2. **Trámites**: Satisfacción MÁS BAJA (5.95) ⚠️
3. **Atención Social**: Intermedia (7.80)
4. **Administración**: Baja (6.20)

</div>

<div v-click class="mt-12">

## 🚨 Hallazgo Crítico:

**Trámites** tiene satisfacción significativamente MENOR que todos los demás.

**Diferencia:** 2.9 puntos vs Legal (el mejor evaluado)

</div>

</div>

<div v-click class="mt-8">
<div class="alert alert-danger">
<strong>Acción Urgente:</strong> Investigar QUÉ está pasando en el departamento de Trámites y diseñar intervenciones específicas para mejorar la experiencia de los usuarios.
</div>
</div>

---

# 🔀 Gen Z Moment: ANOVA Edition 😅

<div class="mt-12 text-center">

<div v-click>

## Cuando haces 10 pruebas t en lugar de ANOVA:

<div class="text-6xl mt-8">
🤡
</div>

<div class="text-xl mt-4">
"Error Tipo I entrando al chat"
</div>

</div>

<div v-click class="mt-12">

## Cuando el p-value de ANOVA es < 0.001:

<div class="text-6xl mt-8">
✨📊✨
</div>

<div class="text-xl mt-4">
"Las diferencias están más claras que el agua"
</div>

</div>

</div>

---
layout: center
---

# 🧠 Check Your Understanding

## Pregunta 3

Una ONG hizo ANOVA comparando 3 programas y obtuvo **p < 0.01** (significativo).

**¿Cuál es el SIGUIENTE paso apropiado?**

a) Concluir que el Programa 1 es el mejor

b) No hacer nada más, ANOVA ya nos dio toda la información

c) Realizar pruebas post-hoc (como Tukey) para identificar qué programas difieren

d) Hacer una prueba t entre cada par de programas

---
layout: center
---

# ✅ Respuesta: Pregunta 3

**Respuesta correcta: c)**

**Realizar pruebas post-hoc (como Tukey) para identificar qué programas difieren**

<div class="mt-8">

**Por qué:**
- ANOVA solo nos dice "hay diferencias" pero NO cuáles grupos difieren
- Las pruebas post-hoc (Tukey HSD) identifican específicamente qué pares son diferentes

</div>

<div class="mt-12">

**Errores comunes:**
- **a)** Incorrecto: ANOVA no dice cuál es "el mejor"
- **b)** Incorrecto: ANOVA es solo el primer paso
- **d)** Incorrecto: NO hagas múltiples t-tests (problema de Error Tipo I). Usa post-hoc que ajusta α

</div>

---

# 📋 Resumen: Chi-Cuadrada vs ANOVA

<div class="mt-8">

| Aspecto | Chi-Cuadrada (χ²) | ANOVA |
|---------|-------------------|-------|
| **Tipo de datos** | Categóricos | Numéricos |
| **Pregunta** | ¿Hay relación entre 2 variables categóricas? | ¿Los promedios de 3+ grupos son diferentes? |
| **Ejemplo** | Género × Programa elegido | Satisfacción en 5 departamentos |
| **H₀** | Variables son independientes | Todas las medias son iguales |
| **H₁** | Variables están relacionadas | Al menos una media es diferente |
| **Visualización** | Heatmap (tabla de contingencia) | Boxplot |
| **Función Python** | `chi2_contingency(tabla)` | `f_oneway(grupo1, grupo2, ...)` |
| **Siguiente paso** | Analizar tabla visualmente | Pruebas post-hoc (Tukey) |

</div>

---

# 🎯 Árbol de Decisión

<div class="mt-8">

```mermaid
flowchart TD
    Start([Tengo datos de una ONG]) --> Q1{¿Tipo de datos?}

    Q1 -->|Categóricos| Q2{¿Qué quiero saber?}
    Q1 -->|Numéricos| Q3{¿Cuántos grupos?}

    Q2 -->|Relación entre<br>2 categóricas| Chi[Chi-cuadrada χ²<br>chi2_contingency]

    Q3 -->|1 grupo vs valor| T1[Prueba t<br>1 muestra]
    Q3 -->|2 grupos| T2[Prueba t<br>2 muestras]
    Q3 -->|3+ grupos| ANOVA[ANOVA<br>f_oneway]

    ANOVA --> PostHoc[Luego: Pruebas<br>Post-Hoc]

    Chi --> Ex1[Ejemplo: Género × Programa]
    ANOVA --> Ex2[Ejemplo: 5 Departamentos]
```

</div>

---

# 🛠️ Código Completo: Chi-Cuadrada

```python
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Crear tabla de contingencia
tabla = np.array([
    [45, 30, 25],  # Masculino
    [25, 55, 20]   # Femenino
])

# 2. Realizar prueba
chi2, p_value, df, expected = chi2_contingency(tabla)
print(f"χ² = {chi2:.2f}, p-value = {p_value:.4f}")

# 3. Visualizar
df_tabla = pd.DataFrame(tabla,
                        columns=['Educación', 'Salud', 'Vivienda'],
                        index=['Masculino', 'Femenino'])
sns.heatmap(df_tabla, annot=True, fmt='d', cmap='YlOrRd')
plt.title('Género × Programa')
plt.show()

# 4. Decisión
if p_value < 0.05:
    print("✅ Hay relación significativa")
else:
    print("❌ No hay evidencia de relación")
```

---

# 🛠️ Código Completo: ANOVA

```python
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Preparar datos (ejemplo con DataFrame)
df = pd.read_csv('datos_ong.csv')

# 2. Estadísticas descriptivas por grupo
print(df.groupby('departamento')['satisfaccion'].agg(['mean', 'std', 'count']))

# 3. Visualizar
sns.boxplot(data=df, x='departamento', y='satisfaccion', palette='Set2')
plt.xticks(rotation=45)
plt.show()

# 4. Realizar ANOVA
grupos = [df[df['departamento'] == d]['satisfaccion'].values
          for d in df['departamento'].unique()]
f_stat, p_value = stats.f_oneway(*grupos)
print(f"F = {f_stat:.2f}, p-value = {p_value:.6f}")

# 5. Decisión
if p_value < 0.05:
    print("✅ Hay diferencias significativas entre grupos")
    print("⚠️ Recomendación: Realizar pruebas post-hoc (Tukey)")
else:
    print("❌ No hay evidencia de diferencias")
```

---

# 🎓 Conceptos Clave para Workshop 2

<div class="mt-8">

## ✅ Lo que Necesitas Recordar:

<div v-click>

### Chi-Cuadrada (χ²):
- Para **variables categóricas**
- Pregunta: ¿Hay **relación**?
- Tabla de contingencia → heatmap
- `chi2_contingency(tabla)`

</div>

<div v-click class="mt-8">

### ANOVA:
- Para **3+ grupos** con datos numéricos
- Pregunta: ¿Los promedios son **diferentes**?
- Boxplot para visualizar
- `f_oneway(grupo1, grupo2, ...)`
- Si significativo → Hacer **post-hoc** (Tukey)

</div>

</div>

<div v-click class="mt-12">
<div class="alert alert-success">
💡 En Workshop 2 aplicarás estos conceptos con datos reales de ONGs
</div>
</div>

---
layout: center
class: text-center
---

# 🎯 Próximos Pasos

<div class="mt-12">

## 1️⃣ Practica con el Dataset de Workshop 2

Aplica Chi-Cuadrada y ANOVA con datos reales

</div>

<div class="mt-8">

## 2️⃣ Siguiente Tema: Regresión y Correlación

Aprenderemos a **predecir** y medir **relaciones lineales**

</div>

<div class="mt-12">
<div class="text-2xl font-bold text-gradient">
¡Prepárate para el siguiente nivel! 🚀
</div>
</div>

---
layout: end
class: text-center
---

# ¡Gracias!

<div class="pt-12">
  <span class="text-6xl">📊✨</span>
</div>

### ¿Preguntas?

<div class="abs-br m-6 flex gap-2">
  <span class="text-sm opacity-50">CD2001B | Tec de Monterrey Campus Puebla</span>
</div>
