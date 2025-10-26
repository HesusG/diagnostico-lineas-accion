# Guía: Tipos de Gráficos y Cuándo Usarlos

## 🎯 La Pregunta Clave

> **"¿Qué quiero que mi audiencia entienda?"**

No existe "el mejor gráfico". Existe **el gráfico correcto para cada mensaje**.

---

## 📊 Matriz de Decisión: ¿Qué Gráfico Usar?

| Tu Objetivo | Tipo de Gráfico Recomendado |
|-------------|------------------------------|
| **Comparar categorías** | Barras, Columnas |
| **Mostrar distribución** | Histograma, Boxplot, Violin |
| **Mostrar tendencia temporal** | Líneas, Áreas |
| **Mostrar relación entre 2 variables** | Scatter Plot, Regresión |
| **Mostrar composición (partes de un todo)** | Pie Chart, Donut, Stacked Bar, Treemap |
| **Mostrar jerarquía** | Treemap, Sunburst |
| **Mostrar geolocalización** | Mapa, Mapa de Burbujas |
| **Mostrar un valor único (KPI)** | Scorecard, Gauge |
| **Mostrar muchas variables** | Radar, Parallel Coordinates |

---

## 📏 COMPARACIÓN

### 1. Gráfico de Barras (Horizontal)

**Cuándo usar:**
- Comparar **categorías**
- Cuando hay **muchas categorías** (>7)
- Cuando las **etiquetas son largas**

**Ejemplo de uso:**
- Satisfacción por área
- Número de beneficiarios por programa
- Top 10 donantes

```
Satisfacción por Área
Norte    ████████████ 8.5
Sur      ██████████ 7.8
Este     ███████████ 8.2
Oeste    ████ 6.1
```

**Ventajas:**
✅ Fácil comparar longitudes
✅ Etiquetas legibles
✅ Funciona con muchas categorías

**Desventajas:**
❌ No muestra tendencias temporales

**Tips:**
- **Ordena** las barras (descendente para ranking)
- Empieza el eje Y en **cero**
- Usa **color** para destacar

---

### 2. Gráfico de Columnas (Vertical)

**Cuándo usar:**
- Comparar **pocas categorías** (<7)
- Cuando las etiquetas son cortas
- Cuando el eje X es temporal (meses, años)

**Ejemplo:**
```
    │
  10│     █
   9│  █  █  █
   8│  █  █  █
     └──────────
      Q1 Q2 Q3
```

**Diferencia con Barras:**
- **Columnas:** Vertical → mejor para tiempo
- **Barras:** Horizontal → mejor para categorías

---

### 3. Gráfico de Barras Agrupadas

**Cuándo usar:**
- Comparar **múltiples métricas** por categoría
- Máximo 2-3 grupos

**Ejemplo de uso:**
- Satisfacción vs Calidad de Atención por Área
- Ingresos vs Gastos por Trimestre

```
      │ ■ Satisfacción
      │ ■ Calidad
   10 │
    8 │ ██ ██  ██ ██
    6 │ ██ ██  ██ ██
      └──────────────
       Norte   Sur
```

**Tips:**
- Máximo **3 categorías agrupadas**
- Leyenda clara
- Colores distintivos

---

### 4. Gráfico de Barras Apiladas (Stacked)

**Cuándo usar:**
- Mostrar **composición** (partes de un todo)
- Comparar **totales** entre categorías

**Ejemplo:**
```
100%│ [Insatisfecho]
 75%│ [Neutral]
 50%│ [Satisfecho]
 25%│ [Muy Satisfecho]
  0%└────────────────
     Norte    Sur
```

**Variantes:**
- **100% Stacked:** Para comparar proporciones
- **Stacked absoluto:** Para ver totales

**Tips:**
- Máximo **4-5 categorías apiladas**
- Colores secuenciales (claro→oscuro)

---

## 📈 TENDENCIAS TEMPORALES

### 5. Gráfico de Líneas

**Cuándo usar:**
- Mostrar **cambios en el tiempo**
- Comparar **múltiples series temporales**
- Datos **continuos**

**Ejemplo de uso:**
- Evolución de satisfacción mensual
- Tendencia de donaciones anuales
- Comparar 2023 vs 2024

```
10│         ╱─╲
  │      ╱─╯   ╲
 8│   ╱─╯       ╲─╮
  │╱─╯             ╲
 6└──────────────────
  E F M A M J J A S
```

**Ventajas:**
✅ Muestra tendencias claramente
✅ Permite comparar múltiples líneas
✅ Identifica patrones (estacionalidad)

**Tips:**
- Máximo **5 líneas** (más = confusión)
- Usa **líneas punteadas** para proyecciones
- Marca **eventos importantes** con anotaciones

---

### 6. Gráfico de Áreas

