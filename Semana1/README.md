# 📊 Semana 1: Introducción a Estadística y Pruebas de Hipótesis

## 📚 Módulo 1 - Parte 1

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:
- ✅ Calcular e interpretar medidas de tendencia central y dispersión
- ✅ Realizar pruebas de hipótesis para una muestra (t de Student)
- ✅ Realizar pruebas de hipótesis para dos muestras (independientes y pareadas)
- ✅ Interpretar p-values y tomar decisiones estadísticas
- ✅ Crear visualizaciones efectivas con Python (histogramas, boxplots)
- ✅ Aplicar estadística a problemas de negocios reales

---

## 📅 Plan Detallado de Clases

Para el **plan detallado día por día** con agendas completas, actividades de equipo opcionales, y notas para el profesor, consulta:

👉 **[PLAN_CLASES.md](PLAN_CLASES.md)** - Plan completo de 4 clases × 2 horas

**Resumen de las 4 clases:**
1. **Clase 1:** Introducción a Estadística Descriptiva (media, mediana, moda)
2. **Clase 2:** Medidas de Dispersión y Visualización (IQR, outliers, boxplots)
3. **Clase 3:** Pruebas de Hipótesis (t-test 1 y 2 muestras)
4. **Clase 4:** Workshop y Revisión (trabajo en clase + Q&A)

---

## 📁 Estructura de la Semana

```
Semana1/
├── README.md                                    # Este archivo
├── notebooks/
│   ├── 01_introduccion_estadistica.ipynb       # Clase 1: Conceptos básicos
│   ├── 02_medidas_tendencia_central.ipynb      # Clase 1-2: Medidas descriptivas
│   └── 03_pruebas_hipotesis_1_2_muestras.ipynb # Clase 3: Pruebas estadísticas
├── ejercicios/
│   ├── ejercicio_medidas_tendencia.ipynb       # Práctica opcional
│   ├── ejercicio_pruebas_hipotesis.ipynb       # Práctica opcional
│   ├── ejercicio_satisfaccion_ong.ipynb        # Práctica opcional
│   └── workshop1_plantilla.ipynb               # ⭐ ENTREGABLE - 10% calificación
├── ejercicios_extra/
│   ├── practica_ong_estadistica_basica.ipynb   # Práctica adicional (ONG)
│   └── practica_ong_estadistica_basica_SOLUCIONES.ipynb
├── datos/
│   ├── ejemplo_satisfaccion_clientes.csv       # Dataset para clases
│   ├── student-alcohol-consumption.csv         # Dataset para Workshop 1
│   ├── fundacion_esperanza_donadores.csv       # Dataset ONG (1000 registros)
│   └── CODEBOOK_fundacion_esperanza.md         # Documentación dataset ONG
└── workshop/
    └── README.md                                # Guía del workshop
```

---

## 📊 Entregables de la Semana

### **🎯 Workshop 1: Análisis Estadístico Básico**

**Archivo:** [workshop1_plantilla.ipynb](ejercicios/workshop1_plantilla.ipynb)
**Dataset:** `student-alcohol-consumption.csv` (consumo de alcohol en estudiantes portugueses)
**Valor:** 10% de la calificación final
**Fecha límite:** Ver calendario del curso

**Contenido del Workshop:**

| Sección | Descripción | Puntos |
|---------|-------------|--------|
| **Parte 1: Análisis Descriptivo** | Medidas de tendencia, dispersión, visualizaciones | 40 pts |
| **Parte 2: Prueba t (1 muestra)** | ¿Calificación promedio es diferente de 12? | 30 pts |
| **Parte 3: Prueba t (2 muestras)** | ¿Diferencia entre bajo vs alto consumo alcohol? | 30 pts |
| **BONUS: Reflexión MEAL** | Análisis académico con citaciones APA 7 | +10 pts |
| **TOTAL** | | **100 pts** (+10 bonus) |

**Lo que necesitas entregar:**
- ✅ Notebook con TODO el código ejecutado (celdas con output visible)
- ✅ TODAS las preguntas de interpretación respondidas
- ✅ Gráficos con títulos y etiquetas claras
- ✅ (Opcional) Reflexión MEAL de 300-400 palabras

**Formato de archivo:** `Workshop1_NombreApellido_Matricula.ipynb`

