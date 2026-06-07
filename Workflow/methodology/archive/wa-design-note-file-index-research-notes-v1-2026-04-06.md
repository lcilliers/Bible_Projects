# WA — Design Note: Research Note Storage and File Index Architecture
**File:** wa-design-note-file-index-research-notes-v1-2026-04-06.md
**Date:** 2026-04-06
**Status:** Parked — for action at a future schema review session
**Origin:** Arose during Dimension Review C02 session — analysis of H1902H higgayon (meditation #108)
**Session log reference:** wa-dim-session-log-C02-v1-2026-04-06.md

---

## 1. The Problem That Surfaced

During the Dimension Review for group 5883-001 (H1902H higgayon, meditation registry 108), a reasoning chain was produced that was too valuable to lose but too rich to store in a database field. The reasoning involved:

- Cross-referencing all 4 STEP Bible occurrences of the term
- Reading verse records across 9 registries for Psa 9:16
- Identifying that Psa 92:3 was correctly set aside (musical context)
- Recognising that Lam 3:62 and Psa 19:14 together demonstrate a morally neutral cognitive faculty whose character is determined entirely by orientation
- A conclusion about the theological significance of that finding for Session B

This kind of reasoning — STEP lookup → verse record cross-reference → holistic reading → analytical conclusion — will recur constantly in Session B and Session D. It cannot be captured in a `context_description` field (too short), a `notes` field (unstructured), or a `wa_session_b_findings` record (too narrow). And if it lives only in chat transcripts, it is effectively lost.

**The need:** A way to store rich analytical prose, linked back to the database entities it concerns, retrievable on demand by future sessions.

---

## 2. The Proposed Architecture

**Researcher's proposal:** Two lightweight tables.

- **Table 1 — File catalogue:** One row per file. Stores filename and a unique reference code. The master index of all programme prose.
- **Table 2 — Term-file links:** One row per link. Connects a term (or registry, or group) to a file reference. Multiple links per file; multiple files per term.

When a question arises about a term, the process is: query Table 2 for the term → retrieve file references → read the relevant files. Claude Code queries; Claude AI reads and reasons.

**File format:** `.md` files. Rich prose, full reasoning chains, no compression. Named per programme conventions.

**Key insight from researcher:** The dimensions, not the registries, are likely to become the primary anchor for the final product's presentation of the data. The architecture should not foreclose this. A file-term link table that also allows linking to a dimension label will serve both the current registry-centric phase and a future dimension-centric presentation.

---

## 3. What the Schema Already Has

`wa_file_index` (203 rows) already exists as a file catalogue. It is referenced by:
- `mti_terms.word_data_ref_fk` — terms to their source word data files
- `wa_cross_registry_links.file_id` — files to cross-registry connections (158 rows, 11 connection types)
- `wa_data_quality_flags.file_id` — files to quality flags (21,551 rows)
- `wa_session_b_findings.file_id` — currently null in all existing records (anticipated but not yet used)

`wa_cross_registry_links` is the existing linking table — connects files to registries with a typed connection.

The infrastructure is close to what is needed. What is missing is the ability to link at term (Strong's) level rather than only registry level, and the ability to register files that are not tied to a single registry.

---

## 4. The Core Design Problem — Why This Cannot Be Fixed Now

`wa_file_index` currently serves a dual purpose that creates a structural problem:

1. As a **file catalogue** — tracking what files exist and when they were produced
2. As a **cross-join bridge** — getting from `word_registry` to `wa_term_inventory` via `word_data_ref_fk` on `mti_terms`

This dual role makes `wa_file_index` both the catalogue and a join table, which makes querying harder than it should be. The `registry_id` and `word` fields are NOT NULL — which means every file must be tied to a single registry, making cross-registry analytical notes structurally awkward to register.

**The correct fix** would separate these concerns:
- A clean file catalogue (nullable registry association, file_type field distinguishing word data files from research notes from session logs)
- A clean linking table at term/registry/group/dimension level with typed connection codes

But this requires a schema migration and a rethink of the join paths that currently depend on `wa_file_index`. This is not a trivial change — it touches `mti_terms`, `wa_cross_registry_links`, `wa_data_quality_flags`, and `wa_session_b_findings`.

**The right moment for this:** After the scraping pass that indexes all existing files and their content. At that point the full picture of what needs linking is visible, and the schema redesign can be done once with complete information rather than incrementally.

---

## 5. Interim Approach

Until the schema redesign, research notes produced during Dimension Review and Session B are:
1. Written as `.md` files per programme naming conventions
2. Referenced in session logs with their filename
3. Picked up during the future file scraping pass

The session log serves as the interim index. The future scraping pass will register all files and build the linking structure properly.

---

## 6. What the Future Schema Should Enable

A query like: *"What analytical notes exist that touch H1902H (higgayon)?"* should return a list of files with one join. Currently this is not possible — there is no term-level file link.

The future schema should support linking at four levels:
- Registry level (already exists via `wa_cross_registry_links`)
- Term level (Strong's number) — not yet supported
- Group level (group_code) — not yet supported
- Dimension level — not yet supported (dimensions are not yet first-class entities in the schema)

When dimensions become the primary anchor for the final product, the schema will need dimension records as a proper table (not just a text field in `wa_dimension_index`), and the linking table should be able to point to a dimension_id as well as a registry_id or term.

---

## 7. The Scraping Pass — What It Must Do

When the time comes to run through all existing files:

1. Register every file in a clean `wa_file_index` (or successor table) with: filename, file_type, produced_date, brief description
2. For each file, extract the registries, terms (Strong's numbers), and groups it discusses
3. Insert linking rows connecting each file to its entities
4. Make the result queryable: *"What files discuss H1902H?"* → immediate answer

This pass is a Claude Code task, possibly assisted by Claude AI reading file content to extract entity references. It is a one-time cost that unlocks the full research retrieval capability for Session B and D.

---

## 8. Immediate Action Taken This Session

The H1902H reasoning chain that prompted this discussion is captured in:
- The session transcript (will survive in Claude.ai history)
- `wa-dim-session-log-C02-v1-2026-04-06.md` (Section 4 — open decision and resolution)
- `wa-dim-refinement-log-C02-v0.5-2026-04-06.md` (Registry 108 Phase B entry)
- This design note file

The 5883-001 group description correction (Option C, confirmed by researcher) will travel in the C02 cluster dimension patch when Phase C produces it.

---

*wa-design-note-file-index-research-notes-v1-2026-04-06.md | 2026-04-06 | Parked for future schema review | Origin: Dimension Review C02 H1902H analysis | Do not act on this until after the file scraping pass*
