# IBA Application Design (v2) — two-phase blueprint: Data Layer, then Analytic Layer

> **Status: draft, for approval.** Prepared 2026-07-21, same day as v1. **Restructures v1
> (`iba-application-design-v1-20260721.md`) along a phase axis — it does not re-litigate or re-resolve
> anything v1 settled.** Every claim below carries the same **[BUILT]** / **[DESIGNED]** / **[OPEN]** tag
> it had in v1; nothing is re-derived or invented. The only new content is the phase assignment itself
> (§0.2) and the Phase-1 exit / Phase-2 entry gate (§13), both organisational, not analytical.
>
> **Why split (researcher instruction, 2026-07-21):** v1's open register (§11) is five items. Re-reading
> it against what each item actually needs to be resolved: three of the five (`char_key` normalisation,
> D5's structural question, D4's grouping) cannot be settled by more design thinking — they need **real,
> populated analytic content** (actual meanings, actual operations, actual near-duplicates) to test
> against, and that content doesn't exist because the analytic layer hasn't been built on top of a
> data layer that isn't itself finished and clean yet. The researcher's ruling: **stop trying to resolve
> analytic-phase questions in the abstract; finish and clean the data layer first, then let the analytic
> layer's own real data resolve them.** This document draws that line explicitly, so the two phases can
> be designed, built, and signed off separately, with a defined gate between them.
>
> **Binding note (carried from v1, unchanged).** Claude Code has no permission to work on this study
> outside the scope of the IBA app, and must use the app's own approved methods for every DB change —
> including changes to the configurator itself (rule **c**, §0.1). Nothing in this document authorises
> an ad-hoc DB write.
>
> **Guardrail (carried from v1, unchanged).** A construct is only in this design once it is confirmed
> needed — a proven-but-abandoned old-DB table is evidence *against* copying it, not a template to
> replicate by default. Every unresolved point is registered in an open list (§8 for data-layer items,
> §12 for analytic-layer items), not merely noted as "unclear" in passing.

---

## 0. Governing configuration principles (unchanged — the north star for both phases)

Restated in full from v1 §0 — these apply identically to Phase 1 and Phase 2; the split below is a
build-sequencing decision, not a governance carve-out.

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

Plus two standing operating rules: **utilities must not be silently skipped**, and **validation must
cover completeness · consistency · quality**, none silently failing.

### 0.1 Where the built app already satisfies this, and where it doesn't (unchanged from v1 §0.1)

| principle | built state | verdict | phase |
|---|---|---|---|
| a (parameter-driven) | **[BUILT]** — the 3 built work packages read every rule from `cfg_*`, not code (1,041 config reads/run measured) | largely satisfied | Phase 1 (extends to Phase 2 modules as built) |
| b (5-column config shape) | **[BUILT, partial]** — `cfg_setting` has 3 columns, not 5; no "where it applies"/"conditions" column anywhere | **gap** — §8 | Phase 1 |
| c (config-maintenance utility, change-tracked, exclusive write path) | **[BUILT, partial]** — `cfgload.py`/`cfg.py` are the only read/write path used; `cfg_change_log` logs reloads only, not row-level changes; nothing **enforces** the exclusive path | **gap** — §8 | Phase 1 |
| d, e (every module/routine governed; own config) | **[BUILT]** for the 3 built work packages; **[DESIGNED, not built]** for every analytic-layer operation | on track | both |
| f (6 months of rules, explicit; adoption impact-evaluated, not blanket) | **[DESIGNED, not built]** — collation exists (~114 items, 43 authored in `iba/config/*.json`), almost none in the live `cfg_*` store; each item earns a row only if it still matters | **gap** — §8 (audit pass) | Phase 1 |
| g (non-module governance) | **[DESIGNED, not built]** — `wide/governance.json` pending | **gap** | Phase 1 |
| h (utilities governed too) | **[BUILT, partial]** — STEP utility governed; file-management/git-ops/morphology utilities don't exist yet | **gap** | Phase 1 |
| i (per-module rule sextet) | evaluated module-by-module, §5 / §11 | mixed | both |
| j (one rule, one home) | **[DESIGNED]**, confirmed, aligned | confirmed | both |
| k (naming via enums) | **[BUILT, partial]** — `cfg_enum` exists (7 groups); no naming-collision check runs | **gap** | Phase 1 |

### 0.2 The phase split, stated as one rule

**Phase 1 = Data Layer.** Everything needed to get the concordance's raw, base, and control substrate
built, populated, internally consistent, and validated for **completeness** and **consistency** — with
no dependency on interpretive judgement. Maps to v1's **Raw / Base / Control** schema layers (§5.1), the
3 built work packages (`new-word`, `set-candidates`, `build-passages`), the configurator, and the
utilities that serve ingestion/build/validation.

