"""_apply_folder_restructure_path_sweep_v1_20260427.py

Sweep scripts/, engine/, and selected docs for path references to old folders
that were restructured on 2026-04-27. Performs targeted text replacements; runs
dry-run by default. The mapping table at the top of this file is the single
source of truth — extend it if new patterns surface.

This is a one-shot script. Once executed live, archive it and move on.

Usage:
  python scripts/archive/_apply_folder_restructure_path_sweep_v1_20260427.py
  python scripts/archive/_apply_folder_restructure_path_sweep_v1_20260427.py --live
  python scripts/archive/_apply_folder_restructure_path_sweep_v1_20260427.py --live --paths scripts engine
"""
from __future__ import annotations
import argparse
import os
import sys
from pathlib import Path

# (old_substring, new_substring) — order matters: more-specific first
PATH_MAPPINGS = [
    # ── DB + manifest + schema (top of priority list) ─────────────────────────
    ("data/bible_research.db", "database/bible_research.db"),
    ("data\\bible_research.db", "database\\bible_research.db"),
    ("data\\\\bible_research.db", "database\\\\bible_research.db"),
    ("'data', 'bible_research.db'", "'database', 'bible_research.db'"),
    ('"data", "bible_research.db"', '"database", "bible_research.db"'),
    ("data/file_manifest.json", "database/file_manifest.json"),
    ("'data', 'file_manifest.json'", "'database', 'file_manifest.json'"),
    ('"data", "file_manifest.json"', '"database", "file_manifest.json"'),
    ("data/schema/create_tables.sql", "Workflow/schema/create_tables.sql"),
    ("'data', 'schema'", "'Workflow', 'schema'"),
    ('"data", "schema"', '"Workflow", "schema"'),

    # ── Discovery (STEP raw output) ───────────────────────────────────────────
    ("data/discovery/", "research/discovery/"),
    ("data/discovery'", "research/discovery'"),
    ('data/discovery"', 'research/discovery"'),
    ("'data', 'discovery'", "'research', 'discovery'"),
    ('"data", "discovery"', '"research", "discovery"'),

    # ── Exports → split by old subfolder ──────────────────────────────────────
    ("data/exports/STEP Extracts", "Sessions/Session_A/STEP Extracts"),
    ("data/exports/reference/", "Workflow/reference/"),
    ("data/exports/reference'", "Workflow/reference'"),
    ('data/exports/reference"', 'Workflow/reference"'),
    ("'data', 'exports', 'reference'", "'Workflow', 'reference'"),
    ('"data", "exports", "reference"', '"Workflow", "reference"'),
    ("data/exports/session_a/terms/", "Sessions/Session_A/terms/"),
    ("data/exports/session_a/terms'", "Sessions/Session_A/terms'"),
    ('data/exports/session_a/terms"', 'Sessions/Session_A/terms"'),
    ("data/exports/session_d/", "Sessions/Session_D/session_d/"),
    ("data/exports/session_d'", "Sessions/Session_D/session_d'"),
    ('data/exports/session_d"', 'Sessions/Session_D/session_d"'),
    ("data/exports/dimension_review/", "Sessions/Session_B/04_dimension_review_process input/"),
    ("data/exports/dimension_review'", "Sessions/Session_B/04_dimension_review_process input'"),
    ("data/exports/verse_context/", "Sessions/Session_B/01_Verse_Context_Process_input/"),
    ("data/exports/verse_context'", "Sessions/Session_B/01_Verse_Context_Process_input'"),

    # ── Imports → new top-level Sessions/ structure ───────────────────────────
    ("data/imports/WA/Patches/", "Sessions/Patches/"),
    ("data/imports/WA/Patches'", "Sessions/Patches'"),
    ('data/imports/WA/Patches"', 'Sessions/Patches"'),
    ("'data', 'imports', 'WA', 'Patches'", "'Sessions', 'Patches'"),
    ('"data", "imports", "WA", "Patches"', '"Sessions", "Patches"'),
    ("data/imports/WA/Session_B_Analysis/", "Sessions/Session_B/09_Analysis_output_logs/"),
    ("data/imports/WA/Session_B_Verse_Context/", "Sessions/Session_B/02_Verse_Context_logs/"),
    ("data/imports/WA/Session_B_Dimension_Review/", "Sessions/Session_B/05_Dimension_Review_logs/"),
    ("data/imports/WA/Session_C_Words/", "Sessions/Session_C/Session_C_Words/"),
    ("data/imports/WA/Session_D_Synthesis/", "Sessions/Session_D/Session_D_Synthesis/"),
    ("data/imports/WA/Word_Data/", "Sessions/Session_A/Word_Data/"),
    ("data/imports/WA/Workflow/Sessionlogs/", "Workflow/Sessionlogs/"),
    ("data/imports/WA/Workflow/methodology_logs/", "Workflow/methodology/"),

    # ── Outputs split: programme reports moved into Workflow/Programme/ ──────
    ("outputs/reports/programme/", "Workflow/Programme/Program_reports/"),
    ("outputs/reports/programme'", "Workflow/Programme/Program_reports'"),
    ('outputs/reports/programme"', 'Workflow/Programme/Program_reports"'),
    ("outputs/reports/words/", "Sessions/Session_B/09_Analysis_output_logs/words/"),
    ("outputs/reports/words'", "Sessions/Session_B/09_Analysis_output_logs/words'"),
    ('outputs/reports/words"', 'Sessions/Session_B/09_Analysis_output_logs/words"'),
    ("outputs/investigations/", "research/investigations/"),
    ("outputs/investigations'", "research/investigations'"),
    ('outputs/investigations"', 'research/investigations"'),
]

