---
name: feedback_all_study_work_in_db
description: GOVERNING rule (2026-06-09). ALL the study work must be captured in the DB — the single source of truth. No lookups, indexes, references, or staged results held in separate ad-hoc structures, in-memory lists, or files. Findings, the clarification library, tier-question links, keyword allocations, signals/vocabularies, intermediate/staged results — all DB-resident. Markdown/JSON are human-readable OUTPUTS or prototypes only, never the system of record. Reinforces "finding = universal unit, DB sole record".
metadata:
  type: feedback
---

**Researcher rule (2026-06-09):** **ALL the study work must be captured in the DB.** We do **not** keep
lookups, indexes, references, or staged results in **separate ad-hoc tables/structures, lists in memory, or
files.** The DB is the single source of truth.

**Implications:**
- The **finding record** (per-term-in-verse tier findings), the **clarification library**, finding↔tier-question
  links, **correction/provenance history**, the **keyword allocation**, relationship-type / thing-type
  vocabularies, adequacy signals, and any **staged/intermediate results** are all **DB-resident**.
- The JSON findings store and CSV keyword map I built are **prototypes only** — the real versions are DB
  tables. `.md`/`.json` files are **human-readable outputs or prototypes**, never the system of record.
- Reinforces [[reference_analysis_rules_finding_lifecycle]] ("finding = universal unit, DB sole record") and
  broadens it to *all* study artefacts.

**So the schema must hold everything.** The L2 finding system (proposed migration M56) extends `verse_context`
(the per-(verse,term) anchor, already carrying `step_meaning_applied`/`pole`/`residue_flag` from M55) and adds
verse-level finding + revision tables; `cluster_finding` (existing) is the cluster-level roll-up. **Design v2
(researcher markup D1–D5): `research/investigations/wa-l2-finding-schema-design-v2-20260609.md`** — D3
reframed: a **clarification is just an OPEN/RESOLVED finding at the correct level**, so there is **no separate
clarification table**; ONE level-aware `finding` table (level VERSE/TERM/CLUSTER/GLOBAL; `justified_by_finding_id`
finding↔finding link); D2 finding↔question is M:N via `finding_question_link`; D5 STATE_SILENT recorded
explicitly (rarity of a positive tier finding across many silent verses is itself significant). Open: legacy
`cluster_finding`/`wa_session_b_findings` migrate INTO `finding` as a later step (not M56).