**Phase 2 = Analytic Layer.** Everything that reads meaning into the data: the **Interpretation** and
**Prose** schema layers, `analyse-characteristic` and its internals, the operation-type semantics,
meaning narration, reconciliation, the concordance's organising grouping, quality validation (which by
definition requires interpretation to judge), and outputs/products.

**The line, concretely (old 9-segment map from v1 §7.1):**

| # | old segment | phase |
|---|---|---|
| 1 | Get data from STEP | **Phase 1** — [BUILT] |
| 2 | Characteristic-seed maintenance | **Phase 1** — [BUILT] |
| 3 | Prepare reading passage | **Phase 1** — [BUILT, fragmented — gap, §8] |
| 4 | Stem-master maintenance | **Phase 1** — [NOT BUILT] (mechanical, no interpretation) |
| 6 | Characteristic maintenance (span-stamping) | **Phase 1** — [BUILT, partial] (candidacy stamping is mechanical; role *derivation* is Phase 2) |
| 7 | Data validation | **Phase 1** for completeness/consistency; **Phase 2** for quality/content-validity |
| 5 | Prepare lexical | **Phase 2** — [NOT BUILT] (interpretive) |
| 8 | Prepare data for analysis | **Phase 2** — [NOT BUILT] |
| 9 | Characteristic findings | **Phase 2** — [NOT BUILT] |

Nothing here reassigns a status — it only sorts the existing v1 rows onto a timeline.

---

# PART A — PHASE 1: DATA LAYER

**Scope:** build, populate, and validate the concordance substrate — raw STEP data, span/candidate
data, passages, the configurator, and the core utilities — to a state that is **complete** (what's
expected is present) and **consistent** (no integrity gaps), with quality validation and interpretation
explicitly out of scope. Phase 1 does **not** include: `operation`/`meaning`/`prose` content, the
`analyse-characteristic` operation, reconciliation, or the concordance's organising grouping (D4).

## A1. Overview — the operator's view (carried from v1 §1, unchanged)

**[BUILT]** Today the operator runs one of four PowerShell entry points directly — there is **no
unified verb dispatcher** yet:

| script | does | maps to |
|---|---|---|
| `Start-Iba.ps1 [-Reload] [-Reset]` | session bootstrap: checks Python + `requests`, loads/validates config into the DB (idempotent), builds data tables if missing, STEP pre-flight, prints READY | `iba.app.init` |
| `New-Word.ps1 -Word <w> -Source <s> [-Fresh]` | runs the `new-word` work package | registry → STEP raw pull → write → validate |
| `Set-Candidates.ps1` | runs `set-candidates` | seed refresh + span-candidate stamping |
| `Build-Passages.ps1` | runs `build-passages` | recomputes a book's passages |

Each script loads its step sequence from `cfg_step` (not the script body) and dispatches through
`iba/app/run.py`, branching on exit codes (`0` ok · `2` paused · `3` stop), resolving failures via
`cfg_on_fail`. **PowerShell holds no process logic** (rule a).

**[DESIGNED, not built]** The unified verb set (`run`/`status`/`resume`/`stop`/`validate`/`config …`/
`debug`/`report`) is still four separate scripts. Concrete Phase-1 build item, not a design disagreement.

**Requirement (researcher, 2026-07-21, still standing):** `BUILD.md` must carry a maintained list of run
commands and their use, kept current as commands are added.

## A2. Architecture — the layered stack, as realised (carried from v1 §2, unchanged)

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

The Phase-2 utilities layer (Claude API adapter) sits **above** this stack, reading from it — it is
scoped in Part B, not here.

## A3. The Configurator (carried from v1 §3, unchanged — this is entirely Phase-1 machinery)

`GOVERNANCE.md` (2026-07-17) names the reconciliation gap in its own words. **Resolved 2026-07-21**,
carried forward unchanged:

### A3.1 The built, running configurator — `iba/app/db/iba.db` `cfg_*`

**[BUILT]** 17 tables, seeded from flat JSON/CSV via `cfgload.py`:

| table | rows today | holds |
|---|---:|---|
| `cfg_table` / `cfg_column` / `cfg_unique` | 17 / 127 / — | the schema itself |
| `cfg_enum` | 26 (7 groups) | controlled vocabularies |
| `cfg_connection` / `cfg_api` | — | STEP connection + routes + `may_source` |
| `cfg_work_package` / `cfg_step` | 3 / 10 | the 3 built runs and their steps |
| `cfg_setting` | 24 | scalars |
| `cfg_on_fail` | 10 | per-step failure → path |
| `cfg_status_flow` | 5 | the `word` status flow only |
| `cfg_write_grant` | 26 | `writer → table` (enforced `may_source`) |
| `cfg_candidate_rule` | 289 (all `kind='accept'`) | the seed accept-list |
| `cfg_book_order`, `cfg_meta`, `cfg_change_log` | — | plumbing |

