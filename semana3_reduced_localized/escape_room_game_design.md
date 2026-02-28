# Documento de Diseño: Escape Room "La Misión del Conde Donador"

## Especificaciones Técnicas

| Atributo | Valor |
|----------|-------|
| **Plataforma** | Navegador web (GitHub Pages) |
| **Tecnología** | HTML5, CSS3, JavaScript vanilla |
| **Almacenamiento** | LocalStorage |
| **Resolución** | 800x600 px |
| **Estilo visual** | Pixel art top-down 32x32 |
| **Tiempo límite** | 30 minutos |

---

## Narrativa

El **Conde Von Donativo** es el mayor benefactor de Fundación Teletón. Tiene una reunión con su junta directiva en 30 minutos y necesita un **reporte ejecutivo con evidencia sólida** para aprobar una donación de $10 millones de pesos.

El jugador asume el rol de un **analista de datos** que debe recorrer la mansión recolectando la evidencia correcta: estadísticas descriptivas, pruebas de hipótesis, análisis estratégico y visualizaciones efectivas.

---

## Condiciones de Victoria y Derrota

### Victoria
- Recolectar las **8 evidencias correctas** antes de que termine el tiempo
- Presentarlas al Conde en el orden lógico de un reporte

### Derrota (Game Over)
- El timer llega a 00:00
- El jugador selecciona **3 distractores** (pierde credibilidad ante la junta)

---

## Flujo de Análisis (Cómo Gana un Analista Real)

El juego sigue la lógica de un análisis profesional:

```
┌─────────────────────────────────────────────────────────────┐
│           FLUJO DE TRABAJO DEL ANALISTA                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. ENTENDER EL CONTEXTO                                    │
│     └─> Archivo Secreto: ¿Qué factores externos afectan?    │
│         (PESTEL)                                             │
│                                                              │
│  2. DESCRIBIR LOS DATOS                                      │
│     └─> Laboratorio: ¿Qué dicen las estadísticas básicas?   │
│         (Media, Mediana, Desviación Estándar)               │
│                                                              │
│  3. PROBAR HIPÓTESIS                                        │
│     └─> Sala de Juntas: ¿Las diferencias son significativas?│
│         (Chi-cuadrada, ANOVA, prueba t)                     │
│                                                              │
│  4. DIAGNOSTICAR SITUACIÓN                                  │
│     └─> Biblioteca: ¿Cuáles son fortalezas y debilidades?   │
│         (FODA con datos)                                     │
│                                                              │
│  5. DEFINIR MÉTRICAS                                        │
│     └─> Oficina: ¿Cómo medimos el éxito?                    │
│         (KPIs: NPS, SERVQUAL)                               │
│                                                              │
│  6. VISUALIZAR PARA DECIDIR                                 │
│     └─> Galería: ¿Cómo comunicamos los hallazgos?           │
│         (Gráficos sin clutter, storytelling)                │
│                                                              │
│  7. PRESENTAR AL CONDE                                      │
│     └─> Gran Vestíbulo: Entregar reporte ejecutivo          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Mapa de la Mansión

```
┌─────────────────────────────────────────────────────────────┐
│                    MANSIÓN DEL CONDE                         │
│                                                              │
│   ┌───────────┐   ┌───────────┐   ┌───────────┐             │
│   │BIBLIOTECA │   │  SALA DE  │   │  OFICINA  │             │
│   │  (FODA)   │───│  JUNTAS   │───│  (KPIs)   │             │
│   │           │   │(Hipótesis)│   │           │             │
│   └─────┬─────┘   └─────┬─────┘   └─────┬─────┘             │
│         │               │               │                    │
│         └───────────────┼───────────────┘                    │
│                         │                                    │
│   ┌─────────────────────┴─────────────────────┐             │
│   │            GRAN VESTÍBULO                  │             │
│   │               (SPAWN)                      │             │
│   │          [TIMER: 30:00]                    │             │
│   │      Aquí entregas el reporte final        │             │
│   └─────────────────────┬─────────────────────┘             │
│                         │                                    │
│         ┌───────────────┼───────────────┐                    │
│         │               │               │                    │
│   ┌─────┴─────┐   ┌─────┴─────┐   ┌─────┴─────┐             │
│   │  GALERÍA  │   │  ARCHIVO  │   │LABORATORIO│             │
│   │ (DataViz) │───│  SECRETO  │───│  (Stats)  │             │
│   │           │   │ (PESTEL)  │   │           │             │
│   └───────────┘   └───────────┘   └───────────┘             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Inventario de Evidencias y Distractores

