# WA-VerseContext-ImpactStudy-v3-20260329

**Project:** Framework B — Soul Word Analysis Programme
**Date:** 2026-03-29
**Version:** 3 — full rewrite incorporating all researcher decisions from review session
**Supersedes:** WA-VerseContext-ImpactStudy-v2-20260329.md
**Purpose:** Definitive impact assessment governing all document updates, schema migrations, and instruction changes required to implement the Verse Context stage and the pool-based simultaneous Session B architecture.
**Produced by:** Claude AI
**Source documents:** WA-Reference-v5.2; WA-Registry-Management-Guide-v5.3; WA-SessionB-DataPrep-Instruction-v5.1; WA-SessionB-Analysis-Instruction-v5.1; WA-SessionB-Extraction-Instruction-v5.2; WA-SessionB-ClaudeCode-Instructions; database_schema_20260329.json; patch_specification v1.1; wa-programme-status-report-20260328.md

---

## 1. What Is Being Introduced

### 1.1 Two new database tables

**`verse_context_group`** — one row per contextual meaning group per term. Group description lives here once. Keyed to `mti_terms.id` — programme-wide, not registry-specific.

**`verse_context`** — one row per verse per term. Carries the relevance filter result, group assignment, anchor/related/set-aside flags, and deletion state.

### 1.2 The Verse Context stage

A new pipeline stage — **Verse Context** — sitting between Phase 1 audit completion and Session B DataPrep. It classifies all active OWNER term verses against a governing inner-being relevance filter, groups relevant verses by contextual meaning, and designates anchor verses as the canonical citation and primary Session B analysis input per term.

Verse Context is a **term-level** operation, not a word-level or cluster-level operation. It runs across all OWNER terms programme-wide in verse-count-managed batches. A batch may span multiple words and multiple clusters.

OWNER terms with zero verse records are excluded from Verse Context by definition.

### 1.3 The anchor verse — formal definition

An anchor verse is the programme's canonical reference verse for a specific contextual meaning group of a term. It is the verse that most clearly and economically demonstrates the inner-being engagement of the term in that contextual group. Anchor verses serve two purposes:

1. **Efficiency instrument** — Session B reads anchor verses rather than the full verse corpus
2. **Citation instrument** — anchor verses appear in the Session B narrative and Session D synthesis as the evidential foundation for claims about the term

Every term must have at least one active anchor across all its groups before Session B analysis may proceed. A term with no anchor is not ready for analysis.

### 1.4 New `word_registry` field — `verse_context_status`

A separate field on `word_registry` tracks Verse Context completion independently of `session_b_status`. This separates concerns cleanly — Verse Context operates at term level across all words simultaneously, while `session_b_status` tracks the word-level analytical pipeline.

Valid values: `NULL` (not started) / `In Progress` / `Complete`

`session_b_status` is unchanged. The DataPrep gate now checks `verse_context_status = Complete` before proceeding.

### 1.5 Three new patch types

- **VERSECONTEXT** — full batch classification run (multiple OWNER terms)
- **VCGROUP** — targeted update to a single `verse_context_group` record
- **VCVERSE** — targeted update to a single `verse_context` record

### 1.6 The XREF architecture — programme-wide significance

This section captures the fundamental change already implemented in the database that underpins the entire Verse Context design.

**The master term index (`mti_terms`)** holds one record per Strong's number — programme-wide, registry-independent. This is the authoritative term identity.

**`wa_term_inventory`** holds multiple records per Strong's number — one per registry that uses the term. Each record is classified as OWNER (the primary analytical home for this term) or XREF (a cross-reference copy in another registry).

**OWNER verses** — active, included in all queries and exports. These are the verses Verse Context processes.

**XREF verses** — delete_flagged. Excluded from all queries and exports. XREF term records remain active for cross-registry linkage queries only.

**The consequence for Verse Context:** A term's verse context classification is done once, by the OWNER registry. It is valid programme-wide. When a word's Session B analysis encounters an XREF term, it does not re-read that term's verses — it reads the contextual meaning groups and anchor verses already classified under the OWNER registry.

