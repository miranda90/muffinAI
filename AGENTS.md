# Contexto de arranque para asistentes de IA

Este repositorio es el taller de maquetación BeBuilder de Invbit. Léelo en este orden:

1. `CLAUDE.md` — qué es el taller, estructura, flujo de un encargo y reglas innegociables.
2. `skills/bebuilder-json/SKILL.md` — cómo se genera y valida el JSON, con las trampas.
3. `docs/bebuilder/10-flujo-verificable.md` — flujo vigente para scripts nuevos.
4. `docs/bebuilder/00-INDICE.md` — el resto de la documentación maestra.

Reglas que no dependen del asistente:

- Ningún script escribe en el directorio actual: la salida va junto al script.
- Ningún JSON se entrega sin pasar el validador (`tools/validate_bebuilder_json.py --strict`).
- Ningún medio fuera de la Media Library del destino: todo va como `URL#ID` del manifest.
- Los scripts de encargos ya entregados están congelados; si se rehace una página, script nuevo.

Con Claude Code, este repo se instala además como plugin: ver `INSTALL.md`.
