# Session Log — 2026-09-14 (continued)

**Scope:** Continuation of today's earlier sessions (see `SESSION-LOG-20260914-ib-observation-node-round-1692-approved-phantom-visualization.md`
and `SESSION-LOG-20260914-answer-stage-quality-review-and-lexical-bypass-finding.md`). This phase, after
a `/clear`: ran the standard `/start-project` orientation (spine clean, 0 FATAL; STEP up; IBA READY);
recorded the researcher's confirmed verse-lexical pipeline shape (Layer 1 as a subgroup-stage
precondition, Layer 2 folded *into* subgroup formation rather than run as a prior pass, subgroup output =
subgroups + membership + catalogue-question `ib_observations`) on #1607/#1691/#1682; assembled and
published a full status/open-items register across all 25 open lexical escalations
(`outputs/markdown/lexical-verse-lexical-status-and-open-items-20260914.md`); gave a requested macro-plan
opinion (three risks named: `role`/T-code redesign as a single point of failure, reading-stage throughput
unproven at scale, catalogue-question architecture possibly needing to precede rather than follow the
subgroup-stage build) and raised the strategic alignment point on #1701; raised and then substantially
corrected #1703 (adjacent-verse-context resolution — the existing `passage` table was wrongly proposed as
a candidate mechanism, withdrawn per the researcher's correction that it is book-reading/debate-pipeline
shaped, not subgroup-reading shaped); fixed and closed escalation #1560 (three dead bare `cluster_strong`
codes); and, the largest piece of this phase, ran a full three-phase discovery pass under new escalation
#1704 mapping every one of the **98 live catalogue questions** to the analytic "event" (data-surfacing
mechanism) each one needs — Phase 1a (structural/config sweep), Phase 1b (corrected pass after the
researcher flagged it was too light on T3–T15 role/movement/web events), Phase 1c (full exhaustive sweep,
no sampling, per explicit researcher instruction). 17 distinct events identified, every one traced to
specific question codes. Session closes here per researcher instruction (concern: unattended machine
restart overnight) — Phase 2 (match each event to the 4-part completeness test) is the next session's
starting point.

## 1. Escalations touched, by id, with outcome

