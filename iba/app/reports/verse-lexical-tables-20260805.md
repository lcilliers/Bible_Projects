# Verse-lexical raw data tables — how they relate

Verified live against `iba/app/db/iba.db`, 2026-08-05.

**Verse spine.** `verse` holds one row per verse (osisId, reference, full text). `span` holds one
row per morphological unit within a verse (`verse_id` FK, `position` for order, `surface` text,
`morph_code`, `strong_variant`) — this is the row-level unit T1 reads. `strong_verse` is a flat,
denormalized index of Strong's-number-occurring-in-verse (`strong` + `verse_id`, no position) —
useful for "which verses use this Strong's" lookups, but it is not the per-word evidence; `span` is.

A span's `strong_variant` (one code, or several space-joined for a compound STEP tag — resolved
independently, one per code) is turned into the `meaning` column live, per code, by
`lib/versespanmeaningreport.py:meaning_for_code` — the actual source of the technique doc's
`# | surface | strong | morph | particle | meaning` row, not a static join:

1. `strong.stepGloss` for that exact code — the anchor gloss, always present if the code is
   registered (never base-collapsed).
2. `strong_meaning_parsed` rows for that exact `strong_variant`, ordered by `sort` — the parsed
   sense list, appended to the gloss. If no row exists under the exact variant (pre-split legacy
   data only), it falls back to the rows keyed by the base code (letter suffix stripped).
3. That fallback is checked, not trusted blindly: if sub-lettered sibling codes share the base,
   the fallback text must share real vocabulary with `stepGloss`
   (`gloss_supported_by_tree`) or it's flagged `[AMBIGUOUS]` and re-resolved with a live STEP
   `call2_getInfo` lookup for that exact code (cached per run).
4. For Greek codes only, `strong_lsj_parsed` (`row_type='lookup'`) and `strong_mounce_parsed` rows
   for that code are appended as well.

`strong_lexicon`'s raw HTML blobs and `strong_sense`/`strong_related` are **not** read at
derivation time — they are upstream source / word-family lookup tables, outside this resolved-
meaning path.

**Strong's identity.** `strong` is the master table, one row per Strong's number: `stepGloss`,
`stepTransliteration`, `language`, corpus `count`. `span.strong_variant` is meant to point here, but
coverage is partial: 5,052 Strong's numbers are in `strong` against 59,604 distinct
`strong_variant` values actually tagged on spans — most of the gap is STEP's compound/phrase tags
(e.g. `"G1722 G0054"`, two Strong's numbers space-joined on one span) plus Strong's numbers never
onboarded into the curated master. Do not assume every span resolves into `strong`; check first.

**Lexical range (T2).** `lemma_inventory` is the broader curated lemma list (11,781 keys, both
languages) — gloss + language per lemma, source-stamped `lemma-inventory-master-2026`.
`strong_meaning_tree` and `strong_meaning_parsed` both key on `lemma_key` and cover a narrower
4,570-lemma subset — the StepBible sense-tree entries (ordered `sort`, one row per sense).
`_tree` holds the sense text raw (HTML markup, embedded `<ref>` tags); `_parsed` is the same
content split into structured columns (`gloss`, `verse_refs`, `note`, `row_type`). Read `_parsed`;
`_tree` is provenance for it. `strong_sense` is a one-row-per-Strong's headword index (`head`,
`is_own_lemma`) — a quick single-sense lookup, not the full range.

**Full lexicon text.** `strong_lexicon` holds the raw lexicon prose per Strong's number: `lsj`
(Liddell-Scott-Jones, Greek) and `mounce` (Mounce's dictionary) as single HTML blobs — 1,506 Strong's
covered. `strong_lsj_parsed` and `strong_mounce_parsed` break those same blobs into rows
(`sense_label`/`row_type`, `gloss`, `note`) so individual senses can be read and cited without
parsing HTML at query time.

**Word family.** `strong_related` (38,103 rows) lists, per Strong's number, the other Strong's
numbers in its cognate/related-word family (`related_strong`, `related_form`,
`related_transliteration`, `related_gloss`) — for T2's "is this sense a standing member of the
word's own range" check when a related form is in view.

**Net shape:** `verse → span → strong` is the read path (word, in verse order, tagged to a Strong's
number where resolvable); `strong → {strong_sense, strong_meaning_parsed, strong_lexicon(+parsed),
strong_related}` is the lexical-range fan-out T2/T3 pull from once a span resolves to a Strong's
number.
