# M10 — Phase 9 findings distribution (pre-synthesis analytics)

**Generated:** 2026-05-24T17:51:59Z
**Source:** `cluster_finding` table — 4158 rows × 22 characteristics × 189 prompts

**Purpose:** characterise the findings landscape **before** the cluster-synthesis session so the synthesis is packaged sensibly — e.g. silent-dominated prompts handled separately from evidence-rich ones; per-characteristic synthesis precedes cross-characteristic comparison.

---

## §1. E / S / G distribution per characteristic

| Char | Short name | E | S | G | E % | S % |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Wilful sinning | 180 | 9 | 0 | 95.2% | 4.8% |
| 2 | Unintentional sinning | 158 | 31 | 0 | 83.6% | 16.4% |
| 3 | Confession | 168 | 21 | 0 | 88.9% | 11.1% |
| 4 | Conscience suppression | 165 | 24 | 0 | 87.3% | 12.7% |
| 5 | Refusal to repent | 174 | 15 | 0 | 92.1% | 7.9% |
| 6 | Habitual defection | 167 | 22 | 0 | 88.4% | 11.6% |
| 7 | Contagious sin | 167 | 22 | 0 | 88.4% | 11.6% |
| 8 | Political revolt | 151 | 38 | 0 | 79.9% | 20.1% |
| 9 | Sinful speech | 178 | 11 | 0 | 94.2% | 5.8% |
| 10 | Specialised sinful mechanisms | 163 | 26 | 0 | 86.2% | 13.8% |
| 11 | Sin as universal condition | 184 | 5 | 0 | 97.4% | 2.6% |
| 12 | Sin as enslaving power | 158 | 31 | 0 | 83.6% | 16.4% |
| 13 | Sin as divine record | 184 | 5 | 0 | 97.4% | 2.6% |
| 14 | Forgiveness sought and received | 183 | 6 | 0 | 96.8% | 3.2% |
| 15 | Generational sin | 168 | 21 | 0 | 88.9% | 11.1% |
| 16 | The sinner as moral character | 183 | 6 | 0 | 96.8% | 3.2% |
| 17 | Guilt as inner-being state | 180 | 9 | 0 | 95.2% | 4.8% |
| 18 | Iniquity as accumulated moral crime | 179 | 10 | 0 | 94.7% | 5.3% |
| 19 | Transgression as deliberate boundary-crossing | 182 | 7 | 0 | 96.3% | 3.7% |
| 20 | Faithlessness as covenant-breaking sin | 179 | 10 | 0 | 94.7% | 5.3% |
| 21 | Perversion as inner inversion | 186 | 3 | 0 | 98.4% | 1.6% |
| 22 | Injustice as moral failure of right conduct | 183 | 6 | 0 | 96.8% | 3.2% |

**Cluster aggregate:** E=3820 (91.9%) · S=338 (8.1%) · G=0 (0.0%) · Total=4158

---

## §2. E / S / G distribution per tier

| Tier | E | S | G | E % | S % | Avg E-per-prompt |
|---|---:|---:|---:|---:|---:|---:|
| T0 | 208 | 56 | 0 | 78.8% | 21.2% | 17.3 / 22 |
| T1 | 519 | 9 | 0 | 98.3% | 1.7% | 21.6 / 22 |
| T2 | 587 | 95 | 0 | 86.1% | 13.9% | 18.9 / 22 |
| T3 | 659 | 67 | 0 | 90.8% | 9.2% | 20.0 / 22 |
| T4 | 464 | 64 | 0 | 87.9% | 12.1% | 19.3 / 22 |
| T5 | 446 | 16 | 0 | 96.5% | 3.5% | 21.2 / 22 |
| T6 | 528 | 0 | 0 | 100.0% | 0.0% | 22.0 / 22 |
| T7 | 409 | 31 | 0 | 93.0% | 7.0% | 20.4 / 22 |

---

## §3. Prompt buckets by synthesis weight

Each prompt is bucketed by how many of the cluster's characteristics evidenced it. **Synthesis weight** = number of `E` findings out of the N characteristics. High weight = many independent E findings to compare → rich synthesis work. Low weight (= many silent) = the cluster is broadly silent on this prompt → synthesis is short and structural.

- **Broad evidence** (≥16/22 chars evidenced E): **173 prompts**
- **Broad silence** (≤5/22 chars evidenced E): **4 prompts**
- **Divergent** (between 6 and 15 chars E): **12 prompts**

**Sample broad-evidence prompts (top 15 by E count):**

| Prompt | E count | E chars (first 8) |
|---|---:|---|
| T0.1.1 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T0.1.3 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T0.2.2 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T0.2.3 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T0.3.1 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T0.3.3 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T1.1.1 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T1.1.2 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T1.1.3 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T1.2.1 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T1.2.2 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T1.2.3 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T1.3.1 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T1.3.2 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |
| T1.3.3 | 22 | 1, 2, 3, 4, 5, 6, 7, 8... +14 |

