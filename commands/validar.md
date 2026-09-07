---
description: Valida un JSON de BeBuilder contra el catálogo real del theme
argument-hint: <ruta/al/pagina.json> [--strict|--fix]
allowed-tools: Bash, Read, Edit
---

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python3 tools/validate_bebuilder_json.py "$1" --strict
```

Salidas: `0` válido · `1` errores · `2` solo warnings con `--strict` · `3` JSON o schema ilegible.

Para un export real del Visual Builder añade `--origin export`. Para arreglar lo mecánico:
`--fix -o salida.ok.json` (no sobrescribe el original y solo publica si `accepted`).

Explica cada issue con su código y arréglalo en el script generador. Un warning solo se deja
pasar si es decisión consciente y la justificas por escrito.
