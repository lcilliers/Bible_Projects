# IBA config rules for the process loop — straightening the `cfg_*` store

> **Status: WORKING DOC. Design-for-confirmation, no DB writes.** Directed 2026-07-20.
> The process loop is now consolidated (`iba-application-plan-v2-20260720.md` §14). This doc
> **extracts every rule that loop implies into the actual `cfg_*` model**, so config — not code —
> carries the process. Config is **DB-authoritative** (`iba/app/db/iba.db`, 16 `cfg_*` tables; the
> `iba/app/config/*.csv` files are a current export, validated row-for-row on 2026-07-20). Two fully
> decided rulesets are drafted here as concrete candidate rows (§4, §5); the rest is inventoried with
> its open decisions (§6–§7) for us to nail one family at a time.

---

## 1. The config model, as it actually is (grounding)

Nothing in the loop is invented structure — it all lands in the existing `cfg_*` shapes:

| `cfg_*` table | Holds | Rows today |
|---|---|---|
| `cfg_work_package` | a run: `name · ps_script · runs_over` | 3 |
| `cfg_step` | a run's ordered steps: `work_package · ordinal · step · handler · scope · does` | 10 |
| `cfg_table` | every DB table declared: `name · grain · use` | 17 |
| `cfg_column` | column-level rules | 127 |
| `cfg_enum` | value sets: `name · value · ordinal` | 26 |
| `cfg_status_flow` | status transitions: `entity · status · set_by · ordinal` | 5 |
| `cfg_write_grant` | write authority: `writer · table_name` (the `may_source` enforcement) | 26 |
| `cfg_on_fail` | per-step failure: `step · condition · path · resolver · message` | 10 |
| `cfg_setting` | scalars: `key · value · use` | 23 |
| `cfg_candidate_rule` | a **domain ruleset** in its own table: `kind · value` | 289 |
| `cfg_api·connection·book_order·unique·meta·change_log` | plumbing | — |

**The load-bearing pattern:** `cfg_candidate_rule` proves domain rulesets get their **own `cfg_*`
table**, not a settings blob. The loop needs several more of these (§6.8).

---

## 2. What exists today — Base layer only

Three work packages, all **Base-layer substrate**; **zero interpretive / concordance runs exist yet.**

- `new-word` (7 steps) — Raw pull for a word: registry → discover → detail → verses → write → validate.
- `set-candidates` (2 steps) — seed refresh + stamp `span_candidate` per book.
- `build-passages` (1 step) — recompute a book's `passage` from candidate continuity.

Everything in §3 of the plan's §14 is **net-new config.**

---

## 3. The inventory — what the loop adds to config (by `cfg_*` type)

Each item tagged **[DECIDED]** (researcher-settled in §14, draftable now) or **[OPEN]** (needs a call
first — collected in §7).

### 3.1 `cfg_table` / `cfg_column` — new/changed DB tables
- `study_unit` — **[OPEN: repurpose `passage`?]** the reading frame; typed by genre (§14.1).
- `study_unit_char` — **[DECIDED]** one row per (study_unit × characteristic) + analytic status.
- `verse_study_unit` — **[DECIDED]** the verse→study-unit index (a verse in at most one unit, cf. `verse_passage`).
- `operation` — **[DECIDED, core]** the characteristic-in-motion edges (§14.4).
- `meaning` — **[DECIDED, core]** the signed-off meaning paragraph (§14.4).
- three concordances — **[OPEN: view vs table; how a span splits across IB / other-being / body]** (§14.5).
- reconcile `ib_entry/ib_finding/ib_relation/ib_neighbour` (plan §6) **vs** `operation/meaning` naming — **[OPEN]** (§14.8).

### 3.2 `cfg_enum` — new value sets
- `char_role` — **[DECIDED]** characteristic · qualifier · standalone · uncertain.
- `verse_state` — **[DECIDED]** not-started · in-progress · not-relevant · complete (§14.2).
- `completion_axis` — **[DECIDED]** concordance · lexical · meaning (each in-progress/complete) (§14.2).
- `body_type` — **[DECIDED]** ib · other-being · physical-body (§14.5).
- `meaning_status` — **[DECIDED]** draft · signed-off · cross-referenced (§14.2).
- `operation_type` — **[OPEN: the catalogue]** affected-by · affects · status · from · to · interacts · co-exists … = the dimensions (§14.4); needs §6.8 `cfg_operation_type`.

