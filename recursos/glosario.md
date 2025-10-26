# Glosario de Términos

## 📖 Glosario del Curso CD2001B

Términos clave organizados por módulo y orden alfabético.

---

## MÓDULO 1: Estadística y Pruebas de Hipótesis

### A

**Alfa (α)**
- Nivel de significancia en pruebas de hipótesis
- Probabilidad de cometer un Error Tipo I (rechazar H₀ cuando es verdadera)
- Comúnmente establecido en 0.05 (5%)
- *Ejemplo:* "Usaremos α = 0.05 para esta prueba"

**Alternativa, Hipótesis (H₁ o Hₐ)**
- Hipótesis que se acepta si se rechaza la hipótesis nula
- Representa el efecto o diferencia que el investigador espera encontrar
- Puede ser bilateral (≠) o unilateral (> o <)
- *Ejemplo:* "H₁: μ₁ ≠ μ₂" (las medias son diferentes)

**ANOVA (Analysis of Variance)**
- Prueba estadística para comparar medias de 3 o más grupos
- Evalúa si al menos una media es diferente de las demás
- Extensión de la prueba t para múltiples grupos
- *Fórmula:* F = varianza entre grupos / varianza dentro de grupos

---

### B

**Beta (β)**
- Probabilidad de cometer un Error Tipo II (no rechazar H₀ cuando es falsa)
- Relacionado con el poder estadístico: Poder = 1 - β
- *Ejemplo:* "Con β = 0.20, tenemos 80% de poder"

**Bilateral, Prueba**
- Prueba de hipótesis que evalúa diferencias en ambas direcciones
- H₁: μ₁ ≠ μ₂ (puede ser mayor O menor)
- Contraste con prueba unilateral
- *Cuándo usar:* Cuando no tienes expectativa de la dirección del efecto

**Bonferroni, Corrección de**
- Ajuste del nivel de significancia para comparaciones múltiples
- α_ajustado = α / número de comparaciones
- Previene inflación del Error Tipo I
- *Ejemplo:* Con 10 comparaciones y α=0.05 → α_ajustado = 0.005

**Boxplot (Diagrama de Caja)**
- Gráfico que muestra la distribución de datos mediante cuartiles
- Incluye: mínimo, Q1, mediana, Q3, máximo
- Útil para identificar outliers
- *Interpretación:* Caja = 50% central de los datos

---

### C

**Chi-cuadrada (χ²), Prueba de**
- Prueba para evaluar asociación entre variables categóricas
- Compara frecuencias observadas vs esperadas
- Requiere: categorías mutuamente excluyentes, frecuencias esperadas ≥5
- *Ejemplo:* ¿Hay asociación entre género y satisfacción (baja/media/alta)?

**Cohen's d**
- Medida del tamaño del efecto para diferencias de medias
- d = (M₁ - M₂) / desviación estándar combinada
- *Interpretación:* Pequeño (0.2), Medio (0.5), Grande (0.8)
- *Ejemplo:* d = 0.75 indica una diferencia grande entre grupos

**Confianza, Intervalo de**
- Rango de valores donde probablemente se encuentra el parámetro poblacional
- Típicamente 95% (α = 0.05) o 99% (α = 0.01)
- *Interpretación:* "Estamos 95% confiados de que μ está entre 7.5 y 8.5"

**Correlación**
- Medida de la relación lineal entre dos variables numéricas
- Rango: -1 (negativa perfecta) a +1 (positiva perfecta)
- No implica causalidad
- Ver: **Pearson, Coeficiente de Correlación de**

**Cramér's V**
- Medida del tamaño del efecto para pruebas χ²
- Rango: 0 (sin asociación) a 1 (asociación perfecta)
- V = √(χ² / (n × min(filas-1, columnas-1)))
- *Interpretación:* Pequeño (0.1), Medio (0.3), Grande (0.5)

