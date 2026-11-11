# Escalation deep history

## #2387 — Units in reports and readers; held rows; shared rows
type=task source=researcher

**v1** (2026-11-07T17:46:00Z, Claude) state=on-hold next_action=review assigned_to=Researcher
> **short description (set this version):** Units in reports and readers; held rows; shared rows
> **comment (set this version):** Left after the #2381 build, accepted by the researcher 2026-11-07. (1) The reports that print a verse (iba/app/handlers/reports.py, iba/app/lib/strongversereport.py, iba/app/lib/stage1coverage.py, iba/app/ps/Verse-Scope.ps1, iba/app/ps/StrongVerse-Report.ps1) and the two reading generators (iba/app/lib/versereadinggenerate.py, iba/app/lib/charreadinggenerate.py) still print one entry per code; they show each code's own word now but do not show the unit once with lexical.unit_view. (2) Three M-coded rows the 28 October migration held keep their surface: Dan 7:19 H3321 (truth, unit says know), Acts 16:29 G1790 (fear, trembling), Job 30:24 H7769 (help, cry); release or keep, the researcher's call. (3) 16262 rows (1559 surfaces) in outputs/escalation/2379-behaviour-and-inner-state-surfaces-v3-20261107.csv are shared: a unit of several content codes whose word STEP does not assign to one code; 2378 of them are in a collection. Design for (1) first, then build; (2) and (3) are decisions. Detail: iba/app/BUILD.md section 469.
> **context (set this version):** iba/app/BUILD.md; outputs/escalation/2381-verse-lexical-surface-fix-design-v2-20261107.md

**v2** (2026-11-11T11:11:22Z, Claude) state=in-progress next_action=review assigned_to=Researcher
> **comment (set this version):** Researcher in chat 2026-11-11, verbatim: '2458, 2457, 2456, 2387 is all completed but I cannot approve it - prepare it properly for approval'.

**v3** (2026-11-11T11:11:22Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **context (set this version):** iba/app/BUILD.md section 469; outputs/escalation/2381-verse-lexical-surface-fix-design-v2-20261107.md; outputs/escalation/2379-behaviour-and-inner-state-surfaces-v3-20261107.csv
> **resolution (set this version):** Approval sought: close #2387 as completed per your statement in chat 2026-11-11, and choose how its three parts are carried.
Checked now: (1) none of the files the item names (iba/app/handlers/reports.py, iba/app/lib/strongversereport.py, iba/app/lib/stage1coverage.py, iba/app/ps/Verse-Scope.ps1, iba/app/ps/StrongVerse-Report.ps1, iba/app/lib/versereadinggenerate.py, iba/app/lib/charreadinggenerate.py) reads lexical.unit_view; only iba/app/lib/lexical.py and iba/app/lib/reading.py do. (2) The three held rows are unchanged in verse_lexical: Dan 7:19 H3321 still surface 'truth' (kind own, role head), Job 30:24 H7769 still 'help'; Acts 16:29 G1790 has no live row now. No release-or-keep ruling is recorded. (3) The shared rows: no ruling is recorded; verse_lexical now holds 53,444 live rows of kind shared (a different measure from the 16,262 rows and 1,559 surfaces of the item's file; not reconciled here).
Options: A (recommended): close #2387 as you state, and I raise the three parts as their own items so none is lost (units in the reports and readers, the three held rows, the shared rows). B: leave it on hold with its comes_back_when as written. C: tell me in chat which parts you consider done and I record each against its evidence.

**v4** (2026-11-11T11:12:13Z, Researcher) state=completed next_action=approved assigned_to=Researcher
> **comment (set this version):**   approved
