# WA-SessionLog-VerseContextDesign-v2-20260329

**Project:** Framework B — Soul Word Analysis Programme
**Session date:** 2026-03-29
**Session type:** Design continuation and impact assessment
**Participants:** Researcher (Leroux), Claude AI
**Continues from:** WA-SessionLog-VerseContextDesign-v1-2026-03-28.md
**Outputs produced this session:**
- WA-SessionB-VerseContext-Instruction-v1_0-20260329.md (preliminary draft — superseded by planned full rewrite)
- WA-VerseContext-ImpactStudy-v1-20260329.md (superseded)
- WA-VerseContext-ImpactStudy-v2-20260329.md (current)

---

## 1. Session Opening — Inputs Reviewed

Two inputs carried forward from the previous session:
- `wa-programme-status-report-20260328.md` — programme status after major Phase 1 data quality work
- `term_sharing_network_20260328.png` — term sharing visualisation at two thresholds

Researcher confirmed: data quality has improved substantially. Not yet ready to resume Session B analysis at pace. Primary concern is the verse analysis approach.

---

## 2. Patch Specification Received

Researcher provided `patch_specification.md` (v1.1, 2026-03-26). This is the governing document for all patch construction. Key points confirmed:

- Standard patch structure: `_patch_meta`, `operations`, `_patch_summary`
- `session_b_status` required in every `_patch_meta` — patch rejected without it
- Supported operation types: update_mti_status, update_registry, bulk operations, insert on wa_session_research_flags, update/bulk_update on mti_terms and word_registry
- Manual operations (not auto-applied): reassign_verses, restore_delete_flagged, add_cross_registry_links, schema_investigation_note
- Patch ID format: `PATCH-{YYYYMMDD}-{registry_no}-{type}-V{n}`
- All operations in single transaction — all or nothing

---

## 3. Composite Uniqueness and Status Tracking — Resolved

**Composite uniqueness on `verse_context`:**

Initial question: should (verse_record_id + mti_term_id) be unique? Researcher clarified: a verse may legitimately carry two contexts under the same term where two distinct inner-being engagements are plainly evident. Therefore the uniqueness constraint is on (verse_record_id + mti_term_id + group_id) — prevents duplicates within a group, permits genuine dual-context across groups.

Dual-context is rare. Claude AI must not abuse this mechanism to resolve interpretive difficulty.

**Status tracking — registry completion logic:**

Researcher defined the status workflow:

- New status `Verse Context Ready` inserted before `Ready for Analysis`
- All registries at NULL or `Ready for Analysis` reset to `Verse Context Ready`
- During processing: `Verse Context In Progress`
- Claude Code completion check: (1) all OWNER terms for the registry have verse_context records; (2) all XREF terms have coverage via their OWNER term's classification → advance to `Ready for Analysis`

---

## 4. Fundamental Principle Confirmed — Term Context Is Programme-Wide

**Decision:** A term's verse context is a property of the term itself — not of the registry it appears in. The same verse does not change its contextual meaning when viewed from the perspective of a different word.

**Consequence:** `verse_context_group` and `verse_context` use `mti_terms.id` as the foreign key — not `wa_term_inventory.id`. This was confirmed against the schema: `wa_verse_records.mti_term_id` (FK to `mti_terms.id`) was already added by Claude Code and is confirmed present in `database_schema_20260329.json`.

XREF terms are never processed by Claude AI — their verse_context records are populated by Claude Code referencing the OWNER term's completed classification.

---

## 5. Table Design — Final Confirmed

### verse_context_group

| Field | Type | Notes |
|---|---|---|
| id | INTEGER PK | Auto-increment — used for all joins |
| mti_term_id | INTEGER FK | → mti_terms.id |
| group_code | TEXT UNIQUE | `{mti_term_id}-{serial}` — human-readable, never a join key |
| context_description | TEXT NOT NULL | Brief inner-being engagement phrase |
| notes | TEXT | Optional |
| delete_flagged | INTEGER DEFAULT 0 | Programme-wide no-physical-delete policy |

### verse_context

| Field | Type | Notes |
|---|---|---|
| id | INTEGER PK | Auto-increment |
| verse_record_id | INTEGER FK | → wa_verse_records.id |
| mti_term_id | INTEGER FK | → mti_terms.id |
| group_id | INTEGER FK | → verse_context_group.id — NULL if is_relevant = 0 |
| is_anchor | INTEGER | 1 = anchor verse |
| is_relevant | INTEGER | 0 = set aside |
| is_related | INTEGER | 1 = shares group meaning with anchor |
| notes | TEXT | |
| delete_flagged | INTEGER DEFAULT 0 | |

UNIQUE constraint: (verse_record_id, mti_term_id, group_id)

