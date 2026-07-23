# IBA Session Log — v2, 2026-07-21

**Topic:** Continuation from `session-log-v1-20260721.md` (Application Design v1 → v2, phased). This
session: the phased design got corrected twice more, then the work turned into an actual build cycle —
`configuration_maintenance` (Layer 1) built from nothing, a whole-app escalation-consistency audit (only
3 of 15 conditions escalated before this session), reports registered and config-governed, and a
report-persistence standard violation found and fixed. Closing now — researcher is closing VS Code and
will open a new session to test.

**Outcome:** ✅ `configuration-maintenance` work package built, tested, and hardened (validate/propose/
report + step-duplication, orphan-config, module-ownership, catch-all, and report-persistence checks).
✅ Two new standalone quality-check work packages (`candidate-quality`, `passage-quality`), both now
correctly escalating and persisting findings. ✅ `reports` work package registered (`report.py` +
`validation.py`, previously standalone scripts). ✅ `Escalation.ps1` built (the one PS front door
`lib/escalation.py` never had). ✅ 7 new memory entries capturing corrections that generalize well
beyond this session. **3 live escalations left genuinely pending** for the researcher to answer next
session (see §9) — none auto-answered.

---

## 1. Trigger / continuation point

Picked up from `session-log-v1-20260721.md`: Application Design v1 existed, §11 had 5 open items, the
researcher's instruction was to split the design into a Data-Layer / Analytic-Layer phased v2. That
happened first (§2 below), then two more rounds of correction on v2's open items, then — at "starting to
come together, proceed" — the session pivoted from design documents into an actual build cycle that ran
for the rest of the day.

## 2. Design v2 — phased restructure, then two correction rounds

- Rewrote `iba-application-design-v1-20260721.md` → `iba-application-design-v2-20260721.md`: Data Layer
  (Raw/Base/Control, the 3 built work packages) vs Analytic Layer (Interpretation/Prose,
  `analyse-characteristic`), with a Phase-1-exit/Phase-2-entry gate.
- **Round 1:** researcher resolved A8-3 (no further old-registry import needed), directed A8-4 (passage
  table will be rebuilt, rules refined), called A8-5/A8-6 config/compliance fixes — re-triaged the whole
  A8 punch list; then A8-1 (config 5-column shape) resolved itself as "resolves by build, not a standing
  decision."
- **Round 2 (the important one):** asked for a Step-2 gap list. Produced one from memory + the design
  doc's own text — **rejected outright**: *"you did not even look at the current build... just a dump
  from memory."* This is the session's first load-bearing lesson (§10, memory
  `feedback_iba_gap_analysis_requires_live_build_inspection`) — every gap-list/audit claim from this
  point on in the session was grounded in actually running code and querying the live DB, not asserted.

Filed: `iba-config-maintenance-and-passage-live-inspection-v1-20260721.md` — real findings from
actually running `cfgcheck.py` (crashed — `FileNotFoundError`, the 07-19 restructure broke the seed
path and nobody noticed since), confirming `cfgreport.py` was never wired to anything, and correcting a
wrong claim in the gap list (`candidate.py` already supports `reject`/`synonym` kinds — the earlier list
said it didn't).

## 3. "80% of your fixes are config, not code" — the second correction

Researcher: most proposed "fixes" were actually missing/stale **config content** or a **missing
registered utility**, not code bugs — *"this whole design is completely not achievable in the way you
are approaching it."* Re-triaged every item into three buckets (code defect / config content / missing
registered utility) and found the sharpest confirming fact myself: `configuration_maintenance` — the
utility principle c names by name — wasn't registered as a work package at all; `cfgload`/`cfgcheck`/
`cfgreport` were standalone scripts nothing else in the app knew about. Memory:
`feedback_iba_fixes_are_config_and_registered_utilities_not_code_patches`.

Researcher: "create the fundamental building blocks first, work in layers." Produced
`iba-configuration-maintenance-layered-design-v1-20260721.md` — Layer 0 (bootstrap facts) through
Layer 4 (content fixes routed through the new utility), designing `configuration_maintenance` as
`validate`/`propose`/`report`.

