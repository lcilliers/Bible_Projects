# #2412 — build plan for design D (Ollama triage of surface items), v1

Basis: researcher, 2026-11-10 (#2412 v22): "we are back with 2412 ... see if Ollama can be made of good use to do all the work that can sensible be done in batches in the background", then "proceed with 2412". Design: `outputs/escalation/2412-engagement-ollama-components-design-v1-20261110.md` (design D). Developer Mode session. Everything the model answers is inferential (B:4).

## Steps (each gated by the one before)

1. **Ground truth.** The 4636 items Claude assessed in seven collections (aloud, call, deal, new, anger, godly, choose) are read from the seven assessment files (`_analytics/surfaces/working_files/engagement/engagement-<c>-assessment-20261109.json`), with the reopen decisions of the review files applied. Read-only. Triage truth: `not_relevant` = none; `relevant` (characteristic, qualifier) and `bears_on` (object, relational_target, enactment) = bearing.
2. **Prompts.** Two prompt keys in `cfg_ai_prompt` through `Ai-Control.ps1 -Action PromptAdd` (role judge): `engagement.triage` and `engagement.triage_b` (the second judge, differently worded). Answer JSON `{"bearing": "inner_being|outward_act|none", "quote": "..."}`.
3. **Module `iba/app/lib/engagementask.py`.** One question per item through `lib/aiclient.py` only: variables from `verse_lexical` and `verse` (reference, ESV text, surface, Strong's code and gloss); a check that refuses an unusable answer; subject `verse_lexical` id. No table write except the `ai_call` row.
4. **Proof run on a stratified sample first** (about 300 items, all seven collections, all truth classes), timed, on the idle server; then the agreement table (model against Claude, by class and collection, and the two judges against each other). Written to `outputs/escalation/2412-engagement-ollama-triage-test-v1-20261110.md`.
5. **Decision point (B:44).** Prompts corrected on that sample only through new versions. Whether to run the other 4336 items, the role question, the bulk job in `Long-Run.ps1` and the writer into the assessment file format (8.18) go to the researcher with the measured agreement before any is built.

## Not in this pass

No engagement writes (Record, Group, Review, Close), no change to a collection, no bulk run, no change to `Engagement.ps1`. USER-GUIDE and BUILD.md entries follow the code that is kept (governance.build_md_on_code_change).
