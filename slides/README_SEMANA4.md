# Slides de Semana 4: Visualización de Datos

## 📊 Estructura de Presentaciones

La Semana 4 está organizada en **6 presentaciones** que cubren todo el espectro de visualización de datos, desde fundamentos hasta herramientas prácticas.

---

## 🎯 Orden Recomendado de Presentación

### **Sesión 1: Fundamentos (3 horas)**

#### 1. **Fundamentos de Visualización de Datos**
📁 `semana4-fundamentos-visualizacion.md`

**Duración:** 60 minutos

**Contenido:**
- Principios de diseño visual (jerarquía, minimalismo, color, etiquetas)
- Catálogo de tipos de gráficos (barras, líneas, scatter, heatmaps)
- Anti-patterns comunes (3D, ejes truncados, demasiados colores)

**Objetivo:** Entender CUÁNDO y CÓMO usar cada tipo de visualización

---

#### 2. **Herramientas de Business Intelligence**
📁 `semana4-herramientas-bi-ecosistema.md`

**Duración:** 60 minutos

**Contenido:**
- Historia de BI (Excel → Tableau → Power BI → Looker Studio)
- Comparativa de las 3 grandes herramientas
- Certificaciones y recursos de aprendizaje
- Concursos de visualización (Iron Viz, DataViz Championships)

**Objetivo:** Conocer el ecosistema de herramientas y elegir la adecuada

---

#### 3. **Visualización en el Pipeline de Datos**
📁 `semana4-dataviz-en-pipeline.md`

**Duración:** 60 minutos

**Contenido:**
- Pipeline completo: Fuentes → Extracción → Transformación → Almacenamiento → Visualización → Decisiones
- ETL vs ELT
- Opciones de almacenamiento (Sheets, BigQuery, Data Warehouse)
- Alternativas modernas (Streamlit, Retool, Zero-ETL)

**Objetivo:** Entender que la visualización es PARTE de un sistema completo

---

### **Sesión 2: Looker Studio Práctico (3 horas)**

#### 4. **Tutorial de Looker Studio con Fundación Teletón** ⭐
📁 `semana4-looker-studio-tutorial.md`

**Duración:** 90 minutos

**Contenido:**
- **Preparación de datos:** Del CSV a Google Sheets (Pasos 1-3)
- **Conexión:** Conectar Looker Studio (Pasos 4-5)
- **Construcción:**
  - KPIs (4 scorecards)
  - Gráfico de barras con formato condicional
  - Gráfico de líneas (tendencias)
  - Tabla detallada
  - Heatmap (tabla pivot)
- **Interactividad:** Filtros (giro, canal, satisfacción)
- **Diseño:** Tema corporativo Teletón
- **Storytelling:** Cuadros de texto con insights
- **Entrega:** Compartir y exportar PDF

**Objetivo:** Crear un dashboard completo de principio a fin

**Hands-on:** Los estudiantes siguen el tutorial paso a paso con datos de Teletón

---

### **Sesión 3: Streamlit como Alternativa (90 minutos)**

#### 5. **Introducción a Streamlit**
📁 `semana4-streamlit-introduccion.md`

**Duración:** 90 minutos

**Contenido:**
- **Instalación y primer dashboard** (10 minutos)
- **Componentes básicos:** Texto, datos, gráficos, widgets
- **Layout:** Columnas, sidebar, tabs
- **Caching** para performance
- **Dashboard Teletón completo** (código completo)
- **Deployment:** Streamlit Cloud gratuito
- **Comparación:** Looker Studio vs Streamlit
- **Casos de uso avanzados:** ML, upload dinámico, autenticación

**Objetivo:** Mostrar alternativa con Python para estudiantes técnicos

**Nota:** Esta presentación es OPCIONAL. Se muestra como "alternativa en paralelo" para quienes quieran control total con código.

---

## 📋 Resumen de Slides por Tema

| Slide | Tema Principal | Enfoque | Audiencia |
|-------|----------------|---------|-----------|
| `fundamentos-visualizacion.md` | Teoría de diseño | Conceptual | Todos |
| `herramientas-bi-ecosistema.md` | Comparativa de herramientas | Panorama | Todos |
| `dataviz-en-pipeline.md` | Arquitectura de datos | Contexto técnico | Todos |
| `looker-studio-tutorial.md` | **Tutorial paso a paso** | **Práctico hands-on** | **Todos (CORE)** |
| `streamlit-introduccion.md` | Alternativa con Python | Código/Avanzado | Opción técnica |

---

## 🎓 Alineación con Evaluación

### **Actividad #2 (Parte 1): Preparación de Datos**

**Slides relevantes:**
- `dataviz-en-pipeline.md` (Pasos 1-3: Fuentes, Extracción, Transformación)
- `looker-studio-tutorial.md` (Pasos 1-3: CSV → Google Sheets)

**Entregable:**
- Jupyter Notebook con limpieza de datos
- CSV/Google Sheets listo para dashboard

---

### **Actividad #2 (Parte 2): Dashboard Looker Studio**

