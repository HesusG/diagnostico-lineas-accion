# Checklist de Visualización de Datos

**Curso:** CD2001B - Diagnóstico para Líneas de Acción
**Propósito:** Asegurar que tu dashboard y visualizaciones sean efectivas y profesionales

---

## 📊 Antes de Crear tu Dashboard

### Planificación

- [ ] Identifiqué mi audiencia principal (directivos ONG, donantes, equipo operativo)
- [ ] Definí el objetivo del dashboard (monitoreo, reportes, toma de decisiones)
- [ ] Listé los 3-5 KPIs más importantes
- [ ] Tengo los datos limpios y en formato adecuado
- [ ] Creé boceto en papel del layout del dashboard

### Datos

- [ ] Datos están actualizados
- [ ] No hay valores faltantes críticos
- [ ] Variables están en formato correcto (fechas, números, categorías)
- [ ] Nombres de columnas son claros y sin caracteres especiales
- [ ] Tengo diccionario de datos documentado

---

## 🎨 Diseño de Visualizaciones

### Selección de Gráficos

- [ ] Usé el tipo de gráfico correcto para cada dato:
  - [ ] **KPI Cards** para métricas principales (Total atenciones, Satisfacción, etc.)
  - [ ] **Líneas** para tendencias temporales
  - [ ] **Barras** para comparaciones entre categorías
  - [ ] **Circular/Dona** para proporciones (max 5 categorías)
  - [ ] **Histograma/Boxplot** para distribuciones
  - [ ] **Scatter** para correlaciones
  - [ ] **Mapas** para datos geográficos

### Elementos Visuales

- [ ] Usé paleta de colores consistente (preferentemente Tec de Monterrey)
- [ ] Evité más de 5 colores diferentes
- [ ] Colores tienen contraste suficiente
- [ ] Usé rojo/naranja para valores negativos o alertas
- [ ] Usé verde para valores positivos o metas alcanzadas
- [ ] Agregué líneas de referencia (metas, promedios)

### Etiquetas y Anotaciones

- [ ] Todos los gráficos tienen título claro
- [ ] Ejes tienen etiquetas descriptivas
- [ ] Unidades están especificadas (%, pesos, minutos)
- [ ] Valores importantes están etiquetados directamente
- [ ] Leyendas son claras y concisas
- [ ] Fechas en formato legible (Ene 2024, no 2024-01-01)

---

## 📱 Layout del Dashboard

### Organización

- [ ] KPIs principales están en la parte superior
- [ ] Gráficos más importantes están arriba a la izquierda
- [ ] Hay un flujo lógico de lectura (izquierda→derecha, arriba→abajo)
- [ ] No hay más de 6-8 visualizaciones en una página
- [ ] Hay espacio en blanco adecuado entre elementos

### Filtros e Interactividad

- [ ] Agregué filtros clave (fecha, ubicación, tipo de servicio)
- [ ] Filtros están en ubicación visible (arriba o lateral izquierdo)
- [ ] Configuré filtros para que afecten múltiples gráficos
- [ ] Probé que los filtros funcionen correctamente
- [ ] Agregué opciones de "Todos" en filtros categóricos

### Responsividad

- [ ] Dashboard se ve bien en pantalla de escritorio
- [ ] Dashboard se ve bien en tablet
- [ ] Dashboard se ve bien en celular (si aplica)

---

## ✅ Calidad de las Visualizaciones

### Evitar Errores Comunes

- [ ] NO usé gráfico de pie con más de 5 categorías
- [ ] NO usé 3D en gráficos (dificulta lectura)
- [ ] NO sobrecargué el dashboard con demasiados gráficos
- [ ] NO usé colores que no transmiten significado
- [ ] NO omití leyendas donde son necesarias
- [ ] NO usé escalas que distorsionan la información
- [ ] NO incluí decimales innecesarios (7.23456 → 7.2)

### Accesibilidad

