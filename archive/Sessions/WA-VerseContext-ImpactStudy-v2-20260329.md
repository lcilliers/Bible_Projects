# WA-VerseContext-ImpactStudy-v2-20260329

**Project:** Framework B — Soul Word Analysis Programme
**Date:** 2026-03-29
**Version:** 2 — full rewrite based on current document set
**Supersedes:** WA-VerseContext-ImpactStudy-v1-20260329.md
**Purpose:** Impact assessment of the Verse Context pipeline stage on all programme documents, database structures, and instruction sets. Governs the update sequence for all downstream documents before the integrated instruction is produced.
**Produced by:** Claude AI — design session 2026-03-29
**Source documents read:** WA-Reference-v5.2-20260329.md; WA-Registry-Management-Guide-v5.3-20260328.md; WA-SessionB-DataPrep-Instruction-v5.1-20260327.docx; WA-SessionB-Analysis-Instruction-v5.1-20260327.docx; WA-SessionB-Extraction-Instruction-v5.2-20260328.md; WA-SessionB-ClaudeCode-Instructions.md; database_schema_20260329.json; patch_specification.md (uploaded this session)

---

## 1. What Is Being Introduced

### 1.1 Two new database tables

**`verse_context_group`** — one row per contextual meaning group per term. The group description lives here once. Foreign key to `mti_terms.id`.

**`verse_context`** — one row per verse per term. Carries the relevance filter result, group assignment, anchor/related flags, and deletion state. Foreign keys to `wa_verse_records.id` and `mti_terms.id`.

### 1.2 A new pipeline stage — Pre-Session B Verse Context

Sits between Phase 1 audit completion and Session B DataPrep. Classifies all active OWNER term verses against the governing inner-being relevance filter. Groups relevant verses by contextual meaning. Designates anchor verses — the canonical citation and Session B analysis input per term. Produces verse context patches for Claude Code application.

OWNER terms with no active verses are excluded from Verse Context processing by definition.

### 1.3 Two new `word_registry.session_b_status` values

- `Verse Context Ready` — post-Phase 1 state; replaces NULL as the entry point for the Verse Context stage
- `Verse Context In Progress` — intermediate state during active Verse Context processing

### 1.4 Three new patch types

- `VERSECONTEXT` — full batch classification run covering multiple terms
- `VCGROUP` — targeted update to a single `verse_context_group` record
- `VCVERSE` — targeted update to a single `verse_context` record

### 1.5 New anchor verse definition

An anchor verse is not merely a representative example. It is the programme's canonical reference verse for a specific contextual meaning group of a term — the verse that most clearly and economically demonstrates the group's inner-being engagement. Anchor verses serve two purposes: (1) primary input for Session B analysis — Claude AI reads anchors rather than the full verse corpus; (2) cited evidence — anchor verses appear in the Session B narrative and in Session D synthesis as the evidential foundation for claims about the term. Every term must have at least one active anchor across all its groups before Session B analysis may proceed.

### 1.6 Re-extraction trigger (new Claude Code obligation)

When a word's Phase 1 extraction is reproduced (audit_word re-run), Claude Code must automatically compare the resulting verse set against existing `verse_context` records for all OWNER terms in the dataset. If any verses have been added or removed, Claude Code must flag the affected terms for Verse Context revision and set their registry status back to `Verse Context In Progress`.

### 1.7 Integrity validation (new Claude Code obligation)

Claude Code must validate `verse_context` integrity as part of its routine operations: any term marked as `delete` or `excluded` in `mti_terms` must have all its `verse_context` rows flagged (`delete_flagged = 1`). This check must run after every patch application cycle.

---

## 2. Database Impact

### 2.1 Schema state — confirmed from database_schema_20260329.json

| Item | Status |
|---|---|
| `wa_verse_records.mti_term_id` | **Confirmed present** — FK to `mti_terms.id` |
| `verse_context_group` table | **Not present** — requires creation (migration M18) |
| `verse_context` table | **Not present** — requires creation (migration M18) |
| `word_registry.session_b_status` new values | **Not yet added** — requires controlled vocabulary update |
| `word_registry.source_category` | **Still present** — M17 rename to `dimensions` not yet applied |

### 2.2 New table — `verse_context_group`

```sql
CREATE TABLE IF NOT EXISTS verse_context_group (
  id INTEGER PRIMARY KEY,
  mti_term_id INTEGER NOT NULL REFERENCES mti_terms(id),
  group_code TEXT NOT NULL UNIQUE,
  context_description TEXT NOT NULL,
  notes TEXT DEFAULT NULL,
  delete_flagged INTEGER DEFAULT 0
);
```

