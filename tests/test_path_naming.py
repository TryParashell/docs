from __future__ import annotations

import re
from pathlib import Path


STALE_PATHS = [
    "Parashell" + "-Modules",
    "Parashell" + "-Monorepo",
    "modules" + "/source",
    "Source" + "/Auth",
    "Source" + "/Bridge",
    "Bridge" + "/rpc_methods",
    "bridge" + ".py",
    "auth_core" + ".py",
]
STALE_PATH_PATTERN = re.compile("|".join(re.escape(path) for path in STALE_PATHS), re.IGNORECASE)

SKIPPED_DIRS = {".git", ".pytest_cache", "node_modules", "vendor"}
TEXT_SUFFIXES = {".json", ".md", ".mdx", ".py", ".svg", ".txt"}


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIPPED_DIRS for part in path.parts):
            continue
        if path.is_file() and (path.suffix in TEXT_SUFFIXES or path.name == "AGENTS.md"):
            yield path


def test_docs_do_not_reference_stale_private_source_paths() -> None:
    root = Path(__file__).resolve().parents[1]
    matches: list[str] = []

    for path in iter_text_files(root):
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if STALE_PATH_PATTERN.search(line):
                matches.append(f"{path.relative_to(root)}:{line_number}: {line}")

    assert not matches, "stale private source paths found:\n" + "\n".join(matches)
