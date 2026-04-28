# VC revision ledger — v1

**Date:** 2026-04-25  
**Status:** v1 initial build. Records per-term routing outcomes from VCB-7..11 patches.  
**Linked planning doc:** [vc-corrective-strategy-v1-20260425.md](vc-corrective-strategy-v1-20260425.md) — strategy §5 Step 1.  
**Sample size:** 30 RE-EVAL terms (NO-CHANGE | REVISE-ONLY | MIXED) — small. Univariate signals only.  
**Caveat:** predictor metadata read from current DB (post-apply); revisions may have changed group counts in a small number of cases. Footnoted per term in the ledger CSV where pre-state differs.

---

## 1. Overall routing distribution

| Routing | Count | % of total |
|---------|------:|-----------:|
| NO-CHANGE | 47 | 75.8% |
| REVISE-ONLY | 8 | 12.9% |
| MIXED | 1 | 1.6% |
| NEW-ONLY | 6 | 9.7% |
| **Total** | **62** | 100.0% |

## 2. Per-batch routing

| Batch | NO-CHANGE | REVISE-ONLY | MIXED | NEW-ONLY | Total |
|-------|----------:|------------:|------:|---------:|------:|
| VCB-10 | 12 | 0 | 0 | 0 | 12 |
| VCB-11 | 11 | 1 | 0 | 3 | 15 |
| VCB-13 | 11 | 3 | 0 | 1 | 15 |
| VCB-7 | 2 | 2 | 1 | 2 | 7 |
| VCB-8 | 3 | 1 | 0 | 0 | 4 |
| VCB-9 | 8 | 1 | 0 | 0 | 9 |

## 3. Univariate predictor scores (RE-EVAL terms only)

**RE-EVAL cohort:** 56 terms (9 revised, base rate 16.1%)

Predictor evaluation: rate of revision (REVISE-ONLY|MIXED) within the predicted-positive subset vs. predicted-negative subset. Lift = positive_rate / base_rate.

| Predictor | Pos n | Pos revised | Pos rate | Neg n | Neg revised | Neg rate | Lift |
|-----------|------:|------------:|---------:|------:|------------:|---------:|-----:|
| groups > 5 | 3 | 0 |   0.0% | 53 | 9 |  17.0% |  n/a  |
| groups == 1 | 37 | 5 |  13.5% | 19 | 4 |  21.1% | 0.84 |
| groups==1 AND verses>=10 | 7 | 3 |  42.9% | 49 | 6 |  12.2% | 2.67 |
| language Hebrew | 12 | 5 |  41.7% | 44 | 4 |   9.1% | 2.59 |
| has_sb_flag | 8 | 3 |  37.5% | 48 | 6 |  12.5% | 2.33 |
| has_ph2_flag | 1 | 0 |   0.0% | 55 | 9 |  16.4% |  n/a  |
| groups<=2 AND verses<=5 | 35 | 5 |  14.3% | 21 | 4 |  19.0% | 0.89 |

## 4. Per-term ledger (RE-EVAL terms)

