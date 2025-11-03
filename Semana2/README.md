# 📈 Semana 2: Pruebas Estadísticas Avanzadas

## 📚 Módulo 1 - Parte 2

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:
- ✅ Realizar pruebas Ji-cuadrada para variables categóricas
- ✅ Aplicar ANOVA para comparar 3+ medias simultáneamente
- ✅ Implementar regresión lineal simple y predecir valores
- ✅ Calcular e interpretar correlaciones de Pearson
- ✅ Decidir cuál prueba estadística usar según tipo de datos
- ✅ Integrar todas las técnicas en análisis completos

---

## 📅 Plan por Día (4 clases × 2 horas)

### **📌 Clase 1: Prueba Ji-Cuadrada (χ²)** (2 horas)

**Contenido:**
- 🔹 Introducción a pruebas para variables categóricas (15 min)
  - ¿Cuándo usar chi-cuadrada vs t-test?
- 🔹 Notebook: [01_ji_cuadrada.ipynb](notebooks/01_ji_cuadrada.ipynb) (70 min)
  - Tablas de contingencia
  - Prueba de independencia
  - Análisis de residuos
  - Interpretación en contexto
- 🔹 Ejercicio guiado (20 min)
- 🔹 Q&A (15 min)

**📚 Material para revisar en casa:**
- Completar ejercicios de chi-cuadrada
- Leer inicio de Notebook 02 (conceptos ANOVA)

**🎮 Actividad de Equipo Opcional:**

<details>
<summary><b>🔍 FAKE RELATIONSHIPS: Correlaciones Espurias</b> (20 min) ⚠️ OPCIONAL - A DISCRECIÓN DEL PROFESOR</summary>

**Objetivo:** Entender que correlación ≠ causalidad con ejemplos absurdos

**Equipos:** 3-4 personas

**Instrucciones:**
1. **Buscar correlación espuria con IA** (7 min):
   ```
   Prompt para ChatGPT/Gemini:
   "Dame 3 ejemplos reales de variables que están correlacionadas
   pero obviamente NO tienen relación causal. Deben ser absurdas
   y graciosas. Incluye la correlación real si es posible."
   ```

   Ejemplo: "Consumo de queso per cápita correlaciona (r=0.95) con
   muertes por ahogamiento en sábanas"

2. **Votar por la más absurda** (5 min):
   - Cada equipo comparte su favorita
   - Clase vota: ¿Cuál es la más ridícula?

3. **Discusión seria** (5 min):
   - ¿Por qué estas correlaciones no implican causalidad?
   - ¿Qué necesitaríamos para probar causalidad?
   - Aplicación a chi-cuadrada: Variables independientes vs dependientes

4. **Conclusión** (3 min):
   - Recordatorio: Chi-cuadrada NO prueba causalidad, solo asociación

**Entregable:** Screenshot del ejemplo más absurdo + explicación de por qué NO hay causalidad

**Beneficios:**
- ✅ Refuerza concepto crítico de forma divertida
- ✅ Estudiantes recuerdan ejemplos absurdos fácilmente
- ✅ Conexión con Semana 1 (correlación vs causalidad)

</details>

---

### **📌 Clase 2: ANOVA (Análisis de Varianza)** (2 horas)

**Contenido:**
- 🔹 Repaso rápido: t-test vs ANOVA (10 min)
  - ¿Por qué no hacer múltiples t-tests?
- 🔹 Notebook: [02_anova.ipynb](notebooks/02_anova.ipynb) (75 min)
  - ANOVA de un factor (one-way)
  - Verificación de supuestos (normalidad, homogeneidad)
  - Interpretación del F-statistic
  - Pruebas post-hoc (Tukey HSD)
- 🔹 Práctica guiada (20 min)
- 🔹 Cierre (15 min)

**📚 Material para revisar en casa:**
- Ejercicios de ANOVA
- Leer Notebook 03 (regresión)

**🎮 Actividad de Equipo Opcional:**

<details>
<summary><b>🎭 ANOVA EXPLAINER: Analogía Challenge</b> (15 min) ⚠️ OPCIONAL - A DISCRECIÓN DEL PROFESOR</summary>

**Objetivo:** Explicar ANOVA con analogías creativas

**Equipos:** 3-4 personas

**Instrucciones:**
1. **Pedir a IA una analogía** (5 min):
   ```
   Prompt para ChatGPT/Claude:
   "Explica qué es ANOVA usando una analogía del mundo real que
   un estudiante de 18 años pueda entender. NO uses términos
   técnicos. Puede ser comida, deportes, videojuegos, etc."
   ```

2. **Mejorar la analogía** (5 min):
   - ¿La analogía es clara?
   - ¿Falta algo?
   - Modificar/adaptar para que sea MÁS clara

