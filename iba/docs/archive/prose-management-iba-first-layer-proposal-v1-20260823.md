# Prose management in IBA — first layer: proposal (escalation #829)

**Stage:** plan/propose/design (in detail), per `cfg_behaviour_rule` class=`development`,
rule_key=`test-plan-per-module-utility` (anchored via escalation #828, GOVERNANCE.md §50):
*"plan/propose/design (in detail) → approve → build per the plan → approve"*. Nothing in this
document has been submitted to `configmaint.propose` or built. This is the design for the
researcher's approve/revise decision.

---

## 0. Scope, stated once, held to throughout

Escalation **#829** (`from_id=784`), raised with this scope, verbatim:

> Scope = the mechanical/storage layer only (Plan v4's config layer), per #784 §15's own inventory
> of what is designed-but-not-built: (1) finish the read-layer config (dispatcher registration for
> the 4 read operations); (2) bring `apply_session_patch.py`'s 6 `prose_section` write operations
> under governance; (3) a dedicated `cfg_prose` module table; (4) a test plan up front, per
> escalation #828. Explicitly OUT of scope — stay parked at #784: the prose-change-flag mechanism,
> chapter-rewrite assistance, `prose_section_verse_link`, the Concordance (5th book),
> raw-material-visibility for writing, and the book-2/book-3 boundary question.

This document is that plan. It reuses, in full, the design already built for this exact scope in
`iba/docs/prose-store-iba-incorporation-plan-v4-20260822.md` (escalation #784, filed 2026-08-22,
never approved — the conversation moved to the wider authoring-process question before it was acted
on; v4 was explicitly *set aside, not rejected*). Nothing here is re-derived from scratch. What is
new in this document is: (a) re-verification that none of v4's live-state claims have drifted since
2026-08-22, and (b) two real deltas the intervening file-control build introduced, folded in rather
than left stale — §2 below.

---

## 1. Re-verified live today (2026-08-23) — zero drift found

| Claim (from v4 §1) | Re-checked how, today | Result |
|---|---|---|
| No `prose*` `cfg_setting` rows exist | `SELECT * FROM cfg_setting WHERE key LIKE 'prose%'` | **0 rows**, unchanged |
| No `cfg_prose` table exists yet | `sqlite_master` | **absent**, unchanged |
| The 4 original scripts still `inactive=1`, old purpose text | `cfg_utility` | **All 4 still inactive=1**, purpose text still the old `NON-COMPLIANT (#648)`/`#729` wording, unchanged |
| `prosestore.py` registered, `inactive=0` | `cfg_utility` | Confirmed, unchanged |
| No dispatcher registration for `prose` | `cfg_work_package`/`cfg_step` | **0 rows**, unchanged |
| No write grants / status flow / enums for `prose_section` | `cfg_write_grant`/`cfg_status_flow`/`cfg_enum` | **0 rows anywhere**, unchanged |
| `prose_section` CHECK constraints and live data shape | `sqlite_master` + `GROUP BY status/author` on `bible_research.db` | Unchanged: `CHECK (status IN ('draft','in_review','approved','archived'))`, `CHECK (author IN ('claude_ai','claude_code','researcher'))`; **922 approved / 107 draft / 11 archived**; **782 claude_code / 256 claude_ai / 2 researcher**; **max id 1040** — identical to v4's numbers, confirming the file-control test rounds (§2 below) left no residue |
| `cfg_passage` precedent + `Cfg.module_setting()` reader | `cfg_passage` schema/rows + `cfg.py:module_setting` | Both present, unchanged (6 `cfg_passage` rows, reader at `iba/app/lib/cfg.py:76`) |
| #795/#796/#798/#799/#828 all resolved (nothing blocking) | `SELECT state, next_action FROM escalation WHERE id IN (...)` | **All 5 `state=completed`** |

Nothing in v4's factual basis has moved. The design below is safe to reuse as-is except where §2
names a real change.

---

## 2. Two real deltas since Plan v4 (2026-08-22) — folded in, not glossed over

**a) `export_chapter`/`import_chapter` behavior changed** under the file-control build that
happened the same day, *after* v4's test cases (§7 there, tests 7–8) were drafted — confirmed by
reading the live code (`iba/app/lib/prosestore.py`), not assumed from the design doc:

- Exports are now named with an edit-cycle version: `{stem}-v{n}-{date}.md`, scanned across both
  the active folder and its archive so a version number is never reused.
- An **unedited re-import is now refused outright** (`ValueError: ... nothing to import ... The
  file is left in place (not archived)`) — v4's test 8 expected "generates a no-op-content patch,
  writes nothing to the DB." That expectation is stale; the actual (and correct, per the
  section-is-the-editing-unit finding at #784 §6) behavior is a clean refusal, not a no-op patch.
- A successful import **auto-archives** the edit file (moves it into
  `{edit_file_dir}/archive/`) and sets the new `prose_section.source_file` to the archived path,
  not the pre-move path.

§7 below corrects tests 7–8 and adds a case for the auto-archive behavior, rather than shipping a
test plan against code that no longer exists.

**b) The edit-file location becomes part of this proposal's `cfg_prose` table, not a separate
decision.** `CHAPTER_EDIT_OUT_DIR` (`prosestore.py`, hardcoded to `Path("outputs") / "markdown" /
"prose-edits"`) was named at #784 §6 as an open choice — *"file-organisation-rules.md vs. a
`cfg_prose` setting, not decided."* Checked: it is a single hardcoded path constant, the identical
shape already flagged `NON-COMPLIANT` on the other 4 prose scripts under escalation #648. Per
`feedback_fix_standard_violations_dont_ask` (a deviation from an established, documented standard
is a bug to fix, not a fresh judgement call), this is folded into component IV below as a 4th
`cfg_prose` key rather than left as a 5th open decision — the value is the live path already in
production use, not a new value needing a researcher call.

