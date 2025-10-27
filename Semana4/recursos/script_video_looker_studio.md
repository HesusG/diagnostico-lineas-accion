# Script Completo: Video Tutorial de Looker Studio (15 minutos)

**Título del Video:** "Crea tu Primer Dashboard en Looker Studio para ONGs en 15 Minutos"

**Objetivo:** Construir un dashboard funcional desde cero mostrando KPIs de una ONG

**Requisitos previos:**
- Cuenta de Google
- Dataset: `datos_ong_ejemplo.csv` (incluido en el curso)

---

## [00:00-00:30] INTRO (30 segundos)

### 🎬 PANTALLA: Título del curso "CD2001B - Semana 4"

**TÚ DICES:**

"Hola, bienvenidos a este tutorial práctico de Looker Studio. En los próximos 15 minutos vamos a construir juntos un dashboard completo para una ONG ficticia, desde cero, sin necesidad de programar ni instalar nada.

Al final de este video, tendrás un dashboard interactivo que incluye:
- KPIs principales de satisfacción y atención
- Gráficos de tendencias temporales
- Comparativas por área y programa
- Y filtros interactivos

Todo esto usando Looker Studio, que es 100% gratuito.

Así que abre tu navegador y sígueme paso a paso. ¡Empecemos!"

---

## [00:30-02:00] PASO 1: PREPARAR LOS DATOS (1.5 minutos)

### 🎬 PANTALLA: Abrir Google Sheets

**TÚ DICES:**

"Lo primero que necesitamos es tener nuestros datos en un formato que Looker Studio pueda leer. La forma más fácil es usar Google Sheets.

Ya tengo preparado un archivo CSV con datos simulados de beneficiarios de una ONG. Este archivo contiene 100 registros con información como:
- Nombre y edad del beneficiario
- Área geográfica que atiende
- Programa al que pertenece
- Fecha de atención
- Satisfacción (escala del 1 al 10)
- Tiempo de atención en minutos

Voy a subir este archivo a Google Sheets."

### 🎬 ACCIÓN:
1. Abrir `drive.google.com`
2. Clic en **"Nuevo" > "Google Sheets" > "Hoja de cálculo en blanco"**
3. **"Archivo" > "Importar" > "Subir"**
4. Seleccionar `datos_ong_ejemplo.csv`
5. Configuración de importación:
   - Tipo de separador: "Detectar automáticamente"
   - Clic en **"Importar datos"**

**TÚ DICES:**

"Perfecto, aquí están nuestros datos. Puedes ver que tenemos 100 filas de beneficiarios con toda la información que necesitamos.

Un tip importante: asegúrate de que tus encabezados estén en la primera fila y que no haya filas vacías al inicio. Esto es crucial para que Looker Studio los reconozca correctamente.

Ahora vamos a renombrar esta hoja para tenerla organizada."

### 🎬 ACCIÓN:
- Clic en "Hoja de cálculo sin título" arriba
- Renombrar a: **"Datos ONG - Dashboard Diagnóstico"**

**TÚ DICES:**

"Listo. Ahora que tenemos nuestros datos en Google Sheets, podemos conectarlos a Looker Studio."

---

## [02:00-04:00] PASO 2: CREAR DASHBOARD EN LOOKER STUDIO (2 minutos)

### 🎬 PANTALLA: Abrir nueva pestaña

**TÚ DICES:**

"Vamos a abrir Looker Studio. Escribe en la barra de direcciones: lookerstudio.google.com"

### 🎬 ACCIÓN:
- Abrir `lookerstudio.google.com`
- Aparece la pantalla de inicio de Looker Studio

**TÚ DICES:**

"Esta es la pantalla de inicio de Looker Studio. Aquí puedes ver reportes que hayas creado antes, templates de ejemplo, y la galería de la comunidad.

Para crear nuestro dashboard desde cero, vamos a hacer clic en el botón azul que dice 'Crear' y luego seleccionar 'Informe'."

### 🎬 ACCIÓN:
- Clic en **"Crear"** (botón azul, esquina superior izquierda)
- Clic en **"Informe"**

**TÚ DICES:**

"Looker Studio ahora nos pregunta qué fuente de datos queremos usar. Como nuestros datos están en Google Sheets, vamos a buscar ese conector."

### 🎬 PANTALLA: Aparece el panel "Agregar datos al informe"

