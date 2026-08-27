# WA-M02-dir-004-vcg-dissolve-applied-v1-20260516

**Phase 8 (v2_2):** Inherited VCG dissolution
**Apply timestamp:** 2026-05-16T14:31:48Z
**Loader:** [scripts/_apply_m02_phase8_vcg_dissolve_20260516.py](../../../scripts/_apply_m02_phase8_vcg_dissolve_20260516.py)
**Directive:** [wa-cluster-M02-dir-004-vcg-dissolve-v1-20260516.md](wa-cluster-M02-dir-004-vcg-dissolve-v1-20260516.md)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_2-20260516 §11
**Trust basis:** [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md) — M01 validation transferred to M02

---

## Outcome

**68 inherited VCGs soft-deleted + 68 vcg_term links soft-deleted.** Single transaction. All meaningful health checks pass.

| Op | Rows |
|---|---:|
| A — `vcg_term` soft-delete | 68 |
| B — `verse_context_group` soft-delete | 68 |
| **Total** | **136** |

## Post-dissolution state

| Item | Value |
|---|---|
| `cluster.status M02` | `Analysis - In Progress` (unchanged) |
| Active M02 VCGs (reachable via vcg_term) | **25** (Phase 7 new VCGs) |
| Active M02 VCG rows (incl. empty M02-D-VCG-04) | 26 |
| Soft-deleted M02 VCGs | 68 (this directive) |
| Active vcg_term rows | 71 |
| Soft-deleted vcg_term rows | 68 (this directive) |
| Active is_relevant verses | 641 (unchanged) |

## Health checks (post-apply)

| Code | Check | Result |
|---|---|---|
| D1 | Active vcg_term pointing to dissolved VCGs | 0 ✓ |
| D2 | Active inherited M02 VCGs (id < 3762) | 0 ✓ |
| D3 | Active is_relevant vc with group_id NULL | 0 ✓ |
| D4 | Active is_relevant vc pointing to delete_flagged VCG | 0 ✓ |
| D5 | Active M02 VCGs reachable via vcg_term | 25 (expected ~26; the 1 missing is the empty M02-D-VCG-04 — see directive §5 note) |

The script's strict D5 assertion failed (expected exactly 26) but the underlying data is correct. The dissolution transaction committed successfully **before** the post-commit healthcheck assertion fired. The empty M02-D-VCG-04 is a known artefact from Phase 7 dual-membership precedence; it's a dangling row with 0 verses and 0 vcg_term links. Researcher may decide at Phase 12 to soft-delete it or leave it as a documented edge case.

## Audit trail

Each dissolved VCG carries the directive id in its `notes` field:

```
| DIR-20260516-011 dissolved (superseded by DIR-20260516-010 new VCGs)
```

## Trust transfer from M01 — recorded reasoning

Per researcher direction (2026-05-16):

> "this is an important validation test, and I thick we should record it in full, the reasoning behind it, the methods of test, the test outcomes and the conclusion - can you write that all out and save it in workflow/methodology. Then you can proceed to dissolve M02, and we do not have to perform the dissolution comparison again."

The M01 blind verification (three tests, 272 findings, recorded in detail at [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)) established:

- 0 empty pick lists across all findings (no fabrication signal)
- 90.6% target precision on the stress test (full M01 corpus distractors)
- 64% pure-target findings (100% picks in M01-A target)
- 0.1% true hallucination rate (2 non-existent vc_ids out of 1,828)

M02 used the same AI (Sonnet 4.6), same prompts, same v2_2 methodology, and produced structurally clean Phase 7 output (R4=0, H2=0, H3=0). The dissolution comparison report normally produced at Phase 8 (M01 had it at [Sessions/Session_Clusters/M01/WA-M01-vcg-dissolution-comparison-v2-20260516.md](../../M01/WA-M01-vcg-dissolution-comparison-v2-20260516.md)) is skipped for M02 per this trust transfer.

The M02 inherited VCG preservation archive ([WA-M02-inherited-vcg-archive-v1-20260516.md](WA-M02-inherited-vcg-archive-v1-20260516.md)) was generated **before** dissolution and provides the durable human-readable record of every dissolved VCG's full content.

## Provenance

- Phase 7 applied: [WA-M02-dir-003-vcg-create-applied-v1-20260516.md](WA-M02-dir-003-vcg-create-applied-v1-20260516.md)
- Inherited VCG archive (durable record): [WA-M02-inherited-vcg-archive-v1-20260516.md](WA-M02-inherited-vcg-archive-v1-20260516.md)
- Analytical lens (3-view comparison): [WA-M02-vcg-analytical-lens-v1-20260516.md](WA-M02-vcg-analytical-lens-v1-20260516.md)
- M01 blind verification methodology (trust basis): [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)
- Apply script: [scripts/_apply_m02_phase8_vcg_dissolve_20260516.py](../../../scripts/_apply_m02_phase8_vcg_dissolve_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_20260516_143147_DIR-20260516-011.db`

---

## Next step — Phase 9 (catalogue prompts)

The 25-VCG (+1 empty) M02 structure is now the cluster's sole active phenomenology. Phase 9 next: prepare AI-facing brief + grouped report for catalogue-prompt findings authoring against the 189 T0–T7 prompts.

*End of applied report.*
