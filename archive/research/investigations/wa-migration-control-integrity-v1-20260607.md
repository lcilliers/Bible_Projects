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
| `EXPECTED_SCHEMA_VERSION` (constants) | **3.27.0** — lags the DB `version_code` **3.28.0** |
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

## 4. The runner flaw (the real root cause)

**Correction to the first read:** the original `run_migrations` did **not** skip already-applied
migrations — it executed **every** registered migration on each invocation, relying on each being perfectly
idempotent (it only skipped *recording* duplicates, not *executing*). Several migrations carry
**unconditional `version_code` bumps** (e.g. M39 sets `'3.16.1'`). So running `--migrate` against this DB
would have **re-run 38 migrations and reset `version_code` 3.28.0 → 3.16.1**, plus re-execute data
migrations (M15/M19/M23/M29/M39). *This* is the root control flaw — and it explains **why** the team
abandoned the registry for one-off scripts: the runner was never safe to re-run after the DB diverged.

## 4b. Reconciliation APPLIED (2026-06-07, code-only, no DB writes)

1. **Runner made history-aware** — `run_migrations` now skips any ref already in `migration_history`; it only
   executes genuinely pending migrations. (Strictly safer: it does *less*.)
2. **M39 version-bump removed** — a data-cleanup migration must not set `version_code` (let alone lower it).
   M39 is now a pure idempotent no-op (0 target rows today).
3. **Registry backfilled** — M16, M17, M40–M54 registered as documented, non-executing (`pass`) entries
   (they are in history → skipped). **Registry now ⊇ history**; nothing in history is unregistered. M18
   remains a documented gap (in neither; schema intact regardless).
4. **`EXPECTED_SCHEMA_VERSION` → 3.28.0** (was 3.27.0, lagging the DB by one — M54).
5. **Verified:** `--db-status` → version aligned, "Migration needed: no"; only **M39** pending (the no-op),
   which self-records harmlessly when V3_2/M55 is applied.

The single remaining DB-side reconciliation (recording M39) now rides along with the V3_2 migration —
**one** backed-up, dry-run-verified `--migrate` instead of two.

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