---

## 3. Full scope — five components (framing unchanged from v4; IV and V updated per §2)

**I. Read/report layer.** Code already built and tested (unchanged from v4; re-verified §1). Only
the config is missing.

**II. Dispatcher registration.** Register `prose` as a real `cfg_work_package` with 4 `cfg_step`
rows, `kind='utility'` — the same wiring every other operating module already has, closing the gap
`governance.rules_must_be_config_driven` names for `Prose.ps1` today.

**III. Write-layer governance.** `apply_session_patch.py`'s 6 `prose_section` operations
(`insert`/`supersede`/`delete`/`approve`/`session_a_replace`/`bulk_supersede`) get: `cfg_enum`
backing for the `status`/`author` CHECK values, `cfg_status_flow` rows recording which operation
sets which status, `cfg_behaviour_rule` rows for the 3 architecture rules the doc states but no
config row backs (the `session_a_replace` author gate, supersede-only immutability, the two-patch
ordering rule), and `cfg_write_grant` rows for the two `bible_research.db` tables this script
writes. **Not** a rearchitecture of `apply_session_patch.py` itself (§5).

**IV. `cfg_prose` — a dedicated per-module table, 4 keys** (was 3 in v4; §2b adds the 4th):
`prose.chapter_names`, `prose.book_stage_map`, `prose.search_default_limit`,
**`prose.edit_file_dir`** (new). Same shape as the `cfg_passage` precedent
(`governance.module.config`), not generic `cfg_setting` — a correction v4 already made for the
original 3; this proposal applies the same fix to the 4th.

**V. Test plan.** Required up front, not written after the build (governance rule 46 /
GOVERNANCE.md §50). Corrected for §2a's behavior change, expanded for §2b's new config key — §7.

---

## 4. Detailed build spec — literal payloads

Submitted serially, one `configmaint.propose` pending change at a time, in the fixed §6 order — no
new spec decisions between submissions.

### IV. `cfg_prose` — new table + 4 rows

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
| `prose.chapter_names` | `{"0":"Preamble","1":"Programme purpose","2":"Research methodology","3":"Research approach","4":"Data architecture","5":"Data integrity & governance","6":"Instruction corpus"}` | Chapter-number → readable-name lookup used when the extract writes Markdown/Word. Read by `prosestore.py:chapter_names(cfg)`. Fixes `build_programme_prose_extract.py`'s `NON-COMPLIANT (#648)` flag. |
| `prose.book_stage_map` | `{"Programme":["programme"],"Detail design":["session_a","session_b","session_b_phase9","session_c","session_d"],"Findings":["synthesis","verse-analysis"],"Essays":["essay"]}` | Allowed `--book` values and which `source_stage`(s) each covers. Read by `prosestore.py:book_stage_map(cfg)`. Same #648 flag. |
| `prose.search_default_limit` | `100` | Default result cap for `search_prose.py` / `prose.search` when `-Limit` isn't given. Read by `prosestore.py:search_default_limit(cfg)`. Fixes `search_prose.py`'s own #648 flag. |
| `prose.edit_file_dir` | `"outputs/markdown/prose-edits"` | Directory `export_chapter` writes editable chapter `.md` files into, and `import_chapter` archives them from (into `{value}/archive/`) on a successful import. Read by `prosestore.py` in place of the hardcoded `CHAPTER_EDIT_OUT_DIR` constant. Closes #784 §6's open location question and the #648-shaped hardcoded-constant violation in the same fix — value unchanged from current production use, not a new researcher decision. |

