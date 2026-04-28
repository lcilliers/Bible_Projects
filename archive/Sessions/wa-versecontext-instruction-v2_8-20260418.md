# wa-versecontext-instruction-v2_8-20260418

**Framework B — Soul Word Analysis Programme
Verse Context Instruction — Integrated Claude AI and Claude Code
Version 2_8 | 20260418 | Status: Active governing instruction**

|**Document**|**Value**|
|-|-|
|Filename|wa-versecontext-instruction-v2_8-20260418.md|
|Supersedes|wa-versecontext-instruction-v2_7-20260414.md|
|Change note|v2_8 (20260418): GR-REF-002 sweep. (1) Filename migrated to current naming convention (underscored version, compact date, lowercase per GR-FILE-003/GR-FILE-007/GR-FILE-009). (2) Companion documents row updated to `[current]` token per GR-REF-002 for operational references. (3) Governing Rules section pointer migrated to `[current]`. (4) Footer supersession line refreshed. Historical change notes (v2_7, v2_6 etc.) retained below for provenance.<br />**v2_7 (20260414):** Manual changes by researcher: (1) Purpose and Scope: change pipeline stage to between Phase 1 completion and Dimension Review.<br />**v2_6 (20260414):** Global rules integration. (1) Governing Rules header added — mandatory load of the global rules file before session start. (2) Section 3.3 borderline retention paragraph replaced with reference to GR-PROG-004. (3) Section 6.2 Step 2 all-verses-fail principle statement ("individual inspection mandatory and non-waivable") replaced with reference to GR-PROG-005; operational deferred-flag procedure retained. (4) Section 6.4 write-on-discovery principle statement replaced with reference to GR-OBS-001; dual-write rule updated to reference GR-FILE-008. (5) Companion documents updated: DataPrep-Instruction removed (retired); patch\_specification updated to v1.10; SessionB updated to v4.8. All filename examples in output table updated to compact date format per GR-FILE-009.|
|Companion documents|wa-reference [current] │ wa-patch-instruction [current] │ wa-dimensionreview-instruction [current] │ wa-sessionb-analysis-readiness [current] │ wa-sessionb-analysis-output [current]|
|Inputs|Full word JSON exports — wa-{nnn}-{word}-extract-{date}.json (for batch construction) │ Verse Context batch JSON — wa-vcb-{batch\_id}-extract-{date}.json (for Claude AI classification)|
|Outputs|Verse Context batch JSON — wa-vcb-{batch\_id}-extract-{date}.json (Claude Code → Claude AI) │ Verse Context patch — wa-vcb-{batch\_id}-patch-v{n}-{date}.json (Claude AI → Claude Code) │ Observations file — wa-vcb-{batch\_id}-term-observations-v{major}.{minor}-{date}.md (Claude AI, progressive) │ Session log — wa-vcb-{batch\_id}-session-log-{scope}-v{n}-{date}.md (Claude AI, at breakpoints) │ Flags register — wa-vcb-{batch\_id}-flags-register-v{n}-{date}.md (Claude AI, end-of-batch flag resolution) │ Session B flags — wa-vcb-{batch\_id}-sessionb-flags-v{n}-{date}.md (Claude AI, when Session B flags raised) │ Re-exported full word JSON per registry (Claude Code → Session B)|
|Claude AI role|Verse reading, relevance filtering, contextual grouping, anchor designation, patch production|
|Claude Code role|Batch JSON construction from full exports, patch application, group\_code resolution, XREF status propagation, registry status management, integrity validation, completion reporting|
|Interaction model|Phase 1 exports → Claude Code constructs batch → Claude AI classifies → Claude Code applies patch, advances status, re-exports per-registry JSON → Session B Analysis Readiness gate opens|

\---

## Governing Rules

This instruction is governed by **wa-global-general-rules [current]**.

Claude AI must confirm the global rules file has been loaded before beginning any work in this session. State aloud per GR-LOAD-001.

Rules stated in the global file are not repeated here. Where a section references a global rule, the rule ID is cited.

\---

## 0\. Purpose and Scope

This document governs the Verse Context stage — the pipeline stage between Phase 1 completion and Dimension Review. Session B analysis follows the Dimension Review. It covers the full cycle: from the existing Phase 1 full word exports that serve as the source data, through batch construction, Claude AI classification, patch application, and confirmation that the patch is processed.

**What Verse Context does:**

* Uses the existing Phase 1 full word exports to identify which OWNER terms need classification
* Reads all verses for every active OWNER term programme-wide
* Filters each verse: does it engage the inner being through this term?
* Groups relevant verses by contextual meaning
* Designates anchor verses — the canonical citation and primary Session B analysis input per term and primary verse(s) for determining the dimension
* 
* Produces patches that Claude Code applies to populate `verse\_context\_group` and `verse\_context`
* Advances `verse\_context\_status` to Complete per registry when all OWNER terms are classified
* Re-exports the full word JSON for each completed registry — the trigger for DataPrep

**What Verse Context does NOT do:**

* Analyse the meaning of terms in depth — that is Session B Analysis
* Draw conclusions about the word being studied — that is Session B Analysis
* Produce cross-registry synthesis — that is Session D
* Assign evidential status to terms — that is Session B Analysis
* Classify XREF terms directly — XREF status is derived from OWNER classification (see Section 0.2)

**Stage sequence:**

```
Phase 1 complete (full word exports available)
     │
     ▼
Verse Context Stage 1 (this document)
  ├── Claude Code: batch construction from full exports
  ├── Claude AI: verse classification session
  ├── Claude Code: patch application + consistency validation
  ├── Claude Code: XREF status propagation
  ├── Claude Code: registry completion check + re-export
  └── loop until all OWNER terms classified
     │
     ▼
Session B DataPrep (verse\_context\_status = Complete triggers DataPrep gate)
     │
     ▼
Session B Analysis → Session B Extraction → Session D
```

|This document is self-standing. It does not rely on session memory. Claude Code requires this document and access to the database. Claude AI requires this document and the batch JSON export.|
|-|

\---

## 0.1 Pipeline Entry Point — What Already Exists

**Before any Verse Context work begins, the following is already in place:**

Phase 1 (Session A) has run for all 181 active registries. Each registry has:

* A full word JSON export: `wa-{nnn}-{word}-extract-{date}.json` stored at `data/exports/`
* All OWNER terms extracted, verse records populated, mti\_term\_id links present
* `session\_b\_status = Verse Context Reset` (reset from prior states — intentional)
* `verse\_context\_status = In Progress` (set during setup — M18)
* `verse\_context\_group` and `verse\_context` tables: empty (0 records — not yet processed)

**Claude Code uses the existing full word exports as the source for batch construction.** It does not re-query STEP or re-run audit\_word at this point. The verse data is already in the database, confirmed by the Phase 1 audit. The full word exports are the visible representation of that data.

**What Claude Code reads from the database to construct a batch:**

* `mti\_terms`: OWNER terms with status `extracted` or `extracted\_thin`
* `wa\_term\_inventory`: confirms `term\_owner\_type = 'OWNER'` and `delete\_flagged = 0`
* `wa\_verse\_records`: verse records for each OWNER term, `delete\_flagged = 0`
* `verse\_context`: existing records for any previously classified terms (to identify what still needs classification)

The batch JSON Claude Code produces is a structured subset of this data — formatted for Claude AI consumption. It is not the same as the full word export. See Section 5.2 for the batch JSON structure.

\---

## 0.2 XREF Terms — How They Are Handled

XREF terms are not classified by Claude AI. Their verse\_context status is derived from the OWNER term's completed classification. This section specifies exactly what Claude Code does with XREF terms.

**Background:** A XREF term is a Strong's number that appears in a registry's term inventory but whose primary analytical home (OWNER) is in a different registry. XREF verse records are delete\_flagged — they are excluded from all analysis. The term identity (`mti\_terms.id`) is shared across OWNER and XREF.

**Because verse\_context uses `mti\_term\_id` (FK to `mti\_terms.id`) as its key — not the term inventory id — the OWNER's verse\_context records are automatically visible to any registry that shares that term.** There is no separate XREF verse\_context record to create. The OWNER's classification is the programme-wide classification for that term.

**What Claude Code must do after every VERSECONTEXT patch:**

For each XREF term whose OWNER term appears in the completed batch:

1. Check whether the OWNER term now has `verse\_context` records (i.e. has been classified in this or a prior batch)
2. If yes: the XREF term is considered covered — no verse\_context insert needed. The XREF term's registry can query verse\_context via `mti\_term\_id` and will see the OWNER's groups and classifications
3. Include this coverage in the completion check (Section 14.5): a registry is complete when all its OWNER terms are classified AND all its XREF terms have an OWNER that is classified

**What this means for the completion check:**
A registry's `verse\_context\_status` advances to Complete only when:

* All its OWNER terms (with verses) have `verse\_context` records; AND
* All its XREF terms have an OWNER term that has `verse\_context` records

This second condition ensures that Session B Analysis, when it reads the pool analysis dataset, will find complete contextual profiles for every term — both OWNER and XREF.

**Claude Code query to check XREF coverage for a registry:**

```sql
-- XREF terms in this registry whose OWNER has not yet been classified
SELECT DISTINCT mt.strongs\_number, mt.owning\_registry\_fk, wr2.word as owner\_word
FROM wa\_term\_inventory ti
JOIN wa\_file\_index fi ON fi.id = ti.file\_id
JOIN word\_registry wr ON wr.id = fi.word\_registry\_fk
JOIN mti\_terms mt ON mt.strongs\_number = ti.strongs\_number
JOIN word\_registry wr2 ON wr2.id = mt.owning\_registry\_fk
WHERE wr.no = {registry\_no}
  AND ti.term\_owner\_type = 'XREF'
  AND ti.delete\_flagged = 0
  AND NOT EXISTS (
    SELECT 1 FROM verse\_context vc WHERE vc.mti\_term\_id = mt.id AND vc.delete\_flagged = 0
  );
-- If any rows returned: XREF terms unresolved — registry cannot advance to Complete yet
-- If zero rows: all XREFs covered — combine with OWNER check for complete assessment
```

**Reporting:** When Claude Code reports completion status, it must distinguish: "Registry {nnn} — {word}: OWNER classification complete, XREF coverage complete → verse\_context\_status set to Complete" vs "OWNER complete, {n} XREF terms pending OWNER classification in registries {list}".

\---

## 1\. The Two-System Model

|**System**|**Role**|
|-|-|
|Claude AI|Reads verse text. Applies the relevance filter. Produces contextual meaning descriptions. Groups verses. Designates anchors. Identifies dual-context. Produces the patch file.|
|Claude Code|Reads full exports and database to construct batch JSONs. Applies verse context patches. Resolves group\_code to integer id. Handles XREF coverage. Updates registry verse\_context\_status. Re-exports full word JSONs. Validates consistency rules. Runs integrity checks. Reports completion. Does not assess verse relevance or produce contextual descriptions.|

|**⚠ Claude Code does not assess verse relevance, produce contextual meaning descriptions, or designate anchors. All classification is Claude AI's responsibility.**|
|-|

\---

## 2\. Database Tables

### 2.1 `verse\_context\_group`

