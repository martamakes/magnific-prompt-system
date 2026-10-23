#!/usr/bin/env python3
"""Comprueba que la copia instalada de la skill coincide con lo que generaría build-dist.py.

Regenera dist/ y la compara con .claude/skills/magnific-prompt-system. Solo informa:
no instala ni modifica la copia. Sale con 1 si hay diferencias.
"""
import filecmp
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUILT = ROOT / "dist" / "magnific-prompt-system"
INSTALLED = ROOT / ".claude" / "skills" / "magnific-prompt-system"

subprocess.run([sys.executable, str(ROOT / "build-dist.py")], check=True, stdout=subprocess.DEVNULL)

if not INSTALLED.is_dir():
    sys.exit(f"No instalada: falta {INSTALLED.relative_to(ROOT)}")


def compare(cmp: filecmp.dircmp, prefix: str = "") -> list[str]:
    out = [f"solo en dist: {prefix}{n}" for n in cmp.left_only]
    out += [f"solo en instalada: {prefix}{n}" for n in cmp.right_only]
    out += [f"distinto: {prefix}{n}" for n in cmp.diff_files]
    for name, sub in cmp.subdirs.items():
        out += compare(sub, f"{prefix}{name}/")
    return out


diffs = compare(filecmp.dircmp(BUILT, INSTALLED))
if diffs:
    print("Copia instalada desactualizada:")
    print("\n".join(f"  {d}" for d in diffs))
    print("Para reinstalar: rm -rf .claude/skills/magnific-prompt-system && cp -R dist/magnific-prompt-system .claude/skills/")
    sys.exit(1)
print("Sincronizada: la copia instalada coincide con el build.")
