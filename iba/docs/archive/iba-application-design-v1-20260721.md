# IBA Application Design (v1) — the build specification

> **Superseded 2026-07-21 by [`iba-application-design-v2-20260721.md`](iba-application-design-v2-20260721.md),**
> which restructures this document's content along a Data-Layer / Analytic-Layer phase split (no content
> re-resolved — v2 carries every [BUILT]/[DESIGNED]/[OPEN] tag from this file forward unchanged). Kept
> here as the pre-split source; resume design work from v2.
>
> **Status: Step 1 draft, for approval before Step 2 (gap list) and Step 3 (build).** Prepared
> 2026-07-21; **revised same day** to incorporate the researcher's comments (`scratchpad_tmp/comments
> app design v1.txt`) — the configurator ruling (§3), the identity-gap resolution via a prose
> architecture (§5.4), D2/D4/D5 (§5.8), the operation-type resolution (§5.5), and "interactive feedback"
> (§6). The open register (§11) is now 5 items, down from 8. Considerable rule-level detail per module
> is still expected to emerge in the next iterations (§7.3's sextet is filled only for the 3 built
> modules). This is **not a design from scratch** — it organises the thinking and snippets already
> collated (`iba-application-plan-v3-reconstructed.md`, the five `scratchpad_tmp` snippets, and
> `iba-app-design-precedence-and-structure-v1-20260721.md`) into one build-checkable document, and
> grounds every claim about "what exists" against the actual built app (`iba/app/BUILD.md`,
> `iba/app/GOVERNANCE.md`, the live `iba/app/db/iba.db`, queried directly 2026-07-21) rather than
> against what a document assumed. Each claim is tagged **[BUILT]** (proven, in the live app),
> **[DESIGNED]** (decided, not yet built), or **[OPEN]** (genuinely unresolved by any artifact —
> kept short, per instruction, not a list of things I could answer myself).
>
> **Binding note (carried from V3 line 12).** Claude Code has no permission to work on this study
> outside the scope of the IBA app, and must use the app's own approved methods for every DB change —
> including changes to the configurator itself (rule **c** below). This document is written under
> that constraint: nothing in it authorises an ad-hoc DB write.
>
> **Guardrail (researcher, 2026-07-21).** This document designs the components it can anticipate —
> data, analysis, prose — but **not everything from the old build transitions to the App.** The old
> `prose_section` family is the cautionary example already on file: `prose_section_dimension_link` and
> `prose_section_finding_link` were declared, keyed, and never populated (0 rows each — "a plausible
> casualty of the dimension layer's retirement"); `wa_prose_section_citations` was piloted on 25 of
> 1,039 sections and never rolled out. **A construct is only in this design once it is confirmed
> needed** — a proven-but-abandoned old-DB table is evidence *against* copying it, not a template to
> replicate by default. Where this document still can't resolve or build something, it is registered
> in §11, not merely noted as "unclear" in passing — an unresolved point that isn't in §11 is a defect
> in this document.

---

## 0. Governing configuration principles (the north star — 2026-07-21 ruling)

Restated in full, because every section below is evaluated against it, not the other way round. Letters
preserved from the researcher's own statement; the second "g" is relabelled **k** here only to remove
the duplicate label — no content changed.

| # | Rule |
|---|---|
| a | All code, PS and Python, must be **parameter-driven** — no option or processing rule hard-coded. |
| b | A configuration is a table with: **config name · config value (the value the code uses) · where it applies · conditions for applying it · description (what the rule does)** — optionally grouping, dependency, or other relational columns. |
| c | Configurations are maintained through a **`configuration_maintenance` utility module**. That module has its own configuration, but fundamentally it **tracks every change** and **restricts any configuration change to go through it** — including Claude Code making a configuration change. |
| d | The rules governing **every** operation, module, or routine must be set in configuration. |
| e | **Each operating module must have its own configuration.** |
| f | **All rules formulated and accepted over the past six months that are still relevant must be included, explicitly.** No rule is taken for granted. |
| g | App- and study-governance rules that are **not** module-specific must also be included. |
| h | Utilities and special operations must **also** be governed by configuration. |
| i | Every operating module must have: rules governing **creation, update, and deletion** of data · rules governing **the data itself** · rules governing **relationships** · rules setting **output** · rules setting **validity** · rules governing **quality**. |
| j | The same rule must **not** be duplicated in many places — if it applies across many modules, define it once and cross-reference it from where it applies. |
| k | **Naming conventions** across the app are governed by the enums configuration; multiple names for the same thing must be avoided. |

Plus two standing operating rules:

- **Utilities must not be silently skipped.** When the same operation recurs, build the utility that
  enforces it consistently, rather than re-implementing it ad hoc each time.
- **Validation must cover three things, and none may fail silently:** **completeness** (what's
  expected vs what's present) · **consistency** (DB integrity, gaps) · **quality** (is the data
  accurate, is the value reasonable in its context).

### 0.1 Where the built app already satisfies this, and where it doesn't

| principle | built state | verdict |
|---|---|---|
| a (parameter-driven) | **[BUILT]** — `New-Word.ps1`/`Set-Candidates.ps1`/`Build-Passages.ps1` read their step sequence from `cfg_step`, not the script; handlers read every rule (filters, `may_source`, status transitions) from `cfg_*` (GOVERNANCE.md §3, measured: 1,041 config reads in one `new-word` run) | **largely satisfied** for the 3 built work packages |
| b (5-column config shape) | **[BUILT, partial]** — `cfg_setting` has 3 columns (`key`, `value`, `use`), not the 5 named here; `use` conflates description + rationale, and there is **no explicit "where it applies" / "conditions for applying" column anywhere in the live schema**. `cfg_candidate_rule` is closer (`kind`, `value`) but still only 2 columns. | **gap** — carried to §11 |
| c (configuration_maintenance utility, change-tracked, exclusive write path) | **[BUILT, partial]** — `cfgload.py`/`cfg.py` exist and are the only read/write path used by the app; `cfg_change_log` exists but **only logs config *reloads* (version, seed hash, timestamp), not individual row-level changes**; nothing in the schema **prevents** a direct `UPDATE cfg_setting …` outside the utility — there is no enforcement, only convention. | **gap** — carried to §11 |
| d, e (every module/routine governed; own config) | **[BUILT]** for the 3 existing work packages (each has its own `cfg_step`/`cfg_setting`/`cfg_on_fail`/`cfg_write_grant` rows); **[DESIGNED, not built]** for every operation named in §7.2 | on track |
| f (6 months of rules, explicit) | **[DESIGNED, not built]** — the collation exists (snippet 1 Appendix C, snippet 5's coverage audit: ~114 items, 43 homed in the *designed* `iba/config/*.json`) — but almost none of it is in the **live**, *running* `cfg_*` store. **Ruling (2026-07-21): adoption is not blanket.** Each item is evaluated for actual relevance/impact to the app as built, not imported because it was once written down — a rule from the collation only earns a `cfg_*` row when it still matters to the app's actual operation. See §3 for the disposition of the JSON collation itself. | **gap** — carried to §3, §11 |
| g (non-module governance) | **[DESIGNED, not built]** — `wide/governance.json` (GR-*/FLAG-*/interaction protocols) is named in the designed layout but marked `pending` (snippet 5 §4) | **gap** |
| h (utilities governed too) | **[BUILT, partial]** — `cfg_connection`/`cfg_api` govern the STEP utility; no config governs file-management, git-ops, or a morphology-parser utility because **those utilities don't exist yet** (§4) | **gap** |
| i (per-module rule sextet) | evaluated module-by-module in §7 | mixed |
| j (one rule, one home) | **[DESIGNED]** — already ruled in snippet 5 §2.3, independently, before this session's restatement; consistent, not a new decision | **confirmed, aligned** |
| k (naming via enums) | **[BUILT, partial]** — `cfg_enum` exists (7 groups today: `candidate_decision`, `candidate_source`, `escalation_type`, `on_fail`, `passage_rule`, `passage_source`, `run_state`, `word_status`); no naming-collision check runs against it yet | **gap** |

