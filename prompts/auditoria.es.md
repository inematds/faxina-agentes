# Prompt de auditoría (pégalo en Claude Code o Codex)

Úsalo en una terminal abierta en la carpeta donde trabajas. El agente solo **lee** y **propone**: no se borra nada sin tu aprobación.

```text
Uso Claude Code y Codex. Haz una auditoría de mi configuración en ambos.

QUÉ AUDITAR
- archivos de instrucciones: CLAUDE.md, AGENTS.md, GEMINI.md y similares (globales y por proyecto)
- skills, reglas, memoria, configuraciones (settings), hooks, plugins, MCP y herramientas conectadas
- agentes y subagentes, tareas programadas y cada proyecto que funciona como un sistema propio

CON QUÉ COMPARARLO
- mi uso real: ejecuta `python3 scripts/varrer_historico.py --dias 60` (o escribe un script similar)
  para contar señales de fricción en mis mensajes y las skills/herramientas que nunca he invocado.
  No leas las conversaciones completas: usa el script.

CON QUÉ CRITERIO
Para cada elemento, indica:
1. qué funciona y debe quedarse;
2. qué es peso muerto (no se usa, es antiguo o está duplicado) y puede eliminarse;
3. qué hace falta;
4. qué reglas se contradicen o existen en uno y no en el otro (Claude × Codex);
5. qué configuración, automatización o proyecto me está estorbando en vez de ayudarme.

CÓMO ENTREGARLO
- una página HTML para leer en el navegador, con una puntuación de 0 a 10 por área,
  los 10 cambios más importantes y, para cada uno, la evidencia (archivo y línea) y el riesgo;
- separa «bajo riesgo, puedo hacerlo ahora» de «necesita mi decisión»;
- no cambies nada todavía. Espera mi aprobación.
```

## Después del informe

1. Aprueba solo la lista de **bajo riesgo** (hook obsoleto, archivo temporal, skill sin uso desde hace meses).
2. Lee con calma la lista que requiere una decisión; tacha lo que quieras conservar.
3. Programa la misma auditoría **cada semana** (tarea programada de Codex o `/schedule` en Claude Code),
   con esta regla: limpiar automáticamente solo lo de bajo riesgo; el resto queda en una lista para que decidas.
