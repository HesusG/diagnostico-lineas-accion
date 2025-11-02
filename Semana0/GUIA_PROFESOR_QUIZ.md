# 👨‍🏫 Guía para Profesores: Quiz Diagnóstico Markdown

## 📋 Descripción General

El **Quiz Diagnóstico Markdown** (`quiz_diagnostico.md`) es una herramienta diseñada para evaluar rápidamente el nivel de conocimientos de todo el grupo antes de iniciar el curso.

**Objetivo:** Adaptar el ritmo y contenido del curso según el nivel real de los estudiantes.

---

## 🎯 ¿Por Qué Usar Este Quiz?

### **Problemas que resuelve:**

1. **Desconoces el nivel real del grupo**
   - ¿Son principiantes totales o tienen experiencia previa?
   - ¿Necesitas más tiempo en Python básico o puedes acelerar?

2. **Dificultad para formar equipos balanceados**
   - Sin datos, los equipos pueden quedar desbalanceados
   - Estudiantes avanzados se aburren, principiantes se frustran

3. **No sabes qué herramientas de IA usan**
   - ¿Usan ChatGPT o herramientas más sofisticadas?
   - ¿Conocen agentes o solo chat básico?
   - ¿Necesitas enseñar uso ético de IA desde cero?

4. **Estadística previa incierta**
   - ¿Recuerdan conceptos básicos o necesitas repasar desde cero?
   - ¿Conocen p-values o es completamente nuevo?

### **Beneficios de usarlo:**

- ✅ **Datos cuantitativos en 10-15 min** (no 45-60 min del quiz interactivo)
- ✅ **Análisis automático** con script Python incluido
- ✅ **Visualizaciones** para presentar en clase
- ✅ **Recomendaciones pedagógicas** basadas en resultados
- ✅ **Identificación de perfiles** (principiantes/intermedios/avanzados)

---

## 🚀 Implementación Paso a Paso

### **Opción 1: Google Forms (Recomendado)**

#### **Paso 1: Crear formulario**

1. Ve a [Google Forms](https://forms.google.com/)
2. Crea un nuevo formulario: "Quiz Diagnóstico - CD2001B"
3. Abre `quiz_diagnostico.md` en tu editor
4. Copia cada pregunta al formulario:

**Para preguntas de opción única (🔘):**
- Tipo: "Opción múltiple" (círculos)
- Copia las opciones A-E

**Para preguntas de opción múltiple (☑️):**
- Tipo: "Casillas de verificación" (cuadrados)
- Copia todas las opciones
- En "Validación": Opcional - "Seleccione al menos 1"

5. **Configuración recomendada:**
   - ✅ Limitar a 1 respuesta por persona (requiere cuenta Google)
   - ✅ Recopilar direcciones de correo
   - ✅ Permitir edición después de enviar
   - ❌ No hacer obligatorias las preguntas (para evitar abandonos)

#### **Paso 2: Distribuir**

**Opción A: Antes del inicio del curso**
```
Asunto: [ACCIÓN REQUERIDA] Quiz Diagnóstico - CD2001B

Hola,

Antes de iniciar el curso, necesito conocer tu nivel actual en estadística,
Python e IA para adaptar el contenido a las necesidades del grupo.

📋 Por favor completa este quiz diagnóstico:
[LINK AL FORMULARIO]

⏱️ Tiempo: 10-15 minutos
🎯 No es calificado - solo diagnóstico
✅ Fecha límite: [FECHA]

Responde honestamente - esto me ayudará a:
• Ajustar el ritmo del curso
• Identificar estudiantes que necesitan apoyo adicional
• Formar equipos balanceados

¡Nos vemos en clase!
[Tu nombre]
```

**Opción B: Primera clase**
- Dedica los primeros 15 minutos para que lo completen
- Puedes analizar resultados mientras hacen introducción

#### **Paso 3: Exportar datos**

1. En Google Forms, ve a "Respuestas"
2. Click en el ícono de Google Sheets (crear hoja de cálculo)
3. Descarga como CSV: Archivo → Descargar → Valores separados por comas (.csv)
4. Guarda como `respuestas_quiz_diagnostico.csv`

#### **Paso 4: Analizar con el script**

```bash
cd Semana0
python analizar_quiz_diagnostico.py respuestas_quiz_diagnostico.csv
```

**Salida del script:**
- Estadísticas en consola (copiables para reporte)
- Gráficos en `analisis_quiz_diagnostico.png` (4 visualizaciones)

---

### **Opción 2: Microsoft Forms**

Proceso similar a Google Forms:

1. Ve a [Microsoft Forms](https://forms.office.com/)
2. Crea nuevo formulario
3. Copia preguntas de `quiz_diagnostico.md`
4. Exporta a Excel → Guarda como CSV
5. Usa el script analizador

---

### **Opción 3: Impreso (Presencial)**

Si prefieres papel:

1. Imprime `quiz_diagnostico.md` (una copia por estudiante)
2. Distribuye en clase
3. Recopila respuestas
4. Captura manualmente en Excel/Google Sheets:

**Estructura del CSV:**

| nombre | matricula | nivel_estadistica | nivel_python | uso_colab | frecuencia_ia | uso_apis_agentes | situacion_actual |
|--------|-----------|-------------------|--------------|-----------|---------------|------------------|------------------|
| Juan P | A00123 | C) Tomé estadística... | D) Puedo escribir... | D) Lo uso regularmente | D) Frecuentemente | A) No, solo chat | D) Uso IA regularmente... |