| Field | Notes |
|---|---|
| id | INTEGER PK — auto-increment. Used for all joins. |
| mti_term_id | FK → mti_terms.id. Programme-wide term identifier. Never registry-instance specific. |
| group_code | TEXT — `{mti_term_id}-{serial}` e.g. `142-001`. Human-readable reference. Constructed by Claude AI at patch time. Never used as a join key. |
| context_description | Brief phrase capturing the contextual meaning — inner-being engagement of the term in this group. |
| notes | Optional qualification or exception. |
| delete_flagged | 0 = active; 1 = dissolved group. Programme-wide no-physical-delete policy. |

### 2.3 New table — `verse_context`

```sql
CREATE TABLE IF NOT EXISTS verse_context (
  id INTEGER PRIMARY KEY,
  verse_record_id INTEGER NOT NULL REFERENCES wa_verse_records(id),
  mti_term_id INTEGER NOT NULL REFERENCES mti_terms(id),
  group_id INTEGER REFERENCES verse_context_group(id),
  is_anchor INTEGER NOT NULL DEFAULT 0,
  is_relevant INTEGER NOT NULL DEFAULT 0,
  is_related INTEGER NOT NULL DEFAULT 0,
  notes TEXT DEFAULT NULL,
  delete_flagged INTEGER DEFAULT 0,
  UNIQUE (verse_record_id, mti_term_id, group_id)
);
```

| Field | Notes |
|---|---|
| id | INTEGER PK — auto-increment |
| verse_record_id | FK → wa_verse_records.id |
| mti_term_id | FK → mti_terms.id |
| group_id | FK → verse_context_group.id — NULL when is_relevant = 0 |
| is_anchor | 1 = anchor verse for its group. Session B reads this. Programme cites this. |
| is_relevant | 0 = set aside (no inner-being engagement); 1 = inner-being relevant |
| is_related | 1 = shares group meaning with anchor, not itself the anchor |
| notes | Dual-context flags, borderline retention notes, revision reasons |
| delete_flagged | 0 = active; 1 = excluded. Programme-wide no-physical-delete policy. |

**Uniqueness constraint:** UNIQUE on (verse_record_id, mti_term_id, group_id). Same verse may appear under two different groups for the same term (genuine dual-context). Same verse may not appear twice in the same group.

### 2.4 Logical consistency rules — enforced by Claude AI, validated by Claude Code

| Rule | Condition |
|---|---|
| R1 | is_relevant = 0 → group_id IS NULL, is_anchor = 0, is_related = 0 |
| R2 | is_anchor = 1 → is_relevant = 1, is_related = 0, group_id NOT NULL |
| R3 | is_related = 1 → is_relevant = 1, group_id references a group with at least one is_anchor = 1 row |
| R4 | Every term must have at least one active (delete_flagged = 0) is_anchor = 1 row before Session B may proceed |

### 2.5 Schema migration required — M18

Migration M17 (source_category → dimensions rename) is still pending. M18 may proceed independently — there is no design dependency between M17 and M18.

**M18 actions:**
1. CREATE TABLE verse_context_group (as above)
2. CREATE TABLE verse_context (as above)
3. Update schema_version record to 3.8.0

`wa_verse_records.mti_term_id` is already present — no action required for that field.

### 2.6 Programme-wide data action — status reset

After M18 is confirmed, a one-time status reset is required:

| Current status | Reset to | Registries affected |
|---|---|---|
| NULL | `Verse Context Ready` | 33 registries |
| `Ready for Analysis` | `Verse Context Ready` | 144 registries |
| `Pre-Analysis Complete` | No change | existing pipeline |
| `Analysis Complete` | No change | existing pipeline |
| `Session B Complete` | No change | existing pipeline |

**Total affected: 177 registries.**

Registries at `Pre-Analysis Complete` or higher have already passed through the pre-analysis stage under the old workflow. They are not subject to retrospective Verse Context processing — see Section 6, Open Item O3.

### 2.7 OWNER terms with no active verses — excluded from Verse Context

Terms where all verse records are `delete_flagged = 1` or where `phase1_verse_count = 0` produce no `verse_context` rows. Claude Code must exclude these terms from batch construction. The registry completion check must not require `verse_context` records for zero-verse terms.

---

## 3. Document Impact — Full Inventory

