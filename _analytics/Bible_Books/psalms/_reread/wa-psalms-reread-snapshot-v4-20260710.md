# Psalms — re-read gate SNAPSHOT v4 (Book IV close), 2026-07-10

> Book-wide gate re-measure at **106 / 150 psalms re-read** (71%) — taken at the close of **Book IV (Ps 90–106)**. Books II–IV (Ps 42–106) are now one continuous corrected-read stretch. Deltas vs the 2026-07-09 baseline and the three prior snapshots.
> **Runner:** `python scripts/_check_reread_measures_v3_20260709.py --book Psalms` (read-only). Prior: [baseline](wa-psalms-reread-baseline-20260709.md), [v2 Book II close](wa-psalms-reread-snapshot-v2-20260710.md), [v3 Book III close](wa-psalms-reread-snapshot-v3-20260710.md). See also the mid-session [discipline audit](wa-psalms-reread-discipline-audit-20260710.md).

## Trajectory — five measurement points
| metric | baseline (0) | 51/150 | Book II (72) | Book III (89) | **Book IV (106)** | Δ vs baseline |
|---|--:|--:|--:|--:|--:|--:|
| characteristics | 3,810 | 3,700 | 3,566 | 3,394 | **3,249** | −561 † |
| active lexical rows | 76,321 | 83,892 | 85,303 | 85,791 | **86,392** | **+10,071** |
| **G2** no operation | 1,847 | 1,160 | 915 | 715 | **520** | **−1,327** |
| **G4** flattened reuse | 4 | 2 | 2 | 1 | **1** | −3 |
| **G6** no discovery | 976 | 654 | 521 | 405 | **294** | **−682** |
| **G9b** malformed pairs | 0 | 0 | 0 | 0 | **0** | held ✅ |
| **G10** incomplete ledger | 3,810 | 2,451 | 1,948 | 1,554 | **1,102** | **−2,708** |
| **G10** dims with ZERO rows | none | none | none | none | **none** | ✅ |
| G1 / G3 / G7 | pass | pass | pass | pass | **pass** | held ✅ |

† Characteristics keep falling as Screen 0 re-roles God-content to qualifier — fewer, **truer** chars. The residual G10/G2/G6 debt is now almost entirely the **44 not-yet-re-read psalms (Book V, Ps 107–150)**.

## Book IV (Ps 90–106) — what the corrected read captured
17 psalms, all gate-clean, read by **char-arc** (the passage refinement adopted mid-book — a passage is bounded by a characteristic's start/end, not arbitrary verse-blocks; see memory `feedback_read_by_passage_not_whole_chapter`). Highlights:
- **Ps 90** Moses on transience vs eternity; **Ps 91** the refuge; **Ps 92** the Sabbath song.
- **Ps 93** — a pure kingship-glory hymn with **no human IB response**, correctly resolved to **all-standalone** (0 char, 0 qual) — the honest reading of pure God-content.
- **Ps 94** God of vengeance; **Ps 95–100** the worship/enthronement cluster (human worship-acts separated from the *cosmic* joy of heavens/sea/hills → standalone); **Ps 103** "Bless the LORD, O my soul."
- **Ps 104** the creation hymn (166 spans) — the clearest demonstration of the char-arc method: 16 characteristics in 3 tight arcs (doxology frame v1↔v35, heart-provision v14-15, closing response v33-35) amid 150 substrate spans.
- **Ps 105** covenant-history (7 arcs) and **Ps 106** the confession-recital (58 chars across 12 rebellion/praise arcs) — read by their internal char-arcs like Ps 78.

## Discipline check (mid-session)
A full DB-side re-verification confirmed **every psalm read this session (Ps 75–104, and now 105-106) is defect-free on all gates** — 0 G10, 0 unroled, 0 God-bearer, 0 G9b, 0 no-discovery. The faster rhythm did not drop any control. The same audit surfaced **pre-existing debt in Book I (Ps 1–41)** — 185 characteristics with God as bearer + 300 candidates under the old `role-reassess-2026` provenance — flagged for a remediation pass (legacy from a prior session, isolated to Book I).

*Filed 2026-07-10, Psalms folder. Read-only validation snapshot at the Book IV close. Next: Book V (Ps 107–150), then the Book I remediation pass.*
