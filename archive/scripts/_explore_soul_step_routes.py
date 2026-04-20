"""
_explore_soul_step_routes.py
─────────────────────────────
Discovery script: compare the three distinct STEP entry points for Soul
(registry 182) to understand the full significance of the verse population and
which Strong's terms belong to the word study.

STEP entry points modelled
──────────────────────────
  Route A — English text search:  search ESV for the word "soul"
             Finds every verse where ESV *uses the word "soul"*, and records
             which Strong's number(s) tagged that word.

  Route B — Hebrew Strong's search: one call per H-prefix term in the DB for
             Soul (H5315, H5315G–N, H4578, H5397).
             Finds every verse where that *Hebrew word appears*, regardless of
             how ESV translates it.

  Route C — Greek Strong's search: one call per G-prefix term in the DB for
             Soul (G5590).
             Finds every verse where that *Greek word appears*, regardless of
             ESV rendering.

Set analysis produced
─────────────────────
  A              — all "soul" (English) refs
  B              — all Hebrew-Strong's refs (union across all H-terms)
  C              — all Greek-Strong's refs  (union across all G-terms)
  B ∪ C          — all registered-Strong's refs
  A ∩ (B ∪ C)    — verses where ESV says "soul" AND a registered term is present
  A \ (B ∪ C)    — "soul" verses with NO registered Strong's → possible gaps
  (B ∪ C) \ A    — registered-Strong's verses NOT rendered "soul" in ESV
                    → translation breadth of each term
  B \ C, C \ B   — Hebrew-only / Greek-only in the union
  A ∩ B, A ∩ C   — English "soul" confirmed by Hebrew / Greek route

Per-term breakdown
──────────────────
  For each registered Strong's:
    - total verse count from STEP
    - count of those verses where ESV says "soul"
    - count where ESV says something else (with a sample of ESV words used)

Unregistered candidates
───────────────────────
  For verses in A \ (B ∪ C), list every Strong's code seen tagging "soul" —
  these are candidates for adding to the word study.

Output
──────
  outputs/soul_step_routes_<YYYYMMDD_HHMMSS>.md

Usage
─────
  python scripts/_explore_soul_step_routes.py

Note: makes many STEP API calls (one per term + one per paginated section).
Expect 3–8 minutes depending on STEP response time.
"""

from __future__ import annotations

import os
import sys
import json
from datetime import datetime, timezone
from collections import defaultdict, Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from analytics.db_client import get_connection
from analytics.step_client import StepClient

REGISTRY_ID = 182
ENGLISH_WORD = "soul"
OUTPUT_DIR   = os.path.join(os.path.dirname(__file__), "..", "outputs")


# ── helpers ────────────────────────────────────────────────────────────────────

def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")

def _now_fmt() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

def _refs(records: list[dict]) -> set[str]:
    return {r["ref"] for r in records}

def _osis_sort_key(ref: str) -> str:
    return ref  # refs are already OSIS-like; lexicographic sort is fine for display

def _fmt_ref_list(refs: list[str], max_show: int = 30) -> str:
    """Format a sorted list of refs for markdown display."""
    if not refs:
        return "_(none)_"
    sorted_refs = sorted(refs)
    if len(sorted_refs) <= max_show:
        return ", ".join(sorted_refs)
    shown = sorted_refs[:max_show]
    remaining = len(sorted_refs) - max_show
    return ", ".join(shown) + f", … _(+{remaining} more)_"


# ── main ───────────────────────────────────────────────────────────────────────