**Cuándo usar:**
- Mostrar **magnitud** además de tendencia
- Enfatizar **acumulación**
- Mostrar **partes de un total** en el tiempo

**Tipos:**

**A) Área Simple:**
```
10│         ╱█████╲
  │      ╱███████████╲
 5│   ╱█████████████████╮
  │╱████████████████████████
 0└──────────────────────────
```

**B) Área Apilada:**
```
  │ [Programa C]
  │ [Programa B]
  │ [Programa A]
 0└────────────────
```

**Tips:**
- **Área apilada:** Ordena series de mayor a menor
- Semi-transparencia para overlaps

---

### 7. Gráfico de Pendiente (Slope Chart)

**Cuándo usar:**
- Comparar **dos puntos en el tiempo**
- Mostrar **cambios individuales**

**Ejemplo:**
```
Antes    Después
 10│              ╱10
   │          ╱─╯
  8│      ╱─╯ 8
   │  ╱─╯
  6│─╯        6
```

**Ventajas:**
✅ Muestra cambio de cada entidad
✅ Identifica ganadores/perdedores

---

## 🔵 RELACIONES Y DISTRIBUCIONES

### 8. Scatter Plot (Dispersión)

**Cuándo usar:**
- Explorar **relación entre 2 variables numéricas**
- Identificar **correlaciones**
- Detectar **outliers**

**Ejemplo de uso:**
- Tiempo de espera vs Satisfacción
- Edad vs Ingresos

```
10│  •
  │    •  •
 8│  •  •   •
  │ •   •  •
 6│•
  └──────────
  10  20  30
  Tiempo (min)
```

**Mejoras:**
- **Tamaño de burbujas:** 3ª variable
- **Color:** 4ª variable (categoría)
- **Línea de tendencia:** Mostrar correlación

**Tips:**
- No uses con más de 500 puntos (se satura)
- Agrega línea de regresión si hay correlación
- Etiqueta outliers importantes

---

### 9. Histograma

**Cuándo usar:**
- Mostrar **distribución** de una variable continua
- Identificar **patrones** (normal, sesgada, bimodal)

**Ejemplo:**
```
Frecuencia
   │
 20│     ██
   │   ████
 10│ ████████
   │██████████
  0└──────────
    5  7  9
  Satisfacción
```

**Configuración clave:**
- **Bins (intervalos):** Típicamente 10-20
  - Pocos bins → pierde detalle
  - Muchos bins → ruido

**Tips:**
- Añade **línea de media** o **mediana**
- Compara con **curva normal** si aplica

---

### 10. Boxplot (Diagrama de Caja)

**Cuándo usar:**
- Comparar **distribuciones** entre grupos
- Identificar **outliers**
- Mostrar **dispersión** (IQR)

**Estructura:**
```
      Outlier →  •
                 ┬  ← Máximo (sin outliers)
    Q3 →        ┌┴┐
  Mediana →     ├─┤
    Q1 →        └┬┘
                 ┴  ← Mínimo
```

**Ventajas:**
✅ Muestra 5 estadísticos clave
✅ Compara múltiples grupos fácilmente
✅ Outliers visibles

**Ejemplo de uso:**
- Satisfacción por Área (4 boxplots)
- Tiempo de atención por Día de la Semana

---

### 11. Violin Plot

**Cuándo usar:**
- Mostrar **distribución completa** (como histograma)
- Comparar **múltiples grupos**
- Datos con **múltiples picos** (bimodal)

**Ventaja sobre Boxplot:**
- Muestra la **forma de la distribución**

```
     │ ╱╲     ╱╲
     │╱  ╲   ╱  ╲
     │    ╲ ╱
     │     ╳
     │    ╱ ╲
     └─────────
     Norte Sur
```

---

## 🥧 COMPOSICIÓN (Partes de un Todo)

### 12. Gráfico Circular (Pie Chart)

**Cuándo usar:**
- Mostrar **proporciones** de un total
- **Máximo 5-6 categorías**
- Cuando las proporciones son **muy diferentes**

**Ejemplo:**
```
    ╱────╲
   │ 40% │
   │     │
    ╲────╱
     30% 20% 10%
```

**Reglas de Oro:**
1. **Máximo 5 categorías** (preferiblemente 3-4)
2. **Ordena** de mayor a menor (empezando a las 12)
3. **Etiqueta directamente** (no solo colores)
4. Usa **"Otros"** para categorías pequeñas (<5%)

**Cuándo NO usar:**
❌ Muchas categorías (>6)
❌ Valores similares (difícil comparar ángulos)
❌ Cambios en el tiempo (usa líneas)

**Alternativas mejores:**
- Barras horizontales (más fácil comparar)
- Treemap (si hay jerarquía)

---

