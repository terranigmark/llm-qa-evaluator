# LLM QA Evaluator

Este repositorio contiene un conjunto de herramientas y documentos para evaluar modelos de lenguaje de gran tamaño (LLMs) a través de prompts y pruebas automatizadas. Incluye ejemplos de validación en un dominio específico (cervezas artesanales), una guía para construir un framework de testing con Python y pytest, y materiales de referencia sobre ingeniería de prompts.

## Estructura del repositorio

```
llm-qa-evaluator/
├── llmqa/               # Código de utilidades para la evaluación
├── prompts/             # Colección de prompts de ejemplo
├── tests/               # Pruebas automatizadas con pytest
└── docs/                # Documentación y guías
```

## Contenido principal

1. **Mini-proyectos de Evaluación**
   - *Evaluación de Respuestas de un LLM en el dominio de cervezas artesanales.*
   - *Comparativa de modelos (GPT vs Claude vs Cohere) usando el mismo set de preguntas.*
2. **Framework de Testing**
   - Gestión de prompts con utilidades simples en Python.
   - Automatización de la validación de outputs mediante `pytest`.
3. **Casos de Estudio de Ingeniería de Prompts**
   - Documentación de iteraciones y hallazgos.
4. **Documentación Profesional**
   - Estrategias de pruebas, análisis de riesgos y checklist de QA manual.

Para más detalles, revisa los archivos dentro de la carpeta `docs/`.

## Requisitos

- Python 3.10+
- `pytest` para ejecutar las pruebas automatizadas.

Instala las dependencias de la siguiente manera:

```bash
pip install -r requirements.txt
```

## Ejecución de pruebas

Para ejecutar los tests de ejemplo:

```bash
pytest
```

## Licencia

MIT
