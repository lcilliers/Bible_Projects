# Row-level completeness check — pre-rebuild baseline

> **Investigation · v1 · 2026-06-07 · CC.** Read-only. Establishes the DB's row-level data state before the
> V3_2 rebuild, and checks whether the **June 1–2 repairs reverted with the 2026-06-03 restore** (the DB was
> restored to May-28; June 1–2 work was applied via handler scripts, not patches, so it was lost — see
> `outputs/markdown/wa-db-recovery-assessment-20260603.md`). **Conclusion: foundational data is largely
> intact; one small term-layer cleanup is needed before the rebuild; everything else is superseded by the
> rebuild.**

---

## 1. Foundational counts (active, sane)

| Table | Active rows |
|---|---|
| `mti_terms` | 4,007 |
| `wa_term_inventory` | 7,015 |
| `wa_verse_records` | 62,753 |
| `verse_context` | 43,493 |
| `verse_context_group` | 1,088 |
| `cluster_finding` | 19,996 |

No gross loss — the extraction/foundation layer is present.

## 2. The three June 1–2 repair items — state now

The restore (to May-28) predates the June 1–2 repairs, so the issues those repairs fixed are present again:

### a) `mti_terms` term-layer pollution — **needs cleanup (the rebuild reads it)**
- **51 duplicate rows** (26 `(strongs, owning_registry_fk)` groups with >1 active row) — mostly
  `status='delete' / candidate_delete / xref_*` rows never soft-deleted.
- **92 active rows with no active inventory**, which split into:
  - **~42 genuine ghosts** — `status='delete'`, `cluster_code` NULL → should be soft-deleted.
  - **~50 FLAG-cluster parked terms** — `cluster_code='FLAG'`, `status` excluded/extracted → **legitimate
    holding state, leave alone** (FLAG is the parking bucket).
- **Net cleanup target ≈ 51 + 42 ≈ 93 rows** — i.e. **re-do the lost June-1 mti_terms dedup**, scoped to the
  delete-status duplicates/ghosts only. *(This is the only pre-rebuild row-level action.)*

### b) `verse_context` ghost-duplicates — **superseded by the rebuild**
- **296 ghost-dup rows** = the **same `(verse_record_id, mti_term_id)` assigned to two different VCGs**
  (e.g. verse 144 / term 246 in groups 124 **and** 125), concentrated in **56 terms**. An artifact of the
  **old VCG model**.
- **The V3_2 rebuild re-forms the entire VCG layer from scratch (L2 → L3)**, so these old-VCG ghosts are
  **superseded** — not worth cleaning separately. *(Verify the rebuild's L1 ingests cleanly where a verse-term
  currently has two rows; fold any tidy-up into L1 pre-flight.)*

### c) Orphan VCGs — **clean (0)**
No active VCG lacks a member verse. Either the May-28 DB never had the 125 orphans the June-1 dissolution
targeted, or they were already clean.

## 3. The rest of the lost June 1–2 work — **moot under V3_2**

The recovery assessment lists more lost work — all of it **re-done or superseded by the V3_2 rebuild**, so it
needs **no separate redo**:
- **Cluster closures** (M10c, M10b, M08, M38, M20 Phase A) — the rebuild **re-analyses every cluster from
  scratch**; these closures are replaced, not restored.
- **Remediation orchestrator / COMMENT_EVALUATION / audit gates A10, VRACT / dedup-ghost handlers** — built
  for the **old remediation flow, which V3_2 supersedes** (Session D is moot; remediation folded into the
  cluster roll-up). Not needed.
- **pointer `cluster_link` / FLAG-cluster classification / M38 sub-group backfill** — re-established by the
  rebuild's L1/L2/L8.

So the restore's true cost, **for the rebuild**, is small: a **~93-row term dedup**. The big-ticket June 1–2
items are things the rebuild was always going to redo.

## 4. Recommendation

1. **Before the rebuild: re-do the scoped mti_terms dedup** — soft-delete the ~51 duplicate + ~42
   delete-status ghost rows (delete/candidate_delete status, no inventory, NULL cluster). **Leave the ~50
   FLAG-cluster parked terms.** This is a small DB write — propose to do it with a backup + a `--dry-run`
   listing for the researcher to eyeball the exact rows first.
2. **Verse-context ghosts:** no separate action — fold into L1 of the first cluster (the rebuild re-forms
   VCGs). Note it in the V3_2 instruction's L1 pre-flight.
3. **Nothing else** — the remaining lost work is superseded by the rebuild.

## 5. Honest limits

- This checks the **inner-life working tables** (terms, verses, verse-context, VCGs, findings). It is not a
  byte-level diff against the lost June-2 DB (which is unrecoverable).
- The "≈" counts on the dedup target are from status/cluster breakdowns; the actual soft-delete should run
  off an explicit row list (dry-run) the researcher approves, not the estimate.

---

*Verdict: the rebuild can proceed on a sound foundation after a small, well-scoped term dedup. The restore's
damage to the rebuild path is minimal — most of the lost June 1–2 work is exactly what V3_2 re-does anyway.*
