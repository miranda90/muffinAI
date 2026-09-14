---
description: Arranca un encargo nuevo de maquetación BeBuilder (carpeta, plantilla, inventario de medios)
argument-hint: <cliente> <pagina>
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

Arranca el encargo `$1` / página `$2` en el taller BeBuilder.

Raíz del taller: `${CLAUDE_PLUGIN_ROOT}`. Todo el trabajo ocurre ahí, no en el
directorio actual del usuario.

1. Lee `${CLAUDE_PLUGIN_ROOT}/skills/bebuilder-json/SKILL.md` y
   `${CLAUDE_PLUGIN_ROOT}/docs/bebuilder/10-flujo-verificable.md` antes de escribir nada.
2. Crea `${CLAUDE_PLUGIN_ROOT}/proyectos/$1/` si no existe y copia
   `proyectos/_plantilla/build_plantilla.py` como `proyectos/$1/build_$2.py`.
3. Medios (doc 09): inventaria imágenes, logos, iconos y vídeos del diseño; descárgalos a
   `proyectos/$1/assets/`; súbelos al WordPress destino; deja `assets/manifest.json` con
   `id` y `url`. Ningún medio inventado, ningún `localhost`, ninguna URL de Figma.
4. Pregunta al usuario lo que falte (URL del diseño, acceso al WordPress destino, tokens de
   color/tipografía) en vez de suponerlo.
5. Maqueta con la API compacta (`el`/`wr`/`nw`/`sec`, ver SKILL §2); campos de cada tipo con
   `python3 tools/fields.py <tipo>`.
6. Termina con `/bebuilder:build proyectos/$1/build_$2.py` para el primer `--check`.
