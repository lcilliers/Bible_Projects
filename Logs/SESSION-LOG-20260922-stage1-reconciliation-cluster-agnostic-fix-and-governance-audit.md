# Session Log — 2026-09-22 — Stage 1 reconciliation built, cluster-agnostic correction, batch controller, full governance audit

**Scope, one line:** Built and validated live the update/withdraw/add reconciliation mechanism escalation #1824 called for, corrected a material misunderstanding that had left `M0.6.5`/`M0.6.6`/`D7.7.1` wrongly restricted to home-strong-only (should be cluster-agnostic like `M0.7`), closed the resulting "second read should find nothing new" gap (`M0.7` per-verse skip + whole-verse batch exclusion), built a multi-cluster batch controller, then ran a full governance-compliance self-audit of this session's and the prior session's work and fixed everything it found — including 2 documentation bugs in `cfg_column.use` that were likely the direct cause of a real query the researcher hit independently.

**Status:** #1824 `ready_for_approval` (v22) — researcher review pending on the whole body of work. #1804 (the living pipeline-trace document) stays assigned to Claude per standing instruction, acknowledged every turn, updated with real findings where any surfaced. No escalation this session was left silently unprogressed.

---

## 1. Stage 1 questions/expected-nodes CSVs, then the reconciliation design (#1824)

Delivered 3 CSVs on request (`stage1-questions-20260922.csv`, `stage1-expected-nodes-20260922.csv`, `stage1-existing-nodes-20260922.csv`) — the wired question set, the deterministic expected-node prediction (no LLM), and the live existing-node extract, all scoped to `M67`. Asked "how many observations are shared across verses" and "how many nodes/observations" — answered directly from live data, catching and correcting my own error along the way (a chunk of "orphaned" rows I'd flagged were actually legitimate Stage 4 `char-answers` data, not Stage 1 debris — confirmed against Stage 4's own live battery query before retracting the claim).

Asked to mark the true orphans withdrawn via the `observation_enhancer` routine — investigated first rather than acting, found there were no orphans (see above), so nothing was withdrawn.

## 2. Reconciliation design — 3 correction rounds before it was right

Design doc `iba/docs/1824-stage1-reconciliation-design-v1-20260922.md`, corrected in place through 3 real researcher pushbacks, not just refined:

1. **First draft proposed wiping the ~25k-row `ib_observation`/`ib_node`/`ib_observation_enhancer_log` legacy dataset.** Researcher: *"a fundamental part of stage 1 is to review and update, remove, add observations that already exist, if the current data is wiped you will not be able to develop or test it."* Retracted — wiping would destroy the exact test bed reconciliation needs.
2. **Candidate scoping gap.** Researcher: *"how do you know what row to expect, so you can compare if it exist."* Checked live: `_existing_candidates()` had no verse filter at all for per-occurrence questions — 22 of 61 matches in the first live test traced to a candidate from a *different verse*. Fixed: candidates for `M0.7`/`M0.6.5`/`M0.6.6`/`D7.7.1` scoped to the exact `(verse, strong)` occurrence before any fuzzy matching.
3. **Reach-back-into-base-data architecture error.** Researcher: *"none of the correction are done as fixes. they are all done as the result of the update routine that runs on the json output that you got from LLM... you should not reach back into the base data."* Retracted the standalone keyword-backfill migration AND the standalone consolidation pass — every correction must be a byproduct of `record_one_observation()` processing a real, fresh LLM answer, never an offline script. This became the session's own governing principle (later found not to be config-registered — see §6).

## 3. Reconciliation built and validated live (BUILD.md #314)

`recordingpass.py`: Fix 1 (candidate scoping, per §2.2) + Fix 2 (three-way branch — 0 candidates→insert, 1→update in place, >1→consolidate to canonical + withdraw the rest, re-pointing `ib_node` citations). `lexical.py`/`VerseReading.ps1`: Fix 3 (`-Force` override, the only lever that ever triggers a correction, matching the governing principle).

