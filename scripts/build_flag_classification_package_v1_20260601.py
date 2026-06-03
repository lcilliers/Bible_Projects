"""Assemble the FLAG-cluster classification package for Claude AI (chat).

Read-only. Emits a self-contained .md: required-inputs declaration, brief +
disposition rules, cluster taxonomy (targets), all 433 live FLAG terms with data
+ lexical hint, and the strict output JSON schema for the returned patch.

Output: research/investigations/flag-cluster-classification-package-v1-20260601.md
"""
import os
import sqlite3
from collections import defaultdict

DB = "database/bible_research.db"
OUT = "research/investigations/flag-cluster-classification-package-v1-20260601.md"

BRIEF = r"""## Required inputs (self-declaration)

- **Brief:** none separate — this package is self-contained for the FLAG-term classification task.
- **Structural inputs (embedded below):** §A cluster taxonomy (targets) · §C the 433 FLAG terms.
- **Controlling principles (embedded):** §B disposition rules incl. the T1/T2 ontology and the two governing principles.
- **Authoritative provenance (background, not required to act):** `wa-cluster-overview [current]` (cluster model); term-anchor model (clusters are agnostic to registries — a term reaches a cluster only via its own meaning, not its source registry).
- **Pre-decisions already made:** these 433 terms are confirmed live (active verse usage) and currently parked in the FLAG holding cluster; they must each be dispositioned.
- **Out of scope:** characteristic/sub-group placement *within* a cluster (a later step); verse-level relevance; any DB write (CC applies the returned patch).

## Task

For **each** FLAG term, assign exactly one **disposition**:

| disposition | meaning | target_clusters |
|---|---|---|
| `cluster` | a T1 characteristic term — names an inner-life faculty/characteristic that belongs to a cluster | one cluster code (the primary home) |
| `boundary` | genuinely sits between clusters — its meaning bridges two (rarely three) characteristics | the 2–3 candidate cluster codes |
| `t2` | a recipient / effect / modifier / particle / function word — NOT a faculty itself (prepositions, negation, "beloved", etc.) | [] |
| `set_aside` | no inner-life content, or not genuinely attested (object/place/relation only) | [] |

## Disposition rules

1. **Verse meaning is the data.** Classify on what the term *means in use*, not its source registry. Clusters are agnostic to registries.
2. **T1 vs T2 (ontology):** T1 = the characteristic *in operation* (the faculty) → `cluster`. T2 = the recipient/effect/modifier/particle → `t2`. *Example: "beloved" (agapētos) is T2, not the love faculty.*
3. **Particles / function words → `t2`.** A term whose lexical HINT sprays across many clusters (e.g. *para*, *sun*, *mē*) is almost always a preposition/particle — that spray is the signal, not a real multi-cluster membership.
4. **Use `boundary` sparingly** — only when the term truly carries two distinct characteristics, not merely co-occurs with other terms.
5. **`set_aside`** for terms with no inner-life faculty content (physical objects, places, pure relations) or zero genuine attestation.
6. **HINT is a suggestion only** (lexical match of transliteration against a cluster's example-term gloss). Confirm or override on meaning.
7. **Record a one-line `reason` for every term**, grounded in its meaning (all observations recorded — the two governing principles).

## Output (return EXACTLY this JSON, no prose)

```json
{
  "package": "flag-cluster-classification-v1-20260601",
  "classifications": [
    {"strongs": "G2588", "disposition": "cluster",  "target_clusters": ["M30"],        "reason": "kardia = heart; seat of the inner life; core characteristic term."},
    {"strongs": "G3844", "disposition": "t2",       "target_clusters": [],              "reason": "preposition 'para'; function word, not a faculty."},
    {"strongs": "Hxxxx", "disposition": "boundary", "target_clusters": ["M05","M07"],  "reason": "carries both X and Y characteristics."},
    {"strongs": "Hyyyy", "disposition": "set_aside", "target_clusters": [],             "reason": "no inner-life content / not attested."}
  ]
}
```

Process in **batches** (e.g. Greek-high-span first, then Hebrew) — the term list is in a stable order so batches are reproducible. Return one JSON block per batch covering every `strongs` in that batch.
"""


def main():
    c = sqlite3.connect(DB, timeout=20); c.row_factory = sqlite3.Row

    span = defaultdict(int)
    for r in c.execute("SELECT term_id, COUNT(DISTINCT reference) n FROM wa_verse_records WHERE span_strong_match=1 AND COALESCE(delete_flagged,0)=0 AND term_id IS NOT NULL GROUP BY term_id"):
        span[r["term_id"]] = r["n"]

    clusters = c.execute("SELECT cluster_code cc, short_name sn, description descr, gloss FROM cluster WHERE cluster_code LIKE 'M%' ORDER BY cluster_code").fetchall()
    cl_gloss = [(r["cc"], (r["gloss"] or "").lower()) for r in clusters]

    seen = set(); terms = []
    for r in c.execute("SELECT strongs_number sn, transliteration tr, gloss, language lang, COALESCE(status,'') status, owning_registry reg FROM mti_terms WHERE cluster_code='FLAG' AND COALESCE(delete_flagged,0)=0 ORDER BY strongs_number"):
        if r["sn"] in seen:
            continue
        seen.add(r["sn"]); terms.append(r)

    def hint(tr):
        if not tr or len(tr) < 3:
            return ""
        t = tr.lower()
        return ";".join(cc for cc, g in cl_gloss if t in g)

    L = ["# FLAG cluster — classification package (Claude AI / chat)", "",
         "**Type:** AI-facing classification package · **Generated:** 2026-06-01 · **Terms:** 433 live FLAG terms.", "",
         BRIEF, "",
         "## §A. Cluster taxonomy — the `cluster` / `boundary` targets", "",
         "| code | short_name | description | example terms |", "|---|---|---|---|"]
    for r in clusters:
        d = (r["descr"] or "").replace("|", "/").replace("\n", " "); d = (d[:80] + "…") if len(d) > 81 else d
        g = (r["gloss"] or "").replace("|", "/"); g = (g[:70] + "…") if len(g) > 71 else g
        L.append(f"| {r['cc']} | {r['sn'] or ''} | {d} | {g} |")

    L += ["", f"## §C. FLAG terms to classify ({len(terms)}) — stable order (language, span desc)", "",
          "span = distinct active-span verses (usage). HINT = lexical-match suggestion (confirm/override on meaning).", "",
          "| strongs | translit | gloss | lang | span | reg | HINT |", "|---|---|---|---|--:|---|---|"]
    for r in sorted(terms, key=lambda r: (r["lang"] or "", -span.get(r["sn"], 0), r["sn"])):
        g = (r["gloss"] or "").replace("|", "/"); g = (g[:42] + "…") if len(g) > 43 else g
        L.append(f"| {r['sn']} | {r['tr'] or ''} | {g} | {r['lang'] or ''} | {span.get(r['sn'],0)} | {r['reg'] or ''} | {hint(r['tr'])} |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"package written: {len(terms)} terms, {len(clusters)} clusters")
    print("wrote:", OUT)
    c.close()


if __name__ == "__main__":
    main()