**Cuartiles**
- Valores que dividen los datos en cuatro partes iguales
- Q1 = percentil 25, Q2 = mediana = percentil 50, Q3 = percentil 75
- IQR = Q3 - Q1 (rango intercuartílico)

---

### D

**Desviación Estándar (SD o σ)**
- Medida de dispersión de los datos respecto a la media
- Raíz cuadrada de la varianza
- Mismas unidades que los datos originales
- *Interpretación:* Mayor SD = mayor dispersión

**Distribución Normal**
- Distribución simétrica en forma de campana (Gaussiana)
- Caracterizada por media (μ) y desviación estándar (σ)
- Regla 68-95-99.7: 68% dentro de ±1σ, 95% dentro de ±2σ, 99.7% dentro de ±3σ

---

### E

**Error Estándar (SE)**
- Desviación estándar de la distribución muestral de la media
- SE = SD / √n
- Disminuye con mayor tamaño de muestra
- *Uso:* Calcular intervalos de confianza

**Error Tipo I**
- Rechazar H₀ cuando es verdadera (falso positivo)
- Probabilidad = α (nivel de significancia)
- *Ejemplo:* Concluir que hay diferencia cuando no la hay

**Error Tipo II**
- No rechazar H₀ cuando es falsa (falso negativo)
- Probabilidad = β
- *Ejemplo:* No detectar una diferencia real

**Eta Cuadrado (η²)**
- Medida del tamaño del efecto para ANOVA
- Proporción de varianza explicada por el factor
- η² = SS_entre / SS_total
- *Interpretación:* Pequeño (0.01), Medio (0.06), Grande (0.14)

---

### H

**Hipótesis Nula (H₀)**
- Hipótesis de "no efecto" o "no diferencia"
- Se asume verdadera hasta que haya evidencia en contra
- *Ejemplo:* "H₀: μ₁ = μ₂" (las medias son iguales)

**Homocedasticidad**
- Igualdad de varianzas entre grupos
- Supuesto de muchas pruebas paramétricas (t-test, ANOVA)
- Verificar con: Prueba de Levene, gráficos de residuos

---

### I

**IQR (Rango Intercuartílico)**
- Diferencia entre Q3 y Q1
- IQR = Q3 - Q1
- Medida de dispersión robusta (no afectada por outliers)
- *Uso:* Identificar outliers (valores < Q1 - 1.5×IQR o > Q3 + 1.5×IQR)

---

### K

**Kruskal-Wallis, Prueba de**
- Alternativa no paramétrica a ANOVA de un factor
- No requiere normalidad
- Compara medianas en lugar de medias
- *Cuándo usar:* Cuando datos no cumplen supuestos de ANOVA

---

### L

**Levene, Prueba de**
- Prueba para evaluar homocedasticidad (igualdad de varianzas)
- H₀: Las varianzas son iguales
- Si p < 0.05 → varianzas diferentes (viola supuesto de ANOVA/t-test)

---

### M

**Media (μ o M)**
- Promedio aritmético de los datos
- Σx / n
- Sensible a outliers

**Mediana**
- Valor central cuando los datos están ordenados
- Percentil 50
- Robusta ante outliers
- *Cuándo preferir sobre media:* Distribuciones asimétricas, presencia de outliers

**Moda**
- Valor más frecuente en un conjunto de datos
- Puede haber múltiples modas (bimodal, multimodal)

---

### N

**Normalidad**
- Supuesto de que los datos siguen una distribución normal
- Verificar con: Prueba de Shapiro-Wilk, Q-Q plot, histograma
- Importante para pruebas paramétricas

**Nula, Hipótesis**
- Ver **Hipótesis Nula (H₀)**

---

### O

**Outlier (Valor Atípico)**
- Observación que se desvía significativamente del patrón general
- Detección: Valores fuera de [Q1 - 1.5×IQR, Q3 + 1.5×IQR]
- Puede ser error de datos o fenómeno real
- *Decisión:* Investigar antes de eliminar