### Resumen

| Tipo | Cantidad | Ubicación |
|------|----------|-----------|
| **Evidencias correctas** | 8 | Distribuidas en 6 habitaciones |
| **Distractores** | 10 | Mezclados con las evidencias |

---

## Habitaciones y Contenido Detallado

### 1. GRAN VESTÍBULO (Spawn / Final)

**Función:** Punto de inicio y entrega final del reporte

**NPC: Mayordomo**
```
"Bienvenido, analista. El Conde lo espera en 30 minutos.
Necesita un reporte con EVIDENCIA SÓLIDA:
- Datos estadísticos que respalden las afirmaciones
- Análisis del entorno y situación interna
- Métricas claras de desempeño
- Visualizaciones que comuniquen, no que decoren

Recorra la mansión y recolecte la evidencia correcta.
CUIDADO: no todo lo que brilla es oro. Algunos documentos
son distractores que harían quedar mal al Conde."
```

**Objetos:** Ninguna evidencia aquí, solo el punto de entrega final.

---

### 2. LABORATORIO DE ESTADÍSTICAS (Tema: Semana 1 - Descriptivas)

**Ambiente:** Monitores con gráficos, pizarrones con fórmulas, computadoras

**Evidencia #1: Estadísticas Descriptivas**
| Campo | Contenido |
|-------|-----------|
| Nombre | Reporte "Análisis Descriptivo de Satisfacción" |
| Visual | Documento con tablas y números |
| Texto | "Satisfacción de benefactores (n=274): Media = 7.89, Mediana = 8.0, DE = 1.23. La mediana > media sugiere algunos valores bajos (outliers). El 68% de los datos está entre 6.66 y 9.12 (±1 DE)." |
| Concepto | Medidas de tendencia central y dispersión |

**Distractor #1: Solo la Media**
| Campo | Contenido |
|-------|-----------|
| Nombre | Nota adhesiva "Resumen rápido" |
| Visual | Post-it amarillo |
| Texto | "Satisfacción promedio: 7.89. ¡Todo bien!" |
| Por qué es incorrecto | Reportar solo la media sin dispersión es incompleto. No sabemos si hay consistencia o variabilidad. |
| Feedback | "La media sin desviación estándar es información incompleta. ¿Los datos son consistentes o muy dispersos?" |

**Distractor #2: Confusión Media-Mediana**
| Campo | Contenido |
|-------|-----------|
| Nombre | Hoja arrugada "Cálculos" |
| Visual | Papel con tachones |
| Texto | "Media = 7.89. Como la media es alta, los salarios de todos los empleados de Teletón son buenos y nadie gana poco." |
| Por qué es incorrecto | La media es sensible a outliers. En salarios, unos pocos altos suben el promedio. La mediana sería mejor. |
| Feedback | "La media es engañosa cuando hay outliers. En salarios, un CEO puede subir el promedio aunque la mayoría gane poco." |

---

### 3. SALA DE JUNTAS (Tema: Semana 2 - Pruebas de Hipótesis)

**Ambiente:** Mesa ejecutiva larga, presentaciones en pantalla, folders

