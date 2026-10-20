# Session log — 2026-10-20 — Audit and redesign of start-project and session-close

**Scope:** The study stays on hold. The researcher asked for an audit of the two session routines.
Both were described step by step from their code, a change proposal was written for each, and the
researcher answered the open points in chat. Nothing is built. The build runs in a fresh
Developer Mode session (#2173).

## 1. Escalations touched

| # | Outcome |
|---|---|
| 2173 | **Raised** (task). v1 → v11, now **in-progress with Claude** (next action: the build). Holds every researcher instruction of the session verbatim: the audit request, the start-project direction, Q1–Q3, "only 4 open escalations", reading linked files intelligently, the behaviour section being incomplete, no meaningless start-up reports, the contradictions to fix, the approval question, "proceed with the session-close design", and the second commit for the log hash. Set to ready_for_approval in v4–v8. That was premature, because approval would have completed it before session-close was designed; it was corrected in v9. |
| 2174 | **Raised** (issue, decision_required) with the researcher: escalation rule 6 `document_reference_grouping`, keep, rebuild or retire (G10). |

No other escalation was changed. Start-up ran the thread check (0 changes), the list (v178), the
threads list (v21) and the spine check (v65, 0 FATAL).

## 2. Files created or changed

- `outputs/markdown/session-routines-start-close-description-v1-20261020.md`: what both routines do, step by step from the code, with findings S1–S6 and C1–C7. S3 was corrected in place.
- `outputs/markdown/session-routines-start-project-change-proposal-v1-20261020.md`: P0 (no meaningless start-up output), P1 (read what open escalations point to), P2 (rule compliance: deliver, restate, acknowledge, prove at close), P3 (spine to close, meaning vs STEP), P4 (analysis integrity), P5 (thread audit), S-list fixes, §8a contradictions G1–G12. Edited in place (review mode).
- `outputs/markdown/session-routines-session-close-change-proposal-v1-20261020.md`: SC1–SC14, G13–G14, test plan, build order.
- `CLAUDE.md` §2: `Logs/` corrected from "historical" to live (G3).
- Generated at start or close: escalation list v178, threads list v21, spine check v65, session-close v138, threads register v25 (with the earlier versions archived).
- Memory (outside the repo): new `feedback_session_log_every_session_read_config_not_folders.md`; `MEMORY.md` compacted from 22.3 KB, with every entry kept.
- This log.

## 3. Decisions made

**The researcher's own decisions** (verbatim on #2173; the target of each is in brackets):

- Read every file the open escalations name; search the content, context and resolution fields; read only the latest version of each file (start-project proposal P1).
- Behaviour rules are read, not counted. Confirm, and name conflicts and rules not followed (P2). Then: the section was "incomplete", so it was rewritten as a compliance file plus evidence at close (P2 A–D).
- The spine check moves to session-close. Meaning completeness is checked in the three core meaning tables against what STEP holds; the parse tables stay retired (Q1; P3, SC2).
- An analysis integrity check: observations into the claims tables, and open items into the register (P4, SC4–SC5).
- Thread quality, validity and integrity checks, with disclosure rather than counts (P5).
- Per-verse placement in reading files is made mandatory (Q2).
- Session logs: the rule was not followed in October (Q3). Session-close writes the log (SC8).
- Open means raised, in-progress or re-assigned. On-hold is parked (P1 scope; G1).
- No meaningless reports at start; reports on demand (P0).
- Fix the contradictions found in rules, config and docs (§8a).
- A second commit for the session log's own hash (session-close proposal §6).

**Fixed directly by Claude:** the CLAUDE.md §2 `Logs/` line (G3); #2173's wrong on-hold and ready_for_approval states; the withdrawn S3 claim (I had read part of a folder listing instead of the setting).

**Not done here, deliberately:** every config, code and command change; these are for the #2173 build. The 46 standing register findings (G13) are left for the build's SC5 design. No session logs were rebuilt for October (no backfill unasked).

## 4. Open items carried forward

- **#2173** (Claude): the build in a fresh Developer Mode session, following both proposals' build order, then a full start and close as the acceptance test, then ready_for_approval. The resolution text from v4 is to be replaced at that point.
- **#2174** (researcher): the escalation rule 6 decision.
- **The study** stays on hold; #2172 awaits the researcher's decision. Unchanged this session.

## 5. Git state

Recorded after the push, in the second commit (decided this session).
