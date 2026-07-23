# Configuration-maintenance — the fundamental building block, layered (v1)

> **Status: Layer 1 BUILT and tested end-to-end, 2026-07-21.** `configuration-maintenance` is now a
> registered work package (`validate`/`propose`/`report`) exactly as designed in §2, with one addition
> found necessary during the build: a `cfg_change_detail` table for the row-level change log §2.2
> promised (the existing `cfg_change_log` had no columns to hold *what* changed — §2.5 below is updated
> to match what was actually built, not what was first drafted). Full build record: `GOVERNANCE.md` §5A,
> `BUILD.md` §2. Bootstrap script: `iba/app/migration/bootstrap_configuration_maintenance.py`. Tested:
> `validate` (clean pass against the live store), `report` (first `CONFIG-REPORT.md` ever generated),
> and `propose`'s full cycle (approve/reject/revise, insert/update/delete, write-grant and
> coherence-check rejections) via a harmless, fully-cleaned-up self-test row, both via the raw dispatcher
> and via `Config-Maintenance.ps1`.
>
> **Review pass, same day, before moving to `registry.create`'s fast-follow:** the researcher asked for
> three specific checks on `validate`. Two built and confirmed working (§2.2 code, tests in
> `GOVERNANCE.md` §5A): **(a)** `cfg_step.step` must be globally unique across every work package, not
> just within one (its PK is `(work_package, step)`, which would silently allow a collision —
> `escalation`/`cfg_on_fail` both match on `step` alone). **(b)** orphan-config detection — a `cfg_setting`
> key or `cfg_enum` group not referenced as a literal string anywhere in `iba/app/**/*.py`, surfaced as
> advisory (not a hard fail, since a config can be legitimately pre-staged for a not-yet-built step).
> Running (b) immediately found two real, pre-existing defects, unrelated to this build: `configmaint.
> report_path` itself was unused by `report()` (fixed in the same pass) and `passage.cross_chapter` is
> pure documentation — `handlers/passage.py` never reads it; "no cross-chapter" is hard-coded into the
> adjacency check instead, so changing that setting via `propose` would silently do nothing. **(c)** a
> "pre-approved list of configs" to validate against does **not** exist — `validate` only checks internal
> coherence, never conformance to an external allowlist; genuinely open, not built, pending the
> researcher's answer on what such a list should actually be.

---

## 1. The layered dependency map

```text
Layer 0  Irreducible bootstrap facts (stay in code — same class as book order / STEP's HTML shape)
           · DB path (iba/app/db/iba.db)
           · the cfg_* schema DDL itself (CFG_DDL in cfgload.py — can't be config; it creates the
             table that would hold it)
           · the SEED location for the very first load, before any cfg_* row exists to read it from

Layer 1  configuration_maintenance registered as a real work package        <- THIS DESIGN
           · validate → load → report, running through run.py like every other work package
           · its own config (cfg_setting under configmaint.*)
           · depends on: Layer 0 only

Layer 2  Hardening of configuration_maintenance itself (not built this pass — named, not silent)
           · enforce the exclusive-write-path (nothing but configmaint.load may touch cfg_* tables)
           · row-level change log (not just reload-level)
           · a reconcile step: diff live cfg_* content against the seed-of-record, flag drift
             (this is exactly what would have caught the stale 289-row cfg_candidate_rule)
           · depends on: Layer 1 existing and working

Layer 3  New utilities, registered the same way, each with its own config (rule e)
           · a naming-collision check (principle k) — plausibly a configmaint validate sub-check,
             or its own step; decide once Layer 1 exists to hang it off
           · git-ops, file-management, morphology-parser — separate work packages
           · depends on: Layer 1 (the registration PATTERN must exist and be proven first)

Layer 4  Content-level fixes — go THROUGH configuration_maintenance, not around it
           · reconcile/correct cfg_candidate_rule (the stale 289 rows)
           · confirm + apply the passage rule (your call, not built here)
           · depends on: Layer 1 (a working load/validate path) and ideally Layer 2's reconcile step
             (so "is the DB current vs. the seed" is answered by the utility, not by me querying by hand)
```

**Why this order:** every layer above 1 either produces config that must be loaded through a working
loader, or is itself a new registered utility that should follow the pattern Layer 1 establishes — proving
the pattern once, correctly, before repeating it for git-ops/file-management/morphology, is cheaper than
inventing the registration shape four times.

---

## 2. Layer 1, in full: `configuration-maintenance` as a registered work package

### 2.1 What "registered" means here, concretely (matching the existing 3 work packages exactly)

Today: `new-word` → `New-Word.ps1` → `run.py` steps `registry.exists/create`, `raw.discover/detail/
verses/write/validate`. Same shape proposed here:

| `cfg_work_package` | value |
|---|---|
| `name` | `configuration-maintenance` |
| `ps_script` | `Config-Maintenance.ps1` |
| `runs_over` | `none` — scope-less, like `set-candidates`'s seed step; `run.py`'s `_scope()` and `_ensure_run()` already handle empty scope (the comment in `run.py` literally says "skip for scope-less runs (e.g. seed refresh)") — confirmed by reading the code, not assumed. |