**Evidencia #2: Prueba Chi-Cuadrada**
| Campo | Contenido |
|-------|-----------|
| Nombre | Informe "Análisis Chi-Cuadrada: Tipo de Organización × Satisfacción" |
| Visual | Folder con tabla de contingencia |
| Texto | "Se analizó si el tipo de organización (Empresa, Gobierno, Educación) está relacionado con el nivel de satisfacción. Resultado: χ² = 12.4, p = 0.002. CONCLUSIÓN: Sí hay relación significativa. Las empresas tienen NPS más bajo (+29) que gobierno (+57)." |
| Concepto | Chi-cuadrada para variables categóricas |

**Evidencia #3: ANOVA de Regiones**
| Campo | Contenido |
|-------|-----------|
| Nombre | Reporte "Comparación Regional - ANOVA" |
| Visual | Documento con boxplots |
| Texto | "Se comparó satisfacción entre 5 regiones. ANOVA: F = 8.34, p < 0.001. Post-hoc Tukey: Norte (+51) y Sur (+48) significativamente más altos que Centro (+31) y Occidente (+30). ACCIÓN: Investigar prácticas de Norte para replicar." |
| Concepto | ANOVA para comparar 3+ grupos |

**Distractor #3: Múltiples Pruebas t**
| Campo | Contenido |
|-------|-----------|
| Nombre | Carpeta "10 Pruebas t" |
| Visual | Folder grueso |
| Texto | "Comparé todas las regiones con pruebas t: Norte vs Sur (p=0.12), Norte vs Centro (p=0.03), Norte vs Occidente (p=0.04)... y así 10 comparaciones. ¡Encontré 3 diferencias significativas!" |
| Por qué es incorrecto | Múltiples pruebas t inflan el Error Tipo I. Con 10 pruebas, hay 40% de probabilidad de al menos un falso positivo. |
| Feedback | "¡Error Tipo I! Con 10 pruebas t, la probabilidad de falso positivo es 40%. Usa ANOVA + Post-hoc para controlar el error." |

**Distractor #4: p-value Mal Interpretado**
| Campo | Contenido |
|-------|-----------|
| Nombre | Email impreso "Gran Descubrimiento" |
| Visual | Hoja de correo |
| Texto | "¡Increíble! El p-value de 0.03 significa que hay 3% de probabilidad de que nuestra hipótesis sea correcta. ¡Casi seguro que tenemos razón!" |
| Por qué es incorrecto | El p-value NO es la probabilidad de que H₀ sea cierta. Es la probabilidad de obtener los datos observados SI H₀ fuera cierta. |
| Feedback | "Interpretación incorrecta del p-value. NO significa 'probabilidad de que la hipótesis sea correcta'. Indica la probabilidad de los datos bajo H₀." |

---

### 4. BIBLIOTECA (Tema: Semana 3 - FODA)

**Ambiente:** Estantes de libros, mesa de estudio, lámpara verde

**Evidencia #4: FODA con Datos**
| Campo | Contenido |
|-------|-----------|
| Nombre | Pergamino "Análisis FODA Basado en Datos" |
| Visual | Documento con 4 cuadrantes |
| Texto | "FORTALEZAS: Empatía 3.91/5 (más alta SERVQUAL), NPS +40. DEBILIDADES: Responsiveness 3.60/5 (más baja), Empresas NPS +29. OPORTUNIDADES: 59% pasivos convertibles, digitalización. AMENAZAS: Crítica ONU, 9,000 competidores." |
| Concepto | FODA con evidencia cuantitativa |

**Distractor #5: FODA de Opinión**
| Campo | Contenido |
|-------|-----------|
| Nombre | Servilleta "Mi FODA" |
| Visual | Servilleta con garabatos |
| Texto | "FORTALEZAS: Somos buena onda. DEBILIDADES: A veces llegamos tarde. OPORTUNIDADES: La gente nos quiere. AMENAZAS: Hay mucha competencia, creo." |
| Por qué es incorrecto | FODA sin datos es especulación. No hay métricas, solo percepciones subjetivas. |
| Feedback | "Un FODA sin datos es pura opinión. 'Somos buena onda' no convence a una junta. Necesitas métricas: Empatía 3.91/5." |

