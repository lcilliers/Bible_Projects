# Escalation deep history

## #2216 — Ledger verses cited with no strand word in them
type=issue source=researcher

**v1** (2026-10-22T10:06:14Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Ledger verses cited with no strand word in them
> **comment (set this version):** From the #2172 catch-up plan, decision 2 (outputs/escalation/2172-catch-up-plan-v1-20261022.md section 3): an October ledger row can cite a verse that holds none of the strand's words (cited for its setting). Researcher, chat 2026-10-22 (verbatim): "Q2 - this should not happen. report it to investigate.  Use open items to raise it." To investigate: how many ledger verses across the five October row ledgers carry no strand word, which rows cite them, and how they came to be cited (the pull, the reading, or a later edit). Count not yet known: none has been listed. Example seen read-only in the origin of thought ledger: Ps 8:3 is cited for "consider", but the word there is H7200 (see), not a thought word. No catch-up import grounds such a verse until this is settled.
> **context (set this version):** outputs/escalation/2172-catch-up-plan-v1-20261022.md; _analytics/cross-cluster-web/origin-of-thought/origin-of-thought-observation-ledger-v2-20261001.md; #2172

**v2** (2026-10-22T10:06:24Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Correction to v1: the Ps 8:3 example is wrong. The ledger (_analytics/cross-cluster-web/origin-of-thought/origin-of-thought-observation-ledger-v2-20261001.md, Checks done) records that Ps 8:3 is H7200 (see) and that the discussion's row LOSES that example, so it is not a cited ledger verse. No example is yet in hand; the investigation lists them.

**v3** (2026-10-22T11:21:52Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Listed by catch-up B (outputs/escalation/2172-catch-up-b-v1-20261022.md, sections 'Verses with no strand word' and 'Rows with no grounded verse' per strand): 1,062 cited verses hold none of their strand's words -- fear 123, anger 762, life-death 134, origin of thought 43 -- and 45 rows are left with no such verse and were not imported (fear 16, anger 8, life-death 16, origin of thought 5). The strand words are the unit pulls' Strong's codes. Most of anger's 762 are from the anger strand ledger of 1 October (AN), which predates the unit pulls (_analytics/Clusters/M02 - anger-wrath/anger-strand-observation-ledger-v1-20261001.md). Next for this item: sort them by cause (a word outside the unit pulls, a verse cited for its setting, a citation slip).
> **context (set this version):** outputs/escalation/2172-catch-up-b-v1-20261022.md

**v4** (2026-10-22T12:54:20Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Five rows of anger at the inner seat cite no verse holding an anger strand word, so they were not recorded (same rule as catch-up B): MS-03 (Neh 5:7; the anger is in 5:6), MS-18 (Job 32:18, 20; anger in 32:2-5), MS-19 (Psa 106:33; anger in 106:32), MS-24 (Pro 22:25; the angry man in 22:24), MS-26 (1Sa 1:10; provocation in 1:6-7). Each carries its anger in a neighbouring verse the ledger row did not cite. Detail: outputs/escalation/2172-anger-seat-basis-v1-20261022.md.

**v5** (2026-10-23T12:09:38Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **context (set this version):** outputs/escalation/2216-2217-plan-v1-20261023.md
> **resolution (set this version):** Decision sought: how to finish this item. Checked 2026-10-23 (read-only): a reading Record now refuses an observation whose verse does not hold its strong (iba/app/lib/strandreading.py check_observations), so the October pattern cannot recur; the fear, anger and life-death ledgers are in the reading index, so their 1,019 cited verses come up as read_in_files_only gaps (inferential: from the gap guide, not yet run); the origin-of-thought ledger is outside reading_index.roots, so its 43 verses and 5 rows would not. Option A: build a registered read-only step that sorts the 1,062 verses by cause (word outside the unit pulls / neighbouring verse holds the word / neither), then dispose. Option B (cheaper): no cause sort; close with the finding above, each verse left to the reading that reaches it, and add _analytics/cross-cluster-web/origin-of-thought to reading_index.roots (configmaint.propose) so its 43 verses are not lost. Approve A or B; either returns to Claude to carry out. Detail: outputs/escalation/2216-2217-plan-v1-20261023.md

**v6** (2026-10-23T12:11:42Z, Researcher) state=re-assigned next_action=approved assigned_to=Claude
> **comment (set this version):** Option B
