"""_add_m15_meanings_to_baseline_v1_20260511.py — read+write JSON only.

Parse the per-sub-group 'verse-meanings-v1' markdown files in
'Sessions/Session_Clusters/M15/files - failed session/' and layer the
'meaning' text into the baseline JSON as a sibling key alongside 'current'.

Reads:
  - Sessions/Session_Clusters/M15/m15-baseline-verses-v1-20260511.json
  - wa-m15-{a,b,c,d,e,f,g,boundary}-verse-meanings-v1-2026-05-11.md (8 files)

Writes:
  - Sessions/Session_Clusters/M15/m15-baseline-verses-v2-20260511.json
  - Sessions/Session_Clusters/M15/m15-meaning-coverage-v1-20260511.md
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M15_DIR = os.path.join(ROOT, "Sessions", "Session_Clusters", "M15")
MEANINGS_DIR = os.path.join(M15_DIR, "files - failed session")
BASELINE_IN = os.path.join(M15_DIR, "m15-baseline-verses-v1-20260511.json")
BASELINE_OUT = os.path.join(M15_DIR, "m15-baseline-verses-v2-20260511.json")
COVERAGE_REPORT = os.path.join(M15_DIR, "m15-meaning-coverage-v1-20260511.md")

SUBGROUPS = ["a", "b", "c", "d", "e", "f", "g", "boundary"]

# Strong's regex — H or G followed by digits, optional letter suffix
_STRONGS_RE = re.compile(r"\b([HG]\d{1,4}[A-Z]?)\b")
_TABLE_HDR_RE = re.compile(r"^\|\s*Reference\s*\|", re.IGNORECASE)
_TABLE_SEP_RE = re.compile(r"^\|\s*[-:]+\s*\|")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_meaning_table(path: str) -> list[dict]:
    """Return list of {reference, strongs, span_label, vcg, verse, meaning}."""
    rows = []
    src = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_table = False
    header_passed = False
    for raw in lines:
        line = raw.rstrip("\n")
        # Detect table header
        if _TABLE_HDR_RE.match(line):
            in_table = True
            header_passed = False
            continue
        if in_table and _TABLE_SEP_RE.match(line):
            header_passed = True
            continue
        if in_table and header_passed:
            if not line.startswith("|"):
                # Table ended
                in_table = False
                header_passed = False
                continue
            # Parse data row — handle 5-col (with VCG) and 4-col (no VCG)
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) == 5:
                reference, term_span, vcg, verse, meaning = cells
            elif len(cells) == 4:
                reference, term_span, verse, meaning = cells
                vcg = None
            else:
                continue
            m = _STRONGS_RE.search(term_span)
            if not m:
                continue
            strongs = m.group(1)
            rows.append({
                "reference": reference,
                "strongs": strongs,
                "span_label": term_span,
                "vcg_in_meaning_file": vcg or None,
                "verse_text_excerpt": verse,
                "meaning": meaning,
                "source_file": src,
            })
    return rows


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    # Parse all 8 meaning files
    print("Parsing meaning files...")
    all_meanings: list[dict] = []
    per_file_counts: dict[str, int] = {}
    for sg in SUBGROUPS:
        path = os.path.join(MEANINGS_DIR, f"wa-m15-{sg}-verse-meanings-v1-2026-05-11.md")
        if not os.path.exists(path):
            print(f"  [WARN] missing: {path}")
            continue
        rows = parse_meaning_table(path)
        per_file_counts[os.path.basename(path)] = len(rows)
        print(f"  {os.path.basename(path):<55s}  {len(rows):>4d} rows")
        all_meanings.extend(rows)
    print(f"  TOTAL meaning rows parsed: {len(all_meanings)}")

    # Index by (reference, strongs)
    lookup: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for m in all_meanings:
        lookup[(m["reference"], m["strongs"])].append(m)

    # Duplicates (same key appearing in multiple files)
    multi_file_keys = [(k, v) for k, v in lookup.items() if len(v) > 1]
    print()
    print(f"Meaning entries with the same (reference, strongs) key appearing "
          f"in >1 row across files: {len(multi_file_keys)}")
    for k, v in multi_file_keys[:5]:
        print(f"  {k[0]:>15s} {k[1]:>8s}  in: {[m['source_file'] for m in v]}")

    # Load baseline
    print()
    print(f"Loading baseline: {BASELINE_IN}")
    with open(BASELINE_IN, "r", encoding="utf-8") as f:
        baseline = json.load(f)
    print(f"  rows: {len(baseline['verses'])}")

    # Layer in meaning
    matched = 0
    unmatched = 0
    vcg_mismatch = 0
    for v in baseline["verses"]:
        key = (v["reference"], v["term"]["strongs"])
        m_rows = lookup.get(key)
        if not m_rows:
            unmatched += 1
            continue
        # If multiple matches, pick the one from the file that matches this
        # row's current sub-group; otherwise just take the first
        chosen = m_rows[0]
        if len(m_rows) > 1 and v["current"].get("subgroup_code"):
            sg = v["current"]["subgroup_code"]
            # The sub-group letter is the last char of subgroup_code (M15-A → A)
            sg_letter = sg.split("-")[-1].lower()
            for m in m_rows:
                if f"m15-{sg_letter}-" in m["source_file"]:
                    chosen = m
                    break
        v["meaning"] = {
            "text": chosen["meaning"],
            "vcg_in_meaning_file": chosen["vcg_in_meaning_file"],
            "source_file": chosen["source_file"],
        }
        matched += 1
        # Flag VCG mismatch between meaning-file VCG and current.group_code
        cur_code = v["current"].get("group_code")
        if (cur_code and chosen["vcg_in_meaning_file"]
                and cur_code != chosen["vcg_in_meaning_file"]):
            vcg_mismatch += 1
            v["meaning"]["vcg_mismatch"] = {
                "current_group_code": cur_code,
                "meaning_file_vcg": chosen["vcg_in_meaning_file"],
            }

    # Meaning rows in files that didn't match any baseline row
    matched_keys = set()
    for v in baseline["verses"]:
        if "meaning" in v:
            matched_keys.add((v["reference"], v["term"]["strongs"]))
    unmatched_meanings = [
        m for k, mrows in lookup.items()
        for m in mrows
        if k not in matched_keys
    ]

    # Update metadata
    baseline["metadata"]["schema_version"] = "baseline-v2"
    baseline["metadata"]["generated_at"] = now_iso()
    baseline["metadata"]["meaning_layer"] = {
        "source": "Sessions/Session_Clusters/M15/files - failed session/wa-m15-*-verse-meanings-v1-2026-05-11.md",
        "files_parsed": list(per_file_counts.keys()),
        "meaning_rows_parsed": len(all_meanings),
        "baseline_rows_with_meaning": matched,
        "baseline_rows_without_meaning": unmatched,
        "meaning_rows_unmatched_to_baseline": len(unmatched_meanings),
        "vcg_mismatches_flagged": vcg_mismatch,
    }

    # Write output JSON
    with open(BASELINE_OUT, "w", encoding="utf-8") as f:
        json.dump(baseline, f, ensure_ascii=False, indent=2)
    print()
    print(f"  matched (meaning added):     {matched}")
    print(f"  unmatched baseline rows:     {unmatched}  <-- these are the 'missing ones'")
    print(f"  unmatched meaning rows:      {len(unmatched_meanings)}")
    print(f"  vcg mismatches flagged:      {vcg_mismatch}")
    print(f"  written: {BASELINE_OUT}")
    print(f"  size: {os.path.getsize(BASELINE_OUT):,} bytes")

    # Coverage report — list missing baseline rows by sub-group
    print()
    print(f"Writing coverage report: {COVERAGE_REPORT}")
    missing_by_sg: dict[str, list[dict]] = defaultdict(list)
    for v in baseline["verses"]:
        if "meaning" not in v:
            sg = v["current"].get("subgroup_code") or "(unrouted)"
            missing_by_sg[sg].append(v)

    with open(COVERAGE_REPORT, "w", encoding="utf-8") as f:
        f.write("# M15 meaning-file coverage report\n\n")
        f.write(f"**Generated:** {now_iso()}\n\n")
        f.write(f"**Source meaning files:** "
                f"`Sessions/Session_Clusters/M15/files - failed session/wa-m15-*-verse-meanings-v1-2026-05-11.md`\n\n")
        f.write(f"**Baseline rows:** {len(baseline['verses'])}\n")
        f.write(f"**Meaning rows parsed across 8 files:** {len(all_meanings)}\n")
        f.write(f"**Baseline rows with meaning attached:** {matched}\n")
        f.write(f"**Baseline rows MISSING a meaning:** {unmatched}\n")
        f.write(f"**Meaning entries that didn't match any baseline row:** "
                f"{len(unmatched_meanings)}\n\n")
        f.write("## Per-file row counts\n\n")
        f.write("| File | Rows parsed |\n|---|---:|\n")
        for fn, n in per_file_counts.items():
            f.write(f"| `{fn}` | {n} |\n")
        f.write("\n## Missing baseline rows by sub-group\n\n")
        for sg in sorted(missing_by_sg):
            rows = missing_by_sg[sg]
            f.write(f"### {sg} — {len(rows)} missing\n\n")
            f.write("| vr_id | reference | strongs | translit | status |\n")
            f.write("|---:|---|---|---|---|\n")
            for v in rows[:200]:  # cap per sg for readability
                t = v["term"]
                f.write(f"| {v['vr_id']} | {v['reference']} | "
                        f"{t['strongs']} | {t['translit']} | "
                        f"{v['current'].get('status','?')} |\n")
            if len(rows) > 200:
                f.write(f"\n_({len(rows) - 200} more not shown — see JSON for full list)_\n")
            f.write("\n")
        if unmatched_meanings:
            f.write("## Meaning entries unmatched to baseline\n\n")
            f.write("These were in the meaning files but no baseline row matched on (reference, strongs):\n\n")
            f.write("| reference | strongs | source_file |\n|---|---|---|\n")
            for m in unmatched_meanings[:100]:
                f.write(f"| {m['reference']} | {m['strongs']} | `{m['source_file']}` |\n")
            if len(unmatched_meanings) > 100:
                f.write(f"\n_({len(unmatched_meanings) - 100} more not shown)_\n")
    print(f"  written: {COVERAGE_REPORT}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