**The consequence for Session B analysis:** Words that share terms via XREF relationships can be analysed simultaneously. The shared terms' verse context is already classified. The analyst sees the full cross-word picture without re-reading shared verses. This eliminates the need for most Session D pointer machinery for shared terms.

**Current XREF scale:** 1,470 XREF term records across 181 registries. The sharing pools in Section 3 show the structure of these relationships.

### 1.7 Two-stage programme sequence

**Stage 1 — Verse Context sweep (immediate priority)**
Run Verse Context across all OWNER terms programme-wide. Term-based batches, 2,000–2,500 verses per session. No word or cluster ordering — work through all 5,518 OWNER terms until every term has verse_context records. This stage is complete when all OWNER terms (with verses) have classifications.

**Stage 2 — Pool/cluster-based Session B analysis**
Once Verse Context is complete, analyse words in pool/cluster batches. Words sharing XREF terms are analysed simultaneously — their shared terms already have verse context from Stage 1. The pool structure (Section 3) governs processing sequence.

### 1.8 Re-extraction trigger

When audit_word is re-run for any registry, Claude Code checks for OWNER term verse records with no corresponding `verse_context` entry. If found, those specific terms are flagged for Verse Context revision and the registry's `verse_context_status` is set to `In Progress`. This is a targeted check — not a full programme reset.

When any verse record is delete_flagged, Claude Code cascades the flag to corresponding `verse_context` rows for the same `mti_term_id`.

### 1.9 Integrity validation

After every patch application cycle, Claude Code validates that any term with `mti_terms.status` of `delete` or `excluded` has all its `verse_context` rows flagged (`delete_flagged = 1`).

---

## 2. Database Impact

### 2.1 Schema state — confirmed from database_schema_20260329.json

| Item | Current state | Required action |
|---|---|---|
| `wa_verse_records.mti_term_id` | Present — FK to `mti_terms.id` | None |
| `verse_context_group` table | Not present | Create — M18 |
| `verse_context` table | Not present | Create — M18 |
| `word_registry.source_category` | Present — rename pending | Rename to `dimensions` — M17 |
| `word_registry.anchor_verses` | Present — superseded | Remove — M17 |
| `word_registry.verse_context_status` | Not present | Add — M18 |
| Schema version | 3.7.0 (M16 complete) | Advance to 3.8.0 after M17+M18 |

### 2.2 Migration M17 — field corrections on `word_registry`

Two actions on the same table, executed together as M17:

**Action 1 — Rename `source_category` to `dimensions`**

SQLite does not support RENAME COLUMN directly in versions below 3.25.0. Claude Code must check SQLite version first:

```sql
SELECT sqlite_version();
```

If 3.25.0 or higher:
```sql
ALTER TABLE word_registry RENAME COLUMN source_category TO dimensions;
```

If below 3.25.0 — table recreation required. Claude Code handles via migrate.py using the standard table-copy pattern.

**Validation:**
```sql
SELECT dimensions FROM word_registry LIMIT 1;
-- Must return without error
SELECT source_category FROM word_registry LIMIT 1;
-- Must return error (column no longer exists)
```

**Action 2 — Remove `anchor_verses`**

`anchor_verses` is superseded by the `verse_context` anchor mechanism. It is an informal text field — no FK dependencies.

SQLite DROP COLUMN requires 3.35.0+. Check version. If supported:
```sql
ALTER TABLE word_registry DROP COLUMN anchor_verses;
```

If not supported — retain the column but deprecate it: update all instruction documents to ignore it, and add a note to the schema record.

**Validation:**
```sql
SELECT anchor_verses FROM word_registry LIMIT 1;
-- Must return error if dropped, or column must be confirmed deprecated
```

**All existing `source_category` values** are retained under the new `dimensions` column name. No data migration required — only the column name changes.

### 2.3 Migration M18 — new tables and new field

**Action 1 — Create `verse_context_group`**

