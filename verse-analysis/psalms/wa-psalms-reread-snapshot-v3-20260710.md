# Psalms — re-read gate SNAPSHOT v3 (Book III close), 2026-07-10

> Book-wide gate re-measure at **89 / 150 psalms re-read** (59%) under the corrected method — taken at the close of **Book III (Ps 73–89)**. Books II and III (Ps 42–89) are now a continuous corrected-read stretch. Deltas shown against the 2026-07-09 baseline, the 07-10 (51/150) snapshot, and the Book II close (72/150).
> **Runner:** `python scripts/_check_reread_measures_v3_20260709.py --book Psalms` (read-only). Unit model = passage (poetic). Prior docs: [`wa-psalms-reread-baseline-20260709.md`](wa-psalms-reread-baseline-20260709.md), [`wa-psalms-reread-snapshot-20260710.md`](wa-psalms-reread-snapshot-20260710.md), [`wa-psalms-reread-snapshot-v2-20260710.md`](wa-psalms-reread-snapshot-v2-20260710.md).

## Trajectory — four measurement points
| metric | baseline 07-09 (0) | 07-10 (51/150) | Book II close (72/150) | **Book III close (89/150)** | Δ vs baseline |
|---|--:|--:|--:|--:|--:|
| characteristics | 3,810 | 3,700 | 3,566 | **3,394** | −416 † |
| active lexical rows | 76,321 | 83,892 | 85,303 | **85,791** | **+9,470** |
| per-span `ve_nr` | no 103/116 | +103,+116 | 103+116 | 103+116 live | 2 dims added |
| **G2** chars with no operation | 1,847 | 1,160 | 915 | **715** | **−1,132** |
| **G4** recurring terms read identically | 4 | 2 | 2 | **1** | **−3** |
| **G6** candidate verses no discovery | 976 | 654 | 521 | **405** | **−571** |
| **G9b** malformed pairs | 0 | 0 | 0 | **0** | held ✅ |
| **G10** chars missing ≥1 mandatory dim | 3,810 (all) | 2,451 | 1,948 | **1,554** | **−2,256** |
| **G10** mandatory dims with ZERO rows | none | none | none | **none** | ✅ |
| G1 / G3 / G7 | pass | pass | pass | **pass** | held ✅ |

† Characteristics keep falling because Screen 0 re-roles God-content spans (God's attributes/acts) the old `role-reassess` pass had mis-called characteristics. Fewer, **truer** characteristics — not lost coverage. At the Book III close the corrected-read portion (Ps 42–89, plus 73–89) carries full genre-aware ledgers; the residual G10/G2/G6 debt is now **entirely the 61 not-yet-re-read psalms** (Books IV–V, Ps 90–150).

## Book III (Ps 73–89) — what the corrected read captured
17 psalms, span-depth, all gate-clean, **read by passage** (the method correction adopted mid-book: long chapters are read passage-by-passage, never swept whole — see memory `feedback_read_by_passage_not_whole_chapter`). Highlights of the inner-being harvest:
- **Ps 73** — the great "till I entered the sanctuary" turn: envy of the wicked → the steadied heart.
- **Ps 77** — the remembrance-lament: the soul that refuses comfort, the spirit that faints, "I will remember the deeds of the LORD."
- **Ps 78** — the 72-verse historical maskil (241 spans, the project's largest read), read along its seven passages: transmission → the unsteadfast generation → the rebellion cycle → false repentance → the plagues → apostasy → the choice of David's upright heart.
- **Ps 84** — pilgrimage-longing: soul faints for the courts, a day better than a thousand.
- **Ps 86** — David's whole-hearted prayer: the poor/godly self, "unite my heart to fear your name."
- **Ps 88** — the darkest psalm, unrelieved: cry unanswered, soul full of troubles, ending in darkness (read as such, no imposed resolution).
- **Ps 89** — the 52-verse Davidic-covenant psalm (199 spans, Book III doxology close): the blessed people who walk in God's light, David's filial cry, the covenant seemingly broken, "how long?", sealed with "Blessed be the LORD forever."

Screen 0 held every God-hymn / covenant-oracle correctly God-centred (Ps 75, 76, 85, 87, 89's oracle sections), routing God's attributes/acts to **qualifier** and imagery/place/names to **standalone**, so that only the genuine human inner being carries a full characteristic ledger.

## Method note
- **G0 unchanged** (159 over the 12-span budget) — the poetic genre caveat: a "passage" for the gate = a whole psalm, so whole-chapter reading exceeds the budget by design, not a true failure. The reading itself now proceeds by sub-passage.
- The reusable ledger library (`scripts/_reread_ledger_lib.py`) now guarantees each characteristic's full poetic mandatory set, so hand-authored reads cannot silently miss a mandatory dim (G10).

*Filed 2026-07-10, Psalms folder. Read-only validation snapshot at the Book III close. Next: Book IV (Ps 90–106).*
