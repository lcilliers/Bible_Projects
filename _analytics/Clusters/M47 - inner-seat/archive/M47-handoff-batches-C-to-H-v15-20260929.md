# M47 → cluster phenomena — handoff (v15)

**Date:** 2026-09-29 · **Supersedes:** v14 (`archive/`). Earlier history is in v1–v14, and is not repeated here.
**Session log:** `Logs/SESSION-LOG-20260929-m02-unit1-and-hardening-investigations.md`.

## Where things stand

- **M02 unit 1 (human anger) is complete and approved.**
  - The reading is `../M02 - anger-wrath/wa-cluster-M02-phenomena-v2-20260928.md`: 35 phenomena, 246 verses, 31 seated verses.
  - The ledger is `wa-cluster-M02-phenomena-ledger-v2-20260928.csv`. It has all 681 M02 verses, with columns `side` and `phenomenon`.
  - Escalations: #1886 (split), #1887 (Gen–Job), #1888 (Psa–Rev). All closed.
- **Psa 95:8 was moved from divine to human (Meribah, §12)** by the researcher's final ruling. This is applied in ledger v2.
- **Still open from #1888, point 2:**
  - **Researcher, verbatim:** "yes it may impact Batch A - but not in the way you portrayed it."
  - **The portrayal:** in the wisdom texts, spirit is the seat where anger rises and is ruled, and heart is where it is kept (v2 §38 point 2).
  - **No Batch A revisit note has been written.** Ask the researcher how it bears on Batch A before touching Batch A.
- **Investigations spun off during unit 1:**
  - **#1890, approved.** No text hardens God's own heart. Findings and ledger are in the M02 folder: `wa-investigation-god-hardening-own-heart-*`.
  - **#1892, first pass approved.** God's heavy hand: the heaviness is felt by those under it, and the sources named are righteousness together with steadfast love (`wa-investigation-god-heavy-hand-perception-source-v1-20260929.md`).
  - **#1893, on hold (signpost).** Resume when the inner being acting through the hands is investigated. It covers the fuller God's-hand pass and a special cluster scan. It is also in memory as `project_signpost_hands_inner_being`.
  - **#1891, on hold with Claude.** The `iba.db` verse gap: 29,760 verses against about 31,100. **Queued behind M02 unit 2** by the researcher. Evidence so far: STEP matches `iba.db` verse for verse for 43 codes.

## NEXT STEP — M02 unit 2: divine anger as borne by the human

**Scope: 394 verses.** These are the ledger v2 rows with `side` = divine (302), B3 (11), B6 (4) and B7 (77, which excludes Jon 4:2, already read in unit 1).
- **B3:** a human agent carries out God's wrath.
- **B6:** God's anger at Moses.
- **B7:** a human addresses God about his anger, or acts toward it.

**The subject is the human side** (`hib.set`, prose section 1090). Read how the human **bears, provokes, pleads against, fears, is filled with, or is the vessel of** God's anger. God's anger itself is not the object.

**Proposed split** (not yet ruled on; confirm with the researcher first): Genesis–Job first, then Psalms–Revelation, as in unit 1. Report the size of each part before reading. **Unit 1 took one review per part.**

**Do it the way unit 1 was done:**
1. **Recreate the scratch scripts** (session scratchpad, `temp_` prefix, run as `.py` files):
   - an extract of the rows filtered by side
   - a context reader (±3 for Genesis–Job, ±2 for Psalms–Revelation; follow narratives further)
   - a batch citation finder, which greps `M47-x-*batch*.md` and the M02 pilot
   - a verse reader

   The unit-1 versions were lost with the scratchpad, and are described in the session log §4.
2. **Read in canonical order.** Let phenomena emerge. Answer the five questions for each. Add a Seat block in the M20 v3 form. **Cite, don't redo**, the M47 batches, the pilot, and M02 phenomena v2.
3. **Before quoting any verse, read it. Before writing "new", search the batches.** Unit 1 needed several corrections for claims made from unread verses or unchecked batch coverage. Unit 1 also used verse-by-verse B-code lists, which worked.
4. **Output:** `../M02 - anger-wrath/wa-cluster-M02-phenomena-v3-{date}.md` (units 1 + 2), or a separate unit-2 document. **Ask the researcher which.** Update the ledger to v3. Commit and push. Set the escalation to ready_for_approval with `-Resolution` filled in and `-AssignedTo Researcher`. **Approving an escalation closes it, so raise a follow-on escalation for each next part.**

**Pointers already waiting for unit 2 (from unit 1):**
- §13: God's anger at Uzzah, and Num 11:10
- §15: the prophet as vessel (Jer 6:11; 15:17; Eze 3:14): God's anger borne as suffering, not action
- §31: the parable master's anger, placed in the hearer's heart (Mat 18:35)
- §34: the cup that comes round (Hab 2:16; Rev 14:10)
- #1892:
  - Psa 32:3–5 (the heavy hand, and confession)
  - Lam 3:7 against 3:33 ("does not afflict from his heart")
  - Isa 59:1–2 (sins that separate)
  - Mic 7:18 (he "does not retain" his anger)
- B7 already contains most of the lament psalms and intercessions: Exo 32:11–12; Deu 9:18–20; Psa 6:1; 38:1–3; 88:7, 16; 90:7–11 …

## Rules (carried forward)

- **Phenomenon level, emergent.** No preset list. Every verse accounted for, with no brushing over.
- **Revisit is the rule;** interaction comes first.
- **Filing** follows the `_analytics/Clusters/{code} - {short name}/` rule (GOVERNANCE.md §83). The same base name means a version bump. Prior versions go to `archive/`.
- **Data:** `iba/app/db/iba.db`, read-only.
  - `verse_lexical.role` holds the M-codes as JSON.
  - STEP needs **exact lettered** Strong's codes (H2388G, not H2388). The client's `_resolved_strong` drops the lettered variants, so call `_search_range` / `_paginate_all` directly.
- **Text filters must be case-insensitive.** One unit-1 bug missed "My heart …".
- **`AskUserQuestion` is banned.** Ask in plain chat, or in a `.md` review file.
