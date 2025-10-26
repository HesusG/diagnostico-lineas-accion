# Guía: Looker Studio Básico

## 🎯 ¿Qué es Looker Studio?

**Looker Studio** (antes Google Data Studio) es una herramienta **gratuita** de Google para crear dashboards y reportes interactivos.

### Ventajas:
- ✅ **Gratis** y basado en la nube
- ✅ Conecta con múltiples fuentes de datos (Sheets, CSV, BigQuery, SQL)
- ✅ Dashboards **interactivos** con filtros
- ✅ Colaboración en tiempo real
- ✅ Se actualiza automáticamente cuando cambian los datos
- ✅ Fácil de compartir (como un Google Doc)

### ¿Para qué usarlo?
- Dashboards para directivos de ONGs
- Reportes de impacto para donantes
- Monitoreo de KPIs en tiempo real
- Visualización de resultados estadísticos

---

## 🚀 Primeros Pasos

### Paso 1: Acceder a Looker Studio

1. Ve a: **https://lookerstudio.google.com**
2. Inicia sesión con tu cuenta de Google
3. Haz clic en **"Crear"** → **"Informe"** (o Report)

---

### Paso 2: Conectar una Fuente de Datos

**Opciones de conectores:**

#### Opción A: Google Sheets (Más fácil)
1. En "Agregar datos a informe", selecciona **Google Sheets**
2. Selecciona la hoja de cálculo
3. Selecciona la pestaña específica
4. Haz clic en **"Agregar"**

#### Opción B: Subir archivo CSV
1. Selecciona **"Subir archivo"**
2. Arrastra tu CSV
3. Haz clic en **"Agregar"**

#### Opción C: BigQuery, MySQL, PostgreSQL (Avanzado)
1. Selecciona el conector correspondiente
2. Configura credenciales
3. Escribe query SQL (opcional)

---

### Paso 3: Tu Primer Visualización

Una vez conectados los datos:

1. **Añadir un gráfico:**
   - Haz clic en **"Añadir un gráfico"** en la barra superior
   - Selecciona tipo (tabla, barras, líneas, etc.)
   - Arrastra al lienzo

2. **Configurar el gráfico:**
   - Panel derecho: **"Configuración"**
   - **Dimensión:** Variable categórica (ej: área, género)
   - **Métrica:** Variable numérica (ej: satisfacción, cantidad)
   - **Orden:** Ascendente/Descendente

3. **Dar estilo:**
   - Panel derecho: **"Estilo"**
   - Cambiar colores, fuentes, leyendas

---

## 📊 Tipos de Visualizaciones

### 1. Scorecard (Tarjeta de Puntuación)

**Cuándo usar:**
- Mostrar un KPI principal
- Valor único destacado

**Configuración:**
- **Métrica:** Promedio de satisfacción, Total de beneficiarios, etc.
- **Métrica de comparación (opcional):** Meta, periodo anterior

**Ejemplo:**
```
┌─────────────────┐
│  Satisfacción   │
│      8.7        │
│   (meta: 8.5)   │
└─────────────────┘
```

---

### 2. Tabla

**Cuándo usar:**
- Mostrar datos detallados
- Comparar múltiples variables

**Configuración:**
- **Dimensiones:** Columnas categóricas
- **Métricas:** Valores numéricos
- **Orden:** Por cualquier columna

**Tip:** Activa "heatmap" para resaltar valores altos/bajos con color.

---

### 3. Gráfico de Barras

**Cuándo usar:**
- Comparar categorías
- Mostrar ranking

**Configuración:**
- **Dimensión:** Categoría (ej: Área)
- **Métrica:** Valor a comparar (ej: Promedio de satisfacción)
- **Orden:** Descendente para ranking

**Tipos:**
- **Barras verticales (columnas):** Pocas categorías (<7)
- **Barras horizontales:** Muchas categorías (>7)
- **Barras apiladas:** Mostrar composición

---

### 4. Gráfico de Líneas

**Cuándo usar:**
- Mostrar tendencias en el tiempo
- Evolución de KPIs

**Configuración:**
- **Dimensión:** Fecha (mes, semana, día)
- **Métrica:** Variable a seguir

**Tip:** Usa "líneas suavizadas" para tendencias más claras.

---

### 5. Gráfico Circular (Pie Chart)

**Cuándo usar:**
- Mostrar proporciones (partes de un todo)
- **Máximo 5-6 categorías**

**Configuración:**
- **Dimensión:** Categoría
- **Métrica:** Conteo o suma
- **Estilo:** Activar "etiquetas de datos" para mostrar %

⚠️ **Evita si:**
- Tienes más de 6 categorías
- Las diferencias son pequeñas (difícil comparar ángulos)

---

### 6. Mapa Geográfico

**Cuándo usar:**
- Datos tienen componente geográfico
- Mostrar distribución por región

**Configuración:**
- **Dimensión:** País, Estado, Ciudad (debe coincidir con nombres estándar)
- **Métrica:** Valor a mostrar
- **Estilo:** Mapa de burbujas o mapa de color

---

