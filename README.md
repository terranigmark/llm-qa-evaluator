# LLM QA Evaluator

Este repositorio contiene un conjunto de herramientas para evaluar modelos de lenguaje (LLMs) de forma manual y automatizada. El dominio de ejemplo son las cervezas artesanales y las preguntas se encuentran definidas en formato JSON.

## Estructura del repositorio

```
llm-qa-evaluator/
├── prompts/                 # Preguntas y datos esperados
├── outputs/                 # Respuestas generadas por el modelo
├── evaluation/              # Scripts de validación automática
├── results/                 # Reportes generados
├── llmqa/                   # Utilidades generales
├── tests/                   # Pruebas con pytest
└── docs/                    # Documentación y guías
```

## Contenido principal

1. **Mini-proyectos de Evaluación**
   - Evaluación de respuestas sobre cervezas artesanales.
   - Comparativa básica de modelos mediante prompts comunes.
2. **Framework de Testing**
   - Automatización de validación con `pytest` y scripts de apoyo.
3. **Documentación Profesional**
   - Estrategias de pruebas y checklist de QA manual.

Para más detalles, revisa la carpeta `docs/`.

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

## Evaluación automática de respuestas

El script `evaluation/evaluate_responses.py` compara las respuestas en `outputs/` con los datos esperados en `prompts/` y genera `results/evaluation_report.csv`.

```bash
python evaluation/evaluate_responses.py
```

## Licencia

MIT
