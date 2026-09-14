---
description: Construye y valida un script build_*.py del taller (flujo verificable)
argument-hint: <ruta/al/build_pagina.py> [--check]
allowed-tools: Bash, Read, Edit, Glob, Grep
---

Ejecuta el flujo verificable sobre `$1` desde `${CLAUDE_PLUGIN_ROOT}`:

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python3 tools/build.py "$1" --check
```

- `--check` construye y valida sin publicar. Itera hasta `accepted` con exit 0. La salida trae
  solo veredicto e incidencias; `--full` imprime el informe completo.
- Campo desconocido o mal escrito: el error lista parecidos; `python3 tools/fields.py <tipo>`
  muestra los campos del elemento en una línea cada uno.
- Sin `--check` publica el JSON junto al script y añade informe, mapa y perfil.
- Solo para scripts nuevos con `build(context)`. Los scripts históricos están congelados:
  no los pases por este runner.
- Si falla, corrige el script — nunca el JSON generado a mano — y vuelve a lanzarlo.
