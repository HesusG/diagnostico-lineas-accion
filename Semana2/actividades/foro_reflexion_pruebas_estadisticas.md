# Foro de Reflexión: Pruebas Estadísticas en la Práctica

**Curso:** CD2001B - Diagnóstico para Líneas de Acción
**Módulo:** Semana 2 - Pruebas de Hipótesis y Modelos
**Tiempo estimado:** 10 minutos
**Modalidad:** Foro de discusión en Canvas
**Puntos:** 10 puntos (participación)

---

## 📋 Instrucciones para el Profesor

### Configuración en Canvas:
1. Crear un nuevo **Discussion** (Foro de discusión)
2. Título: "Reflexión: ¿Cuándo usar cada prueba estadística?"
3. Puntos: 10
4. Fecha límite: [Configurar según calendario del curso]
5. Criterios de evaluación:
   - **Publicación inicial (6 pts):** Respuesta completa y reflexiva a la pregunta
   - **Interacción con compañeros (4 pts):** Al menos 1 respuesta constructiva a otro estudiante

---

## 📝 Instrucciones para Estudiantes

### Contexto:

En las últimas semanas hemos trabajado con diferentes **pruebas estadísticas** usando Python:

- **Prueba t** (t-test): `scipy.stats.ttest_ind()`, `scipy.stats.ttest_rel()`
- **Chi-Cuadrada (χ²)**: `scipy.stats.chi2_contingency()`
- **ANOVA**: `scipy.stats.f_oneway()`
- **Regresión Lineal**: `sklearn.linear_model.LinearRegression()`

---

## 🎯 Tu Tarea (10 minutos)

### Parte 1: Publicación Inicial (6 puntos)

Imagina que eres el **analista de datos** de una ONG que trabaja con educación. Tu director te presenta **3 preguntas** diferentes para investigar. **Para cada pregunta:**

1. Identifica **qué prueba estadística** usarías
2. Explica **por qué** elegiste esa prueba (1-2 oraciones)
3. Menciona **qué función de Python** usarías

---

### 🔍 Las 3 Preguntas de la ONG:

#### Pregunta A:
> "¿Los estudiantes que asistieron a nuestro programa de tutorías mejoraron sus calificaciones comparado con antes del programa?"

**Tu respuesta:**
- **Prueba que usarías:** [Tu respuesta aquí]
- **Por qué:** [Explica tu razonamiento]
- **Función de Python:** `[nombre de la función]`

---

#### Pregunta B:
> "¿Hay una relación entre el género de los estudiantes (masculino/femenino) y su interés en áreas STEM (Sí/No)?"

**Tu respuesta:**
- **Prueba que usarías:** [Tu respuesta aquí]
- **Por qué:** [Explica tu razonamiento]
- **Función de Python:** `[nombre de la función]`

---

#### Pregunta C:
> "¿Hay diferencias significativas en el desempeño académico entre estudiantes de 5 escuelas diferentes que participaron en nuestro programa?"

**Tu respuesta:**
- **Prueba que usarías:** [Tu respuesta aquí]
- **Por qué:** [Explica tu razonamiento]
- **Función de Python:** `[nombre de la función]`

---

### Parte 2: Interacción (4 puntos)

**Lee al menos 2 respuestas de tus compañeros** y responde a **UNA** de ellas con:

- ✅ Si estás de acuerdo con su elección, explica qué te pareció correcto
- 🤔 Si tienes dudas o una perspectiva diferente, compártela de manera constructiva
- 💡 Agrega un consejo o un detalle adicional que consideres importante

**Ejemplo de buena interacción:**

> "Hola @María, estoy de acuerdo con tu elección de usar t-test pareada para la Pregunta A porque son las mismas personas medidas antes/después. Solo agregaría que es importante verificar que la distribución sea aproximadamente normal antes de aplicar la prueba, o considerar una prueba no paramétrica como alternativa. ¡Buen análisis! 👍"

---

## 🎯 Criterios de Evaluación

### Publicación Inicial (6 puntos):

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Pregunta A** | 2 pts | Prueba correcta (1 pt) + Justificación clara (0.5 pt) + Función Python correcta (0.5 pt) |
| **Pregunta B** | 2 pts | Prueba correcta (1 pt) + Justificación clara (0.5 pt) + Función Python correcta (0.5 pt) |
| **Pregunta C** | 2 pts | Prueba correcta (1 pt) + Justificación clara (0.5 pt) + Función Python correcta (0.5 pt) |

### Interacción con Compañeros (4 puntos):

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Respuesta constructiva** | 2 pts | Comentario reflexivo, bien fundamentado |
| **Aporte de valor** | 2 pts | Agrega información útil, hace una pregunta inteligente, o ayuda a clarificar |

---

## 💡 Consejos para una Buena Participación

1. **Sé específico:** No digas solo "usaría t-test". Di "usaría **t-test pareada** porque..."
2. **Piensa en los datos:** ¿Son numéricos o categóricos? ¿Cuántos grupos? ¿Son independientes o pareados?
3. **Menciona supuestos:** Por ejemplo, "asumo que los datos son aproximadamente normales"
4. **Sé respetuoso:** Al interactuar con compañeros, usa lenguaje constructivo y profesional

---

## 🔑 Guía de Decisión Rápida

**Usa esto como referencia al responder:**

| Si quieres... | Tipo de datos | Prueba | Función Python |
|---------------|---------------|--------|----------------|
| Comparar ANTES vs DESPUÉS (mismas personas) | Numéricos | **t-test pareada** | `scipy.stats.ttest_rel()` |
| Comparar DOS GRUPOS diferentes | Numéricos | **t-test independiente** | `scipy.stats.ttest_ind()` |
| Comparar 3+ GRUPOS | Numéricos | **ANOVA** | `scipy.stats.f_oneway()` |
| Ver relación entre 2 CATEGORÍAS | Categóricos | **Chi-cuadrada (χ²)** | `scipy.stats.chi2_contingency()` |
| Predecir una variable numérica | Numéricos | **Regresión Lineal** | `LinearRegression().fit()` |

---

## ⏰ Recordatorio

- **Fecha límite:** [El profesor configurará esto en Canvas]
- **Tiempo estimado:** 10 minutos
- **Formato:** Texto directo en Canvas (no es necesario subir archivos)

---

## 📚 Recursos de Apoyo

Si necesitas repasar antes de participar:

1. **Slides de clase:** "Pruebas de Hipótesis" (semana1-pruebas-hipotesis.md)
2. **Notebooks:**
   - `01_introduccion_estadistica.ipynb`
   - `02_medidas_tendencia_central.ipynb`
3. **Documentación de Python:**
   - [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
   - [sklearn.linear_model](https://scikit-learn.org/stable/modules/linear_model.html)

---

## 🎓 Objetivo de Aprendizaje

Al completar esta actividad, serás capaz de:

✅ Identificar qué prueba estadística aplicar según el tipo de pregunta de investigación
✅ Justificar tu elección con criterios claros (tipo de datos, número de grupos, etc.)
✅ Conectar conceptos teóricos con funciones prácticas de Python
✅ Evaluar críticamente las respuestas de tus compañeros

---

**¡Buena suerte! 🚀**
