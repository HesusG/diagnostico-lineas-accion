# Semana1 Pruebas Hipotesis

> **Curso:** CD2001B - Diagnóstico para Líneas de Acción
> **Tecnológico de Monterrey - Campus Puebla**

---

# Pruebas de Hipótesis

## Tomando Decisiones Basadas en Evidencia

    CD2001B - Diagnóstico para Líneas de Acción

  Semana 1 | Tec de Monterrey

---

# ¿Qué es una Hipótesis?

## 🤔 Empecemos con lo Básico

Una **hipótesis** es simplemente una **idea** o **suposición** sobre algo que queremos investigar.

### Ejemplos en la Vida Diaria:
- **"Creo que estudiar más horas me ayuda a tener mejores calificaciones"**
- **"Pienso que esta marca de café sabe mejor"**
- **"Esta ONG realmente está ayudando a la comunidad"**

💡 **Observa:** Todas estas son solo **ideas** o **creencias**. Aún no sabemos si son ciertas.

---

# ¿Qué es una Hipótesis Estadística?

## 📊 Hipótesis + Datos = Hipótesis Estadística

Es cuando tomamos una **idea** y la convertimos en algo que podemos **probar con números**.

### De Idea a Hipótesis Estadística:

**Idea vaga:** "Esta ONG es efectiva"

**Hipótesis estadística:** "El programa de la ONG redujo la desnutrición infantil de 35% a menos de 30%"

✅ **Lo importante:** Ahora tenemos **números específicos** que podemos medir y comparar

---

# El Propósito: ¿Por Qué Hacemos Esto?

### 🎯 No se Trata de "Tener Razón"

Cuando hacemos una prueba de hipótesis, **NO** estamos tratando de demostrar que nuestras ideas son correctas.

### 🔍 Se Trata de Evaluar la Evidencia

Queremos saber: **¿Los datos que tenemos apoyan nuestra idea, o no?**

⚠️ **Ojo:** A veces los datos nos dirán que nuestra idea original estaba equivocada. ¡Y eso está bien! Es parte del proceso científico.

---

# 💡 Analogía para Entender Mejor

## Imagina un Juicio Legal

Cuando un juez evalúa un caso, funciona de manera **muy similar** a una prueba de hipótesis.

Veamos cómo...

---

# ⚖️ En un Juicio Legal

### 1. Presunción de Inocencia

**"El acusado es inocente hasta que se pruebe lo contrario"**

### 2. Carga de la Prueba

El fiscal debe presentar **evidencia convincente** para cambiar el veredicto.

### 3. El Veredicto

- ✅ **Culpable** → Si hay evidencia suficiente
- ❌ **No culpable** → Si la evidencia NO es suficiente

💡 Observa que "No culpable" NO significa "Inocente". Solo significa: "No hay suficiente evidencia para condenar"

---

# 📊 En una Prueba de Hipótesis

### 1. H₀: Hipótesis Nula (Presunción de Inocencia)

**"No hay efecto / No hay diferencia"**

Es como decir: "Asumimos que nada cambió, hasta que los datos demuestren lo contrario"

### 2. H₁: Hipótesis Alternativa (La Acusación)

**"SÍ hay efecto / SÍ hay diferencia"**

Es la afirmación que queremos probar con nuestros datos.

⚠️ **Dato importante:** Al igual que en el juicio, empezamos asumiendo que H₀ es cierta (igual que la presunción de inocencia).

---

# 🎯 La Decisión Final

### Basándonos en la Evidencia (Datos)

**Si la evidencia es suficiente:**
- ✅ Rechazamos H₀
- Concluimos que **SÍ** hay efecto

**Si la evidencia NO es suficiente:**
- ❌ NO rechazamos H₀
- Concluimos que **NO tenemos evidencia** de un efecto

**MUY IMPORTANTE:** "No rechazar H₀" ≠ "Aceptar H₀"

Solo significa: **"No hay suficiente evidencia"**

(Igual que "No culpable" ≠ "Inocente")

---

# 📚 Ejemplo Práctico: ONG "Comedores Comunitarios"

## 📋 La Situación

Una ONG implementó un programa de comedores comunitarios para niños en una comunidad vulnerable.

