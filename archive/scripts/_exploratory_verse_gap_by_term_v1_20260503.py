"""_exploratory_verse_gap_by_term_v1_20260503.py — read-only.

For each active OWNER term, compute:
  - verses_pulled  — wa_verse_records pulled in by STEP for this term
  - vc_classified  — verse_context rows actually written for this term
  - gap            — verses_pulled - vc_classified  (verses pulled but not yet
                     classified)
  - gap_pct        — gap / verses_pulled * 100

Plus a per-registry roll-up showing where the bulk of the verse-classification
gap sits.

This decomposes the 'NO VC ROW' layer (4,809 distinct canonical verses,
~20,000+ verse-record-occurrences) by term so the cleanup can be prioritised.
"""
from __future__ import annotations

import os
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
OUT_MD = os.path.join("outputs", "markdown", "verse-gap-by-term-20260503.md")
OUT_JSON = os.path.join("outputs", "markdown", "verse-gap-by-term-20260503.json")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT mt.id AS mti_id, mt.strongs_number, mt.transliteration, mt.gloss,
               mt.language, mt.status,
               wr.no AS reg_no, wr.word AS reg_word,
               (SELECT COUNT(*) FROM wa_verse_records vr
                 WHERE vr.term_inv_id = ti.id AND vr.delete_flagged=0) AS verses_pulled,
               (SELECT COUNT(*) FROM verse_context vc
                 WHERE vc.mti_term_id = mt.id AND vc.delete_flagged=0) AS vc_classified,
               (SELECT COUNT(*) FROM verse_context vc
                 WHERE vc.mti_term_id = mt.id AND vc.delete_flagged=0
                   AND vc.is_relevant=1) AS vc_relevant,
               (SELECT COUNT(*) FROM verse_context vc
                 WHERE vc.mti_term_id = mt.id AND vc.delete_flagged=0
                   AND vc.is_anchor=1) AS vc_anchor
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                    AND ti.term_owner_type = 'OWNER'
                                    AND ti.delete_flagged = 0
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
         WHERE mt.delete_flagged = 0
           AND mt.status IN ('extracted','extracted_thin','extracted_theological_anchor')
           AND wr.phase1_status != 'Excluded'
    """).fetchall()

    # Build per-term records
    items = []
    for r in rows:
        d = dict(r)
        d["gap"] = (d["verses_pulled"] or 0) - (d["vc_classified"] or 0)
        d["gap_pct"] = (d["gap"] / d["verses_pulled"] * 100) if d["verses_pulled"] else 0
        items.append(d)

    # Per-registry roll-up
    per_reg = defaultdict(lambda: {"terms": 0, "verses_pulled": 0,
                                    "vc_classified": 0, "vc_relevant": 0,
                                    "vc_anchor": 0, "gap": 0})
    for it in items:
        k = (it["reg_no"], it["reg_word"])
        b = per_reg[k]
        b["terms"] += 1
        b["verses_pulled"] += it["verses_pulled"] or 0
        b["vc_classified"] += it["vc_classified"] or 0
        b["vc_relevant"] += it["vc_relevant"] or 0
        b["vc_anchor"] += it["vc_anchor"] or 0
        b["gap"] += it["gap"]

    L = []
    L.append("# Verse Gap by Term — Where the Unclassified Verses Live")
    L.append("")
    L.append(f"_Generated {now_iso()}_  ·  source: "
             "`scripts/_exploratory_verse_gap_by_term_v1_20260503.py`")
    L.append("")
    L.append("For each active OWNER term: how many verses STEP pulled in, how many "
             "have been classified by VC, and the gap (verses_pulled − vc_classified). "
             "The gap is the cohort of verses that are in `wa_verse_records` for this "
             "term but have no `verse_context` row at all.")
    L.append("")

    # Programme totals
    total = {"terms": len(items),
             "verses_pulled": sum(i["verses_pulled"] or 0 for i in items),
             "vc_classified": sum(i["vc_classified"] or 0 for i in items),
             "vc_relevant": sum(i["vc_relevant"] or 0 for i in items),
             "vc_anchor": sum(i["vc_anchor"] or 0 for i in items),
             "gap": sum(i["gap"] for i in items)}
    L.append("## Programme totals")
    L.append("")
    L.append(f"- Active OWNER terms: **{total['terms']:,}**")
    L.append(f"- Total verses pulled (`wa_verse_records`): **{total['verses_pulled']:,}**")
    L.append(f"- Total vc rows written: **{total['vc_classified']:,}**  "
             f"({total['vc_classified']/total['verses_pulled']*100:.1f}% classified)")
    L.append(f"- Of vc rows: relevant={total['vc_relevant']:,}, anchor={total['vc_anchor']:,}")
    L.append(f"- **Total gap (pulled but not classified): {total['gap']:,}**  "
             f"({total['gap']/total['verses_pulled']*100:.1f}% of pulled)")
    L.append("")

    # Per-registry top 30 by absolute gap
    L.append("## Per-registry — top 30 by absolute gap")
    L.append("")
    L.append("| Reg | Word | Terms | Verses pulled | VC classified | Gap | Gap % |")
    L.append("|---:|---|---:|---:|---:|---:|---:|")
    for (no, word), v in sorted(per_reg.items(), key=lambda x: -x[1]["gap"])[:30]:
        gap_pct = (v["gap"] / v["verses_pulled"] * 100) if v["verses_pulled"] else 0
        L.append(f"| {no} | {word} | {v['terms']} | {v['verses_pulled']:,} | "
                 f"{v['vc_classified']:,} | {v['gap']:,} | {gap_pct:.1f}% |")
    L.append("")

    # Per-term top 50 by absolute gap
    L.append("## Per-term — top 50 by absolute gap")
    L.append("")
    L.append("Terms with the largest unclassified-verse cohort. These are the "
             "highest-leverage VC processing targets.")
    L.append("")
    L.append("| Reg | Word | Strong's | Translit | Gloss | Lang | Pulled | Classified | Gap | Gap% |")
    L.append("|---:|---|---|---|---|---|---:|---:|---:|---:|")
    for it in sorted(items, key=lambda x: -x["gap"])[:50]:
        L.append(f"| {it['reg_no']} | {it['reg_word']} | `{it['strongs_number']}` | "
                 f"{it['transliteration'] or ''} | {(it['gloss'] or '')[:25]} | "
                 f"{it['language'][:1]} | {it['verses_pulled']:,} | "
                 f"{it['vc_classified']:,} | {it['gap']:,} | {it['gap_pct']:.1f}% |")
    L.append("")

    # Terms with 100% gap (totally unclassified) — by verses_pulled
    fully_unclassified = [i for i in items
                          if i["verses_pulled"] > 0 and i["vc_classified"] == 0]
    L.append(f"## Terms 100% unclassified — {len(fully_unclassified)} terms")
    L.append("")
    L.append("Terms where every pulled verse is unclassified — VC processing was "
             "never started for these terms.")
    L.append("")
    L.append("Top 30 by verses pulled:")
    L.append("")
    L.append("| Reg | Word | Strong's | Translit | Gloss | Lang | Status | Verses |")
    L.append("|---:|---|---|---|---|---|---|---:|")
    for it in sorted(fully_unclassified, key=lambda x: -x["verses_pulled"])[:30]:
        L.append(f"| {it['reg_no']} | {it['reg_word']} | `{it['strongs_number']}` | "
                 f"{it['transliteration'] or ''} | {(it['gloss'] or '')[:25]} | "
                 f"{it['language'][:1]} | `{it['status']}` | {it['verses_pulled']:,} |")
    L.append("")

    # Terms with high relative gap (50%+ but partially classified) — different problem
    partial = [i for i in items
               if i["verses_pulled"] >= 20 and 0 < i["gap_pct"] < 100 and i["gap_pct"] >= 50]
    L.append(f"## Partial-coverage terms — {len(partial)} terms with ≥50% gap and ≥20 verses pulled")
    L.append("")
    L.append("Top 30 by gap size:")
    L.append("")
    L.append("| Reg | Word | Strong's | Gloss | Verses pulled | Classified | Gap% |")
    L.append("|---:|---|---|---|---:|---:|---:|")
    for it in sorted(partial, key=lambda x: -x["gap"])[:30]:
        L.append(f"| {it['reg_no']} | {it['reg_word']} | `{it['strongs_number']}` | "
                 f"{(it['gloss'] or '')[:25]} | {it['verses_pulled']:,} | "
                 f"{it['vc_classified']:,} | {it['gap_pct']:.1f}% |")
    L.append("")

    # Distribution of gap_pct
    buckets = {"0%": 0, "1-25%": 0, "26-50%": 0, "51-75%": 0, "76-99%": 0, "100%": 0}
    for it in items:
        if it["verses_pulled"] == 0:
            continue
        g = it["gap_pct"]
        if g == 0: buckets["0%"] += 1
        elif g <= 25: buckets["1-25%"] += 1
        elif g <= 50: buckets["26-50%"] += 1
        elif g <= 75: buckets["51-75%"] += 1
        elif g < 100: buckets["76-99%"] += 1
        else: buckets["100%"] += 1
    L.append("## Coverage-gap distribution across terms")
    L.append("")
    L.append("| Gap % bucket | # terms | Description |")
    L.append("|---|---:|---|")
    descs = {
        "0%": "fully classified",
        "1-25%": "mostly classified",
        "26-50%": "moderately classified",
        "51-75%": "mostly unclassified",
        "76-99%": "largely unclassified",
        "100%": "never started",
    }
    for k in ["0%", "1-25%", "26-50%", "51-75%", "76-99%", "100%"]:
        L.append(f"| {k} | {buckets[k]} | {descs[k]} |")
    L.append("")

    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    import json
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump({"meta": {"generated_at": now_iso(), "n_terms": len(items)},
                   "totals": total,
                   "per_registry": [{"reg_no": k[0], "reg_word": k[1], **v}
                                    for k, v in per_reg.items()],
                   "terms": items},
                  f, indent=2, ensure_ascii=False, default=str)

    print(f"Wrote: {OUT_MD}")
    print(f"Wrote: {OUT_JSON}")
    print()
    print(f"Active OWNER terms: {total['terms']:,}")
    print(f"Verses pulled: {total['verses_pulled']:,}")
    print(f"VC classified: {total['vc_classified']:,}")
    print(f"Gap: {total['gap']:,}  ({total['gap']/total['verses_pulled']*100:.1f}%)")
    print()
    print(f"Coverage distribution:")
    for k in ["0%", "1-25%", "26-50%", "51-75%", "76-99%", "100%"]:
        print(f"  {k}: {buckets[k]} terms")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