- [ ] Textos son legibles (tamaño mínimo 10-12pt)
- [ ] Usé paleta amigable para daltonismo
- [ ] Evité depender solo del color para transmitir información
- [ ] Agregué tooltips con información adicional

---

## 📊 Tipos de Visualizaciones Recomendadas por Caso

### Para tu ONG, considera incluir:

**KPIs de Calidad:**
- [ ] Card: Satisfacción promedio
- [ ] Card: % de beneficiarios satisfechos
- [ ] Gráfico de línea: Tendencia de satisfacción mensual
- [ ] Gráfico de barras: Satisfacción por grupo demográfico

**KPIs de Eficiencia:**
- [ ] Card: Tiempo promedio de atención
- [ ] Histograma: Distribución de tiempos
- [ ] Boxplot: Comparación de tiempos por ubicación

**KPIs de Alcance:**
- [ ] Card: Total de atenciones
- [ ] Gráfico de área: Acumulado de atenciones en el tiempo
- [ ] Mapa: Distribución geográfica de beneficiarios

**KPIs de Recursos:**
- [ ] Card: Costo promedio por beneficiario
- [ ] Gráfico de barras apiladas: Distribución de presupuesto

---

## 🚀 Antes de Compartir

### Revisión Final

- [ ] Revisé ortografía en todos los textos
- [ ] Verifiqué que los números son correctos
- [ ] Probé todos los filtros
- [ ] Actualicé fecha de "Última actualización"
- [ ] Dashboard tiene título descriptivo
- [ ] Agregué mi nombre y contacto
- [ ] Incluí fuente de datos y periodo cubierto

### Documentación

- [ ] Creé guía breve de uso del dashboard
- [ ] Documenté definiciones de KPIs
- [ ] Expliqué cómo interpretar cada gráfico
- [ ] Indiqué frecuencia de actualización de datos

### Testing

- [ ] Probé el dashboard con alguien que no esté familiarizado
- [ ] Esa persona pudo entender los hallazgos principales
- [ ] Esa persona pudo usar los filtros sin ayuda
- [ ] Recibí y apliqué feedback

---

## 💡 Tips de Mejores Prácticas

### Do's (Hacer):
✅ Usa gráficos simples y claros
✅ Destaca los hallazgos más importantes
✅ Usa anotaciones para explicar anomalías
✅ Mantén consistencia en colores y formatos
✅ Actualiza regularmente los datos
✅ Cuenta una historia con tus datos

### Don'ts (No hacer):
❌ Sobrecargar con demasiados gráficos
❌ Usar efectos visuales innecesarios
❌ Ocultar información importante
❌ Usar escalas engañosas
❌ Ignorar valores atípicos sin explicación
❌ Crear dashboards sin propósito claro

---

## 📚 Recursos de Apoyo

**Guías del curso:**
- `/Semana4/guias/guia_tipos_graficos.md` - Cuándo usar cada tipo de gráfico
- `/Semana4/guias/guia_looker_studio_basico.md` - Tutorial de Looker Studio
- `/Semana4/ejemplos/dashboard_ejemplo_ong.pdf` - Ejemplo de dashboard completo

**Recursos externos:**
- [Looker Studio Gallery](https://lookerstudio.google.com/gallery) - Ejemplos e inspiración
- [Data Visualization Catalogue](https://datavizcatalogue.com/) - Catálogo de tipos de gráficos
- [Coolors.co](https://coolors.co/) - Generador de paletas de colores

---

## ✅ Checklist Rápido Final

Antes de entregar tu dashboard, asegúrate de:

- [ ] Responde claramente las preguntas clave de negocio
- [ ] Puede ser entendido sin explicación adicional
- [ ] Es visualmente atractivo pero no distractivo
- [ ] Los datos son precisos y están actualizados
- [ ] Funciona correctamente en diferentes dispositivos
- [ ] Tiene un propósito claro y lo cumple

---

**¡Tu dashboard está listo para presentar!** 🎉

Recuerda: Un buen dashboard cuenta una historia con datos, facilita la toma de decisiones y es fácil de entender a primera vista.