| Batch | mti | Strongs | Reg | Word | Lang | Verses | Groups | vcrows | Routing | SB | PH2 |
|-------|----:|---------|----:|------|------|-------:|-------:|-------:|---------|---:|----:|
| VCB-10 | 892 | G0724 | 70 | greed          | G | 3 | 2 | 3 | NO-CHANGE | 0 | 0 |
| VCB-10 | 5493 | G0726 | 70 | greed          | G | 13 | 5 | 13 | NO-CHANGE | 0 | 0 |
| VCB-10 | 893 | G4123 | 70 | greed          | G | 4 | 1 | 4 | NO-CHANGE | 0 | 0 |
| VCB-10 | 6115 | G0577 | 131 | rejection      | G | 2 | 2 | 2 | NO-CHANGE | 0 | 0 |
| VCB-10 | 1094 | G0580 | 131 | rejection      | G | 2 | 1 | 2 | NO-CHANGE | 0 | 0 |
| VCB-10 | 1096 | H5951 | 132 | rejoicing      | H | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |
| VCB-10 | 1199 | G0544 | 165 | unbelief       | G | 14 | 5 | 14 | NO-CHANGE | 0 | 1 |
| VCB-10 | 1198 | G0570 | 165 | unbelief       | G | 11 | 8 | 11 | NO-CHANGE | 1 | 0 |
| VCB-10 | 6602 | G1211 | 165 | unbelief       | G | 5 | 4 | 5 | NO-CHANGE | 0 | 0 |
| VCB-10 | 4465 | G4704 | 181 | zeal           | G | 11 | 2 | 11 | NO-CHANGE | 0 | 0 |
| VCB-10 | 4467 | G4705 | 181 | zeal           | G | 2 | 2 | 2 | NO-CHANGE | 0 | 0 |
| VCB-10 | 1268 | G4710 | 181 | zeal           | G | 12 | 11 | 12 | NO-CHANGE | 1 | 0 |
| VCB-11 | 819 | G0543 | 50 | disobedience   | G | 6 | 2 | 6 | NO-CHANGE | 0 | 0 |
| VCB-11 | 820 | G3876 | 50 | disobedience   | G | 3 | 1 | 3 | NO-CHANGE | 0 | 0 |
| VCB-11 | 3392 | G1760 | 85 | imagination    | G | 3 | 1 | 3 | NO-CHANGE | 0 | 0 |
| VCB-11 | 917 | G1761 | 85 | imagination    | G | 4 | 1 | 4 | REVISE-ONLY | 1 | 0 |
| VCB-11 | 1432 | G3116 | 115 | passion        | G | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |
| VCB-11 | 5948 | G3392 | 115 | passion        | G | 4 | 1 | 4 | NO-CHANGE | 1 | 0 |
| VCB-11 | 1023 | G3394 | 115 | passion        | G | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |
| VCB-11 | 1295 | G3552 | 193 | craving        | G | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |
| VCB-11 | 7222 | G3554 | 193 | craving        | G | 11 | 1 | 11 | NO-CHANGE | 0 | 0 |
| VCB-11 | 1296 | G3713 | 193 | craving        | G | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |
| VCB-11 | 1362 | G3339 | 202 | transformation | G | 4 | 2 | 4 | NO-CHANGE | 1 | 0 |
| VCB-11 | 7377 | G3445 | 202 | transformation | G | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |
| VCB-13 | 885 | G0019 | 67 | goodness       | G | 4 | 1 | 4 | NO-CHANGE | 0 | 0 |
| VCB-13 | 886 | G5544 | 67 | goodness       | G | 7 | 2 | 7 | REVISE-ONLY | 1 | 0 |
| VCB-13 | 884 | H2896A | 67 | goodness       | H | 306 | 9 | 306 | NO-CHANGE | 0 | 0 |
| VCB-13 | 5480 | G2168 | 69 | gratitude      | G | 38 | 1 | 38 | REVISE-ONLY | 1 | 0 |
| VCB-13 | 891 | G2169 | 69 | gratitude      | G | 15 | 1 | 15 | NO-CHANGE | 0 | 0 |
| VCB-13 | 5481 | G2170 | 69 | gratitude      | G | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |
| VCB-13 | 935 | G0861 | 92 | integrity      | G | 6 | 2 | 6 | NO-CHANGE | 0 | 0 |
| VCB-13 | 933 | H8538 | 92 | integrity      | H | 5 | 1 | 5 | NO-CHANGE | 0 | 0 |
| VCB-13 | 1080 | G1256 | 127 | reasoning      | G | 13 | 1 | 13 | NO-CHANGE | 0 | 0 |
| VCB-13 | 6065 | G1258 | 127 | reasoning      | G | 6 | 1 | 6 | NO-CHANGE | 0 | 0 |
| VCB-13 | 1081 | G1261 | 127 | reasoning      | G | 14 | 2 | 14 | NO-CHANGE | 0 | 0 |
| VCB-13 | 1221 | H2181 | 171 | whoredom       | H | 83 | 5 | 83 | NO-CHANGE | 0 | 0 |
| VCB-13 | 1220 | H2183 | 171 | whoredom       | H | 10 | 1 | 10 | REVISE-ONLY | 0 | 0 |
| VCB-13 | 1222 | H2184 | 171 | whoredom       | H | 9 | 1 | 9 | NO-CHANGE | 0 | 0 |
| VCB-7 | 6132 | G0341 | 134 | renewal        | G | 2 | 1 | 2 | NO-CHANGE | 0 | 0 |
| VCB-7 | 1097 | G0342 | 134 | renewal        | G | 2 | 1 | 2 | NO-CHANGE | 0 | 0 |
| VCB-7 | 6136 | H2475 | 134 | renewal        | H | 1 | 0 | 1 | REVISE-ONLY | 0 | 0 |
| VCB-7 | 1098 | H2487 | 134 | renewal        | H | 11 | 1 | 11 | MIXED | 0 | 0 |
| VCB-7 | 6134 | H4253 | 134 | renewal        | H | 3 | 0 | 3 | REVISE-ONLY | 0 | 0 |
| VCB-8 | 939 | G3863 | 96 | jealousy       | G | 4 | 2 | 4 | REVISE-ONLY | 0 | 0 |
| VCB-8 | 1099 | G1345 | 139 | righteousness  | G | 10 | 1 | 10 | NO-CHANGE | 1 | 0 |
| VCB-8 | 1264 | H4263 | 179 | yearning       | H | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |
| VCB-8 | 1365 | G4273 | 203 | treachery      | G | 3 | 1 | 3 | NO-CHANGE | 0 | 0 |
| VCB-9 | 5001 | G3435 | 41 | defilement     | G | 3 | 1 | 3 | NO-CHANGE | 0 | 0 |
| VCB-9 | 787 | G3436 | 41 | defilement     | G | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |
| VCB-9 | 922 | G0024 | 87 | indignation    | G | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |
| VCB-9 | 921 | H2152 | 87 | indignation    | H | 3 | 1 | 3 | REVISE-ONLY | 0 | 0 |
| VCB-9 | 1126 | G1505 | 148 | sincerity      | G | 3 | 1 | 3 | NO-CHANGE | 0 | 0 |
| VCB-9 | 6231 | G1506 | 148 | sincerity      | G | 2 | 1 | 2 | NO-CHANGE | 0 | 0 |
| VCB-9 | 1275 | H7589 | 189 | malice         | H | 3 | 1 | 3 | NO-CHANGE | 0 | 0 |
| VCB-9 | 7360 | G4832 | 209 | likeness       | G | 2 | 1 | 2 | NO-CHANGE | 0 | 0 |
| VCB-9 | 1377 | G4833 | 209 | likeness       | G | 1 | 1 | 1 | NO-CHANGE | 0 | 0 |