---

### P

**Pareada, Prueba t**
- Prueba t para comparar dos mediciones del mismo sujeto
- Ejemplo: Antes vs Después de una intervención
- Supuestos: Normalidad de las diferencias

**p-value (Valor p)**
- Probabilidad de obtener resultados al menos tan extremos como los observados, asumiendo H₀ verdadera
- NO es la probabilidad de que H₀ sea verdadera
- *Interpretación:*
  - p < 0.05 → estadísticamente significativo (evidencia contra H₀)
  - p ≥ 0.05 → no significativo (no hay suficiente evidencia contra H₀)

**Pearson, Coeficiente de Correlación de (r)**
- Mide la relación lineal entre dos variables numéricas
- Rango: -1 a +1
- *Interpretación:*
  - r ≈ 0: Sin relación lineal
  - 0 < |r| < 0.3: Débil
  - 0.3 ≤ |r| < 0.7: Moderada
  - 0.7 ≤ |r| ≤ 1: Fuerte

**Poder Estadístico (1 - β)**
- Probabilidad de rechazar H₀ cuando es falsa (detectar efecto real)
- Depende de: tamaño de muestra, tamaño del efecto, α
- Recomendado: ≥ 0.80 (80%)

**Post-hoc, Pruebas**
- Pruebas de comparaciones múltiples después de ANOVA significativa
- Tipos: Tukey HSD, Bonferroni, Scheffé
- *Objetivo:* Identificar qué grupos difieren entre sí

---

### R

**Regresión Lineal**
- Modelo que predice una variable dependiente a partir de una(s) independiente(s)
- Ecuación: Y = β₀ + β₁X₁ + ... + ε
- *Simple:* 1 variable independiente
- *Múltiple:* 2+ variables independientes

**Residuos**
- Diferencia entre valor observado y valor predicho
- e = Y_observado - Y_predicho
- Supuestos: Normalidad, homocedasticidad, independencia

**R² (R-cuadrado)**
- Proporción de varianza de Y explicada por el modelo
- Rango: 0 a 1
- *Interpretación:* R² = 0.75 → 75% de la varianza explicada

---

### S

**Shapiro-Wilk, Prueba de**
- Prueba de normalidad
- H₀: Los datos provienen de una distribución normal
- Si p < 0.05 → datos NO normales
- Sensible con muestras grandes (n > 100)

**Significancia Estadística**
- Resultado es estadísticamente significativo si p < α
- NO es lo mismo que significancia práctica o importancia

---

### T

**Tamaño del Efecto**
- Magnitud de la diferencia o asociación (independiente del tamaño de muestra)
- Medidas: Cohen's d, η², r, Cramér's V
- *Importancia:* p-value + tamaño del efecto = interpretación completa

**t-test (Prueba t)**
- Prueba para comparar medias
- *Tipos:*
  - **1 muestra:** Comparar media con valor de referencia
  - **2 muestras independientes:** Comparar medias de 2 grupos diferentes
  - **Pareada:** Comparar 2 mediciones del mismo sujeto

**Tukey HSD (Honest Significant Difference)**
- Prueba post-hoc después de ANOVA
- Compara todos los pares de grupos
- Controla la tasa de Error Tipo I

---

### U

**Unilateral, Prueba**
- Prueba de hipótesis que evalúa diferencia en una sola dirección
- H₁: μ₁ > μ₂ (solo "mayor") o H₁: μ₁ < μ₂ (solo "menor")
- *Cuándo usar:* Cuando tienes hipótesis direccional a priori

---

### V

**Varianza**
- Medida de dispersión (cuadrado de la desviación estándar)
- σ² o s²
- Unidades: (unidad original)²

---

## MÓDULO 2: Administración Estratégica y Visualización

### B

**BCG, Matriz**
- Matriz de Boston Consulting Group
- Clasifica productos/programas en: Estrellas, Vacas Lecheras, Interrogantes, Perros
- Ejes: Tasa de crecimiento del mercado (Y) vs Participación relativa (X)