**Two more corrections before building:**
- "If you're basing configs on the archived JSONs, you have it wrong — DB is master, old files are
  reference only." (Memory: `project_iba_db_is_master_over_legacy_json_seeds` — applies to both app
  config *and* the candidate seed migration.)
- "DB-direct is a no-no — I want to validate and be involved in any updates." Redesigned `propose()` to
  be approval-gated via escalation, not silent DB-direct writes. (Memory:
  `feedback_iba_config_changes_require_researcher_approval_never_silent`.) Then: approval payloads must
  be **representative** and three-way (**approve/not-approve/resubmit-with-comment**), never yes/no.
  (Memory: `feedback_iba_validation_approval_must_be_representative_and_three_way`.)

## 4. `configuration_maintenance` — Layer 1 built, tested, and immediately re-audited

At "proceed," built:
- `handlers/configmaint.py` — `validate` (ports `lib/cfgcheck.py`'s checks to query the live DB),
  `propose` (DB-direct, single-row, approval-gated — mirrors `registry.create`'s escalation shape),
  `report` (regenerate `CONFIG-REPORT.md`).
- `lib/escalation.py` extended — run-scoped, three-way answer (`approve`/`reject`/`revise` + comment),
  non-breaking alongside the original word-scoped yes/no path.
- `migration/bootstrap_configuration_maintenance.py` — the one-time, documented, direct registration
  (can't route through `propose()` since that utility doesn't exist until this script runs it — same
  class of exception as `cfgload.py`'s own hard-coded schema bootstrap).
- `cfg_change_detail` — a new table, found necessary mid-build: `cfg_change_log`'s existing shape had
  nowhere to record *what* changed, only that a reload happened.
- `ps/Config-Maintenance.ps1`.

**Bugs found and fixed during the SAME build, by actually running it** (not just reading code): my own
bootstrap script used the wrong module path (`handlers.configmaint` instead of
`iba.app.handlers.configmaint` — crashed on first real test); missing `cfg_on_fail` rows made the first
pause/resume test hard-stop instead of pause; `escalation.py`'s own docstring (and `registry.py`'s) had
a pre-existing stale CLI path (`iba.app.escalation` instead of `iba.app.lib.escalation`) — fixed.

Tested full cycle: `validate` clean pass, `report` (first `CONFIG-REPORT.md` ever generated), `propose`
approve/reject/revise/insert/update/delete, write-grant and coherence-check rejections — all via a
harmless, fully-cleaned-up self-test row.

## 5. Module ownership, consistency, anti-catch-all

Researcher review, same day: (a) step-duplication check — built, hard error (two work packages sharing
a step name would collide, since `escalation`/`cfg_on_fail` match on `step` alone). (b) orphan-config
detection — built, advisory; immediately found `configmaint.report_path` itself unused by `report()`
(fixed) and `passage.cross_chapter` dead in `passage.py`. (c) "pre-approved config list" — didn't exist;
researcher dropped the requirement ("configs will be loaded interactively" from now).

Then: "should settings be in another table?" → real correction: the actual concern was completeness
auditing and load lifecycle, not table shape. Built `cfg_setting.module` (backfilled by **grepping real
consumers**, not trusting key prefixes — several didn't match, e.g. `discovery.particle_pattern` is
prefixed "discovery" but consumed by `stepapi.py`'s `Step` class) + `config_module` enum + a
"no-catch-all" rule: `propose()` now requires `module` on every new `cfg_setting` row and attaches a
mandatory "NEEDS JUSTIFICATION" warning when the target module already has its own dedicated table
(`MODULE_DEDICATED_TABLE`, currently `candidate` → `cfg_candidate_rule`).

## 6. `span_candidate` rules — investigation before building surfaced the escalation gap

Asked to add three rules (`candidate_tag` not null, no special chars/transliteration, `lemma_key` must
be in `strong`). Checked the live data **before** building anything (now the established discipline):
17.7% of rows already null, virtually all non-null values are messy migration gloss text, and 52.3% of
rows reference a `lemma_key` with no `strong` row yet — the last one is not a data-quality bug, it's an
inherent consequence of `strong` growing incrementally per registered word while the candidate seed is
deliberately independent. Filed `iba-span-candidate-rules-findings-v1-20260721.md`, recommended
report-only, asked hard-block vs report-only.

**Researcher's correction reframed the whole rest of the session:** *"not hard blocking - it should go
through the escalation routine... it seems that you are not familiar with escalation and that makes we
question how many other rules do we have that is linked to escalation."*

## 7. The escalation-consistency audit — the big one

Audited every `fail()`/`escalate()` condition app-wide: **only 3 of 15 escalated** before this pass
(`raw.discover`/zero-strongs, `registry.create`/needs-approval, `configmaint.propose`/needs-approval).
Everything else was `report-stop` or silent `report-continue` — and `configmaint.validate`'s own
advisory checks (§5) didn't even fit that taxonomy, a **fourth, unsanctioned "silent counts blob"**
pattern I'd introduced without noticing. Memory:
`feedback_iba_data_judgment_calls_must_escalate_not_silent_report`.

Fixed in one batch (`migration/bootstrap_quality_validate_steps.py`, direct — per the researcher's
explicit "I do not want to approve each and every issue individually" for this class of infrastructure
registration):
- `configmaint.validate`'s findings now escalate (`needs-review`) instead of returning silently.
- **`candidate-quality`/`candidate.validate`** and **`passage-quality`/`passage.validate`** — two new
  standalone work packages (deliberately **not** added to `set-candidates`/`build-passages`'s existing
  sequence — at 17.7%/52.3%/81% prevalence, escalating on every book build would be pure noise). One
  escalation per invocation, batched, with samples + counts — not one per row.
- Reclassified `raw.detail`/no-vocab and `raw.verses`/shortfall from silent `report-continue` to
  `pause-continue` — the latter is exactly the class of bug `BUILD.md` §5 already documents.
- `CONFIG-REPORT.md` §5 rebuilt: split into "escalates" / "does not," with a leading count — the
  "easily review the rules" requirement.

## 8. Reports registered + config-governed (Phase 2 of the same instruction)

`report.py` and `validation.py` were standalone scripts, invoked directly, outside the dispatcher — same
gap `configuration_maintenance` closed for `cfgload`/`cfgcheck`/`cfgreport`. Registered as `reports`
(`report.word`, `validation.word`, `validation.book`; `handlers/reports.py` thin adapters).
`report.py` gained `report.output_dir`/`report.output_pattern` (was hard-coded); `validation.py` had
**zero** config before this — gained an output-dir setting and 7 section-inclusion toggles.
Deliberately left `migration/build_base_all_books.py` unregistered — a one-off batch transcript, not an
ongoing report.

## 9. Escalation's missing PS front door

Researcher: `python -m iba.app.lib.escalation list` doesn't run in PS as instructed — *"the rule is all
user driven methods must be encapsulated in PS and added to the project documentation."* Every other
governed operation had a PS wrapper; answering an escalation never did (including in code written
earlier the same session). Built `ps/Escalation.ps1` (`List`/`Answer`/`AnswerRun`); fixed every place
that printed the raw command (`configmaint.py`, 3 PS scripts, `registry.py`'s docstring, `BUILD.md`).

## 10. Report persistence — a standard violation, found and fixed, then codified

Asked where the new quality-check configs direct output. Found: `report.py`/`validation.py`/
`cfgreport.py` all persist to `.md` (matching `CLAUDE.md`'s own "output always to a file" standard);
`candidate.validate`/`passage.validate`/`configmaint.validate`'s findings did not — only a terminal
print + an `escalation` row. Researcher: *"should you fix it? why ask?... errors is not optional to fix
it. you can add this as an app config... so you do not have to ask me again."*

Fixed + codified: both quality checks now write a full persistent report every run
(`candidate-quality.md`, `passage-quality.md`); `configmaint.validate`'s findings folded into
`CONFIG-REPORT.md` §0; **`governance.reports_must_persist`** (new `governance` module) states the
standard as a real setting, and a genuine new coherence check
(`lib/cfgquality.find_missing_report_paths`) enforces it as a hard error — the app checks its own
compliance now, not only memory. `lib/cfgquality.py` extracted (shared by `configmaint.py` and
`cfgreport.py` without a circular import). Memory: `feedback_fix_standard_violations_dont_ask` — the
general principle: a deviation from an *already-established* standard is a bug to fix, not a question.

## 11. Memory saved this session (7 new entries, all foundational-tier)

1. `feedback_iba_gap_analysis_requires_live_build_inspection`
2. `feedback_iba_fixes_are_config_and_registered_utilities_not_code_patches`
3. `project_iba_db_is_master_over_legacy_json_seeds`
4. `feedback_iba_config_changes_require_researcher_approval_never_silent`
5. `feedback_iba_validation_approval_must_be_representative_and_three_way`
6. `feedback_iba_data_judgment_calls_must_escalate_not_silent_report`
7. `feedback_fix_standard_violations_dont_ask`

Also compacted `MEMORY.md` mid-session (it hit its size ceiling) — demoted the paused RESET/
lexical-study-methodology memories (recoverable, listed in the footer comment; nothing deleted).

## 12. Current state — what's pending for the next session

**Three live escalations, genuinely open, none auto-answered:**

| # | step | what |
|---|---|---|
| run `RUN-20260721_163604_125-CANDIDATE-QUALITY` | `candidate.validate` | 15,541 null tags, ~36k messy tags, 46,003 rows (386 lemmas) with no `strong` entry — full detail in `iba/app/reports/candidate-quality.md` |
| run `RUN-20260721_163620_949-PASSAGE-QUALITY` | `passage.validate` | 18,571 passages, avg 1.34 verses/passage, 81% single-verse — full detail in `iba/app/reports/passage-quality.md` |
| run `FINAL-CHECK-PHASE2` | `configmaint.validate` | 11 orphan configs, 3 settings needing justification (see `CONFIG-REPORT.md` §0) |

Answer any of them: `iba\app\ps\Escalation.ps1 -Action AnswerRun -RunId <id> -Decision Approve\|Reject\|Revise [-Comment ...]`.
List them again any time: `iba\app\ps\Escalation.ps1 -Action List`.

Also still pending, pre-existing, untouched this session: escalation `#169`, a new-word approval for
"blindness (spiritual" (`registry.create`) — unrelated to this session's work.

**Everything built this session is tested and working** (see §4–10 above for what was actually run, not
just written). Nothing was left mid-build.

## 13. Key files

**Design docs** (`iba/docs/`): `iba-application-design-v2-20260721.md` (current, supersedes v1),
`iba-configuration-maintenance-layered-design-v1-20260721.md`, `iba-config-maintenance-and-passage-live-
inspection-v1-20260721.md`, `iba-module-config-completeness-audit-v1-20260721.md`,
`iba-span-candidate-rules-findings-v1-20260721.md`.

**App code** (`iba/app/`): `handlers/configmaint.py`, `handlers/reports.py` (new); `handlers/candidate.py`,
`handlers/passage.py`, `handlers/registry.py`, `report.py`, `validation.py` (extended);
`lib/cfgquality.py` (new); `lib/escalation.py`, `lib/cfgreport.py` (extended);
`ps/Config-Maintenance.ps1`, `ps/Candidate-Quality.ps1`, `ps/Passage-Quality.ps1`, `ps/Reports.ps1`,
`ps/Escalation.ps1` (all new); five `migration/bootstrap_*.py` one-off registration scripts (all
idempotent, safe to re-run); `GOVERNANCE.md` §5A–5E (the full build record); `BUILD.md` (run-command
table, kept current).

**Generated, not hand-maintained:** `iba/app/config/CONFIG-REPORT.md` (regenerate:
`Config-Maintenance.ps1 -Step Report`), `iba/app/reports/candidate-quality.md`,
`iba/app/reports/passage-quality.md`.

## 14. Resuming next session

1. Read this log, then `GOVERNANCE.md` (§5A–5E is the whole day's build record) for full context.
2. `Escalation.ps1 -Action List` to see the 3 pending decisions fresh.
3. Decide the 3 findings (§12) — each is a real, current picture of the data, not synthetic.
4. Beyond that: `registry.create`'s word-approval is still yes/no, not the new three-way answer — a
   named, deliberate fast-follow (`GOVERNANCE.md` §6), not started.
5. Layer 2 hardening (hard technical write-enforcement, batching, full hypothetical-validate,
   `cfg_setting`'s reconcile-vs-seed step) is named but not built — next whenever wanted.
