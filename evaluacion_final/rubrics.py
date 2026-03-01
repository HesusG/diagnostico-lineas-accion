#!/usr/bin/env python3
"""
Definicion de las 6 rubricas oficiales para el sistema de evaluacion.
Basado en las subcompetencias del Tecnologico de Monterrey.

Version mejorada: criterios con conductas observables y ejemplos contextualizados.
"""

NIVELES = {
    "Destacado": 100,
    "Solido": 88,
    "Basico": 75,
    "Incipiente": 55,
    "Sin evidencia": 0
}

PONDERACIONES = {
    "SCD0104": 0.20,  # Estadistica Descriptiva
    "SCD0105": 0.20,  # Graficos Dinamicos
    "SCD0303": 0.25,  # Insights y Lineas de Accion
    "SEGE201": 0.15,  # Innovacion
    "SEGE203": 0.10,  # Trabajo Colaborativo
    "SEGE401": 0.10,  # Etica y Responsabilidad Social
}

RUBRICAS = {
    "SCD0104": {
        "nombre": "Estadistica Descriptiva",
        "descripcion": "Resume la informacion mediante herramientas de estadistica descriptiva utilizando soluciones tecnologicas actuales.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Identifica y clasifica todas las variables relevantes del dataset (numericas y categoricas) justificando su inclusion",
                    "Calcula e interpreta correctamente media, mediana, desviacion estandar e IQR; presenta tablas de frecuencia con categorias relevantes usando Python (pandas/scipy) sin errores",
                    "Presenta visualizaciones (histogramas, boxplots, tablas) con titulos, etiquetas de ejes y leyendas que permiten lectura autonoma sin explicacion adicional",
                    "Conecta cada resultado estadistico con una implicacion practica para la problematica; por ejemplo, explica que significa un IQR alto en el contexto del socio formador"
                ],
                "ejemplos": [
                    "Identifica edad, genero, tipo de discapacidad y satisfaccion como variables clave; justifica excluir ID por ser solo identificador",
                    "Reporta: 'La mediana de satisfaccion (8/10) es mayor que la media (7.2), lo que indica sesgo negativo por casos atipicos bajos que podrian representar pacientes con experiencias problematicas'"
                ]
            },
            "Solido": {
                "puntos": 88,
                "criterios": [
                    "Identifica la mayoria de las variables relevantes del dataset y las clasifica correctamente",
                    "Calcula correctamente las estadisticas descriptivas principales (media, mediana, DE) usando Python; las tablas de frecuencia contienen las categorias correctas",
                    "Las visualizaciones tienen titulos y etiquetas, aunque alguna puede carecer de leyenda o formato optimo",
                    "Interpreta los resultados en contexto de la problematica pero sin profundizar en todas las implicaciones practicas"
                ],
                "ejemplos": [
                    "Calcula todas las medidas correctamente pero no comenta la diferencia entre media y mediana ni su implicacion",
                    "Presenta boxplot con titulo pero sin indicar que representan los outliers en el contexto del socio formador"
                ]
            },
            "Basico": {
                "puntos": 75,
                "criterios": [
                    "Identifica al menos la mitad de las variables relevantes; omite variables importantes o incluye variables irrelevantes sin justificacion",
                    "Calcula las estadisticas descriptivas pero con errores menores (ej: confunde mediana con moda) o usa solo un subconjunto de medidas",
                    "Presenta visualizaciones pero les faltan titulos, etiquetas o son de tipo incorrecto para la variable (ej: histograma para variable categorica)",
                    "Describe los numeros obtenidos sin conectarlos con la problematica del socio formador"
                ],
                "ejemplos": [
                    "Reporta 'la media es 7.2' sin explicar que significa en el contexto de satisfaccion de beneficiarios",
                    "Usa grafico de barras para variable continua cuando un histograma seria apropiado"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "Identifica menos de la mitad de las variables relevantes o no las clasifica",
                    "Los calculos estadisticos contienen errores significativos o solo presenta una medida (ej: solo la media)",
                    "Las visualizaciones son ilegibles, carecen de etiquetas, o no corresponden a los datos analizados",
                    "No conecta los resultados con la problematica o la interpretacion contiene errores conceptuales graves"
                ],
                "ejemplos": [
                    "Solo calcula la media de una variable sin explorar distribucion ni dispersión",
                    "Afirma 'la desviacion estandar es alta' sin definir respecto a que ni contextualizar"
                ]
            }
        }
    },

    "SCD0105": {
        "nombre": "Graficos Dinamicos",
        "descripcion": "Genera graficos dinamicos acordes a la naturaleza de las variables, asegurandose que muestran informacion relevante para la toma de decisiones haciendo uso de soluciones tecnologicas actuales.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Selecciona el tipo de grafico correcto segun el nivel de medicion de cada variable (barras para categoricas, histograma para continuas, scatter para relaciones bivariadas)",
                    "Los graficos incluyen interactividad o elementos dinamicos (filtros, tooltips, seleccion) usando herramientas como Plotly, widgets de Jupyter o dashboards",
                    "Cada grafico tiene titulo descriptivo, etiquetas de ejes con unidades, leyenda cuando aplica, y escala apropiada",
                    "Redacta una interpretacion de cada grafico que identifica patrones, tendencias o anomalias relevantes para la toma de decisiones"
                ],
                "ejemplos": [
                    "Usa heatmap interactivo (Plotly) para mostrar correlaciones entre variables numericas del dataset con tooltip que muestra el valor exacto",
                    "Interpreta: 'El scatter plot muestra una correlacion positiva moderada (r=0.64) entre horas de terapia y mejora funcional, sugiriendo que aumentar sesiones podria beneficiar a los pacientes'"
                ]
            },
            "Solido": {
                "puntos": 88,
                "criterios": [
                    "Selecciona el tipo de grafico correcto para la mayoria de las variables; puede tener un error menor de seleccion",
                    "Los graficos son estaticos pero estan bien construidos con matplotlib/seaborn; tiene al menos un intento de interactividad",
                    "La mayoria de los graficos tiene titulos y etiquetas completas; puede faltar alguna leyenda",
                    "Interpreta los graficos correctamente pero no identifica todos los patrones relevantes"
                ],
                "ejemplos": [
                    "Presenta graficos correctos con seaborn pero sin elementos interactivos",
                    "Interpreta la tendencia general pero no menciona outliers visibles en el boxplot"
                ]
            },
            "Basico": {
                "puntos": 75,
                "criterios": [
                    "Selecciona un tipo de grafico incorrecto para al menos una variable (ej: pie chart para variable continua o grafico de lineas para datos sin orden temporal)",
                    "Los graficos son solo estaticos, sin interactividad, usando configuracion por defecto de la libreria",
                    "A varios graficos les faltan titulos, etiquetas de ejes, o tienen escalas confusas",
                    "Las interpretaciones son superficiales ('se ve que hay diferencia') sin cuantificar o contextualizar"
                ],
                "ejemplos": [
                    "Usa pie chart para mostrar distribucion de edades (variable continua) en vez de histograma",
                    "Escribe 'los datos se ven normales' sin fundamentar con test de normalidad o referencia visual"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "Los graficos son de tipo incorrecto para la mayoria de las variables analizadas",
                    "No hay ningun intento de graficos dinamicos o interactivos; solo graficos por defecto de Python",
                    "Los graficos carecen de titulos, etiquetas y leyendas; son ilegibles o confusos",
                    "No interpreta los graficos o la interpretacion contiene errores conceptuales"
                ],
                "ejemplos": [
                    "Presenta un unico grafico sin etiquetas para todo el analisis",
                    "Interpreta incorrectamente una tendencia negativa como positiva"
                ]
            }
        }
    },

    "SCD0303": {
        "nombre": "Insights y Lineas de Accion",
        "descripcion": "Propone lineas de accion con base en insights que identifica a traves de herramientas de analitica de negocios.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Extrae al menos 3 insights especificos y no triviales de los datos; cada insight conecta un hallazgo estadistico con su significado practico",
                    "Usa herramientas de analisis avanzadas (regresion, segmentacion, analisis multivariado) de forma pertinente al problema",
                    "Identifica al menos 1 riesgo y 1 oportunidad concretos, cuantificados o respaldados con evidencia del dataset",
                    "Propone lineas de accion estrategicas que son especificas, factibles y vinculadas directamente a los insights identificados"
                ],
                "ejemplos": [
                    "Insight: 'Los pacientes de 0-5 anios muestran 23% mas satisfaccion que los de 13-18; la regresion sugiere que la edad predice negativamente la satisfaccion (beta=-0.31, p<0.05)'",
                    "Linea de accion: 'Disenar un programa piloto de atencion diferenciada para adolescentes (13-18) con actividades adaptadas a su etapa de desarrollo, dado que este grupo muestra la menor satisfaccion'"
                ]
            },
            "Solido": {
                "puntos": 88,
                "criterios": [
                    "Extrae al menos 2 insights relevantes de los datos con conexion al contexto del problema",
                    "Usa herramientas de analisis apropiadas para el estudio (pruebas de hipotesis, estadistica descriptiva avanzada)",
                    "Identifica riesgos u oportunidades relevantes aunque no todos esten cuantificados",
                    "Propone lineas de accion coherentes con los hallazgos aunque les falta especificidad en implementacion"
                ],
                "ejemplos": [
                    "Insight correcto pero general: 'Los adolescentes estan menos satisfechos que los ninos'",
                    "Linea de accion: 'Mejorar la atencion a adolescentes' (correcta pero sin especificar como)"
                ]
            },
            "Basico": {
                "puntos": 75,
                "criterios": [
                    "Extrae 1-2 insights basicos que restatan lo obvio de los datos sin profundizar en el significado",
                    "Usa herramientas basicas (solo estadistica descriptiva simple) cuando el problema requeria analisis mas profundo",
                    "Identifica pocos riesgos u oportunidades, o estos son genericos y no estan vinculados a los datos",
                    "Las lineas de accion son vagas o genericas, no se derivan claramente de los hallazgos"
                ],
                "ejemplos": [
                    "Insight trivial: 'La media de satisfaccion es 7.2' sin explicar que implica",
                    "Linea de accion generica: 'Mejorar los servicios' sin especificar cuales ni por que"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "No identifica insights claros o los confunde con datos crudos (ej: reporta un numero sin interpretarlo)",
                    "Usa las herramientas de analisis de forma incorrecta o no usa ninguna",
                    "No identifica riesgos ni oportunidades, o los identificados son irrelevantes al contexto",
                    "Las lineas de accion no tienen relacion con los datos o son inviables"
                ],
                "ejemplos": [
                    "Presenta una tabla de estadisticas descriptivas sin ningun insight derivado",
                    "Propone 'hacer mas encuestas' como unica linea de accion sin basarse en hallazgos"
                ]
            }
        }
    },

    "SEGE201": {
        "nombre": "Innovacion",
        "descripcion": "Genera soluciones innovadoras y de valor ante las problematicas del entorno, a traves de un proceso sistematico que incorpore la validacion y el aprendizaje en situaciones positivas y adversas.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Propone al menos una solucion que combina tecnicas o enfoques de forma original y no evidente a partir de los datos analizados",
                    "Valida la solucion propuesta con evidencia del dataset (ej: muestra que el segmento objetivo existe y tiene el problema identificado)",
                    "Demuestra que la solucion es aplicable al contexto del socio formador con argumentos concretos de viabilidad"
                ],
                "ejemplos": [
                    "Propone un sistema de alerta temprana basado en las variables que predicen baja satisfaccion, validado con el modelo de regresion construido",
                    "Argumenta viabilidad: 'El modelo identifica correctamente al 78% de los pacientes en riesgo de abandono usando solo 3 variables que ya se recolectan en la ficha de ingreso'"
                ]
            },
            "Solido": {
                "puntos": 88,
                "criterios": [
                    "Propone una solucion pertinente y fundamentada en los datos aunque no es particularmente original",
                    "Respalda la propuesta con al menos un resultado del analisis como evidencia",
                    "La solucion es aplicable al contexto pero no detalla completamente como implementarla"
                ],
                "ejemplos": [
                    "Propone segmentar pacientes por grupo etario (basado en los datos) pero la estrategia de segmentacion es convencional",
                    "Menciona que el analisis muestra diferencias significativas pero no cuantifica el impacto esperado"
                ]
            },
            "Basico": {
                "puntos": 75,
                "criterios": [
                    "Propone una solucion generica que podria aplicar a cualquier organizacion sin ser especifica al contexto analizado",
                    "La solucion tiene conexion debil con los datos: se menciona el analisis pero no se usa como fundamento directo",
                    "No evalua la viabilidad de la propuesta ni considera limitaciones"
                ],
                "ejemplos": [
                    "Propone 'implementar encuestas de satisfaccion periodicas' sin vincular a hallazgos especificos del analisis",
                    "La solucion podria haberse propuesto sin hacer ningun analisis de datos"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "No propone una solucion clara, o la propuesta no tiene relacion con los datos analizados",
                    "No presenta evidencia ni validacion de ninguna propuesta",
                    "La propuesta es inviable o no considera el contexto del socio formador"
                ],
                "ejemplos": [
                    "Propone 'usar inteligencia artificial' sin especificar para que ni como se conecta con el analisis realizado",
                    "No presenta ninguna propuesta de solucion, solo describe los datos"
                ]
            }
        }
    },

    "SEGE203": {
        "nombre": "Trabajo Colaborativo",
        "descripcion": "Genera resultados y compromisos en los grupos donde participa, por medio del trabajo colaborativo, la toma de decisiones y la generacion de valor.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "El entregable muestra integracion coherente de contribuciones de multiples integrantes (secciones complementarias, no repetitivas)",
                    "Se evidencian decisiones tomadas en equipo: el documento explica por que se eligieron ciertos enfoques sobre otros",
                    "Cada integrante contribuye con un rol o seccion distinguible y el resultado final es mayor que la suma de las partes",
                    "Los objetivos planteados en el proyecto se cumplen en su totalidad con evidencia medible"
                ],
                "ejemplos": [
                    "El informe divide claramente quien analizo estadistica descriptiva, quien graficos y quien insights, pero las conclusiones integran los tres analisis en una narrativa coherente",
                    "Incluyen seccion de 'Decisiones del equipo' donde explican: 'Elegimos enfocarnos en satisfaccion por grupo etario porque el ANOVA mostro diferencias significativas (F=4.2, p=0.02)'"
                ]
            },
            "Solido": {
                "puntos": 88,
                "criterios": [
                    "El entregable muestra contribuciones de varios integrantes pero la integracion tiene algunas inconsistencias de estilo o formato",
                    "Se observan decisiones conjuntas aunque no todas estan explicitamente justificadas",
                    "La mayoria de los integrantes contribuye de forma distinguible; el resultado es coherente",
                    "Los objetivos se cumplen en su mayoria con evidencia clara"
                ],
                "ejemplos": [
                    "El trabajo tiene secciones bien hechas pero el tono cambia notablemente entre secciones (falta edicion conjunta)",
                    "Cumplen los objetivos de analisis pero la conclusion final no integra todos los hallazgos"
                ]
            },
            "Basico": {
                "puntos": 75,
                "criterios": [
                    "El entregable parece fragmentado: secciones desconectadas que se concatenaron sin integracion",
                    "No hay evidencia de decisiones tomadas en equipo; el trabajo parece dividido sin coordinacion",
                    "Algunos integrantes no tienen contribucion visible o sus aportes son repetitivos",
                    "Los objetivos se cumplen parcialmente"
                ],
                "ejemplos": [
                    "Cada integrante analizo una variable diferente pero no hay conclusion que integre los hallazgos",
                    "Las secciones usan formatos y librerias inconsistentes (uno usa matplotlib, otro Plotly, sin justificacion)"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "El entregable evidencia trabajo individual, no colaborativo: una sola persona parece haber hecho todo",
                    "No hay evidencia de coordinacion, toma de decisiones conjunta ni division de trabajo",
                    "Los aportes individuales no son distinguibles o la mayoria del equipo no contribuyo",
                    "Los objetivos del proyecto no se cumplen o se cumplen de forma muy parcial"
                ],
                "ejemplos": [
                    "El notebook tiene un unico estilo de codigo y comentarios, sugiriendo un solo autor",
                    "No se entrega el trabajo o el entregable esta incompleto (falta mas del 50% de lo solicitado)"
                ]
            }
        }
    },

    "SEGE401": {
        "nombre": "Etica y Responsabilidad Social",
        "descripcion": "Respeta la dignidad, derechos, contribuciones, circunstancias personales y de los demas, procurando presentar soluciones constructivas y solidarias ante situaciones ajenas.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Propone soluciones que priorizan el bienestar de los beneficiarios del socio formador, no solo la eficiencia operativa",
                    "Identifica y discute implicaciones eticas del manejo de datos (privacidad, sesgo, representatividad de la muestra)",
                    "Demuestra sensibilidad al contexto social: adapta recomendaciones considerando las circunstancias de la poblacion atendida",
                    "Reconoce explicitamente las contribuciones de los demas (companeros, socio formador, fuentes de datos)"
                ],
                "ejemplos": [
                    "Discute: 'Los datos de satisfaccion podrian estar sesgados porque los pacientes con discapacidades mas severas tienen menor tasa de respuesta; nuestras conclusiones podrian no representar a toda la poblacion'",
                    "Propone: 'Antes de segmentar por diagnostico, debemos considerar si etiquetar a los pacientes podria generar estigma; sugerimos usar categorias amplias aprobadas por el equipo clinico'"
                ]
            },
            "Solido": {
                "puntos": 88,
                "criterios": [
                    "Las soluciones propuestas consideran el impacto en los beneficiarios aunque no es el foco principal del analisis",
                    "Menciona al menos una consideracion etica relevante (privacidad, sesgo) aunque no profundiza",
                    "Muestra respeto por el contexto social en el tono y las recomendaciones del documento",
                    "Reconoce las contribuciones del equipo y del socio formador en el documento"
                ],
                "ejemplos": [
                    "Menciona: 'Es importante proteger la identidad de los pacientes en los reportes' pero no detalla como",
                    "Las recomendaciones son respetuosas pero no discuten explicitamente posibles impactos negativos"
                ]
            },
            "Basico": {
                "puntos": 75,
                "criterios": [
                    "Las soluciones se enfocan en resultados tecnicos sin considerar explicitamente el impacto humano",
                    "No menciona consideraciones eticas sobre el manejo de datos aunque el analisis es correcto",
                    "El tono del documento es profesional pero no demuestra sensibilidad especial hacia la poblacion atendida",
                    "Las contribuciones del equipo se mencionan de forma minima"
                ],
                "ejemplos": [
                    "Analiza datos de pacientes como 'registros' sin reconocer que representan personas con necesidades especificas",
                    "No cuestiona la representatividad de la muestra ni menciona limitaciones eticas"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "Las soluciones ignoran o contradicen el bienestar de los beneficiarios",
                    "No hay ninguna consideracion etica en el manejo de datos; usa datos sensibles sin precaucion",
                    "El tono del documento es insensible o inapropiado para el contexto de la poblacion atendida",
                    "No reconoce contribuciones de los demas o se apropia del trabajo ajeno"
                ],
                "ejemplos": [
                    "Publica nombres o datos identificables de pacientes en graficos o tablas",
                    "Propone reducir servicios a grupos 'poco rentables' sin considerar su vulnerabilidad"
                ]
            }
        }
    }
}