### 🎬 ACCIÓN:
- En el buscador, escribir **"Google Sheets"**
- Clic en **"Google Sheets"** (ícono verde de Sheets)

**TÚ DICES:**

"Ahora Looker Studio nos muestra todos los archivos de Google Sheets que tenemos en nuestro Drive. Vamos a seleccionar el archivo que acabamos de subir."

### 🎬 ACCIÓN:
- Buscar y hacer clic en **"Datos ONG - Dashboard Diagnóstico"**
- Seleccionar la **Hoja 1** (o como se llame)
- Clic en **"Agregar"** (botón azul abajo a la derecha)

**TÚ DICES:**

"Perfecto! Looker Studio ahora está conectado a nuestros datos. Vamos a confirmar que queremos agregar esta fuente de datos al informe."

### 🎬 ACCIÓN:
- Aparece popup "Agregar datos al informe"
- Clic en **"Agregar al informe"**

**TÚ DICES:**

"Excelente. Ya tenemos nuestro lienzo en blanco conectado a los datos. Fíjate que arriba a la derecha dice 'Informe sin título'. Vamos a ponerle un nombre descriptivo."

### 🎬 ACCIÓN:
- Clic en "Informe sin título" (arriba a la derecha)
- Renombrar a: **"Dashboard de Diagnóstico - [Nombre de ONG Ficticia]"**
- Enter

---

## [04:00-07:00] PASO 3: CREAR KPI CARDS (3 minutos)

**TÚ DICES:**

"Ahora viene la parte divertida: agregar visualizaciones. Vamos a seguir las mejores prácticas de diseño de dashboards que vimos en clase:

**Arriba:** Los KPIs más importantes
**Medio:** Gráficos de tendencias
**Abajo:** Tablas de detalle

Empecemos por los KPIs principales. En Looker Studio, los KPIs se llaman 'Scorecards'. Vamos a agregar uno."

### 🎬 ACCIÓN:
- Clic en **"Agregar un gráfico"** en el menú superior (ícono de gráfico de barras)
- Seleccionar **"Tarjeta de puntuación"** (Scorecard)

**TÚ DICES:**

"Ahora haz clic en el lienzo donde quieres que aparezca el KPI. Yo lo voy a poner en la parte superior izquierda."

### 🎬 ACCIÓN:
- Clic en la parte superior izquierda del lienzo
- Aparece una scorecard con un número

**TÚ DICES:**

"Perfecto! Por defecto, Looker Studio está contando el número de registros. Pero nosotros queremos mostrar la **satisfacción promedio**. Vamos a configurar esto en el panel de la derecha."

### 🎬 PANTALLA: Panel derecho "Configuración de datos"

**TÚ DICES:**

"En el panel de la derecha vemos dos secciones importantes:
- **Configuración**: Aquí elegimos qué mostrar
- **Estilo**: Aquí personalizamos cómo se ve

Vamos a cambiar la métrica que se muestra."

### 🎬 ACCIÓN:
- En el panel derecho, sección "Configuración"
- Buscar **"Métrica"**
- Hacer clic en "Record Count" (cuenta de registros)
- Aparece menú desplegable
- Hacer clic en **"satisfaccion"**
- Cambiar agregación de "Suma" a **"Promedio"** (AVG)

**TÚ DICES:**

"Genial! Ahora está mostrando el promedio de satisfacción. Pero el número tiene muchos decimales. Vamos a formatearlo para que muestre solo 1 decimal."

### 🎬 ACCIÓN:
- En el mismo panel, buscar **"Precisión decimal"** o hacer clic en el lápiz junto a la métrica
- Cambiar a **1 decimal**

**TÚ DICES:**

"Mucho mejor. Ahora vamos a agregar una etiqueta para que sea claro qué significa este número."

### 🎬 ACCIÓN:
- Hacer clic en **pestaña "Estilo"** (arriba en el panel derecho)
- Buscar **"Etiqueta de métrica"**
- Activar checkbox **"Mostrar"**
- En el campo de texto escribir: **"Satisfacción Promedio"**

**TÚ DICES:**

"Perfecto! Ya tenemos nuestro primer KPI. Ahora vamos a agregar dos más: el total de beneficiarios y el tiempo promedio de atención."

### 🎬 ACCIÓN (repetir para 2 KPIs más):

