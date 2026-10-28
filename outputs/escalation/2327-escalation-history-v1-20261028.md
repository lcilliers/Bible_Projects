# Escalation deep history

## #2327 — Record: existing party or link finding is refused
type=issue source=researcher

**v1** (2026-10-28T08:59:50Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **short description (set this version):** Record: existing party or link finding is refused
> **comment (set this version):** Researcher, chat 2026-10-28 (verbatim): 'proceed with 5 consecutive batches, but record and feedback the time it takes to process every batch'. Claude: in batch 5 of reading m21-asking the verse Judg 1:14 repeats the text of Jos 15:18 word for word, so its four findings name the live observations 20725 to 20728 as existing (one finding, many nodes, RW-03). Reading.ps1 -Step Record then fails in both directions: without a route the check says 'another party is stated but no observation of the kind party with its route' (iba/app/lib/reading.py, the after map takes the route from the sheet finding at line 609), with a route it says 'an existing finding takes nodes only' (iba/app/lib/observationrecord.py, the check of an existing finding). A party or link observation that already exists therefore cannot gain the nodes of a second verse, which is the case RO11 and RW-03 require. Nothing was written; Judg 1:14 stays in hand. Fix: for an existing finding take the kind and route from the live observation row. A correction of the build to the approved design, no new decision.
> **context (set this version):** iba/app/lib/reading.py; iba/app/lib/observationrecord.py; outputs/reading/m21-asking/m21-asking.json