def main() -> int:
    client = StepClient()
    conn   = get_connection()

    # ── Load registered Strong's numbers from DB ──────────────────────────────
    print("Loading registered Strong's numbers from DB...")
    fi_rows = conn.execute(
        "SELECT id FROM wa_file_index WHERE registry_id = ?",
        (str(REGISTRY_ID),),
    ).fetchall()
    file_ids = [r["id"] for r in fi_rows]

    if not file_ids:
        print(f"[ERROR] No wa_file_index rows for registry {REGISTRY_ID}. Aborting.")
        conn.close()
        return 1

    ti_rows = conn.execute(
        "SELECT strongs_number, term_id, status_note FROM wa_term_inventory WHERE file_id IN ({})".format(
            ",".join("?" * len(file_ids))
        ),
        file_ids,
    ).fetchall()
    conn.close()

    # Build list: (strong_code, status_note).  Use term_id as fallback.
    registered: list[tuple[str, str | None]] = []
    for ti in ti_rows:
        code = ti["strongs_number"] or ti["term_id"]
        if code:
            registered.append((code, ti["status_note"]))

    hebrew_codes = [(c, n) for c, n in registered if c.startswith("H")]
    greek_codes  = [(c, n) for c, n in registered if c.startswith("G")]

    print(f"  Hebrew terms: {[c for c,_ in hebrew_codes]}")
    print(f"  Greek terms:  {[c for c,_ in greek_codes]}")

    # ── Route A: English "soul" search ────────────────────────────────────────
    print(f"\nRoute A — English text search: \"{ENGLISH_WORD}\"...")
    route_a_records = client.get_verse_records_by_english(ENGLISH_WORD)
    route_a_refs    = _refs(route_a_records)
    route_a_by_ref  = {r["ref"]: r for r in route_a_records}

    # Tally which Strong's numbers tag "soul" in Route A verses
    a_strong_tally: Counter = Counter()
    for rec in route_a_records:
        for s in rec["tagging_strongs"]:
            a_strong_tally[s] += 1
    print(f"  Route A: {len(route_a_records)} verses")

    # ── Route B: Hebrew Strong's search ───────────────────────────────────────
    # term_records[code] = list[dict] — verse records from STEP for that term
    print("\nRoute B — Hebrew Strong's searches...")
    b_term_records: dict[str, list[dict]] = {}
    for code, status_note in hebrew_codes:
        # Skip terms marked "no separate verse record"
        if status_note and "no separate verse record" in status_note.lower():
            print(f"  {code}: SKIPPED (no separate verse record)")
            b_term_records[code] = []
            continue
        print(f"  {code}: fetching...", end="", flush=True)
        recs, _ = client.get_verse_records_with_html(code)
        b_term_records[code] = recs
        print(f" {len(recs)} verses")

    # ── Route C: Greek Strong's search ────────────────────────────────────────
    print("\nRoute C — Greek Strong's searches...")
    c_term_records: dict[str, list[dict]] = {}
    for code, status_note in greek_codes:
        if status_note and "no separate verse record" in status_note.lower():
            print(f"  {code}: SKIPPED (no separate verse record)")
            c_term_records[code] = []
            continue
        print(f"  {code}: fetching...", end="", flush=True)
        recs, _ = client.get_verse_records_with_html(code)
        c_term_records[code] = recs
        print(f" {len(recs)} verses")

    # ── Set algebra ───────────────────────────────────────────────────────────
    print("\nComputing set analysis...")

    # All B refs combined
    route_b_refs: set[str] = set()
    for recs in b_term_records.values():
        route_b_refs |= _refs(recs)

    # All C refs combined
    route_c_refs: set[str] = set()
    for recs in c_term_records.values():
        route_c_refs |= _refs(recs)

    bc_refs  = route_b_refs | route_c_refs        # all registered Strong's
    a_and_bc = route_a_refs & bc_refs              # English "soul" + registered Strong's
    a_only   = route_a_refs - bc_refs              # "soul" with no registered Strong's
    bc_only  = bc_refs - route_a_refs              # registered Strong's not translated "soul"
    all_refs = route_a_refs | bc_refs              # complete union

    # For each registered term: count how many of its verses are in Route A
    term_in_a: dict[str, int] = {}
    for code, recs in {**b_term_records, **c_term_records}.items():
        term_refs = _refs(recs)
        term_in_a[code] = len(term_refs & route_a_refs)

    # For bc_only (registered Strong's not translated "soul"): sample ESV words
    # Build a map: ref → ESV target_word from Strong's route
    bc_only_words: dict[str, list[str]] = defaultdict(list)  # ref → [target_word, …]
    for code, recs in {**b_term_records, **c_term_records}.items():
        for rec in recs:
            ref = rec["ref"]
            if ref in bc_only:
                tw = rec.get("target_word", "").strip()
                if tw:
                    for w in tw.split(","):
                        w = w.strip()
                        if w:
                            bc_only_words[ref].append(w)

    # Tally ESV words used when registered Strong's is NOT translated "soul"
    esv_word_counter: Counter = Counter()
    for ref, words in bc_only_words.items():
        for w in words:
            esv_word_counter[w.lower()] += 1

    # Unregistered candidate Strong's (from a_only verses)
    unregistered_tally: Counter = Counter()
    for ref in a_only:
        rec = route_a_by_ref[ref]
        for s in rec["tagging_strongs"]:
            if s not in {c for c, _ in registered}:
                unregistered_tally[s] += 1
    # Includes blank (untagged "soul" spans)
    untagged_count = sum(1 for ref in a_only
                         if not route_a_by_ref[ref]["tagging_strongs"])

    # ── Per-term breakdown: how ESV translates each registered term ───────────
    # For terms in Route B/C, find what ESV target_word is used
    term_esv_words: dict[str, Counter] = {}
    for code, recs in {**b_term_records, **c_term_records}.items():
        ctr: Counter = Counter()
        for rec in recs:
            tw = rec.get("target_word", "").strip()
            if tw:
                for w in tw.split(","):
                    w = w.strip()
                    if w:
                        ctr[w.lower()] += 1
        term_esv_words[code] = ctr

    # ── Build report ─────────────────────────────────────────────────────────
    print("Building report...")
    lines: list[str] = []

    def p(s: str = "") -> None:
        lines.append(s)

    p("# Soul (Registry 182) — STEP Route Comparison")
    p(f"**Generated:** {_now_fmt()} UTC")
    p()
    p("This report compares three distinct STEP entry points for the word study of Soul.")
    p("The goal is to understand the full scope of relevant verses and related terms.")
    p()
    p("---")
    p()
    p("## Route Definitions")
    p()
    p("| Route | Description | Entry point |")
    p("|-------|-------------|-------------|")
    p(f"| **A** | ESV English text search for `\"{ENGLISH_WORD}\"` | Every verse where ESV uses this English word |")
    p(f"| **B** | Hebrew Strong's search — {len(hebrew_codes)} term(s) | Every verse containing the Hebrew word, regardless of ESV rendering |")
    p(f"| **C** | Greek Strong's search  — {len(greek_codes)} term(s) | Every verse containing the Greek word, regardless of ESV rendering |")
    p()
    p("---")
    p()
    p("## Summary Counts")
    p()
    p("| Set | Description | Count |")
    p("|-----|-------------|-------|")
    p(f"| A | English `\"{ENGLISH_WORD}\"` verses | **{len(route_a_refs)}** |")
    p(f"| B | Hebrew Strong's verses (union) | **{len(route_b_refs)}** |")
    p(f"| C | Greek Strong's verses (union) | **{len(route_c_refs)}** |")
    p(f"| B ∪ C | All registered Strong's verses | **{len(bc_refs)}** |")
    p(f"| A ∩ (B ∪ C) | 'soul' + registered Strong's -- both agree | **{len(a_and_bc)}** |")
    p(f"| A \\ (B ∪ C) | 'soul' verses with **no** registered Strong's | **{len(a_only)}** |")
    p(f"| (B ∪ C) \\ A | Registered Strong's verses **not** rendered 'soul' in ESV | **{len(bc_only)}** |")
    p(f"| A ∪ (B ∪ C) | Complete union of all routes | **{len(all_refs)}** |")
    p()
    p("---")
    p()
    p("## Route B — Hebrew Terms Detail")
    p()
    p("| Strong's | STEP verse count | In Route A (rendered 'soul') | Not rendered 'soul' |")
    p("|----------|-----------------|------------------------------|---------------------|")
    for code, _ in hebrew_codes:
        recs  = b_term_records.get(code, [])
        total = len(recs)
        in_a  = term_in_a.get(code, 0)
        p(f"| {code} | {total} | {in_a} | {total - in_a} |")
    p()
    p("### ESV translation variety for each Hebrew term")
    p('_(when the term is NOT rendered "soul" in ESV - top 15 ESV words used)_')
    p()
    for code, _ in hebrew_codes:
        recs = b_term_records.get(code, [])
        if not recs:
            p(f"**{code}:** _(no verse records)_")
            p()
            continue
        # Words used in non-"soul" verses
        not_soul_ctr: Counter = Counter()
        for rec in recs:
            if rec["ref"] not in route_a_refs:
                tw = rec.get("target_word", "").strip()
                if tw:
                    for w in tw.split(","):
                        w = w.strip()
                        if w:
                            not_soul_ctr[w.lower()] += 1
        in_a_count  = term_in_a.get(code, 0)
        not_a_count = len(recs) - in_a_count
        p(f"**{code}** — {not_a_count} non-'soul' verses:")
        if not_soul_ctr:
            top = not_soul_ctr.most_common(15)
            p("  " + ", ".join(f"{w} ({n})" for w, n in top))
        else:
            p("  _(no target_word data available)_")
        p()

    p("---")
    p()
    p("## Route C — Greek Terms Detail")
    p()
    p("| Strong's | STEP verse count | In Route A (rendered 'soul') | Not rendered 'soul' |")
    p("|----------|-----------------|------------------------------|---------------------|")
    for code, status_note in greek_codes:
        recs  = c_term_records.get(code, [])
        total = len(recs)
        in_a  = term_in_a.get(code, 0)
        skip_note = " _(skipped: no separate verse record)_" if (
            status_note and "no separate verse record" in status_note.lower()
        ) else ""
        p(f"| {code} | {total}{skip_note} | {in_a} | {total - in_a} |")
    p()
    p("### ESV translation variety for each Greek term")
    p()
    for code, status_note in greek_codes:
        if status_note and "no separate verse record" in status_note.lower():
            p(f"**{code}:** _(skipped — researcher consolidated; no separate verse record)_")
            p()
            continue
        recs = c_term_records.get(code, [])
        if not recs:
            p(f"**{code}:** _(no verse records returned by STEP)_")
            p()
            continue
        not_soul_ctr: Counter = Counter()
        for rec in recs:
            if rec["ref"] not in route_a_refs:
                tw = rec.get("target_word", "").strip()
                if tw:
                    for w in tw.split(","):
                        w = w.strip()
                        if w:
                            not_soul_ctr[w.lower()] += 1
        in_a_count  = term_in_a.get(code, 0)
        not_a_count = len(recs) - in_a_count
        p(f"**{code}** — {not_a_count} non-'soul' verses:")
        if not_soul_ctr:
            top = not_soul_ctr.most_common(15)
            p("  " + ", ".join(f"{w} ({n})" for w, n in top))
        else:
            p("  _(no target_word data available)_")
        p()

    p("---")
    p()
    p("## Strong's Codes Found Tagging 'soul' in Route A")
    p("_(which Strong's numbers drive the ESV translation choice 'soul')_")
    p()
    p("| Strong's | Verses where it tags 'soul' | In DB? |")
    p("|----------|-----------------------------|--------|")
    registered_codes = {c for c, _ in registered}
    for s, count in a_strong_tally.most_common():
        in_db = "✓" if s in registered_codes else "**candidate — not in DB**"
        p(f"| {s} | {count} | {in_db} |")
    p()

    p("---")
    p()
    p(f"## A minus (B union C) -- 'soul' Verses with No Registered Strong's  ({len(a_only)} verses)")
    p()
    if not a_only:
        p("_None — all English 'soul' verses are covered by at least one registered Strong's number._")
    else:
        p("These verses use the ESV word 'soul' but none of the currently registered Strong's")
        p("numbers appear in them. They may indicate:")
        p("- A Strong's term that should be added to this word study")
        p("- A translation choice driven by context rather than a primary soul-word")
        p()
        p("**Candidate Strong's codes found in these verses:**")
        p()
        p("| Strong's | Count | Status |")
        p("|----------|-------|--------|")
        for s, count in unregistered_tally.most_common():
            p(f"| {s} | {count} | not in DB |")
        if untagged_count:
            p(f"| _(no span tag)_ | {untagged_count} | 'soul' appears untagged in STEP HTML |")
        p()
        p("**Verse list:**")
        p()
        sorted_a_only = sorted(a_only)
        for ref in sorted_a_only:
            rec = route_a_by_ref[ref]
            tag_str = ", ".join(rec["tagging_strongs"]) if rec["tagging_strongs"] else "_(untagged)_"
            p(f"- **{ref}** (tags: {tag_str})  ")
            p(f"  {rec['esv_text']}")
        p()

    p("---")
    p()
    p(f"## (B union C) minus A -- Registered Strong's Verses NOT Rendered 'soul' ({len(bc_only)} verses)")
    p()
    if not bc_only:
        p("_None — every registered Strong's verse is rendered 'soul' in ESV._")
    else:
        p("These verses contain a registered Strong's term (Hebrew/Greek) but the ESV")
        p("does not use the word 'soul'. This shows the **translation breadth** of the terms.")
        p()
        p("**Top ESV words used instead of 'soul' (across all terms):**")
        p()
        p("| ESV word | Verse count |")
        p("|----------|-------------|")
        for w, n in esv_word_counter.most_common(30):
            p(f"| {w} | {n} |")
        p()
        p("**Per-term breakdown of non-'soul' verses:**")
        p()
        all_term_codes = [c for c, _ in hebrew_codes] + [c for c, _ in greek_codes]
        for code in all_term_codes:
            recs = {**b_term_records, **c_term_records}.get(code, [])
            non_soul_recs = [r for r in recs if r["ref"] in bc_only]
            if not non_soul_recs:
                continue
            p(f"### {code} — {len(non_soul_recs)} non-'soul' verses")
            p()
            for rec in sorted(non_soul_recs, key=lambda r: r["osisId"]):
                tw = rec.get("target_word", "").strip() or "_(no tag)_"
                p(f"- **{rec['ref']}** → ESV: *{tw}*  ")
                p(f"  {rec['esv_text']}")
            p()

    p("---")
    p()
    p("## Raw Data Appendix")
    p()
    p("### Route A — all 'soul' verse refs")
    p()
    p(_fmt_ref_list(sorted(route_a_refs)))
    p()
    p("### Route B — all Hebrew Strong's verse refs (union)")
    p()
    p(_fmt_ref_list(sorted(route_b_refs)))
    p()
    p("### Route C — all Greek Strong's verse refs (union)")
    p()
    p(_fmt_ref_list(sorted(route_c_refs)))
    p()

    # ── Write output ──────────────────────────────────────────────────────────
    ts = _now_ts()
    out_filename = f"soul_step_routes_{ts}.md"
    out_path = os.path.join(OUTPUT_DIR, out_filename)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print(f"\nReport written: {out_path}")
    print(f"  Route A: {len(route_a_refs)} verses")
    print(f"  Route B (Hebrew union): {len(route_b_refs)} verses")
    print(f"  Route C (Greek union):  {len(route_c_refs)} verses")
    print(f"  'soul' with no registered Strong's: {len(a_only)}")
    print(f"  Registered Strong's not rendered 'soul': {len(bc_only)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
