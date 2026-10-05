# Anger strand (fear process): handoff for the next chat

**Date:** 2026-10-05 · **State:** process approved (#1963, rulings in proposal §7); **unit 1 ledger approved** (#1966, 2026-10-05): `anger-observation-ledger-unit1-v1-20261005.md` (AG-01 to AG-59, faces A–Z, 239 hits, quote check 0 failures). **Unit 2 ledger approved** (#1967, 2026-10-05): `anger-observation-ledger-unit2-v1-20261005.md` (AG-60 to AG-101, faces 2A–2W, 132 hits, quote check 0 failures); OT-15 added to the register. **Unit 3 ledger approved** (#1968, 2026-10-05): `anger-observation-ledger-unit3-v1-20261005.md` (AG-102 to AG-146, faces 3A–3Z and 3AA, 217 hits, quote check 0 failures); OT-06 touched. **Unit 4 ledger approved** (#1969, 2026-10-05): `anger-observation-ledger-unit4-v1-20261005.md` (AG-147 to AG-198, faces 4A–4Z and 4AA–4AE, 221 hits, quote check 0 failures); OT-06 touched; ruling #1970 (no re-tagging; cfg_behaviour_rule 70, GOVERNANCE.md §88). **Unit 5 ledger written, for approval** (#1973, 2026-10-05): `anger-observation-ledger-unit5-v1-20261005.md` (AG-199 to AG-240, faces 5A–5Z and 5AA–5AB, 110 hits, quote check 0 failures). With it all 65 Strong's and 919 hits are faced. Weave held until the cross-ledger overview. **Next, once #1973 is approved: step 2 (reconciliation of units 1–5 against the 65 Strong's and 919 hits), then step 3 (cross-ledger overview).** Before or beside it: #1965, moving `fear/` and `life-death/` into their cluster folders (rule applied, #1964).

## Read first

1. `anger-key-characteristic-process-proposal-v1-20261005.md`: §3 steps, §3A (#1944–#1947 behaviour), §7 rulings.
2. `anger-observation-ledger-unit1-v1-20261005.md`: the format to copy (columns: observation · setting/meaning/implication · chain · verses · basis · parties · also appears · disp.; closing §F "What emerged, and what it changes", §G chains).
3. `Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md` (only when chapter text is written: step 4).

## Unit plan (fixed from the live vocabulary, 2026-10-05; 65 Strong's, 919 hits)

| Unit | Words | Hits |
|---|---|---|
| 1 ✔ | *ʾaph* H0639G, *ʾānap̄* H0599 | 239 |
| 2 ✔ | *ḥēmāh* H2534 (125) with the heat words H2525, H2528, H2152 | 132 |
| 3 ✔ | *ḥārāh* H2734 (91), *ḥārôn* H2740 (41), H2750 (6), *kāʿas* H3707 (53), H3708A (22), H3708B (4) | ~217 |
| 4 ✔ | the rest of the Hebrew and Aramaic: *qāṣap̄/qeṣep̄* (H7107, H7108, H7109, H7110A/B, H7111), *ʿebrāh* (H5678, H5674B), *zaʿam* (H2194, H2195), *zaʿap̄* (H2196, H2197, H2198), strife and Meribah (H4079, H4808, H4809G/H), *qînāh* H7015, *saʿar* H5590, H6225, H6696B, H5307K, H6440M, H0888, H1149, H2121, H7265, H7266 | 221 |
| 5 ✔ | the Greek (25 Strong's): *orgē* G3709, *thymos* G2372, *orgizō* G3710, *eris* G2054, *aganakteō* G0023, *paroxynō* and the rest | 110 |

This is five units, not the four estimated in the proposal: *ʾaph* alone filled unit 1, and units stay at a reading size like fear's.

## Method (do not re-derive)

- **Pull:** `python _analytics/cross-cluster-web/life-death/strand-unit-pull-v1-20261002.py OUT.csv <strongs…>`, then join `wa-cluster-M02-phenomena-ledger-v5-20260929.csv` by reference (side, phenomenon, m02_words), as unit 1 did. (The pull script moves with #1965; update this path then.)
- **Faces:** a face-assign script per unit (pattern `anger-unit2-face-assign-v1-20261005.py`), with the parties columns (ruling 6.2). Every hit gets a face. Face labels carry the unit number (unit 2: 2A–2W; unit 3: 3A…); AG ids continue from AG-199; unit 5 faces 5A…. Where one verse needs two faces, set them by (reference, position), as unit 3 did for 2Ki 23:26.
- **Read by surface first**; prior work cited, not restated (U1 §n, U2 §n, AN-nn).
- **Quote check:** `_analytics/cross-cluster-web/fear/fear-quote-check-v1-20261001.py` on a copy with observation + meaning + chain joined and the verses column as the reference cell (see unit 1 §H).
- **"Already in the chapters":** match references against the chapter files with full book names (use `os.path.basename`; the first unit-1 run collapsed the file keys on Windows paths).
- **Escalation tip (unit 3):** `-Action Raise` ignores `-NextAction`/`-Resolution`; after raising, run `-Action Update -NextAction ready_for_approval -AssignedTo Researcher -Resolution …` so the approval can be recorded.
- **Chapter match (unit 4):** `anger-chapter-match-v1-20261005.py PULL.csv` lists the verses already cited in the chapters (book carried forward to bare references).
- **No re-tagging (#1970, cfg_behaviour_rule 70):** a word that reads as belonging with another cluster is recorded in §F as a cross-cluster association; never raise a tag change.
- Check the open threads register before each pull (OT-06 hand, OT-08 death side held, OT-12, OT-13, OT-14, OT-15 heat family).
- **Quote check tip (unit 2):** keep a quote that runs across two verses as two quotes, since the checker orders verses by first mention in the row; do not put your own labels in quotation marks.

## Working rhythm

One unit per chat: pull → read by surface → ledger → researcher approval → records → session-close (commit + push).
