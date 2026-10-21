# IBA DB schema-change plan (v1) — from today's process/config work to concrete schema

> **Status: DESIGN FOR CONFIRMATION. No DB changes.** Directed 2026-07-20, prepared at the researcher's
> request to (a) restate the objectives the schema must serve and (b) turn the four documents written
> today into a single, concrete map of **what changes in `iba/app/db/iba.db`** — tagged by how settled
> each piece is. **D5** (whether `reconcile`/`consolidate`/`refine-rule` are their own work packages) is
> **intentionally left open** — the researcher will settle it once we analyse real data, not on paper.
>
> **Sources digested:** `iba-application-plan-v2-20260720.md` §13–§14 (the governing sections) ·
> `iba-process-loop-steps-to-flesh-out-v1-20260720.md` (agenda + researcher's own comments, which
> supersede the agenda where they differ) · `iba-operation-ruleset-v1-20260720.md` (the `operation`
> composition mechanism) · `iba-config-rules-for-process-loop-v1-20260720.md` (the `cfg_*` inventory,
> §6a decisions, §7 open blockers). Grounded against the **live** `iba/app/db/iba.db` (34 tables,
> queried directly 2026-07-20) — not the stale `Workflow/schema/*` snapshots, and not the `iba/config/`
> wide-seed (that JSON seed is drafted but **not yet loadable**; the runtime is the DB `cfg_*` tables).

---

## 1. Objectives this schema must serve (restated, to confirm understanding)

Five things the schema exists to make true. If any of these is misread, the tables below are wrong.

1. **The unit of identity is meaning-in-context, not a Strong's number and not a registry word.**
   `strong_meaning_tree` already proves Strong↔sense flows both ways (one Strong, many senses; many
   Strongs, one sense) — so no table may key "a characteristic" on `strong` or on `word_registry.word`.
   *(plan §2–§3; still an open naming question — see §3 below, this is the single biggest gap.)*
2. **The output is a spiderweb, not one table.** Evidence (span) → an inclusion decision (role) → three
   parallel readings (IB / other-being / physical-body, via a `body_type` tag, **not** three physical
   copies) → a lexical decomposition (`ve_nr` dimension values) → the operation-in-motion (`operation`) →
   the synthesised paragraph (`meaning`). Each is queryable on its own and cross-referenced, never
   duplicated. *(plan §13.1; config-rules D2.)*
3. **Locality over bulk.** The schema must let one study-unit's work be deepened in place — via
   revision trails, cross-references, and an explicit `escalation`-style alert — never a global
   re-sweep. A few operations are legitimately bulk (raw pulls, seed updates, initial concordance
   creation) and the schema should make that split explicit, not implicit. *(plan §13.2, §14.3.)*
4. **Completeness is measurable per verse, on three independent axes** (concordance / lexical /
   meaning), not a single flag. *(plan §14.2.)*
5. **Every rule is a config row, not code — and every operation on the DB, by the researcher or by
   Claude Code, goes through a defined app operation.** No ad-hoc SQL against `iba.db` outside a
   work-package step. *(plan §1.2, §13.5 — this binds the schema-design process itself: what follows
   is a plan, and Step 1 of the actual build still runs through `db --reset` / the config path, not a
   manual `ALTER TABLE`.)*

---

## 2. Current schema baseline (live, queried 2026-07-20)

`iba/app/db/iba.db` has **34 tables**. Only three groups exist; **nothing analytical/interpretive has
been built yet** — the whole of §14's "concordance" side is still on paper.

| Layer | Tables | Grain (from `cfg_table`) |
|---|---|---|
| **Raw** | `strong`, `strong_lexicon`, `strong_sense`, `strong_meaning_tree`, `strong_verse`, `verse`, `word_strong` | Strong's identity, lexicon text, sense head, sense tree, strong-in-verse assertion, the addressable verse, word→strong discovery |
| **Base** | `lemma_inventory`, `candidate_seed`, `span`, `span_candidate`, `passage`, `verse_passage` | corpus lemma substrate → seed decision → one row per verse-code (span) → candidate stamp → reading-frame passage → passage membership |
| **Registry** | `word_registry` | one row per English IB word, the study's entry point |
| **Control** | `run`, `escalation`, `validation_result`, plus `cfg_*` (17 tables) | run tracking, the one sanctioned researcher-interaction pause, check outcomes, the rulebook |

