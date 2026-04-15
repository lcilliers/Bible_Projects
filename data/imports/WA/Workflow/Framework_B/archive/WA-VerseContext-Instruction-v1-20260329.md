# WA-VerseContext-Instruction-v1-20260329

**Framework B — Soul Word Analysis Programme**
**Verse Context Instruction — Integrated Claude AI and Claude Code**
**Version 1.0 | March 2026 | Status: Active governing instruction**

| **Document** | **Value** |
|---|---|
| Filename | WA-VerseContext-Instruction-v1-20260329.md |
| Supersedes | WA-SessionB-VerseContext-Instruction-v1_0-20260329.md (preliminary draft) |
| Companion documents | WA-VerseContext-SetupInstruction-v1 │ WA-Reference-v5.2 │ WA-VerseContext-ImpactStudy-v3 |
| Inputs | Verse Context batch JSON — wa-vcb-{batch_id}-extract-{date}.json |
| Outputs | Verse Context patch — wa-vcb-{batch_id}-patch-{date}.json |
| Claude AI role | Verse reading, relevance filtering, contextual grouping, anchor designation, patch production |
| Claude Code role | Batch JSON construction, patch application, group_code resolution, registry status management, integrity validation |
| Interaction model | Claude Code constructs batch → Claude AI classifies and produces patch → Claude Code applies patch and manages status |

---

## 0. Purpose and Scope

This document governs the Verse Context stage — the pipeline stage that must be completed before any Session B DataPrep or Analysis can begin for a registry.

**What Verse Context does:**
- Reads all verses for every active OWNER term programme-wide
- Filters each verse: does it engage the inner being through this term?
- Groups relevant verses by contextual meaning
- Designates anchor verses — the canonical citation and Session B analysis input per term
- Produces patches that Claude Code applies to populate `verse_context_group` and `verse_context`

**What Verse Context does NOT do:**
- Analyse the meaning of terms in depth — that is Session B Analysis
- Draw conclusions about the word being studied — that is Session B Analysis
- Produce cross-registry synthesis — that is Session D
- Assign evidential status to terms — that is Session B Analysis
- Process XREF terms — XREF verse_context records are derived by Claude Code from OWNER classifications

**Stage sequence:**
```
Phase 1 complete → Verse Context (this stage) → Session B DataPrep → Session B Analysis → Session B Extraction → Session D
```

| This document is self-standing. It requires two inputs: this document and the batch JSON export. It does not rely on session memory. |
|---|

---

## 1. The Two-System Model

| **System** | **Role** |
|---|---|
| Claude AI | Reads verse text. Applies the relevance filter. Produces contextual meaning descriptions. Groups verses. Designates anchors. Identifies dual-context. Produces the patch file. |
| Claude Code | Constructs batch JSON exports. Applies verse context patches. Resolves group_code to integer id. Updates registry verse_context_status. Validates consistency rules. Runs integrity checks. Does not assess verse relevance or produce contextual descriptions. |

| **⚠ Claude Code does not assess verse relevance, produce contextual meaning descriptions, or designate anchors. All classification is Claude AI's responsibility.** |
|---|

---

## 2. Database Tables

### 2.1 `verse_context_group`

| Field | Type | Notes |
|---|---|---|
| id | INTEGER PK | Used for all joins — never use group_code as join key |
| mti_term_id | INTEGER FK | → mti_terms.id — programme-wide term identifier |
| group_code | TEXT UNIQUE | `{mti_term_id}-{serial}` — human-readable, patch-constructable, never a join key |
| context_description | TEXT | Brief phrase — inner-being engagement of the term in this group |
| notes | TEXT | Optional qualification |
| delete_flagged | INTEGER | 0 = active; 1 = dissolved (no physical deletes) |

### 2.2 `verse_context`

| Field | Type | Notes |
|---|---|---|
| id | INTEGER PK | |
| verse_record_id | INTEGER FK | → wa_verse_records.id |
| mti_term_id | INTEGER FK | → mti_terms.id |
| group_id | INTEGER FK | → verse_context_group.id — NULL if is_relevant = 0 |
| is_anchor | INTEGER | 1 = anchor verse for its group |
| is_relevant | INTEGER | 0 = set aside; 1 = inner-being relevant |
| is_related | INTEGER | 1 = shares group meaning with anchor |
| notes | TEXT | Dual-context flags, borderline notes, revision reasons |
| delete_flagged | INTEGER | 0 = active; 1 = excluded (no physical deletes) |

