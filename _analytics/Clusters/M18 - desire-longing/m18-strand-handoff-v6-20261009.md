# M18 Desire & Longing: strand handoff (v6)

**Date:** 2026-10-09 (v6, groups A, D, E and F of item F done) · **Escalation:** #1993 · **Supersedes:** `archive/m18-strand-handoff-v5-20261009.md`.

Use this to restart the M18 strand. Every open item gives its state and where to restart. All paths are in `_analytics/Clusters/M18 - desire-longing/` unless given in full.

## 1. Done (do not redo)

| Step | Output | State |
|---|---|---|
| Cluster overview | `m18-cluster-overview-v1-20261008.md` and its 3 CSVs | done |
| Delight and pleasure pairing filter | `m18-delight-pleasure-pairing-filter-v1-20261008.md` and CSVs | done. **It is a working aid, not a decision item** (researcher, 2026-10-09). Use it as a hint while reading |
| Shared-verse pull (348) | `m18-shared-m47-m25-m02-crossref-v2-20261009.csv` | done |
| **M47 read-back** (208) | `m18-m47-validation-register-v1-20261009.md` and `.csv` | woven; claim register v34 |
| **M25 read-back** (89) | `m18-m25-validation-register-v1-20261009.md` and `.csv`; reading `m18-m25-inner-being-reading-v1-20261009.md` | woven; claim register v35 |
| **Held items** (jealousy OT-95, *ṭôb* OT-96, heat OT-15, rousing #1942) | `m18-held-items-reading-v1-20261009.md`; passages and pull script | woven; all four threads closed; #1942 ready for approval |
| **Item F, group A** (desire, craving, longing; 151 verses after filtering) | `m18-group-A-register-v1-20261009.csv` (reasons in `m18-group-A-decisions-v1-20261009.py`); reading `m18-group-A-reading-v1-20261009.md`; worksheet `m18-group-A-worksheet-v1-20261009.md`; weave `m18-group-A-narrative-weave-v1-20261009.py` | woven (10.6 v13 with new *Coveting*; 13.1 v13; 13.4 v3; 10.7 v22; Ch 11 v23; Ch 12 v16; Ch 2 v16; 10.2 v11); claim register v37 |
| **Item F, group D** (jealousy, zeal; 51 verses after filtering) | `m18-group-D-register-v1-20261009.csv` (reasons in `m18-group-D-decisions-v1-20261009.py`); reading `m18-group-D-reading-v1-20261009.md`; weave `m18-group-D-narrative-weave-v1-20261009.py` (with quote check); records `m18-group-D-records-update-v1-20261009.py` | woven (10.6 v14: zeal read in, new *Jealousy against a person* and *A husband's jealousy with no witness*; 13.1 v14; 10.3 v6; Ch 11 v24; Ch 12 v17); claim register v38 |
| **Item F, group E** (thirst, hunger; 30 verses after filtering) | `m18-group-E-register-v1-20261009.csv` (reasons in `m18-group-E-decisions-v1-20261009.py`); reading `m18-group-E-reading-v1-20261009.md`; weave `m18-group-E-narrative-weave-v1-20261009.py` | woven (10.6 v15 *Thirst answered* widened; 10.10 v17; 10.2 v12); claim register v39 |
| **Item F, group F** (precious; 44 verses after filtering) | `m18-group-F-register-v1-20261009.csv` (reasons in `m18-group-F-decisions-v1-20261009.py`); reading `m18-group-F-reading-v1-20261009.md`; weave `m18-group-F-narrative-weave-v1-20261009.py`; records `m18-group-F-records-update-v1-20261009.py` | woven (10.6 v16 with new *Precious*; 10.4 v9; 13.1 v15; Ch 12 v18; 10.2 v13; 10.10 v18; 10.5 v16; 10.13 v6; Ch 11 v25); claim register v40 |
| **M02 read-back** (51) | `m18-m02-validation-register-v1-20261009.md` and `.csv`; reading `m18-m02-inner-being-reading-v1-20261009.md` | woven; OT-19 closed; claim register v36 |

**OT-08** was closed by the researcher (*"no longer relavant"*). There is no block on Ch 2.

**Narration standard** (researcher, 2026-10-09, verbatim): *"the narration must be done from the perspective of the inner being workings - merely restating the verse is not a proper narration, thinking about the item and asking probing questions in important : compare, why different, what lies behind it; does the relationships make a difference; and other probing; it is especially important to not just restate figurative speach but explore it."*

**No holding** (researcher, verbatim): *"don't hold things unnecessarily"*. Read a verse when it comes up.

## 2. Narrative state

All files are in `_analytics/essay/spirit_soul_body/inner-being-narrative/`, with each prior version in `archive/`:

| Chapter | Version | Chapter | Version |
|---|---|---|---|
| Ch 2 | v16 | 10.8 | v6 |
| Ch 4 | v14 | 10.9 | v16 |
| Ch 6 | v12 | 10.10 | v18 |
| 10.1 | v15 | 10.12 | v5 |
| 10.2 | v13 | 10.13 | v6 |
| 10.3 | v6 | Ch 11 | v25 |
| 10.4 | v9 | Ch 12 | v18 |
| 10.5 | v16 | 13.1 | v15 |
| 10.6 | v16 (sectioned) | 13.2 | v3 |
| 10.7 | v22 | 13.4 | v3 |

Claim register is v40.

## 3. Open

### F. The M18 words themselves (groups A, D, E and F done; next G, then B, C)
**Tools (reusable, per group):** `m18-group-pull-worksheet-v1-20261009.py {G}` builds the pull and worksheet. It filters decided verses and searches the narrative text for bare citations. `m18-group-register-build-v1-20261009.py {G}` builds the register from `m18-group-{G}-decisions-v1-20261009.py`. **Add each finished group's register to the filter list** in the pull script, so later groups skip those verses too.

The read-backs covered only the verses shared with M47, M25 and M02. Before pulling a gloss group, filter out every verse already decided in the three registers. Decide by verse, and check the M18 word, not just the citation (#1987).

| Group | Hits | Notes |
|---|---|---|
| A. desire, craving, longing | 258 | **done** (151 read) |
| B. delight, pleasure | 640 | Use the pairing filter only as a hint |
| C. will, willing, acceptance | 372 | *thelō* 206, *thelēma* 62. Compare with `../M64 - will-resolve/m64-will-reading-v1-*` and 10.7 *Willing*. Many *thelō* verses are now in 10.7 and 13.1 |
| D. jealousy, zeal | 112 | **done** (51 read) |
| E. thirst, hunger | 45 | **done** (30 read) |
| F. precious | 60 | **done** (44 read) |
| G. gloss away from desire | 23 | |

Notes carried forward:
- the kings who "did as he pleased": Dan 8:4 (routed C in the M25 pass) and Dan 11:3, 16. Dan 11:36 is woven in 10.7

**Structure, decided (researcher, verbatim, 2026-10-09):** *"10.6 is fine for M18."* There is no separate sub-chapter. The M18 words are read into 10.6 and its sections.

### H. M72 (Authority & Dominion)
It shares 182 verses with M18 (45 of them in the 348). M72 has no analysis. This is recorded so it is not lost.

### I. Tool fix (task chip task_6efadc92)
The cross-reference parser does not carry a book across a bare citation such as "(17:3)". It hit twice this session (Psa 119:40 in Ch 2; Exo 17:3 in 10.5). Until it is fixed, check every "not cited" verse by a text search, as was done here.

### J. Housekeeping
- The M25 weave and the held items are committed (cd5a1325). The M02 pass is committed after it.
- The push and the narrative copy to learning4comfort happen at `/session-close`.
- #1942 approved (researcher, 2026-10-09: *"approved 1942"*) and completed.