### 3.3 `cfg_status_flow` — new transitions
- `verse` completion flow (the three axes) — **[DECIDED]** (§14.2).
- `study_unit_char` analytic status — **[DECIDED]**.
- `meaning` sign-off — **[DECIDED]**.

### 3.4 `cfg_work_package` + `cfg_step` — new runs
- `prepare-for-read` — **[DECIDED]** steps in §14.6; scope = study-unit request.
- `analyse-characteristic` — **[DECIDED]** the meaning loop, §14.6 steps 1–10; scope = char-in-study-unit.
- `initialise-concordances` — **[OPEN, blocked by 3.1 span-split]** one-off bulk (§14.3).
- `seed-update` — **[DECIDED]** add/withdraw seed → auto re-run set-characteristics (§14.3).
- researcher specifics — **[DECIDED]** `add-candidate` / `remove-candidate` / `reassign-strong` (§14.7).
- `report` — **[DECIDED]** the report/extract set (§14.7).
- `consolidate` / `reconcile` / `refine-rule` — **[OPEN: own package, or steps inside analyse?]** (§14.8).

### 3.5 `cfg_write_grant` — new write authority
One grant per new handler → new table (the enforced `may_source`). Follows mechanically once §3.1/§3.4
are set. E.g. `analyse.record → operation`, `analyse.record → meaning`, `analyse.record → span (role)`,
`prepare.build → study_unit_char`, `prepare.build → verse_study_unit`.

### 3.6 `cfg_on_fail` — new failure conditions
Per new step: e.g. `prepare.resolve-unit / no-genre`, `analyse.load / char-not-candidate`,
`analyse.record / role-conflict`. Follows once §3.4 steps exist.

### 3.7 `cfg_setting` — new scalars
Thresholds the rulesets reference: poem short-vs-long boundary, chapter-section size, completeness
minimums, screen parameters. Small; filled as the rulesets below are built.

### 3.8 New **domain rule-tables** (the `cfg_candidate_rule` pattern) — the real substance
These are where "the rules" actually live:
- `cfg_study_unit_rule` — **[DECIDED — drafted in §4]** the genre→unit derivation (§14.1).
- `cfg_operation_type` — **[OPEN]** the dimension/operation-type catalogue + mechanical/hybrid/API split.
- `cfg_screen_rule` — **[OPEN]** Screen-0 (human-IB vs God-arena) · three-body split · role assignment · inclusion.
- `cfg_reconcile_rule` — **[OPEN]** the confirm/extend/adjust/contradict triggers (§14.6 step 7).

---

## 4. Drafted now — `cfg_study_unit_rule` (§14.1, fully decided)

The entry-point derivation, ready to become rows (`request_kind · genre · size · yields · route`):

| request_kind | genre | size | yields | route |
|---|---|---|---|---|
| book | poetic | short | 1 unit = whole poem | `unit:poem-whole` |
| book | poetic | long | many units = logical divisions | `unit:poem-divide` |
| book | narrative | — | 1 unit per narrative (scene/episode) | `unit:narrative-split` |
| book | (prose/chapter) | — | 1 unit per chapter **section** | `unit:chapter-section` |
| chapter | any | — | split chapter into sections | `unit:chapter-section` |
| verse | any | — | the verse's already-assigned unit; else read genre → apply book+genre row | `unit:verse-resolve` |
| characteristic | any | — | pull its verses + report; researcher selects verses → each takes the `verse` row | `unit:char-extract` |

Open only: the *short/long* boundary and the *section* detector are `cfg_setting` scalars + a Step-2
heuristic on John (plan §11).

---

## 5. Drafted now — the completeness model (§14.2, fully decided)