**Uniqueness:** UNIQUE on (verse_record_id, mti_term_id, group_id). Same verse may appear under two groups (dual-context). Never twice in the same group.

### 2.3 Logical consistency rules

| Rule | Condition |
|---|---|
| R1 | is_relevant = 0 → group_id IS NULL, is_anchor = 0, is_related = 0 |
| R2 | is_anchor = 1 → is_relevant = 1, is_related = 0, group_id NOT NULL |
| R3 | is_related = 1 → is_relevant = 1, group_id references a group with at least one active anchor |
| R4 | Every term must have at least one active anchor before Session B may proceed |

---

## 3. The Governing Filter

Every verse is assessed against one question:

> **Does this verse, through the use of this term, say something about the inner being — understood as the non-physical, internal states, capacities, and expressions that constitute a person's invisible life: how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God?**

**If yes:** classify the contextual meaning (Section 6).
**If no:** set aside (is_relevant = 0). No further work for this verse.

### 3.1 What passes the filter

A verse passes when the term's use engages one or more of:
- An internal state — emotion, feeling, disposition, attitude
- A capacity of the inner life — will, intention, thought, belief, desire
- A relational orientation — how the person is oriented toward God, others, or themselves inwardly
- A moral or character quality of the whole person
- A spiritual characteristic — responsiveness to God, spiritual condition, worship disposition

### 3.2 What does not pass the filter

- Purely physical use — the term refers to a body part, physical process, or material object with no inner-being engagement
- Purely social or narrative — external conduct or events with no window into the inner life
- Purely positional or geographical — locating something in space or time

| **⚠ Apply the filter to the term's specific use in this verse — not to the verse's general theme.** |
|---|

### 3.3 Borderline cases

Where the filter decision is genuinely uncertain: retain (is_relevant = 1) and record the uncertainty in the notes field. The cost of a missed inclusion is higher than the cost of retaining an uncertain verse.

---

## 4. Anchor Verses

An anchor verse is the programme's **canonical reference verse** for a specific contextual meaning group of a term.

**Dual purpose:**
1. **Efficiency instrument** — Session B Analysis reads anchor verses, not the full corpus
2. **Citation instrument** — anchor verses appear in Session B narratives and Session D synthesis as the evidential foundation for claims about the term

**Selection criteria:**
- Makes the contextual meaning evident without requiring surrounding context
- The term's inner-being function is unambiguous in the verse
- Stands alone as evidence — does not depend on interpretation of adjacent passages

**Minimum requirement:** every term must have at least one active anchor across all its groups. A term with no anchor cannot proceed to Session B.

**Quantity:** 1–2 anchors per group. Where two are designated, they represent distinct aspects of the group's meaning.

---

## 5. Claude Code — Batch JSON Construction

### 5.1 Batch construction criteria

- **OWNER terms only** — `wa_term_inventory.term_owner_type = 'OWNER'`
- **Active terms only** — `mti_terms.status IN ('extracted', 'extracted_thin')`
- **Terms with verses only** — `COUNT(wa_verse_records WHERE delete_flagged = 0) > 0`
- **Target size** — accumulate terms until unclassified verse count reaches 2,000–2,500
- **Never split a term** across batches — all verses for a term appear in one batch
- **Priority order** — terms with no existing `verse_context` records first, ordered by `mti_terms.owning_registry_fk` ascending
- **Batch ID** — sequential: VCB-001, VCB-002 etc.

### 5.2 Batch JSON structure