---

## 1. Overview — the operator's view

**[BUILT]** Today the operator runs one of four PowerShell entry points directly — there is **no
unified verb dispatcher** yet (the designed `run <module|pipeline> --scope …` / `status` / `config
show|set` surface of snippet 1 §3.3.1 does not exist):

| script | does | maps to |
|---|---|---|
| `Start-Iba.ps1 [-Reload] [-Reset]` | session bootstrap: checks Python + `requests`, loads/validates config into the DB (idempotent), builds data tables if missing, STEP pre-flight, prints READY | `iba.app.init` |
| `New-Word.ps1 -Word <w> -Source <s> [-Fresh]` | runs the `new-word` work package | registry → STEP raw pull → write → validate |
| `Set-Candidates.ps1` | runs `set-candidates` | seed refresh + span-candidate stamping |
| `Build-Passages.ps1` | runs `build-passages` | recomputes a book's passages |

Each script loads its step sequence from `cfg_step` (not from the script body) and dispatches through
`iba/app/run.py`, which branches on each step's exit code (`0` ok · `2` paused · `3` stop) and resolves
failures via `cfg_on_fail`. **PowerShell holds no process logic** — confirmed in `BUILD.md`/
`GOVERNANCE.md`, and this matches rule **a**.

**[DESIGNED, not built]** The consistent "slash-command" verb set (`run`/`status`/`resume`/`stop`/
`validate`/`config …`/`debug`/`report`) is still four separate scripts, one per work package, with no
common front door. This is a concrete Step-2 gap, not a design disagreement.

**Requirement (researcher, 2026-07-21):** `BUILD.md` must carry a maintained **list of the run commands
and their use** — kept current whenever a new command/work-package is added. Today it documents only
`New-Word.ps1`'s invocation (§2 of `BUILD.md`); the table above is the missing piece for
`Start-Iba.ps1`/`Set-Candidates.ps1`/`Build-Passages.ps1` and should be folded into `BUILD.md` itself,
not left only in this design document, so the command list stays where the operator actually looks.

---

## 2. Architecture — the layered stack, as realised

```text
Operator ──▶ 4 PS scripts (Start-Iba / New-Word / Set-Candidates / Build-Passages)   [BUILT — no unified verb set yet]
                     │
                     ▼
             run.py — the dispatcher / run-state machine                              [BUILT]
             reads cfg_step (sequence) + cfg_on_fail (failure path) ── reads ──▶ cfg_* in iba.db  [BUILT]
                     │ invokes, per step
                     ▼
             handlers/  registry.py · raw.py · candidate.py · passage.py               [BUILT]
                     │ use
                     ▼
             lib/  db.py (schema-from-config) · stepapi.py (the 3 STEP calls)          [BUILT]
             lib/  cfgload.py (seed→DB) · cfg.py (the runtime reader)                  [BUILT]
                     ▼
             iba/app/db/iba.db  (34 tables: study data + cfg_* + app control)          [BUILT]
```

The designed "reusable utilities" layer (git ops, file management/archiving, morphology parser,
authentication beyond `.env`-free STEP) **does not exist as code yet** — see §4.

---

## 3. The Configurator — three things that must be reconciled, not two

`GOVERNANCE.md` (2026-07-17) names this gap in its own words: *"reconciliation with the heavyweight
`iba/config` configurator — this app uses its own lightweight runtime config. Whether the two configs
converge is a later decision."* No later artifact resolves it. So this section states all three and
what each is, rather than picking one.