### Lo que la ONG afirma:

**"Nuestro programa redujo la desnutrición infantil en la comunidad"**

💡 Pero necesitamos **evidencia numérica** para verificar esta afirmación.

---

# 📊 Los Datos del Programa

### Mediciones Realizadas:

**🔴 ANTES del programa:**
- Tasa de desnutrición infantil: **35%**

**🟢 DESPUÉS del programa:**
- Tasa de desnutrición infantil: **28%**
- Medido en una muestra de **150 niños**

**📉 Diferencia observada:** 35% - 28% = **7 puntos porcentuales**

---

# 🤔 La Pregunta Crítica

## ¿Esta reducción de 7% es REAL?

### Hay dos posibles explicaciones:

**1. 🎯 El programa realmente funciona**
- La reducción es un efecto genuino del programa

**2. 🎲 Es solo casualidad**
- La muestra aleatoriamente tuvo menos casos de desnutrición
- El programa en realidad no tuvo ningún efecto

**¡Aquí entra la Prueba de Hipótesis!**

Nos ayuda a decidir cuál de estas dos explicaciones es más probable, usando **rigor estadístico**.

---

# Paso 1: Plantear las Hipótesis

### Ahora vamos a formalizar las dos posibles explicaciones

### 🔵 H₀: Hipótesis Nula

**"El programa NO tuvo efecto"**

**¿Qué significa esto en números?**
- La tasa de desnutrición sigue siendo 35%
- La diferencia que vimos (7%) es solo casualidad de la muestra

💡 Esta es nuestra **"posición escéptica"** que intentaremos refutar con evidencia.

---

# Paso 1: Plantear las Hipótesis (continuación)

### 🟢 H₁: Hipótesis Alternativa

**"El programa SÍ redujo la desnutrición"**

**¿Qué significa esto en números?**
- La tasa de desnutrición es **realmente menor** a 35%
- La diferencia observada (7%) es un **efecto genuino** del programa

✅ Esta es la afirmación que queremos **demostrar con evidencia**.

---

# 🗺️ Proceso de Decisión

```mermaid
flowchart TD
    A[📊 Observamos los datos
de la muestra] --> B{🤔 ¿Los datos son compatibles
con H₀?}
    B -->|❌ NO
evidencia fuerte| C[✅ Rechazamos H₀]
    B -->|✓ SÍ
evidencia débil| D[⚠️ No rechazamos H₀]
    C --> E[🎉 Conclusión:
El programa SÍ funciona]
    D --> F[🤷 Conclusión:
No hay evidencia suficiente
para decir que funciona]
```

---

# 🎲 Analogía para Entender el Valor P

## El Caso de la Moneda

**Situación:**

Tu amigo lanza una moneda **100 veces** y obtiene **cara 70 veces**.

### 🤔 La Gran Pregunta:

**¿La moneda está cargada (trucada)?**

**¿O solo tuvo mucha suerte?**

---

# 🎲 Planteando las Hipótesis

### H₀: Hipótesis Nula

**"La moneda es justa (no está cargada)"**

Si esto es cierto, esperamos que salga cara aproximadamente **50 veces** de 100 lanzamientos.

### H₁: Hipótesis Alternativa

**"La moneda está cargada"**

Sale cara más frecuentemente de lo que debería por pura casualidad.

---

# 🧮 ¿Qué tan Raro es Obtener 70 Caras?

Si la moneda **fuera justa** (H₀ es cierta):
- Esperamos aproximadamente **50 caras**
- Podría variar un poco: 45-55 caras sería normal

Pero obtener **70 caras** sería:
- ✨ **Extremadamente raro**
- 📊 Probabilidad: ~0.0001 (solo 0.01% de probabilidad)

⚠️ **Valor P bajo:** Los datos observados son muy improbables si H₀ fuera cierta

---

# ✅ Conclusión del Experimento de la Moneda

### Razonamiento:

**SI** la moneda fuera justa (H₀), sería **casi imposible** obtener 70 caras.

### Decisión:

Por tanto: **Rechazamos H₀**

### Conclusión Final:

La moneda probablemente **está cargada**.

💡 Este es exactamente el mismo razonamiento que usamos con los datos de la ONG!

---

# 📘 Definición Formal del Valor P

