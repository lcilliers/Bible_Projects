# M18 Desire & Longing: strand handoff (open items and where everything is)

**Date:** 2026-10-09 · **Escalation:** #1993 · **Purpose:** to restart the M18 strand after the session closes without redoing work already done. Every open item gives its state, its files and the point to restart from.

All paths are in `_analytics/Clusters/M18 - desire-longing/` unless given in full.

## 1. What is done (do not redo)

| Step | Date | Output | State |
|---|---|---|---|
| 1. Cluster overview | 2026-10-08 | `m18-cluster-overview-v1-20261008.md` + pull script and 3 CSVs (`m18-cluster-hits-*`, `-strongs-*`, `-mcode-cooccurrence-*`) | done |
| 2. Delight and pleasure pairing filter (640 hits, 19 Strong's) | 2026-10-08 | `m18-delight-pleasure-pairing-filter-v1-20261008.md` + `-pairing-pull-*.py`, `-pairing-*.csv`, `-filter-*.py`, `-filter-*.csv` | done; **decisions open (item A)** |
| 3. Shared-verse pull: M18 × M47 / M25 / M02 (348 verses) | 2026-10-09 | `m18-shared-m47-m25-m02-verses-v1-20261009.csv`. The working file is `m18-shared-m47-m25-m02-crossref-v2-20261009.csv`: narrative places, open threads, and every partner analysis file per verse | done |
| 4. Test batch (6 verses) and method | 2026-10-09 | `m18-shared-m47-m25-m02-validation-v1-20261009.md` | done; method approved ("proceed with M47 first") |
| 5. **M47 read-back** (208 verses) | 2026-10-09 | `m18-m47-validation-register-v1-20261009.md` (report) and `.csv` (one decision per verse); worksheet `m18-m47-validation-worksheet-v1-20261009.md`; scripts `m18-m47-validation-*-build-*.py`, `m18-m47-narrative-weave-v1-20261009.py`, `m18-m47-records-update-v1-20261009.py` | **done and woven**: 13 chapters, claim register v34, OT-95, OT-96 |

The researcher's rule for the read-back (verbatim, 2026-10-09): *"a) why would the verse not be narrated in the first place, is it because something was missed - fix it; b) does the new reading add new perspective to the narration, maybe from a different angle - validate this new perspective and add it c) is there a fundamental error that need to be re-alligned. It is very important to work with the analysis already generated in the cluster work to avoid re-doing investigatory work alraedy done."*

## 2. Open items

### A. Delight-filter decisions (researcher)
- **Asked in:** `m18-delight-pleasure-pairing-filter-v1-20261008.md` §3. No answer yet.
- **Decision 1:** park bucket 3 (269 hits, 248 of them *ṭôb*) as qualifiers of things. First take out the God rows: *ṭôb* said of the LORD (15), of God (4), and "God saw that it was good" (Gen 1).
- **Decision 2:** bucket 2 (117 hits, the paired word has an M-code). Read these as pairs, or hold them for the paired characteristic's strand. Loose tags ("king", "word", "hand") would fall back to bucket 3.
- **Decision 3:** read bucket 1 (254 hits) in passages as the delight and pleasure set.
- **Linked:** OT-96 holds the 10 M47-shared *ṭôb* verses until this is decided.
- **Restart:** `m18-delight-pleasure-filter-v1-20261008.csv` has the `filter_bucket` column for every hit.

### B. M25 read-back (next)
- **Scope:** 111 M18 × M25 verses. **22 are also M47 and are already done** (see the decision in `m18-m47-validation-register-v1-20261009.csv`), so 89 remain.
- **Existing analysis to use:** the M25 ledgers and faces in `_analytics/Clusters/M25 - life-death/`:
  - unit 3, "living before God": 54 verses (`life-death-observation-ledger-unit3-*`, `life-death-unit3-faces-*.csv`)
  - unit 2, "dying and death": 43 verses
  - units 1 and 4, and the Q2/Q3 ledgers
- **Constraint to raise first:** Ch 2's placement is on hold (OT-08; researcher 2026-10-04: *"M25 is a particularly difficult section and I am not sure it is the right time to try and massage it"*). Most M25 verses would place in Ch 2. **Ask the researcher whether Ch 2 may be edited in this read-back, or whether Ch 2 placements are recorded and held.**
- **Test-batch item carried:** Psa 34:12. M25 face L09 is sound. Only its New Testament quotation (1Pe 3:10) is narrated (Ch 2, 10.5). Possible add to 10.6 as the want for life itself (test batch §4.4).
- **Method:** as for M47:
  1. Build a worksheet like `m18-m47-validation-worksheet-build-v1-20261009.py`, filtered to M25, with the M25 ledgers as the analysis source.
  2. Record one decision per verse.
  3. Weave on instruction.
  4. Quote-check against iba.db.
  5. Bump chapter versions.
  6. Update the claim register v35 and the index.

### C. M02 read-back (after M25)
- **Scope:** 59 M18 × M02 verses. 5 are also M47 (done) and 3 are also M25 (done with B), so 51 remain.
- **Existing analysis:** anger unit ledgers 1–5 and the faces CSVs (`_analytics/Clusters/M02 - anger-wrath/anger-unit*-faces-*.csv`), the cross-ledger overview v2 §F (M18 row), and `wa-cluster-M02-mcode-face-combinations-v1-20261005.csv` (rows mcode = M18).
- **OT-19** holds these 59 verses face by face. Its trigger is reached; resolve it in this step.
- **Test-batch items carried:**
  - Pro 6:34: sound. "jealousy makes it hard" in 10.1 *When feeling changes character* needs an "I read" marker.
  - Psa 37:1: not cited. Add it in 10.1 beside Psa 37:8, with "Delight yourself in the Lord" (37:4) in the psalm's own list of answers (37:3–7). (Test batch §4.5, §4.6.)

### D. OT-95: jealousy and zeal (8 verses held)
- **Verses:** 1Ki 19:10, 14; Eze 36:5; Jam 3:14; Jam 4:5; Num 11:29; Pro 23:17; Eze 8:3; also Psa 73:3.
- **Comes back when:** the M18 jealousy words are read (overview §3D: H7065, H7068, H7067G/H, H7072, G2205, G2207; 112 hits), and with OT-19.
- **Note:** jealousy has no account yet. 10.6 cites only Song 8:6, and 10.13 has God's wrath joined with jealousy. The researcher's rule for key characteristics (#1961) may apply. That is the researcher's call.

### E. OT-96: generic *ṭôb* (10 verses held)
- **Verses:** Isa 38:3; 2Ki 20:3; Gen 1:21; Ecc 7:26; Lam 3:25; Psa 73:1; Psa 125:4; 2Ch 19:3; Pro 14:14; Jos 23:14.
- **Comes back when:** item A is decided. Four are said of God and would go to 13.1.

### F. The M18 words themselves, after the read-back (researcher to choose the starting point)
- Overview §7 lists the starting points. The read-back came first by instruction.
- **What the read-back has already covered:** only verses shared with M47, M25 or M02. Before pulling any gloss group, filter out verses already decided in `m18-m47-validation-register-v1-20261009.csv` and the later M25/M02 registers (decided by verse; check the M18 word, not just the citation, #1987).
- **Gloss groups** (overview §3):

| Group | Hits | Notes |
|---|---|---|
| A. desire, craving, longing | 258 | |
| B. delight, pleasure | 640 | filtered (item A) |
| C. will, willing, acceptance | 372 | *thelō* G2309 206, *thelēma* G2307 62. The M64 will reading (#1986) left these aside as M18; compare with `../M64 - will-resolve/m64-will-reading-v1-*` |
| D. jealousy, zeal | 112 | item D |
| E. thirst, hunger | 45 | |
| F. precious | 60 | 4 Strong's, all from M29 |
| G. gloss away from desire | 23 | "collection", "far", "untroubled" |

- **Structural question (researcher):** 10.6 *Wanting* is now v10 but has no sections. Should desire get a full account as its own sub-chapter, like 10.12 Fear and 10.13 Anger (#1961)?

### G. OT-15: the heat family
- *ḥāmam* (H2552, tagged T3), for example Isa 57:5 "you who burn with lust".
- It names "a strand on desire (M18)" as a trigger. The trigger is reached; take it up with group A or D. No re-tagging (#1970).

### H. M72 (Authority & Dominion)
- It shares 182 verses with M18 (overview §5), 45 of them inside the 348 read-back set (`m72_flag` column in the shared-verse CSV).
- M72 has no analysis, so it is not part of the read-back. It is recorded so it is not lost.

### I. Tool fix (task chip)
- `../M64 - will-resolve/verse-narrative-ot-crossref-v2-20261006.py` does not carry a book to a bare citation such as "(4:4)" after a quotation, so cross-reference counts run low.
- In the M47 pass, 18 such placements and Isa 58:5 were confirmed by direct search.
- A task chip was raised in session 2026-10-09 (task_6efadc92). Until it is fixed, check bare citations by direct search.

### J. Session housekeeping
- Nothing from 2026-10-08/09 on M18 is committed yet. That is done at `/session-close`, which commits under the standing rule.
- OT-09 is noted: the M18 × M47 check is done.

## 3. Narrative state after the M47 read-back

Current chapter versions touched: 04 v13, 05 v4, 06 v11, 07 v7, 08 v6, 10.1 v14, 10.5 v13, 10.6 v10, 10.7 v19, 11 v20, 12 v14, 13.1 v10 (new *Delight*), 13.2 v2.
- Prior versions are in `inner-being-narrative/archive/`.
- Claim register v34, section "Strand updates — desire (M18) × M47".
- The narrative copy to learning4comfort ran (33 files verified).