**KPI 2: Total de Beneficiarios**
1. Agregar nueva Scorecard (posición: centro superior)
2. Métrica: **"beneficiario_id"**
3. Agregación: **"Recuento de valores únicos"** (COUNT DISTINCT)
4. Etiqueta: "Total Beneficiarios"

**KPI 3: Tiempo Promedio de Atención**
1. Agregar nueva Scorecard (posición: derecha superior)
2. Métrica: **"tiempo_atencion_min"**
3. Agregación: **"Promedio"**
4. Precisión: **0 decimales**
5. Etiqueta: "Tiempo Prom. Atención (min)"

**TÚ DICES (mientras los creas):**

"Fíjense que para el total de beneficiarios uso 'Recuento de valores únicos' en lugar de 'Recuento'. Esto es importante porque si un beneficiario fue atendido 2 veces, solo lo cuento una vez.

Y para el tiempo de atención, uso promedio y sin decimales porque 25.7 minutos se entiende mejor como simplemente 26 minutos.

Ahora tenemos nuestros 3 KPIs principales en la parte superior. Vamos a darles un poco de formato para que se vean profesionales."

### 🎬 ACCIÓN (personalizar diseño):
- Seleccionar el primer scorecard
- En **"Estilo"**, cambiar:
  - Tamaño de fuente del número: **Grande** (40-50)
  - Color de fondo: **Azul claro** (o color institucional)
  - Alinear texto: **Centro**
- Copiar formato a los otros 2 scorecards (Ctrl+C en el primero, Ctrl+V en los otros)

**TÚ DICES:**

"Mucho mejor! Ya tenemos la parte más importante: los KPIs que resumen la salud de la ONG de un vistazo."

---

## [07:00-10:00] PASO 4: AGREGAR GRÁFICOS DE TENDENCIA Y COMPARACIÓN (3 minutos)

**TÚ DICES:**

"Ahora vamos a la sección media del dashboard: los gráficos que nos ayudan a entender **tendencias** y **comparaciones**.

Primero, un gráfico de línea que muestre cómo ha evolucionado la satisfacción mes a mes."

### 🎬 ACCIÓN:
- Clic en **"Agregar un gráfico"**
- Seleccionar **"Gráfico de serie temporal"** (línea con eje de tiempo)
- Hacer clic en el lienzo (posición: debajo de los KPIs, lado izquierdo)

**TÚ DICES:**

"Looker Studio automáticamente detecta que tenemos una columna de fecha y la usa para el eje X. Ahora solo necesitamos cambiar el eje Y para que muestre la satisfacción promedio."

### 🎬 ACCIÓN:
- En el panel derecho, **"Configuración"**
- **Dimensión de fecha:** Ya debe estar en "fecha" ✅
- **Intervalo de fecha:** Cambiar a **"Mes"** (para agrupar por mes)
- **Métrica:** Cambiar de "Record Count" a **"satisfaccion"** con agregación **"Promedio"**

**TÚ DICES:**

"Perfecto! Ahora vemos la tendencia mensual de satisfacción. Podemos ver que ha ido mejorando ligeramente con el tiempo.

Vamos a personalizar el título para que sea descriptivo."

### 🎬 ACCIÓN:
- Hacer doble clic en el título del gráfico (arriba del gráfico)
- Escribir: **"Tendencia de Satisfacción Mensual"**
- Enter

**TÚ DICES:**

"Ahora agreguemos un gráfico de barras para comparar la satisfacción entre las diferentes áreas geográficas que atiende la ONG."

### 🎬 ACCIÓN:
- Clic en **"Agregar un gráfico"**
- Seleccionar **"Gráfico de barras"**
- Hacer clic en el lienzo (posición: debajo de KPIs, lado derecho)

**TÚ DICES:**

"Configuremos este gráfico para que muestre las áreas en el eje Y y la satisfacción promedio en el eje X."

### 🎬 ACCIÓN:
- Panel derecho, **"Configuración"**
- **Dimensión:** Cambiar a **"area"**
- **Métrica:** Cambiar a **"satisfaccion"** con agregación **"Promedio"**
- **Ordenar:** Por "satisfaccion Promedio" **Descendente** (para que la mejor área esté arriba)

**TÚ DICES:**

"Excelente! Ahora podemos ver rápidamente qué área tiene mejor desempeño. Parece que el área Norte tiene la satisfacción más alta con 8.3, mientras que el área Oeste tiene la más baja.

Vamos a agregar un gráfico más: un gráfico de barras apiladas que nos muestre cuántos beneficiarios atiende cada programa."