**Proven working, not decorative:** `may_source` violations are hard errors; a `cfg_on_fail` row change
changes behaviour with no code touched.

### A3.2 The designed, elaborate configurator — `iba/config/*.json`

**[DESIGNED, not loadable]** Full rule-anatomy model, Tier A/A-utilities/B, ~114 inventory items (43
authored). **Confirmed not yet loadable.**

### A3.3 The reconciliation — RESOLVED (researcher ruling, 2026-07-21)

**Option (i) adopted: promote the built, lightweight `cfg_*` store. Do not build a loader for
`iba/config/*.json`.** The JSON collation's remaining use is a one-time **audit reference** — confirm no
still-relevant rule has been missed, then **archive `iba/config/*.json`**. **That audit pass is a Phase-1
build item** (§8, item 2) — it must complete before Phase 1 is declared clean, since it is exactly the
kind of "is this rule still relevant" check that belongs to consolidating the data-layer's own rule set.

### A3.4 What principle (b)'s column shape implies for the built store

`cfg_setting` has 3 columns; principle b names five. **[RESOLVES BY BUILD — not a standing decision]**
— **researcher, 2026-07-21: this resolves itself as each individual configuration is built**, not as a
prior schema ruling. No column set is fixed in advance; each `cfg_*` table takes on whatever
"where it applies"/"conditions for applying" shape its own rules actually need as it's authored — the
same pattern already proven by `cfg_candidate_rule` growing its own extra columns beyond the generic
`key`/`value`/`use` shape. Not tracked as a Phase-1 open item any more (§8, item 1) — there is nothing to
decide ahead of the build, only something to observe as it happens.

## A4. Utilities — the Phase-1 subset

Per rule h, utilities are governed by config exactly like modules. **Data-layer utilities only** — the
Claude API adapter is Phase 2 (§B3).

| utility | status | evidence | phase-1 relevance |
|---|---|---|---|
| DB access layer | **[BUILT]** | `lib/db.py` — schema built from `cfg_column`; rejects undeclared columns | core |
| Configurator read/write | **[BUILT, partial]** | `cfgload.py` + `cfg.py`; row-level change tracking (rule c) **not built** | core — gap, §8 |
| STEP client | **[BUILT]** | `lib/stepapi.py`, pre-flighted by known-answer probes | core |
| Run/orchestrator | **[BUILT]** | `run.py` — resumable state machine | core |
| Validation engine | **[BUILT, partial]** | parse-check only (15,334 rows); readiness/consistency battery incomplete | core — gap, §A7/§8 |
| Escalation | **[BUILT, partial]** | `escalation` + `run.state` pause/resume; `registry.create`'s approval stubbed to auto-approve | core |
| Morphology parser | **[NOT BUILT]** | no `stem`/morphology-derivation code | build item, §8 — mechanical, not interpretive, so Phase 1 |
| Git operations | **[NOT BUILT]** | no git-utility module | build item, §8 |
| File management (archive/version/manifest) | **[NOT BUILT]** | no in-app equivalent of the legacy manifest script | build item, §8 |
| Auth/secrets | **[BUILT, minimal]** | not needed today; will be needed once the Phase-2 Claude API adapter is built | Phase 1 now, re-triggered at Phase 2 entry |

**Standing extraction debt** (rule: utilities must not be silently skipped) — three repeated-but-unshared
operations, all data-layer: (1) the STEP-call retry/cap/forward-walk logic, currently inside `raw.py`;
(2) the config self-validation pattern, currently only in `cfgload.py`; (3) the pre/post
validation-gate envelope, currently informal in `run.py`. All three should be pulled into shared
utilities **within Phase 1**, before more data-layer modules are added.

## A5. The DB / schema — Raw, Base, Control (Phase-1 layers only)

### A5.1 Role of the DB and the layer model (from v1 §5.1)

**[BUILT, partial]** The live `iba.db` (34 tables) realises **Raw** (`strong`/`verse`/`word_strong`/
`strong_*`), **Base** (`span`/`span_candidate`/`candidate_seed`/`lemma_inventory`/`passage`/
`verse_passage`), and **Control** (`run`/`escalation`/`validation_result`/`cfg_*`) — **these three layers
are the entire Phase-1 schema scope.** **Interpretation** and **Prose** (zero rows, zero tables) are
Phase 2 — see §B1.

### A5.2 Migration disposition — settled by evidence