**Benchmark**
- Valor de referencia para comparación
- Puede ser: histórico, de la industria, meta
- *Ejemplo:* "El benchmark sectorial de satisfacción es 8.0/10"

---

### C

**Customer Journey Map**
- Mapa visual de la experiencia del beneficiario
- Etapas típicas: Descubrimiento, Consideración, Servicio, Post-servicio, Lealtad
- Identifica: touchpoints, emociones, pain points, momentos de verdad

---

### D

**Dashboard**
- Panel de visualización de KPIs en tiempo real
- Características: Interactivo, visual, actualizado
- Herramientas: Looker Studio, Tableau, Power BI

**Diamante de Porter**
- Modelo de las 5 fuerzas competitivas
- Fuerzas:
  1. Rivalidad entre competidores
  2. Amenaza de nuevos entrantes
  3. Poder de negociación de clientes/beneficiarios
  4. Poder de negociación de proveedores/donantes
  5. Amenaza de productos/servicios sustitutos

---

### F

**FODA (SWOT)**
- Análisis de: Fortalezas, Oportunidades, Debilidades, Amenazas
- Fortalezas/Debilidades: Interno (controlable)
- Oportunidades/Amenazas: Externo (no controlable)

---

### K

**KPI (Key Performance Indicator)**
- Indicador clave de desempeño
- Características: Específico, Medible, Relevante, Temporal
- *Tipos:* Resultado (outcome), Proceso (output), Impacto

---

### L

**Looker Studio**
- Herramienta gratuita de Google para dashboards
- Antes: Google Data Studio
- Conecta con: Google Sheets, BigQuery, CSV, SQL

---

### M

**Misión**
- Razón de ser de la organización
- Responde: ¿Qué hacemos? ¿Para quién? ¿Cómo?

**Momento de Verdad**
- Interacción crítica que define la percepción del servicio
- *Ejemplo:* Primera llamada telefónica, entrevista inicial

---

### N

**NPS (Net Promoter Score)**
- Medida de lealtad del cliente/beneficiario
- Pregunta: "¿Qué tan probable es que recomiendes...?" (0-10)
- Clasificación:
  - Promotores: 9-10
  - Pasivos: 7-8
  - Detractores: 0-6
- NPS = % Promotores - % Detractores

---

### O

**ODS (Objetivos de Desarrollo Sostenible)**
- 17 objetivos globales de la ONU para 2030
- Agenda 2030 para el Desarrollo Sostenible
- Ejemplos: ODS 1 (Fin de la pobreza), ODS 4 (Educación de calidad)

---

### P

**Pain Point (Punto de Dolor)**
- Momento de frustración o dificultad en el Customer Journey
- Oportunidad de mejora
- *Ejemplo:* Tiempo de espera largo, información poco clara

**Porter, Diamante de**
- Ver **Diamante de Porter**

---

### S

**SMART (Objetivos)**
- Criterio para formular objetivos
- **S**pecific (Específico)
- **M**easurable (Medible)
- **A**chievable (Alcanzable)
- **R**elevant (Relevante)
- **T**ime-bound (Con plazo definido)

**Storytelling con Datos**
- Arte de comunicar insights mediante narrativa + datos + visualización
- Estructura: Inicio (contexto), Conflicto (problema), Resolución (acción)

---

### T

**Touchpoint (Punto de Contacto)**
- Cualquier interacción entre beneficiario y organización
- *Ejemplos:* Sitio web, llamada telefónica, visita presencial, email

**Teoría de Cambio (Theory of Change)**
- Modelo lógico que conecta actividades → outputs → outcomes → impacto
- Muestra cómo y por qué se espera que ocurra el cambio

---

### V

**Visión**
- Estado futuro deseado de la organización
- Responde: ¿Hacia dónde vamos?
- Características: Inspiradora, ambiciosa, realista, con horizonte temporal

