"""Project checks kept separate from BeBuilder's serialization grammar."""
from __future__ import annotations

import re
from urllib.parse import urlsplit

from contracts import public_url, validate_manifest

DYNAMIC = re.compile(r"\{[^{}]+\}")
MEDIA_KEYS = {"src", "image", "mp4", "ogv", "bg_video_mp4", "bg_video_ogv", "placeholder",
              "logo", "decor_top", "decor_bottom"}
DEPENDENCY_KEYS = {"menu": "menus", "form": "forms", "cf7": "forms", "query_post_type": "post_types",
                   "query_terms_taxonomy": "taxonomies", "mfn_global_section_id": "templates"}


def check_project(document, validator):
    profile = validator.o.profile or {}
    manifest = validator.o.manifest
    source = validator.o.origin
    if not isinstance(profile, dict):
        validator.err("E070", "$", "El perfil del proyecto debe ser un objeto.")
        return
    domains = profile.get("media_domains", [])
    if not isinstance(domains, list) or any(not isinstance(x, str) for x in domains):
        validator.err("E070", "$", "media_domains debe ser una lista de dominios.")
        return
    if manifest is not None:
        try:
            validate_manifest(manifest, domains)
        except ValueError as exc:
            validator.err("E070", "$", str(exc))
            return
    media_refs = {"%s#%s" % (x["url"], x["id"]) for x in (manifest or {}).values()}
    known_urls = {x["url"] for x in (manifest or {}).values()}
    ids, links = {}, []

    def media(value, path):
        if not value:
            return
        if not isinstance(value, str):
            validator.err("E071", path, "Medio debe ser string.")
            return
        if DYNAMIC.search(value) and not "{theme_uri}" in value:
            validator.info("I070", path, "Medio dinámico; requiere datos del destino.")
            return
        if value.startswith("url("):
            validator.err("E071", path, "El helper ya añade url(); guardar solo URL#ID.")
            return
        if not public_url(value) or "placeholders/" in value or (urlsplit(value).hostname or "").endswith("figma.com"):
            validator.err("E071", path, "Medio local, temporal o placeholder; resolver antes de entregar.")
            return
        host = urlsplit(value).hostname
        if domains and host not in domains:
            validator.err("E071", path, "Medio de un dominio ajeno al perfil.")
        if not re.search(r"#[1-9][0-9]*$", value):
            validator.warn("W070", path, "Medio estático sin #ID; registrar adjunto y consumidor.")
        if source == "generated":
            if manifest is None:
                validator.warn("W071", path, "Medio no contrastado: proporcionar --manifest.")
            elif value not in media_refs:
                validator.err("E072", path, "Medio no coincide con URL e ID del manifest.")

    def css_media(value, path):
        if isinstance(value, dict):
            for key, val in value.items():
                css_media(val, path + "." + key)
        else:
            media(value, path)

    def walk(obj, path):
        if isinstance(obj, list):
            for i, value in enumerate(obj): walk(value, "%s[%d]" % (path, i))
            return
        if not isinstance(obj, dict): return
        if obj.get("type") == "video" and isinstance(obj.get("attr"), dict):
            attr = obj["attr"]
            if attr.get("mp4") and attr.get("video") != "":
                validator.warn("W072", path + ".attr.video", "Vídeo HTML5: declarar video vacío para impedir un proveedor ajeno al editar.")
            params = attr.get("html5_parameters")
            if params and (not isinstance(params, str) or len(params.split(";")) != 5):
                validator.err("E073", path + ".attr.html5_parameters", "Se requieren cinco posiciones separadas por punto y coma.")
            if attr.get("object_fit") and not all(attr.get(k) for k in ("css_video_width", "css_video_height")):
                validator.warn("W073", path + ".attr", "object_fit requiere anchura y altura del vídeo.")
        for key, value in obj.items():
            here = path + "." + key
            if key == "custom_id" and isinstance(value, str) and value:
                if value in ids: validator.warn("W074", here, "Ancla duplicada; también en " + ids[value])
                ids[value] = here
            if key == "link" and isinstance(value, str): links.append((value, here))
            if isinstance(value, str) and "XXXXXXXX" in value:
                validator.warn("W075", here, "Referencia provisional sin resolver.")
            if key in MEDIA_KEYS and isinstance(value, str) and value and not value.startswith("icon-"):
                # Element config enums can also be called image; uploads and URI-shaped values only.
                if key != "image" or "/" in value or DYNAMIC.search(value): media(value, here)
            if isinstance(value, dict) and value.get("style") in ("background-image", "-webkit-mask-image"):
                css_media(value.get("val"), here + ".val")
            if key in DEPENDENCY_KEYS and value and profile:
                category = DEPENDENCY_KEYS[key]
                available = profile.get("dependencies", {}).get(category)
                if available is None:
                    validator.warn("W076", here, "Dependencia no comprobada: " + category)
                elif str(value) not in {str(x) for x in available}:
                    validator.warn("W076", here, "Dependencia ausente del perfil: %s/%s" % (category, value))
            if key == "font-family" and value and profile:
                fonts = profile.get("fonts", [])
                if value not in fonts:
                    validator.warn("W077", here, "Familia no declarada en el perfil tipográfico.")
            if key == "be_classes" and isinstance(value, list):
                available = profile.get("global_styles", [])
                for cls in value:
                    if cls not in available: validator.warn("W078", here, "Global Style sin definición declarada: " + str(cls))
            walk(value, here)
    walk(document, "$")
    for link, path in links:
        if link == "#": validator.warn("W075", path, "Enlace provisional #.")
        elif link.startswith("#") and link[1:] not in ids:
            validator.warn("W079", path, "Ancla sin destino en el documento; declarar excepción si pertenece a otra plantilla.")
