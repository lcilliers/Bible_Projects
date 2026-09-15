# Session Log — 2026-09-15

**Scope:** Started via `/start-project` (spine clean, 0 FATAL; STEP up; IBA READY; 33→ escalation
backlog). Answered a researcher question on how T3–T15 role data actually reaches the pipeline
(traced `lib/lexical.py` live), which led to the researcher's own **role-driven reading-sequence
design** (5-step sequence, pointer-vs-relational observations, `verb_argument` flagged inadequate,
faculty reframed) — recorded on #1704, spun `verb_argument` out as its own escalation **#1705**.
Consolidated nine scattered Layer 1/2 escalations (#1589/1590/1591/1592/1594/1595/1597/1606/1607)
plus the cluster-reading sign-off pack into **one build proposal, #1706** — then, across several
turns of researcher review, built the actual **#1606 fix** (strong→cluster_strong sync now
guaranteed, not just checked: `reconcile()`/`cluster.validate` escalate on gaps instead of silently
absorbing them, all 111 orphaned strongs classified), closed the **cross-run escalation-acknowledgment
gap** found via #1707 (a known backlog no longer re-raises every run), fixed a real **`database is
locked` crash** in the escalation CLI (#1708) plus cleaned up two test-artifact escalations it
produced (#1709/#1710), resolved **all 5 of #1697's open items** (cluster-status lifecycle fully
designed), and corrected a **real self-contradiction in #1706's own pipeline shape** (Layer 2 is its
own stage — produce, then capture — not folded into subgroup formation as first drafted). Closed
with real research: pulled **live verse examples** for every `verb_argument` scenario type
(21,160-verse base pool), which the researcher reviewed and found genuinely inconclusive — "the
deeper we dig, the more noise we create" — explicitly asked not to be reacted to, wants to digest.
**Session ends here, resuming with #1705** per direct researcher instruction.

## 1. Escalations touched, by id, with outcome

| # | Outcome this session |
|---|---|
| **#1606** | Built and **completed** (approved). Root cause traced: both live strong-creation paths already attempted auto-classification, but a failed attempt was never escalated (`cluster.validate` only checked two narrower exception shapes). Fixed: `handlers/raw.py` (`reconcile()`/`backfill_meaning()`) now `fail("unclassified", ...)`; `handlers/cluster.py:validate()` escalates on unclassified too; all 111 Leg-3 orphan strongs classified (5→T5, 40→T6, 66→T2) via new one-off migration, one self-caught correction (`G3304` "rather" fixed live before reporting). 3 flagged data anomalies confirmed T2 by the researcher, out of scope. Verified live (synthetic tests + a real end-to-end `cluster.validate` dispatch). One tool bug found and fixed along the way — the escalation CLI's own `approved` transition silently dropped the comment and left a stale `resolution` field; corrected via `-Action Correction`. |
| **#1589 / #1590 / #1591 / #1594 / #1597** | Consolidated into #1706 (dispositions: #1590 confirmed superseded-by-design, #1591 confirmed moot, #1597 confirmed resolved-by-architecture, #1594's ambiguous quote later fully resolved). Researcher then closed all five directly via the escalation tool (`supersede`/`reject`, #1589/1590/1591 folded into #1704, #1594/#1597 confirming this session's own readings) — outside chat, discovered mid-session and recorded here for the record. |
| **#1592 / #1595 / #1607** | Consolidated into #1706 as the Layer 1/2 build spec (Phase B). #1607's D2/D3 (`resolved_sense`) resolved this session — dropped from Layer 1 entirely, moved to the new Layer 2 stage (see #1706 below). Still `in-progress`/`review`, no independent close. |
| **#1691** | Cross-referenced twice — pointer-observation-kind requirement (from #1704's role-driven design) and the `stage='subgroup'` scope, both folded in as build requirements on its still-open `tag` taxonomy. Still `in-progress`/`review`. |
| **#1696** | Held all session on the researcher's own explicit sequencing ("I will first complete 1706") — acknowledged every turn the stop-hook flagged it, never built. One direct researcher comment appeared on it mid-session ("migration can proceed") that reads differently from the chat instruction; flagged the discrepancy rather than silently picking one reading. Still `in-progress`/`review`, assigned Claude. |
| **#1697** | **All 5 open items resolved this session**, moved to `ready_for_approval`: (1) enum spellings confirmed as proposed; (2) ordinals 1–2 confirmed as a historical, no-longer-active phase (kept in the enum, no gating code needed), ordinals 3–8 confirmed as the real lifecycle to build; (3) `ready_for_observations` confirmed as the rollup signal for "every subgroup's reading stage complete"; (4) `strongs_reassigned` must raise a real escalation to the researcher at the moment it fires — no automatic resubmission or recommend-routine, researcher wants manual control for several rounds first; (5) initial backfill: all 95 live `cluster` rows start at ordinal 2. |
| **#1701** | Cross-referenced from #1704's role-driven design (faculty resolution: end-of-read, subgroup-level reflection, not a per-strong tag — dissolves the old Inner-Faculties objection). Still `in-progress`/`review` — the actual replacement catalogue question is not yet authored. |
| **#1704** | Updated with the researcher's own 5-step role-driven reading-sequence design (`1704-role-driven-reading-sequence-design-v1-20260915.md`, new) and the researcher's confirming decisions on all 5 points (sequence forced not advisory, pointer-vs-relational split, `verb_argument` spun to #1705, faculty resolved). Still `in-progress`/`review` — Phase 2/3 (match events, corrective actions) not started. |
| **#1705** | **Raised** this session (spun out of #1704) for `verb_argument`'s model expansion. Built two reference docs (`1705-verb-argument-what-exists-reference-v1-20260915.md`, `1705-verb-argument-scenario-examples-v1-20260915.md`). Researcher confirmed it gates the pipeline (cannot be parked), gave rich new context (the T3 methodological history — why verbs were pulled out of individual M-code clusters into their own category — and the full discovery-question set a T3 role triggers: source/target/action/M-code-relation/direction/transformation/blockage/body-impact, explicitly not exhaustive). Real verse examples pulled live across all 12 T-codes plus the two named party-combos. **Researcher's own review of those examples found no conclusive, consistent method** — explicitly asked not to be reacted to, wants time to digest. **This is the explicit starting point for next session.** |
| **#1706** | **Raised** this session as the consolidated build proposal for the whole lexical stack. Built, then substantially revised across several researcher-review rounds: full pipeline table (11 stages), per-escalation dispositions, a 33-item ordered build list across 7 phases, explicit Layer 1 config cutover steps (dissolve old / set new), and — the largest correction — fixed a genuine self-contradiction in the pipeline shape (Layer 2 was described as both "part of subgroup formation" and "supplying subgroup its own input," which can't both be true; corrected to Layer 2 = its own produce+capture pair, running before subgroup, which then only consumes it). Still under active researcher review — item 4 (pack sign-off), item 8 (Layer 2 stage's own internal design), item 9 (confirm "dumped" = soft-delete) remain open. |
| **#1707** | Auto-raised this session by a live `cluster.validate` verification run (the pre-existing, unrelated no-word/sibling-conflict backlog, 4,460/2,789). Researcher: *"this report is as expected. Can be signed off. This situation should no longer create an exception everytime it runs."* Built the actual fix requested (`lib/escalation.py:answered_baseline_for_step()`, a cross-run acknowledgment mechanism — a prior run's approval now covers a later run's identical or smaller findings) and **completed** (approved). Verified live: a second `cluster.validate` dispatch acknowledged automatically, no duplicate escalation raised. |
| **#1708** | Auto-raised: a real `database is locked` crash on the researcher's own direct `escalation update` CLI call, caused by this session's own concurrent heavy DB-wide verification runs. Fixed (`lib/escalation.py:main()` now retries on that specific error, 3 attempts, 1s/2s/4s backoff, before falling through to the existing crash-recording path) and **completed** (self-correctable). Verified with 3 synthetic cases plus a live regression check. |
| **#1709 / #1710** | Auto-raised — both confirmed as artifacts of my own verification testing for #1708 (the tracebacks show my own mock functions), not real defects. **Completed** (self-correctable), no code fix needed. |

## 2. Files created or changed

- `iba/app/handlers/raw.py` — `reconcile()`/`backfill_meaning()` now fail on an unclassified strong instead of always `ok()` (#1606).
- `iba/app/handlers/cluster.py` — `validate()` escalates on unclassified strongs too, and checks the new cross-run acknowledgment baseline before escalating at all (#1606, #1707).
- `iba/app/lib/escalation.py` — new `answered_baseline_for_step()` (#1707); `main()` retries on `database is locked` (#1708).
- `iba/app/migration/assign_leg3_orphan_strongs_v1_20260915.py` — new. One-off, classifies all 111 Leg-3 orphan strongs; registered in `cfg_utility` then set `inactive=1` once run.
- `iba/app/BUILD.md` — 3 new entries (#264 Leg-3 guarantee + classification, #265 cross-run acknowledgment, #266 escalation-CLI lock retry).
- `iba/docs/1704-role-driven-reading-sequence-design-v1-20260915.md` — new. The researcher's 5-step role-driven reading model, decisions recorded in place.
- `iba/docs/1705-verb-argument-what-exists-reference-v1-20260915.md` — new. Full consolidation of everything live/decided/found about `verb_argument` across #1449/#1606/#1607/#1704/#1705, plus the T3 methodological history and the discovery-question-set framing.
- `iba/docs/1705-verb-argument-scenario-examples-v1-20260915.md` — new. Real verses pulled live for every T-code scenario type, with an explicit co-occurrence-not-confirmed-linkage caveat.
- `iba/docs/1706-lexical-stack-full-rebuild-consolidated-build-proposal-v1-20260915.md` — new. The full consolidated build proposal, revised across the session (pipeline-shape correction, cutover steps, #1697 resolutions folded back in).
- `outputs/escalation/escalation-list-v83-20260915.md`, `1697-escalation-history-v1-20260915.md`, `1705-escalation-history-v1-20260915.md` — regenerated escalation reports (normal rotation, prior versions archived).
- `research/discovery/spine-check-v15-20260915.md` + `research/discovery/spine-check.md` — regenerated spine-check report (0 FATAL, `/start-project` orientation step), prior version archived.
- `_analytics/Clusters/cluster-assign-v5-20260915.md` + `_analytics/Clusters/cluster-assign.md` — regenerated cluster-validate reports from the #1606/#1707 verification runs, prior versions archived.

## 3. Decisions made

**Researcher's own decisions (not self-correctable):**
- `reconcile() must check and guarantee that strong-cluster is in sync... assign the strongs to the right cluster` — the explicit instruction behind #1606's build.
- 3 flagged data anomalies (`G1306`/`G4315`/`G3637`) confirmed T2, no IB implication, STEP-level tagging issues explicitly out of scope for the study.
- #1606 and #1707 both explicitly approved for processing/sign-off, verbatim.
- The full role-driven reading-sequence design (5 steps) and all 5 confirming decisions on it (forced not advisory, pointer separate from relational, `verb_argument` inadequate, faculty is a reflection not a tag).
- `verb_argument` cannot be postponed or parked — gates the pipeline, not carried-forward work.
- The T3 methodological history (why verbs were pulled out of characteristic-centric clusters into their own category) and the full discovery-question set a T3 role triggers.
- All 5 of #1697's open items, verbatim, across several turns (spellings, ordinal meaning, `ready_for_observations` gate, `strongs_reassigned` must warn not auto-reset, initial backfill).
- Phase B's full rebuild scope: dump old lexical records, dissolve old config, no reconciliation of old data.
- `resolved_sense` moves to a new Layer 2 stage, not a Layer 1 replacement — and the correction that Layer 2 is its own produce+capture pair, not folded into subgroup formation.
- Reviewed the real verb_argument examples and found no conclusive, consistent method — explicit instruction not to react to this yet, wants time to digest.

**Self-correctable (fixed directly, not escalated):**
- #1606/#1707/#1708's actual code fixes — each is a mechanical consequence of an explicit researcher instruction or a genuine crash, not a design choice Claude made unilaterally.
- The `G3304` mid-build self-caught correction (a transcription slip in the T-code classification script, fixed live before reporting done).
- #1709/#1710 diagnosis and closure (confirmed test artifacts, not defects).
- One escalation-tool bug found and fixed via the `-Action Correction` path (a silently-dropped comment/stale resolution on #1606's first `approved` transition) — reported transparently, not glossed over.

## 4. Open items carried into next session

- **#1705 is the explicit starting point.** The researcher's own words stand as the live state:
  looking at real verse examples does not give a conclusive, consistent method; almost every verse
  needs different treatment; some of this session's own preliminary pattern-observations were
  misplaced; the role/T-code framework may not be making the positive impact it was meant to. No
  reaction was given per direct instruction — whatever comes next on #1705 should start from
  wherever the researcher's own digestion lands, not from an assumption that the existing design
  direction (significance grading, multi-M-code relation, referent-identity widening) still holds
  as stated.
- **#1706** — still under active review. Open: pack sign-off (item 4), the new Layer 2 stage's own
  internal design (item 8 — stage name, scope grain, which catalogue questions, write path), and
  confirming "dumped" means soft-delete not a literal hard delete (item 9).
- **#1696** — held on the researcher's own sequencing, resumes only after #1706 (or an explicit
  greenlight); the "migration can proceed" vs. "I will first complete 1706" discrepancy noted mid-
  session is still unresolved, not acted on either way.
- **#1592 / #1595 / #1607** — folded into #1706's Phase B build spec; no independent action needed,
  not formally closed.
- **#1704 Phase 2/3** — match each of the 17 discovered events against the 4-part test, then compile
  the corrective-action list; not started this session (this session's work was an addition to
  Phase 1's scope, not a move to Phase 2).
- **#1701** — faculty framing resolved, but the actual replacement catalogue question still needs
  authoring; no schema work identified yet.

## 5. Git state

- Branch: `main`
- Commit: `919a69e8` — "session 20260915: Leg-3 sync guaranteed + 111 strongs classified (#1606),
  cross-run escalation ack (#1707), escalation-CLI lock retry (#1708), #1697 fully resolved, #1706
  lexical-stack build proposal consolidated + pipeline-shape corrected, #1704 role-driven-reading-
  sequence design, #1705 verb_argument raised + researched" (23 files changed)
- Push: confirmed — `4274dd4b..919a69e8 main -> main`
- `git status` post-push: `working tree clean`
