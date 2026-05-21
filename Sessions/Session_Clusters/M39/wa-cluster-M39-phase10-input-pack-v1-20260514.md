# M39 — Phase 10 input pack (CC-prepared)

**Cluster:** M39 — Blessing, Favour and Grace
**Phase:** 10 — Verification, BOUNDARY exit, closure
**Authored by:** Claude Code, 2026-05-14
**Purpose:** consolidate all CC-prepared analytical and mechanical inputs needed for AI to author **dir-005 verification-corrections** per v1_11 §13.7 (single packaged directive carrying corrections, gap resolution, BOUNDARY exit, and the `Analysis Completed` status flip).

---

## Status going into Phase 10

| Phase | Directive | Status |
|---|---|---|
| 4 | dir-001 subgroup-assign | ✓ applied |
| 7 | dir-002 M39-A mapping | ✓ applied |
| 7 | dir-003 M39-B mapping | ✓ applied |
| 9 | dir-004 findings-record | ✓ applied (380 `cluster_finding` rows) |
| **10** | **dir-005 verification-corrections** | **NOT YET AUTHORED — this pack is its input** |

`cluster.status = 'Analysis - In Progress'`.

---

## Section 1 — Gap-row resolution (T6.7.1 [A], T6.7.1 [B], T6.7.3 [CLUSTER])

These three `cluster_finding` rows are currently at `finding_status='gap'`. CC has computed the answers and proposes the text below. AI to confirm wording, then include as `cluster_finding` UPDATE operations in dir-005's SCOPE.

### Data summary

`wa_dimension_index` carries dimensions on `verse_context_group_id` (persists across the 2026-05-04 C→M cluster pivot). M39 VCG coverage in the dim index: **34 of 35 (97%)**.

**M39 dimensional fingerprint:**

| Sub-group | VCGs | Distinct dims | Dominant dim |
|---|---:|---:|---|
| M39-A | 23 | 5 | `06 — Relational Disposition` (14 of 23 VCGs) |
| M39-B | 4 | 3 | `01 — Emotion — Positive` (2 of 4 VCGs) |
| M39-BOUNDARY | 8 | 6 | (mixed — informational only) |

**Cluster-wide overlap:** M39 shares ≥1 dimension with **45 other M-clusters**. 19 share all 6 of M39's dimensions. Lowest sharers: M15 (1 dim only — `03 — Cognition`) and M20 (1 dim only — `05 — Moral Character`).

### Proposed resolution text — review and revise as needed

#### T6.7.1 [A] — proposed (currently `gap`)

> M39-A's 23 active VCGs carry 5 of the programme's 11 analytical dimensions: `06 — Relational Disposition` (14 VCGs — dominant), `05 — Moral Character` (4), `11 — Divine-Human Correspondence` (3), `04 — Volition` (1), `01 — Emotion — Positive` (1). The sub-group's dimensional signature is **relational disposition**: more than half of M39-A's VCGs sit in that register, consistent with grace as constitutively a disposition of one party toward another. The full 5-dimension set is shared with 14+ other M-clusters (M02, M03, M04, M05, M08, M09, M10, M18, M19, M22, M23, M26, M27, M28); M39-A occupies the core inner-being dimensional space rather than a rare corner.

Proposed `finding_status` = `finding`.

#### T6.7.1 [B] — proposed (currently `gap`)

> M39-B's 4 active VCGs carry 3 dimensions: `01 — Emotion — Positive` (2 VCGs — dominant), `05 — Moral Character` (1), `03 — Cognition` (1). The sub-group's dimensional signature is **positive emotion**, consistent with the affective-gladness pole of tov/ya.tav. All 3 dimensions are shared with 15+ other M-clusters; M39-B sits in the affective register that M04 (Joy), M22 (Praise), and M33 (Peace) also occupy.

Proposed `finding_status` = `finding`.

#### T6.7.3 [CLUSTER] — proposed (currently `gap`)

> M39 carries 6 of the programme's 11 dimensions across its sub-groups; shares ≥1 dimension with 45 other M-clusters. 19 clusters share all 6 of M39's dimensions, placing M39 firmly in the core inner-being dimensional register, not at a rare-dimension corner. The discriminating signal is at sub-group level rather than cluster level: M39-A on `06 — Relational Disposition`, M39-B on `01 — Emotion — Positive`. The lowest-sharing M-clusters with M39 are M15 (wisdom — 1 dim, `03 — Cognition`) and M20 (doubt/despair/anxiety — 1 dim, `05 — Moral Character`); these are the two complete clusters whose characteristic content sits furthest from grace+goodness on the dimensional axis.