---

### 5. ARCHIVO SECRETO (Tema: Semana 3 - PESTEL)

**Ambiente:** Archiveros metálicos, luz roja, documentos clasificados

**Evidencia #5: Análisis PESTEL**
| Campo | Contenido |
|-------|-----------|
| Nombre | Expediente "Análisis del Entorno Externo" |
| Visual | Folder clasificado |
| Texto | "P: Convenios gubernamentales vigentes. E: Inflación encarece equipos médicos, pero $1.8MM en inversiones protegen donaciones. S: Debate 'caridad vs derechos' en redes. T: CRITs con robótica de vanguardia. E: Alto costo energético. L: Donataria Autorizada SAT renovada." |
| Concepto | PESTEL - Factores externos documentados |

**Distractor #6: Rumores de Prensa**
| Campo | Contenido |
|-------|-----------|
| Nombre | Recorte "Escándalo: ¿Evasión Fiscal?" |
| Visual | Periódico sensacionalista |
| Texto | "FUENTES CERCANAS AL CASO afirman que Teletón PODRÍA estar usando las donaciones para fines dudosos. No hay pruebas, pero el rumor crece en redes sociales." |
| Por qué es incorrecto | Fuentes anónimas y especulación no son análisis. Sin datos verificables. |
| Feedback | "Fuentes anónimas y 'podría' no son evidencia. El análisis estratégico requiere hechos verificables, no rumores de redes." |

---

### 6. OFICINA DEL CONDE (Tema: Semana 3 - KPIs)

**Ambiente:** Escritorio ejecutivo, computadora, diplomas, caja fuerte

**Evidencia #6: Dashboard de KPIs**
| Campo | Contenido |
|-------|-----------|
| Nombre | Reporte "KPIs de Satisfacción Q4 2024" |
| Visual | Dashboard impreso |
| Texto | "NPS: +40 (Promotores 40.5%, Pasivos 59.1%, Detractores 0.4%). SERVQUAL: 3.67/5 promedio. Transparencia: 79%. Meta de Responsiveness: Subir de 3.60 a 4.0 en 6 meses para convertir pasivos → promotores." |
| Concepto | KPIs accionables con metas |

**Evidencia #7: Regresión Calidad-Satisfacción**
| Campo | Contenido |
|-------|-----------|
| Nombre | Análisis "Modelo Predictivo" |
| Visual | Gráfico de regresión |
| Texto | "Regresión: Satisfacción = 2.1 + 1.5(Calidad_Atención) - 0.08(Tiempo_Espera). R² = 0.79. Interpretación: Por cada punto que sube calidad de atención, satisfacción sube 1.5 puntos. Por cada 10 min de espera adicional, baja 0.8 puntos." |
| Concepto | Regresión lineal múltiple |

**Distractor #7: Correlación = Causalidad**
| Campo | Contenido |
|-------|-----------|
| Nombre | Memo "Descubrimiento Importante" |
| Visual | Nota ejecutiva |
| Texto | "Encontré correlación de r = 0.85 entre satisfacción y número de publicaciones en redes sociales. CONCLUSIÓN: Debemos publicar más en redes para aumentar la satisfacción de benefactores." |
| Por qué es incorrecto | Correlación NO implica causalidad. Puede haber una tercera variable (ej: eventos exitosos generan ambas cosas). |
| Feedback | "Correlación ≠ Causalidad. Publicar más en redes no CAUSA más satisfacción. Probablemente ambas cosas aumentan cuando hay eventos exitosos." |

**Distractor #8: Objetivo No-SMART**
| Campo | Contenido |
|-------|-----------|
| Nombre | Plan estratégico "Visión 2025" |
| Visual | Documento corporativo |
| Texto | "Objetivo: Mejorar mucho la satisfacción de todos los benefactores lo antes posible para ser los mejores de México." |
| Por qué es incorrecto | No es SMART: no es específico (¿cuánto?), no es medible, no tiene plazo definido. |
| Feedback | "Objetivo vago. ¿'Mejorar mucho' cuánto es? ¿'Lo antes posible' es cuándo? Un objetivo SMART sería: 'Subir NPS de +40 a +50 en 12 meses'." |

