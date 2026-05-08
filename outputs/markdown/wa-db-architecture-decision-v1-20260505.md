# Database architecture decision — continue, hybrid, or new DB?

**Date:** 2026-05-05
**Status:** PROPOSAL — researcher decision required
**Background:** With registries deprecated as analytical units, dimension-review removed, verse-context-groups marginalised, and Q&A findings reduced to a directional appendix (per [feedback_findings_marginal_value.md](../../C:/Users/lerouxc/.claude/projects/g--My-Drive-Bible-study-projects/memory/feedback_findings_marginal_value.md)), the existing 64-table SQLite database carries substantial legacy analytical machinery that is no longer load-bearing for the new pipeline.

---

## 1. What is in the current DB

**Total: 64 tables, ~165 MB on disk, ~6.6M rows across the largest tables.**

### Canonical raw data — must be preserved (~595k rows)

| Table | Rows | Purpose |
|---|---:|---|
| `wa_verse_records` | 229,778 | One row per term-occurrence-in-verse — the canonical verse source from STEP |
| `wa_verse_term_links` | 226,791 | Span-level links between verses and terms |
| `wa_term_related_words` | 101,970 | Term-relatedness (root families, cognates) |
| `wa_meaning_sense` | 15,956 | Parsed meaning sub-senses (per-term) |
| `mti_terms` | 7,571 | Canonical Strong's master |
| `wa_term_inventory` | 7,550 | Per-file term metadata + OWNER/XREF marker |
| `wa_meaning_parsed` | 7,449 | Parsed meaning text |
| `wa_term_root_family` | 2,861 | Root family membership |
| `mti_term_flags` | 1,005 | Term-level flags |
| `mti_term_cross_refs` | 462 | Strong's cross-references |
| `word_registry` | 214 | The 214-word registry (historical artefact, but still useful for crosswalk) |
| `books` | 66 | Bible book reference |

### Legacy analytical — now reference-only (~78k rows)

| Table | Rows | Status |
|---|---:|---|
| `verse_context` | 41,189 | Old verse-classification — partial, broken methodology |
| `wa_data_quality_flags` | 19,298 | Engine-derived flags from old pipeline |
| `wa_finding_catalogue_links` | 6,199 | Q&A-finding links |
| `verse_context_group` | 3,589 | Old contextual meaning groups |
| `wa_dimension_index` | 3,509 | Old dimensions (rejected per program reset) |
| `wa_session_b_findings` | 2,883 | Q&A findings (registry-scope shotgun, marginal value) |
| `wa_session_research_flags` | 657 | SD pointers + flags |
| `wa_obs_question_catalogue` | 412 | Observation question catalogue (M31) |
| `wa_finding_entity_links` | 287 | Finding↔verse/group links |
| `prose_section` (+5 FTS) | 206 (+~1,300) | DB-canonical prose store (M20) |
| `wa_prose_section_citations` | 562 | Prose citation links |
| `session_d_*` (4 tables) | 0 | Never populated |

### Engine + control (~5k rows)

`engine_run_log`, `engine_stream_checkpoint`, `term_fetch_log`, `word_run_state`, `schema_version`, `wa_file_index` — needed for engine operation; small and unobtrusive.

---

## 2. The three options

### Option A — Continue in the current DB, untouched

Keep everything as is. New analytical work is done by reading from canonical tables (`wa_verse_records`, `mti_terms`, `wa_term_inventory`) and writing to whatever new tables we create. Old analytical tables are simply not consulted.

**Pros**
- Zero data-migration risk.
- Engine, scripts, audit pipeline all still work without change.
- Old findings/pointers remain queryable by direct SQL if needed for occasional dipping.
- No drift between source-of-truth and any copy.

**Cons**
- Schema is cluttered: 30+ tables that aren't part of the new pipeline make the namespace noisy.
- Easy to slip back into using legacy tables (no enforced break).
- DB file stays 165 MB even though half of that is legacy analytical mass.
- Conceptual confusion for any new collaborator: which tables matter?

### Option B — Hybrid: new analytical layer, same DB

Same DB. Add a clean, prefixed schema for the new pipeline:

```text
m_cluster              — M01..M46 + T2 + FLAG identity (45+2 rows)
m_cluster_term         — term → M-cluster assignment + bucket + provenance
m_term_verse_analysis  — per (term, verse): meaning reading, status, group, decision
m_cluster_relation     — cross-cluster claims with anchor verses
m_term_status          — per term: derived coverage state (live view or table)
```

Legacy tables remain untouched. New scripts query canonical raw tables (`wa_verse_records`, `mti_terms`, etc.) and the new `m_*` tables only. Nothing reads or writes `verse_context` / `wa_session_b_findings` / `wa_session_research_flags` from the new pipeline.

Optional: classify legacy tables by adding a `LEGACY:` prefix in CLAUDE.md (or a docstring view). No physical rename.

**Pros**
- Clean break in code without data migration.
- All raw data stays single-source-of-truth.
- Old findings/pointers stay accessible for the "occasional dip" the researcher described.
- Easy to add migrations to the new layer (M-clusters can evolve).
- Engine and audit pipeline unaffected.