### 13. Donut Chart

**Cuándo usar:**
- Similar a Pie Chart
- **Centro disponible** para mostrar total o KPI

**Ejemplo:**
```
   ╱──────╲
  │        │
  │ Total  │
  │  500   │
   ╲──────╱
```

**Ventaja:**
✅ Centro útil para contexto adicional

---

### 14. Treemap

**Cuándo usar:**
- Mostrar **jerarquía** y **proporciones**
- Muchas categorías (>6)
- Espacio limitado

**Estructura:**
```
┌─────────────┬────────┐
│             │  20%   │
│    50%      ├────┬───┤
│             │15% │15%│
└─────────────┴────┴───┘
```

**Ejemplo de uso:**
- Distribución de presupuesto por programa
- Beneficiarios por región y comunidad

**Ventajas:**
✅ Eficiente en espacio
✅ Muestra jerarquías
✅ Puede manejar 20+ categorías

---

### 15. Waffle Chart (100 squares)

**Cuándo usar:**
- Mostrar **porcentajes** de forma intuitiva
- Audiencia general (fácil entender)

**Ejemplo:**
```
■■■■■■■■■■
■■■■■■■■■■
■■■■■■■■■■   ← 70 de 100 cuadros coloreados
■■■■■■■□□□      = 70%
□□□□□□□□□□
```

**Ventajas:**
✅ Muy intuitivo
✅ Funciona en infografías

---

## 🗺️ GEOLOCALIZACIÓN

### 16. Mapa Coroplético (Color por Región)

**Cuándo usar:**
- Mostrar **variación geográfica**
- Datos por país, estado, municipio

**Ejemplo:**
```
[Mapa de México]
- Estados en verde: Alta satisfacción
- Estados en rojo: Baja satisfacción
```

**Tips:**
- Usa **gradiente secuencial** (claro→oscuro)
- Incluye **leyenda clara**
- Evita rojo-verde (daltónicos)

---

### 17. Mapa de Burbujas

**Cuándo usar:**
- Mostrar **cantidad** en ubicaciones
- Tamaño de burbuja = magnitud

**Ejemplo de uso:**
- Número de beneficiarios por ciudad
- Donaciones por región

**Ventajas:**
✅ Muestra magnitud + ubicación
✅ Identifica clusters

---

## 📊 VALORES ÚNICOS (KPIs)

### 18. Scorecard / Métrica Destacada

**Cuándo usar:**
- Mostrar **1 valor clave**
- Dashboards ejecutivos

**Estructura:**
```
┌────────────────┐
│ Satisfacción   │
│     8.7        │ ← Grande y destacado
│  ▲ +0.5 vs Q2  │ ← Comparación
└────────────────┘
```

**Mejoras:**
- **Comparación:** vs meta, vs periodo anterior
- **Flecha:** ▲ mejora, ▼ declive
- **Color:** Verde = bueno, Rojo = malo

---

### 19. Gauge (Medidor)

**Cuándo usar:**
- Mostrar **progreso hacia meta**
- Visualizar **rangos** (bajo, medio, alto)

**Ejemplo:**
```
     ┌───┬───┬───┐
     │   │   │███│ ← 85/100
     └───┴───┴───┘
    Bajo  OK  Excelente
```

**Cuándo NO usar:**
❌ Comparar múltiples valores (usa barras)
❌ Mostrar tendencia (usa líneas)

---

## 🎨 GRÁFICOS ESPECIALIZADOS

### 20. Heatmap (Mapa de Calor)

**Cuándo usar:**
- Mostrar **patrones** en matriz de datos
- Variables **categóricas x categóricas**

**Ejemplo de uso:**
- Satisfacción por Día de Semana x Hora del Día
- Correlaciones entre variables

```
        Lun  Mar  Mié
Mañana  ██   ███  █
Tarde   ███  █    ██
```

**Color:**
- Gradiente: Bajo (claro) → Alto (oscuro)
- Divergente: Negativo (rojo) ← 0 → Positivo (azul)

---

### 21. Gráfico de Gantt

**Cuándo usar:**
- **Cronogramas** de proyectos
- Líneas de tiempo

**Ejemplo:**
```
Fase 1  ██████
Fase 2      ████████
Fase 3           ██████
        ───────────────
        E  F  M  A  M
```

---

### 22. Funnel (Embudo)

**Cuándo usar:**
- Mostrar **proceso con pérdidas** en cada etapa
- Conversión, retención

**Ejemplo de uso:**
- Proceso de selección de beneficiarios
- Funnel de donaciones

```
┌──────────────┐
│   Contacto   │ 1000
├──────────────┤
│  Evaluación  │ 500
├──────────────┤
│   Admitidos  │ 200
└──────────────┘
```

---

### 23. Waterfall (Cascada)

