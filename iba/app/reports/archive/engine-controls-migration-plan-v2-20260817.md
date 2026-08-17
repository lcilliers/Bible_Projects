# Engine-controls migration into IBA — architecture plan (v2)

> v1: `iba/app/reports/archive/engine-controls-migration-plan-20260817.md`. Answered **revise**
> (escalation #669, 2026-08-17T04:17:48Z): *"the plan as stated is moving in the right direction,
> but I am not convinced it was holistically planned and structured. The plan is not only about a
> catalog of what has happened in the past, it should also cater for what is intended, through IBA
> process control, to happen in the future... the engine should cope with the fact that the project
> is changing... rather than silently ignore it."* v1 inventoried `engine/` and proposed porting
> it — this version starts from the goal instead, per the researcher's comments in full:
> `Workflow/Chat_responses/Comments - engine migration 2026-08-17`.

## 1. The actual goal (the researcher's own words, in full)

> *"The migration of the engine from research_db to IBA-db aims at consolidating the entire run
> control of the project and ensuring that the disciplines and structure of the research_db engine
> control is not neglected or lost. With the advent of IBA-db the run controls are fragmented and
> incomplete. A single and complete set of rules should apply for all engine activity. All engine
> activity across the whole project must consistently be captured. In terms of project governance,
> IBA App is in control of all processing in the project. Therefore, I expect to see the engine
> control to be in the configs, the governing principles captured in configs, the rules, tables,
> and everything else to be captured in configs. All routines should enforce the configs, and no
> engine operations should run outside the control of IBA and the configs."*

So this is not "retire `engine/`, keep IBA" — it's **one governed control plane for every operation
in the whole project**, present and future, with `engine/`'s own discipline (audit checks, lock/backup
safety, version gating) carried forward into it rather than dropped. `governance.scope_iba_app`
("IBA App is the central process control mechanism for all operations in the entire project") and
`governance.project_change_rule` ("any operation defined in the past that is not in the IBA app
must be migrated to the app") already state this as policy — this plan is how it actually happens.

## 2. The real size of the fragmentation (measured, not assumed)

Not just `engine/`. A live count, this session:

| surface | live `.py` files | registered in `cfg_utility`? |
|---|---|---|
| `iba/app/` | (the governed core — libs, handlers, tools, migrations) | yes, 33 modules |
| `engine/` | 11 | no |
| `scripts/` (excl. `archive/`) | ~390 top-level + subfolders | no |
| `research/`, `iba/prototype/`, `iba/scripts/`, repo-root loose scripts | ~15 | no |
| **total outside `iba/app/`+`engine/`+`archive/`** | **345** | **no** |

That 345 is the actual scale of "fragmented and incomplete" — `CLAUDE.md` §6 already sorts
`scripts/` by *prefix convention* (`_apply_*` mutates, `_check_*` is read-only, `_delete_*` is
destructive) but that convention is enforced by nobody — it's a naming discipline, not a config
row, not a write-grant, not a dispatch gate. Exactly the gap `governance.rules_must_be_config_driven`
names in general and this plan must close for engine-shaped activity specifically.

This is also **escalation #648's own scope** ("project-wide config-driven-rule sweep... on hold
until further instruction") — the researcher's comments here read as that instruction. Not
resumed unilaterally; flagged for a decision (§6).

## 3. What "capturing engine activity as it emerges" requires (the forward-looking half v1 lacked)

v1 only asked "how do we port what exists." The researcher's correction is that the plan must also
answer: **when someone (researcher or Claude) writes the next new operation next month, what stops
it from starting life ungoverned, the way all 345 files above did?** Proposed mechanism, mirroring
patterns already proven inside `iba/app/` itself:

- **A standing governance rule** (new `cfg_setting`, module `governance`, proposed for approval
  like every other row in that module): *any new script/routine, anywhere in the project, must be
  registered in `cfg_utility` (and, if it runs data-changing steps, `cfg_step`/`cfg_write_grant`)
  in the same unit of work it is created* — the identical "same unit of work" shape as
  `governance.build_md_on_code_change`, extended past `iba/app/**` to the whole project.
- **A self-checking integrity check**, same shape as the write-grant-coverage check just built for
  escalation #657 (`cfgquality.find_cfg_tables_missing_configmaint_grant`, `BUILD.md` §120): a
  companion `find_unregistered_project_scripts()` that walks the repo for `.py`/`.ps1` files outside
  `iba/app/` and flags any not present in `cfg_utility` — run as part of `configmaint.validate`, so
  drift is a hard-error finding, not a thing that has to be rediscovered by a full sweep again in
  six months. This is the concrete answer to "cope with the project changing... rather than
  silently ignore it."
- **One dispatcher.** `run.py`'s model (cfg-declared steps, `cfg_write_grant`-checked writes,
  escalation-gated pauses, the `module_blocking` gate just built) is already the pattern the
  researcher is describing — the plan is to extend its *reach*, not invent a second one.

