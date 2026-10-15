# Escalation deep history

## #2151 — Unresolved verse references in the narrative register
type=issue source=narrativeregister (narrative_register.record)

**v1** (2026-10-15T04:52:32Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Unresolved verse references in the narrative register
> **comment (set this version):** narrative_register.record wrote 2 reference(s) that match no verse row. Researcher, 2026-10-13 (#2134), verbatim: "if the narrative have unresolved references then there is an error and an escalation should be created resolve it." Correct each one in its chapter file or claim source (or the reference parser, if it misread the text), then record again:
- Ch 10.14 *The proud brought low, the lowly raised*: 'Job 40:11–14' read as Job 40:13
- claim C-181 source: 'Job 40:11-14' read as Job 40:13
> **context (set this version):** iba/app/lib/narrativeregister.py (parse_refs, unresolved); the rows are in narrative_citation / narrative_claim_source with verse_id NULL; Narrative-Register.ps1 -Action Check lists every current one

**v2** (2026-10-15T04:53:02Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Job 40:13 has no verse row in iba.db. Per governance.verse_gap_by_design (researcher ruling 2026-07-29) a missing verse row is by design, not a data error: the range Job 40:11-14 in 10.14 (The proud brought low, the lowly raised) and in claim C-181 is correct as written (the quoted words are from 40:11-12 and 40:14). Recommended: no change to the text or the claim; close.
> **resolution (set this version):** No fix needed: verse gap by design (Job 40:13 not in iba.db). Recommend closing.

**v3** (2026-10-15T05:14:41Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):** noted