**Cuándo usar:**
- Mostrar **incrementos y decrementos** acumulativos
- Análisis de cambios (presupuesto, varianza)

**Ejemplo de uso:**
- Cómo llegamos del presupuesto inicial al final
- Cambios en número de beneficiarios

```
   │ ┌───┐
   │ │ 50│ +20
100├─┘   └─┐
   │       │ -30
 90│       └───┐
   │           └─ 90
```

---

## 🚫 Anti-Patterns: Gráficos a Evitar

### ❌ 1. Gráfico de Pie 3D
**Problema:** Distorsiona proporciones
**Alternativa:** Pie 2D o barras

### ❌ 2. Eje Y Truncado (en barras)
**Problema:** Exagera diferencias
**Solución:** Siempre empezar en cero para barras

### ❌ 3. Gráfico de Radar con 10+ variables
**Problema:** Ilegible
**Alternativa:** Barras horizontales ordenadas

### ❌ 4. Doble Eje Y con Escalas Engañosas
**Problema:** Crea correlaciones falsas
**Solución:** 2 gráficos separados o normalizar escalas

### ❌ 5. Rainbow Colors
**Problema:** No tiene orden perceptual
**Alternativa:** Gradiente secuencial (claro→oscuro)

---

## 🎯 Árbol de Decisión Rápido

```
¿Qué quieres comunicar?
│
├─ Comparar categorías
│  ├─ Pocas (<7) → Columnas
│  └─ Muchas (>7) → Barras horizontales
│
├─ Tendencia en el tiempo
│  ├─ Una serie → Líneas
│  └─ Múltiples series → Líneas (máx 5)
│
├─ Relación entre 2 variables
│  └─ Scatter + línea de tendencia
│
├─ Distribución
│  ├─ Una variable → Histograma
│  └─ Comparar grupos → Boxplot / Violin
│
├─ Composición
│  ├─ Pocas partes (<5) → Pie / Donut
│  └─ Muchas partes → Treemap / Barras
│
├─ Ubicación geográfica
│  └─ Mapa coroplético / Burbujas
│
└─ Un valor único
   └─ Scorecard / Gauge
```

---

## 📊 Tabla Resumen

| Gráfico | Mejor Para | Evitar Si | Alternativa |
|---------|------------|-----------|-------------|
| **Barras** | Comparar categorías | Tendencias temporales | Líneas |
| **Líneas** | Tendencias temporales | Categorías | Barras |
| **Scatter** | Relación 2 variables | Más de 500 puntos | Binning + Heatmap |
| **Pie** | Proporciones simples | >5 categorías | Barras |
| **Boxplot** | Comparar distribuciones | Audiencia no técnica | Barras con error bars |
| **Heatmap** | Patrones en matriz | Datos dispersos | Tabla |
| **Mapa** | Datos geográficos | Pocos puntos | Lista o tabla |

---

## ✅ Checklist de Calidad

Antes de publicar un gráfico, verifica:

**Claridad:**
- [ ] El mensaje se entiende en **5 segundos**
- [ ] Título **describe el insight**, no solo el tipo de gráfico
- [ ] Ejes tienen **etiquetas claras** con unidades
- [ ] Leyenda **fácil de entender** (o etiquetado directo)

**Precisión:**
- [ ] Eje Y empieza en **cero** (para barras)
- [ ] Escalas son **apropiadas** (no exageran)
- [ ] Datos son **correctos** y actuales
- [ ] Fuente de datos **citada**

**Diseño:**
- [ ] **Color** usado con propósito (no decoración)
- [ ] Texto **legible** (mínimo 12pt)
- [ ] No hay **chart junk** (elementos innecesarios)
- [ ] Funciona en **blanco y negro** (para impresión)

**Accesibilidad:**
- [ ] No solo rojo-verde (daltónicos)
- [ ] Alto **contraste**
- [ ] Patrones alternativos a color si es necesario

---

## 📚 Recursos para Profundizar

### Libros:
- **"The Visual Display of Quantitative Information"** - Edward Tufte
- **"Storytelling with Data"** - Cole Nussbaumer Knaflic
- **"The Truthful Art"** - Alberto Cairo

### Sitios Web:
- [DataVizProject.com](https://datavizproject.com/) - Catálogo de tipos de gráficos
- [From Data to Viz](https://www.data-to-viz.com/) - Árbol de decisión interactivo
- [The R Graph Gallery](https://r-graph-gallery.com/) - Ejemplos de código

### Herramientas:
- **Flourish:** Templates de visualizaciones
- **RAWGraphs:** Gráficos avanzados sin código
- **Chart Chooser:** Herramienta de decisión de Juice Analytics

---

**¡Elige el gráfico correcto y comunica con claridad!** 📊✨