### 7. Tabla Dinámica (Pivot Table)

**Cuándo usar:**
- Análisis multidimensional
- Cruce de variables

**Configuración:**
- **Filas:** Dimensión 1
- **Columnas:** Dimensión 2
- **Métricas:** Valor a mostrar

---

## 🎨 Diseño de Dashboard Efectivo

### Principios de Diseño:

#### 1. Jerarquía Visual

```
┌─────────────────────────────────────┐
│  TÍTULO DEL DASHBOARD               │  ← Grande, arriba
├─────────────────────────────────────┤
│  [KPI 1]  [KPI 2]  [KPI 3]         │  ← Scorecards destacados
├─────────────────────────────────────┤
│                                      │
│  [Gráfico Principal]                │  ← Más grande
│                                      │
├──────────────┬──────────────────────┤
│ [Gráfico 2]  │  [Gráfico 3]        │  ← Secundarios
└──────────────┴──────────────────────┘
```

#### 2. Regla del 5-7

- **Máximo 5-7 visualizaciones** por página
- Si necesitas más, crea páginas adicionales

#### 3. Uso de Color

**Paleta para ONGs (sugerida):**
- **Azul:** Confianza, profesionalismo (#1E88E5)
- **Verde:** Éxito, crecimiento (#43A047)
- **Naranja:** Advertencia (#FB8C00)
- **Rojo:** Crítico, urgente (#E53935)
- **Gris:** Neutral, contexto (#757575)

**Reglas:**
- Usa colores consistentes (mismo color = mismo concepto)
- Máximo 3-4 colores principales
- Evita rojo-verde juntos (daltónicos)

#### 4. Espaciado y Alineación

- **Márgenes:** Al menos 20px de los bordes
- **Alinear** elementos (usa las guías automáticas)
- **Agrupar** visualizaciones relacionadas

---

## 🎛️ Filtros Interactivos

Los **filtros** permiten a los usuarios explorar los datos.

### Tipos de Filtros:

#### 1. Filtro de Lista Desplegable

**Cuándo usar:** Filtrar por categoría (ej: Área, Género)

**Cómo agregarlo:**
1. Clic en **"Añadir un control"** → **"Filtro de lista desplegable"**
2. Selecciona la dimensión (ej: "area")
3. Coloca en la parte superior del dashboard

#### 2. Filtro de Fecha

**Cuándo usar:** Seleccionar periodo de tiempo

**Tipos:**
- **Rango de fechas:** El usuario elige inicio y fin
- **Control deslizante:** Arrastra para cambiar periodo

#### 3. Filtro de Búsqueda

**Cuándo usar:** Muchas opciones (ej: lista de ciudades)

---

### Ejemplo de Configuración de Filtros:

```
┌──────────────────────────────────────┐
│ Dashboard de Satisfacción - ONG XYZ  │
├──────────────────────────────────────┤
│ Área: [Todas ▼]  Mes: [Enero 2024 ▼]│  ← Filtros arriba
├──────────────────────────────────────┤
│  [Visualizaciones que se actualizan] │
│  automáticamente al cambiar filtros  │
└──────────────────────────────────────┘
```

---

## 📈 Campos Calculados

Los **campos calculados** permiten crear nuevas métricas a partir de datos existentes.

### Ejemplos Comunes:

#### 1. Porcentaje de Satisfacción

```
CASE
  WHEN satisfaccion >= 8 THEN 'Satisfecho'
  WHEN satisfaccion >= 6 THEN 'Neutral'
  ELSE 'Insatisfecho'
END
```

#### 2. Promedio Ponderado

```
SUM(satisfaccion * peso) / SUM(peso)
```

#### 3. Diferencia con Meta

```
AVG(satisfaccion) - 8.5
```

#### 4. Categoría de Edad

```
CASE
  WHEN edad < 35 THEN 'Joven'
  WHEN edad <= 55 THEN 'Adulto'
  ELSE 'Mayor'
END
```

### Cómo crear un campo calculado:

1. Panel derecho: **"Fuente de datos"** → **"Editar"**
2. Haz clic en **"Añadir un campo"**
3. Escribe la fórmula
4. Asigna un nombre
5. Haz clic en **"Guardar"**

---

## 🔗 Compartir y Colaborar

### Opciones de Compartir:

#### 1. Compartir con Personas Específicas

1. Haz clic en **"Compartir"** (arriba derecha)
2. Añade correos electrónicos
3. Asigna permisos:
   - **Puede ver:** Solo lectura
   - **Puede editar:** Puede modificar el dashboard

#### 2. Compartir con Enlace Público

1. Haz clic en **"Compartir"** → **"Obtener enlace"**
2. Cambia a: **"Cualquier persona con el enlace puede ver"**
3. Copia el enlace

⚠️ **Cuidado:** Cualquiera con el enlace puede ver los datos.

#### 3. Incrustar en Página Web

1. Haz clic en **"Archivo"** → **"Incrustar informe"**
2. Copia el código HTML
3. Pégalo en tu sitio web

---

### Descargar/Exportar:

- **PDF:** Archivo → Descargar como PDF
- **Imagen:** Captura de pantalla (no nativo)

---

## 💡 Ejemplo Paso a Paso: Dashboard de Satisfacción

### Objetivo:
Crear un dashboard que muestre:
- Satisfacción promedio general
- Satisfacción por área
- Distribución de calificaciones
- Tendencia mensual

### Paso 1: Preparar Datos en Google Sheets

**Columnas necesarias:**
- id
- area
- mes
- satisfaccion

### Paso 2: Conectar a Looker Studio

1. Crear nuevo informe
2. Conectar Google Sheets
3. Seleccionar hoja

### Paso 3: Añadir Scorecard (Satisfacción Promedio)

1. Insertar → Scorecard
2. Métrica: **AVG(satisfaccion)**
3. Formato: 1 decimal
4. Tamaño grande, arriba

### Paso 4: Gráfico de Barras (Por Área)

1. Insertar → Gráfico de barras
2. Dimensión: **area**
3. Métrica: **AVG(satisfaccion)**
4. Orden: Descendente
5. Estilo: Color azul

### Paso 5: Gráfico Circular (Distribución)

1. Crear campo calculado "Categoría":
   ```
   CASE
     WHEN satisfaccion >= 9 THEN 'Excelente'
     WHEN satisfaccion >= 7 THEN 'Bueno'
     WHEN satisfaccion >= 5 THEN 'Regular'
     ELSE 'Malo'
   END
   ```
2. Insertar → Gráfico circular
3. Dimensión: **Categoría**
4. Métrica: **COUNT(id)**

### Paso 6: Gráfico de Líneas (Tendencia)

1. Insertar → Gráfico de líneas
2. Dimensión: **mes**
3. Métrica: **AVG(satisfaccion)**
4. Línea suavizada

### Paso 7: Añadir Filtros

1. Insertar → Control → Lista desplegable
2. Dimensión: **area**
3. Permitir "Todas las opciones"

### Paso 8: Diseño Final

1. Alinear elementos
2. Añadir título: "Dashboard de Satisfacción - ONG"
3. Ajustar colores al branding de la ONG
4. Añadir logo (Insertar → Imagen)

---

## 🎓 Mejores Prácticas

### ✅ DO (Hacer):

1. **Título claro:** "Dashboard de Satisfacción del Cliente - 2024"
2. **Fecha de actualización:** "Última actualización: 15/03/2024"
3. **Leyendas:** Explica qué significa cada métrica
4. **Colores consistentes:** Mismo color = mismo concepto
5. **Filtros visibles:** Usuario debe saber que puede filtrar
6. **Actualización automática:** Conecta directamente a la fuente
7. **Mobile-friendly:** Prueba en celular

### ❌ DON'T (Evitar):

1. **Demasiados gráficos:** Causa "parálisis por análisis"
2. **Gráficos 3D:** Distorsionan comparaciones
3. **Muchos colores:** Confunde, no ilumina
4. **Texto pequeño:** Ilegible en presentaciones
5. **Gráficos sin contexto:** Siempre incluye meta o comparación
6. **Datos desactualizados:** Mejor actualizar automático
7. **Filtros escondidos:** Usuario no los encontrará

---

## 🐛 Troubleshooting (Solución de Problemas)

### Problema: "El gráfico muestra datos incorrectos"

**Solución:**
- Verifica que la **agregación** sea correcta (AVG vs SUM)
- Revisa si hay **duplicados** en los datos fuente
- Comprueba **filtros** aplicados sin querer

### Problema: "El filtro no funciona en todos los gráficos"

**Solución:**
- Haz clic derecho en el filtro → **"Aplicar a todos los gráficos"**

### Problema: "Los datos no se actualizan"

**Solución:**
- Verifica que la fuente (Google Sheets) tenga permisos
- Refresca manualmente: **Ver → Actualizar datos**
- Configura actualización automática en la fuente de datos

---

## 📚 Recursos Adicionales

### Tutoriales Oficiales:
- [Looker Studio Learning Center](https://support.google.com/looker-studio/)
- [Galería de Templates](https://lookerstudio.google.com/gallery)

### Inspiración:
- Explora dashboards públicos en la galería
- Copia y adapta templates existentes

### Comunidad:
- [Looker Studio Community](https://www.en.advertisercommunity.com/t5/Looker-Studio/ct-p/looker-studio)
- YouTube: "Looker Studio tutorial"

---

## ✍️ Ejercicio Práctico

**Crea tu primer dashboard con estos pasos:**

1. **Prepara datos en Google Sheets** con:
   - 50-100 filas
   - Columnas: area, mes, satisfaccion, genero

2. **Conecta a Looker Studio**

3. **Crea 4 visualizaciones:**
   - Scorecard (satisfacción promedio)
   - Barras (por área)
   - Líneas (tendencia mensual)
   - Tabla (top 10 registros)

4. **Añade 1 filtro** (por área)

5. **Personaliza** colores y título

6. **Comparte** enlace público

---

**¡Estás listo para crear dashboards profesionales!** 📊