**Valor P =**

Probabilidad de observar datos tan extremos (o más)

**SI** la hipótesis nula (H₀) fuera cierta

📌 **En palabras simples:**

¿Qué tan raro/improbable es lo que observamos, **asumiendo que H₀ es verdadera**?

---

# 📖 Cómo Leer la Notación Estadística

## Símbolos que Verás Frecuentemente

### 1. H₀ (se lee: "H sub-cero" o "H cero")

**Significa:** Hipótesis Nula

**Ejemplo:** "H₀: La media es 50" se lee como "La hipótesis nula dice que la media es 50"

### 2. H₁ (se lee: "H sub-uno" o "H uno")

**Significa:** Hipótesis Alternativa

**Ejemplo:** "H₁: La media es diferente de 50"

---

# 📖 Cómo Leer la Notación Estadística (cont.)

### 3. El símbolo < (se lee: "menor que")

**P < 0.05** se lee: "P es menor que cero punto cero cinco"

**Significa:** El valor P es más pequeño que 0.05

**Ejemplos:**
- P = 0.03 → 0.03 < 0.05 ✅ (Verdadero: 0.03 es menor que 0.05)
- P = 0.12 → 0.12 < 0.05 ❌ (Falso: 0.12 NO es menor que 0.05)

💡 **Tip:** Piensa en el símbolo < como una "boca abierta" que siempre apunta hacia el número más grande.

<code>3 < 5</code> (la boca se abre hacia el 5 porque es más grande)

---

# Interpretando el Valor P

## ¿Qué Significa Cada Rango?

| Valor P | Interpretación | Decisión Típica |
|---------|----------------|-----------------|
| **< 0.01** | Evidencia muy fuerte contra H₀ | Rechazar H₀ (muy seguro) |
| **0.01 - 0.05** | Evidencia fuerte contra H₀ | Rechazar H₀ (seguro) |
| **0.05 - 0.10** | Evidencia débil contra H₀ | Zona gris (depende del contexto) |
| **> 0.10** | Evidencia insuficiente contra H₀ | No rechazar H₀ |

---

# 🎯 El Umbral Estándar: α = 0.05

### ¿Qué es α (alfa)?

**α** (se lee "alfa") es el **nivel de significancia**: el umbral que usamos para decidir si rechazamos H₀.

### La Regla Más Común:

**α = 0.05** (5%)

**Si P < 0.05 → Rechazamos H₀**

**Si P ≥ 0.05 → NO rechazamos H₀**

⚠️ **¿Qué significa el 5%?**

Estamos aceptando un **5% de riesgo** de rechazar H₀ cuando en realidad es verdadera (Error Tipo I).

---

# ✅ Ejemplo: Volviendo a la ONG

### Resultado de la Prueba:

**P = 0.012** (1.2%)

### ¿Qué significa esto?

Hay solo **1.2% de probabilidad** de observar esta reducción (o mayor) si el programa **NO funcionara**.

### Decisión:

**P = 0.012 < 0.05** ✅

Por tanto: **Rechazamos H₀**

**Conclusión Final:**

Tenemos evidencia suficiente para decir que el programa de la ONG **SÍ es efectivo**.

---

# ❌ Ejemplo Alternativo: Evidencia Insuficiente

### Resultado de una Prueba Diferente:

**P = 0.18** (18%)

### ¿Qué significa esto?

Hay **18% de probabilidad** de observar esta diferencia por **pura casualidad**.

### Decisión:

**P = 0.18 > 0.05** ❌

Por tanto: **NO rechazamos H₀**

**Conclusión Final:**

NO tenemos evidencia suficiente para decir que el programa funciona.

(Esto NO significa que "no funciona", solo que no podemos estar seguros con estos datos)

---

# ⚠️ Los Dos Tipos de Error

### Incluso con pruebas estadísticas, podemos equivocarnos

Como en cualquier decisión basada en evidencia, hay **dos formas** de cometer errores.

Veamos esto con un ejemplo que usas todos los días...

---

# 📱 Ejemplo Gen Z: Filtro de Spam de Instagram

### La Situación:

Instagram tiene que decidir: **¿Este mensaje es spam o es legítimo?**

