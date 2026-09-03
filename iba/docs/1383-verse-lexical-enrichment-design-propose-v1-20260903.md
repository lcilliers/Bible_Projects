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

## 1. Objective — REVISED 2026-09-03

*v1's objective did not capture the researcher's actual instruction and read against an early
document rather than the full chain; corrected here by re-reading #1378 and #1379's full history,
especially the later versions, per direct researcher instruction.*

**Overarching purpose this build serves (per #1378, researcher verbatim, 2026-09-01) — not this
build's own deliverable:** "the focus is to explore how the lexical feeds into the questions.
Maybe the end result of this work is that a finding is produced for each verse and each IB word in
the verse that captures the inner being word lexical analysis — something that fundamentally
answers (not just regurgitates existing raw data)." That end state is Window 2 (HIB/finding
production) territory.

**This build's actual scope: Window 1 only — the validated prerequisite building block**, per the
researcher's own staged plan (#1379 v7, 2026-09-02, session close-out): "once this Window-1
building block is validated, focus shifts entirely to Window 2 (inner-being analysis)... deciding
that is for next time." Window 1 = understanding a verse's own words from its own span/morph/
lexicon data. Not Window 2 (HIB/phenomenon/operation — `operations-ingest`, already live,
untouched by this work). The single bridge rule: anything Window 1 can't resolve from the verse's
own data is recorded `unresolved`, never guessed, never resolved by reaching into another verse.

