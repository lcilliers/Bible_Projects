# Programme-Wide Prose Session — Reference Bundle

**Date:** 2026-04-21
**Purpose:** brief the AI session that will author the 8 programme-wide prose sections.

---

## 1. What the session is writing

Eight programme-stage prose sections are seeded in `prose_section_type` with `source_stage = 'programme'`, all currently empty (`prose_section` has 0 active rows). They are:

| Section code | Subject |
| --- | --- |
| `prog_anchor_verse` | Anchor Verse Definition |
| `prog_xref_architecture` | XREF Architecture |
| `prog_validation_standard` | Document Validation Standard |
| `prog_delete_discipline` | Soft-Delete Discipline |
| `prog_field_authority` | Field Authority Rules |
| `prog_backup_discipline` | Backup Discipline |
| `prog_patch_failure_protocol` | Patch Failure / REPAIR Protocol |
| `prog_instruction_override_protocol` | Instruction Override Protocol |

Each section is a short narrative explaining the named programme-wide discipline / protocol, suitable for inclusion in programme orientation material.

---

## 2. Attach these files to the AI session

### 2.1 Fresh JSON extracts (authoritative, current state)

| File | Purpose | Fresh as of |
| --- | --- | --- |
| [wa-global-rules-extract-20260421.json](../../data/exports/reference/wa-global-rules-extract-20260421.json) | All 36 active rules — authoring discipline, file/naming conventions, document discipline (GR-REF-001/002 especially), programme orientation rules | 2026-04-21 post batch1/2/3 |
| [wa-programme-prose-extract-20260421.json](../../data/exports/reference/wa-programme-prose-extract-20260421.json) | Current prose state: 8 empty section types the session will populate, and (if any) existing prose. `--include-body` flag was used. | 2026-04-21 |
| [wa-reference-snapshot-20260421.json](../../data/exports/reference/wa-reference-snapshot-20260421.json) | Controlled vocabulary (5 sets), patch types, file patterns, label patterns, schema summary (61 tables) | 2026-04-21 |
| [database-schema-v3.14.0-20260421.json](../../data/schema/database-schema-v3.14.0-20260421.json) | Full DB schema — column-level detail for tables the prose will describe (XREF, soft-delete, backup, field authority) | 2026-04-21 post DIR-001 |

### 2.2 Instruction documents (markdown, read directly from Session_B/)

| File | Why | Scope |
| --- | --- | --- |
| [wa-patch-instruction-v2_3-20260421.md](../../data/imports/WA/Workflow/Framework_B/Session_B/wa-patch-instruction-v2_3-20260421.md) | PROSE patch type format (§3.3), operation patterns for `prose_section` inserts | Needed to produce the PROSE patch |
| [wa-reference-v5_7-20260420.md](../../data/imports/WA/Workflow/Framework_B/Session_B/wa-reference-v5_7-20260420.md) | Programme vocabulary, prose store design (§13.14), writing conventions | Reference while drafting |
| [wa-directive-instruction-v1_1-20260418.md](../../data/imports/WA/Workflow/Framework_B/Session_B/wa-directive-instruction-v1_1-20260418.md) | Directive format — only needed if a schema change is discovered mid-session | On demand |

### 2.3 What NOT to attach (not relevant for programme prose)

- Word registry / verse / term exports — this is programme-wide, no word scope
- Session B / C / D analysis extracts — different stage
- Patch type extracts and vocab extracts as standalone files — already bundled in the reference snapshot

---

## 3. Suggested session approach

Each of the 8 sections is short (likely 150–400 words each). The AI can draft them as a batch in a single session:

1. Read the four JSON extracts + three MD docs.
2. For each of the 8 `prog_*` section types, draft a prose section. Heading = the section's label from `prose_section_type`. Body = narrative drawn from the relevant rules + schema facts + current programme state. Keep tense consistent (present-tense normative for disciplines; past-tense provenance for history).
3. Produce one PROSE patch (§3.3 in v2_3 instruction) containing 8 `insert` operations on `prose_section`, one per section type. Use `registry_id = NULL` (programme-wide has no registry). Set `author = 'claude_ai'`, `status = 'draft'`, `version = 1`. Include `source_file` pointing to this bundle.
4. Per rules-update workflow (analogue): draft → self-check → show to researcher → apply on approval → regenerate programme prose extract.

---

## 4. Source material hints per section

To save the session research time, brief pointers to the best source for each prose:

| Section | Primary source |
| --- | --- |
| `prog_anchor_verse` | wa-reference §14.2 (anchor verse in final extract); wa-versecontext-instruction §5 anchor designation rules; verse_context.is_anchor schema |
| `prog_xref_architecture` | CLAUDE.md §3 (XREF Architecture block); `wa_term_inventory.term_owner_type` schema; mti_terms + verse_context programme-wide nature |
| `prog_validation_standard` | GR-REF-001 (five disciplines) — applied recursively to prose itself; wa-reference document-validation section |
| `prog_delete_discipline` | GR-OBS-005 (now absorbed into patch instruction §5.4); `delete_flagged` column across tables; applicator's rejection of physical DELETE |
| `prog_field_authority` | Researcher-authored fields (e.g. `word_registry.inference_note`, `word_synopsis`); pipeline-derivable fields; CLAUDE.md §4.16 retained-vs-dropped block |
| `prog_backup_discipline` | `engine/backup.py` (rolling 10, pre/post-run); applicator per-patch backup convention; 6-month retention mentioned in prior session logs |
| `prog_patch_failure_protocol` | wa-patch-instruction v2_3 §10 (Failure Patch) + §9 (REPAIR Catalogue) |
| `prog_instruction_override_protocol` | GR-PROC-004 (researcher approval); hierarchy — Global rules > instructions > conversational; override path via patch or directive |

---

## 5. Session output

One PROSE patch: `wa-prose-programme-v1-20260421.json` (or similar per §2.4 programme-wide filename convention in v2_3 patch instruction).

After apply + regenerate:
- `data/exports/reference/wa-programme-prose-extract-{YYYYMMDD}.json` will show 8 active content sections with bodies.
- The MD companion (if `--also-markdown` is added to the extractor; currently it only emits JSON) will give a readable view.

---

*Bundle produced 2026-04-21 to brief the programme-wide prose authoring session.*