**Load-bearing facts for the plan below:**
- `span` has **no `role` column yet** — the char_role assignment (characteristic/qualifier/standalone/
  uncertain, ve_nr 115) is not stored anywhere today.
- **There is no per-occurrence dimension-value table at all** — no `ve_lexical` equivalent exists in
  `iba.db`. `strong_sense`/`strong_meaning_tree`/`strong_lexicon` are *lexicon reference*, not
  *interpretive reading of a specific span*. This is bigger than a missing row in the inventory — see §3.
- `passage`/`verse_passage` already give **one reading-frame per book with at-most-one-passage-per-verse**
  membership (`verse_passage.verse_id UNIQUE`) — structurally this is 90% of what `study_unit`/
  `verse_study_unit` need (§4.1).
- `word_registry` carries a `word_status` flow (proposed→approved→raw-complete→signed-off/rejected) —
  this is the **word**-grain workflow, not the **characteristic**-grain one §14.2 needs; they must not be
  conflated.
- `iba/config/wide/reconciliations.md` (a separate, not-yet-loadable seed) independently lists
  `recon.role-enum` = `[characteristic, qualifier, standalone, uncertain]` as **OPEN** — corroborates
  §14's `char_role` enum from an unrelated document, which is a useful cross-check.

---

## 3. The identity gap — the one thing that blocks almost everything else

Plan §6 proposed `ib_entry` keyed on `char_key` (base-lemma + normalised gloss) as the meaning-in-context
identity row. **D3 (config-rules §6a) renamed the *analytical output* tables to `operation` / `finding` /
`meaning`** — but it did **not** say what those tables key *on*. Today, nothing in `iba.db` represents
"a characteristic, at the grain of meaning-in-context":

- `word_registry` is **word**-grain (too coarse — one English word, many senses).
- `candidate_seed` / `span_candidate` are **lemma/span**-grain (the over-inclusive net, not a meaning).
- There is no row anywhere that says "*this* is the entity `study_unit_char`, `operation`, and `meaning`
  all point at."

**This must be settled before `study_unit_char`, `operation`, or `meaning` can be given real foreign
keys.** Two ways to resolve it, both consistent with everything decided so far:

- **(a) Revive a thin `ib_entry`-equivalent** (e.g. rename to `char_entry` to fit the D3 naming) — one
  row per meaning-in-context, `char_key` = normalised identity, minimal columns (definition, status),
  and `operation`/`meaning`/`study_unit_char` FK to it. This is the plan-§6 design, just renamed.
- **(b) No entry row — key everything on `(study_unit_id, char_key_text)`** directly, deferring identity
  consolidation entirely to the `finding` layer's neighbour/merge machinery (§7 of the plan). Cheaper to
  start, but pushes the Strong-flow problem (§1 of this doc) into every join.

**Recommendation:** (a) — a thin entry row costs little and gives `operation`/`meaning`/`study_unit_char`
a stable join key from day one; the consolidation machinery (match-on-write, merge, neighbour-link) still
runs exactly as designed in plan §7. **Flagged for confirmation in §6 below — this is the top blocker.**

---

## 4. Proposed additions, by `cfg_*` category

Every item tagged: **[DECIDED]** (researcher-settled, ready to draft as rows/DDL) · **[LEANING]** (a
clear direction in the documents, not yet explicitly ratified) · **[OPEN]** (a live blocker, listed
again in §6).

### 4.1 New / repurposed tables

