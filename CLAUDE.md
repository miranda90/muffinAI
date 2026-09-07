# muffinAI — Taller de maquetación BeBuilder

Taller centralizado: aquí se genera y valida el JSON de BeBuilder para TODOS los proyectos
WordPress de Invbit. Este repo no es un proyecto de cliente; los sitios viven en sus
servidores y aquí solo se fabrica y comprueba lo que luego se importa.

## Estructura

- `proyectos/<cliente>/` — un encargo por carpeta: `build_<pagina>.py`, JSON generados,
  `assets/` (medios del diseño + `manifest.json` con el `id`/`url` de cada uno en el WordPress
  destino) e `icons/`. **Todo lo nuevo nace aquí, nunca en la raíz.**
- `proyectos/_plantilla/build_plantilla.py` — punto de partida de cualquier página nueva.
- `tools/mfn.py` — helpers comunes (uid, css, typo, pad, section, wrap, nested, item,
  selectores base, `load_manifest`/`media` para medios como `URL#ID`). Los scripts previos a
  la librería llevan los helpers duplicados dentro: congelados a propósito, no migrarlos.
- `tools/validate_bebuilder_json.py` — validador contra el catálogo real del theme. Uso en
  `tools/README.md`.
- `skills/bebuilder-json/SKILL.md` — la skill: flujo de generación, reglas
  innegociables, trampas. **Leerla antes de generar cualquier JSON.**
- `docs/bebuilder/` — documentación maestra (arquitectura, CSS pipeline, elementos, global
  styles, iconos, tipografía, **medios: imágenes y vídeo — doc 09**). `docs/legacy/` es historia,
  no referencia.
- `builder-elements/` — 176 fichas de elementos regeneradas ejecutando el PHP real, más
  `GUIA-MAQUETACIONES.md` (patrones de layout).
- `betheme/` — copia del theme como fuente de verdad para leer código. No se edita.
- `examples/` — exports reales del VB, sirven para calibrar el validador.

## Flujo de un encargo

1. `mkdir proyectos/<cliente>` si no existe; copiar la plantilla como `build_<pagina>.py`.
2. **Medios** (doc 09): inventariar en Figma todas las imágenes, logos, iconos y vídeos;
   descargarlos a `proyectos/<cliente>/assets/` con nombre descriptivo; subirlos al WordPress
   destino (`wp media import` por SSH o REST); dejar `assets/manifest.json` con `id` + `url`.
   Vídeo: `export_video` si es un timeline de Figma; si es un *video fill*, pedir el `.mp4` al
   cliente (la API no lo entrega) y optimizarlo con `ffmpeg` antes de subir. Tokens del diseño
   al script.
3. Generar: `python3 proyectos/<cliente>/build_<pagina>.py` (el JSON se escribe solo,
   junto al script). Todo medio va como `media(MAN, "fichero")` → `URL#ID`; nunca URLs de
   Figma, `localhost` ni inventadas.
4. Validar desde la raíz: `python3 tools/validate_bebuilder_json.py proyectos/<cliente>/x.json --strict`
   e iterar hasta exit 0. Warnings solo si son decisión consciente y explicada.
5. Entregar: import por el panel Export/Import del VB del sitio destino y **guardar una vez
   en el VB** para que se genere el CSS local (trampas 6 y 17).

## Reglas del taller

- Ningún script escribe en el CWD: salida siempre `HERE / "nombre.json"`.
- Ningún JSON se entrega sin validar. Sin excepciones.
- Ningún JSON se entrega con medios fuera de la Media Library del destino: cada `src`,
  `bg_video_mp4`, `mp4`, `placeholder` y fondo lleva `URL#ID` del manifest. Un medio que no se ha
  conseguido (vídeo sin fichero, foto en baja) se lista como pendiente en la entrega.
- Los scripts de encargos entregados no se tocan: si se rehace una página, script nuevo.
- Tras actualizar `betheme/`, regenerar catálogo y fichas:
  `cd builder-elements/_generator && php extract.php && python3 generate_fichas.py`.

## Verificación rápida del entorno

```bash
python3 tools/validate_bebuilder_json.py examples/example2/home.json --origin export --json  # calibrado
python3 tools/check.py                                                        # todo el taller
python3 proyectos/_plantilla/build_plantilla.py                              # librería viva
```

## Flujo actualizado para scripts nuevos

Leer `docs/bebuilder/10-flujo-verificable.md`. Usar `build(context)` y `tools/build.py`;
`--check` construye/valida sin publicar, y la salida normal añade informe/mapa/perfil.
No ejecutar scripts históricos con el nuevo runner. `python3 tools/check.py` comprueba
regresiones, catálogo, fichas y plantilla. `accepted` es la condición de entrega local;
WordPress y fidelidad visual permanecen pendientes hasta ejecutarlos realmente.

## Distribución como plugin de Claude Code

El repositorio **es** el plugin (`.claude-plugin/plugin.json` con `source: "./"` en
`.claude-plugin/marketplace.json`). La skill vive en `skills/bebuilder-json/`, con un enlace
desde `.claude/skills/` para las sesiones abiertas dentro del propio taller. Los comandos
`/bebuilder:encargo`, `/bebuilder:build`, `/bebuilder:validar` y `/bebuilder:check` están en
`commands/` y resuelven la raíz del taller con `${CLAUDE_PLUGIN_ROOT}`. Instalación y uso sin
Claude Code: `INSTALL.md`; contexto de arranque para otros modelos: `AGENTS.md`.
