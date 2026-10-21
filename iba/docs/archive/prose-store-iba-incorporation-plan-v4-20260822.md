# Prose store — IBA incorporation build plan (v4 — full-scope, single-pass)

**Escalation #784.** Supersedes v1/v2/v3 (same file family, left on disk for history). This is a
**re-plan under the new development cycle** (`cfg_behaviour_rule` class=`development`,
`rule_key='test-plan-per-module-utility'`, anchored via escalation #828, GOVERNANCE.md §50):
*"plan/propose/design (in detail) → approve → build per the plan → approve"* — one design, approved
whole, then built, then tested, then approved — not a sequence of partial proposals each answered
before the next is written. Researcher, this escalation, 2026-08-22: *"the current plan looks like
it was a progressive spec build spec build which is no longer accepted."* Correct — v1→v3 each
added scope in response to what the previous round surfaced. This document is the single full-scope
design v1-v3 should have been from the start.

**How to read this document:** every decision is followed by **Rule:** citing what governs it, per
the researcher's 2026-08-22 instruction on #784 v10. Where a design point is a genuine judgement
call rather than a rule application, it is marked **Decision needed** instead.

---

## 1. What was actually checked to write this (live, not assumed)

Per `feedback_verify_db_claims_via_visible_tooling` — every claim below was checked directly
against the live `iba.db` and `bible_research.db` this session, not carried over from v1-v3's prose.

| Claim | Checked how | Result |
|---|---|---|
| `prosestore.py` / `handlers/prose.py` / `Prose.ps1` exist and are wired together | file listing + read | All 3 exist. `cfg_utility` row for `prosestore` present, `inactive=0`. |
| The 3 queued `prose.*` settings (chapter_names, book_stage_map, search_default_limit) | `SELECT * FROM cfg_setting WHERE key LIKE 'prose%'` | **0 rows** — none applied yet. |
| The orphan `key=NULL` row from the #787 mis-apply (v3's "escalation #796, awaiting decision") | `SELECT * FROM cfg_setting WHERE key IS NULL` | **0 rows** — the orphan is gone. #796 shows `state=completed` in the escalation list; resolved and cleaned up since v3 was written. |
| The 4 original scripts' `cfg_utility` activation + purpose text (v3's Part A3) | `SELECT ... FROM cfg_utility WHERE file_path LIKE '%prose%'` | All 4 still `inactive=1`, purpose text still the **old** `NON-COMPLIANT (escalation #648)` / `escalation #729` wording — A3 not applied. |
| Dispatcher registration of the 4 read operations (v3's Part A4, "held") | `SELECT * FROM cfg_work_package/cfg_step WHERE ... LIKE '%prose%'` | **0 rows** — no work package, no steps. `Prose.ps1` exists as a file but has no config-driven dispatch entry, unlike every other `*.ps1` module. |
| The write side (`apply_session_patch.py` → `prose_section`) — any IBA registration | `cfg_write_grant`, `cfg_status_flow`, `cfg_enum` all searched for `prose_section` / `prose` | **0 rows anywhere.** Confirms v3 Part B's finding still holds exactly. |
| `#795`/`#796`/`#798`/`#799`/`#828` — the items v3 listed as "pending, block everything" | `SELECT state, next_action FROM escalation WHERE id IN (...)` | **All 5 now `state=completed`.** Nothing is blocking a fresh plan from being approved and built in one pass. |
| `prose_section`'s actual CHECK constraints and live data shape | `PRAGMA`/`sqlite_master` on `bible_research.db` | `CHECK (status IN ('draft','in_review','approved','archived'))`, `CHECK (author IN ('claude_ai','claude_code','researcher'))`. Live rows: 922 `approved`, 107 `draft`, 11 `archived`, 0 `in_review`; 782 `claude_code`, 256 `claude_ai`, **2** `researcher` (the architecture doc's §3.2 says "exactly one" — stale by one row, cosmetic, noted not fixed here). |
| `apply_session_patch.py`'s actual `prose_section` operations | Read lines 1662–1850 | Six operations: `insert`, `supersede`, `delete`, `approve`, `session_a_replace`, `bulk_supersede`. All six take `status`/`author` from the **caller's JSON payload**, not from a fixed enum in code — the CHECK constraint in SQLite is the only real gate today. |
| `docs/prose-store-architecture.md` §9 "current state" table (last measured 2026-04-23) | live count vs. the doc | Doc says 21 active rows total, all `draft`. Live: **1,040 rows**, mostly `approved`. The doc's schema/rules sections (§2–§8) are still accurate; only §9's numbers are stale. Not fixed here — flagged for the doc's own next revision, out of scope for a code/config plan. |
| `cfg_table`/`cfg_column` coverage of the `prose_section` family | `SELECT * FROM cfg_table WHERE name LIKE 'prose%'` | **Already complete** — 9 tables (including FTS5 shadow tables), 68 columns catalogued. `governance.table_columns` is already satisfied for this table family; nothing to do here. |
| Whether a per-module settings table precedent exists (`governance.module.config`) | `cfg_passage` schema + rows | Yes — `cfg_passage(key, value, use, inactive)`, described in GOVERNANCE.md as *"the project's second per-module settings table"*. v3's plan to use generic `cfg_setting` with `module='prose'` for the 3 queued settings does not follow this precedent. |
| `cfg_write_grant` enforcement scope | `iba/app/lib/cfg.py:may_write()` + `cfgquality.find_unknown_write_grant_writers` | `may_write()` already accepts a `database` parameter (`'iba'` default, widened by #680) — no code change needed to grant against `bible_research`. The orphan-writer *validator*, however, only checks rows `WHERE database='iba'` — a `bible_research`-scoped grant is safe to add but will not be structurally validated until that checker is widened (separate, smaller item, flagged in §6). |

---

## 2. The task at hand, confirmed

Tracing #784's own instruction chain (v1 → v14, quoted, not paraphrased):

- **v1** (Researcher): *"design the build of Prose in the project and build the management of prose
  into the IBA App."*
- **v6** (Researcher): *"next task is to extract from IBA all configs that is related to prose."*
- **v8** (Researcher, verbatim): *"activate the 4 scripts, make them compliant, activate the tables
  and columns, and align it with the architecture."*
- **v10** (Researcher, verbatim): *"prose management is not a utility, it is a full scale module of
  the project. You need to cross read the architecture to ensure that all the rules of the
  architecture is built into the configs. this is a governance rule by itself."*

**Confirmed single-sentence task:** bring the prose store — both its read side (extract / search /
export / import) and its write side (`apply_session_patch.py`'s six `prose_section` operations) —
under IBA as a genuinely config-governed module, the same standard every other operating module in
`iba/app/handlers/` already meets, per `governance.module.config` and
`governance.rules_must_be_config_driven`.

That is **wider than v3's own Part A**, which only ever covered the read/report layer. v3 correctly
identified this gap (Part B) but explicitly declined to plan it (*"not fixing this now... a second,
separate, larger piece of work"*). Under the new cycle, that deferral itself has to be a stated,
approved scope decision, not a quiet parking — so §5 below states it as one, rather than repeating
the deferral silently.

---

## 3. Full scope — five components, planned together

### I. Read/report layer — finish what v3 Part A started

Code already built and tested (v3 §A1, re-verified this session, unchanged). Config not yet applied
(§1 table above). No design change from v3 here — the literal payloads were already correct; only
the location changes (see IV below: a dedicated `cfg_prose` table replaces v3's plan to use generic
`cfg_setting`).

### II. Dispatcher registration of the read layer (v3's "held" Part A4)

Register `prose` as a real `cfg_work_package` with 4 `cfg_step` rows (`kind='utility'` — none of the
four writes to `prose_section`; matches `candidate-curation`'s own `kind='utility'` shape, not
`verse-lexical`'s `kind='operations'`). This is what makes `Prose.ps1` a config-driven module entry
point instead of a file that exists but isn't wired in — closing the exact gap
`governance.rules_must_be_config_driven` names.

**Rule:** *"every-interactive-module-needs-ps-script"* (`cfg_behaviour_rule` id 41) — `Prose.ps1`
already exists; this step is what makes it real per `governance.rules_must_be_config_driven`, not a
new requirement.

### III. Write layer — bring `apply_session_patch.py`'s `prose_section` operations under governance

This is the component v3 Part B found and declined to plan. Scoped narrowly and deliberately here —
**not** a rearchitecture of `apply_session_patch.py` itself (that script also handles findings,
verse context, dimension review, and a dozen other unrelated patch types; rewriting it as an IBA
dispatcher module is a project-wide undertaking, out of scope for a prose-store escalation — see §5).
What IS in scope: making the *rules the architecture doc already states* real config rows, per
`governance.rules_must_be_config_driven`'s explicit text — *"no operational or process rule may
exist only in ... memory without a referenced cfg_* row."*

Five gaps, from v3 Part B's own table, now closed:

1. **`status` CHECK values** (`draft`/`in_review`/`approved`/`archived`) → new `cfg_enum` group
   `prose_section_status`.
2. **`author` CHECK values** (`claude_ai`/`claude_code`/`researcher`) → new `cfg_enum` group
   `prose_section_author`.
3. **`session_a_replace` exception**, gated in code on `author='claude_code'` → new
   `cfg_behaviour_rule` row, class=`sqlite` (per `governance.behaviour_boundary.backup_recovery`'s
   own precedent: database-write-discipline is a `sqlite`-class concern, not a separate class).
4. **Supersede-only discipline** (a revision inserts a new row; nothing already written is edited or
   lost) → second `cfg_behaviour_rule` row, same class.
5. **The two-patch pattern** (`CATALOGUE_POPULATION` then `PROSE`) → **narrowed from v3's framing.**
   The full `patch_type` vocabulary (`wa_patch_type_registry`, ~20+ types spanning the whole
   programme, not just prose) migrating into `cfg_enum` wholesale is a separate, larger,
   project-wide item — out of scope here (§5). What IS in scope: a `cfg_behaviour_rule` row stating
   the two-patch *ordering rule* for prose specifically (Patch 1 creates `prose_section_type` rows,
   Patch 2 references them by code) — the rule the architecture doc states, without migrating the
   registry it's drawn from.

Plus **write grants**, currently entirely absent for `bible_research.db` (§1 table): two
`cfg_write_grant` rows, `database='bible_research'`, writer=`apply_session_patch` (the script itself
is the writer identity — it isn't a `cfg_step`, so it's a declared non-step identity, the same shape
as the existing `run`/`escalation`/`migration` fallback identities), tables `prose_section` and
`prose_section_type`.

**Decision needed:** one row per operation (6 granular writer identities, e.g.
`apply_session_patch.prose_section.approve`) vs. one writer covering the whole script. This plan
uses **one writer, `apply_session_patch`**, matching `feedback_simple_steps_not_engineered_designs`
— granular per-operation writers would be more precise but nothing downstream currently
distinguishes them, and `apply_session_patch.py` is a single trusted entry point, not six
independently-invoked ones. Flagging this as the one real judgement call in this component; happy to
build the 6-row version instead if you'd rather have the finer grain now.

### IV. Per-module settings table — `cfg_prose`, not generic `cfg_setting`

**Correction to v3, not a new decision:** v3 proposed the 3 read-layer settings
(`chapter_names`/`book_stage_map`/`search_default_limit`) as generic `cfg_setting` rows with
`module='prose'`. `governance.module.config` states *"each operating module must have a config table
(or tables) in the cfg_* series"* — and `cfg_passage` is the live precedent for exactly this shape.
Per `feedback_fix_standard_violations_dont_ask` (a deviation from an established standard is a bug
to fix, not a judgement call), this plan uses a new `cfg_prose(key, value, use, inactive)` table,
same shape as `cfg_passage`, instead of generic `cfg_setting`. Same 3 keys, same values, same `use`
text as v3 — only the table changes.

### V. Test plan (governance rule 46 / GOVERNANCE.md §50)

Required as part of THIS design, not written after the build. Full table in §7.

---

## 4. Detailed build spec — literal payloads

`configmaint.propose` allows one pending change at a time (v3's own finding, still true) — so these
are submitted **serially in the fixed order below**, all already decided here; no new spec
decisions happen between submissions.

### IV. `cfg_prose` — new table + 3 rows

```sql
CREATE TABLE cfg_prose (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    use TEXT NOT NULL,
    inactive INTEGER NOT NULL DEFAULT 0
);
```

| key | value | use |
|---|---|---|
| `prose.chapter_names` | `{"0":"Preamble","1":"Programme purpose","2":"Research methodology","3":"Research approach","4":"Data architecture","5":"Data integrity & governance","6":"Instruction corpus"}` | Chapter-number → readable-name lookup used when the extract writes Markdown/Word. Read by `prosestore.py:chapter_names(cfg)`. Fixes `cfg_utility` `NON-COMPLIANT (escalation #648)` flag on `build_programme_prose_extract.py`. |
| `prose.book_stage_map` | `{"Programme":["programme"],"Detail design":["session_a","session_b","session_b_phase9","session_c","session_d"],"Findings":["synthesis","verse-analysis"],"Essays":["essay"]}` | Allowed `--book` values and which `source_stage`(s) each covers. Read by `prosestore.py:book_stage_map(cfg)`. Same #648 flag. |
| `prose.search_default_limit` | `100` | Default result cap for `search_prose.py` / `prose.search` when `-Limit` isn't given. Read by `prosestore.py:search_default_limit(cfg)`. Fixes `search_prose.py`'s own #648 flag. |

*(Table creation itself is a schema migration, not a `configmaint.propose` row — goes through the
same migration path `cfg_passage` originally used.)*

### I / III (enum + behaviour rule) — new `cfg_enum` groups

| name | value | ordinal |
|---|---|---|
| `prose_section_status` | `draft` | 0 |
| `prose_section_status` | `in_review` | 1 |
| `prose_section_status` | `approved` | 2 |
| `prose_section_status` | `archived` | 3 |
| `prose_section_author` | `claude_ai` | 0 |
| `prose_section_author` | `claude_code` | 1 |
| `prose_section_author` | `researcher` | 2 |

### III — new `cfg_status_flow` rows, `entity='prose_section'`

| status | set_by | ordinal |
|---|---|---|
| `draft` | `apply_session_patch.py: prose_section insert/supersede/bulk_supersede (caller-supplied, the default when omitted)` | 0 |
| `in_review` | `apply_session_patch.py: prose_section insert/supersede (caller-supplied status — no dedicated transition op exists; live data currently has 0 rows at this status)` | 1 |
| `approved` | `apply_session_patch.py: prose_section approve (the one dedicated transition op — also stamps approved_at/approved_by)` | 2 |
| `archived` | `apply_session_patch.py: prose_section insert (caller-supplied status only — confirmed live: 11 existing rows were archived at insert time, not via a transition op)` | 3 |

### III — new `cfg_behaviour_rule` rows, `class='sqlite'`

| rule_key | rule_text (source: `docs/prose-store-architecture.md` §6.1 / §7) |
|---|---|
| `prose-section-session-a-replace-author-gate` | "The `session_a_replace` operation is the one exception to `prose_section`'s supersede-only immutability — it updates a row in place. Code-gated on `author='claude_code'` (the `UPDATE ... WHERE id=? AND author='claude_code'` clause in `apply_session_patch.py`); permitted only for Session A mechanical extracts, because they are reproducible from structured data rather than analytical judgement." |
| `prose-section-supersede-only-discipline` | "Narrative `prose_section` rows are immutable once written, outside the one exception above. A revision creates a new row (`version = old.version + 1`, `supersedes_id = old.id`); the predecessor's `superseded_by_id` is set to point forward. No `UPDATE` of `body` on an existing narrative row is a sanctioned operation." |
| `prose-section-two-patch-ordering` | "A new prose chapter reaches the database in two ordered patches: `CATALOGUE_POPULATION` first (creates `prose_section_type` handles), then `PROSE` (content, referencing handles by `section_type_id_lookup: {code}` so the content patch never needs Patch 1's assigned integer IDs). Applying `PROSE` before its `CATALOGUE_POPULATION` fails at the code lookup, by design." |

### III — new `cfg_write_grant` rows, `database='bible_research'`

| writer | table_name |
|---|---|
| `apply_session_patch` | `prose_section` |
| `apply_session_patch` | `prose_section_type` |

### II — new `cfg_work_package` + 4 `cfg_step` rows

`cfg_work_package`: `name='prose'`, `ps_script='iba/app/ps/Prose.ps1'`, `runs_over='none'`,
`chained=0`.

| ordinal | step | handler | kind | does |
|---|---|---|---|---|
| 0 | `prose.extract` | `iba.app.handlers.prose:extract` | utility | Programme-prose extract (JSON/MD/DOCX) |
| 1 | `prose.search` | `iba.app.handlers.prose:search` | utility | FTS/plain search over `prose_section` |
| 2 | `prose.export_chapter` | `iba.app.handlers.prose:export_chapter` | utility | Export a chapter to editable `.md` |
| 3 | `prose.import_chapter` | `iba.app.handlers.prose:import_chapter` | utility | Turn an edited `.md` into a patch file (writes no DB row itself) |

### I — reactivate the 4 original scripts (`cfg_utility`)

Unchanged from v3 §A3 — same 4 rows, same new `purpose` text (superseded-pointer wording), `inactive: 1 → 0`. Not repeated here; v3's table is still correct, only its status changes from "queued" to "part of this approved batch."

---

## 5. Explicitly out of scope (stated, not silently deferred)

| Item | Why it's not here | Where it belongs |
|---|---|---|
| Migrating the full `wa_patch_type_registry` (~20+ patch types, whole-programme) into `cfg_enum` | Far larger than prose; touches every patch type the programme uses, not just `PROSE`/`CATALOGUE_POPULATION` | A separate escalation, if/when `apply_session_patch.py` as a whole is brought under IBA |
| Rearchitecting `apply_session_patch.py` into an IBA dispatcher module | Same reason — it serves the whole programme, not just prose | Separate, larger item |
| Widening `find_unknown_write_grant_writers` to also validate `database='bible_research'` grants | A `configmaint.validate` mechanism change, unrelated to prose content itself | Small follow-on item, noted here so it isn't lost — not blocking this plan (the grant rows are still correct and documented even before the checker covers them) |
| `docs/prose-store-architecture.md` §9 "current state" table refresh (stale since 2026-04-23) | Doc maintenance, not a config/code change | Next time that doc is touched |
| Generic `.md`-marker round-trip import tool (architecture doc §8.3) | The architecture doc itself already defers this ("availability... tracked separately") | Unchanged from the doc's own note |
| Escalation **#786** (Programme Prose Chapter 4 rewrite) | A sibling escalation under the same `related_activity`, not a child of #784 — content work, not infrastructure | Its own thread, unaffected by this plan |
| `cfg_prose_chapter` status `not_yet_aligned` for chapters 4–6 | Tracked in escalation #739 (on-hold, scheduled before analysis phase) | #739 |

---

## 6. Sequencing (the "build per the plan" stage)

Once this whole plan is approved, submit in this fixed order (one `configmaint.propose` pending at
a time, per existing constraint — order fixed now, not decided proposal-by-proposal):

1. `cfg_prose` table creation + 3 rows (§4, component IV).
2. `cfg_enum` — `prose_section_status` (4 rows) + `prose_section_author` (3 rows).
3. `cfg_status_flow` — 4 rows, `entity='prose_section'`.
4. `cfg_behaviour_rule` — 3 rows, `class='sqlite'`.
5. `cfg_write_grant` — 2 rows, `database='bible_research'`.
6. `cfg_work_package` `prose` + 4 `cfg_step` rows.
7. `cfg_utility` — reactivate the 4 original scripts (`inactive: 1→0` + new `purpose` text), 4 changes.

13 proposals total (down from v3's 13 — same count, different shape: v3's 4 A2/A3 config items
split differently; this plan's 13 cover the same read-layer ground plus the write-layer + dispatcher
registration v3 held back).

---

## 7. Test plan (governance rule 46 — required, run after build, results go in the resolution)

| # | Function / operation | Test case | Expected |
|---|---|---|---|
| 1 | `prose.extract` | `--book Programme --also-markdown --also-docx --include-body` | JSON+MD+DOCX written, chapter names resolved from `cfg_prose` (not hardcoded) |
| 2 | `prose.extract` | omit `--book` | All books extracted |
| 3 | `prose.extract` | invalid `--book` value not in `book_stage_map` | Clean error, not a crash |
| 4 | `prose.search` | `grace` (plain text) | Results ≤ `prose.search_default_limit` when `--limit` omitted |
| 5 | `prose.search` | `--limit 3` | Exactly 3 shown, total count still reported |
| 6 | `prose.search` | `--fts "grace OR love"` | FTS5 expression path exercised, distinct from plain-text path |
| 7 | `prose.export_chapter` | `--book Programme --chapter 1` | Editable `.md` with `PROSE_SECTION id:` markers |
| 8 | `prose.import_chapter` | unedited re-import of #7's output | Validates clean, generates a no-op-content patch, **writes nothing to the DB** (checked via DB mtime, same discipline v3 §A1 used) |
| 9 | `prose.import_chapter` | edited body, missing a required marker | Clean validation error, not a crash |
| 10 | `Prose.ps1 -Step Extract/Search/ExportChapter/ImportChapter` | each of the 4, once | Dispatcher-driven run succeeds identically to the direct handler call (confirms component II's wiring, not just component I's code) |
| 11 | `apply_session_patch.py`, `prose_section` `insert` | new row, `status='draft'` | Row created, `word_count` derived |
| 12 | `apply_session_patch.py`, `prose_section` `supersede` | supersede an existing row | New row v+1, old row's `superseded_by_id` set, old row content unchanged (immutability) |
| 13 | `apply_session_patch.py`, `prose_section` `approve` | approve a `draft` row | `status='approved'`, `approved_at`/`approved_by` stamped |
| 14 | `apply_session_patch.py`, `prose_section` `approve` | approve an already-`approved` row (idempotency) | No-op (code's own `WHERE status != 'approved'` clause), not a duplicate stamp |
| 15 | `apply_session_patch.py`, `prose_section` `session_a_replace` | replace a `claude_code`-authored row | In-place update succeeds |
| 16 | `apply_session_patch.py`, `prose_section` `session_a_replace` | attempt on a `claude_ai`-authored row | `WHERE author='claude_code'` clause blocks it — 0 rows affected, confirming the author gate is real |
| 17 | `apply_session_patch.py`, `prose_section` `delete` | soft-delete a row | `delete_flagged=1`, row still present (no physical delete) |
| 18 | `apply_session_patch.py`, `prose_section` `bulk_supersede` | 2+ targets in one call | All targets superseded in one transaction, correct count in `counts` |
| 19 | `cfg_write_grant` (informational, not enforced yet per §5) | confirm rows present via `Cfg.may_write('apply_session_patch', database='bible_research')` | Returns `{'prose_section', 'prose_section_type'}` |
| 20 | `configmaint.validate` full run | after all 13 proposals applied | Clean — no new structural violations introduced (checked, not assumed) |

All 20 cases run against the live `bible_research.db`/`iba.db` (read-only where the operation
itself is read-only; write cases use throwaway test rows, cleaned up after, same discipline
escalation #795's own test batch used — `#815`-`#822`). Results — pass/fail per row, not a prose
summary — go into the resolution when this batch is submitted for final approval.

---

## 8. What I need from you

One decision, on the whole plan:

1. **Approve this plan as written** (§3–§7) — I submit the 13 proposals in the fixed §6 order, one
   at a time through `configmaint.propose` as usual, build the code changes (`prosestore.py` config
   reads already point at `cfg.module_setting`-shaped calls for I; II/III are new wiring), run all
   20 test cases in §7, and bring the full results back in one resolution — not a running commentary
   per proposal.
2. Or **flag specific items to change first** — in particular §3's "Decision needed" (one
   `apply_session_patch` writer vs. six per-operation writers) is the one place this plan made a
   judgement call rather than applying an existing rule; everything else cites its governing rule
   directly.

No partial go-ahead needed item-by-item — that's the exact pattern this re-plan exists to stop.
