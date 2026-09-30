# `mti_terms` Deduplication — Migration Design — v1 — 2026-04-20

| Field | Value |
|---|---|
| Filename | mti-terms-dedup-design-v1-20260420.md |
| Trigger | OT-DBR-009 (HIGH priority) — raised 2026-04-19 during r68 sweep trial |
| Purpose | Design the migration(s) to consolidate 7,571 `mti_terms` rows into 3,955 canonical rows |
| Action reference | Programme control v1 — Action R |
| Sibling designs | Coverage flag redesign M29 (evidence-flag reframe); both independent |
| Status | **DRAFT v1 — awaiting researcher review** |
| Migration number (tentative) | M32 (after coverage-flag M29/M30/M31; can be re-ordered) |

---

## 1. Headline

**7,571 `mti_terms` rows → 3,955 canonical rows.** ~3,616 rows retire (hard-delete after FK repoint). ~1,269 FK references on five child tables must be repointed to canonical rows before the retirement. A post-migration `UNIQUE` index on `strongs_number` prevents recurrence.

Dry-run first (on DB copy); per-step backup discipline; reversible per migration step up to row retirement; point-of-no-return at hard-delete.

---

## 2. Current-state diagnostics (live DB 2026-04-20)

### 2.1 Duplication pattern

| Metric | Value |
|---|---:|
| Total `mti_terms` rows | 7,571 |
| Active (`delete_flagged=0`) | 3,891 |
| Delete-flagged | 3,680 |
| Distinct `strongs_number` | 3,955 |
| Avg rows per strongs | 1.91 |
| Strongs with 1 row (clean) | 2,175 |
| Strongs with 2+ rows (duplicated) | 1,780 (45%) |
| Strongs with >5 rows | 121 |
| Strongs with >10 rows | 5 |
| Worst case | 4 strongs with 15 rows each |

### 2.2 Status distribution

| Status | Rows |
|---|---:|
| `delete` | 2,611 |
| NULL | 2,276 |
| `extracted` | 2,291 |
| `extracted_thin` | 326 |
| `candidate_delete` | 32 |
| `extracted_theological_anchor` | 17 |
| `excluded` | 9 |
| `xref_*` (4 distinct values) | 4 |
| `phase2_enrichment` | 5 |

Notable: the designed XREF-marker pattern (`xref_[owner_word]`) was populated for only **4 rows** out of an expected ~1,470 XREF relationships. The `xref_*` status was effectively never adopted at scale.

### 2.3 Canonical-row selection test

Rule tested: canonical = `delete_flagged=0 AND status IN ('extracted','extracted_thin') AND owning_registry_fk IS NOT NULL`, tie-break `MIN(id)`.

| Outcome | Count |
|---|---:|
| Strongs with exactly one canonical row under the rule | 2,606 |
| Strongs with zero canonical rows under the rule | 1,349 |
| Strongs with **multiple** canonical rows under the rule | **0** (good — no ambiguity) |

### 2.4 No-canonical strongs — not orphans, actually XREF-only

Spot-check revealed the 1,349 "no-canonical" strongs are not orphan: they are **XREF-only strongs**. They appear in active `wa_term_inventory` rows (as XREF) but the registry-owner role was never assigned to any of their mti_terms copies.

Active references into no-canonical strongs:

| Child table | Active refs |
|---|---:|
| `wa_term_inventory` (strongs-keyed, not FK) | 2,558 |
| `verse_context` (FK → `mti_terms.id`) | 495 |
| `verse_context_group` (FK → `mti_terms.id`) | 32 |

So for these 1,349 strongs we need a **second canonical-row rule** that picks a single row to serve as the XREF target. Candidate rule: pick the oldest non-delete-flagged row, relabel status to a standardised XREF-only marker (or keep NULL + leave a marker in a new field).

### 2.5 FK references to non-canonical rows

References that will need repointing before retirement:

| Child table | FK column | refs → `status='delete'` | refs → `status=NULL` | Total refs to retire |
|---|---|---:|---:|---:|
| `mti_term_flags` | `mti_term_id` | 245 | 364 | 609 |
| `mti_term_cross_refs` | `mti_term_id` | 57 | 0 | 57 |
| `verse_context_group` | `mti_term_id` | 17 | 32 | 49 |
| `verse_context` | `mti_term_id` | 210 | 344 | 554 |
| `wa_session_b_findings` | `term_id` | 0 | 0 | 0 |
| **Total** | | **529** | **740** | **1,269** |