```sql
CREATE TABLE IF NOT EXISTS verse_context_group (
  id          INTEGER PRIMARY KEY,
  mti_term_id INTEGER NOT NULL REFERENCES mti_terms(id),
  group_code  TEXT NOT NULL UNIQUE,
  context_description TEXT NOT NULL,
  notes       TEXT DEFAULT NULL,
  delete_flagged INTEGER DEFAULT 0
);
```

Field notes:
- `group_code` format: `{mti_term_id}-{3-digit-serial}` e.g. `142-001`. Human-readable. Never used as join key.
- `delete_flagged = 1` dissolves the group without physical deletion — programme-wide policy.

**Action 2 — Create `verse_context`**

```sql
CREATE TABLE IF NOT EXISTS verse_context (
  id              INTEGER PRIMARY KEY,
  verse_record_id INTEGER NOT NULL REFERENCES wa_verse_records(id),
  mti_term_id     INTEGER NOT NULL REFERENCES mti_terms(id),
  group_id        INTEGER REFERENCES verse_context_group(id),
  is_anchor       INTEGER NOT NULL DEFAULT 0,
  is_relevant     INTEGER NOT NULL DEFAULT 0,
  is_related      INTEGER NOT NULL DEFAULT 0,
  notes           TEXT DEFAULT NULL,
  delete_flagged  INTEGER DEFAULT 0,
  UNIQUE (verse_record_id, mti_term_id, group_id)
);
```

Uniqueness constraint: same verse may appear under two different groups for the same term (dual-context) but not twice in the same group.

**Logical consistency rules — enforced by Claude AI, validated by Claude Code:**

| Rule | Condition |
|---|---|
| R1 | is_relevant = 0 → group_id IS NULL, is_anchor = 0, is_related = 0 |
| R2 | is_anchor = 1 → is_relevant = 1, is_related = 0, group_id NOT NULL |
| R3 | is_related = 1 → is_relevant = 1, group_id references a group with at least one is_anchor = 1 row |
| R4 | Every term must have at least one active (delete_flagged = 0, is_anchor = 1) row before Session B may proceed |

**Action 3 — Add `verse_context_status` to `word_registry`**

```sql
ALTER TABLE word_registry ADD COLUMN verse_context_status TEXT DEFAULT NULL;
```

Valid values: NULL / `In Progress` / `Complete`

**Validation for M18:**
```sql
SELECT name FROM sqlite_master WHERE type='table'
  AND name IN ('verse_context_group','verse_context');
-- Expected: both rows returned

SELECT verse_context_status FROM word_registry LIMIT 1;
-- Expected: returns NULL (default)
```

### 2.4 Schema version update

After M17 and M18 are confirmed:
```sql
UPDATE schema_version SET version_code = '3.8.0',
  applied_at = date('now'),
  migration_history = migration_history || ', M17, M18';
```

### 2.5 Programme-wide data operations — status resets

After M17 and M18 are confirmed, execute the following resets. **Do not execute until migrations are confirmed.**

**Operation 1 — Set `verse_context_status` for all registries**

All 181 active registries begin at `In Progress` — not NULL, because the programme already has OWNER term data ready for processing:

```sql
UPDATE word_registry
SET verse_context_status = 'In Progress'
WHERE phase1_status = 'Complete'
  AND phase1_term_count > 0;
-- Expected: approximately 177 registries
```

Zero-term registries and excluded registries remain NULL.

**Operation 2 — Reset 35 Analysis Complete registries**

These registries completed Session B under the old word-by-word workflow. They must be reset for Verse Context and re-analysis in pool context. Their existing analytical documents are parked — not deleted — but superseded.

```sql
UPDATE word_registry
SET session_b_status = 'Verse Context Reset',
    verse_context_status = 'In Progress'
WHERE session_b_status = 'Analysis Complete';
-- Expected: 35 registries
```

`Verse Context Reset` is a new `session_b_status` value indicating: prior Session B work exists but has been superseded by the pool-based re-analysis requirement. It is distinct from NULL (never started) and from `In Progress` (currently being processed).

