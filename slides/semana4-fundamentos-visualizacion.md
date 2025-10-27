---
theme: default
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Fundamentos de Visualización de Datos
  Curso CD2001B - Diagnóstico para Líneas de Acción
  Tecnológico de Monterrey Campus Puebla
drawings:
  persist: false
transition: slide-left
title: Fundamentos de Visualización
mdc: true
download: true
exportFilename: semana4-fundamentos-visualizacion
css: unocss
---

<style src="./styles/tec-theme.css"></style>

# Fundamentos de Visualización de Datos

## Diseño Efectivo para Comunicar Insights

<div class="pt-12">
  <span class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    CD2001B - Semana 4 | Módulo 2
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <span class="text-sm opacity-50">Tec de Monterrey Campus Puebla</span>
</div>

---
layout: center
class: text-center
---

# ¿Por Qué Visualizar Datos?

<div class="grid grid-cols-2 gap-8 mt-12">
<div v-click>

### 📊 El Cerebro Procesa Imágenes 60,000x Más Rápido que Texto

**Tabla de datos:**
```
Año  Beneficiarios
2020  1,200
2021  1,450
2022  2,100
2023  2,850
```

¿Ves el patrón fácilmente? 🤔

</div>
<div v-click>

### 📈 Gráfico de Línea

[Imagina un gráfico de línea con tendencia ascendente pronunciada]

**Insight instantáneo:**
- Crecimiento acelerado (137% en 3 años)
- Punto de inflexión en 2022

**Resultado:** Decisiones más rápidas y acertadas

</div>
</div>

<div v-click class="mt-12 text-xl font-bold text-gradient">
"Una imagen vale más que mil números" - Visualización efectiva
</div>

---
layout: section
---

# Parte 1: Principios de Diseño Visual

## Los Fundamentos de una Buena Visualización

---

# Principio 1: Jerarquía Visual

<div class="grid grid-cols-2 gap-8">
<div>

## ¿Qué es?

**Jerarquía Visual:** Organizar elementos por orden de importancia para guiar la atención del lector

<div v-click class="mt-6">

### Técnicas

**1. Tamaño**
- Números grandes para KPIs principales
- Gráficos pequeños para datos secundarios

**2. Posición**
- Arriba-Izquierda = Más importante (patrón de lectura)
- Abajo-Derecha = Menos importante

**3. Color**
- Colores brillantes = Llaman atención
- Grises = Contexto de fondo

**4. Contraste**
- Negrita para destacar
- Fino para texto secundario

</div>

</div>
<div v-click>

## Ejemplo: Dashboard de ONG

### ❌ Sin Jerarquía

```
┌────────────────────────────────┐
│ Beneficiarios: 1,500           │ (tamaño normal)
│ Satisfacción: 8.2/10           │ (tamaño normal)
│ Costo/beneficiario: $250       │ (tamaño normal)
│ Voluntarios activos: 45        │ (tamaño normal)
└────────────────────────────────┘
```
Todo parece igual → ¿Qué es importante?

### ✅ Con Jerarquía

```
┌────────────────────────────────┐
│    SATISFACCIÓN                │
│       8.2/10                   │ (GRANDE, arriba)
│    Meta: 8.5 (falta 0.3)       │
├────────────────────────────────┤
│ Beneficiarios  │ Voluntarios  │ (pequeños, abajo)
│   1,500        │    45         │
└────────────────────────────────┘
```
Clara prioridad → Satisfacción es el KPI principal

</div>
</div>

---

# Principio 2: Menos es Más (Minimalismo)

<div class="grid grid-cols-2 gap-8">
<div>

## Concepto

**Ley de Simplicidad:** Elimina todo lo que no aporta información

<div v-click class="mt-6">

### Elementos a Eliminar

- ❌ Bordes innecesarios
- ❌ Fondos con textura/gradientes
- ❌ Efectos 3D (distorsionan datos)
- ❌ Líneas de cuadrícula excesivas
- ❌ Etiquetas redundantes
- ❌ Colores decorativos

</div>

<div v-click class="mt-6">

### Regla del Data-Ink Ratio

**Data-Ink Ratio =** (Tinta usada para datos) / (Tinta total)

**Objetivo:** Maximizar este ratio (≥ 0.7)

</div>

</div>
<div v-click>

## Ejemplo: Gráfico de Barras

### ❌ Sobrecargado