**[BUILT fact]** The DB is genuinely fresh — built directly from STEP, never from the legacy
`database/bible_research.db`. No `src_old_id`/`src_old_ref` column anywhere; the old migration procedure
was never run. **[OPEN — Phase-1 item, §8 item 3]** whether the old registry's 6 months of term
curation should still be imported. This is a data-layer question (it's about `word_registry`/raw-term
provenance, not about interpretive content) and does **not** depend on the analytic layer — it can be
resolved and closed within Phase 1.

### A5.3 Current live schema (exact, 2026-07-21) — the Phase-1 substrate today

| table | rows | note |
|---|---:|---|
| `word_registry` | 178 | the registry, entry point |
| `strong` | 3,463 | identity, one per Strong's |
| `verse` | 29,037 | unique verses touched so far |
| `span` | 534,075 | one row per code |
| `candidate_seed` | 2,086 | the lemma-level seed |
| `span_candidate` | 87,922 | the over-inclusive stamp |
| `passage` | 18,571 | **avg 1.56 verses/passage** — fragmentation gap, §8 item 4 |
| `verse_passage` | 24,847 | ~85.6% of verses passage-assigned; ~4,190 verses still unassigned |
| `run` | 687 | control records |
| `escalation` | 178 | one per word (matches stubbed-auto-approve path) |
| `validation_result` | 15,334 | parse-check results recorded |

No `role` column on `span` (role *derivation* is a Phase-2 concern — it requires the interpretive read to
decide whether a candidate span is a characteristic, standalone, or qualifier); no per-occurrence
dimension-value table; no `stem` table.

### A5.4 The study-unit model — infrastructure only (from v1 §5.6)

The entry-point derivation table (request_kind → yields → route) is **infrastructure** — it defines how
a study-unit *request* resolves to a *unit of text*, with no interpretation of content. **Phase 1.**
Only genuinely open piece: the short/long poem boundary and section-size detector are `cfg_setting`
scalars, fixed empirically on John — unchanged since 2026-07-20, no new decision needed.

### A5.5 Completeness model — infrastructure, content-agnostic (from v1 §5.7)

The three-axis done/not-done model (concordance · lexical · meaning) and its enums are **structural
definitions** — they say what "done" means without requiring the content itself to exist yet. **Phase
1** builds and seeds these enums; **actually reaching** `axis_state = complete` on the `lexical` and
`meaning` axes is inherently Phase-2 work (it requires the Interpretation/Prose content to exist).

## A6. User Interaction — Phase-1 operations only

**[BUILT]** 4 parameterised PS scripts (§A1), no verb dispatcher, no `config show/set/diff` surface.

**[DESIGNED, not built] — Phase-1 bulk/specific ops** (from v1 §6, filtered to non-interpretive ops):

- **Bulk:** `new-word` **[BUILT]** · `set-characteristic`/`set-candidates` **[BUILT]** ·
  `initialise-concordances` **[NOT BUILT]** — this is **Phase 1**: it builds the empty concordance
  *structure* (the join tables and indexes), not its interpretive content; it no longer depends on the
  identity gap (resolved, §B1) but its eventual **display grouping** is D4, a Phase-2 item (§12 item 3).
- **Specific (data-layer):** add/remove seed · add/remove candidate characteristic · reassign a Strong to
  another registry · start new study unit — **all [NOT BUILT]**, all mechanical/administrative, all
  Phase 1.
- **Specific (analytic — moved to Part B):** interactively work a study unit · start new char focus —
  these require the interpretive read and belong to Phase 2 (§B4).

**"Interactive feedback" — RESOLVED, applies to both phases.** Maps onto the built `escalation`
mechanism (`escalation` table + `run.state` pause/resume), proven for `raw.discover`'s zero-strongs path
(Phase 1) and stubbed for `registry.create`'s approval seam. Every future interactive-feedback need in
**either** phase routes through this same surface — no new mechanism, only new `(step, condition)` rows
in `cfg_on_fail`.

- **Reports (data-layer):** register status · book status · validations & errors — **[NOT BUILT]**,
  though `validation_result` (15,334 rows) already holds the data a "validations & errors" report would
  read. Study-unit status and char status reports straddle both phases and are listed again in §B4.

## A7. Validation and errors — completeness + consistency only

Per the standing three-fold rule, **Phase 1 owns completeness and consistency; quality is Phase 2**
(quality validation is inherently interpretive — "is the value reasonable in its context" requires the
context to have been interpreted).

