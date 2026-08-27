# wa-global-dir-001-M02-term-transfer-v1-20260516

**Phase 4 (v2_2):** Term transfers + status transition
**Source cluster:** `M02` Anger, Wrath and Indignation
**Date:** 2026-05-16
**Directive id:** `DIR-20260516-008`
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §7

---

## 1. MOTIVATION

Per the M02 Phase 3 constitution debate ([wa-cluster-M02-debate-v1-20260516.md](wa-cluster-M02-debate-v1-20260516.md)), AI evaluated 47 terms against M02's characteristic (anger / wrath / indignation / jealousy / provocation / dispute / vexation) using each term's Phase 2 meaning corpus. The debate produced:

| Verdict | Count |
|---|---:|
| STAYS | 38 |
| TRANSFERS | 4 |
| BOUNDARY | 5 |
| **Total** | **47** |

This directive executes the 4 TRANSFERS (Op A) and the cluster status transition (Op N). The 5 BOUNDARY terms remain in M02 and will be placed in the M02-BOUNDARY sub-group at Phase 6 per v2_2 §7.4 (no Phase 4 DB write required for BOUNDARY).

## 2. SCOPE — Operation A (term transfers)

| mti_id | Strong's | Translit | Gloss | From → To | Rationale (abridged) |
|---:|---|---|---|---|---|
| 19 | G2052 | eritheia | rivalry | M02 → **M28-Envy** | Corpus consistently names selfish ambition, factional self-promotion, competitive self-seeking — not anger. Jam 3:14 pairs with bitter jealousy in heart. Rom 2:8 frames eritheia as cause of wrath, not wrath itself. |
| 3043 | H2102 | zid | to boil | M02 → **M08-Pride** | Corpus uniformly names insolent arrogance, presumptuous self-exaltation — the "boiling" register here is pride-driven defiance, not anger-heat. |
| 166 | H4843 | ma.rar | to provoke | M02 → **M03-Grief** | Corpus shows the term naming bitter inner sorrow (Job 27:2 — God has made my soul bitter) and grief-driven inner woundedness, not anger as the term's own content. |
| 214 | H6869C | tsa.rah | vexer | M02 → **M24-Weakness** | Corpus shows the term as one who afflicts/oppresses — the inner-being content centres on the recipient's suffering / pressure / constraint, not on the vexer's anger. |

## 3. SCOPE — Operation N (status transition)

Per v2_2 §7.6:

- `cluster.status` for M02: `Data - In Progress` → `Analysis - In Progress`
- Operation N is inline within this directive (not standalone).

## 4. BOUNDARY designation (recorded, no DB write per §7.4)

The following 5 terms remain in M02 and will be placed in the M02-BOUNDARY sub-group at Phase 6. Phase 12 closure requires explicit researcher disposition (set-aside / promote-to-M02-subgroup / reassign / retain-BOUNDARY).

| mti_id | Strong's | Translit | Gloss | Rationale (abridged) |
|---:|---|---|---|---|
| 1091 | G0485 | antilogia | dispute | Mixed register: procedural/intellectual (Heb 6:16, 7:7), hostility (Heb 12:3), self-assertive contention (Jude 11). No verse evidences anger-heat as primary inner-being content. |
| 4556 | G2042 | erethizō | to provoke/irritate | Thin corpus (2 verses); opposed valences (positive 2Cor 9:2 vs negative Col 3:21); inner-being focus is on recipient's discouragement, not provoker's anger. |
| 2747 | G2200 | zestos | hot | Thin corpus (2 verses); concerns fervent zeal vs lukewarmness (Rev 3:15-16) — closer to M34 Perseverance or M21 Prayer/devotion than M02. |
| 151 | H3708B | ka.a.s | vexation | Border ambiguity between anger-vexation (M02) and grief-vexation (M03). Researcher decision required. |
| 234 | H7379 | riv | strife | Phase 1 set aside 12 of 15 UT verses as legal-procedural; remaining is_relevant corpus is small and ambiguous between anger-driven contention and procedural dispute. |

## 5. OUTCOME REQUIRED

| Cluster | Pre-state | Δ | Post-state |
|---|---:|---:|---:|
| M02 (source) | 47 active terms | −4 | 43 active terms |
| M28 (destination) | 37 → ? | +1 | 38 |
| M08 (destination) | 47 → ? | +1 | 48 |
| M03 (destination) | 88 → ? | +1 | 89 |
| M24 (destination) | 73 → ? | +1 | 74 |
| **Sum of moves** | | **4** | |

Status: `cluster.M02.status` changes to `Analysis - In Progress`.

Note for destination clusters that are already `Analysis Completed` (M05, M06, M15, M26, M39, M46): not applicable here — all 4 destinations are `Not started`. If a future Phase 4 directive transfers to an `Analysis Completed` cluster, that cluster's status would update to `Analysis Completed (Terms Added)` per programme convention.

## 6. COMPLETION CONFIRMATION

Post-apply queries:

```sql
-- Source: M02 active term count
SELECT COUNT(*) FROM mti_terms
WHERE cluster_code='M02' AND status IN ('extracted','extracted_thin')
  AND COALESCE(delete_flagged,0)=0;
-- Expected: 43 (down from 47)

-- Each destination
SELECT cluster_code, COUNT(*) FROM mti_terms
WHERE cluster_code IN ('M28','M08','M03','M24')
  AND status IN ('extracted','extracted_thin')
  AND COALESCE(delete_flagged,0)=0
GROUP BY cluster_code;

-- Transferred terms by mti_id (verify destinations)
SELECT id, cluster_code, strongs_number, transliteration FROM mti_terms
WHERE id IN (19, 3043, 166, 214);

-- Cluster status
SELECT cluster_code, status FROM cluster WHERE cluster_code='M02';
-- Expected: 'Analysis - In Progress'
```

## 7. Pre-conditions (verified before apply)

| Check | Expected | Status |
|---|---|---|
| Source cluster status | `Data - In Progress` | TBD by apply script |
| Each destination cluster row exists | M28, M08, M03, M24 in `cluster` | TBD |
| Transferred terms exist and have status `extracted` or `extracted_thin` | 4 of 4 | TBD |
| All 47 M02 terms have a verdict in the debate file | 47/47 | ✓ |

## 8. Operations summary

| Op | Description | Rows |
|---|---|---:|
| A | UPDATE `mti_terms.cluster_code` for 4 transferred terms | 4 |
| N | UPDATE `cluster.status` for M02: Data - In Progress → Analysis - In Progress | 1 |
| _Total_ | | **5** |

## 9. Provenance & roll-back

- **Pre-apply backup:** `backups/bible_research_backup_*_DIR-20260516-008.db`
- **Audit:** every transferred term's row carries the new cluster_code; pre-state captured in backup.
- **Roll-back:** restore from pre-apply backup; OR inverse patch resetting `mti_terms.cluster_code` to 'M02' for the 4 transferred mti_ids + cluster.status back to 'Data - In Progress'.

---

*End of directive.*