### I / III — new `cfg_enum` groups (unchanged from v4)

| name | value | ordinal |
|---|---|---|
| `prose_section_status` | `draft` | 0 |
| `prose_section_status` | `in_review` | 1 |
| `prose_section_status` | `approved` | 2 |
| `prose_section_status` | `archived` | 3 |
| `prose_section_author` | `claude_ai` | 0 |
| `prose_section_author` | `claude_code` | 1 |
| `prose_section_author` | `researcher` | 2 |

### III — new `cfg_status_flow` rows, `entity='prose_section'` (unchanged from v4)

| status | set_by | ordinal |
|---|---|---|
| `draft` | `apply_session_patch.py: prose_section insert/supersede/bulk_supersede (caller-supplied, the default when omitted)` | 0 |
| `in_review` | `apply_session_patch.py: prose_section insert/supersede (caller-supplied status — no dedicated transition op exists; live data currently has 0 rows at this status)` | 1 |
| `approved` | `apply_session_patch.py: prose_section approve (the one dedicated transition op — also stamps approved_at/approved_by)` | 2 |
| `archived` | `apply_session_patch.py: prose_section insert (caller-supplied status only — confirmed live: 11 existing rows were archived at insert time, not via a transition op)` | 3 |

### III — new `cfg_behaviour_rule` rows, `class='sqlite'` (unchanged from v4)

| rule_key | rule_text (source: `docs/prose-store-architecture.md` §6.1 / §7) |
|---|---|
| `prose-section-session-a-replace-author-gate` | "The `session_a_replace` operation is the one exception to `prose_section`'s supersede-only immutability — it updates a row in place. Code-gated on `author='claude_code'` (the `UPDATE ... WHERE id=? AND author='claude_code'` clause in `apply_session_patch.py`); permitted only for Session A mechanical extracts, because they are reproducible from structured data rather than analytical judgement." |
| `prose-section-supersede-only-discipline` | "Narrative `prose_section` rows are immutable once written, outside the one exception above. A revision creates a new row (`version = old.version + 1`, `supersedes_id = old.id`); the predecessor's `superseded_by_id` is set to point forward. No `UPDATE` of `body` on an existing narrative row is a sanctioned operation." |
| `prose-section-two-patch-ordering` | "A new prose chapter reaches the database in two ordered patches: `CATALOGUE_POPULATION` first (creates `prose_section_type` handles), then `PROSE` (content, referencing handles by `section_type_id_lookup: {code}` so the content patch never needs Patch 1's assigned integer IDs). Applying `PROSE` before its `CATALOGUE_POPULATION` fails at the code lookup, by design." |

### III — new `cfg_write_grant` rows, `database='bible_research'` (unchanged from v4; §6 decision still standing)

| writer | table_name |
|---|---|
| `apply_session_patch` | `prose_section` |
| `apply_session_patch` | `prose_section_type` |

**Standing decision (carried from v4, not re-decided here):** one writer identity
(`apply_session_patch`) covering the whole script, vs. six granular per-operation identities (e.g.
`apply_session_patch.prose_section.approve`). This plan keeps v4's answer — one writer, per
`feedback_simple_steps_not_engineered_designs` — nothing downstream currently distinguishes the six
operations, and the script is a single trusted entry point. Flagged again here as the one place
this proposal makes a judgement call rather than applying an existing rule; happy to build the
six-row version instead if the finer grain is wanted now.

### II — new `cfg_work_package` + 4 `cfg_step` rows (unchanged from v4)

`cfg_work_package`: `name='prose'`, `ps_script='iba/app/ps/Prose.ps1'`, `runs_over='none'`,
`chained=0`.

| ordinal | step | handler | kind | does |
|---|---|---|---|---|
| 0 | `prose.extract` | `iba.app.handlers.prose:extract` | utility | Programme-prose extract (JSON/MD/DOCX) |
| 1 | `prose.search` | `iba.app.handlers.prose:search` | utility | FTS/plain search over `prose_section` |
| 2 | `prose.export_chapter` | `iba.app.handlers.prose:export_chapter` | utility | Export a chapter to editable `.md` |
| 3 | `prose.import_chapter` | `iba.app.handlers.prose:import_chapter` | utility | Turn an edited `.md` into a patch file (writes no DB row itself) |

### I — reactivate the 4 original scripts (`cfg_utility`) (unchanged from v4)