**H₀ (Hipótesis Nula):** El mensaje es legítimo (no es spam)

**H₁ (Hipótesis Alternativa):** El mensaje es spam

### Las Posibles Decisiones:

- **Rechazar H₀** → Marcar el mensaje como spam y bloquearlo
- **No rechazar H₀** → Dejar pasar el mensaje a tu bandeja principal

---

# 🚨 Error Tipo I: Falso Positivo

### ¿Qué es?

Rechazar H₀ cuando **en realidad es verdadera**

### 📱 En Instagram:

Un mensaje **legítimo** (como una oportunidad de trabajo real) es marcado como **spam** y lo pierdes.

**Consecuencia:** Perdiste algo importante 😢

### 📊 En la ONG:

Concluir que el programa **funciona** cuando en realidad **NO tuvo ningún efecto**.

**Consecuencia:** Invertir recursos en un programa inefectivo 💸

**Probabilidad del Error Tipo I:** α = 0.05 (5%)

---

# 😔 Error Tipo II: Falso Negativo

### ¿Qué es?

**NO** rechazar H₀ cuando **en realidad es falsa**

### 📱 En Instagram:

Un mensaje de **spam real** (estafa, phishing) pasa como legítimo y llega a tu bandeja.

**Consecuencia:** Podrías caer en una estafa 🚨

### 📊 En la ONG:

Concluir que el programa **NO funciona** cuando en realidad **SÍ es efectivo**.

**Consecuencia:** Cancelar un programa que realmente ayudaba 😞

**Probabilidad del Error Tipo II:** β (varía según el diseño del estudio)

---

# 📊 Resumen: Tabla de Decisiones



|                           | **H₀ es Verdadera**<br>(No hay efecto real) | **H₀ es Falsa**<br>(Sí hay efecto real) |
|---------------------------|---------------------------------------------|------------------------------------------|
| **Rechazamos H₀**         | ❌ **Error Tipo I** (α = 5%)<br>Falso Positivo | ✅ **Decisión Correcta**<br>Detectamos el efecto |
| **No Rechazamos H₀**      | ✅ **Decisión Correcta**<br>No hay efecto y no lo afirmamos | ❌ **Error Tipo II** (β)<br>Falso Negativo |


---

# 🎯 Analogía: Detector de Humo

### Error Tipo I: Falsa Alarma

- El detector **suena cuando NO hay fuego**
- Molesto e inconveniente, pero no peligroso
- Te despierta a las 3am por nada 😴

### Error Tipo II: No Detecta el Peligro

- El detector **NO suena cuando SÍ hay fuego** 🔥
- Extremadamente peligroso
- Podría ser fatal

⚠️ **¿Cuál error prefieres?** En este caso, preferimos Error Tipo I (falsas alarmas) sobre Error Tipo II (no detectar el fuego).

---

# 🏥 Analogía: Prueba Médica (COVID-19)

### Error Tipo I: Falso Positivo

- La prueba dice que **tienes COVID**, pero en realidad **estás sano**
- Consecuencia: Cuarentena innecesaria, ansiedad, más pruebas
- Molesto, pero no crítico

### Error Tipo II: Falso Negativo

- La prueba dice que **NO tienes COVID**, pero en realidad **SÍ estás infectado**
- Consecuencia: Sigues tu vida normal, contagias a otros
- Muy peligroso para ti y los demás

💡 Por eso algunas pruebas médicas son diseñadas para ser "sensibles" (prefieren Error Tipo I sobre Error Tipo II).

---

# ⚖️ El Balance (Trade-off)

### El Dilema:

No podemos eliminar **completamente** ambos tipos de error al mismo tiempo.

### Si somos MÁS estrictos (bajamos α):

- ✅ Reducimos Error Tipo I (menos falsos positivos)
- ❌ Aumentamos Error Tipo II (más falsos negativos)

### Si somos MENOS estrictos (subimos α):

- ❌ Aumentamos Error Tipo I (más falsos positivos)
- ✅ Reducimos Error Tipo II (menos falsos negativos)

**💡 La Solución:** Aumentar el tamaño de muestra (n) reduce AMBOS errores simultáneamente!

---

# 🗺️ Panorama: Tipos de Pruebas de Hipótesis

