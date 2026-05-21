# wa-cluster-M08-dir-001-term-transfer-v1-20260520

> Cluster directive — M08 Phase 4 term transfers
> Cluster: M08 — Pride, Arrogance and Boasting
> Date: 2026-05-20
> Author: CC
> Governed by: `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §7

---

## MOTIVATION

Phase 3 constitution debate (run under the §6.3.2 verse-level relationship test) produced **3 TRANSFERS verdicts** and **1 BOUNDARY designation** across M08's 49 terms. Source: [WA-M08-constitution-debate-v1-20260520.md](WA-M08-constitution-debate-v1-20260520.md). Co-occurrence list (informational, per §7.3.1): [WA-M08-phase4-cooccurrence-list-v1-20260520.md](WA-M08-phase4-cooccurrence-list-v1-20260520.md).

All three transfers are accidental-placement cases — narrow-corpus terms whose Pass A meaning records evidence no pride / arrogance / boasting relational content in any verse:

| mti_id | Strong's | Translit | Status | Verses | M08-relational? | Verdict |
|---:|---|---|---|---:|---|---|
| 3081 | G0830 | authairetos | extracted | 2 is_relevant | 0 verses evidence pride/arrogance | TRANSFERS-TO-M29 |
| 4335 | H1984I | ha.lal | extracted | 5 is_relevant | 0 verses evidence pride/arrogance | TRANSFERS-TO-M16 |
| 1312 | H7989 | shal.lit | extracted | 1 is_relevant | 0 verses evidence pride/arrogance | TRANSFERS-TO-M23 |

### Rationale per transfer

**G0830 `authairetos` → M29 (Desire).** Both NT uses (2 Cor 8:3, 8:17) describe positive self-chosen volition in the Macedonian giving and in Titus's eagerness to come — the inner-being content is one of unprompted willingness, not pride-in-self. No verse in the corpus carries any pride-by-contrast or instrument-of-pride dynamic. Belongs in the volitional / desire register.

**H1984I `ha.lal` → M16 (Folly).** Homonymic sense-split from the boast/praise senses of the same consonantal root. This Strong's ID names "to rave / be mad" — the 5 verses (1 Sa 21:13, Job 12:17, Ecc 2:2, Ecc 7:7, Jer 25:16) uniformly describe feigned madness, oracle-bewildering, irrational laughter, oppression-induced disorientation, drunken folly. None evidence self-elevation or boasting. The boast/praise senses are carried by the other H1984 sense-splits which stay in M08; this one is a clean accidental placement on Folly.

**H7989 `shal.lit` → M23 (Strength).** Single occurrence (Gen 42:6) describing Joseph as governor over Egypt — neutral institutional authority, the verb of formal political rule. No verse in the corpus evidences pride-in-rule or arrogant authority; the M08-relevant "pride-of-rule" content is carried by other authority terms (e.g. `archō`, `exousia`, `kuriotēs`) which stay in M08 with cross-register flags. Belongs in the strength / capacity / power register.

### Cross-register flag STAYS (carried forward via verdict doc, not in this directive)

18 terms STAY in M08 with cross-register flags per §6.3.2 (verse-level relationship test surfaced active M08 relational content in every one of their corpora). Flags break down as:

| Primary register flag | Count |
|---|---:|
| M22 (majesty / glory) | 6 |
| M23 (strength / power / authority) | 5 |
| M04 (joy / delight) | 2 |
| M39 (blessing / praise) | 2 |
| M09 (humility — antonymic) | 1 |
| M28 (volition / will) | 1 |
| M42 (speech) | 1 |

Flags carry forward to Phase 5 (sub-group formation under §8.0 — characteristic-driven) and Phase 7 (VCG design) for informed placement. No Phase 4 DB write.

### BOUNDARY designation (no Phase 4 DB write, per §7.4)

| mti_id | Strong's | Translit | Reason cited | Resolution path |
|---:|---|---|---|---|
| 1113 | G0193 | akratēs | §6.3.1 reason 3 — supportive / qualifying register | Phase 5/6 sub-group `M08-BOUNDARY` → Phase 8.5 resolution |

`G0193 akratēs` ("without self-control") — corpus is supportive of pride-as-undisciplined-self-elevation but the term itself names the self-control deficit, not pride per se. Researcher decision at Phase 8.5: confirm BOUNDARY → either route to M27 (self-control register) or retain as supportive-qualifying within M08.

---

## SCOPE

### Operation A — Term transfers (mti_terms.cluster_code UPDATE)

| mti_id | Strong's | Translit | Pre-cluster | Post-cluster |
|---:|---|---|---|---|
| 3081 | G0830 | authairetos | M08 | M29 |
| 4335 | H1984I | ha.lal | M08 | M16 |
| 1312 | H7989 | shal.lit | M08 | M23 |

SQL:

```sql
UPDATE mti_terms
SET cluster_code = 'M29', last_changed = ?
WHERE id = 3081 AND cluster_code = 'M08' AND COALESCE(delete_flagged, 0) = 0;

