# 📅 Plan de Clases - Semana 2

## Pruebas Estadísticas Avanzadas

**Total:** 4 clases × 2 horas = 8 horas
**Modalidad:** Presencial con práctica en computadora
**Herramientas:** Python, Google Colab, pandas, scipy, statsmodels

---

## 📌 Clase 1: Prueba Ji-Cuadrada (χ²)

**Duración:** 2 horas
**Objetivo:** Analizar relaciones entre variables categóricas

### 📋 Agenda Detallada

| Tiempo | Actividad | Descripción |
|--------|-----------|-------------|
| **15 min** | 🔄 Introducción a variables categóricas | - Repaso: Variables numéricas vs categóricas<br>- ¿Cuándo usar chi-cuadrada vs t-test?<br>- Ejemplos del mundo real |
| **70 min** | 💻 Notebook 01: Ji-Cuadrada | - Tablas de contingencia<br>- Prueba de independencia<br>- Análisis de residuos<br>- Interpretación en contexto<br>- Ejercicios guiados |
| **20 min** | 📝 Ejercicio guiado | - Caso completo en clase<br>- Desde tabla hasta conclusión |
| **15 min** | 💬 Q&A | - Dudas<br>- Tarea para casa |

### 📚 Material para revisar en casa:
- ✅ Completar ejercicios de chi-cuadrada
- ✅ Leer inicio de Notebook 02 (conceptos ANOVA)
- ✅ Ver video recomendado sobre ANOVA (Stat Quest)

### 🎮 Actividad de Equipo Opcional (20 min)

<details>
<summary><b>🔍 FAKE RELATIONSHIPS: Correlaciones Espurias</b> ⚠️ OPCIONAL - A DISCRECIÓN DEL PROFESOR</summary>

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

### 📌 Notas para el Profesor:
- Tener datasets categóricos pre-cargados
- Preparar ejemplos de tablas de contingencia interpretables
- Explicar residuos con analogía (diferencia entre esperado y observado)
- Conectar con chi-cuadrada de bondad de ajuste (si hay tiempo)

---

## 📌 Clase 2: ANOVA (Análisis de Varianza)

**Duración:** 2 horas
**Objetivo:** Comparar múltiples medias simultáneamente

### 📋 Agenda Detallada

| Tiempo | Actividad | Descripción |
|--------|-----------|-------------|
| **10 min** | 🔄 Repaso: t-test vs ANOVA | - ¿Por qué no hacer múltiples t-tests?<br>- Problema de inflación de error Tipo I |
| **75 min** | 💻 Notebook 02: ANOVA | - ANOVA de un factor (one-way)<br>- Verificación de supuestos (normalidad, homogeneidad)<br>- Interpretación del F-statistic<br>- Pruebas post-hoc (Tukey HSD)<br>- Ejercicios guiados |
| **20 min** | 📝 Práctica guiada | - Comparar satisfacción entre 4 áreas<br>- Interpretación completa |
| **15 min** | 💬 Cierre | - Dudas<br>- Preparación para Clase 3 |

### 📚 Material para revisar en casa:
- ✅ Ejercicios de ANOVA
- ✅ Leer Notebook 03 (regresión)
- ✅ Repasar conceptos de correlación de Semana 1

### 🎮 Actividad de Equipo Opcional (15 min)

<details>
<summary><b>🎭 ANOVA EXPLAINER: Analogía Challenge</b> ⚠️ OPCIONAL - A DISCRECIÓN DEL PROFESOR</summary>

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

### 📌 Notas para el Profesor:
- Enfatizar concepto de varianza dentro vs entre grupos
- Mostrar visualmente con boxplots superpuestos
- Explicar por qué F-statistic (no t-statistic)
- Preparar interpretación de Tukey con ejemplos claros

---

## 📌 Clase 3: Regresión Lineal y Correlación

**Duración:** 2 horas
**Objetivo:** Predecir valores y cuantificar relaciones lineales

### 📋 Agenda Detallada

| Tiempo | Actividad | Descripción |
|--------|-----------|-------------|
| **15 min** | 🎯 Introducción a predicción | - ¿Qué es predecir?<br>- Diferencia entre correlación y predicción<br>- Aplicaciones en negocios |
| **70 min** | 💻 Notebook 03: Regresión y Correlación | - Correlación de Pearson (r)<br>- Scatter plots con línea de tendencia<br>- Regresión lineal simple (y = mx + b)<br>- Interpretación de R²<br>- Hacer predicciones<br>- Ejercicios guiados |
| **20 min** | 💻 Notebook 04: Integración | - Árbol de decisión: ¿Qué prueba usar?<br>- Ejercicio integrador<br>- Repaso de toda la semana |
| **15 min** | 💬 Cierre | - Dudas<br>- Introducción a Workshop 2 |

### 📚 Material para revisar en casa:
- ✅ Completar ejercicios de regresión
- ✅ Empezar Workshop 2
- ✅ Revisar árbol de decisión de pruebas

### 🎮 Actividad de Equipo Opcional (20 min)

<details>
<summary><b>🎯 PREDICTION GAME: ¿Quién predice mejor?</b> ⚠️ OPCIONAL - A DISCRECIÓN DEL PROFESOR</summary>

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

