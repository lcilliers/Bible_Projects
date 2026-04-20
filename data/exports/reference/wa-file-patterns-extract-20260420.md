# WA File-Name Pattern Registry — 2026-04-20

_Schema 3.13.0 · source: `wa_file_name_pattern`._

---

## Summary

**Patterns:** 23

By scope:

- `patch-id`: 1
- `per-batch`: 1
- `per-cluster`: 8
- `per-group`: 2
- `per-registry`: 8
- `programme`: 3

## Scope: `patch-id`

| Code | Pattern | Description | Governing |
|---|---|---|---|
| `patch_id` | `PATCH-{YYYYMMDD}-{NNN}-{TYPE}-V{n}` | Patch identifier (uppercase, inside _patch_meta.patch_id) | wa-reference [current] §1.5 |

## Scope: `per-batch`

| Code | Pattern | Description | Governing |
|---|---|---|---|
| `vcb_file` | `wa-vcb-{NNN}-{type}-v{n}-{YYYYMMDD}.{ext}` | Verse Context Batch files | wa-reference [current] §1.2 |

## Scope: `per-cluster`

| Code | Pattern | Description | Governing |
|---|---|---|---|
| `dim_cc_directive` | `wa-dim-{cluster}-cc-directive-{YYYYMMDD}.md` | CC directive document (DimReview) | wa-dimensionreview-instruction [current] §15 |
| `dim_cluster_extract` | `wa-dim-{cluster}-extract-{YYYYMMDD}.json` | Dimension Review cluster extract | wa-dimensionreview-instruction [current] §15 |
| `dim_existing_pointers` | `wa-dim-{cluster}-existing-pointers-{YYYYMMDD}.json` | Existing SB findings + SD pointers | wa-dimensionreview-instruction [current] §15 |
| `dim_grpdesc_patch` | `wa-dim-{cluster}-grpdesc-patch-v{n}-{YYYYMMDD}.json` | DimReview group-description correction patch | wa-dimensionreview-instruction [current] §15 |
| `dim_handoff_kickoff` | `wa-dim-{cluster}-handoff-kickoff-v{n}-{YYYYMMDD}.md` | DimReview handoff kickoff (build_dimension_extract --bundle) | wa-dimensionreview-instruction [current] §15; build_dimension_extract.py |
| `dim_observations` | `wa-dim-{cluster}-observations-v{n}-{YYYYMMDD}.md` | DimReview observations log | wa-dimensionreview-instruction [current] §15 |
| `dim_rootfamily` | `wa-dim-{cluster}-rootfamily-{YYYYMMDD}.json` | Dimension Review root-family | wa-dimensionreview-instruction [current] §15 |
| `dim_session_log` | `wa-dim-{cluster}-session-log-v{n}-{YYYYMMDD}.md` | DimReview session log | wa-dimensionreview-instruction [current] §15 |

## Scope: `per-group`

| Code | Pattern | Description | Governing |
|---|---|---|---|
| `dim_grpverify` | `wa-dim-{cluster}-grpverify-{group_code}-{YYYYMMDD}.json` | Group verification extract | wa-dimensionreview-instruction [current] §15 |
| `dim_vpass` | `wa-dim-{cluster}-vpass-{group_code}-{YYYYMMDD}.json` | Verification pass extract | wa-dimensionreview-instruction [current] §15 |

## Scope: `per-registry`

| Code | Pattern | Description | Governing |
|---|---|---|---|
| `dim_reg_patch` | `wa-dim-{cluster}-reg{nnn}-patch-v{n}-{YYYYMMDD}.json` | DimReview per-registry patch | wa-dimensionreview-instruction [current] §15 |
| `dim_return` | `wa-dim-{cluster}-{registry_no}-return-v{n}-{YYYYMMDD}.md` | DimReview return document | wa-dimensionreview-instruction [current] §15 |
| `final_registry_extract` | `wa-{NNN}-{word}-final-v{n}-{YYYYMMDD}.json` | Final registry extract | wa-reference [current] §14.1 |
| `patch_filename` | `wa-{NNN}-{word}-{type}-patch-v{n}-{YYYYMMDD}.json` | Patch file on disk (lowercase wa- prefix) | wa-reference [current] §1.5 |
| `sdpointers_file` | `wa-{NNN}-{word}-sdpointers-{YYYYMMDD}.json` | Session D pointers export | wa-reference [current] §14.2 |
| `sessiona_md` | `wa-{NNN}-{word}-sessiona-{YYYYMMDD}.md` | Session A extract markdown | Session A advice v1 |
| `sessiona_patch` | `wa-{NNN}-{word}-sessiona-patch-{YYYYMMDD}.json` | Session A PROSE patch | Session A advice v1 |
| `word_level` | `wa-{NNN}-{word}-{type}-v{n}-{YYYYMMDD}.{ext}` | Word-level Session B/C/D outputs | wa-reference [current] §1.1 |

## Scope: `programme`

| Code | Pattern | Description | Governing |
|---|---|---|---|
| `instruction_doc` | `wa-{instruction-name}-v{n}-{YYYYMMDD}.{ext}` | Instruction documents | wa-reference [current] §1.4 |
| `programme_level` | `wa-global-{type}-v{n}-{YYYYMMDD}.{ext}` | Programme-level files | wa-reference [current] §1.3 |
| `reference_snapshot` | `wa-reference-snapshot-{YYYYMMDD}.json` | Reference-as-DB session-start snapshot (M32+) | reference-as-database-design-20260420 |

---
*Generated 2026-04-20T16:45:01Z.*