**Repointing is the central risk** — any FK left pointing to a retired row creates a broken reference.

### 2.6 Sample worst-case — strongs H0226G (15 rows)

| id | status | owning_registry | owning_word | delete_flagged | last_changed |
|---:|---|---|---|---:|---|
| 1169 | extracted | 159 | testimony | 0 | 2026-03-18 |
| 1451 | delete | NULL | sign: miraculous | 1 | 2026-03-25 |
| 4767 | NULL | NULL | sign: miraculous | 1 | 2026-03-28 |
| 4818 | NULL | NULL | sign: miraculous | 1 | 2026-03-28 |
| ...  | NULL | NULL | sign: miraculous | 1 | (12 more imports, 2026-03-28) |

Root cause: 14 re-import attempts on 2026-03-28 each inserted a new `mti_terms` row rather than updating. Canonical is obvious (`id=1169`, owning testimony r159).

---

## 3. Migration strategy — phased, reversible up to step 5

### Phase 0 — Prep

- Full DB backup labelled `pre_M32_mti_dedup`
- Dry-run on DB copy first

### Phase 1 — Canonical map construction

Build a mapping table `mti_canonical_map (strongs_number, canonical_id, selection_rule)`:

**Rule A — OWNER canonical:** `status IN ('extracted','extracted_thin','extracted_theological_anchor') AND delete_flagged=0 AND owning_registry_fk IS NOT NULL`, tie-break `MIN(id)`. Expected: 2,606 strongs.

**Rule B — XREF-only canonical:** For strongs not matched by Rule A, pick `status IS NOT 'delete' AND delete_flagged=0`, tie-break `MIN(id)`. Expected: most of 1,349 strongs. The picked row's `status` is updated to `'xref_canonical'` (new controlled-vocabulary value) as part of this phase.

**Rule C — fully-delete canonical:** For strongs where all rows are `delete` or `delete_flagged=1`: no canonical needed; all rows retire. Expected: small residual set.

Dry-run output: every strongs placed into A / B / C buckets with count.

**Decision needed:** Should Rule B pick `MIN(id)` (oldest), `MAX(id)` (newest), or some other signal (e.g. "the row most-referenced by active FKs")? Simpler to pick oldest; references-based picking adds complexity without obvious benefit.

### Phase 2 — FK repointing

For each of the four child tables with FK refs (`mti_term_flags`, `mti_term_cross_refs`, `verse_context_group`, `verse_context`):

```sql
UPDATE {child_table}
   SET {fk_col} = (
         SELECT cm.canonical_id FROM mti_canonical_map cm
          WHERE cm.strongs_number = (
                 SELECT strongs_number FROM mti_terms
                  WHERE id = {child_table}.{fk_col}
                )
       )
 WHERE {fk_col} IN (SELECT id FROM mti_terms)
   AND {fk_col} NOT IN (SELECT canonical_id FROM mti_canonical_map);
```

Ordering:
1. `mti_term_flags` (609 refs) — low-risk; flag data consolidates onto canonical rows, potentially creating duplicate `(mti_term_id, flag_id)` pairs which PK uniqueness will reject — must DISTINCT before UPDATE, or use INSERT OR IGNORE with a rebuild
2. `mti_term_cross_refs` (57 refs) — low-risk
3. `verse_context_group` (49 refs) — low-risk
4. `verse_context` (554 refs) — highest-volume; critical for Verse Context integrity

After each UPDATE: run FK integrity query — expect 0 refs still pointing to non-canonical rows.

**Known complication for `mti_term_flags`:** its PK is `(mti_term_id, flag_id)`. Repointing may create duplicates (same canonical_id + flag_id appearing twice). Strategy: rebuild `mti_term_flags` as `INSERT OR IGNORE ... SELECT DISTINCT canonical_id, flag_id FROM {old_rows}`; drop original; rename.

### Phase 3 — Post-repoint integrity verification

Five FK counts must all be 0:

```sql
SELECT COUNT(*) FROM {child_table} c
  LEFT JOIN mti_canonical_map cm ON cm.canonical_id = c.{fk_col}
 WHERE cm.canonical_id IS NULL
   AND c.{fk_col} IS NOT NULL;
```

If any non-zero: halt, diagnose, roll back via backup.

### Phase 4 — Retire non-canonical rows (HARD DELETE)

**Point of no return.**

```sql
DELETE FROM mti_terms
 WHERE id NOT IN (SELECT canonical_id FROM mti_canonical_map);
```

