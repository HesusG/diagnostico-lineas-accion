#!/usr/bin/env python3
"""
Definición de las 6 rúbricas oficiales para el sistema de evaluación.
Basado en las subcompetencias del Tecnológico de Monterrey.
"""

NIVELES = {
    "Destacado": 100,
    "Sólido": 88,
    "Básico": 75,
    "Incipiente": 55,
    "Sin evidencia": 0
}

PONDERACIONES = {
    "SCD0104": 0.20,  # Estadística Descriptiva
    "SCD0105": 0.20,  # Gráficos Dinámicos
    "SCD0303": 0.25,  # Insights y Líneas de Acción
    "SEGE201": 0.15,  # Innovación
    "SEGE203": 0.10,  # Trabajo Colaborativo
    "SEGE401": 0.10,  # Ética y Responsabilidad Social
}

RUBRICAS = {
    "SCD0104": {
        "nombre": "Estadística Descriptiva",
        "descripcion": "Resume la información mediante herramientas de estadística descriptiva utilizando soluciones tecnológicas actuales.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Identifica en su totalidad las variables esenciales en la información",
                    "Utiliza herramientas tecnológicas y resume de manera apropiada la información mediante tablas de frecuencia y estadísticas descriptivas",
                    "Muestra de manera atractiva la información relevante contenida en las variables",
                    "Interpreta de manera coherente los resultados de los gráficos y análisis descriptivos en el contexto de la problemática planteada"
                ]
            },
            "Sólido": {
                "puntos": 88,
                "criterios": [
                    "Identifica en su totalidad las variables esenciales en la información",
                    "Utiliza herramientas tecnológicas y resume de manera adecuada la información mediante tablas de frecuencia y estadísticas descriptivas",
                    "Muestra de manera adecuada la información relevante contenida en las variables",
                    "Interpreta de manera articulada los resultados de los gráficos y análisis descriptivos en el contexto de la problemática planteada"
                ]
            },
            "Básico": {
                "puntos": 75,
                "criterios": [
                    "Identifica de manera parcial las variables esenciales en la información",
                    "Utiliza herramientas tecnológicas y resume de manera aceptable la información mediante tablas de frecuencia y estadísticas descriptivas",
                    "Muestra de manera adecuada la información relevante contenida en las variables",
                    "Interpreta de manera básica los resultados de los gráficos y análisis descriptivos en el contexto de la problemática planteada"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "Identifica de forma incompleta las variables esenciales en la información",
                    "Utiliza herramientas tecnológicas y resume de manera inapropiada la información mediante tablas de frecuencia y estadísticas descriptivas",
                    "Muestra de manera deficiente la información relevante contenida en las variables",
                    "Deriva interpretaciones insuficientes de los gráficos y análisis descriptivos en el contexto de la problemática planteada"
                ]
            }
        }
    },

    "SCD0105": {
        "nombre": "Gráficos Dinámicos",
        "descripcion": "Genera gráficos dinámicos acordes a la naturaleza de las variables, asegurándose que muestran información relevante para la toma de decisiones haciendo uso de soluciones tecnológicas actuales.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Elabora gráficos dinámicos claros y atractivos",
                    "Identifica de forma precisa los niveles de medición de las variables",
                    "La selección del tipo de gráfico es congruente a los respectivos niveles de medición",
                    "Interpreta de manera clara y efectiva la información que muestran"
                ]
            },
            "Sólido": {
                "puntos": 88,
                "criterios": [
                    "Elabora gráficos dinámicos adecuados",
                    "Identifica con precisión los niveles de medición de las variables",
                    "Selecciona el tipo de gráfico apropiado",
                    "Interpreta de manera congruente la información que muestran"
                ]
            },
            "Básico": {
                "puntos": 75,
                "criterios": [
                    "Elabora gráficos dinámicos aceptables",
                    "Identifica de forma parcial los niveles de medición de las variables",
                    "La selección del tipo de gráfico es parcialmente apropiada",
                    "Interpreta de manera limitada la información que muestran"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "Elabora gráficos dinámicos insuficientes",
                    "Identifica de manera confusa los niveles de medición de las variables",
                    "Selecciona un tipo de gráfico inapropiado a los niveles de medición",
                    "Interpreta de manera incorrecta la información que muestran"
                ]
            }
        }
    },

    "SCD0303": {
        "nombre": "Insights y Líneas de Acción",
        "descripcion": "Propone líneas de acción con base en insights que identifica a través de herramientas de analítica de negocios.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Interpreta de manera efectiva los insights de los tableros inteligentes o en el seguimiento de los indicadores del plan estratégico",
                    "Hace uso de herramientas de análisis pertinentes para el estudio",
                    "Identifica posibles riesgos u oportunidades relevantes para el negocio",
                    "Propone de manera acertada líneas de acción estratégicas"
                ]
            },
            "Sólido": {
                "puntos": 88,
                "criterios": [
                    "Interpreta de manera adecuada los insights de los tableros inteligentes o en el seguimiento de los indicadores",
                    "Hace uso de herramientas de análisis apropiadas para el estudio",
                    "Identifica posibles riesgos u oportunidades relevantes para el negocio",
                    "Propone de manera aceptable líneas de acción estratégicas"
                ]
            },
            "Básico": {
                "puntos": 75,
                "criterios": [
                    "Interpreta de manera aceptable algunos insights de los tableros inteligentes o en el seguimiento de los indicadores",
                    "Hace uso de herramientas convencionales",
                    "Identifica pocos riesgos u oportunidades relevantes",
                    "Propone líneas de acción parciales"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "Interpreta de manera limitada los insights",
                    "Hace uso deficiente de las herramientas de análisis",
                    "Identifica riesgos u oportunidades poco relevantes",
                    "Propone líneas de acción inadecuadas o insuficientes"
                ]
            }
        }
    },

    "SEGE201": {
        "nombre": "Innovación",
        "descripcion": "Genera soluciones innovadoras y de valor ante las problemáticas del entorno, a través de un proceso sistemático que incorpore la validación y el aprendizaje en situaciones positivas y adversas.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Genera de manera óptima soluciones innovadoras",
                    "Presenta prototipos validados en sus características",
                    "Garantiza aplicabilidad efectiva en uno o más contextos solicitados en la unidad de formación"
                ]
            },
            "Sólido": {
                "puntos": 88,
                "criterios": [
                    "Genera de manera apropiada prototipos de soluciones innovadoras",
                    "Valida las características de los prototipos",
                    "Garantiza aplicabilidad efectiva en uno o más contextos solicitados"
                ]
            },
            "Básico": {
                "puntos": 75,
                "criterios": [
                    "Genera de manera limitada prototipos de soluciones innovadoras",
                    "Valida de modo suficiente las características",
                    "Garantiza aplicación aceptable en uno o más contextos solicitados"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "Genera de manera insuficiente soluciones",
                    "No valida las características de las soluciones",
                    "Limita la aplicabilidad en uno o más contextos solicitados en la unidad de formación"
                ]
            }
        }
    },

    "SEGE203": {
        "nombre": "Trabajo Colaborativo",
        "descripcion": "Genera resultados y compromisos en los grupos donde participa, por medio del trabajo colaborativo, la toma de decisiones y la generación de valor.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Genera de manera óptima resultados derivados de un trabajo colaborativo idóneo",
                    "Establece de forma estratégica compromisos, propuestas o acciones integrales",
                    "Da cuenta del cumplimiento eficaz de una o más funciones o tareas de negociación con otras personas",
                    "Logra consistentemente los objetivos planteados"
                ]
            },
            "Sólido": {
                "puntos": 88,
                "criterios": [
                    "Genera de manera concreta resultados derivados de un trabajo colaborativo adecuado",
                    "Establece compromisos, propuestas o acciones adecuadas",
                    "Da cuenta del cumplimiento eficaz de una o más funciones o tareas de negociación con otras personas",
                    "Logra de manera consistente los objetivos planteados"
                ]
            },
            "Básico": {
                "puntos": 75,
                "criterios": [
                    "Genera de manera aceptable resultados derivados de un trabajo colaborativo",
                    "Cumple con una o más funciones o tareas de negociación con otras personas",
                    "Logra parcialmente los objetivos planteados"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "Genera de manera incompleta resultados derivados de un trabajo colaborativo inadecuado o insuficiente",
                    "Omite compromisos, propuestas o acciones",
                    "No logra el cumplimiento de una o más funciones o tareas de negociación con otras personas",
                    "No logra consistentemente los objetivos planteados"
                ]
            }
        }
    },

    "SEGE401": {
        "nombre": "Ética y Responsabilidad Social",
        "descripcion": "Respeta la dignidad, derechos, contribuciones, circunstancias personales y de los demás, procurando presentar soluciones constructivas y solidarias ante situaciones ajenas.",
        "niveles": {
            "Destacado": {
                "puntos": 100,
                "criterios": [
                    "Genera de manera articulada soluciones constructivas y solidarias ante situaciones ajenas",
                    "Demuestra sensibilidad social",
                    "Demuestra compromiso comunitario",
                    "Demuestra respeto a la dignidad de las personas"
                ]
            },
            "Sólido": {
                "puntos": 88,
                "criterios": [
                    "Genera de manera apropiada soluciones constructivas y solidarias ante situaciones ajenas",
                    "Demuestra sensibilidad social",
                    "Demuestra compromiso comunitario",
                    "Demuestra respeto a la dignidad de las personas"
                ]
            },
            "Básico": {
                "puntos": 75,
                "criterios": [
                    "Genera de manera aceptable soluciones solidarias",
                    "Demuestra integridad personal",
                    "Demuestra compromiso comunitario",
                    "Demuestra respeto por la dignidad de las personas"
                ]
            },
            "Incipiente": {
                "puntos": 55,
                "criterios": [
                    "Genera de manera inapropiada soluciones que no son constructivas ni solidarias ante situaciones ajenas",
                    "Carece de sensibilidad social",
                    "Carece de respeto por la dignidad, contribuciones y circunstancias de otras personas"
                ]
            }
        }
    }
}