**Operation 3 — Verify 33 NULL-status registries**

```sql
SELECT no, word, phase1_status, phase1_term_count
FROM word_registry
WHERE session_b_status IS NULL
ORDER BY no;
```

Classify each: set `verse_context_status = 'In Progress'` for those with Phase 1 complete and terms present. Document any that cannot be classified.

**Operation 4 — Validate XREF verse_context exclusion**

After Verse Context records begin being created, this integrity check must run after every patch cycle:

```sql
SELECT mt.strongs_number, mt.status, COUNT(vc.id) as vc_active
FROM mti_terms mt
JOIN verse_context vc ON vc.mti_term_id = mt.id
WHERE mt.status IN ('delete','excluded')
  AND vc.delete_flagged = 0
GROUP BY mt.id;
-- Expected: zero rows. Any result is an integrity violation.
```

---

## 3. Sharing Pools — Processing Sequence for Stage 2

The pools identified in the programme status report (Section 5) are used as the processing sequence for Stage 2. Clusters remain the organisational entity in the database. Pools define the order of work.

### 3.1 Pool structure summary

| Pool | Words | Shared terms | Processing unit |
|---|---|---|---|
| Not-shared | 17 words (term_sharing_ratio = 0) | 0 | Independent — any order |
| Unconnected | 47 words (connected below 15-term threshold) | Minimal | Near-independent — group by cluster |
| Pool 2 | 11 words (suffering/fear) | Internal only | Single simultaneous batch |
| Pool 3 | envy, jealousy, zeal | qana root | Single session |
| Pool 4 | compassion, mercy | chesed/racham | Single session |
| Pool 5 | justice, righteousness | tsedeq | Single session |
| Pool 6 | shame, contempt | dishonour vocab | Single session |
| Pool 7 | surrender, flesh | submission vocab | Single session |
| Pool 8 | consecration, holiness | qodesh | Single session |
| Pool 1 sub-pools | See 3.2 | Complex | Sequential sub-pool batches |

### 3.2 Pool 1 sub-pool processing sequence

Ordered by internal bond strength — simplest first:

| Order | Sub-pool | Words | Shared terms |
|---|---|---|---|
| 1 | Anger pair | anger, wrath | 51 — strongest pair |
| 2 | Love pair | kindness, love | 33 |
| 3 | Heart-spirit pair | heart, spirit | 41 |
| 4 | Wisdom pair | goodness, meditation | 30 |
| 5 | Power axis | courage, strength, power, authority, dominion | ~25 avg |
| 6 | Volitional Core | desire, faith, guilt, hope, purpose, thought, trust, will, pray | Most complex — 9 words |
| 7 | Isolates by gravitational attractor | 41 words grouped by closest sub-pool | After their attractor sub-pool |

### 3.3 Implications for Session B analysis unit

Session B Analysis is now a **pool/cluster batch** operation, not a word-by-word operation. A Session B analysis session takes:
- A set of words (the pool/sub-pool/cluster batch)
- All their OWNER term anchor verses grouped by contextual meaning
- All their XREF term contextual profiles from the OWNER registries
- Produces one word narrative per word in the batch, coherent with each other

---

## 4. New Session B Input JSON — Pool Dataset

The existing `full` word export (`wa-{nnn}-{word}-extract-{date}.json`) remains in use for Phase 1 audit and Verse Context batch construction. It is no longer the primary input for Session B Analysis.

### 4.1 New JSON type — pool analysis dataset

A new export type is required for Session B Analysis:

**File naming:** `wa-pool-{pool_id}-analysis-{date}.json`

Where `pool_id` identifies the pool/sub-pool/cluster batch (e.g. `pool2`, `c01-volitional`, `c07-anger-pair`).

### 4.2 Content of the pool analysis dataset

**Meta block:** batch identifier, word list, cluster assignments, date, verse_context completion status per word

