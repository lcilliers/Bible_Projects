"""_inspect_m26_meanings_v1_20260509.py — read-only inspection of Step A output.

Reads the M26 Step A JSONL and produces a per-term grouped markdown view
to make researcher review of ~868 verse meanings practical.

Each Strong's term gets a section with:
  - sub-group + label (from DB)
  - gloss / transliteration / verse count
  - one row per verse: reference, meaning, evidence_quote

Sorted by sub-group code (M26-A..G, then BOUNDARY, then unassigned),
then by Strong's within each sub-group, then by canonical book order.

NO API calls, NO DB writes.
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

DB_PATH = os.path.join("database", "bible_research.db")


def load_term_meta(conn) -> dict[int, dict]:
    """mti_term_id -> {strong, gloss, translit, lang}.

    Post-M46 the term-to-sub-group mapping is m:n via mti_term_subgroup;
    there is no single sub-group per term. Sub-group is now resolved
    per-verse via verse_context.cluster_subgroup_id (see load_vc_routing).
    """
    out = {}
    for r in conn.execute("""
        SELECT mt.id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language
          FROM mti_terms mt
         WHERE mt.cluster_code='M26' AND COALESCE(mt.delete_flagged,0)=0
    """):
        out[r[0]] = {
            "strong": r[1], "translit": r[2], "gloss": r[3], "lang": r[4],
        }
    return out


def load_subgroup_meta(conn) -> dict[int, dict]:
    """cluster_subgroup_id -> {sg_code, sg_label, sort_order} for all M26
    sub-groups (active)."""
    out = {}
    for r in conn.execute("""
        SELECT cs.id, cs.subgroup_code, cs.label, cs.sort_order
          FROM cluster_subgroup cs
         WHERE cs.cluster_code='M26'
           AND COALESCE(cs.delete_flagged,0)=0
    """):
        out[r[0]] = {"sg_code": r[1], "sg_label": r[2], "sort_order": r[3]}
    return out


def load_vc_routing(conn) -> dict[tuple[int, int], list[int]]:
    """(vr_id, mti_term_id) -> list of cluster_subgroup_id values.

    Returns a list because a (verse, term) pair can route to multiple
    sub-groups when the verse straddles them (DEC-3, e.g. M26 'both'
    verses post-M26-A-apply will have TWO vc rows differing only in
    cluster_subgroup_id).
    """
    out: dict[tuple[int, int], list[int]] = defaultdict(list)
    for r in conn.execute("""
        SELECT vc.verse_record_id, vc.mti_term_id, vc.cluster_subgroup_id
          FROM verse_context vc
          JOIN mti_terms mt ON mt.id=vc.mti_term_id
         WHERE mt.cluster_code='M26'
           AND COALESCE(vc.delete_flagged,0)=0
           AND vc.cluster_subgroup_id IS NOT NULL
    """):
        out[(r[0], r[1])].append(r[2])
    return out


def load_verse_refs(conn) -> dict[int, str]:
    """vr_id -> reference."""
    return {r[0]: r[1] for r in conn.execute(
        "SELECT id, reference FROM wa_verse_records "
        " WHERE COALESCE(delete_flagged,0)=0"
    )}


CANONICAL_BOOKS = [
    "Gen", "Ex", "Lev", "Num", "Dt", "Jos", "Jdg", "Ru",
    "1Sa", "2Sa", "1Ki", "2Ki", "1Ch", "2Ch", "Ezr", "Ne",
    "Est", "Job", "Ps", "Pr", "Ec", "SS", "Is", "Je", "La",
    "Eze", "Da", "Hos", "Joel", "Am", "Ob", "Jon", "Mi",
    "Na", "Hab", "Zep", "Hag", "Zec", "Mal",
    "Mt", "Mk", "Lk", "Jn", "Ac", "Ro", "1Cor", "2Cor",
    "Ga", "Eph", "Php", "Col", "1Th", "2Th", "1Ti", "2Ti",
    "Tit", "Phm", "He", "Jas", "1Pe", "2Pe", "1Jn", "2Jn",
    "3Jn", "Jud", "Re",
]
BOOK_ORDER = {b: i for i, b in enumerate(CANONICAL_BOOKS)}


def ref_sort_key(ref: str):
    parts = ref.split(maxsplit=1)
    book = parts[0]
    rest = parts[1] if len(parts) > 1 else ""
    chap, _, vrs = rest.partition(":")
    try:
        c = int(chap)
    except ValueError:
        c = 0
    try:
        v = int(vrs.split()[0]) if vrs else 0
    except ValueError:
        v = 0
    return (BOOK_ORDER.get(book, 999), c, v)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl", help="Path to m26-meanings-*.jsonl")
    ap.add_argument("--out", default=None,
                    help="Output markdown path (default: alongside jsonl)")
    args = ap.parse_args()

    if not Path(args.jsonl).exists():
        print(f"ERROR: not found: {args.jsonl}", file=sys.stderr)
        return 2

    rows = []
    with open(args.jsonl, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception as e:
                print(f"  [warn] bad JSONL line: {e}", file=sys.stderr)

    print(f"Loaded {len(rows)} records from {args.jsonl}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    term_meta = load_term_meta(conn)
    sg_meta = load_subgroup_meta(conn)
    vc_routing = load_vc_routing(conn)
    verse_refs = load_verse_refs(conn)
    conn.close()

    UNROUTED_KEY = -1  # sentinel for records with no vc routing match
    sg_meta[UNROUTED_KEY] = {
        "sg_code": "M26-UNROUTED", "sg_label": "(no vc routing)",
        "sort_order": 999,
    }

    # Group: cluster_subgroup_id -> mti_term_id -> [records]
    # A meaning record with multiple vc routings (DEC-3 'both') is rendered
    # under each of its sub-groups.
    by_sg_term = defaultdict(lambda: defaultdict(list))
    for r in rows:
        key = (r["vr_id"], r["mti_term_id"])
        sg_ids = vc_routing.get(key) or [UNROUTED_KEY]
        for sg_id in sg_ids:
            by_sg_term[sg_id][r["mti_term_id"]].append(r)

    out_path = args.out or args.jsonl.replace(".jsonl", "-by-term.md")

    lines = [
        f"# M26 — Step A meanings, grouped by term\n",
        f"Source: `{args.jsonl}`  ·  records: {len(rows)}\n",
    ]

    sg_ids_sorted = sorted(
        by_sg_term.keys(),
        key=lambda sid: (sg_meta.get(sid, {}).get("sort_order", 998),
                         sg_meta.get(sid, {}).get("sg_code", "")),
    )
    for sg_id in sg_ids_sorted:
        sg = sg_meta.get(sg_id, {}).get("sg_code", "?")
        sg_label = sg_meta.get(sg_id, {}).get("sg_label", "")
        n_verses = sum(len(v) for v in by_sg_term[sg_id].values())
        n_terms = len(by_sg_term[sg_id])
        lines.append(f"\n## {sg} — {sg_label}")
        lines.append(f"Terms: {n_terms}  ·  Verses: {n_verses}\n")

        # Sort terms within sub-group by Strong's
        term_ids = sorted(by_sg_term[sg_id].keys(),
                          key=lambda m: (term_meta.get(m, {}).get("strong", "")))
        for mid in term_ids:
            meta = term_meta.get(mid, {})
            verses = by_sg_term[sg_id][mid]
            verses.sort(key=lambda r: ref_sort_key(
                verse_refs.get(r["vr_id"], "Zzz 0:0")))

            lines.append(
                f"\n### {meta.get('strong', '?')} "
                f"*{meta.get('translit', '')}* "
                f"({meta.get('gloss', '')})  ·  {len(verses)} verses"
            )
            lines.append("")
            lines.append("| ref | meaning | evidence |")
            lines.append("|-----|---------|----------|")
            for r in verses:
                ref = verse_refs.get(r["vr_id"], f"vr={r['vr_id']}")
                m = (r.get("meaning") or "").replace("|", "\\|")
                e = (r.get("evidence_quote") or "").replace("|", "\\|")
                lines.append(f"| {ref} | {m} | {e} |")

    Path(out_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out_path}")
    print(f"  Sub-groups: {len(sg_ids_sorted)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