```json
{
  "batch_id": "VCB-{nnn}",
  "produced_date": "{yyyy-mm-dd}",
  "produced_by": "Claude Code — VerseContext batch export",
  "total_verse_count": 0,
  "total_term_count": 0,
  "verse_context_summary": {
    "total_verses": 0,
    "classified_verses": 0,
    "unclassified_verses": 0,
    "set_aside_verses": 0,
    "anchor_verses": 0
  },
  "terms": [
    {
      "mti_term_id": 0,
      "strongs_number": "{H/Gnnnn}",
      "transliteration": "{text}",
      "gloss": "{text}",
      "language": "{Hebrew or Greek}",
      "mti_status": "{extracted or extracted_thin}",
      "term_owner_type": "OWNER",
      "owning_registry_id": 0,
      "owning_registry_word": "{word}",
      "registry_verse_context_status": "{NULL or In Progress or Complete}",
      "term_classification_complete": false,
      "total_verses": 0,
      "classified_count": 0,
      "unclassified_count": 0,
      "group_count": 0,
      "existing_groups": [
        {
          "id": 0,
          "group_code": "{mti_term_id}-{serial}",
          "context_description": "{text}",
          "notes": null,
          "delete_flagged": 0,
          "anchor_count": 0,
          "related_count": 0
        }
      ],
      "verses": [
        {
          "verse_record_id": 0,
          "reference": "{Book Ch:V}",
          "verse_text": "{text}",
          "target_word": "{text}",
          "span_strong_match": 1,
          "verse_delete_flagged": 0,
          "verse_context": {
            "id": 0,
            "group_id": 0,
            "group_code": "{mti_term_id}-{serial}",
            "is_anchor": 0,
            "is_relevant": 0,
            "is_related": 0,
            "notes": null,
            "delete_flagged": 0
          }
        }
      ]
    }
  ]
}
```

**Notes on verse_context field:** NULL for the entire object if no verse_context record exists for this verse_record_id + mti_term_id combination. Include ALL verse_context records regardless of delete_flagged — Claude AI needs full history for revision decisions.

Include ALL verses for each term regardless of existing classification — classified and unclassified. Include ALL existing groups regardless of delete_flagged — Claude AI needs prior dissolved groups visible.

---

## 6. Claude AI — Classification Workflow

For each term in the batch, complete this sequence in full before moving to the next term.

### 6.1 Read all verses

Read every verse in the term's verse array. Do not skip. Do not classify before reading. Note the existing_groups and any pre-classified verses before beginning.

### 6.2 Apply the relevance filter

For each verse, apply the governing filter (Section 3). If an existing verse_context record is present — review it but do not assume it is correct. You may revise prior classifications.

Mark each verse:
- **Relevant** (is_relevant = 1) — passes the filter
- **Set aside** (is_relevant = 0) — does not pass the filter

### 6.3 Group relevant verses by contextual meaning

Ask for each relevant verse: **does this verse say the same thing about the inner being through this term as verses already grouped?**

If yes → same group.
If no → new group or existing group that fits better.

Check existing_groups first — assign to an existing group if appropriate before creating a new one.

**context_description** — a brief phrase (one sentence maximum) capturing what the group says about the inner being. Grounded in what the verses show. Sufficient to distinguish this group from others for this term.

Examples of appropriate descriptions:
- *Term names an inward state of distress under divine discipline*
- *Term describes the orientation of the will toward God*
- *Term identifies the seat of moral decision in the person*

### 6.4 Designate anchors

For each group: designate 1–2 anchor verses meeting the criteria in Section 4.

If revising a prior classification: a verse previously marked is_related may be promoted to is_anchor. A verse previously marked is_anchor may be demoted if a better anchor is found — but ensure the group retains at least one anchor.

### 6.5 Dual-context verses

Where a verse plainly operates at two distinct inner-being levels through the same term — assign to two groups. This is the exception. Only when two distinct engagements are plainly evident. Record reason in notes on both rows.

### 6.6 Per-term classification summary

Before moving to the next term, state:

```
Term: {strongs_number} ({transliteration}) — {gloss}
Total verses: {n} | Relevant: {n} | Set aside: {n}
Groups: {n}
  Group {group_code}: "{context_description}" — Anchors: {references} | Related: {n}
Revisions to prior classifications: {n} (if any — describe)
Dual-context: {n} (if any)
Borderline retained: {n} (if any)
```

---

## 7. Patch Production

### 7.1 Patch types

Three patch types govern all Verse Context database operations:

| Type | Purpose | When to use |
|---|---|---|
| VERSECONTEXT | Full batch — all terms in batch | After completing all terms in a batch |
| VCGROUP | Targeted group update | When revising a single group outside a batch |
| VCVERSE | Targeted verse update | When a single verse changes (added, removed, reclassified) |

### 7.2 VERSECONTEXT patch — structure