**Per word block** (one per word in the batch):
- Registry meta: registry number, word, phase1_term_count, phase1_verse_count
- Term inventory: all active OWNER terms with mti_status, evidential_status, phase2 flags
- For each OWNER term with verse_context:
  - verse_context_groups: group_code, context_description, anchor verse count, related verse count, set-aside count
  - Anchor verses: full verse text, reference, target_word, span_strong_match — grouped under their context group
- XREF terms (informational):
  - strongs_number, transliteration, gloss, mti_status
  - OWNER registry: registry_id, word
  - OWNER's verse_context_groups for this term: group_code, context_description, anchor verse references (no full text — OWNER registry owns the verses)
  - Note: full anchor verse text for XREF terms is available by querying the OWNER registry's pool dataset if needed

**Cross-word map block:**
- For each shared term appearing in 2+ words in this batch: which words share it, which registry owns it, how many contextual groups it has
- This is the primary inter-word relationship view — visible in the analysis session without querying other registries

### 4.3 What this replaces

The pool analysis dataset replaces the word-by-word `full` export as the Session B Analysis input. It makes the cross-word picture visible within a single session. It eliminates the need for most Session D pointer production for shared terms — those relationships are directly visible in the analysis.

---

## 5. Session D — Revised Boundary

### 5.1 What moves into Session B

With pool-based simultaneous Session B, the following previously required Session D work is now done in Session B:

- Cross-word observations for terms shared within a pool
- Inter-word relationship characterisation within a pool
- Evidential comparison between words sharing the same term

### 5.2 What remains for Session D

Session D shifts to genuinely synthesis-level questions:

- **Cross-pool interoperability** — how pools relate to each other conceptually (e.g. how the volitional core interacts with the suffering/fear pool)
- **Whole-programme patterns** — patterns visible only when all 212 words are considered together
- **Conceptual dynamics** — how words influence and condition each other at an experiential level (e.g. peace increases, worries diminish — what does the biblical text say about that dynamic?)
- **Conceptual Word Register integration** — connecting the analytical findings to modern inner-life concepts that have no direct biblical lexical equivalent

### 5.3 Session D pointers — revised role

Many current Session D pointers will no longer be produced as such — the observations they capture will be made directly in pool-based Session B and included in the word narratives. Genuine Session D pointers are those capturing cross-pool or whole-programme observations that cannot be made within any single pool analysis.

The Session D orientation document must be updated to reflect this boundary shift. This update is deferred until Stage 2 analysis begins and the practical shape of the new boundary becomes visible.

### 5.4 Session B output for Session D

The Session B output JSON (`wa-{nnn}-{word}-json-{date}.json`) currently includes a `session_d_pointers` array. This array is retained but its scope narrows: only observations that genuinely require cross-pool or whole-programme synthesis belong here. Intra-pool cross-word observations are captured in the narrative, not in the pointers array.

---

## 6. Document Status — Retirement, Update, New

### 6.1 Retired documents

| Document | Reason |
|---|---|
| WA-SessionB-DataPrep-Instruction-v5.1 (verse reading sections) | DataPrep no longer involves verse reading — Verse Context precedes it. DataPrep retains term classification function only. |
| Session D pointer production as currently specified | Scope narrows materially. Extraction instruction's SD pointer sections require fundamental rewrite. |

Note: no document is fully retired — all are updated. "Retired" applies to specific sections or functions within documents.

### 6.2 New documents

| Document | Purpose | Status |
|---|---|---|
| WA-VerseContext-SetupInstruction-v1 | Claude Code: M17, M18, status resets, data migrations | To produce this session |
| WA-VerseContext-Instruction-v1 | Integrated Claude AI + Claude Code: full Verse Context cycle | To produce this session |

### 6.3 Documents requiring update