```
┌─────────────────────────────────┐
│ 📊 SATISFACCIÓN POR ÁREA 📊     │ (título redundante)
├─────────────────────────────────┤
│ (Fondo con gradiente azul)      │
│                                  │
│   🟦 Norte    ███████ 8.5       │ (3D, emojis, sombras)
│   🟩 Sur      ██████  7.8       │
│   🟨 Este     ████████ 9.1      │
│   🟥 Oeste    █████   7.2       │
│                                  │
│ Grid: ─ ─ ─ ─ ─ ─ ─ ─ ─ ─      │ (cuadrícula excesiva)
└─────────────────────────────────┘
```

### ✅ Minimalista

```
Satisfacción por Área (sobre 10)

Norte  ███████████████ 8.5
Sur    █████████████   7.8
Este   ████████████████9.1 ⭐
Oeste  ███████████     7.2

       0    2    4    6    8   10
```

</div>
</div>

---

# Principio 3: Color Intencional

<div class="grid grid-cols-2 gap-8">
<div>

## Tipos de Paletas

### 1. Secuencial
**Uso:** Mostrar progresión (baja → alta)

**Ejemplo:** Satisfacción de 1 a 10
- Claro (1) → Oscuro (10)
- Rojo claro → Rojo oscuro

### 2. Divergente
**Uso:** Dos extremos con punto medio

**Ejemplo:** Variación vs promedio
- Rojo (abajo del promedio) ← Blanco (promedio) → Verde (arriba)

### 3. Categórica
**Uso:** Distinguir categorías (sin orden)

**Ejemplo:** Programas de la ONG
- Alimentación (Azul), Salud (Verde), Educación (Naranja)

</div>
<div v-click>

## Mejores Prácticas

### ✅ Hacer

- Usar **2-5 colores** máximo
- Asignar significado consistente
  - Rojo = Problema/Urgente
  - Verde = Bueno/Meta alcanzada
  - Amarillo/Naranja = Advertencia
  - Azul/Gris = Neutral/Información