**Slides relevantes:**
- `fundamentos-visualizacion.md` (Qué gráficos usar)
- `looker-studio-tutorial.md` (Pasos 4-15: Construcción completa)

**Entregable:**
- Link a dashboard Looker Studio
- PDF exportado
- Documento de interpretación (1-2 páginas)

---

## 🔄 Flujo de Clase Sugerido

### **Día 1: Teoría (3 horas)**

```
09:00 - 10:00 | Fundamentos de Visualización
              | - Principios de diseño
              | - Tipos de gráficos
              | - Anti-patterns

10:00 - 11:00 | Herramientas de BI
              | - Historia de BI
              | - Tableau vs Power BI vs Looker Studio
              | - Recursos y certificaciones

11:00 - 12:00 | Pipeline de Datos
              | - ETL vs ELT
              | - Opciones de almacenamiento
              | - Alternativas modernas
```

---

### **Día 2: Práctica Looker Studio (3 horas)**

```
09:00 - 09:15 | Intro: Qué vamos a construir (dashboard Teletón)

09:15 - 09:45 | Preparación de Datos (Pasos 1-3)
              | - Limpiar CSV en Python
              | - Exportar a Google Sheets
              | - Columnas calculadas

09:45 - 10:30 | Conexión y KPIs (Pasos 4-6)
              | - Conectar Looker Studio
              | - Crear 4 scorecards
              | - Aplicar colores Teletón

10:30 - 11:15 | Gráficos (Pasos 7-10)
              | - Barras con formato condicional
              | - Líneas de tendencia
              | - Tabla detallada
              | - Heatmap

11:15 - 11:45 | Interactividad y Diseño (Pasos 11-13)
              | - Filtros (giro, canal, satisfacción)
              | - Tema corporativo
              | - Insights con cuadros de texto

11:45 - 12:00 | Entrega (Pasos 14-15)
              | - Compartir link
              | - Exportar PDF
              | - Checklist de calidad
```

---

### **Día 3 (Opcional): Streamlit (90 minutos)**

```
09:00 - 09:30 | Intro a Streamlit
              | - Instalación
              | - Primer dashboard en 10 min
              | - Componentes básicos

09:30 - 10:15 | Dashboard Teletón con Streamlit
              | - Código completo
              | - KPIs, gráficos, filtros
              | - Tabs y sidebar

10:15 - 10:30 | Deployment y Cierre
              | - Streamlit Cloud (gratis)
              | - Comparación final: Looker vs Streamlit
              | - Casos de uso avanzados
```

**Nota:** Esta sesión es OPCIONAL. Solo para estudiantes interesados en Python avanzado.

---

## 📦 Materiales Complementarios

### **Datos para Práctica**

```
📁 Semana4/datos/
├── teleton_benefactores.csv (274 registros)
└── teleton_benefactores_clean.csv (procesado)
```

**Variables:**
- `benefactor_id`: ID único
- `empresa`: Nombre de la empresa
- `giro`: Sector (Salud, Educación, Retail, etc.)
- `canal_apoyo`: Tipo de apoyo (Donación, Patrocinio, Voluntariado)
- `region`: Geográfica (Norte, Sur, Este, Oeste, Centro)
- `tiempo_colaboracion`: Años colaborando
- `satisfaccion`: Escala 1-10
- `recomendaria`: Sí/No
- `comentarios`: Texto libre

---

### **Código de Soporte**

```
📁 Semana4/notebooks/
├── 01_preparacion_datos_looker.ipynb
│   └── Limpieza y transformación para Looker
├── 02_visualizacion_python.ipynb
│   └── Gráficos con Matplotlib/Plotly
└── 03_dashboard_streamlit_basico.ipynb
    └── Template de Streamlit
```

---

### **Plantillas**

```
📁 Semana4/plantillas/
├── plantilla_dashboard_ong.md
│   └── Template para cualquier ONG
└── checklist_visualizacion.md
    └── Lista de verificación de calidad
```

---

## 🎨 Paleta de Colores Teletón

**Para usar en Looker Studio y Streamlit:**

```python
# Colores oficiales Fundación Teletón
TELETON_COLORS = {
    'azul_primary':   '#00A3E0',  # Azul principal
    'rosa_secondary': '#E30074',  # Rosa vibrante
    'verde_success':  '#8DC63F',  # Verde éxito
    'amarillo_alert': '#FFB612',  # Amarillo advertencia
    'azul_dark':      '#004B87',  # Azul oscuro (contraste)
    'gris_text':      '#333333',  # Texto
    'blanco':         '#FFFFFF',  # Fondo
}
```

**Aplicar en Looker Studio:**
- Tema → Personalizar → Introducir códigos hexadecimales

**Aplicar en Streamlit:**
```python
import plotly.express as px

fig = px.bar(df, x='giro', y='satisfaccion',
             color_discrete_sequence=['#00A3E0'])
```

---

## 🔗 Enlaces Útiles

### **Herramientas**

- **Looker Studio:** https://lookerstudio.google.com
- **Streamlit Cloud:** https://share.streamlit.io
- **Google Sheets:** https://sheets.google.com

### **Inspiración**