Deliberately does **not** use `ib_observation.supersedes_observation_id` for withdraw/replace despite the column existing for exactly this shape — checked `cfg_column.use` first and it's documented "synthesis stage only," a different stage's column (same principle #1824's own `meaning_keywords` fix already applied: a new column rather than overloading an unrelated one).

One real bug found building it: `_existing_candidates()`'s new JOIN referenced `cluster_code` unqualified — ambiguous once joined against `ib_node` (which also has `cluster_code`). $0.12 wasted before the crash, no bad data written, confirmed live, closed as **#1830** (self-correctable).

**Validated live**: the same 5 verses from the original failing test, `-Force`'d through every wired question, $0.52. Of 106 occurrences: 56 `aligned-superficial-edit-consolidated` (legacy duplicates merged), 29 `aligned-superficial-edit`, 20 `new-observation`, 1 `new-expands-existing`. **73 legacy duplicate rows withdrawn.** Cross-verse mismatch check: zero remaining.

## 4. LLM validation check built into the pipeline (BUILD.md #315)

Researcher, verbatim: *"stage 1 need to pre-calculate the expected result for each scope, and measure the result received from llm as the llm validation check. build this now into the code."* New module `iba/app/lib/stage1coverage.py` (`expected_nodes()` + `validate_coverage()`), wired into `lexical.meaning()`'s live path — every live run now self-checks and persists a report.

**Investigated why the LLM misses `M0.7` items**: not truncation — home strongs get 16/16 every time (36/36 checked); non-home M-code strongs average only 7.3/16 (13/37 got just 2 questions). A real, still-open instruction-compliance gap, not fixed this session.

**Investigated 33 unexpected rows**: 2 real bugs in this module's own gating logic (`M0.6.6`/`D7.7.1` "record none" misread as "don't expect a node," and an invented party-tag requirement never actually in the catalogue). Fixed; unexpected dropped 33→6, the remaining 6 a genuine, understood limit (T3 tagging itself sometimes misses a real operation word claimed by an M-code label instead).

## 5. Material misunderstanding corrected: cluster-agnostic verse-reading (BUILD.md #316)

Researcher, verbatim: *"verse reading is supposed to be agnostic to cluster definition. every M-code word has the same status in the verse and need to be treated the same. this is not a fix for later, the code must be adjusted to rectify this material mis understanding (it was a change in strategy, introduced a while ago, but I am aware you have silently ignored it)."*

Checked the history before touching code: not purely silent — escalation #1806 v18 (this session) had already flagged this exact tension and asked for confirmation before generalizing; the confirmation never came, and a separate new family (`M0.7`) got built cluster-agnostic instead of generalizing the existing three questions. Should have followed up rather than letting the open question drop.

Fixed: `M0.6.5`/`M0.6.6`/`D7.7.1` now answered for every M-code strong in the verse, matching `M0.7`'s pattern exactly — new per-verse front-load skip (`_verse_cluster_agnostic_coverage`, later broadened again in §7), `meaning_sources_by_strong` widened, `D7.7.1`'s invented party-tag requirement dropped from the live prompt too. Deliberately left open (not decided unilaterally): whether these should be re-attributed to the word's own home cluster like `M0.1`/`M0.5`, or stay filed under the answering pass's cluster like `M0.7` already does — flagged, not assumed.

Verified live (`2Cor.8.8`, $0.23): 3 non-home strongs that had never received these answers now do, in one batch.

## 6. Multi-cluster node tracking — investigated, designed, left as a decision (not built)

Researcher walked through a concrete consequence: *"a word for M32 is in a verse that surfaced with a word for M67... there should be no need for any further analysis of that verse... if the second read of the verse finds additional observations then something went wrong in the first reading."* Also: *"However 50% of verses have multi cluster implications. the multi cluster membership must be captured in the nodes."*

Verified: the real figure is 66.7% (16,442 of 24,649 verses with any M-code strong span more than one cluster), confirmed multiplicity is purely verse-level (0 strongs belong to 2+ M-code clusters). Design doc `iba/docs/1824-multi-cluster-node-tracking-v1-20260922.md`: 3 options, recommended (B) — an extra `ib_node` row per relevant cluster for the same observation, no schema change. **Not built** — awaiting the researcher's decision on B vs. C.

## 7. "Second read finds nothing new" gap closed (BUILD.md #317)

Traced the consequence of §5: `M0.7` had zero per-verse skip protection (unlike the just-fixed three, and unlike `M0.1`/`M0.5`'s global one). Fixed: folded `M0.7` into the same per-verse coverage check (renamed `_verse_relational_coverage` → `_verse_cluster_agnostic_coverage`, field `relational_already_covered` → `already_covered`). Plus whole-verse batch exclusion (`stage1coverage.fully_covered_verse_ids()`) — a verse where every expected triple is already covered is excluded from batch construction entirely, before any LLM cost, unless `-Force`. Verified live 3 ways (preview exclusion count, single-verse "nothing to do" at $0, `-Force` bypass confirmed).

## 8. Batch controller built (BUILD.md #318)

Researcher: *"you can start work on a batch controller to allow for running this process in batch mode in the background using the processbatch utility for monitoring."* The "processbatch utility" turned out to be the already-existing `BatchProgress.ps1`/`batchprogressreport.py` (escalation #1756) — no new monitoring needed. Built `iba/app/ps/Run-Stage1Batch.ps1`, a PS-level loop over the existing single-cluster step. **Three real bugs found and fixed**, the serious one: local variable `$live` collided with the script's own `[switch] $Live` parameter (PowerShell variable names are case-insensitive) — every live run was silently misreported as FAILED even when real work committed correctly, isolated by reproducing at $0 cost. Also fixed a single-cluster array-unwrap crash and a cost-estimate double-count. `BatchProgress.ps1` confirmed to see the controller's runs with zero changes needed.

## 9. Two ad hoc data-integrity questions answered directly

- "Is `verse_reference` in the note table aligned with `verse`'s format?" — No: `verse_lexical_note` (the retired old shape) uses a numeric `verse_id` FK, not a text reference at all.
- "Why isn't `WHERE v.reference = 'Mark.6.25'` resolving?" — `verse.reference` holds STEP-abbreviated text (`"Mar 6:25"`), not the dotted `osisId` format (`"Mark.6.25"`) the query expected; wrong column.

## 10. Full governance-compliance self-audit (BUILD.md #319, #320)

Researcher instruction, verbatim: *"all the work you did today and yesterday must be FULLY GOVERNANCE compliant. audit it and confirm positive... Can you also check that every other column in observation and node table is fully compliant."*

**Column audit**: `ib_node.verse_reference`↔`verse.osisId` join integrity 100% (0 of 10,115 orphaned). Every column in `ib_observation`/`ib_node` registered in `cfg_column`. Enum-drift check clean except `meaning_source` (known, pre-existing, deliberately-unvalidated debt, escalation #1796/#1771 — not this session's doing).

**Full `BUILD.md` #306-318 sweep**, every claimed registration checked against the live DB, not the prose — **5 real gaps found and fixed**: 2 unregistered/orphaned `cfg_setting` keys from yesterday's work (#311), 1 `cfg_method_rule` stale relative to **this session's own** §5 fix, 1 undocumented behaviour rule (the §2.3 governing principle, never actually registered), 1 hardcoded report path (**this session's own** §4 build). All 5 fixed via `iba/app/migration/fix_stage1_governance_gaps_v1_20260922.py`, plus `GOVERNANCE.md` §80 for the one that's a real process rule.

**Then**, pushed on independently by the researcher's own query bug (§9): found `cfg_column.use` for `ib_node.verse_reference` itself was factually wrong — documented as resolving against `verse.reference` when the real code uses `verse.osisId`. Very likely the direct cause of the researcher's query failure. A second column (`cluster_subgroup.anchor_verse_reference`) carried the identical wrong claim, inherited by explicit cross-reference. Both fixed (`fix_ib_node_verse_reference_doc_v1_20260922.py`), confirmed no stale claim remains anywhere in `cfg_column`.

## 11. Escalations touched this session

| id | outcome |
|---|---|
| #1804 | in-progress, stays assigned to Claude — living pipeline-trace document, acknowledged every turn (v20→v42), real findings added where any surfaced (M0.7 coverage gap, unexplained UNEXPECTED rows, batch-controller work) |
| #1824 | re-assigned, `ready_for_approval` (v22) — the main thread: wipe rejected, offline-script design rejected, candidate scoping + three-way reconciliation built and validated, coverage-validation check built, cluster-agnostic correction, multi-cluster design delivered (not built), second-read gap closed, batch controller built, full governance audit run and fixed |
| #1829 | completed (self-correctable) — `lexical.meaning` preview stdout/JSON contract fixed |
| #1830 | completed (self-correctable) — ambiguous `cluster_code` column crash fixed |

## 12. Files created or changed

**Code:**
- `iba/app/lib/recordingpass.py` — candidate scoping (Fix 1), three-way branch (Fix 2), `_consolidate_duplicates()`
- `iba/app/lib/versereadinggenerate.py` — cluster-agnostic `M0.6.5`/`M0.6.6`/`D7.7.1`, `already_covered` mechanism (now covers `M0.7` too), `D7.7.1` party-tag requirement dropped
- `iba/app/lib/stage1coverage.py` — **new**: `expected_nodes()`, `validate_coverage()`, `fully_covered_verse_ids()`
- `iba/app/handlers/lexical.py` — `-Force` (Fix 3), `-VerseList`, whole-verse exclusion, coverage-validation wiring, config-defined report path, stdout/stderr contract fix
- `iba/app/ps/VerseReading.ps1` — `-VerseList`, `-Force` params
- `iba/app/ps/Run-Stage1Batch.ps1` — **new**: multi-cluster batch controller

**Migrations (registered in `cfg_utility`, run, `inactive=1`):**
- `fix_stage1_governance_gaps_v1_20260922.py`
- `fix_ib_node_verse_reference_doc_v1_20260922.py`

**Design docs:**
- `iba/docs/1824-stage1-reconciliation-design-v1-20260922.md`
- `iba/docs/1824-multi-cluster-node-tracking-v1-20260922.md`

**Documentation record:**
- `iba/app/BUILD.md` — #313 through #320
- `iba/app/GOVERNANCE.md` — §80

**Deliverables (`outputs/`):** `stage1-questions-20260922.csv`, `stage1-expected-nodes-20260922.csv`, `stage1-existing-nodes-20260922.csv`, `stage1-expected-vs-existing-comparison-20260922.csv`, 3 named coverage-validation test CSVs, the final batch-controller proof CSV + its paired coverage report. 15 disposable debug/repro artifacts from live-testing the batch controller archived to `outputs/archive/2026-09-22-stage1-batch-controller-debug/` (governance.redundancy_archiving) rather than left cluttering `outputs/`.

## 13. Decisions — researcher's own vs Claude self-correctable

**Researcher's own:**
- Reject the data wipe; reconciliation must be developed against real, already-messy data.
- Reject the offline-script architecture; corrections only via a real LLM rerun.
- `M0.6.5`/`M0.6.6`/`D7.7.1` must be cluster-agnostic — reasserted, not new.
- "The second option" (whole-verse batch exclusion) — proceed.
- Batch controller build directive.
- Multi-cluster tracking is real and must be addressed — design delivered, the actual B-vs-C build choice still theirs.

**Claude self-correctable (found and fixed without a researcher decision):**
- `#1830` ambiguous column crash.
- `#1829` stdout/JSON contract crash (found earlier, closed this session's opening turns).
- 3 PowerShell bugs in the batch controller (variable collision, array unwrap, cost double-count).
- 2 gating-logic bugs in `stage1coverage.py` (M0.6.6/D7.7.1 "record none" misread; invented party-tag requirement).
- 5 governance-registration gaps found by self-audit (2 mine, 2 from yesterday, 1 shared) — fixed directly as standard-deviation bugs, not judgment calls.
- 2 `cfg_column.use` documentation bugs (`ib_node.verse_reference`, `cluster_subgroup.anchor_verse_reference`) — likely the direct cause of the researcher's own independently-discovered query bug.

**Not self-correctable — surfaced, not decided by Claude:**
- Multi-cluster node tracking: Option B (extra node row per relevant cluster) vs. C (new column) — awaiting decision.
- `M0.7` instruction-compliance gap (non-home strongs average 7.3/16 vs. home strongs' 16/16) — real, diagnosed, not fixed.
- Whether `M0.6.5`/`M0.6.6`/`D7.7.1` observations should be re-attributed to the word's own home cluster (like `M0.1`/`M0.5`) rather than staying filed under the answering pass.

## 14. Open items carried into the next session

- `#1824` — awaiting the researcher's final sign-off on the whole body of work (v22, `ready_for_approval`).
- Multi-cluster node tracking — build Option B (or a different direction) once decided.
- `M0.7` instruction-compliance gap — non-home M-code strongs are inconsistently answered; needs its own fix (e.g. a per-strong checklist rather than a prose instruction).
- `M67`'s own `M0.7` coverage is still incomplete (988 of 2020 expected missing as of the last check) — real processing work remains even on the one cluster already exercised this session.
- `iba/docs/ps tools worksheet.xlsx` sync for `Run-Stage1Batch.ps1`'s and `VerseReading.ps1`'s new params (`governance.ps_worksheet_sync_on_change`) — not done, deliberately (Excel-crash risk while its current open/closed state is unknown).
- Wider rollout of the reconciliation fixes to clusters other than `M67` not yet attempted.
- `#1804` (living trace document) stays assigned to Claude per standing instruction.

## 15. Git state

- Branch: `main`
- Commit: `93f3bd2802036f473530a155f6c144753ec93beb` (2026-09-22T08:44:54+01:00) — "session 20260922: Stage 1 reconciliation built, cluster-agnostic correction, batch controller, full governance audit"
- Pushed: `38b410fa..93f3bd28 main -> main` — confirmed via `git push`
- `git status` after push: `On branch main. Your branch is up to date with 'origin/main'. nothing to commit, working tree clean.`