Same 4 rows, same superseded-pointer `purpose` text, `inactive: 1 → 0`.

---

## 5. Explicitly out of scope (stated, not silently deferred)

| Item | Why it's not here | Where it belongs |
|---|---|---|
| Migrating the full `wa_patch_type_registry` (~20+ patch types, whole-programme) into `cfg_enum` | Far larger than prose | A separate escalation, if/when `apply_session_patch.py` as a whole is brought under IBA |
| Rearchitecting `apply_session_patch.py` into an IBA dispatcher module | Same reason | Separate, larger item |
| Widening `find_unknown_write_grant_writers` to also validate `database='bible_research'` grants | A `configmaint.validate` mechanism change, unrelated to prose content | Small follow-on item, noted so it isn't lost — not blocking |
| `docs/prose-store-architecture.md` §9 "current state" table refresh (stale since 2026-04-23) | Doc maintenance, not config/code | Next time that doc is touched |
| Generic `.md`-marker round-trip import tool (architecture doc §8.3) | Already deferred by the architecture doc itself | Unchanged |
| Escalation **#786** (Programme Prose Chapter 4 rewrite) | Sibling escalation, content work not infrastructure | Its own thread |
| `cfg_prose_chapter` status `not_yet_aligned` for chapters 4–6 | Tracked separately | Escalation #739 (on-hold) |
| The prose-change-flag mechanism (§7 of the #784 capture) | Authoring-process layer, agreed shape but not designed in detail | Parked at #784, analytics-phase detail design |
| Chapter-rewrite assistance (mechanical briefing + Claude AI authoring) | Downstream of the change-flag mechanism | Parked at #784 |
| `prose_section_verse_link` | Named as the fix for the verse-grounding gap, not designed | Parked at #784 |
| The Concordance (5th book) | Two distinct sub-problems, base concordance already live, prose-integrated half genuinely open | Parked at #784 |
| Raw-material-visibility for writing | Named as an open thread, not designed | Parked at #784 |
| The book-2/book-3 boundary question | Real content sample already shows the current line doesn't hold; needs its own design pass | Parked at #784 |
| "Delete a section from an edit file" — silent no-op vs. refuse/warn/retire | A behavior/design decision, not a config-governance gap | Parked at #784 §6, explicitly not reopened by this proposal |

---

## 6. Sequencing (the "build per the plan" stage)

Once this whole document is approved, submitted in this fixed order (one `configmaint.propose`
pending at a time):

1. `cfg_prose` table creation + **4** rows (§4, component IV — was 3 rows in v4).
2. `cfg_enum` — `prose_section_status` (4 rows) + `prose_section_author` (3 rows).
3. `cfg_status_flow` — 4 rows, `entity='prose_section'`.
4. `cfg_behaviour_rule` — 3 rows, `class='sqlite'`.
5. `cfg_write_grant` — 2 rows, `database='bible_research'`.
6. `cfg_work_package` `prose` + 4 `cfg_step` rows.
7. `cfg_utility` — reactivate the 4 original scripts (`inactive: 1→0` + new `purpose` text).
8. Code change: `prosestore.py`'s hardcoded `CHAPTER_EDIT_OUT_DIR` constant replaced with
   `cfg.module_setting('cfg_prose', 'prose.edit_file_dir')`, read once per call rather than a
   module-level constant.

(Table creation and the `prosestore.py` code edit are migration/code steps, not
`configmaint.propose` rows, same as v4's own treatment of the `cfg_prose` table.)

---

## 7. Test plan (governance rule 46 — required, run after build, results go in the resolution)

Corrected for §2a, expanded for §2b. Changes from v4's 20 cases marked **[corrected]** / **[new]**.

| # | Function / operation | Test case | Expected |
|---|---|---|---|
| 1 | `prose.extract` | `--book Programme --also-markdown --also-docx --include-body` | JSON+MD+DOCX written, chapter names resolved from `cfg_prose` (not hardcoded) |
| 2 | `prose.extract` | omit `--book` | All books extracted |
| 3 | `prose.extract` | invalid `--book` value not in `book_stage_map` | Clean error, not a crash |
| 4 | `prose.search` | `grace` (plain text) | Results ≤ `prose.search_default_limit` when `--limit` omitted |
| 5 | `prose.search` | `--limit 3` | Exactly 3 shown, total count still reported |
| 6 | `prose.search` | `--fts "grace OR love"` | FTS5 expression path exercised, distinct from plain-text path |
| 7 | `prose.export_chapter` | `--book Programme --chapter 1` | Editable `.md` with `PROSE_SECTION_ID` markers, filename matches `{stem}-v{n}-{date}.md`, `n` reflecting the correct next edit-cycle version scanned across both the active dir and `{edit_file_dir}/archive/` **[corrected: filename shape now asserted]** |
| 8 | `prose.import_chapter` | unedited re-import of #7's output | **Refused outright** (`ValueError: ... nothing to import`), file left in place, **not** archived, **no** patch file written **[corrected: was "generates a no-op patch," now matches actual code]** |
| 8a | `prose.import_chapter` | edit exactly 1 of N bundled sections, re-import | Patch with exactly 1 `supersede` operation (only the changed section), file **archived** into `{edit_file_dir}/archive/`, `prose_section.source_file` on the new row points at the archived path, not the pre-move path **[new — confirms §2a's auto-archive + section-is-the-editing-unit behavior together]** |
| 9 | `prose.import_chapter` | edited body, missing a required marker | Clean validation error, not a crash |
| 9a | `prose.import_chapter` | hand-edited `CHAPTER_NO` marker (mismatch vs. DB) | Refused outright (`marker CHAPTER_NO changed: file=X, database=Y`), file untouched **[new — confirms the move/reorder-refusal path stays intact under this proposal, unchanged behavior]** |
| 9b | `prose.import_chapter` | a block with a fabricated `SECTION_ID` | Refused outright (`section N is not an active current prose row`), file untouched **[new — confirms the add-refusal path stays intact, unchanged]** |
| 10 | `Prose.ps1 -Step Extract/Search/ExportChapter/ImportChapter` | each of the 4, once | Dispatcher-driven run succeeds identically to the direct handler call (confirms component II's wiring) |
| 11 | `apply_session_patch.py`, `prose_section` `insert` | new row, `status='draft'` | Row created, `word_count` derived |
| 12 | `apply_session_patch.py`, `prose_section` `supersede` | supersede an existing row | New row v+1, old row's `superseded_by_id` set, old row content unchanged (immutability) |
| 13 | `apply_session_patch.py`, `prose_section` `approve` | approve a `draft` row | `status='approved'`, `approved_at`/`approved_by` stamped |
| 14 | `apply_session_patch.py`, `prose_section` `approve` | approve an already-`approved` row (idempotency) | No-op (`WHERE status != 'approved'` clause), not a duplicate stamp |
| 15 | `apply_session_patch.py`, `prose_section` `session_a_replace` | replace a `claude_code`-authored row | In-place update succeeds |
| 16 | `apply_session_patch.py`, `prose_section` `session_a_replace` | attempt on a `claude_ai`-authored row | `WHERE author='claude_code'` clause blocks it — 0 rows affected |
| 17 | `apply_session_patch.py`, `prose_section` `delete` | soft-delete a row | `delete_flagged=1`, row still present (no physical delete) |
| 18 | `apply_session_patch.py`, `prose_section` `bulk_supersede` | 2+ targets in one call | All targets superseded in one transaction, correct count in `counts` |
| 19 | `cfg_write_grant` (informational, not enforced until the §5-listed validator widening) | `Cfg.may_write('apply_session_patch', database='bible_research')` | Returns `{'prose_section', 'prose_section_type'}` |
| 19a | `cfg_prose` | `cfg.module_setting('cfg_prose', 'prose.edit_file_dir')` | Returns `"outputs/markdown/prose-edits"`, matching the current hardcoded value it replaces **[new]** |
| 20 | `configmaint.validate` full run | after all proposals applied | Clean — no new structural violations introduced |

22 cases (was 20 in v4: +1a, +9a, +9b, +19a; −1 test-8 rewritten rather than added). All run against
the live `bible_research.db`/`iba.db` (read-only where the operation itself is read-only; write
cases use throwaway test rows, cleaned up after, same discipline as escalation #795's own test
batch, `#815`–`#822`). Results — pass/fail per row, not a prose summary — go into #829's resolution
when this batch is submitted for final approval.

---

## 8. What I need from you

One decision, on the whole document — no partial go-ahead item-by-item (that pattern is exactly
what the new development cycle exists to stop):

1. **Approve this proposal as written** (§3–§7) — I submit the proposals in the fixed §6 order
   through `configmaint.propose`, make the one code change (§6.8), run all 22 test cases in §7, and
   bring the full results back in one resolution against #829.
2. Or **flag specific items to change first** — in particular §4's standing writer-grant decision
   (one `apply_session_patch` identity vs. six per-operation identities) is the one place this
   proposal makes a judgement call rather than applying an existing rule; everything else cites its
   governing rule directly.
