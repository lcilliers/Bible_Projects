# Escalation deep history

## #2158 — Unresolved verse references in the narrative register
type=issue source=narrativeregister (narrative_register.record)

**v1** (2026-10-15T13:31:48Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Unresolved verse references in the narrative register
> **comment (set this version):** narrative_register.record wrote 2 reference(s) that match no verse row. Researcher, 2026-10-13 (#2134), verbatim: "if the narrative have unresolved references then there is an error and an escalation should be created resolve it." Correct each one in its chapter file or claim source (or the reference parser, if it misread the text), then record again:
- Ch 13.1 *Majesty*: 'Job 40:10–14' read as Job 40:13
- claim C-239 source: 'Job 40:10-14' read as Job 40:13
> **context (set this version):** iba/app/lib/narrativeregister.py (parse_refs, unresolved); the rows are in narrative_citation / narrative_claim_source with verse_id NULL; Narrative-Register.ps1 -Action Check lists every current one
