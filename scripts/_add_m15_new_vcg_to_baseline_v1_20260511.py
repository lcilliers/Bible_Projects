"""_add_m15_new_vcg_to_baseline_v1_20260511.py — read+write JSON only.

Parse the per-sub-group 'verse-meanings-v2' markdown files. The v2 files
contain a 'Section 2 — Derived Verse Context Groups' that proposes new
VCG groupings (VCG-A-01, VCG-A-02, etc.). For each baseline verse, add:

  new_vcg          — the proposed new VCG code/title/description + any
                     verse-level annotation (e.g. [MISASSIGNED note])
  vcg_comparison   — side-by-side text of the DB VCG description and the
                     proposed new VCG description, so AI/human can judge
                     whether they describe the same grouping concept

Reads:
  - Sessions/Session_Clusters/M15/m15-baseline-verses-v2-20260511.json
    (or v1 if v2 not present — but v2 should be present from the meaning
    layer)
  - wa-m15-{a,b,c,d,e,f,g,boundary}-verse-meanings-v2-2026-05-11.md

Writes:
  - Sessions/Session_Clusters/M15/m15-baseline-verses-v3-20260511.json
  - Sessions/Session_Clusters/M15/m15-new-vcg-coverage-v1-20260511.md
"""
from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
MEANINGS_DIR = os.path.join(M15_DIR, "files - failed session")
BASELINE_IN = os.path.join(M15_DIR, "m15-baseline-verses-v2-20260511.json")
BASELINE_OUT = os.path.join(M15_DIR, "m15-baseline-verses-v3-20260511.json")
COVERAGE_REPORT = os.path.join(M15_DIR, "m15-new-vcg-coverage-v1-20260511.md")
DB_PATH = os.path.join("database", "bible_research.db")

SUBGROUPS = ["a", "b", "c", "d", "e", "f", "g", "boundary"]

# Books that prefix a reference
_BOOKS = {
    "Gen", "Exo", "Lev", "Num", "Deu",
    "Jos", "Judg", "Rut", "1Sa", "2Sa", "1Ki", "2Ki", "1Ch", "2Ch",
    "Ezr", "Neh", "Est", "Job", "Psa", "Pro", "Ecc", "Song",
    "Isa", "Jer", "Lam", "Eze", "Dan", "Hos", "Joel", "Amo", "Oba",
    "Jon", "Mic", "Nah", "Hab", "Zep", "Hag", "Zec", "Mal",
    "Mat", "Mar", "Luk", "Joh", "Act",
    "Rom", "1Cor", "2Cor", "Gal", "Eph", "Phili", "Col",
    "1Th", "2Th", "1Ti", "2Ti", "Tit", "Phlm", "Heb",
    "Jam", "1Pe", "2Pe", "1Jo", "2Jo", "3Jo", "Jud", "Rev",
}

_VCG_HEADING_RE = re.compile(
    r"^###\s+(VCG-[A-Za-z0-9]+-\d+)\s*[—-]\s*(.+?)\s*$"
)
_SECTION2_RE = re.compile(r"^##\s+Section\s+2\b", re.IGNORECASE)
_SECTION3PLUS_RE = re.compile(r"^##\s+Section\s+[3-9]\b", re.IGNORECASE)
_BULLET_RE = re.compile(r"^[-*]\s+(.+?)\s*$")
_REF_TOKEN_RE = re.compile(
    r"^\s*([A-Za-z0-9]+)\s+(\d+):(\d+(?:[a-z])?)\s*$"
)
_CHAPVERSE_ONLY_RE = re.compile(r"^\s*(\d+):(\d+(?:[a-z])?)\s*$")
_ITALIC_DESC_RE = re.compile(r"^\*(.+)\*\s*$")
_SUBSECTION_RE = re.compile(r"^\*\*(.+?):\*\*\s*$")
_BRACKET_NOTE_RE = re.compile(r"\[([^\]]+)\]")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def split_refs(refs_text: str, last_book: str | None) -> tuple[list[str], str | None]:
    """Split a comma-separated reference string into canonical refs.
    Inherit book from last_book when a part lacks a book prefix.
    Returns (refs, new_last_book)."""
    out: list[str] = []
    for part in refs_text.split(","):
        p = part.strip()
        if not p:
            continue
        m = _REF_TOKEN_RE.match(p)
        if m:
            book, ch, vs = m.group(1), m.group(2), m.group(3)
            if book in _BOOKS:
                last_book = book
                out.append(f"{book} {ch}:{vs}")
                continue
        m = _CHAPVERSE_ONLY_RE.match(p)
        if m and last_book:
            out.append(f"{last_book} {m.group(1)}:{m.group(2)}")
            continue
        # Unparseable — try heuristic: maybe `Pro 1:5a` or similar; otherwise drop
        if last_book:
            # Try last_book + p if p looks like chap:vs
            m2 = re.match(r"^(\d+):(\d+(?:[a-z])?)$", p)
            if m2:
                out.append(f"{last_book} {m2.group(1)}:{m2.group(2)}")
                continue
    return out, last_book