### 📌 Notas para el Profesor:
- Enfatizar interpretación de R² (% de variabilidad explicada)
- Mostrar ejemplos de buena vs mala regresión (scatter plots)
- Explicar cuándo NO usar regresión lineal (relaciones no lineales)
- Conectar pendiente con interpretación de negocios

---

## 📌 Clase 4: Integración y Workshop 2

**Duración:** 2 horas
**Objetivo:** Consolidar conceptos y trabajar en Workshop 2

### 📋 Agenda Detallada

| Tiempo | Actividad | Descripción |
|--------|-----------|-------------|
| **30 min** | 🔄 Repaso integrador | - ¿Qué prueba usar según tipo de variables?<br>- Árbol de decisión completo (t-test, chi², ANOVA, regresión)<br>- Errores comunes<br>- Quiz rápido |
| **15 min** | 📋 Introducción a Workshop 2 | - Explicación de rúbrica<br>- Dataset: Fundación Esperanza (ONG)<br>- Estructura MEAL comparativa<br>- FAQ |
| **60 min** | 💻 Tiempo de trabajo en Workshop 2 | - Estudiantes trabajan en clase<br>- Profesor circula para dudas<br>- Checkpoint a mitad de tiempo |
| **15 min** | 💬 Cierre y próximos pasos | - Recordatorio de entrega<br>- Vista previa de Semana 3<br>- Celebrar completar Módulo 1! 🎉 |

### 📚 Tarea para entregar:
- ⭐ **Workshop 2:** [workshop2_plantilla.ipynb](ejercicios/workshop2_plantilla.ipynb)
- 📅 **Fecha límite:** Ver calendario del curso
- 🎯 **Valor:** 10% de la calificación final

### 🎮 Actividad de Equipo Opcional (20 min)

<details>
<summary><b>🎨 STAT MEME CREATION: Meme Educativo</b> ⚠️ OPCIONAL - A DISCRECIÓN DEL PROFESOR</summary>

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

### 📌 Notas para el Profesor:
- Crear ambiente positivo (música suave opcional)
- Celebrar que completaron Módulo 1 de estadística!
- Hacer checkpoint a los 30 min de trabajo
- Recordar que workshop se termina en casa
- Preparar preview emocionante de Semana 3

---

## 📊 Resumen de Entregables de la Semana

| Entregable | Tipo | Fecha | Valor |
|------------|------|-------|-------|
| Ejercicios opcionales | Práctica | - | 0% (preparación) |
| **Workshop 2** | Evaluación | Fin de semana | **10%** |

---

## 🎯 Checklist para el Profesor

**Antes de la semana:**
- [ ] Verificar que todos los notebooks estén actualizados
- [ ] Probar que datasets categóricos se cargan bien
- [ ] Preparar ejemplos de cada prueba estadística
- [ ] Revisar actividades opcionales y decidir cuáles usar
- [ ] Actualizar rúbrica de Workshop 2

**Durante cada clase:**
- [ ] Compartir link de Colab al inicio
- [ ] Conectar con conceptos de Semana 1
- [ ] Enfatizar árbol de decisión de pruebas
- [ ] Circular por el salón durante ejercicios

**Después de Clase 4:**
- [ ] Compartir rúbrica de Workshop 2 detallada
- [ ] Enviar árbol de decisión completo como referencia
- [ ] Publicar FAQ basado en preguntas de la semana
- [ ] Preparar materiales de Semana 3

---

## 💡 Tips de Enseñanza

### Para conectar con Semana 1:
- 🔗 "Recuerdan cuando vimos t-test? ANOVA es su primo para 3+ grupos"
- 🔗 "Chi-cuadrada es como t-test pero para variables categóricas"
- 🔗 "Regresión es el siguiente paso después de correlación"

### Para el árbol de decisión:
- 🌳 Proyectar árbol en cada clase
- 🌳 Hacer que estudiantes lo usen antes de cada ejercicio
- 🌳 Quiz oral: "Tengo 2 variables categóricas, ¿qué prueba uso?"

### Para mantener engagement:
- 🎮 Usar actividades de equipo (15-20 min máximo)
- 📊 Conectar con casos reales (A/B testing, encuestas, predicción de ventas)
- 🏆 Reconocer publicly a estudiantes que ayudan a compañeros

### Para gestionar complejidad:
- 📝 Proveer cheat sheet de comandos Python por prueba
- 🎨 Enfatizar visualización ANTES de prueba
- 💬 "No memoricen fórmulas, entiendan CUÁNDO usar cada prueba"

---

## 🎓 Mensaje de Cierre para Estudiantes

> "¡Felicidades por completar el Módulo 1! 🎉
>
> Ahora tienen un arsenal completo de técnicas estadísticas:
> - Descriptiva (media, SD, IQR)
> - t-tests (1 y 2 muestras)
> - Chi-cuadrada (variables categóricas)
> - ANOVA (múltiples grupos)
> - Regresión (predicción)
>
> En el mundo real, **saber CUÁNDO usar cada prueba** es más importante
> que memorizar fórmulas. ¡Ya están listos para analizar datos como pros!"

---

**¿Preguntas sobre el plan de clases?**
Consulta el [README principal](README.md) o las [guías de workshops](workshop/)
