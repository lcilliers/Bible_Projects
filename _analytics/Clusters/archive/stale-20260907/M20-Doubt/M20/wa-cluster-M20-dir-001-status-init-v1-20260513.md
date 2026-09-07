# wa-cluster-M20-dir-001-status-init-v1-20260513

> **Directive ID:** DIR-20260513-M20-001
> **Cluster:** M20 (Doubt, Despair and Anxiety)
> **Pattern:** Cluster-process directive, compact form (single UPDATE) per `wa-directive-instruction [current]`
> **Governed by:** `wa-sessionb-cluster-instruction [current]` §4.1 — Status-init directive (required at session open, before any analytical work)
> **Authored:** 2026-05-13

---

## 1. MOTIVATION

Session B cluster analytical session opened for M20 (Doubt, Despair and Anxiety). Phase 1 comprehensive data has been prepared (`Sessions/Session_Clusters/M20/wa-cluster-M20-comprehensive-v1-20260513.md`). Per the cluster instruction §4.1, the first cluster-process directive at session open transitions `cluster.status` from `Not started` to `Data - In Progress`, registering the analytical session as active. This is `dir-001` for M20.

Source documents:
- Phase 1 comprehensive report: `Sessions/Session_Clusters/M20/wa-cluster-M20-comprehensive-v1-20260513.md`
- Governing instruction: `Workflow/Instructions/wa-sessionb-cluster-instruction-v1_4-20260513.md` §4.1

## 2. SCOPE

**Table touched:** `cluster`

**Operation:**

```sql
UPDATE cluster
   SET status = 'Data - In Progress',
       last_updated_date = ?    -- current UTC timestamp, ISO-8601
 WHERE cluster_code = 'M20'
   AND status = 'Not started';
```

**Set-aside handling:** N/A — single-row metadata update; no verse or term rows touched.

## 3. OUTCOME REQUIRED

- Exactly **one row updated**.
- Post-state: `cluster.status = 'Data - In Progress'` for `cluster_code = 'M20'`.
- Post-state: `cluster.last_updated_date` reflects the directive's apply timestamp.
- All other columns on the row unchanged (no collateral writes).

## 4. COMPLETION CONFIRMATION

CC runs:

```sql
SELECT cluster_code, status, last_updated_date
  FROM cluster
 WHERE cluster_code = 'M20';
```

Expected result:

| cluster_code | status | last_updated_date |
|---|---|---|
| M20 | Data - In Progress | (apply timestamp, ≥ 2026-05-13) |

And, untouched-table check (paranoia — confirm no collateral writes):

```sql
SELECT COUNT(*) FROM cluster WHERE status = 'Analysis Completed';
-- Expected: unchanged from pre-apply count (currently 4 — M05, M06, M15, M26)
```

## 5. Post-apply

- Record the transition in the M20 obslog (Phase 1 section): "Cluster status `Not started` → `Data - In Progress` via DIR-20260513-M20-001 at {timestamp}".
- Phase 1 process steps 1–4 (read the comprehensive report) may now begin.
