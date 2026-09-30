# Rollback — piecemeal COMMENT_EVALUATION fragmentation (2026-06-03)

**What:** Rolled the DB back to the `pre_M06` snapshot, reverting the M06 (Hate), M08 (Pride) and
M46 (Abundance) pointer/finding dispositions. **Why:** they used a flawed *piecemeal cross-cluster
re-allocation* of individual pointers/findings, instead of the correct **term-centric, cluster-as-a-
whole** method (see memory `feedback_term_is_the_unit_of_movement`). M46 made it explicit — peace
*findings/pointers* were shipped to M33 (Peace) while the peace *terms* stayed in M46's sub-groups,
fragmenting a term from its findings.

## The correct model (researcher, 2026-06-03)
A pointer belongs to a term; a term has verses; a term lives in a cluster. **The term is the unit of
movement** — its verses, VCGs and findings move *with* it. A term moved after Tier 1–7 triggers
**reprocessing** of the receiving cluster. Work clusters as wholes. **Content and context lead.**

## Rollback executed
- Restored `C:\Users\lerouxc\db_recovery\bible_research_pre_M06_commenteval_20260603.db` → `database/bible_research.db`.
- Current-state safety snapshot kept: `bible_research_pre_rollback_errorstate_20260603.db`.
- Verified post-restore: integrity ok; FLAG live 539; M10c finding 55 + M10b finding 101 `set_aside` (kept); M06/M46 findings back to `pending`; observations 277/278/279 gone; `routed_cluster→M33` back to 21 (pre-existing).

## KEPT (sound, validated, within-cluster or infrastructure — NOT the error)
FLAG rescue · cluster_link schema+populate (D2 cleared) · orphan set-aside (30+72) · M10c (Defilement)
+ M10b (Wickedness) within-cluster closes · citation-extractor sweep. **The v3 audit
(`wa-programme-cluster-audit-v3-20260603.md`) was generated at exactly this pre-M06 state, so it
remains the accurate current snapshot** (M10c PASS; M06/M08/M46 still failing, correctly).

## REVERTED (the error)
M06 (Hate), M08 (Pride), M46 (Abundance) COMMENT_EVALUATION dispositions. Their disposition `.md`s
carry a ⛔ REVERTED banner; the M46 analysis (Abundance≠peace; M33 Peace owns the peace terms;
legacy-synthesis pattern is programme-wide) **stands and feeds the redo**.

## Redo approach (next)
Per cluster, examine **its terms** in context as a whole. A term whose content doesn't fit → move the
**term + verses + VCGs + findings** to the cluster its content fits; reprocess the receiver. A term
whose content genuinely spans clusters → represented in each, becoming findings at their analysis.
No more loose-pointer routing.