| axis | designed | built | phase |
|---|---|---|---|
| **Completeness** | per-layer ingest/regeneration/read-validity/derivation controls | **[BUILT, narrow]** — STEP-count parity (forward-walk check) + span/strong_verse parse-check | **Phase 1** |
| **Consistency** | FK integrity, integrity invariants (I1–I13) | **[BUILT, narrow]** — `UNIQUE` constraints enforce structural consistency; the I1–I13 invariant set is not encoded anywhere in `iba.db` | **Phase 1** |
| **Quality** | dimension rules, content-validity V1/V2/V3, drift, acceptance-sample | **[NOT BUILT]** — no interpretive layer exists to validate | **Phase 2** — §B5 |

**Process controls:** `run` (687 rows) and `escalation` (178 rows) give run-level tracking and
pause/resume — **[BUILT]**, Phase 1. **[NOT BUILT]**, Phase 1 build items: replayable-patch writes
(writes today are direct commits) and a formal backtrack/rerun-by-provenance mechanism.

Two silent gaps found in v1's review are **Phase-1 validation debt**, not stylistic notes: no
`reject`-kind candidate rows (§A3.1/§8 item 5); no fragmentation-quality check on passages (§8 item 4).

## A8. Phase-1 open items and build debt (the items that must close before Phase 2 starts)

These are the items from v1's registers that are **genuinely Phase-1-scoped** — they do not need
analytic content to resolve. **Triaged by the researcher, 2026-07-21: none is a standing open
decision any more — every item is either resolved, or resolves by doing the build, or is a scoped
build todo.**

**Resolved:**

- **3. Old registry migration** (§A5.2) — **RESOLVED (researcher, 2026-07-21): no further imports from
  the old registry are required.** The fresh-build-from-STEP path stands as final; §A5.2's "genuinely
  fresh, no `src_old_id`" fact is not revisited. Closed, not carried to §13's gate.

**Resolves by doing the build (not a decision to make ahead of time):**

- **1. Config 5-column shape** (§A3.4) — **RESOLVED-BY-BUILD (researcher, 2026-07-21): this resolves
  itself as each individual configuration is built**, not as a prior schema ruling. No fixed shape is
  chosen in advance; each `cfg_*` table takes on whatever "where it applies"/"conditions" columns its
  own rules actually need as it's authored (the `cfg_candidate_rule` pattern already does this). Not a
  gate condition — there is nothing to decide ahead of the four build todos below.

**Build todos (scoped work, not open decisions):**

- **2. JSON-collation audit-then-archive** (§A3.3) — run the one completeness pass against
  `iba/config/*.json`, confirm no still-relevant rule is missed, then archive it. Action item.
- **4. Passage fragmentation** (§A5.3/§A7) — **directed (researcher, 2026-07-21): the passage table
  will be rebuilt, and all the config rules governing passage-building need refinement as part of that
  rebuild** — `passage.default_rule` (`char-continuity`), `passage.min_shared_strongs`,
  `passage.cross_chapter`, `passage.review_over`, and any other `cfg_setting`/`cfg_candidate_rule`
  feeding `passage.build`. Not an accept-vs-fix decision any more — a scoped rebuild task, with the
  1.56-verses/passage figure (§A5.3) as the defect the refined rules must resolve.
- **5. Candidate `reject`-kind gap** (§A3.1) — **a config fix.** Add a `reject` kind to
  `cfg_candidate_rule` (or equivalent) so a deliberate exclusion is recorded as a row, not left as a
  silent absence — closes principle i's deletion clause for this module.
- **6. Configurator row-level change tracking** (§A4/§0.1c) — **a compliance/config rule fix.** Extend
  `cfg_change_log` (or add a sibling table) to log individual `cfg_*` row writes, and route all writes
  exclusively through `configuration_maintenance` per rule c — closes rule c's *enforcement* gap, not
  just its logging gap.

**Net effect:** Phase 1's punch list has **zero standing open decisions** — two resolved items (1, 3,
neither carried to §13's gate) and four build todos (2, 4, 5, 6). §13's gate is judged purely against
the four todos being done.

---

# PART B — PHASE 2: ANALYTIC LAYER

**Entry condition:** Part A's open items (§8) are closed or explicitly deferred with reason, and §13's
gate criteria are met. **Scope:** everything that reads meaning into the data — the Interpretation and
Prose schema layers, the `analyse-characteristic` operation and its internals, meaning narration,
operation typing, reconciliation, the concordance's organising grouping, quality validation, and
outputs/products. **Nothing in Part B is built yet** — all items below are [DESIGNED] or [OPEN], carried
from v1 unchanged.

## B1. Schema — Interpretation and Prose layers

### B1.1 Missing tables — identity gap resolved via a prose architecture (from v1 §5.4)

Per precedence: **`operation` + `finding` + `meaning`** are the canonical names (2026-07-20 D3), not the
2026-07-15 `ib_entry`/`ib_relation`/`ib_neighbour` naming.