### 3.1 Source documents confirmed current

| Document | Version | Confirmed current |
|---|---|---|
| WA-Reference | v5.2 | Yes — 20260329 |
| WA-Registry-Management-Guide | v5.3 | Yes — 20260328 |
| WA-SessionB-DataPrep-Instruction | v5.1 | Yes — 20260327 |
| WA-SessionB-Analysis-Instruction | v5.1 | Yes — 20260327 |
| WA-SessionB-Extraction-Instruction | v5.2 | Yes — 20260328 |
| WA-SessionB-ClaudeCode-Instructions | — | Yes — updated 20260329 |
| database_schema | — | Yes — 20260329 (schema 3.7.0, M16 complete) |
| patch_specification | v1.1 | Yes — uploaded this session |

### 3.2 WA-Reference-v5.2 → update to v5.3

| Section | Change required |
|---|---|
| 1.1 Word-level files | Add scope tokens: `vcb-extract` for batch JSON input (`wa-vcb-{batch_id}-extract-{date}.json`); `vcb-patch` for batch patch output (`wa-vcb-{batch_id}-patch-{date}.json`) |
| 1.3 Instruction documents | Add `WA-SessionB-VerseContext-Instruction-v{n}-{date}.md` |
| 1.4 Patch ID convention | Add three new patch ID formats: `PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1`; `PATCH-{YYYYMMDD}-VCGROUP{group_id}-V1`; `PATCH-{YYYYMMDD}-VCVERSE{verse_record_id}-V1` |
| 3. session_b_status vocabulary | Add `Verse Context Ready` and `Verse Context In Progress` with definitions |
| 12. Patch type vocabulary | Add VERSECONTEXT, VCGROUP, VCVERSE — each referencing WA-SessionB-VerseContext-Instruction-v1.0 |
| 13.1 word_registry | Note two new valid status values in session_b_status description |
| 13 schema summary | Add `verse_context_group` and `verse_context` table summaries; update schema version reference to 3.8.0 |
| New section — anchor verse | Define anchor verse formally (see Section 1.5 above). This definition must appear here as the authoritative reference. |

### 3.3 WA-Registry-Management-Guide-v5.3 → update to v5.4

| Section | Change required |
|---|---|
| 2. Registry fields | Update `session_b_status` field row to include two new values and note the new gate |
| 3. Registry Status Lifecycle | Insert `Verse Context Ready` and `Verse Context In Progress` into the status table and narrative. Update the gate warning: Session B DataPrep now requires `Ready for Analysis` — which is only reached after Verse Context completion, not directly from NULL |
| 6.2 Words Ready for Analysis | Query unchanged — `Ready for Analysis` remains the DataPrep gate. Add new query 6.8: Words at Verse Context stage (`WHERE session_b_status IN ('Verse Context Ready', 'Verse Context In Progress')`) |
| 8. Terminology reference | Add: `Verse Context` (definition of the new stage); `anchor verse` (formal definition per Section 1.5); `contextual meaning group` (a set of verses where the term functions in the same way in relation to the inner being, described by a single context_description) |
| 9. File naming reference | Add `vcb-extract` and `vcb-patch` scope tokens |

### 3.4 WA-SessionB-DataPrep-Instruction-v5.1 → update to v5.2

**Impact: low — one gate addition only**

| Section | Change required |
|---|---|
| 4. Registry Status Validation | Add two new rows to the status table: `Verse Context Ready` → stop, direct to complete Verse Context first; `Verse Context In Progress` → stop, Verse Context not yet complete for this registry |
| Change note | Record that v5.2 adds the Verse Context gate check — no other changes |

### 3.5 WA-SessionB-Analysis-Instruction-v5.1 → update to v5.2

**Impact: medium — verse reading protocol changes materially**

| Section | Change required |
|---|---|
| 4.2 Startup sequence | Add step: confirm that Verse Context is complete for this registry. The word JSON export will carry verse_context data — Claude AI must confirm at least one anchor verse exists per active term before proceeding |
| 4.3 Registry status validation | Add `Verse Context Ready` and `Verse Context In Progress` as invalid entry states with stop instruction |
| 5.1 Core reading rules | Replace "Read every verse in the active term inventory" with: Read anchor verses for each term. Related verses are pre-classified as sharing the same contextual meaning as their anchor — they do not require independent reading unless the anchor classification is uncertain or a term has no anchor |
| 5.2 What to observe | Unchanged — observation protocol applies to anchor verses |
| New Section 5.3 | How to use verse context data: reading the group structure from the JSON; interpreting set-aside verses; handling dual-context anchors; what to do when a term has no Verse Context data (stop — Verse Context not complete) |
| 10.2 Required sections | Note that Section 8 (Key verse observations) draws from anchor verses, not the full corpus |

