# Tutorial: BigQuery + Looker Studio para Dashboard Teletón

Este tutorial te guiará paso a paso para configurar BigQuery, cargar los datos de Teletón, configurar permisos para alumnos @tec.mx, y crear un dashboard en Looker Studio.

---

## 📋 Tabla de Contenidos

1. [Requisitos Previos](#requisitos-previos)
2. [Parte 1: Configuración de BigQuery](#parte-1-configuración-de-bigquery)
3. [Parte 2: Cargar Datos a BigQuery](#parte-2-cargar-datos-a-bigquery)
4. [Parte 3: Configurar Permisos IAM](#parte-3-configurar-permisos-iam)
5. [Parte 4: Conectar Looker Studio](#parte-4-conectar-looker-studio)
6. [Parte 5: Crear Dashboard en Looker Studio](#parte-5-crear-dashboard-en-looker-studio)
7. [Solución de Problemas](#solución-de-problemas)

---

## Requisitos Previos

### 1. Cuenta de Google Cloud Platform (GCP)

- **Profesor**: Necesitas una cuenta de GCP con permisos de administrador
- **Costo**: BigQuery ofrece 10 GB de almacenamiento y 1 TB de consultas gratis por mes
- **Registro**: [https://cloud.google.com/](https://cloud.google.com/)

### 2. Archivos Preparados

Asegúrate de haber ejecutado el **Notebook 3: Preparación Looker** que genera:

```
looker/bigquery_data/
├── dimensiones.csv
├── hechos.csv
├── agregaciones.csv
├── kpis_globales.csv
└── teleton_completo.csv
```

### 3. Herramientas Necesarias

- Navegador web (Chrome recomendado)
- Acceso a Google Cloud Console
- Acceso a Looker Studio ([https://lookerstudio.google.com/](https://lookerstudio.google.com/))

---

## Parte 1: Configuración de BigQuery

### Paso 1.1: Crear Proyecto en Google Cloud

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Haz clic en el selector de proyectos (arriba a la izquierda)
3. Clic en **"Nuevo Proyecto"**
4. Configura:
   - **Nombre del proyecto**: `dashboard-teleton-2024` (o el que prefieras)
   - **Organización**: Selecciona tu organización o déjalo en blanco
   - **Ubicación**: Deja el valor predeterminado
5. Haz clic en **"Crear"**

### Paso 1.2: Habilitar BigQuery API

1. En el menú de navegación (☰), ve a **"APIs y servicios" > "Biblioteca"**
2. Busca **"BigQuery API"**
3. Haz clic en **"BigQuery API"** y luego en **"Habilitar"**

### Paso 1.3: Crear Dataset en BigQuery

1. En el menú de navegación (☰), ve a **"BigQuery"**
2. En el panel de exploración (izquierda), haz clic en tu proyecto
3. Haz clic en los tres puntos (⋮) junto a tu proyecto y selecciona **"Crear conjunto de datos"**
4. Configura:
   - **ID del conjunto de datos**: `teleton_satisfaccion`
   - **Ubicación de los datos**: `US` (o la región más cercana)
   - **Caducidad predeterminada de las tablas**: Ninguna
   - **Cifrado**: Predeterminado
5. Haz clic en **"Crear conjunto de datos"**

---

## Parte 2: Cargar Datos a BigQuery

### Paso 2.1: Cargar Tabla "dimensiones"

1. Haz clic en el dataset `teleton_satisfaccion`
2. Haz clic en **"Crear tabla"** (botón + o menú de tres puntos)
3. Configura:
   - **Crear tabla desde**: Subir
   - **Seleccionar archivo**: Navega y selecciona `dimensiones.csv`
   - **Formato de archivo**: CSV
   - **Nombre de la tabla**: `dimensiones`
   - **Esquema**:
     - Selecciona **"Detección automática"** (BigQuery detectará los tipos)
     - O importa el esquema desde `bigquery_schemas.json` (sección "dimensiones")
   - **Opciones avanzadas**:
     - ✅ Número de filas de encabezado que se omitirán: `1`
     - ✅ Permitir campos con comillas
4. Haz clic en **"Crear tabla"**

### Paso 2.2: Cargar Tabla "hechos"

Repite el proceso del Paso 2.1 con los siguientes cambios:

- **Seleccionar archivo**: `hechos.csv`
- **Nombre de la tabla**: `hechos`
- **Esquema**: Detección automática o importar desde JSON (sección "hechos")

### Paso 2.3: Cargar Tabla "agregaciones"

- **Seleccionar archivo**: `agregaciones.csv`
- **Nombre de la tabla**: `agregaciones`
- **Esquema**: Detección automática o importar desde JSON (sección "agregaciones")

### Paso 2.4: Cargar Tabla "kpis_globales"

- **Seleccionar archivo**: `kpis_globales.csv`
- **Nombre de la tabla**: `kpis_globales`
- **Esquema**: Detección automática o importar desde JSON (sección "kpis_globales")

### Paso 2.5: Cargar Tabla "teleton_completo" (Opcional)

- **Seleccionar archivo**: `teleton_completo.csv`
- **Nombre de la tabla**: `teleton_completo`
- **Esquema**: Detección automática

Esta tabla contiene todos los datos en una sola tabla para consultas ad-hoc.

### Paso 2.6: Verificar Carga

1. En el panel de exploración, expande `teleton_satisfaccion`
2. Deberías ver 4-5 tablas: `dimensiones`, `hechos`, `agregaciones`, `kpis_globales` (y opcionalmente `teleton_completo`)
3. Haz clic en cada tabla y ve a la pestaña **"Esquema"** para verificar los campos
4. Ve a la pestaña **"Vista previa"** para ver algunos datos

---

## Parte 3: Configurar Permisos IAM

Esta sección configura el acceso para que **solo alumnos con correo @tec.mx** puedan ver el dataset.

### Paso 3.1: Acceder a Configuración de IAM del Dataset

1. En BigQuery, haz clic en el dataset `teleton_satisfaccion`
2. Haz clic en **"Compartir" > "Permisos"** (o botón "Compartir" en la parte superior)
3. Se abrirá el panel de permisos

### Paso 3.2: Agregar Acceso para Dominio @tec.mx

#### Opción A: Acceso para Todo el Dominio @tec.mx

1. Haz clic en **"Agregar entidad principal"**
2. En el campo **"Nuevas entidades principales"**, escribe:
   ```
   domain:tec.mx
   ```
3. En **"Selecciona un rol"**, busca y selecciona:
   ```
   BigQuery > Visualizador de datos de BigQuery
   ```
4. Haz clic en **"Guardar"**

#### Opción B: Acceso para Grupo Específico de Alumnos

Si tienes un Google Group con los alumnos (ej. `alumnos-cd2001b@tec.mx`):

1. Haz clic en **"Agregar entidad principal"**
2. En **"Nuevas entidades principales"**, escribe:
   ```
   group:alumnos-cd2001b@tec.mx
   ```
3. Selecciona el rol **"Visualizador de datos de BigQuery"**
4. Haz clic en **"Guardar"**

#### Opción C: Acceso Individual por Alumno

Para agregar alumnos individualmente:

1. Haz clic en **"Agregar entidad principal"**
2. Escribe el correo del alumno: `alumno@tec.mx`
3. Selecciona el rol **"Visualizador de datos de BigQuery"**
4. Haz clic en **"Guardar"**
5. Repite para cada alumno

### Paso 3.3: Verificar Permisos

1. En la sección de permisos, deberías ver:
   ```
   domain:tec.mx → Visualizador de datos de BigQuery
   ```
   (o los grupos/individuos que agregaste)

2. **Probar acceso** (opcional):
   - Pide a un alumno que intente acceder a BigQuery
   - Deben poder ver el dataset `teleton_satisfaccion` en el proyecto
   - NO deben poder editar ni eliminar datos

---

## Parte 4: Conectar Looker Studio

### Paso 4.1: Acceder a Looker Studio

1. Ve a [https://lookerstudio.google.com/](https://lookerstudio.google.com/)
2. Inicia sesión con tu cuenta de Google (la misma de GCP)

### Paso 4.2: Crear Nuevo Informe

1. Haz clic en **"Crear" > "Informe"** (o botón **"+ Crear"**)
2. Se te pedirá seleccionar una fuente de datos

### Paso 4.3: Conectar a BigQuery

1. En la lista de conectores, busca y selecciona **"BigQuery"**
2. Autoriza a Looker Studio para acceder a BigQuery (si es primera vez)
3. Navega en la estructura:
   - **Mi Proyecto** > Selecciona `dashboard-teleton-2024` (tu proyecto)
   - **Conjunto de datos** > Selecciona `teleton_satisfaccion`
   - **Tabla** > Selecciona `teleton_completo` (o la tabla que prefieras)
4. Haz clic en **"Agregar"**

### Paso 4.4: Agregar Más Fuentes de Datos (Opcional)

Si quieres usar múltiples tablas:

1. En el informe, haz clic en **"Recurso" > "Administrar fuentes de datos agregadas"**
2. Haz clic en **"Agregar fuente de datos"**
3. Repite el proceso para agregar `dimensiones`, `hechos`, `agregaciones`, y `kpis_globales`

---

## Parte 5: Crear Dashboard en Looker Studio

### Paso 5.1: Configurar Tema con Colores Teletón

1. En el menú superior, haz clic en **"Tema y diseño"**
2. En **"Tema"**, selecciona **"Personalizar"**
3. Configura los colores:
   - **Color primario**: `#4B1F76` (Morado Profundo)
   - **Color secundario**: `#F7C600` (Amarillo Teletón)
   - **Color de énfasis**: `#7E3AA7` (Morado Medio)

### Paso 5.2: Crear Sección de KPIs

#### KPI 1: Satisfacción General

1. Haz clic en **"Agregar un gráfico" > "Tarjeta de resultados"**
2. Arrastra para crear la tarjeta en el lienzo
3. En el panel derecho (Configuración):
   - **Métrica**: Selecciona `satisfaccion_general` y cambia agregación a **"Promedio"**
   - **Nombre del campo**: `Satisfacción General`
4. En la pestaña **"Estilo"**:
   - **Tamaño del número**: Grande (32-40)
   - **Color de fondo**: Blanco (`#FFFFFF`)
   - **Borde**: Sí, color `#F7C600`, grosor 3px

#### KPI 2-6: Repetir para otros KPIs

Crea tarjetas similares para:
- **NPS** (fórmula personalizada - ver abajo)
- **Índice Calidad Servicio** (promedio de `indice_calidad_servicio`)
- **Transparencia** (promedio de `transparencia`)
- **Calidad Percibida** (promedio de `calidad_percibida`)
- **Antigüedad Promedio** (promedio de `anos_benefactor`)

#### Fórmula para NPS en Looker

1. Haz clic en **"Agregar un campo"** (o botón **"+ Campo"**)
2. Crea un campo calculado llamado **"NPS Score"**:
   ```sql
   ((COUNT(CASE WHEN nps >= 9 THEN benefactor_id END) -
     COUNT(CASE WHEN nps <= 6 THEN benefactor_id END)) /
     COUNT(benefactor_id)) * 100
   ```
3. Usa este campo en una tarjeta de resultados
4. Formato: Número con 1 decimal

### Paso 5.3: Gráfico de Distribución NPS

1. Haz clic en **"Agregar un gráfico" > "Gráfico de barras"**
2. Configuración:
   - **Dimensión**: Crear campo calculado `NPS Categoría`:
     ```sql
     CASE
       WHEN nps >= 9 THEN 'Promotores (9-10)'
       WHEN nps >= 7 THEN 'Pasivos (7-8)'
       ELSE 'Detractores (0-6)'
     END
     ```
   - **Métrica**: `RECORD COUNT` (conteo de registros)
   - **Métrica opcional**: Agregar porcentaje
3. Estilo:
   - **Colores**:
     - Promotores: `#2ECC71` (Verde)
     - Pasivos: `#F7C600` (Amarillo)
     - Detractores: `#E74C3C` (Rojo)
   - **Orientación**: Horizontal

### Paso 5.4: Gráfico de Calidad de Servicio (13 Dimensiones)

1. **Preparar campo calculado** para las 13 dimensiones:
   - Haz clic en **"Agregar campo"**
   - Nombre: `Dimensión Calidad`
   - Este campo requiere UNION de las 13 columnas (ver nota abajo)

2. Alternativamente, crea un **gráfico de barras horizontal**:
   - **Dimensión**: Usa cada columna de calidad como fila (manual)
   - **Métrica**: Promedio de cada columna
   - **Ordenar**: Por valor descendente
   - **Color**: `#7E3AA7` (Morado Medio)
   - **Línea de referencia**: Añadir línea en el promedio general

> **Nota**: Looker Studio no permite UNPIVOT nativo. Para un gráfico dinámico, considera usar la tabla `hechos` y agregar las 13 filas manualmente, o usar SQL personalizado en BigQuery para crear una vista UNPIVOT.

### Paso 5.5: Mapa Geográfico

1. Haz clic en **"Agregar un gráfico" > "Mapa geográfico"**
2. Configuración:
   - **Dimensión**: `estado`
   - **Métrica**: `RECORD COUNT` (cantidad de benefactores)
   - **Métrica opcional**: `satisfaccion_general` (promedio)
3. Estilo:
   - **Color base**: `#1A2A6C` (Azul Teletón)
   - **Color de énfasis**: `#F7C600` (Amarillo)

### Paso 5.6: Tabla de Datos por Giro

1. Haz clic en **"Agregar un gráfico" > "Tabla"**
2. Configuración:
   - **Dimensión**: `giro`
   - **Métricas**:
     - Cantidad: `RECORD COUNT`
     - Satisfacción: `AVG(satisfaccion_general)`
     - NPS: `AVG(nps)`
     - Calidad: `AVG(indice_calidad_servicio)`
3. Estilo:
   - **Colores alternativos de filas**: Sí
   - **Barras de datos**: Activar para columnas numéricas
   - **Ordenar**: Por satisfacción descendente

### Paso 5.7: Filtros Interactivos

1. Haz clic en **"Agregar un control" > "Lista desplegable"**
2. Crea filtros para:
   - **Estado** (dimensión: `estado`)
   - **Giro** (dimensión: `giro`)
   - **Segmento Antigüedad** (dimensión: `segmento_antiguedad`)
3. Coloca los filtros en una barra superior del dashboard

### Paso 5.8: Gráfico de Línea - Tendencia por Antigüedad

1. Haz clic en **"Agregar un gráfico" > "Gráfico de líneas"**
2. Configuración:
   - **Dimensión**: `segmento_antiguedad`
   - **Métricas**:
     - `AVG(satisfaccion_general)`
     - `AVG(nps)`
     - `AVG(indice_calidad_servicio) * 2` (normalizado a escala 0-10)
3. Estilo:
   - **Colores de serie**:
     - Satisfacción: `#4B1F76` (Morado)
     - NPS: `#F7C600` (Amarillo)
     - Calidad: `#7E3AA7` (Morado Medio)
   - **Mostrar leyenda**: Sí

### Paso 5.9: Diseño Final

1. **Organiza los componentes** en secciones:
   ```
   ┌─────────────────────────────────────────────────┐
   │  HEADER: Título + Logo Teletón                  │
   ├─────────────────────────────────────────────────┤
   │  FILTROS: Estado | Giro | Antigüedad            │
   ├─────────────────────────────────────────────────┤
   │  KPIs: [6 tarjetas en 2 filas de 3]            │
   ├─────────────────────────────────────────────────┤
   │  NPS: [Gráfico distribución] + [Interpretación] │
   ├─────────────────────────────────────────────────┤
   │  CALIDAD: [Gráfico 13 dimensiones]              │
   ├─────────────────────────────────────────────────┤
   │  PERFIL: [Mapa] + [Tabla Giros]                │
   ├─────────────────────────────────────────────────┤
   │  TENDENCIA: [Gráfico líneas antigüedad]         │
   └─────────────────────────────────────────────────┘
   ```

2. **Agregar Logo Teletón**:
   - Haz clic en **"Insertar" > "Imagen"**
   - Sube el logo de Teletón (descárgalo de su sitio oficial)
   - Colócalo en el header

3. **Agregar Título**:
   - Haz clic en **"Insertar" > "Texto"**
   - Escribe: "Dashboard de Satisfacción - Fundación Teletón"
   - Formato: Tamaño 28-32, Color `#4B1F76`, Negrita

### Paso 5.10: Compartir Dashboard

#### Opción A: Compartir con Dominio @tec.mx

1. Haz clic en **"Compartir"** (arriba a la derecha)
2. En **"Agregar personas y grupos"**, escribe:
   ```
   tec.mx
   ```
3. Selecciona permisos: **"Puede ver"**
4. Haz clic en **"Listo"**

#### Opción B: Enlace para Cualquier Persona (No Recomendado)

1. Haz clic en **"Compartir"**
2. En **"Obtener vínculo"**, cambia a **"Cualquier persona con el vínculo"**
3. Permisos: **"Puede ver"**
4. Copia el enlace y compártelo

#### Opción C: Compartir con Grupo de Alumnos

1. Haz clic en **"Compartir"**
2. Agrega el grupo: `alumnos-cd2001b@tec.mx`
3. Permisos: **"Puede ver"**

---

## Solución de Problemas

### ❌ Error: "No se pudieron cargar los datos"

**Causa**: Problemas de permisos o esquema incorrecto.

**Solución**:
1. Verifica que el usuario tenga rol "Visualizador de datos de BigQuery"
2. Revisa que los tipos de datos en BigQuery coincidan con lo esperado
3. Ejecuta una consulta de prueba en BigQuery para verificar datos

### ❌ Error: "No se encuentra el dataset"

**Causa**: El dataset no está compartido o el usuario no tiene acceso.

**Solución**:
1. Ve a BigQuery > `teleton_satisfaccion` > Compartir > Permisos
2. Verifica que `domain:tec.mx` esté agregado
3. Asegúrate que el usuario esté usando su cuenta @tec.mx

### ❌ Gráfico muestra datos incorrectos

**Causa**: Agregación incorrecta o campo mal configurado.

**Solución**:
1. Verifica la **agregación** (promedio, suma, conteo)
2. Revisa los **filtros** aplicados al gráfico
3. Prueba con una tabla simple primero para ver los datos crudos

### ❌ Colores no coinciden con la paleta Teletón

**Solución**:
1. Ve a cada gráfico individualmente
2. En **"Estilo" > "Colores"**, selecciona **"Personalizar colores"**
3. Aplica los códigos hex de la paleta:
   - `#F7C600` (Amarillo)
   - `#4B1F76` (Morado Profundo)
   - `#7E3AA7` (Morado Medio)
   - `#2ECC71` (Verde)
   - `#E74C3C` (Rojo)

### ❌ No puedo agregar campo calculado

**Solución**:
1. Asegúrate de estar en modo **"Edición"** (no "Vista")
2. Ve a la fuente de datos (pestaña **"Datos"**)
3. Haz clic en **"Agregar un campo"** (botón con +)
4. Escribe la fórmula SQL usando la sintaxis de BigQuery

---

## 📚 Recursos Adicionales

### Documentación Oficial

- [BigQuery - Guía de Inicio](https://cloud.google.com/bigquery/docs/quickstarts)
- [Looker Studio - Tutoriales](https://support.google.com/looker-studio/answer/6283323)
- [BigQuery - Control de Acceso IAM](https://cloud.google.com/bigquery/docs/access-control)

### Fórmulas Útiles para Looker Studio

#### NPS Score
```sql
((COUNT(CASE WHEN nps >= 9 THEN benefactor_id END) -
  COUNT(CASE WHEN nps <= 6 THEN benefactor_id END)) /
  COUNT(benefactor_id)) * 100
```

#### Porcentaje de Promotores
```sql
(COUNT(CASE WHEN nps >= 9 THEN benefactor_id END) /
 COUNT(benefactor_id)) * 100
```

#### Satisfacción Normalizada (%)
```sql
(AVG(satisfaccion_general) / 10) * 100
```

#### Categoría de Satisfacción
```sql
CASE
  WHEN AVG(satisfaccion_general) >= 8 THEN 'Excelente'
  WHEN AVG(satisfaccion_general) >= 6 THEN 'Bueno'
  ELSE 'Mejorable'
END
```

### Paleta de Colores Teletón (Referencia Rápida)

| Color | Hex | Uso Recomendado |
|-------|-----|-----------------|
| Amarillo | `#F7C600` | Acentos, highlights, valores positivos |
| Morado Profundo | `#4B1F76` | Títulos, gráficos principales |
| Morado Medio | `#7E3AA7` | Gráficos secundarios |
| Verde | `#2ECC71` | Promotores, valores buenos |
| Amarillo | `#F7C600` | Pasivos, valores regulares |
| Rojo | `#E74C3C` | Detractores, valores malos |
| Blanco | `#FFFFFF` | Fondos, tarjetas |
| Gris Claro | `#F5F5F5` | Fondos secundarios |

---

## ✅ Checklist de Completitud

Usa esta lista para verificar que completaste todos los pasos:

- [ ] Proyecto de GCP creado
- [ ] BigQuery API habilitada
- [ ] Dataset `teleton_satisfaccion` creado
- [ ] Tabla `dimensiones` cargada
- [ ] Tabla `hechos` cargada
- [ ] Tabla `agregaciones` cargada
- [ ] Tabla `kpis_globales` cargada
- [ ] Permisos IAM configurados para @tec.mx
- [ ] Looker Studio conectado a BigQuery
- [ ] 6 KPIs creados con tarjetas
- [ ] Gráfico de distribución NPS creado
- [ ] Gráfico de calidad de servicio creado
- [ ] Mapa geográfico creado
- [ ] Tabla por giro creada
- [ ] Gráfico de tendencia por antigüedad creado
- [ ] Filtros interactivos agregados
- [ ] Colores Teletón aplicados
- [ ] Dashboard compartido con alumnos

---

**¡Felicidades! Has completado la configuración de BigQuery y Looker Studio para el Dashboard de Teletón.**

Si tienes dudas, consulta la [documentación oficial de Google Cloud](https://cloud.google.com/docs) o contacta al equipo de soporte.