---

## 🔧 Herramientas Python

### **Librerías principales:**
```python
import pandas as pd              # Manipulación de datos
import numpy as np               # Operaciones numéricas
from scipy import stats          # Funciones estadísticas (t-test, etc.)
import matplotlib.pyplot as plt  # Visualización básica
import seaborn as sns            # Visualización estadística
```

### **Comandos clave:**

**Medidas de tendencia:**
```python
df['columna'].mean()    # Media
df['columna'].median()  # Mediana
df['columna'].mode()[0] # Moda
```

**Medidas de dispersión:**
```python
df['columna'].std()             # Desviación estándar
df['columna'].var()             # Varianza
df['columna'].quantile(0.25)    # Q1
df['columna'].quantile(0.75)    # Q3
```

**Pruebas de hipótesis:**
```python
# Prueba t de 1 muestra
stats.ttest_1samp(df['columna'], valor_comparacion)

# Prueba t de 2 muestras independientes
stats.ttest_ind(grupo1, grupo2)

# Prueba t pareada
stats.ttest_rel(antes, despues)
```

---

## 💡 Tips de Estudio

### **Para aprobar la semana:**

1. **📖 No memorices, entiende:**
   - No importa recordar fórmulas → Python las calcula
   - SÍ importa saber CUÁNDO usar cada prueba
   - SÍ importa INTERPRETAR resultados en contexto

2. **📊 Visualiza primero, calcula después:**
   - Siempre haz histograma/boxplot ANTES de prueba t
   - Las gráficas te dicen si hay diferencias obvias
   - Ayudan a detectar outliers que invalidan pruebas

3. **🤖 Usa IA como asistente, no como reemplazo:**
   - ✅ OK: "Explícame qué es un p-value con una analogía"
   - ✅ OK: "¿Por qué mi código da error?"
   - ❌ NO: "Dame el código completo del workshop"
   - ❌ NO: "Escribe mi reflexión MEAL"

4. **👥 Estudia en grupo:**
   - Explica conceptos a compañeros (mejor forma de aprender)
   - Compara gráficos y resultados
   - Discute interpretaciones

5. **⏰ Gestiona tu tiempo:**
   - Clase 1-2: Domina descriptiva (es la base)
   - Clase 3: Entiende pruebas de hipótesis (40% del workshop)
   - Clase 4: Termina workshop en clase (aprovecha tiempo con profesor)

---

## 🆘 Recursos de Apoyo

### **Material del curso:**
- [Semana 0: Introducción a Herramientas](../Semana0/) - Repaso de Python básico
- [CODEBOOK: Dataset ONG](datos/CODEBOOK_fundacion_esperanza.md) - Documentación completa
- [Práctica extra con ONG](ejercicios_extra/practica_ong_estadistica_basica.ipynb) - Ejercicios adicionales

### **Recursos externos:**