|Field|Type|Notes|
|-|-|-|
|id|INTEGER PK|Used for all joins — never use group\_code as join key|
|mti\_term\_id|INTEGER FK|→ mti\_terms.id — programme-wide term identifier, not registry-specific|
|group\_code|TEXT UNIQUE|`{mti\_term\_id}-{serial}` — human-readable, patch-constructable, never a join key|
|context\_description|TEXT|Brief phrase — inner-being engagement of the term in this group|
|notes|TEXT|Optional qualification|
|delete\_flagged|INTEGER|0 = active; 1 = dissolved (no physical deletes)|

### 2.2 `verse\_context`

|Field|Type|Notes|
|-|-|-|
|id|INTEGER PK||
|verse\_record\_id|INTEGER FK|→ wa\_verse\_records.id|
|mti\_term\_id|INTEGER FK|→ mti\_terms.id|
|group\_id|INTEGER FK|→ verse\_context\_group.id — NULL if is\_relevant = 0|
|is\_anchor|INTEGER|1 = anchor verse for its group|
|is\_relevant|INTEGER|0 = set aside; 1 = inner-being relevant|
|is\_related|INTEGER|1 = shares group meaning with anchor|
|set\_aside\_reason|TEXT|NULL if is\_relevant = 1. Controlled vocabulary when is\_relevant = 0 — see below.|
|notes|TEXT|Dual-context flags, borderline notes, revision reasons|
|delete\_flagged|INTEGER|0 = active; 1 = excluded (no physical deletes)|

**`set\_aside\_reason` controlled vocabulary** (applies when `is\_relevant = 0` only):

|Value|Meaning|
|-|-|
|`no\_inner\_being`|The term carries no inner-being content in this verse — the verse as a whole may or may not have inner-being content but this term does not carry it here|
|`physical\_only`|The term refers to a physical process, body part, or material object with no inner-being engagement|
|`spatial\_only`|The term is used in a locational or geographical sense with no inner-being engagement|
|`wrong\_face`|The verse contains inner-being content, but that content is carried by a different term — not by the term being classified. This verse belongs to another registry's analytical face. See Section 3.6 for the rediscovery procedure.|
|`other`|The set-aside reason does not fit the above categories. The `notes` field must explain.|

**Rule:** `set\_aside\_reason` must be populated for every `is\_relevant = 0` record from VCB-032 onward. It must be `NULL` for every `is\_relevant = 1` record. The `wrong\_face` value is the vertical-pass-enabling value — it marks verses that have analytical significance for a different registry's perspective, preserving that information for future rediscovery without re-reading the full corpus. Pre-VCB-031 set-aside records with `set\_aside\_reason = NULL` are a known gap; they will be populated in a future programme-wide audit if needed.

**Uniqueness:** UNIQUE on (verse\_record\_id, mti\_term\_id, group\_id). Same verse may appear under two groups for the same term (dual-context). Never twice in the same group.

**Programme-wide key:** `mti\_term\_id` is the same integer regardless of which registry views the term. OWNER and XREF registries query the same verse\_context records via this key.

### 2.3 Logical consistency rules

|Rule|Condition|
|-|-|
|R1|is\_relevant = 0 → group\_id IS NULL, is\_anchor = 0, is\_related = 0|
|R2|is\_anchor = 1 → is\_relevant = 1, is\_related = 0, group\_id NOT NULL|
|R3|is\_related = 1 → is\_relevant = 1, group\_id references a group with at least one active anchor|
|R4|Every term must have at least one active anchor before Session B may proceed|

\---

## 3\. The Governing Filter

Every verse is assessed against one question:

> \*\*Does this verse, through the use of this term, say something about the inner being — understood as the non-physical, internal states, capacities, and expressions that constitute a person's invisible life: how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God?\*\*

**If yes:** classify the contextual meaning (Section 6).
**If no:** set aside (is\_relevant = 0). No further work for this verse.

### 3.1 What passes the filter

A verse passes when the term's use engages one or more of:

* An internal state — emotion, feeling, disposition, attitude
* A capacity of the inner life — will, intention, thought, belief, desire
* A relational orientation — how the person is oriented toward God, others, or themselves inwardly
* A moral or character quality of the whole person
* A spiritual characteristic — responsiveness to God, spiritual condition, worship disposition

### 3.2 What does not pass the filter

* **Purely physical use** (`physical\_only`) — the term refers to a body part, physical process, or material object with no inner-being engagement
* **Purely social or narrative** (`no\_inner\_being`) — external conduct or events with no window into the inner life through this term
* **Purely positional or geographical** (`spatial\_only`) — locating something in space or time
* **Wrong face** (`wrong\_face`) — the verse contains inner-being content, but that content is carried by a different term, not by the term being classified. See Section 3.6.

When setting a verse aside, record the appropriate `set\_aside\_reason` value from Section 2.2 in the patch. Do not leave `set\_aside\_reason` null for any set-aside record from VCB-032 onward.

|**⚠ Apply the filter to the term's specific use in this verse — not to the verse's general theme. A verse about covenant renewal may use the term in a purely legal sense with no inner-being engagement for this specific term. Filter at term level, not verse level.**|
|-|

### 3.3 Borderline cases

Per GR-PROG-004: where the filter decision is genuinely uncertain, retain (is\_relevant = 1) and record the uncertainty in the notes field. Batch uncertainty questions at the end of each term's classification — do not stop mid-term.

### 3.4 Expressions as inner-being evidence

Where a term names a human act of expression — vocal, physical, or behavioural — the relevance filter is satisfied if the act plausibly originates in an inner state rather than being purely mechanical or reflexive. The direction of travel (inner state → outward expression) is itself inner-being data. The inner state need not be named explicitly in the verse; its presence may be inferred from the nature and force of the expression.

**What this means in practice:**

* A cry, call, or shout that carries urgency, distress, longing, outrage, or devotion passes the filter — even if the verse does not name an inner state explicitly. The force and character of the expression implies its inner origin.
* A groan, gesture, or act of worship passes when the expression plausibly reflects an inward disposition rather than a trained reflex or mechanical procedure.
* Administrative, liturgical, or physical acts with no personally engaged human agent (a procedure to be followed, a reflex without agent) do not pass on this basis alone.

**Rationale:** The inner being is the origin of human expression. Separating the expression from its inner origin would remove part of the causal chain from view. Every human act of expression originates somewhere in the person; the nature of that origination is significant inner-being data.

**Boundary:** This principle applies where the term itself names the act of expression, not merely a verse that happens to contain an expressive act. The term must carry the expression for Section 3.4 to apply.

**Where the distinction is uncertain:** retain (Section 3.3 applies).

*Programme note: This principle was established as RD-PC-001 during VCB-003 patch construction, arising from classification of H7121I (qa.ra call-out). It applies from VCB-004 onward and was applied retrospectively to H7121I in VCB-003.*

\---

### 3.5 Grammatical and functional particles

Where a term is a grammatical or functional particle — including pronouns, quantifiers, interrogatives, conjunctions, adverbs, particles of entreaty, and similar grammatical elements — the relevance filter requires an explicit assessment of how the particle functions in the specific verse, not merely whether the verse contains inner-being content.

**A grammatical particle passes the filter if it:**

* **Directs** inner-being content — orients a question, command, or assertion toward an inner-being subject (e.g. an interrogative pronoun framing a question about inner identity or moral worth)
* **Intensifies** an inner-being state or act — amplifies, sharpens, or emphasises the force of an inner-being expression
* **Qualifies the scope** of an inner-being condition — universalises, restricts, or otherwise shapes what an inner-being statement covers (e.g. a quantifier applied to a moral condition)
* **Discloses an inner orientation** through the manner in which it frames inner-being content — e.g. a particle of entreaty that reveals the posture of the speaker before God

**A grammatical particle does not pass the filter if it is:**

* **Purely syntactic** — present as a grammatical requirement with no semantic contribution to inner-being content
* **A social register marker** — indicating politeness, courtesy, or social function without inner-being implication
* **A temporal connector** — linking events or states in time without contributing to the inner-being dimension
* **Procedural filler** — serving a formal function in legal, liturgical, or administrative text with no personal inner-being engagement

**The test:** Remove the particle from the verse mentally. Does the inner-being content change meaningfully in how it engages the inner being? If the particle's presence shapes, frames, or intensifies that engagement, it passes. If the inner-being content is identical with or without the particle, it does not.

**Where the distinction is uncertain:** retain (Section 3.3 applies).

*Programme note: This section was added in v2.2, arising from programme flags PF-VCB007-001. It applies from VCB-008 onward. Applicable retrospectively to VCB-007 classifications of H4310 mi and H3605 kol, which were classified under this criterion during VCB-007 processing even before it was formally codified.*

\---

### 3.6 Wrong-face set-asides

A verse is a **wrong-face set-aside** when it contains genuine inner-being content — but that content is carried by a different term in the verse, not by the term currently being classified. The verse is analytically significant; it simply does not belong to this term's classification face.

**Examples:**

* Jer 7:24: "they walked in the stubbornness of their evil hearts" — when classifying *sha.ma* (hear/listen), the inner-being content is carried by *lev* (heart) and *she.ri.rut* (stubbornness), not by *sha.ma*. The refused hearing is a consequence of the stubborn heart, not the inner-being subject. Set aside for *sha.ma* with `set\_aside\_reason = 'wrong\_face'`.
* A verse about forgiveness where *ne.phesh* (soul) carries the inner-being content but the term being classified is a grammatical particle present in the same verse.

**When to use `wrong\_face`:**

* The verse passes the general relevance question ("does this verse contain inner-being content?") — yes
* The term-specific relevance question ("does this term carry the inner-being content?") — no
* The inner-being content in the verse is identifiably carried by a different term with its own registry

**When not to use `wrong\_face`:**

* The verse simply has no inner-being content at all — use `no\_inner\_being`, `physical\_only`, or `spatial\_only`
* The term partially carries the inner-being content (even weakly) — retain rather than set aside (Section 3.3)

**Patch treatment:**
Set aside normally (is\_relevant = 0, group\_id = null). Set `set\_aside\_reason = 'wrong\_face'`. In the `notes` field, identify which term carries the inner-being content and which registry it belongs to, where known: e.g. `"wrong\_face: inner-being content carried by lev (H3820A, Reg 183)"`.

**Rediscovery procedure:**
When a future analytical session (vertical pass, Session B cross-registry review, or programme audit) examines a verse across multiple registry faces, wrong-face set-asides are queryable:

```sql
SELECT vc.verse\_record\_id, vc.mti\_term\_id, vc.notes, vr.verse\_text
FROM verse\_context vc
JOIN wa\_verse\_records vr ON vr.id = vc.verse\_record\_id
WHERE vc.set\_aside\_reason = 'wrong\_face'
  AND vc.mti\_term\_id = {target\_mti\_term\_id};
```

This returns all verses set aside as wrong-face for a given term — i.e. verses where the term is present but the inner-being content belongs to a different face. The `notes` field identifies which term carries the content, enabling cross-registry analysis.

*Programme note: This section was added in v2.5, arising from VCB-031 vertical pass experiment. The `wrong\_face` value enables the vertical pass model to be applied to the existing VC classification corpus without re-reading every verse. Applies from VCB-032 onward.*

\---

**Dual purpose:**