**Process model — per the researcher's own v7 correction**, superseding the earlier two-layer
"mechanical-then-enriched" framing an earlier round of this design used: **ONE integrated
technical read per verse/passage block.** Genre and language/testament determination are that
read's own first move, not a separate pass. Passage boundaries are self-determining and
sequential — each read hands off the next read's own starting point — not pre-planned across the
whole Bible (rejected by the researcher as premature/infeasible at project scale). Hard ceiling:
20 verses maximum per passage/block, must split if exceeded (decided #1379 v7).

**⚠ Open gate, flagged not silently skipped:** the researcher's own recorded plan for the session
after v7 was, in order: (1) run the documented checklist on more practical example verses/passages
beyond the three already tested (Dan 1:8, Ps 25:2, Hos 2:4); (2) do a deep-dive MANUAL analysis of
those same passages to verify the checklist's results against it; (3) only then move to Developer
Mode to build. This document's own record shows no additional test verses and no manual cross-
check beyond the original three — steps (1) and (2) do not appear to have happened before this
design was drafted. **The exact plan for that validation gate is filed separately:
`1383-verse-lexical-window1-validation-test-plan-v1-20260903.md`** — proposed passage set, exact
methodology, exit criteria. §5 onward below (the schema design) does not depend on that plan
running first and is independently grounded against live schema; but per the researcher's own
sequencing, it is not to be treated as build-ready until that validation phase actually closes.

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

## 5. Schema design (proposed — not yet applied) — REVISED 2026-09-03 per researcher review

**Field-usage correspondence, confirmed live, cast in concrete here per direct researcher
instruction (not just "as designed" — verified):** `surface` = `span.surface`, the literal text at
one span, independent of sense. `grain` (the authoritative sense-resolution unit, per the live
glossary — a lettered sub-entry Strong's code, e.g. `H5315G`) = `verse_lexical.strong`, already
correctly populated from STEP's own sub-entry coding — confirmed identical to
`bible_research.db.wa_verse_term_links.step_subgloss_code` on a live cross-check (`H5315G` "soul",
same code, same gloss, both databases). `resolved_sense` = the further, separate narrowing *within*
a grain to this occurrence's actual sense (stem/voice-selected) — confirmed working correctly at
full scale (551,793 of 551,797 live resolved rows, 99.999%, carry real per-stem narrowing, not a
flat fallback — verified live, `H1288` bless/kneel narrows correctly by stem: Qal keeps "kneel,"
Piel drops it, Niphal shows "be blessed/bless oneself"). These three never get mixed, and nothing
in Window 1's build reads `resolved_sense` where `surface` is meant or vice versa.

### 5.1 `verse_lexical` — mechanical columns, REVISED to include this session's full Layer-1 output

The original 4-column list only covered the earliest-decided mechanical fields. This session's own
drift-mitigation work (proven live against Gal 5:16-17, not just designed) mechanized three more
checks that belong in this same list, not left as manual `verse_lexical_note` judgement calls —
they are deterministic, code-only, zero-selection, the same class as `position`/`surface`:

| column | type | source | notes |
|---|---|---|---|
| `position` | INTEGER | `span.position`, denormalized | mechanical |
| `surface` | TEXT | `span.surface`, denormalized | mechanical |
| `language` | TEXT | `strong.language`, denormalized | mechanical |
| `testament` | TEXT | derived, `cfg_book_order.ordinal` | mechanical, 'OT'/'NT' |
| `is_negator` | INTEGER (0/1) | lookup against `cfg_lexical_code_class` (class='negator') — **NOT a code constant**, per direct researcher instruction (rules belong in config, not code); seeded this session: `H0408`/`H3808`/`H3809`/`G3756`/`G3361`/`G3760`/`G3761`, growable by adding rows, not editing a handler | mechanical |
| `narrative_morph` | TEXT, nullable | Hebrew wayyiqtol / `az`+imperfect flag, derived from `morph_code` pattern | mechanical; the chain test's own signal, promoted from a manual per-verse check to a stored column |
| `gloss_consistent_in_verse` | INTEGER (0/1) | same-code/different-gloss check within the verse — the checklist's own data-quality item, fully mechanical, proven live this session | mechanical; promoted out of `verse_lexical_note` (§5.3 below) — it never needed to be a manual note |
| `party_kind` | TEXT, nullable (`divine`/`human`/`non_human`) | lookup against `cfg_lexical_code_class` (class in `party_divine`/`party_human`/`party_angelic`) — same table as `is_negator`, one home for every code-classification lexicon, not five ad-hoc ones. **Divine-name class verified live this session** (`H0430G`/`H0410G`/`H3068G`, `G2316`/`G2962G`/`G5547`/`G2424G`); `party_human`/`party_angelic` classes flagged as needed but not yet seeded — see the catalogue-finishing document's §4 status table. | mechanical, but ONLY for codes that are themselves a name (a direct party-denoting code) — a pronoun's own `party_kind` is NOT stored redundantly here; it derives via its `entity_link` note's `target_verse_lexical_id`, a two-hop join, not a second stored value. Added per catalogue-mapping work (§7 of the companion coverage document) — this is what makes T0.1.1/T4.1.1/T4.2.1-class questions genuinely answerable from stored data, not just "aggregatable in principle." |
| — | — | **`cfg_lexical_code_class` itself** — new `iba.db` table, `strong_code`/`class`/`evidence_note`/`active`, one row per classified code. Every mechanical column above queries it; none hardcode a code list in a handler. Full spec: catalogue-finishing document §4. | schema addition, this build |

**Note on the "verb — triggered by what, impacts what" checklist item**: reviewing every item
against the schema (per researcher instruction, this pass) surfaced that this item has **no clean
home** in either the mechanical columns above or the `note_type` list below — `chain`/`connective`
cover *some* triggered-by relations, `entity_link` covers *some* impacts, but a verb's general
trigger/impact pair isn't a single, distinct capture point anywhere in the current design. Flagged
as a real gap in this schema, not silently left implicit — needs its own `note_type` or a decision
that `chain`+`connective`+`entity_link` together are judged sufficient coverage.

### 5.2 `passage` — 1 new column

| column | type | notes |
|---|---|---|
| `genre` | TEXT, nullable | manual, set as part of the passage's own read; no catalogue/enum yet — free text this round, per D above (not deferred further, but not over-engineered into a controlled vocabulary before real data exists to design one from) |

### 5.3 new table `verse_lexical_note` — REVISED note_type list

`data_quality` removed from this list — promoted to the mechanical `gloss_consistent_in_verse`
column above (§5.1); it was never a judgement call. **`structural_pattern` added**, per direct
researcher correction this session on escalation #1443: verse-level rhetorical structure (merism,
antithetic parallelism, chiasm, paired-image) is word/verse-relevant — it belongs in Stage 1, not
deferred to an emergent-question log as this document originally (wrongly) recommended. Split,
explicitly: **detecting** that a structural pattern exists (a fact about how specific spans/codes
in this verse relate to each other, derivable from the verse's own morph/syntax data) is Stage 1's
job, captured here; **interpreting what the pattern means for the inner being** is Stage 2's job,
out of this table's scope entirely — this row records the detection only, never the interpretation.

| column | type | notes |
|---|---|---|
| `id` | INTEGER PK | |
| `verse_lexical_id` | INTEGER, FK `verse_lexical.id`, NOT NULL | the code-row this note is about |
| `verse_id` | INTEGER, FK `verse.id`, NOT NULL | denormalized, matches `phenomenon` |
| `passage_id` | INTEGER, FK `passage.id`, NOT NULL | denormalized, matches `phenomenon` |
| `note_type` | TEXT, NOT NULL, `cfg_enum` | `idiom`, `pronoun_resolution`, `noun_relational`, `noun_severity`, `chain`, `connective`, `related_word`, `polarity`, `entity_link`, `inert`, `structural_pattern` (NEW) |
| `resolution_status` | TEXT, `cfg_enum` | `resolved`, `unresolved`, `unclassified`, `not_supported_this_language`, `checked_empty` |
| `target_verse_lexical_id` | INTEGER, nullable, FK `verse_lexical.id` | same-verse resolution target (pronoun/noun/entity-link tests), NULL if unresolved |
| `related_verse_lexical_ids` | TEXT, nullable, JSON array of ids | **NEW** — for `structural_pattern` rows specifically, since a chiasm/merism spans multiple codes, not one target the way pronoun-resolution does; `target_verse_lexical_id` stays single-purpose |
| `value_text` | TEXT, nullable | the finding itself (free text — content varies too much by `note_type` for typed columns without real data to design against yet, matching `simple-steps-not-engineered-designs`) |
| `evidence_text` | TEXT, nullable | what in the verse's own data supports it (morph marker, related-word pull, etc.) |
| `created_at` | TEXT | |
| `deleted` | INTEGER | soft-delete, same convention as every other iba.db table |

**FK link to `phenomenon`/`operation` — DEFERRED, not built this round.** Researcher correction:
`phenomenon` is a HIB-dependent (Stage 2) observation; wiring a Stage-1 table to it now presumes a
Stage-2 schema that doesn't exist yet, and the researcher separately flagged that the findings
infrastructure proper lives in `bible_research.db`, not `iba.db` — an open cross-database question
this build should not try to pre-empt. Parked for Stage 2's own design cycle (per the blueprint
document's C.11), not decided here.

Version-aware write convention matches `lexical.build`'s own (soft-delete + insert on rewrite), not
a new pattern.

### 5.4 Passage determination — ADDED 2026-09-03, a real miss in the original proposal

**Direct researcher question this section answers: does running the new lexical at scale need its
own separate passage-determination process, or is it baked into this pipeline?** Answer: baked in,
same unit of work, per the already-decided "no further prototyping later" rule (A5) — this was
already named as a build requirement in the checklist's own "Passage-coverage build" section
(2026-09-02), items 3 and 4 of which never made it into this document until now. Not a new design,
a missed transcription.

**The gap, checked live and named exactly.** `passage.build` exists and can register a passage, but
its own governing rule (`feasibility-self-assessment`) is a *qualitative* self-assessment supplied
by whoever submits the payload — it does not itself find or propose boundaries, and today's 42
registered passages (777 verses, 2.6% of the corpus) are 100% hand-built. Running Stage 1 across
the whole Bible needs something that doesn't yet exist: a way to propose the *next* candidate
passage as the corpus sweep proceeds, not just register one a human already fully specified.

**The mechanism, and why it isn't circular with "genre is the read's own first move."** A
genre/chain-signal-based **boundary suggester**: given the next un-passaged verse after wherever
the sweep currently stands, propose a candidate block (respecting the 20-verse cap) using cheap,
mechanical proxy signals only — `narrative_morph` density (§5.1), the legacy book-level
`bible_research.db.verse.genre` tag as a rough prior, paragraph/chapter markers. **This is
explicitly not the passage's real genre determination** — that still happens properly, as Stage 1's
own read's first move, only once the passage is actually confirmed and registered. The suggester's
job is narrower and cheaper: propose *where a block plausibly ends*, not *what it is*. No
circularity — the suggester's signals are a boundary heuristic, not a genre claim.

**The human-confirmation gate stays**, matching every other decision this session about the process
model (manual, one-at-a-time, chat-driven — #1379 v1/v7's own repeated framing, not overridden
here): suggester proposes → **researcher confirms or adjusts** → `passage.build` registers it,
unchanged from its own existing mechanism → *then* Stage 1's real read (`lexical.build`/
`lexical.enrich`) runs on that now-registered passage. This is one pipeline with a human gate in
the middle, not two disconnected runs.

**Completion tracking, also missing until now.** `passage` already carries `phenomena_complete_at`
(Window 2's own coverage marker) but nothing equivalent for Stage 1. Add `lexical_complete_at`
(TEXT, nullable, same shape), set once every verse in a passage has a `verse_lexical` row for every
code and — for judgement-bearing items — a `verse_lexical_note` disposition (finding or explicitly
`checked_empty`/`unresolved`, never silently missing). This is what makes "is Stage 1 actually done
for this passage" a checkable fact, not an assumption — the same discipline `phenomenon.set/
control-total` already established for Window 2, applied here for the first time to Stage 1.

## 6. Config registration plan (same unit of work as the schema, per
`config-updated-same-unit-of-work-as-change`)

- **`cfg_table`**: 1 new row (`verse_lexical_note`); `verse_lexical` and `passage` rows already
  exist (updated column set, not new table rows).
- **`cfg_column`**: 4 rows for `verse_lexical`'s new columns, 1 for `passage.genre`, ~10 for
  `verse_lexical_note`'s full column set.
- **`cfg_enum`**: `note_type` (11 values above), `resolution_status` (5 values above).
- **`cfg_step`**: extend existing `lexical.build` (work package `verse-lexical`) to populate the
  mechanical `verse_lexical` columns (§5.1, now 7: position/surface/language/testament/is_negator/
  narrative_morph/gloss_consistent_in_verse/party_kind) — no new step needed there. **Two new
  steps**: `lexical.enrich` (work package `verse-lexical`, `kind='operations'`, scope `passage`,
  handler `iba.app.handlers.lexical:enrich`) — JSON-payload-driven, one passage at a time, writing
  `verse_lexical_note` rows and `passage.genre`, mirroring `phenomenon.set`'s shape; **and
  `passage.suggest_boundary`** (§5.4, `kind='operations'`, scope `verse`, handler
  `iba.app.handlers.passage:suggest_boundary`) — proposes the next candidate passage, output is a
  proposal for the PS entry point to surface for researcher confirm/adjust, never auto-registers.
- **`cfg_setting`**: 1 new row, `key='passage.max_verses'`, `value='20'`, `module='passage'` — the
  hard ceiling decided in #1379 v7, not yet built anywhere (checked live: no numeric ceiling exists
  in `passage.py`/`cfg_setting` today, only the qualitative `feasibility-self-assessment` rule).
- **`cfg_method_rule`**: new rows under `step='lexical.build'` (testament/language derivation,
  `H0853` fix + its evidence) and `step='lexical.enrich'` (genre-is-manual-this-round, chain-test-
  Hebrew-only, related-word-sorting-held-manual, 20-verse cap enforcement, unresolved-not-guessed
  discipline).
- **`cfg_column`**: 1 more row, `passage.lexical_complete_at` (§5.4).
- **PS entry point** (`every-interactive-module-needs-ps-script`): extend the existing
  `iba/app/ps/VerseLexical.ps1` with a new `-Action Enrich` (mirrors how `Operations-Ingest.ps1`
  carries multiple steps of its own package in one file) — not a new PS file, since `lexical.enrich`
  is a new step within the already-PS-covered `verse-lexical` package. `passage.suggest_boundary`
  goes through the existing passage PS entry point (whichever script already carries `passage.build`
  — checked live before build, not assumed).
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
