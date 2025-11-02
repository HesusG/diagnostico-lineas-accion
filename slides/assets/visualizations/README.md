# Visualization Assets for Slidev Presentation

This folder contains professional SVG charts generated for the `semana4-fundamentos-visualizacion.md` presentation.

## 📊 Generated Charts

### Good Examples (Professional Visualizations)

| File | Description | Used In Slide |
|------|-------------|---------------|
| `bar-satisfaction-by-area.svg` | Horizontal bar chart showing satisfaction by geographic area | Slide: "Gráficos de Barras - Ejemplo" |
| `line-satisfaction-trend.svg` | Line chart showing temporal satisfaction trend with annotations | Slide: "¿Por Qué Visualizar Datos?" & "Gráficos de Líneas" |
| `scatter-time-vs-satisfaction.svg` | Scatter plot with regression line showing time vs satisfaction correlation | Slide: "Scatter Plots" |
| `histogram-attention-time.svg` | Histogram showing distribution of attention times | Slide: "Histogramas y Box Plots" |
| `boxplot-satisfaction-by-program.svg` | Box plot comparing satisfaction across programs | Slide: "Histogramas y Box Plots" |
| `heatmap-satisfaction-area-month.svg` | Heatmap showing satisfaction by area × month | Slide: "Heatmaps" |
| `stacked-bar-program-distribution.svg` | 100% stacked bar showing program distribution | Slide: "Pie Charts (alternative)" |
| `line-multiple-areas-comparison.svg` | Multi-line chart comparing satisfaction across areas | Slide: "Gráficos de Líneas - Múltiples Líneas" |
| `bar-grouped-gender-program.svg` | Grouped bar chart showing program participation by gender | Slide: "Gráficos de Barras - Variantes" |
| `kpi-cards-example.svg` | KPI card designs for dashboards | Slide: "Dashboard Design" (optional) |

### Anti-Pattern Examples (What NOT to Do)

| File | Description | Used In Slide |
|------|-------------|---------------|
| `bar-3d-bad-example.svg` | 3D bar chart showing perception distortion | Slide: "Anti-Pattern 1: Gráficos 3D" |
| `line-truncated-axis-comparison.svg` | Side-by-side comparison of truncated vs full axis | Slide: "Anti-Pattern 2: Ejes Truncados" |
| `bar-color-comparison.svg` | Comparison of rainbow colors vs semantic colors | Slide: "Anti-Pattern 3: Demasiados Colores" |
| `pie-vs-bar-comparison.svg` | Pie chart with many slices vs horizontal bars | Slide: "Anti-Pattern 4: Pie Charts" |
| `line-double-axis-bad-example.svg` | Double Y-axis showing manipulation potential | Slide: "Anti-Pattern 5: Doble Eje Y" |

## 🎨 Design Specifications

### Color Palette (Tec de Monterrey)
- **Primary Blue**: `#0062A4`
- **Dark Blue**: `#003E7E`
- **Green**: `#8CC63F`
- **Orange**: `#FF6F31`
- **Gray**: `#6D6E71`

### Semantic Colors
- **Success/Good**: Green (#8CC63F)
- **Warning**: Orange (#FF6F31)
- **Error/Bad**: Red (#D32F2F)
- **Neutral**: Gray (#6D6E71)

### Technical Specs
- **Format**: SVG (scalable vector graphics)
- **Dimensions**: 10x6 inches (standard presentation ratio)
- **DPI**: 150 (high quality for projection)
- **Style**: Seaborn whitegrid (clean, professional)
- **Font**: Sans-serif, 12-14pt
- **Total file size**: ~2-3 MB (all charts combined)

## 🔄 Regenerating Visualizations

If you need to regenerate these charts (e.g., with updated data):

### Prerequisites
```bash
pip install pandas matplotlib seaborn numpy
```

### Run Generation Script
```bash
cd /path/to/slides
python3 generate_visualizations.py
```

### Output
- All SVG files will be regenerated in this folder
- Existing files will be overwritten
- Generation takes approximately 30-60 seconds

## 📂 Data Source

All charts are generated from: `../../../Semana4/datos/datos_ong_ejemplo.csv`

**Dataset:** 100 records of ONG beneficiaries with columns:
- `beneficiario_id`: Unique identifier
- `nombre`: Beneficiary name
- `edad`: Age
- `genero`: Gender (M/F)
- `area`: Geographic area (Norte, Sur, Este, Oeste, Centro)
- `programa`: Program type (Alimentación, Salud, Educación, Vivienda, Empleo)
- `fecha`: Date of service
- `satisfaccion`: Satisfaction score (1-10)
- `tiempo_atencion_min`: Attention time in minutes
- `resolucion_exitosa`: Successful resolution (SI/NO)
- `comentarios`: Optional comments

## 🎯 Usage in Slidev

### Embedding Images
```markdown
<img src="./assets/visualizations/bar-satisfaction-by-area.svg"
     class="w-full max-h-96 object-contain" />
```

### Sizing Classes
- `max-h-64`: Small (256px)
- `max-h-80`: Medium (320px)
- `max-h-96`: Large (384px)
- `w-full`: Full width of container
- `object-contain`: Maintain aspect ratio

## 📝 Maintenance Notes

### When to Regenerate
- ✅ Data in `datos_ong_ejemplo.csv` is updated
- ✅ Design specifications change (colors, fonts)
- ✅ New chart types are needed
- ✅ Bug fixes in visualization logic

### Version Control
- ✅ All SVG files are committed to git
- ✅ Generation script (`generate_visualizations.py`) is version controlled
- ✅ This README is updated when charts change

### File Naming Convention
- **Good examples**: `[chart-type]-[description].svg`
  - Example: `bar-satisfaction-by-area.svg`
- **Anti-patterns**: `[chart-type]-[problem]-[bad/comparison].svg`
  - Example: `bar-3d-bad-example.svg`
  - Example: `line-truncated-axis-comparison.svg`

## 🔗 Related Files

- **Generation Script**: `../../generate_visualizations.py`
- **Presentation**: `../../semana4-fundamentos-visualizacion.md`
- **Data Source**: `../../../Semana4/datos/datos_ong_ejemplo.csv`
- **Backup**: `../../semana4-fundamentos-visualizacion.md.backup`

## 📚 Resources

### Libraries Used
- **Pandas**: Data manipulation
- **Matplotlib**: Base plotting library
- **Seaborn**: Statistical visualization
- **NumPy**: Numerical operations

### Style Reference
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Data Visualization Best Practices](https://www.storytellingwithdata.com/)

---

**Last Updated**: October 2025
**Version**: 1.0
**Maintained by**: CD2001B Course Team