### 3.1 The built, running configurator — `iba/app/db/iba.db` `cfg_*`

**[BUILT]** 17 tables, seeded from flat JSON/CSV (`iba/app/config/*.csv`, exported from the DB, not the
other way round) via `cfgload.py`:

| table | rows today | holds |
|---|---:|---|
| `cfg_table` / `cfg_column` / `cfg_unique` | 17 / 127 / — | the schema itself — every table/column declared, with `use` |
| `cfg_enum` | 26 (7 groups) | controlled vocabularies |
| `cfg_connection` / `cfg_api` | — | STEP connection + the 3 routes + `may_source` |
| `cfg_work_package` / `cfg_step` | 3 / 10 | the 3 built runs and their steps |
| `cfg_setting` | 24 | scalars (thresholds, patterns, STEP bounds) |
| `cfg_on_fail` | 10 | per-step failure → path |
| `cfg_status_flow` | 5 | the `word` status flow only |
| `cfg_write_grant` | 26 | `writer → table` (the enforced `may_source`) |
| `cfg_candidate_rule` | 289 (all `kind='accept'`) | the seed accept-list (domain ruleset pattern) |
| `cfg_book_order`, `cfg_meta`, `cfg_change_log` | — | plumbing (canonical OSIS order; version+seed-hash audit) |

**Proven working, not decorative** (GOVERNANCE.md §4): `may_source` violations are hard errors; a
`cfg_on_fail` row changed in the DB changes behaviour with no code touched.

### 3.2 The designed, elaborate configurator — `iba/config/*.json`

