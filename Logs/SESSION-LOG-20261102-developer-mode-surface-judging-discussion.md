# Session log 2026-11-02: Developer Mode declaration and the surface-judging discussion (#2354)

Session id: 1f90883d-fae6-4def-96fe-fb4c7353ce31 (Developer Mode, started 2026-11-02T12:11Z, closed 2026-11-02).

## 1. Scope
Declared Developer Mode (compliance file passes, marker set). No build was done. The session was a discussion of #2354 (concepts retry): what a (strong, surface) pair is, the count of surfaces in concepts (4,884 surfaces against 10,722 pairs), the judging prompt in `iba/app/lib/surfacejudge.py`, and two read-only Ollama trials (the word "made"). #2358 was found stale and closed. Nothing in `iba/app/db/iba.db` was changed by hand.

## 2. Escalations
- #2358 (config store incoherent, 9 errors): Claude first handed it over with options (comment v2 by Correction), which was wrong; the errors were already fixed (`ollama` and `surface_judge` are in `enum.config_module`); resolved as self-correctable, v3 completed.
- #2354 (Reset narrative): updated v16 to v20, each carrying the researcher's words verbatim (the surface-level principle, the 972 multi-concept surfaces, the dictionary method, the 10-month remark, and at close the six unrecorded messages). Assigned to the Researcher, ready_for_approval, needs follow-up 1; not completed.
- #2357 (config advisories): not touched.

## 3. Files
- `Logs/compliance/COMPLIANCE-20261102-1f90883d.md`: the session compliance file.
- `Logs/SESSION-LOG-20261102-developer-mode-surface-judging-discussion.md`: this log.
- `outputs/escalation/2358-escalation-history-v1-20261102.md`, `outputs/escalation/escalation-list-v231-20261102.md`, `outputs/escalation/escalation-context-v23-20261102.md`: generated reports.
- `iba/app/reports/session-close-v277-20261102.md` and `iba/app/reports/session-close.md`: close reports.
- `.claude/.developer-mode-active`: the Developer Mode marker.
- No code or config file changed; no BUILD.md entry is needed.

## 4. Decisions
- Researcher: the judging unit for the concept of a word is the surface; the Strong's code matters only when the uses of a surface are studied; recorded in #2354 v16.
- Researcher: the 972 surfaces in several concepts are mostly not behavioural surfaces; recorded in #2354 v17.
- Researcher: a word's behaviour is judged from its dictionary definition (a human can do it), with no Bible context and no "depends"; recorded in #2354 v18.
- Researcher: no more Ollama trials unless asked; recorded in #2354 v19.
- Claude, self-correctable: #2358 closed because its fault was already fixed and Claude's earlier hand-over was wrong; recorded in #2358 v3.

## 5. Open items
- #2354 (Researcher): the judging unit (surface or pair), the test for behaviour as against generic verbs, the source of dictionary senses, and a rule for the 972 multi-concept surfaces.
- #2354 (Researcher): the judging prompt in `iba/app/lib/surfacejudge.py` is a code literal, not a `cfg_*` row (B:6); to be fixed when the method is settled.
- #2357 (Researcher): config advisories, unchanged.

## 6. Git
- Branch: `main`.
- Commit: `0f1d432d658b80daca888ad2caeecf8d73d4503d` "session 20261102: Developer Mode declaration, #2354 judging discussion recorded (v16-v20), #2358 resolved, session log, compliance file and close reports".
- Push output: `To https://github.com/lcilliers/Bible_Projects.git   ea36b2ed..0f1d432d  main -> main`.
