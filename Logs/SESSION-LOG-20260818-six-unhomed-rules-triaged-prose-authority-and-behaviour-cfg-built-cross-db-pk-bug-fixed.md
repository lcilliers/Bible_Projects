# SESSION LOG — 2026-08-18 — six unhomed `wa_rule_registry` principles triaged into two new cfg mechanisms (prose-canonical-authority, operational-behaviour rules), which surfaced and fixed a real cross-database compound-PK registration bug

Opened on `start-project` — clean git state, STEP already up, IBA `READY`. Governance-alignment
register showed row 5 (`wa_rule_registry`/`Workflow/Global_rules/*` vs. `GOVERNANCE.md`) resolved
in principle but with an open note: six specific principle-rules (`GR-DB-001`, `GR-REF-001`,
`GR-PROC-001`, `GR-PROG-001`/`002`/`009`) had no `cfg_*` home anywhere after the table's blanket
retirement. This session closed that gap, and the work it triggered kept surfacing real, unrelated
defects the closer it looked.

## 1. The six unhomed rules, triaged and paired into two new escalations

Read each rule's actual text (not summarised from memory), then paired by kind rather than fixed
individually:

- **`GR-PROG-001`** (verse always leads) reframed, on the researcher's direction, as "the programme
  prose is the project's canonical authority" — parked as escalation `#714`, a six-part instruction
  (a–f: governance anchor, a new `cfg_*` prose table, `cfg_table`/`cfg_column` registration, a
  chapters-4–6 alignment item, deriving pointer-configs for chapters 0–3, methodology-change
  flagging).
- **`GR-PROG-002`** (the governing question) — researcher decision, addendum to `#714`: superseded
  by the prose entirely, every reference to be replaced with a pointer once the prose mechanism
  exists. 26-file reference sweep scoped (mostly historical/archive; 6 live files flagged, not yet
  edited).
- **`GR-DB-001`/`GR-PROC-001`/`GR-REF-001`** — genuine operational-behaviour rules (not research
  content), paired into a new escalation `#715`: a project-wide `cfg_behaviour_class`/
  `cfg_behaviour_rule` mechanism (chat/terminal/sqlite/documentation classes), replacing the
  "guides scattered across USER-GUIDE/GOVERNANCE/BUILD/README/CLAUDE.md" problem the researcher
  named directly.
- **`GR-PROG-009`** (inferential vs. confirmed) — reframed by the researcher as the general
  API/LLM-use discipline rule. Recommended (not decided unilaterally) as a fourth peer class,
  `llm_output`, inside the same `#715` mechanism rather than nested under `chat` or a separate
  table — approved as given.

Both escalations' full instructions and reasoning filed as living plan docs (`gr-prog-001-prose-
canonical-authority-plan-20260818.md`, `operational-behaviour-rules-cfg-plan-20260818.md`) so
nothing survived only in chat.

## 2. `#715` cycle 1 — the operational-behaviour cfg layer, built

Researcher's detailed comments (`Workflow/Chat_responses/comments-operational-behaviour-plan`):
proceed; **scope is project-wide, not `iba/app/**` only**; start with the obvious ones, clear them,
then work everything else in later cycles; rule text must be definitive, not interpretive; no rule
lives in both a document and `cfg_*` at once; deviation must eventually be monitored, not just
documented.

Built (`bootstrap_behaviour_rules_v1_20260818.py`): `cfg_behaviour_class` + `cfg_behaviour_rule`
tables; `governance.operational_behaviour_control` anchor; five classes (`chat` seeded
deliberately empty — its real content needs a separate `CLAUDE.md`/memory audit, not guessed);
four rules seeded, the direct successors of `GR-DB-001`/`GR-PROC-001`/`GR-REF-001`/`GR-PROG-009`.

## 3. `#712` finished, and the compound-PK cascade it surfaced across BOTH databases

Separately, `#712` (`configmaint.propose`'s hardcoded `CFG_TABLES` allowlist — 6 tables missing
the day before) had a deferred two-part follow-on. Researcher: *"first complete #712, then we can
get back to the sweep for #715."*