**Sample broad-silence prompts (top 15 by S count):**

| Prompt | S count | E count | E chars |
|---|---:|---:|---|
| T0.2.1 | 19 | 3 | 3, 14, 17 |
| T0.1.2 | 17 | 5 | 11, 13, 14, 21, 22 |
| T0.3.2 | 17 | 5 | 1, 11, 13, 14, 16 |
| T4.6.3 | 17 | 5 | 2, 16, 17, 18, 19 |

**Sample divergent prompts (top 15 by S-vs-E spread):**

| Prompt | E | S | G |
|---|---:|---:|---:|
| T3.5.1 | 7 | 15 | 0 |
| T3.5.2 | 7 | 15 | 0 |
| T3.5.3 | 7 | 15 | 0 |
| T7.1.8 | 15 | 7 | 0 |
| T2.1.3 | 13 | 9 | 0 |
| T4.6.1 | 9 | 13 | 0 |
| T4.6.4 | 13 | 9 | 0 |
| T2.1.1 | 12 | 10 | 0 |
| T2.1.2 | 12 | 10 | 0 |
| T2.1.4 | 12 | 10 | 0 |
| T4.6.2 | 10 | 12 | 0 |
| T7.1.9 | 12 | 10 | 0 |

---

## §4. Buckets per tier

| Tier | Broad evidence | Broad silence | Divergent |
|---|---:|---:|---:|
| T0 | 9 | 3 | 0 |
| T1 | 24 | 0 | 0 |
| T2 | 27 | 0 | 4 |
| T3 | 30 | 0 | 3 |
| T4 | 20 | 1 | 3 |
| T5 | 21 | 0 | 0 |
| T6 | 24 | 0 | 0 |
| T7 | 18 | 0 | 2 |

---

## §5. Per-characteristic strength (E % across 189 prompts)

Characteristics with low E % had broadly thin evidence corpora for the catalogue's question-set — their contribution to cluster synthesis is structural ('this characteristic is broadly silent on the catalogue'). Characteristics with high E % drive the cross-characteristic comparison.

| Char | Short name | E count | E % | Strength |
|---:|---|---:|---:|---|
| 21 | Perversion as inner inversion | 186 | 98.4% | HIGH |
| 11 | Sin as universal condition | 184 | 97.4% | HIGH |
| 13 | Sin as divine record | 184 | 97.4% | HIGH |
| 14 | Forgiveness sought and received | 183 | 96.8% | HIGH |
| 16 | The sinner as moral character | 183 | 96.8% | HIGH |
| 22 | Injustice as moral failure of right conduct | 183 | 96.8% | HIGH |
| 19 | Transgression as deliberate boundary-crossing | 182 | 96.3% | HIGH |
| 1 | Wilful sinning | 180 | 95.2% | HIGH |
| 17 | Guilt as inner-being state | 180 | 95.2% | HIGH |
| 18 | Iniquity as accumulated moral crime | 179 | 94.7% | HIGH |
| 20 | Faithlessness as covenant-breaking sin | 179 | 94.7% | HIGH |
| 9 | Sinful speech | 178 | 94.2% | HIGH |
| 5 | Refusal to repent | 174 | 92.1% | HIGH |
| 3 | Confession | 168 | 88.9% | HIGH |
| 15 | Generational sin | 168 | 88.9% | HIGH |
| 6 | Habitual defection | 167 | 88.4% | HIGH |
| 7 | Contagious sin | 167 | 88.4% | HIGH |
| 4 | Conscience suppression | 165 | 87.3% | HIGH |
| 10 | Specialised sinful mechanisms | 163 | 86.2% | HIGH |
| 2 | Unintentional sinning | 158 | 83.6% | HIGH |
| 12 | Sin as enslaving power | 158 | 83.6% | HIGH |
| 8 | Political revolt | 151 | 79.9% | HIGH |

---

## §6. Synthesis load summary

If the cluster synthesis runs in a single session against the full matrix, the AI reads:

- 4158 finding blocks
- Total character count in finding bodies: ~2,463,452
- Equivalent to ~547 pages of analytical text

**Recommended packaging given this distribution:**

- Broad-evidence bucket (173 prompts) carries the bulk of the comparative work and deserves the most careful per-prompt synthesis.
- Divergent bucket (12 prompts) is where the most interesting cross-characteristic tensions live — these warrant dedicated attention.

**Per-characteristic synthesis (pre-cross-cluster):** each of the 22 characteristics has 189 findings of its own. If a per-characteristic distillation precedes cross-characteristic synthesis, the cluster-scope AI session reads N characteristic-summaries instead of N × 189 raw blocks.
