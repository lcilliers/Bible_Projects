# Verse-lexical Window 1 enrichment — design + propose (v1)

**Filename:** 1383-verse-lexical-enrichment-design-propose-v1-20260903.md
**Escalation lineage:** #1376 (Characteristic model — cross-db inventory and reconciliation) →
#1377 (Vocabulary/glossary, seeded from #1376's own glossary) → #1378 (Lexical-to-finding
pipeline purpose) → #1379 (Verse_lexical rework: intrinsic contextual enrichment — scope
reconciliation + prototype checklist, tested against Ps 25:2 and Hos 2:4) → **this document**,
carried by a new escalation spawned from #1376 per researcher instruction (2026-09-03, Developer
Mode session). `from_id`/`related_activity` were retired 2026-08-27 (#909) — lineage is recorded in
prose (here, and in the new escalation's own context), not a DB link field.
**Stage:** DESIGN + PROPOSE (of the plan → design → propose → test-plan → build-plan → build
cycle). No schema or code changes have been made yet. Awaiting researcher approval before the test
plan / build stage.
**Session:** Developer Mode (`.claude/.developer-mode-active` set 2026-09-03). Per the session's
own standing constraint (§3 of `/developer-mode`), Developer Mode removes only
`configmaint.propose`'s per-row research-approval gate — every other rule below is loaded and
applied in full, including `decision-points-are-terminal-not-inline`: the open decisions (A–G)
below are genuine judgement calls and are answered here as **recommendations for approval**, not
silently decided and built.

**Inputs this document builds from, not re-derives** (per
`feedback_never_model_output_on_prior_unreviewed_pass` — grounded against live schema/code this
session, not copied from the prior docs' own claims):
`Workflow/Catalogue/1379-lexical-to-finding-worked-example-v1-20260901.md` (Dan 1:8 worked example),
`iba/docs/1379-verse-lexical-enrichment-scope-v1-20260902.md` (reconciliation + open decisions A–G),
`iba/docs/1379-verse-lexical-enrichment-checklist-v1-20260902.md` (prototype checklist, v1),
`Workflow/Catalogue/1379-verse-lexical-enrichment-applied-ps25-2-hos2-4-v1-20260902.md` (applied test).

---

## 1. Objective (researcher, this session)

Enrich `verse_lexical` to produce the results the prototype checklist demonstrated on Dan 1:8 /
Ps 25:2 / Hos 2:4 — additional columns, the configs/controls that govern them, an updated glossary,
and every process built to actually follow IBA app governance (registration, method rules, test
plan, PS entry point) rather than being a one-off script.

**Scope: Window 1 only.** Understanding a verse's own words from its own span/morph/lexicon data.
Not Window 2 (HIB/phenomenon/operation — `operations-ingest`, already live, untouched by this
work). The single bridge: anything Window 1 can't resolve from the verse's own data is recorded
`unresolved`, never guessed, never resolved by reaching into another verse.

## 2. What's live today (confirmed this session, not assumed from the prior docs)

- `verse_lexical` (grain: one row per Strong's code within a span): `id, span_id, verse_id,
  code_ordinal, strong, morph_code, role, status, resolved_sense, ambiguity_note, created_at,
  deleted`. Written by `lexical.build` (work package `verse-lexical`, handler
  `iba.app.handlers.lexical:build`, `iba/app/lib/lexical.py`) — mechanical only, T1-T3.
- `span`: `id, verse_id, position, surface, strong_variant, morph_code, is_particle, built_at,
  deleted`.
- `phenomenon` (Window 2 precedent for this design): `id, passage_id, verse_id, hib_id,
  description, textual_warrant, status, ordinal, created_at, deleted` — already denormalizes both
  `passage_id` and `verse_id`, a pattern `verse_lexical` never got.
- `passage`: no `genre` column. `cfg_book_order`: 66 rows, ordinal 0–65, canonical OT-then-NT order
  confirmed — Mal=38, Matt=39, i.e. **testament is a pure ordinal-boundary derivation
  (`ordinal <= 38` = OT, `> 38` = NT), no new reference table needed.**
- `strong.language` exists (Hebrew/Greek/Aramaic) — one join away from `verse_lexical`, never
  denormalized.
- No `cfg_method_rule` rows exist yet for `step='lexical.build'` (checked live, zero rows) — every
  rule this build introduces is genuinely new, not a gap in existing config.
- **`classify_role` bug confirmed live** (`iba/app/lib/lexical.py:67-74`): the Hebrew
  function-word regex only matches the reserved `H9\d{3}` range. `H0853` (the untranslatable direct
  -object marker, `stepGloss='[Obj.]'`) falls outside that range and is classified `content`.
  **10,521 live rows** (`SELECT COUNT(*) FROM verse_lexical WHERE strong='H0853' AND role='content'
  AND deleted=0`) carry this misclassification today. Checked `span.is_particle` as a possible
  existing signal to lean on instead — ruled out: it's set per-*span* (compound-code grouping), not
  per-code, and doesn't track role reliably (157,203 live `role='function'` rows have
  `is_particle=0`) — not the right mechanism for this fix.
- Glossary (`bible_research.db.prose_section` id 64, "Original Language Vocabulary", built #1377):
  checked live — contains none of `Window 1`, `Window 2`, `verse_lexical`, `T1-T3`, `passage`,
  `phenomenon`. All genuinely new entries, not omissions to merely restore.

## 3. Open decisions (A–G, from the #1379 scope doc) — recommendations for approval

**A. Scope of the merge (v4 technique doc vs. worked example vs. operations-ingest).**
**Recommend: do not rewrite `WA-verse-reading-technique-v4` as one merged document.** Its T1-T3 is
already exactly `lexical.build`; its T4 is already exactly `hib.set`/`hib_referent_option`
(confirmed live, `cfg_method_rule` `referent-crux-resolution`); its T6-T9 substantially overlaps
the already-live, differently-named `operations-ingest` pipeline (`hib.set` → `phenomenon.set` →
`operation.set`), which this build does not touch. What v4 actually lacks and this build supplies
is **T5 (genre) and everything the worked example found that T1-T9 never named at all** (idiom
test, polarity, chain/connective, related-word discipline, primary-operation field) — that is
Window 1's real gap, not a full T1-T9 rewrite. Action: add one superseding note to v4's own header
pointing T1-T3 readers to `lexical.build`, T4 readers to `hib.set`, T6-T9 readers to
`operations-ingest`, and Window-1-gap readers to this build's own checklist doc — cheaper and more
accurate than re-deriving one merged spec.

**B. Where the enrichment lives.** **Recommend a hybrid, matching existing grain conventions
already in this schema** (not one big table, not columns crammed onto the wrong grain):
- Cheap, always-computable, per-*code* fields (position, surface, language, testament) →
  **new columns directly on `verse_lexical`** (matches its existing per-code grain; mechanical,
  written by `lexical.build` itself, no judgement involved).
- Genre → **new column on `passage`** (`passage.genre`), not `verse_lexical` or `verse`. Grain-
  correct per the researcher's own 2026-09-02 finding (genre is a passage property, confirmed via
  the John 1:5 case) and avoids repeating an identical value on every code-row of every verse in
  the passage.
- The judgement-derived, per-code-or-span structured findings (idiom/combined-span test, pronoun/
  noun relational-vs-severity classification, chain/sequencing, logical/causal connective,
  related-word raw pull, polarity, entity-linking, data-quality flag, inert-confirmation) →
  **new table `verse_lexical_note`**, one row per (verse_lexical_id × note_type), FK to
  `verse_lexical` plus `passage_id`/`verse_id` denormalized (matching `phenomenon`'s own
  precedent). A single typed table, not nine sparse nullable columns bolted onto `verse_lexical` —
  most codes in a verse won't carry most of these (an article gets only the inert-confirmation
  note; a content noun might get three). `note_type` is a `cfg_enum`, not free text, so it stays
  queryable.

**C. Automation vs. manual capture.** **Recommend (ii): schema/capture structure, populated one
verse/passage-block at a time**, not a `lexical.build`-style scale mechanization. Grounds: (1) the
researcher's own words in #1379 v1 name this directly ("not a repetitive cookie-cutter process...
take it one by one"); (2) every test so far (Dan 1:8, Ps 25:2, Hos 2:4) was hand-driven; (3) it
matches `phenomenon`'s own existing manual-capture pattern (`phenomenon.set`, JSON-payload,
chat/hand-driven), which this design's `verse_lexical_note` table is deliberately built to sit
alongside. The four mechanical columns from (B) still auto-populate at `lexical.build` scale —
only the judgement-bearing note table is manual.

**D. Genre.** **Recommend: `passage.genre` (nullable TEXT), populated manually as part of the same
integrated read that produces the passage's lexical notes — not ported from
`bible_research.db.verse.genre`** (confirmed book-level, too coarse, wrong on its own Dan 1:8 tag),
**and not auto-re-derived this round.** This matches what the prototype already tested (checklist's
process gate: "genre is determined and recorded manually per verse") and resolves the CRITICAL flag
without inventing an unvalidated auto-classifier.

**E. Language/testament.** **Yes — denormalize both onto `verse_lexical`, unconditionally**, per
the scope doc's own "cheap and uncontroversial" framing and confirmed here as genuinely trivial:
language = a straight copy of `strong.language`; testament = `CASE WHEN cfg_book_order.ordinal <=
38 THEN 'OT' ELSE 'NT' END`, computed once at `lexical.build` time (no new reference table).

**F. Related-word enrichment.** **Recommend: hold the sorting out of automation, as the checklist
already concluded** — pull `strong_related` rows mechanically (safe, STEP's own curation) into
`verse_lexical_note` (`note_type='related_word'`), but leave same-concept/genuine-relative/
coincidental sorting as an explicit `resolution_status='unclassified'` field for manual judgement,
since the one mechanical rule tried (`lemma_key` match) failed its own control case in the Dan 1:8
pass.

**G. Hebrew/Greek asymmetry (chain test).** **Recommend: build Hebrew-only now** (waw-consecutive/
wayyiqtol detection via `morph_code`), and **record `note_type='chain', resolution_status=
'not_supported_this_language'`** for Greek verses rather than silently omitting the note — a
positive, checkable fact ("checked, no equivalent test exists yet"), not a silent gap, consistent
with the checklist's own "inert / pure-grammar confirmation" discipline of recording checked-and-
empty explicitly.

## 4. Additional items resolved by this document

- **Logical/causal connective** (surfaced by Hos 2:4, not in the original checklist scope) —
  **fold in as a permanent `note_type='connective'`**, alongside `chain`, in "Finding connections."
  Distinguished from `chain` by testing clause-linkage-by-reason vs. narrated-sequence.
- **`H0853` role-classification bug** — **fix now, in this same build**, per
  `root-fix-not-one-off`: (a) code fix — extend `classify_role`'s Hebrew function-word check with a
  small, explicit, evidence-commented exception set beyond the `H9xxx` range, starting with
  `H0853` (stepGloss `[Obj.]`, a grammatical formative by the same definition the module already
  uses for `H9xxx`); (b) data fix, same unit of work — a scoped correction
  (`UPDATE verse_lexical SET role='function' WHERE strong='H0853' AND role='content' AND
  deleted=0`) for the 10,521 already-written rows, so the fix isn't only forward-looking.
- **Greek gaps generally** (the researcher's 2026-09-02 note that `verse_lexical` "does not work
  for large parts of the NT") — **stays parked**, explicitly out of scope for this build, per
  direct researcher instruction already on record in #1379.

## 5. Schema design (proposed — not yet applied)

### 5.1 `verse_lexical` — 4 new columns

| column | type | source | notes |
|---|---|---|---|
| `position` | INTEGER | `span.position`, denormalized | mechanical |
| `surface` | TEXT | `span.surface`, denormalized | mechanical |
| `language` | TEXT | `strong.language`, denormalized | mechanical |
| `testament` | TEXT | derived, `cfg_book_order.ordinal` | mechanical, 'OT'/'NT' |

### 5.2 `passage` — 1 new column

| column | type | notes |
|---|---|---|
| `genre` | TEXT, nullable | manual, set as part of the passage's own read; no catalogue/enum yet — free text this round, per D above (not deferred further, but not over-engineered into a controlled vocabulary before real data exists to design one from) |

### 5.3 new table `verse_lexical_note`

| column | type | notes |
|---|---|---|
| `id` | INTEGER PK | |
| `verse_lexical_id` | INTEGER, FK `verse_lexical.id`, NOT NULL | the code-row this note is about |
| `verse_id` | INTEGER, FK `verse.id`, NOT NULL | denormalized, matches `phenomenon` |
| `passage_id` | INTEGER, FK `passage.id`, NOT NULL | denormalized, matches `phenomenon` |
| `note_type` | TEXT, NOT NULL, `cfg_enum` | `idiom`, `pronoun_resolution`, `noun_relational`, `noun_severity`, `chain`, `connective`, `related_word`, `polarity`, `entity_link`, `data_quality`, `inert` |
| `resolution_status` | TEXT, `cfg_enum` | `resolved`, `unresolved`, `unclassified`, `not_supported_this_language`, `checked_empty` |
| `target_verse_lexical_id` | INTEGER, nullable, FK `verse_lexical.id` | same-verse resolution target (pronoun/noun/entity-link tests), NULL if unresolved |
| `value_text` | TEXT, nullable | the finding itself (free text — content varies too much by `note_type` for typed columns without real data to design against yet, matching `simple-steps-not-engineered-designs`) |
| `evidence_text` | TEXT, nullable | what in the verse's own data supports it (morph marker, related-word pull, etc.) |
| `created_at` | TEXT | |
| `deleted` | INTEGER | soft-delete, same convention as every other iba.db table |

Version-aware write convention matches `lexical.build`'s own (soft-delete + insert on rewrite), not
a new pattern.

## 6. Config registration plan (same unit of work as the schema, per
`config-updated-same-unit-of-work-as-change`)

- **`cfg_table`**: 1 new row (`verse_lexical_note`); `verse_lexical` and `passage` rows already
  exist (updated column set, not new table rows).
- **`cfg_column`**: 4 rows for `verse_lexical`'s new columns, 1 for `passage.genre`, ~10 for
  `verse_lexical_note`'s full column set.
- **`cfg_enum`**: `note_type` (11 values above), `resolution_status` (5 values above).
- **`cfg_step`**: extend existing `lexical.build` (work package `verse-lexical`) to populate the 4
  mechanical `verse_lexical` columns — no new step needed there. **One new step**,
  `lexical.enrich` (work package `verse-lexical`, `kind='operations'`, scope `passage`, handler
  `iba.app.handlers.lexical:enrich`) — JSON-payload-driven, one passage at a time, writing
  `verse_lexical_note` rows and `passage.genre`, mirroring `phenomenon.set`'s shape.
- **`cfg_setting`**: 1 new row, `key='passage.max_verses'`, `value='20'`, `module='passage'` — the
  hard ceiling decided in #1379 v7, not yet built anywhere (checked live: no numeric ceiling exists
  in `passage.py`/`cfg_setting` today, only the qualitative `feasibility-self-assessment` rule).
- **`cfg_method_rule`**: new rows under `step='lexical.build'` (testament/language derivation,
  `H0853` fix + its evidence) and `step='lexical.enrich'` (genre-is-manual-this-round, chain-test-
  Hebrew-only, related-word-sorting-held-manual, 20-verse cap enforcement, unresolved-not-guessed
  discipline).
- **PS entry point** (`every-interactive-module-needs-ps-script`): extend the existing
  `iba/app/ps/VerseLexical.ps1` with a new `-Action Enrich` (mirrors how `Operations-Ingest.ps1`
  carries multiple steps of its own package in one file) — not a new PS file, since `lexical.enrich`
  is a new step within the already-PS-covered `verse-lexical` package.
- **Dispatch** (`every-active-ps-script-dispatches-through-run-py`): the new `-Action Enrich` goes
  through `run.py` like every other step in `VerseLexical.ps1` already does — not a manual front
  door (that exception is scoped to `Escalation.ps1` only).

## 7. Glossary updates needed (confirmed live: none of these exist yet)

`Window 1`, `Window 2`, `verse_lexical` (as a term, distinct from the table name), `note_type`
(and its 11 values), `testament` (as a derived field, not just the Bible-study sense), `passage`
(as the Window-1/2 shared unit), the `T1-T3`/`T4`/`T6-T9` mapping from §3.A above so a reader can
find which live mechanism actually implements which technique-doc step.

## 8. Build plan (ordered, pending approval)

1. `H0853` fix: code + data correction (§4) — smallest, most self-contained, do first.
2. Schema: `verse_lexical` 4 columns, `passage.genre`, `verse_lexical_note` table + indexes.
3. Config: `cfg_table`/`cfg_column`/`cfg_enum`/`cfg_setting`/`cfg_method_rule` rows (§6).
4. Extend `lexical.build` to populate position/surface/language/testament.
5. Build `lexical.enrich` handler + `VerseLexical.ps1 -Action Enrich`.
6. Glossary entries (§7).
7. `USER-GUIDE.md` update (`user-guide-updated-same-unit-of-work`).
8. `BUILD.md` entry.

## 9. Test plan (per `test-plan-per-module-utility` — required before build is considered
complete, results included in the closing escalation resolution, not just claimed)

- `H0853` fix: re-run on the 10,521 affected rows (or a representative book), confirm `role=
  'function'` post-fix; confirm no other `H9xxx`-range code regresses (spot-check a known content
  code, e.g. `H0413`, still classifies `content`).
- `lexical.build` extension: run on a small already-covered book range; confirm `position`/
  `surface` match `span` exactly; confirm `language` matches `strong.language`; confirm `testament`
  correct on a boundary case each side (Malachi vs. Matthew) and a clearly-interior case each
  testament.
- `lexical.enrich`: run against the two already-hand-verified prototype cases (Ps 25:2, Hos 2:4) —
  confirm the mechanical checks it reproduces (chain test negative on both — no wayyiqtol; polarity
  fires on `H0408`/`H3808`) match the applied doc's own recorded results exactly, not just "runs
  without error." Then run on one fresh, previously-untested verse to confirm it isn't overfit to
  the two known cases. Test the `unresolved` path explicitly (a pronoun/entity-link with no
  same-verse antecedent) and the `not_supported_this_language` path (a Greek verse's chain test).
  Test the 20-verse cap: a passage payload of 21 verses is refused, one of exactly 20 is accepted.
- Config: `configmaint.validate` clean (no unregistered tables/columns) after step 3.

## 10. What this document is not

Not the build itself. Per `decision-points-are-terminal-not-inline`, §3's recommendations (A–G)
are proposals for approval, not decisions already taken — the escalation carrying this document is
raised `resolution_kind=decision_required`, `next_action_assigned_to=Researcher`. Build starts only
after approval.