- **Part 1:** backfilled all 20 foundational `cfg_*` tables into `cfg_table`/`cfg_column`
  (`backfill_foundational_cfg_tables_v1_20260818.py`) — 29/29 registered.
- **Part 2:** `CFG_TABLES` retired; `_known_cfg_tables(conn)` derives it live from `cfg_table`.

Running `configmaint.validate` to check part 2 hard-failed: 11 of the just-backfilled tables had a
genuine compound physical primary key, registered truthfully — and truthfully was itself the bug.
Checked `lib/db.py` directly: `_col_ddl()` emits an invalid multi-column inline `PRIMARY KEY` for
more than one `is_pk=1` column (SQLite only allows one); `Db.upsert()`'s dedup key breaks the same
way. Not a false-positive check — a real latent defect the backfill had just introduced.

**Researcher's direct challenge** ("I would expect another flag to appear because
bible_research_db definitely have multiple FKs... if this is about more than cfg.* related
indexes") found the identical pattern in **7 `bible_research.db` tables**, invisible because
`_validate_live` hardcoded `database='iba'` throughout — and, one layer deeper, because the
checker meant to enforce `governance.rules_must_be_config_driven` was itself not config-driven
about which database(s) to check (no `cfg_enum` named the project's databases;
`governance.project_databases` was prose, not queryable).

Raised as three separate escalations (`#721`/`#722`/`#723`) rather than fixed inline — researcher:
several distinct focus areas. All approved, then built:

- `cfg_unique` widened with a `database` column (`add_cfg_unique_database_column_v1_20260818.py`),
  same precedent as `cfg_table`/`cfg_write_grant`'s prior widenings — needed because both
  databases can now register `cfg_unique` rows for shared table names (`passage` already existed).
  `Cfg.unique_key()` fixed to filter by it (was missing the filter entirely).
- `cfg_enum project_database` (`iba`, `bible_research`) + `database.iba.path`/
  `database.bible_research.path` settings (`bootstrap_project_database_enum_v1_20260818.py`) —
  the researcher's own refinement of the design, naming convention matched to existing
  `<module>.<key>` settings.
- `_validate_live` rewritten to loop over `cfg_enum project_database` instead of one hardcoded
  database — structurally closes the `bible_research.db` blind spot, not a hand-maintained twin.
- `fix_compound_pk_registration_v1_20260818.py` — `is_pk=0` + correctly-ordered `cfg_unique` rows
  for all 19 affected tables (12 `iba.db` + 7 `bible_research.db`); `cfg_index`'s own 2026-08-07
  half-fix (missing its `cfg_unique` backing) closed at the same time.

Verified end to end: `_validate_live` direct call → 0 errors; `Cfg.unique_key()` spot-checked
correct for all 12 `iba.db` tables; real dispatcher run clean. `#712`/`#721`/`#722`/`#723` all
marked complete.

## 4. `#715` cycle 2 — `Workflow/*` survey, then 11 more rules

Per the researcher's own sequencing, surveyed `Workflow/*` before writing more content. Found
`Workflow/Claude_API/`, `Workflow/SQLite/`, `Workflow/Obsidian/` (all 2026-08-15, never in
`CLAUDE.md`) — live, current, unclaimed rule content, not failed attempts. The actual failed
prior attempt was `wa_rule_registry` itself (confirmed via session-log search) — the lesson taken:
a rules table without a live enforcement mechanism tends to rot, regardless of how well-intentioned
it started.

`bootstrap_behaviour_rules_cycle2_v1_20260818.py` — 11 rules seeded: 6 `llm_output` (from the
Claude-API guide — SDK-dependency decision, no hardcoded call params, cost-cap gate, usage
logging, Sonnet-5 default, never expose the API key), 4 `sqlite` (read-only default, never write
via an ad-hoc tool, don't assume which database, query-file conventions), 1 `documentation` (an
Obsidian-edited copy is never authoritative). `chat` still empty.