1. **Efficiency instrument** — Session B Analysis reads anchor verses, not the full verse corpus. Verse Context reduces 133,353 active verses to a small set of anchors that carry the essential inner-being content for each term.
2. **Citation instrument** — anchor verses appear in Session B narratives and Session D synthesis as the evidential foundation for claims about the term

**Selection criteria:**

* Makes the contextual meaning evident without requiring surrounding context
* The term's inner-being function is unambiguous in the verse
* Stands alone as evidence — does not depend on interpretation of adjacent passages

**Minimum requirement:** every term must have at least one active anchor across all its groups (Rule R4). A term with no anchor cannot proceed to Session B Analysis. This is an absolute gate — Claude Code enforces it in the completion check.

**Quantity:** 1–2 anchors per group. Where two are designated, they represent distinct aspects of the group's meaning. Do not designate more than 2 unless a third genuinely adds something the first two do not.

**When no clear anchor exists:** if a group's verses are all contextually dependent (require surrounding passage to make sense), designate the least dependent one as the anchor and note the limitation. Do not leave a group without an anchor.

\---

## 5\. Claude Code — Batch JSON Construction

### 5.1 Trigger

Claude Code constructs a new batch:

* When Stage 1 begins (first batch)
* After each VERSECONTEXT patch is applied and completion checks run (subsequent batches)
* When researcher instructs a manual batch construction

### 5.2 Batch construction criteria

* **OWNER terms only** — `wa\_term\_inventory.term\_owner\_type = 'OWNER'`
* **Active terms only** — `mti\_terms.status IN ('extracted', 'extracted\_thin')`
* **Terms with verses only** — at least one `wa\_verse\_records` record where `delete\_flagged = 0`
* **Unclassified or incomplete terms first** — terms with no existing `verse\_context` records, ordered by `mti\_terms.owning\_registry\_fk` ascending (keeps terms from the same registry together where possible)
* **Target size** — accumulate terms until the count of unclassified verses (verses with no verse\_context record) reaches 2,000–2,500
* **Never split a term** — all verses for a term must appear in one batch; if adding a term would exceed 2,500 verses, exclude it and start it in the next batch
* **Batch ID** — sequential: VCB-001, VCB-002 etc.

**Registry split across batches — expected behaviour:** Because the 2,000–2,500 verse target is applied at term level, a registry with many terms may not be fully included in a single batch. When a batch closes before all OWNER terms of a registry have been classified, the registry remains at `verse\_context\_status = In Progress`. Its remaining terms are picked up in the next batch. This is the normal expected outcome — it is not an error condition. The registry completion check (Section 13) will correctly advance the registry to Complete only when all its OWNER terms have verse\_context records. Claude Code must report partial registries in the batch completion summary (Section 13.4) with the count of terms classified and terms remaining, so the researcher can confirm the split is working correctly.

**SQL policy:** SQL query construction for batch assembly is Claude Code's responsibility. This section provides all criteria, field names, derivation rules, and expected outcomes required. Claude Code constructs the accumulation query from these specifications and the database schema. An unclassified verse is any wa\_verse\_records record (delete\_flagged = 0) for an OWNER term that has no corresponding verse\_context record for that mti\_term\_id.

### 5.3 Batch JSON structure

The batch JSON contains all data Claude AI needs to classify verses — verse text, term identity, and the full state of any prior classifications for these terms.

```json
{
  "batch\_id": "VCB-{nnn}",
  "produced\_date": "{yyyy-mm-dd}",
  "produced\_by": "Claude Code — WA-VerseContext-Instruction v1.8",
  "governing\_instruction": "WA-VerseContext-Instruction-v1.8-20260331.md",
  "total\_verse\_count": 0,
  "total\_term\_count": 0,
  "unclassified\_verse\_count": 0,
  "verse\_context\_summary": {
    "total\_verses\_in\_batch": 0,
    "previously\_classified": 0,
    "unclassified": 0,
    "set\_aside\_in\_prior\_batches": 0,
    "anchor\_verses\_existing": 0
  },
  "terms": \[
    {
      "mti\_term\_id": 0,
      "strongs\_number": "{H/Gnnnn}",
      "transliteration": "{text}",
      "gloss": "{text}",
      "language": "{Hebrew or Greek}",
      "mti\_status": "{extracted or extracted\_thin}",
      "term\_owner\_type": "OWNER",
      "owning\_registry\_id": 0,
      "owning\_registry\_word": "{word}",
      "registry\_verse\_context\_status": "{NULL or In Progress or Complete}",
      "term\_classification\_complete": false,
      "total\_verses": 0,
      "unclassified\_count": 0,
      "existing\_groups": \[
        {
          "id": 0,
          "group\_code": "{mti\_term\_id}-{serial}",
          "context\_description": "{text}",
          "notes": null,
          "delete\_flagged": 0,
          "anchor\_count": 0,
          "related\_count": 0
        }
      ],
      "verses": \[
        {
          "verse\_record\_id": 0,
          "reference": "{Book Ch:V}",
          "verse\_text": "{full ESV text}",
          "target\_word": "{the specific word form occurring in this verse}",
          "span\_strong\_match": 1,
          "verse\_delete\_flagged": 0,
          "verse\_context": {
            "id": 0,
            "group\_id": 0,
            "group\_code": "{mti\_term\_id}-{serial}",
            "is\_anchor": 0,
            "is\_relevant": 0,
            "is\_related": 0,
            "notes": null,
            "delete\_flagged": 0
          }
        }
      ]
    }
  ]
}
```

**Source tables for batch JSON construction:**

|Field|Source|
|-|-|
|mti\_term\_id|mti\_terms.id|
|strongs\_number|mti\_terms.strongs\_number|
|transliteration|mti\_terms.transliteration|
|gloss|mti\_terms.gloss|
|language|mti\_terms.language|
|mti\_status|mti\_terms.status|
|term\_owner\_type|wa\_term\_inventory.term\_owner\_type (WHERE delete\_flagged = 0)|
|owning\_registry\_id|mti\_terms.owning\_registry\_fk|
|owning\_registry\_word|word\_registry.word (JOIN via mti\_terms.owning\_registry\_fk → word\_registry.id)|
|registry\_verse\_context\_status|word\_registry.verse\_context\_status (JOIN via owning\_registry\_fk)|
|total\_verses|COUNT(wa\_verse\_records WHERE term\_inv\_id = ti.id AND delete\_flagged = 0)|
|unclassified\_count|COUNT(wa\_verse\_records WHERE term\_inv\_id = ti.id AND delete\_flagged = 0 AND NOT EXISTS (SELECT 1 FROM verse\_context WHERE verse\_record\_id = vr.id AND mti\_term\_id = mt.id))|
|existing\_groups|verse\_context\_group WHERE mti\_term\_id = mt.id (ALL rows including delete\_flagged = 1)|
|existing\_groups.anchor\_count|COUNT(verse\_context WHERE group\_id = vcg.id AND is\_anchor = 1 AND delete\_flagged = 0)|
|existing\_groups.related\_count|COUNT(verse\_context WHERE group\_id = vcg.id AND is\_related = 1 AND delete\_flagged = 0)|
|verses|wa\_verse\_records WHERE term\_inv\_id = ti.id (ALL rows including delete\_flagged = 1 for revision history)|
|verses.verse\_context|verse\_context WHERE verse\_record\_id = vr.id AND mti\_term\_id = mt.id (NULL object if no record)|
|term\_classification\_complete|true if COUNT(wa\_verse\_records WHERE term\_inv\_id = ti.id AND delete\_flagged = 0 AND NOT EXISTS (SELECT 1 FROM verse\_context WHERE verse\_record\_id = vr.id AND mti\_term\_id = mt.id AND delete\_flagged = 0)) = 0|

**Notes on field population:**

* `verse\_context` field on each verse: set to `null` as a JSON object if no verse\_context record exists for this `verse\_record\_id` + `mti\_term\_id` combination. Populate all fields when a record exists, including `delete\_flagged` — Claude AI needs to see the full history including dissolved records.
* `existing\_groups`: include ALL groups for the term regardless of `delete\_flagged` — Claude AI needs to see dissolved groups to avoid duplicating their meaning in a new group.
* `term\_classification\_complete`: set to `true` only if every verse for this term already has a non-flagged verse\_context record. If `true`, Claude AI should review rather than re-classify from scratch.
* `verses`: include ALL verse records for the term, classified and unclassified alike — Claude AI may revise prior classifications.

### 5.4 Output file

`wa-vcb-{batch\_id}-extract-{date}.json`

Stored at `data/exports/verse\_context/` (or equivalent batch export directory). Provided to Claude AI for the classification session.

\---

## 6\. Claude AI — Classification Workflow

### 6.1 Startup

On receiving the batch JSON:

1. Read this instruction document in full (or confirm it is already loaded for this session)
2. Load and parse the batch JSON
3. State the startup summary (Annexure A template)
4. Note any terms marked `term\_classification\_complete: true` — review these but do not re-classify unless a revision is clearly warranted (see revision rule in Step 2 below)
5. Note any terms with existing verse\_context records but term\_classification\_complete = false — these are partially classified and must be flagged to researcher before continuing (see partial completion rule in Step 2 below)
6. **Processing order:** Terms are processed in registry sequence, ascending by registry number. Within a registry, terms are processed in the order they appear in the batch JSON. This order is fixed and does not require researcher confirmation at batch start.

### 6.2 For each term — complete this sequence before moving to the next term

**Step 1: Read all verses**
Read every verse in the term's verse array. Do not skip. Do not begin classifying while reading. Note the term's gloss and any existing\_groups before beginning. Understand what the term means before filtering verses.

**Step 2: Apply the relevance filter**
For each verse, apply the governing filter (Section 3).

* If an existing verse\_context record is present, review it — but do not assume it is correct. You may revise prior classifications if a revision is clearly warranted (see revision rule below).
* Mark each verse: Relevant (is\_relevant = 1) or Set aside (is\_relevant = 0).

**All-verses-fail rule:** Per GR-PROG-005 (non-waivable): if every verse for a term fails the relevance filter, individual inspection of every verse is mandatory before reaching this finding — no sampling regardless of corpus size. Once full individual inspection is complete, the all-verses-fail finding is treated as a deferred flag under the Deferred Flag Protocol (Section 6.5). Do not stop mid-classification. Accumulate the finding, record it in the flags register, and continue classifying. The finding must be documented with: term identity, verse count, the basis for the finding, and confirmation that individual inspection was completed for all verses.

**The only condition that triggers an immediate stop** is a structural data integrity failure that would prevent correct classification of subsequent verses — for example, a partial completion anomaly in the extract (some verses already classified but term\_classification\_complete = false). In all other cases, including all-verses-fail and all borderline classification decisions, proceed and defer to the end-of-batch flag session.

**Partial completion rule:** If a term has existing verse\_context records (some verses already classified) but term\_classification\_complete = false (some verses still unclassified), this indicates a prior batch was not completed correctly. This is an error condition. Stop for this term. Flag to the researcher with: the term details, which verses are classified, which are unclassified, and the reason for incompleteness if discernible. Await researcher instruction. The batch submission must not proceed for this term until the researcher has confirmed how to resolve it.

