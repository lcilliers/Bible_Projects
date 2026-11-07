# #2380 — Affix strongs carry the whole span's surface: analysis (2026-11-07)

Raised from #2379 (the surface-work CSV). Read-only analysis: nothing in the database or code was changed. Everything about collections and surface groups is model output and so inferential (B:4). Counts are from the live `iba.db` today.

## 1. What is wrong, in one paragraph

STEP tags one HTML span with every code of a rendering unit (for example `H2519 H9028 H9005 H9038` on "slippery paths") and leaves some English untagged. `span.surface` is the English of the whole unit, and `verse_lexical.surface` copies it onto every code of the span (the recorded meaning of `span.surface` says it "repeats across a word's codes"). So an affix code such as H9005 (to/for) is stored with the surface of the word it is attached to ("children", "workers"). Any step that keys on the surface text and then reads the strong back through `verse_lexical` attributes the affix strong to that word.

## 2. How the surface is set today (checked in code and config)

| Step | What it does | Where |
|---|---|---|
| Parse | `span.surface` is the English of the whole span tag | `span` (cfg_column use: "the English word this code belongs to; repeats across a word's codes") |
| Build | `verse_lexical.surface` is `span.surface` copied to each code of the span | `verse_lexical.surface` (cfg_column use: "span.surface, denormalized"; filled by lexical.build) |
| Fix of 28 Oct (#2326, BUILD 428) | A code in a multi-code span takes the untagged English word just before the span if that word is exactly its STEP gloss. A particle (H9xxx, `discovery.particle_pattern`) is skipped, and every other code keeps the span's word. | `iba/app/lib/lexical.py` `span_code_surfaces`, lines 47 to 81 |

So #2326 never touched affix codes by design, and it only corrects a content code when an untagged word equals its gloss exactly. It changed 1,882 of 544,667 rows (0.35%), none of them H9xxx (checked: 0 live rows with an H9 code differ from their span's surface).

## 3. Scale (live, 544,667 live `verse_lexical` rows)

| Measure | Rows |
|---|---|
| H9xxx or G9xxx rows (affix and grammatical formatives) | 140,144 (25.7%) |
| of which in multi-code spans | 131,024 |
| of which in a span that also holds a non-H9 code (so the surface is another code's word) | 128,002 |
| H9 rows in single-code spans (surface is their own) | 9,118 |
| Rows in multi-code spans of any kind | 285,424 |
| Spans with two or more content codes (surface can belong to only one) | 34,045 spans, 70,981 rows |
| Content rows in multi-code spans with a multi-word surface | 8,072 |

`span.is_particle` is 1 on 10,579 spans only (a span flags only when every code is a particle), so it cannot be used to find these rows.

## 4. Why it reaches the collections (surface cycle)

- `surface_term` is keyed on the surface text alone (cfg_table use: "nothing here is repeated on a (Strong's code, surface) pair"). It holds 6,225 live rows (6,066 surface, 159 computed).
- 3,526 of the 6,066 surface terms (58%) occur on at least one H9 row. None occurs only on H9 rows, so the affix never creates a surface term; it is attributed to it by the join.
- H9 codes are in no M cluster (0 rows in `cluster_strong`) and in no `surface_subgroup` (0 pairs), which is why the cluster, subgroup, domain and concept columns are blank for them in the #2379 CSV.
- In the CSV, 5,908 of 25,715 rows (23%) are H9xxx; the largest are H9002 (986), H9005 (963), H9003 (553), H9009 (437), H9023 (429).

## 5. The problem is wider than affixes (inferential: a sample, not a count of errors)

Content-level codes that STEP tags on the same span also carry the span's word. Random sample of rows (strong, surface stored, span codes, STEP gloss of the strong):

- H3588A, "gave" and "speak" (spans `H5414G H3588A`, `H1696G H3588A`), gloss "for": a conjunction carrying the verb's word.
- H0413, "place" (`H4725 H0413`), gloss "to[wards]".
- H3117G, "life" (`H3117G H9005 H9031`), gloss "day".
- G1525, "entered" (`G1525 G1519`), gloss "to enter": the preposition G1519 would carry "entered" as well.

The rows where the surface shares no word with the STEP gloss number 92,569 of 154,400 content rows in multi-code spans, but that figure mixes real errors with legitimate inflections ("peoples" for "people"), so it is not a count of defects and I do not offer it as one.

## 6. History (written record)

| Escalation | What it said | Outcome |
|---|---|---|
| #1591 (2026-09-07) | 192 rows with surface word-alignment defects (Deut 7:18 H2142 "remember" carrying "of them but you shall"; 1Thess 1:1 empty surfaces) | Superseded into the #1706 rebuild; the repair was dropped as moot and "a post-rebuild data-quality check" was carried forward as a build item (#1706 item 9). I did not verify that this check exists. |
| #2326 (2026-10-28) | Researcher: "I have noticed that you regularly have the wrong surface for multi-span items" | Fixed for non-particle codes with an exact-gloss word before the span; particles and the rest kept the span's word. |
| #2362 (2026-11-06) | Four junk surfaces | Soft deleted in the study layer only; corpus rows untouched. |

So the 28 October fix closed the multi-code case the researcher showed (H5750 "still"), not the systemic cause. The structural cause (one surface per span copied to every code) is unchanged and still runs on every new build.

## 7. What I have not established

- Whether any step other than the surface cycle (readings, `ib_node.surface`, `reading_strand_hit.surface`, subgroup allocation) reads affix rows by surface. `surface_subgroup` holds no H9 pairs, which suggests M-cluster readings are not exposed, but I have not traced them.
- How many content-code misattributions are real errors (section 5 is a sample).
- Whether the #1706 post-rebuild check was built and what it tests.

## 8. Options for the researcher (no design decided; B:105)

A. **Filter at the consumer.** The surface cycle and every surface-keyed join read only rows whose strong is not an affix (and optionally only the span's own word). Smallest change; does not repair `verse_lexical`; each new consumer must remember the filter.

B. **Mark at the source.** Add to `verse_lexical` a recorded kind of surface (own to the code, or the span's word shared by the unit), set by the build, and have consumers read only own surfaces. Heals the whole class, including the content-code cases of section 5, and keeps the span's word for display. Needs a schema change, a build change and a back-fill of 544,667 rows.

C. **Set the surface of affix codes to their own gloss or blank.** Simple to state; breaks anything that reads `verse_lexical.surface` as the word at that position (the strand, node and display code), and loses the link from an affix to its host word.

D. **Extend the #2326 rule to more codes** (function-word content codes such as H3588A, H0413, G1519). Narrower than B; needs a way to tell which code owns which word where a span has several content codes, which STEP does not give.

Recommendation (inferential): B, with A as the interim guard for the surface cycle until B is built, because A alone leaves the cause in place and the same defect has been found by the researcher on 7 September, 28 October and now.