**[DESIGNED, not loadable]** The full rule-anatomy model: Tier A (IBA-wide: `enums`/`pipeline`/
`patterns`/`governance`/`settings`/`db-governance`/`principles`/`filing`/`git`/`reconciliations`),
Tier A-utilities, Tier B (7 per-process files: `registry · fetch · raw · verses-passages · lexical ·
characteristics · findings`), the A.10 rule envelope (`statement · form · authority · reference ·
composition · location · intent · satisfaction · validation`), one-rule-one-home, enums-are-definitional.
Coverage as of 2026-07-15: ~114 inventory items, 43 authored, ~66 gap-with-a-named-home, 5 gap-with-no-home
(the study's products/end-point layer — §9). **Confirmed by snippet 3 §7 independently: "the
`config/*.json` seed is not yet loadable."**

### 3.3 The reconciliation — RESOLVED (researcher ruling, 2026-07-21)

**Option (i) is adopted: promote the built, lightweight `cfg_*` store. Do not build a loader for
`iba/config/*.json`.** The researcher's own verdict on the JSON collation: *"highly suspicious… this
was an attempt to gather the configurations from the old system. It was only partially successful,
created a lot of noise, and created rules that was no longer needed and badly worded."* Directly
confirming §0.1(b)/(c): the JSON rule-anatomy structure was "over the top, complex, difficult to
understand, and impossible to maintain"; the current DB configs are "much lighter," and the flat
per-table shape already lets a specific config table grow its own extra columns where that helps define
or maintain its scope (the `cfg_candidate_rule` pattern — a domain ruleset gets its own table rather than
forcing one universal shape).

**The JSON collation's remaining use is as an audit reference, not a design input:** run one completeness
pass — inspect it to confirm no still-relevant rule has been missed — reviewing every item's content
against the actual build for continued relevance (per §0.1(f)'s ruling), **then archive `iba/config/*.json`
entirely** ("to stop the bleeding on this noise"). That audit pass has not been run yet — it is Step-2
work, listed in §11, not done as a side-effect of this document.

### 3.4 What principle (b)'s column shape implies for the built store

`cfg_setting` has 3 columns (`key`/`value`/`use`) today; the researcher's principle b names five
(name/value/where-it-applies/conditions-for-applying/description) plus optional grouping/dependency
columns. **[OPEN, deliberately not resolved here]** — per the researcher's instruction, the exact
column set is not to be invented now: build should proceed under this uncertainty, and the specific
missing columns (a "where it applies" / "conditions for applying" equivalent) are flagged for
clarification once testing and real data scenarios surface what's actually needed — not fixed by me in
advance. Carried to §11.

---

## 4. Utilities

Per rule **h**, utilities are governed by config exactly like modules. Status against the designed set
(snippet 1 §3.3.3; snippet 5 §2.1a candidate list: `config-maintenance · run · discovery · db · step ·
morphology · validation · api · git · filing · auth`):

| utility | status | evidence |
|---|---|---|
| DB access layer | **[BUILT]** | `lib/db.py` — schema built from `cfg_column`; `write()` rejects undeclared columns; `upsert()` keys from `cfg_unique` |
| Configurator read/write (`config-maintenance`) | **[BUILT, partial — see §0.1/§3]** | `lib/cfgload.py` (seed→DB, self-validates, versions) + `lib/cfg.py` (the sole runtime reader) exist; **row-level change tracking and write-restriction (rule c) are not built** |
| STEP client | **[BUILT]** | `lib/stepapi.py` — governed by `cfg_connection`/`cfg_api`, pre-flighted by known-answer probes (`step.probe_strong`, `step.expect_min_verses`, `step.expect_gloss_contains`) |
| Run/orchestrator | **[BUILT]** | `run.py` — the dispatcher/state machine, resumable (`run.state`/`resume_point`), exercised by the zero-strongs pause path |
| Validation engine | **[BUILT, partial]** | `handlers/raw.py:validate` + `validation_result` (15,334 rows recorded) — but only the parse-check (`span` vs `strong_verse`) is proven; the full battery (readiness/content-validity/drift/acceptance-sample, §8) does not exist |
| Escalation (the researcher-pause) | **[BUILT, partial]** | `escalation` table + `run.state` pause/resume exist and are used (`raw.discover`'s zero-strongs path); `registry.create`'s approval seam is **stubbed to auto-approve** (BUILD.md D4) |
| Morphology parser | **[NOT BUILT]** | no `stem`/morphology-derivation code in `iba/app/lib/`; V3 §"Grounding facts" already flags "no dedicated stem-master table exists" |
| Git operations | **[NOT BUILT]** | no git-utility module in `iba/app/` |
| File management (archive/version/manifest) | **[NOT BUILT]** | no equivalent of the legacy `scripts/build_file_manifest.py` inside `iba/app/` |
| Claude API adapter | **[NOT BUILT]** | no interpretive `[I]` module exists yet — consistent with §7.2: the interpretive layer hasn't started |
| Auth/secrets | **[BUILT, minimal]** | confirmed **not needed today** — `Start-Iba.ps1`'s own docstring: "The app needs NO `.env` and NO secrets: STEP is the local server… with no key." Will be needed the moment the Claude API adapter is built. |

**Per the standing "utilities must not be silently ignored" rule:** three operations are already
repeated per-module without a shared utility and should be extracted before more modules are added —
(1) the STEP-call retry/cap/forward-walk logic (currently inside `raw.py`, will be needed again by any
future STEP-calling module), (2) the config self-validation pattern (`cfgload.py` does this once; any
second config source, §3.3(ii), would need the same checks), (3) the pre/post validation-gate envelope
(`pre-validate → run → post-validate → checkpoint`, currently informal in `run.py`, needed identically
by every future module per rule d).

---

## 5. The DB / schema

### 5.1 Role of the DB and the four-layer model

**[BUILT, partial]** The live `iba.db` (34 tables) realises **Raw** (`strong`/`verse`/`word_strong`/
`strong_*`), **Base** (`span`/`span_candidate`/`candidate_seed`/`lemma_inventory`/`passage`/
`verse_passage`), and **Control** (`run`/`escalation`/`validation_result`/`cfg_*`). **Interpretation**
and **Prose** layers do not exist yet — zero rows, zero tables (§5.4, §9).

### 5.2 Migration disposition — settled by evidence, not by choice

**[BUILT fact, not a decision to make]** The DB is genuinely fresh — built directly from STEP
(`BUILD.md` §1/§3), never from the legacy `database/bible_research.db`. No table anywhere carries a
`src_old_id`/`src_old_ref` column. The migration procedure designed in snippet 1 §3.4.1 (raw/registry
import, cross-DB back-links) **was never run and nothing supersedes that plan** — it is simply not
what happened. **[OPEN — registered in §11]** whether the old registry's 6 months of term curation
should still be imported. The researcher's D5 comment (§5.8) describes populating the new tables from
the old DB as a step that happens once the app baseline is built — relevant context, but it does not
by itself settle the raw/registry migration question.

### 5.3 Current live schema (exact, 2026-07-21)

34 tables; row counts where non-trivial:

| table | rows | note |
|---|---:|---|
| `word_registry` | 178 | the registry, entry point |
| `strong` | 3,463 | identity, one per Strong's |
| `verse` | 29,037 | unique verses touched so far |
| `span` | 534,075 | one row per code |
| `candidate_seed` | 2,086 | the lemma-level seed |
| `span_candidate` | 87,922 | the over-inclusive stamp |
| `passage` | 18,571 | **avg 1.56 verses/passage** — the fragmentation the plan's §5 movement-segment critique names |
| `verse_passage` | 24,847 | ~85.6% of verses (24,847/29,037) are currently passage-assigned; ~4,190 verses have none yet |
| `run` | 687 | control records |
| `escalation` | 178 | one per word (matches the stubbed-auto-approve path, §4) |
| `validation_result` | 15,334 | parse-check results recorded |

No `role` column on `span`; no per-occurrence dimension-value table (`ve_lexical` equivalent) anywhere;
no `stem` table.

### 5.4 Missing tables — named per the latest ruling (D3), identity gap resolved via a prose architecture

Per precedence (§1 of the precedence doc): **`operation` + `finding` + `meaning`** are the canonical
names (2026-07-20 D3, latest), not `ib_entry`/`ib_relation`/`ib_neighbour` (2026-07-15, superseded).
V3's own "not yet built" list (`Concordance, VE_lexical, Char_Operations, Char_meaning`) names the same
set in shorthand.

**Resolution (researcher, 2026-07-21):** `meaning` is a **new, prose-shaped table** — it holds the
narration of a characteristic in the context of the verse. The old DB's `prose_section` family is the
approximate equivalent, and its architecture is designed for exactly this (large-scale narrative text,
a proven revision trail, a controlled-vocabulary type). **Per the guardrail (§0), only the proven core
transitions — the abandoned link/citation tables (0 rows, piloted-and-dropped) do not.**

**Proposed shape** (a proposal, for confirmation — grounded in the old schema, not invented from
nothing):

| table | columns (drawn from `prose_section`'s proven core) | omitted from the old design, and why |
|---|---|---|
| `prose_type` | `id · code (unique) · label · description · created_at · deleted` | old had 108 codes, "grown by accretion… over half belong to 'programme' rather than any analytical stage." Seed with **one row** — `meaning_in_context` — and add codes only as a real need appears |
| `prose` (generic infrastructure, per the researcher's instruction to build the infrastructure, not just one table) | `id · prose_type_id (FK) · body TEXT NOT NULL · status (draft/in_review/approved/archived — the old CHECK, proven) · version · supersedes_id / superseded_by_id (self-FK, the proven revision chain — never overwrite) · author (claude_ai/claude_code/researcher — the old CHECK) · created_at · approved_at · approved_by · deleted` | omit `heading`, `metadata_json`, `source_file`, `word_count` unless/until a real need appears (§0 guardrail) |
| `meaning` | = `prose` rows where `prose_type.code = 'meaning_in_context'` (a view or a thin table with `prose_id` — cheaper to decide once the identity key below is fixed) | — |

**The many-verses-to-one-meaning index (the researcher's explicit rule — no duplicates):** a join table,
e.g. `verse_meaning(verse_id, char_key, prose_id, is_primary)`. **This closes the identity gap without a
separate entry table**: rather than inventing a new surrogate "characteristic entity" row, the natural
key is `char_key` (a text key, the same pattern `candidate_seed.lemma_key` already uses) paired with the
verse — many `(verse_id, char_key)` rows may point at the **same** `prose_id`, because many verses can
carry exactly the same meaning-in-context. **The researcher's ruling explicitly extends this same
many-to-one indexing rule to `operation`** — an `operation` row (the verbalised motion) is also
deduplicated the same way via a `verse_operation(verse_id, char_key, operation_id)` join, rather than
writing a duplicate `operation` row per verse that says the same thing.

**Still open** (§11): whether `char_key`'s exact normalisation (base-lemma + gloss, as sketched in the
earlier concordance plan) is sufficient as the join key, or whether a stronger identity mechanism is
still needed once real near-duplicates are seen in practice.

### 5.5 The operation-type catalogue — #7/8/9 RESOLVED (researcher, 2026-07-21)

The 9-type set, as drafted 2026-07-20:

| # | operation_type | draws from ve_nr | direction |
|---|---|---|---|
| 1 | performs | 106 (+107) | char → |
| 2 | arises-from | 103 source | driver → char |
| 3 | directed-at | 107 target (+116) | char → object |
| 4 | produces | 111 effect | char → state |
| 5 | seated-in | 104 seat | seat → char |
| 6 | borne-by | 105 bearer | person → char |
| 7 | has-status | 102 (type=status) | — |
| 8 | interacts-with | char↔char relation | char ↔ char |
| 9 | co-exists-with | 112 coupling | char ↔ co-term |

Composition rule (unchanged): predicate = ve_nr 106; subject/driver = 103 or 105; object/locus = 107(+116)
or 104; result = 111; qualifiers (109/110/108/118/117) fold into the sentence, never spawn their own row;
every argument carries a `body_type` tag (ib/other-being/physical, mechanics elaborated in §5.8).

**Resolution — all three (7/8/9) are real and distinct**, and the determining evidence for each is now
given: **has-status** applies when the verse context uses the characteristic as a **declaration of the
state/status of the inner being**; **interacts-with** applies when two characteristics have a **cause
and effect** on each other; **co-exists-with** applies when characteristics are grouped or mentioned in
the same context **with no evidence of impact** on each other. These are not three simultaneous facets
of one operation — a given operation instance is one, or a mixture across different characteristic-pairs
in the same verse, never all three for the same pair at once.

### 5.6 The study-unit model (snippet 2 researcher comments + snippet 4 §4, both 2026-07-20, no later revision)

Entry-point derivation (ready to become rows — `cfg_study_unit_rule`):

| request_kind | genre | yields | route |
|---|---|---|---|
| book | poetic, short | 1 unit = whole poem | `unit:poem-whole` |
| book | poetic, long | many units, logical divisions | `unit:poem-divide` |
| book | narrative | 1 unit per narrative | `unit:narrative-split` |
| book | prose/chapter | 1 unit per chapter section | `unit:chapter-section` |
| chapter | any | split into sections | `unit:chapter-section` |
| verse | any | the verse's assigned unit, else genre→book+genre rule | `unit:verse-resolve` |
| characteristic | any | pull verses + report; researcher selects | `unit:char-extract` |

Only genuinely open piece named in the source: the short/long poem boundary and the section-size
detector are `cfg_setting` scalars fixed empirically on John (unchanged since 2026-07-20).

### 5.7 Completeness model (snippet 4 §5, fully decided, no later revision)

A verse/characteristic is **done** when all three axes are complete (or the verse is `not-relevant`):
**concordance** (all its verses in the concordance) · **lexical** (has a lexical decomposition) ·
**meaning** (signed-off, or cross-referenced to a signed-off meaning). Enums: `verse_state`
(not-started/in-progress/not-relevant/complete), `completion_axis` (concordance/lexical/meaning),
`axis_state` (in-progress/complete), `meaning_status` (draft/signed-off/cross-referenced).

### 5.8 D2, D4, D5 — elaborated / deferred-by-design / clarified (researcher, 2026-07-21)

**D2 — `body_type` mechanics (elaborated, proposal for confirmation, not yet decided elsewhere).**
`body_type` is **not a static property of a span or lemma** — the same lemma ("hand", "God") can be a
different `body_type` depending on the argument role it fills in a *specific* operation (e.g. "God" as
the agent of `arises-from` is `other-being`; the same word as mere background reference may not enter
an operation argument at all). So it cannot live as a fixed column on `span`. **Proposal:** it is a
property of **the argument slot within an `operation` row**, matching the fixed predicate-slot shape
already used there (source/target/seat/bearer/effect as named columns, §5.4/operation-ruleset §2) —
i.e. `source_body_type`, `target_body_type`, `seat_body_type`, `bearer_body_type` as sibling columns to
`source_span_id`/`target_span_id`/etc., each drawing from the `cfg_enum(body_type)` = {ib, other-being,
physical-body} already decided (D2's principle, snippet 4 §6a). This keeps the fixed-column shape
consistent with the rest of `operation` and avoids a child table unless a future operation type needs a
variable number of tagged arguments (e.g. several co-terms under `co-exists-with`) — if that need
appears, a child `operation_argument` table is the fallback, not a redesign. Mechanical assistance (not
a substitute for the interpretive read, per infer-don't-extract): ve_nr 116 (locus=external) plus the
object-type of the referenced entity can **pre-fill a likely `body_type`** for the model to confirm, the
same way the mechanical floor grounds every other interpretive read.

**D4 — register vs cluster (deferred by design, not stuck).** The registry is "a very rough allocation
of Strong to each register word" and a poor categoriser of the Strong list into characteristic
groupings — which is why clusters were invented (grouping like-minded Strong terms). But clusters
aren't confirmed to work for the concordance either, and visualising the concordance will need **some**
grouping (else it's unreadable) — what that grouping should be isn't yet known. **Ruling: wait.** Build
the concordance without a required organising grouping first; decide the grouping once the concordance
has real content to group, rather than picking one now on no evidence (this is deliberately staged, not
an unresolved unknown).

**D5 — clarified with process context, structural question still open.** The researcher's process:
once the app baseline is built, existing tables populate from the old DB, and the study then proceeds
book by book, **re-evaluating and reconciling results carried over from prior studies into new findings
as each book is worked** — i.e. reconciliation is a natural per-book activity against migrated legacy
data, not a separate global sweep. This clarifies *when and against what* reconciliation happens, but
does **not** by itself settle the original structural question (own work package vs steps inside
`analyse-characteristic`) — that mechanical choice is still deferred to when baseline population begins,
per the researcher's original instruction.

### 5.9 What remains genuinely open in the schema (short)

- **`char_key` normalisation** (§5.4) — sufficiency of the join key once real near-duplicates are seen.
- **Old registry migration** (§5.2) — whether to import the old DB's 6 months of registry curation.
- **D5's mechanical question** — own work package vs steps (process context now given, §5.8; structural
  choice still open).
- **Config 5-column shape** (§3.4) — deliberately not fixed yet.

---

## 6. User Interaction

**[BUILT]** Today: 4 parameterised PS scripts (§1), no verb dispatcher, no `config show/set/diff`
surface (config is edited via CSV/JSON seed + `-Reload`, not a live command).

**[DESIGNED, not built]** The researcher-operations set (snippet 2 "Researcher operations", unchanged
since 2026-07-20):
- **Bulk:** `new-word` **[BUILT]** · `set-characteristic`/`set-candidates` **[BUILT]** ·
  `initialise-concordances` **[NOT BUILT — no longer blocked on the identity gap, §5.4 resolved it;
  still depends on D4's deferred concordance grouping only where a report needs to group, §5.8]**.
- **Specific:** add/remove seed · add/remove candidate characteristic · reassign a Strong to another
  registry · start new study unit · interactively work a study unit · start new char focus · get
  reports — **all [NOT BUILT]**.

**"Interactive feedback" — RESOLVED as a mapping onto the already-built `escalation` mechanism, not a
new concept.** The researcher asked what methods exist, within the app, for a feedback loop — a message
to the researcher, a prompt for a decision, process input — **noting the app does not use chat as part
of the application.** It already has exactly this, built and proven: the `escalation` table
(`run_id · word · at_step · type · question · preset · tried · state · answer · answered_at · raised_at`)
paired with `run.state`/`resume_point` — a step raises a question, the run pauses (`pause-continue`),
the researcher answers outside chat (via the DB/report surface), and the run resumes at its checkpoint.
**[BUILT, proven]** for `raw.discover`'s zero-strongs path; **[BUILT, stubbed]** for `registry.create`'s
approval seam (auto-approved today, per BUILD.md D4, §4). Every future "interactive feedback" need
(screen-inclusion uncertainty, a reconciliation the LLM can't resolve alone, a rule-refinement alert per
D6) routes through this same `escalation` surface — it does not need a new mechanism, only new
`(step, condition)` rows in `cfg_on_fail` pointing at `pause-continue`.

- **Reports:** the concordance (with exclude-verse-refs / exclude-related-words options) · study-unit
  status · char status · register status · book status · validations & errors — **all [NOT BUILT]**,
  though `validation_result` (15,334 rows) already holds the data a "validations & errors" report would
  read.

---

## 7. Operation Modules

### 7.1 Old 9-segment names vs what's actually built — reconciled by evidence

| # | old segment name (snippet 1) | maps to | status |
|---|---|---|---|
| 1 | Get data from STEP | `new-word`'s `raw.discover/detail/verses/write/validate` | **[BUILT]** |
| 2 | Characteristic-seed maintenance | `set-candidates`'s `candidate.seed` | **[BUILT]** |
| 3 | Prepare reading passage | `build-passages`'s `passage.build` | **[BUILT]**, but fragmented (§5.3: 1.56 verses/passage avg) — the exact gap the plan's movement-segment critique (§5 of the earlier v2 plan) named |
| 4 | Stem-master maintenance | — | **[NOT BUILT]** — no stem table, no code |
| 5 | Prepare lexical | — | **[NOT BUILT]** — no `ve_lexical`, no interpretive code |
| 6 | Characteristic maintenance | `set-candidates`'s `candidate.set` (span-stamping only) | **[BUILT, partial]** — stamps candidacy; does **not** derive/maintain a characteristic entity or role (no `role` column exists) |
| 7 | Data validation | `raw.validate` + `validation_result` | **[BUILT, partial]** — the parse-check only; no readiness/content-validity/drift/acceptance-sample battery |
| 8 | Prepare data for analysis | — | **[NOT BUILT]** |
| 9 | Characteristic findings | — | **[NOT BUILT]** |

**Reconciliation of the "two models" (item 3 from the precedence doc):** the 7 Tier-B *process* files
(`registry · fetch · raw · verses-passages · lexical · characteristics · findings`, snippet 5) are the
**rule-governance grouping**; the *operations* named in §7.2 below (`prepare-for-read`,
`analyse-characteristic`, …) are the **invoked runs**, each drawing rules from one or more processes.
Neither axis conflicts with the 9-segment names above — the segments are simply the oldest layer of
naming for the same underlying work, mostly still unbuilt past segment 3/6/7.

### 7.2 New process-loop operations — none built yet, spec unchanged since 2026-07-20

| operation | input unit | output | status |
|---|---|---|---|
| `prepare-for-read` | study-unit request (§5.6) | study-unit text + candidate-char list (incl. existing analysis) | **[NOT BUILT]** |
| `analyse-characteristic` | char(s)-in-study-unit | span role updated; lexicals; `operation` rows; `meaning`; concordance revalidated | **[NOT BUILT]** — internally: screen-inclusion → analyse-operation → record → reconcile → refine-rule (each per snippet 2 §A) |
| `consolidate` / `reconcile` / `refine-rule` | — | — | **[NOT BUILT]; D5 open (§5.8) on whether these are separate work packages** |
| `seed-update` | seed add/withdraw | auto re-runs `set-candidates` | **[NOT BUILT]**, though the underlying `candidate.seed` step it would call already exists |
| researcher-specific ops | — | — | **[NOT BUILT]** (§6) |
| `report` | — | the report set (§6) | **[NOT BUILT]** |

### 7.3 Rule (i) applied — the per-module sextet, for every module that exists

Per rule i, each **built** module's six rule-categories, read directly from the live config (not
invented):

**`new-word`**
- *Create/update/delete:* `registry.create` writes `word_registry` (status proposed→approved);
  `raw.write` commits; no delete path (soft-delete convention only, per project-wide governance, not
  yet an explicit `cfg_status_flow` row for word deletion).
- *Data rules:* `registry.strip_ends_pattern` (word-entry normalisation); `discovery.follow_related=false`
  (relatedNos excluded — root-family noise); `discovery.particle_pattern` (grammar particles excluded
  from discovery, flagged on span); `meaning.head_marker` (sense-vs-own-lemma split).
- *Relationship rules:* `cfg_write_grant` — 6 handlers, 12 distinct table grants (e.g. only
  `call3_strong` may write `span`/`strong_verse`/`verse`).
- *Output rules:* `report.span_fields`, `report.strong_fields`, `report.sample_verses`,
  `report.show_validation`, `report.show_verse_text` — all config, not hard-coded in `report.py`.
- *Validity rules:* `raw.validate`'s parse-check (`span` must recover `strong_verse`, per Strong's);
  `step.expect_min_verses`/`step.expect_gloss_contains`/`step.probe_strong` (STEP pre-flight,
  known-answer).
- *Quality rules:* the forward-walk completeness check (STEP's reported total must equal stored count —
  the bug BUILD.md §5 found and fixed was exactly this check catching a real 39-verse under-return).

**`set-candidates`**
- *Create/update/delete:* `candidate.seed` refreshes `candidate_seed` over `lemma_inventory`;
  `candidate.set` stamps `span_candidate` (existence = candidate; no separate reject row is written —
  a real gap against principle i's "deletion" clause, since a span that stops being a candidate has no
  recorded transition).
- *Data rules:* `candidate.lemma_base_pattern` (strip Strong's sub-letters to the lemma key — the
  seed/stamp key).
- *Relationship rules:* `candidate_seed.registry_match` — the double-control (a candidate with no
  registry match = a registry gap, per the live `cfg_table` description).
- *Output rules:* none dedicated (feeds `passage.build` and, eventually, reports).
- *Validity rules:* `cfg_on_fail(candidate.seed, no-inventory)` — refuses to run against an empty
  `lemma_inventory`.
- *Quality rules:* none beyond existence — **this is a real gap**: 289/289 `cfg_candidate_rule` rows
  are `kind='accept'`; there is no `reject` kind despite the column implying one, so a deliberate
  exclusion has no explicit record (matches the identity-gap-adjacent concern already raised in the
  precedence doc).

**`build-passages`**
- *Create/update/delete:* `passage.build` recomputes a book's passages wholesale each run (no
  incremental update; a rebuild replaces, per the handler's `does` text).
- *Data rules:* `passage.default_rule='char-continuity'`, `passage.min_shared_strongs=1`,
  `passage.cross_chapter=false`.
- *Relationship rules:* `verse_passage` — a verse belongs to at most one passage (schema-enforced,
  `UNIQUE(verse_id)`).
- *Output rules:* `vw_passages_by_book` view (exists per the config dir listing).
- *Validity rules:* `cfg_on_fail(passage.build, no-candidates)`.
- *Quality rules:* `passage.review_over=10` — flags `needs_review` on any passage longer than 10 verses;
  **no quality rule catches the opposite failure** (the single-verse fragmentation at 1.56 avg
  verses/passage, §5.3) — this is the exact gap the plan's movement-segment critique names, and it is
  visible in the live numbers, not just in the design documents.

For the **not-yet-built** modules (§7.2), the per-module sextet cannot be filled from evidence — it is
specified in the source snippets (screen-inclusion rules, reconciliation confirm/extend/adjust/contradict
triggers, etc.) but has no built counterpart to check against. Those specifications carry forward
unchanged into Step 3; restating them again here would duplicate snippet 2/3/4 rather than add anything
(rule j).

---

## 8. Validation and errors

**[DESIGNED vs BUILT, per the standing three-fold rule: completeness · consistency · quality]**

| axis | designed (snippet 1 §3.7.1) | built |
|---|---|---|
| **Completeness** | per-layer ingest/regeneration/read-validity/derivation controls | **[BUILT, narrow]** — STEP-count parity (the forward-walk check) and the span/strong_verse parse-check only |
| **Consistency** | FK integrity, the integrity invariants (I1–I13) | **[BUILT, narrow]** — `UNIQUE` constraints (`span(verse_id,position)`, `verse_passage(verse_id)`, etc.) enforce structural consistency; the I1–I13 invariant *set* from the old programme is not encoded anywhere in `iba.db` |
| **Quality** | dimension rules, content-validity V1/V2/V3, drift, acceptance-sample | **[NOT BUILT]** — no interpretive layer exists yet to validate |

**Process controls** (run log, replayable patches, backtrack, rerun): `run` (687 rows) and `escalation`
(178 rows) give run-level tracking and pause/resume; **[NOT BUILT]**: replayable-patch writes (writes
today are direct commits, not patch records) and a formal backtrack/rerun-by-provenance mechanism.

Per the standing rule ("validation errors or omissions must not be silently ignored"): the two silent
gaps found in this review — no `reject`-kind candidate rows (§7.3), no fragmentation-quality check on
passages (§7.3) — should be treated as validation debt, not stylistic notes.

---

## 9. Outputs & Products (Layer 4)

**[Confirmed, documented deferral — not designed here.]** Snippet 5's own coverage audit found this is
the one part of the inventory with **no home anywhere**: three orders of output, the three audiences,
milestones M1–M3, the science-lens policy, the standing-question catalogue. The plan's own build order
(framework → modules → prove sustainable → *then* re-run the study) places this rightly last. Recorded
here so it stays a recorded debt, not a silence (per snippet 5's own recommendation: a
`process/prose.json` marked `INACTIVE` when the designed configurator is built out).

---

## 10. Governance, patterns, settings

**[DESIGNED, not built]** `wide/governance.json` (GR-*/FLAG-*/interaction protocols) and
`wide/patterns.json` (file-naming/label/versioning/patch-type rules) are both named in the designed
layout and both `pending` — unauthored in either configurator. **[BUILT, informal]** the *app's own*
build record (BUILD.md/GOVERNANCE.md) already follows several of these conventions in practice (dated
status headers, decision logs, "decisions I made without asking" sections) without them being encoded
as config anywhere.

---

## 11. Open decisions register (consolidated, revised 2026-07-21 — kept short, per instruction)

Six of the original eight items were resolved by the researcher's 2026-07-21 comments (§0, §3.3, §5.4,
§5.5, §5.8, §6) and are removed from this list — resolution is recorded at the section cited, not
repeated here. **Only items no artifact still answers:**

1. **`char_key` normalisation** (§5.4) — whether base-lemma + gloss is a sufficient join key for the
   `verse_meaning`/`verse_operation` dedup index, or whether a stronger identity mechanism is needed
   once real near-duplicates are seen in practice.
2. **Old registry migration** (§5.2) — whether the old DB's 6 months of registry curation should still
   be imported, beyond the fresh-build-from-STEP path already taken.
3. **D5's mechanical question** (§5.8) — reconcile/consolidate/refine-rule as their own work packages or
   as steps inside `analyse-characteristic`. Process context is now given (populate from the old DB,
   then reconcile per book as the study proceeds) but the structural choice itself is still deferred by
   the researcher, on purpose.
4. **Config 5-column shape** (§3.4) — deliberately not fixed now; flagged for clarification once testing
   and real data scenarios show what's actually needed.
5. **D4's eventual grouping** (§5.8) — register, cluster, or something else, once the concordance has
   content to group — deliberately deferred, not stuck.

**Resolved this session, for the record (not open):** the two-configurator convergence (§3.3 — built
`cfg_*` wins, JSON collation to be audited then archived); the identity gap (§5.4 — a prose-shaped
`meaning`/`prose` architecture + a many-to-one `char_key` join, not a new entry table); D2 mechanics
(§5.8 — `body_type` as sibling columns on `operation`'s argument slots, elaborated as a proposal); D4's
principle (§5.8 — wait for content before choosing a grouping); operation-type #7/8/9 (§5.5 — all three
real, with the declaration/cause-effect/no-impact test); "interactive feedback" (§6 — it's the existing
`escalation` mechanism, not a new concept).

---

## 12. Compliance checklist

One line per section above; mark against the live app at each Step-3 review:

| § | item | current status |
|---|---|---|
| 0 | Configuration principles a–k satisfied | partial — b, c, f, g, h, k have gaps (§0.1); adoption of old rules is impact-evaluated, not blanket (f) |
| 1 | Unified verb-set interface | not built; BUILD.md's command list needs maintaining as commands are added (§1) |
| 2 | Layered stack realised | built, utilities layer thin |
| 3 | Configurator reconciled | **resolved 2026-07-21** — built `cfg_*` is the one store; JSON collation audit-then-archive still to run |
| 4 | All designed utilities built | 5 of 11 built or partially built |
| 5 | Schema: 4 layers present | Raw/Base/Control built; Interpretation/Prose absent |
| 5 | Identity-gap resolved | **resolved 2026-07-21** — prose architecture + many-to-one join, proposal stage, not yet built |
| 6 | Verb-set + reports built | not built; "interactive feedback" resolved onto `escalation` (§6) |
| 7 | 9 old segments / new operations built | 3 of 9 segments built (1,2,3 partial, 6,7 partial); 0 of 7 new operations built |
| 8 | 3-fold validation (completeness/consistency/quality) | completeness/consistency narrow; quality layer absent |
| 9 | Products layer | deliberately deferred, recorded |
| 10 | Governance/patterns config | not authored in either store |
| 11 | Open decisions | 5 items, listed, none silently dropped |
