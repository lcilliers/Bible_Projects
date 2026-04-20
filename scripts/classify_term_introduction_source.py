"""classify_term_introduction_source.py — Heuristic classifier for M30 backfill.

Read-only script. Walks every OWNER term in wa_term_inventory and proposes a
value for the new `term_introduction_source` column per the 9-code controlled
vocabulary in coverage-flags-redesign-v1-20260420.md §12.5.

Output: outputs/term-introduction-classification-proposals-{YYYYMMDD}.md
  — proposals per registry, stats summary, and a list of ambiguous cases for
  researcher review.

No DB writes. Apply separately after researcher reviews the proposals.

Heuristics (priority order):
  1. OWNER term whose strongs is the #1 entry in word_registry.strongs_list
     → `step_keyword` (primary English-keyword search anchor)
  2. OWNER term whose strongs is in the top-5 of strongs_list
     → `step_association` (STEP cluster expansion / sub-gloss)
  3. OWNER term whose strongs is elsewhere in strongs_list
     → `step_association` (still from STEP discovery, lower rank)
  4. OWNER term whose strongs is NOT in strongs_list but appears in another
     term's `meaning` field in the same registry
     → `derived_from_meaning`
  5. OWNER term not matching any above → `legacy_unknown`

First pass: OWNER terms only. XREFs inherit OWNER's classification in a later pass.

Usage:
  python scripts/classify_term_introduction_source.py
  python scripts/classify_term_introduction_source.py --registry=N  # single-registry

Author: Claude Code — M30 backfill investigation.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

DB_PATH = os.path.join("data", "bible_research.db")


def open_db(path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def parse_strongs_list(raw: str | None) -> list[dict]:
    if not raw:
        return []
    try:
        return json.loads(raw)
    except Exception:
        return []


def classify_registry(conn: sqlite3.Connection, registry_row: sqlite3.Row) -> dict:
    """Classify all OWNER terms in one registry. Return proposals + stats."""
    reg_id = registry_row["id"]
    reg_no = registry_row["no"]
    word = registry_row["word"]
    strongs_list = parse_strongs_list(registry_row["strongs_list"])

    # Top-N strongs positions for heuristic ranking
    rank_of: dict[str, int] = {}
    for i, entry in enumerate(strongs_list):
        s = entry.get("strong") if isinstance(entry, dict) else None
        if s and s not in rank_of:
            rank_of[s] = i

    # OWNER terms in this registry
    owner_terms = conn.execute(
        """
        SELECT ti.id, ti.strongs_number, ti.transliteration, ti.step_search_gloss,
               ti.word_analysis_gloss, ti.language, ti.meaning, ti.term_owner_type
          FROM wa_term_inventory ti
         WHERE ti.delete_flagged = 0
           AND ti.term_owner_type = 'OWNER'
           AND ti.file_id IN (SELECT id FROM wa_file_index WHERE word_registry_fk = ?)
         ORDER BY ti.strongs_number
        """,
        (reg_id,),
    ).fetchall()

    # Build a lowercase corpus of all 'meaning' texts in the registry for
    # derived_from_meaning heuristic
    meaning_corpus = " \n".join((t["meaning"] or "") for t in owner_terms).lower()

    proposals = []
    for t in owner_terms:
        strongs = t["strongs_number"]
        rank = rank_of.get(strongs)
        proposed = None
        rationale = None

        if rank == 0:
            proposed = "step_keyword"
            rationale = f"Strongs {strongs} is rank #1 in registry strongs_list (primary anchor)"
        elif rank is not None and rank < 5:
            proposed = "step_association"
            rationale = f"Strongs {strongs} is rank #{rank + 1} in registry strongs_list (top-5 cluster)"
        elif rank is not None:
            proposed = "step_association"
            rationale = f"Strongs {strongs} is rank #{rank + 1} in registry strongs_list"
        else:
            # Not in strongs_list — check meaning corpus for the term's key tokens
            triggers = []
            # Look for strongs_number or transliteration appearing in meaning text of other terms
            if strongs and strongs.lower() in meaning_corpus.replace(t["meaning"] or "", "").lower():
                triggers.append(f"strongs '{strongs}' in another term's meaning")
            translit = (t["transliteration"] or "").strip()
            if translit and len(translit) > 2:
                pattern = re.compile(r"\b" + re.escape(translit.lower()) + r"\b")
                other_meanings = " ".join(
                    (ot["meaning"] or "").lower() for ot in owner_terms if ot["id"] != t["id"]
                )
                if pattern.search(other_meanings):
                    triggers.append(f"transliteration '{translit}' in another term's meaning")
            if triggers:
                proposed = "derived_from_meaning"
                rationale = "; ".join(triggers)
            else:
                proposed = "legacy_unknown"
                rationale = "No signal: not in strongs_list, not referenced in other terms' meanings"

        proposals.append(
            dict(
                term_inv_id=t["id"],
                strongs=strongs,
                transliteration=t["transliteration"],
                step_gloss=t["step_search_gloss"],
                proposed=proposed,
                rationale=rationale,
            )
        )

    # Stats
    stats = Counter(p["proposed"] for p in proposals)
    return dict(
        registry_no=reg_no,
        word=word,
        total_owner_terms=len(owner_terms),
        proposals=proposals,
        stats=dict(stats),
    )


def render_report(results: list[dict]) -> str:
    out = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    total_terms = sum(r["total_owner_terms"] for r in results)
    overall: Counter = Counter()
    for r in results:
        for k, v in r["stats"].items():
            overall[k] += v

    out.append(f"# Term Introduction Source — Classifier Proposals — {now[:10]}\n")
    out.append("| Field | Value |")
    out.append("|---|---|")
    out.append("| Scope | OWNER terms only (first pass) |")
    out.append(f"| Registries scanned | {len(results)} |")
    out.append(f"| OWNER terms classified | {total_terms:,} |")
    out.append(f"| Generated | {now} |")
    out.append("| Source | `scripts/classify_term_introduction_source.py` |")
    out.append("| Mode | READ-ONLY — no DB writes |")
    out.append("\n---\n")

    out.append("## Programme summary — proposed distribution\n")
    out.append("| Proposed source | Count | Share |")
    out.append("|---|---:|---:|")
    for src in ("step_keyword", "step_association", "derived_from_meaning",
                "legacy_unknown"):
        n = overall.get(src, 0)
        pct = (n / total_terms * 100) if total_terms else 0
        out.append(f"| `{src}` | {n:,} | {pct:.1f}% |")
    out.append("")

    # Ambiguous cases: anything classified legacy_unknown is worth review
    ambig = []
    for r in results:
        for p in r["proposals"]:
            if p["proposed"] == "legacy_unknown":
                ambig.append((r["registry_no"], r["word"], p))

    out.append(f"\n## Ambiguous cases (proposed `legacy_unknown`): {len(ambig)}\n")
    out.append("Researcher review recommended for any that should be `researcher_external`, `ai_proposed`, or another classification.\n")
    if ambig:
        out.append("| Reg | Word | Strongs | Translit | Step gloss | Rationale |")
        out.append("|---:|---|---|---|---|---|")
        for reg_no, word, p in ambig[:200]:  # cap output
            out.append(
                f"| {reg_no} | {word} | `{p['strongs']}` | {p['transliteration'] or '—'} | "
                f"{(p['step_gloss'] or '—')[:40]} | {p['rationale']} |"
            )
        if len(ambig) > 200:
            out.append(f"\n_Truncated at 200 of {len(ambig)} ambiguous cases._\n")

    out.append("\n---\n")
    out.append("## Per-registry proposals\n")

    for r in sorted(results, key=lambda x: x["registry_no"]):
        if r["total_owner_terms"] == 0:
            continue
        out.append(f"### r{r['registry_no']:>03} {r['word']}\n")
        out.append(f"Total OWNER terms: {r['total_owner_terms']}; "
                   f"proposed distribution: " +
                   ", ".join(f"`{k}`={v}" for k, v in sorted(r['stats'].items())))
        out.append("")
        out.append("| Strongs | Translit | Proposed | Rationale |")
        out.append("|---|---|---|---|")
        for p in r["proposals"]:
            out.append(
                f"| `{p['strongs']}` | {p['transliteration'] or '—'} | "
                f"`{p['proposed']}` | {p['rationale']} |"
            )
        out.append("")

    out.append("---\n")
    out.append("## Apply the classification\n")
    out.append("After researcher review + any overrides, apply via a UPDATE script "
               "(not in this read-only run). Each row should get both "
               "`term_introduction_source` and a `term_introduction_rationale` note.\n")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Classify term_introduction_source — report only")
    ap.add_argument("--registry", type=int, default=None,
                    help="single registry no (default: all non-excluded)")
    ap.add_argument("--out", type=str,
                    default=None,
                    help="output .md path (default: outputs/term-introduction-classification-proposals-{YYYYMMDD}.md)")
    ap.add_argument("--db", type=str, default=DB_PATH)
    args = ap.parse_args()

    conn = open_db(args.db)
    if args.registry is not None:
        regs = conn.execute(
            "SELECT id, no, word, strongs_list FROM word_registry WHERE no = ?",
            (args.registry,),
        ).fetchall()
    else:
        regs = conn.execute(
            """SELECT id, no, word, strongs_list FROM word_registry
                WHERE carry_forward = 1 AND strongs_list IS NOT NULL
                ORDER BY no"""
        ).fetchall()

    results = []
    for r in regs:
        results.append(classify_registry(conn, r))

    report = render_report(results)

    out_path = args.out
    if not out_path:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
        out_path = f"outputs/term-introduction-classification-proposals-{stamp}.md"
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(report, encoding="utf-8")

    total = sum(r["total_owner_terms"] for r in results)
    overall: Counter = Counter()
    for r in results:
        for k, v in r["stats"].items():
            overall[k] += v

    print(f"Wrote: {out_path}")
    print(f"Registries: {len(results)}; OWNER terms classified: {total:,}")
    print(f"Distribution: {dict(overall)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
