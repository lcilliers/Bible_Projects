# Session log 2026-11-07: multi-term units in verse_lexical, the surface group entity, the #2379 exports

Session id: 8e72859c-b408-45e1-bd42-35d4522bb098 (Developer Mode from 2026-11-07T05:29Z, exited before this close; the close ran in standard mode)

## 1. Scope

Developer Mode declaration and compliance file; the open escalations ordered for Developer Mode work; #2372 (the surface group `entity` in config and data); #2381 (multi-term units in `verse_lexical` and in the analysis: design v2, build stages 1 to 4, back-fill of 544,667 rows); #2379 (both CSV exports rebuilt on the corrected data); #2386 (my own refused Prose call, closed); session close.

## 2. Escalations

- #2378, #2363, #2380: closed by the researcher (approved; #2363 option a; #2380 options B and C); read at v3 each, no change by me.
- #2372: researcher decision (entity throughout) applied, verified, handed over (v3); approved by the researcher and completed (v4).
- #2381: moved to in-progress, design v1 then v2 written, handed over (v4), approved in chat, built (v5, v6); approved by the researcher (v7); follow-up flag cleared and completed (v8).
- #2387 raised (task, on hold, with the researcher): the points left after the #2381 build.
- #2380: its analysis (outputs/escalation/2380-affix-surface-analysis-v1-20261107.md) is the input of #2381; no change by me this session.
- #2379: updated v9 to v11: the two exports rebuilt; the researcher's messages recorded verbatim; remains with me.
- #2386: raised by my own refused `Prose.ps1 -Step FlagFixPropose` call; resolved (self_correctable), completed (v2).
- #2357: a new finding group (15 draft glossary findings of #2374) was recorded on it by `configmaint.validate`; no action by me.

## 3. Files

- iba/app/lib/lexical.py (is_affix, affix_role, apply_unit_fields, unit_view, unit columns in the write)
- iba/app/lib/reading.py (sheet groups per unit); iba/app/lib/observationrecord.py (occurrence_surfaces reads the columns); iba/app/lib/versescope.py (word selector excludes gloss rows)
- iba/app/lib/surfacegroup.py and iba/app/ps/Surface-Group.ps1 (comments: entity)
- iba/app/BUILD.md (sections 468 and 469); iba/app/USER-GUIDE.md (8.8 note, reading section, new 8.16)
- iba/app/migration/archive/surface_group_entity_2372_v1_20261107.py; iba/app/migration/archive/verse_lexical_units_2381_v1_20261107.py; iba/app/migration/archive/verse_lexical_units_backfill_2381_v1_20261107.py
- iba/app/tools/temp_2381_units_test_run.py (new); iba/app/tools/temp_2326_surface_migration_test_run.py (applies the stage 1 migration to its snapshot; B1 reworded)
- archive/patches/wa-prose-glossary-surface-group-entity-v1-20261107.json (applied: glossary entry 1131, draft, in database/bible_research.db)
- outputs/escalation/2372-group-before-image-v1-20261107.csv; outputs/escalation/2381-verse-lexical-surface-fix-design-v2-20261107.md; outputs/escalation/2381-surface-backfill-follow-v1-20261107.tsv; outputs/escalation/open-escalations-developer-mode-order-v1-20261107.md; outputs/escalation/2379-behaviour-and-inner-state-surfaces-v3-20261107.csv; outputs/escalation/2379-surface-collections-members-verses-v4-20261107.csv
- Moved to archive: outputs/escalation/archive/2381-verse-lexical-surface-fix-design-v1-20261107.md and the superseded 2379 CSV versions
- Database iba/app/db/iba.db (not in git): verse_lexical (544,667 rows), surface_term, ai_call, surface_event, cfg_* rows; rollback snapshot backups/iba-pre-2381-unit-columns-20261107.db
- Logs/compliance/COMPLIANCE-20261107-8e72859c.md; generated reports (config report, escalation list and histories, session-close report)

## 4. Decisions

- Researcher: use `entity` throughout, in configs and data; recorded in #2372 v3 and iba/app/BUILD.md section 468.
- Researcher: #2380 options B and C (own gloss for affix codes; the compound clear in `verse_lexical`; avoid the consumer filter); recorded in #2381 v3 and outputs/escalation/2381-verse-lexical-surface-fix-design-v2-20261107.md.
- Researcher: D1 to D5 are mine to decide, the sub-gloss must not be confused with the multi-term meaning and the multi-term meaning must stay visible; recorded in #2379 v11 and #2381 v4.
- Researcher: design v2 approved, build; recorded in #2381 v5.
- Researcher: rebuild the #2379 exports; recorded in #2379 v9 and #2379 v10.
- Researcher: refine the collections next, close the session in standard mode; recorded in #2379 v11.
- Claude, self-correctable: the wrong flag code passed to Prose.ps1; recorded in #2386 v2.
- Claude, self-correctable: the first members-file query missed the member-term route and wrote duplicates; recorded in #2379 v10.

## 5. Open items

- Left after the units build, for the researcher (#2387): the reports and the two reading generators still print one entry per code; the three held M-coded rows (Dan 7:19 H3321, Acts 16:29 G1790, Job 30:24 H7769) to release or keep; the 16,262 `shared` rows (units of several content codes, word not decided).
- Refining the collections, and review of the rebuilt #2379 exports: carried on #2379.
- #2376 (Rebuild narrative), #2377 (Assemble narration chapter scope), #2368 (whole-cluster reading rules), #2366 (judge cycle port), #2357 (config advisory findings): unchanged, with the researcher.

## 6. Git

(written after the first commit)