### 🎬 ACCIÓN:
- Agregar **"Gráfico de columnas"** (barras verticales)
- Posición: Debajo de los anteriores
- **Dimensión:** "programa"
- **Métrica:** "beneficiario_id" con **"Recuento de valores únicos"**
- Título: **"Beneficiarios por Programa"**

---

## [10:00-12:00] PASO 5: AGREGAR FILTROS INTERACTIVOS (2 minutos)

**TÚ DICES:**

"Ahora viene una de las partes más poderosas de Looker Studio: los filtros interactivos. Vamos a agregar filtros que permitan a los usuarios del dashboard ver los datos segmentados por área o por programa.

Primero, un filtro de área."

### 🎬 ACCIÓN:
- Clic en **"Agregar un control"** en el menú superior (ícono de embudo)
- Seleccionar **"Lista desplegable"**
- Hacer clic en el lienzo (posición: arriba a la izquierda, antes de los KPIs)

**TÚ DICES:**

"Ahora configuramos qué campo queremos filtrar."

### 🎬 ACCIÓN:
- Panel derecho, **"Configuración"**
- **Dimensión del control:** Seleccionar **"area"**
- Activar checkbox **"Incluir 'Todos'"** (para poder ver todas las áreas o solo una)
- **Etiqueta:** "Filtrar por Área"

**TÚ DICES:**

"Perfecto! Ahora voy a probar el filtro. Mira cómo al seleccionar 'Norte', todos los gráficos se actualizan automáticamente para mostrar solo los datos del área Norte."

### 🎬 ACCIÓN:
- Hacer clic en el filtro desplegable
- Seleccionar **"Norte"**
- Mostrar cómo los KPIs y gráficos cambian
- Volver a seleccionar **"Todos"**

**TÚ DICES:**

"Impresionante, ¿verdad? Esto es lo que hace a Looker Studio tan potente: la interactividad sin necesidad de programar.

Agreguemos un segundo filtro para el programa."

### 🎬 ACCIÓN:
- Agregar otro **"Lista desplegable"**
- Posición: Al lado del primer filtro
- Dimensión: **"programa"**
- Incluir "Todos"
- Etiqueta: "Filtrar por Programa"

**TÚ DICES:**

"Ahora los usuarios pueden filtrar por área, por programa, o por ambos. Por ejemplo, si quieren ver solo la satisfacción del programa de Salud en el área Sur, pueden seleccionar ambos filtros."

### 🎬 ACCIÓN:
- Demostrar filtrando por "Sur" y "Salud"
- Mostrar cómo todo se actualiza
- Regresar a "Todos" en ambos

---

## [12:00-13:30] PASO 6: AGREGAR TABLA DE DETALLE (1.5 minutos)

**TÚ DICES:**

"Para completar nuestro dashboard, vamos a agregar una tabla en la parte inferior con los datos detallados. Esto permite que los usuarios puedan hacer 'drill-down' si necesitan ver registros específicos."

### 🎬 ACCIÓN:
- Clic en **"Agregar un gráfico"**
- Seleccionar **"Tabla"**
- Hacer clic en el lienzo (posición: parte inferior, ocupando todo el ancho)

**TÚ DICES:**

"Por defecto, la tabla muestra todas las columnas. Vamos a seleccionar solo las más importantes."

### 🎬 ACCIÓN:
- Panel derecho, **"Configuración"**
- **Dimensiones:** Seleccionar solo:
  - beneficiario_id
  - nombre
  - area
  - programa
  - fecha
  - satisfaccion
  - tiempo_atencion_min
- **Métrica:** Quitar (no necesitamos agregaciones en tabla de detalle)
- **Filas por página:** Cambiar a **10**

**TÚ DICES:**

"Perfecto! Ahora tenemos una tabla limpia que los usuarios pueden ordenar haciendo clic en los encabezados, y pueden navegar entre páginas si hay más de 10 registros.

Vamos a personalizar el título."

### 🎬 ACCIÓN:
- Doble clic en título de la tabla
- Escribir: **"Detalle de Atenciones"**

---

## [13:30-14:30] PASO 7: PERSONALIZACIÓN FINAL Y COMPARTIR (1 minuto)

**TÚ DICES:**

"Nuestro dashboard ya está funcional. Ahora vamos a darle algunos toques finales de diseño profesional.

Primero, vamos a agregar un título principal al dashboard."

