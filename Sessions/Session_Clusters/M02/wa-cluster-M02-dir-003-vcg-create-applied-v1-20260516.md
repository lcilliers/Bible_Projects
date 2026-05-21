# WA-M02-dir-003-vcg-create-applied-v1-20260516

**Phase 7 (v2_2):** VCG creation, routing, anchor designation
**Apply timestamp:** 2026-05-16T13:06:18Z
**Loader:** [scripts/_apply_m02_phase7_vcg_creation_20260516.py](../../../scripts/_apply_m02_phase7_vcg_creation_20260516.py)
**Directive:** [wa-cluster-M02-dir-003-vcg-create-v1-20260516.md](wa-cluster-M02-dir-003-vcg-create-v1-20260516.md)
**Governing instruction:** wa-sessionb-cluster-instruction-v2_2-20260516 §10

---

## Outcome

**26 new VCGs created · 71 vcg_term links · 641 verses routed · 53 anchors total (26 AI + 27 provisional) · 15 dual-membership notes · 5 phantom vc_ids dropped · 0 set-asides.** Single transaction. All health checks pass.

## Per-sub-group VCG distribution

| Sub-group | VCGs | Verses | AI anchors | Term placements |
|---|---:|---:|---:|---:|
| M02-A Divine Wrath as Judicial Force | 5 | 110 | 5 | 9 |
| M02-B Burning Rage and Inner Heat | 7 | 252 | 7 | 22 |
| M02-C Indignation and Moral Displeasure | 3 | 38 | 3 | 8 |
| M02-D Provocation — Anger Aroused | 4 | 60 | 4 | 6 |
| M02-E Jealousy, Zeal and Possessive Passion | 4 | 77 | 4 | 6 |
| M02-F Strife, Quarrel and Contentious Anger | 2 | 16 | 2 | 8 |
| M02-BOUNDARY | 1 | 82 | 1 | 12 |
| **Total** | **26** | **641** | **26** | **71** |

(Cumulative verse counts include dual-memberships at primary routing; the 15 dual-membership cases are recorded in `verse_context.notes`.)

## Anchor breakdown

- **26 AI-designated VCG anchors** — one per VCG.
- **27 provisional per-term anchors** — for each term whose verses route to a VCG not anchored by one of its own verses, the term's first canonical-order is_relevant verse is promoted to is_anchor=1. CC enforces this at apply time (R4 rule).
- **53 total anchors.**

## Phantom vc_id filtering

| vc_id | Cause |
|---|---|
| 64718 | mti=136 is_relevant=0 (set-aside, AI mis-routed) |
| 64660 | mti=136 is_relevant=0 (set-aside) |
| 285 | mti=79 is_relevant=0 (set-aside) |
| 356 | Does not exist in verse_context |
| 399 | Does not exist in verse_context |

These were dropped before processing; no DB write attempted.

## Missing-verse remediation

39 vc_ids were missing from AI's main JSON pass (37 in M02-B, 2 in M02-A). Claude API atomic per-row classification assigned all 39 to existing VCGs (no NEW-NEEDED). See [WA-M02-vcg-missing-verse-assignments-v1-20260516.json](WA-M02-vcg-missing-verse-assignments-v1-20260516.json).

## Cross-routing flags (recorded, no DB action)

AI flagged 5 verses with cross-routing observations (kept in primary sub-group, noted in flags doc):

- vc=95 Mar 3:5 (M02-A) — grief-pairing aligns with M02-C; retained in M02-A-VCG-04
- vc=64926 Ecc 5:17 (M02-A) — atypical for qe.tseph (chronic inner state, not judicial); retained in M02-A-VCG-03
- vc=64773 Neh 4:7 (M02-B) — primary content is hostility (M06 territory); retained in M02-B-VCG-02
- vc=64787 Isa 45:24 (M02-B) — enemy rage against God + shame consequence; retained
- vc=862, 865 (1Sa 1:6, 1Sa 1:7, M02-D) — Hannah's evidenced state is grief (M03); retained because the term's role (provocation) is M02

## Set-asides

**0 set-asides.** Per AI's cross-routing flags §2 — no divine-inner-state set-aside candidates met the M01 strict criterion (private inner emotional experience as divine inner life event). All divine-wrath verses describe the characteristic in operation and are in scope.

## Health checks (post-apply)

| Code | Check | Expected | Actual | Status |
|---|---|---|---|---|
| H2 | is_relevant verses without group_id | 0 | 0 | ✓ |
| H3 | vc mti not in vcg term set | 0 | 0 | ✓ |
| R4 | terms with relevant verses but no anchor | 0 | 0 | ✓ |

## State summary

| Item | Value |
|---|---|
| `cluster.status` | `Analysis - In Progress` (unchanged) |
| Active terms in M02 | 43 |
| Active sub-groups | 7 |
| **New VCGs (Phase 7)** | **26** |
| **Inherited VCGs (still in DB, to be dissolved Phase 8)** | **73** |
| Active is_relevant verses | 641 |
| Routed verses | 641 |
| Anchors total | 53 |
| Set-asides total in M02 | 56 (pre-existing; no Phase 7 additions) |

## Notes for follow-up

1. **27 provisional anchors set by CC** — first canonical verse per anchorless term. Analytically defensible per v2_2 §4.4 R4 fallback. Researcher may revisit at Phase 12 to choose more representative anchor verses.

2. **15 dual-membership rows** — primary VCG set; secondary recorded in `verse_context.notes`. If schema later supports m:n verse-to-VCG, these can be expanded.

3. **99 VCGs touching M02** — 26 new + 73 inherited. Phase 8 dissolution comparison report will identify inherited VCGs for researcher-reviewed soft-delete.

## Tables modified

| Table | Operation | Rows |
|---|---|---:|
| `verse_context_group` | INSERT | 26 |
| `vcg_term` | INSERT | 71 |
| `verse_context` | UPDATE `group_id`, `notes`, `is_anchor` | 641 group + 26 + 27 anchor sets + 71 anchor resets |

## Tables not touched

| Table | Reason |
|---|---|
| `cluster.status` | Mid-flow — Phase 12 owns closure |
| Inherited `verse_context_group` rows | Phase 8 dissolves them with researcher gate |
| `cluster_subgroup` | Phase 6 work |
| `mti_term_subgroup` | Phase 6 work |

## Provenance

- AI design: [WA-M02-vcg-creation-v1-20260516.json](WA-M02-vcg-creation-v1-20260516.json) + 6 per-sub-group design docs
- AI cross-routing flags: [WA-M02-phase7-cross-routing-flags-v1-20260516.md](WA-M02-phase7-cross-routing-flags-v1-20260516.md)
- CC missing-verse assignment: [WA-M02-vcg-missing-verse-assignments-v1-20260516.json](WA-M02-vcg-missing-verse-assignments-v1-20260516.json)
- Apply script: [scripts/_apply_m02_phase7_vcg_creation_20260516.py](../../../scripts/_apply_m02_phase7_vcg_creation_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_*_DIR-20260516-010.db`

---

## Next step — Phase 8 (VCG dissolution comparison report)

CC generates the researcher-facing comparison report (post-hoc snapshot reconstruction from the pre-Phase-7 backup as done for M01), then applies dissolution after researcher approval.

*End of applied report.*