3. **Presentación relámpago** (5 min):
   - Cada equipo presenta en 45 segundos
   - Clase vota: ¿Cuál analogía es la mejor?
   - Ganador explica en pizarrón

**Ejemplo de buena analogía:**
> "ANOVA es como comparar 3 marcas de hot dogs en un concurso de sabor.
> Si los 3 jueces de cada marca dan calificaciones MUY diferentes entre sí,
> no podemos confiar en que las diferencias entre marcas sean reales.
> Pero si dentro de cada marca las calificaciones son consistentes (varianza
> baja dentro), y entre marcas son diferentes (varianza alta entre),
> entonces SÍ podemos decir que una marca es mejor."

**Entregable:** Analogía en 2-3 oraciones

**Beneficios:**
- ✅ Concepto difícil se vuelve memorable
- ✅ Creatividad + entendimiento profundo
- ✅ Diferentes analogías cubren diferentes perspectivas

</details>

---

### **📌 Clase 3: Regresión Lineal y Correlación** (2 horas)

**Contenido:**
- 🔹 Introducción a predicción con datos (15 min)
- 🔹 Notebook: [03_regresion_correlacion.ipynb](notebooks/03_regresion_correlacion.ipynb) (70 min)
  - Correlación de Pearson (r)
  - Scatter plots con línea de tendencia
  - Regresión lineal simple (y = mx + b)
  - Interpretación de R²
  - Hacer predicciones
- 🔹 Notebook: [04_integracion_estadistica.ipynb](notebooks/04_integracion_estadistica.ipynb) (20 min)
  - Árbol de decisión: ¿Qué prueba usar?
  - Ejercicio integrador
- 🔹 Cierre (15 min)

**📚 Material para revisar en casa:**
- Completar ejercicios de regresión
- Empezar Workshop 2

**🎮 Actividad de Equipo Opcional:**

<details>
<summary><b>🎯 PREDICTION GAME: ¿Quién predice mejor?</b> (20 min) ⚠️ OPCIONAL - A DISCRECIÓN DEL PROFESOR</summary>

**Objetivo:** Generar modelo de regresión y hacer predicciones reales

**Equipos:** 3-4 personas

**Instrucciones:**
1. **Dataset:** Usar `ejemplo_satisfaccion_clientes.csv`

2. **Pedir a IA código de regresión** (7 min):
   ```
   Prompt para ChatGPT/Gemini:
   "Genera código Python para crear un modelo de regresión lineal
   que prediga 'satisfaccion' basado en 'tiempo_servicio'.
   Usa scikit-learn o statsmodels. Incluye:
   - Scatter plot con línea de regresión
   - R² del modelo
   - Predicción para tiempo_servicio = 24 meses"
   ```

3. **Ejecutar y analizar** (8 min):
   - Copiar código a Colab
   - Ejecutar
   - Interpretar: ¿El modelo es bueno? (R² > 0.7?)
   - ¿La predicción tiene sentido?

4. **Competencia de predicción** (5 min):
   - Profesor da valor: "tiempo_servicio = 36 meses"
   - Cada equipo predice satisfacción con su modelo
   - ¿Quién se acerca más a la media real del grupo con ese tiempo?

**Entregable:** Screenshot del gráfico + predicción + valor de R²

**Beneficios:**
- ✅ Ven utilidad práctica de regresión (predecir)
- ✅ Aprenden a generar modelos con IA
- ✅ Competencia crea engagement

</details>

---

### **📌 Clase 4: Integración y Workshop 2** (2 horas)

**Contenido:**
- 🔹 Repaso integrador (30 min)
  - ¿Qué prueba usar según tipo de variables?
  - Árbol de decisión completo (t-test, chi², ANOVA, regresión)
  - Errores comunes
- 🔹 Introducción a Workshop 2 (15 min)
  - Explicación de rúbrica
  - Dataset: Fundación Esperanza (ONG)
  - Estructura MEAL
- 🔹 Tiempo de trabajo en Workshop 2 (60 min)
  - Estudiantes trabajan en clase
  - Profesor circula para dudas
- 🔹 Cierre y próximos pasos (15 min)

**📚 Tarea para entregar:**
- **Workshop 2:** [workshop2_plantilla.ipynb](ejercicios/workshop2_plantilla.ipynb)
- **Fecha límite:** Ver calendario del curso
- **Valor:** 10% de la calificación final

**🎮 Actividad de Equipo Opcional:**

<details>
<summary><b>🎨 STAT MEME CREATION: Meme Educativo</b> (20 min) ⚠️ OPCIONAL - A DISCRECIÓN DEL PROFESOR</summary>

**Objetivo:** Consolidar conceptos creando memes estadísticos

**Equipos:** 3-4 personas