| `cfg_step` (ordinal, step, handler, scope, does) |
|---|
| 0 · `configmaint.validate` · `handlers.configmaint:validate` · none · "coherence-check the LIVE `cfg_*` tables as they stand right now (schema FKs, may_source, handler resolution, on_fail paths, status flow, regex, report fields) — read-only, runnable any time, no approval needed" |
| 1 · `configmaint.propose` · `handlers.configmaint:propose` · none · "the only path that may change a `cfg_*` row — see §2.2 for the approval-gated shape" |
| 2 · `configmaint.report` · `handlers.configmaint:report` · none · "regenerate `CONFIG-REPORT.md` from the live `cfg_*` tables — read-only, runnable any time; auto-chains after an approved `propose`" |

Each step is a thin wrapper `def h(ctx) -> Outcome` (the exact contract every other handler uses) around
the logic that **already exists and works** — `cfgcheck.check()`, `cfgload.load()`'s write phase,
`cfgreport.generate()` — not a rewrite. The point of Layer 1 isn't new logic; it's making the existing
logic **run through the same dispatcher, run-log, and escalation machinery every other module uses**,
instead of as three disconnected standalone scripts nothing else in the app knows about.

**Confirmed to fit the dispatcher without changes:** `Ctx` always constructs a `Step(cfg)` session, but I
read `stepapi.py`'s `Step.__init__` — it only reads config values, no network call. So a
`configuration-maintenance` run costs nothing extra and doesn't require STEP to be up, which matters
since config-maintenance must work even when STEP is down.

### 2.2 The new module: `handlers/configmaint.py` — DB-direct, approval-gated (resolved 2026-07-21)

**Three corrections folded in, all from you:**
1. No JSON file is the ongoing seed to reload from (the archived files are a one-time reference only,
   §2.3) — so `propose` is not "DROP and reload from a file."
2. **"DB-direct" does not mean unattended.** Your words: *"I want to validate and be involved in any
   updates to the configs... messing it up will seriously break everything."* Every change pauses for
   your explicit decision before it commits — reusing the escalation pattern proven in
   `handlers/registry.py`'s `create()` (check for an existing answer → if none, raise and pause →
   re-running the step after you answer resumes and acts on it). Not a new mechanism.
3. **The approval contract itself has two hard requirements (your standing rule, stated 2026-07-21):**
   *"the data presented to approve must be representative of what I need to approve... Approve / not
   approve / resubmit with an opportunity to provide a comment."* Concretely:
   - **Representative payload** — the escalation's `question`/`preset` must contain everything needed to
     actually judge *this specific* change, not a bare `old -> new` value diff. What "representative"
     means depends on the proposal: a `cfg_setting` scalar change may genuinely only need the value diff
     plus its `use` description; a `passage.*` rule change needs affected-passage examples and
     before/after stats attached; a `cfg_candidate_rule` batch needs the actual rows, not a count. This
     is built per proposal kind, not generically — flagged as real design work, not a detail.
   - **Three-way answer, not yes/no** — Approve / Not approve / **Resubmit with comment**. This is a
     schema change beyond what `escalation` has today (currently just an `answer` of yes/no, no comment
     field) — see the note below.

```
def validate(ctx) -> Outcome:
    # read-only coherence check of the LIVE cfg_* tables as they stand — cfgcheck.check()'s logic,
    # retargeted to query the DB instead of a JSON seed dict. No proposal involved; safe to run any time.

def propose(ctx) -> Outcome:
    # params describe ONE targeted change: Table, Op (insert/update/delete), Where (the row's natural
    # key), Set (column: new value), plus whatever REPRESENTATIVE context this proposal kind needs
    # attached (see above — built per kind, not generic).
    #   1. an existing answered escalation for this proposal?
    #        approve            -> write the single row, append a ROW-LEVEL cfg_change_log entry, ok()
    #        not-approve        -> fail("change-rejected", ...), nothing written, proposal closed
    #        resubmit + comment -> fail("needs-revision", message=comment, ...) — the proposer (Claude
    #                              Code or whoever raised it) must revise and call propose again; this is
    #                              feedback, not a rejection, and not auto-retried unattended
    #   2. no answer yet ->
    #        coherence-check the PROPOSED change (same checks as validate(), applied to the hypothetical
    #        post-change state) — fail immediately if incoherent, never escalate a proposal that's
    #        already wrong
    #        else escalate("needs-approval", question=<representative payload for this kind>, ...) — pause

def report(ctx) -> Outcome:
    # calls cfgreport.generate(); ok() with the output path — read-only, unaffected by the above
```

**Schema note (a real, small build item, not just a config row):** the `escalation` table needs a
`comment TEXT` column and its `answer` values need a third option (today: `yes`/`no`; needed: something
like `approve`/`reject`/`revise`). `escalation` is a *data* table, governed by `cfg_column` like any
other — so this is a normal schema addition through the existing mechanism, not a `cfg_*` config change.
Per your rule, it should apply everywhere `escalation` is used, including `registry.create`'s existing
new-word approval — not stay config-maintenance-only.