def get_rubric_prompt(codigo: str) -> str:
    """Genera el prompt de evaluación para una subcompetencia específica."""
    rubrica = RUBRICAS[codigo]

    prompt = f"""Eres un evaluador académico del Tecnológico de Monterrey.

## Subcompetencia a Evaluar: {codigo} - {rubrica['nombre']}
{rubrica['descripcion']}

## Escala de Evaluación (usa EXACTAMENTE estos niveles y puntos):
- Destacado (100 puntos): Desempeño óptimo
- Sólido (88 puntos): Desempeño apropiado
- Básico (75 puntos): Desempeño aceptable
- Incipiente (55 puntos): Desempeño deficiente
- Sin evidencia (0 puntos): No hay evidencia de la subcompetencia

## Criterios por Nivel:

"""
    for nivel, data in rubrica['niveles'].items():
        prompt += f"### {nivel} ({data['puntos']} pts):\n"
        for criterio in data['criterios']:
            prompt += f"- {criterio}\n"
        prompt += "\n"

    prompt += """## Instrucciones:
1. Lee cuidadosamente el trabajo del estudiante
2. Identifica evidencias específicas relacionadas con esta subcompetencia
3. Compara las evidencias con los criterios de cada nivel
4. Asigna el nivel que mejor corresponda según las evidencias encontradas
5. Sé justo pero no demasiado estricto - busca lo positivo primero

## IMPORTANTE - Formato de Respuesta:
Responde ÚNICAMENTE con un JSON válido (sin markdown, sin ```json):
{"nivel": "Destacado|Sólido|Básico|Incipiente|Sin evidencia", "puntos": 100|88|75|55|0, "evidencias": ["evidencia 1", "evidencia 2"], "fortalezas": ["fortaleza 1"], "areas_mejora": ["area 1"], "retroalimentacion": "texto breve"}
"""
    return prompt


def get_all_prompts() -> dict:
    """Retorna todos los prompts de evaluación."""
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
        nivel = "Sólido"
    elif nota_final >= 70:
        nivel = "Básico"
    elif nota_final > 0:
        nivel = "Incipiente"
    else:
        nivel = "Sin evidencia"

    return nota_final, nivel


if __name__ == "__main__":
    # Test
    print("Rúbricas cargadas:")
    for codigo, rubrica in RUBRICAS.items():
        print(f"  - {codigo}: {rubrica['nombre']} (peso: {PONDERACIONES[codigo]*100}%)")

    print("\nEjemplo de cálculo de nota final:")
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