Produced once per batch, after all terms are complete.

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1",
    "batch_id": "VCB-{nnn}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-VerseContext-Instruction-v1.0",
    "session_b_status": null,
    "description": "Verse context classification — batch VCB-{nnn}, {n} terms, {n} verses"
  },
  "operations": [],
  "_patch_summary": {
    "total_operations": 0,
    "group_inserts": 0,
    "group_updates": 0,
    "verse_context_inserts": 0,
    "verse_context_updates": 0,
    "relevant_verses": 0,
    "set_aside_verses": 0,
    "anchor_verses": 0,
    "dual_context_verses": 0,
    "revisions_to_prior": 0
  }
}
```

Note: `session_b_status` is null in Verse Context patches — status is managed via `verse_context_status`, not `session_b_status`. The patch applicator must accept null here without rejection.

### 7.3 Operation types

#### Insert new group

```json
{
  "op_id": "OP-001",
  "operation": "insert",
  "table": "verse_context_group",
  "record": {
    "mti_term_id": 142,
    "group_code": "142-001",
    "context_description": "{brief phrase}",
    "notes": null,
    "delete_flagged": 0
  },
  "description": "New group for {strongs_number}: {context_description}"
}
```

Claude Code: after inserting, capture `last_insert_rowid()` as the integer id for this group. Use this integer in all subsequent verse_context inserts referencing this group.

#### Update existing group

```json
{
  "op_id": "OP-002",
  "operation": "update",
  "table": "verse_context_group",
  "match": { "id": 47 },
  "set": {
    "context_description": "{revised phrase}",
    "notes": "{reason for revision}",
    "delete_flagged": 0
  },
  "description": "Revised context description for group {group_code}"
}
```

Only fields being changed appear in `set`. `delete_flagged = 0` reinstates a dissolved group. `delete_flagged = 1` dissolves a group. When dissolving: check that affected anchor verses are reassigned or that the term retains at least one anchor from another group.

#### Insert new verse_context record

**Anchor:**
```json
{
  "op_id": "OP-003",
  "operation": "insert",
  "table": "verse_context",
  "record": {
    "verse_record_id": 4821,
    "mti_term_id": 142,
    "group_id": "142-001",
    "is_anchor": 1,
    "is_relevant": 1,
    "is_related": 0,
    "notes": null,
    "delete_flagged": 0
  },
  "description": "{Book Ch:V} — anchor, group 142-001: {context_description}"
}
```

**Related:**
```json
{
  "op_id": "OP-004",
  "operation": "insert",
  "table": "verse_context",
  "record": {
    "verse_record_id": 4822,
    "mti_term_id": 142,
    "group_id": "142-001",
    "is_anchor": 0,
    "is_relevant": 1,
    "is_related": 1,
    "notes": null,
    "delete_flagged": 0
  },
  "description": "{Book Ch:V} — related, group 142-001"
}
```

**Set aside:**
```json
{
  "op_id": "OP-005",
  "operation": "insert",
  "table": "verse_context",
  "record": {
    "verse_record_id": 4823,
    "mti_term_id": 142,
    "group_id": null,
    "is_anchor": 0,
    "is_relevant": 0,
    "is_related": 0,
    "notes": null,
    "delete_flagged": 0
  },
  "description": "{Book Ch:V} — set aside, no inner-being engagement for {strongs_number}"
}
```

Note: `group_id` in operations references group_code strings (e.g. `"142-001"`) for new groups inserted in the same patch. Claude Code resolves these to integer ids at apply time. For existing groups from prior patches, use the integer id directly.

#### Update existing verse_context record

```json
{
  "op_id": "OP-006",
  "operation": "update",
  "table": "verse_context",
  "match": { "id": 892 },
  "set": {
    "group_id": 47,
    "is_anchor": 1,
    "is_relevant": 1,
    "is_related": 0,
    "notes": "{reason for revision}",
    "delete_flagged": 0
  },
  "description": "{Book Ch:V} — reclassified: promoted to anchor, group {group_code}"
}
```

All corrections are UPDATE operations. Never delete and reinsert. `delete_flagged = 1` flags a record out of the active set without physical deletion.

### 7.4 Operation ordering within patch

For each term:
1. All `verse_context_group` inserts for the term (new groups)
2. All `verse_context_group` updates for the term (revisions to existing groups)
3. All `verse_context` inserts — anchors first, then related, then set-aside
4. All `verse_context` updates — revisions to prior classifications last

Across terms: process terms in the order they appear in the batch JSON.

### 7.5 Anchor integrity rule

Any operation that removes, dissolves, or reclassifies the last anchor for a term must be accompanied in the same patch by a promotion operation ensuring the term retains at least one active anchor. Claude AI is responsible for this. Claude Code validates after application.

### 7.6 Pre-submission validation

Before submitting any patch, verify:
- Every verse in the batch has exactly one verse_context row, except dual-context verses (exactly two)
- Every new group has at least one anchor insert
- Every is_related = 1 row references a group that has an anchor
- Every is_relevant = 0 row has group_id = null
- No row has is_anchor = 1 and is_related = 1 simultaneously
- _patch_summary counts are accurate

### 7.7 Handoff to Claude Code

```
PATCH SUBMISSION TO CLAUDE CODE