**Resolution (researcher, 2026-07-21):** `meaning` is a **new, prose-shaped table** — narration of a
characteristic in the context of the verse, modelled on the old DB's `prose_section` family's proven
core, explicitly **omitting** the abandoned link/citation tables.

**Proposed shape** (for confirmation, grounded in the old schema):

| table | columns | omitted, and why |
|---|---|---|
| `prose_type` | `id · code (unique) · label · description · created_at · deleted` | old had 108 codes, over half programme-not-analytical; seed with **one row** (`meaning_in_context`), add codes only as real need appears |
| `prose` | `id · prose_type_id (FK) · body TEXT NOT NULL · status (draft/in_review/approved/archived) · version · supersedes_id/superseded_by_id (self-FK revision chain) · author (claude_ai/claude_code/researcher) · created_at · approved_at · approved_by · deleted` | omit `heading`, `metadata_json`, `source_file`, `word_count` unless a real need appears |
| `meaning` | `prose` rows where `prose_type.code = 'meaning_in_context'` (view or thin table — cheaper to decide once `char_key` is fixed) | — |

**The many-verses-to-one-meaning index:** `verse_meaning(verse_id, char_key, prose_id, is_primary)` —
many `(verse_id, char_key)` rows may point at the same `prose_id`. **Extended identically to
`operation`:** `verse_operation(verse_id, char_key, operation_id)`.

**Still open** (§12 item 1): `char_key`'s exact normalisation (base-lemma + gloss) — sufficiency as a
join key once real near-duplicates are seen. **This is the item that cannot be resolved without real
Phase-2 content**, which is exactly why it waits here rather than in Part A.

### B1.2 The operation-type catalogue — #7/8/9 RESOLVED (from v1 §5.5)

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

Composition rule unchanged: predicate = ve_nr 106; subject/driver = 103 or 105; object/locus = 107(+116)
or 104; result = 111; qualifiers fold into the sentence, never spawn their own row; every argument
carries a `body_type` tag (§B1.3).

**Resolution — all three (7/8/9) real and distinct:** **has-status** = the verse declares the state of
the inner being; **interacts-with** = cause-and-effect between characteristics; **co-exists-with** =
grouped/mentioned together with no evidence of impact. Not simultaneous facets — one operation instance
is one, or a mixture across different characteristic-pairs in the same verse.

### B1.3 D2, D4, D5 — elaborated / deferred-by-design / clarified (from v1 §5.8)

**D2 — `body_type` mechanics (elaborated proposal).** Not a static property of a span or lemma — the
same lemma's `body_type` is contextual to the argument role it fills in a specific operation. **Proposal:**
sibling columns on `operation`'s existing argument slots (`source_body_type`/`target_body_type`/
`seat_body_type`/`bearer_body_type`), each drawing from `cfg_enum(body_type)` = {ib, other-being,
physical-body}. Mechanical pre-fill assist: ve_nr 116 (locus=external) plus the referenced entity's
object-type can pre-fill a likely `body_type` for the model to confirm — not a substitute for the
interpretive read.