5. Guarda como CSV y usa el script analizador

---

## 📊 Interpretación de Resultados

### **Perfil 1: Grupo Principiante (>50% responde A-B en Preg 1, 7, 12)**

**Características:**
- Poca o nula experiencia en estadística
- Python básico o nulo
- Uso limitado de IA

**Adaptaciones recomendadas:**

1. **Semana 0 obligatoria** (no opcional)
   - Dedicar sesión completa a repaso
   - Crear tutoriales grabados de Python básico

2. **Ritmo más lento en Semana 1-2**
   - Más ejemplos paso a paso
   - Ejercicios guiados con hints
   - Sesiones de Q&A adicionales

3. **Soporte adicional:**
   - Horas de oficina extendidas
   - TAs disponibles para consultas
   - Grupos de estudio facilitados

4. **Expectativas realistas:**
   - Workshop 1 puede dividirse en 2 entregas
   - Permitir más tiempo para práctica extra

---

### **Perfil 2: Grupo Mixto (Distribución balanceada A-E)**

**Características:**
- Mezcla de principiantes, intermedios y avanzados
- Niveles heterogéneos

**Adaptaciones recomendadas:**

1. **Diferenciación:**
   - Crear ejercicios "básicos" y "desafío"
   - Permitir que avanzados salten Semana 0
   - Material extra para quienes terminen rápido

2. **Peer learning:**
   - Formar equipos balanceados (1 avanzado + 2 intermedios + 1 principiante)
   - Roles de "mentor" para estudiantes avanzados
   - Sessions de peer tutoring

3. **Recursos opcionales:**
   - Videos de repaso para principiantes
   - Ejercicios avanzados opcionales para avanzados

---

### **Perfil 3: Grupo Avanzado (>50% responde D-E en Preg 1, 7, 12)**

**Características:**
- Experiencia sólida en estadística y Python
- Uso frecuente de IA, algunos con APIs/agentes

**Adaptaciones recomendadas:**

1. **Acelerar el ritmo:**
   - Semana 0 completamente opcional
   - Combinar Semanas 1-2 en una (comprimida)
   - Enfocarse en aplicaciones avanzadas

2. **Contenido más desafiante:**
   - Casos de negocio complejos
   - Datasets grandes (>10k registros)
   - Técnicas avanzadas (bootstrapping, simulación Monte Carlo)

3. **Proyectos aplicados:**
   - Conectar con empresas reales para casos
   - Proyectos capstone desde Semana 3