**Revision criterion for term\_classification\_complete = true:** A revision is clearly warranted when: (a) the existing context\_description would materially misrepresent the term's inner-being function in light of the full verse set now visible; or (b) a clearly stronger anchor verse is available and the designated anchor is demonstrably weaker. When a revision is made, Claude AI must: record the reason for the revision in the verse\_context notes field; and include a clear description of what changed and why in the per-term classification summary (Annexure B) so the researcher can review the change.

**Step 3: Group relevant verses**
Ask for each relevant verse: **does this verse engage the same inner-being characteristic through this term as verses already assigned to a group?**

* If yes → assign to that group
* If no → check existing\_groups first; assign to an existing group if appropriate; only create a new group if no existing group fits

**Characteristic-perspective grouping model:**

Groups must be formed from the perspective of the inner-being characteristic the verse cluster is primarily about — not from the perspective of what the term does. This distinction matters because:

* **Characteristic terms** name an inner-being state directly (e.g. *lev* = heart, *ne.phesh* = soul, *pistis* = faith). Their groups are naturally characteristic-centred.
* **Property terms** describe how inner-being characteristics operate — their mechanism, condition, expression, or channel (e.g. *sha.ma* = hear/listen, *o.zen* = ear, *akoē* = hearing). Property terms can serve different characteristics across their verse corpus, and can serve the same characteristic in opposite ways (e.g. receptive hearing as the channel of faith; refused hearing as the expression of heart-stubbornness).

**For property terms especially:** the group description must name the characteristic being served — not just the term's function. A group called "refusing to hear God" is term-centric. A group called "heart-stubbornness expressed through refusal of God's word" is characteristic-perspective. The difference is analytically significant: Session B analyses characteristics, and group descriptions must map to that analysis correctly.

**Forming context\_description:** A brief phrase (one sentence maximum) capturing what the group says about the inner being. It must:

* Name the inner-being characteristic the verse cluster primarily engages
* State the term's role accurately relative to that characteristic (as seat, expression, channel, mechanism, obstacle, or counterpart)
* Be grounded in what the verses show — not in prior theological knowledge
* Be sufficient to distinguish this group from others for this term

Examples of well-formed descriptions under the characteristic-perspective model:

