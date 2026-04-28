# WA Label Pattern Registry — 2026-04-20

_Schema 3.13.0 · source: `wa_label_pattern`._

---

**Patterns:** 11

| Code | Pattern | Entity / Column | Description | Governing |
|---|---|---|---|---|
| `dim_finding` | `DIM-{registry_no}-{3-digit-sequence}` | wa_session_b_findings.finding_id | Dimension Review Session B finding — e.g. DIM-112-004 | wa-dimensionreview-instruction [current] §7.5 |
| `dim_sd_pointer` | `DIM-{registry_no}-SD{3-digit-sequence}` | wa_session_research_flags.flag_label | Dimension Review Session D pointer — e.g. DIM-112-SD003 | wa-dimensionreview-instruction [current] §7.5 |
| `directive_id` | `DIR-{YYYYMMDD}-{3-digit-sequence}` | directive identifier | Directive ID — e.g. DIR-20260420-001 | wa-directive-instruction [current] |
| `flag_id_legacy` | `FLAG-{3-digit-sequence}` | wa-global-flags flag identifier | Programme-wide flag — e.g. FLAG-010 / FLAG-016 | wa-global-flags [current] |
| `group_code` | `{mti_term_id}-{3-digit-serial}` | verse_context_group.group_code | Verse context group code — e.g. 730-001 | wa-reference [current] §13.11 |
| `patch_id` | `PATCH-{YYYYMMDD}-{NNN}-{TYPE}-V{n}` | patch identifier | Patch ID (uppercase, in _patch_meta.patch_id) | wa-reference [current] §1.5 |
| `ph2_finding` | `PH2-{registry_no}-{3-digit-sequence}` | wa_session_research_flags.flag_label | Phase 2 research flag — e.g. PH2-112-001 | wa-reference [current] §5.4 |
| `q_cov_catalogue` | `Q-COV-{2-digit-sequence}` | wa_obs_question_catalogue.question_code | Evidence-flag-routing catalogue question — Q-COV-01..12 | wa-reference [current] §8b |
| `sb_finding_legacy` | `{registry_no}-F{3-digit-sequence}` | wa_session_b_findings.finding_id | Pre-DIM prefix format (legacy; reconciliation pending) | historical convention |
| `sd_pointer_legacy` | `{registry_no}-SD{3-digit-sequence}` | wa_session_research_flags.flag_label | Pre-DIM prefix format (legacy; reconciliation pending) | historical convention |
| `verse_context_batch` | `VCB-{3-digit-sequence}` | verse-context batch identifier | Verse Context Batch id — e.g. VCB-003 | wa-versecontext-instruction [current] |

---
*Generated 2026-04-20T16:45:02Z.*