"""_exploratory_pos_noise_crosstab_v1_20260503.py — read-only.

Cross-tabulates the STEP-derived POS lookup against verse_context state.
Produces a structured cleanup-candidate report grouped by POS category.

Inputs:
  outputs/markdown/step-pos-lookup-20260503.json  — Strong's -> POS

Outputs:
  outputs/markdown/pos-noise-crosstab-20260503.md   — readable report
  outputs/markdown/pos-noise-crosstab-20260503.json — per-Strong's payload
"""
from __future__ import annotations

import json
import os
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
POS_JSON = os.path.join("outputs", "markdown", "step-pos-lookup-20260503.json")
OUT_MD = os.path.join("outputs", "markdown", "pos-noise-crosstab-20260503.md")
OUT_JSON = os.path.join("outputs", "markdown", "pos-noise-crosstab-20260503.json")

NOISE_POS = {
    "pronoun", "pronoun-personal", "pronoun-reflexive", "pronoun-demonstrative",
    "pronoun-interrogative", "pronoun-correlative", "pronoun-relative",
    "pronoun-reciprocal", "pronoun-possessive", "pronoun-indefinite",
    "particle", "preposition", "conjunction", "conditional-particle",
    "interjection", "article", "suffix", "adverb",
}
CONTENT_POS = {"noun", "verb", "adjective"}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    with open(POS_JSON, encoding="utf-8") as f:
        pos_data = json.load(f)
    pos_meta = {k: v for k, v in pos_data["results"].items()}

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Per-Strong's vc state
    rows = conn.execute("""
        SELECT mt.strongs_number, mt.transliteration, mt.gloss, mt.language,
               COUNT(vc.id) AS total_vc,
               SUM(CASE WHEN vc.is_relevant=1 THEN 1 ELSE 0 END) AS rel,
               SUM(CASE WHEN vc.is_relevant=1 AND vc.is_anchor=1 THEN 1 ELSE 0 END) AS anchor,
               SUM(CASE WHEN vc.is_relevant=0 AND vc.set_aside_reason IS NOT NULL
                          AND vc.set_aside_reason!='' THEN 1 ELSE 0 END) AS clean_sa,
               SUM(CASE WHEN vc.is_relevant=0 AND (vc.set_aside_reason IS NULL
                          OR vc.set_aside_reason='') THEN 1 ELSE 0 END) AS muddled
          FROM mti_terms mt
          JOIN wa_term_inventory ti ON ti.strongs_number = mt.strongs_number
                                   AND ti.term_owner_type='OWNER'
                                   AND ti.delete_flagged = 0
          JOIN wa_verse_records vr ON vr.term_inv_id = ti.id AND vr.delete_flagged=0
          LEFT JOIN verse_context vc ON vc.verse_record_id = vr.id
                                     AND vc.mti_term_id = mt.id
                                     AND vc.delete_flagged = 0
         WHERE mt.delete_flagged = 0
         GROUP BY mt.strongs_number
    """).fetchall()

    # Annotate with POS + bucket
    enriched = []
    for r in rows:
        s = r["strongs_number"]
        pos = pos_meta.get(s, {}).get("pos")
        if pos in NOISE_POS:
            bucket = f"NOISE: {pos}"
        elif pos in CONTENT_POS:
            bucket = f"CONTENT: {pos}"
        elif pos is None:
            bucket = "UNKNOWN: no STEP morph"
        else:
            bucket = f"OTHER: {pos}"
        enriched.append({
            **dict(r), "pos": pos, "bucket": bucket,
        })

    # Aggregate by bucket
    agg = defaultdict(lambda: {"strongs": 0, "total_vc": 0, "rel": 0,
                               "anchor": 0, "clean_sa": 0, "muddled": 0})
    for r in enriched:
        b = agg[r["bucket"]]
        b["strongs"] += 1
        b["total_vc"] += r["total_vc"] or 0
        b["rel"] += r["rel"] or 0
        b["anchor"] += r["anchor"] or 0
        b["clean_sa"] += r["clean_sa"] or 0
        b["muddled"] += r["muddled"] or 0

    # Render markdown
    L = []
    L.append("# POS-Based Noise Cross-Tab")
    L.append("")
    L.append(f"_Generated {now_iso()}_  ·  source: "
             "`scripts/_exploratory_pos_noise_crosstab_v1_20260503.py`")
    L.append("")
    L.append("Every active OWNER Strong's (3,712) is classified by part-of-speech derived "
             "from STEP's local OSHB / SBLG_th morphology. Verse-context state (anchor / "
             "relevant / set-aside / muddled) is then aggregated per POS category.")
    L.append("")
    L.append("**Filter logic:**")
    L.append("- A Strong's whose POS is a pronoun/particle/preposition/conjunction/")
    L.append("  interjection/article/suffix/adverb is a **grammatical-noise candidate**.")
    L.append("- A Strong's whose POS is noun/verb/adjective carries content; the verse")
    L.append("  classification on it must be evaluated semantically, not auto-filtered.")
    L.append("- The 'suffix' POS is OSHM's tag for pronominal suffixes ('-his', '-her',")
    L.append("  '-my', '-your') attached to nouns and verbs as inflectional morphology.")
    L.append("  These appear as separate Strong's in `mti_terms` and `verse_context` but")
    L.append("  carry no analytical signal in their own right.")
    L.append("")

    L.append("## Cross-tab summary")
    L.append("")
    L.append("| Category | # Strong's | Total vc | Still relevant | Anchors | Cleanly set aside | Muddled |")
    L.append("|---|---:|---:|---:|---:|---:|---:|")
    for cat in sorted(agg.keys()):
        a = agg[cat]
        L.append(f"| {cat} | {a['strongs']:,} | {a['total_vc']:,} | {a['rel']:,} | "
                 f"{a['anchor']:,} | {a['clean_sa']:,} | {a['muddled']:,} |")
    L.append("")

    # Aggregate noise vs content
    def sum_buckets(prefix: str) -> dict:
        out = {"strongs": 0, "total_vc": 0, "rel": 0, "anchor": 0,
               "clean_sa": 0, "muddled": 0}
        for cat, a in agg.items():
            if cat.startswith(prefix):
                for k in out:
                    out[k] += a[k]
        return out

    noise = sum_buckets("NOISE:")
    content = sum_buckets("CONTENT:")

    L.append("## Aggregate noise vs content")
    L.append("")
    L.append("| | # Strong's | Total vc | Still relevant | Anchors | Cleanly set aside | Muddled |")
    L.append("|---|---:|---:|---:|---:|---:|---:|")
    L.append(f"| **NOISE (grammatical)** | {noise['strongs']:,} | "
             f"{noise['total_vc']:,} | {noise['rel']:,} | {noise['anchor']:,} | "
             f"{noise['clean_sa']:,} | {noise['muddled']:,} |")
    L.append(f"| **CONTENT (noun/verb/adj)** | {content['strongs']:,} | "
             f"{content['total_vc']:,} | {content['rel']:,} | {content['anchor']:,} | "
             f"{content['clean_sa']:,} | {content['muddled']:,} |")
    L.append("")

    # Top noise Strong's by anchor count
    L.append("## Top 50 noise Strong's by anchor count")
    L.append("")
    L.append("Each row is a Strong's flagged as grammatical noise that nevertheless "
             "carries one or more **anchor** designations.")
    L.append("")
    noise_strongs = [r for r in enriched if r["bucket"].startswith("NOISE:")]
    noise_strongs.sort(key=lambda r: (-(r["anchor"] or 0), -(r["rel"] or 0)))
    L.append("| strongs | translit | gloss | lang | POS | anchors | still rel | total vc |")
    L.append("|---|---|---|---|---|---:|---:|---:|")
    for r in noise_strongs[:50]:
        L.append(f"| `{r['strongs_number']}` | {r['transliteration'] or ''} | "
                 f"{(r['gloss'] or '')[:30]} | {r['language'][:1]} | {r['pos']} | "
                 f"{r['anchor']:,} | {r['rel']:,} | {r['total_vc']:,} |")
    L.append("")

    # Per-POS breakdown — top 5 each
    L.append("## Top entries per noise category")
    L.append("")
    by_pos: dict = defaultdict(list)
    for r in noise_strongs:
        by_pos[r["pos"]].append(r)
    for pos in sorted(by_pos.keys()):
        items = by_pos[pos]
        items.sort(key=lambda r: (-(r["anchor"] or 0), -(r["rel"] or 0)))
        n_str = sum(1 for _ in items)
        n_vc = sum(r["total_vc"] or 0 for r in items)
        n_anc = sum(r["anchor"] or 0 for r in items)
        L.append(f"### {pos} — {n_str} Strong's, {n_vc:,} vc rows, {n_anc} anchors")
        L.append("")
        L.append("| strongs | translit | gloss | lang | anchors | still rel | total vc |")
        L.append("|---|---|---|---|---:|---:|---:|")
        for r in items[:10]:
            L.append(f"| `{r['strongs_number']}` | {r['transliteration'] or ''} | "
                     f"{(r['gloss'] or '')[:30]} | {r['language'][:1]} | "
                     f"{r['anchor']:,} | {r['rel']:,} | {r['total_vc']:,} |")
        L.append("")

    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    payload = {
        "meta": {
            "generated_at": now_iso(),
            "n_strongs": len(enriched),
            "noise_pos_set": sorted(NOISE_POS),
            "content_pos_set": sorted(CONTENT_POS),
        },
        "buckets": agg,
        "strongs": enriched,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, default=str)

    conn.close()
    print(f"Wrote: {OUT_MD}")
    print(f"Wrote: {OUT_JSON}")
    print()
    print(f"NOISE (grammatical):   {noise['strongs']:,} Strong's, "
          f"{noise['total_vc']:,} vc rows, {noise['anchor']:,} anchors")
    print(f"CONTENT (n/v/adj):     {content['strongs']:,} Strong's, "
          f"{content['total_vc']:,} vc rows, {content['anchor']:,} anchors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