---

## 🔍 Insights Específicos por Pregunta

### **Pregunta 15: Uso de APIs/Agentes**

**Si >30% responde C-E (usan APIs o agentes):**

**Implicaciones:**
- Estudiantes están adoptando IA de manera sofisticada
- Pueden ayudar a compañeros con uso de herramientas
- Oportunidad para ejercicios que integren IA

**Recomendaciones:**
- Mostrar ejemplos de uso de APIs de OpenAI en Python
- Permitir (con restricciones) uso de agentes en proyectos
- Discutir ética y limitaciones de agentes autónomos

**Si <10% responde C-E:**
- Grupo usa IA de manera básica (solo chat)
- Necesitan educación sobre herramientas avanzadas
- Oportunidad para enseñar uso productivo de IA

---

### **Pregunta 5: P-values**

**Si >50% responde A o E (no saben o respuesta incorrecta):**

**Acción:**
- Dedicar tiempo extra a pruebas de hipótesis
- Crear analogías y ejemplos intuitivos
- No asumir conocimiento previo de inferencia estadística

**Si >70% responde C (correcto):**
- Pueden avanzar más rápido en Semana 1
- Enfocarse en aplicaciones vs teoría básica

---

### **Pregunta 9: ¿Qué es pandas?**

**Si >40% responde A (no saben):**

**Acción:**
- Tutorial de pandas obligatorio antes de Semana 1
- Crear "Pandas Cheat Sheet" de referencia
- Ejemplos paso a paso en todos los notebooks

**Si >80% responde C (correcto):**
- Pueden saltar introducción básica de pandas
- Ir directo a operaciones avanzadas (groupby, merge)

---

## 📈 Métricas Clave a Monitorear

### **Indicadores de Riesgo:**

| Indicador | Umbral de Alerta | Acción Recomendada |
|-----------|------------------|---------------------|
| % que nunca ha programado Python (Preg 7A) | >30% | Semana 0 obligatoria + tutoriales extra |
| % que no sabe qué es pandas (Preg 9A) | >40% | Workshop de pandas (2 horas) |
| % que no sabe qué es p-value (Preg 5A) | >50% | Repasar fundamentos de inferencia estadística |
| % que nunca ha usado Colab (Preg 10A-B) | >25% | Sesión práctica guiada de Colab |
| % que no usa IA (Preg 12A) | >15% | Introducción obligatoria a IA generativa |

### **Indicadores de Oportunidad:**

| Indicador | Umbral | Oportunidad |
|-----------|--------|-------------|
| % que usa APIs/agentes (Preg 15C-E) | >25% | Integrar ejercicios con APIs |
| % con experiencia avanzada Python (Preg 7E) | >20% | Roles de mentor/TA |
| % que usa IA frecuentemente (Preg 12D-E) | >50% | Casos de uso avanzados de IA |

---

## 🛠️ Uso del Script Analizador

### **Instalación de Dependencias:**

```bash
pip install pandas matplotlib seaborn
```

### **Ejecución:**

```bash
python analizar_quiz_diagnostico.py respuestas_quiz_diagnostico.csv
```

### **Salida Esperada:**

```
╔═══════════════════════════════════════════════════════════════════╗
║  ANALIZADOR DE QUIZ DIAGNÓSTICO - CD2001B                         ║
╚═══════════════════════════════════════════════════════════════════╝

Total de estudiantes: 35

======================================================================
📈 SECCIÓN 1: CONOCIMIENTOS DE ESTADÍSTICA
======================================================================

🔍 Nivel actual de conocimiento en estadística:
A)    8  (22.9%)
B)   12  (34.3%)
C)   10  (28.6%)
D)    4  (11.4%)
E)    1  ( 2.9%)

======================================================================
💻 SECCIÓN 2: EXPERIENCIA CON PYTHON
======================================================================

🐍 Nivel de experiencia con Python:
...

👥 PERFILES DE ESTUDIANTES:
   Principiantes: 12 (34.3%)
   Intermedios: 18 (51.4%)
   Avanzados: 5 (14.3%)

💡 RECOMENDACIONES:
   ⚠️  Grupo mixto - considerar:
      • Ejercicios diferenciados (básicos + desafío)
      • Equipos balanceados
      • Material de nivelación para principiantes
```