def parse_v2_file(path: str, sg_letter: str) -> tuple[list[dict], dict]:
    """Return (assignments, vcg_meta).

    assignments: list of {reference, sg_letter, new_vcg_code, subsection, annotation}
    vcg_meta:    {code: {title, description, source_file}}
    """
    assignments: list[dict] = []
    vcg_meta: dict[str, dict] = {}
    src = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_section_2 = False
    current_vcg: str | None = None
    current_title: str | None = None
    current_desc: str | None = None
    current_subsection: str | None = None
    last_book: str | None = None
    # Wait for italic description line right after heading
    awaiting_desc_for: str | None = None

    for raw in lines:
        line = raw.rstrip("\n")
        # Section gating
        if _SECTION2_RE.match(line):
            in_section_2 = True
            continue
        if _SECTION3PLUS_RE.match(line):
            in_section_2 = False
            continue
        if not in_section_2:
            continue
        # VCG heading
        m = _VCG_HEADING_RE.match(line)
        if m:
            current_vcg = m.group(1)
            current_title = m.group(2)
            current_desc = None
            current_subsection = None
            awaiting_desc_for = current_vcg
            last_book = None
            vcg_meta[current_vcg] = {
                "code": current_vcg,
                "title": current_title,
                "description": None,
                "source_file": src,
                "sg_letter": sg_letter,
            }
            continue
        # Italic description right after heading (allowing blank lines between)
        if awaiting_desc_for and current_vcg:
            stripped = line.strip()
            if stripped == "":
                continue
            md = _ITALIC_DESC_RE.match(stripped)
            if md:
                current_desc = md.group(1).strip()
                vcg_meta[current_vcg]["description"] = current_desc
                awaiting_desc_for = None
                continue
            # If we hit content before description, assume no description present
            awaiting_desc_for = None
        # Subsection header within VCG
        ms = _SUBSECTION_RE.match(line.strip())
        if ms and current_vcg:
            current_subsection = ms.group(1).strip()
            continue
        # Bullet
        mb = _BULLET_RE.match(line)
        if mb and current_vcg:
            content = mb.group(1)
            # Split refs side from text side at first em-dash (or " - " /" — ")
            split_at = None
            for sep in (" — ", " – ", " - "):
                idx = content.find(sep)
                if idx != -1:
                    split_at = (idx, len(sep))
                    break
            if split_at:
                refs_text = content[:split_at[0]]
                text_side = content[split_at[0] + split_at[1]:]
            else:
                refs_text = content
                text_side = ""
            # Annotation
            ann = None
            am = _BRACKET_NOTE_RE.search(text_side)
            if am:
                ann = am.group(1)
            refs, last_book = split_refs(refs_text, last_book)
            for ref in refs:
                assignments.append({
                    "reference": ref,
                    "sg_letter": sg_letter,
                    "new_vcg_code": current_vcg,
                    "subsection": current_subsection,
                    "annotation": ann,
                    "verse_text_excerpt": text_side.strip(),
                    "source_file": src,
                })
    return assignments, vcg_meta


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    print("Parsing v2 files (derived VCG sections)...")
    all_assignments: list[dict] = []
    # Namespace by sub-group letter — BOUNDARY's file reuses VCG-B-NN codes
    # for its own VCGs, colliding with M15-B. Key by (sg_letter, code).
    all_meta: dict[tuple[str, str], dict] = {}
    per_file_counts: dict[str, int] = {}
    for sg in SUBGROUPS:
        path = os.path.join(MEANINGS_DIR, f"wa-m15-{sg}-verse-meanings-v2-2026-05-11.md")
        if not os.path.exists(path):
            print(f"  [WARN] missing: {path}")
            continue
        asn, meta = parse_v2_file(path, sg)
        per_file_counts[os.path.basename(path)] = len(asn)
        n_vcgs = len(meta)
        print(f"  {os.path.basename(path):<55s}  refs={len(asn):>4d}  VCGs={n_vcgs}")
        all_assignments.extend(asn)
        # Namespace by sg_letter
        for code, m in meta.items():
            all_meta[(sg, code)] = m
    print(f"  TOTAL refs parsed: {len(all_assignments)}  VCGs defined: {len(all_meta)}")

    # Index assignments by (reference, sg_letter) — preferred lookup
    by_ref_sg: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for a in all_assignments:
        by_ref_sg[(a["reference"], a["sg_letter"])].append(a)
    # Also a fallback by reference alone
    by_ref: dict[str, list[dict]] = defaultdict(list)
    for a in all_assignments:
        by_ref[a["reference"]].append(a)

    # Fetch DB VCG descriptions
    print()
    print("Fetching DB VCG context_descriptions for M15...")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    db_vcgs: dict[int, dict] = {}
    for r in conn.execute("""
        SELECT DISTINCT vcg.id, vcg.group_code, vcg.context_description
          FROM verse_context_group vcg
          JOIN vcg_term vt ON vt.vcg_id = vcg.id AND COALESCE(vt.delete_flagged,0)=0
          JOIN mti_terms mt ON mt.id = vt.mti_term_id
         WHERE mt.cluster_code='M15' AND COALESCE(vcg.delete_flagged,0)=0
    """):
        db_vcgs[r["id"]] = {
            "code": r["group_code"],
            "description": r["context_description"],
        }
    print(f"  DB VCG rows for M15: {len(db_vcgs)}")
    conn.close()

    # Load baseline
    print()
    print(f"Loading baseline: {BASELINE_IN}")
    with open(BASELINE_IN, "r", encoding="utf-8") as f:
        baseline = json.load(f)
    print(f"  rows: {len(baseline['verses'])}")

    # Layer new_vcg + vcg_comparison
    matched = 0
    unmatched = 0
    sg_mismatch_matched = 0  # matched via fallback (different sub-group)
    multi_match_flagged = 0
    annotations_attached = 0
    for v in baseline["verses"]:
        ref = v["reference"]
        sg_code = v["current"].get("subgroup_code")
        sg_letter = sg_code.split("-")[-1].lower() if sg_code else None

        chosen = None
        match_type = None
        candidates = []
        if sg_letter:
            cands = by_ref_sg.get((ref, sg_letter), [])
            if cands:
                chosen = cands[0]
                candidates = cands
                match_type = "subgroup_aligned"
        if chosen is None:
            cands = by_ref.get(ref, [])
            if cands:
                chosen = cands[0]
                candidates = cands
                match_type = "subgroup_fallback"
                sg_mismatch_matched += 1

        if chosen is None:
            unmatched += 1
            continue
        matched += 1
        if len(candidates) > 1:
            multi_match_flagged += 1
        if chosen.get("annotation"):
            annotations_attached += 1

        # Resolve meta using the chosen assignment's sg_letter (namespaced)
        meta = all_meta.get((chosen["sg_letter"], chosen["new_vcg_code"]), {})
        v["new_vcg"] = {
            "code": chosen["new_vcg_code"],
            "source_subgroup": chosen["sg_letter"],
            "title": meta.get("title"),
            "description": meta.get("description"),
            "subsection": chosen.get("subsection"),
            "verse_annotation": chosen.get("annotation"),
            "match_type": match_type,
            "candidates_seen": len(candidates),
            "source_file": chosen["source_file"],
        }

        # Build vcg_comparison
        db_grp_id = v["current"].get("group_id")
        db_info = db_vcgs.get(db_grp_id) if db_grp_id else None
        v["vcg_comparison"] = {
            "db": {
                "group_id": db_grp_id,
                "code": v["current"].get("group_code"),
                "description": db_info["description"] if db_info else None,
            },
            "new": {
                "code": chosen["new_vcg_code"],
                "title": meta.get("title"),
                "description": meta.get("description"),
            },
        }

    # Update metadata
    baseline["metadata"]["schema_version"] = "baseline-v3"
    baseline["metadata"]["generated_at"] = now_iso()
    baseline["metadata"]["new_vcg_layer"] = {
        "source": "Sessions/Session_Clusters/M15/files - failed session/wa-m15-*-verse-meanings-v2-2026-05-11.md",
        "files_parsed": list(per_file_counts.keys()),
        "ref_assignments_parsed": len(all_assignments),
        "new_vcgs_defined": len(all_meta),
        "baseline_rows_with_new_vcg": matched,
        "baseline_rows_without_new_vcg": unmatched,
        "matched_via_subgroup_fallback": sg_mismatch_matched,
        "verses_with_multiple_candidates": multi_match_flagged,
        "verses_with_annotation": annotations_attached,
    }

    # Write output
    with open(BASELINE_OUT, "w", encoding="utf-8") as f:
        json.dump(baseline, f, ensure_ascii=False, indent=2)
    print()
    print(f"  matched (new_vcg added):       {matched}")
    print(f"  unmatched:                     {unmatched}")
    print(f"  matched via fallback subgroup: {sg_mismatch_matched}")
    print(f"  verses with multi-candidates:  {multi_match_flagged}")
    print(f"  verses with annotation:        {annotations_attached}")
    print(f"  written: {BASELINE_OUT}")
    print(f"  size: {os.path.getsize(BASELINE_OUT):,} bytes")

    # Coverage report
    print()
    print(f"Writing coverage report: {COVERAGE_REPORT}")
    # missing by sub-group
    missing_by_sg: dict[str, list[dict]] = defaultdict(list)
    for v in baseline["verses"]:
        if "new_vcg" not in v:
            sg = v["current"].get("subgroup_code") or "(unrouted)"
            missing_by_sg[sg].append(v)
    # Sample of vcg_comparison pairs (5 per sub-group) for human read
    sample_by_sg: dict[str, list[dict]] = defaultdict(list)
    for v in baseline["verses"]:
        if "vcg_comparison" not in v:
            continue
        sg = v["current"].get("subgroup_code") or "(unrouted)"
        if len(sample_by_sg[sg]) < 3:
            sample_by_sg[sg].append(v)

    with open(COVERAGE_REPORT, "w", encoding="utf-8") as f:
        f.write("# M15 new-VCG coverage and comparison report\n\n")
        f.write(f"**Generated:** {now_iso()}\n\n")
        f.write(f"**Source v2 files:** "
                f"`Sessions/Session_Clusters/M15/files - failed session/wa-m15-*-verse-meanings-v2-2026-05-11.md`\n\n")
        f.write(f"**Baseline rows:** {len(baseline['verses'])}\n")
        f.write(f"**Ref assignments parsed:** {len(all_assignments)}\n")
        f.write(f"**New VCGs defined:** {len(all_meta)}\n")
        f.write(f"**Rows with new_vcg attached:** {matched}\n")
        f.write(f"**Rows MISSING new_vcg:** {unmatched}\n")
        f.write(f"**Matched via sub-group fallback (verse in different sg's v2 file):** "
                f"{sg_mismatch_matched}\n")
        f.write(f"**Verses with multiple candidate VCGs:** {multi_match_flagged}\n")
        f.write(f"**Verses with verse-level annotation:** {annotations_attached}\n\n")

        f.write("## Per-file counts\n\n| File | refs | VCGs |\n|---|---:|---:|\n")
        for sg in SUBGROUPS:
            fn = f"wa-m15-{sg}-verse-meanings-v2-2026-05-11.md"
            n_refs = per_file_counts.get(fn, 0)
            n_vcgs = sum(1 for k, v in all_meta.items() if k[0] == sg)
            f.write(f"| `{fn}` | {n_refs} | {n_vcgs} |\n")

        f.write("\n## New VCGs defined per sub-group\n\n")
        by_sg: dict[str, list] = defaultdict(list)
        for (sg_let, code), m in sorted(all_meta.items()):
            by_sg[sg_let].append(m)
        for sg in sorted(by_sg):
            f.write(f"### {sg.upper()}\n\n")
            for m in by_sg[sg]:
                f.write(f"- **{m['code']}** — {m['title']}\n")
                if m.get("description"):
                    f.write(f"  - _{m['description']}_\n")
            f.write("\n")

        f.write("## Rows MISSING new_vcg by sub-group\n\n")
        for sg in sorted(missing_by_sg):
            rows = missing_by_sg[sg]
            f.write(f"### {sg} — {len(rows)} missing\n\n")
            f.write("| vr_id | reference | strongs | translit | status |\n|---:|---|---|---|---|\n")
            for v in rows[:150]:
                t = v["term"]
                f.write(f"| {v['vr_id']} | {v['reference']} | {t['strongs']} | "
                        f"{t['translit']} | {v['current'].get('status','?')} |\n")
            if len(rows) > 150:
                f.write(f"\n_({len(rows) - 150} more not shown)_\n")
            f.write("\n")

        f.write("## Sample vcg_comparison pairs (3 per sub-group)\n\n")
        for sg in sorted(sample_by_sg):
            f.write(f"### {sg}\n\n")
            for v in sample_by_sg[sg]:
                cmp = v["vcg_comparison"]
                f.write(f"**{v['reference']}**  ({v['term']['strongs']} {v['term']['translit']})\n\n")
                f.write(f"- DB **{cmp['db']['code']}**: _{cmp['db']['description'] or '(no description)'}_\n")
                f.write(f"- NEW **{cmp['new']['code']}** ({cmp['new']['title']}): "
                        f"_{cmp['new']['description'] or '(no description)'}_\n\n")
    print(f"  written: {COVERAGE_REPORT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