### 2.3 Its own config (rule e — every module has its own config)

New `cfg_setting` rows, namespace `configmaint.*`:

| key | value (proposed) | use |
|---|---|---|
| `configmaint.report_path` | `iba/app/config/CONFIG-REPORT.md` | where `report` writes the snapshot |
| `configmaint.auto_report` | `true` | whether an approved `propose` automatically chains to `report` (existing `cfg_on_fail` step-chaining — no new concept) |
| `configmaint.reference_seed_dir` | `iba/app/config/archive` | **reference only**, per [[project_iba_db_is_master_over_legacy_json_seeds]] — where a one-time completeness cross-check (Layer 2's reconcile step) looks for anything the live tables might be missing that's still relevant. Never read by `propose`; the DB is master, not this. |

**Built addition, not in the original draft:** a `cfg_change_detail` table — `run_id · table_name · op ·
where_json · set_json · before_json · applied_at`, one row per write `propose` actually applies. Needed
because `cfg_change_log`'s existing shape (`config_version · seed_hash · loaded_at · validated`) can only
say a reload happened, never *what* changed — and §2.2 always intended a genuine row-level record. A real,
small DATA table (registered via `cfg_table`/`cfg_column` like any other), not a `cfg_*` meta table.

### 2.4 What this resolves — BUILT, not just decided

**Built and tested:** the ongoing edit model is DB-direct, single-row, approval-gated — no file
round-trip, no silent write, ever. Confirmed working end-to-end (§ status header) for insert/update/
delete and all three answers (approve/reject/revise).

**Resolved during the build, not left as guesses:**
- `Where`/`Set` in `propose`'s params are plain JSON objects keyed by real column names — validated
  against `PRAGMA table_info(<table>)` at proposal time, so any `cfg_*` table's natural key (simple
  `key` for `cfg_setting`, composite `(work_package, step)` for `cfg_step`, etc.) is handled generically,
  no per-table special-casing needed.
- `validate`'s coherence checks and `propose`'s pre-write check share the same rule shapes (schema FK/
  enum/handler checks); `propose` currently runs a smaller, *targeted* subset for the specific
  high-risk tables (`cfg_on_fail`, `cfg_status_flow`) rather than a full hypothetical-post-change
  re-run of every `validate` rule — noted in code as a real limitation, not silently assumed complete.

### 2.5 What Layer 1 deliberately does NOT do (named, not silently dropped — carried to Layer 2)

- Does **not** technically *prevent* some other script from bypassing `propose` and writing `cfg_*`
  directly with raw SQL — `cfg_write_grant` now covers every `cfg_*` table for the `configmaint.propose`
  writer, but nothing stops a *different* piece of code from calling `sqlite3` directly. Layer 1 makes
  `propose` the one *sanctioned, approval-gated* path; hard technical enforcement (e.g. a DB-level
  trigger) is a harder, separate problem for Layer 2.
- Does **not** batch multiple related changes into one approval — every `propose` call is one row, one
  question. Whether a batch/transaction shape is ever needed is a Layer-2+ question, not assumed here.
- Does **not** run a *full* hypothetical-post-change validate on every proposal — only the targeted
  checks named in §2.4. A proposal that passes today's targeted checks but would break a rule
  `validate()` checks (and `propose` doesn't yet) is a real, named gap, not a false guarantee.
- Does **not** reconcile the live DB against anything (the stale 289-row `cfg_candidate_rule` case) —
  that needs its own reconcile step, deliberately deferred to Layer 2, itself routed through `propose`
  once it exists (a reconcile finding is just another proposal to approve, not a special case).
- Does **not** extend the three-way answer to `registry.create`'s existing word-approval — the schema
  now supports it (`escalation.comment` + the `escalation_answer` enum are general), but wiring
  `registry.create` to actually use `approve`/`reject`/`revise` instead of `yes`/`no` is a deliberate,
  separate fast-follow (`GOVERNANCE.md` §6).

---

## 3. Where this stands now — Layer 1 complete

Built, registered, and tested (status header). The step shape is `validate` / `propose` / `report` —
three steps, matching rule c's "tracks every change" (row-level, via `propose`'s `cfg_change_detail`
entry) and "restricts changes to go through it" (as the one sanctioned path; hard technical enforcement
is Layer 2, §2.5, named not built).

**Next, per the layer map (§1):** Layer 2 (hardening — enforcement, batching, full hypothetical-validate,
the reconcile step) or Layer 3 (new utilities following this same pattern — git-ops, file-management,
morphology-parser) or Layer 4 (route the actual passage-rule/candidate-rule content fixes through
`propose` now that it exists) — your call on which comes next.

**One thing worth confirming before I build:** is three steps the right scope for this first pass, or do
you want the reconcile-drift step (the one that would surface things like the stale 289-row
`cfg_candidate_rule`) pulled into Layer 1 now instead of waiting for Layer 2? Either way, once you say
go, I'll build exactly what's in §2 — the handler module, the `cfg_work_package`/`cfg_step`/`cfg_setting`
seed rows, and the PS wrapper — and nothing beyond it in this pass.
