"""Shared, offline contracts. No WordPress or network side effects."""
from __future__ import annotations

import hashlib
import ipaddress
import json
import math
import os
import tempfile
from pathlib import Path
from urllib.parse import urlsplit

MAX_BYTES = 32 * 1024 * 1024
MAX_DEPTH = 64
MAX_NODES = 500_000
BREAKPOINTS = {"laptop": 1440, "tablet": 959, "mobile": 767}


def inspect_tree(document):
    stack = [(document, 0)]
    count = 0
    while stack:
        value, depth = stack.pop()
        if depth > MAX_DEPTH or count > MAX_NODES:
            raise ValueError("Documento demasiado profundo o grande (máximo 64 niveles / 500000 valores).")
        if isinstance(value, dict):
            if any(not isinstance(k, str) for k in value):
                raise ValueError("Las claves JSON deben ser strings.")
            values = value.values()
        elif isinstance(value, list):
            values = value
        else:
            values = (value,)
        count += len(value) if isinstance(value, (dict, list)) else 1
        for child in values:
            if isinstance(child, (dict, list)):
                stack.append((child, depth + 1))
            elif isinstance(child, float) and not math.isfinite(child):
                raise ValueError("JSON no admite números no finitos.")
            elif child is not None and not isinstance(child, (str, int, float, bool)):
                raise ValueError("Valor no serializable: %s" % type(child).__name__)
        if count > MAX_NODES:
            raise ValueError("Documento mayor de 500000 valores.")


def strict_loads(text):
    if len(text.encode("utf-8")) > MAX_BYTES:
        raise ValueError("Documento mayor de 32 MiB.")
    def pairs(values):
        result = {}
        for key, value in values:
            if key in result:
                raise ValueError("Clave JSON duplicada: %s" % key)
            result[key] = value
        return result
    def constant(value):
        raise ValueError("Número JSON no finito: %s" % value)
    try:
        result = json.loads(text.lstrip("\ufeff"), object_pairs_hook=pairs, parse_constant=constant)
        inspect_tree(result)
        return result
    except RecursionError as exc:
        raise ValueError("Documento demasiado profundo.") from exc


def read_json(path):
    with Path(path).open("rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("Documento mayor de 32 MiB.")
    return strict_loads(raw.decode("utf-8-sig"))


def atomic_json(path, data, indent=2):
    inspect_tree(data)
    payload = json.dumps(data, ensure_ascii=False, indent=indent, allow_nan=False) + "\n"
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    name = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix="." + path.name, delete=False) as stream:
            name = stream.name
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)


def public_url(value):
    if not isinstance(value, str) or any(c.isspace() for c in value):
        return False
    try:
        url = urlsplit(value)
        host = (url.hostname or "").lower()
        if url.scheme not in ("http", "https") or not host or url.username or url.password:
            return False
        if host == "localhost" or host.endswith((".localhost", ".local")):
            return False
        try:
            if not ipaddress.ip_address(host).is_global:
                return False
        except ValueError:
            pass
        return True
    except ValueError:
        return False


def validate_manifest(manifest, domains=(), root=None):
    if not isinstance(manifest, dict):
        raise ValueError("El manifest debe ser un objeto por nombre de recurso.")
    ids = {}
    for name, entry in manifest.items():
        if not isinstance(name, str) or not name or not isinstance(entry, dict):
            raise ValueError("Entrada de manifest inválida: %r" % name)
        aid, url = entry.get("id"), entry.get("url")
        if isinstance(aid, bool) or not isinstance(aid, (str, int)) or not str(aid).isdigit() or int(aid) <= 0:
            raise ValueError("%s: id debe ser un entero positivo." % name)
        if not public_url(url) or urlsplit(url).fragment:
            raise ValueError("%s: URL pública sin fragmento requerida." % name)
        if domains and urlsplit(url).hostname not in domains:
            raise ValueError("%s: dominio ajeno al destino." % name)
        if int(aid) in ids and ids[int(aid)] != url:
            raise ValueError("ID de adjunto con URLs contradictorias: %s" % aid)
        ids[int(aid)] = url
        for key in ("width", "height"):
            if key in entry and (type(entry[key]) is not int or entry[key] <= 0):
                raise ValueError("%s: %s debe ser positivo." % (name, key))
        if root is not None and entry.get("local"):
            local = (Path(root) / entry["local"]).resolve()
            if not local.is_relative_to(Path(root).resolve()) or not local.is_file():
                raise ValueError("%s: fichero local ausente o fuera del proyecto." % name)
            if entry.get("sha256") and hashlib.sha256(local.read_bytes()).hexdigest() != entry["sha256"]:
                raise ValueError("%s: hash del medio no coincide." % name)
    return manifest
