#!/usr/bin/env python3
"""Genera dist/magnific-prompt-system(.zip) desde prompt-system/.

Fuente de verdad: prompt-system/. dist/ se regenera entero; no se edita a mano.
Formato de salida: una sola skill (SKILL.md = director) + references/ con el resto.
Uso: python3 build-dist.py
"""
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "prompt-system"
DIST = ROOT / "dist"
OUT = DIST / "magnific-prompt-system"
REFS = OUT / "references"

SKILLS = ["brief", "script", "breakdown", "review", "coherencia", "character-ref", "prop-ref", "location-ref", "shot-composer", "video-prompt", "audio-prompt", "edit-plan", "repair"]
DIRECTOR_DESC = (
    "Prepara por escrito producciones audiovisuales con IA para pegar los prompts en Magnific "
    "(imagen Nano Banana, vídeo Seedance). Úsala cuando el usuario diga «oye Amenábar», «Amenábar, …», "
    "«sigue mi proyecto», «¿en qué fase estoy?» o «¿qué toca ahora?», o pegue un dossier; también para "
    "brief, guion, desglose, revisión del desglose con un estilo («revisa con estilo redes»), plan de referencias y referencias de personaje, localización u objeto e imagen inicial y prompt de vídeo de un plano. "
    "Dice en qué fase está el proyecto y cuál es el siguiente paso. No genera imágenes ni vídeo. "
    "Audio: sin audio, externo o en Magnific, según el proyecto."
)


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n+", "", text, count=1, flags=re.S)


def fix_paths(text: str) -> str:
    text = re.sub(r"REGLAS\.md", "references/reglas.md", text)
    text = re.sub(r"PROYECTO\.md", "references/proyecto.md", text)
    text = re.sub(r"MODELOS\.md", "references/modelos.md", text)
    text = re.sub(r"PLATAFORMAS\.md", "references/plataformas.md", text)
    text = re.sub(r"(?<![/\w])estilos/", "references/estilos/", text)
    return re.sub(r"EX00_KISS\.md", "references/ex00-kiss.md", text)


if OUT.exists():
    shutil.rmtree(OUT)
REFS.mkdir(parents=True)

# Skills secundarias -> references/<nombre>.md, con su frontmatter fuera.
for name in SKILLS:
    body = strip_frontmatter((SRC / name / "SKILL.md").read_text(encoding="utf-8"))
    (REFS / f"{name}.md").write_text(fix_paths(body), encoding="utf-8")

# Documentos comunes.
(REFS / "reglas.md").write_text(
    fix_paths((SRC / "REGLAS.md").read_text(encoding="utf-8")), encoding="utf-8"
)
(REFS / "proyecto.md").write_text(
    fix_paths((SRC / "PROYECTO.md").read_text(encoding="utf-8")), encoding="utf-8"
)
(REFS / "modelos.md").write_text(
    fix_paths((SRC / "MODELOS.md").read_text(encoding="utf-8")), encoding="utf-8"
)
(REFS / "plataformas.md").write_text(
    fix_paths((SRC / "PLATAFORMAS.md").read_text(encoding="utf-8")), encoding="utf-8"
)
(REFS / "ex00-kiss.md").write_text(
    fix_paths((SRC / "EX00_KISS.md").read_text(encoding="utf-8")), encoding="utf-8"
)
(REFS / "estilos").mkdir()
for style in sorted((SRC / "estilos").glob("*.md")):
    (REFS / "estilos" / style.name).write_text(
        fix_paths(style.read_text(encoding="utf-8")), encoding="utf-8"
    )
(REFS / "guia-usuario.md").write_text(
    fix_paths((SRC / "FLUJO-idea-a-desglose.md").read_text(encoding="utf-8")), encoding="utf-8"
)

# SKILL.md raíz = director, con rutas a references/.
director = strip_frontmatter((SRC / "director" / "SKILL.md").read_text(encoding="utf-8"))
director = fix_paths(director)
for name in SKILLS:
    director = director.replace(f"| {name} |", f"| `references/{name}.md` |")
root = f"---\nname: magnific-prompt-system\ndescription: {DIRECTOR_DESC}\n---\n\n{director}"
(OUT / "SKILL.md").write_text(root, encoding="utf-8")

# Zip.
zip_path = DIST / "magnific-prompt-system.zip"
if zip_path.exists():
    zip_path.unlink()
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(OUT.rglob("*")):
        z.write(f, f.relative_to(DIST))

print(f"OK: {OUT} y {zip_path}")
