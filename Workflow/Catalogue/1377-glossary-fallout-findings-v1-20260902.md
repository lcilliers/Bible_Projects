# Glossary fallout findings (v1) — developed per 7.4 before 7.3's wording

**Date:** 2026-09-02 · **Escalation:** #1377. Full raw scan output filed at
`Workflow/Catalogue/glossary-fallout-raw-20260902.json` (all ~40 seed terms, unfiltered). This
document is the worked-through analysis — what the fallout actually changes about the wording in
the [`1377-glossary-draft-entries-v1-20260902.json`](1377-glossary-draft-entries-v1-20260902.json) review
file, per your prediction that some findings here would bear on that wording.

## Method

Read-only scan (script kept at
`scripts/discovery/_check_glossary_fallout-20260902.py`, not registered as a utility yet — this is
design-support analysis, the registered `report.glossary_fallout` version is build-plan work) over
`cfg_column.name`/`cfg_column.use` (both databases), `cfg_setting.value`/`.use`, `cfg_prose.value`/
`.use`, word-boundary matched, case-insensitive. Answers 7.4: this **is** the fallout mechanism
described in the design doc §5, run manually now rather than waiting for the registered report to
exist.

## Corrections this scan forces on the draft entries (the "bearing on wording" you expected)

1. **The 4-way delete-marker spelling is not ONE sense — it's at least three.** The design's v1
   worked example treated `delete_flagged`/`deleted`/`delete_flag`/`deprecated` as pure spelling
   variance on a single concept. The scan disproves that:
   - **Plain soft-delete** (most tables, both DBs): "1 = soft-deleted; the row is retained but
     excluded from live use" (`bible_research.verse_context.delete_flagged`).
   - **Version-aware soft-delete** (`iba.verse_lexical.deleted` and its siblings — `hib`,
     `phenomenon`, `operation`, several `passage_*` tables, per the seed's own Part 4 note):
     "rewriting... inserts a fresh row and flips the superseded row's `deleted` to 1" — a
     genuinely different semantic (supersession-on-write), same column name.
   - **Folder-existence state** (`iba.folder_purpose.status`, a `cfg_enum` VALUE not a boolean
     column): "'deleted' is set by Method A when a folder no longer exists on disk" — a third,
     structurally unrelated thing that happens to use the same word.

   Draft entries corrected to three senses (`delete_marker.plain_soft_delete`,
   `delete_marker.version_aware_supersession`, `delete_marker.folder_existence_state`), aliases
   split accordingly — folding all three into one entry would have repeated the exact ambiguity
   the mechanism exists to resolve.

2. **A closely-related but genuinely distinct pattern surfaced that the seed never named:**
   `cfg_table.inactive` / `cfg_column.inactive` / `cfg_enum.inactive` — *"a data table no longer
   in use... marked `inactive=1` here rather than deleted from `cfg_table`"*. This is the
   convention this whole build already relies on (every table above uses `inactive`, not
   `delete_flagged`). Added as its own entry (`config_registration_inactive_flag`) cross-linked
   from the delete-marker entries, specifically so a reader looking up "deleted" is pointed at
   this sibling convention rather than left to independently notice cfg tables use a different
   word for a related idea.

3. **`characteristic` has (at least) five grains live, not three.** The design's worked example
   (programme concept / Model A table / Model B family) undercounted. The scan found two more,
   both real, both currently live:
   - `bible_research.ib_characteristic_legacy` — the Model B *predecessor*, still in the schema
     (29 rows, its own code/name/gist/colour_range fields), distinct from the current
     `ib_characteristic` (1,634 rows) it was superseded by.
   - `bible_research.verse_span_index.characteristic` — a free-text, span-level field ("keyed on
     meaning-in-context and often quoting the verse itself"), structurally unrelated to any of the
     table-level senses — closer to `ib_characteristic`'s "structured counterpart"
     (`verse_span_index.ib_char_id`) than to Model A's `characteristic` table.
   Two entries added: `characteristic.model_b_legacy`, `characteristic.span_level_freetext`.

4. **`operation` is its own same-word-different-things case, not previously flagged in the seed
   at all.** `iba.db`'s `operation` table is a structured, debate-pipeline entity ("NOT NULL by
   design... may only originate from an already-registered phenomenon"). `bible_research.db`'s
   `ib_characteristic.operation` / `ib_observation.operation` are free-text fields describing "what
   the term does in context" as a verbal phrase ('refuse to submit', 'be needy') — a description,
   not a registered object. Added `operation.iba_debate_entity` and
   `operation.legacy_freetext_description` as two senses.

5. **`family` likewise splits in two**, only one of which the seed named:
   `ib_characteristic.family` (48 thematic families, Model B) was already known; the scan also
   surfaced `wa_term_root_family` — an entirely unrelated linguistic/etymological grouping
   ("CHARAH" / "tov" root families). Added `family.ib_characteristic_thematic` and
   `family.linguistic_root`.

6. **A pure methodology artefact, worth recording so it doesn't get mistaken for a schema
   finding:** case-insensitive matching on `FLAG` (the T-code / special cluster code) returns the
   same 55+ hits as generic lowercase "flag" (quality flags, research flags, term flags,
   inference flags) — because the scan is case-insensitive and English "flag" is everywhere. This
   is exactly the confusion category the design exists to prevent, so the `FLAG` cluster-code
   entry's `heading` is deliberately written as **"FLAG (cluster code) — not the generic 'flag'
   quality/research marker"** rather than a bare "FLAG", specifically so a search for the word
   doesn't return this entry as if it settled every other "flag" mention.

## Confirmed as originally designed (no wording change needed)

- `cluster` M-code vs C-code split — confirmed exactly as documented (`ib_characteristic.cluster`,
  `verse_span_index.cluster`, `file_manifest.cluster` = M-code; `wa_dim_review_cluster_log.cluster`
  = C-code, unique per row). Extra detail found (the `bucket` column's REVIEW/SUPPLEMENTARY holding
  buckets) folded into the `cluster.mcode` entry's body as elaboration, not a new sense.
- `scope`'s four column-level meanings — confirmed live, plus found the general-English
  `governance.scope_*` family of `cfg_setting` keys (project/app/db scope statements) adding a
  fifth, even-more-generic sense — left as Part 3b-style "sampled, not catalogued" per the design's
  own existing framing, not given its own entry (see Open Points below).

## Open point from 7.2, answered with evidence, decision still needed

Found the second glossary-shaped mechanism the researcher expected might exist:
**`wa_vocab_set`/`wa_vocab_member`** (`bible_research.db`) — 8 declared vocabularies, 39 member
values, each with a `label`/`description`/full supersession mechanism
(`deprecated`/`deprecation_note`/`superseded_by_member_id`) **never once used** (0 of 39 rows
deprecated). Checked its actual content: all 8 sets govern the **retired Dimension Review** stage
(`wa_dimension_index`, `wa_session_b_findings` Stage 2c) — `DIMENSION_LABEL`, `DOMINANT_SUBJECT`,
`DIMENSION_CONFIDENCE`, `QA_FLAG`, `MANUAL_OVERRIDE`, plus three Stage 2c synthesis vocabularies.
CLAUDE.md's own table listing already marks the tables these govern as "Legacy / superseded."

**This is a real judgement call, not decided here:** (a) migrate all 39 as `status='archived'`
Glossary entries (useful if any current prose or researcher lookup still references old Dimension
Review terminology), (b) leave the table as legacy DB content outside this build's scope entirely
(consistent with `feedback_inactive_tables_never_active_inputs` — retired-mechanism content is not
a live input), or (c) something else. Not drafted into the JSON review file pending your call.

## What did NOT get a draft entry, and why

The high-volume generic-English terms (`term`, `word`, `span`, `surface`, `content`, `function`,
`status`, `resolution`, `source`, `registry`, `passage`, `anchor`, `dimension`, `model`) each
returned 20–150+ raw hits — confirmed as genuinely pervasive, ordinary words rather than bounded
collisions with a small number of clear senses. Cataloguing every hit for these would not produce
a usable glossary entry; it would reproduce the seed's own Part 3b judgement ("sample, not
exhaustive"). None drafted this round — left for your open-point-3 call (full sort now vs.
tracked follow-on), now with real hit-volume evidence behind that recommendation rather than a
guess.