### Hay MUCHOS tipos de pruebas estadísticas...

Pero **NO te preocupes**: todas siguen la misma lógica que acabamos de aprender.

La pregunta clave es: **¿Qué tipo de datos tengo y qué quiero comparar?**

Veamos un mapa para ayudarte a decidir cuál usar...

---

# 🗺️ Diagrama de Decisión: ¿Qué Prueba Usar?

💡 Tip: Haz clic derecho en el diagrama y selecciona "Abrir imagen en nueva pestaña" para verlo más grande

```mermaid
flowchart TD
    A[🤔 ¿Qué quiero probar?] --> B{📊 ¿Tipo de datos?}
    B -->|📝 Categóricos
ej: género, región| C[📈 Chi-cuadrado
χ²]
    B -->|🔢 Numéricos
ej: edad, satisfacción| D{👥 ¿Cuántos grupos?}
    D -->|1 grupo vs valor fijo| E[📏 Prueba t
de una muestra]
    D -->|2 grupos| F{🔄 ¿Independientes?}
    D -->|3+ grupos| G[📊 ANOVA]
    F -->|Sí: grupos diferentes| H[📊 Prueba t
independiente]
    F -->|No: mismas personas| I[🔁 Prueba t
pareada]

    C --> C1[💡 Ejemplo: ¿El género
afecta la satisfacción?]
    E --> E1[💡 Ejemplo: ¿La media
de satisfacción = 7?]
    H --> H1[💡 Ejemplo: Satisfacción
Hombres vs Mujeres]
    I --> I1[💡 Ejemplo: Satisfacción
Antes vs Después]
    G --> G1[💡 Ejemplo: Comparar
5 departamentos]
```

📌 **No te aprendas esto de memoria!** Siempre puedes consultar este diagrama. Lo importante es entender LA LÓGICA detrás de cada prueba.

---

# 📏 Prueba t: ¿Qué es y Para Qué Sirve?

### En Palabras Simples:

La **prueba t** te ayuda a responder: **"¿Estos dos promedios son REALMENTE diferentes, o solo parece por casualidad?"**

### 📊 Ejemplo del Día a Día:

Tienes dos grupos de personas que usaron los servicios de la ONG:
- Grupo A (Hombres): Promedio de satisfacción = 7.2
- Grupo B (Mujeres): Promedio de satisfacción = 6.8

**Pregunta:** ¿Esta diferencia de 0.4 puntos es significativa, o podría ser solo variación aleatoria?

💡 La prueba t toma en cuenta NO SOLO la diferencia, sino también la VARIABILIDAD de los datos y el tamaño de las muestras.

---

# 📏 Los 3 Tipos de Prueba t

### 1️⃣ Prueba t de Una Muestra

**¿Cuándo?** Cuando quieres comparar el promedio de **un grupo** vs **un valor conocido/esperado**

**Ejemplo ONG:** "¿La satisfacción promedio de nuestros beneficiarios es diferente de 7.0?"

### 2️⃣ Prueba t de Dos Muestras Independientes

**¿Cuándo?** Cuando quieres comparar **dos grupos DIFERENTES** de personas

**Ejemplo ONG:** "¿La satisfacción de hombres es diferente a la de mujeres?"

### 3️⃣ Prueba t Pareada (Antes/Después)

**¿Cuándo?** Cuando mides a **las MISMAS personas** en dos momentos diferentes

**Ejemplo ONG:** "¿La satisfacción ANTES del programa es diferente a la satisfacción DESPUÉS?"

---

# 📊 Ejemplo Paso a Paso: Satisfacción por Género

### 📋 Los Datos de la ONG:

- **Hombres:** Media = 7.2, Desviación Estándar = 1.5, n = 80 personas
- **Mujeres:** Media = 6.8, Desviación Estándar = 1.3, n = 120 personas

### ❓ La Pregunta:

¿La satisfacción de hombres es **significativamente diferente** a la de mujeres?

### 📝 Planteamos las Hipótesis:

- **H₀:** No hay diferencia (las medias son iguales: μ₁ = μ₂)
- **H₁:** SÍ hay diferencia (las medias son diferentes: μ₁ ≠ μ₂)

---

# 🐍 Prueba t en Python (SciPy)

