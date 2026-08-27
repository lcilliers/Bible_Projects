# Schema Gap Register — Session B v5.0 Design
## wa-global-sessionb-schema-gaps-v1_2-20260415.md
**Date:** 2026-04-15
**Status:** Active — G-7 and G-8 resolved by researcher decision 2026-04-15
**Supersedes:** wa-global-sessionb-schema-gaps-v1_1-20260415.md

---

## Change note v1.2 (20260415)

G-7 and G-8 resolved by researcher decision. Session C feedback path confirmed. FLAG-009 raised to ensure Session C instruction mirrors this design when drafted.

---

## Gap Register

| # | Gap | Severity | Table | Resolution | Status |
|---|-----|----------|-------|------------|--------|
| G-1 | No attribution fields on `verse_context` (`classified_by_instruction`, `classified_date`) | Low | OT-1 | CC directive needed | **Open** — does not block Session B v5.0 |
| G-2 | No attribution field on `verse_context_group` (`classified_by_instruction`) | Low | OT-2 | CC directive needed | **Open** — does not block Session B v5.0 |
| G-3 | No instruction version field on `wa_dimension_index` (`dim_review_instruction`) | Low | OT-3 | CC directive needed | **Open** — does not block Session B v5.0 |
| G-4 | `wa_session_b_findings` missing 9 lifecycle fields | High | OT-4, OT-8 | Resolved via DIR-20260415-004 | **Resolved** |
| G-5 | No entity-level linkage table (`wa_finding_entity_links`) | High | OT-4 | Resolved via DIR-20260415-005 | **Resolved** |
| G-6 | `finding_type` naming inconsistency (mixed case) | Medium | OT-4 | Resolved via DIR-20260415-006 | **Resolved** |
| G-7 | Verse annotations have no confirmed database home | Medium | OT-5 | **Resolved by researcher decision 2026-04-15.** Verse annotations are stored as `finding_type = VERSE_ANNOTATION` in `wa_session_b_findings`. Session C reads VERSE_ANNOTATION findings together with anchor verse records from `verse_context` to generate the verse prose section. No additional schema change needed. Session C feedback path confirmed — new insights or unanswered questions arising during Session C verse prose generation are raised as SESSION_C_CORRECTION or OPEN_ITEM findings, written back to `wa_session_b_findings` before the prose that depends on them is finalised. See FLAG-009 for Session C instruction update requirement. | **Resolved** |
| G-8 | `VERSE_ANNOTATION_COMPLETE` flag has no database implementation | Low | OT-5 | **Resolved by researcher decision 2026-04-15.** Completion is verified by count match at Closure Checklist Domain B: count of VERSE_ANNOTATION findings must equal count of anchor verses. No separate flag needed. | **Resolved** |
| G-9 | `flag_code` naming duplication (VOLUME_LIMITATION variants) | Low | OT-6/7 | Resolved via DIR-20260415-003 | **Resolved** |
| G-10 | `strongs_reference` multi-value entries in `wa_session_research_flags` (7 rows) | Low | OT-6/7 | Split at query time — no schema change needed | **Deferred — low impact** |
| G-11 | `session_raised` format inconsistency in `wa_session_research_flags` | Low | OT-6/7 | Enforce standard format going forward — existing rows are historical | **Deferred — historical data** |
| G-12 | No FK from resolved pointer to resolving finding | Low | OT-6 | Deferred to Session D instruction design | **Deferred** |
| G-13 | Root family records missing for ~22% of root-coded terms | Medium | OT-4 (root) | CC directive needed before root entity links are activated in Session B | **Open — directive needed before root-level entity links are used** |
| G-14 | No `resolution_note` field on `wa_session_b_findings` | High | OT-4 | Resolved via DIR-20260415-004 | **Resolved** |

---

## Gaps blocking Session B v5.0 execution

**None.** All high and medium severity gaps are resolved. Remaining open gaps (G-1, G-2, G-3, G-13) are low severity or require a directive before a specific sub-feature activates. None prevent Session B from running.

**G-13 note:** Root entity links in `wa_finding_entity_links` use `entity_type = root_family` pointing to `wa_term_root_family.id`. Where a root family record does not exist, the entity link cannot be created. Session B notes root family gaps in the observations log and raises them for CC resolution before the entity link write at pass close.
