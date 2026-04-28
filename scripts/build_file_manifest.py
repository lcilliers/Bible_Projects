#!/usr/bin/env python3
"""
build_file_manifest.py — Generates database/file_manifest.json

Scans the project tree and produces a machine-readable index of every
non-code file (imports, exports, patches, directives, reports, logs,
discovery, docs, archived files).  Archive contents are included —
archived files are put aside, not dead.

Usage:
    python scripts/build_file_manifest.py              # full rebuild
    python scripts/build_file_manifest.py --search "grace"
    python scripts/build_file_manifest.py --search "registry:068"
    python scripts/build_file_manifest.py --search "type:observations"
    python scripts/build_file_manifest.py --stats       # summary counts
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = PROJECT_ROOT / "database" / "file_manifest.json"

# Directories to scan (relative to PROJECT_ROOT)
SCAN_DIRS = [
    "data/imports",
    "data/exports",
    "research/discovery",
    "data/schema",
    "archive",
    "outputs",
    "docs",
    "Logs",
]

# Directories to skip entirely
SKIP_DIRS = {
    ".git", "__pycache__", "venv", ".venv", "node_modules",
    "backups", ".claude",
}

# File extensions to include
INCLUDE_EXTS = {
    ".md", ".json", ".csv", ".txt", ".docx", ".pdf", ".xlsx",
    ".html", ".png", ".log", ".sql",
}

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

# Date patterns in filenames
DATE_COMPACT = re.compile(r'(\d{4})(\d{2})(\d{2})')
DATE_HYPHEN = re.compile(r'(\d{4})-(\d{2})-(\d{2})')

# Registry number patterns
REG_PATTERNS = [
    re.compile(r'(?:^|[-_])(\d{3})[-_]'),           # wa-068-grace or 068_grace
    re.compile(r'registry[_-]?(\d+)', re.I),          # registry111
    re.compile(r'reg[_-]?(\d{3})', re.I),             # reg068
    re.compile(r'[-_](\d{1,3})[-_](?:full|report|complete|owner)', re.I),
]

# Version patterns
VERSION_RE = re.compile(r'-v(\d+(?:\.\d+)?)')

# VCB batch pattern
VCB_RE = re.compile(r'vcb[_-]?(\d{3})', re.I)

# Cluster pattern
CLUSTER_RE = re.compile(r'(?:^|[-_])(c\d{2})(?:[-_]|$)', re.I)

# Word name — extract from wa-NNN-{word} or {word}_{reg}
WORD_FROM_WA = re.compile(r'wa-\d{3}-([a-z]+)')
WORD_FROM_UNDERSCORE = re.compile(r'^([a-z]+)_\d+')
WORD_FROM_LONG = re.compile(r'(?:registry|reg)\d+-([a-z]+)', re.I)


def extract_date(filename: str) -> str | None:
    """Extract date from filename, return as YYYY-MM-DD or None."""
    # Try hyphenated first (more specific)
    m = DATE_HYPHEN.search(filename)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    # Try compact
    m = DATE_COMPACT.search(filename)
    if m:
        y, mo, d = m.group(1), m.group(2), m.group(3)
        if 2025 <= int(y) <= 2030 and 1 <= int(mo) <= 12 and 1 <= int(d) <= 31:
            return f"{y}-{mo}-{d}"
    return None


def extract_registry(filename: str) -> int | None:
    """Extract registry number from filename."""
    for pat in REG_PATTERNS:
        m = pat.search(filename)
        if m:
            val = int(m.group(1))
            if 1 <= val <= 300:
                return val
    return None


def extract_version(filename: str) -> str | None:
    """Extract version string from filename."""
    m = VERSION_RE.search(filename)
    return m.group(1) if m else None


def extract_vcb_batch(filename: str) -> int | None:
    """Extract VCB batch number."""
    m = VCB_RE.search(filename)
    return int(m.group(1)) if m else None


def extract_cluster(filename: str) -> str | None:
    """Extract cluster code (e.g. C17)."""
    m = CLUSTER_RE.search(filename)
    return m.group(1).upper() if m else None


def extract_word(filename: str) -> str | None:
    """Extract word name from filename."""
    m = WORD_FROM_WA.search(filename)
    if m:
        return m.group(1)
    m = WORD_FROM_UNDERSCORE.search(filename)
    if m:
        return m.group(1)
    m = WORD_FROM_LONG.search(filename)
    if m:
        return m.group(1).lower()
    return None


def classify_category(rel_path: str) -> str:
    """Determine the top-level category from the relative path."""
    parts = rel_path.replace("\\", "/").lower()
    if parts.startswith("data/imports/wa/patches") or parts.startswith("archive/patches"):
        # Distinguish patches from directives
        if parts.endswith(".json"):
            return "patch"
        elif "directive" in parts:
            return "directive"
        return "patch"
    if parts.startswith("data/imports"):
        return "import"
    if parts.startswith("data/exports"):
        return "export"
    if parts.startswith("research/discovery"):
        return "discovery"
    if parts.startswith("data/schema"):
        return "schema"
    if parts.startswith("archive/scripts"):
        return "script"
    if parts.startswith("archive/logs"):
        return "log"
    if parts.startswith("archive/docs"):
        return "doc"
    if parts.startswith("archive/patches"):
        if parts.endswith(".json"):
            return "patch"
        return "directive"
    if parts.startswith("outputs/reports"):
        return "report"
    if parts.startswith("research/investigations"):
        return "investigation"
    if parts.startswith("outputs"):
        return "report"
    if parts.startswith("docs"):
        return "doc"
    if parts.startswith("logs"):
        return "log"
    return "other"


def classify_type(filename: str, category: str, rel_path: str) -> str:
    """Determine the specific file type."""
    fn = filename.lower()
    rp = rel_path.replace("\\", "/").lower()

    # Patches and directives
    if category == "patch":
        if "preanalysis" in fn:
            return "preanalysis-patch"
        if "analysis" in fn and "pre" not in fn:
            return "analysis-patch"
        if "sessionb-complete" in fn:
            return "sessionb-complete-patch"
        if "sessionb" in fn:
            return "sessionb-patch"
        if "versecontext" in fn:
            return "versecontext-patch"
        if "vcgroup" in fn:
            return "vcgroup-patch"
        if "vcverse" in fn:
            return "vcverse-patch"
        if "repair" in fn:
            return "repair-patch"
        if "sessiond" in fn:
            return "sessiond-patch"
        if "clustering" in fn:
            return "clustering-patch"
        if "sdenrich" in fn:
            return "sdenrich-patch"
        if "sdpointers" in fn:
            return "sdpointers-patch"
        if "dimcorrect" in fn:
            return "dimcorrect-patch"
        if "dimreview" in fn:
            return "dimreview-patch"
        if "dim" in fn:
            return "dimension-patch"
        return "patch"
    if category == "directive":
        return "cc-directive"

    # Imports
    if category == "import":
        if "observations" in fn:
            return "observations"
        if "session-log" in fn or "sessionlog" in fn or "session_log" in fn:
            return "session-log"
        if "term-observations" in fn:
            return "term-observations"
        if "sessionb-flags" in fn or "sessionb_flags" in fn:
            return "sessionb-flags"
        if "word-study" in fn or "word_study" in fn:
            return "word-study"
        if "brief" in fn:
            return "brief"
        if "cc-directive" in fn:
            return "cc-directive"
        if "patch-log" in fn:
            return "patch-log"
        if "note" in fn:
            return "note"
        if "log" in fn:
            return "session-log"
        if "instruction" in fn:
            return "instruction"
        if "reference" in fn:
            return "reference-doc"
        if "template" in fn:
            return "template"
        if "analysis-report" in fn:
            return "analysis-report"
        if "compliance" in fn or "methodology" in fn:
            return "methodology"
        if "flag" in fn:
            return "flags"
        if fn.endswith(".json"):
            return "session-a-data"
        return "import"

    # Exports
    if category == "export":
        if "step extracts" in rp or "step_extracts" in rp:
            return "step-extract"
        if "session c" in rp or "session_c" in rp:
            if "owner_only" in fn or "owner-only" in fn:
                return "owner-only-extract"
            return "complete-extract"
        if "verse_context" in rp:
            return "vc-batch-extract"
        if "dimension_review" in rp:
            if "rootfamily" in fn:
                return "dim-rootfamily-extract"
            if "pointers" in fn:
                return "dim-pointers-extract"
            return "dim-extract"
        if "session_d" in rp:
            if "pointer-audit" in fn or "pointer_audit" in fn:
                return "sd-pointer-audit"
            return "sd-pointers"
        if "pool_analysis" in rp:
            return "pool-analysis"
        if "vertical_pass" in rp:
            return "vertical-pass"
        return "export"

    # Discovery
    if category == "discovery":
        if fn.endswith(".json"):
            return "discovery-json"
        return "discovery-summary"

    # Reports
    if category == "report":
        if "programme" in rp:
            if "schema" in fn:
                return "schema-snapshot"
            if "status" in fn:
                return "programme-status"
            if "dimension" in fn:
                return "dimension-report"
            if "registry" in fn or "overview" in fn:
                return "registry-overview"
            if "pooling" in fn:
                return "pool-report"
            return "programme-report"
        if "words" in rp:
            if fn.startswith("vc-report"):
                return "vc-word-report"
            return "word-report"
        return "report"

    # Investigation
    if category == "investigation":
        return "investigation"

    # Schema
    if category == "schema":
        if fn.endswith(".sql"):
            return "ddl"
        return "schema-snapshot"

    # Docs
    if category == "doc":
        if "architecture" in fn:
            return "architecture"
        if "setup" in fn:
            return "setup-guide"
        if "organisation" in fn or "organization" in fn:
            return "org-rules"
        if "pipeline" in fn:
            return "pipeline-design"
        if "interaction" in fn:
            return "interaction-prefs"
        if "field-data" in fn:
            return "data-flow"
        return "doc"

    # Logs
    if category == "log":
        return "session-log"

    return "other"


# ---------------------------------------------------------------------------
# Scanner
# ---------------------------------------------------------------------------

def scan_project() -> list[dict]:
    """Walk SCAN_DIRS and build manifest entries."""
    entries = []

    for scan_dir in SCAN_DIRS:
        root_dir = PROJECT_ROOT / scan_dir
        if not root_dir.exists():
            continue

        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Prune skipped directories
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

            for fname in filenames:
                fpath = Path(dirpath) / fname
                ext = fpath.suffix.lower()
                if ext not in INCLUDE_EXTS:
                    continue

                rel = fpath.relative_to(PROJECT_ROOT).as_posix()
                stat = fpath.stat()

                category = classify_category(rel)
                file_type = classify_type(fname, category, rel)
                is_archived = "/archive/" in rel.lower() or rel.lower().startswith("archive/")

                entry = {
                    "path": rel,
                    "category": category,
                    "type": file_type,
                    "registry": extract_registry(fname),
                    "word": extract_word(fname),
                    "cluster": extract_cluster(fname),
                    "batch": extract_vcb_batch(fname),
                    "version": extract_version(fname),
                    "date": extract_date(fname),
                    "ext": ext,
                    "archived": is_archived,
                    "size_bytes": stat.st_size,
                    "modified": datetime.fromtimestamp(
                        stat.st_mtime, tz=timezone.utc
                    ).strftime("%Y-%m-%dT%H:%M:%SZ"),
                }
                entries.append(entry)

    # Sort by path for stable output
    entries.sort(key=lambda e: e["path"])
    return entries


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------

def search_manifest(entries: list[dict], query: str) -> list[dict]:
    """Filter manifest entries by query string."""
    # Structured queries: "field:value"
    if ":" in query and not query.startswith("/"):
        field, value = query.split(":", 1)
        field = field.strip().lower()
        value = value.strip().lower()

        if field == "registry":
            try:
                reg_num = int(value)
                return [e for e in entries if e.get("registry") == reg_num]
            except ValueError:
                pass

        if field == "type":
            return [e for e in entries if value in (e.get("type") or "").lower()]

        if field == "category":
            return [e for e in entries if value in (e.get("category") or "").lower()]

        if field == "cluster":
            return [e for e in entries if (e.get("cluster") or "").lower() == value.lower()]

        if field == "word":
            return [e for e in entries if (e.get("word") or "").lower() == value.lower()]

        if field == "date":
            return [e for e in entries if (e.get("date") or "").startswith(value)]

        if field == "archived":
            want = value in ("true", "1", "yes")
            return [e for e in entries if e.get("archived") == want]

    # Free text: search in path
    q = query.lower()
    return [e for e in entries if q in e["path"].lower()]


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def print_stats(entries: list[dict]):
    """Print summary statistics."""
    total = len(entries)
    archived = sum(1 for e in entries if e["archived"])
    active = total - archived

    print(f"Total files indexed: {total}")
    print(f"  Active: {active}")
    print(f"  Archived: {archived}")
    print()

    # By category
    cats = {}
    for e in entries:
        cats[e["category"]] = cats.get(e["category"], 0) + 1
    print("By category:")
    for cat in sorted(cats, key=cats.get, reverse=True):
        print(f"  {cat:20s} {cats[cat]:5d}")
    print()

    # By type (top 20)
    types = {}
    for e in entries:
        types[e["type"]] = types.get(e["type"], 0) + 1
    print("By type (top 20):")
    for t in sorted(types, key=types.get, reverse=True)[:20]:
        print(f"  {t:30s} {types[t]:5d}")
    print()

    # Registries with most files
    regs = {}
    for e in entries:
        r = e.get("registry")
        if r is not None:
            regs[r] = regs.get(r, 0) + 1
    if regs:
        print("Top 10 registries by file count:")
        for r in sorted(regs, key=regs.get, reverse=True)[:10]:
            print(f"  reg {r:3d}: {regs[r]:4d} files")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Build or search the project file manifest")
    parser.add_argument("--search", type=str, help="Search query (free text or field:value)")
    parser.add_argument("--stats", action="store_true", help="Print summary statistics")
    parser.add_argument("--output", type=str, help="Override output path")
    args = parser.parse_args()

    if args.search:
        # Load existing manifest and search
        manifest_path = Path(args.output) if args.output else MANIFEST_PATH
        if not manifest_path.exists():
            print(f"Manifest not found at {manifest_path}. Run without --search first.")
            sys.exit(1)
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        results = search_manifest(data["files"], args.search)
        print(f"Found {len(results)} matches for '{args.search}':\n")
        for e in results:
            flag = " [archived]" if e["archived"] else ""
            print(f"  {e['path']}{flag}")
        return

    # Full rebuild
    print("Scanning project tree...")
    entries = scan_project()

    manifest = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "scripts/build_file_manifest.py",
        "total_files": len(entries),
        "total_active": sum(1 for e in entries if not e["archived"]),
        "total_archived": sum(1 for e in entries if e["archived"]),
        "files": entries,
    }

    out_path = Path(args.output) if args.output else MANIFEST_PATH
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"Manifest written: {out_path}")
    print(f"  Total: {manifest['total_files']}  Active: {manifest['total_active']}  Archived: {manifest['total_archived']}")

    if args.stats:
        print()
        print_stats(entries)


if __name__ == "__main__":
    main()