### **Visualizaciones Generadas:**

El script crea `analisis_quiz_diagnostico.png` con 4 gráficos:

1. **Top-left:** Nivel de estadística (distribución)
2. **Top-right:** Nivel de Python (distribución)
3. **Bottom-left:** Frecuencia de uso de IA
4. **Bottom-right:** Experiencia con Google Colab

**Uso:** Presenta estos gráficos en la primera clase para contextualizar el curso.

---

## 💡 Consejos Prácticos

### **Timing Óptimo:**

**Opción A: Pre-curso (Recomendado)**
- Enviar 1 semana antes del inicio
- Fecha límite: 2 días antes de primera clase
- Ventaja: Tiempo para adaptar syllabus

**Opción B: Primera clase**
- Primeros 15 minutos de clase
- Analizar mientras introducción del curso
- Ventaja: Participación garantizada

**Opción C: Post-Semana 0**
- Después de completar material introductorio
- Ventaja: Evaluación de aprendizaje

### **Incentivos para Completar:**

- **Puntos extra:** 1-2% de calificación final
- **Prioridad:** Para formar equipos de proyecto
- **Transparencia:** "Esto me ayuda a adaptar el curso a USTEDES"

### **Comunicación de Resultados:**

En segunda clase, comparte resumen agregado:

> "Basándome en el quiz diagnóstico:
> - 35% son nuevos en Python → Tendremos tutoriales extras
> - 80% usan ChatGPT → Discutiremos uso ético en Semana 1
> - 60% conocen estadística básica → Podemos acelerar repaso
>
> Gracias por completarlo, esto me ayuda a servir mejor al grupo."

---

## 🔒 Privacidad y Ética

### **Buenas Prácticas:**

1. **Anonimización en reportes:**
   - Solo comparte estadísticas agregadas con el grupo
   - No identifiques a estudiantes individualmente en público

2. **Uso de datos:**
   - Solo para adaptar el curso
   - No para pre-juzgar capacidades

3. **Transparencia:**
   - Explica el propósito del quiz
   - Asegura que no es calificado

4. **Consentimiento:**
   - Si publicas resultados en paper/conferencia, pide consentimiento
   - Anonimiza completamente

---

## ❓ FAQ para Profesores

**P: ¿Cuánto tiempo toma analizar los resultados?**
R: Con el script, 5-10 minutos. Manualmente, 30-45 minutos para grupo de 30 estudiantes.

**P: ¿Qué hago si nadie completa el quiz?**
R: Ofrece puntos extra (1-2%). Envía recordatorio 2 días antes de deadline. En última instancia, hazlo en clase.

**P: ¿Debo modificar el quiz para mi contexto?**
R: Sí, siéntete libre. Agrega preguntas sobre tu industria específica o herramientas que uses.

**P: ¿El script funciona con respuestas parciales?**
R: Sí, maneja valores faltantes. Sin embargo, alienta completitud.

**P: ¿Puedo compartir resultados con TAs?**
R: Sí, es útil para que TAs sepan nivel del grupo. Recuérdales confidencialidad.

---

## 📞 Soporte

**¿Problemas con el script?**
- Verifica que pandas, matplotlib, seaborn estén instalados
- Asegúrate de que CSV tenga columnas correctas
- Revisa que no haya caracteres especiales en respuestas

**¿Necesitas ayuda para adaptar el quiz?**
- Contacta al autor del curso
- Revisa `quiz_diagnostico.md` para ver estructura

---

**¡Buena suerte con tu implementación!** 🎓

Este quiz te ahorrará semanas de ajustes al adaptar el curso desde el inicio.
