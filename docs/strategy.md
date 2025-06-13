# Estrategia de Pruebas para LLMs

Este documento resume un enfoque básico de validación manual y automatizada para modelos de lenguaje de gran tamaño.

## Riesgos
- **Alucinaciones**: el modelo puede inventar datos.
- **Sesgos**: respuestas que reflejan prejuicios en el dataset de entrenamiento.
- **Prompt Injection**: usuarios malintencionados pueden alterar el comportamiento del modelo.

## Checklist de QA manual
- [ ] La respuesta es coherente con el prompt.
- [ ] Se mantiene el tono solicitado.
- [ ] No hay datos inventados detectables.

## Automatización
Utilizamos `pytest` para ejecutar casos de prueba que comprueben la estructura y formato de las respuestas. Las funciones en `llmqa.evaluator` son un punto de partida y pueden extenderse con reglas de validación más complejas.