- Considerar **daltonismo** (8% población masculina)
- Usar herramientas: [ColorBrewer](https://colorbrewer2.org/)

### ❌ Evitar

- Colores al azar (sin significado)
- Depender solo del color (agregar texturas/patrones)
- Rojo-Verde exclusivamente (daltónicos no distinguen)
- Colores muy brillantes/saturados (cansa la vista)

</div>
</div>

<div v-click class="mt-8 p-6 bg-blue-500 bg-opacity-10 rounded text-center">

**Paleta Tec de Monterrey:**
🔵 Azul Reflex (#0062A4) | 🔷 Azul Oscuro (#003E7E) | 🟢 Verde (#8CC63F) | 🟠 Naranja (#FF6F31)

</div>

---

# Principio 4: Etiquetas Claras y Directas

<div class="grid grid-cols-2 gap-8">
<div>

## Componentes de Etiquetado

### 1. Título
- ✅ Descriptivo y específico
- ✅ Responde: "¿Qué muestra este gráfico?"

**Ejemplo:**
- ❌ "Datos 2023"
- ✅ "Satisfacción del Beneficiario por Trimestre (2023)"

### 2. Ejes
- ✅ Etiqueta del eje + Unidad
- ✅ Rango apropiado (no truncado)

**Ejemplo:**
- ❌ Eje Y sin etiqueta
- ✅ "Número de Beneficiarios (Miles)"

### 3. Leyenda
- ✅ Solo si es necesaria
- ✅ Cerca de los datos

</div>
<div v-click>

### 4. Anotaciones
- ✅ Resalta puntos clave
- ✅ Explica anomalías

**Ejemplo:**
```
Beneficiarios Atendidos (2020-2024)

  4,000│                      ●  (Enero 2024)
       │                    ╱
  3,000│                  ╱
       │                ╱     "Apertura de
  2,000│              ●       3 nuevos centros"
       │            ╱         ↑
  1,000│    ●─────●           (Mar 2022)
       │
       └─────────────────────────────────
        2020  2021  2022  2023  2024
```

### 5. Unidades
- ✅ Siempre especificar
- ✅ Consistentes en todo el dashboard

**Ejemplos:**
- Dinero: $1,250 MXN (no solo "$1,250")
- Porcentaje: 85% (no "0.85")
- Tiempo: 25 minutos (no "25 min" y luego "30 minutos")

</div>
</div>

---
layout: section
---

# Parte 2: Tipos de Gráficos

## Elegir el Gráfico Correcto para tus Datos

---

# El Catálogo de Gráficos

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Por Propósito

### 📊 Comparación
- Barras / Columnas
- Barras apiladas
- Bullet chart

### 📈 Tendencias
- Líneas
- Áreas
- Slope chart

### 📉 Distribución
- Histograma
- Box plot
- Violin plot

</div>
<div>

### 🔗 Relación
- Scatter plot
- Heatmap (matriz de correlación)
- Bubble chart

### 🥧 Composición/Proporción
- Pie chart (limitado)
- Donut chart
- Treemap

### 🌍 Geográfico
- Mapas de calor
- Mapas de coropletas
- Mapas de puntos

</div>
</div>

<div v-click class="mt-8 p-6 bg-purple-500 bg-opacity-10 rounded text-center">

**Regla de Oro:** El tipo de gráfico depende de tu **pregunta de negocio**, no de tus preferencias estéticas

</div>

---

# 1. Gráficos de Barras / Columnas

<div class="grid grid-cols-2 gap-8">
<div>

## Cuándo Usar

**Pregunta:** ¿Cómo se comparan las categorías?

**Casos de Uso:**
- Comparar satisfacción entre áreas
- Comparar número de beneficiarios por programa
- Rankings

<div v-click class="mt-6">

### Mejores Prácticas

✅ **Barras horizontales** cuando:
- Nombres de categorías son largos
- Comparación de 5+ categorías

✅ **Columnas verticales** cuando:
- Nombres cortos
- Enfatizar progresión temporal

✅ **Ordenar** por valor (descendente) para rankings

</div>

</div>
<div v-click>

## Ejemplo

### Beneficiarios por Programa (2023)

```
Alimentación      ████████████████████ 2,500
Salud             ███████████████ 1,800
Educación         ████████████ 1,200
Vivienda          ███████ 800
Empleo            ████ 450

                  0    500  1,000  2,000  3,000
```

### Variantes

**Barras Apiladas:** Mostrar sub-categorías
```
              │ Mujeres │ Hombres │
Alimentación  │████████│████     │
Salud         │██████  │████     │
```

**Barras Agrupadas:** Comparar 2 grupos lado a lado
```
              2022  2023
Alimentación  ███   ████████
Salud         ██    ██████
```

</div>
</div>

---

# 2. Gráficos de Líneas

<div class="grid grid-cols-2 gap-8">
<div>

## Cuándo Usar

**Pregunta:** ¿Cómo cambia esto con el tiempo?

**Casos de Uso:**
- Tendencias temporales (mensual, anual)
- Comparar múltiples series temporales
- Identificar estacionalidad

<div v-click class="mt-6">

### Mejores Prácticas

✅ Eje X siempre es **tiempo** (izquierda → derecha)

✅ Máximo **4-5 líneas** (más = confuso)

✅ Línea más importante en **color más oscuro**

✅ Etiqueta **directa** en la línea (no solo leyenda)

✅ Resalta **puntos clave** (máximos, mínimos, cambios)

</div>

</div>
<div v-click>

## Ejemplo

### Satisfacción Mensual (2023)

```
10 │                        ●────● (Meta: 8.5)
   │                    ●─╱
 9 │                ●─╱
   │            ●─╱
 8 │        ●─╱         📍 Mejora sostenida
   │    ●─╱              desde Abril
 7 │●─╱
   └─────────────────────────────────
    E F M A M J J A S O N D (2023)
```

### Con Múltiples Líneas

```
10 │
   │      ●════●════●  Norte (mejor desempeño)
 9 │    ╱
   │  ●────●────●     Centro
 8 │╱
   │●─────●─────●     Sur (estable pero bajo)
 7 │
   └─────────────────────────────────
    Trim1  Trim2  Trim3
```

</div>
</div>

---

# 3. Pie Charts (Gráficos Circulares)

<div class="grid grid-cols-2 gap-8">
<div>

## Cuándo Usar (con PRECAUCIÓN)

**Pregunta:** ¿Qué porcentaje representa cada categoría del total?

**Casos de Uso LIMITADOS:**
- Máximo **3-5 categorías**
- Cuando una categoría es dominante (>50%)

<div v-click class="mt-6">

### ⚠️ Problemas

❌ Difícil comparar rebanadas similares

❌ No funciona con muchas categorías

❌ 3D hace impossible interpretación

❌ Exploded pie charts son decorativos, no informativos

</div>

<div v-click class="mt-6">

### ✅ Alternativa Mejor: Barras

Para mostrar proporciones, **barras horizontales apiladas al 100%** son más claras

</div>

</div>
<div v-click>

## Ejemplo

### ❌ Pie Chart Malo

```
     Programa A: 28%
   ╱─────────────╲
  │  A  │   B    │  Programa B: 24%
  │     │        │  Programa C: 22%
  │  D  │   C    │  Programa D: 26%
   ╲─────────────╱
```
¿Cuál es más grande, B o D? 🤔 Difícil de ver.

### ✅ Barras Apiladas Mejor

```
│ A (28%) │ B (24%) │ C (22%) │ D (26%) │
├──────────┼─────────┼─────────┼─────────┤
0%        28%       52%       74%       100%
```
Comparación clara e instantánea.

### ✅ Uso Válido de Pie: Dominancia

```
   ╱────────╲
  │         │
  │    A    │  Programa A: 85%
  │  85%    │  Otros: 15%
  │    │15% │
   ╲────────╱
```
Cuando quieres mostrar que algo domina (>80%)

</div>
</div>

---

# 4. Histogramas y Box Plots

<div class="grid grid-cols-2 gap-8">
<div>

## Histograma

**Pregunta:** ¿Cómo se distribuyen los datos?

**Casos de Uso:**
- Distribución de edades de beneficiarios
- Distribución de tiempos de atención
- Identificar normalidad, asimetría, outliers

### Ejemplo: Tiempos de Atención

```
Frecuencia
 50│     ████
   │   ████████
 30│ ██████████
   │████████████
 10│████████████████
   └──────────────────────
    0  10  20  30  40  50
      Minutos de Atención

Insight: Mayoría 10-20 min,
         Pero hay casos de 40+ min
```

</div>
<div v-click>

## Box Plot

**Pregunta:** ¿Dónde está el centro y cuánta variación hay?

**Componentes:**
- Caja: 50% central de datos (Q1 a Q3)
- Línea central: Mediana
- Bigotes: Rango (excluyendo outliers)
- Puntos: Outliers

### Ejemplo: Satisfacción por Área

```
10│
  │       ●  (outlier: caso excepcional)
 9│    ┌──┐
  │    │  │
 8│────┤  ├────  Mediana: 8.2
  │    │  │
 7│    └──┘
  │       ●  (outlier bajo)
 6│
  └────────────
      Norte
```

**Ventaja:** Compara múltiples grupos fácilmente

</div>
</div>

---

# 5. Scatter Plots (Diagramas de Dispersión)

<div class="grid grid-cols-2 gap-8">
<div>

## Cuándo Usar

**Pregunta:** ¿Existe relación entre dos variables numéricas?

**Casos de Uso:**
- Correlación: Tiempo de servicio vs Satisfacción
- Segmentación: Impacto vs Esfuerzo (matriz)
- Outliers: Identificar casos atípicos

<div v-click class="mt-6">

### Mejores Prácticas

✅ Agregar **línea de tendencia** para visualizar correlación

✅ Usar **color** para tercera dimensión (categoría)

✅ Etiquetar **puntos importantes**

✅ Agregar **líneas de referencia** (ej: promedio)

</div>

</div>
<div v-click>

## Ejemplo: Tiempo vs Satisfacción

```
Satisfacción
10│
  │ ●
 9│   ●  ●
  │       ●    Correlación
 8│  ●       ●  negativa
  │      ●   ╲  (más tiempo →
 7│ ●        ●╲ menor satisfacción)
  │           ●╲
 6│              ●
  └─────────────────────────
   0  10  20  30  40  50  60
      Tiempo de Atención (min)
```

### Con Categorías (Color)

```
10│ ● Norte (alta satisfacción, bajo tiempo)
  │
 8│     ○ Sur (variado)
  │
 6│         ● Este (problemático)
  └─────────────────────────
   0      20     40      60
```

</div>
</div>

---

# 6. Heatmaps (Mapas de Calor)

<div class="grid grid-cols-2 gap-8">
<div>

## Cuándo Usar

**Pregunta:** ¿Cómo se comparan muchas combinaciones de dos variables?

**Casos de Uso:**
- Matriz de correlación entre variables
- Satisfacción por mes × área
- Volumen de atención por día × hora

<div v-click class="mt-6">

### Mejores Prácticas

✅ Usar escala de color **secuencial** o **divergente**

✅ Incluir **escala de colores** (leyenda)

✅ Alinear categorías de forma lógica

✅ Resaltar **valores extremos** con anotaciones

</div>

</div>
<div v-click>

## Ejemplo: Satisfacción por Área × Mes

```
        Ene  Feb  Mar  Abr  May  Jun
Norte   8.5  8.7  8.9  9.0  8.8  8.6
        ███  ███  ████ ████ ███  ███

Sur     7.2  7.5  7.8  7.9  8.1  8.3
        ███  ███  ███  ███  ███  ███

Este    6.8  7.0  7.2  7.4  7.6  7.9
        ██   ██   ███  ███  ███  ███

Oeste   8.0  8.1  7.9  8.2  8.4  8.6
        ███  ███  ███  ███  ███  ███

Escala: █ (6.5-7.5) ██ (7.5-8.0) ███ (8.0-8.5) ████ (8.5-9.0)

Insight: Norte mejora consistentemente
         Este inicia bajo pero crece
```

</div>
</div>

---

# Matriz de Decisión: Tipo de Gráfico

<div class="text-xs">

| Pregunta de Negocio | Tipo de Datos | Gráfico Recomendado | Alternativas |
|---------------------|---------------|---------------------|--------------|
| ¿Cómo se comparan A, B, C? | Categórica → Numérica | **Barras** | Columnas, Tabla |
| ¿Cómo cambia con el tiempo? | Temporal → Numérica | **Líneas** | Áreas, Columnas |
| ¿Qué % representa cada categoría? | Categórica (≤5) → % | **Barra apilada 100%** | Pie (solo si <4 categorías) |
| ¿Cómo se distribuyen los datos? | Numérica continua | **Histograma** | Box plot, Violín |
| ¿Existe correlación entre X e Y? | Numérica × Numérica | **Scatter plot** | Líneas, Heatmap |
| ¿Cuál es el rango y mediana? | Numérica por grupos | **Box plot** | Violin plot |
| ¿Cómo se comparan muchas combinaciones? | Categórica × Categórica → Numérica | **Heatmap** | Tabla pivote |
| ¿Dónde están geográficamente? | Coordenadas/Regiones | **Mapa de puntos/calor** | Tabla por región |
| ¿Cuánto progresé hacia la meta? | Métrica única + Meta | **Bullet chart / KPI card** | Gauge (velocímetro) |

</div>

<div v-click class="mt-8 p-6 bg-yellow-500 bg-opacity-10 rounded text-center">

**Regla:** Prueba 2-3 tipos de gráficos y elige el que comunica el insight **más rápido y claramente**

</div>

---
layout: section
---

# Parte 3: Anti-Patterns (Errores Comunes)

## Qué NO Hacer en Visualización

---

# Anti-Pattern 1: Gráficos 3D

<div class="grid grid-cols-2 gap-8">
<div>

## El Problema

**3D distorsiona la percepción de valores**

### Ejemplo: Barras 3D

```
      Valor aparente   Valor real
A:    Parece 45%       Realmente 35%
B:    Parece 30%       Realmente 40%
C:    Parece 25%       Realmente 25%
```

<div v-click class="mt-6">

### ¿Por Qué la Gente Usa 3D?

- Parece "más profesional" ❌
- Software lo ofrece por defecto ❌
- Llena espacio vacío ❌

### La Realidad

- **Nunca** agrega información útil
- **Siempre** dificulta lectura
- Es **decorativo**, no informativo

</div>

</div>
<div v-click>

## Solución: Siempre 2D

### ❌ Pie Chart 3D

```
   Perspectiva distorsiona
   ╱─────────────────╲
  │   A   │    B     │  A parece más grande
  │       │          │  por estar al frente
  │   D   │    C     │
   ╲─────────────────╱
```

### ✅ Barras 2D

```
A  ████████ 35%
B  ██████████ 40%
C  █████ 25%
```
Comparación precisa y clara.

<div v-click class="mt-6 p-4 bg-red-500 bg-opacity-10 rounded text-sm">

**Regla Absoluta:** NUNCA uses 3D. Punto.

</div>

</div>
</div>

---

# Anti-Pattern 2: Ejes Y Truncados/Manipulados

<div class="grid grid-cols-2 gap-8">
<div>

## El Problema

**Ejes que no inician en 0 exageran diferencias**

### ❌ Eje Truncado

```
Satisfacción
8.5│                    ●
   │                ●
8.0│            ●
   │        ●
7.5│    ●
   └────────────────────────
    Ene Feb Mar Abr May

Parece ENORME mejora (50%)
```

<div v-click class="mt-6">

### ✅ Eje Completo

```
10│
 8│    ●────●────●────●────●
 6│
 4│
 2│
 0│
  └────────────────────────
   Ene Feb Mar Abr May

Mejora real: 6% (de 8.0 a 8.5)
```

</div>

</div>
<div v-click>

## Excepciones Válidas

### Cuando SÍ puedes truncar:

**1. Datos con rango estrecho**
- Temperatura (15°C - 25°C)
- Tipos de cambio (19.80 - 20.20)

**2. Cambios porcentuales pequeños pero importantes**
- Tasas de interés (7.25% - 7.75%)

### Regla de Oro:

✅ **SI truncas, SIEMPRE indícalo claramente**

```
Temperatura (°C)
25│      ●        ⚠️ Eje no inicia en 0
   │   ●    ●
20│ ●          ●
   │
15│ [Eje truncado]
   └──────────────────────
```

<div v-click class="mt-4 p-4 bg-yellow-500 bg-opacity-10 rounded text-sm">

**Advertencia:** Políticos y marketers usan ejes truncados para **manipular**. No seas uno de ellos.

</div>

</div>
</div>

---

# Anti-Pattern 3: Demasiados Colores

<div class="grid grid-cols-2 gap-8">
<div>

## El Problema

**Paletas arcoíris sin significado confunden**

### ❌ Sobrecarga de Color

```
Satisfacción por Programa

Alimentación  🟥 8.5
Salud         🟦 8.2
Educación     🟩 7.9
Vivienda      🟨 8.1
Empleo        🟪 7.5
Legal         🟧 8.3
Psicológico   🟫 8.7
```

**Problema:**
- ¿Qué significa cada color?
- Difícil recordar 7 colores
- No hay jerarquía visual

</div>
<div v-click>

## Solución: Color con Propósito

### ✅ Enfoque con Color

```
Satisfacción por Programa

Psicológico   ████████████ 8.7 🟢 (arriba meta)
Alimentación  ██████████ 8.5 🟢
Legal         ██████████ 8.3 🟢
Salud         █████████ 8.2 🟡 (cerca)
Vivienda      █████████ 8.1 🟡
Educación     ████████ 7.9 🟡
Empleo        ███████ 7.5 🔴 (abajo meta)

Meta: ≥ 8.5
```

**Beneficios:**
- 3 colores con significado (🟢🟡🔴)
- Prioridad clara (rojos primero)
- Fácil de interpretar

### Regla: Máximo 5 Colores Distintos

</div>
</div>

---

# Anti-Pattern 4: Pie Charts con Muchas Categorías

<div class="grid grid-cols-2 gap-8">
<div>

## El Problema

**Más de 5 rebanadas = ilegible**

### ❌ Pie con 10 Categorías

```
     ╱──────────────╲
    │1│2│3│4│5│6│7 │
    │  │  │  │  │  │
    │10│9│8│  │  │  │
     ╲──────────────╱

Categorías:
1. Alimentación (15%)
2. Salud (12%)
3. Educación (11%)
4. Vivienda (10%)
5. Empleo (9%)
6. Legal (8%)
7. Psicológico (7%)
8. Deportes (6%)
9. Cultura (5%)
10. Otros (17%)
```

**Imposible** comparar rebanadas pequeñas

</div>
<div v-click>

## Soluciones

### ✅ Opción 1: Barras Ordenadas

```
Alimentación    ███████████████ 15%
Otros           █████████████████ 17%
Salud           ████████████ 12%
Educación       ███████████ 11%
Vivienda        ██████████ 10%
Empleo          █████████ 9%
Legal           ████████ 8%
Psicológico     ███████ 7%
Deportes        ██████ 6%
Cultura         █████ 5%
```

### ✅ Opción 2: Agrupar Categorías Pequeñas

```
     ╱──────────────╲
    │  Otros  │ 43%  │  (Suma de < 10%)
    │  (7 cat)│      │
    │  Alim   │      │  Alimentación: 15%
    │  15%    │      │  Salud: 12%
    │    Salud│      │  Educación: 11%
     ╲─12%  11%────╱   Vivienda: 10%
```

</div>
</div>

---

# Anti-Pattern 5: Doble Eje Y

<div class="grid grid-cols-2 gap-8">
<div>

## El Problema

**Dos escalas en un gráfico confunden**

### ❌ Doble Eje Y

```
Beneficiarios (izq)  Satisfacción (der)
3,000│                      │10
     │        ●             │
2,000│    ●     ●           │8
     │●             ●       │
1,000│                  ●   │6
     │                      │
     └──────────────────────┘
      E F M A M J J (2023)

 ─── Beneficiarios (eje izq)
 ─── Satisfacción (eje der)
```

**Problemas:**
- Fácil manipular escala para "forzar" correlación
- Difícil comparar

</div>
<div v-click>

## Soluciones

### ✅ Opción 1: Dos Gráficos Separados

```
Beneficiarios (personas)
3,000│        ●
     │    ●     ●
2,000│●             ●
1,000│                  ●
     └──────────────────────
      E F M A M J J

Satisfacción (escala 1-10)
10│
 8│  ●─────●────●
 6│●            ●───●
  └──────────────────────
   E F M A M J J
```

### ✅ Opción 2: Normalizar Escalas

Convertir ambas a % de cambio vs baseline

<div v-click class="mt-6 p-4 bg-red-500 bg-opacity-10 rounded text-sm">

**Excepción:** Solo usa doble eje si variables están **directamente relacionadas** (ej: ventas en pesos y en dólares)

</div>

</div>
</div>

---

# Checklist Anti-Patterns

<div class="grid grid-cols-2 gap-6 text-sm">
<div>

## Evita Siempre

- [ ] ❌ Gráficos 3D
- [ ] ❌ Pie charts con >5 categorías
- [ ] ❌ Ejes Y truncados sin advertencia
- [ ] ❌ Más de 5 colores sin significado
- [ ] ❌ Doble eje Y (salvo excepciones)
- [ ] ❌ Efectos especiales (sombras, gradientes, texturas)
- [ ] ❌ Usar color como única forma de distinguir
- [ ] ❌ Gráficos decorativos sin datos
- [ ] ❌ Comic Sans u otras fuentes no profesionales
- [ ] ❌ Animar gráficos sin razón (distrae)

</div>
<div v-click>

## Prioriza Siempre

- [ ] ✅ Simplicidad (menos es más)
- [ ] ✅ Etiquetas claras en ejes y título
- [ ] ✅ Color con propósito (semáforo: 🔴🟡🟢)
- [ ] ✅ Tipo de gráfico alineado a pregunta de negocio
- [ ] ✅ Jerarquía visual (lo importante grande/arriba)
- [ ] ✅ Fuente de datos y fecha en el gráfico
- [ ] ✅ Probar con alguien más (¿entiende sin explicación?)
- [ ] ✅ Accesibilidad (legible para daltónicos)
- [ ] ✅ Espacio en blanco (no saturar)
- [ ] ✅ Consistencia en formato (mismo estilo en todo dashboard)

</div>
</div>

---
layout: center
class: text-center
---

# Resumen: Fundamentos de Visualización

<div class="grid grid-cols-3 gap-6 mt-12 text-sm">

<div v-click>

### 🎨 Principios de Diseño
- Jerarquía visual
- Minimalismo
- Color intencional
- Etiquetas claras

</div>

<div v-click>

### 📊 Tipos de Gráficos
- Barras (comparar)
- Líneas (tendencias)
- Scatter (relación)
- Heatmap (múltiples variables)

</div>

<div v-click>

### ❌ Anti-Patterns
- NO 3D
- NO ejes manipulados
- NO demasiados colores
- NO pie con >5 categorías

</div>

</div>

<div v-click class="mt-16 text-2xl font-bold text-gradient">
El mejor gráfico es el que comunica el insight en <3 segundos
</div>

---
layout: end
class: text-center
---

# ¡Gracias!

## Próxima Clase: Looker Studio - Tutorial Completo

<div class="mt-8 opacity-75">
CD2001B - Semana 4<br>
Tec de Monterrey Campus Puebla
</div>
