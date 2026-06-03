# Cluster Instruction Streamlining Audit — v1_7 → v1_8 proposed

**Date:** 2026-05-14
**Source:** [Workflow/Instructions/wa-sessionb-cluster-instruction-v1_7-20260513.md](../../Workflow/Instructions/wa-sessionb-cluster-instruction-v1_7-20260513.md)
**Scope:** non-semantic cleanups for consistency + de-duplication. No rule meaning changes.

---

## Findings — applied in v1_8

| # | Issue | Change | Rationale |
|---|---|---|---|
| A | Frontmatter carries 6 full-paragraph change notes (v1_2→v1_7), each duplicated verbatim in §19 Change history. ~5,000 chars of duplication; header is dominated by historical noise rather than current status. | Keep only the most recent change note (v1_6→v1_7) in the frontmatter. Full history lives in §19. Frontmatter adds a "See §19 for full change history" pointer. | Header should communicate current status, not history. |
| B | §5 numbering gap: §5.1 then jumps to §5.4. No §5.2 or §5.3 — artefact of v1_6 reorganisation. | Renumber §5.4 → §5.2 (the only sub-section after §5.1). | Numbering consistency. |
| C | §5.1 heading reads `### 5.1 DB writes — VCNEW patch (corrected v1_6)`. The "(corrected v1_6)" annotation is historical metadata that belongs in §19, not in a section heading. | Drop the parenthetical. | Section headings should describe current content, not edit history. |
| D | §17 pre/post controls row 4 (Phase 4) omits the cluster status transition `Data - In Progress → Analysis - In Progress` defined in §7.7. | Add to row 4 post-check: "`cluster.status='Analysis - In Progress'`". | §17 is the consolidated check table — must reflect §7.7. |
| E | §17 row 7 (Phase 7) omits the `vcg_term` backfill check defined in §10.4 (added in v1_7). | Add to row 7 post-check: "vcg_term backfill check: every NEW VCG has ≥1 vcg_term row per mti_term_id with verses in it". | §17 must reflect v1_7's new requirement. |
| F | §11.6 hard-codes "Record under T1.2.1" for BOUNDARY structural characterisations. If the catalogue version renames or renumbers T1.2.1, the instruction silently breaks. | Soften to "the T1.2.x structural-role prompt (currently T1.2.1)". | Catalogue is independently versioned — instruction shouldn't pin to a specific prompt code. |
| G | §7.4 introduces `OQ-NNN` markers in Phase 4 without defining the abbreviation. | Add a one-line definition on first use: "(OQ-NNN = Open Question NNN — a question that cannot be resolved by reading alone)". | Defined-on-first-use discipline. |

---

## Findings — flagged, resolved in v1_9 (researcher direction, 2026-05-14)

Researcher confirmed all three flagged items with broader principle: **package directives, automate status transitions, AI prepares for compliance; CC processes in succession.** Applied in v1_9:

| # | Issue | Resolution in v1_9 |
|---|---|---|
| H | §7.7 status-transition discipline | Rewritten as one packaged subgroup-assign directive carrying Operations A (sub-group create + assign), B (cluster_code rebind if needed), C (status `Data - In Progress` → `Analysis - In Progress`). Same principle applied to Phase 10 closure (§13.9): `Analysis Completed` transition is an operation within the verification-corrections directive, not a standalone directive. New §2.5 (Directive packaging discipline) + §2.6 (Status transition discipline) establish the principle programme-wide. M20's separate `dir-004-status-bump` and `dir-010-status-complete` are now anti-patterns. |
| I | §9.5 letter collision (§A–§E vs Pass A/B/C) | Renamed §A–§E → §1–§5. Cross-refs in §10.2, §17 updated. |
| J | Phase 7 directive segmentation ambiguity | Replaced with explicit segmentation discipline (§10.3 new): Phase 7 begins with a data-volume **pre-assessment written to the obslog** declaring the processing segments (cluster-wide / per-sub-group / combined / within-sub-group). AI writes a **segment-close summary to the obslog at the end of each segment** before the next begins. The `{seq}` ambiguity is dissolved — the filename pattern is now `dir-{seq}-{segment-tag}-mapping` where segment-tag identifies the segment (sub-group code, combined code like `AB`, or split-tag like `D-split1`) and {seq} is the cluster-wide directive number. |

---

## Non-issues (verified consistent)

- §1 ↔ §11.1 ↔ §14: tier catalogue path reference is identical (`Workflow/Tiers/wa-obs-catalogue-tiered-v{N}-{date}.md`).
- §11.1 ↔ §11.2 ↔ §14: science-extract requirement (mandatory input for Phase 8) is consistently stated.
- §6.1 T1 framework and §6.2 onion-principle wording: stable across phases.
- §15 BOUNDARY lifecycle table matches §13.6 closure exit options.

---

## M39 input readiness check (incidental — produced during audit)

| Asset | Path | Size | Status |
|---|---|---|---|
| Cluster row | `cluster.M39` | — | `Data - In Progress` (transition fired 2026-05-14T03:08:12Z, backup taken) |
| Comprehensive report | `Sessions/Session_Clusters/M39/wa-cluster-M39-comprehensive-v1-20260514.md` | 1.3 MB | Fresh |
| Detail report (latest) | `Sessions/Session_Clusters/M39/wa-cluster-M39-detail-v4-20260508.md` | 6 KB | From 2026-05-08 — may need re-gen if the cluster has changed since |
| Science extract | `Workflow/Sciences/wa-m39-blessing-scienceextract-v1_0-20260513.md` | 9 KB | Present |
| Cluster name | — | — | "Blessing, Favour and Grace" (short_name: "Blessing") |
| Active terms | — | — | 16 mti_terms (39 inc. delete-flagged — script filters) |
| Sub-groups | — | — | 0 — Phase 3/4 will define |

**Ready for AI Phase 1.**
