"""Validated, atomic delivery for NEW build(context) scripts only."""
from __future__ import annotations

import argparse
import ast
import importlib.util
from pathlib import Path
import sys
import time

from contracts import atomic_json, read_json, validate_manifest
from mfn import BuildContext
from validate_bebuilder_json import validate


def design_issues(design, document):
    issues = []
    nodes = {}
    def walk(value):
        if isinstance(value, dict):
            if value.get("uid"): nodes[value["uid"]] = value
            for key in ("items", "wraps"):
                for child in value.get(key, []): walk(child)
        elif isinstance(value, list):
            for child in value: walk(child)
    walk(document)
    seen = set()
    mapped = set()
    for block in design.get("blocks", []):
        if block.get("id") in seen: issues.append("Bloque duplicado: " + str(block.get("id")))
        seen.add(block.get("id"))
        if block.get("evidence") == "pending": issues.append("Bloque pendiente: " + str(block.get("id")))
        uids = block.get("uids", [])
        if not uids and not block.get("exception"): issues.append("Bloque sin correspondencia: " + str(block.get("id")))
        for uid in uids:
            if uid not in nodes: issues.append("UID de diseño inexistente: " + uid)
            if uid in nodes:
                descendants = [nodes[uid]]
                while descendants:
                    current = descendants.pop()
                    mapped.add(current.get("uid"))
                    descendants.extend(current.get("items", []))
                    descendants.extend(current.get("wraps", []))
        if not block.get("responsive") and not block.get("exception"):
            issues.append("Decisión responsive ausente: " + str(block.get("id")))
    unmapped = set(nodes) - mapped
    if unmapped: issues.append("Nodos sin correspondencia: " + ", ".join(sorted(unmapped)))
    if not design.get("source"): issues.append("Origen del diseño sin registrar")
    if not design.get("blocks"): issues.append("Sin mapa de correspondencia del diseño")
    return issues


def deliver(document, context, output, *, check=False, draft=False):
    started = time.perf_counter()
    validate_manifest(context.manifest, context.profile.get("media_domains", []))
    result = validate(document, strict=True, editor=context.profile.get("editor", "visual"),
                      manifest=context.manifest, profile=context.profile, exceptions=context.exceptions)
    if result["structurally_valid"]:
        mapping = design_issues(context.design, document)
    else:
        mapping = ["No se puede verificar el mapa con estructura inválida"]
    result["design_issues"] = mapping
    result["accepted"] = result["accepted"] and not mapping
    result["exit_code"] = result["exit_code"] or (2 if mapping else 0)
    result["visual_verification"] = "not_run"
    result["wordpress_roundtrip"] = "not_run"
    result["elapsed_validation_ms"] = round((time.perf_counter() - started) * 1000, 3)
    result["artifact_kind"] = context.profile.get("artifact_kind", "page")
    result["delivery_steps"] = ["Resolver dependencias del perfil", "Importar plantillas/Global Styles requeridos",
                                "Importar JSON en Visual Builder", "Guardar una vez para generar CSS con UID nuevos",
                                "Comprobar edición, exportación y renderizado"]
    result.pop("document")
    if not check and (result["accepted"] or draft):
        output = Path(output)
        # Una entrega aceptada se publica siempre; --draft solo conserva la propuesta rechazada.
        if draft and not result["accepted"]: output = output.with_name(output.stem + ".draft.json")
        atomic_json(output.with_suffix(".report.json"), result)
        atomic_json(output.with_suffix(".design.json"), context.design)
        atomic_json(output.with_suffix(".profile.json"), context.profile)
        atomic_json(output, document)
    return result


def main(argv=None):
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("script", type=Path)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--draft", action="store_true")
    parser.add_argument("--profile", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--design", type=Path)
    parser.add_argument("--output", type=Path)
    opts = parser.parse_args(argv)
    try:
        script = opts.script.resolve()
        tree = ast.parse(script.read_text())
        if not any(isinstance(n, ast.FunctionDef) and n.name == "build" for n in tree.body):
            raise ValueError("Script histórico sin build(context): no se ejecuta ni migra automáticamente")
        # Repository scripts are trusted Python; --check requires import without side effects.
        spec = importlib.util.spec_from_file_location("muffin_page_build", script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        profile = read_json(opts.profile) if opts.profile else getattr(module, "PROFILE", {})
        manifest_path = opts.manifest or script.parent / "assets" / "manifest.json"
        manifest = read_json(manifest_path) if manifest_path.exists() else {}
        validate_manifest(manifest, profile.get("media_domains", []), manifest_path.parent)
        design = read_json(opts.design) if opts.design else {"source": getattr(module, "SOURCE", {}), "blocks": []}
        context = BuildContext(profile=profile, manifest=manifest, design=design,
                               tokens=getattr(module, "TOKENS", {}), exceptions=getattr(module, "EXCEPTIONS", []))
        with context: document = module.build(context)
        output = opts.output or script.parent / getattr(module, "OUTPUT", "salida.json")
        if not output.is_absolute(): output = script.parent / output
        result = deliver(document, context, output, check=opts.check, draft=opts.draft)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return result["exit_code"]
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"accepted": False, "exit_code": 3, "error": str(exc)}, ensure_ascii=False))
        return 3


if __name__ == "__main__": sys.exit(main())