# Files where the OLD path is a documented historical reference (Logs/, archive/ — git-tracked
# session logs from before the restructure) — do NOT rewrite these.
SKIP_DIRS = {"backups", ".git", ".venv", "venv", "node_modules", "Logs",
             "archive", "outputs/archive"}

# Restrict by default to live code paths.
DEFAULT_TARGETS = ["scripts", "engine"]


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    return bool(parts & SKIP_DIRS)


def sweep_file(p: Path, dry: bool) -> tuple[int, list[str]]:
    """Return (n_replacements, list of 'old → new (count)' lines)."""
    try:
        text = p.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return 0, []

    summary = []
    new_text = text
    total = 0
    for old, new in PATH_MAPPINGS:
        if old in new_text:
            n = new_text.count(old)
            new_text = new_text.replace(old, new)
            summary.append(f"  {old!r}  →  {new!r}  ({n}×)")
            total += n

    if total and not dry:
        p.write_text(new_text, encoding="utf-8")

    return total, summary


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true",
                    help="Apply edits (default: dry-run, prints planned changes)")
    ap.add_argument("--paths", nargs="+", default=DEFAULT_TARGETS,
                    help=f"Folders to scan (default: {DEFAULT_TARGETS})")
    ap.add_argument("--ext", nargs="+", default=[".py", ".md", ".sh", ".ps1", ".txt"],
                    help="File extensions to scan")
    args = ap.parse_args()

    files_changed = 0
    total_replacements = 0
    for root in args.paths:
        rp = Path(root)
        if not rp.exists():
            print(f"[skip] {root} not found")
            continue
        for p in rp.rglob("*"):
            if not p.is_file():
                continue
            if should_skip(p):
                continue
            if p.suffix not in args.ext:
                continue
            n, summary = sweep_file(p, dry=not args.live)
            if n:
                files_changed += 1
                total_replacements += n
                print(f"\n[{('DRY' if not args.live else 'LIVE')}] {p}: {n} replacement(s)")
                for line in summary:
                    print(line)

    mode = "DRY-RUN" if not args.live else "LIVE"
    print(f"\n=== {mode} summary ===")
    print(f"Files changed: {files_changed}")
    print(f"Total replacements: {total_replacements}")
    if not args.live:
        print("(re-run with --live to apply)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