Proposed `finding_status` = `cluster_synthesis` (it was authored as a CLUSTER-scope finding originally).

### How AI packages this in dir-005

For each of the three rows, the directive's SCOPE includes:

```
Operation: cluster_finding gap resolution

UPDATE cluster_finding
   SET finding_status = '{finding|cluster_synthesis}',
       finding_text = '<resolved text from above>',
       notes = notes || '; gap resolved by dim-share analysis 2026-05-14',
       last_updated_date = ?
 WHERE id = <id_for_T6.7.1_A | T6.7.1_B | T6.7.3>
```

The ids can be resolved by AI in the directive's SCOPE via `WHERE cluster_code='M39' AND obs_id=<T6.7.1-or-T6.7.3-obs-id> AND cluster_subgroup_id=<A|B|NULL>` — or AI can leave the WHERE clauses symbolic and CC will resolve at apply time.

---

## Section 2 — BOUNDARY exit (§13.6, §15)

Three terms in M39-BOUNDARY require explicit exit before closure. Full analysis: [outputs/markdown/m39-boundary-exit-investigation-v1-20260514.md](../../outputs/markdown/m39-boundary-exit-investigation-v1-20260514.md).

| Term | CC recommendation | DB operation for dir-005 |
|---|---|---|
| H2868 te.ev (mti=633, 1 verse) | **Cluster reassignment to M04 (Joy)** — `owning_word='gladness'`, Dan 6:23 = exceedingly glad. M39 was a routing error. | `UPDATE mti_terms SET cluster_code='M04' WHERE id=633`; soft-delete the M39-BOUNDARY `mti_term_subgroup` row for mti=633. VCG 633-001 stays as-is (it's keyed by `group_code`). |
| G1435 dōron (mti=6837, 17 verses, 6 VCGs, 5 anchors) | **Promote to M39-A** (not on AI's option list) — characteristic-bearing by the data: 17 verses, 6 designed VCGs, Eph 2:8 grace-as-gift anchor. | `UPDATE mti_term_subgroup SET cluster_subgroup_id=<M39-A id> WHERE mti_term_id=6837 AND cluster_subgroup_id=<M39-BOUNDARY id>`. Phase 8 catalogue coverage gap: see note in the investigation doc. |
| H7862 shay (mti=2976, 3 verses) | **Set aside within M39** — concur with AI. Reverence/homage register, not grace/goodness. | `UPDATE verse_context SET is_relevant=0, set_aside_reason='H7862 shay names tribute/homage to God expressing reverence and acknowledgment of supremacy — inner-being register is reverence/awe rather than grace or goodness; outside M39 characteristic scope' WHERE mti_term_id=2976 AND COALESCE(delete_flagged,0)=0` (3 rows). `mti_term_subgroup` placement remains in M39-BOUNDARY (the §15.2 set-aside exit pattern). |

After these three operations, BOUNDARY contains the set-aside H7862 only — the §13.6 exit gate is satisfied (every BOUNDARY term has an explicit exit recorded).

---

## Section 3 — Coverage gaps and authoring deviations to address

### G1: T5.7.2 not addressed in the consolidated findings

Phase 9 found 188 of 189 catalogue prompts addressed; T5.7.2 has no row for either sub-group. AI should either:

- Author rows for T5.7.2 [A], T5.7.2 [B] (and [CLUSTER] if applicable) and include INSERTs in dir-005's SCOPE, OR
- If the prompt genuinely doesn't apply, record `S — not applicable for this cluster` rows so the catalogue completeness rule is satisfied.

### G2: BOUNDARY characterisation under T1.2.1 — only 1 row, expected 3

Per v1_11 §11.6, every BOUNDARY term receives one structural characterisation note under T1.2.x. M39-BOUNDARY has 3 terms (G1435, H7862, H2868) but only 1 BOUNDARY-scope `cluster_finding` row was loaded.

- If H2868 te.ev is reassigned to M04 (Section 2 above), no characterisation is needed for it in M39 — drop from the expected count.
- After exit decisions, expected BOUNDARY rows = 2 (G1435 if it stays BOUNDARY pending decision, H7862). Under CC's recommended exit (G1435 → M39-A, H7862 set aside), expected BOUNDARY rows = **1** — already satisfied by the existing row. AI to confirm the existing row covers the right term.

---

## Section 4 — Feedback to AI (lessons from M39)

### F1: Schema query — `wa_dimension_index`, not `dimensions`

The Phase 9 gap-row query template referenced `dimensions` and `dimensions.obs_id`:

```sql
JOIN dimensions d ON d.obs_id = cf_m39.obs_id
```

Neither the table nor the join key exists. The actual schema:

- Table: `wa_dimension_index`
- Join key: `wa_dimension_index.verse_context_group_id` → `verse_context_group.id`
- Dimension is attached to **VCGs, not catalogue prompts (obs_ids)**.

Reach a VCG's dimensions via `verse_context_group_id`, then map to the current cluster via `verse_context → mti_terms.cluster_code`.

### F2: The C-code legacy in `wa_dimension_index`

`wa_dimension_index.cluster_assignment` still uses pre-2026-05-04 **C01–C22** codes. Zero rows for any M-cluster. Future analytical SQL that touches this table must either:

- Ignore `cluster_assignment` entirely and join via `verse_context_group_id` (the M39 fix above), OR
- Treat `cluster_assignment` as historical only — never join an M-code directly to it.

This legacy could be cleaned up in a future migration, but for now, the v1_11 §A1 appendix is the authority for which columns to use.

### F3: Schema-reference appendix exists — please consult

The cluster instruction v1_11 §A1 (Cluster-process tables — column reference) was added specifically to prevent the kind of analogy-by-name confusion that produced both the dir-002/003 schema errors (`verse_context_group.subgroup_code` instead of `group_code`) and the gap-resolution SQL with the fictional `dimensions.obs_id` join. The appendix lists the real columns for `cluster`, `cluster_subgroup`, `mti_term_subgroup`, `verse_context_group`, `vcg_term`, `verse_context`, and `cluster_finding`. Consult it when authoring SQL or directives that touch these tables.

`wa_dimension_index` is not currently in §A1. If dimensional sharing becomes a recurring Phase 9 question, suggest adding it (and the legacy-C-code caveat) to §A1 in a v1_12 minor bump.

### F4: BOUNDARY characterisation as one row per term

Per v1_11 §11.6, each BOUNDARY term receives its own structural characterisation row — not a consolidated single block. The M39 Phase 8 output produced a single `[BOUNDARY]` block; if AI's intent was per-term characterisations, the canonical syntax to use in future is one block per term:

```text
**[BOUNDARY — G1435 dōron]** {characterisation text}
**[BOUNDARY — H7862 shay]** {characterisation text}
```

This isn't currently in §11.8's marker catalogue. If the per-term BOUNDARY-block pattern is what AI intends going forward, suggest adding it to §11.8 in a v1_12 minor bump alongside the §A1 additions in F3.

### F5: Directive-as-package — dir-005 should bundle everything

Per v1_11 §2.5 / §13.7, dir-005 verification-corrections is a **single packaged directive** carrying:

1. Section 1 — 3 gap-row UPDATEs (T6.7.1 A/B + T6.7.3 CLUSTER)
2. Section 2 — 3 BOUNDARY exit operations (te.ev reassign, dōron promote, shay set-aside)
3. Section 3 — T5.7.2 coverage gap (INSERTs or S-rows)
4. Section 3 — BOUNDARY characterisation count reconciliation (no-op if the existing row covers the right term post-exit)
5. **Final operation: cluster.status `Analysis - In Progress` → `Analysis Completed`**

No standalone `dir-006-status-complete` — the status flip is the final operation of dir-005 (§13.9, anti-pattern §2.6).

---

## Section 5 — Pre-flight check CC will run before dir-005 apply

When dir-005 lands, CC's apply script will pre-check:

1. Every cited verse_record_id resolves to an `wa_verse_records` row.
2. Every cited `mti_term_id` is in M39 (or, for the te.ev reassign, currently in M39).
3. Every cited `cluster_subgroup_id` exists for cluster M39.
4. Every cited `obs_id` exists in `wa_obs_question_catalogue`.
5. The three target gap rows are currently at `finding_status='gap'`.
6. Pre-state backup of all rows that will be modified.
7. Single transaction; rollback on any failure.
8. Post-apply verification re-run via `scripts/_validate_cluster_completion_v1_*.py`.

---

## Appendix — supporting scripts

- Gap-row analytical query: archived to [scripts/archive/_tmp_m39_dim_sharing.py](../../scripts/archive/_tmp_m39_dim_sharing.py) (re-runnable for cross-check).
- BOUNDARY exit investigation: [outputs/markdown/m39-boundary-exit-investigation-v1-20260514.md](../../outputs/markdown/m39-boundary-exit-investigation-v1-20260514.md).

---

*WA-M39-phase10-input-pack-v1-20260514 — handoff to AI for dir-005 authoring.*
