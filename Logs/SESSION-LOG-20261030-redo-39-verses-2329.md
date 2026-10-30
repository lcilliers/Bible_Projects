# Session log 2026-10-30: #2329 redo of the 39 m21-asking verses (standard mode)

Session id: 5523ff98-1dd3-41df-9fa6-259a6b821182 (standard mode, /start-project).

## 1. Scope

2026-10-30: standard-mode session. Start-up, then the redo of the 39 m21-asking verses under the nine observation items (#2329, BUILD 435), checks after it (meaning-tree quote check, read-back of all 522 observations, query test), the follow-up on the held items, and the researcher's decisions that ended the observation reading (#2320 withdrawn, #2335 withdrawn, #2336 rejected) while the approach to the study is rethought. No code or config changed.

## 2. Escalations

- #2329 (Phase 1 observations: fit for purpose): taken up to in-progress (v25), progress comment (v26), handed over ready_for_approval with the result (v27), approved by the researcher (v28), closed completed (v29).
- #2320 (Build Analysis_phase_1 to specification v4): decision handed over after the hold lifted (v34), in-progress on the researcher's "2320 approved for your action" (v36), handed back with the gate finding (v37), withdrawn on the researcher's instruction (v38).
- #2335 (raised this session, nuance rows and route values): raised, handed over with its options (v2), approved (v4), withdrawn on the researcher's instruction (v5).
- #2336 (raised this session, reading every verse does not scale): raised, handed over with options (v2), comment with the researcher's words (v3), rejected as withdrawn (v4).
- #2259 (v9) and #2161 (v12): comment that the redo hold is lifted and that each waits for the claims phase (#2315).
- #2334 (asking record is free text): referred to in the result; not changed.
- Backlog read at start and at each stop (#2171, #2172, #2235, #2268, #2276, #2278, #2280, #2303): acknowledged, untouched; none due.

## 3. Files

- `_analytics/Clusters/M21 - fasting-piety/m21-asking/m21-asking.json`: the scope JSON, 39 verses reopened, observed and recorded.
- `outputs/escalation/2329-redo-result-v1-20261030.md`: the result of the redo (per-verse time table, checks, claims test, nuance proposals, limits).
- `Logs/compliance/COMPLIANCE-20261030-5523ff98.md`, this log, `iba/app/reports/session-close-v*-20261030.md`.
- Escalation exports the scripts wrote under `outputs/escalation/` (list, context, history, thread audit), with the previous versions moved to `outputs/escalation/archive/`.
- Database `iba/app/db/iba.db`: 522 live Analysis_phase_1 observations with their nodes on the 39 verses, 135 old-form observations soft deleted, observation changes in `ib_observation_change`.
- Named snapshot before the redo: `iba/app/db/snapshots/kept/iba-20261030T102648Z-2329-redo-39-verses.db`.
- Scratch helpers (not project files): in the session scratchpad.

## 4. Decisions

Researcher's own:
- "proceed with 2329": run the redo; recorded in #2329 v26.
- "I approved 2329 it is for your follow up": #2329 approved; recorded in #2329 v29.
- "2335 approved for your follow up": approved, then "2335 is withdrawn"; recorded in #2335 v4 and v5.
- "2320 approved for your action": taken as option A; the gate refused it; recorded in #2320 v36 and v37.
- "if 230 verses are going to be so many tokens then it is not feasible ... it will take years": recorded in #2336 v1.
- "2320 can now be marked as withdrawn ...": recorded in #2320 v38 and #2336 v3.
- "2336 is rejected. I need to rethink how to approach the study": recorded in #2336 v4.

Claude's, within the approved plan and not new design:
- Judg 1:14 uses the live observations of Jos 15:18 as existing with its own nodes (RW-03); recorded in `outputs/escalation/2329-redo-result-v1-20261030.md` section 1.
- Route B on all 115 party and link observations, from rule 72 (inferential, B:4); recorded in `outputs/escalation/2329-redo-result-v1-20261030.md` section 6 and #2335 v2.
- Self-correctable: four meaning-tree quotes and six observation wordings restated after the checks, each by Reopen, Observe and Record with the reason in `ib_observation_change`; recorded in `outputs/escalation/2329-redo-result-v1-20261030.md` section 3.

## 5. Open items carried

(#2329 completed and #2320, #2335, #2336 withdrawn are in section 2. The approach to the study is with the researcher; `governance.study_status` still reads ACTIVE and was not changed.)

- #2334 (the kind, answerer and outcome of an asking are free text): raised before this session, with the researcher.
- #2259 and #2161 (Claude): held for the claims phase (#2315).
- The parked items assigned to Claude (#2171, #2172, #2235, #2268, #2276, #2278, #2280, #2303): untouched.

## 6. Git

(to be written after the first commit)