### 3.6 WA-SessionB-Extraction-Instruction-v5.2 → update to v5.3

**Impact: low — reference additions only**

| Section | Change required |
|---|---|
| 3. Extraction process | Note that verse context data (anchor verses, group descriptions) is available in the database and may be referenced when populating the key_findings and anchor_verses fields — it does not need to be re-derived from the narrative |
| 5. Database field mapping | Add `verse_context_group` and `verse_context` as queryable sources for anchor verse references in the key_findings array |

### 3.7 WA-SessionB-ClaudeCode-Instructions → update

**Impact: significant — new section required**

| Section | Change required |
|---|---|
| 2.6 Ongoing obligations | Add: after every audit_word re-run, compare resulting verse set against existing `verse_context` records for all OWNER terms. Flag affected terms for revision. Reset registry status to `Verse Context In Progress` for any term where verses were added or removed. |
| 4. Patch application | Add Section 4.3: Verse Context patch types (VERSECONTEXT, VCGROUP, VCVERSE) — operation types, group_code resolution, consistency rule validation, anchor integrity check, registry completion check logic |
| 6. Programme state queries | Add three queries: (a) terms ready for Verse Context batch construction; (b) Verse Context completion status per registry; (c) terms with delete/excluded status whose verse_context rows are not delete_flagged (integrity check) |
| 8. Controlled vocabulary | Add Verse Context status values; add patch types VERSECONTEXT, VCGROUP, VCVERSE |
| 12. Engine and script status | Add: verse context batch export function; verse context patch applicator; re-extraction trigger; integrity validation |
| New Section — Verse Context Operations | Full operational specification for Claude Code's Verse Context responsibilities: batch construction criteria; JSON export structure; patch application for all three patch types; group_code → id resolution; registry completion check; anchor integrity check; re-extraction trigger; integrity validation |

### 3.8 patch_specification.md (v1.1) → update to v1.2

**Impact: medium — new patch types and status values**

| Section | Change required |
|---|---|
| 0. Session B Status Workflow | Insert `Verse Context Ready` and `Verse Context In Progress` into the status diagram and status table |
| 1. File naming | Add VERSECONTEXT, VCGROUP, VCVERSE to the Types list |
| New Section — Verse Context Patch Operations | Specify all operation types for three patch types: insert/update on verse_context_group; insert/update on verse_context; group_code resolution instruction; consistency rule validation requirements; anchor integrity check |
| Appendix A.5 | Add `Verse Context Ready` and `Verse Context In Progress` to the valid session_b_status table |

### 3.9 WA-SessionD-Orientation-v2 — no immediate update required

The verse context data — particularly `verse_context_group.context_description` as a pre-classified semantic summary per term — will be a valuable Session D input. No update required until Session D design is formalised. Flag for future revision.

---

## 4. Three Output Documents Required

Per researcher instruction, three documents are to be produced following this impact study:

| # | Document | Format | Purpose |
|---|---|---|---|
| 1 | **Setup Instruction** | .md | Claude Code instruction for schema migration M18 and programme-wide status reset. Includes full SQL DDL, validation queries, and the status reset operation. |
| 2 | **Integrated Instruction** | .md | Single document governing both Claude AI and Claude Code through the full Verse Context cycle. Covers: batch JSON input specification (Claude Code); verse reading, filtering, grouping, and anchor designation (Claude AI); all three patch types with full operation specifications (Claude AI produces, Claude Code applies); re-extraction trigger; integrity validation; registry completion check. |
| 3 | **Impact Update** | .md | This document — listing all changes needed in upstream and downstream instructions (complete). |

---

## 5. Document Update Sequence

Dependencies govern this sequence. Earlier steps must be confirmed before later ones proceed.