| Document | Current version | New version | Scope of change |
|---|---|---|---|
| WA-Reference | v5.2 | v5.3 | Patch index section; new status values; new file naming tokens; new table summaries; anchor verse definition; pool processing vocabulary; schema 3.8.0 |
| WA-Registry-Management-Guide | v5.3 | v5.4 | verse_context_status field; revised status lifecycle; pool processing sequence; terminology additions; revised queries |
| WA-SessionB-DataPrep-Instruction | v5.1 | v5.2 | Gate check: verse_context_status = Complete required; remove verse reading references; retain term classification function |
| WA-SessionB-Analysis-Instruction | v5.1 | v5.2 | Pool dataset as input; anchor verse reading protocol; XREF contextual profile usage; multi-word simultaneous analysis; revised output scope |
| WA-SessionB-Extraction-Instruction | v5.2 | v5.3 | Pool dataset references; revised SD pointer scope; post-patch outputs adjusted |
| WA-SessionB-ClaudeCode-Instructions | current | updated | New Verse Context section; pool dataset export; three patch types; re-extraction trigger; integrity validation; revised programme state queries |
| patch_specification | v1.1 | v1.2 | New patch types; new status values; patch index cross-reference |
| WA-SessionD-Orientation | v2 | v2.1 | Revised boundary; cross-pool synthesis focus; defer full redesign until Stage 2 begins |

---

## 7. Patch Index — to be added to WA-Reference v5.3

This section will appear in WA-Reference as the single navigation point for all patch types.

| Patch type | Governing document | Valid session_b_status values | Purpose |
|---|---|---|---|
| PREANALYSIS | WA-SessionB-DataPrep-Instruction | Pre-Analysis Complete | Term classification — extracted/delete/xref |
| SESSIONB | WA-SessionB-Extraction-Instruction | Analysis Complete / Session B Complete | Evidential status, dimensions, findings, SD pointers |
| VERSECONTEXT | WA-VerseContext-Instruction-v1 | n/a (verse_context_status driven) | Verse relevance filter, contextual grouping, anchor designation |
| VCGROUP | WA-VerseContext-Instruction-v1 | n/a | Targeted verse_context_group update |
| VCVERSE | WA-VerseContext-Instruction-v1 | n/a | Targeted verse_context update |
| SESSIOND | WA-SessionD-Orientation | n/a | Session D discovery and synthesis |
| CLUSTERING | WA-Implementation-Instruction | n/a | Cluster assignment updates |
| REPAIR | Any — per anomaly | Retain current status | Data corrections |

---

## 8. Open Items — Resolved

All open items from v1 and v2 are now resolved:

| Item | Resolution |
|---|---|
| O1 — source_category rename | M17 — schema migration, in setup instruction |
| O2 — anchor_verses field | Removed — M17, in setup instruction |
| O3 — 35 Analysis Complete registries | Reset to `Verse Context Reset` status — reprocess through Verse Context and pool-based Session B |
| O4 — Prototype batch selection | Term-based, not word-based — Claude Code constructs first batch from OWNER terms ordered by registry_id, up to 2,500 verses |
| Registry status tracking | New `verse_context_status` field on `word_registry` (Option B) |
| Session B JSON design | New pool analysis dataset — `wa-pool-{pool_id}-analysis-{date}.json` |
| XREF engagement in Session B | XREF contextual profiles included in pool dataset — group descriptions and anchor references, no full verse text |
| Session D boundary | Shifts to cross-pool interoperability and whole-programme synthesis |
| Cluster vs pool | Clusters retained as organisational entity; pools define processing sequence |
| Patch index location | WA-Reference new section |

---

## 9. Remaining Design Work — Not Yet Specified

These items are acknowledged but not yet fully specified. They require the setup instruction and Verse Context instruction to be implemented and validated before they can be properly designed.

| Item | Dependency |
|---|---|
| Full pool analysis dataset JSON specification | After Verse Context instruction is validated |
| Revised Session B Analysis instruction for pool-based analysis | After first pool prototype run |
| Revised Session B Extraction instruction | After revised Analysis instruction |
| Session D orientation update beyond boundary shift | After Stage 2 analysis begins |
| Pool 1 isolate grouping — which isolates go with which sub-pool | After Volitional Core and other sub-pools are analysed and the gravitational relationships are confirmed empirically |

---

*WA-VerseContext-ImpactStudy-v3-20260329 | Supersedes v1 and v2 | Definitive reference for all Verse Context implementation work*