## 5. `#714` executed (parts a/b/c/e)

`bootstrap_prose_authority_v1_20260818.py`: `governance.prose_canonical_authority` anchor;
`cfg_prose_chapter` (7 chapters — 0–3 reviewed/final per the researcher's direct statement, 4–6
flagged `not_yet_aligned`, NOT re-derived from the prose extract's own stale per-section `draft`
metadata); `cfg_prose_concept` — a pointer index, not a copy — `verse_primacy`/
`inner_being_definition` both resolve to chapter 1, direct successors of `GR-PROG-001`/
`GR-PROG-002`. Part (d) escalated separately (`#725`, chapters 4–6 alignment, not started —
researcher's guidance on it: expect discrepancies vs. `GOVERNANCE.md`/`CLAUDE.md`, include root
`README.md` too). Part (f)'s principle is stated in the anchor setting; the flagging mechanism
itself isn't built.

## 6. The rules overview — `iba/app/reports/cfg-rules-overview-20260818.md`

Requested as a five-part narrative: how the project starts up (`init.py`'s 7-step sequence), how
the interfaces behave (the 5 behaviour classes), how the environment is governed (the propose→
validate→escalate→apply loop, the 7 `cfg_escalation` rules), what the project is built on (the
two-database split, the prose authority, the three programme stages), and how the working elements
behave (27 work packages, 55 steps, 37 method rules, 17 quality checks, failure routing). Written
from live queries throughout, gaps stated plainly rather than smoothed over.

## 7. `#727` — genuine orphans actually fixed, not noted again

Researcher, on a recurring advisory escalation this session had repeatedly closed `noted` without
addressing: *"this need your attention, a few missing strings still."* Three real orphans,
root-caused:

- `prose_chapter_status` enum — a real gap in this session's own `#714` work (created, never
  checked against). Fixed: `_validate_live` gained the check, same shape as the existing
  `word_status` one.
- `database.iba.path`/`database.bible_research.path` — `Cfg.database_path(name)` is their real
  consumer, wired into `init.py`'s startup sequence as a live path-drift check. Verified live.
  Both still *show* as orphans in the automated report — checked why: the checker's same-file-
  literal-match heuristic can't see a key built via f-string interpolation. Documented as a known
  false positive rather than degrading the code to satisfy the scanner.
- The stale-`GOVERNANCE.md` flag riding alongside `#727` was checked and found to be an unrelated
  false alarm (the flagged change was a routine content insert, not a rule change) — but surfaced
  a real, accumulated gap anyway: this session's actual governance-*mechanism* changes had only
  been recorded in `BUILD.md`. Closed as `GOVERNANCE.md` §40.

## Escalations touched this session

Raised: `#714`, `#715`, `#721`, `#722`, `#723`, `#725`. Closed/completed: `#712`, `#714` (parts
a/b/c/e — d still open as `#725`), `#715` (2 cycles in, more remain), `#716`–`#720`, `#721`,
`#722`, `#723`, `#724`, `#726`, `#727`, `#728`. Still open: `#715` (cycles 3+), `#725` (not
started).

**Files:** `iba/app/migration/{bootstrap_behaviour_rules_v1_20260818,
bootstrap_behaviour_rules_cycle2_v1_20260818, bootstrap_prose_authority_v1_20260818,
backfill_foundational_cfg_tables_v1_20260818, add_cfg_unique_database_column_v1_20260818,
bootstrap_project_database_enum_v1_20260818, fix_compound_pk_registration_v1_20260818,
fix_missing_write_grants_v1_20260818}.py`, `iba/app/handlers/configmaint.py`, `iba/app/lib/cfg.py`,
`iba/app/lib/cfgquality.py`, `iba/app/init.py`, `iba/app/BUILD.md` (§§145–148),
`iba/app/GOVERNANCE.md` (§40), `iba/app/reports/{gr-prog-001-prose-canonical-authority-plan,
operational-behaviour-rules-cfg-plan, cfg-pk-registration-and-validator-scoping-plan,
cfg-rules-overview}-20260818.md`.