## 4. The open question this plan does NOT decide: one DB or two, governed either way

The researcher was explicit this is undecided: *"I am not sure what would work best, if the tables
should be consolidated into a single DB, or if the rules can be clear and precise so that the
current tables can continue to operate without confusion, neglect or duplication."* Laid out
plainly, not pre-empted:

| | consolidate into one DB (`iba.db`) | keep two DBs, config-precise ownership |
|---|---|---|
| **for** | removes cross-DB reference friction entirely; "one set of rules" is literally true, not just procedurally true | avoids a ~766 MB physical migration and its own risk (this project already lost 6 weeks once to a DB-corruption incident, `wa-db-loss-incident-20260603.md`); `bible_research.db`'s prose/findings shape is genuinely different data from `iba.db`'s process-control/base-data shape |
| **against** | large, risky, one-way migration of live research data; blurs `governance.scope_research_db` vs `governance.scope_iba_db`'s current clean split | requires real discipline (cfg_table/cfg_column coverage across BOTH DBs, checked, not just documented) to avoid exactly the "confusion, neglect, duplication" the researcher is worried about |
| **already gated on** | #653 (research_db table disposition) + #657 (design audit) — both explicitly sequence before this question is even askable with real information | same |

This plan's position: **don't decide this now.** Build the governance mechanism in §3 first (works
identically either way — a `cfg_utility` row and a write-grant don't care which physical file the
table lives in), let #653/#657 finish surfacing which `bible_research.db` tables are actually
base-data-vs-findings, and revisit the one-DB-vs-two question with that evidence in hand rather than
as a guess now.

## 5. Revised phases

1. **Governance mechanism first** (§3) — the standing rule + the unregistered-script integrity
   check. Doesn't touch `engine/` or `bible_research.db` at all; makes the *next* piece of drift
   impossible while the rest of this plan executes. Smallest, safest, most leveraged first step.
2. **`engine/` itself**, once #653/#657 land (unchanged from v1's reasoning, restated): retire
   `gap_fill.py` outright (already superseded); fold `constants.py` thresholds into `cfg_setting`;
   redesign (not port) `audit.py`'s 20 `WR-*` checks (WR-01–WR-20, confirmed by distinct code, not
   grep line-count — v1's "47" was a miscount, `grep -c` over total line-matches rather than
   distinct `WR-NN` codes; `CLAUDE.md` §4's "WR-01..WR-20" was right all along, no correction needed
   there) against whichever tables #653 confirms persist;
   retire the standalone `python -m engine.engine` CLI once the above land, in favour of `run.py`.
3. **`scripts/`'s ~390 files**, triaged by `CLAUDE.md` §6's existing prefix convention as a first
   pass (read-only diagnostics register cheaply; `_apply_*`/`_delete_*` mutating ones get the full
   redesign-not-port treatment per escalation #656's standing rule) — the single largest piece of
   "fragmented and incomplete," sized here (345 files) for the first time, not yet phased in detail;
   that detail is its own follow-up plan once phase 1 (§3's mechanism) exists to register them into.
4. **The one-DB-vs-two decision** (§4), revisited with #653/#657's findings once available — not
   before.

## 6. Decisions requested

- Approve phase 1 (§3's governance mechanism) to start now, independent of #653/#657?
- Is this plan's reading correct that the researcher's comments here effectively supersede #648's
  "on hold until further instruction," or should #648 stay separately gated?
- Confirm §4's "don't decide DB consolidation yet" stance, or state a preference now.
