# Psalms — re-read gate SNAPSHOT v5 (PSALTER CLOSE), 2026-07-11

> **The Psalter is complete: 150 / 150 psalms re-read under the corrected method.** Book-wide 9-gate re-measure taken at the close of **Book V (Ps 107–150)** and of the whole book. Deltas vs the 2026-07-09 baseline and the four prior snapshots.
> **Runner:** `python scripts/_check_reread_measures_v3_20260709.py --book Psalms` (read-only). Prior: [baseline](wa-psalms-reread-baseline-20260709.md), [v2 Book II](wa-psalms-reread-snapshot-v2-20260710.md), [v3 Book III](wa-psalms-reread-snapshot-v3-20260710.md), [v4 Book IV](wa-psalms-reread-snapshot-v4-20260710.md), [discipline audit](wa-psalms-reread-discipline-audit-20260710.md).

## Trajectory — six measurement points
| metric | baseline (0) | 51/150 | Book II (72) | Book III (89) | Book IV (106) | **CLOSE (150)** | Δ vs baseline |
|---|--:|--:|--:|--:|--:|--:|--:|
| characteristics | 3,810 | 3,700 | 3,566 | 3,394 | 3,249 | **2,854** | −956 † |
| active lexical rows | 76,321 | 83,892 | 85,303 | 85,791 | 86,392 | **88,108** | **+11,787** |
| **G2** no operation | 1,847 | 1,160 | 915 | 715 | 520 | **0** | **−1,847 ✅** |
| **G4** flattened reuse | 4 | 2 | 2 | 1 | 1 | **2** | −2 |
| **G6** no discovery | 976 | 654 | 521 | 405 | 294 | **0** | **−976 ✅** |
| **G9b** malformed pairs | 0 | 0 | 0 | 0 | 0 | **0** | held ✅ |
| **G10** incomplete ledger | 3,810 | 2,451 | 1,948 | 1,554 | 1,102 | **0** | **−3,810 ✅** |
| **G10** dims with ZERO rows | none | none | none | none | none | **none** | ✅ |
| G1 / G3 / G7 | pass | pass | pass | pass | pass | **pass** | held ✅ |
| G0 digestion (poetic caveat) | 159 | 159 | 159 | 159 | 159 | **159** | genre caveat |

† Characteristics fell by 956 across the whole read as Screen 0 re-roled God-content (God's attributes/acts → qualifier) and outward imagery (→ standalone) that the old `role-reassess` pass had mis-called characteristics. **Fewer, truer chars** — every one of the 2,854 now carries a full genre-aware poetic ledger.

## What the close means
- **G2, G6, G10 are at ZERO for the first time.** Every characteristic in the Psalter (all 2,854) has a named operation (106), a discovery note (114), and the full mandatory poetic ledger (101,102,104,105,106,107,108,112 + 116,114,115). The residual debt that stood at every prior snapshot was **entirely the not-yet-re-read psalms**; with Book V done, it is gone.
- **G9b held at 0 throughout** — no malformed pairs introduced across the entire corrected read.
- **Two residual flags, both understood:**
  - **G0 = 159** (unchanged, by design): the poetic genre caveat — the gate treats a whole psalm as one "passage" and so whole-chapter budgets are exceeded structurally. The *reading itself* proceeded by **char-arc passages** (a passage bounded by a characteristic's start→end, per `feedback_read_by_passage_not_whole_chapter`), not whole-chapter sweeps.
  - **G4 = 2**: two recurring terms (≥5×) still read closely alike book-wide — a small distinctions-residual to review, down from 4 at baseline.

## Book V (Ps 107–150) — what the corrected read captured
44 psalms, span-depth, char-arc, all gate-clean. Highlights of the final stretch (this session):
- **Ps 119** (the 176-verse acrostic, 641 spans) — read char-by-char via a reproducible builder, not stanza-chunks: 244 char / 317 qualifier / 80 standalone.
- **Ps 135–138** — Hallel/great-Hallel/Babylon-lament/David's-thanks; the refrain "his steadfast love endures forever" correctly resolved to qualifier+standalone.
- **Ps 139** (omniscience, 20 chars) — the clearest operation-focused read of the batch: the interior *laid open* and *known from afar*, the mind's *limit*, the futile *impulse to flee*, the inmost *seat formed*, then *zeal* (aligned hatred of God's enemies) and *self-offering* ("Search me… know my heart").
- **Ps 140–145** — the Davidic laments (the wicked's heart-scheming vs the psalmist's plea and assurance; guarded speech and heart; the isolated soul in the cave; the penitential crushed/thirsting self; the war-song's twofold beatitude) and the great acrostic **Ps 145** (12 movement-anchored praise-operations).
- **Ps 146–150** — the final Hallel. **Ps 148** honestly resolves to almost-all-standalone (personified creation praising) with only 2 human chars; **Ps 150** to 3 movement-anchored praise-chars amid the instruments. The Psalter closes on "Let everything that has breath praise the LORD."

## Standing debt — Book I (Ps 1–41), unchanged
The corrected read of **Books II–V (Ps 42–150, 109 psalms) is defect-free on every check**, including the IB-screen: **0 God-bearer characteristics, 0 old-provenance candidates.**

**Book I (Ps 1–41) still carries its pre-existing debt** (read in an earlier session, before consistent IB-screen enforcement):
- **185 characteristics with God as bearer** (ve_nr 105 = `God` / `the LORD` / …) — God-content mis-roled as characteristics; per Screen 0 these should be qualifiers.
- **300 char-candidates under the old `role-reassess-2026` provenance** — never brought under the corrected `read-2026` pass.

This is the **one remaining piece** to bring the whole Psalter to the corrected standard. It is a self-contained remediation pass (re-screen the 185 God-bearers → qualifier; re-read the 300 old-provenance candidates under `read-2026`), isolated to Ps 1–41.

*Filed 2026-07-11, Psalms folder. Read-only validation snapshot at the Psalter close (150/150). Next: the Book I (Ps 1–41) IB-screen remediation pass.*
