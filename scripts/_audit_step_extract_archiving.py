"""Auditor + applicator for STEP Extracts archiving.

Groups files in data/exports/STEP Extracts/ by {word}_{reg}_{scope},
keeps the latest-dated file per group (and the highest v{n} within
that date), and lists older siblings as candidates for archive to
data/exports/archive/STEP Extracts/.

Usage:
    # Dry-run (default): writes a markdown plan, moves nothing.
    python scripts/_audit_step_extract_archiving.py

    # Apply: moves each file listed in the plan to the archive folder.
    python scripts/_audit_step_extract_archiving.py --apply
"""
from __future__ import annotations

import argparse
import re
import shutil
from collections import defaultdict
from datetime import datetime
from pathlib import Path

SRC = Path("data/exports/STEP Extracts")
DST = Path("data/exports/archive/STEP Extracts")
OUT = Path("outputs/investigations") / f"step-extract-archive-plan-{datetime.now().strftime('%Y%m%d')}.md"

# Expected filename pattern:
#   {word}_{reg}_{scope}_{YYYYMMDD}[_v{n}].json
# where {word} may contain underscores (e.g. "Inner_being"). We therefore
# match from the right: ...{YYYYMMDD}[_v{n}].json
PATTERN = re.compile(
    r"^(?P<stem>.+?)_(?P<date>\d{8})(?:_v(?P<ver>\d+))?\.json$"
)


def classify(files: list[Path]) -> tuple[dict, list[str]]:
    """Group files by stem (word_reg_scope). Return (groups, unparsed)."""
    groups: dict[str, list[dict]] = defaultdict(list)
    unparsed: list[str] = []
    for f in files:
        m = PATTERN.match(f.name)
        if not m:
            unparsed.append(f.name)
            continue
        groups[m.group("stem")].append({
            "path": f,
            "date": m.group("date"),
            "ver": int(m.group("ver") or 0),
        })
    return groups, unparsed


def select_moves(groups: dict) -> tuple[list[dict], dict]:
    """For each group, select the latest (keep) and the rest (archive)."""
    moves = []
    summary: dict[str, int] = {"groups": 0, "keep": 0, "archive": 0, "singletons": 0}
    for stem, entries in sorted(groups.items()):
        summary["groups"] += 1
        entries.sort(key=lambda e: (e["date"], e["ver"]), reverse=True)
        latest = entries[0]
        summary["keep"] += 1
        if len(entries) == 1:
            summary["singletons"] += 1
            continue
        for e in entries[1:]:
            summary["archive"] += 1
            moves.append({
                "stem": stem,
                "source": e["path"],
                "target": DST / e["path"].name,
                "reason": f"superseded by {latest['path'].name}",
            })
    return moves, summary


def write_plan(moves: list[dict], summary: dict, unparsed: list[str]) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    lines.append("# STEP Extract Archive Plan — Dry Run")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Source folder:** `{SRC}`")
    lines.append(f"**Archive target:** `{DST}`")
    lines.append("")
    lines.append("This plan is produced by `scripts/_audit_step_extract_archiving.py`. "
                 "**No files have been moved.** Review, then execute by passing `--apply` to the script.")
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|---|---:|")
    lines.append(f"| Groups (unique word+registry+scope) | {summary['groups']} |")
    lines.append(f"| Latest files kept in place | {summary['keep']} |")
    lines.append(f"| Older files to archive | {summary['archive']} |")
    lines.append(f"| Singletons (no siblings; unchanged) | {summary['singletons']} |")
    if unparsed:
        lines.append(f"| Files that did not match expected pattern | {len(unparsed)} |")
    lines.append("")

    if unparsed:
        lines.append("## Files that did not match the expected pattern")
        lines.append("")
        lines.append("The following filenames did not match `{stem}_{YYYYMMDD}[_v{n}].json`. "
                     "They will be ignored by an --apply run. Spot-check these.")
        lines.append("")
        for name in unparsed:
            lines.append(f"- `{name}`")
        lines.append("")

    lines.append("## Proposed moves")
    lines.append("")
    if not moves:
        lines.append("_No moves proposed — every group is a singleton._")
    else:
        current_stem = None
        for m in sorted(moves, key=lambda x: (x["stem"], x["source"].name)):
            if m["stem"] != current_stem:
                current_stem = m["stem"]
                lines.append(f"### `{current_stem}`")
                lines.append("")
                lines.append(f"| Source | → | Target | Reason |")
                lines.append(f"|---|:---:|---|---|")
            rel_src = m["source"].relative_to(Path.cwd()) if m["source"].is_absolute() else m["source"]
            rel_tgt = m["target"]
            lines.append(f"| `{rel_src}` | → | `{rel_tgt}` | {m['reason']} |")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")


def apply_moves(moves: list[dict]) -> tuple[int, list[str]]:
    """Execute the archive moves. Returns (count_moved, errors)."""
    DST.mkdir(parents=True, exist_ok=True)
    moved = 0
    errors: list[str] = []
    for m in moves:
        src, tgt = m["source"], m["target"]
        if not src.exists():
            errors.append(f"missing: {src}")
            continue
        if tgt.exists():
            errors.append(f"target already exists: {tgt}")
            continue
        try:
            shutil.move(str(src), str(tgt))
            moved += 1
        except Exception as e:
            errors.append(f"{src} -> {tgt}: {e!s}")
    return moved, errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true",
                        help="execute the archive moves (default: dry-run only)")
    args = parser.parse_args()

    if not SRC.is_dir():
        raise SystemExit(f"Source folder not found: {SRC}")
    files = [f for f in sorted(SRC.iterdir()) if f.is_file() and f.suffix == ".json"]
    groups, unparsed = classify(files)
    moves, summary = select_moves(groups)
    write_plan(moves, summary, unparsed)
    print(f"Groups: {summary['groups']}  "
          f"Archive: {summary['archive']}  "
          f"Keep: {summary['keep']}  "
          f"Unparsed: {len(unparsed)}")
    print(f"Plan written: {OUT}")

    if args.apply:
        moved, errors = apply_moves(moves)
        print(f"APPLIED: {moved} files moved to {DST}")
        if errors:
            print(f"ERRORS ({len(errors)}):")
            for e in errors:
                print(f"  {e}")


if __name__ == "__main__":
    main()