| Step | Action | Version change | Dependency |
|---|---|---|---|
| 1 | Schema migration M18 — Claude Code executes | Schema 3.7.0 → 3.8.0 | None |
| 2 | Setup Instruction produced and executed | New document | None |
| 3 | Programme-wide status reset — Claude Code executes | 177 registries | Step 1 confirmed |
| 4 | WA-Reference updated | v5.2 → v5.3 | Step 1 confirmed |
| 5 | Integrated Instruction produced (full rewrite) | v1.0 | Steps 1–4 confirmed |
| 6 | WA-Registry-Management-Guide updated | v5.3 → v5.4 | Step 5 confirmed |
| 7 | WA-SessionB-DataPrep-Instruction updated | v5.1 → v5.2 | Step 5 confirmed |
| 8 | WA-SessionB-Analysis-Instruction updated | v5.1 → v5.2 | Step 5 confirmed |
| 9 | WA-SessionB-Extraction-Instruction updated | v5.2 → v5.3 | Step 5 confirmed |
| 10 | WA-SessionB-ClaudeCode-Instructions updated | — | Step 5 confirmed |
| 11 | patch_specification updated | v1.1 → v1.2 | Step 5 confirmed |
| 12 | Prototype and validation run | First batch | Steps 1–11 confirmed |

Steps 6–11 may proceed in parallel once Step 5 is complete and validated.

Step 12 (prototype run) must not begin until all instruction documents are updated and confirmed.

---

## 6. Open Items — Requiring Researcher Decision

These items were identified during the design session and require research or decision before they can be resolved. They do not block document production but must be resolved before the programme-wide status reset (Step 3) is executed.

| # | Item | Question | Blocks |
|---|---|---|---|
| O1 | M17 pending — source_category → dimensions rename | Has M17 been applied? The database_schema_20260329.json shows `source_category` still present on `word_registry`. Should M17 be applied before or after M18? | M18 sequencing only — no design dependency |
| O2 | `word_registry.anchor_verses` field | This informal field currently exists at registry level. With the new `verse_context` anchor mechanism formalised at term level, what is the status of `word_registry.anchor_verses`? Options: (a) retain as informal researcher notes field; (b) deprecate — Verse Context anchor mechanism supersedes it; (c) backfill from completed Session B analyses. Impacts DataPrep and Analysis instruction references. | Step 7 and 8 |
| O3 | Retrospective Verse Context for 35 Analysis Complete registries | These completed Session B under the old workflow without Verse Context. Options: (a) no retrospective requirement — they proceed to Session B Complete as-is; (b) retrospective Verse Context required before Session B Complete status can be assigned; (c) retrospective Verse Context recommended but not required. Affects status reset scope and programme workload. | Step 3 |
| O4 | Prototype batch selection | The programme status report recommended the 17 not-shared words as the simplest starting point (zero cross-registry complexity, 2,445 verses across 98 terms). Confirm this selection, or identify alternative. | Step 12 |

---

## 7. Additional Design Decisions Confirmed This Session

These were resolved during the design conversation and are recorded here for instruction production reference.

| Decision | Detail |
|---|---|
| Integer PKs throughout | All table joins use integer PKs. group_code is a human-readable label only — never used as a join key. |
| No physical deletes anywhere | delete_flagged = 1 on both `verse_context_group` and `verse_context`. Consistent with programme-wide policy. |
| Update-only correction policy | All corrections to existing records are UPDATE operations. Delete + reinsert is not permitted. |
| Full state snapshot in batch JSON | All verses included (classified and unclassified); all existing groups included; all existing verse_context records included regardless of delete_flagged. Claude AI needs full history for consistent revision decisions. |
| OWNER terms only in batches | Claude Code includes only term_owner_type = OWNER terms in batch construction. XREF verse_context records are populated by Claude Code referencing the OWNER term's completed classification — not processed by Claude AI. |
| Batch target: 2,000–2,500 verses | Accumulate OWNER terms until unclassified verse count reaches target. Never split a term across batches. |
| Dual-context: rare exception | Same verse may appear under two groups for the same term only when two distinct inner-being engagements are plainly evident. Not to be used to resolve interpretive difficulty. |
| Anchor integrity rule | Any operation affecting an anchor (reclassification, delete_flagged, group dissolution) must be accompanied by a promotion operation in the same patch ensuring the term retains at least one active anchor. |
| group_code format | `{mti_term_id}-{serial}` — serial is a zero-padded 3-digit sequence resetting per term. Example: term 142, first group → `142-001`. |
| group_code → id resolution | Claude Code resolves group_code to integer id at patch apply time. Within a single patch, newly inserted group ids are captured immediately after insert and used for subsequent verse_context inserts referencing that group. |

---

*WA-VerseContext-ImpactStudy-v2-20260329 | Produced by Claude AI | Supersedes v1 | For researcher review and open item resolution before document production proceeds*