| Table | Status | Proposal | Derives from |
|---|---|---|---|
| **`study_unit`** | **[LEANING]** repurpose `passage` | Add columns: `unit_type` (the `cfg_study_unit_rule` route — `poem-whole`/`poem-divide`/`narrative-split`/`chapter-section`/`verse-resolve`/`char-extract`), keep `book`/`anchor_verse_id`/`ref`/`verse_count`/`rule`/`source`/`needs_review` as-is. Researcher explicitly asked to repurpose, not duplicate, `passage` (plan §13.6.2). | plan §14.1, §13.6.2; config-rules §3.1, §4 |
| **`verse_study_unit`** | **[LEANING]** repurpose `verse_passage` | Rename only — grain (`verse_id` UNIQUE = at-most-one-unit-per-verse) already matches. | config-rules §3.1 (cites `verse_passage` as the pattern) |
| **`char_entry`** *(new name for plan's `ib_entry`, to fit D3)* | **[OPEN — see §3]** | `id`, `char_key` (normalised identity), `definition`, `status` (emerging/established/under-revision), `registry_word_id` (nullable FK → `word_registry`, the double-control), `created_at`/`deleted`. | plan §2, §6; this doc §3 |
| **`char_entry_revision`** | **[OPEN — depends on `char_entry`]** | the definition trail: `entry_id`, `definition`, `status`, `superseded_by`, `written_at`. | plan §2, §6 |
| **`study_unit_char`** | **[DECIDED, shape]** but **FK to characteristic is OPEN (§3)** | `id`, `study_unit_id` FK, `char_entry_id` FK (pending §3), `analytic_status` (untouched/in-progress/recorded/reconciled/closed), `assigned_at`/`updated_at`/`deleted`. | plan §14.1 table; process-loop-steps step 2 (`select-next` queue) |
| **`span.role`** *(column, not a table)* | **[DECIDED]** | add `role` TEXT to existing `span` — enum `char_role` (characteristic/qualifier/standalone/uncertain, ve_nr 115). Simplest home: the researcher names it "span - update role" directly (§14.6 step 9), not a new table. | plan §14.6 step 9; corroborated independently by `iba/config/wide/reconciliations.md` `recon.role-enum` |
| **`ve_lexical`** | **[OPEN — not inventoried anywhere, but load-bearing]** | **Does not exist in `iba.db` at all.** One row per (span/occurrence × ve_nr dimension), the per-occurrence decomposition the `operation` mechanism reads *from* (operation-ruleset §2: slots 103/104/105/106/107/108/109/110/111/116/117/118 must come from *somewhere*). Columns per the 2026-07-02 catalogue shape: `span_id`, `ve_nr`, `label`, `value`, `stated_or_inferred`, `from_span`/`to_span` (pairs), `notes`, `provenance`. | operation-ruleset §2 (assumes this exists); plan §6 `ve_lexical`; **this is a bigger gap than the config-rules inventory flagged** — see §5 |
| **`operation`** | **[DECIDED, core]** | `id`, `char_entry_id` FK (pending §3), `study_unit_id` FK, `operation_type` (enum, §4.2), `source_span_id`/`target_span_id`/`seat_span_id`/`effect_span_id` (nullable, per slot), `body_type` per argument (or a small `operation_argument` child table if one row can't hold n arguments cleanly — **flagged**), `verbalised_text`, `qualifiers` (intensity/specifier/manner/direction/device — likely a JSON or child rows), `stated_or_inferred`, `written_at`/`deleted`. | operation-ruleset §2–§3 in full |
| **`meaning`** | **[DECIDED, core]** | `id`, `char_entry_id` FK, `study_unit_id` FK (nullable if cross-referenced), `paragraph_text`, `status` (draft/signed-off/cross-referenced), `cross_ref_meaning_id` (self-FK, nullable), `written_at`/`deleted`. | plan §14.4; config-rules §5 (`meaning_status` enum) |
| **`concordance`** | **[DECIDED]** a **view**, not a table (D1) | `SELECT` over `char_entry` + `study_unit_char` + `span`/`verse` + `word_registry` (nullable) → columns **Gloss · Strong · transliteration · related words · verse references**, filterable by `body_type`. Options to exclude verse-refs / related-words are query parameters, not schema. | config-rules §6a D1; process-loop-steps researcher comments ("Concordance table... columns to include") |
| **`ib_relation`** (char↔char, in a unit) | **[OPEN — naming]** | plan §6 named this separately from `operation`'s types 8–9 (`interacts-with`, `co-exists-with`). operation-ruleset §3 folds char↔char into `operation` types 8/9 directly. **Recommend: drop `ib_relation` as a separate table — it is operation types 8–9.** Flagged for confirmation (§6). | plan §6 vs operation-ruleset §3 note ("types 1–7 are argument-structure... 8–9 are char-to-char... feed... the neighbour graph") |
| **`ib_neighbour`** (entry↔entry sense-adjacency) | **[OPEN — deferred]** | still needed for the Strong-flow problem (§1 objective 1) — entries that are close but not merged. Seeded from `strong_meaning_tree`. Not blocking Step 1; can follow once `char_entry` (§3) exists. | plan §3.3, §6 |

### 4.2 New `cfg_enum` values

| enum | values | status | source |
|---|---|---|---|
| `char_role` | characteristic · qualifier · standalone · uncertain | **[DECIDED]** | plan §14.1 (ve_nr 115); `reconciliations.md recon.role-enum` |
| `verse_state` | not-started(0) · in-progress(1) · not-relevant(2) · complete(3) | **[DECIDED]** | config-rules §5 |
| `completion_axis` | concordance(0) · lexical(1) · meaning(2) | **[DECIDED]** | config-rules §5 |
| `axis_state` | in-progress(0) · complete(1) | **[DECIDED]** | config-rules §5 |
| `meaning_status` | draft(0) · signed-off(1) · cross-referenced(2) | **[DECIDED]** | config-rules §5; plan §14.4 |
| `body_type` | ib · other-being · physical-body | **[DECIDED]** | plan §14.5; config-rules §6a D2 |
| `study_unit_route` | poem-whole · poem-divide · narrative-split · chapter-section · verse-resolve · char-extract | **[DECIDED]** | config-rules §4 (`cfg_study_unit_rule`, 7 rows already drafted) |
| `operation_type` | performs · arises-from · directed-at · produces · seated-in · borne-by · has-status · interacts-with · co-exists-with | **[LEANING — the set itself is operation-ruleset's open confirm question §8]** | operation-ruleset §3, full table below |

**The `operation_type` catalogue (operation-ruleset §3, carried in full — this is the table to
ratify/adjust):**

| # | operation_type | researcher's verb | draws from ve_nr | direction |
|---|---|---|---|---|
| 1 | performs | (the act) | 106 (+107) | char → |
| 2 | arises-from | comes-from / affected-by | 103 source | driver → char |
| 3 | directed-at | goes-to / affects | 107 target (+116) | char → object |
| 4 | produces | affects | 111 effect | char → state |
| 5 | seated-in | (has a seat) | 104 seat | seat → char |
| 6 | borne-by | (whose) | 105 bearer | person → char |
| 7 | has-status | has-a-status | 102 (type=status) | — |
| 8 | interacts-with | interacts | char↔char relation | char ↔ char |
| 9 | co-exists-with | co-exists | 112 coupling | char ↔ co-term |

Open per operation-ruleset §8: is `has-status` (7) real, and are `interacts`/`co-exists` (8–9) one type
or two? — carried into §6 below.

### 4.3 New `cfg_status_flow` entries

| entity | flow | status | source |
|---|---|---|---|
| `verse` | the three completion axes (concordance/lexical/meaning), independent | **[DECIDED]** | config-rules §5 |
| `study_unit_char` | analytic status (untouched→in-progress→recorded→reconciled→closed) | **[DECIDED, shape]**, exact states not yet drafted as rows | plan §14.1; process-loop-steps step 2 |
| `meaning` | draft → signed-off (or → cross-referenced) | **[DECIDED]** | plan §14.4 |
| `char_entry` | emerging → established → under-revision | **[LEANING]** — plan §2's definition status, not restated in §14; confirm it still stands post-D3 rename | plan §2 |

### 4.4 New `cfg_work_package` / `cfg_step`

| work package | runs over | steps (from §14.6) | status |
|---|---|---|---|
| `prepare-for-read` | study-unit request | resolve unit (§14.1 rule) → produce report (text + candidate list incl. existing analysis) → write `study_unit_char` + `verse_study_unit` → if already started, offer create-new/revise/select-next | **[DECIDED]** |
| `analyse-characteristic` | char-in-study-unit | select focus char(s) → deep-read → load existing (concordance/lexical/operations) → generate lexicals for **all** chars in the unit if none exist → screen-inclusion for interrelated chars → synergise operations → reconcile → generate meaning → record (span role, unit status, concordance-validate, lexicals, operations, meaning) → refine-rule if a gap surfaced | **[DECIDED]**, 10 steps as written in plan §14.6 |
| `seed-update` | seed (add/withdraw) | auto re-run `set-candidates` | **[DECIDED]** |
| `initialise-concordances` | corpus (one-off) | **[OPEN — blocked by the identity gap §3 and the span-split mechanics (D2 is decided in principle, not in column-level detail)]** | **[OPEN]** |
| researcher-specific | — | add/remove-candidate, reassign-strong-to-registry, add/remove-seed | **[DECIDED]** |
| `report` | — | concordance / study-unit status / char status / register status / book status / validations-errors | **[DECIDED]**, exact SQL per report not drafted |
| `reconcile` / `consolidate` / `refine-rule` | — | **whether these are their own work packages or steps inside `analyse-characteristic`** | **[D5 — explicitly deferred by the researcher; not to be decided on paper]** |

### 4.5 `cfg_write_grant` / `cfg_on_fail` / `cfg_setting`

Mechanical once §4.1–§4.4 are fixed (one grant per new handler→table; one on-fail per new step's likely
failure). Not drafted here — no new judgement calls, just enumeration once the tables above are final.
Settings needed: poem short/long boundary, chapter-section-size heuristic, completeness minimums —
all deferred to Step-2 empirical tuning on John per plan §11.

---

## 5. What this surfaces that wasn't explicit in the config-rules inventory

Re-reading everything today's four documents assumed against the **live** schema turns up one gap none
of them named directly: **`ve_lexical` (the per-occurrence dimension-value table) does not exist in
`iba.db` at all.** The operation-ruleset's entire composition mechanism (§2: "an operation is a
predication... each slot is drawn from a specific ve_nr dimension") presupposes those dimension values
are already sitting somewhere per span. They aren't. Building `operation` before `ve_lexical` exists
would have nothing to draw its slots from.

**Practical consequence for sequencing:** `ve_lexical` is not just one more row in the table inventory —
it is a **prerequisite** for `operation`, ahead of it in build order regardless of how the identity gap
(§3) or D1–D4 land. This changes the plan-§8 build sequence's Step 3 ("dimension catalogue in config")
into two things: the *config* (which dimensions, mandatory-per-genre) **and** the *table* to hold values
once read. Worth confirming this reading is right before Step 1 is cut.

---

## 6. Decisions to confirm before schema is cut

In rough dependency order — each blocks something below it:

1. **The identity gap (§3).** Revive a thin `char_entry` (recommended) or key everything on raw
   `(study_unit, char_key_text)` pairs with no entry row. Blocks `study_unit_char`, `operation`,
   `meaning`, the concordance view.
2. **`ve_lexical` must be built** as its own table before `operation` (§5) — confirm this is accepted as
   a corrected/added prerequisite, not an oversight to argue about.
3. **Repurpose `passage`/`verse_passage`** into `study_unit`/`verse_study_unit` (rename + add
   `unit_type`), rather than building parallel new tables — confirm this reading of §13.6.2 is right.
4. **`ib_relation` — drop it?** Recommend folding char↔char relations entirely into `operation` types
   8–9, per operation-ruleset §3's own framing, rather than keeping plan §6's separate `ib_relation`
   table. Confirm or keep both.
5. **`operation_type` catalogue (§4.2 table)** — ratify/adjust the 9 types; specifically confirm
   `has-status` (7) is real and whether `interacts`/`co-exists` (8–9) should be one type or two
   (operation-ruleset §8's own open question).
6. **D4 (register vs cluster as the concordance's organising collection)** — still genuinely open; not
   needed for Step 1, but the concordance view (§4.1) will eventually need a `GROUP BY` target.
7. **D5 (reconcile/consolidate/refine-rule as own work packages)** — confirmed deferred by the
   researcher this session; **not** to be settled here. Noted so it isn't silently re-opened later.
8. **`char_entry` status flow (emerging/established/under-revision)** — confirm it survives the D3
   rename unchanged, since §14 never restates it.

---

## 7. What is *not* touched by any of this

Per the operating model (plan §1.2, §13.5): this document is analysis only. No `ALTER TABLE`, no
`db --reset`, no `cfg_*` row written. The moment §6's items are confirmed, Step 1 of the plan's build
sequence (§8) — cutting the schema via the config path — becomes live work, on John, and nothing
corpus-wide until it passes.
