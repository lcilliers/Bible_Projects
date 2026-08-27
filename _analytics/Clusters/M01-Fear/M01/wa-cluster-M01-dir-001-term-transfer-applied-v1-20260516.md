# WA-M01-dir-001-term-transfer-applied-v1-20260516

**Directive:** [DIR-20260516-001 — wa-global-dir-001-M01-term-transfer-v1-20260516.md](wa-global-dir-001-M01-term-transfer-v1-20260516.md)
**Apply timestamp:** 2026-05-16T03:27:52Z (single transaction)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_0-20260515 §7

---

## Outcome

**13 terms transferred. M01 → 81 terms. Cluster status `Data - In Progress` → `Analysis - In Progress`.** Single transaction. All preconditions verified before apply.

---

## Apply results

### Term counts (pre → post)

| Cluster | Pre | Post | Δ |
|---|---:|---:|---:|
| **M01 Fear** | 94 | **81** | −13 |
| M02 Anger | 46 | 47 | +1 |
| M03 Grief | 86 | 88 | +2 |
| M10 Guilt | 87 | 88 | +1 |
| M20 Doubt | 12 | 15 | +3 |
| M24 Weakness | 67 | 73 | +6 |

### Cluster status

| Field | Pre | Post |
|---|---|---|
| `cluster.status` | `Data - In Progress` | **`Analysis - In Progress`** |
| `cluster.last_updated_date` | 2026-05-15T18:53:57Z | 2026-05-16T03:27:52Z |

### 13 transfers — verified per mti_id

| mti_id | Strong's | Translit | M01 → | Verified |
|---:|---|---|---|---|
| 21 | G2347 | thlipsis | M24 | ✓ |
| 51 | G4730 | stenochoria | M24 | ✓ |
| 156 | H4164 | mu.tsaq | M24 | ✓ |
| 162 | H4712 | me.tsar | M24 | ✓ |
| 198 | H6330 | pu.qah | M10 | ✓ |
| 1552 | H2750 | cho.ri | M02 | ✓ |
| 2494 | H8513 | te.la.ah | M24 | ✓ |
| 4481 | G1280 | diaporeō | M20 | ✓ |
| 4482 | G0639 | aporeō | M20 | ✓ |
| 4483 | H7672 | she.vash | M20 | ✓ |
| 5572 | H5076 | ne.dud | M03 | ✓ |
| 6210 | H6115 | o.tser | M24 | ✓ |
| 6385 | H1742 | dav.va | M03 | ✓ |

### Carry-along (no direct updates — auto-resolved via `mti_term_id → mti_terms.cluster_code`)

| Destination | vc rows | VCGs |
|---|---:|---:|
| M02 | 6 | 1 |
| M03 | 4 | 2 |
| M10 | 1 | 1 |
| M20 | 11 | 3 |
| M24 | 61 | 9 |
| **Total** | **83** | **16** |

---

## What stays in M01 (12 BOUNDARY + 69 regular = 81)

**BOUNDARY (12 terms — placed in M01-BOUNDARY at Phase 6):**

| With corpus (researcher question) | Without corpus (all-set-aside) |
|---|---|
| G0085 ademoneo | H2189 za.a.vah |
| G2285 thambos | H8047G sham.mah |
| H3735 ke.ra | H6178 a.ruts |
| H4867 mish.bar | H6426 pa.lats |
| H6125 a.qah | |
| H7661 sha.vats | |
| H8312 sar.ap.pim | |
| H8539 ta.mah | |

**STAYS regular (69 terms):** the AI-confirmed STAYS list (67 terms after deduplication of a.ruts/pa.lats appearing in both lists) plus 3 terms AI didn't reach in either pass: H0367 e.mah (mti=284), G5156 tromos (mti=308), H0366 a.yom (mti=1722). All three are uncontroversial core M01 fear vocabulary.

---

## Notes flagged but not addressed by this directive

1. **mo.rah / mo.ra duplicate (H4172A mti=270 vs H4172B mti=271)** — both have identical 11-verse sets across the same references. Likely an OT-DBR-009 dedup case at the lexical-variant level. Both remain in M01 with their (identical) meaning corpora.

2. **M20 Doubt is `Analysis Completed`** but now has 3 new terms (aporeō, diaporeō, she.vash, total 11 new vc rows + 3 inherited VCGs). The cluster_code transfer is purely structural; M20's analysis was conducted without these terms. Researcher decision needed on whether to reopen M20 for analysis of the new term content.

3. **AI did not produce a v2 of the constitution-debate document** — instead appended the addendum to the focused re-read file in place. Content is complete and correct; document organisation is non-standard. Worth a note to AI for next cluster.

---

## Tables not touched (per directive §5)

| Table | Modified? |
|---|---|
| `cluster_subgroup` | NO (Phase 6 work) |
| `mti_term_subgroup` | NO (Phase 6 work) |
| `verse_context` | NO (auto-resolved via FK only) |
| `verse_context_group` | NO (auto-resolved via FK only) |
| `vcg_term` | NO (auto-resolved via FK only) |
| `cluster_finding` | NO |
| `wa_session_b_findings` | NO |
| `wa_session_research_flags` | NO |

---

## Next step — AI Phase 5

Per v2_0 §8 — AI clusters the meaning corpus of the 81 remaining M01 terms (1031 - 83 = 948 verses with meanings) into provisional sub-groups + a BOUNDARY sub-group for the 12 BOUNDARY terms.

CC's deliverable for AI: regenerated constitution report v3 reflecting the now-stable 81-term cluster (or the post-Phase-4 meaning corpus by some other slice). Plus the Phase 5 design document spec per v2_0 §8.3.

---

## Provenance

- Directive: [Sessions/Session_Clusters/M01/wa-global-dir-001-M01-term-transfer-v1-20260516.md](wa-global-dir-001-M01-term-transfer-v1-20260516.md)
- AI debate (main): [Sessions/Session_Clusters/M01/wa-M01-constitution-debate-v1-20260516.md](wa-M01-constitution-debate-v1-20260516.md)
- AI debate (addendum): [Sessions/Session_Clusters/M01/wa-cluster-M01-constitution-focused-rereadgreek-v1-20260516.md](wa-cluster-M01-constitution-focused-rereadgreek-v1-20260516.md)
- Constitution report (input): `wa-cluster-M01-constitution-v2-20260515.md`
- Pre-apply backup: `backups/bible_research_backup_20260515_182459_pre-M01-rerun-reset.db`