**Key design decisions:**
- Integer PKs throughout — no string join keys (performance requirement)
- group_code → integer id resolved by Claude Code at patch apply time
- No physical deletes — delete_flagged on both tables
- Update-only correction policy — all corrections are UPDATE operations
- Full state snapshot in batch JSON — all verses and all existing classifications included regardless of delete_flagged

---

## 6. Three Patch Types Defined

### VERSECONTEXT (batch)
Full classification run. Input: full state snapshot JSON (all terms, all verses, all existing groups and classifications). Output: insert/update operations on verse_context_group and verse_context covering all terms in batch.

### VCGROUP (targeted group update)
Input: single group snapshot including current field values and anchor verse list. Operations: update on verse_context_group — revise description, notes, or delete_flagged. If reinstating a dissolved group (delete_flagged reset to 0): verse_context rows flagged at dissolution time are NOT automatically reinstated — requires separate VERSECONTEXT or VCVERSE patch.

### VCVERSE (targeted verse update)
Input: single verse snapshot including current verse_context record (if any) and all available groups for the term. Three scenarios: (a) new verse — insert; (b) verse removed from active set — update delete_flagged = 1; (c) reclassify — update existing row. If affected verse was an anchor: anchor integrity check required in same patch.

**Anchor integrity rule — applies to all three patch types:**
Any operation removing, dissolving, or reclassifying an anchor must be accompanied in the same patch by a promotion operation ensuring the term retains at least one active anchor.

---

## 7. Anchor Verse Definition — Expanded and Formalised

An anchor verse is the programme's canonical reference verse for a specific contextual meaning group of a term. It serves two purposes:

1. **Efficiency instrument:** Session B analysis reads anchor verses rather than the full verse corpus
2. **Citation instrument:** Anchor verses appear in the Session B narrative and Session D synthesis as the evidential foundation for claims about the term

Every term must have at least one active anchor across all its groups before Session B analysis may proceed.

Selection criteria: the verse that most clearly and economically demonstrates the contextual meaning; the term's inner-being function is unambiguous; the verse stands alone without requiring surrounding context.

---

## 8. Additional Design Pointers — Confirmed This Session

**1. Re-extraction trigger:** When audit_word is re-run for a word, Claude Code must compare the resulting verse set against existing `verse_context` records for all OWNER terms. If verses are added or removed, flag affected terms for Verse Context revision and reset registry status to `Verse Context In Progress`.

**2. Zero-verse terms excluded:** OWNER terms with no active verses are excluded from Verse Context processing by definition. Claude Code must not require `verse_context` records for these terms in the completion check.

**3. Integrity validation:** Claude Code must validate that any term marked `delete` or `excluded` in `mti_terms` has all its `verse_context` rows flagged (`delete_flagged = 1`). This runs after every patch application cycle.

**4. Integrated instruction:** A single instruction document governing both Claude AI and Claude Code is to be produced — reducing friction and ensuring both systems operate in unison.

**5. Three output documents:**
- Setup Instruction (for Claude Code — schema migration and status reset)
- Integrated Instruction (Claude AI + Claude Code working in unison)
- Impact Update (this impact study — changes needed in all documents)

**6. Missing reference documents:** All documents now uploaded to project files and read fresh. No reliance on session memory.

**7. Open items:** Four items require researcher research/decision before final execution (see Section 9).

---

## 9. Open Items — Unresolved, Pending Researcher Decision

| # | Item | Options |
|---|---|---|
| O1 | M17 pending (source_category → dimensions rename) | Apply before or after M18? |
| O2 | `word_registry.anchor_verses` field | Retain as informal notes field / deprecate / backfill? |
| O3 | Retrospective Verse Context for 35 Analysis Complete registries | Required / recommended / not required? |
| O4 | Prototype batch selection | Confirm 17 not-shared words or alternative? |

---

## 10. Documents Read This Session (fresh — no memory reliance)

- WA-Reference-v5.2-20260329.md
- WA-Registry-Management-Guide-v5.3-20260328.md
- WA-SessionB-DataPrep-Instruction-v5.1-20260327.docx
- WA-SessionB-Analysis-Instruction-v5.1-20260327.docx
- WA-SessionB-Extraction-Instruction-v5.2-20260328.md
- WA-SessionB-ClaudeCode-Instructions.md
- database_schema_20260329.json
- patch_specification.md (uploaded)

---

## 11. Next Session Agenda

1. Resolve four open items (O1–O4) — researcher decisions required
2. Once resolved: produce Setup Instruction (Claude Code — M18 migration + status reset)
3. Produce full Integrated Instruction (Claude AI + Claude Code)
4. Update all downstream documents per impact study Section 5 (update sequence)
5. Prototype and validation run — first batch

---

*WA-SessionLog-VerseContextDesign-v2-20260329 | Session ends | Continues from v1-20260328*
