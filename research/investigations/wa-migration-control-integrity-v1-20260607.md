# Migration control-system integrity — investigation

> **Investigation · v1 · 2026-06-07 · CC.** Triggered by the registry/history drift found while planning the
> V3_2 migration, and the researcher's concern that the control system may be compromised — possibly by the
> 2026-06-03 DB restore. Read-only. **Verdict: the schema is intact; the *control process* drifted (real,
> pre-existing); the restore is NOT the cause.** Do **not** run `--migrate` until the control system is
> reconciled (§4).

---

## 1. What was found

| Signal | Finding |
|---|---|
| `migration_history` entries | **52** (M01–M54, **missing M18, M39**), latest applied **2026-05-27** |
| `migrate.py` registered | **M01–M17, M19–M39** (38; M18 never registered) — frozen at **M39** |
| Last edit to `migrate.py` | **2026-04-28** (git) — untouched since |
| `EXPECTED_SCHEMA_VERSION` (constants) | **3.27.0** | vs DB `version_code` **3.28.0** (constant lags) |
| M39 (registered, not in history) | "delete NULL-skeleton verse_context rows" — **target = 0 rows today (no-op)** |
| `_fix_migration_history.py` | a **benign one-time dedup** of history (archived); not a falsification |
| "m39" name reuse | unrelated `_apply_m39_dir_*` directive scripts (2026-05-14) — **number collision** |

## 2. The decisive check — IS THE SCHEMA INTACT?

**Yes.** Every schema change that M40–M54 claim to have made **is present** in the live DB (18/18 verified):
`analysis_note`, `wa_prose_section_citations`, `cluster_subgroup` + `mti_terms.cluster_code`,
`cluster_finding` (+ `vcg_scope`, `characteristic_id`), `mti_term_subgroup`, `vcg_term`, `characteristic` +
`cluster_observation`, `verse_context.keywords`, `finding_citation`, `cluster.char_structure`,
`prose_section.cluster_code`. **The restore preserved the full schema through M54.**

## 3. What actually happened (the real story)

- **`migrate.py` was the canonical migration registry through ~M39 (late April 2026), then was abandoned.**
  Git confirms it was last touched 2026-04-28. From **M40 onward (2026-04-27 → 05-27)**, schema changes were
  applied via **one-off `_apply_*` scripts** and direct ALTERs — recorded in `migration_history` but **never
  registered in `migrate.py`**. The registry simply froze; the DB kept moving.
- **The `migration_history` is trustworthy as a record** (the only edit was a benign dedup), and it **matches
  the live schema** (§2). The version constant (3.27.0) was not kept in step with the DB (3.28.0).
- **The restore is not implicated.** M40–M54 all applied *before* the restore point (2026-05-28) and are all
  present in the restored schema. The drift is a **pre-existing process change**, not a restore artifact.

**So: the *data/schema* is sound. The *control system* (single-source-of-truth, version tracking,
numbering) is what broke** — exactly the researcher's concern, validated, but it is a **process** failure,
not corruption.

## 4. Why NOT to run `--migrate` now

The engine runner applies *registered* migrations not yet in history. With the current state it would fire
**M39** (registered, not in history). M39 is a no-op today (0 target rows), so it is low-risk — **but it is
the wrong path**: running the frozen registry against a DB that moved past it by one-off scripts invites
exactly the kind of mismatch we are trying to fix. **Adding the V3_2 migration to this frozen registry and
running `--migrate` would compound the drift.**

## 5. Recommendation — reconcile before V3_2 (don't plaster)

Before the V3_2 schema migration, **re-establish a single source of truth**:

1. **Decide the canonical mechanism going forward** — either (a) **re-adopt `migrate.py`** as the registry
   (backfill M40–M54 as recorded/idempotent entries so registry = history), or (b) **formally bless the
   one-off-script pattern** with a documented protocol + a registry table. *(Recommend (a): one runner, one
   registry, idempotent, dry-run-able.)*
2. **Backfill the registry** with M40–M54 (idempotent `CREATE/ALTER … IF NOT EXISTS` mirrors of what the
   one-off scripts did) so `--migrate` is a clean no-op against the current DB — proving the registry and the
   DB agree.
3. **Resolve M39** — mark it applied/superseded (target is 0; the cleanup already happened), so it stops
   showing as pending.
4. **Fix `EXPECTED_SCHEMA_VERSION`** to match the DB (3.28.0) and keep it in step thereafter.
5. **Retire the "m39" name collision** — the `_apply_m39_dir_*` scripts are directive scripts, not migration
   M39; archive/rename to avoid confusion.
6. **Then** apply the V3_2 migration (`wa-v3_2-schema-migration-plan-v1`) as the **next** registry entry
   (M55), via the now-canonical runner, after backup + dry-run.

## 6. What this does NOT establish

- This verifies **schema** integrity, not **row-level data** completeness. The known 2026-06-03 loss (June
  1–2 work, DB recovered to 2026-05-28) is separate and already tracked.
- It does not audit the *correctness* of the one-off scripts' data effects — only that the schema objects
  exist. A deeper row-level audit is a separate exercise if wanted.

---

## Verdict

**Good news:** the restored DB's schema is intact through M54; no structural loss; the V3_2 migration is
still safe to design as planned. **Validated concern:** the migration control system genuinely drifted
(registry frozen at M39; one-off scripts; version constant lagging) — a process failure to fix **before**
adding V3_2, so we don't build the new work on an unreconciled base. **Restore exonerated** on this point.