| # | Outcome this session |
|---|---|
| **#1560** | Fixed and **completed**. Researcher confirmed the correction (T8, not T7; real membership belongs on `G1135G`/`G1135H`/`H0802G`/`H0802H`/`H0802I`, not the bare codes). Applied via the registered `apply_1598_cluster_batch.py` tool: 3 dead bare codes soft-deleted (`G1135`/T8, `G2424`/T7, `H0802`/T8 — none had a `strong`-table row or any span occurrence), 5 suffixed codes relocated `T2`→`T8` (they existed with real occurrences but were misfiled as excluded). Verified live before and after, not just trusted the tool's own report — corpus-wide re-check afterward confirmed **zero** remaining live `cluster_strong` codes with no real span occurrence, answering the researcher's own follow-up question. `G2424J` (1 occurrence, ambiguous Jesus/other) deliberately left untouched, researcher confirmed via STEP it is correctly `T8`. Researcher approved v3. |
| **#1589** | Updated (v1→v2) — sharpened the original 6-of-15-undefined `note_type` finding into a full three-way coverage table (config / code / catalogue-question link) by checking `lexicalenrich.py`'s actual structural checks and `lexicalenrichgenerate.py`'s LLM prompt live, not just `cfg_method_rule`. New finding: `chain`/`idiom` are code-enforced with **zero** config definition anywhere — code ahead of config, the opposite drift direction from the original finding. Confirmed zero structural link from any `note_type` to any catalogue question, in any form. Spawned #1704. Still `in-progress`/`review`. |
| **#1607** | Updated (v14→v15) — recorded the researcher's confirmed pipeline shape verbatim: Layer 1 is a hard precondition on the cluster-subgroup stage; Layer 2 lexical judgement now runs *as part of* subgroup formation, not as a prior independent pass; subgroup-stage output = subgroups + membership + catalogue-question-driven `ib_observations`; the reading stage takes, per subgroup, that subgroup's own `ib_observations` plus the raw lexical for its verses. Directly operationalizes v14's own closing note and answers #1691 v16's open "subgroup stage value" question. Still `in-progress`/`review`. |
| **#1682** | Cross-referenced (v18→v19) — same pipeline-shape record, parent-thread pointer. No new design decision. |
| **#1691** | Cross-referenced (v16→v17) — confirms the "subgroup" stage value's scope specifically (catalogue-question-driven observations, not just incidental findings). No new design decision. |
| **#1701** | Updated (v2→v3) — strategic cross-reference: the cluster-reading data model built this session (family/subgroup, `ib_observation`/`ib_node` as a relational graph, non-destructive synthesis) is genuinely process/relational-shaped and already surfacing emergent cross-family patterns unprompted; the catalogue question set this escalation critiques is the one piece that does not yet reflect that. Recommended #1700/#1701 be treated as a prerequisite gate on process-(d) trustworthiness, not parallel background work — not decided, researcher's own call on sequencing. |
| **#1703** | Raised (v1), then substantially corrected (v2) same session. Original framing: adjacent-verse-context needs are flagged, not fetched (#1682 process d default); rate unmeasured (one data point, 4 flags in one family); no resolution mechanism defined; proposed the existing `passage`/`verse_passage` structure as a candidate lookup mechanism. **Researcher correction, v2**: `passage` is a product of the retired/gated #737 debate pipeline, built on a book-reading premise — wrong shape entirely for subgroup-based reading, where the verse that actually resolves a need may not be adjacent at all. Candidate withdrawn; the real resolution mechanism has to be content/relevance-driven, not proximity-driven — genuinely unresolved, not just unreliable. Still `in-progress`/`review`. |
| **#1704** | Raised (v1) as the dedicated escalation for the analytic-event inventory, per explicit researcher instruction to pull the scattered `note_type`/config/code/catalogue drift together into one place with every corrective action documented. Updated 3 times this session (v1→v4) across Phase 1a (structural/config sweep — 5 non-communicating event vocabularies found: `note_type` 15 values, Layer 1 mechanical columns, reading-stage tags 8 values, answer-stage flags 2, subgroup-stage observations unnamed), Phase 1b (researcher correction — too light on T3–T15 role/movement/web events; re-read T1.4/T2.7/T2.10/T4/T5/T6/T7 in full, found `directional-party-frame` as the single largest gap, plus `T3-operation-surfacing`, `T14-body-part-surfacing`, and a **retired** cross-characteristic co-occurrence mechanism), and Phase 1c (researcher instruction — no sampling, map every question; all 98 live questions read and accounted for, 17 total events identified, one genuine design tension flagged for the researcher rather than papered over — T2.1's constitutional-level vocabulary has no T-code referent class at all, and its one prior attempt, the retired Inner-Faculties tier, was already judged conceptually wrong). Full record: `iba/docs/1704-analytic-event-inventory-phase1-discovery-v1-20260914.md`. Still `in-progress`/`review` — Phase 2 (match each event to name/config/code/purpose) is the explicit next step. |

## 2. Files created or changed

- `outputs/markdown/lexical-verse-lexical-status-and-open-items-20260914.md` — new. Full status register across all 25 open lexical escalations, grouped, with a suggested closing sequence.
- `iba/docs/1560-cluster-reallocation-v1-20260914.json` — new. The reviewable payload applied via `apply_1598_cluster_batch.py` to fix #1560.
- `iba/docs/1704-analytic-event-inventory-phase1-discovery-v1-20260914.md` — new. Phase 1a/1b/1c discovery, built incrementally across the session (edited in place per review-mode convention, not versioned until the researcher approves).
- `outputs/escalation/escalation-list-v81-20260914.md` + `1560-escalation-history-v1-20260914.md` + `1589-escalation-history-v1-20260914.md` — regenerated escalation reports (normal rotation, prior versions archived to `outputs/escalation/archive/`).
- `research/discovery/spine-check-v14-20260914.md` + `research/discovery/spine-check.md` — regenerated spine-check report (0 FATAL, `/start-project` orientation step), prior version archived.

