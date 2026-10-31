# Escalation deep history

## #2339 — Concept mapping: domains and concepts into the database
type=task source=researcher

**v1** (2026-10-31T06:41:52Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Concept mapping: domains and concepts into the database
> **comment (set this version):** Researcher, chat 2026-10-31 (Developer Mode session eccac799): asked for an escalation to process the concept mapping. The mapping is the new basis for the narrative, domains as chapters and concepts as sub-chapters, and must be held in the database so base data to narrative can be followed (researcher ruling, spec field researcher_ruling). Carries the to-do of #2338 (M85 build, standard session 272d94cd); #2338 keeps the M85 record.

Spec: iba/docs/concept-mapping-spec-v1-20261031.json (14 domains, 101 concepts, 411 subgroups; each live group or qualifier subgroup sits in exactly one concept). Review file, regenerated to match the spec and copied into the project: outputs/concept-mapping/concepts-v1-20261031.md (checked: 101 concept headings; domain subgroup counts sum to 411).

Proposed in #2338, not yet approved as a design: tables concept_domain (domain, order, nullable narrative_chapter_id), concept (domain, order, nullable narrative_section_id), concept_subgroup (concept_id, cluster_subgroup_id, one live concept per subgroup), each registered in cfg_table, cfg_column and cfg_write_grant (about 40 to 50 cfg rows, so apply_logged). The 38 narrative chapters and 406 narrative sections stay untouched; the two link columns stay empty until the narrative is rebuilt on the domains.

Open: Feeling kept as four domains (as reviewed) or one chapter with four parts; the dual-tagged spirit subgroup (researcher said not yet). First step: state the build plan and the table design for approval (B:17, B:105), then build and test against a copy.
> **context (set this version):** iba/docs/concept-mapping-spec-v1-20261031.json; outputs/concept-mapping/concepts-v1-20261031.md; iba/app/db/iba.db