---

### 7. GALERÍA DE ARTE (Tema: Semana 4 - DataViz / Storytelling)

**Ambiente:** Cuadros con gráficos, iluminación dramática, marcos dorados

**Evidencia #8: Visualización Efectiva**
| Campo | Contenido |
|-------|-----------|
| Nombre | Cuadro "Dashboard de Impacto" |
| Visual | Gráfico de barras limpio |
| Texto | "Barras ordenadas de mayor a menor. Colores semáforo: Verde (meta alcanzada), Amarillo (cerca), Rojo (atención). Título: 'Norte y Sur lideran satisfacción; Centro requiere acción urgente'. Sin 3D, sin clutter, insight en 3 segundos." |
| Concepto | Storytelling with Data - Gráfico efectivo |

**Distractor #9: Gráfico 3D con Clutter**
| Campo | Contenido |
|-------|-----------|
| Nombre | Poster "Infografía Premium" |
| Visual | Pie chart 3D con 12 colores |
| Texto | "Dashboard ejecutivo con gráficos 3D, 12 colores vibrantes, animaciones, sombras y efectos especiales. ¡Se ve muy profesional y moderno!" |
| Por qué es incorrecto | 3D distorsiona percepción, muchos colores agregan clutter, efectos no comunican datos. |
| Feedback | "El 3D distorsiona la percepción de valores. 12 colores agregan carga cognitiva sin aportar información. Un buen gráfico comunica en 3 segundos, no decora." |

**Distractor #10: Título Descriptivo**
| Campo | Contenido |
|-------|-----------|
| Nombre | Lámina "Gráfico de Satisfacción" |
| Visual | Gráfico de barras plano |
| Texto | "Título: 'Gráfico de barras de satisfacción por región Q4 2024 (Datos procesados con Python)'. Subtítulo: 'Elaborado por el departamento de análisis de datos'." |
| Por qué es incorrecto | El título describe el gráfico, no comunica el insight. No dice qué acción tomar. |
| Feedback | "El título debe comunicar el INSIGHT, no describir el gráfico. En vez de 'Gráfico de satisfacción por región', di 'Norte supera la meta; Centro necesita intervención'." |

---

## Tabla Resumen de Objetos

### Evidencias Correctas (8)

| # | Nombre | Ubicación | Concepto | Semana |
|---|--------|-----------|----------|--------|
| 1 | Análisis Descriptivo | Laboratorio | Media, Mediana, DE | 1 |
| 2 | Chi-Cuadrada | Sala Juntas | Relación entre categóricas | 2 |
| 3 | ANOVA Regional | Sala Juntas | Comparar 3+ grupos | 2 |
| 4 | FODA con Datos | Biblioteca | Diagnóstico estratégico | 3 |
| 5 | PESTEL | Archivo | Entorno externo | 3 |
| 6 | Dashboard KPIs | Oficina | Métricas accionables | 3 |
| 7 | Regresión | Oficina | Predicción | 2 |
| 8 | Visualización Efectiva | Galería | Storytelling with Data | 4 |

### Distractores (10)

| # | Nombre | Ubicación | Error |
|---|--------|-----------|-------|
| 1 | Solo la Media | Laboratorio | Sin dispersión |
| 2 | Confusión Media-Mediana | Laboratorio | Outliers ignorados |
| 3 | Múltiples Pruebas t | Sala Juntas | Error Tipo I inflado |
| 4 | p-value Mal Interpretado | Sala Juntas | Confusión probabilística |
| 5 | FODA de Opinión | Biblioteca | Sin datos |
| 6 | Rumores de Prensa | Archivo | Fuentes no verificables |
| 7 | Correlación = Causalidad | Oficina | Confusión conceptual |
| 8 | Objetivo No-SMART | Oficina | Meta vaga |
| 9 | Gráfico 3D + Clutter | Galería | Viola principios DataViz |
| 10 | Título Descriptivo | Galería | No comunica insight |

