# Prose Store — Architecture and Stages of Development

**SUPERSEDED 2026-08-24 — escalation #829, build step §8.1
(`iba/docs/prose-management-iba-first-layer-proposal-v9-20260824.md`).** This document described
how the programme's prose lived in the database as of 2026-04-23. That description is no longer the
canonical source — the app now operates on config, not this Markdown file. Everything this document
used to state informally is now a live, queryable `cfg_*` row, plus two `GOVERNANCE.md` sections
recording how it was built:

| What this doc used to describe | Where it lives now |
|---|---|
| Schema — table/column meanings | `cfg_table`/`cfg_column` (live, `bible_research.db`) |
| `status`/`author`/`source_stage`/`lifecycle_tag`/`book_label` vocabularies | `cfg_enum` groups `prose_section_status`/`prose_section_author`/`prose_section_type_source_stage`/`prose_section_type_lifecycle_tag`/`prose_section_type_book_label` |
| Status transitions (draft → in_review → approved → archived) | `cfg_status_flow`, `entity='prose_section'` |
| The `session_a_replace` author gate, the two-patch ordering rule | `cfg_behaviour_rule`, `class='sqlite'` |
| Tool settings (`chapter_names`, `book_stage_map`, `search_default_limit`, `edit_file_dir`) | `cfg_prose` (module table) |
| Write authorisation | `cfg_write_grant` |
| Versioning / supersede mechanics (this doc's §6 described the OLD insert-a-new-row model) | **Rebuilt onto Model A** (system-versioned temporal tables) + `record_change_log` — `GOVERNANCE.md` §52, escalation #836 |
| Dispatcher registration, CLI usage (`Prose.ps1`) | `GOVERNANCE.md` §53 / `USER-GUIDE.md` §13d, escalation #829 |
| The quality-flag mechanism (`prose.flag`) | `GOVERNANCE.md` §53.5, `USER-GUIDE.md` §13d, escalation #829 §12 |

**Full design record for how the current state was reached:**
`iba/docs/prose-management-iba-first-layer-proposal-v1` through `-v9-20260824.md` (the consolidated,
self-contained final version is v9); `iba/docs/prose-change-log-design-v1` through `-v9-20260824.md`
and `iba/docs/prose-change-log-proposal-v1` through `-v3-20260824.md` (the versioning rebuild,
escalation #836).

---

## References (historical design rationale — not operative, kept for provenance)

| Doc | Purpose |
|---|---|
| [wa-prose-store-design-v1-20260419.md](../research/investigations/wa-prose-store-design-v1-20260419.md) | Full design workings, schema rationale, round-trip tooling design. |
| [prose-in-sqlite-advice-v1-20260419.md](../research/investigations/prose-in-sqlite-advice-v1-20260419.md) | Decision record: Option D (DB-canonical) adopted 2026-04-19. |
| [programme-prose-structure-design-v1-20260421.md](../research/investigations/programme-prose-structure-design-v1-20260421.md) | Proposed 6-chapter × 45-sub-section structure for programme prose. |
| [prose-instructions-compatibility-review-v1-20260421.md](../research/investigations/prose-instructions-compatibility-review-v1-20260421.md) | Gap analysis of patch + directive instructions vs prose lifecycle; fix plan that landed in commit `9ebcf7e`. |
| [WA-WorkingMemoryAndSnapshots-v1.0-2026-04-21.md](../Workflow/methodology/WA-WorkingMemoryAndSnapshots-v1.0-2026-04-21.md) | Governing principle — database-as-memory, snapshot-as-first-class-research-act. |
| [CLAUDE.md §3 Table Group 17](../CLAUDE.md) | Schema summary entry in project reference (also stale relative to this supersession — not corrected here). |

---

*Architectural summary produced 2026-04-23. Superseded 2026-08-24 — see the table above for live
sources.*
