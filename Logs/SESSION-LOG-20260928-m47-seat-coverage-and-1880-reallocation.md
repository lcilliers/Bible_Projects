# SESSION LOG — 2026-09-28 — M47 status, seat coverage, and the #1880 re-allocation

**Session:** Claude Code desktop (working directory `G:\My Drive\Bible_study_projects`; files written to `C:\Bible_study_projects`). This continues the same chat as `SESSION-LOG-20260928-m47-batch-h-and-fg-revisits.md`.
**Entry point for the next session:** `outputs/markdown/M47-handoff-batches-C-to-H-v8-20260928.md`.

---

## 1. What was done

| # | Work | Output | Commit |
|---|---|---|---|
| 1 | One-page M47 status overview | `outputs/markdown/M47-status-overview-v1-20260928.md` | `b28bf5b9` |
| 2 | **Seat-coverage investigation.** No M-cluster is absent from the M47 angle, but only **10%** of M-cluster verses (2,404 of 24,365) name a seat word. 31% have one within ±3 verses; 59% have none nearby. Also found: `strong_verse` is incomplete, so `verse_lexical` is the source. A plan with tie classes and a pilot was proposed. | `research/investigations/M47-seat-coverage-and-unseated-verses-v1-20260928.md` | `dbaa42fe` |
| 3 | **T-code vs M-code question.** Answer: it matters (die, death, say, *qereb*, body parts); a JSON spec is feasible; the risk is low if it is done first. | `research/investigations/M47-t-code-to-m-code-question-v1-20260928.md` | `3c563ce9` |
| 4 | **Re-allocation register.** 72 items (114 Strong's) harvested from every flag in the M47 files, validated against live `cluster_strong`. **Escalation #1880** raised. | register v1 → v2; spec v1 → v2 → v3 | `7ec0c668`, `35ec63b9`, `d85ddd65` |
| 5 | **#1880 prepared for approval.** Open items resolved to proposals (C-R5 by a STEP check). Apply script built; dry run clean. | `iba/app/migration/apply_m47_reallocation_1880_v1_20260928.py` | `d85ddd65` |
| 6 | **#1880 applied** after researcher approval. DB backup; migration live (88 strongs); `verse_lexical.role` rebuilt for 66 books (7,445 codes updated, 0 removed); 0 role mismatches; 0 stale clusters. | BUILD.md §333 | `f8148f18` |
| 7 | **M47 inputs regenerated.** The method was validated to reproduce the v1 files exactly from the backup. Surface file identical; pairs 8,605 → 8,393; **155 genuinely new pairs in 115 verses** (the death side of Life & Death). Spirit CSV v2 (Psa 106:33 → U). Handoff v8. | `research/investigations/cluster-M47-*-v2-20260928.csv`, delta CSV, handoff v8 | `f8148f18` |
| 8 | Session close. #1881 raised: `session.close` reads a stale transcript. | this log; `iba/app/reports/session-close-v11-20260928.md` | (this commit) |

**DB writes:** `cluster_strong` (#1880; 111 rows) and `verse_lexical.role` (7,445 codes), both via governed routes. The backup is `iba/app/db/iba.db.pre-1880-m47-reallocation-20260928.bak`.

## 2. Researcher direction given this session (verbatim)

1. "write me a one-page overview of where M47 stands"
2. "before synthesizing, it seems that we need to first exploring a different angle. If I understand it correctly then the M47 work was about where inner being words explicitly interacts/relates to the seat. It would be interesting to know if there are any clusters that have not been included in this angle at all. Related to it, should be not explore each cluster separately, with a special emphasis on the verses that have no ties to the seat. The ties may be implicit, through cross correlation, but it may also not tie back at all - and what does that tell us. I think this work need to be done before batch H can take place, and maybe the sythesis will be redefined by then."
3. "and one more preparatory question. Does it matter that some terms are currently in T-codes, and should be in M-codes. Would it make sense for you to run through the M47 work and prepare a json that can be handed to VS code to update all the tables. Is there a risk that it would negatively impact any work already done?"
4. "1 - yes draft the list; 2 - if you have access, then apply it, as long as you follow governance and the configs 3 - yes, anything identified in the M47 work and the batches that flags a re-allocation should be included."
5. #1880 v2: "proceed to prepare this excalation for ready for approval"
6. "approved #1880 — proceed with the apply" (#1880 v4: "approve to finalise")
7. "first do a session close, then will start with a new chat and handoff v8"

## 3. Decisions made

- **Order of work:** re-allocation (done) → delta revisit → seat-coverage tie-profile and pilot → synthesis, which may be redefined. Batch H was already complete, so "before batch H" was read as "before the synthesis".
- **#1880:** all 72 items approved as proposed; no exceptions. Among them:
  - "die" and "death" dual-coded into M25
  - body parts moved T2 → T14; *splanchna* to T14 + M50
  - "say" (H0559) and *qereb* not re-coded; they are to be handled as seat-coverage tie classes
- **Batch A R7 closed** by option (b): one consolidated register.
- Applied **in this environment**, not handed to VS Code (researcher: "if you have access, then apply it").

## 4. Design points debated

- **Move or add.** The dual-code precedent (H0639G M02 + T14) favoured **adding** M-codes and keeping T-codes wherever the T identity is true (death as realm; die as operation).
- **Word-level or sense-level.** Re-coding every "say" would flood an M-cluster (4,340 verses); the angle is widened instead.
- **Destination checks against cluster descriptions** reversed three draft proposals: the poverty words stay in M09; "teach" goes to M16, not M15; "be quiet" stays in M33.

## 5. Skipped / deferred

- **Seat-coverage plan §6 decisions** (tie classes, body-seat list, pilot clusters, T-code angle): not yet answered. They are needed before Step 1.
- **Death-side delta revisit** (155 pairs; Batch G → v3): next session.
- **M67** gained H7423B and H5647I; its readiness check must run before its reading resumes.
- **E-R6** (the faith family across M13 / M31 / M19): cluster-structure review not raised.
- **`cluster-M47-other-m-code-cooccurrence-20260927.csv`** is stale and was not regenerated.
- **Manifest rebuild skipped:** `scripts/build_file_manifest.py` does not exist under `C:\Bible_study_projects`.

## 6. Session-close checks

- `Session-Close.ps1` → `iba/app/reports/session-close-v11-20260928.md`: 0 gaps.
- **But it read an earlier session's transcript** (session `753f0db2…`), so it missed #1880 and today's `iba/app` changes. Checked by hand:
  - #1880 v1–v5 complete: researcher words verbatim, proposal, approval, outcome, deferred items
  - the new migration script is covered by BUILD.md §333
  - no GOVERNANCE.md, CLAUDE.md or USER-GUIDE.md change is required
- The defect is raised as **#1881** (self-correctable, not fixed here).

## 7. Next

New chat from handoff v8:
1. Death-side delta revisit (Batch G v3).
2. Researcher decisions on the seat-coverage plan §6 → tie-profile → pilot.
3. Synthesis.
