# Psalms — re-read gate SNAPSHOT v6 (PSALTER FULLY CORRECTED), 2026-07-11

> **The entire Psalter is now corrected end-to-end.** Book I (Ps 1–41) has been re-read by char-arc under `read-2026`, resolving the last standing debt. Every content gate is now at **zero** book-wide — including the IB-screen and G4, which were the only remaining residuals at the v5 close.
> **Runner:** `python scripts/_check_reread_measures_v3_20260709.py --book Psalms` (read-only). Prior: [v5 Psalter close](wa-psalms-reread-snapshot-v5-20260711.md), [baseline](wa-psalms-reread-baseline-20260709.md).

## Final gate state (150/150 psalms, corrected method)
| gate | baseline | v5 (Psalter close) | **v6 (post Book I)** |
|---|--:|--:|--:|
| characteristics | 3,810 | 2,854 | **2,168** † |
| active lexical rows | 76,321 | 88,108 | **80,578** |
| **G2** no operation | 1,847 | 0 | **0** ✅ |
| **G4** flattened reuse | 4 | 2 | **0** ✅ |
| **G6** no discovery | 976 | 0 | **0** ✅ |
| **G9b** malformed pairs | 0 | 0 | **0** ✅ |
| **G10** incomplete ledger | 3,810 | 0 | **0** ✅ |
| **G10** dims with ZERO rows | none | none | **none** ✅ |
| G1 / G3 / G5 / G7 | pass | pass | **pass** ✅ |
| G0 digestion (poetic caveat) | 159 | 159 | 159 (by design) |
| **IB-screen** God-bearer chars | (Book I 185) | (Book I 185) | **0** ✅ |
| **old-provenance candidates** | (Book I 300) | (Book I 300) | **0** ✅ |

† The char count fell again (2,854 → 2,168, −686) because Book I's *old* read (the pre-IB-screen `role-reassess` pass) had inflated the count with God-content and imagery mis-called characteristics. The corrected re-read produced **fewer, truer** chars, each carrying a full genre-aware poetic ledger. Every one of the 2,168 is now a genuine human inner-being movement.

## What the Book I remediation did
Re-read all **41 psalms of Book I** by char-arc under `read-2026`, the same pipeline as Ps 42–150 — not a mechanical bearer-flip. This resolved **both** standing debts at once:
- **185 God-bearer characteristics → 0** (God's attributes/acts correctly re-screened to qualifier).
- **300 old-provenance candidates → 0** (all brought under the corrected `read-2026` pass).

The re-read was banked in five batches (Ps 1–8, 9–17, 18–25, 26–33, 34–41), each coverage-checked (100%), gate-checked (G10=0, G6=0), integrity-swept (0 missing-dims / 0 unroled / 0 God-bearer / 0 G9b), and committed. **Every batch: 0 defects.**

### Interior gems surfaced in Book I
- **Ps 1** the threefold refusal (walk→stand→sit = a deepening non-participation); **Ps 8** wonder at frail man crowned with dignity; **Ps 10** a sustained profile of the *wicked's* inner life (arrogance, self-glorying greed, practical atheism, "God won't see"); **Ps 15** an almost-total portrait of the righteous interior; **Ps 16** dense contented trust (God as portion, the heart instructed at night, fullness of joy).
- **Ps 22** the dereliction arc (forsakenness → worm-abasement → melted heart → the turn to proclaim → universal praise); **Ps 23** the shepherd's contentment and fearlessness; **Ps 25** the acrostic of trust/guidance/forgiveness; **Ps 27** "one thing I ask" (desire consolidated onto gazing at God's beauty).
- **Ps 32** the confession psalm (silence rotting the bones → the confessing turn); **Ps 34** taste-and-see; **Ps 35** the costly compassion once shown to enemies who now repay evil; **Ps 37** the "fret not" wisdom imperatives; **Ps 38** sin written into the flesh; **Ps 39** man as a mere breath, the plea "look away that I may smile"; **Ps 41** the wound of a trusted friend's betrayal, then the Book I doxology.

## Status
**The Psalms are complete and fully corrected: 150/150 psalms, every content gate at zero, no IB-screen or provenance debt anywhere in the book.** The only non-zero measures are the G0 poetic genre caveat (the gate treats a whole psalm as one passage; the reading itself proceeded by char-arc) — understood and by design.

*Filed 2026-07-11, Psalms folder. Read-only validation snapshot. The Psalter re-read project is complete.*