Expected rows deleted: ~3,616.

This is hard-delete because (a) FK refs have been repointed in Phase 2, (b) all retained rows have a canonical meaning, (c) keeping 3,616 orphan-rows defeats the purpose.

**Audit trail:** a `mti_terms_retired_audit` table captures the pre-delete state (id, strongs_number, status, owning_registry_fk, owning_word, delete_flagged, last_changed) for every retired row. Enables post-migration reconciliation if questions arise.

### Phase 5 — Enforce uniqueness going forward

```sql
CREATE UNIQUE INDEX idx_mti_terms_strongs_unique ON mti_terms (strongs_number);
```

Prevents future accidental duplication at insertion time. After this, any insert of a strongs already present raises a constraint violation — forcing the caller to UPDATE rather than INSERT.

### Phase 6 — Status value cleanup (optional consolidation)

Now that each strongs has one row:

- Strongs with Rule A canonical → status stays `extracted` / `extracted_thin` / `extracted_theological_anchor`
- Strongs with Rule B canonical → status becomes `xref_canonical` (new value added to controlled vocabulary)
- No rows should now have `status=NULL` or `status='delete'` post-Phase 4

This phase is a stamping exercise, not a restructure. Can merge with Phase 1 if preferred.

---

## 4. Risk assessment

| Risk | Severity | Mitigation |
|---|---|---|
| Wrong canonical chosen for a strongs (Rule A ties) | LOW | Rule A has 0 ambiguity in current data; tie-break `MIN(id)` is deterministic |
| Wrong canonical chosen for XREF-only strongs (Rule B) | MEDIUM | Spot-check 20 Rule-B selections; researcher confirms pattern holds before Phase 2 |
| FK repoint misses a reference | HIGH | Phase 3 integrity query guarantees 0 dangling refs before Phase 4; halt if non-zero |
| `mti_term_flags` PK duplication on repoint | MEDIUM | INSERT-OR-IGNORE rebuild pattern — must test on dry-run |
| Hard-delete in Phase 4 removes a row someone analytical cares about | MEDIUM | Audit table preserves full retired-row content; reversible via restore |
| Post-migration UNIQUE index prevents legitimate future multi-status rows | LOW | Designed intentionally — one strongs = one row is the target invariant |
| Active sweep/audit code breaks on consolidated rows | LOW-MEDIUM | Post-DBR code already joins through canonical row via `vcg.mti_term_id`; most consumer logic already assumes one-row-per-strongs |

---

## 5. Consumer-code audit

Scripts and engine modules that interact with `mti_terms`:

| Consumer | Change expected |
|---|---|
| `engine/audit_word.py` | Already post-DBR; joins canonical mti_terms via strongs_number. Should be unchanged by dedup — actually **benefits** from it. |
| `engine/audit.py` | Unchanged. |
| `scripts/apply_session_patch.py` | Uses `id` and `strongs_number` lookup. Should be unchanged. Verify no place does `id` lookup where post-dedup the id no longer exists. |
| `scripts/readiness_sweep_pilot.py` | Already has OT-DBR-010 canonical-row filter. Post-dedup, the filter becomes tautological (all rows are canonical) but the code is still correct. |
| `scripts/build_dimension_extract.py` | Joins through `verse_context_group.mti_term_id` → `mti_terms`; post-repoint always hits canonical. |
| `scripts/build_complete_extract.py` | Verify — likely same pattern. |
| `scripts/generate_session_a_extract.py` | New — already uses canonical lookup via `ORDER BY CASE status IN ('extracted',...)`. Post-dedup this ordering becomes redundant. |

No pre-migration consumer-code changes required. Post-migration cleanup (removing now-redundant canonical-selection logic) is cosmetic and can be deferred.

---

## 6. Rollback procedure

### Pre-Phase 4 (before hard-delete)
Full rollback via DB restore from `pre_M32_mti_dedup` backup. No data lost.

### Post-Phase 4 (after hard-delete)
Row-level rollback possible via `mti_terms_retired_audit` table:

1. INSERT retired rows back into `mti_terms` (regenerating original ids if preserved in audit)
2. Manually repoint affected FKs back (complex — reverse of Phase 2)

In practice: if Phase 4 goes wrong, restore from backup rather than row-level reverse. Keep the backup for at least 6 months per Q6 discipline.

### Post-Phase 5 (after unique index)
Drop the index:
```sql
DROP INDEX idx_mti_terms_strongs_unique;
```