UPDATE mti_terms
SET cluster_code = 'M16', last_changed = ?
WHERE id = 4335 AND cluster_code = 'M08' AND COALESCE(delete_flagged, 0) = 0;

UPDATE mti_terms
SET cluster_code = 'M23', last_changed = ?
WHERE id = 1312 AND cluster_code = 'M08' AND COALESCE(delete_flagged, 0) = 0;
```

Pre-check: all 3 rows show `cluster_code='M08'`.
Post-check: rows show their respective new `cluster_code` values; total affected row count = 3.

### Operation N — Cluster status transition (per §2.6, §7.6)

```sql
UPDATE cluster
SET status = 'Analysis - In Progress', last_updated_date = ?
WHERE cluster_code = 'M08' AND status = 'Data - In Progress';
```

Pre-check: `cluster.M08.status='Data - In Progress'`.
Post-check: `cluster.M08.status='Analysis - In Progress'`.

## OUTCOME REQUIRED

- 3 `mti_terms` rows reassigned: G0830 → M29, H1984I → M16, H7989 → M23 (cluster_code FK).
- M08 term count: pre - 3 = 46.
- M29 term count: pre + 1.
- M16 term count: pre + 1.
- M23 term count: pre + 1.
- M08 `cluster.status`: `Data - In Progress` → `Analysis - In Progress`.
- `verse_context` and `verse_context_group` rows for the 3 transferred terms remain unchanged (cluster ownership resolves through `mti_term_id → mti_terms.cluster_code`).
- BOUNDARY (G0193) — no DB write; carries forward to Phase 5/6.

## COMPLETION CONFIRMATION

Post-state queries:

```sql
-- Should return 46
SELECT COUNT(*) FROM mti_terms WHERE cluster_code='M08' AND COALESCE(delete_flagged,0)=0;

-- Should show 'Analysis - In Progress'
SELECT status FROM cluster WHERE cluster_code='M08';

-- Should each show the new destination
SELECT id, strongs_number, cluster_code FROM mti_terms WHERE id IN (3081, 4335, 1312);
```

## ROLLBACK

```sql
-- Reverse term transfers
UPDATE mti_terms SET cluster_code='M08' WHERE id IN (3081, 4335, 1312) AND cluster_code IN ('M29','M16','M23');

-- Reverse status
UPDATE cluster SET status='Data - In Progress' WHERE cluster_code='M08' AND status='Analysis - In Progress';
```

## SCRIPT

`scripts/_apply_m08_phase4_term_transfer_20260520.py` — runs Op A (3 transfers) + Op N (status advance) with pre/post checks and reports.

---

*M08 Phase 4 term-transfer directive. BOUNDARY (G0193) carried forward to Phase 5/6 with no Phase 4 write; cross-register flags carried forward via the verdict document for Phase 5/7 consumption.*
