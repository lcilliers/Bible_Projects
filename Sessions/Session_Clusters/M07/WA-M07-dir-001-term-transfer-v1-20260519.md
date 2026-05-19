# wa-cluster-M07-dir-001-term-transfer-v1-20260519

> Cluster directive — M07 Phase 4 term transfers
> Cluster: M07 — Shame, Disgrace and Humiliation
> Date: 2026-05-19
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_7-20260519.md` §7

---

## MOTIVATION

Phase 3 constitution debate (v2, revised under the verse-level relationship test in §6.3.2) produced **2 TRANSFERS verdicts** and 5 BOUNDARY designations across M07's 36 terms. Source: [WA-M07-constitution-debate-v2-20260519.md](WA-M07-constitution-debate-v2-20260519.md). Co-occurrence list (informational, per §7.3.1): [WA-M07-phase4-cooccurrence-list-v1-20260519.md](WA-M07-phase4-cooccurrence-list-v1-20260519.md).

Both transfers are accidental-placement cases — the chesed root family. The Hebrew consonant cluster `ch-s-d` carries two distinct roots: (a) the narrow shame/reproach sense, and (b) the steadfast-love / loyal-faithfulness sense. M07 holds both Strong's IDs (H2616B, H2617B) as if they were the shame sense, but the actual meaning corpus on these two mti_terms evidences exclusively the loyal-love sense:

| mti_id | Strong's | Translit | Status | Verses | M07-relational? | Verdict |
|---:|---|---|---|---:|---|---|
| 338 | H2616B | cha.sad | extracted_thin | 2 is_relevant (3 vc rows) | 0 verses evidence shame relational content | TRANSFERS-TO-M05 |
| 1633 | H2617B | che.sed | extracted_thin | 162 is_relevant (296 vc rows) | 0 verses evidence shame relational content | TRANSFERS-TO-M05 |

Pass A meanings for both terms uniformly name steadfast love / loyal faithfulness / covenant devotion. None evidence shame, disgrace, or humiliation. The narrow shame sense of *chesed* (e.g., Pro 14:34 "reproach to a people") is absent from both terms' corpora — confirming the senses were data-separated but the dominant-sense term mis-classified to M07.

Other 8 originally-transfer candidates from v1 were retained as STAYS with cross-register flags per §6.3.2 (the verse-level relationship test surfaced active M07 relational content in every one of their corpora):

| mti_id | Strong's | Translit | Primary register flag |
|---:|---|---|---|
| 6115 | G0577 | apoballō | M19 (trust/confidence) — flag to Phase 5/7 |
| 974 | G0880 | afōnos | M09 (humility/meekness) — flag to Phase 5/7 |
| 1279 | G1848 | exoutheneō | M06 (contempt/hostility) — flag to Phase 5/7 |
| 838 | G2551 | kakologeō | M06/M42 — flag to Phase 5/7 |
| 1135 | G3059 | loidoria | M42 (speech) — flag to Phase 5/7 |
| 431 | G5392 | fimoō | M42 (speech) — flag to Phase 5/7 |
| 928 | H5356A | niq.qa.von | M12 (purity) — flag to Phase 5/7 |
| 5620 | H5356B | qe.ha.von | M12 (purity) — flag to Phase 5/7 |

The 5 BOUNDARY designations (G2699 katatomē, H4893A mish.chat, H5206 ni.dah, H8213 sha.phel, H8400 te.val.lul) have no Phase 4 DB writes per §7.4 — they remain in M07 and are processed at Phase 5/6 (sub-group formation places them in `M07-BOUNDARY`) and Phase 8.5 (BOUNDARY resolution finalises disposition).

## SCOPE

### Operation A — Term transfers (mti_terms.cluster_code UPDATE)

| mti_id | Strong's | Translit | Pre-cluster | Post-cluster |
|---:|---|---|---|---|
| 338 | H2616B | cha.sad | M07 | M05 |
| 1633 | H2617B | che.sed | M07 | M05 |

SQL:

```sql
UPDATE mti_terms
SET cluster_code = 'M05', last_changed = ?
WHERE id IN (338, 1633) AND cluster_code = 'M07' AND COALESCE(delete_flagged, 0) = 0;
```

Pre-check: both rows show `cluster_code='M07'`.
Post-check: both rows show `cluster_code='M05'`; affected row count = 2.

### Operation N — Cluster status transition (per §2.6, §7.6)

```sql
UPDATE cluster
SET status = 'Analysis - In Progress', last_updated_date = ?
WHERE cluster_code = 'M07' AND status = 'Data - In Progress';
```

Pre-check: `cluster.status='Data - In Progress'`.
Post-check: `cluster.status='Analysis - In Progress'`.

## OUTCOME REQUIRED

- 2 `mti_terms` rows moved M07 → M05 (cluster_code FK).
- M07 term count: pre - 2 = 34.
- M05 term count: pre + 2.
- M07 cluster.status: `Data - In Progress` → `Analysis - In Progress`.
- `verse_context` and `verse_context_group` rows for the 2 transferred terms remain unchanged (they resolve cluster ownership through `mti_term_id → mti_terms.cluster_code`).

## COMPLETION CONFIRMATION

Post-state queries:

```sql
-- Should return 34
SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M07' AND COALESCE(delete_flagged,0)=0;

-- Should show 'Analysis - In Progress'
SELECT status FROM cluster WHERE cluster_code='M07';

-- Should both return 'M05'
SELECT id, strongs_number, cluster_code FROM mti_terms WHERE id IN (338, 1633);
```

## ROLLBACK

```sql
-- Reverse term transfers
UPDATE mti_terms SET cluster_code='M07' WHERE id IN (338, 1633) AND cluster_code='M05';

-- Reverse status
UPDATE cluster SET status='Data - In Progress' WHERE cluster_code='M07' AND status='Analysis - In Progress';
```

## SCRIPT

`scripts/_apply_m07_phase4_term_transfer_20260519.py` — runs Op A + Op N with pre/post checks and reports.

---

*M07 Phase 4 term-transfer directive. BOUNDARY terms carried forward to Phase 5/6 with no Phase 4 writes; cross-register flags carried forward via the verdict document for Phase 5/7 consumption.*
