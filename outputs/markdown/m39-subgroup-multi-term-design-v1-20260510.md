# M39 — Term-to-sub-group many-to-many design (v1)

**Programme:** Soul Word Analysis Programme — schema migration design
**Status:** DRAFT (awaiting researcher approval before any DB-touching code is written)
**Date:** 2026-05-10
**Driver:** Researcher decision 2026-05-10 — the 1:1 term→sub-group FK was forcing artificially wide sub-groups (M26-A absorbed God + Human + justification senses of the same Strong's term because it had nowhere else to live). Splitting M26-A into "God Righteousness" and "Human Righteousness — State of being right" requires the same term to belong to multiple sub-groups.
**Schema target:** v3.19.0 → v3.20.0 (migration code M39)

---

## 1. What changes

A single FK `mti_terms.cluster_subgroup_id` (1:1) becomes a join table `mti_term_subgroup` (m:n). Verses gain a direct `cluster_subgroup_id` so each verse-occurrence routes to ONE sub-group even when its term belongs to several.

### 1a. New table: `mti_term_subgroup`

```sql
CREATE TABLE mti_term_subgroup (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    mti_term_id         INTEGER NOT NULL
                          REFERENCES mti_terms(id),
    cluster_subgroup_id INTEGER NOT NULL
                          REFERENCES cluster_subgroup(id),
    is_primary          INTEGER NOT NULL DEFAULT 0,
    placement_note      TEXT,
    delete_flagged      INTEGER NOT NULL DEFAULT 0,
    created_at          TEXT NOT NULL,
    last_updated_date   TEXT NOT NULL,
    UNIQUE (mti_term_id, cluster_subgroup_id)
);
CREATE INDEX ix_mts_term ON mti_term_subgroup(mti_term_id)
  WHERE delete_flagged = 0;
CREATE INDEX ix_mts_subgroup ON mti_term_subgroup(cluster_subgroup_id)
  WHERE delete_flagged = 0;
```

`is_primary` flags the term's "home" sub-group (used by reports that need a single answer per term). Exactly one row per term should have `is_primary=1`. Backfill sets `is_primary=1` from the existing `mti_terms.cluster_subgroup_id`.

### 1b. New column: `verse_context.cluster_subgroup_id`

```sql
ALTER TABLE verse_context
  ADD COLUMN cluster_subgroup_id INTEGER
  REFERENCES cluster_subgroup(id);
CREATE INDEX ix_vc_cluster_subgroup
  ON verse_context(cluster_subgroup_id)
  WHERE delete_flagged = 0;
```

This is the per-verse routing answer. When a term is in two sub-groups, this column tells the renderer which one this verse belongs to. NULL is allowed for legacy/unrouted rows; backfill sets it from `mti_terms.cluster_subgroup_id` for terms that are still single-mapped.

### 1c. Legacy column: `mti_terms.cluster_subgroup_id`

**Decision needed (DEC-1):** keep as a "primary sub-group" view for backwards-compat scripts, OR drop after migration?
- *Option a* (keep, recommended): zero-cost compat for existing reports; column value mirrors `mti_term_subgroup.is_primary=1`. Triggers or post-migration cleanup keep them aligned.
- *Option b* (drop): forces all consumers to use the new join table; cleaner long-term, but every script that joins through this FK breaks until updated. ~12 scripts identified by grep.

### 1d. `cluster_finding.cluster_subgroup_id`

No change needed — findings remain pinned to a single sub-group via this FK (a finding exists in the context of one sub-group, even when the underlying term spans several).

---

## 2. What does NOT change

- `cluster` table — unchanged.
- `cluster_subgroup` table — unchanged structurally; new rows added per cluster as splits happen.
- `verse_context_group` / `verse_context.group_id` — unchanged. This was the per-term VC-group infrastructure; it remains for finer-grained verse cuts inside a sub-group.
- `wa_session_b_findings`, dimension tables, observation catalogue — all unchanged.

---

## 3. Migration sequence (M39)

1. **DDL** — create `mti_term_subgroup`; add `verse_context.cluster_subgroup_id` (nullable).
2. **Backfill `mti_term_subgroup`** — INSERT one row per `mti_terms` row where `cluster_subgroup_id IS NOT NULL`, with `is_primary=1`. ~243 rows.
3. **Backfill `verse_context.cluster_subgroup_id`** — UPDATE all active vc rows where the linked term has exactly one sub-group: SET cluster_subgroup_id = mt.cluster_subgroup_id. The 14 M26-A rows currently NULL on `group_id` are not affected by this; they just get their cluster_subgroup_id set from the term FK like the rest.
4. **Verification** — counts before/after; spot-check JOIN consistency; confirm no orphan FKs.
5. **Schema version bump** — append M39 to migration_history; set version_code = '3.20.0'.

Single transaction. Idempotent (pre-flight aborts if `mti_term_subgroup` already exists). Dry-run mode previews counts. ~2 sec wall time. No API calls. No cost.

---

## 4. Application to M26-A (the immediate driver)

After the schema migration is in place, a separate apply script does the M26-A split:

1. **Create two new sub-groups** in `cluster_subgroup` for cluster M26:
   - `M26-AG` — *God Righteousness* (label and core_description from `WA-M26A-god-righteousness-v1_0-20260509.md`)
   - `M26-AH` — *Human Righteousness — State of being right* (from `WA-M26A-human-righteousness-v1_0-20260509.md`)
2. **Map all 6 M26-A terms to BOTH** new sub-groups (12 rows in `mti_term_subgroup`); existing M26-A row per term retained (with `is_primary` flag now ambiguous — see DEC-2).
3. **Route verses** — for each of the 589 active M26-A verse_context rows, set `cluster_subgroup_id` to the M26-AG or M26-AH FK based on the subject classifier output (`m26-subject-claude-sonnet-4-6-M26-A-20260509.jsonl`).
   - 157 → M26-AG
   - 341 → M26-AH
   - 11 'both' → **DEC-3** below
   - 80 'neither' → **DEC-4** below
4. **Disposition of the original M26-A row** — **DEC-5** below.
5. **Verification** — both new sub-groups populated with expected term + verse counts; M26-A residual count behaves per DEC-5.

---

## 5. Decisions needed before code is written

| ID | Decision | Default | Note |
|----|----------|---------|------|
| DEC-1 | Keep `mti_terms.cluster_subgroup_id` for compat, or drop it? | **Keep** | Cheaper. ~12 scripts unaffected. Mirrors `is_primary=1`. |
| DEC-2 | When a term is mapped to multiple sub-groups, which is `is_primary`? | The pre-split sub-group (M26-A for the 6 M26-A terms) | Or pick the larger of the two new ones |
| DEC-3 | The 11 'both' verses (1Jn 2:29 / 3:7, 2Cor 5:21, Phil 3:9, Rom 10:4, Gen 15:6, Hos 10:12, Isa 56:1, etc.) — route where? | **M26-AG (God)** per the file's scope note | Alternative: leave M26-A as-is for these, marking them "hinge" |
| DEC-4 | The 80 'neither' verses (term qualifying impersonal nouns, adverbial uses, "weapons of righteousness", "for righteousness' sake") — route where? | **Hold in M26-A** (residual bucket — the original sub-group keeps the verses that don't fit the split) | Or create M26-AN "Righteousness — qualifier/abstraction" |
| DEC-5 | After the split, what is M26-A? | **Residual** (keeps the 'neither' verses; updated label + core_description; sort_order unchanged) | Or fully retired (delete_flagged=1) once empty |
| DEC-6 | Sub-group code format — `M26-AG` / `M26-AH` or `M26-A1` / `M26-A2` or other? | **`M26-AG` / `M26-AH`** (mnemonic) | |
| DEC-7 | Migration scope — schema migration applies to all 46 clusters at once (always); the M26-A apply script runs on M26 only? | **Yes** — schema is global, application is per-cluster | |
| DEC-8 | Backwards-compat for the existing 15 M26-A `verse_context_group` rows that already approximate this split? | **No change** — they continue to provide finer per-term cuts inside whichever new sub-group their verses land in | |

---

## 6. Files this change creates / touches

**New files (this design + the migration + the M26 apply):**
- `outputs/markdown/m39-subgroup-multi-term-design-v1-20260510.md` (this doc)
- `Workflow/schema/migrations/M39_term_subgroup_m2m.sql` (DDL only, optional)
- `engine/migrations/M39_term_subgroup_m2m.py` (engine-runnable migration, idempotent)
- `scripts/_apply_m26a_split_v1_20260510.py` (the M26-specific application; depends on M39 being applied first)

**Files that will need updating after M39 lands** (partial list — exact list confirmed by grep before code is written):
- `scripts/_generate_cluster_comprehensive_v1_20260505.py` — terms-by-sub-group join now via `mti_term_subgroup`; verses-by-sub-group join now via `verse_context.cluster_subgroup_id`
- `scripts/_generate_cluster_term_report_v1_20260505.py`
- `scripts/_generate_cluster_overview_v1_20260508.py`
- `scripts/_inspect_m26_meanings_v1_20260509.py`, `_inspect_m26_subject_v1_20260509.py` (cluster_subgroup_id now lives on verse_context too)
- Any future cluster reports

The legacy column stays populated, so most reports that join through `mt.cluster_subgroup_id = cs.id` keep working at the term level — they just won't see the verse-level split until updated to use `verse_context.cluster_subgroup_id`.

---

## 7. Risk + mitigation

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Backfill mis-routes verses (term→sub-group ambiguous because we just made it m:n) | Low for non-M26-A terms (they're still single-mapped) | Backfill SQL only sets `vc.cluster_subgroup_id` for terms with exactly one sub-group |
| Existing scripts break on missing column / unfamiliar join | Medium | Keep `mti_terms.cluster_subgroup_id` (DEC-1); flag scripts to update over time, not as a hard cut-over |
| `is_primary` drift over time (multiple primaries / no primary per term) | Medium | Add a CHECK or post-write validation in the migration; verification step counts terms-with-primary |
| `cluster_finding.cluster_subgroup_id` orphans if a sub-group is deleted | Low (no clusters being deleted as part of M39) | Standard FK behaviour; out of scope for this migration |
| Re-applying M39 against an already-migrated DB | Low | Pre-flight aborts if `mti_term_subgroup` already exists |

---

## 8. Cost + effort

- API: zero (no AI calls in the migration or the apply script).
- Wall time: migration ~2 sec; M26-A apply ~5 sec.
- My implementation effort: migration script + apply script + 2 renderer updates ≈ a half-day session.
- DB risk: low — all changes additive (new table, new column, backfill); no DROP / ALTER on existing data.

---

## 9. What I need from you

1. Approve / amend the 8 decisions in §5 (or signal "defaults are fine").
2. Confirm scope: just the schema migration + M26-A application this cycle, with renderer updates as a follow-up?

Once approved I'll:
1. Write `engine/migrations/M39_term_subgroup_m2m.py` (idempotent, dry-run-able)
2. Run it dry, present counts, get a go/no-go
3. Run it live
4. Write `scripts/_apply_m26a_split_v1_20260510.py` (idempotent, dry-run-able)
5. Run dry, present, go/no-go, run live
6. Regenerate the M26 comprehensive report against the new structure
7. Update renderers as needed for the new view
