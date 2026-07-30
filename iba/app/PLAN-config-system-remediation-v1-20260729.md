# PLAN — config-system remediation: from the current hodgepodge to the system expected from the start

**Status (updated 2026-07-29, same day):** Phase 1 implemented (code fixes verified, 19 `cfg_*`
proposals raised and PAUSED awaiting researcher decision — `Escalation.ps1 -Action List`); Phase 3
partially implemented (2 new hard checks + 2 new advisory checks live in `configmaint.validate`,
verified against the real dispatcher). Phase 2 (runtime `inactive` enforcement) and Phase 4 (utility
registry) deliberately deferred — see `BUILD.md` §37 for the full account and reasons. A DB
snapshot (`iba/app/db/snapshots/iba-20260729T153836Z-pre-config-remediation-plan-20260729.db`,
`keep=999`) and clean git HEAD (`2125addd`) were the fallback in place before any change started.
**Supersedes nothing; extends** `PLAN-reports-config-governance-v1-20260722.md` (that plan built the
report-config bundle; this one covers everything it didn't).
**Sourced from:** live inspection of `iba.db`, `lib/cfg.py`, `handlers/configmaint.py`,
`lib/cfgquality.py`, `lib/valuequality.py`, `run.py`, `GOVERNANCE.md` (full, 1162 lines), `BUILD.md`
(§9-36), `USER-GUIDE.md`, and the four reports already filed this session
(`passage-rules-audit-20260729.md`, `passage-config-full-extract-20260729.md`,
`configmaint-validate-coverage-20260729.md`, `configmaint-validate-gap-analysis-20260729.md`,
`config-expectations-vs-documented-history-20260729.md`). Every finding below was re-verified
directly against the live DB/code while writing this plan — not carried over by assumption.

---

## PART A — Comprehensive findings (the full review, app-wide, not passage-only)

The earlier gap analysis used the passage configs as the worked example. This section re-runs the
same lens across the **whole** app to confirm the passage hodgepodge is a symptom, not the disease,
and to make sure nothing is left for "later."

### A1. ROOT CAUSE — `inactive` has no runtime effect anywhere. It is validator-only metadata.

Checked directly: `iba/app/lib/cfg.py` — the **only** class the running app uses to read config —
contains the string `inactive` **zero times**. Every one of its 14 read methods (`setting`, `enum`,
`tables`, `columns`, `unique_key`, `connection`, `route`, `may_write`, `sequence`, `step`,
`is_chained`, `book_order`, `candidate_rules`, `on_fail`) returns whatever is in the table,
active or not. `run.py`'s dispatcher calls `cfg.step()` directly with no filter of its own either
(already the substance of open escalation #334).

**This is the mechanism behind almost every other finding below.** "Retiring" a `cfg_*` row today
means exactly one thing: it stops showing up as compliant in `configmaint.validate`'s own report.
It does **not** stop the row from being read and applied by any code that calls for it. The whole
`inactive` mechanism (`GOVERNANCE.md` §15D, 2026-07-23) was built, in its own words, to let
`configmaint.validate` "exclude inactive configs from validation" — and it does exactly that and
**only** that. Whether a retired mechanism actually stops running was never addressed, and §15D says
so honestly: *"Blocking execution outright is a different, not-yet-made decision."*

### A2. Stale `filled_by` — not a passage-only defect. 21 columns across 2 retired modules.

Queried live across the **whole** `cfg_column` table (not scoped to `passage`):

| table | columns affected | `filled_by` (all inactive steps) |
|---|---|---|
| `candidate_seed` | `decision`, `layer`, `registry_match`, `tag`, `assessed_at` | `candidate.seed` |
| `candidate_seed` | `sense_seq`, `step_status`, `ib_referent_type` | `candidate.load` |
| `span_candidate` | `seed_source`, `set_at` | `candidate.set` |
| `passage` | `start_chapter`, `start_verse`, `end_chapter`, `end_verse`, `ref`, `verse_count`, `rule`, `source`, `needs_review`, `created_at` | `passage.build` |
| `verse_passage` | `is_anchor`, `created_at` | `passage.build` |

The candidate system was retracted 2026-07-23 (`GOVERNANCE.md` §15D); the passage system 2026-07-26
(`BUILD.md` §23). **Neither retraction touched `cfg_column`.** This is a systemic gap in the
retraction *procedure* itself, not something specific to how the passage retraction was done.

### A3. Enum staleness — the candidate retraction did this correctly; the passage retraction didn't.

| enum group | inactive members | still referenced by an active column? |
|---|---|---|
| `candidate_decision` / `candidate_source` / `candidate_step_status` / `candidate_ib_referent` | **all 15 values, correctly `inactive=1`** | no — retracted alongside the columns |
| `passage_rule` / `passage_source` | **0 of 4 values inactive — still fully active** | `passage.rule`/`passage.source` (the exact columns in A2, populated by nothing) |
| `passage_debate_status` | 0 inactive (correct — this one IS live, used by `report.passage_debate`) | yes, genuinely |

The same author, applying the same retraction pattern twice six days apart
(`migration/retract_candidate_system.py` → `migration/retract_passage_system.py`), did the enum
half correctly the first time and missed it the second time. This is a **process-consistency**
finding, not a one-off oversight — the retraction procedure has no checklist that would have caught
either the `cfg_column` gap (A2) or this one.

### A4. Code-side fallback defaults silently drifting from the DB's real, active value.

Every `cfg.setting(key, <literal>)` call site in the app (30 found by direct grep) was compared
against its own key's live DB value. 28 match or are dormant (inactive). **Two are live,
active, and wrong:**

| key | code fallback (`lib/stepapi.py`) | DB value (active) | consequence if the row were ever deleted |
|---|---|---|---|
| `step.expect_min_verses` | `1` | `1000` | the STEP health-probe's "server returned a real answer" test would silently accept 1 verse instead of 1000 |
| `step.expect_gloss_contains` | `""` | `"God"` | same probe's gloss-sanity check would silently accept any/no gloss |

Both are the STEP-up health probe verified at this session's `Start-Iba.ps1` ("2088 verses" for
H0430 — clears 1000, contains "God"). The probe works today only because the DB rows exist; nothing
would notice if they didn't, because the code's own fallback silently defeats the check it's a
fallback *for*.

### A5. A known, already-documented "one rule, two homes" duplication, never closed.

`GOVERNANCE.md` §5 (2026-07-22, still current — nothing since has touched this): `handlers/raw.py`'s
hardcoded `BASE_RE` pattern (`^([HG]\d+)([A-Z]?)$`) is the **identical** pattern to
`cfg_setting candidate.lemma_base_pattern` — one fact expressed twice, once in code (still live,
`raw` module) and once in config (now `inactive=1`, retracted `candidate` module). Named in writing
7 days ago as a defect ("Not fixed in this pass — named here so it doesn't hide"). Still not fixed.

### A6. Cross-reference completeness — only 1 of at least 4 reference types is checked.

| reference | checked by `configmaint.validate`? | live result if checked now |
|---|---|---|
| `cfg_on_fail.step` → `cfg_step.step` | **yes** (existing check #8) | clean |
| `cfg_report_section.step` / `cfg_report_csv_table.step` → `cfg_step.step` | no | clean today, by luck |
| `cfg_write_grant.writer` → `cfg_step.step` (or a declared exception) | no | 6 of 13 active writers aren't steps (`call1_meanings`, `call2_getInfo`, `call3_strong`, `escalation`, `migration`, `run`) — legitimate by convention, but nothing distinguishes that from a typo |
| `cfg_column.filled_by` → `cfg_step.inactive` | no | **21 violations, A2** |

### A7. Config-bundle completeness — counted app-wide, not passage-scoped.

- **11 active steps have zero `cfg_on_fail` rows**: `raw.write`, `configmaint.report`,
  `validation.word`, `validation.book`, `retention.report`, `table.export`, `report.strong_meaning`,
  `report.span_analysis`, `report.schema_overview`, `report.registry`, `lexicon.parse`.
- **6 active data-writing steps have no `cfg_report` row**: `configmaint.propose`, `lexicon.parse`,
  `lexicon.related`, `raw.validate`, `raw.write`, `registry.create`.
- Neither list distinguishes "genuinely doesn't need one" from "was missed" — nothing in the schema
  records that decision either way.

### A8. Hardcoded logic that should be config, beyond the passage example.

- `run.py:28` — `PATH_EXIT` dict (path → process exit code), hardcoded, never sourced from config.
- `lib/cfgquality.py`'s own `REPORT_STEPS`, `QUALITY_CHECK_REPORT_PATH`, `MODULE_DEDICATED_TABLE` —
  the validator's definition of "what should be configured" is itself hardcoded Python, disconnected
  from `cfg_step`/`cfg_write_grant` (the module's own docstrings say so).
- A5 above (raw.py `BASE_RE`).

### A9. No utility-routine registry exists at all.

`cfg_step` (+ `REPORT_STEPS`) covers *steps* — things `run.py` dispatches to. Library code
(`lib/stepapi.py`, `lib/words.py`, `lib/reportkit.py`, `lib/cfgquality.py`, `lib/valuequality.py`,
`lib/passagetrack.py`, etc.) reads `cfg.setting()` ad hoc with **no equivalent registry** to check
completeness against — this expectation ((d) in the researcher's list) currently has no config
category to attach to.

### A10. Documentation currency — the project's own rule, not honoured for 3 days of real work.

`GOVERNANCE.md §8`'s own standing rule (LIVE `cfg_setting` rows, escalations #238/#239): any
config-rule change → `GOVERNANCE.md` updated, same unit of work. `GOVERNANCE.md`'s last section
(§16) is dated 2026-07-26, *before* that day's own passage retirement (§23 in `BUILD.md`). **At
least 7 `BUILD.md` sections since then are real `cfg_*` rule changes with no `GOVERNANCE.md`
counterpart**: §23 (passage retirement), §27 (`report.passage_debate` registered), §28 (passage
tables repurposed, new write grants), §31 (`passage-quality` reactivated), §32
(`report.whole_book_read` registered), §35 (`governance.verse_gap_by_design` inserted), §36 (a
`passage` data correction). `USER-GUIDE.md` §8 still shows the retired `passage.build` as live
example output.

### A11. `configmaint.validate` confirmed clean today (0 hard errors, 0 orphans, 0 justifications) despite A1-A10 all being true, live, right now.

Already established in `configmaint-validate-gap-analysis-20260729.md` and re-confirmed while
building this plan. The validator checks structure exclusively; nothing above is a structural
break by its current definition of "coherent."

### A12-A16 — Core, ACTIVE modules, not just the retired ones (added after review — see full detail in `core-module-config-intent-vs-effect-20260729.md`)

A1-A11 above were drawn entirely from cross-cutting infrastructure and the two **retired** modules
(candidate, passage-build). Asked directly — for every config, what does it *intend*, does it
*actually do that*, is it *effective*, and is the config *complete* (does it control everything
we'd expect it to) — across every **active, currently-used** module, the same two failure classes
recur, worse in some cases because these modules run every session:

- **A12 — a setting that is read but does nothing.** `discovery.follow_related` (module `raw`):
  `handlers/raw.py:79-80` reads it, then does `if true: pass  # would expand here`. Flipping it via
  `configmaint.propose` changes *nothing* — the expansion logic was never built. This passes every
  existing check (the key literal sits next to a `.setting(` call) while failing the actual "is it
  effective" test.
- **A13 — a whole rule-set governing an active module with almost no config.** `lexicon.parse`/
  `lexicon.related` (run regularly, feed `raw.backfill_meaning` directly) are driven by
  `lib/lexiconparse.py`, which has **zero** `cfg.setting()` calls — six regexes and a hardcoded
  tag-set decide the entire parse. The module's whole config footprint is one report-path setting.
- **A14 — the pass/fail criterion for a live check is hardcoded, not config.** `handlers/
  narrative.py`'s `REQUIRED_LABELS` (the three channel names the scope-check enforces) is a Python
  tuple; `handlers/registry.py`'s `BUILT` status set and its 100%-shared-strongs duplicate-warning
  threshold are likewise hardcoded, despite `cfg_status_flow` existing for exactly the first case.
- **A15 — a live write/read coherence gap in the method actually in use right now.**
  `report.passage_debate` writes section headings from `cfg_report_section.heading`;
  `report.whole_book_read` reads them back using its **own, independently hardcoded** regexes
  (`lib/wholebookread.py:44-45`). Two representations of one fact, nothing keeping them in sync —
  changing the config value would silently break the reader, the same failure shape `BUILD.md` §33
  already hit once (a heading-variant mismatch).
- **A16 — `BASE_RE` (`^([HG]\d+)([A-Z]?)$`) exists in a THIRD place**, `lib/
  versespanmeaningreport.py:27`, not just the two `GOVERNANCE.md` §5 already named.

These are not edge cases found by chance — they surfaced in the first five active modules checked
this way. The prior Part A (A1-A11) undercounts the problem by construction: it never asked this
question of live code, only of retired code and shared infrastructure.

---

## PART B — The migration plan

Six phases. Sequenced so each phase is safe given what the phase before it fixed — in particular,
**Phase 2 (making `inactive` real) cannot run before Phase 1 removes the one live case where an
"inactive" row is still genuinely needed by active code** (`candidate.tag_clean_pattern`, A5). Every
phase ends in a verifiable state; nothing is marked "later" — items with no code-level fix yet
(documentation backfill, the utility registry) are scheduled with a concrete phase, not deferred
indefinitely.

### Phase 1 — Remediate the specific live defects found (data + doc fixes, no architecture change yet)

All `cfg_*` writes go through `configmaint.propose` (approval-gated, per the standing rule) — this
phase *proposes* each one; the researcher approves/rejects/revises exactly as normal, nothing silent.

1. **Fix A5/A16** — decide single ownership for the Strong's-code split pattern
   (`^([HG]\d+)([A-Z]?)$`), which now exists in **three** places (`raw.py`, the inactive
   `candidate.lemma_base_pattern`, and `lib/versespanmeaningreport.py:27`): either all three read
   one reactivated `cfg_setting` (module `raw`), or the setting is deleted and the fact stays
   code-only, documented as a deliberate "fact, not a rule" exception (§5's own category).
   **Recommendation: reactivate under module `raw`, and point all three call sites at it** — this is
   exactly the kind of cross-module reuse `cfg_setting.module` exists to prevent drifting on.
2. **Fix A3** — deactivate `passage_rule`/`passage_source` enum values (2 members each), matching
   the candidate precedent exactly.
3. **Fix A2** — for each of the 21 columns: either (a) clear `filled_by` to NULL and add a `use`
   note explaining the column is now dormant (matches `passage.rule`/`.source`'s real state), or
   (b) where a column is now populated by a *different*, currently-active mechanism (e.g.
   `passage.created_at`/`verse_passage.created_at` are in fact written by `lib/passagetrack.py`
   today, not `passage.build`), update `filled_by` to name the real current writer. Requires one
   pass per table, not a blanket clear — `passagetrack.py` genuinely writes several of these columns
   now.
4. **Fix A4** — correct `lib/stepapi.py`'s two fallback defaults (`expect_min_verses`,
   `expect_gloss_contains`) to match the DB's real, intended values (`1000`, `"God"`) — a code
   change, not a `cfg_*` proposal, reviewed as part of this plan's approval.
5. **Backfill A10** — write the missing `GOVERNANCE.md` entries for the 7 named `BUILD.md` sections
   (§23/27/28/31/32/35/36), in the same style as the existing §9A-§16 entries. Correct
   `USER-GUIDE.md` §8's passage example to reflect the current passage-debate method instead of the
   retired `passage.build`.
6. **Fix A12** — either build the `relatedNos`-following logic `discovery.follow_related` was
   always meant to gate, or remove the dead `if true: pass` branch and the setting with it, so a
   config that changes nothing stops existing.
7. **Fix A13** — bring `lib/lexiconparse.py`'s parsing rules under config where they express a
   genuine choice (which regex/tag-set decides a row's classification), starting with the ones a
   researcher would plausibly want to tune (`_LEVEL_TAGS`, `_TOP_LEVEL_LABEL_RE`); anything that's
   a wire-format fact about STEP's own HTML (not a choice this app makes) stays code, documented as
   such per §5's fact/rule boundary — the same judgement call already applied elsewhere, not a new
   category.
8. **Fix A14** — move `narrative.py`'s `REQUIRED_LABELS` into a `cfg_enum` group (module
   `narrative`) so the channel set is a config decision; move `registry.py`'s `BUILT` status tuple
   onto a `cfg_status_flow` read (the table already exists for this); give the 100%-overlap
   duplicate threshold a real `cfg_setting` (module `registry`) even if its value stays `1.0`
   — so "why 100%" becomes an answerable, changeable fact instead of a silent constant.
9. **Fix A15** — the highest-priority item in this phase, because it's live in the method used
   every session: either (a) `report.whole_book_read` derives its heading-match patterns from the
   same `cfg_report_section.heading` rows `report.passage_debate` writes from (one source of
   truth), or (b) if the two must stay independent for now, add the missing coherence check to
   `configmaint.validate` (a heading regex that can never match its own generator's current
   `cfg_report_section.heading` value is a hard error) so a future `configmaint.propose` on that
   heading can't silently break the reader the way it can today.

**Exit criterion:** `configmaint.validate` still clean; `GOVERNANCE.md`/`USER-GUIDE.md` current
against `BUILD.md`; no column anywhere names an inactive step as `filled_by` without an explicit
note; the candidate/passage enum treatment is consistent; no active setting has a dead branch
behind it (A12); `report.whole_book_read` cannot silently desync from `report.passage_debate`'s own
heading config (A15).

### Phase 2 — Make `inactive` actually mean something at runtime (the root-cause fix, A1)

1. Add `AND inactive=0` (or the `cfg_step`/`cfg_work_package` equivalent) to every read method in
   `lib/cfg.py` that has an `inactive` column to filter on: `setting`, `enum`, `step`, `sequence`,
   `may_write`, `on_fail`, `candidate_rules`. (`connection`, `route`, `book_order`, `columns`,
   `unique_key` read tables without an `inactive` column of their own — no change needed there.)
2. `run.py:run_step` — refuse to dispatch (clear error, no partial execution) if
   `cfg_work_package.inactive=1` or the resolved `cfg_step.inactive=1` — this is the literal fix for
   open escalation #334, part (b).
3. **Correction made during implementation (2026-07-29):** the real live dependency to check
   before this phase is not `candidate.lemma_base_pattern` (only ever read inside
   `handlers/candidate.py`, itself only reachable via already-inactive steps) — it is
   `candidate.tag_clean_pattern`, read generically by `lib/valuequality.py:_scan_pattern` for
   **any** `cfg_column.expectation = "pattern:candidate.tag_clean_pattern"` row, which includes
   `word_registry.word` and `lemma_inventory.gloss` — both live, active, non-retired columns
   checked by `validation.word`/`validation.book` every run. **Verified directly before touching
   `cfg.py`:** `_scan_pattern`'s own call already carries a literal fallback
   (`cfg.setting(setting_key, r"^[A-Za-z][A-Za-z' -]*$")`) that is byte-identical to
   `candidate.tag_clean_pattern`'s current DB value — so filtering `cfg.setting()` by `inactive=0`
   does not change this check's behaviour today, by coincidence rather than design. Recorded here,
   not assumed, per this whole plan's own standard. Run `configmaint.validate` plus a full manual
   smoke pass (`Start-Iba.ps1`, one `report.passage_debate` run, one `passage.validate -Book`, one
   `validation.book` run against a book with `word_registry.word`/`lemma_inventory.gloss` data)
   after this phase, specifically watching for any silent behaviour change now that `inactive` rows
   genuinely stop being read.

**Exit criterion:** flipping any row's `inactive` to `1` demonstrably changes runtime behavior
(the project's own §4 "proof of life" test, applied to `inactive` itself, which — per A1 — has never
actually passed that test until this phase).

### Phase 3 — Extend `configmaint.validate` with the missing check categories (A6, A7, A8 generalised)

Each is a genuine coherence check, not a hardcoded list, so a new instance of the same problem is
caught automatically going forward rather than needing another one-off audit:

1. **Inactive-reference coherence** (generalises A2/A6): for every `cfg_step` row with
   `inactive=1`, confirm no *active* `cfg_column.filled_by`, `cfg_on_fail.step`,
   `cfg_report.step`/`cfg_report_section.step`/`cfg_report_csv_table.step`, or
   `cfg_write_grant.writer` names it. Hard error, same class as the existing FK checks.
2. **`cfg_write_grant.writer` completeness**: every active writer must resolve to a real
   `cfg_step.step`, OR be a member of a small, explicit, named whitelist of non-step writer
   identities (`run`, `escalation`, `migration`, `call1_meanings`, `call2_getInfo`, `call3_strong`)
   stored as its own tiny reference list (a `cfg_enum` group, `writer_identity`, is the natural
   home — consistent with how every other controlled vocabulary in this app is stored) — not
   hardcoded in Python.
3. **Config-bundle completeness** (replaces the two hardcoded lists behind A7): derive
   "which steps need a `cfg_on_fail`/`cfg_report` row" from a live join (every active step in
   `cfg_write_grant` needs at least one `cfg_on_fail` row OR an explicit `cfg_step.no_on_fail_needed`
   flag; likewise for `cfg_report`) rather than the current `REPORT_STEPS`/
   `QUALITY_CHECK_REPORT_PATH` Python tuples. Requires two new nullable/boolean columns on
   `cfg_step` (`no_on_fail_needed`, `no_report_needed`) so "doesn't need one" becomes a recorded
   decision, not a silent absence — directly closes the "can't tell missed from intentional" gap in
   A7.
4. **Code-default drift check**: a scan (regex over `iba/app/**/*.py`, run as part of
   `configmaint.validate`, not a separate ad-hoc script) matching `cfg.setting("<key>", <literal>)`
   call sites against `cfg_setting.value` for the same key; flag any active mismatch as a hard
   error. This is what would have caught A4 automatically.
5. **Documentation-currency check** (already named as follow-up in `GOVERNANCE.md` §8 on
   2026-07-22 and not built then — building it now, not deferring a third time): compare
   `GOVERNANCE.md`/`BUILD.md`'s file mtimes against `cfg_change_detail.applied_at`'s latest row and
   the newest file mtime under `iba/app/**` (excluding the docs themselves); flag if either doc is
   older than the newest real change. Advisory (escalate), not a hard fail — doc updates are a
   human act the check can only prompt, not perform.
6. **Dead-branch detection** (generalises A12): where a `cfg.setting()` read feeds a conditional
   whose only consequence is a no-op (`pass`, or a branch with no write/return that changes
   `Outcome`), flag it. This can't be fully mechanised by static analysis alone, so build it as an
   AST-level heuristic (a boolean setting whose `if` branch is empty or `pass`-only) that escalates
   for a human read rather than claiming certainty — closing the gap conservatively rather than not
   at all.
7. **Module config-density review, standing, per module** (generalises A13/A14, and directly
   answers the researcher's question going forward, not just for today's snapshot): whenever a
   module's handler/lib code changes, `configmaint.validate` reports the ratio of
   `cfg_setting`/`cfg_enum` rows in that module against a rough count of hardcoded literal
   constants (regex/tuple/set assignments) in its own files — not to force everything into config
   mechanically, but to make a module like `lexicon` (1 setting against 6+ hardcoded regexes) show
   up as a visible outlier requiring a judgement call, instead of being invisible until someone
   reads the file by hand, as happened this session.

### Phase 4 — Utility-routine registry (A9)

Add a lightweight `cfg_utility` table (module, file path, one-line purpose, the `cfg_setting` keys
it depends on) — populated once by direct enumeration of `iba/app/lib/*.py` (same discipline as
every retraction/reactivation migration in this app: enumerate first, don't assume). Extends
`configmaint.validate`'s orphan check to run against this table the same way it already does for
`cfg_step`, closing the "no utility completeness check exists" gap structurally rather than by
another one-off sweep.

### Phase 5 — Run the new checks against the live DB and clear the backlog

Phase 3/4's new checks will surface findings beyond what Phase 1 already fixed (they're broader
than the specific instances found by hand in Part A). Work through every finding via
`configmaint.propose`, same approval-gated discipline, until `configmaint.validate` is clean under
the **new**, wider check set — not just the old 16.

### Phase 6 — Make this a standing discipline, not a one-time sweep

`GOVERNANCE.md` §16 already says, in writing, that config/doc drift "should be fixed as found,
per this standard, rather than claimed complete by a one-time sweep." Concretely: any session that
proposes a `cfg_*` change or retires/reactivates a module runs `configmaint.validate` (the Phase 3
version) **and** the doc-currency check **before** the session is considered closed — the same
"session log triggers commit" shape `CLAUDE.md` §12 already uses for git, applied to config
currency.

---

## What "done" looks like

- `configmaint.validate` reports clean under the Phase 3/4 check set (not the current 16), against
  the live DB, with the backlog from Phase 5 cleared.
- Flipping any `cfg_*` row's `inactive` flag demonstrably changes what the app does (Phase 2's exit
  test) — for every table that carries the column, not just the one this session happened to look
  at.
- `GOVERNANCE.md`, `BUILD.md`, and `USER-GUIDE.md` agree with the live config as of the date this
  plan is executed, and the doc-currency check (Phase 3.5) keeps that true going forward without
  needing another manual audit.
- No `cfg_column.filled_by`/`cfg_write_grant.writer`/`cfg_report*.step` anywhere names a retired
  mechanism without an explicit, current note — checked mechanically, not by memory of what was
  retired when.
- No active setting has a dead branch behind it (A12), and no module carries real, tunable
  processing rules with zero config counterpart without that being a deliberate, documented
  fact/rule call (A13/A14) — visible as a standing signal (Phase 3.7), not something that has to be
  found again by hand next time.
- The one write/read config-coherence gap live in the method used every session (A15) is closed or
  actively guarded, not left to fail silently on the next `configmaint.propose`.

Nothing above is scheduled as "future work, not decided" — every item in Part A has a phase and an
action in Part B. Awaiting review before Phase 1 begins.