**Cons**
- Discipline needed — easy to accidentally use a legacy table.
- DB file size unchanged.
- Mixed-model schema requires clear instruction docs.

### Option C — Spawn a new DB

Create `database/bible_clusters.db` (or similar). Copy *only* the canonical raw data into it (a one-shot ETL). Build the new pipeline against the new DB. Old DB becomes a frozen reference accessible only by occasional explicit query.

**Pros**
- Clean schema slate.
- Smaller file (~25-50 MB vs 165 MB).
- Hard architectural boundary — impossible to accidentally use legacy tables.
- Cleaner mental model for future work.

**Cons**
- **Data drift risk** — if the source DB is ever updated (engine ingests new STEP data, term re-extraction), the new DB diverges. Need a re-ETL discipline.
- Engine and audit pipeline need to be re-pointed or duplicated.
- Loss of in-place access to legacy reference data (would need cross-DB attach for ad-hoc dipping).
- Migration effort: write the ETL, validate row counts, handle edge cases.
- Two DBs to back up, version, gitignore.

---

## 3. Decision matrix

| Criterion | A: Continue | B: Hybrid | C: New DB |
|---|---|---|---|
| Data-migration risk | None | None | Medium |
| Engine compatibility | Full | Full | Needs work |
| Schema cleanliness | Poor | Good | Excellent |
| Legacy data access | Native | Native | Cross-DB attach |
| Risk of accidental legacy use | High | Medium | None |
| File size | 165 MB | 165 MB | ~30-50 MB |
| Developer mental model | Cluttered | Clear with docs | Cleanest |
| Forward compatibility | Worst | Good | Best |
| Maintenance overhead | Low | Low | Medium (ETL discipline) |
| Time to be productive on M05 | **Now** | **Now** (after ~1 day of schema) | ~3-5 days |

## 4. Recommendation — Option B (hybrid)

Reasons:

1. **The canonical raw data is already clean.** `wa_verse_records`, `mti_terms`, `wa_term_inventory`, root families, parsed meanings — these are the foundation and they're already correct. Migrating them to a new DB adds risk without benefit.

2. **The legacy analytical mass is a write-once-read-occasionally archive.** The researcher said: *"keep the existing findings and pointers as references and every now and then dip into it"*. That's precisely what Option B delivers — they remain in place, queryable, but not in the new pipeline's path.

3. **Building the new analytical schema is the actual work.** Whether that schema lives in `bible_research.db` or `bible_clusters.db` is incidental. What matters is that the new tables are well-designed.

4. **A new DB introduces a synchronisation problem.** Any time STEP data is refreshed, terms are re-extracted, or root families are updated, both DBs must be kept in lockstep. Option B avoids this entirely.

5. **The "discipline" cost of Option B is smaller than the "ETL discipline" cost of Option C.** Code reviews and a single CLAUDE.md classification of legacy tables solve the discipline problem.

**Proposed plan for Option B:**

1. **Design** the new analytical schema (5-7 `m_*` tables) — single design pass, ~½ day.
2. **Migrate** the schema (apply via `engine.engine --migrate` or a one-shot script).
3. **Update CLAUDE.md** with a *"Canonical vs Legacy"* table (annotated list of all 64 tables, marked).
4. **Build** the first analytical script (`scripts/_m_term_analysis_v1.py`) that reads from canonical raw tables + writes to `m_term_verse_analysis` for an M-cluster.
5. **Pilot M05** end-to-end against the new schema.
6. **Freeze** the legacy tables — no new writes from any script. Existing engine flows that touch them get audited / paused.

## 5. Risks under Option B

- **Discipline drift.** Easy for a future script to import from `verse_context` "just to get the verse text". Mitigation: explicit instruction in CLAUDE.md, naming convention, code review of new scripts.
- **Engine entanglement.** The audit pipeline (`engine.audit`) writes to `wa_data_quality_flags` etc. If those are now classified legacy, what runs them? Decision needed: retire the audit pipeline, or run it only for STEP-ingest validation.
- **Schema versioning conflict.** Adding `m_*` tables means new schema_version (3.18.0). Existing engine constants (`EXPECTED_SCHEMA_VERSION = "3.17.0"`) need to advance — coordinated with the new tables.

## 6. What Option B does NOT decide

- The exact shape of `m_term_verse_analysis` — that's the next design pass once Option B is approved.
- Whether to retire the audit pipeline — separate decision.
- Whether to mark legacy tables with `LEGACY_` prefix or just classify in docs — small ergonomic call.
- What to do about `engine.engine --mode=audit_word` (heavily wired to old pipeline) — separate decision.

## 7. Decision sought

Pick A, B, or C. If B, I'll proceed to the schema-design pass for the `m_*` tables.

If you want to think about it further, the M05 term-level work can also start *without* this decision — initially as scripts that just read from canonical tables and write `.json` outputs (no DB writes). That defers the schema decision while still progressing the analysis.