* *Term names the inner seat of the emotion of fear — the place where fear arises and is registered* (characteristic: fear; term's role: seat)
* *Term serves as the channel through which faith arrives — hearing as the mechanism of faith reception* (characteristic: faith; term's role: channel)
* *Term expresses the stubbornness of the heart — refusal to hear as the outward form of inner resistance* (characteristic: stubbornness; term's role: expression)
* *Term names the cognitive capacity of the inner person — the faculty by which wisdom is received and held* (characteristic: wisdom/understanding; term's role: faculty)

Examples of descriptions to avoid (term-centric, not characteristic-perspective):

* <i>~~Term describes an act of refusing to listen~~</i> — names what the term does, not what the verse is about
* <i>~~Term is used when God addresses people~~</i> — describes context, not the inner-being characteristic
* <i>~~Term indicates active, engaged hearing~~</i> — describes the term's behaviour, not the characteristic served

**Grouping criterion — when a new group is warranted:** A new group is warranted when the inner-being characteristic being engaged is materially different from all existing groups, or when the same characteristic is engaged in a materially different way. Materially different means: an analysis of the verses in the candidate group, evaluated against the existing groups, would arrive at a differential conclusion about the characteristic. The following factors indicate material difference: (1) a different inner-being characteristic is the primary subject; (2) the term serves the same characteristic in a distinguishably different role (e.g. seat vs. channel vs. expression); (3) the same characteristic appears in a materially different orientation (e.g. toward God vs. against God; positive vs. negative register). Minor variations in emphasis or tone within the same essential characteristic engagement do not warrant a new group. Where 5 or more groups emerge for a single term, pause and assess whether consolidation better serves the criterion before adding further groups. Note the count in the per-term summary.

**Step 4: Designate anchors**
For each group: designate 1–2 anchor verses meeting the criteria in Section 4.

If revising prior classification: a verse previously marked is\_related may be promoted to is\_anchor. A verse previously marked is\_anchor may be demoted if a better anchor is found — but ensure the group retains at least one anchor.

**Step 5: Identify dual-context verses**
Where a verse plainly operates at two distinct inner-being levels through the same term — assign to two groups. This is the exception, not the norm. Record the reason for dual-context in the notes field on both verse\_context rows.

**Step 6: Per-term classification summary and observations file write**
Before moving to the next term, state the summary (Annexure B template) and write the term's Classification blocks to the observations file immediately. This produces a readable record and the machine-parseable record simultaneously.

**⚠ Classification block integrity rules — these govern the observations file as a machine-parseable source document:**

**Unique group codes:** Every Classification block written for a term must carry a unique `{mti\_id}-{serial}` group code. Once a code is written to the file (e.g. `235-001`), that code is permanently bound to the group it was first assigned to. It must not be reused for a different group in the same term entry, even if the original group is revised or abandoned.

**Mid-stream revision protocol:** If, during classification of a term, a group is revised or abandoned and replaced with a different group, the following steps are mandatory:

1. Mark the original Classification block explicitly as superseded by prepending `\~\~SUPERSEDED\~\~` to that block.
2. Assign the revised group a new sequential code (e.g. if `235-001` is superseded, the revision becomes `235-004` — the next available serial for that term).
3. Write the revised block with the new code immediately after the superseded block.
4. Update the SUMMARY line to reflect the final count of active (non-superseded) groups only.

**Why this matters:** The patch builder parses Classification blocks by group code. Duplicate codes for different groups cause the patch builder to conflate or dissolve correct groups along with incorrect ones. The superseded-block marking ensures the patch builder identifies and skips abandoned draft groups without ambiguity. This failure mode occurred in VCB-006 (H7451A group 235-001) and caused correct verses to be incorrectly set aside in the patch.

### 6.3 After all terms are classified

Review the full batch classification summary. Then, before producing the VERSECONTEXT patch:

**Step 1 — End-of-batch flag resolution session (mandatory if any flags were deferred):**
Produce the flags register (Section 6.5) and present it to the researcher for decisions. Do not begin patch preparation until all flags are resolved. After the researcher provides decisions, update the observations file to reflect any classification changes arising from those decisions, increment the observations file version, and dual-write.

**Step 2 — Session B flags document (mandatory if any Session B flags were raised during flag resolution):**
Produce the Session B flags document (Section 6.6). This document must be completed before the patch construction session begins, as it forms part of the handoff chain to Session B.

**Step 3 — Produce the VERSECONTEXT patch (Section 7).**

### 6.4 Session discipline — file writing, session logs, and memory management

**⚠ This section governs how Claude AI manages its working process throughout a Verse Context session. These rules exist because context window exhaustion is the primary operational risk in large batches.**

**Continuous file writing — observations file (per GR-OBS-001, non-waivable):**
The per-batch observations file must be written progressively to disk during the session, not accumulated in memory and written at the end. Per GR-FILE-008 (dual-write): every write goes to both `/home/claude/` and `/mnt/user-data/outputs/`. The write discipline is as follows:

* **After every term** (Step 6 of Section 6.2): write that term's Classification blocks and SUMMARY line to the observations file immediately. Do not defer. Do not batch multiple terms before writing.
* **On every write**: increment the minor version number in the filename and in the file header (e.g. `v1.2` → `v1.3`). The version number is the only reliable differentiator between saves.
* **Version confirmation**: before each write, state aloud: *"Writing observations file — current version: v{n}. Incrementing to v{n+1}."* This confirms the save is occurring and makes the version progression visible in the session transcript.
* **Session log version reference**: every session log must state the current observations file version at the time of writing (e.g. *"Observations file at time of this log: wa-vcb-006-term-observations-v1.7-20260331.md"*). This creates a recoverable link between session logs and the observations file state they describe.
* **New session startup**: at the start of every new session that continues an existing batch, Claude AI must confirm the observations file version it is reading before doing any work. State: *"Observations file loaded: {filename} version {v}. This is the most recent version and will be the base for continued writes."*

If the session is interrupted, the observations file must contain a complete record of every term classified up to that point, and the version number must reflect the last completed write.

**Unified file naming convention — all Claude AI outputs:**

All files produced by Claude AI during a Verse Context classification or patch construction session must follow this pattern:

```
wa-vcb-{batch\_id}-{scope}-{version}-{date}.{ext}
```

|Component|Rule|
|-|-|
|`wa-vcb`|Fixed prefix — always lowercase, always present|
|`{batch\_id}`|Batch identifier — e.g. `003` for VCB-003|
|`{scope}`|Short descriptor of the file's content — see table below|
|`{version}`|Version string — see versioning rules below|
|`{date}`|Creation date in `YYYYMMDD` format — does not change on update|
|`{ext}`|File extension — `.md`, `.json`|

**Scope values for Claude AI outputs:**

|File type|Scope value|Example|
|-|-|-|
|Observations file|`term-observations`|`wa-vcb-003-term-observations-v1.2-20260331.md`|
|Session log|`session-log-{breakpoint}`|`wa-vcb-003-session-log-R19-v1-20260331.md`|
|Final session log|`session-log-final`|`wa-vcb-003-session-log-final-v1-20260331.md`|
|Flags register|`flags-register`|`wa-vcb-015-flags-register-v1-20260403.md`|
|Session B flags|`sessionb-flags`|`wa-vcb-015-sessionb-flags-v1-20260403.md`|
|Patch file|`patch`|`wa-vcb-003-patch-v1-20260331.json`|

**Breakpoint identifiers for session logs** — use the registry number(s) completed at that breakpoint:

* Single registry: `R19`, `R20`, `R28` etc.
* Multiple registries in one log: `R20-R23`, `R24-R26` etc.
* Final log covering all registries: `final`

**Versioning rules:**

* `{version}` always starts at `v1` for a new file
* For the observations file, which is updated progressively within a session, increment the minor version on each save: `v1`, `v1.1`, `v1.2`, etc. The version number is the only reliable differentiator between saves — do not rely on file size or timestamp
* For session logs and flag resolution files, which are written once per breakpoint, use `v1` unless a correction is issued, in which case increment: `v2`, `v3`, etc.
* `{date}` is the creation date and does not change when the file is updated

**Sorting behaviour:** All batch outputs sort together under `wa-vcb-{batch\_id}-` when listed alphabetically, making the full batch file set visible at a glance.

**Example — complete set for VCB-015:**

```
wa-vcb-015-flags-register-v1-20260403.md
wa-vcb-015-patch-v1-20260403.json
wa-vcb-015-session-log-classA-v1-20260403.md
wa-vcb-015-session-log-classB-v1-20260403.md
wa-vcb-015-session-log-classC-v1-20260403.md
wa-vcb-015-session-log-final-v1-20260403.md
wa-vcb-015-sessionB-flags-v1-20260403.md
wa-vcb-015-term-observations-v4.6-20260403.md
```

This convention applies from VCB-003 onward. Files produced before this version of the instruction are not retroactively renamed. **Mixed-case or non-standard prefixes (e.g. `WA-SessionLog-VCB003-...`) are a naming violation — do not use them.**

**Session logs at natural breakpoints:**
A session log must be produced at every natural breakpoint — completion of a registry, a researcher checkpoint, a context window warning, or a session close. Do not wait until the end of the batch. Session logs must capture: terms classified, groups and anchors per term, all researcher decisions made, any open flags, and the work order for the next session. If the session ends unexpectedly, the most recent session log is the recovery point.

**No large in-memory accumulation:**
Do not hold growing data structures in memory across many terms. The observations file and session logs are the durable record. Patch operations should be derived from these files in a separate dedicated patch construction step, not accumulated in the classification session. For batches with more than approximately 50 terms, treat patch construction as a separate session that reads the observations file and extract JSON as its inputs — not a continuation of the classification session. See deferred patch construction below.

**Deferred patch construction — valid workflow:**
When a batch is large enough that accumulating patch operations during classification would fill the context window, classification and patch construction are performed in separate sessions. This is the expected workflow for batches of this programme's scale. Requirements for the deferred path:

* The observations file must contain a **Classification block** for every active term, in structured format: `{mti\_id}-{serial}: \*{context\_description}\* | Anchor: {ref} | Related: {ref, ...}`. This structured block is what the patch builder reads — prose-only entries cannot be reliably parsed. Write the Classification block for every term at classification time, even for terms with a single verse. The observations file provided to the patch construction session must be the most recent version (highest version number).
* The final session log before patch construction must contain a complete per-term table showing: mti\_id, Strong's, verse count, relevant count, group count, and anchor references. This table is the reconciliation check for the patch.
* The patch construction session must verify every anchor reference against the actual verse\_record\_ids in the extract JSON before producing any operations. Anchor references that do not match the term's verse set must be corrected — they are typically reference format variants (e.g. `Jude 3` vs `Jud 1:3`) or verses assigned to a different term.
* The patch construction session must run programmatic pre-submission validation (Section 7.6) before producing the output file.

**Instruction document size awareness:**
This instruction document is long. When loading it alongside a large batch JSON and an observations file, the combined context load is significant. Claude AI should read the instruction once at session start and not reload it unless a specific section is needed. For patch construction sessions, load only the observations file, the extract JSON, and Sections 7–7.6 of this instruction — not the full document.

\---

## 6.5 Deferred Flag Protocol

**⚠ This section replaces the previous per-term stop rule for all-verses-fail findings and borderline classification decisions. Flags that do not block the classification of other verses are accumulated during classification and resolved in a single interactive session at end-of-batch, before patch preparation begins.**

### 6.5.1 What is a deferred flag

A deferred flag is any classification finding or question that:

* Does not prevent correct classification of the remaining verses in the batch
* Requires researcher judgement before the patch can be correctly produced
* Would, under the previous protocol, have caused a mid-classification interruption

**Examples of deferred flags:**

* All-verses-fail findings (all verse counts, all term types)
* Borderline relevance judgements where the filter decision is genuinely uncertain
* Classification boundary questions (e.g. where a term's inner-being connection is indirect)
* Homograph split observations (informational flags, no decision required)
* Analytical observations that require researcher input before a Session B note can be formed

**The only condition that still triggers an immediate stop** is a structural data integrity issue that would prevent correct classification of subsequent verses — specifically, a partial completion anomaly where some verses for a term already have verse\_context records but term\_classification\_complete = false. This indicates a prior batch was not completed correctly and must be resolved before continuing.

### 6.5.2 During classification — flag accumulation

While classifying, when a deferred flag arises:

1. Record the flag identifier (DF-{nnn}, sequential within the batch) in the running flags list maintained in working memory or in the observations file notes
2. Make a working classification decision (typically: classify as best you can on current evidence, note the assumption made, continue)
3. For all-verses-fail findings: record the term identity, verse count, basis for the finding, and confirmation that individual inspection was completed for all verses
4. Do not interrupt the session. Do not present the flag to the researcher until the end-of-batch flag session

### 6.5.3 End-of-batch — producing the flags register

After all terms are classified, produce the flags register before the patch. The flags register is a structured document (not a prose summary) with one entry per flag.

**File:** `wa-vcb-{batch\_id}-flags-register-v1-{date}.md`

**Each flag entry must contain:**

1. **Flag identifier** — DF-{nnn} | term identity (Strong's, transliteration, gloss, mti\_id, registry)
2. **The verse(s) under consideration** — full verse text for every verse relevant to the flag. Do not use references alone. The researcher cannot make a sound judgement from references alone.
3. **The specific issue** — what was found and why a decision is required
4. **What each option means for the patch** — concrete patch consequence of each option: which verses will be classified as relevant or set aside, whether a group will exist or not, whether an all-verses-fail record will be produced
5. **Claude AI's own assessment** — state which option is analytically stronger and why, grounded in the verse texts, the filter criteria, and programme precedent. Label explicitly: *"Claude AI assessment: \[option/finding] is \[stronger/correct] because \[reason]."* Do not present options as equally weighted when one is clearly more consistent with programme criteria

**Format:**

```
### DF-{nnn} | {strongs} ({transliteration}) — {gloss} | mti\_id={n} | Registry {nnn} ({word})
\*\*Verse count:\*\* {n}
\*\*Finding / Issue:\*\* {description}

\*\*The verse(s):\*\*
vid={n} {ref}: \*"{full verse text}"\*
\[repeat for all relevant verses]

\*\*Option A:\*\* {description} — patch consequence: {what happens}
\*\*Option B:\*\* {description} — patch consequence: {what happens}
\[or: CONFIRM / OVERRIDE for all-verses-fail findings]

\*\*Claude AI assessment:\*\* {which option/finding, and why}

→ \*\*Your decision:\*\*
```

The register closes with a summary table listing all flags, their type, and Claude AI's recommendation. This allows the researcher to see the full scope before making decisions.

### 6.5.4 Receiving researcher decisions

The researcher returns the flags register with decisions recorded against each flag. On receiving it:

1. **Parse all decisions** before making any changes
2. **Update the observations file** — for each decision that changes a classification (e.g. moving verses to set-aside, confirming all-verses-fail), append a clearly marked decisions section to the observations file. Do not edit inline — append after the last term entry under the heading `## FLAG RESOLUTION DECISIONS — {date}`. This preserves the full classification record and makes the decision trail visible
3. **Record Session B flags** — for any flag where the researcher's decision includes an analytical observation or question for Session B exploration (see Section 6.6), record it in the Session B flags list
4. **Increment the observations file version** (e.g. v4.5 → v4.6) and dual-write after all decision updates are complete
5. **Proceed to Session B flags document** (Section 6.6) if any Session B flags were raised, then proceed to patch construction

### 6.5.5 All-verses-fail — patch treatment

For any term confirmed as all-verses-fail:

* No verse\_context records are inserted for this term
* The term proceeds to Session B with no anchor. Rule R4 (every term must have at least one active anchor before Session B may proceed) is noted as not applicable for this term
* The all-verses-fail finding is documented in the final session log

\---

## 6.6 Session B Flags

**Purpose:** The Session B flags document carries analytical insights and questions that emerge during Verse Context classification — from the researcher's flag decisions, from unexpected term behaviour, or from verse engagement that raises questions beyond the scope of the filter decision — into the Session B Analysis stage. Verse Context intentionally defers interpretation; this document is the formal channel through which Verse Context observations inform Session B.

**When to produce:** If any Session B flags are raised during the end-of-batch flag resolution session, produce the Session B flags document before the patch construction session. If no Session B flags were raised, the document is not required for that batch.

**File:** `wa-vcb-{batch\_id}-sessionB-flags-v1-{date}.md`

### 6.6.1 What qualifies as a Session B flag

A Session B flag is raised when:

* The researcher's decision on a flag includes an explicit analytical question or observation for Session B to explore
* A term's classification raises an interpretive question that goes beyond the filter decision (e.g. the term behaves in a way that may reveal a previously unidentified inner-being dynamic)
* A researcher comment on a flag suggests a connection between terms, registries, or clusters that Session B should investigate

Session B flags are not corrections or errors. They are analytical starting points.

### 6.6.2 Content of each Session B flag entry

Each entry must contain:

1. **Flag identifier** — SBF-{batch\_id}-{nnn} (e.g. SBF-VCB015-001)
2. **Term and registry** — Strong's, transliteration, gloss, mti\_id, registry number and word
3. **Source** — which deferred flag triggered this Session B flag (DF-{nnn})
4. **The analytical question** — the question or observation the researcher raised, expanded with analytical context grounded in the verse corpus
5. **Suggested Session B exploration** — concrete lines of inquiry for Session B Analysis, including which group codes carry the most relevant verses, any cross-registry connections, and what the question implies for the programme's understanding of the inner being
6. **Relevant group codes** — the group codes in the observations file most directly relevant to this exploration

### 6.6.3 Position in the handoff chain

The Session B flags document must be provided to the Session B DataPrep and Analysis sessions alongside the re-exported full word JSON for each affected registry. It is not a replacement for the Session B instructions — it is supplementary analytical context that enriches how the analyst approaches those terms.

When Session B begins for a registry that has Session B flags, Claude AI must load the flags document alongside the standard Session B instructions and explicitly acknowledge each flag at the start of analysis for the affected term.

**⚠ Session B flags must not be lost between sessions.** The patch construction session should note in its handoff that Session B flags exist for specific registries. Claude Code's completion report for a registry should flag whether a sessionB-flags file exists for that batch.

\---

## 7\. Patch Production

### 7.1 Patch types

|Type|Purpose|When to use|
|-|-|-|
|VERSECONTEXT|Full batch — all terms in batch|After completing all terms in a batch session|
|VCGROUP|Targeted group update|When revising a single group description or dissolving/reinstating a group outside a batch|
|VCVERSE|Targeted verse update|When a single verse changes state (new verse added after audit\_word re-run, verse removed, reclassification needed)|

### 7.2 VERSECONTEXT patch — structure

Produced once per batch, after all terms are complete and pre-submission validation passes.

```json
{
  "\_patch\_meta": {
    "patch\_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1",
    "batch\_id": "VCB-{nnn}",
    "produced\_date": "{yyyy-mm-dd}",
    "produced\_by": "WA-VerseContext-Instruction-v1.8",
    "session\_b\_status": null,
    "description": "Verse context classification — batch VCB-{nnn}, {n} terms, {n} verses"
  },
  "operations": \[],
  "\_patch\_summary": {
    "total\_operations": 0,
    "group\_inserts": 0,
    "group\_updates": 0,
    "verse\_context\_inserts": 0,
    "verse\_context\_updates": 0,
    "relevant\_verses": 0,
    "set\_aside\_verses": 0,
    "anchor\_verses": 0,
    "dual\_context\_verses": 0,
    "revisions\_to\_prior": 0
  }
}
```

Note: `session\_b\_status` is `null` in all Verse Context patches. The applicator must not reject this. `verse\_context\_status` is managed by Claude Code completion logic, not by patch files.

**`\_patch\_summary` field definitions:**

* `dual\_context\_verses` — count of *verses* (not verse\_context rows) that appear in more than one group for the same term. A verse assigned to two groups contributes 1 to this count regardless of how many verse\_context rows it generates.

### 7.3 Operation types

#### Insert new group

```json
{
  "op\_id": "OP-001",
  "operation": "insert",
  "table": "verse\_context\_group",
  "record": {
    "mti\_term\_id": 142,
    "group\_code": "142-001",
    "context\_description": "{brief phrase — inner-being engagement}",
    "notes": null,
    "delete\_flagged": 0
  },
  "description": "New group for {strongs\_number}: {context\_description}"
}
```

**Claude Code:** after inserting, capture `last\_insert\_rowid()` as the integer id for this group. Use this integer in all subsequent verse\_context inserts that reference this group in the same patch.

#### Update existing group

```json
{
  "op\_id": "OP-002",
  "operation": "update",
  "table": "verse\_context\_group",
  "match": { "id": 47 },
  "set": {
    "context\_description": "{revised phrase}",
    "notes": "{reason for revision}",
    "delete\_flagged": 0
  },
  "description": "Revised context description for group {group\_code}: {reason}"
}
```

Only fields being changed appear in `set`. `delete\_flagged = 1` dissolves a group. When dissolving: check that affected anchor verses are reassigned or that the term retains at least one anchor from another group — include those operations in the same patch.

#### Insert new verse\_context record — anchor

```json
{
  "op\_id": "OP-003",
  "operation": "insert",
  "table": "verse\_context",
  "record": {
    "verse\_record\_id": 4821,
    "mti\_term\_id": 142,
    "group\_id": "142-001",
    "is\_anchor": 1,
    "is\_relevant": 1,
    "is\_related": 0,
    "notes": null,
    "delete\_flagged": 0
  },
  "description": "{Book Ch:V} — anchor, group 142-001: {context\_description}"
}
```

#### Insert new verse\_context record — related

```json
{
  "op\_id": "OP-004",
  "operation": "insert",
  "table": "verse\_context",
  "record": {
    "verse\_record\_id": 4822,
    "mti\_term\_id": 142,
    "group\_id": "142-001",
    "is\_anchor": 0,
    "is\_relevant": 1,
    "is\_related": 1,
    "notes": null,
    "delete\_flagged": 0
  },
  "description": "{Book Ch:V} — related, group 142-001"
}
```

#### Insert new verse\_context record — set aside

```json
{
  "op\_id": "OP-005",
  "operation": "insert",
  "table": "verse\_context",
  "record": {
    "verse\_record\_id": 4823,
    "mti\_term\_id": 142,
    "group\_id": null,
    "is\_anchor": 0,
    "is\_relevant": 0,
    "is\_related": 0,
    "set\_aside\_reason": "{no\_inner\_being | physical\_only | spatial\_only | wrong\_face | other}",
    "notes": null,
    "delete\_flagged": 0
  },
  "description": "{Book Ch:V} — set aside ({set\_aside\_reason}), no inner-being engagement for {strongs\_number}"
}
```

**`set\_aside\_reason` is required** for every set-aside record from VCB-032 onward. Use the controlled vocabulary from Section 2.2. For `wrong\_face`, populate the `notes` field with the term and registry carrying the inner-being content where known: e.g. `"wrong\_face: inner-being content carried by lev (H3820A, Reg 183)"`. For `other`, the `notes` field must explain the reason. `NULL` is not acceptable from VCB-032 onward.

```

#### Update existing verse\_context record

```json
{
  "op\_id": "OP-006",
  "operation": "update",
  "table": "verse\_context",
  "match": { "id": 892 },
  "set": {
    "group\_id": 47,
    "is\_anchor": 1,
    "is\_relevant": 1,
    "is\_related": 0,
    "notes": "{reason for revision}",
    "delete\_flagged": 0
  },
  "description": "{Book Ch:V} — reclassified: promoted to anchor, group {group\_code}"
}
```

**All corrections are UPDATE operations. Never delete and reinsert.** Use `delete\_flagged = 1` to flag a record out of the active set without physical deletion.

**Note on group\_id references:** In operations within the same patch, `group\_id` may be a group\_code string (e.g. `"142-001"`) for groups being inserted in the same patch. Claude Code resolves these to the captured integer id at apply time. For existing groups from prior patches, use the integer id directly.

### 7.4 Operation ordering within patch

For each term, order operations as follows:

1. All `verse\_context\_group` inserts for the term (new groups — so integer ids are available for subsequent rows)
2. All `verse\_context\_group` updates (revisions to existing groups)
3. All `verse\_context` inserts — anchors first, then related, then set-aside
4. All `verse\_context` updates (revisions to prior classifications)

Across terms: process terms in the order they appear in the batch JSON.

### 7.5 Decision context requirement — researcher decisions during patch construction

When Claude AI identifies an issue during patch construction that requires a researcher decision (anchor missing, group dissolution, cross-term assignment, ambiguous reference, or any other unresolvable condition), it must present the decision with the following elements. A bare option list is not acceptable.

**Required elements for every researcher decision:**

1. **The affected term and group** — Strong's number, transliteration, gloss, mti\_id, group code, and group description.
2. **The specific issue** — what was found and why it cannot be resolved automatically.
3. **Full verse text for every verse under consideration** — not just references. The researcher cannot make a sound judgement from references alone.
4. **What each option means for the patch** — spell out the concrete consequence of each choice: which verses will be classified, which will be set aside, whether a group will exist in the database.
5. **Claude AI's own assessment** — state which option is analytically stronger, and why, grounded in the verse texts and the group description. Claude AI must not present options as equally weighted when one is clearly more consistent with the programme's classification criteria. Label this explicitly: *"Claude AI assessment: \[option] is stronger because \[reason]."*

**Rationale:** During VCB-006 patch construction, 10 decisions were presented to the researcher as option lists with minimal verse context. The researcher noted that in 90% of cases the decision required a judgement call without sufficient information. This instruction corrects that discipline. The researcher's role is to make an informed decision, not to guess.

**Format template:**

```
Decision D-NNN | mti\_id={n} | {strongs} ({transliteration}) — {gloss}
Group {code}: {description}

Issue: {what was found and why it cannot be auto-resolved}

Verses under consideration:
  {ref} vid={n}: "{full verse text}"
  {ref} vid={n}: "{full verse text}"
  \[repeat for all relevant verses]

Options:
  A. {description of option A} — patch consequence: {what happens}
  B. {description of option B} — patch consequence: {what happens}

Claude AI assessment: Option {A/B} is analytically stronger because {reason grounded in verse text and group description}.

→ Your decision:
```

### 7.6 Anchor integrity rule

Any operation that removes, dissolves, or reclassifies the last anchor for a term must be accompanied in the same patch by a promotion operation ensuring the term retains at least one active anchor. This rule is absolute. Claude AI is responsible for ensuring it. Claude Code validates after application.

### 7.7 Pre-submission validation

Before submitting any patch, verify:

* Every verse in the batch has exactly one verse\_context row, except dual-context verses (exactly two)
* Every new group has at least one anchor insert in this patch or an existing anchor in the database
* Every is\_related = 1 row references a group that has an anchor (in this patch or existing)
* Every is\_relevant = 0 row has group\_id = null
* No row has is\_anchor = 1 and is\_related = 1 simultaneously
* \_patch\_summary counts match the actual operation counts

**Programmatic validation — required for large batches (>50 terms):** When the patch is produced in a deferred patch construction session (see Section 6.4), validation must be performed programmatically against the extract JSON before the patch file is written. Specifically:

1. **Anchor reference verification** — every anchor reference in the classification data must be resolved to an actual verse\_record\_id in the term's verse set. References that do not resolve must be corrected before operations are generated. Silent failure (generating a patch with unresolved anchors) is not acceptable.
2. **Duplicate key check** — verify no (verse\_record\_id, mti\_term\_id, group\_id) combination appears more than once. This catches the case where a verse appears in both the anchor and related lists for the same group.
3. **Coverage check** — every verse\_record\_id in the extract for every term must appear in exactly one verse\_context insert (or two for dual-context verses). No verse may be missed.
4. **R1–R4 pre-check** — apply the consistency rules (Section 11.3) to the proposed operations before writing the file, not only after application.

### 7.8 Handoff to Claude Code

```
PATCH SUBMISSION TO CLAUDE CODE

Patch file: wa-vcb-{batch\_id}-patch-{date}.json
Patch type: VERSECONTEXT

Action required:
  1. Apply patch — insert/update verse\_context\_group and verse\_context records
  2. Resolve group\_code strings to integer ids for new groups in this patch
  3. Validate consistency rules R1–R4 after application
  4. Run integrity validation (Section 13 below)
  5. Handle XREF coverage check for all affected registries (Section 0.2)
  6. For each registry whose OWNER terms appear in this batch:
     - Run completion check (Section 14.5)
     - If complete: SET verse\_context\_status = 'Complete', re-export full word JSON
  7. Report: records inserted/updated, registries advanced to Complete, XREF coverage status,
     any integrity violations, next batch construction status
```

\---

## 8\. VCGROUP Patch — Targeted Group Update

Use when revising a single `verse\_context\_group` record outside a full batch run — for example, when a context\_description needs refinement after researcher review, or when a group is dissolved because its verses belong better in another group.

### 8.1 Input required from Claude Code

Before producing a VCGROUP patch, Claude Code must provide:

```json
{
  "group": {
    "id": 0,
    "mti\_term\_id": 0,
    "strongs\_number": "{H/Gnnnn}",
    "group\_code": "{text}",
    "context\_description": "{current text}",
    "notes": null,
    "delete\_flagged": 0,
    "anchor\_count": 0,
    "related\_count": 0,
    "anchor\_verses": \[
      {
        "verse\_record\_id": 0,
        "reference": "{Book Ch:V}",
        "verse\_text": "{text}"
      }
    ]
  }
}
```

**Source tables for VCGROUP input:**

|Field|Source|
|-|-|
|group.id|verse\_context\_group.id|
|group.mti\_term\_id|verse\_context\_group.mti\_term\_id|
|group.strongs\_number|mti\_terms.strongs\_number (JOIN via verse\_context\_group.mti\_term\_id → mti\_terms.id)|
|group.group\_code|verse\_context\_group.group\_code|
|group.context\_description|verse\_context\_group.context\_description|
|group.notes|verse\_context\_group.notes|
|group.delete\_flagged|verse\_context\_group.delete\_flagged|
|group.anchor\_count|COUNT(verse\_context WHERE group\_id = vcg.id AND is\_anchor = 1 AND delete\_flagged = 0)|
|group.related\_count|COUNT(verse\_context WHERE group\_id = vcg.id AND is\_related = 1 AND delete\_flagged = 0)|
|group.anchor\_verses|verse\_context (WHERE group\_id = vcg.id AND is\_anchor = 1 AND delete\_flagged = 0) → wa\_verse\_records (verse\_record\_id, reference, verse\_text)|

### 8.2 Patch structure

```json
{
  "\_patch\_meta": {
    "patch\_id": "PATCH-{YYYYMMDD}-VCGROUP{group\_id}-V1",
    "group\_id": 0,
    "produced\_date": "{yyyy-mm-dd}",
    "produced\_by": "WA-VerseContext-Instruction-v1.8",
    "session\_b\_status": null,
    "description": "Targeted group update — group {group\_code}: {reason}"
  },
  "operations": \[
    {
      "op\_id": "OP-001",
      "operation": "update",
      "table": "verse\_context\_group",
      "match": { "id": 0 },
      "set": {
        "context\_description": "{revised text}",
        "notes": "{reason if applicable}",
        "delete\_flagged": 0
      },
      "description": "Revised group {group\_code}: {reason}"
    }
  ],
  "\_patch\_summary": {
    "total\_operations": 1,
    "group\_updates": 1
  }
}
```

**Reinstatement note:** If `delete\_flagged` is reset from 1 to 0 (reinstating a dissolved group), the verse\_context rows that were flagged when the group was dissolved are NOT automatically reinstated. A separate VERSECONTEXT or VCVERSE patch is required to reinstate those verses.

\---

## 9\. VCVERSE Patch — Targeted Verse Update

Use when a single verse changes state: a new verse was added after audit\_word re-run, a verse was removed, or a reclassification is needed outside a full batch run.

### 9.1 Input required from Claude Code

```json
{
  "verse": {
    "verse\_record\_id": 0,
    "reference": "{Book Ch:V}",
    "verse\_text": "{current text}",
    "target\_word": "{text}",
    "span\_strong\_match": 1,
    "verse\_delete\_flagged": 0,
    "mti\_term\_id": 0
  },
  "existing\_verse\_context": {
    "id": 0,
    "group\_id": 0,
    "group\_code": "{text}",
    "is\_anchor": 0,
    "is\_relevant": 0,
    "is\_related": 0,
    "notes": null,
    "delete\_flagged": 0
  },
  "available\_groups": \[
    {
      "id": 0,
      "group\_code": "{text}",
      "context\_description": "{text}",
      "anchor\_count": 0,
      "delete\_flagged": 0
    }
  ]
}
```

`existing\_verse\_context` is null if no record exists yet.

**Source tables for VCVERSE input:**

|Field|Source|
|-|-|
|verse.verse\_record\_id|wa\_verse\_records.id|
|verse.reference|wa\_verse\_records.reference|
|verse.verse\_text|wa\_verse\_records.verse\_text|
|verse.target\_word|wa\_verse\_records.target\_word|
|verse.span\_strong\_match|wa\_verse\_records.span\_strong\_match|
|verse.verse\_delete\_flagged|wa\_verse\_records.delete\_flagged|
|verse.mti\_term\_id|wa\_verse\_records.mti\_term\_id|
|existing\_verse\_context|verse\_context WHERE verse\_record\_id = vr.id AND mti\_term\_id = {mti\_term\_id} (NULL object if no row exists)|
|existing\_verse\_context.group\_code|verse\_context\_group.group\_code (JOIN via verse\_context.group\_id → verse\_context\_group.id)|
|available\_groups|verse\_context\_group WHERE mti\_term\_id = {mti\_term\_id} AND delete\_flagged = 0|

### 9.2 Three scenarios

**Scenario A — New verse, first-time classification:**
Use `insert` operation. Assign to an existing group if it fits; insert new group first if needed.

**Scenario B — Verse removed (`wa\_verse\_records.delete\_flagged` set to 1):**

```json
{
  "op\_id": "OP-001",
  "operation": "update",
  "table": "verse\_context",
  "match": { "id": 0 },
  "set": { "delete\_flagged": 1 },
  "description": "{Book Ch:V} — verse removed from active set, flagging verse\_context record"
}
```

If the verse was an anchor: include a second operation promoting another related verse in the same group to anchor status. If no related verses remain active in the group, include a note flagging that the group has no anchor — researcher decision required before Session B proceeds.

**Scenario C — Reclassify existing verse:**
Use `update` operation on the existing verse\_context id. Include notes explaining the reason for reclassification. Maintain anchor integrity.

### 9.3 Patch naming

`PATCH-{YYYYMMDD}-VCVERSE{verse\_record\_id}-V1`

\---

## 10\. Researcher Compliance Rules

|**⚠ Do not make assumptions or guesses. When uncertain about whether a verse passes the relevance filter, retain the verse, note the uncertainty, and proceed. Do not stop the session for borderline filter decisions — batch uncertainty questions at the end of each term's classification and present them together.**|
|-|

Additional rules:

* Do not develop analytical conclusions about terms during Verse Context — that is Session B
* Do not draw cross-registry connections during Verse Context — that is Session D
* Do not assign evidential status — that is Session B DataPrep and Analysis
* Context descriptions must be grounded in what the verses show — not in prior theological knowledge about the term
* Dual-context is rare — only when two distinct inner-being engagements are plainly evident. Do not use it to resolve interpretive difficulty
* All corrections are UPDATE operations — never produce delete + reinsert
* The anchor integrity rule is absolute — a term must retain at least one active anchor at all times

\---

## 11\. Claude Code — Patch Application Protocol

### 11.1 Apply in single transaction

All operations in a VERSECONTEXT patch apply as one transaction — all or nothing.

### 11.2 Group\_code resolution

For each `verse\_context\_group` insert: after the insert executes, capture `last\_insert\_rowid()`. Store this mapping: `group\_code → integer id`. Apply this mapping to all subsequent `verse\_context` inserts in the same patch that reference this group\_code as their group\_id value.

### 11.3 Consistency rule validation

Run after every patch application:

```sql
-- R1: set-aside rows clean
SELECT COUNT(\*) FROM verse\_context
WHERE is\_relevant=0 AND (group\_id IS NOT NULL OR is\_anchor=1 OR is\_related=1);
-- Expected: 0

-- R2: anchor rows clean
SELECT COUNT(\*) FROM verse\_context
WHERE is\_anchor=1 AND (is\_relevant=0 OR is\_related=1 OR group\_id IS NULL);
-- Expected: 0

-- R3: related rows have an active anchor in their group
SELECT COUNT(\*) FROM verse\_context vc
WHERE is\_related=1 AND NOT EXISTS (
  SELECT 1 FROM verse\_context a
  WHERE a.group\_id=vc.group\_id AND a.is\_anchor=1 AND a.delete\_flagged=0);
-- Expected: 0
```

Any violation: report to researcher. Do not advance registry status until violations resolved.

### 11.4 Anchor integrity check

After any patch affecting anchor status, for each affected term:

```sql
SELECT COUNT(\*) as active\_anchors FROM verse\_context
WHERE mti\_term\_id = {mti\_term\_id} AND is\_anchor = 1 AND delete\_flagged = 0;
-- If 0: flag to researcher — term has no anchor and cannot proceed to Session B
```

### 11.5 Re-extraction trigger and reset requirement

**Pre-extraction REPAIR patch required:** Before any audit\_word re-run for a registry, a REPAIR patch must be applied to reset the registry state. This patch must be applied and confirmed before audit\_word runs. No re-extraction may proceed without it.

The REPAIR patch resets:

* `word\_registry.session\_b\_status` → `Verse Context Reset`
* `word\_registry.verse\_context\_status` → `In Progress`
* All `verse\_context` records for this registry's OWNER terms → `delete\_flagged = 1`
* All `verse\_context\_group` records for this registry's OWNER terms → `delete\_flagged = 1`
* All Session B analytical outputs (wa\_session\_b\_dimensions, wa\_session\_b\_findings, wa\_session\_research\_flags SD\_POINTER records, wa\_term\_inventory.evidential\_status) for this registry → cleared

The REPAIR patch naming convention: `PATCH-{YYYYMMDD}-{nnn}-REPAIR-AUDITWORD-RERUN-V1`
Full patch specification: WA-PipelineStatusReview-v2-20260330 Section 3.2.

**Claude Code expectation — audit\_word routine:** Claude Code must build the following into the audit\_word re-run routine. When audit\_word detects it is re-running for a registry that already has data (i.e. wa\_term\_inventory records exist for this registry), the routine must:

1. Verify the REPAIR patch has been applied (check patch history for REPAIR-AUDITWORD-RERUN on this registry). If not applied: halt with error — do not proceed.
2. On re-run, the STALE\_TERM mechanism (Step A6) handles wa\_term\_inventory updates — it compares the incoming JSON against existing records and applies only the delta. This is the authoritative mechanism for updating term inventory on re-run. No separate delete/re-insert of wa\_term\_inventory records is required.
3. After audit\_word completes, re-export the full word JSON (Step A11). The re-export confirms the updated state for the next pipeline stage (Verse Context).

**Post-audit\_word detection (existing check retained):**

After every audit\_word re-run, check for OWNER terms with verse records that have no corresponding verse\_context entry:

```sql
SELECT DISTINCT mt.id, mt.strongs\_number, mt.owning\_registry\_fk
FROM wa\_verse\_records vr
JOIN wa\_term\_inventory ti ON ti.id = vr.term\_inv\_id
JOIN mti\_terms mt ON mt.id = vr.mti\_term\_id
WHERE ti.term\_owner\_type = 'OWNER' AND vr.delete\_flagged = 0
  AND NOT EXISTS (
    SELECT 1 FROM verse\_context vc
    WHERE vc.verse\_record\_id = vr.id AND vc.mti\_term\_id = mt.id
  );
```

For each term returned: set owning registry `verse\_context\_status = 'In Progress'`. Report to researcher.

Cascade delete\_flag from verse records to verse\_context when a verse is flagged:

```sql
UPDATE verse\_context SET delete\_flagged = 1
WHERE verse\_record\_id IN (SELECT id FROM wa\_verse\_records WHERE delete\_flagged = 1)
  AND delete\_flagged = 0;
```

**Claude Code expectation — Verse Context batch preparation routine:** When Claude Code prepares a Verse Context batch for a registry that previously had verse\_context records (i.e. this is a re-run after a reset), the batch preparation routine must:

1. Confirm that all verse\_context and verse\_context\_group records for this registry's OWNER terms are delete\_flagged (the REPAIR patch should have done this — verify before constructing the batch).
2. Treat the registry as a fresh start — do not carry forward any prior contextual groupings into the new batch JSON. The batch JSON's `existing\_groups` array for each term must reflect only active (delete\_flagged = 0) groups — which after the reset will be empty.
3. Re-assess the wa\_term\_inventory records for this registry: confirm that mti\_terms.status values are still appropriate (extracted/extracted\_thin) after the audit\_word re-run. If any terms now have NULL status (new terms added by the re-run), flag these to researcher for DataPrep re-classification before Verse Context proceeds.

\---

## 12\. Claude Code — Integrity Validation

Run after every patch application cycle:

```sql
-- Terms with delete/excluded status should have no active verse\_context rows
SELECT mt.strongs\_number, mt.status, COUNT(vc.id) as active\_vc\_rows
FROM mti\_terms mt
JOIN verse\_context vc ON vc.mti\_term\_id = mt.id
WHERE mt.status IN ('delete','excluded') AND vc.delete\_flagged = 0
GROUP BY mt.id;
-- Expected: zero rows. Any result is an integrity violation — report to researcher.
```

\---

## 13\. Claude Code — Registry Completion Check and Re-export

Run after every VERSECONTEXT patch, for each registry whose OWNER terms appear in the batch.

### 13.1 OWNER term completion check

```sql
SELECT COUNT(\*) as unclassified\_owner\_terms
FROM wa\_term\_inventory ti
JOIN wa\_file\_index fi ON fi.id = ti.file\_id
JOIN word\_registry wr ON wr.id = fi.word\_registry\_fk
JOIN mti\_terms mt ON mt.strongs\_number = ti.strongs\_number
WHERE wr.no = {registry\_no}
  AND ti.term\_owner\_type = 'OWNER' AND ti.delete\_flagged = 0
  AND mt.status IN ('extracted','extracted\_thin')
  AND EXISTS (
    SELECT 1 FROM wa\_verse\_records vr
    WHERE vr.term\_inv\_id = ti.id AND vr.delete\_flagged = 0
  )
  AND NOT EXISTS (
    SELECT 1 FROM verse\_context vc
    WHERE vc.mti\_term\_id = mt.id AND vc.delete\_flagged = 0
  );
-- If 0: all OWNER terms with verses are classified
```

### 13.2 XREF coverage check

```sql
-- XREF terms in this registry whose OWNER has not yet been classified
SELECT COUNT(\*) as unresolved\_xref\_terms
FROM wa\_term\_inventory ti
JOIN wa\_file\_index fi ON fi.id = ti.file\_id
JOIN word\_registry wr ON wr.id = fi.word\_registry\_fk
JOIN mti\_terms mt ON mt.strongs\_number = ti.strongs\_number
WHERE wr.no = {registry\_no}
  AND ti.term\_owner\_type = 'XREF'
  AND ti.delete\_flagged = 0
  AND NOT EXISTS (
    SELECT 1 FROM verse\_context vc WHERE vc.mti\_term\_id = mt.id AND vc.delete\_flagged = 0
  );
-- If 0: all XREF terms have OWNER classification available
```

### 13.3 Advancing status and re-exporting

When both checks return 0 for a registry:

```sql
UPDATE word\_registry SET verse\_context\_status = 'Complete' WHERE no = {registry\_no};
```

**Double-check verification (G06-F):** Immediately after writing `verse\_context\_status = Complete`, re-run both the OWNER completion check (Section 13.1) and the XREF coverage check (Section 13.2) for this registry. If either returns a non-zero count:

* Reverse the status write: `UPDATE word\_registry SET verse\_context\_status = 'In Progress' WHERE no = {registry\_no};`
* Report the inconsistency to the researcher with the query results showing what remains unclassified.
* Do not proceed with re-export until the inconsistency is resolved.

If both checks confirm zero: proceed with re-export.

Then immediately re-export the full word JSON:

```bash
python -m engine.engine --export-word --registry={registry\_no}
```

This produces a fresh `wa-{nnn}-{word}-extract-{date}.json` carrying `verse\_context\_status = Complete` in its meta. **This re-export is what opens the DataPrep gate.** DataPrep reads this file, sees `verse\_context\_status = Complete`, and proceeds.

**Note on session\_b\_status:** This process does not update `session\_b\_status`. The value `Ready for Analysis` in the session\_b\_status vocabulary is set by `audit\_word` (using COALESCE — only when current status is NULL), not by any Verse Context operation. The DataPrep gate check (wa-sessionb-analysis-readiness [current] Section 4.1) gates on `verse\_context\_status = Complete` — it does not require `session\_b\_status = Ready for Analysis`. No session\_b\_status write is needed here.

### 13.4 Completion report to researcher

For each registry reaching Complete, report:

```
Registry {nnn} — {word}:
  OWNER terms classified: {n} / {total}
  XREF terms covered: {n} (via OWNER classifications in registries: {list})
  verse\_context\_status: Complete
  Re-export: wa-{nnn}-{word}-extract-{date}.json produced
  Ready for: Session B DataPrep
```

For each registry remaining In Progress after this batch (partial registry split), report:

```
Registry {nnn} — {word}:
  OWNER terms classified this batch: {n}
  OWNER terms remaining: {n} (to be included in VCB-{next\_batch\_id})
  verse\_context\_status: In Progress — continuation expected
```

After all per-registry reports for this batch, produce a batch-level summary:

```
BATCH {batch\_id} COMPLETION SUMMARY

Registries in this batch: {n}
  Reached Complete this batch: {n} — {list: nnn—word}
  Still In Progress: {n} — {list: nnn—word, reason}
    Of which: partial split (continuation in next batch): {n}
    Of which: all-verses-fail or other pending decision: {n}

Programme-wide Stage 1 progress:
  verse\_context\_status = Complete: {n} / 181 registries
  verse\_context\_status = In Progress: {n} registries
  Unclassified OWNER terms remaining: {n}
```

\---

## 14\. Stage 1 Completion

Stage 1 is complete when all 181 active registries have `verse\_context\_status = Complete`.

### 14.1 Monitoring query

```sql
SELECT verse\_context\_status, COUNT(\*) as count
FROM word\_registry
WHERE session\_b\_status IS NOT NULL
GROUP BY verse\_context\_status;
-- Target: Complete = 181, In Progress = 0, NULL = 31 (excluded)
```

### 14.2 Stage 1 completion report

When the monitoring query shows Complete = 181, Claude Code produces the Stage 1 completion report:

```
STAGE 1 — VERSE CONTEXT SWEEP COMPLETE

Date: {yyyy-mm-dd}
Batches processed: {n} (VCB-001 through VCB-{nnn})

Summary:
  Registries classified: 181 / 181
  verse\_context\_group records created: {n}
  verse\_context records created: {n}
    - Anchor verses: {n}
    - Related verses: {n}
    - Set aside: {n}
  OWNER terms classified: {n}
  XREF terms covered: {n}

All 181 registries are now at verse\_context\_status = Complete.
All re-exports are current.

Programme state:
  session\_b\_status = Verse Context Reset: 181 registries
  verse\_context\_status = Complete: 181 registries
  DataPrep gate: OPEN for all 181 registries

Stage 2 — Session B Analysis may now begin.
Processing sequence: per pool/cluster batch order in wa-registry-management-guide [current] Section 7.
```

### 14.3 What happens next

After Stage 1 completion, the programme moves to Stage 2 — Session B Analysis. Processing proceeds in pool/cluster batch order as defined in wa-registry-management-guide [current] Section 7. The governing instruction for each stage is:

|Stage|Governing instruction|
|-|-|
|Session B Analysis Readiness|wa-sessionb-analysis-readiness [current]|
|Session B Analysis Output|wa-sessionb-analysis-output [current]|
|(Session B Extraction — retired, content folded into Analysis Output)|—|

DataPrep is triggered per registry as registries reach `verse\_context\_status = Complete`. It does not wait for all 181 to complete — registries that complete Verse Context early can begin DataPrep immediately.

\---

## Annexure A — Startup Summary Template

```
Verse Context v1.8 startup complete.
Batch: {batch\_id}
Governing instruction: WA-VerseContext-Instruction-v1.8-20260331.md

Terms in batch: {n}
Total verses: {n} | Unclassified: {n} | Previously classified: {n}

Term inventory:
  {strongs\_number} ({transliteration}) — {gloss} — {n} verses ({n} unclassified)
    OWNER for: {owning\_word} (registry {owning\_registry\_id})
    Existing groups: {n} | Previously classified verses: {n}
  \[repeat for each term]

Notes on previously classified terms:
  {list any terms with term\_classification\_complete: true and whether revision seems warranted}

Ready to proceed. Beginning with {first\_strongs\_number} ({transliteration}).
```

\---

## Annexure B — Per-Term Classification Summary Template

```
Term: {strongs\_number} ({transliteration}) — {gloss}
mti\_term\_id: {integer}
OWNER for: {owning\_word} (registry {owning\_registry\_id})
Total verses: {n} | Relevant: {n} | Set aside: {n}

Groups:
  {group\_code} \[{new / existing}]: "{context\_description}"
    Anchors: {verse reference(s)}
    Related: {n} verses
    \[repeat for all groups]

Revisions to prior classifications: {n}
  {describe each: what changed and why}
Dual-context verses: {n}
  {describe each: what two engagements are present}
Borderline retained: {n}
  {list references and note uncertainty}
Anchor integrity: confirmed — {n} active anchors across {n} groups

Ready for patch.
```

\---

## Annexure C — VERSECONTEXT Patch Template

File naming: `wa-vcb-{batch\_id}-patch-{YYYYMMDD}.json`

```json
{
  "\_patch\_meta": {
    "patch\_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1",
    "batch\_id": "VCB-{nnn}",
    "produced\_date": "{yyyy-mm-dd}",
    "produced\_by": "WA-VerseContext-Instruction-v1.8",
    "session\_b\_status": null,
    "description": "Verse context classification — batch VCB-{nnn}, {n} terms, {n} verses"
  },
  "operations": \[
    {
      "op\_id": "OP-001",
      "operation": "insert",
      "table": "verse\_context\_group",
      "record": {
        "mti\_term\_id": 0,
        "group\_code": "{mti\_term\_id}-001",
        "context\_description": "{brief phrase}",
        "notes": null,
        "delete\_flagged": 0
      },
      "description": "Group 1 for {strongs\_number}: {context\_description}"
    },
    {
      "op\_id": "OP-002",
      "operation": "insert",
      "table": "verse\_context",
      "record": {
        "verse\_record\_id": 0,
        "mti\_term\_id": 0,
        "group\_id": "{mti\_term\_id}-001",
        "is\_anchor": 1,
        "is\_relevant": 1,
        "is\_related": 0,
        "notes": null,
        "delete\_flagged": 0
      },
      "description": "{Book Ch:V} — anchor, group {mti\_term\_id}-001: {context\_description}"
    },
    {
      "op\_id": "OP-003",
      "operation": "insert",
      "table": "verse\_context",
      "record": {
        "verse\_record\_id": 0,
        "mti\_term\_id": 0,
        "group\_id": "{mti\_term\_id}-001",
        "is\_anchor": 0,
        "is\_relevant": 1,
        "is\_related": 1,
        "notes": null,
        "delete\_flagged": 0
      },
      "description": "{Book Ch:V} — related, group {mti\_term\_id}-001"
    },
    {
      "op\_id": "OP-004",
      "operation": "insert",
      "table": "verse\_context",
      "record": {
        "verse\_record\_id": 0,
        "mti\_term\_id": 0,
        "group\_id": null,
        "is\_anchor": 0,
        "is\_relevant": 0,
        "is\_related": 0,
        "notes": null,
        "delete\_flagged": 0
      },
      "description": "{Book Ch:V} — set aside, no inner-being engagement for {strongs\_number}"
    }
  ],
  "\_patch\_summary": {
    "total\_operations": 4,
    "group\_inserts": 1,
    "group\_updates": 0,
    "verse\_context\_inserts": 3,
    "verse\_context\_updates": 0,
    "relevant\_verses": 2,
    "set\_aside\_verses": 1,
    "anchor\_verses": 1,
    "dual\_context\_verses": 0,
    "revisions\_to\_prior": 0
  }
}
```

\---

*wa-versecontext-instruction-v2_8-20260418 | Supersedes wa-versecontext-instruction-v2_7-20260414 | v2_8: GR-REF-002 sweep — filename current-conventions, operational cross-refs migrated to `[current]`*

*Historical: WA-VerseContext-Instruction-v2.2-20260401 | Supersedes v2.1-20260401 | v2.2: (1) Section 3.5 added: Relevance filter for grammatical and functional particles — pass criteria (directs/intensifies/qualifies scope/discloses inner orientation) and fail criteria (purely syntactic/social register/temporal connector/procedural) stated explicitly; (2) Section 6.2 Step 1: All-verses-fail rule rewritten — individual inspection is now explicitly non-waivable for all terms regardless of corpus size; researcher confirmation no longer required for full-corpus grammatical particles or confirmed homographs where individual inspection is complete*