**D4 — register vs cluster (deferred by design).** Neither the registry nor clusters are confirmed as a
good organising grouping for the concordance. **Ruling: wait** — build the concordance without a
required grouping first (Phase 1's `initialise-concordances`, §A6); decide the grouping once the
concordance has real content, which only exists once Phase 2 has produced it. **This is why D4 cannot be
a Phase-1 item** — it is a Phase-2 decision that needs Phase-2 output to evaluate against. Carried at
§12 item 3.

**D5 — clarified with process context, structural question still open.** Once the app baseline is built
(Phase 1 complete) and existing tables populate from the old DB, the study proceeds book by book,
re-evaluating and reconciling carried-over prior-study results into new findings as each book is worked.
This clarifies *when and against what* reconciliation happens (a Phase-2-time activity), but not
*whether* `consolidate`/`reconcile`/`refine-rule` are their own work packages or steps inside
`analyse-characteristic` — deferred to when Phase 2 build begins. Carried at §12 item 2.

## B2. Utilities — Phase-2 addition

| utility | status | evidence |
|---|---|---|
| Claude API adapter | **[NOT BUILT]** | no interpretive `[I]` module exists yet — consistent with no analytic operation having started |
| Auth/secrets (re-triggered) | **[BUILT, minimal] → needed at Phase-2 entry** | not needed today (STEP needs no key); will be needed the moment the Claude API adapter is built |

## B3. Operation Modules — the analytic layer proper

### B3.1 Old segments 4/5/8/9, reconciled (from v1 §7.1)

| # | old segment name | maps to | status |
|---|---|---|---|
| 4 | Stem-master maintenance | — | **[NOT BUILT]** *(mechanical — actually a Phase-1 build item per §A4; listed here only for the old-segment map's completeness)* |
| 5 | Prepare lexical | — | **[NOT BUILT]** — genuinely Phase 2, interpretive |
| 8 | Prepare data for analysis | — | **[NOT BUILT]** — Phase 2 |
| 9 | Characteristic findings | — | **[NOT BUILT]** — Phase 2 |

### B3.2 New process-loop operations — none built yet, spec unchanged since 2026-07-20 (from v1 §7.2)

| operation | input unit | output | status |
|---|---|---|---|
| `prepare-for-read` | study-unit request | study-unit text + candidate-char list | **[NOT BUILT]** |
| `analyse-characteristic` | char(s)-in-study-unit | span role updated; lexicals; `operation` rows; `meaning`; concordance revalidated | **[NOT BUILT]** — internally: screen-inclusion → analyse-operation → record → reconcile → refine-rule |
| `consolidate` / `reconcile` / `refine-rule` | — | — | **[NOT BUILT]; D5 open (§12 item 2)** on separate work packages vs steps |
| `seed-update` | seed add/withdraw | auto re-runs `set-candidates` | **[NOT BUILT]**, though the underlying `candidate.seed` step (Phase 1) already exists |
| researcher-specific ops (interpretive) | — | — | **[NOT BUILT]** — §B4 |
| `report` (analytic) | — | the report set | **[NOT BUILT]** |

### B3.3 Rule (i) sextet — not yet fillable

For every not-yet-built Phase-2 module, the per-module rule sextet (create/update/delete · data ·
relationship · output · validity · quality) **cannot be filled from evidence** — it is specified in the
source snippets (screen-inclusion rules, reconciliation confirm/extend/adjust/contradict triggers) but
has no built counterpart. These specifications carry forward unchanged into Phase-2 build; restating
them again here would duplicate the source snippets (rule j).

## B4. User Interaction — analytic operations

**[DESIGNED, not built]** From v1 §6's "Specific" operator ops, the interpretive subset: interactively
work a study unit · start new char focus · get reports (concordance with exclude-verse-refs/
exclude-related-words options · study-unit status · char status).

Escalation resolution (§A6) applies identically here — no new mechanism needed for analytic-phase
feedback loops (screen-inclusion uncertainty, a reconciliation the LLM can't resolve alone, a
rule-refinement alert per D6): all route through `escalation` + new `cfg_on_fail` rows.

## B5. Validation — the quality axis

**[NOT BUILT]** — dimension rules, content-validity V1/V2/V3, drift, acceptance-sample. Cannot exist
before the Interpretation layer exists to validate. This is the one axis of the three-fold validation
rule that is **entirely** Phase-2 scope (completeness and consistency are Phase 1, §A7).

## B6. Outputs & Products (Layer 4)

**[Confirmed, documented deferral.]** The one part of the inventory with no home anywhere: three orders
of output, three audiences, milestones M1–M3, the science-lens policy, the standing-question catalogue.
Build order (framework → modules → prove sustainable → *then* re-run the study) places this rightly
last — after Phase 2's core analytic operations, not before. Recorded as debt, not silence.

## B7. Governance, patterns, settings

**[DESIGNED, not built]** `wide/governance.json` and `wide/patterns.json`, both `pending`. **[BUILT,
informal]** the app's own build record (BUILD.md/GOVERNANCE.md) already follows several of these
conventions without them being encoded as config. Cross-cutting, but the authoring work naturally lands
in Phase 2 alongside the rest of the governance/config completion, since it depends on the Phase-1
audit-then-archive (§8 item 2) settling what rules remain to be encoded.

## B8. Phase-2 open items (the items genuinely blocked on the data layer)

These are the three v1 open items that **cannot** be resolved by more design work — they need real,
populated Phase-2 content to test against, which is exactly the researcher's framing for why the split
was needed:

1. **`char_key` normalisation** (§B1.1) — whether base-lemma + gloss is a sufficient join key for the
   `verse_meaning`/`verse_operation` dedup index, or a stronger identity mechanism is needed. **Cannot
   be resolved until `meaning`/`operation` rows exist in volume** — near-duplicates have to be observed,
   not predicted.
2. **D5's mechanical question** (§B1.3) — reconcile/consolidate/refine-rule as their own work packages
   or steps inside `analyse-characteristic`. Process context is given; the structural choice is
   deliberately deferred to when Phase-2 build begins, since the right shape may depend on how
   `analyse-characteristic` actually behaves once running.
3. **D4's eventual grouping** (§B1.3) — register, cluster, or something else, once the concordance has
   content to group. Deliberately deferred, not stuck — needs the concordance's real Phase-2 output.

---

## 12. Open items index (cross-reference)

**Genuinely open (awaiting a decision) — Phase 1 has none; all three remaining are Phase 2:**

| # | item | phase | resolves when |
|---|---|---|---|
| 7 | `char_key` normalisation | Phase 2 (§B8.1) | real `meaning`/`operation` volume exists |
| 8 | D5 structural question | Phase 2 (§B8.2) | `analyse-characteristic` build begins |
| 9 | D4 grouping | Phase 2 (§B8.3) | concordance has real content |

**Build todos (directed, scoped work — not decisions):**

| # | item | phase | closes when |
|---|---|---|---|
| 2 | JSON-collation audit-then-archive | Phase 1 (§8.2) | audit pass run, `iba/config/*.json` archived |
| 4 | Passage table rebuild + config-rule refinement | Phase 1 (§8.4) | directed 2026-07-21: table rebuilt, `passage.*` rules refined |
| 5 | Candidate `reject`-kind gap | Phase 1 (§8.5) | config fix: `reject` kind added to `cfg_candidate_rule` |
| 6 | Configurator row-level change tracking | Phase 1 (§8.6) | compliance/config fix: row-level logging + enforced write path |

**Resolves by doing the build (not a gate condition):**

| # | item | phase | resolves as |
|---|---|---|---|
| 1 | Config 5-column shape | Phase 1 (§8.1) | each `cfg_*` table takes on the columns its own rules need, as it's authored — researcher ruling 2026-07-21, no prior schema decision required |

**Resolved, for the record (not open, either phase):** old registry migration (§A5.2/§8 — **no further
imports required**, researcher ruling 2026-07-21); two-configurator convergence (§A3.3); the identity
gap (§B1.1 — prose architecture + many-to-one join); D2 mechanics (§B1.3); operation-type #7/8/9
(§B1.2); "interactive feedback" (§A6/§B4 — the `escalation` mechanism, not a new concept).

---

## 13. Phase-1 exit / Phase-2 entry gate

**Proposal, for confirmation — not yet ruled on.** Phase 2 design work resumes once:

1. The four Phase-1 build todos (§8 items 2, 4, 5, 6) are done. (Items 1 and 3 — config 5-column shape
   and old registry migration — are not gate conditions: item 3 is already resolved, and item 1
   resolves organically as each configuration is built, not as a prior ruling to wait on.)
2. The JSON-collation audit-then-archive (§8.2) has run, so Phase-2 rule-authoring (§B7) starts from a
   single clean rule source, not two.
3. `validation_result` completeness/consistency coverage (§A7) is judged sufficient by the researcher —
   not necessarily the full I1–I13 invariant set, but a deliberate researcher sign-off rather than a
   default.
4. The passage table has been rebuilt and its config rules (`passage.default_rule`,
   `passage.min_shared_strongs`, `passage.cross_chapter`, `passage.review_over`, and any other rule
   feeding `passage.build`) refined per the researcher's direction (§8.4) — Phase 2's
   `analyse-characteristic` inherits the rebuilt, refined passage set, not the current 1.56-avg
   fragmented one.

**Not required for the gate** (deliberately excluded, per the researcher's own framing): resolving
`char_key`, D4, or D5 — these are Phase-2-internal open items that resolve *during* Phase 2, using
Phase-2's own output, not preconditions for starting it.

---

## 14. Compliance checklist — split by phase

**Phase 1**

| § | item | current status |
|---|---|---|
| A1 | Unified verb-set interface | not built; BUILD.md's command list needs maintaining |
| A2 | Layered stack (Raw/Base/Control) realised | built |
| A3 | Configurator reconciled | **resolved 2026-07-21**; JSON audit-then-archive still to run (§8.2) |
| A4 | Data-layer utilities built | 6 of 10 built or partially built |
| A5 | Schema: Raw/Base/Control present | built |
| A6 | Data-layer verb-set + reports | not built |
| A7 | Completeness + consistency validation | narrow but built |
| A8 | Phase-1 open items | 6 items, listed, none silently dropped |

**Phase 2**

| § | item | current status |
|---|---|---|
| B1 | Schema: Interpretation/Prose layers | designed (proposal stage), not built |
| B2 | Claude API adapter | not built |
| B3 | Analytic operations (old segments 5/8/9 + new process-loop ops) | 0 of 6 new operations built |
| B4 | Analytic-layer verb-set + reports | not built |
| B5 | Quality validation | not built (structurally cannot exist yet) |
| B6 | Outputs & Products | deliberately deferred, recorded |
| B7 | Governance/patterns config | not authored |
| B8 | Phase-2 open items | 3 items, each explicitly data-dependent |
