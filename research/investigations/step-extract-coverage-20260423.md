# STEP Extract Coverage Report — 2026-04-23

**Trigger:** Tier 2 cleanup applied — 219 superseded STEP Extracts moved to `data/exports/archive/STEP Extracts/`. This report confirms coverage across the word registry.

---

## Summary

| Metric | Count |
|---|---:|
| Total registries | 214 |
| Registries with ≥1 active STEP Extract | 184 |
| Registries without a STEP Extract | 30 |
| Active files in `data/exports/STEP Extracts/` | 186 |
| Archived files (post-Tier 2) | 219 |

**Result:** 100 % of non-Excluded registries (184 / 184) have an active STEP Extract. The 30 missing registries are all Phase 1 `Excluded` with zero terms — no STEP Extract was ever produced for them.

---

## Registries without a STEP Extract — all Excluded

All 30 have `phase1_status = 'Excluded'` and `phase1_term_count = 0`. Expected — these words were filtered out of Phase 1 before STEP extraction.

| no | word | no | word | no | word |
|---:|---|---:|---|---:|---|
| 9 | assent | 10 | awareness | 12 | betrayal |
| 14 | blamelessness | 21 | commitment | 22 | communion |
| 25 | conformity | 36 | cowardice | 37 | darkening |
| 38 | deadness | 45 | determination | 54 | emotion |
| 79 | hopelessness | 82 | identity | 84 | image of God |
| 88 | ingratitude | 95 | intuition | 101 | laziness |
| 106 | manipulation | 118 | personality | 119 | personhood |
| 133 | reliability | 136 | resentment | 141 | self-awareness |
| 143 | sensitivity | 145 | sexuality | 154 | stupor |
| 161 | transformation | 169 | vulnerability | 195 | spiritual powers |

---

## Registries with two active extracts — intentional (scope variance)

Not duplicates — `full` and `final` scopes are semantically distinct (pre-analysis vs post-analysis snapshots). Both retained.

| no | word | Active files |
|---:|---|---|
| 112 | mind | `mind_112_final_20260328_v1.json`, `mind_112_full_20260402_v1.json` |
| 182 | soul | `Soul_182_final_20260328_v1.json`, `Soul_182_full_20260404_v1.json` |

---

## Files in `STEP Extracts/` that are NOT per-registry extracts

Six files do not match the `{word}_{reg}_{scope}_{date}.json` pattern and were left in place by the archiver. These are flagged for your review — they may belong in a different folder.

| File | Guess at purpose |
|---|---|
| `term_G4893.json` | Term-level Strong's extract (G4893 = syneidēsis, conscience) |
| `term_H2534.json` | Term-level Strong's extract (H2534 = ḥēmāh, wrath) |
| `term_H2734.json` | Term-level Strong's extract (H2734 = ḥārāh, anger) |
| `wa-112-mind-final-20260328.json` | Registry-scoped extract in `wa-{NNN}-{word}-{scope}-{YYYYMMDD}` format — belongs under `data/exports/Session C/` per §3.1? |
| `wa-182-soul-final-20260328.json` | Same pattern as above |
| `wa-registry-clustering-input-20260327.json` | Clustering input artefact — likely `outputs/investigations/` or a programme-reports location |

**Recommendation:** reclassify these six files once you decide their proper home. They're not in the way today but violate the folder's intended contents.

---

## What the Tier 2 archive contains

`data/exports/archive/STEP Extracts/` now holds 219 prior-dated extracts. Each was superseded by a later extract for the same `{word}_{reg}_{scope}` group. The archive is indexed by the file manifest; nothing is lost, just out of the active working set.

Examples of what was archived:

- `anger_4_full_20260324.json`, `anger_4_full_20260325.json` (superseded by `anger_4_full_20260330_v1.json`)
- `Soul_182_full_20260324.json`, `Soul_182_full_20260328_v1.json`, `Soul_182_full_20260328_v2.json` (superseded by `Soul_182_full_20260404_v1.json`)
- `authority_197_full_20260326.json` through `_v5.json` (five same-day versions; latest `authority_197_full_20260405_v1.json` retained)

---

*Report produced 2026-04-23 after Tier 2 STEP Extracts cleanup.*