def get_rubric_prompt(codigo: str) -> str:
    """Genera el prompt de evaluacion para una subcompetencia especifica."""
    rubrica = RUBRICAS[codigo]

    prompt = f"""Eres un evaluador academico del Tecnologico de Monterrey.

## Subcompetencia a Evaluar: {codigo} - {rubrica['nombre']}
{rubrica['descripcion']}

## Escala de Evaluacion (usa EXACTAMENTE estos niveles y puntos):
- Destacado (100 puntos): Desempeno optimo
- Solido (88 puntos): Desempeno apropiado
- Basico (75 puntos): Desempeno aceptable
- Incipiente (55 puntos): Desempeno deficiente
- Sin evidencia (0 puntos): No hay evidencia de la subcompetencia

## Criterios por Nivel:

"""
    for nivel, data in rubrica['niveles'].items():
        prompt += f"### {nivel} ({data['puntos']} pts):\n"
        for criterio in data['criterios']:
            prompt += f"- {criterio}\n"
        if 'ejemplos' in data:
            prompt += f"\nEjemplos de referencia:\n"
            for ejemplo in data['ejemplos']:
                prompt += f"  > {ejemplo}\n"
        prompt += "\n"

    prompt += """## Instrucciones:
1. Lee cuidadosamente el trabajo del estudiante
2. Identifica evidencias especificas relacionadas con esta subcompetencia
3. Compara las evidencias con los criterios de cada nivel
4. Asigna el nivel que mejor corresponda segun las evidencias encontradas
5. Se justo pero no demasiado estricto - busca lo positivo primero

## IMPORTANTE - Formato de Respuesta:
Responde UNICAMENTE con un JSON valido (sin markdown, sin ```json):
{"nivel": "Destacado|Solido|Basico|Incipiente|Sin evidencia", "puntos": 100|88|75|55|0, "evidencias": ["evidencia 1", "evidencia 2"], "fortalezas": ["fortaleza 1"], "areas_mejora": ["area 1"], "retroalimentacion": "texto breve"}
"""
    return prompt