### 🎬 ACCIÓN:
- Clic en **"Insertar" > "Texto"**
- Hacer clic en la parte superior central del lienzo
- Escribir: **"Dashboard de Diagnóstico - ONG [Nombre]"**
- Seleccionar el texto y cambiar formato:
  - Fuente: **Negrita**
  - Tamaño: **24-28**
  - Alinear: **Centro**

**TÚ DICES:**

"Ahora vamos a aplicar un tema de colores para que todo se vea cohesivo. Looker Studio tiene temas predefinidos que podemos usar."

### 🎬 ACCIÓN:
- Clic en **"Tema y diseño"** en el menú superior (ícono de paleta de colores)
- Seleccionar un tema profesional (ej: "Apollo" o "Orbita")
- Mostrar cómo todos los colores se actualizan automáticamente

**TÚ DICES:**

"Mucho mejor! Ya tenemos un dashboard completo y profesional. El último paso es compartirlo. Vamos a generar un link que podamos enviar a los directivos de la ONG."

### 🎬 ACCIÓN:
- Clic en **"Compartir"** (botón arriba a la derecha)
- Clic en **"Administrar el acceso"**
- Cambiar de "Restringido" a **"Cualquier persona con el enlace"**
- Permisos: **"Visualizador"** (para que solo puedan ver, no editar)
- Copiar el link

**TÚ DICES:**

"Y listo! Ahora puedes enviar este link a cualquier persona y podrá ver el dashboard interactivo, aplicar filtros, y explorar los datos, todo desde su navegador, sin necesidad de instalar nada."

---

## [14:30-15:00] CIERRE Y PRÓXIMOS PASOS (30 segundos)

**TÚ DICES:**

"Felicidades! En solo 15 minutos construimos un dashboard completo que incluye:
- 3 KPIs principales
- Gráficos de tendencias y comparaciones
- Filtros interactivos
- Tabla de detalle
- Y está listo para compartir

Este es exactamente el tipo de dashboard que necesitas para tu proyecto de diagnóstico de ONG en el reto final del curso.

**Próximos pasos recomendados:**
1. Practica recreando este dashboard con tus propios datos
2. Explora la galería de Looker Studio para inspirarte en diseños más avanzados
3. Revisa los notebooks de Python de la semana 4 para ver cómo preparar tus datos antes de subirlos

Si tienen preguntas, las vemos en clase. ¡Nos vemos en la siguiente sesión!"

### 🎬 PANTALLA: Fade out al dashboard final

---

## NOTAS DE PRODUCCIÓN

### Equipamiento recomendado:
- **Grabación de pantalla:** OBS Studio (gratuito) o Loom
- **Micrófono:** Cualquier headset con micrófono decente
- **Resolución:** 1920x1080 (Full HD)
- **Frame rate:** 30 FPS mínimo

### Edición:
- Agregar zoom en secciones críticas (cuando haces clic en menús pequeños)
- Agregar flechas/círculos para resaltar botones importantes
- Música de fondo suave (opcional, no invasiva)
- Subtítulos en español (muy recomendado para accesibilidad)

### Publicación:
- **YouTube:** Modo "No listado" (solo con link pueden ver)
- **Título:** "Looker Studio para ONGs - Tutorial Completo | CD2001B"
- **Descripción:** Incluir timestamps de cada sección
- **Tags:** looker studio, data studio, dashboard, visualización, ong, analítica

### Timestamps para descripción de YouTube:
```
0:00 - Intro
0:30 - Preparar datos en Google Sheets
2:00 - Crear dashboard en Looker Studio
4:00 - Agregar KPI cards
7:00 - Gráficos de tendencia y comparación
10:00 - Filtros interactivos
12:00 - Tabla de detalle
13:30 - Personalización y compartir
14:30 - Cierre y próximos pasos
```

---

## RECURSOS ADICIONALES PARA MENCIONAR

**En la descripción del video:**

- Link al dataset de ejemplo
- Link a la galería de Looker Studio
- Link al notebook de preparación de datos (Semana 4)
- Link a checklist de visualización
- Link a documentación oficial de Google

**Archivos de ejemplo para descargar:**
- `datos_ong_ejemplo.csv` - Dataset usado en el tutorial
- `checklist_looker_studio.pdf` - Checklist de buenas prácticas
- `plantilla_dashboard_ong.md` - Plantilla de estructura de dashboard