**Estadística:**
- [Khan Academy - Estadística](https://es.khanacademy.org/math/statistics-probability) - Videos en español
- [Stat Quest (YouTube)](https://www.youtube.com/c/joshstarmer) - Explicaciones visuales (inglés)
- [Seeing Theory](https://seeing-theory.brown.edu/es.html) - Visualizaciones interactivas

**Python:**
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) - Referencia rápida
- [SciPy Stats Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html) - Funciones estadísticas
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html) - Ejemplos de gráficos

**Para el workshop:**
- [Guía APA 7 - Citaciones](https://apastyle.apa.org/style-grammar-guidelines/citations) - Para reflexión MEAL
- [Estructura MEAL](ejercicios/workshop1_plantilla.ipynb#MEAL) - Ejemplo completo en workshop

---

## 📚 Lecturas Recomendadas (Opcional)

**Libro de texto principal:**
- Levin, R. I. & Rubin, D. S. (2010). *Estadística para administradores* (7ª ed.). Pearson.
  - **Capítulo 1:** Introducción a estadística
  - **Capítulo 2:** Medidas de tendencia central y dispersión
  - **Capítulo 8:** Pruebas de hipótesis para una muestra
  - **Capítulo 9:** Pruebas de hipótesis para dos muestras

**Complementaria:**
- Newbold, P., Carlson, W. & Thorne, B. (2013). *Estadística para administración y economía* (8ª ed.). Pearson.

---

## ❓ Preguntas Frecuentes

**P: ¿Puedo usar Excel o SPSS en lugar de Python?**
R: El curso está diseñado para Python, pero puedes usar otras herramientas para **verificar** resultados. El entregable debe ser en Python (Jupyter Notebook).

**P: ¿Qué hago si no tengo experiencia con Python?**
R:
1. Completa [Semana 0](../Semana0/) primero (2-3 horas)
2. Mira videos de Khan Academy sobre pandas
3. Copia y modifica código de los notebooks de clase
4. Pide ayuda a IA: "Explica este código línea por línea"

**P: ¿Los ejercicios opcionales cuentan para la calificación?**
R: No, pero **altamente recomendados**. Te preparan para el workshop (que sí cuenta 10%).

**P: ¿Qué pasa si no entrego el workshop a tiempo?**
R: Consulta la política de entregas tardías en el syllabus del curso.

**P: ¿Puedo trabajar el workshop en equipo?**
R: Puedes discutir conceptos, pero cada quien entrega su propio notebook. **No copies código de compañeros** - es plagio académico.

**P: ¿Cómo sé si mi interpretación de p-value es correcta?**
R: Usa este template:
> "Con un p-value de [X.XX] y α = 0.05, [rechazamos/no rechazamos] H₀. Esto significa que [interpretación en contexto del negocio]."

**P: ¿Qué son las actividades de equipo opcionales?**
R: Son actividades cortas (10-20 min) que el profesor **puede** usar en clase para reforzar conceptos de forma interactiva. No son obligatorias ni calificadas.

---

## 🚀 Próximos Pasos

**Al terminar Semana 1:**
1. ✅ Dominas estadística descriptiva
2. ✅ Sabes hacer pruebas t en Python
3. ✅ Puedes interpretar p-values
4. ✅ Has completado Workshop 1 (10% de tu calificación)

**Siguiente semana:**
- [Semana 2: Pruebas Estadísticas Avanzadas](../Semana2/)
  - Chi-cuadrada (variables categóricas)
  - ANOVA (comparar 3+ grupos)
  - Regresión lineal (predecir variables continuas)

---

## 📝 Checklist de la Semana

Marca las actividades completadas:

**Antes de Clase 1:**
- [ ] Revisé [Semana 0](../Semana0/) si necesito repaso de Python
- [ ] Tengo Google Colab funcionando
- [ ] Descargué/accedí a los notebooks

**Durante Clase 1:**
- [ ] Completé Notebook 01
- [ ] Entendí diferencia entre media/mediana/moda
- [ ] (Opcional) Participé en actividad "IA Explainer Battle"

**Entre Clase 1-2:**
- [ ] Completé Notebook 02 hasta sección 7
- [ ] Practiqué con ejercicio de medidas de tendencia

**Durante Clase 2:**
- [ ] Entendí varianza, desv. estándar, IQR
- [ ] Sé cómo detectar outliers
- [ ] Puedo crear e interpretar boxplots
- [ ] (Opcional) Participé en "Visualización Challenge"

**Entre Clase 2-3:**
- [ ] Leí introducción de Notebook 03 (conceptos de hipótesis)
- [ ] Entiendo qué es H₀ y H₁

**Durante Clase 3:**
- [ ] Sé cuándo usar prueba t de 1 muestra
- [ ] Sé cuándo usar prueba t de 2 muestras
- [ ] Puedo interpretar un p-value
- [ ] (Opcional) Creé diagrama Mermaid del árbol de decisión

**Entre Clase 3-4:**
- [ ] Completé Notebook 03
- [ ] Practiqué con ejercicio de pruebas de hipótesis

**Durante Clase 4:**
- [ ] Entendí la rúbrica del Workshop 1
- [ ] Trabajé en Workshop 1 en clase
- [ ] Resolví dudas con profesor
- [ ] (Opcional) Participé en debate correlación vs causalidad

**Después de Clase 4:**
- [ ] **Entregué Workshop 1 completo y a tiempo** ⭐

---

**¡Éxito en tu primera semana!** 📊🚀

Recuerda: La estadística no es solo matemáticas - es **tomar decisiones informadas con datos**. ¡Cada empresa necesita personas que sepan hacer esto!