def get_all_prompts() -> dict:
    """Retorna todos los prompts de evaluacion."""
    return {codigo: get_rubric_prompt(codigo) for codigo in RUBRICAS.keys()}


def calcular_nota_final(evaluaciones: dict) -> tuple:
    """
    Calcula la nota final ponderada.

    Args:
        evaluaciones: dict con {codigo_subcompetencia: puntos}

    Returns:
        tuple: (nota_final, nivel_final)
    """
    total = 0
    for codigo, puntos in evaluaciones.items():
        peso = PONDERACIONES.get(codigo, 0)
        total += puntos * peso

    nota_final = round(total, 1)

    # Determinar nivel final
    if nota_final >= 95:
        nivel = "Destacado"
    elif nota_final >= 81:
        nivel = "Solido"
    elif nota_final >= 70:
        nivel = "Basico"
    elif nota_final > 0:
        nivel = "Incipiente"
    else:
        nivel = "Sin evidencia"

    return nota_final, nivel


if __name__ == "__main__":
    # Test
    print("Rubricas cargadas:")
    for codigo, rubrica in RUBRICAS.items():
        print(f"  - {codigo}: {rubrica['nombre']} (peso: {PONDERACIONES[codigo]*100}%)")
        for nivel, data in rubrica['niveles'].items():
            n_criterios = len(data['criterios'])
            n_ejemplos = len(data.get('ejemplos', []))
            print(f"      {nivel}: {n_criterios} criterios, {n_ejemplos} ejemplos")

    print("\nEjemplo de calculo de nota final:")
    ejemplo = {
        "SCD0104": 88,
        "SCD0105": 100,
        "SCD0303": 88,
        "SEGE201": 75,
        "SEGE203": 88,
        "SEGE401": 100
    }
    nota, nivel = calcular_nota_final(ejemplo)
    print(f"  Evaluaciones: {ejemplo}")
    print(f"  Nota final: {nota} - {nivel}")
