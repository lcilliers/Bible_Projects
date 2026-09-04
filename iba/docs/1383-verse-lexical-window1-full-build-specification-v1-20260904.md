# Verse-lexical Window 1 (Stage 1) — full build specification (v1)

> **★ CORRECTION (researcher, 2026-09-04, escalation #1383 v23) — the Window 1/Window 2 boundary
> stated throughout this document is wrong, and has been consistently wrong across this escalation's
> whole record.** The boundary was drawn as a **mechanical** one — Layer 1 "mechanical" vs. Layer 2
> "judgement," with anything not cleanly mechanical treated as ambiguous or "adjacent" to Window 1.
> **The actual boundary is definitional, not mechanical:** `verse_lexical`/`verse_lexical_note` (this
> whole document's subject) can **never** carry an inner-being concept, by definition — and **nothing
> in Window 1 ever determines whether something is a phenomenon.** Layer 1 and Layer 2 are **both**
> Window 1 regardless of how mechanical or judgement-bearing the work is; that split is an internal
> Window-1 distinction (how the work gets done), never the Window-1/Window-2 line (what the work is
> about). Three concrete consequences, applied below at their exact locations, not just stated here:
> 1. **§(h)'s `passage_emergent_question` open item is not a 50/50 choice.** A `lexical.enrich →
>    passage_emergent_question` write grant would have Window 1 writing into a table whose purpose is
>    inner-being-adjacent emergent questions — the wrong side of the line. The consistent answer is
>    the second option already on record: hold structural findings in `verse_lexical_note`
>    (`note_type='structural_pattern'`) only, surfaced to Window 2's `closing.set` payload author via
>    the exception report — never a direct Window-1 write into `passage_emergent_question`.
> 2. **§(i) item 3 (the `phenomenon`/`operation` FK link) is not "deferred Window 1 scope."** It was
>    never Window 1's decision to make. `phenomenon`/`operation` are themselves inner-being objects;
>    a link from them into Window 1's tables is Window 2 reaching into Window 1's data, and the
>    link's design belongs entirely to Window 2's own build cycle — not reconfirmed here as "still
>    deferred" the way item 3's current text does, corrected below.
> 3. **The aggregation/rollup layer (design doc/#1383 v12-v13, ~20 catalogue questions) is Window 2
>    work**, not a Window-1 extension — not itself named as a row in this document's schema, but
>    referenced in the knock-on/open-items framing closely enough to need the same correction.
>
> Full record and the same correction applied to `iba/docs/1446-verse-word-analytic-methods-extract-
> v2-20260904.md`: escalation #1383 v23, #1446. This banner is the fix for this document; the
> specific table rows below are also corrected in place, not left to rely on the banner alone.

**Filename:** 1383-verse-lexical-window1-full-build-specification-v1-20260904.md
**Escalation:** #1383
**Instruction this document answers, verbatim (researcher, 2026-09-04):** the existing design/
propose document (`1383-verse-lexical-enrichment-design-propose-v1-20260903.md`, v21 across this
escalation) is still too high-level to approve. This document must show, concretely: (a) governance
— every config that will actively govern the method, full DB row; (b) configs — every config,
existing and new, that will control operations, full DB row; (c) the logic — input params, unit-
of-reading determination, per-field determination and derivation, tables affected; (d) validation —
completeness/quality/objective-alignment per field; (e) error and debug — where, what messages,
how standard controls apply; (f) every PS variant/flag/input's practical behaviour; (g) reporting —
a per-run exception report (the self-audit/validation output) and a separate multi-filter JSON
extract for Phase 2; (h) knock-on changes to every other table (glossary, catalogue, cfg_*); (i)
every conflict, open item, and silently-parked item.

**Relationship to the prior documents.** This document does not replace the design/propose
document's Objective (§1), open-decision recommendations A–G (§3), or the researcher's approval of
those recommendations across v4–v21 of this escalation — those stand. It **operationalises** them:
every schema field and config row the design doc named in outline is given its full row content
here, every mechanism named in prose is given its exact input/output/failure behaviour, and every
place this exercise found a real gap the prior nine documents hadn't surfaced is named as such, not
folded in silently. Nothing below has been built. This is still the PROPOSE stage.

**Sources this document is built from** (read in full before writing this, not sampled): the
design/propose doc (v21), the IB analytical cycle blueprint, the method-and-drift-mitigation doc,
the capture-design-vs-study-purpose doc, the Stage-1 catalogue field-mapping doc, the
catalogue-finishing-and-config-not-code-audit doc, the Window-1 checklist (v1), and the live
`iba.db` schema/config/code queried directly for this document (not assumed from any of the above).

---

## (a) Governance — every rule that actively governs this build, full DB row

Two kinds of governing rule apply: **standing project rules** (`cfg_behaviour_rule`, already live,
apply to this build like every other) and **method rules specific to this build's own steps**
(`cfg_method_rule`, new — see (b) for the full proposed rows). This section lists the standing
rules; (b) carries the new method rules since they're inseparable from the config rows they attach
to.

### A.1 Standing behaviour rules this build must comply with — live rows, `class='sqlite'` unless noted

| id | class | rule_key | rule_text (verbatim, live) | enforcement_status |
|---|---|---|---|---|
| 1 | sqlite | verify-before-acting | "Before any operation that depends on database state (row counts, flag values, existence/absence of a record, referential integrity, or the presence of a prior write), that state must be verified directly against the live database. Acting on assumed, remembered, or previously-reported state is a violation regardless of how recent or reliable the prior report seemed." | context_delivered |
| 11 | sqlite | readonly-by-default | "Open a database connection read-only by default when browsing or checking a claim against iba.db or bible_research.db; use a write connection only with a specific reason." | context_delivered |
| 13 | sqlite | dont-assume-which-database | "Don't assume which database a table lives in. bible_research.db (prose + analytic findings) and iba.db (process control + the entire base data layer) have a defined split; a 'no such table' error usually means the wrong database was opened, not a typo." | context_delivered |
| 61 | sqlite | inactive-tables-never-active-inputs | "If a table, column, or row is marked inactive in the configs..., it is never included in any report, analysis, or result — unless the request explicitly asks to explore historical/inactive data. ... Default to ignoring inactive state entirely..." | context_delivered |
| 48 | sqlite | record-change-log-choke-point | "Every write to a table under record_change_log versioning discipline (prose_section, prose_section_type) must produce a matching record_change_log row..." | mechanically_enforced |

`record_change_log` (id 48/49/50) currently covers only `prose_section`/`prose_section_type` — it
does **not** automatically cover `verse_lexical_note`. Whether this build's judgement-bearing table
should be added to that discipline, or stay on `verse_lexical`'s own simpler soft-delete-only
convention, is a real open item — see (i).

### A.2 Standing governance settings (`cfg_setting`, `module='governance'`) this build must comply with

Quoted verbatim from the live `Start-Iba.ps1` bootstrap output (each is a real `cfg_setting` row,
`key`/`value` pair, `module='governance'`):

| key | value (verbatim) |
|---|---|
| `governance.module.config` | "each operating module must have a config table (or tables) in the cfg_* series to control all aspects of the module's operation" |
| `governance.rules_must_be_config_driven` | "no operational or process rule may exist only in GOVERNANCE.md, BUILD.md, USER-GUIDE.md, or memory without a referenced cfg_* row recording it as the evidence that the configuration control is in operation..." |
| `governance.config_control` | "every configuration entry in any cfg_* table is controlled by the cfg.configmaint rules" |
| `governance.new_utility_registration_timing` | "Any new script or routine, anywhere in the project, must be registered in cfg_utility (and cfg_step/cfg_write_grant if it writes data) in the same unit of work it is created..." |
| `governance.module_utility_test_plan` | "...every module/utility design must include a test plan covering all its meaningful interaction/parameter/option combinations...RUN after the approved design is built...actual results are included in the build's escalation resolution, not just asserted." |
| `governance.tables` | "each table in the project must be listed in cfg_table with a proper use text. This applies to all databases. Tables no longer in use must be set as inactive." |
| `governance.table_columns` | "each column in each table in the project must be listed in cfg_column with a proper use text. ... Updating a column in any routine must validate the use of the column against this config." |
| `governance.reports_must_persist` | "every quality-check or report-producing step must persist its output to a config-defined report path — a terminal print + an escalation row is not sufficient..." |
| `governance.ps_worksheet_sync_on_change` | "any change to a PS scripts declared parameters ... must be reflected in the same unit of work in iba/docs/ps tools worksheet.xlsx..." |
| `governance.build_md_on_code_change` | "any code change under iba/app/** must update iba/app/BUILD.md in the same unit of work" |
| `governance.governance_md_on_rule_change` | "any governance/process rule change must be set in cfg_* first (via configmaint.propose), then GOVERNANCE.md updated to reflect it in the same unit of work" |
| `governance.escalation.scope` | "all open items, discovery of anomalies, clarifications and other forms of escalation must be recorded in escalation using escalation rules" |
| `governance.project_change_rule` | "Any change of operations, methodologies or approach must channel through the IBA App. Any operation defined in the past that is not in the IBA app must be migrated to the app." |
| `governance.scope_iba_db` | "The iba_db is the home for all project process control and base data, including all related tables from STEP through Strongs, verses, meaning, and lexicals..." |
| `governance.verse_gap_by_design` | "...a verse missing from iba.db's verse table...is BY DESIGN, not a data-integrity error...Verse-existence is gated on prior term discovery... Both report.verse_span_meaning...and report.passage_debate note each detectable gap inline...and skip straight to the next available verse..." |

**How each actually binds this build**, not just listed:
- `governance.scope_iba_db` settles (a): every new table/column below lives in `iba.db`, not
  `bible_research.db` — consistent with every existing precedent table this build extends
  (`verse_lexical`, `passage`, `phenomenon`).
- `governance.verse_gap_by_design` settles a real question the passage-boundary suggester (§5.4 of
  the design doc) would otherwise hit: a book-sweep that reaches a missing verse (2,049/31,086,
  6.59% of the corpus) does not escalate or stop — it notes the gap and proceeds to the next
  available verse, the same discipline `report.verse_span_meaning`/`report.passage_debate` already
  apply. Named explicitly here because §5.4 of the design doc didn't address it.
- `governance.new_utility_registration_timing` + `governance.module_utility_test_plan` together
  mean: `lexical.enrich`'s handler, `passage.suggest_boundary`'s handler, and the `report.
  lexical_extract`/`report.lexical_exceptions` steps (§g below) each need a `cfg_utility` row, a
  `cfg_step` row, `cfg_write_grant` rows, **and** a written test plan (§(d) below is that plan's
  content) — all in the same unit of work as the code, not after.
- `governance.rules_must_be_config_driven` is what makes `cfg_lexical_code_class` a `cfg_*` table
  (not an ordinary data table) — see the correction under (b) §B.1.

---

## (b) Configs — every config row, existing and new, full DB row

### B.1 Correction found while writing this section, not in any prior document

`cfg_lexical_code_class` was proposed in the design doc as a plain schema addition alongside
`verse_lexical_note`. Checked live against `cfg_table.category`'s actual values (`data` / `log` /
`rule`): every existing lookup/rule table of this shape — `cfg_enum`, `cfg_book_order`,
`cfg_method_rule`, `cfg_setting` — is filed `category='rule'`, not `data`, and (per
`governance.config_control`) every `cfg_*`-prefixed table's rows are maintained through
`configmaint.propose` (approval-gated), never a direct `INSERT`. **`cfg_lexical_code_class` is
therefore a `rule`-category config table, and growing its lexicon (adding a new negator/connective/
divine-name/human-name/angelic-name code) is a `configmaint.propose` action each time, not a quick
direct write** — a real operational consequence for how "the lexicon grows by evidence" (design doc
§3.G) actually happens in practice. This corrects an implicit assumption in the design doc, not a
change of plan.

### B.2 `cfg_table` — existing rows this build reads/extends (unchanged, quoted for reference)

| database | name | grain | use | category |
|---|---|---|---|---|
| iba | verse_lexical | "one row per Strong's code within a span (span_id, code_ordinal) — a compound span yields several rows, one per component code" | "L4b — DERIVED, version-aware. The mechanical T1-T3 reading... Read by report.verse_lexical and, downstream, by T4-T9 — never by re-deriving from span/strong/strong_meaning_parsed directly." | data |
| iba | passage | "one row per passage — a reading frame (global, per book)" | "extends a characteristic's context to adjacent verses for assessing movement/process/qualifying spans; NOT a thematic unit" | data |
| iba | phenomenon | "phenomenon" | "the phenomena register (Step 3 output) — one row per HIB per verse per passage." | data |
| iba | span | "ONE ROW PER HTML <span> TAG of a verse (O3)..." | "L4a - SOURCE, immutable..." | data |
| iba | strong_related | "one row per (strong, related strong) pair STEP's getInfo returned" | "L2b — NOT derived from any raw table; fetched live from STEP..." | data |

### B.3 `cfg_table` — new rows proposed

| database | name | grain | use | category |
|---|---|---|---|---|
| iba | `verse_lexical_note` | "one row per (verse_lexical_id, note_type) — the judgement-bearing Layer-2 finding for one code, one test" | "Stage 1 Layer 2 output. Written by lexical.enrich, one passage-block at a time. FK to verse_lexical; passage_id/verse_id denormalized matching phenomenon's own precedent. NOT read by Window 2's phenomenon/operation writers (no FK link this increment — see open item, §i)." | data |
| iba | `cfg_lexical_code_class` | "one row per (strong_code, class) — a code-classification lexicon entry" | "The single home for every mechanical code-classification lookup this build needs (negator, connective-type, party-kind lexicons) — governance.rules_must_be_config_driven; queried by lexical.build/lexical.enrich, never hardcoded. Rows are configmaint.propose-gated, same as every other cfg_* table." | **rule** (corrected, §B.1 — not `data`) |

### B.4 `cfg_column` — existing rows for `verse_lexical` (unchanged; quoted so the new columns'
placement is clear against what's already there)

| name | ordinal | type | notnull | fk | use |
|---|---|---|---|---|---|
| id | 0 | INTEGER | 1 | — | surrogate PK |
| span_id | 1 | INTEGER | 1 | span.id | "which span this reading is for" |
| verse_id | 2 | INTEGER | 1 | verse.id | "denormalized from span... query without joining through span" |
| code_ordinal | 3 | INTEGER | 1 | — | "position of this code within the span's space-joined strong_variant, 0-based" |
| strong | 4 | TEXT | 0 | strong.strongNumber | "the single code this row resolves" |
| morph_code | 5 | TEXT | 0 | — | "this code's own morph slice" |
| role | 6 | TEXT | 1 | — | "'content' ... or 'function' ... Classification metadata only" |
| status | 7 | TEXT | 1 | — | "'resolved' ... or 'unregistered'" |
| resolved_sense | 8 | TEXT | 0 | — | "stem/voice-selected sense text for 'resolved' rows" |
| ambiguity_note | 9 | TEXT | 0 | — | "set only when the sibling/base-fallback ambiguity check fires" |
| created_at | 10 | TEXT | 1 | — | ISO-8601 UTC |
| deleted | 11 | INTEGER | 1 | — | "version-aware soft-delete... rewriting a (span_id, code_ordinal) inserts a fresh row" |

### B.5 `cfg_column` — new rows proposed, `verse_lexical` (ordinals 12–19, appended)

| name | ordinal | type | notnull | dflt | fk | use | filled_by |
|---|---|---|---|---|---|---|---|
| `position` | 12 | INTEGER | 1 | — | — | "span.position, denormalized — mechanical, no judgement" | lexical.build |
| `surface` | 13 | TEXT | 0 | — | — | "span.surface, denormalized — the literal text at this span, independent of sense (never confused with resolved_sense — see grain-vs-resolved_sense glossary entry, §h)" | lexical.build |
| `language` | 14 | TEXT | 1 | — | — | "strong.language, denormalized — 'Hebrew'/'Greek'/'Aramaic'" | lexical.build |
| `testament` | 15 | TEXT | 1 | — | — | "derived: 'OT' if cfg_book_order.ordinal<=38 else 'NT' (Mal=38/Matt=39 boundary) — pure ordinal derivation, no reference table" | lexical.build |
| `is_negator` | 16 | INTEGER | 0 | NULL | — | "1 if strong is in cfg_lexical_code_class WHERE class='negator' AND active=1, else NULL (never 0 — NULL means 'not in the lexicon,' 0 is not a meaningful negative here since most codes are simply not negators)" | lexical.build |
| `narrative_morph` | 17 | TEXT | 0 | NULL | — | "Hebrew wayyiqtol / az+imperfect flag, derived from morph_code pattern — NULL unconditionally for language != 'Hebrew' (no guessed Greek equivalent — see cfg_method_rule narrative-morph-hebrew-only)" | lexical.build |
| `gloss_consistent_in_verse` | 18 | INTEGER | 1 | — | — | "1 unless this (strong, morph_code) pair carries >1 distinct resolved_sense value among this verse's own rows — mechanical data-quality check, promoted out of verse_lexical_note; see cfg_quality_flag distinct from analytical flags" | lexical.build |
| `party_kind` | 19 | TEXT | 0 | NULL | — | "'divine'/'human'/'non_human' — set ONLY when this code IS ITSELF a name (cfg_lexical_code_class class IN party_divine/party_human/party_angelic); a pronoun's own party_kind is NOT stored here, it derives via its entity_link note's target_verse_lexical_id (two-hop join). party_angelic codes resolve to party_kind='non_human' at this column's own 3-value grain — the finer angelic/adversarial distinction lives in cfg_lexical_code_class.class itself, queried directly where T4.6.1-class questions need it, not re-exposed as a 4th party_kind value (clarified this pass, not changed from the design doc)." | lexical.build |

### B.6 `cfg_column` — new row proposed, `passage`

| name | ordinal | type | notnull | fk | use | filled_by |
|---|---|---|---|---|---|---|
| `genre` | 24 | TEXT | 0 | — | "manual, set as part of lexical.enrich's own first move for this passage; no controlled vocabulary yet — free text this round (design doc §3.D). NOT ported from bible_research.db.verse.genre (book-level, confirmed too coarse — wrong on its own Dan 1:8 tag)." | lexical.enrich |
| `lexical_complete_at` | 25 | TEXT | 0 | — | "NULL until every verse in this passage has a verse_lexical row for every code AND (for judgement-bearing codes) a verse_lexical_note disposition — set only by an explicit control check (mirrors phenomena_complete_at), never by trust." | lexical.enrich |

(`passage`'s existing 24 columns — `id` through `phenomena_complete_at`/`open_decisions_note`/
`story_summary`/`feasibility_note` — are unchanged; full existing set already quoted in the schema
dump, not repeated here since none of them change.)

### B.7 `cfg_column` — new rows proposed, `verse_lexical_note` (full table)

| name | ordinal | type | notnull | fk | use | filled_by |
|---|---|---|---|---|---|---|
| `id` | 0 | INTEGER PK | 1 | — | surrogate PK | lexical.enrich |
| `verse_lexical_id` | 1 | INTEGER | 1 | verse_lexical.id | "the code-row this note is about" | lexical.enrich |
| `verse_id` | 2 | INTEGER | 1 | verse.id | "denormalized, matches phenomenon's own precedent" | lexical.enrich |
| `passage_id` | 3 | INTEGER | 1 | passage.id | "denormalized, matches phenomenon's own precedent" | lexical.enrich |
| `note_type` | 4 | TEXT | 1 | — | "cfg_enum note_type — idiom / pronoun_resolution / noun_relational / noun_severity / chain / connective / related_word / polarity / entity_link / inert / structural_pattern" | lexical.enrich |
| `resolution_status` | 5 | TEXT | 1 | — | "cfg_enum resolution_status — resolved / unresolved / unclassified / not_supported_this_language / checked_empty" | lexical.enrich |
| `target_verse_lexical_id` | 6 | INTEGER | 0 | verse_lexical.id | "same-verse resolution target (pronoun/noun/entity-link), NULL if unresolved" | lexical.enrich |
| `related_verse_lexical_ids` | 7 | TEXT | 0 | — | "JSON array of ids — structural_pattern rows only, since a chiasm/merism spans multiple codes" | lexical.enrich |
| `value_text` | 8 | TEXT | 0 | — | "the finding itself, free text — content shape varies too much by note_type for typed columns yet" | lexical.enrich |
| `evidence_text` | 9 | TEXT | 0 | — | "what in the verse's own data supports it (morph marker, related-word pull, etc.)" | lexical.enrich |
| `created_at` | 10 | TEXT | 1 | — | ISO-8601 UTC | lexical.enrich |
| `deleted` | 11 | INTEGER | 1 | — | "version-aware soft-delete, same convention as every other iba.db table" | lexical.enrich |

### B.8 `cfg_column` — new rows proposed, `cfg_lexical_code_class` (full table)

| name | ordinal | type | notnull | fk | use | filled_by |
|---|---|---|---|---|---|---|
| `id` | 0 | INTEGER PK | 1 | — | surrogate PK | configmaint.propose |
| `strong_code` | 1 | TEXT | 1 | strong.strongNumber | "the code this classification applies to" | configmaint.propose |
| `class` | 2 | TEXT | 1 | — | "cfg_enum lexical_code_class — negator / connective_causal / connective_coordinating / connective_purpose / party_divine / party_human / party_angelic" | configmaint.propose |
| `evidence_note` | 3 | TEXT | 1 | — | "why this code is classed this way — traceable-by-construction, never a bare assertion" | configmaint.propose |
| `active` | 4 | INTEGER | 1 | — | "1 = live lookup row; 0 = retired classification, kept for history" | configmaint.propose |

### B.9 `cfg_enum` — new groups proposed

| name | value | ordinal |
|---|---|---|
| `note_type` | idiom | 0 |
| `note_type` | pronoun_resolution | 1 |
| `note_type` | noun_relational | 2 |
| `note_type` | noun_severity | 3 |
| `note_type` | chain | 4 |
| `note_type` | connective | 5 |
| `note_type` | related_word | 6 |
| `note_type` | polarity | 7 |
| `note_type` | entity_link | 8 |
| `note_type` | inert | 9 |
| `note_type` | structural_pattern | 10 |
| `resolution_status` | resolved | 0 |
| `resolution_status` | unresolved | 1 |
| `resolution_status` | unclassified | 2 |
| `resolution_status` | not_supported_this_language | 3 |
| `resolution_status` | checked_empty | 4 |
| `lexical_code_class` | negator | 0 |
| `lexical_code_class` | connective_causal | 1 |
| `lexical_code_class` | connective_coordinating | 2 |
| `lexical_code_class` | connective_purpose | 3 |
| `lexical_code_class` | party_divine | 4 |
| `lexical_code_class` | party_human | 5 |
| `lexical_code_class` | party_angelic | 6 |
| `party_kind` | divine | 0 |
| `party_kind` | human | 1 |
| `party_kind` | non_human | 2 |

(`party_kind` is its own enum, distinct from `lexical_code_class`, per the clarification in §B.5 —
three values at the *column's* grain vs. seven at the *lexicon's* grain.)

### B.10 `cfg_setting` — new row proposed

| key | value | use | module |
|---|---|---|---|
| `passage.max_verses` | `"20"` | "hard ceiling decided #1379 v7 — a passage/reading-block payload exceeding this many verses is refused before any write (too-many-verses), never silently truncated or auto-split" | passage |

### B.11 `cfg_step` — existing row, `lexical.build` (current, to be revised)

| work_package | ordinal | step | handler | scope | does (current, live) | kind |
|---|---|---|---|---|---|---|
| verse-lexical | 0 | lexical.build | iba.app.handlers.lexical:build | book | "verse : verse_lexical extract — mechanical T1-T3 engine: for every code in a span's (possibly compound) strong_variant, classifies role..., stem/voice-selects the operative sense..., and flags — never resolves — the sibling/base-fallback ambiguity case..." | operations |

**Revised `does` text, proposed:** append — "...; from this build onward, also denormalizes
position/surface/language/testament and computes is_negator/narrative_morph/
gloss_consistent_in_verse/party_kind via cfg_lexical_code_class lookups, unconditionally for every
row, no selection (method-and-drift-mitigation doc §2 Layer 1). Also applies the H0853
classify_role exception (design doc §4)."

### B.12 `cfg_step` — new rows proposed

| work_package | ordinal | step | handler | scope | does | kind |
|---|---|---|---|---|---|---|
| verse-lexical | 2 | `lexical.enrich` | iba.app.handlers.lexical:enrich | passage | "Stage 1 Layer 2 — JSON-payload-driven, one passage-block at a time (≤20 verses). Writes verse_lexical_note rows and passage.genre; sets passage.lexical_complete_at once every applicable code in the block has a disposition. Requires lexical.build to have already run for every verse in the block (Layer 1 output is Layer 2's own input, method-and-drift-mitigation doc §2)." | operations |
| build-passages | 1 | `passage.suggest_boundary` | iba.app.handlers.passage:suggest_boundary | verse | "Proposes the next candidate passage boundary (≤20 verses) from the next un-passaged verse, using cheap mechanical proxy signals only (narrative_morph density, legacy book-level genre tag, paragraph/chapter markers) — NOT a genre determination. Output is a proposal for the PS entry point to surface for researcher confirm/adjust; never auto-registers (passage.build still does that, unchanged)." | operations |
| verse-lexical | 3 | `report.lexical_exceptions` | iba.app.handlers.reports:lexical_exceptions_report | passage | "Per-run exception report (§g.1) — every unresolved/unclassified/checked_empty/UNCLASSIFIED-connective disposition and every genuine judgement call from the most recent lexical.enrich run for this passage, laid out for researcher review. Read-only against verse_lexical/verse_lexical_note, never an independent write." | operations |
| verse-lexical | 4 | `report.lexical_extract` | iba.app.handlers.reports:lexical_extract | none | "Multi-filter JSON extract (§g.2) over verse_lexical/verse_lexical_note — passage/verse/surface/strong/lemma filters, each accepting a list or range. Read-only, JSON output, feeds Phase 2 (Stage 2) input assembly." | reports |

### B.13 `cfg_method_rule` — new rows proposed, `step='lexical.build'`

| rule_key | rule_text | source_doc | enforced_by |
|---|---|---|---|
| `language-testament-derivation` | "language and testament are denormalized onto verse_lexical unconditionally, at build time — language = strong.language (verbatim copy); testament = 'OT' if cfg_book_order.ordinal<=38 else 'NT'. Both mechanical, no judgement, run on every row." | design doc §5.1/§3.E | schema: verse_lexical.language/testament + lexical.py:build_for_verse |
| `h0853-function-word-exception` | "H0853 (the Hebrew direct-object marker, stepGloss='[Obj.]') is classified role='function' — classify_role's H9xxx regex gets an explicit, evidence-commented exception set (starting with H0853), not a widened range." | design doc §4 | code: lib/lexical.py:classify_role exception set; data: one-time UPDATE on the 10,521 pre-existing rows |
| `lexical-code-class-lookup-not-hardcoded` | "Every code-classification lexicon (negator, connective-type, party_kind's divine/human/angelic classes) is a queried row in cfg_lexical_code_class, never a hardcoded list/dict in a handler. A code absent from the table is reported UNCLASSIFIED/NULL — never guessed, never silently defaulted." | catalogue-finishing doc §4; governance.rules_must_be_config_driven | schema: cfg_lexical_code_class + lexical.py lookup functions |
| `mechanical-columns-run-on-every-code-no-selection` | "position/surface/language/testament/is_negator/narrative_morph/gloss_consistent_in_verse/party_kind are computed for every verse_lexical row, unconditionally — none is selectively computed based on whether a code 'looks interesting.' Direct structural fix for the selective-attention drift found live 2026-09-03 (Gal 5:16-17, the G1063/G1937-G1939 misses)." | method-and-drift-mitigation doc §1-2 | lib/lexical.py:build_for_verse (single code path, no content-type branch) |
| `narrative-morph-hebrew-only` | "narrative_morph is derived only for language='Hebrew' rows; Greek rows get NULL unconditionally — no guessed Greek chain-test equivalent exists yet." | design doc §3.G | lib/lexical.py |

### B.14 `cfg_method_rule` — new rows proposed, `step='lexical.enrich'`

| rule_key | rule_text | source_doc |
|---|---|---|
| `one-integrated-read-genre-first` | "Genre/language/testament are this read's own first move for the block, not a separate prior pass. One integrated technical read; the only split is Layer1-mechanical/Layer2-judgement within it." | checklist doc correction 2026-09-02; design doc §1 |
| `twenty-verse-cap` | "A payload exceeding 20 verses is refused (too-many-verses) before any row is written — never silently split or truncated." | #1379 v7 |
| `unresolved-not-guessed` | "Where a test cannot resolve from the current block's own data, resolution_status='unresolved' is recorded explicitly — never guessed, never resolved by reaching outside the block. Genuine cross-verse cruxes stay Window 2's job." | checklist doc; design doc §1 |
| `related-word-pull-total-sorting-manual` | "Every content-role code gets a full, unconditional strong_related pull as note_type='related_word' rows. The pull is mechanical/total; same-concept-vs-coincidental sorting is Layer 2, resolution_status='unclassified' until sorted." | checklist doc; design doc §3.F |
| `genre-manual-this-round` | "passage.genre is set manually as part of the same integrated read — not auto-derived, not ported from bible_research.db.verse.genre." | design doc §3.D |
| `structural-pattern-detect-only` | "A structural_pattern note records that a rhetorical relationship exists and which spans — detection only. Interpreting what it means is Stage 2's job, out of this table's scope entirely." | capture-design doc §6; #1443 |
| `phase-separation-layer1-before-layer2` | "Layer 1's complete mechanical output for every code in the block must exist before any Layer 2 note is written for any code in it — mirrors phenomenon.set/phase-separation, rescoped to Layer1/Layer2 within one block." | method-and-drift-mitigation doc |
| `completeness-by-code-count` | "A block's Layer-2 pass is complete only when every non-inert code has ≥1 note row (a finding, or an explicit checked_empty/not_supported_this_language/unresolved) — a known, checkable total, not trust. Mirrors phenomenon.set/control-total." | method-and-drift-mitigation doc §2; capture-design doc §4 |

### B.15 `cfg_method_rule` — new rows proposed, `step='passage.suggest_boundary'`

| rule_key | rule_text | source_doc |
|---|---|---|
| `proxy-signals-not-genre-determination` | "The suggester proposes a candidate end-point using cheap mechanical proxy signals only (narrative_morph density, legacy book-level genre tag, paragraph/chapter markers) — explicitly NOT the real genre determination, which still happens as lexical.enrich's own first move once the passage is confirmed. No circularity." | design doc §5.4 |
| `human-confirmation-gate` | "Suggester proposes → researcher confirms/adjusts → passage.build registers unchanged from its own existing mechanism. The suggester never auto-registers." | design doc §5.4 |

### B.16 `cfg_write_grant` — new rows proposed

| writer | table_name | database |
|---|---|---|
| lexical.build | verse_lexical | iba |
| lexical.enrich | verse_lexical_note | iba |
| lexical.enrich | passage | iba |
| passage.suggest_boundary | *(none — read-only, proposes only, no table write)* | — |

(`lexical.build → verse_lexical` already exists live, unchanged. `lexical.enrich → passage` is
needed because it sets `genre`/`lexical_complete_at`, the same pattern `phenomenon.set` already has
two grants — `phenomenon` and `passage` — for its own phase-gate write.)

### B.17 `cfg_utility` — existing row to update, new rows to add

Existing: `lexical` / `iba/app/lib/lexical.py` / purpose "the lexical (verse_lexical) engine: T1-T3
of the verse-lexical technique" — **purpose text needs updating** once `lexical.enrich` is added to
the same file (or a new module, `lib/lexicalenrich.py` — a real implementation decision, not
pre-empted here, see (i)).

New (if `lexicalenrich.py` is a separate module): `lexicalenrich` / `iba/app/lib/lexicalenrich.py` /
"Stage 1 Layer 2 engine: verse_lexical_note capture + passage.genre/lexical_complete_at, JSON-
payload-driven." New: `passagesuggest` (or folded into `lib/passage.py`, updating its existing
`cfg_utility` row) / purpose "boundary-suggester: proposes the next candidate passage from cheap
mechanical proxy signals."

### B.18 — new rows completing `1446` §2c's candidate refinements

**Researcher instruction, verbatim, 2026-09-04:** "the design proposal at this point does not take
1446 2a, 2b, and 2c full into account."

Checked against `1446-verse-word-analytic-methods-extract-v2-20260904.md` §2c item by item. Three
of its five candidates already had a real home in this document (the `az`+imperfect chain signal —
§B.5's `narrative_morph` field; the connective 3-way split — §B.9's `lexical_code_class` enum, §D.2's
quality rule; genre and the connective calibration are both already built into §C.2). **Two had no
home at all — added here, not previously in any version of this document:**

| new `note_type` value | ordinal | What it tests | Source (1446 §2c) |
|---|---|---|---|
| `recurrence_role_shift` | 11 | the same `(strong, morph_code)` pair recurs ≥2 times in one verse, but its grammatical/rhetorical **role** shifts across occurrences (e.g. subject → object → predicate) — a genuine judgement call (does the shift carry rhetorical weight, or is it incidental repetition), not mechanical | `G3056` (John 1:1, "Word": subject → object → predicate); `G2222` (John 1:4, "life": subject → predicate) |
| `cross_lemma_shared_gloss` | 12 | two **different** `(strong, morph_code)` pairs in the same verse resolve to the same English gloss — the inverse of the existing `gloss_consistent_in_verse` mechanical check (same code, different gloss); this is different code, same gloss, and stays a judgement call (Layer 2) rather than a mechanical column because confirming it's a real distinct-lemma coincidence, not a data error, needs the same related-word cross-check the original finding used | `G1937` (Gal 5:17) vs. `G1939` (Gal 5:16) — both "desire," confirmed live as two genuinely distinct Greek roots |

**`cfg_method_rule` additions, `step='lexical.enrich'`** (alongside B.14's existing rows):

| rule_key | rule_text | source_doc |
|---|---|---|
| `recurrence-role-shift-is-judgement-not-mechanical` | "A `recurrence_role_shift` note is written only when the same-code recurrence's role change is judged rhetorically significant (e.g. contributes to the verse's own argument or imagery), not for every mechanical repetition of a code — plain repeated function words (e.g. repeated `H9003` prepositional prefixes) never qualify. `resolution_status` is `resolved` when the shift is judged significant, `checked_empty` when the same code recurs with no meaningful role shift (recorded, not silently skipped)." | 1446 §2c; validation-applied doc, John 1:1/1:4 |
| `cross-lemma-shared-gloss-requires-related-word-check` | "A `cross_lemma_shared_gloss` note may only be written after the related-word pull for both codes has been checked (confirming they are genuinely distinct lemmas, not a data-entry duplicate) — mirrors the discipline that caught G1937/G1939 in the first place (the calibration doc's exhaustive related-word pull, not a surface gloss comparison alone)." | 1446 §2c; #1383 v9 calibration doc |
| `related-word-sorting-language-aware` | "Sorting a `related_word` pull into same-concept/genuine-relative/coincidental is judged differently by language: Hebrew families skew toward root-sharing (triliteral roots, including proper-name-heavy families that are mostly coincidental); Greek families skew toward compound-morphology relationships (e.g. `G2316`'s God-hating/God-fighting/God-breathed compounds, genuinely related by composition). The sorting judgement must account for this difference explicitly, not apply one shape's heuristic to the other language's data." | 1446 §2c; validation-applied doc, Deut 6:5 (`H3824`) vs. John 1:1 (`G3056`/`G2316`) |
| `boundary-ambiguity-recorded-honestly` | "Where a passage/reading-block's own extent is genuinely ambiguous (a couplet's argument arguably continuing into the next verse, etc.), the ambiguity is recorded explicitly as a judgement call on record — never silently resolved either way by picking the more convenient boundary. Matches the practice already demonstrated live (Prov 3:5-6 vs. extending to 3:7, #1383 v8), now stated as a standing rule rather than left as an unrepeated observation." | 1446 §2c; validation-applied doc, Passage 2 summary |

**`cfg_enum` addition** — `note_type` grows from 11 to 13 values (append to §B.9's existing table):
`recurrence_role_shift` (ordinal 11), `cross_lemma_shared_gloss` (ordinal 12).

**Cross-verse resolution, confirmed not just demonstrated — §C.2 corrected, not left as an informal
observation.** 1446 §2b flagged that `pronoun_resolution`/`entity_link` are *specified* as
same-verse-only but were *demonstrated* resolving correctly at passage-block scope (6 confirming
instances, #1383's own validation run) — "not yet built into schema" per that document. Checked
against this document's own §C.2 table: `target_verse` + `target_position` already resolves against
*any* verse's `verse_lexical` row, not restricted to the source row's own verse — the schema already
supports passage-scope resolution; §C.2's row is corrected below (this section) to say so explicitly
rather than leave the impression that cross-verse resolution needs new schema work it does not.

## (c) The logic — input params, unit-of-reading determination, per-field derivation, tables affected

### C.1 `lexical.build` (extended) — mechanical, Layer 1

**Input params** (unchanged from today's live step): `Book` (OSIS code), `Chapters` (whole-chapter
range) **or** `Range` (single-chapter verse range) — mutually exclusive, matching `VerseLexical.ps1`
today. **Unit of reading = one verse at a time**, within the book/chapter/range the caller names —
`lexical.build` does not itself determine passage boundaries; it runs over whatever range it's
given, same as today.

**Per-field determination, added this build** (every row already written by today's live pipeline,
same span/code loop, no new traversal):

| Field | Determined how, exactly |
|---|---|
| `position` | `= span.position` for this row's `span_id` — a straight copy, one join, no logic |
| `surface` | `= span.surface` for this row's `span_id` — straight copy |
| `language` | `= strong.language` for this row's `strong` code — straight copy |
| `testament` | `book`'s `cfg_book_order.ordinal`; `'OT'` if `<= 38`, else `'NT'` — computed once per verse (all codes in a verse share one testament), not per code |
| `is_negator` | `SELECT 1 FROM cfg_lexical_code_class WHERE strong_code=? AND class='negator' AND active=1` — 1 if a row matches, else `NULL` |
| `narrative_morph` | if `language != 'Hebrew'`: `NULL`. Else: regex-match `morph_code` for the wayyiqtol pattern (waw-consecutive + imperfect) already used by the existing chain test; also flags the `az`+imperfect narrative-opening case found live in the Exod 15:1 validation test. Value is the matched pattern name, or `NULL` if neither fires. |
| `gloss_consistent_in_verse` | for this row's `(strong, morph_code)` pair, compare `resolved_sense` against every other row in the same `verse_id` sharing that exact pair; `1` unless ≥2 distinct values found, in which case `0` |
| `party_kind` | `SELECT class FROM cfg_lexical_code_class WHERE strong_code=? AND active=1 AND class LIKE 'party_%'` → map `party_divine→'divine'`, `party_human→'human'`, `party_angelic→'non_human'`; `NULL` if no match (this code is not itself a name) |

**Tables affected:** `verse_lexical` only (8 new columns on the existing table, no new rows beyond
what `lexical.build` already writes today — same row count, richer content per row).

### C.2 `lexical.enrich` — judgement, Layer 2

**Input params:** `-PayloadPath` (JSON, matching `phenomenon.set`/`hib.set`'s own convention), plus
`Book`/`Chapters` or `Book`/`Range` to identify the passage-block scope, matching `VerseLexical.ps1`
today.

**Unit-of-reading determination — the actual mechanism, stated exactly:**
1. The payload names an explicit verse range (a passage-block, ≤20 verses) — it does **not** self-
   determine its own boundary at the code level; boundary proposal is `passage.suggest_boundary`'s
   job (§C.3), confirmation is the researcher's, registration is `passage.build`'s. `lexical.enrich`
   receives an **already-registered** passage (`passage.id`) and reads/writes strictly inside it.
2. `lexical.enrich` REFUSES (`too-many-verses`) if the named range's verse count exceeds
   `cfg_setting.passage.max_verses` (20) — checked before any row is touched.
3. `lexical.enrich` REFUSES (`no-passage`) if no live `passage` row covers the named range exactly —
   matching `phenomenon.set`'s own live `no-passage` behaviour (`_find_new_model_passage`), not a
   new pattern.
4. Genre/language/testament are this read's own first move (per `one-integrated-read-genre-first`):
   in practice, the payload's own `genre` field is read and written to `passage.genre` as step one
   of processing the payload, before any `verse_lexical_note` row is written.

**Per-field determination, `verse_lexical_note`** (one row per finding; the payload supplies
`note_type`/`resolution_status`/`value_text`/`evidence_text` per code — `lexical.enrich` resolves
FKs and enforces the rules, it does not itself judge anything):

| Payload key | Resolved to | Determination |
|---|---|---|
| `verse` + `position` (or `strong`+`code_ordinal`) | `verse_lexical_id` | look up the live `verse_lexical` row for this verse's this code; `unknown-code` if no match |
| `note_type` | `note_type` | validated against `cfg_enum note_type`; `bad-payload` if not a member |
| `resolution_status` | `resolution_status` | validated against `cfg_enum resolution_status`; `bad-payload` if not a member |
| `target_verse` + `target_position` (optional) | `target_verse_lexical_id` | resolved the same way as the source code; `unknown-target` if named but unresolvable — **not** silently dropped. **`target_verse` is explicitly not restricted to the source code's own verse (corrected, §B.18)** — any verse within the passage block currently loaded is a valid target, which is exactly the mechanism `pronoun_resolution`/`entity_link` need to resolve at passage scope (demonstrated live, 6 confirming instances across the validation run) rather than only within one verse |
| `related_codes` (optional, `structural_pattern` only) | `related_verse_lexical_ids` (JSON array) | each entry resolved the same way; any one unresolvable fails the whole note (`unknown-related-code`) |
| `finding` | `value_text` | free text, as supplied |
| `evidence` | `evidence_text` | free text, as supplied |

**Tables affected:** `verse_lexical_note` (insert, version-aware — see (e) for the exact write
convention), `passage` (`genre`, `lexical_complete_at` — the latter set only once the completeness
check in §(d) passes for the whole block).

### C.3 `passage.suggest_boundary` — proxy-signal proposal, no write

**Input params:** `Book` (the sweep target); no verse range — it computes its own starting point.

**Unit-of-reading determination:** starts from the first verse in `Book` with no live `passage`
covering it (a plain anti-join against `verse_passage`), then extends forward verse-by-verse while
the cheap proxy signals stay coherent (same `narrative_morph` density band, same legacy
`bible_research.db.verse.genre` book-level tag, no paragraph/chapter-boundary crossed), stopping at
whichever comes first: a genuine signal break, a chapter boundary, or the 20-verse cap.
`governance.verse_gap_by_design` applies here directly: a missing verse encountered mid-sweep is
noted and skipped, not treated as a stopping condition or an error.

**Output:** a proposal object (`{book, start_ref, end_ref, verse_count, signal_summary}`) printed/
returned for the researcher to confirm or adjust — **no table write**, matching `cfg_write_grant`
having no row for this step (§B.16).

---

## (d) Validation — completeness, quality, and objective-alignment, per field

Three distinct validation questions apply to every field, following this session's own
governing-principle #7 ("completeness by structure"): (1) **completeness** — did every applicable
row get a value (or an explicit non-value)? (2) **quality** — is the value actually correct, not
just present? (3) **objective-alignment** — does this field, once populated, actually let a
downstream question (catalogue or Window 2) get answered, per the field-mapping document?

### D.1 Layer 1 (mechanical) fields

| Field | Completeness check | Quality check | Objective-alignment check |
|---|---|---|---|
| `position`/`surface` | 100% of rows (straight copy, cannot be NULL if `span` row exists) | spot-check equals `span.position`/`span.surface` exactly on a sample range | T7.2.1(a) sentence-role questions need this as their base unit |
| `language` | 100% (every `strong` row has a `language`) | matches `strong.language` exactly | T7.1.8/T7.1.9 (OT/NT vocabulary rollups) |
| `testament` | 100% | boundary case each side (Malachi vs. Matthew) + one clearly-interior case each testament, per the design doc's own test plan (§9) | same as above |
| `is_negator`/`party_kind` | count of non-NULL rows should match `SELECT COUNT(*) FROM verse_lexical WHERE strong IN (SELECT strong_code FROM cfg_lexical_code_class WHERE active=1)` exactly — a known total, not "ran without error" | spot-check the 7 divine-name codes, 7 negator codes already verified live (Gal 5:16-17) still resolve correctly after the schema move from prototype script to real column | T0.1.1/T4.1.1/T4.2.1 (party-kind derivation, field-mapping doc §3) |
| `narrative_morph` | 100% of Hebrew rows get a real value-or-NULL (never skipped); 100% of non-Hebrew rows are NULL | re-run against the already-hand-verified Exod 14:31/15:1/15:2 cases (chain test, genre-pivot blind spot) and confirm the same result the validation-applied doc recorded | T7.2.1(b) argument/chain partial |
| `gloss_consistent_in_verse` | 100% (never NULL — always 0 or 1) | re-run against Dan 1:8's known `H0834A` case, confirm `0` | DB-integrity, not analytical — its own quality-flag lineage, not a catalogue question |

### D.2 Layer 2 (judgement) fields, `verse_lexical_note`

**Completeness — the control-total, stated exactly** (mirrors `phenomenon.set/control-total`):
for a given passage-block, the expected note count is `(number of content-role codes × applicable
note-types for that code's part-of-speech) + (number of function-role codes × 1 [inert or
connective/negator-confirmation])`. `lexical.enrich` computes this expected total from Layer 1's
own already-written rows before accepting a payload, and refuses (`incomplete-block`,
§(e)) if the payload's note count for any code falls short — no note type is silently skipped for a
code it applies to.

**Quality** — per `note_type`:

| note_type | Quality check |
|---|---|
| `chain` | `resolution_status='resolved'` only permitted where `narrative_morph` is non-NULL on the source code (a chain claim with no morphological basis is a contradiction, checkable mechanically) |
| `connective` | `value_text` must be one of `cfg_lexical_code_class`'s three connective classes, or `UNCLASSIFIED` — free-text connective types are a quality defect, not a valid finding |
| `related_word` | every row's `target`/`related` code must actually appear in `strong_related` for the source code — a related_word note naming a code STEP itself never related is a quality defect |
| `idiom` | `resolution_status IN ('resolved','checked_empty')` only — `unresolved`/`unclassified` are not valid states for this note_type (an idiom test is binary: found or checked-and-absent) |
| `structural_pattern` | `related_verse_lexical_ids` must contain ≥2 entries (a "pattern" naming only one span is a quality defect — merism/chiasm/parallelism are inherently multi-span) |
| `recurrence_role_shift` (§B.18) | `target_verse_lexical_id` (or `related_verse_lexical_ids`, if >2 occurrences) must point at the same `(strong, morph_code)` pair as the source row — a role-shift note comparing two *different* codes is a contradiction of what this note_type means |
| `cross_lemma_shared_gloss` (§B.18) | the source and target rows must have **different** `strong` values and the **same** `resolved_sense` — a same-code pair belongs to `gloss_consistent_in_verse` (§2a), not here; enforcing the distinction mechanically prevents the two checks' findings from being confused with each other |

**Objective-alignment** — per the field-mapping document's own tables (§2 there): every `note_type`
maps to a named catalogue question or an explicit "no current catalogue question, kept for Window 2
traceability" status; none is speculative capture with no downstream consumer.

### D.3 `passage.genre`/`passage.lexical_complete_at`

**Completeness:** `lexical_complete_at` is set only when D.2's control-total passes for every verse
in the passage AND `genre` is non-NULL — a single field standing in for "Stage 1 is actually done
for this passage," matching the design doc's own stated purpose for it.
**Quality:** no automated check possible (genre is free-text judgement this round, per D above) —
quality here is researcher review at write time, not a mechanical gate.
**Objective-alignment:** T7.2.2 (field-mapping doc §1) is answered directly and completely by this
field alone.

---

## (e) Error handling and debug — every failure point, exact messages, standard controls

This build follows the **exact, already-live error convention** `phenomenon.set`/`hib.set`/
`operation.set` use (`iba/app/handlers/operations.py`) — a `fail(code, message)` tuple, never a raw
exception surfaced to the caller, and never a partial write. No new error-handling pattern is being
invented; every code below is the same shape as the live `bad-payload`/`no-passage`/
`unresolved-reference`/`unreconciled` codes already in production.

### E.1 `lexical.build` (extended) — failure points

| Failure point | Error code | Message shape | Standard control applied |
|---|---|---|---|
| `cfg_lexical_code_class` lookup finds no active table at all (migration not yet run) | `config-not-loaded` | "cfg_lexical_code_class has no active rows — has the migration been run?" | fails the whole build step, not a per-row skip (a config gap is systemic, not per-verse) |
| A code's `morph_code` is malformed for `narrative_morph` pattern matching | *(not a fail — recorded)* | `narrative_morph=NULL`, not an exception | matches the existing `resolve_code`'s own safe-fallback discipline — a malformed input becomes an explicit non-value, never a crash |
| Verse gap encountered mid-range | *(not a fail)* | note + skip, per `governance.verse_gap_by_design` | `gap_note()` already used by `report.verse_span_meaning`/`report.passage_debate` — reused, not reinvented |

### E.2 `lexical.enrich` — failure points

| Failure point | Error code | Message shape | Standard control |
|---|---|---|---|
| Payload has neither `notes` nor `remove` | `empty-payload` | "payload has no 'notes' or 'remove' entries" | matches `phenomenon.set`'s own `empty-payload` exactly |
| Payload malformed JSON / missing required key | `bad-payload` | `str(e)` from the parse/key error | matches `phenomenon.set`'s `_load_payload`/`BadPayload` path exactly |
| Named range has no live `passage` row | `no-passage` | "no tracked passage for {book} this range — run Build-Passages.ps1 (passage.build) first" | matches `phenomenon.set`'s own `no-passage` message shape verbatim |
| Named range's verse count > `passage.max_verses` | `too-many-verses` | "{n} verses exceeds the {cap}-verse cap — split into smaller passage-blocks" | new code, same tuple shape |
| A payload verse/code doesn't resolve to a live `verse_lexical` row | `unknown-code` | "unknown verse/code {verse}:{position} — has lexical.build run for this verse?" | mirrors `hib.set`'s `unknown verse {p['verse']!r}` pattern exactly |
| `note_type` or `resolution_status` not a live `cfg_enum` member | `bad-enum-value` | "'{value}' is not a live {enum_name} member" | new code, same fail() shape |
| `target_verse`/`related_codes` name an unresolvable code | `unknown-target` / `unknown-related-code` | "{n} problem(s): {list[:5]} ..." | mirrors `hib.set`'s truncated-list-of-problems convention exactly (`problems[:5]`, `' ...' if len > 5`) |
| Payload's note count for some code falls short of Layer 1's expected total (§D.2) | `incomplete-block` | "{n} code(s) in this block have no disposition for {note_type}: {list[:5]} ... — every applicable code needs a finding or an explicit checked_empty/unresolved" | new code — the control-total check, phrased the same way `phenomenon.set`'s own `missing` (verse/HIB pair) check is phrased |
| `structural_pattern` note names <2 related codes | `bad-payload` | "structural_pattern note for {code} names {n} related code(s), needs ≥2" | quality gate at write time, not post-hoc |
| Cascade guard: a `remove` targets a note some other structure already depends on | *(not currently applicable — verse_lexical_note has no dependents yet, since the phenomenon/operation FK link is deferred, §i)* | — | flagged as a **future** control, not built this round — see open item |

### E.3 `passage.suggest_boundary` — failure points

| Failure point | Error code | Message shape |
|---|---|---|
| No un-passaged verse remains in `Book` | `book-complete` | "every verse in {book} already belongs to a live passage — nothing to suggest" |
| Proxy signals never stabilise even at 1 verse (a single verse's own signals are internally contradictory — should not occur, defensive only) | `no-stable-boundary` | "could not find a stable boundary starting at {ref} — manual passage.build registration needed" |

### E.4 Standard controls applied throughout (already-live patterns, reused not reinvented)

- **`cfg_write_grant` check (`_may()`)** before any write — `lexical.enrich` calls `_may(ctx,
  'lexical.enrich', 'verse_lexical_note')` and `_may(ctx, 'lexical.enrich', 'passage')`, the same
  call shape `phenomenon_set` makes for `phenomenon`/`passage`.
- **Version-aware writes, never in-place overwrite** — a rewritten `verse_lexical_note` row (same
  `verse_lexical_id`+`note_type`) soft-deletes the superseded row and inserts fresh, matching
  `verse_lexical`'s own convention (`write_readings_for_span`), not `phenomenon.set`'s in-place
  UPDATE convention — because `verse_lexical_note` has no downstream FK dependent yet (unlike
  `phenomenon`, which must UPDATE in place to avoid orphaning `operation.phenomenon_id`).
- **Reconciliation-style dry comparison before writing** — `lexical.enrich` should compare an
  incoming payload's `(verse_lexical_id, note_type)` set against what's already live for the block,
  the same `unchanged`/`changed`/`new`/`removed` split `_reconcile()` already does for
  `phenomenon.set`/`hib.set` — a re-run with identical content is a no-op, not a churn of new rows.
- **Audit trail** — whether `verse_lexical_note` writes get logged to `debate_change_detail`
  (extending its own covered-row-type list) or stay unlogged the way `verse_lexical` itself is
  today is a genuine open item, not decided here — see (i).
- **Exit-code convention** — `lexical.enrich`/`passage.suggest_boundary`, run through
  `VerseLexical.ps1`/`Build-Passages.ps1` and `python -m iba.app.run`, follow the same 0/2/3 exit
  code convention every other step does (0 = ok, 2 = paused, 3 = stopped) — no new PS-level error
  handling needed.

---

## (f) PS variants, flags, and inputs — practical behaviour of each

### F.1 `VerseLexical.ps1` — extended

| Flag | Behaviour today | Behaviour once this build lands |
|---|---|---|
| `-Book <code>` (mandatory) | scopes `lexical.build`/`report.verse_lexical` to one OSIS book | unchanged; also scopes `lexical.enrich`/`report.lexical_exceptions` |
| `-Chapters <range>` XOR `-Range <ch:v-v>` | whole-chapter or single-chapter-verse-range scoping | unchanged; for `lexical.enrich` this names the passage-block (must resolve to a live, ≤20-verse `passage`) |
| `-Step <name>` | restricts the chained run to one step (`lexical.build` \| `report.verse_lexical`) | `-ValidateSet` extended to include `lexical.enrich`, `report.lexical_exceptions`, `report.lexical_extract` — same restrict-to-one-step behaviour, no new mechanic |
| `-PayloadPath <path>` | **does not exist today** (no step currently needs one) | **new**, required when `-Step lexical.enrich` (or omitted, running the full sequence) is used — same convention as `Operations-Ingest.ps1`'s existing `-PayloadPath` |
| `-BookLabel` | folder-name override | unchanged |
| `-RunId` / `-Trace` | resume/re-tag a run; print every config read | unchanged |
| *(no flag)* full sequence | runs `lexical.build` → `report.verse_lexical` | runs `lexical.build` → `lexical.enrich` → `report.verse_lexical` → `report.lexical_exceptions`, in `cfg_step.ordinal` order — **`lexical.enrich` without `-PayloadPath` in the full-sequence case fails fast** (`bad-payload`, missing payload) rather than silently skipping itself; a full run genuinely needs the JSON prepared first |

### F.2 `Build-Passages.ps1` — extended

| Flag | Behaviour |
|---|---|
| `-Book <code>` | unchanged — scopes `passage.build`'s existing recompute |
| `-Suggest` (new switch) | runs `passage.suggest_boundary` first, prints the proposal, and pauses (exit code 2, `Write-IbaPaused`) for the researcher to either re-run with an explicit `-Chapters`/`-Range` matching (or adjusting) the suggestion, or accept it verbatim via a `-Confirm` flag that feeds the same range straight into the existing `passage.build` call — the human-confirmation gate (§C.3) implemented as two ordinary PS invocations, not one opaque auto-confirming call |
| *(no `-Suggest`)* | today's existing behaviour, entirely unchanged — the suggester is opt-in, never runs unasked |

### F.3 New standalone report scripts, or extended `Reports.ps1`/`Catalogue-Report.ps1`

Not yet decided which — a real implementation choice, not pre-empted here (see (i)). Either way:

| Flag (proposed) | Behaviour |
|---|---|
| `-Passage <id>` or `-Book`/`-Range` | scopes `report.lexical_exceptions`/`report.lexical_extract` |
| `-Filter passage:\|verse:\|surface:\|strong:\|lemma:<value-or-list-or-range>` (repeatable, `report.lexical_extract` only) | each filter accepts a single value, a comma-list, or a range (`Gen.1.1-Gen.1.5`, `H0001-H0100`) — combined with AND across distinct filter keys, OR within one key's list; matches `Manifest-Search.ps1`'s own existing `-Query "key:value"` convention, not a new syntax |
| `-Out <path>` | overrides the config-defined report path for this one run (governance.reports_must_persist still requires SOME persisted path — this only lets the caller redirect it, never skip it) |

---

## (g) Reporting — the exception report and the extract, as two genuinely different things

### G.1 `report.lexical_exceptions` — the per-run self-audit / exception report

**Purpose, exact:** after every `lexical.enrich` run, the researcher must be able to see, without
re-deriving it, every unresolved/unclassified/checked_empty/UNCLASSIFIED-connective/genuinely-
parked observation from that run — this **is** the self-audit validation output the method-and-
drift-mitigation doc's "Layer 3 — Reporting, symmetric not curated" section already specified; this
step is that specification, implemented.

**Input:** the `passage_id`(s) just processed by `lexical.enrich` (same run, or named explicitly).
**Output (Markdown, persisted per `governance.reports_must_persist`):**

```
## Exception report — {passage.ref} — run {run_id}

### Layer 1 tally (mechanical, complete enumeration)
- codes processed: N
- negators found: n1 (list)
- connectives found: n2 (n2a causal / n2b coordinating / n2c purpose)
- UNCLASSIFIED connectives: n3 -- POINTS AT THE LEXICON, name each code
- narrative_morph fired: n4 (list, by verse)
- gloss_consistent_in_verse=0: n5 -- data-quality, list each

### Layer 2 dispositions (judgement, complete against Layer 1's total)
- resolved: n6
- unresolved: n7 -- list each, verse:code, with why (no antecedent in block, etc.)
- unclassified (related_word sorting pending): n8
- not_supported_this_language: n9
- checked_empty: n10

### Judgement calls made this run, each labelled
- resolved / genuine-open-question / correction-to-prior-item -- per the drift-mitigation doc's
  own Layer-3 discipline, no "wins" framing, no curated highlights
```

**No "confirms"/"validates"/"closes the gap" framing anywhere in this template** — the exact
correction the researcher made to the first-pass applied document (escalation v9) is baked into the
report's own structure, not left as a style reminder.

### G.2 `report.lexical_extract` — the Phase-2 input, a genuinely different report

**Why this is separate, not the same report with a different format:** the exception report's
audience is the researcher, reviewing one run's own self-check. The extract's audience is **Stage
2's own input-assembly step** (the blueprint's §4) — it needs the raw, already-settled
`verse_lexical`/`verse_lexical_note` content across an arbitrary, possibly cross-passage,
possibly cross-book selection, not one run's own scope.

**Input — multi-filter, every filter list/range-capable, per the researcher's instruction:**

| Filter | Accepts |
|---|---|
| `passage` | one id, a comma-list of ids, or a numeric range |
| `verse` | one `osisId`, a comma-list, or a reference range (`Gen.1.1-Gen.1.10`) |
| `surface` | one literal string, or a comma-list (exact match against `verse_lexical.surface`) |
| `strong` | one code, a comma-list, or a code range (rare but supported for symmetry, e.g. `H0001-H0100`) |
| `lemma` | one `strong_related`-family root, or a comma-list — resolves to every code sharing that family before filtering |

Filters combine with AND across keys; a list/range within one key is OR'd. Omitting every filter is
refused (`no-filter`, §e-style fail tuple) — an unbounded full-corpus extract is not this step's
job (per `feedback_no_full_corpus_push`/`project_api_reads_budget_bounded_small_batches` in spirit,
even though that memory is about STEP calls specifically — the same discipline applies to DB-scale
extracts once this runs at corpus scale).

**Output: JSON**, one object per `verse_lexical` row matched, each carrying its own full row content
plus its `verse_lexical_note` children nested (not a separate join the caller has to do):

```json
{
  "filters_applied": {"passage": [12, 13], "strong": null, "surface": null, "verse": null, "lemma": null},
  "rows": [
    {
      "verse_lexical_id": 40123, "verse": "Gal.5.17", "strong": "G1937", "role": "content",
      "position": 1, "surface": "epithumei", "language": "Greek", "testament": "NT",
      "resolved_sense": "...", "party_kind": null,
      "notes": [
        {"note_type": "related_word", "resolution_status": "unclassified",
         "value_text": "G1939 (desire, noun)", "evidence_text": "strong_related pull"}
      ]
    }
  ],
  "row_count": 1
}
```

This shape is deliberately close to `word.export`'s own existing full-word-JSON precedent (a
registered, live `cfg_step`) and `prose.extract`'s own JSON output mode — not a new export
convention invented for this build.

---

## (h) Knock-on — every other table/document this build touches

| Target | Change | Governed by |
|---|---|---|
| `bible_research.db.wa_obs_question_catalogue` | **Corrected/expanded, 2026-09-04 — this row previously understated the scope.** Three distinct sub-items, not one: (1) new `answered_by` column (needs migration, not yet built); (2) 4 question splits + `T7.2.1` wording fix (catalogue-finishing doc §1-3); (3) **write the Stage-1 field-mapping document's own already-worked-out per-question derivation into `review_note`, for every one of the 27 question codes it names (T0.1.1–T7.2.3) — checked live, this pass: 0/27 have any `review_note` content today; every row's `last_modified` is 2026-08-31 (the Scope-focus classification work), none touched since 2026-09-03's field-mapping pass. The mapping exists only in `1383-verse-lexical-stage1-catalogue-field-mapping-v1-20260903.md`, never applied to the table itself.** Item (3) is immediately actionable now — `review_note` already exists, `obs_catalogue.update` is already registered and ungated — independent of whether/when (1)'s `answered_by` column gets built; (1) is a home for a *rollup* one-liner once it exists, (3) is the underlying derivation text itself. Researcher instruction 2026-09-04: this is the concrete step needed before this knock-on can be called complete. | catalogue-finishing doc §1-3 for (1)/(2); this document + researcher instruction 2026-09-04 for (3) — ordinary content, `obs_catalogue.update` per row, one at a time, not a bulk sweep (matching catalogue-finishing doc §6's own discipline) |
| `bible_research.db.prose_section` id 64 (glossary) | new entries: `Window 1`/`Window 2` (or `Stage 1`/`Stage 2` per the blueprint's renaming), `verse_lexical` (as a term), `note_type` + its 11 values, `testament` (derived-field sense), `passage` (shared unit), `Layer 1`/`Layer 2`, `party_kind`, `grain` vs. `resolved_sense` cross-reference, `structural_pattern`, `passage boundary suggester`, `cfg_lexical_code_class` | catalogue-finishing doc §5; #1377's own governed chapter-edit cycle (`prosestore.py`) |
| **`passage_emergent_question`** | **new finding, this document — corrected 2026-09-04 (see banner), now decided, not open.** #1443's structural findings stay in `verse_lexical_note` (`note_type='structural_pattern'`) only, surfaced to `closing.set`'s own payload author via the exception report. **A `lexical.enrich → passage_emergent_question` write grant is explicitly rejected**, not left open — `passage_emergent_question` is inner-being-adjacent (Window 2's own emergent-question log, single-writer-gated on Window-2 completeness for exactly that reason); a Window-1 process writing to it directly crosses the definitional boundary regardless of how the write grant might otherwise be justified. | governance.new_utility_registration_timing — no new writer needed, so no new `cfg_write_grant` row for this table |
| `iba/app/GOVERNANCE.md` | new rules from §B.13-B.15 recorded (governance.governance_md_on_rule_change) | same-unit-of-work rule |
| `iba/app/BUILD.md` | new build-record entry (governance.build_md_on_code_change) | same-unit-of-work rule |
| `iba/app/USER-GUIDE.md` | new sections for `lexical.enrich`/`passage.suggest_boundary`/the two new reports | user-guide-updated-same-unit-of-work |
| `iba/docs/ps tools worksheet.xlsx` | new tabs/rows for `VerseLexical.ps1`'s new `-PayloadPath`/`-Step` values, `Build-Passages.ps1`'s new `-Suggest`/`-Confirm` | governance.ps_worksheet_sync_on_change |
| `cfg_column` (existing rows, unrelated tables) | none required — no existing column changes meaning, only additions | — |

---

## (i) Conflicts, open items, and items silently parked — the full honest list

**Genuinely open, needs a researcher decision before build:**

1. **`verse_lexical_note` audit-trail coverage** (§(e), E.4) — extend `debate_change_detail` to cover
   it (one shared audit discipline across Window 1 and Window 2), or leave it on `verse_lexical`'s
   own simpler soft-delete-only convention with no separate log row? Not addressed in any prior
   document — found writing this one.
2. ~~`passage_emergent_question` write path for Stage 1~~ — **RESOLVED, 2026-09-04 (see banner):**
   held in `verse_lexical_note` only, no direct write grant for `lexical.enrich`. Moved out of the
   open list; kept struck through here rather than deleted, so the correction has a visible before.
3. **The FK link from `phenomenon`/`operation` back to `verse_lexical`/`verse_lexical_note` — reframed
   2026-09-04 (see banner): this is not a Window-1 item to keep "deferring."** It is Window 2's own
   design decision, full stop — this document has no further standing to reconfirm or reopen it, and
   should not list it as one of *this* build's open items going forward; named here only so the
   correction is visible against the prior text ("already recorded as deferred… reconfirmed here as
   still deferred, not reopened").
4. **`resolved_sense` fallback rate** — the capture-design doc's §5 finding (every sampled code in
   the 19-verse validation run hit the flat `stepGloss` fallback) was investigated 2026-09-03 (v18)
   and found to be a **display artefact**, not a real gap (99.999% of live rows genuinely narrow).
   Closed, not open — listed here only so this document's own honesty-check doesn't imply it's
   still live.
5. **Where `lexical.enrich`'s code lives** — extending `lib/lexical.py`, or a new `lib/
   lexicalenrich.py`? Named as undecided in §B.17, a real implementation choice with a
   `cfg_utility` consequence either way.
6. **Which PS surface carries the two new reports** — extend `VerseLexical.ps1` (fits the existing
   "one file per work package carries every step" convention), or a new dedicated script? Assumed
   `VerseLexical.ps1` in §F for concreteness; not yet confirmed.
7. **`party_angelic`/`party_human` lexicons are not built** — named as needed (T4.3.1/T4.4.1/T4.6.1/
   T4.6.2a/T4.6.3a stay unanswerable until they exist), not a blocker for the rest of this build,
   but a real pre-build task in its own right (catalogue-finishing doc §4).
8. **The "verb — triggered by what, impacts what" checklist item has no clean schema home**
   (design doc §5.1 note) — `chain`/`connective`/`entity_link` partially cover it; whether that's
   judged sufficient or needs its own `note_type` is still open.

**Deliberately, explicitly parked — not silently dropped, not this build's job:**

9. Stage 2 (Level 2/behaviour) design — relation-signal mechanics, the pointer mechanism, Pass 2a/2b
   schema — genuinely open, scoped for after Stage 1 ships (blueprint §4, §9).
10. The `T0.2.1`-class questions (~85 of 181 catalogue questions) — never Stage 1's job, by
    definition (blueprint §6, field-mapping doc §5).
11. `T7.2.1`(argument half)/`T7.2.3` (premise-conclusion structure) — real, named gaps with no owner
    anywhere in the current design (field-mapping doc §5).
12. `T7.1.4`-`T7.1.7`'s mechanical/judgement split — flagged as a follow-on batch, not done this pass
    (catalogue-finishing doc §3).
13. The catalogue's general wording-clarity sweep — the researcher's own observation, explicitly
    scoped as separate, later work (blueprint §6, §10 item 4).
14. Greek gaps generally (`verse_lexical` not working for large parts of the NT) — stays parked per
    direct researcher instruction already on record (#1379).
15. Stage 3 (Publishing) — named, not designed, not touched by this build (blueprint §5).
16. Whether the whole blueprint (Stage 0-3) needs its own escalation split from #1383 — raised in
    the blueprint (§10 item 1), still open, not resolved by writing this document.

**Genuinely resolved, not reopened here (listed only for completeness of this section):**

17. Open decisions A-G (design doc §3) — approved in principle across v4-v21, not relitigated.
18. `H0853` fix — designed, ready to build, unchanged.
19. #1442 (desire noun/verb pair) — resolved as evidence for the Layer-1 related-words mechanism,
    not a build item of its own.

---

## What this document is not

Still not the build. Every schema row, config row, and rule text above is a **proposal** —
`resolution_kind=decision_required`, `next_action_assigned_to=Researcher`, matching the design
doc's own §10 closing statement, which this document doesn't change. The open items in (i),
items 1-8, need answers (or an explicit "recommended reading stands, proceed") before the build
plan (design doc §8) actually starts.
