# Presentaciones Slidev - CD2001B

Material de apoyo visual para el curso **Diagnóstico para Líneas de Acción**.

## Contenido

### Semana 1
- `semana1-medidas-descriptivas.md` - Medidas de Tendencia Central y Dispersión
- `semana1-pruebas-hipotesis.md` - Introducción a Pruebas de Hipótesis

## Instalación

```bash
cd slides
npm install
```

## Uso

### Modo presentación (servidor de desarrollo)

```bash
npm run dev
```

Esto abrirá el navegador en `http://localhost:3030` donde podrás:
- Navegar entre slides con flechas del teclado
- Ver notas del presentador presionando `s`
- Modo presentador con `p`
- Dibujar en las slides con `d`

### Construir para producción

```bash
npm run build
```

Genera archivos estáticos en `dist/`

### Exportar a PDF

```bash
npm run export
```

Genera un archivo PDF de la presentación.

## Características

### Tema Personalizado Tec
- Colores oficiales Tec de Monterrey (Azul Reflex #0062A4)
- Estilos personalizados en `styles/tec-theme.css`
- Animaciones suaves con `v-click`

### Elementos Interactivos
- **Animaciones progresivas**: Usa `<div v-click>` para revelar contenido paso a paso
- **Diagramas Mermaid**: Flowcharts y diagramas integrados
- **Layouts flexibles**: two-cols, center, cover, section
- **Cajas de alerta**: `.alert-info`, `.alert-warning`, `.alert-success`

## Navegación en Presentación

| Tecla | Acción |
|-------|--------|
| `→` / `Space` | Siguiente slide/click |
| `←` | Slide anterior |
| `↑` / `↓` | Navegar clicks en slide |
| `f` | Pantalla completa |
| `o` | Vista general de slides |
| `d` | Modo dibujo |
| `s` | Notas del presentador |

## Estructura de Archivos

```
slides/
├── README.md                          # Este archivo
├── package.json                       # Dependencias Slidev
├── styles/
│   └── tec-theme.css                 # Tema personalizado Tec
├── semana1-medidas-descriptivas.md   # Presentación 1
└── semana1-pruebas-hipotesis.md      # Presentación 2
```

## Documentación Slidev

Para más información sobre cómo usar Slidev, consulta:
- [Documentación oficial](https://sli.dev)
- [Sintaxis de Markdown](https://sli.dev/guide/syntax)
- [Animaciones](https://sli.dev/guide/animations)