---

## Ruta Óptima del Analista

```
INICIO (Gran Vestíbulo)
    │
    ▼
1. ARCHIVO SECRETO (2-3 min)
   └─> Recoger: PESTEL
   └─> Ignorar: Rumores de prensa
    │
    ▼
2. LABORATORIO (3-4 min)
   └─> Recoger: Análisis Descriptivo
   └─> Ignorar: Solo media, Confusión media-mediana
    │
    ▼
3. SALA DE JUNTAS (4-5 min)
   └─> Recoger: Chi-Cuadrada, ANOVA
   └─> Ignorar: Múltiples t, p-value mal interpretado
    │
    ▼
4. BIBLIOTECA (2-3 min)
   └─> Recoger: FODA con Datos
   └─> Ignorar: FODA de opinión
    │
    ▼
5. OFICINA (4-5 min)
   └─> Recoger: KPIs, Regresión
   └─> Ignorar: Correlación=Causalidad, Objetivo no-SMART
    │
    ▼
6. GALERÍA (2-3 min)
   └─> Recoger: Visualización Efectiva
   └─> Ignorar: 3D+Clutter, Título descriptivo
    │
    ▼
7. GRAN VESTÍBULO (1 min)
   └─> Presentar reporte al Conde
    │
    ▼
VICTORIA (~20-25 min)
```

**Tiempo estimado ruta óptima:** 20-25 minutos
**Margen disponible:** 5-10 minutos para errores/exploración

---

## Interfaz de Usuario

### HUD Permanente
```
┌────────────────────────────────────────────────────┐
│ ⏰ 24:32    📦 Evidencias: 5/8    ⚠️ Errores: 1/3 │
├────────────────────────────────────────────────────┤
│                                                     │
│               [ÁREA DE JUEGO]                       │
│                                                     │
├────────────────────────────────────────────────────┤
│ 🚪 Ubicación: Sala de Juntas                       │
└────────────────────────────────────────────────────┘
```

### Alertas de Timer
| Tiempo | Visual | Audio |
|--------|--------|-------|
| 30:00 - 10:00 | Blanco | Ninguno |
| 10:00 - 5:00 | Amarillo pulsante | Tick suave |
| 5:00 - 2:00 | Naranja pulsante | Tick rápido |
| 2:00 - 0:00 | Rojo parpadeante | Alarma |

---

## Diálogos de NPCs

### Científica (Laboratorio)
```
"La media cuenta solo una parte de la historia.
Sin desviación estándar, no sabes si los datos
son consistentes o muy dispersos.
Dos ONGs pueden tener media 8.0, pero una
tiene DE=0.5 (consistente) y otra DE=3.0 (caótica)."
```

### Ejecutiva (Sala de Juntas)
```
"Si quieres comparar 5 grupos, NO hagas 10 pruebas t.
El Error Tipo I se acumula: 40% de encontrar un
falso positivo. Usa ANOVA y luego post-hoc Tukey.
Y recuerda: el p-value NO es la probabilidad
de que tu hipótesis sea correcta."
```

### Bibliotecario (Biblioteca)
```
"Un FODA sin datos es poesía, no estrategia.
'Somos buenos' no convence a nadie.
'Empatía 3.91/5, la más alta de SERVQUAL' sí."
```

### Detective (Archivo)
```
"PESTEL analiza lo que NO controlas: gobierno,
economía, sociedad, tecnología, ambiente, leyes.
Fuentes anónimas y rumores NO son análisis.
Datos verificables sí."
```

### Mayordomo (Oficina)
```
"Un KPI sin meta es solo un número.
NPS +40 está bien, pero ¿cuál es el objetivo?
Y cuidado: correlación NO es causalidad.
Que dos cosas se muevan juntas no significa
que una cause la otra."
```