## 3. Decisions made

**Researcher's own decisions (not self-correctable):**
- Macro-plan opinion requested and given (workable, three named risks) — researcher confirmed agreement and volunteered that volume/batching is already gated, removing the throughput-feasibility part of that concern (mechanically, not the separate "how long will it actually take" question).
- Adjacent-verse-context resolution: the `passage` table candidate is **wrong**, corrected by the researcher directly — book-reading/debate-pipeline shaped, not applicable to subgroup-based reading; the real need may not be adjacent at all.
- #1560: "should be T8... G2424 and H0802 should be resolved in the same way" — the researcher's own correction and generalization instruction, executed and approved.
- `G2424J` confirmed correctly `T8` (researcher checked STEP directly) — no change needed, a loose end closed, not carried forward.
- Full verse-lexical pipeline shape (Layer 1/Layer 2/subgroup/reading) given verbatim, recorded on #1607/#1691/#1682.
- #1704 raised at the researcher's own explicit instruction, with the 3-vector discovery methodology and 3-phase (discover/match/corrective-actions) process specified by the researcher, not proposed by Claude.
- Two explicit corrections to the discovery work itself, both acted on immediately: (1) Phase 1a was too narrow, missing the T3–T15 role/movement/web dimension entirely; (2) Phase 1b still wasn't exhaustive enough — "we are not looking for samples... map events for every question eventuallity."
- Session-closing instruction: write this session log and ensure escalations are up to date before stopping, due to the risk of an unattended overnight machine restart.

**Self-correctable (fixed directly, not escalated):**
- #1560's actual DB fix (3 soft-deletes, 5 relocations) — the design decision was the researcher's own (verbatim instruction), the execution (which registered tool, exact payload, live verification) was Claude's, reported transparently including the one part of the researcher's stated condition that turned out not to be true (the suffixed codes were not already in T8, they were in T2) before acting on it.

## 4. Open items carried into next session

- **#1704 Phase 2** is the explicit priority: match each of the 17 discovered events against the 4-part test (name / config / code / purpose) and separate genuine gaps from things that are actually fine. Phase 3 (compile the corrective-action list) follows once Phase 2 is done.
- **#1589** — still open, folded into #1704's broader scope; not independently resolved.
- **#1607 / #1682 / #1691** — sign-off pack still incomplete (#1691/#1696/#1697 not yet approved; #1690/#1692/#1693 already are). The confirmed pipeline shape from this session is the target for #1690/#1691/#1693 to build against, nothing built yet.
- **#1701** — deliberately parked by the researcher ("we will come back to this"); now also carries this session's sequencing recommendation (treat #1700/#1701 as a prerequisite gate on process-(d) trustworthiness).
- **#1703** — genuinely unresolved: rate unmeasured, and the resolution mechanism needs to be content/relevance-driven, with no candidate identified yet (the proximity-based one was withdrawn).
- **#1526** — reading-pacing/anchor-verse strategy still on hold at the researcher's own instruction; the "can the pipeline handle volume" concern is resolved (batching), the "how long will it actually take" question is not.
- **Two items worth flagging for whoever picks up #1704 Phase 2**: (1) T6.3's dependency on the retired `lexical_code_class` `connective_causal` granularity needs checking — did it survive the migration into the flat `T6` bucket; (2) T2.1's constitutional-level vocabulary gap is a design tension (no T-code referent class, and the one prior attempt was retired as conceptually wrong per #1598/#1701), not a mechanical fix — needs the researcher's own read before Phase 2 tries to "solve" it as if it were an ordinary gap.

## 5. Git state

- Branch: `main`
- Commit: `d34c8fdc` — "session 20260914 (cont.): verse-lexical pipeline shape confirmed (#1607/#1682/#1691), #1560 fixed and closed, #1703 raised and corrected, #1704 analytic-event inventory Phase 1 (a/b/c) complete" (11 files changed)
- Push: confirmed — `f181b2c6..d34c8fdc main -> main`