```python {all|1-2|4-7|9-10|12-13|15-18|all}
from scipy import stats
import numpy as np

# Datos (simulados para el ejemplo)
hombres = np.random.normal(7.2, 1.5, 80)  # Media=7.2, DE=1.5, n=80
mujeres = np.random.normal(6.8, 1.3, 120) # Media=6.8, DE=1.3, n=120

# Realizar prueba t de dos muestras independientes
t_statistic, p_value = stats.ttest_ind(hombres, mujeres)

# Mostrar resultados
print(f"Estadístico t: {t_statistic:.3f}")
print(f"Valor P: {p_value:.4f}")

# Decisión
if p_value < 0.05:
    print("✅ Rechazamos H₀: HAY diferencia significativa")
else:
    print("❌ No rechazamos H₀: NO hay evidencia de diferencia")
```

📚 **Documentación:** [scipy.stats.ttest_ind()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)

---

# 📊 Interpretando los Resultados

### Resultado del Código:

```
Estadístico t: 2.05
Valor P: 0.042
```

### ✅ Decisión:

**P = 0.042 < 0.05** → Rechazamos H₀

### 💡 Conclusión en Lenguaje Simple:

Hay evidencia estadísticamente significativa de que la satisfacción de **hombres** es **mayor** que la de **mujeres**.

**🎯 Acción Recomendada para la ONG:**

Investigar POR QUÉ las mujeres tienen menor satisfacción y diseñar intervenciones específicas para mejorar su experiencia.

---

# 📋 Resumen: Conceptos Clave

| Concepto | Definición | Aplicación |
|----------|------------|------------|
| **H₀** | Hipótesis nula: "No hay efecto" | Punto de partida escéptico |
| **H₁** | Hipótesis alternativa: "SÍ hay efecto" | Lo que queremos probar |
| **p-value** | Probabilidad de los datos si H₀ fuera cierta | Si p < 0.05 → rechazamos H₀ |
| **α** | Nivel de significancia (usualmente 0.05) | Umbral para decisión |
| **Error Tipo I** | Rechazar H₀ cuando es verdadera (falso positivo) | α = 5% de riesgo |
| **Error Tipo II** | No rechazar H₀ cuando es falsa (falso negativo) | β (varía) |

---

# 🛠️ Las 3 Pruebas t que Aprendiste

| Tipo | Cuándo Usarla | Función Python | Ejemplo ONG |
|------|---------------|----------------|-------------|
| **t de 1 muestra** | 1 grupo vs valor conocido | `ttest_1samp(datos, valor)` | ¿Satisfacción = 7.0? |
| **t independiente** | 2 grupos diferentes | `ttest_ind(grupo1, grupo2)` | Hombres vs Mujeres |
| **t pareada** | Mismas personas, 2 momentos | `ttest_rel(antes, despues)` | Antes vs Después |

✅ Con estas 3 pruebas puedes responder la mayoría de las preguntas sobre **comparación de promedios** en el contexto de ONGs

---

# ✅ Checklist de Comprensión

Antes de ir al Workshop, verifica que puedas:

### Conceptos:
- [ ] Explicar qué es H₀ y H₁
- [ ] Interpretar correctamente un p-value
- [ ] Distinguir entre "rechazar" y "no rechazar" H₀
- [ ] Explicar Error Tipo I y Tipo II con ejemplos

### Aplicación:
- [ ] Decidir qué tipo de prueba t usar según el escenario
- [ ] Plantear hipótesis correctamente
- [ ] Leer e interpretar resultados de Python
- [ ] Conectar resultados estadísticos con acciones para la ONG

---

# 🎯 Próximos Pasos

## 1️⃣ Practica con el Ejercicio

Aplica estos conceptos con el dataset de prueba antes del Workshop 1

## 2️⃣ Workshop 1

Usa pruebas t con datos reales de ONGs

## 3️⃣ Semana 2: Más Herramientas

Aprenderás Chi-Cuadrada, ANOVA, y Regresión para casos más complejos

¡Ahora tienes las bases para analizar datos con rigor estadístico! 📊

---

# ¡Gracias!

  📊

### Preguntas

  CD2001B | Tec de Monterrey Campus Puebla