### Curadora (Galería)
```
"Un buen gráfico comunica en 3 segundos.
Sin 3D (distorsiona), sin clutter (distrae),
con color intencional (resalta lo importante).
Y el título debe decir el INSIGHT, no describir
que es 'un gráfico de barras'."
```

---

## Pantallas de Fin

### Victoria
```
┌─────────────────────────────────────────┐
│         🏆 ¡MISIÓN CUMPLIDA!            │
│                                          │
│  👑 CONDE VON DONATIVO:                  │
│                                          │
│  "¡Extraordinario! Este reporte tiene:  │
│   ✓ Datos descriptivos sólidos          │
│   ✓ Pruebas estadísticas rigurosas      │
│   ✓ Análisis estratégico fundamentado   │
│   ✓ Visualizaciones que comunican       │
│                                          │
│  La junta aprobó los $10 millones.      │
│  ¡Teletón recibirá la donación!"        │
│                                          │
│  Tiempo: XX:XX | Errores: X/3           │
│                                          │
│          [JUGAR DE NUEVO]                │
└─────────────────────────────────────────┘
```

### Derrota por Tiempo
```
┌─────────────────────────────────────────┐
│            💀 GAME OVER                 │
│                                          │
│  👑 CONDE VON DONATIVO:                  │
│                                          │
│  "La junta se fue. Sin evidencia a      │
│  tiempo, no hay donación.               │
│                                          │
│  Los niños de Teletón tendrán que       │
│  esperar otro año para ese equipo       │
│  de rehabilitación..."                  │
│                                          │
│          [INTENTAR DE NUEVO]             │
└─────────────────────────────────────────┘
```

### Derrota por Errores
```
┌─────────────────────────────────────────┐
│            💀 GAME OVER                 │
│                                          │
│  👑 CONDE VON DONATIVO:                  │
│                                          │
│  "¿Gráficos 3D? ¿Rumores sin fuente?    │
│  ¿Correlación confundida con causa?     │
│                                          │
│  La junta perdió la confianza en        │
│  el análisis. La donación ha sido       │
│  CANCELADA."                            │
│                                          │
│          [INTENTAR DE NUEVO]             │
└─────────────────────────────────────────┘
```

---

## LocalStorage

```javascript
{
  "escapeRoom_completed": true,     // Si ganó alguna vez
  "escapeRoom_bestTime": "18:45",   // Mejor tiempo
  "escapeRoom_attempts": 3          // Intentos totales
}
```

---

## Checklist de Implementación

- [ ] Pantalla de inicio con narrativa
- [ ] Movimiento top-down (WASD/Flechas)
- [ ] Mapa con 7 habitaciones
- [ ] Timer de 30 minutos visible
- [ ] 8 evidencias correctas con feedback
- [ ] 10 distractores con feedback educativo
- [ ] 6 NPCs con diálogos de ayuda
- [ ] Sistema de inventario (8 slots)
- [ ] Contador de errores (máx 3)
- [ ] Pantalla de victoria
- [ ] Pantallas de derrota (2 variantes)
- [ ] LocalStorage para persistencia
- [ ] Funciona en GitHub Pages

---

## Objetivos de Aprendizaje

Al completar este escape room, el alumno habrá practicado:

1. **Estadística descriptiva:** Importancia de reportar media Y dispersión
2. **Pruebas de hipótesis:** Chi-cuadrada, ANOVA, evitar múltiples t-tests
3. **Interpretación correcta:** p-value, correlación vs causalidad
4. **Análisis estratégico:** FODA y PESTEL con datos, no opiniones
5. **KPIs y objetivos:** Métricas accionables, objetivos SMART
6. **Visualización efectiva:** Principios de Storytelling with Data
7. **Pensamiento crítico:** Discriminar evidencia sólida de distractores

---

**Documento de diseño v2.0**
**Curso:** CD2001B - Diagnóstico para Líneas de Acción
**Tec de Monterrey - Campus Puebla**