---

## 7. Interaction with other programme work

### 7.1 M29 / M30 / M31 (evidence-flag redesign + provenance tracking + question-linking)

**No direct dependency.** Can run before, after, or in parallel with M32. The two design directions don't interact on schema or data.

### 7.2 OT-DBR-010 (pilot XREF join fix)

**Made redundant post-M32.** The pilot's current canonical-row EXISTS subquery was a workaround; post-dedup, every row is canonical, so the subquery always returns true. Can be simplified in a follow-up cleanup.

### 7.3 Readiness sweep scorecard

**Will refresh automatically** on next programme scan. Path 4 findings for broken XREFs should drop substantially (the ones caused by mti_terms duplication will vanish — only truly broken XREFs remain).

### 7.4 Session A / Session B extracts

**Unchanged.** Already use canonical-row lookups.

### 7.5 6 reset words (compassion, fellowship, forgiveness, grace, love, mercy)

**Benefit.** These are the words queued for Phase F.6 reprocess; cleaner mti_terms simplifies their re-extract + VC + DimReview cycles.

---

## 8. Testing and validation plan

### Dry-run verification (before live)

Dry-run on a fresh copy of the live DB. Measure:

1. Phase 1: canonical map population count — expect ~3,955 rows
2. Phase 2: per-table FK repoint count — expect ~1,269 total UPDATEs
3. Phase 3: all 5 integrity queries return 0
4. Phase 4: retire count — expect ~3,616
5. Phase 5: UNIQUE index creation — success
6. Post-migration: every active `wa_term_inventory.strongs_number` maps to exactly one `mti_terms` row

Regression test: after dry-run, run `readiness_sweep_pilot.py` on r68 grace (previously 24 findings post-OT-DBR-010) and r62 fellowship (BANKED). Expect r68 findings to drop further; expect r62 to remain BANKED.

### Live-run go/no-go checkpoints

- After Phase 0: backup succeeded, dry-run passed
- After Phase 1: canonical map sane on inspection (spot-check 20 strongs)
- After Phase 3: integrity queries all zero
- Before Phase 4: researcher sign-off on delete count
- After Phase 5: UNIQUE index success

---

## 9. Open decisions for researcher

| # | Question | Recommendation |
|---|---|---|
| 1 | **Approve the overall approach?** Hard-delete is the point of no return. | Proceed with approach |
| 2 | **Rule B tiebreaker** — oldest (MIN(id)), newest, or reference-count based? | MIN(id) — simplest, deterministic |
| 3 | **`xref_canonical` as new controlled-vocabulary status value?** | Yes — clean consolidation and avoids leaving NULL status on surviving rows |
| 4 | **Migration sequencing** — M32 before or after M29/M30/M31 (evidence-flag redesign)? Either order works; no dependency. | M32 first — it's atomic and clears a significant source of analytical confusion |
| 5 | **Phase 4 audit-table retention period** | 6 months per GR-BACKUP Q6 discipline; researcher may choose longer |
| 6 | **Restore `mti_term_flags` PK uniqueness strategy** — INSERT-OR-IGNORE rebuild vs aggregate-before-update | INSERT-OR-IGNORE rebuild cleanest for dry-run verification |
| 7 | **Execution mode** — single session, or staged with pauses between phases? | Single session with per-phase go/no-go checkpoints; not broken across days (too much risk of partial state) |

---

## 10. Estimate

| Phase | Effort |
|---|---|
| Design review + researcher approval | ~0.5 day |
| Dry-run script (Phase 1–5) implementation | ~1 day |
| Dry-run execution + iteration | ~0.5 day |
| Live execution + validation | ~0.5 day |
| Post-migration consumer-code cleanup (optional) | ~0.5 day |
| **Total** | **~2.5–3 days** |

Matches yesterday's estimate (Action R original: "~2-3 days").

---

## 11. Recommended next move

**Pause on execution. Put design to researcher review.** Open items §9 Q1–Q7 need direction before migration code is written.

Assuming §9 resolves cleanly:

1. Write migration code in `engine/migrate.py` as `_m32_mti_dedup` (or as standalone script — decide with researcher)
2. Dry-run on DB copy; iterate on failures
3. Researcher sign-off on dry-run outputs (per Phase 4 checkpoint)
4. Live execution with per-phase backups

---

*Draft v1 — 2026-04-20. Awaiting researcher approval on §9 before execution planning.*
