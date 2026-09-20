# Escalation deep history

## #1783 — Two same-named ib_observation tables, different schemas
type=issue source=researcher

**v1** (2026-09-20T07:31:05Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Two same-named ib_observation tables, different schemas
> **comment (set this version):** Discovered live while fixing #1782 (ib_observation.status wiring). iba.db has the real, live ib_observation table (7,046 rows, cluster-reading pipeline, columns cluster_code/stage/tag/strong/question_code/obs_text/status/etc). bible_research.db ALSO has a table named ib_observation -- 81 rows, completely different schema (operation/dimension/narrative/term_anchor/origin_verse/reconsider_at/status/provenance/basis/raw_file/created), status counts (resolved 56, needs-corroboration 15, open 8, silent 2) matching the stale count cfg_column.use text records for a 'bible_research' database ib_observation.status row -- looks like a relic from the pre-IBA 'characteristics' era (CLAUDE.md's 2026-06-25 method reset / 2026-08-15 base-layer-to-IBA move), not touched since, coincidentally sharing the same table name and a similarly-shaped status enum. Not fixed here -- flagging only, since disposition (archive/rename/drop) needs your call and is unrelated to the live iba.db table this session is actually working on.
> **context (set this version):** cfg_column has two rows for name=ib_observation.status: database=bible_research (use text with the stale 56/15/8/2 counts) and database=iba (use text WRONGLY says 'provisional|corroborated|superseded -- synthesis stage only', not matching the live 4/5-value enum -- being corrected under #1782 for the iba row only).

**v2** (2026-09-20T12:07:38Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  is this still relevant, or must it be withdrawin. 
> **context (set this version):**   