---

## TÉRMINOS DE PYTHON

### D

**DataFrame**
- Estructura de datos tabular de pandas
- Filas y columnas (como hoja de cálculo)
- *Ejemplo:* `df = pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]})`

---

### L

**Librería (Library)**
- Colección de funciones y herramientas en Python
- *Ejemplos:* pandas, numpy, matplotlib, scipy

---

### N

**NumPy**
- Librería para computación numérica en Python
- Provee arrays multidimensionales y funciones matemáticas
- Base de pandas y scipy

---

### P

**pandas**
- Librería para manipulación y análisis de datos
- Estructuras principales: Series, DataFrame
- *Uso:* `import pandas as pd`

**Pip**
- Gestor de paquetes de Python
- Instalación: `pip install nombre_paquete`

---

### S

**scipy**
- Librería para computación científica
- Módulo `stats`: Estadística y pruebas de hipótesis
- *Uso:* `from scipy import stats`

**seaborn**
- Librería de visualización estadística
- Basada en matplotlib, con gráficos más estéticos
- *Uso:* `import seaborn as sns`

**statsmodels**
- Librería para modelos estadísticos
- Regresión, series de tiempo, pruebas
- *Uso:* `import statsmodels.api as sm`

---

## SÍMBOLOS ESTADÍSTICOS

| Símbolo | Significado |
|---------|-------------|
| α (alfa) | Nivel de significancia, Error Tipo I |
| β (beta) | Error Tipo II |
| μ (mu) | Media poblacional |
| σ (sigma) | Desviación estándar poblacional |
| σ² | Varianza poblacional |
| x̄ (x barra) | Media muestral |
| s | Desviación estándar muestral |
| s² | Varianza muestral |
| n | Tamaño de muestra |
| N | Tamaño de población |
| H₀ | Hipótesis nula |
| H₁ o Hₐ | Hipótesis alternativa |
| p | Valor p (p-value) |
| r | Coeficiente de correlación de Pearson |
| R² | Coeficiente de determinación |
| t | Estadístico t (t-test) |
| F | Estadístico F (ANOVA) |
| χ² (chi cuadrado) | Estadístico chi-cuadrado |
| df | Grados de libertad (degrees of freedom) |
| SE | Error estándar (Standard Error) |
| CI | Intervalo de confianza (Confidence Interval) |

---

## ABREVIATURAS COMUNES

| Abreviatura | Significado |
|-------------|-------------|
| ONG | Organización No Gubernamental |
| KPI | Key Performance Indicator |
| NPS | Net Promoter Score |
| ODS | Objetivos de Desarrollo Sostenible |
| SDG | Sustainable Development Goals (ODS en inglés) |
| SMART | Specific, Measurable, Achievable, Relevant, Time-bound |
| FODA | Fortalezas, Oportunidades, Debilidades, Amenazas |
| SWOT | Strengths, Weaknesses, Opportunities, Threats (FODA en inglés) |
| BCG | Boston Consulting Group |
| PESTEL | Political, Economic, Social, Technological, Environmental, Legal |
| ROI | Return on Investment |
| SROI | Social Return on Investment |
| CSV | Comma-Separated Values |
| URL | Uniform Resource Locator |
| API | Application Programming Interface |

---

## 📝 Cómo Usar Este Glosario

1. **Durante la lectura:** Si encuentras un término desconocido, búscalo aquí
2. **Antes de exámenes:** Repasa los términos clave de cada módulo
3. **En análisis de datos:** Consulta símbolos y fórmulas
4. **En presentaciones:** Verifica que usas la terminología correctamente

---

## 🔄 Actualizaciones

Este glosario se actualizará conforme avanza el curso.

**Sugerencias de términos:**
Si crees que falta un término importante, contáctanos:
- GitHub: Abre un Issue
- Email: [instructor@tec.mx]

---

**Última actualización:** Noviembre 2025
