# WA-M01-dir-002-subgroup-assign-applied-v1-20260515

**Directive:** [DIR-20260515-002 — wa-cluster-M01-dir-001-subgroup-assign-v1-20260515.md](wa-cluster-M01-dir-001-subgroup-assign-v1-20260515.md)
**Apply timestamp:** 2026-05-15T15:13:43Z
**Loader:** [scripts/_apply_m01_dir002_subgroup_assign_20260515.py](../../scripts/_apply_m01_dir002_subgroup_assign_20260515.py)

---

## Outcome

**9 sub-groups created · 86 term-to-subgroup links inserted (82 primary + 4 secondary cross-listings) · cluster.status flipped `Data - In Progress` → `Analysis - In Progress`.** All in one transaction.

---

## Verification — directive's 6 completion queries

### Q1 — M01 active term count: **82** ✓

### Q2 — Sub-groups created (9)

| Sub-group | Label |
|---|---|
| M01-A | Reverential Fear / Fear of God |
| M01-B | Threatening / Creaturely Fear |
| M01-C | Terror and Dread |
| M01-D | Dismay and Alarm |
| M01-E | Trembling and Shuddering |
| M01-F | Anxiety |
| M01-G | Awe and Wonder |
| M01-H | Timidity and Cowardice |
| M01-BOUNDARY | Boundary |

### Q3 — Term counts per sub-group

| Sub-group | Count | Expected |
|---|---:|---:|
| M01-A | 19 | 19 ✓ |
| M01-B | 13 | 13 ✓ |
| M01-C | 17 | 17 ✓ |
| M01-D | 5 | 5 ✓ |
| M01-E | 19 | 19 ✓ |
| M01-F | 3 | 3 ✓ |
| M01-G | 4 | 4 ✓ |
| M01-H | 3 | 3 ✓ |
| M01-BOUNDARY | 3 | 3 ✓ |
| **Total** | **86** | **86** ✓ |

### Q4 — H6 health check: **0** ✓ (all 82 active M01 terms have at least one `mti_term_subgroup` row)

### Q5 — Cluster status: **`Analysis - In Progress`** ✓ (transition 2026-05-15T15:13:43Z)

### Q6 — Representative term per sub-group

| Sub-group | Strong's | mti_id | Transliteration |
|---|---|---:|---|
| M01-A | H3374 | 269 | yir.ah |
| M01-B | G1719 | 257 | emfobos |
| M01-C | H0367 | 284 | e.mah |
| M01-D | H0926 | 92 | ba.hal |
| M01-E | H2729 | 305 | cha.rad |
| M01-F | H1674 | 107 | de.a.gah |
| M01-G | G1568 | 16 | ekthambeo |
| M01-H | G1167 | 288 | deilia |
| M01-BOUNDARY | G1280 | 4481 | diaporeō |

---

## CC alignment notes

### Schema reality vs directive wording

The directive references `mti_terms.cluster_subgroup_id` (in §SCOPE and §COMPLETION CONFIRMATION). That column does not exist on `mti_terms`. The cluster-to-subgroup mapping is held entirely in the m:n table `mti_term_subgroup`. CC used `mti_term_subgroup` for all 86 INSERTs — same precedent as DIR-20260515-001. The Q4 H6 health check was rewritten to test the equivalent (no active `mti_term_subgroup` row for an M01 active term) rather than `cluster_subgroup_id IS NULL`.

### 86 rows vs 82 terms — the 4 cross-listings

Per directive §3, four terms appear in two sub-group lists. CC inserted one `mti_term_subgroup` row per (term, sub-group) pair, distinguishing primary vs secondary in the `placement_note` field. The 4 cross-listed terms:

| Strong's | mti_id | Primary | Secondary | Rationale (from directive) |
|---|---:|---|---|---|
| H2865 *cha.tat* | 703 | M01-D | M01-A | "primary D; VCG-003 (reverential awe) verse-routed to A in Phase 6" |
| H2730 *cha.red* | 310 | M01-A | M01-E | "primary A (VCG-001: trembling at word of God); cross-listed E: trembling vocabulary" |
| G5156 *tromos* | 308 | M01-E | M01-A | "primary E; VCG-002 (trembling reverential service) verse-routed to A" |
| H6206 *a.rats* | 306 | M01-A | M01-E | "primary A (VCG-002: holy reverence); cross-listed E: trembling vocabulary" |

`placement_note` for each row carries `[primary]` or `[secondary]` tag plus the directive's rationale text. Phase 6 VCG mapping will be able to route specific verses to either sub-group.

### Preconditions verified before any write

- M01 active term count = 82 (matches directive expectation)
- Existing M01 subgroups in `cluster_subgroup` = 0 (no conflicts)
- All 82 mti_ids in directive verified present, M01, active, with Strong's matching directive's claims

---

## Side effects

- Each row in `cluster_subgroup` carries `cluster_code='M01'`, `status='active'`, `version='v1'`, `source=<directive id>`, `created_at`/`last_updated_date` = apply timestamp, `sort_order` 1..9 (matches directive list order).
- `cluster.last_updated_date` bumped to apply timestamp on the status flip.
- No `cluster_finding`, `verse_context`, `verse_context_group`, `vcg_term`, or `wa_session_b_findings` rows touched.

---

## Next steps

Per cluster-instruction v1_13:

1. **Phase 5** — 250-word first-reading summary per sub-group (§8) — input to Phase 6.
2. **Phase 6** — VCG reconciliation (§9), three-pass: Pass A read every verse + write meaning to obslog; Pass B design VCGs fresh; Pass C reconcile against existing 116 inherited VCGs. *(reminder for AI in [WA-M01-phase6-reminder-to-AI-v1-20260515.md](WA-M01-phase6-reminder-to-AI-v1-20260515.md))*
3. **Phase 7** — group-verse mapping (DIR-20260515-003 expected).

For CC to support Phase 5/6, a fresh grouped report (`scripts/_generate_cluster_grouped_v1_*.py`) will be needed after this directive lands.

---

## Provenance

- Directive: [Sessions/Session_Clusters/M01/wa-cluster-M01-dir-001-subgroup-assign-v1-20260515.md](wa-cluster-M01-dir-001-subgroup-assign-v1-20260515.md)
- Source comprehensive report: `wa-cluster-M01-comprehensive-v4-20260515.md`
- Phase 4 analytical basis: `wa-obslog-M01-cluster-m01-v1-20260515.md`
- Governing instruction: `wa-sessionb-cluster-instruction-v1_13-20260514` §7
- Predecessor: DIR-20260515-001 (cross-cluster term transfer, 12 terms out)
- Backup: `backups/bible_research_backup_20260515_161343_DIR-20260515-002.db`
