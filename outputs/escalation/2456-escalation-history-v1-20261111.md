# Escalation deep history

## #2456 — Inspect the 72 phrases flagged phrase_no_match
type=task source=researcher

**v1** (2026-11-10T16:38:42Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Inspect the 72 phrases flagged phrase_no_match
> **comment (set this version):** From #2437 (closed 2026-11-10). 72 phrases of collection a are reached by neither the English-word route nor the own-Strong's-code route and carry an open surface_flag of kind phrase_no_match (list: select from surface_flag where kind='phrase_no_match' and status='open'). Researcher, verbatim: 'I seriously question the validity of those that does not match.' and 'no match should be flagged for inspection.' Next: the researcher inspects them; settling a flag sets it settled.

**v2** (2026-11-11T11:11:22Z, Claude) state=in-progress next_action=review assigned_to=Researcher
> **comment (set this version):** Researcher in chat 2026-11-11, verbatim: '2458, 2457, 2456, 2387 is all completed but I cannot approve it - prepare it properly for approval'.

**v3** (2026-11-11T11:11:22Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **context (set this version):** surface_flag kind phrase_no_match status open (72 rows); iba/app/USER-GUIDE.md section 8.14 (AttachPhrases)
> **resolution (set this version):** Approval sought: close #2456 as inspected by you (your statement in chat 2026-11-11: completed), and choose what happens to the 72 flags.
Checked now in the tables: all 72 surface_flag rows of kind phrase_no_match are still status open (made 2026-11-10T15:52:21Z); no event has settled any; the USER-GUIDE documents no tool that settles them. The outcome of your inspection (which of the 72 phrases are valid, which not) is not recorded anywhere I can read, so I cannot state it.
Options: A (recommended): close the item now; the 72 flags stay open as the standing list for the collection work (no write). B: close it and settle all 72 flags as inspected: a bulk write of 72 rows, each with a surface_event, on your instruction only; it cannot tell a phrase you accepted from one you rejected. C: tell me in chat which phrases are valid and which not, and I record that per phrase before closing.

**v4** (2026-11-11T11:12:33Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):**   approved
