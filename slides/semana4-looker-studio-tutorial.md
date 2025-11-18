---
theme: default
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Looker Studio: Tutorial Práctico con Fundación Teletón
  Curso CD2001B - Diagnóstico para Líneas de Acción
  Tecnológico de Monterrey Campus Puebla
drawings:
  persist: false
transition: slide-left
title: Tutorial Looker Studio
mdc: true
download: true
exportFilename: semana4-looker-studio-tutorial
css: unocss
---

<style src="./styles/tec-theme.css"></style>

# Looker Studio: Tutorial Práctico

## Creando un Dashboard para Fundación Teletón

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

# ¿Qué Vamos a Construir?

<div class="grid grid-cols-2 gap-8 mt-12">
<div v-click>

### 📊 Dashboard Ejecutivo de Teletón

**Objetivo:** Visualizar la satisfacción de **274 empresas benefactoras** para identificar oportunidades de mejora

</div>
<div v-click>

### 🎯 Componentes del Dashboard

- **4 KPI Cards** (métricas principales)
- **Gráfico de tendencia** por canal de apoyo
- **Comparación** por giro empresarial
- **Distribución** de satisfacción
- **Filtros interactivos** (giro, canal, región)

</div>
</div>

<div v-click class="mt-12 text-xl font-bold text-gradient">
Al final de esta clase tendrás tu primer dashboard profesional en Looker Studio
</div>

---
layout: section
---

# Parte 1: Preparación de Datos

## Del CSV a Google Sheets

---

# Datos de Fundación Teletón

<div class="grid grid-cols-2 gap-8">
<div>

## Dataset: Satisfacción de Empresas Benefactoras

**Archivo:** `teleton_benefactores.csv`

**Columnas principales:**
```python
- benefactor_id       # ID único
- empresa             # Nombre empresa
- giro                # Industria
- canal_apoyo         # Tipo de apoyo
- region              # Geográfica
- tiempo_colaboracion # Años
- satisfaccion        # 1-10
- recomendaria        # Sí/No
- comentarios         # Texto libre
```

**Total:** 274 registros

</div>
<div v-click>

## Paso 1: Revisar Calidad de Datos en Python

```python
import pandas as pd

# Cargar datos
df = pd.read_csv('Semana4/datos/teleton_benefactores.csv')

# Revisar
print(df.info())
print(df['satisfaccion'].describe())

# Verificar valores faltantes
print(df.isnull().sum())

# Distribución por giro
print(df['giro'].value_counts())
```

### Checklist
- ✅ Sin valores nulos en columnas clave
- ✅ Satisfacción en rango 1-10
- ✅ Categorías consistentes
- ✅ Fechas en formato correcto

</div>
</div>

---

# Paso 2: Exportar a Google Sheets

<div class="grid grid-cols-2 gap-8">
<div>

## Opción A: Manual (Más Fácil)

**Pasos:**
1. Guardar CSV desde Python
   ```python
   df.to_csv('teleton_dashboard.csv', index=False)
   ```

