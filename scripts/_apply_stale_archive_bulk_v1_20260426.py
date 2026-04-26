"""_apply_stale_archive_bulk_v1_20260426.py — one-off bulk archive of stale versions.

Implements the scan in outputs/investigations/stale-version-scan-v1-20260426.md.
Skips Word lock files (~$). Uses git mv so file history is preserved.

Run with --dry-run first; commits actual moves only with --live.
Archive script; archive after the run.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from collections import defaultdict

SCAN_DIRS = [
    "data/imports/WA/Workflow/Framework_B/Session_B",
    "data/imports/WA/Workflow/Sessionlogs",
    "data/imports/WA/Workflow/methodology_logs",
    "data/imports/WA/Session_B_Analysis",
    "data/imports/WA/Session_B_Verse_Context",
    "data/imports/WA/Session_B_Dimension_Review",
    "data/imports/WA/Session_C_Words",
    "data/imports/WA/Patches",
    "data/imports/WA/Prose",
    "data/imports/WA/Word_Data",
    "data/exports/session_a",
    "data/exports/session_a/terms",
    "data/exports/verse_context",
    "data/exports/dimension_review",
    "data/exports/Session C",
    "data/exports/session_d",
    "data/exports/STEP Extracts",
    "data/exports/reference",
    "data/schema",
    "outputs/markdown",
    "outputs/reports/programme",
    "outputs/reports/words",
    "outputs/investigations",
    "outputs/docx",
    "outputs/pdf",
    "outputs/session-logs",
    "docs",
    "scripts",
    "engine",
    "analytics",
]

RE_VDATE = re.compile(r"^(.+)-v([0-9]+(?:[._][0-9]+)?)-((?:\d{8})|(?:\d{4}-\d{2}-\d{2}))\.([A-Za-z0-9]+)$")
RE_DATE = re.compile(r"^(.+)-((?:\d{8})|(?:\d{4}-\d{2}-\d{2}))\.([A-Za-z0-9]+)$")


def normalise_date(s: str) -> int:
    if len(s) == 10 and s[4] == "-":
        return int(s.replace("-", ""))
    return int(s)


def parse_version(v: str) -> tuple:
    parts = v.replace(".", "_").split("_")
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return (0,)


def to_posix(p: str) -> str:
    return p.replace(os.sep, "/")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="actually move files (default: dry-run)")
    args = ap.parse_args()

    groups: dict = defaultdict(list)
    for d in SCAN_DIRS:
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            path = os.path.join(d, fn)
            if not os.path.isfile(path):
                continue
            if fn.startswith("~$"):
                continue
            m = RE_VDATE.match(fn)
            if m:
                base, ver, date, ext = m.groups()
                key = (d, f"{base}.{ext}")
                groups[key].append((fn, parse_version(ver), normalise_date(date), True))
                continue
            m = RE_DATE.match(fn)
            if m:
                base, date, ext = m.groups()
                key = (d, f"{base}.{ext}")
                groups[key].append((fn, (0,), normalise_date(date), False))
                continue

    duplicates = {k: v for k, v in groups.items() if len(v) > 1}

    moves = []
    for (d, key), files in duplicates.items():
        files_sorted = sorted(files, key=lambda x: (x[2], x[1]), reverse=True)
        older = files_sorted[1:]
        archive_dir = os.path.join(d, "archive")
        for fn, _, _, _ in older:
            src = os.path.join(d, fn)
            dst = os.path.join(archive_dir, fn)
            moves.append((src, dst))

    print(f"Found {len(duplicates)} duplicate groups; {len(moves)} files to archive.")

    if not args.live:
        print("[DRY-RUN] no moves performed.")
        for src, dst in moves[:20]:
            print(f"  would mv  {to_posix(src):60s}  ->  {to_posix(dst)}")
        if len(moves) > 20:
            print(f"  ... and {len(moves) - 20} more")
        return 0

    archive_dirs = sorted({os.path.dirname(dst) for _, dst in moves})
    for ad in archive_dirs:
        os.makedirs(ad, exist_ok=True)

    ok = 0
    failures = []
    for src, dst in moves:
        r = subprocess.run(
            ["git", "mv", to_posix(src), to_posix(dst)],
            capture_output=True,
            text=True,
        )
        if r.returncode == 0:
            ok += 1
        else:
            failures.append((src, dst, r.stderr.strip()))

    print(f"\n[LIVE] moved {ok}/{len(moves)} files.")
    if failures:
        print(f"Failures: {len(failures)}")
        for s, d, e in failures[:20]:
            print(f"  {to_posix(s)} -> {to_posix(d)}")
            print(f"    {e}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