**Instrucciones:**
1. **Elegir concepto estadístico** (3 min):
   - Opciones: p-value, ANOVA, correlación vs causalidad, R², outliers
   - Cada equipo elige uno diferente

2. **Crear meme con IA** (10 min):
   ```
   Prompt para ChatGPT/DALL-E/Gemini:
   "Genera idea para un meme gracioso que explique [concepto].
   Usa formato de meme popular (Drake, distracted boyfriend, etc.).
   Dame el texto para cada panel."
   ```

   Luego usar:
   - [Imgflip Meme Generator](https://imgflip.com/memegenerator)
   - O simplemente escribir texto en PowerPoint/Google Slides

3. **Compartir** (5 min):
   - Proyectar cada meme
   - Clase vota: ¿Cuál es el más gracioso Y educativo?

4. **Galería** (2 min):
   - Profesor compila en presentación
   - Compartir en canal del curso

**Ejemplo:**
```
[Meme de Drake]
Panel 1 (rechazo): "Usar ANOVA sin verificar supuestos"
Panel 2 (aprobación): "Verificar normalidad y homogeneidad
                        antes de ANOVA"
```

**Entregable:** Imagen del meme (screenshot)

**Beneficios:**
- ✅ Repaso ligero y divertido
- ✅ Creatividad + contenido educativo
- ✅ Gen Z aprende mejor con memes
- ✅ Material reutilizable para futuros estudiantes

</details>

---

## 📁 Estructura de la Semana

```
Semana2/
├── README.md                                 # Este archivo
├── notebooks/
│   ├── 01_ji_cuadrada.ipynb                 # Clase 1: Variables categóricas
│   ├── 02_anova.ipynb                       # Clase 2: Comparar 3+ grupos
│   ├── 03_regresion_correlacion.ipynb       # Clase 3: Predicción
│   └── 04_integracion_estadistica.ipynb     # Clase 3-4: Árbol de decisión
├── ejercicios/
│   └── workshop2_plantilla.ipynb            # ⭐ ENTREGABLE - 10% calificación
├── ejercicios_extra/
│   ├── practica_ong_estadistica_avanzada.ipynb  # Práctica adicional
│   └── textbook_exercises.ipynb             # Ejercicios de libro
└── datos/
    └── (reutiliza datos de Semana1/)
```

---

## 📊 Entregables de la Semana

### **🎯 Workshop 2: Análisis Estadístico Avanzado**

**Archivo:** [workshop2_plantilla.ipynb](ejercicios/workshop2_plantilla.ipynb)
**Dataset:** `fundacion_esperanza_donadores.csv` (ONG - 1000 donadores)
**Valor:** 10% de la calificación final
**Fecha límite:** Ver calendario del curso

**Contenido del Workshop:**

| Sección | Descripción | Puntos |
|---------|-------------|--------|
| **Parte 1: Chi-cuadrada** | ¿Tipo de donante afecta retención? | 25 pts |
| **Parte 2: ANOVA** | Comparar satisfacción por canal de donación | 30 pts |
| **Parte 3: Regresión** | Predecir satisfacción con años como donante | 25 pts |
| **Parte 4: Integración** | Análisis completo + recomendaciones | 20 pts |
| **BONUS: Reflexión MEAL** | Análisis académico comparativo (Semana 1 vs 2) | +10 pts |
| **TOTAL** | | **100 pts** (+10 bonus) |

---

## 🔧 Herramientas Python

### **Librerías principales:**
```python
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency, f_oneway, pearsonr
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
```

### **Comandos clave:**

**Chi-cuadrada:**
```python
from scipy.stats import chi2_contingency

# Crear tabla de contingencia
tabla = pd.crosstab(df['var1'], df['var2'])

# Prueba chi-cuadrada
chi2, p_value, dof, expected = chi2_contingency(tabla)
```

**ANOVA:**
```python
from scipy.stats import f_oneway

# ANOVA de un factor
f_stat, p_value = f_oneway(grupo1, grupo2, grupo3)

# Post-hoc (Tukey)
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(df['variable'], df['grupo'])
```

**Regresión:**
```python
from scipy.stats import pearsonr

# Correlación
r, p_value = pearsonr(df['x'], df['y'])

# Regresión lineal simple
from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Predicción
y_pred = slope * x_nuevo + intercept
```

---

## 💡 Tips de Estudio

1. **🗺️ Usa el árbol de decisión:**
   - Antes de cada análisis: ¿Qué tipo de variables tengo?
   - Categórica vs categórica → Chi-cuadrada
   - Numérica con 3+ grupos → ANOVA
   - 2 numéricas para predecir → Regresión

2. **📊 SIEMPRE visualiza primero:**
   - Chi-cuadrada → Gráfico de barras agrupadas
   - ANOVA → Boxplots por grupo
   - Regresión → Scatter plot con línea de tendencia

3. **✅ Verifica supuestos:**
   - Chi-cuadrada: Frecuencias esperadas > 5
   - ANOVA: Normalidad (Shapiro), homogeneidad (Levene)
   - Regresión: Linealidad, residuos normales

4. **🤖 Usa IA estratégicamente:**
   - ✅ "Explica cuándo usar ANOVA vs chi-cuadrada"
   - ✅ "Mi ANOVA dio p=0.03, ¿qué significa?"
   - ❌ "Dame todo el código del workshop"

---

## 🆘 Recursos de Apoyo

### **Material del curso:**
- [Semana 1: Estadística Básica](../Semana1/) - Repasar t-test y conceptos base
- [CODEBOOK: Dataset ONG](../Semana1/datos/CODEBOOK_fundacion_esperanza.md)
- [Práctica extra avanzada](ejercicios_extra/practica_ong_estadistica_avanzada.ipynb)

### **Recursos externos:**

**Estadística:**
- [Stat Quest - ANOVA](https://www.youtube.com/watch?v=0Vj2V2qRU10) - Video explicativo
- [Seeing Theory - Regresión](https://seeing-theory.brown.edu/regression-analysis/index.html)

**Python:**
- [SciPy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html) - Todas las pruebas
- [Statsmodels](https://www.statsmodels.org/stable/index.html) - ANOVA y regresión avanzada

---

## ❓ Preguntas Frecuentes

**P: ¿Cuándo uso chi-cuadrada vs ANOVA?**
R:
- **Chi-cuadrada:** Ambas variables son **categóricas** (ej: género × área)
- **ANOVA:** Variable numérica comparada entre **3+ grupos categóricos** (ej: satisfacción × 4 áreas)

**P: ¿Por qué no hacer múltiples t-tests en lugar de ANOVA?**
R: Múltiples t-tests aumentan el error Tipo I (falsos positivos). ANOVA controla este error.

**P: ¿Qué significa R² = 0.65 en regresión?**
R: El modelo explica 65% de la variabilidad en Y. Mientras más cerca de 1, mejor el modelo.

**P: ¿Puedo usar regresión si las variables no están perfectamente relacionadas linealmente?**
R: Depende. Si r < 0.3, la relación es muy débil. Usa scatter plot para verificar linealidad.

**P: ¿Las actividades de equipo opcionales cuentan para calificación?**
R: No, son opcionales y a discreción del profesor. Son para reforzar conceptos de forma interactiva.

---

## 🚀 Próximos Pasos

**Al terminar Semana 2:**
1. ✅ Dominas chi-cuadrada, ANOVA, y regresión
2. ✅ Sabes elegir prueba correcta según tipo de datos
3. ✅ Has completado Workshop 2 (10% de tu calificación)
4. ✅ **Completaste Módulo 1** (estadística completa) 🎉

**Siguiente módulo:**
- [Semana 3: Análisis Estratégico](../Semana3/)
  - Matriz BCG
  - Diamante de Porter
  - Customer Journey Map
  - Selección de ONG para proyecto final

---

## 📝 Checklist de la Semana

**Durante Clase 1 (Chi-cuadrada):**
- [ ] Entendí cuándo usar chi-cuadrada
- [ ] Sé crear tablas de contingencia
- [ ] Puedo interpretar p-value de chi-cuadrada
- [ ] (Opcional) Encontré correlaciones espurias divertidas

**Durante Clase 2 (ANOVA):**
- [ ] Entendí diferencia entre ANOVA y múltiples t-tests
- [ ] Sé interpretar F-statistic y p-value
- [ ] Entiendo para qué sirven pruebas post-hoc
- [ ] (Opcional) Creé analogía clara de ANOVA

**Durante Clase 3 (Regresión):**
- [ ] Puedo calcular correlación de Pearson
- [ ] Sé crear modelo de regresión lineal
- [ ] Entiendo qué significa R²
- [ ] Puedo hacer predicciones con el modelo
- [ ] (Opcional) Competí en Prediction Game

**Durante Clase 4 (Integración):**
- [ ] Uso árbol de decisión para elegir prueba
- [ ] Trabajé en Workshop 2 en clase
- [ ] Resolví dudas con profesor
- [ ] (Opcional) Creé meme estadístico

**Después de Clase 4:**
- [ ] **Entregué Workshop 2 completo** ⭐

---

**¡Felicidades por completar el Módulo 1 de Estadística!** 📊🎉

Ahora tienes un arsenal completo de técnicas estadísticas. En el mundo real, **saber CUÁNDO usar cada prueba** es más importante que memorizar fórmulas. ¡Ya estás listo para el proyecto final!