- **Looker Studio Gallery:** https://lookerstudio.google.com/gallery
- **Tableau Viz of the Day:** https://public.tableau.com/app/discover/viz-of-the-day
- **Streamlit Gallery:** https://streamlit.io/gallery

### **Aprendizaje**

- **Data Viz Project:** https://datavizproject.com (catálogo de gráficos)
- **ColorBrewer:** https://colorbrewer2.org (paletas accesibles)
- **Streamlit Docs:** https://docs.streamlit.io

---

## ✅ Checklist para Profesores

**Antes de la clase:**
- [ ] Descargar datos de Teletón (`teleton_benefactores.csv`)
- [ ] Probar tutorial de Looker Studio (steps 1-15)
- [ ] Crear cuenta en Looker Studio (Google)
- [ ] Preparar Google Sheets de ejemplo
- [ ] (Opcional) Instalar Streamlit para demostración

**Durante la clase:**
- [ ] Compartir slides vía proyector
- [ ] Demostrar Looker Studio en vivo (no solo slides)
- [ ] Ayudar a estudiantes con conexión a Google Sheets
- [ ] Resolver problemas comunes (ver slide "Troubleshooting")
- [ ] Recordar fecha límite de Actividad #2

**Después de la clase:**
- [ ] Compartir links de recursos adicionales
- [ ] Publicar ejemplo de dashboard completo
- [ ] Abrir foro de Canvas para preguntas
- [ ] Preparar rúbrica de evaluación

---

## 🆘 Problemas Comunes y Soluciones

### **Problema 1: "No tengo cuenta Google"**

**Solución:**
- Crear cuenta gratuita @gmail.com
- O usar cuenta institucional @tec.mx

---

### **Problema 2: "Looker Studio no encuentra mi Google Sheet"**

**Causas:**
- Sheets no compartido con cuenta correcta
- Permisos insuficientes

**Solución:**
```
1. Abrir Google Sheets
2. Compartir → Cambiar a "Cualquiera con el enlace"
3. Permisos: "Puede ver"
4. En Looker Studio → Refrescar conectores
```

---

### **Problema 3: "Dashboard muy lento"**

**Causas:**
- Demasiados datos en Sheets (>10K filas)
- Campos calculados complejos

**Solución:**
```
1. Filtrar datos en Python antes de exportar
   (ej: solo últimos 12 meses)
2. Precalcular métricas en Sheets
3. Usar extractos de datos (cache)
```

---

### **Problema 4: "Streamlit no se instala"**

**Solución:**
```bash
# Actualizar pip
pip install --upgrade pip

# Instalar en entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install streamlit

# Verificar
streamlit --version
```

---

## 📝 Notas para el Instructor

### **Tiempo por Slide**

- **Fundamentos:** ~40-50 slides → 60 min → ~1 min/slide
- **Herramientas BI:** ~35-40 slides → 60 min → ~1.5 min/slide
- **Pipeline:** ~30-35 slides → 60 min → ~2 min/slide
- **Looker Tutorial:** ~50-60 slides → 90 min → ~1.5 min/slide (incluye práctica)
- **Streamlit:** ~40-45 slides → 90 min → ~2 min/slide (incluye código)

### **Énfasis Sugerido**

**Fundamentos:**
- ⭐⭐⭐ Anti-patterns (estudiantes cometen estos errores)
- ⭐⭐⭐ Matriz de decisión de gráficos
- ⭐⭐ Principios de color

**Looker Studio:**
- ⭐⭐⭐ Pasos 6-10 (construcción de gráficos)
- ⭐⭐⭐ Paso 11 (filtros interactivos)
- ⭐⭐ Paso 13 (storytelling)
- ⭐ Paso 15 (compartir)

**Streamlit:**
- ⭐⭐⭐ Dashboard completo (código de ejemplo)
- ⭐⭐ Deployment (para que puedan compartir)
- ⭐ Casos avanzados (solo mencionar)

---

## 🎯 Competencias Desarrolladas

**SCD0105.B - Gráficos Dinámicos:**
- ✅ Crear dashboards interactivos
- ✅ Seleccionar visualizaciones apropiadas
- ✅ Aplicar principios de diseño
- ✅ Comunicar insights efectivamente

**Evidencia de logro:**
- Dashboard Looker Studio completo (Actividad #2 Parte 2)
- Documento de interpretación con insights accionables

---

## 📚 Lecturas Asignadas

**Obligatoria:**
- Knaflic, C. "Storytelling with Data" - Capítulos 1-4

**Complementaria:**
- Tufte, E. "The Visual Display of Quantitative Information"
- Cairo, A. "The Truthful Art"

---

## 🔄 Mejoras Futuras

**Sugerencias para próximas versiones:**

1. **Agregar slide de accesibilidad** (WCAG, color blindness)
2. **Ejemplos de dashboards reales** de ONGs mexicanas
3. **Video tutoriales** embebidos en slides
4. **Quiz interactivo** post-cada sección
5. **Template de dashboard** pre-configurado para clonar

---

**Última actualización:** Enero 2025
**Versión:** 1.0
**Autor:** CD2001B Course Team
**Contacto:** carlos.alonso@tec.mx