Patch file: wa-vcb-{batch_id}-patch-{date}.json
Patch type: VERSECONTEXT

Action required:
  1. Apply patch — insert/update verse_context_group and verse_context records
  2. Resolve group_code strings to integer ids for new groups in this patch
  3. Validate consistency rules R1–R4 after application
  4. Run integrity validation (Section 5.5 of setup instruction)
  5. For each registry whose OWNER terms appear in this batch:
     - Run completion check (Section 5.2 of setup instruction)
     - Advance verse_context_status to 'Complete' where all conditions met
  6. Report: records inserted/updated, registries advanced to Complete, any integrity violations
```

---

## 8. VCGROUP Patch — Targeted Group Update

Use when revising a single `verse_context_group` record outside a full batch run.

### 8.1 Input required from Claude Code

Before producing a VCGROUP patch, Claude Code must provide:

```json
{
  "group": {
    "id": 0,
    "mti_term_id": 0,
    "group_code": "{text}",
    "context_description": "{current text}",
    "notes": null,
    "delete_flagged": 0,
    "anchor_count": 0,
    "related_count": 0,
    "anchor_verses": [
      { "verse_record_id": 0, "reference": "{Book Ch:V}", "verse_text": "{text}" }
    ]
  }
}
```

### 8.2 Patch structure

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-VCGROUP{group_id}-V1",
    "group_id": 0,
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-VerseContext-Instruction-v1.0",
    "session_b_status": null,
    "description": "Targeted group update — group {group_code}"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "update",
      "table": "verse_context_group",
      "match": { "id": 0 },
      "set": {
        "context_description": "{revised text}",
        "notes": "{if applicable}",
        "delete_flagged": 0
      },
      "description": "Revised group {group_code}: {reason}"
    }
  ],
  "_patch_summary": {
    "total_operations": 1,
    "group_updates": 1
  }
}
```

**Reinstatement note:** If `delete_flagged` is reset from 1 to 0 (reinstating a dissolved group), the verse_context rows flagged when the group was dissolved are NOT automatically reinstated. A separate VERSECONTEXT or VCVERSE patch is required to reinstate verses.

---

## 9. VCVERSE Patch — Targeted Verse Update

Use when a single verse changes state: new verse added, verse removed, or reclassification required.

### 9.1 Input required from Claude Code

```json
{
  "verse": {
    "verse_record_id": 0,
    "reference": "{Book Ch:V}",
    "verse_text": "{current text}",
    "target_word": "{text}",
    "span_strong_match": 1,
    "verse_delete_flagged": 0,
    "mti_term_id": 0
  },
  "existing_verse_context": {
    "id": 0,
    "group_id": 0,
    "group_code": "{text}",
    "is_anchor": 0,
    "is_relevant": 0,
    "is_related": 0,
    "notes": null,
    "delete_flagged": 0
  },
  "available_groups": [
    {
      "id": 0,
      "group_code": "{text}",
      "context_description": "{text}",
      "anchor_count": 0,
      "delete_flagged": 0
    }
  ]
}
```

`existing_verse_context` is null if no record exists yet.

### 9.2 Three scenarios

**Scenario A — New verse, first-time classification:**
Use `insert` operation. If the verse fits an existing group, reference its integer id. If a new group is needed, insert the group first.

**Scenario B — Verse removed (`wa_verse_records.delete_flagged` set to 1):**
```json
{
  "op_id": "OP-001",
  "operation": "update",
  "table": "verse_context",
  "match": { "id": 0 },
  "set": { "delete_flagged": 1 },
  "description": "{Book Ch:V} — verse removed from active set, flagging verse_context record"
}
```

If the verse was an anchor: include a second operation promoting another related verse in the same group to anchor status. If no related verses remain, include a note flagging that the group has no anchor — researcher decision required.

**Scenario C — Reclassify existing verse:**
Use `update` operation on the existing verse_context id. Include notes explaining the reason for reclassification.

### 9.3 Patch naming

`PATCH-{YYYYMMDD}-VCVERSE{verse_record_id}-V1`

---

## 10. Researcher Compliance Rules