2. Ir a Google Sheets: [sheets.google.com](https://sheets.google.com)

3. **Archivo → Importar → Subir → teleton_dashboard.csv**

4. Configurar:
   - Tipo separador: Coma
   - Convertir texto a números: Sí

5. **Renombrar hoja:** "Dashboard Teletón - Datos"

</div>
<div v-click>

## Opción B: Automática con API

```python
import gspread
from google.oauth2.service_account import Credentials

# 1. Configurar credenciales
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file(
    'credentials.json',
    scopes=scope
)
client = gspread.authorize(creds)

# 2. Crear Google Sheet
sheet = client.create('Dashboard Teletón - Datos')
worksheet = sheet.get_worksheet(0)

# 3. Subir datos
data = [df.columns.values.tolist()] + df.values.tolist()
worksheet.update(data)

# 4. Compartir
sheet.share('tu-email@tec.mx', perm_type='user', role='writer')

print(f"✅ Datos subidos: {sheet.url}")
```

**Ventaja:** Actualización automática

</div>
</div>

---

# Paso 3: Agregar Columnas Calculadas en Sheets

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## ¿Por Qué en Sheets y No en Python?

**Looker Studio funciona mejor con cálculos en la fuente**

### Columnas a Agregar

#### 1. Categoría de Satisfacción
```excel
=IF(H2>=9, "😀 Muy Satisfecho",
   IF(H2>=7, "🙂 Satisfecho",
      IF(H2>=5, "😐 Neutral", "😞 Insatisfecho")))
```

#### 2. Meta Alcanzada
```excel
=IF(H2>=8, "✅ Meta Alcanzada", "❌ Bajo Meta")
```

#### 3. Grupo de Tiempo (años colaborando)
```excel
=IF(F2<2, "Nuevo (<2 años)",
   IF(F2<5, "Mediano (2-5 años)", "Fiel (>5 años)"))
```

</div>
<div v-click>

#### 4. Costo por Punto de Satisfacción
```excel
=J2/H2
```
*(Donde J2 = monto_aportado)*

### Vista Final en Sheets

| benefactor_id | empresa | giro | satisfaccion | **categoria_sat** | **meta_alcanzada** |
|---------------|---------|------|--------------|-------------------|-------------------|
| 1 | Empresa A | Retail | 9.2 | 😀 Muy Satisfecho | ✅ Meta Alcanzada |
| 2 | Empresa B | Tech | 7.5 | 🙂 Satisfecho | ❌ Bajo Meta |
| 3 | Empresa C | Finanzas | 6.8 | 🙂 Satisfecho | ❌ Bajo Meta |

<div v-click class="mt-6 p-4 bg-green-500 bg-opacity-10 rounded">

**Tip:** Aplica la fórmula a toda la columna arrastrando desde la celda inicial

</div>

</div>
</div>

---
layout: section
---

# Parte 2: Conectar Looker Studio

## Primeros Pasos con la Herramienta

---

# Paso 4: Crear Nuevo Reporte en Looker Studio

<div class="grid grid-cols-2 gap-8">
<div>

## Acceso

1. Ir a: [lookerstudio.google.com](https://lookerstudio.google.com)
2. Iniciar sesión con cuenta Google
3. **Crear → Informe**

<div v-click class="mt-6">

## Conectar Google Sheets

**Pantalla: "Agregar datos a informe"**

1. Buscar conector: **Google Sheets**
2. Seleccionar tu hoja: "Dashboard Teletón - Datos"
3. Seleccionar pestaña (worksheet): Sheet1
4. Clic **Agregar**
5. Clic **Agregar al informe**

</div>

</div>
<div v-click>

## Verificar Conexión

**Panel derecho → Datos**

Deberías ver:
```
📊 Fuente de datos: Dashboard Teletón - Datos

Dimensiones (texto/categorías):
- benefactor_id
- empresa
- giro
- canal_apoyo
- region
- categoria_sat     ✅ Nueva
- meta_alcanzada    ✅ Nueva

Métricas (números):
- satisfaccion (Tipo: Número, Agregación: Promedio)
- tiempo_colaboracion
- Record Count (automático)
```

<div v-click class="mt-6 p-4 bg-yellow-500 bg-opacity-10 rounded text-sm">

**Problema común:** Si satisfaccion aparece como dimensión (texto), haz clic → Cambiar tipo → Número

</div>

</div>
</div>

---

# Paso 5: Interfaz de Looker Studio

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Barra Superior

```
[Archivo] [Editar] [Ver] [Insertar] [Tema] [Compartir]
```

**Principales:**
- **Insertar:** Agregar gráficos/filtros
- **Tema:** Cambiar colores
- **Compartir:** Dar acceso

## Panel Izquierdo (Toolbox)

**Insertar componentes:**

📊 **Gráficos**
- Tablas
- Scorecards (KPI cards)
- Series temporales
- Barras/Columnas
- Circulares
- Mapas geográficos

🎛️ **Controles**
- Filtro de lista desplegable
- Control de intervalo de fechas
- Casillas de verificación

</div>
<div v-click>

## Panel Derecho (Propiedades)

**Cambia según qué selecciones:**

### Cuando seleccionas un Gráfico:
**Pestaña DATOS:**
- Fuente de datos
- Dimensión (eje X / categoría)
- Métrica (eje Y / valor)
- Ordenar por
- Filtro

**Pestaña ESTILO:**
- Colores
- Fuente
- Leyenda
- Ejes
- Bordes

### Canvas Central

**Tu dashboard:**
- Arrastra componentes aquí
- Redimensiona con esquinas
- Mueve arrastrando
- Elimina con tecla Delete

</div>
</div>

---
layout: section
---

# Parte 3: Construyendo el Dashboard

## Paso a Paso: De Blanco a Profesional

---

# Paso 6: Crear Sección de KPIs (Scorecards)

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## KPI 1: Satisfacción Promedio

**Insertar → Scorecard**

**Panel Derecho → DATOS:**
- Fuente: Dashboard Teletón - Datos
- Métrica: AVG(satisfaccion)
- **Nombre métrico:** "Satisfacción Promedio"

**Panel Derecho → ESTILO:**
- Métrico:
  - Tamaño: 48
  - Color: #00A3E0 (Azul Teletón)
  - Formato: 0.0 (un decimal)
- Etiqueta métrica:
  - "Satisfacción General (sobre 10)"
  - Tamaño: 14
- Fondo: Blanco

**Posición:** Arriba-izquierda

</div>
<div v-click>

## KPI 2: Total Empresas Benefactoras

**Insertar → Scorecard**

**DATOS:**
- Métrica: Record Count
- **Nombre:** "Total Empresas"

**ESTILO:**
- Métrico:
  - Tamaño: 48
  - Color: #E30074 (Rosa Teletón)
  - Formato: 0 (sin decimales)
- Etiqueta: "Empresas Benefactoras"

**Posición:** Arriba, al lado del KPI 1

<div v-click class="mt-6">

## KPI 3: % Meta Alcanzada

**DATOS:**
- Métrica personalizada:
  ```
  COUNT(CASE WHEN meta_alcanzada = "✅ Meta Alcanzada"
        THEN benefactor_id END) / Record Count * 100
  ```
- Nombre: "% Meta"

**ESTILO:**
- Color: #8DC63F (Verde Teletón)
- Formato: 0% (porcentaje sin decimales)

</div>

</div>
</div>

---

# Crear Métrica Calculada: % Meta Alcanzada

<div class="grid grid-cols-2 gap-8">
<div>

## Método Simplificado

**En el panel de DATOS del Scorecard:**

1. Clic en **Agregar métrica**
2. Clic en **Crear campo**
3. **Nombre:** `Porcentaje Meta Alcanzada`
4. **Fórmula:**
   ```sql
   CASE
     WHEN meta_alcanzada = "✅ Meta Alcanzada"
     THEN 1
     ELSE 0
   END
   ```
5. **Guardar**
6. Cambiar agregación a **Promedio**
7. En ESTILO → Formato métrico: **Porcentaje**

**Resultado:** Muestra automáticamente 62% (ejemplo)

</div>
<div v-click>

## KPI 4: Promedio Años Colaborando

**Insertar → Scorecard**

**DATOS:**
- Métrica: AVG(tiempo_colaboracion)
- Nombre: "Años Promedio"

**ESTILO:**
- Color: #FFB612 (Amarillo Teletón)
- Formato: 0.0 años
- Sufijo personalizado: " años"

**Layout Final de KPIs:**

```
┌────────────────────────────────────────────┐
│  KPI 1        KPI 2        KPI 3      KPI 4│
│  8.2/10       274          62%       4.5    │
│  Satisfacción Empresas     Meta      Años   │
│  Promedio     Benefactoras Alcanzada Prom.  │
└────────────────────────────────────────────┘
```

<div v-click class="mt-4 p-4 bg-blue-500 bg-opacity-10 rounded">

**Tip:** Usa **Tema → Aplicar paleta Teletón** para colores consistentes

</div>

</div>
</div>

---

# Paso 7: Gráfico de Barras - Satisfacción por Giro

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Insertar Gráfico

**Insertar → Gráfico de barras**

**Panel DATOS:**
- Fuente: Dashboard Teletón - Datos
- **Dimensión:** giro
- **Métrica:** AVG(satisfaccion)
- **Ordenar:** Por métrica, Descendente
- **Métrica secundaria (opcional):** Record Count

**Resultado:**
```
Salud             ████████████ 8.9 (35)
Educación         ███████████  8.4 (42)
Retail            ██████████   8.0 (68)
Tecnología        █████████    7.8 (51)
Manufactura       ████████     7.5 (45)
Servicios         ███████      7.1 (33)
```

</div>
<div v-click>

## Panel ESTILO

### Barras
- **Color de serie:**
  - Opción 1: Un solo color (#00A3E0)
  - Opción 2: **Formato condicional**:
    ```
    Verde  (≥8.5): #8DC63F
    Amarillo (7-8.5): #FFB612
    Rojo (<7): #E30074
    ```

### Etiquetas de datos
- ✅ Mostrar etiquetas de datos
- Formato: 0.0

### Ejes
- Título eje Y: "Satisfacción Promedio (sobre 10)"
- Título eje X: "Giro Empresarial"
- Rango eje Y: 0 - 10 (para contexto)

### Leyenda
- Posición: Inferior
- Alineación: Centro

<div v-click class="mt-4 p-4 bg-green-500 bg-opacity-10 rounded">

**Insight:** Empresas del sector Salud muestran mayor satisfacción (8.9), mientras que Servicios requiere atención (7.1)

</div>

</div>
</div>

---

# Formato Condicional en Looker Studio

<div class="grid grid-cols-2 gap-8">
<div>

## Paso a Paso

**En panel ESTILO → Color de serie:**

1. Clic en **Formato condicional**
2. **Agregar regla de formato:**

**Regla 1: Meta Superada**
- Condición: AVG(satisfaccion) ≥ 8.5
- Color: #8DC63F (Verde Teletón)

**Regla 2: En Rango**
- Condición: AVG(satisfaccion) ≥ 7 Y < 8.5
- Color: #FFB612 (Amarillo Teletón)

**Regla 3: Bajo Meta**
- Condición: AVG(satisfaccion) < 7
- Color: #E30074 (Rosa Teletón)

3. **Guardar**

</div>
<div v-click>

## Resultado Visual

<img src="./assets/visualizations/bar-conditional-formatting-teleton.svg" class="w-full max-h-96 object-contain" />

**Ventaja:** Identificación inmediata de segmentos problemáticos

### Aplicar a Otros Gráficos

El formato condicional se puede usar en:
- ✅ Barras
- ✅ Tablas (celdas coloreadas)
- ✅ Scorecards (cambiar color según umbral)
- ✅ Mapas de calor

</div>
</div>

---

# Paso 8: Gráfico de Líneas - Tendencia por Canal

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Insertar Serie Temporal

**Insertar → Gráfico de serie temporal**

**Panel DATOS:**
- **Dimensión de intervalo de fechas:** fecha_registro
  - *Si no tienes fechas, usa una dimensión ordinal como "mes_inicio"*
- **Dimensión de desglose:** canal_apoyo
- **Métrica:** AVG(satisfaccion)

**Resultado (ejemplo con meses):**

```
10│                 ●───────● Donación
  │           ●───●           (línea verde)
 8│     ●───●               Patrocinio
  │   ●                       (línea azul)
 6│                         Voluntariado
  │                           (línea naranja)
  └────────────────────────────
   Ene  Feb  Mar  Abr  May  Jun
```

</div>
<div v-click>

## Panel ESTILO

### Serie
- **Tipo de línea:** Suave
- **Grosor:** 3px
- **Colores por canal:**
  - Donación: #00A3E0
  - Patrocinio: #8DC63F
  - Voluntariado: #FFB612
  - Otro: #E30074

### Puntos de datos
- ✅ Mostrar puntos
- Tamaño: 5

### Ejes
- Título eje Y: "Satisfacción (1-10)"
- Rango: 0 - 10
- Cuadrícula: Líneas principales

### Leyenda
- Posición: Derecha
- ✅ Mostrar título: "Canal de Apoyo"

<div v-click class="mt-4 p-4 bg-yellow-500 bg-opacity-10 rounded">

**Insight:** Canal "Donación" mantiene satisfacción consistentemente alta (8.5+). "Voluntariado" muestra crecimiento (+15% Feb-Jun).

</div>

</div>
</div>

---

# Paso 9: Tabla de Datos - Detalles por Empresa

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Insertar Tabla

**Insertar → Tabla**

**Panel DATOS:**
- **Dimensiones:**
  1. empresa
  2. giro
  3. canal_apoyo
  4. categoria_sat

- **Métricas:**
  1. AVG(satisfaccion) → Alias: "Satisfacción"
  2. tiempo_colaboracion → Alias: "Años"
  3. recomendaria → Alias: "Recomienda"

- **Ordenar por:** Satisfacción (Descendente)
- **Filas por página:** 10

</div>
<div v-click>

## Panel ESTILO

### Encabezado de tabla
- Fondo: #00A3E0 (Azul Teletón)
- Texto: Blanco
- Fuente: Roboto Bold, 12px

### Filas
- Alternar colores de fila: ✅
  - Color 1: Blanco
  - Color 2: #F5F5F5 (Gris claro)

### Formato de celdas
- Satisfacción: 0.0, con **formato condicional**:
  - ≥9: Verde
  - 7-9: Amarillo
  - <7: Rojo

### Paginación
- ✅ Mostrar paginación
- Posición: Inferior

<div v-click class="mt-4 p-4 bg-blue-500 bg-opacity-10 rounded">

**Uso:** Permite drill-down a nivel empresa para identificar casos específicos de baja satisfacción

</div>

</div>
</div>

---

# Paso 10: Mapa de Calor (Heatmap)

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Crear Tabla Pivot como Heatmap

**Insertar → Tabla dinámica**

**Panel DATOS:**
- **Dimensión de fila:** giro
- **Dimensión de columna:** canal_apoyo
- **Métrica:** AVG(satisfaccion)

**Configuración:**
- Mostrar totales: ✅ Fila y Columna
- Formato métrica: 0.0

**Resultado:**
```
              Donación Patrocinio Volunt. Total
Salud         9.2      8.8        8.5     8.9
Educación     8.6      8.3        8.2     8.4
Retail        8.1      7.9        8.0     8.0
Tech          7.8      7.7        7.9     7.8
Manufactura   7.6      7.4        7.5     7.5
Total         8.3      8.0        8.0     8.1
```

</div>
<div v-click>

## Aplicar Formato de Mapa de Calor

**Panel ESTILO → Formato condicional:**

**Escala de Colores:**
- **Tipo:** Gradiente de colores
- **Mínimo (7.0):** #E30074 (Rosa)
- **Medio (8.0):** #FFB612 (Amarillo)
- **Máximo (9.0+):** #8DC63F (Verde)

**Métricas → Formato:**
- Alineación: Centro
- Tamaño fuente: 14px
- Negrita: ✅

**Encabezados:**
- Fondo giro: #00A3E0
- Fondo canal: #004B87 (Azul oscuro)

<div v-click class="mt-4 p-4 bg-purple-500 bg-opacity-10 rounded">

**Insight:** Combinación "Salud + Donación" tiene la satisfacción más alta (9.2). "Manufactura + Patrocinio" requiere atención (7.4).

</div>

</div>
</div>

---

# Paso 11: Filtros Interactivos

<div class="grid grid-cols-2 gap-8">
<div>

## Filtro 1: Giro Empresarial

**Insertar → Control de lista desplegable**

**Panel DATOS:**
- Fuente: Dashboard Teletón - Datos
- **Dimensión de control:** giro
- **Métrica (opcional):** Record Count (para mostrar cantidad)

**Panel ESTILO:**
- **Etiqueta del control:** "Filtrar por Giro:"
- Permitir varios valores: ✅ (multiselect)
- Incluir opción "Todos": ✅
- Ordenar por: Métrica (más empresas primero)

**Posición:** Arriba del dashboard (debajo de KPIs)

</div>
<div v-click>

## Filtro 2: Canal de Apoyo

**Insertar → Casillas de verificación**

**DATOS:**
- Dimensión: canal_apoyo

**ESTILO:**
- Etiqueta: "Canal de Apoyo:"
- Disposición: Horizontal
- Todas seleccionadas por defecto: ✅

**Posición:** Al lado del Filtro 1

### Filtro 3: Rango de Satisfacción

**Insertar → Control deslizante**

**DATOS:**
- Dimensión: satisfaccion
- Rango: 1 - 10

**ESTILO:**
- Etiqueta: "Rango de Satisfacción:"
- Paso: 0.5

</div>
</div>

---

# Paso 12: Layout y Diseño Final

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Estructura del Dashboard

```
┌──────────────────────────────────────────┐
│  LOGO TELETÓN     TÍTULO DEL DASHBOARD   │
├──────────────────────────────────────────┤
│  KPI 1    KPI 2    KPI 3         KPI 4   │
├──────────────────────────────────────────┤
│  Filtro Giro ▼   Canal ☑☑☑   Satisf. ─● │
├──────────────────────────────────────────┤
│  Satisfacción por Giro (Barras)          │
│  ████████████ 8.9                        │
│  ███████████  8.4                        │
├────────────────────┬─────────────────────┤
│ Tendencia Temporal │  Heatmap Giro×Canal│
│ (Líneas)           │  (Tabla Dinámica)  │
├────────────────────┴─────────────────────┤
│  Tabla Detallada (Top 10 empresas)       │
└──────────────────────────────────────────┘
```

</div>
<div v-click>

## Aplicar Tema Corporativo

**Tema → Personalizar**

### Colores de la Marca (Teletón)
```
Primario:   #00A3E0 (Azul)
Secundario: #E30074 (Rosa)
Acento 1:   #8DC63F (Verde)
Acento 2:   #FFB612 (Amarillo)
Fondo:      #FFFFFF (Blanco)
Texto:      #333333 (Gris oscuro)
```

### Tipografía
- **Títulos:** Montserrat Bold, 24px
- **Subtítulos:** Montserrat SemiBold, 16px
- **Cuerpo:** Open Sans Regular, 12px

### Logo
**Insertar → Imagen**
- Subir logo Teletón (PNG transparente)
- Posición: Esquina superior izquierda
- Tamaño: 120x60px

</div>
</div>

---

# Paso 13: Agregar Contexto y Storytelling

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Cuadros de Texto para Insights

**Insertar → Cuadro de texto**

### Insight 1: Arriba del gráfico de barras
```
📊 Hallazgo Clave:

Las empresas del sector SALUD muestran la
mayor satisfacción (8.9/10), superando el
promedio general en 0.7 puntos.

Acción sugerida: Replicar las prácticas de
engagement del sector Salud en otros giros.
```

**Estilo:**
- Fondo: #E8F5FA (Azul muy claro)
- Borde izquierdo: 4px sólido #00A3E0
- Padding: 12px

</div>
<div v-click>

### Insight 2: Debajo de la tabla
```
⚠️ Área de Oportunidad:

12 empresas (4.4%) tienen satisfacción <6/10
y están en riesgo de no continuar su apoyo.

Acción inmediata: Contacto personalizado
de la Dirección de Alianzas en próximos 7 días.
```

**Estilo:**
- Fondo: #FFF4E6 (Amarillo muy claro)
- Borde: 2px punteado #FFB612

### Metadata Footer
```
─────────────────────────────────────────
Fuente: Encuesta Satisfacción Benefactores 2024
Elaborado por: [Tu Nombre] | Fecha: Enero 2025
Datos: 274 empresas benefactoras
─────────────────────────────────────────
```

</div>
</div>

---

# Paso 14: Compartir y Exportar

<div class="grid grid-cols-2 gap-8">
<div>

## Opción 1: Compartir Link

**Botón Compartir (arriba derecha)**

### Niveles de Acceso

**1. Ver (recomendado para entrega)**
- Usuario puede ver e interactuar
- No puede editar
- Link: `https://lookerstudio.google.com/reporting/abc123...`

**2. Editar**
- Usuario puede modificar dashboard
- Solo para colaboradores

### Configuración
- ✅ Obtener enlace para compartir
- ✅ Cualquier persona con el enlace puede VER
- ❌ No permitir edición

**Copiar link y entregar en Canvas**

</div>
<div v-click>

## Opción 2: Exportar como PDF

**Archivo → Descargar informe**

### Configuración de Exportación

**Orientación:** Horizontal (para dashboards anchos)

**Tamaño:** A4 o Carta

**Incluir:**
- ✅ Todas las páginas
- ✅ Mantener interactividad (si soporta PDF interactivo)
- ❌ Credenciales de datos (privacidad)

**Formato:** PDF

**Nombre:** `Dashboard_Teleton_[TuNombre]_2024.pdf`

### Opción 3: Programar Envíos

**Programar entrega por correo:**
- Frecuencia: Semanal/Mensual
- Destinatarios: stakeholders@teleton.org
- Formato: PDF adjunto

</div>
</div>

---

# Paso 15: Checklist de Calidad

<div class="grid grid-cols-2 gap-6 text-sm">
<div>

## ✅ Datos
- [ ] Fuente de datos conectada correctamente
- [ ] Sin errores de tipo (números como texto)
- [ ] Valores nulos manejados
- [ ] Métricas calculadas probadas
- [ ] Filtros funcionan correctamente

## ✅ Visualizaciones
- [ ] Tipo de gráfico apropiado para cada pregunta
- [ ] Ejes etiquetados con unidades
- [ ] Colores consistentes con marca
- [ ] Formato condicional aplicado
- [ ] Leyendas claras

## ✅ Diseño
- [ ] Jerarquía visual (KPIs arriba)
- [ ] Espaciado consistente
- [ ] Alineación de elementos
- [ ] Logo y branding incluidos
- [ ] Sin elementos superpuestos

</div>
<div v-click>

## ✅ Interactividad
- [ ] Filtros funcionan en todos los gráficos
- [ ] Rango de fechas (si aplica) operativo
- [ ] Drill-down habilitado donde corresponde
- [ ] Sin filtros conflictivos

## ✅ Narrativa
- [ ] Título descriptivo
- [ ] Insights destacados con cuadros de texto
- [ ] Recomendaciones accionables incluidas
- [ ] Metadata (fuente, fecha) en footer

## ✅ Entrega
- [ ] Link compartido con permisos correctos
- [ ] PDF exportado (backup)
- [ ] Documento de interpretación (1-2 páginas)
- [ ] Probado en vista de solo lectura

</div>
</div>

<div v-click class="mt-6 p-6 bg-green-500 bg-opacity-10 rounded text-center">

**Listo para Entregar:** Si marcaste todos los checkboxes, tu dashboard está profesional

</div>

---
layout: section
---

# Parte 4: Tips Avanzados y Troubleshooting

## Problemas Comunes y Soluciones

---

# Problemas Comunes en Looker Studio

<div class="grid grid-cols-2 gap-6 text-sm">
<div>

## Problema 1: "Sin datos"

### Causas
- Fuente desconectada
- Filtros muy restrictivos
- Campo incorrecto seleccionado

### Solución
```
1. Panel DATOS → Verificar fuente activa
2. Quitar todos los filtros temporalmente
3. Verificar permisos de Google Sheets
4. Refrescar datos: Recurso → Administrar datos
   → [Tu fuente] → Actualizar
```

## Problema 2: Números como Texto

### Síntoma
- AVG muestra valores raros (ej: 789.2)
- Suma concatena en vez de sumar

### Solución
```
1. Recurso → Administrar campos agregados
2. Buscar campo (ej: satisfaccion)
3. Tipo → Cambiar a: Número
4. Agregación predeterminada → Promedio
```

</div>
<div v-click>

## Problema 3: Dashboard Muy Lento

### Causas
- Fuente con >100K filas
- Muchos campos calculados complejos
- Gráficos con demasiadas series

### Solución
```
1. Filtrar datos en la fuente (Google Sheets)
   Ej: Solo últimos 12 meses
2. Precalcular métricas en Python antes de subir
3. Limitar categorías en gráficos (Top 10)
4. Usar extractos de datos (cache)
```

## Problema 4: Colores No Se Guardan

### Síntoma
- Aplicas tema, pero al recargar vuelven colores default

### Solución
```
1. Tema → Personalizar tema
2. Aplicar colores en TEMA, no en cada gráfico
3. Guardar como "Tema personalizado - Teletón"
4. Aplicar tema a TODO el informe
```

</div>
</div>

---

# Tips Avanzados para Dashboards Profesionales

<div class="grid grid-cols-3 gap-6 text-xs">

<div>

### 1. Uso de Parámetros

**Qué son:** Variables que el usuario puede cambiar

**Ejemplo:** Umbral de satisfacción dinámico

**Crear parámetro:**
```
Recurso → Administrar parámetros
→ Crear parámetro

Nombre: umbral_meta
Tipo: Número
Valores permitidos: Lista
  - 7.5
  - 8.0
  - 8.5
Default: 8.0
```

**Usar en campo calculado:**
```sql
CASE
  WHEN satisfaccion >= @umbral_meta
  THEN "Meta Alcanzada"
  ELSE "Bajo Meta"
END
```

</div>

<div v-click>

### 2. Drill-Down Jerárquico

**Escenario:** De región → estado → ciudad

**Configurar:**
```
1. Gráfico de barras: región
2. En gráfico → Interacciones
3. ✅ Aplicar filtro al hacer clic
4. Crear segunda página con gráfico de ciudades
5. Enlazar: Clic en región → Ir a página 2
```

**Resultado:** Usuario hace clic en "Norte" → ve detalle de ciudades del Norte

### 3. Control de Periodo Comparativo

**Comparar vs año anterior:**

**Campo calculado:**
```sql
satisfaccion -
  LAG(satisfaccion, 12)
  OVER (ORDER BY mes)
```

Muestra: +0.5 (mejoró), -0.3 (empeoró)

</div>

<div v-click>

### 4. Alertas Visuales

**Indicadores de alerta:**

**Campo calculado (icono):**
```sql
CASE
  WHEN satisfaccion < 6
  THEN "🔴 URGENTE"
  WHEN satisfaccion < 7.5
  THEN "🟡 REVISAR"
  ELSE "🟢 OK"
END
```

**Usar en tabla como primera columna**

### 5. Combinar Múltiples Fuentes

**Ejemplo:** Datos de encuesta + Datos de CRM

**Data blending:**
```
1. Agregar segunda fuente (CRM)
2. En gráfico → DATOS
3. Combinar datos
4. Join por: benefactor_id
5. Dimensiones de Fuente 1
6. Métricas de ambas fuentes
```

</div>

</div>

---

# Galería de Inspiración: Dashboards Teletón

<div class="grid grid-cols-2 gap-8 text-sm">
<div>

## Ejemplo 1: Dashboard Ejecutivo Minimalista

**Características:**
- Solo 4 KPIs principales
- 2 gráficos de tendencia
- Mucho espacio en blanco
- Sin filtros (vista única para Junta)

**Cuándo usar:**
- Presentaciones ejecutivas
- Reportes mensuales a Dirección
- Vista rápida de 30 segundos

## Ejemplo 2: Dashboard Operativo Completo

**Características:**
- 8-10 visualizaciones
- Múltiples filtros (giro, región, tiempo)
- Tabla de detalles drill-down
- Sección de alertas

**Cuándo usar:**
- Equipos operativos diarios
- Análisis detallado
- Investigación de problemas

</div>
<div v-click>

## Ejemplo 3: Dashboard de Storytelling

**Características:**
- Estructura narrativa (problema → análisis → solución)
- Anotaciones con insights
- 3 páginas: Overview → Deep Dive → Recomendaciones
- Iconos y elementos visuales

**Cuándo usar:**
- Presentaciones a stakeholders externos
- Reportes anuales
- Casos de estudio

## Recursos de Ejemplos

**Looker Studio Gallery:**
- [lookerstudio.google.com/gallery](https://lookerstudio.google.com/gallery)
- Buscar: "nonprofit", "NGO", "satisfaction survey"

**Templates para clonar:**
- Filtrar por: "Cloneable templates"
- Adaptar con tus datos Teletón

</div>
</div>

---
layout: center
class: text-center
---

# Resumen: Tutorial Looker Studio

<div class="grid grid-cols-3 gap-6 mt-12 text-sm">

<div v-click>

### 🔧 Preparación
1. Limpiar datos en Python
2. Exportar a Google Sheets
3. Agregar columnas calculadas
4. Conectar Looker Studio

</div>

<div v-click>

### 📊 Construcción
5. KPIs (4 scorecards)
6. Gráficos (barras, líneas, tabla)
7. Filtros interactivos
8. Formato condicional
9. Heatmap (tabla dinámica)

</div>

<div v-click>

### 🎨 Finalización
10. Tema corporativo Teletón
11. Insights con cuadros de texto
12. Logo y metadata
13. Checklist de calidad
14. Compartir/Exportar

</div>

</div>

<div v-click class="mt-16 text-2xl font-bold text-gradient">
Dashboard Teletón completo en ~90 minutos
</div>

---
layout: end
class: text-center
---

# ¡Gracias!

## Próxima Clase: Streamlit - Alternativa con Python

### Actividad: Completar tu Dashboard de Teletón y compartir el link

<div class="mt-8 opacity-75">
CD2001B - Semana 4<br>
Tec de Monterrey Campus Puebla
</div>