**`cfg_enum` rows:**
- `verse_state`: `not-started`(0) · `in-progress`(1) · `not-relevant`(2) · `complete`(3)
- `completion_axis`: `concordance`(0) · `lexical`(1) · `meaning`(2)
- `axis_state`: `in-progress`(0) · `complete`(1)
- `meaning_status`: `draft`(0) · `signed-off`(1) · `cross-referenced`(2)

**Done rule** (a characteristic/verse is complete when **all three**): (1) all its verses are in the
concordance, (2) it has a lexical, (3) its meaning is `signed-off` **or** `cross-referenced` to a
signed-off meaning. → encoded as a `validate` step + `cfg_setting` `completeness.requires =
concordance,lexical,meaning`.

**`cfg_status_flow` (entity `verse`)** tracks the three axes independently; overall `in-progress`
= any axis unfinished; overall `complete` = all axes complete (or `not-relevant`).

---

## 6. Proposed order to straighten the rest

Dependency-first, so nothing references a rule that doesn't exist yet:

1. **Enums + new tables** (§3.1–3.3) — everything else references them. Mostly DECIDED; unblocks fast.
2. **The domain rule-tables** (§3.8) — the substance. `cfg_study_unit_rule` (drafted) → then the three
   OPEN ones (`cfg_operation_type`, `cfg_screen_rule`, `cfg_reconcile_rule`), each its own focused pass.
3. **Work packages + steps** (§3.4) — compose the rules into runs (§14.6 is the blueprint).
4. **Guards** — `cfg_write_grant` + `cfg_on_fail` (§3.5–3.6), mechanical once steps exist.
5. **Settings + reports** (§3.7, report package).

---

## 6a. Decisions locked (researcher, 2026-07-20)

- **D1** — concordance = a **view** (start there).
- **D2** — **not** three physically-split concordances; the span carries a **body_type marker**
  (ib / other-being / physical) so the other-being and physical catalogues are *extractable with their
  verses*. Other-being/physical mostly function as **qualifiers** on the IB reading.
- **D3** — rename the analytical tables to **`operation`** + **`finding`** (new semantics, not the old
  `ib_*`); `meaning` (§14.4) also stands. operation/finding/meaning boundary pinned in the operation
  ruleset (`iba-operation-ruleset-v1-20260720.md` §6).
- **D4** — organising collection undecided, but an **aggregator layer is required** (register or cluster
  or other).
- **D6** — rule-refinement propagation = **raise a researcher-decision alert** (the `escalation` path);
  **no bulk propagation**.
- **Item 8** — prepare the operation ruleset → done (`iba-operation-ruleset-v1-20260720.md`).

## 7. Decisions that block config (surface these first)

| # | Decision | Blocks |
|---|---|---|
| D1 | Concordance = **view or table**? | §3.1 concordance tables |
| D2 | How a span **splits across the three bodies** (IB / other-being / physical) | `initialise-concordances`, §3.1 |
| D3 | Keep plan §6's `ib_entry/finding/relation/neighbour`, or **rename to `operation`/`meaning`**? | all §3.1 core tables |
| D4 | Organise concordance by **register or cluster** (and the register re-naming it forces) | report package, entry key |
| D5 | `reconcile` / `consolidate` / `refine-rule` = **own work packages or steps inside `analyse`**? | §3.4 |
| D6 | **Rule-refinement propagation** — how the app triggers re-work without a bulk sweep | `cfg_reconcile_rule`, refine-rule |

---

## 8. Recommended first move

**Start with §3.8 `cfg_operation_type` — the dimension/operation catalogue.** Reason: it is the most
study-defining ruleset (the `operation` table *is* the analytical heart, §14.4), it is the least
dependent on the OPEN table-shape decisions (D1–D3), and it directly reuses the existing ve_nr
dimension work — so we convert prior thinking into config rather than inventing. `cfg_study_unit_rule`
(§4) and the completeness enums (§5) can be committed alongside since they're already drafted.

**Question for you:** start at `cfg_operation_type`, or would you rather settle the blocking table
decisions (D1–D3) first so the whole schema falls out together?
