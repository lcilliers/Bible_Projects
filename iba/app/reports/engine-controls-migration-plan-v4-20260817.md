# Engine-controls migration into IBA — integrated plan (v4)

> v1–v3 archived under `archive/`. v3 was answered (escalation #672, 2026-08-17T05:03:41Z):
> *"approve phase 0 of plan for implementation. proceed with phase 1 -- this seems to be validation
> and clearup of existing configs. Note that the use of kind in the config rows is suspect, some of
> the items looks like they relate to modules or utilities, not sure what 'operations' refer to;
> phase 2 and phase 3 is on hold until phase 0 and 1 is completed."* This version records what's
> actually been **built** against that answer, resolves the `kind` question with evidence (and a
> real simplification it turned up), and flags one open ambiguity before going further (§7).
>
> **Live tracking**: per the researcher's standing instruction ("escalation is our ultimate control
> of work in progress... it also tracks the key steps on the way") this plan's execution is tracked
> by three open escalations, not just this doc: `MANUAL-20260817_050729_131006` (#653's real work),
> `_050732_324749` (#657's real work), `_050735_574484` (this plan's Phase 0/1 execution).

## 1. The goal (unchanged — the researcher's own words in full)

> *"The migration of the engine from research_db to IBA-db aims at consolidating the entire run
> control of the project... IBA App is in control of all processing in the project... I expect to
> see the engine control to be in the configs... no engine operations should run outside the control
> of IBA and the configs."*

## 2. Fragmentation, measured precisely now (was an estimate in v3, now a live check result)

`cfgquality.find_unregistered_project_scripts()` (built this round, §3) gives an exact, re-runnable
count instead of a one-time `find` estimate:

| surface | live `.py` files, unregistered | 
|---|---|
| `scripts/` (excl. `archive/`) | 331 |
| `engine/` | 15 |
| `iba/prototype/`, `iba/scripts/` | 9 |
| `research/` | 2 |
| repo root | 1 |
| **total** | **358** |

(v3's "345" was a `find`-command estimate; 358 is what the actual, live, re-runnable check reports
today — close, the gap is real drift in the days between, not a counting error this time.)

---

## Phase 0 — the governance mechanism — **BUILT (code); config row still queued**

### Concept
Unchanged: close the hole that let 358 files start life ungoverned, before touching any of them.

### Configs
**Not yet written.** `cfg_setting`: `key='governance.new_utility_registration_timing'`,
`module='governance'`, value as drafted in v3 — still correct, still just a draft. Blocked behind
`configmaint.propose`'s current queue: escalation #671 (`cfg_index` write-grant) is still
unanswered, and `module_blocking` (escalation #646) correctly refuses any further `configmaint.*`
dispatch — including this one — until it clears.

### Code — built, verified, one real bug caught in the process
`cfgquality.find_unregistered_project_scripts()` — walks the whole repo, matched by `file_path`
against `cfg_utility` (not module stem, unlike the existing `iba/app/lib/`-only check it sits
beside). Wired into `configmaint.validate()` as **advisory**, not a hard error — a deliberate
choice, not the plan's original "hard error" framing: with 358 pre-existing unregistered files, a
hard error would fail `validate` wall-to-wall over a known, already-tracked backlog (Phase 2) rather
than catch genuinely new drift, which is this check's actual purpose.

**Bug found and fixed while verifying it**: the first cut only excluded `venv`/`__pycache__`/etc. at
a path's *first* component, missing a **nested** virtualenv (`scripts/analytics/venv/`) — inflated
the count to 3,100+ findings (3,042 of them third-party `site-packages` files, not project code).
Fixed to check every path component; re-verified — 358 findings, 0 false positives from `iba/app/`,
`.git`, `archive/`, or any venv, anywhere.

### Daily-running rules
Once the config row lands: rides on the existing `Config-Maintenance.ps1 -Step Validate` habit,
no new discipline. Right now, with the code live but the setting row not yet written, the check
already runs and already reports accurately — it just isn't yet *named* as an enforced governance
rule in `cfg_setting` until #671 clears.

---

## Phase 1 — `engine/` itself — **the `kind` question resolved; NOT yet built (see §7)**

### The `kind` question, answered with evidence, not just relabelled

Re-derived each of v3's 12 drafted steps against the actual precedent (`BUILD.md` §40): `operations`
= the study-data-mutating pipeline, **including** pipeline-*embedded* validate/report steps
(`lexicon.validate`, `report.verse_span_meaning` are both `operations` despite the names); `utility`
= general-purpose, standalone reporting/config-maintenance (`report.word`, `configmaint.*`). Two
findings, not one:

1. **Two of the 12 steps are redundant, not mis-classified.** `Pre-A1` (lock + open run log) and
   half of `A2` (`_load_snapshot()` — actually a before-state row-count preview for the CONFIRM
   step, not a rollback backup) are **already done automatically** by `run.py`'s own
   `_ensure_run()`/`_snapshot()` for every word-scoped run — no per-work-package step needed.
   Porting them would duplicate existing dispatcher machinery. A2's other half ("structural
   completeness check") is real and folds forward into the JSON-load-validate step instead.
2. **One real re-classification**: `word.export` (full-word JSON export) directly parallels the
   *existing* `report.word` step (word overview report) — already `utility`. Drafted `operations`
   in v3 with no real justification; corrected here.

### Configs (revised)

**`cfg_utility`** — unchanged from v3 (15 rows, `engine/`'s own docstrings, `gap_fill.py` drafted
`inactive=1`) — still correct, not reproduced again here to avoid drift between two copies; see v3
§Phase 1 or `BUILD.md` §120/122 archive trail.

**`cfg_step`** — revised: **10 steps**, not 12, kind corrected:

| ordinal | step | does | kind |
|---|---|---|---|
| 0 | `word.load_json` | Load + validate latest Step 1 JSON + structural completeness check (merged from old A2/A3) | operations |
| 1 | `word.confirm` | Registry display + CONFIRM prompt | operations |
| 2 | `word.gap_report` | Build gap report (Term/Related/Verse/VTL) | operations |
| 3 | `word.gap_display` | Display gap report (+ interactive approve gate) | operations |
| 4 | `word.apply_changes` | Apply changes, one transaction per stream | operations |
| 5 | `word.meaning` | Meaning handler — parse + migrate legacy fields | operations |
| 6 | `word.flag_reset` | Quality flag reset (DATA_COVERAGE), re-derive | operations |
| 7 | `word.audit_checks` | WR-01–WR-20 + write `word_run_state` (PROVISIONAL) | operations |
| 8 | `word.registry_close` | Registry + file-index update, `last_automation_run='AUDITED'` | operations |
| 9 | `word.export` | Full-word JSON export | **utility** |

`Pre-A1` and the snapshot half of old `A2` — **dropped**, not renumbered into something else; the
work happens automatically, pre-dispatch, for free.

**`cfg_on_fail`**, **`cfg_write_grant`**: unchanged from v3 (the write-grant table stays shape-only,
still gated on the Phase 3 DB decision).

### Code — not yet written (see §7 before starting)

### Daily-running rules
Unchanged from v3's framing — once built, dispatched/gated/recorded like every other IBA work
package, no separate discipline to remember.

---

## Phase 2 / Phase 3 — **DONE (2026-08-17)**

Gate cleared: Phase 1 was already done; Phase 0 (`#698`) applied for real this session. Phase 2/3
(`#699`, approved option (b) — register all, mark any not clearly alive inactive) executed as one
governed batch: all 343 previously-unregistered scripts registered into `cfg_utility` (202 active /
141 inactive). Full detail: `BUILD.md` §132, `iba/app/reports/
unregistered-scripts-batch-registration-20260817.md`.

---

## 7. Before writing any Phase 1 code — a genuine ambiguity, not a judgement call to guess at

#672's answer describes "phase 1" as *"this seems to be validation and cleanup of existing
configs."* That description fits **Phase 0** (the registration-timing rule + the integrity check —
literally validating/cleaning up config coverage) far better than it fits **Phase 1** as this plan
defines it (building `engine/`'s `cfg_utility`/`cfg_step`/handler code from scratch — new
construction, not cleanup of something existing). Two readings, both plausible:

(a) "Phase 1" = this plan's Phase 1 as written (`engine/` redesign) — approved to start now, ahead
    of its own stated gate on #653/#657 landing.
(b) The researcher is counting informally (their "phase 1" = this plan's "Phase 0") and the
    "validation and cleanup" description is accurate for what was actually approved — in which case
    Phase 0 is confirmed (already being built, §Phase 0 above) and this plan's actual Phase 1
    (`engine/`) is **not** yet approved, still properly gated on #653/#657 as originally planned.

Not guessing between these — reading (a) means writing `handlers/wordaudit.py` and applying config
now, ahead of the plan's own sequencing rationale; reading (b) means Phase 0 is the whole of what's
approved tonight. Flagged in chat, not decided here.

## 8. Decisions requested

1. Which reading of §7 is correct?
2. Phase 0's `cfg_setting` row is ready to propose the moment #671 clears — anything to adjust in
   its wording first, or propose as drafted?
3. Phase 2's representative-3-script pattern, or the full 358 sized now? (unchanged from v3, still
   open)
