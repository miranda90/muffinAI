# Instalar el taller BeBuilder en otro equipo

El repositorio **es** el plugin: `git clone` y `/plugin install` entregan lo mismo.
Quien lo instale obtiene documentación, catálogo del theme, validador, plantilla y encargos.

## Con Claude Code (recomendado)

```bash
git clone <url-del-repo> ~/muffinAI      # o la ruta que prefieras
```

Dentro de Claude Code:

```
/plugin marketplace add ~/muffinAI
/plugin install bebuilder@muffinai
```

Desde ese momento, en cualquier proyecto:

- la skill `bebuilder-json` se carga sola al hablar de BeBuilder / Muffin Builder / builder JSON;
- están disponibles `/bebuilder:encargo`, `/bebuilder:build`, `/bebuilder:validar`, `/bebuilder:check`.

Si el repo está publicado en GitHub, `/plugin marketplace add <owner>/<repo>` evita el clone manual.
`/plugin marketplace update muffinai` trae los cambios posteriores.

## Sin plugin, o con otro modelo de IA

El taller funciona igual clonando el repo y trabajando dentro de él: los comandos son Python
puro y no dependen de Claude Code.

```bash
cd ~/muffinAI
python3 tools/check.py                                                   # entorno sano
python3 tools/build.py proyectos/_plantilla/build_plantilla.py --check   # flujo verificable
python3 tools/validate_bebuilder_json.py proyectos/<cliente>/x.json --strict
```

Para otro asistente, dale como contexto de arranque `AGENTS.md` (equivalente a `CLAUDE.md`)
y `skills/bebuilder-json/SKILL.md`.

## Requisitos

- Python 3.9+ (sin dependencias externas).
- PHP solo si se regenera el catálogo desde `betheme/`
  (`builder-elements/_generator/extract.php`).
- Acceso SSH o REST al WordPress destino para subir medios y para el import final.
