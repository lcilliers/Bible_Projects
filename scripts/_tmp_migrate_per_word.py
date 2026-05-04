"""_tmp_migrate_per_word.py

Migrate per-word artefacts from current investigation/staging locations into
per-word subfolders under Sessions/Session_B/words/{NNN}_{word}/.

Source locations:
  - research/investigations/ai_question_test_bundle_20260429/
    (data packages, validation reports, analytic statuses, AI obslog outputs,
     parsed-capture-preview.{md,json})
  - research/investigations/chapter_assembly_prototype/
    (assembled chapters + combined extracts)
  - Sessions/Session_B/09_Analysis_output_logs/words/
    (existing parse manifests, validation reports, sessionlog files,
     readiness outputs from prior pipeline runs)

Target structure per word (e.g. R067 goodness):
  Sessions/Session_B/words/067_goodness/
    inputs/        — data package, validation, analytic-status, readiness outputs
    obslog/        — obslog .md files + sessionb-sessionlog .md files + zips
    capture/       — parse manifests, parsed-capture-preview, capture validation
    chapters/      — 6 chapter .md files + combined extract
    prior/         — older artefacts that don't fit cleanly above
    README.md      — what's in this folder + generation date

Bundle-level files (catalogue JSON, instruction docs, index files, adequacy
assessment, db growth projection, investigation-findings) move to:
  Sessions/Session_B/words/_bundle_provenance/

Usage:
  python scripts/_tmp_migrate_per_word.py            # dry-run
  python scripts/_tmp_migrate_per_word.py --live     # actually move files
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from datetime import datetime, timezone

WORDS = {
    23: "compassion", 30: "contrition", 62: "fellowship", 64: "forgiveness",
    67: "goodness", 68: "grace", 103: "love", 111: "mercy",
}

SOURCES = [
    "research/investigations/ai_question_test_bundle_20260429",
    "research/investigations/chapter_assembly_prototype",
    "Sessions/Session_B/09_Analysis_output_logs/words",
]

TARGET_BASE = os.path.join("Sessions", "Session_B", "words")
PROVENANCE = os.path.join(TARGET_BASE, "_bundle_provenance")


def slug_for(no: int) -> str:
    return f"{no:03d}_{WORDS[no]}"


def categorise(filename: str) -> str:
    """Return target subfolder for a per-word file based on filename pattern."""
    name = filename.lower()
    if "obslog" in name or "sessionb-sessionlog" in name or "sessionlog" in name:
        return "obslog"
    if any(t in name for t in ["data v2.md", "-data v2.md"]) or name.endswith("-data v2.md"):
        return "inputs"
    if "-data.md" in name or "data.md" in name and "preview" not in name:
        return "inputs"
    if "validation" in name or "analytic-status" in name or "readiness" in name:
        return "inputs"
    if "parse-manifest" in name or "capture-preview" in name or "capture" in name:
        return "capture"
    if "ch1-assembled" in name or "ch2-assembled" in name or "ch3-assembled" in name \
       or "ch4-assembled" in name or "ch5-assembled" in name or "ch6-assembled" in name \
       or "assembled-prose-extract" in name or "assembled-prototype" in name:
        return "chapters"
    if name.endswith(".zip"):
        return "obslog"
    return "prior"


def detect_word_no(path: str) -> int | None:
    """Match a path to a registry number based on filename or parent folder."""
    parts = re.split(r"[/\\]", path)
    for part in parts:
        lower = part.lower()
        # NNN- or rNNN forms
        m = re.search(r"\br?(\d{2,3})\b", lower)
        if m:
            try:
                no = int(m.group(1))
                if no in WORDS:
                    # Verify the word string is also present in the parent folder
                    # or filename — avoid false positives from random NNN matches
                    word = WORDS[no]
                    full_lower = path.lower()
                    if word in full_lower or f"r{no:03d}" in full_lower or f"-{no:03d}-" in full_lower:
                        return no
            except ValueError:
                pass
        for no, word in WORDS.items():
            if word in lower and (str(no) in lower or f"r{no:03d}" in lower or
                                   f"-{no:03d}-" in lower):
                return no
    # Last resort: word-only match in basename
    base_lower = os.path.basename(path).lower()
    for no, word in WORDS.items():
        if word in base_lower:
            return no
    return None


def is_bundle_level(filename: str) -> bool:
    """Files that span the whole bundle, not specific to one word."""
    name = filename.lower()
    bundle_patterns = [
        "wa-obs-question-catalogue",
        "wa-second-tier-analysis-instruction",
        "wa-obs-framework-second-tier",
        "_index.md",
        "capture-preview-index",
        "data-adequacy-assessment",
        "investigation-findings",
        "db-growth-projection",
    ]
    return any(p in name for p in bundle_patterns)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true")
    args = ap.parse_args()

    plan: dict[int, list[tuple[str, str]]] = {no: [] for no in WORDS}
    bundle_plan: list[tuple[str, str]] = []
    unassigned: list[str] = []

    for src in SOURCES:
        if not os.path.exists(src):
            print(f"[skip] source missing: {src}")
            continue
        for root, dirs, files in os.walk(src):
            for f in files:
                full = os.path.join(root, f)
                no = detect_word_no(full)
                if no is None:
                    if is_bundle_level(f):
                        target = os.path.join(PROVENANCE, f)
                        bundle_plan.append((full, target))
                    else:
                        unassigned.append(full)
                    continue
                subdir = categorise(f)
                target = os.path.join(TARGET_BASE, slug_for(no), subdir, f)
                plan[no].append((full, target))

    print("=== Migration plan ===\n")
    grand_total = 0
    for no in sorted(WORDS):
        items = plan[no]
        if not items:
            continue
        print(f"\nR{no:03d} {WORDS[no]} ({len(items)} files):")
        # group by target subdir
        by_subdir: dict[str, list[tuple[str, str]]] = {}
        for src, dst in items:
            sub = os.path.basename(os.path.dirname(dst))
            by_subdir.setdefault(sub, []).append((src, dst))
        for sub in ("inputs", "obslog", "capture", "chapters", "prior"):
            sub_items = by_subdir.get(sub, [])
            if not sub_items:
                continue
            print(f"  → {sub}/ ({len(sub_items)} files)")
            for src, dst in sub_items[:3]:
                print(f"      {os.path.relpath(src):60s} → {os.path.basename(dst)}")
            if len(sub_items) > 3:
                print(f"      ... and {len(sub_items)-3} more")
        grand_total += len(items)

    if bundle_plan:
        print(f"\n_bundle_provenance/ ({len(bundle_plan)} files):")
        for src, dst in bundle_plan[:5]:
            print(f"  {os.path.relpath(src):60s} → {os.path.basename(dst)}")
        if len(bundle_plan) > 5:
            print(f"  ... and {len(bundle_plan)-5} more")
        grand_total += len(bundle_plan)

    if unassigned:
        print(f"\nUnassigned ({len(unassigned)} files — will stay where they are):")
        for f in unassigned[:10]:
            print(f"  {os.path.relpath(f)}")
        if len(unassigned) > 10:
            print(f"  ... and {len(unassigned)-10} more")

    print(f"\n=== Total: {grand_total} files to migrate ===")

    if not args.live:
        print("\n[DRY-RUN] No files moved. Re-run with --live to execute.")
        return 0

    # === Live migration ===
    print("\n=== Migrating ===\n")
    moved = 0
    skipped = 0
    errors: list[str] = []

    def safe_move(src: str, dst: str) -> bool:
        nonlocal moved, skipped
        if not os.path.exists(src):
            errors.append(f"source vanished: {src}")
            return False
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        # If target exists, append a numeric suffix or skip if same content
        if os.path.exists(dst):
            try:
                if os.path.getsize(src) == os.path.getsize(dst):
                    # Likely same file — just remove the source
                    os.remove(src)
                    skipped += 1
                    return True
            except OSError:
                pass
            # Find a non-clashing name
            base, ext = os.path.splitext(dst)
            n = 1
            while os.path.exists(f"{base}__{n}{ext}"):
                n += 1
            dst = f"{base}__{n}{ext}"
        shutil.move(src, dst)
        moved += 1
        return True

    for no in sorted(WORDS):
        for src, dst in plan[no]:
            safe_move(src, dst)
    for src, dst in bundle_plan:
        safe_move(src, dst)

    # Per-word READMEs
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for no in sorted(WORDS):
        if not plan[no]:
            continue
        slug = slug_for(no)
        word_dir = os.path.join(TARGET_BASE, slug)
        readme = os.path.join(word_dir, "README.md")
        if os.path.exists(readme):
            continue
        with open(readme, "w", encoding="utf-8") as f:
            f.write(f"# R{no:03d} {WORDS[no].title()} — Session B Artefact Bundle\n\n")
            f.write(f"**Consolidated:** {today}\n\n")
            f.write(f"**Folder layout:**\n\n")
            f.write(f"- `inputs/` — registry data package, validation report, analytic status, readiness outputs (Stage 2 prerequisites)\n")
            f.write(f"- `obslog/` — comprehensive obslog `.md` and session log `.md` (AI's Stage 2a/2b/2c output)\n")
            f.write(f"- `capture/` — parse manifests, parsed-capture-preview, validation records (CC's Phase 2 writer output)\n")
            f.write(f"- `chapters/` — six assembled chapter files + combined extract (mechanically assembled from DB)\n")
            f.write(f"- `prior/` — older artefacts from earlier pipeline iterations (kept as historical record)\n\n")
            f.write(f"**Capture model:** see `capture/` for the parser version applied. Chapters were assembled by `scripts/_tmp_assemble_chapters_full.py` reading from `database/bible_research.db` (schema v3.17.0) on {today}.\n")

    # Bundle README
    if bundle_plan:
        readme = os.path.join(PROVENANCE, "README.md")
        if not os.path.exists(readme):
            os.makedirs(PROVENANCE, exist_ok=True)
            with open(readme, "w", encoding="utf-8") as f:
                f.write(f"# v1.8 8-Word Bundle Provenance\n\n")
                f.write(f"**Consolidated:** {today}\n\n")
                f.write("Bundle-level artefacts that span all 8 words tested under v1.8 (R023, R030, R062, R064, R067, R068, R103, R111). Per-word artefacts moved into `Sessions/Session_B/words/{NNN}_{word}/` subfolders.\n\n")
                f.write("**Contents:**\n\n")
                f.write("- Catalogue JSON (`WA-obs-question-catalogue-v2-2026-04-29.json`)\n")
                f.write("- Second-tier analysis instruction (legacy v1.7 model)\n")
                f.write("- Framework definitions (T0–T7)\n")
                f.write("- Bundle indexes (`_index.md`, `capture-preview-index.md`)\n")
                f.write("- Investigation findings (chapter-assembly feasibility, data-adequacy assessment, DB growth projection)\n")

    print(f"\n=== Migration complete ===")
    print(f"  Moved: {moved}")
    print(f"  Skipped (duplicate at target): {skipped}")
    if errors:
        print(f"  Errors: {len(errors)}")
        for e in errors[:5]:
            print(f"    {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