## 5. Per-term ledger (NEW-ONLY terms — partial-completion or fresh)

Listed for completeness. NEW-ONLY routing reflects partial-completion gaps absorbed by VCNEW or true FRESH classification — not predictive of future RE-EVAL revision risk.

| Batch | mti | Strongs | Reg | Word | Lang | Verses | Groups | vcrows | vcnew_ops |
|-------|----:|---------|----:|------|------|-------:|-------:|-------:|----------:|
| VCB-11 | 5111 | G3878 | 50 | disobedience   | G | 2 | 1 | 2 | 1 |
| VCB-11 | 916 | H4906 | 85 | imagination    | H | 6 | 1 | 6 | 3 |
| VCB-11 | 1364 | H2498 | 202 | transformation | H | 27 | 4 | 27 | 17 |
| VCB-13 | 934 | H8549G | 92 | integrity      | H | 51 | 2 | 51 | 45 |
| VCB-7 | 6135 | H2500 | 134 | renewal        | H | 2 | 0 | 2 | 2 |
| VCB-7 | 6137 | H4252 | 134 | renewal        | H | 1 | 0 | 1 | 1 |

## 6. Observations

Filled in narrative form once the numbers above are reviewed. Initial template:

- Strongest predictor surfaced (or "no clear univariate signal at N=30").
- Whether revisions cluster by language / registry / term type.
- Whether revision shape is dominated by description sharpening (consistent with strategy §3.2 prior).
- Specific terms whose outcome surprises (e.g. high-group term that returned NO-CHANGE).

## 7. Next actions

- If a predictor shows lift >2.0 with positive_rate >50% on N>=10 in the cohort: candidate triage rule. Validate on the next 1–2 batches before promoting.
- If no signal at N=30: continue VCB rolling, append to ledger after each batch, re-score at N=50 and N=100.
- Predictor candidates not yet tested in v1 (require additional schema queries): set_aside_reason gap on prior rows; dimension_index flag presence on registry; property-vs-characteristic term type. Add in v1.1 if signal warrants.

---
*Generated by `scripts/_build_vc_revision_ledger.py`. Re-run after each VCB to refresh.*