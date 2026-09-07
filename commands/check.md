---
description: Comprueba el taller completo (regresiones, catálogo, fichas, plantilla)
allowed-tools: Bash, Read
---

```bash
cd "${CLAUDE_PLUGIN_ROOT}" && python3 tools/check.py
```

Comprueba sintaxis de todos los scripts, el catálogo, las fichas de elementos y que la
plantilla sigue viva. Ejecútalo tras tocar `tools/`, `builder-elements/` o `betheme/`.
Si `betheme/` ha cambiado, regenera antes catálogo y fichas:

```bash
cd "${CLAUDE_PLUGIN_ROOT}/builder-elements/_generator" && php extract.php && python3 generate_fichas.py
```
