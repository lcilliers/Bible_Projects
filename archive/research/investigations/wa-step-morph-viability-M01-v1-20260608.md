# STEP morph extraction — viability prototype (H3372G,H6342,H2729,H7264,H1674,H4035,H3374,G5401,G5156)

> READ-ONLY (`scripts/_prototype_step_morph.py`). Pulls STEP preview HTML per verse and extracts the term's own `morph` code; decodes POS + Hebrew verb STEM (the BDB sense-branch selector). Measures coverage = share of the term's verses where a morph was recoverable. No DB writes.

| Term | Lang | verses | morph found | % | POS | stems (verbs) |
|---|---|---|---|---|---|---|
| H3372G H3372G |  | 194 | 194 | 100% | verb:194 | Qal:179, Niphal:11, Piel:4 |
| H6342 H6342 |  | 25 | 25 | 100% | verb:25 | Qal:22, Piel:2, Hiphil:1 |
| H2729 H2729 |  | 39 | 39 | 100% | verb:39 | Qal:23, Hiphil:16 |
| H7264 H7264 |  | 40 | 40 | 100% | verb:40 | Qal:29, Hiphil:7, Hithpael:4 |
| H1674 H1674 |  | 6 | 6 | 100% | noun:6 | — |
| H4035 H4035 |  | 2 | 2 | 100% | noun:2 | — |
| H3374 H3374 |  | 45 | 45 | 100% | noun:44, verb:1 | Qal:1 |
| G5401 G5401 |  | 43 | 43 | 100% | noun:12, adjective:12, adverb:10, G:9 | — |
| G5156 G5156 |  | 5 | 5 | 100% | G:3, adverb:1, noun:1 | — |

**Overall coverage: 399/399 (100% of occurrences had a recoverable morph)**.

> Viability read: high coverage + clean stem decode ⇒ a STEP morph backfill into `wa_verse_records.morph_code`/`stem` is worth running (would make S2 sense-resolution, 84% of verses, STEP-mechanical). Greek terms carry tense/voice/mood rather than a Hebrew stem.