| **⚠ Do not make assumptions or guesses. When uncertain about whether a verse passes the relevance filter, retain the verse, note the uncertainty, and proceed. Do not stop the session for borderline filter decisions. Batch uncertainty questions together at the end of each term's classification.** |
|---|

Additional rules:
- Do not develop analytical conclusions about terms during Verse Context — that is Session B
- Do not draw cross-registry connections — that is Session D
- Do not assign evidential status — that is Session B
- Context descriptions must be grounded in what the verses show — not in prior knowledge of the term's theological significance
- Dual-context is rare — only when two distinct inner-being engagements are plainly evident. Do not use it to resolve interpretive difficulty
- All corrections are UPDATE operations. Never produce delete + reinsert
- The anchor integrity rule is absolute — a term must retain at least one active anchor at all times

---

## Annexure A — Startup Summary Template

```
Verse Context v1.0 startup complete.
Batch: {batch_id}
Terms: {n}
Total verses: {n} | Unclassified: {n} | Previously classified: {n}

Term inventory:
  {strongs_number} ({transliteration}) — {gloss} — {n} verses — OWNER for {owning_word}
    Existing groups: {n} | Classified verses: {n} | Unclassified: {n}
  [repeat for each term]

Ready to proceed.
```

---

## Annexure B — Per-Term Classification Summary Template

```
Term: {strongs_number} ({transliteration}) — {gloss}
mti_term_id: {integer}
Total verses: {n} | Relevant: {n} | Set aside: {n}

Groups:
  {group_code}: "{context_description}"
    Anchors: {verse reference(s)}
    Related: {n} verses
  [repeat for all groups]

Revisions to prior classifications: {describe if any}
Dual-context verses: {n} [describe if any]
Borderline retained: {list references if any}
Anchor integrity: confirmed — {n} active anchors across {n} groups

Ready for patch.
```

---

## Annexure C — Verse Context Patch Template (VERSECONTEXT)

File naming: `wa-vcb-{batch_id}-patch-{YYYYMMDD}.json`

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1",
    "batch_id": "VCB-{nnn}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-VerseContext-Instruction-v1.0",
    "session_b_status": null,
    "description": "Verse context classification — batch VCB-{nnn}, {n} terms, {n} verses"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "insert",
      "table": "verse_context_group",
      "record": {
        "mti_term_id": 0,
        "group_code": "{mti_term_id}-001",
        "context_description": "{brief phrase}",
        "notes": null,
        "delete_flagged": 0
      },
      "description": "Group 1 for {strongs_number}: {context_description}"
    },
    {
      "op_id": "OP-002",
      "operation": "insert",
      "table": "verse_context",
      "record": {
        "verse_record_id": 0,
        "mti_term_id": 0,
        "group_id": "{mti_term_id}-001",
        "is_anchor": 1,
        "is_relevant": 1,
        "is_related": 0,
        "notes": null,
        "delete_flagged": 0
      },
      "description": "{Book Ch:V} — anchor, group {mti_term_id}-001"
    },
    {
      "op_id": "OP-003",
      "operation": "insert",
      "table": "verse_context",
      "record": {
        "verse_record_id": 0,
        "mti_term_id": 0,
        "group_id": "{mti_term_id}-001",
        "is_anchor": 0,
        "is_relevant": 1,
        "is_related": 1,
        "notes": null,
        "delete_flagged": 0
      },
      "description": "{Book Ch:V} — related, group {mti_term_id}-001"
    },
    {
      "op_id": "OP-004",
      "operation": "insert",
      "table": "verse_context",
      "record": {
        "verse_record_id": 0,
        "mti_term_id": 0,
        "group_id": null,
        "is_anchor": 0,
        "is_relevant": 0,
        "is_related": 0,
        "notes": null,
        "delete_flagged": 0
      },
      "description": "{Book Ch:V} — set aside, no inner-being engagement"
    }
  ],
  "_patch_summary": {
    "total_operations": 4,
    "group_inserts": 1,
    "group_updates": 0,
    "verse_context_inserts": 3,
    "verse_context_updates": 0,
    "relevant_verses": 2,
    "set_aside_verses": 1,
    "anchor_verses": 1,
    "dual_context_verses": 0,
    "revisions_to_prior": 0
  }
}
```

---

*WA-VerseContext-Instruction-v1-20260329 | Integrated Claude AI + Claude Code | Governing instruction for Verse Context stage*
