# WA-VerseContext-Instruction-v2_5-20260409

**Framework B — Soul Word Analysis Programme**
**Verse Context Instruction — Integrated Claude AI and Claude Code**
**Version 2.5 | April 2026 | Status: Active governing instruction**

| **Document** | **Value** |
|---|---|
| Filename | WA-VerseContext-Instruction-v2.5-20260409.md |
| Supersedes | WA-VerseContext-Instruction-v2.4-20260403.md |
| Change note | v2.5 — Two substantive additions arising from VCB-031 processing and the vertical pass experiment conducted in that session. (1) Section 2.2 (amended): `set_aside_reason` field added to `verse_context` table definition. The field captures the specific reason a verse is set aside (is_relevant = 0), using five controlled values: `no_inner_being` (term carries no inner-being content in this verse), `physical_only` (term refers to a physical process or body part with no inner engagement), `spatial_only` (term used in a locational/geographical sense), `wrong_face` (verse contains inner-being content but it is carried by a different term, not this one — the verse belongs to a different registry's face), `other` (set-aside reason does not fit the controlled categories — notes field must explain). The `wrong_face` value is the vertical-pass-enabling value: it flags verses that are analytically significant but belong to a different registry's perspective, enabling them to be rediscovered in future vertical pass sessions without re-reading the full corpus. Section 3.2 (amended): the four set-aside categories in the filter are now aligned with the controlled vocabulary. Section 3.6 (new): wrong-face set-aside procedure — definition, when to use it, rediscovery procedure. Section 7.3 (amended): set-aside patch record updated to include `set_aside_reason` field. Rationale: arose from VCB-031 vertical pass experiment on Jer 7:24, where H3820A lev ("their hearts") was absent from the verse's term links because mti=581 had been incorrectly deleted. The experiment also showed that even correctly classified set-asides from one registry's perspective may be analytically important from another registry's perspective — but this information was being lost at classification time because no mechanism existed to record it. The `wrong_face` value and rediscovery procedure preserve this information in the database for future analytical use. (2) Section 6.2 Step 3 (amended): grouping rule revised from term-centric to characteristic-perspective model. The previous rule asked what the term does in the verse; the revised rule asks what inner-being characteristic the verse cluster is primarily about. The distinction between characteristic terms (naming an inner-being state directly) and property terms (describing how characteristics operate — their mechanism, condition, or expression) is now explicit. A property term can serve different characteristics across its corpus and can serve the same characteristic in opposite ways. Group descriptions must name the inner-being characteristic that the verse cluster engages, with the term's role stated accurately relative to that characteristic. Rationale: arose from VCB-031 analysis of sha.ma (listen/hear) and o.zen (ear) — the error identified was that groups were being named after what the term does rather than what the verse is about. A group called "refusing to hear God" is term-centric; "heart-stubbornness expressed through refusal of God's word" is characteristic-perspective. The revision ensures that group descriptions at the Verse Context stage serve Session B analysis correctly, because Session B analyses characteristics — not term behaviours. Applies from VCB-032 onward. Four substantive additions arising from VCB-015 processing, which was the first batch to operate under the deferred flag protocol piloted in that session. Researcher assessment: "This method of working through the flags is infinitely better than in the past." Changes: (1) Section 6.2 Step 2 (amended): All-verses-fail rule and per-term stop rule replaced by the Deferred Flag Protocol. The previous rule required Claude AI to stop mid-classification for every borderline, all-verses-fail, or clarification need. Under the new protocol, all flags that do not block the classification of other verses are accumulated during classification and presented in a single interactive register at end-of-batch, with full context for each decision. The only condition that still triggers an immediate stop is a structural data integrity failure that would prevent correct classification of subsequent verses. All-verses-fail findings — regardless of verse count — are treated as deferred flags unless blocking. See Section 6.5 for the full protocol. Rationale: The previous rule produced fragmented mid-session interruptions with insufficient context for researcher decisions. The deferred protocol produces a single structured decision session where all flags receive full verse text, concrete patch consequences, and Claude AI assessment, enabling informed and consistent decisions. (2) Section 6.3 (amended): "After all terms are classified" now explicitly includes the end-of-batch flag resolution session as a mandatory step before patch preparation, and the production of the Session B flags document as a required output if any Session B flags were raised. (3) Section 6.5 (new): Deferred Flag Protocol — full specification of the flag accumulation, categorisation, presentation, and resolution process. Covers the flags register format, the two flag categories (deferred vs blocking), the decision context requirements, and the update of the observations file following researcher decisions. (4) Section 6.6 (new): Session B Flags — specification of the Session B flags document as a named pipeline output. Defines the document's purpose (carrying analytical insights from Verse Context classification into Session B analysis), its required content, naming convention, and position in the handoff chain. Outputs table and scope value table in Section 6.4 updated to include both new file types. v2.3 — Section 6.1 Step 6 (new): Processing order rule added. Terms are processed in registry sequence, ascending by registry number; within a registry, in batch JSON order. This order is fixed and does not require researcher confirmation at batch start. Rationale: established programme practice recurring across all batches; codified to eliminate repeated researcher queries. v2.2 — Two substantive additions arising from programme flags PF-VCB007-001 and PF-VCB007-002 raised during VCB-007 processing: (1) Section 3.5 (new): Relevance filter for grammatical and functional particles. Establishes the filter criterion for pronouns, quantifiers, conjunctions, and adverbs — a particle passes if it directs, intensifies, qualifies the scope of, or discloses an inner orientation through inner-being content; it does not pass if purely syntactic, social register, temporal connector, or procedural. Rationale: arose from classification of H4310 mi (interrogative pronoun) and H3605 kol (universal quantifier) in VCB-007, where the filter decision for grammatical terms required an explicit criterion that was absent from the instruction. (2) Section 6.2 Step 1 (amended): All-verses-fail rule expanded to remove the requirement for researcher confirmation in the case of full-corpus grammatical/functional terms. Where the classifier has individually inspected every verse in a large corpus and confirmed all fail (rather than sampling), the all-verses-fail finding may be submitted without researcher confirmation. The requirement for individual inspection of every verse is now explicit and non-waivable regardless of corpus size. Rationale: arose from VCB-007 classification of H1992 hem.mah (pronoun, 189 verses) and H4177 mo.rah (homograph, 3 verses) — both confirmed all-verses-fail by full inspection; the instruction was ambiguous about whether researcher confirmation was required when individual inspection was complete. | Three substantive changes arising from VCB-006 quality review: (1) Section 6.2 Step 6: observations file structure rules tightened — Classification blocks must use unique sequential group codes; mid-stream group revision must produce a clearly labelled revised block, not an additional block with the same code; the earlier draft block must be explicitly struck through or marked SUPERSEDED before the revision block. (2) Section 6.4: observations file write discipline strengthened — file must be written to disc and version-incremented after every term, not just at registry completion; the current file version number must be stated in every session log; Claude AI must confirm the version number aloud before writing each save. (3) Section 7.5 (new): Decision context requirement — when Claude AI raises a decision for the researcher during patch construction, it must supply: (a) the full verse text for every verse under consideration, (b) the group description the verse is being evaluated against, (c) the specific question being asked, (d) a clear statement of what each option means for the patch, and (e) Claude AI's own assessment of which option is analytically stronger and why. Researcher decisions must never be presented as bare option lists without this context. v2.0 — Section 3.4 added: Expressions as inner-being evidence. Establishes the programme-wide principle that where a term names a human act of expression, the relevance filter is satisfied if the act plausibly originates in an inner state. The direction of travel (inner state → outward expression) is itself inner-being data. The inner state need not be named explicitly in the verse. Pure mechanical acts with no plausible inner origin do not satisfy the filter. Rationale: arose from anchor resolution on H7121I (qa.ra call-out) in VCB-003 — the classification decision that all vocal calls plausibly originate in an inner state (urgency, distress, longing, outrage, devotion) revealed a gap in the instruction's explicit filter criteria. Researcher decision (RD-PC-001): "the inner being is like a machine — I don't want us to take some of the gears or pulleys out of the process." Major version increment: this is a substantive methodological change to the relevance filter, not a procedural update. Applies from VCB-004 onward; applied retrospectively to H7121I in VCB-003. v1.9 — Section 6.4: unified file naming convention added covering all Claude AI outputs (session logs, flag resolution, and any other batch-scoped files). All VCB-batch output files must follow the pattern `wa-vcb-{batch_id}-{scope}-{version}-{date}.{ext}`. Rationale: session logs and ancillary files were being named with mixed case and non-standard prefixes (e.g. `WA-SessionLog-VCB003-...`), breaking sort order and making batch-scoped files difficult to locate together. The convention is now stated explicitly for every file type Claude AI produces in a classification or patch session. v1.8 — Section 6.4: observations file versioning rule added. Filename convention updated to include version number (`v[major].[minor]`) between the description and the date: `wa-vcb-{batch_id}-term-observations-v{major}.{minor}-{date}.md`. Replaces the prior date-only convention. Rationale: in-place updates without renaming created ambiguity when multiple versions of a file coexisted; file size was the only differentiator, which is fragile and error-prone. The version number is now the progression signal; the creation date remains stable in the filename. Applies from VCB-003 onward. v1.7 — Lessons from VCB-001 processing. Section 5.2: registry split across batches explicitly documented as normal expected outcome. Section 6.3: renamed; new Section 6.4 added — session discipline rules (continuous file writing, session logs at natural breakpoints, no large in-memory accumulation; deferred patch construction documented as valid workflow with requirements). Section 7.2: `dual_context_verses` field clarified — counts verses not verse_context rows. Section 7.6: programmatic validation requirement added for large batches. Section 13.4: completion report template extended to include partial-registry progress and continuation batch. v1.6 — Internal version strings corrected throughout. No substantive content changes. v1.5 — Section 11.5: REPAIR patch requirement added. Section 13.3: double-check verification rule added. v1.4 — Section 5.2: SQL policy statement added. Section 6.1: all-verses-fail error rule, partial completion rule, revision documentation rule added. Section 6.2 Step 3: grouping criterion specified. |
| Companion documents | WA-VerseContext-SetupInstruction-v1.1 │ WA-Reference-v5.5 │ WA-VerseContext-ImpactStudy-v3 │ WA-SessionB-DataPrep-Instruction-v5.6 │ patch_specification-v1.6 |
| Inputs | Full word JSON exports — wa-{nnn}-{word}-extract-{date}.json (for batch construction) │ Verse Context batch JSON — wa-vcb-{batch_id}-extract-{date}.json (for Claude AI classification) |
| Outputs | Verse Context batch JSON — wa-vcb-{batch_id}-extract-{date}.json (Claude Code → Claude AI) │ Verse Context patch — wa-vcb-{batch_id}-patch-v{n}-{date}.json (Claude AI → Claude Code) │ Observations file — wa-vcb-{batch_id}-term-observations-v{major}.{minor}-{date}.md (Claude AI, progressive) │ Session log — wa-vcb-{batch_id}-session-log-{scope}-v{n}-{date}.md (Claude AI, at breakpoints) │ Flags register — wa-vcb-{batch_id}-flags-register-v{n}-{date}.md (Claude AI, end-of-batch flag resolution) │ Session B flags — wa-vcb-{batch_id}-sessionB-flags-v{n}-{date}.md (Claude AI, when Session B flags raised) │ Re-exported full word JSON per registry (Claude Code → DataPrep) |
| Claude AI role | Verse reading, relevance filtering, contextual grouping, anchor designation, patch production |
| Claude Code role | Batch JSON construction from full exports, patch application, group_code resolution, XREF status propagation, registry status management, integrity validation, completion reporting |
| Interaction model | Phase 1 exports → Claude Code constructs batch → Claude AI classifies → Claude Code applies patch, advances status, re-exports per-registry JSON → DataPrep gate opens |

---

## 0. Purpose and Scope

This document governs the Verse Context stage — the pipeline stage between Phase 1 completion and Session B DataPrep. It covers the full cycle: from the existing Phase 1 full word exports that serve as the source data, through batch construction, Claude AI classification, patch application, and the re-export that opens the DataPrep gate for each registry.

**What Verse Context does:**
- Uses the existing Phase 1 full word exports to identify which OWNER terms need classification
- Reads all verses for every active OWNER term programme-wide
- Filters each verse: does it engage the inner being through this term?
- Groups relevant verses by contextual meaning
- Designates anchor verses — the canonical citation and primary Session B analysis input per term
- Produces patches that Claude Code applies to populate `verse_context_group` and `verse_context`
- Advances `verse_context_status` to Complete per registry when all OWNER terms are classified
- Re-exports the full word JSON for each completed registry — the trigger for DataPrep

**What Verse Context does NOT do:**
- Analyse the meaning of terms in depth — that is Session B Analysis
- Draw conclusions about the word being studied — that is Session B Analysis
- Produce cross-registry synthesis — that is Session D
- Assign evidential status to terms — that is Session B Analysis
- Classify XREF terms directly — XREF status is derived from OWNER classification (see Section 0.2)

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
Session B DataPrep (verse_context_status = Complete triggers DataPrep gate)
     │
     ▼
Session B Analysis → Session B Extraction → Session D
```

| This document is self-standing. It does not rely on session memory. Claude Code requires this document and access to the database. Claude AI requires this document and the batch JSON export. |
|---|

---

## 0.1 Pipeline Entry Point — What Already Exists

**Before any Verse Context work begins, the following is already in place:**

Phase 1 (Session A) has run for all 181 active registries. Each registry has:
- A full word JSON export: `wa-{nnn}-{word}-extract-{date}.json` stored at `data/exports/`
- All OWNER terms extracted, verse records populated, mti_term_id links present
- `session_b_status = Verse Context Reset` (reset from prior states — intentional)
- `verse_context_status = In Progress` (set during setup — M18)
- `verse_context_group` and `verse_context` tables: empty (0 records — not yet processed)

**Claude Code uses the existing full word exports as the source for batch construction.** It does not re-query STEP or re-run audit_word at this point. The verse data is already in the database, confirmed by the Phase 1 audit. The full word exports are the visible representation of that data.

**What Claude Code reads from the database to construct a batch:**
- `mti_terms`: OWNER terms with status `extracted` or `extracted_thin`
- `wa_term_inventory`: confirms `term_owner_type = 'OWNER'` and `delete_flagged = 0`
- `wa_verse_records`: verse records for each OWNER term, `delete_flagged = 0`
- `verse_context`: existing records for any previously classified terms (to identify what still needs classification)

The batch JSON Claude Code produces is a structured subset of this data — formatted for Claude AI consumption. It is not the same as the full word export. See Section 5.2 for the batch JSON structure.

---

## 0.2 XREF Terms — How They Are Handled

XREF terms are not classified by Claude AI. Their verse_context status is derived from the OWNER term's completed classification. This section specifies exactly what Claude Code does with XREF terms.

**Background:** A XREF term is a Strong's number that appears in a registry's term inventory but whose primary analytical home (OWNER) is in a different registry. XREF verse records are delete_flagged — they are excluded from all analysis. The term identity (`mti_terms.id`) is shared across OWNER and XREF.

**Because verse_context uses `mti_term_id` (FK to `mti_terms.id`) as its key — not the term inventory id — the OWNER's verse_context records are automatically visible to any registry that shares that term.** There is no separate XREF verse_context record to create. The OWNER's classification is the programme-wide classification for that term.

**What Claude Code must do after every VERSECONTEXT patch:**

For each XREF term whose OWNER term appears in the completed batch:

1. Check whether the OWNER term now has `verse_context` records (i.e. has been classified in this or a prior batch)
2. If yes: the XREF term is considered covered — no verse_context insert needed. The XREF term's registry can query verse_context via `mti_term_id` and will see the OWNER's groups and classifications
3. Include this coverage in the completion check (Section 14.5): a registry is complete when all its OWNER terms are classified AND all its XREF terms have an OWNER that is classified

**What this means for the completion check:**
A registry's `verse_context_status` advances to Complete only when:
- All its OWNER terms (with verses) have `verse_context` records; AND
- All its XREF terms have an OWNER term that has `verse_context` records

This second condition ensures that Session B Analysis, when it reads the pool analysis dataset, will find complete contextual profiles for every term — both OWNER and XREF.

**Claude Code query to check XREF coverage for a registry:**
```sql
-- XREF terms in this registry whose OWNER has not yet been classified
SELECT DISTINCT mt.strongs_number, mt.owning_registry_fk, wr2.word as owner_word
FROM wa_term_inventory ti
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
JOIN word_registry wr2 ON wr2.id = mt.owning_registry_fk
WHERE wr.no = {registry_no}
  AND ti.term_owner_type = 'XREF'
  AND ti.delete_flagged = 0
  AND NOT EXISTS (
    SELECT 1 FROM verse_context vc WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
  );
-- If any rows returned: XREF terms unresolved — registry cannot advance to Complete yet
-- If zero rows: all XREFs covered — combine with OWNER check for complete assessment
```

**Reporting:** When Claude Code reports completion status, it must distinguish: "Registry {nnn} — {word}: OWNER classification complete, XREF coverage complete → verse_context_status set to Complete" vs "OWNER complete, {n} XREF terms pending OWNER classification in registries {list}".

---

## 1. The Two-System Model

| **System** | **Role** |
|---|---|
| Claude AI | Reads verse text. Applies the relevance filter. Produces contextual meaning descriptions. Groups verses. Designates anchors. Identifies dual-context. Produces the patch file. |
| Claude Code | Reads full exports and database to construct batch JSONs. Applies verse context patches. Resolves group_code to integer id. Handles XREF coverage. Updates registry verse_context_status. Re-exports full word JSONs. Validates consistency rules. Runs integrity checks. Reports completion. Does not assess verse relevance or produce contextual descriptions. |

| **⚠ Claude Code does not assess verse relevance, produce contextual meaning descriptions, or designate anchors. All classification is Claude AI's responsibility.** |
|---|

---

## 2. Database Tables

### 2.1 `verse_context_group`

| Field | Type | Notes |
|---|---|---|
| id | INTEGER PK | Used for all joins — never use group_code as join key |
| mti_term_id | INTEGER FK | → mti_terms.id — programme-wide term identifier, not registry-specific |
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
| set_aside_reason | TEXT | NULL if is_relevant = 1. Controlled vocabulary when is_relevant = 0 — see below. |
| notes | TEXT | Dual-context flags, borderline notes, revision reasons |
| delete_flagged | INTEGER | 0 = active; 1 = excluded (no physical deletes) |

**`set_aside_reason` controlled vocabulary** (applies when `is_relevant = 0` only):

| Value | Meaning |
|---|---|
| `no_inner_being` | The term carries no inner-being content in this verse — the verse as a whole may or may not have inner-being content but this term does not carry it here |
| `physical_only` | The term refers to a physical process, body part, or material object with no inner-being engagement |
| `spatial_only` | The term is used in a locational or geographical sense with no inner-being engagement |
| `wrong_face` | The verse contains inner-being content, but that content is carried by a different term — not by the term being classified. This verse belongs to another registry's analytical face. See Section 3.6 for the rediscovery procedure. |
| `other` | The set-aside reason does not fit the above categories. The `notes` field must explain. |

**Rule:** `set_aside_reason` must be populated for every `is_relevant = 0` record from VCB-032 onward. It must be `NULL` for every `is_relevant = 1` record. The `wrong_face` value is the vertical-pass-enabling value — it marks verses that have analytical significance for a different registry's perspective, preserving that information for future rediscovery without re-reading the full corpus. Pre-VCB-031 set-aside records with `set_aside_reason = NULL` are a known gap; they will be populated in a future programme-wide audit if needed.

**Uniqueness:** UNIQUE on (verse_record_id, mti_term_id, group_id). Same verse may appear under two groups for the same term (dual-context). Never twice in the same group.

**Programme-wide key:** `mti_term_id` is the same integer regardless of which registry views the term. OWNER and XREF registries query the same verse_context records via this key.

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

- **Purely physical use** (`physical_only`) — the term refers to a body part, physical process, or material object with no inner-being engagement
- **Purely social or narrative** (`no_inner_being`) — external conduct or events with no window into the inner life through this term
- **Purely positional or geographical** (`spatial_only`) — locating something in space or time
- **Wrong face** (`wrong_face`) — the verse contains inner-being content, but that content is carried by a different term, not by the term being classified. See Section 3.6.

When setting a verse aside, record the appropriate `set_aside_reason` value from Section 2.2 in the patch. Do not leave `set_aside_reason` null for any set-aside record from VCB-032 onward.

| **⚠ Apply the filter to the term's specific use in this verse — not to the verse's general theme. A verse about covenant renewal may use the term in a purely legal sense with no inner-being engagement for this specific term. Filter at term level, not verse level.** |
|---|

### 3.3 Borderline cases

Where the filter decision is genuinely uncertain: retain (is_relevant = 1) and record the uncertainty in the notes field. The cost of a missed inclusion is higher than the cost of retaining an uncertain verse. Batch uncertainty questions at the end of each term's classification — do not stop mid-term.

### 3.4 Expressions as inner-being evidence

Where a term names a human act of expression — vocal, physical, or behavioural — the relevance filter is satisfied if the act plausibly originates in an inner state rather than being purely mechanical or reflexive. The direction of travel (inner state → outward expression) is itself inner-being data. The inner state need not be named explicitly in the verse; its presence may be inferred from the nature and force of the expression.

**What this means in practice:**
- A cry, call, or shout that carries urgency, distress, longing, outrage, or devotion passes the filter — even if the verse does not name an inner state explicitly. The force and character of the expression implies its inner origin.
- A groan, gesture, or act of worship passes when the expression plausibly reflects an inward disposition rather than a trained reflex or mechanical procedure.
- Administrative, liturgical, or physical acts with no personally engaged human agent (a procedure to be followed, a reflex without agent) do not pass on this basis alone.

**Rationale:** The inner being is the origin of human expression. Separating the expression from its inner origin would remove part of the causal chain from view. Every human act of expression originates somewhere in the person; the nature of that origination is significant inner-being data.

**Boundary:** This principle applies where the term itself names the act of expression, not merely a verse that happens to contain an expressive act. The term must carry the expression for Section 3.4 to apply.

**Where the distinction is uncertain:** retain (Section 3.3 applies).

*Programme note: This principle was established as RD-PC-001 during VCB-003 patch construction, arising from classification of H7121I (qa.ra call-out). It applies from VCB-004 onward and was applied retrospectively to H7121I in VCB-003.*

---

### 3.5 Grammatical and functional particles

Where a term is a grammatical or functional particle — including pronouns, quantifiers, interrogatives, conjunctions, adverbs, particles of entreaty, and similar grammatical elements — the relevance filter requires an explicit assessment of how the particle functions in the specific verse, not merely whether the verse contains inner-being content.

**A grammatical particle passes the filter if it:**
- **Directs** inner-being content — orients a question, command, or assertion toward an inner-being subject (e.g. an interrogative pronoun framing a question about inner identity or moral worth)
- **Intensifies** an inner-being state or act — amplifies, sharpens, or emphasises the force of an inner-being expression
- **Qualifies the scope** of an inner-being condition — universalises, restricts, or otherwise shapes what an inner-being statement covers (e.g. a quantifier applied to a moral condition)
- **Discloses an inner orientation** through the manner in which it frames inner-being content — e.g. a particle of entreaty that reveals the posture of the speaker before God

**A grammatical particle does not pass the filter if it is:**
- **Purely syntactic** — present as a grammatical requirement with no semantic contribution to inner-being content
- **A social register marker** — indicating politeness, courtesy, or social function without inner-being implication
- **A temporal connector** — linking events or states in time without contributing to the inner-being dimension
- **Procedural filler** — serving a formal function in legal, liturgical, or administrative text with no personal inner-being engagement

**The test:** Remove the particle from the verse mentally. Does the inner-being content change meaningfully in how it engages the inner being? If the particle's presence shapes, frames, or intensifies that engagement, it passes. If the inner-being content is identical with or without the particle, it does not.

**Where the distinction is uncertain:** retain (Section 3.3 applies).

*Programme note: This section was added in v2.2, arising from programme flags PF-VCB007-001. It applies from VCB-008 onward. Applicable retrospectively to VCB-007 classifications of H4310 mi and H3605 kol, which were classified under this criterion during VCB-007 processing even before it was formally codified.*

---

### 3.6 Wrong-face set-asides

A verse is a **wrong-face set-aside** when it contains genuine inner-being content — but that content is carried by a different term in the verse, not by the term currently being classified. The verse is analytically significant; it simply does not belong to this term's classification face.

**Examples:**
- Jer 7:24: "they walked in the stubbornness of their evil hearts" — when classifying *sha.ma* (hear/listen), the inner-being content is carried by *lev* (heart) and *she.ri.rut* (stubbornness), not by *sha.ma*. The refused hearing is a consequence of the stubborn heart, not the inner-being subject. Set aside for *sha.ma* with `set_aside_reason = 'wrong_face'`.
- A verse about forgiveness where *ne.phesh* (soul) carries the inner-being content but the term being classified is a grammatical particle present in the same verse.

**When to use `wrong_face`:**
- The verse passes the general relevance question ("does this verse contain inner-being content?") — yes
- The term-specific relevance question ("does this term carry the inner-being content?") — no
- The inner-being content in the verse is identifiably carried by a different term with its own registry

**When not to use `wrong_face`:**
- The verse simply has no inner-being content at all — use `no_inner_being`, `physical_only`, or `spatial_only`
- The term partially carries the inner-being content (even weakly) — retain rather than set aside (Section 3.3)

**Patch treatment:**
Set aside normally (is_relevant = 0, group_id = null). Set `set_aside_reason = 'wrong_face'`. In the `notes` field, identify which term carries the inner-being content and which registry it belongs to, where known: e.g. `"wrong_face: inner-being content carried by lev (H3820A, Reg 183)"`.

**Rediscovery procedure:**
When a future analytical session (vertical pass, Session B cross-registry review, or programme audit) examines a verse across multiple registry faces, wrong-face set-asides are queryable:

```sql
SELECT vc.verse_record_id, vc.mti_term_id, vc.notes, vr.verse_text
FROM verse_context vc
JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
WHERE vc.set_aside_reason = 'wrong_face'
  AND vc.mti_term_id = {target_mti_term_id};
```

This returns all verses set aside as wrong-face for a given term — i.e. verses where the term is present but the inner-being content belongs to a different face. The `notes` field identifies which term carries the content, enabling cross-registry analysis.

*Programme note: This section was added in v2.5, arising from VCB-031 vertical pass experiment. The `wrong_face` value enables the vertical pass model to be applied to the existing VC classification corpus without re-reading every verse. Applies from VCB-032 onward.*

---

**Dual purpose:**
1. **Efficiency instrument** — Session B Analysis reads anchor verses, not the full verse corpus. Verse Context reduces 133,353 active verses to a small set of anchors that carry the essential inner-being content for each term.
2. **Citation instrument** — anchor verses appear in Session B narratives and Session D synthesis as the evidential foundation for claims about the term

**Selection criteria:**
- Makes the contextual meaning evident without requiring surrounding context
- The term's inner-being function is unambiguous in the verse
- Stands alone as evidence — does not depend on interpretation of adjacent passages

**Minimum requirement:** every term must have at least one active anchor across all its groups (Rule R4). A term with no anchor cannot proceed to Session B Analysis. This is an absolute gate — Claude Code enforces it in the completion check.

**Quantity:** 1–2 anchors per group. Where two are designated, they represent distinct aspects of the group's meaning. Do not designate more than 2 unless a third genuinely adds something the first two do not.

**When no clear anchor exists:** if a group's verses are all contextually dependent (require surrounding passage to make sense), designate the least dependent one as the anchor and note the limitation. Do not leave a group without an anchor.

---

## 5. Claude Code — Batch JSON Construction

### 5.1 Trigger

Claude Code constructs a new batch:
- When Stage 1 begins (first batch)
- After each VERSECONTEXT patch is applied and completion checks run (subsequent batches)
- When researcher instructs a manual batch construction

### 5.2 Batch construction criteria

- **OWNER terms only** — `wa_term_inventory.term_owner_type = 'OWNER'`
- **Active terms only** — `mti_terms.status IN ('extracted', 'extracted_thin')`
- **Terms with verses only** — at least one `wa_verse_records` record where `delete_flagged = 0`
- **Unclassified or incomplete terms first** — terms with no existing `verse_context` records, ordered by `mti_terms.owning_registry_fk` ascending (keeps terms from the same registry together where possible)
- **Target size** — accumulate terms until the count of unclassified verses (verses with no verse_context record) reaches 2,000–2,500
- **Never split a term** — all verses for a term must appear in one batch; if adding a term would exceed 2,500 verses, exclude it and start it in the next batch
- **Batch ID** — sequential: VCB-001, VCB-002 etc.

**Registry split across batches — expected behaviour:** Because the 2,000–2,500 verse target is applied at term level, a registry with many terms may not be fully included in a single batch. When a batch closes before all OWNER terms of a registry have been classified, the registry remains at `verse_context_status = In Progress`. Its remaining terms are picked up in the next batch. This is the normal expected outcome — it is not an error condition. The registry completion check (Section 13) will correctly advance the registry to Complete only when all its OWNER terms have verse_context records. Claude Code must report partial registries in the batch completion summary (Section 13.4) with the count of terms classified and terms remaining, so the researcher can confirm the split is working correctly.

**SQL policy:** SQL query construction for batch assembly is Claude Code's responsibility. This section provides all criteria, field names, derivation rules, and expected outcomes required. Claude Code constructs the accumulation query from these specifications and the database schema. An unclassified verse is any wa_verse_records record (delete_flagged = 0) for an OWNER term that has no corresponding verse_context record for that mti_term_id.

### 5.3 Batch JSON structure

The batch JSON contains all data Claude AI needs to classify verses — verse text, term identity, and the full state of any prior classifications for these terms.

```json
{
  "batch_id": "VCB-{nnn}",
  "produced_date": "{yyyy-mm-dd}",
  "produced_by": "Claude Code — WA-VerseContext-Instruction v1.8",
  "governing_instruction": "WA-VerseContext-Instruction-v1.8-20260331.md",
  "total_verse_count": 0,
  "total_term_count": 0,
  "unclassified_verse_count": 0,
  "verse_context_summary": {
    "total_verses_in_batch": 0,
    "previously_classified": 0,
    "unclassified": 0,
    "set_aside_in_prior_batches": 0,
    "anchor_verses_existing": 0
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
      "unclassified_count": 0,
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
          "verse_text": "{full ESV text}",
          "target_word": "{the specific word form occurring in this verse}",
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

**Source tables for batch JSON construction:**

| Field | Source |
|---|---|
| mti_term_id | mti_terms.id |
| strongs_number | mti_terms.strongs_number |
| transliteration | mti_terms.transliteration |
| gloss | mti_terms.gloss |
| language | mti_terms.language |
| mti_status | mti_terms.status |
| term_owner_type | wa_term_inventory.term_owner_type (WHERE delete_flagged = 0) |
| owning_registry_id | mti_terms.owning_registry_fk |
| owning_registry_word | word_registry.word (JOIN via mti_terms.owning_registry_fk → word_registry.id) |
| registry_verse_context_status | word_registry.verse_context_status (JOIN via owning_registry_fk) |
| total_verses | COUNT(wa_verse_records WHERE term_inv_id = ti.id AND delete_flagged = 0) |
| unclassified_count | COUNT(wa_verse_records WHERE term_inv_id = ti.id AND delete_flagged = 0 AND NOT EXISTS (SELECT 1 FROM verse_context WHERE verse_record_id = vr.id AND mti_term_id = mt.id)) |
| existing_groups | verse_context_group WHERE mti_term_id = mt.id (ALL rows including delete_flagged = 1) |
| existing_groups.anchor_count | COUNT(verse_context WHERE group_id = vcg.id AND is_anchor = 1 AND delete_flagged = 0) |
| existing_groups.related_count | COUNT(verse_context WHERE group_id = vcg.id AND is_related = 1 AND delete_flagged = 0) |
| verses | wa_verse_records WHERE term_inv_id = ti.id (ALL rows including delete_flagged = 1 for revision history) |
| verses.verse_context | verse_context WHERE verse_record_id = vr.id AND mti_term_id = mt.id (NULL object if no record) |
| term_classification_complete | true if COUNT(wa_verse_records WHERE term_inv_id = ti.id AND delete_flagged = 0 AND NOT EXISTS (SELECT 1 FROM verse_context WHERE verse_record_id = vr.id AND mti_term_id = mt.id AND delete_flagged = 0)) = 0 |

**Notes on field population:**

- `verse_context` field on each verse: set to `null` as a JSON object if no verse_context record exists for this `verse_record_id` + `mti_term_id` combination. Populate all fields when a record exists, including `delete_flagged` — Claude AI needs to see the full history including dissolved records.
- `existing_groups`: include ALL groups for the term regardless of `delete_flagged` — Claude AI needs to see dissolved groups to avoid duplicating their meaning in a new group.
- `term_classification_complete`: set to `true` only if every verse for this term already has a non-flagged verse_context record. If `true`, Claude AI should review rather than re-classify from scratch.
- `verses`: include ALL verse records for the term, classified and unclassified alike — Claude AI may revise prior classifications.

### 5.4 Output file

`wa-vcb-{batch_id}-extract-{date}.json`

Stored at `data/exports/verse_context/` (or equivalent batch export directory). Provided to Claude AI for the classification session.

---

## 6. Claude AI — Classification Workflow

### 6.1 Startup

On receiving the batch JSON:

1. Read this instruction document in full (or confirm it is already loaded for this session)
2. Load and parse the batch JSON
3. State the startup summary (Annexure A template)
4. Note any terms marked `term_classification_complete: true` — review these but do not re-classify unless a revision is clearly warranted (see revision rule in Step 2 below)
5. Note any terms with existing verse_context records but term_classification_complete = false — these are partially classified and must be flagged to researcher before continuing (see partial completion rule in Step 2 below)
6. **Processing order:** Terms are processed in registry sequence, ascending by registry number. Within a registry, terms are processed in the order they appear in the batch JSON. This order is fixed and does not require researcher confirmation at batch start.

### 6.2 For each term — complete this sequence before moving to the next term

**Step 1: Read all verses**
Read every verse in the term's verse array. Do not skip. Do not begin classifying while reading. Note the term's gloss and any existing_groups before beginning. Understand what the term means before filtering verses.

**Step 2: Apply the relevance filter**
For each verse, apply the governing filter (Section 3).
- If an existing verse_context record is present, review it — but do not assume it is correct. You may revise prior classifications if a revision is clearly warranted (see revision rule below).
- Mark each verse: Relevant (is_relevant = 1) or Set aside (is_relevant = 0).

**All-verses-fail rule:** If every verse for a term fails the relevance filter, individual inspection is mandatory and non-waivable before reaching this finding. Sampling — reviewing a subset and inferring the remainder — is not permitted regardless of corpus size. Once full individual inspection is complete, the all-verses-fail finding is treated as a deferred flag under the Deferred Flag Protocol (Section 6.5) — regardless of verse count and regardless of whether the term is a grammatical particle, homograph, or any other type. Do not stop mid-classification. Accumulate the finding, record it in the flags register, and continue classifying. The finding must be documented with: term identity, verse count, the basis for the finding, and confirmation that individual inspection was completed for all verses. See Section 6.5 for the full resolution process.

**The only condition that triggers an immediate stop** is a structural data integrity failure that would prevent correct classification of subsequent verses — for example, a partial completion anomaly in the extract (some verses already classified but term_classification_complete = false). In all other cases, including all-verses-fail and all borderline classification decisions, proceed and defer to the end-of-batch flag session.

**Partial completion rule:** If a term has existing verse_context records (some verses already classified) but term_classification_complete = false (some verses still unclassified), this indicates a prior batch was not completed correctly. This is an error condition. Stop for this term. Flag to the researcher with: the term details, which verses are classified, which are unclassified, and the reason for incompleteness if discernible. Await researcher instruction. The batch submission must not proceed for this term until the researcher has confirmed how to resolve it.

**Revision criterion for term_classification_complete = true:** A revision is clearly warranted when: (a) the existing context_description would materially misrepresent the term's inner-being function in light of the full verse set now visible; or (b) a clearly stronger anchor verse is available and the designated anchor is demonstrably weaker. When a revision is made, Claude AI must: record the reason for the revision in the verse_context notes field; and include a clear description of what changed and why in the per-term classification summary (Annexure B) so the researcher can review the change.

**Step 3: Group relevant verses**
Ask for each relevant verse: **does this verse engage the same inner-being characteristic through this term as verses already assigned to a group?**

- If yes → assign to that group
- If no → check existing_groups first; assign to an existing group if appropriate; only create a new group if no existing group fits

**Characteristic-perspective grouping model:**

Groups must be formed from the perspective of the inner-being characteristic the verse cluster is primarily about — not from the perspective of what the term does. This distinction matters because:

- **Characteristic terms** name an inner-being state directly (e.g. *lev* = heart, *ne.phesh* = soul, *pistis* = faith). Their groups are naturally characteristic-centred.
- **Property terms** describe how inner-being characteristics operate — their mechanism, condition, expression, or channel (e.g. *sha.ma* = hear/listen, *o.zen* = ear, *akoē* = hearing). Property terms can serve different characteristics across their verse corpus, and can serve the same characteristic in opposite ways (e.g. receptive hearing as the channel of faith; refused hearing as the expression of heart-stubbornness).

**For property terms especially:** the group description must name the characteristic being served — not just the term's function. A group called "refusing to hear God" is term-centric. A group called "heart-stubbornness expressed through refusal of God's word" is characteristic-perspective. The difference is analytically significant: Session B analyses characteristics, and group descriptions must map to that analysis correctly.

**Forming context_description:** A brief phrase (one sentence maximum) capturing what the group says about the inner being. It must:
- Name the inner-being characteristic the verse cluster primarily engages
- State the term's role accurately relative to that characteristic (as seat, expression, channel, mechanism, obstacle, or counterpart)
- Be grounded in what the verses show — not in prior theological knowledge
- Be sufficient to distinguish this group from others for this term

Examples of well-formed descriptions under the characteristic-perspective model:
- *Term names the inner seat of the emotion of fear — the place where fear arises and is registered* (characteristic: fear; term's role: seat)
- *Term serves as the channel through which faith arrives — hearing as the mechanism of faith reception* (characteristic: faith; term's role: channel)
- *Term expresses the stubbornness of the heart — refusal to hear as the outward form of inner resistance* (characteristic: stubbornness; term's role: expression)
- *Term names the cognitive capacity of the inner person — the faculty by which wisdom is received and held* (characteristic: wisdom/understanding; term's role: faculty)

Examples of descriptions to avoid (term-centric, not characteristic-perspective):
- ~~*Term describes an act of refusing to listen*~~ — names what the term does, not what the verse is about
- ~~*Term is used when God addresses people*~~ — describes context, not the inner-being characteristic
- ~~*Term indicates active, engaged hearing*~~ — describes the term's behaviour, not the characteristic served

**Grouping criterion — when a new group is warranted:** A new group is warranted when the inner-being characteristic being engaged is materially different from all existing groups, or when the same characteristic is engaged in a materially different way. Materially different means: an analysis of the verses in the candidate group, evaluated against the existing groups, would arrive at a differential conclusion about the characteristic. The following factors indicate material difference: (1) a different inner-being characteristic is the primary subject; (2) the term serves the same characteristic in a distinguishably different role (e.g. seat vs. channel vs. expression); (3) the same characteristic appears in a materially different orientation (e.g. toward God vs. against God; positive vs. negative register). Minor variations in emphasis or tone within the same essential characteristic engagement do not warrant a new group. Where 5 or more groups emerge for a single term, pause and assess whether consolidation better serves the criterion before adding further groups. Note the count in the per-term summary.

**Step 4: Designate anchors**
For each group: designate 1–2 anchor verses meeting the criteria in Section 4.

If revising prior classification: a verse previously marked is_related may be promoted to is_anchor. A verse previously marked is_anchor may be demoted if a better anchor is found — but ensure the group retains at least one anchor.

**Step 5: Identify dual-context verses**
Where a verse plainly operates at two distinct inner-being levels through the same term — assign to two groups. This is the exception, not the norm. Record the reason for dual-context in the notes field on both verse_context rows.

**Step 6: Per-term classification summary and observations file write**
Before moving to the next term, state the summary (Annexure B template) and write the term's Classification blocks to the observations file immediately. This produces a readable record and the machine-parseable record simultaneously.

**⚠ Classification block integrity rules — these govern the observations file as a machine-parseable source document:**

**Unique group codes:** Every Classification block written for a term must carry a unique `{mti_id}-{serial}` group code. Once a code is written to the file (e.g. `235-001`), that code is permanently bound to the group it was first assigned to. It must not be reused for a different group in the same term entry, even if the original group is revised or abandoned.

**Mid-stream revision protocol:** If, during classification of a term, a group is revised or abandoned and replaced with a different group, the following steps are mandatory:
1. Mark the original Classification block explicitly as superseded by prepending `~~SUPERSEDED~~` to that block.
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

**Continuous file writing — observations file:**
The per-batch observations file must be written progressively to disc during the session, not accumulated in memory and written at the end. The write discipline is as follows:

- **After every term** (Step 6 of Section 6.2): write that term's Classification blocks and SUMMARY line to the observations file immediately. Do not defer. Do not batch multiple terms before writing.
- **On every write**: increment the minor version number in the filename and in the file header (e.g. `v1.2` → `v1.3`). The version number is the only reliable differentiator between saves.
- **Version confirmation**: before each write, state aloud: *"Writing observations file — current version: v{n}. Incrementing to v{n+1}."* This confirms the save is occurring and makes the version progression visible in the session transcript.
- **Session log version reference**: every session log must state the current observations file version at the time of writing (e.g. *"Observations file at time of this log: wa-vcb-006-term-observations-v1.7-20260331.md"*). This creates a recoverable link between session logs and the observations file state they describe.
- **New session startup**: at the start of every new session that continues an existing batch, Claude AI must confirm the observations file version it is reading before doing any work. State: *"Observations file loaded: {filename} version {v}. This is the most recent version and will be the base for continued writes."*

If the session is interrupted, the observations file must contain a complete record of every term classified up to that point, and the version number must reflect the last completed write.

**Unified file naming convention — all Claude AI outputs:**

All files produced by Claude AI during a Verse Context classification or patch construction session must follow this pattern:

```
wa-vcb-{batch_id}-{scope}-{version}-{date}.{ext}
```

| Component | Rule |
|---|---|
| `wa-vcb` | Fixed prefix — always lowercase, always present |
| `{batch_id}` | Batch identifier — e.g. `003` for VCB-003 |
| `{scope}` | Short descriptor of the file's content — see table below |
| `{version}` | Version string — see versioning rules below |
| `{date}` | Creation date in `YYYYMMDD` format — does not change on update |
| `{ext}` | File extension — `.md`, `.json` |

**Scope values for Claude AI outputs:**

| File type | Scope value | Example |
|---|---|---|
| Observations file | `term-observations` | `wa-vcb-003-term-observations-v1.2-20260331.md` |
| Session log | `session-log-{breakpoint}` | `wa-vcb-003-session-log-R19-v1-20260331.md` |
| Final session log | `session-log-final` | `wa-vcb-003-session-log-final-v1-20260331.md` |
| Flags register | `flags-register` | `wa-vcb-015-flags-register-v1-20260403.md` |
| Session B flags | `sessionB-flags` | `wa-vcb-015-sessionB-flags-v1-20260403.md` |
| Patch file | `patch` | `wa-vcb-003-patch-v1-20260331.json` |

**Breakpoint identifiers for session logs** — use the registry number(s) completed at that breakpoint:
- Single registry: `R19`, `R20`, `R28` etc.
- Multiple registries in one log: `R20-R23`, `R24-R26` etc.
- Final log covering all registries: `final`

**Versioning rules:**

- `{version}` always starts at `v1` for a new file
- For the observations file, which is updated progressively within a session, increment the minor version on each save: `v1`, `v1.1`, `v1.2`, etc. The version number is the only reliable differentiator between saves — do not rely on file size or timestamp
- For session logs and flag resolution files, which are written once per breakpoint, use `v1` unless a correction is issued, in which case increment: `v2`, `v3`, etc.
- `{date}` is the creation date and does not change when the file is updated

**Sorting behaviour:** All batch outputs sort together under `wa-vcb-{batch_id}-` when listed alphabetically, making the full batch file set visible at a glance.

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

- The observations file must contain a **Classification block** for every active term, in structured format: `{mti_id}-{serial}: *{context_description}* | Anchor: {ref} | Related: {ref, ...}`. This structured block is what the patch builder reads — prose-only entries cannot be reliably parsed. Write the Classification block for every term at classification time, even for terms with a single verse. The observations file provided to the patch construction session must be the most recent version (highest version number).
- The final session log before patch construction must contain a complete per-term table showing: mti_id, Strong's, verse count, relevant count, group count, and anchor references. This table is the reconciliation check for the patch.
- The patch construction session must verify every anchor reference against the actual verse_record_ids in the extract JSON before producing any operations. Anchor references that do not match the term's verse set must be corrected — they are typically reference format variants (e.g. `Jude 3` vs `Jud 1:3`) or verses assigned to a different term.
- The patch construction session must run programmatic pre-submission validation (Section 7.6) before producing the output file.

**Instruction document size awareness:**
This instruction document is long. When loading it alongside a large batch JSON and an observations file, the combined context load is significant. Claude AI should read the instruction once at session start and not reload it unless a specific section is needed. For patch construction sessions, load only the observations file, the extract JSON, and Sections 7–7.6 of this instruction — not the full document.

---

## 6.5 Deferred Flag Protocol

**⚠ This section replaces the previous per-term stop rule for all-verses-fail findings and borderline classification decisions. Flags that do not block the classification of other verses are accumulated during classification and resolved in a single interactive session at end-of-batch, before patch preparation begins.**

### 6.5.1 What is a deferred flag

A deferred flag is any classification finding or question that:
- Does not prevent correct classification of the remaining verses in the batch
- Requires researcher judgement before the patch can be correctly produced
- Would, under the previous protocol, have caused a mid-classification interruption

**Examples of deferred flags:**
- All-verses-fail findings (all verse counts, all term types)
- Borderline relevance judgements where the filter decision is genuinely uncertain
- Classification boundary questions (e.g. where a term's inner-being connection is indirect)
- Homograph split observations (informational flags, no decision required)
- Analytical observations that require researcher input before a Session B note can be formed

**The only condition that still triggers an immediate stop** is a structural data integrity issue that would prevent correct classification of subsequent verses — specifically, a partial completion anomaly where some verses for a term already have verse_context records but term_classification_complete = false. This indicates a prior batch was not completed correctly and must be resolved before continuing.

### 6.5.2 During classification — flag accumulation

While classifying, when a deferred flag arises:

1. Record the flag identifier (DF-{nnn}, sequential within the batch) in the running flags list maintained in working memory or in the observations file notes
2. Make a working classification decision (typically: classify as best you can on current evidence, note the assumption made, continue)
3. For all-verses-fail findings: record the term identity, verse count, basis for the finding, and confirmation that individual inspection was completed for all verses
4. Do not interrupt the session. Do not present the flag to the researcher until the end-of-batch flag session

### 6.5.3 End-of-batch — producing the flags register

After all terms are classified, produce the flags register before the patch. The flags register is a structured document (not a prose summary) with one entry per flag.

**File:** `wa-vcb-{batch_id}-flags-register-v1-{date}.md`

**Each flag entry must contain:**

1. **Flag identifier** — DF-{nnn} | term identity (Strong's, transliteration, gloss, mti_id, registry)
2. **The verse(s) under consideration** — full verse text for every verse relevant to the flag. Do not use references alone. The researcher cannot make a sound judgement from references alone.
3. **The specific issue** — what was found and why a decision is required
4. **What each option means for the patch** — concrete patch consequence of each option: which verses will be classified as relevant or set aside, whether a group will exist or not, whether an all-verses-fail record will be produced
5. **Claude AI's own assessment** — state which option is analytically stronger and why, grounded in the verse texts, the filter criteria, and programme precedent. Label explicitly: *"Claude AI assessment: [option/finding] is [stronger/correct] because [reason]."* Do not present options as equally weighted when one is clearly more consistent with programme criteria

**Format:**

```
### DF-{nnn} | {strongs} ({transliteration}) — {gloss} | mti_id={n} | Registry {nnn} ({word})
**Verse count:** {n}
**Finding / Issue:** {description}

**The verse(s):**
vid={n} {ref}: *"{full verse text}"*
[repeat for all relevant verses]

**Option A:** {description} — patch consequence: {what happens}
**Option B:** {description} — patch consequence: {what happens}
[or: CONFIRM / OVERRIDE for all-verses-fail findings]

**Claude AI assessment:** {which option/finding, and why}

→ **Your decision:**
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
- No verse_context records are inserted for this term
- The term proceeds to Session B with no anchor. Rule R4 (every term must have at least one active anchor before Session B may proceed) is noted as not applicable for this term
- The all-verses-fail finding is documented in the final session log

---

## 6.6 Session B Flags

**Purpose:** The Session B flags document carries analytical insights and questions that emerge during Verse Context classification — from the researcher's flag decisions, from unexpected term behaviour, or from verse engagement that raises questions beyond the scope of the filter decision — into the Session B Analysis stage. Verse Context intentionally defers interpretation; this document is the formal channel through which Verse Context observations inform Session B.

**When to produce:** If any Session B flags are raised during the end-of-batch flag resolution session, produce the Session B flags document before the patch construction session. If no Session B flags were raised, the document is not required for that batch.

**File:** `wa-vcb-{batch_id}-sessionB-flags-v1-{date}.md`

### 6.6.1 What qualifies as a Session B flag

A Session B flag is raised when:
- The researcher's decision on a flag includes an explicit analytical question or observation for Session B to explore
- A term's classification raises an interpretive question that goes beyond the filter decision (e.g. the term behaves in a way that may reveal a previously unidentified inner-being dynamic)
- A researcher comment on a flag suggests a connection between terms, registries, or clusters that Session B should investigate

Session B flags are not corrections or errors. They are analytical starting points.

### 6.6.2 Content of each Session B flag entry

Each entry must contain:

1. **Flag identifier** — SBF-{batch_id}-{nnn} (e.g. SBF-VCB015-001)
2. **Term and registry** — Strong's, transliteration, gloss, mti_id, registry number and word
3. **Source** — which deferred flag triggered this Session B flag (DF-{nnn})
4. **The analytical question** — the question or observation the researcher raised, expanded with analytical context grounded in the verse corpus
5. **Suggested Session B exploration** — concrete lines of inquiry for Session B Analysis, including which group codes carry the most relevant verses, any cross-registry connections, and what the question implies for the programme's understanding of the inner being
6. **Relevant group codes** — the group codes in the observations file most directly relevant to this exploration

### 6.6.3 Position in the handoff chain

The Session B flags document must be provided to the Session B DataPrep and Analysis sessions alongside the re-exported full word JSON for each affected registry. It is not a replacement for the Session B instructions — it is supplementary analytical context that enriches how the analyst approaches those terms.

When Session B begins for a registry that has Session B flags, Claude AI must load the flags document alongside the standard Session B instructions and explicitly acknowledge each flag at the start of analysis for the affected term.

**⚠ Session B flags must not be lost between sessions.** The patch construction session should note in its handoff that Session B flags exist for specific registries. Claude Code's completion report for a registry should flag whether a sessionB-flags file exists for that batch.

---

## 7. Patch Production

### 7.1 Patch types

| Type | Purpose | When to use |
|---|---|---|
| VERSECONTEXT | Full batch — all terms in batch | After completing all terms in a batch session |
| VCGROUP | Targeted group update | When revising a single group description or dissolving/reinstating a group outside a batch |
| VCVERSE | Targeted verse update | When a single verse changes state (new verse added after audit_word re-run, verse removed, reclassification needed) |

### 7.2 VERSECONTEXT patch — structure

Produced once per batch, after all terms are complete and pre-submission validation passes.

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1",
    "batch_id": "VCB-{nnn}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-VerseContext-Instruction-v1.8",
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

Note: `session_b_status` is `null` in all Verse Context patches. The applicator must not reject this. `verse_context_status` is managed by Claude Code completion logic, not by patch files.

**`_patch_summary` field definitions:**
- `dual_context_verses` — count of *verses* (not verse_context rows) that appear in more than one group for the same term. A verse assigned to two groups contributes 1 to this count regardless of how many verse_context rows it generates.

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
    "context_description": "{brief phrase — inner-being engagement}",
    "notes": null,
    "delete_flagged": 0
  },
  "description": "New group for {strongs_number}: {context_description}"
}
```

**Claude Code:** after inserting, capture `last_insert_rowid()` as the integer id for this group. Use this integer in all subsequent verse_context inserts that reference this group in the same patch.

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
  "description": "Revised context description for group {group_code}: {reason}"
}
```

Only fields being changed appear in `set`. `delete_flagged = 1` dissolves a group. When dissolving: check that affected anchor verses are reassigned or that the term retains at least one anchor from another group — include those operations in the same patch.

#### Insert new verse_context record — anchor

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

#### Insert new verse_context record — related

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

#### Insert new verse_context record — set aside

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
    "set_aside_reason": "{no_inner_being | physical_only | spatial_only | wrong_face | other}",
    "notes": null,
    "delete_flagged": 0
  },
  "description": "{Book Ch:V} — set aside ({set_aside_reason}), no inner-being engagement for {strongs_number}"
}
```

**`set_aside_reason` is required** for every set-aside record from VCB-032 onward. Use the controlled vocabulary from Section 2.2. For `wrong_face`, populate the `notes` field with the term and registry carrying the inner-being content where known: e.g. `"wrong_face: inner-being content carried by lev (H3820A, Reg 183)"`. For `other`, the `notes` field must explain the reason. `NULL` is not acceptable from VCB-032 onward.
```

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

**All corrections are UPDATE operations. Never delete and reinsert.** Use `delete_flagged = 1` to flag a record out of the active set without physical deletion.

**Note on group_id references:** In operations within the same patch, `group_id` may be a group_code string (e.g. `"142-001"`) for groups being inserted in the same patch. Claude Code resolves these to the captured integer id at apply time. For existing groups from prior patches, use the integer id directly.

### 7.4 Operation ordering within patch

For each term, order operations as follows:
1. All `verse_context_group` inserts for the term (new groups — so integer ids are available for subsequent rows)
2. All `verse_context_group` updates (revisions to existing groups)
3. All `verse_context` inserts — anchors first, then related, then set-aside
4. All `verse_context` updates (revisions to prior classifications)

Across terms: process terms in the order they appear in the batch JSON.

### 7.5 Decision context requirement — researcher decisions during patch construction

When Claude AI identifies an issue during patch construction that requires a researcher decision (anchor missing, group dissolution, cross-term assignment, ambiguous reference, or any other unresolvable condition), it must present the decision with the following elements. A bare option list is not acceptable.

**Required elements for every researcher decision:**

1. **The affected term and group** — Strong's number, transliteration, gloss, mti_id, group code, and group description.
2. **The specific issue** — what was found and why it cannot be resolved automatically.
3. **Full verse text for every verse under consideration** — not just references. The researcher cannot make a sound judgement from references alone.
4. **What each option means for the patch** — spell out the concrete consequence of each choice: which verses will be classified, which will be set aside, whether a group will exist in the database.
5. **Claude AI's own assessment** — state which option is analytically stronger, and why, grounded in the verse texts and the group description. Claude AI must not present options as equally weighted when one is clearly more consistent with the programme's classification criteria. Label this explicitly: *"Claude AI assessment: [option] is stronger because [reason]."*

**Rationale:** During VCB-006 patch construction, 10 decisions were presented to the researcher as option lists with minimal verse context. The researcher noted that in 90% of cases the decision required a judgement call without sufficient information. This instruction corrects that discipline. The researcher's role is to make an informed decision, not to guess.

**Format template:**
```
Decision D-NNN | mti_id={n} | {strongs} ({transliteration}) — {gloss}
Group {code}: {description}

Issue: {what was found and why it cannot be auto-resolved}

Verses under consideration:
  {ref} vid={n}: "{full verse text}"
  {ref} vid={n}: "{full verse text}"
  [repeat for all relevant verses]

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
- Every verse in the batch has exactly one verse_context row, except dual-context verses (exactly two)
- Every new group has at least one anchor insert in this patch or an existing anchor in the database
- Every is_related = 1 row references a group that has an anchor (in this patch or existing)
- Every is_relevant = 0 row has group_id = null
- No row has is_anchor = 1 and is_related = 1 simultaneously
- _patch_summary counts match the actual operation counts

**Programmatic validation — required for large batches (>50 terms):** When the patch is produced in a deferred patch construction session (see Section 6.4), validation must be performed programmatically against the extract JSON before the patch file is written. Specifically:

1. **Anchor reference verification** — every anchor reference in the classification data must be resolved to an actual verse_record_id in the term's verse set. References that do not resolve must be corrected before operations are generated. Silent failure (generating a patch with unresolved anchors) is not acceptable.
2. **Duplicate key check** — verify no (verse_record_id, mti_term_id, group_id) combination appears more than once. This catches the case where a verse appears in both the anchor and related lists for the same group.
3. **Coverage check** — every verse_record_id in the extract for every term must appear in exactly one verse_context insert (or two for dual-context verses). No verse may be missed.
4. **R1–R4 pre-check** — apply the consistency rules (Section 11.3) to the proposed operations before writing the file, not only after application.

### 7.8 Handoff to Claude Code

```
PATCH SUBMISSION TO CLAUDE CODE

Patch file: wa-vcb-{batch_id}-patch-{date}.json
Patch type: VERSECONTEXT

Action required:
  1. Apply patch — insert/update verse_context_group and verse_context records
  2. Resolve group_code strings to integer ids for new groups in this patch
  3. Validate consistency rules R1–R4 after application
  4. Run integrity validation (Section 13 below)
  5. Handle XREF coverage check for all affected registries (Section 0.2)
  6. For each registry whose OWNER terms appear in this batch:
     - Run completion check (Section 14.5)
     - If complete: SET verse_context_status = 'Complete', re-export full word JSON
  7. Report: records inserted/updated, registries advanced to Complete, XREF coverage status,
     any integrity violations, next batch construction status
```

---

## 8. VCGROUP Patch — Targeted Group Update

Use when revising a single `verse_context_group` record outside a full batch run — for example, when a context_description needs refinement after researcher review, or when a group is dissolved because its verses belong better in another group.

### 8.1 Input required from Claude Code

Before producing a VCGROUP patch, Claude Code must provide:

```json
{
  "group": {
    "id": 0,
    "mti_term_id": 0,
    "strongs_number": "{H/Gnnnn}",
    "group_code": "{text}",
    "context_description": "{current text}",
    "notes": null,
    "delete_flagged": 0,
    "anchor_count": 0,
    "related_count": 0,
    "anchor_verses": [
      {
        "verse_record_id": 0,
        "reference": "{Book Ch:V}",
        "verse_text": "{text}"
      }
    ]
  }
}
```

**Source tables for VCGROUP input:**

| Field | Source |
|---|---|
| group.id | verse_context_group.id |
| group.mti_term_id | verse_context_group.mti_term_id |
| group.strongs_number | mti_terms.strongs_number (JOIN via verse_context_group.mti_term_id → mti_terms.id) |
| group.group_code | verse_context_group.group_code |
| group.context_description | verse_context_group.context_description |
| group.notes | verse_context_group.notes |
| group.delete_flagged | verse_context_group.delete_flagged |
| group.anchor_count | COUNT(verse_context WHERE group_id = vcg.id AND is_anchor = 1 AND delete_flagged = 0) |
| group.related_count | COUNT(verse_context WHERE group_id = vcg.id AND is_related = 1 AND delete_flagged = 0) |
| group.anchor_verses | verse_context (WHERE group_id = vcg.id AND is_anchor = 1 AND delete_flagged = 0) → wa_verse_records (verse_record_id, reference, verse_text) |

### 8.2 Patch structure

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-VCGROUP{group_id}-V1",
    "group_id": 0,
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-VerseContext-Instruction-v1.8",
    "session_b_status": null,
    "description": "Targeted group update — group {group_code}: {reason}"
  },
  "operations": [
    {
      "op_id": "OP-001",
      "operation": "update",
      "table": "verse_context_group",
      "match": { "id": 0 },
      "set": {
        "context_description": "{revised text}",
        "notes": "{reason if applicable}",
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

**Reinstatement note:** If `delete_flagged` is reset from 1 to 0 (reinstating a dissolved group), the verse_context rows that were flagged when the group was dissolved are NOT automatically reinstated. A separate VERSECONTEXT or VCVERSE patch is required to reinstate those verses.

---

## 9. VCVERSE Patch — Targeted Verse Update

Use when a single verse changes state: a new verse was added after audit_word re-run, a verse was removed, or a reclassification is needed outside a full batch run.

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

**Source tables for VCVERSE input:**

| Field | Source |
|---|---|
| verse.verse_record_id | wa_verse_records.id |
| verse.reference | wa_verse_records.reference |
| verse.verse_text | wa_verse_records.verse_text |
| verse.target_word | wa_verse_records.target_word |
| verse.span_strong_match | wa_verse_records.span_strong_match |
| verse.verse_delete_flagged | wa_verse_records.delete_flagged |
| verse.mti_term_id | wa_verse_records.mti_term_id |
| existing_verse_context | verse_context WHERE verse_record_id = vr.id AND mti_term_id = {mti_term_id} (NULL object if no row exists) |
| existing_verse_context.group_code | verse_context_group.group_code (JOIN via verse_context.group_id → verse_context_group.id) |
| available_groups | verse_context_group WHERE mti_term_id = {mti_term_id} AND delete_flagged = 0 |

### 9.2 Three scenarios

**Scenario A — New verse, first-time classification:**
Use `insert` operation. Assign to an existing group if it fits; insert new group first if needed.

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

If the verse was an anchor: include a second operation promoting another related verse in the same group to anchor status. If no related verses remain active in the group, include a note flagging that the group has no anchor — researcher decision required before Session B proceeds.

**Scenario C — Reclassify existing verse:**
Use `update` operation on the existing verse_context id. Include notes explaining the reason for reclassification. Maintain anchor integrity.

### 9.3 Patch naming

`PATCH-{YYYYMMDD}-VCVERSE{verse_record_id}-V1`

---

## 10. Researcher Compliance Rules

| **⚠ Do not make assumptions or guesses. When uncertain about whether a verse passes the relevance filter, retain the verse, note the uncertainty, and proceed. Do not stop the session for borderline filter decisions — batch uncertainty questions at the end of each term's classification and present them together.** |
|---|

Additional rules:
- Do not develop analytical conclusions about terms during Verse Context — that is Session B
- Do not draw cross-registry connections during Verse Context — that is Session D
- Do not assign evidential status — that is Session B DataPrep and Analysis
- Context descriptions must be grounded in what the verses show — not in prior theological knowledge about the term
- Dual-context is rare — only when two distinct inner-being engagements are plainly evident. Do not use it to resolve interpretive difficulty
- All corrections are UPDATE operations — never produce delete + reinsert
- The anchor integrity rule is absolute — a term must retain at least one active anchor at all times

---

## 11. Claude Code — Patch Application Protocol

### 11.1 Apply in single transaction

All operations in a VERSECONTEXT patch apply as one transaction — all or nothing.

### 11.2 Group_code resolution

For each `verse_context_group` insert: after the insert executes, capture `last_insert_rowid()`. Store this mapping: `group_code → integer id`. Apply this mapping to all subsequent `verse_context` inserts in the same patch that reference this group_code as their group_id value.

### 11.3 Consistency rule validation

Run after every patch application:

```sql
-- R1: set-aside rows clean
SELECT COUNT(*) FROM verse_context
WHERE is_relevant=0 AND (group_id IS NOT NULL OR is_anchor=1 OR is_related=1);
-- Expected: 0

-- R2: anchor rows clean
SELECT COUNT(*) FROM verse_context
WHERE is_anchor=1 AND (is_relevant=0 OR is_related=1 OR group_id IS NULL);
-- Expected: 0

-- R3: related rows have an active anchor in their group
SELECT COUNT(*) FROM verse_context vc
WHERE is_related=1 AND NOT EXISTS (
  SELECT 1 FROM verse_context a
  WHERE a.group_id=vc.group_id AND a.is_anchor=1 AND a.delete_flagged=0);
-- Expected: 0
```

Any violation: report to researcher. Do not advance registry status until violations resolved.

### 11.4 Anchor integrity check

After any patch affecting anchor status, for each affected term:

```sql
SELECT COUNT(*) as active_anchors FROM verse_context
WHERE mti_term_id = {mti_term_id} AND is_anchor = 1 AND delete_flagged = 0;
-- If 0: flag to researcher — term has no anchor and cannot proceed to Session B
```

### 11.5 Re-extraction trigger and reset requirement

**Pre-extraction REPAIR patch required:** Before any audit_word re-run for a registry, a REPAIR patch must be applied to reset the registry state. This patch must be applied and confirmed before audit_word runs. No re-extraction may proceed without it.

The REPAIR patch resets:
- `word_registry.session_b_status` → `Verse Context Reset`
- `word_registry.verse_context_status` → `In Progress`
- All `verse_context` records for this registry's OWNER terms → `delete_flagged = 1`
- All `verse_context_group` records for this registry's OWNER terms → `delete_flagged = 1`
- All Session B analytical outputs (wa_session_b_dimensions, wa_session_b_findings, wa_session_research_flags SD_POINTER records, wa_term_inventory.evidential_status) for this registry → cleared

The REPAIR patch naming convention: `PATCH-{YYYYMMDD}-{nnn}-REPAIR-AUDITWORD-RERUN-V1`
Full patch specification: WA-PipelineStatusReview-v2-20260330 Section 3.2.

**Claude Code expectation — audit_word routine:** Claude Code must build the following into the audit_word re-run routine. When audit_word detects it is re-running for a registry that already has data (i.e. wa_term_inventory records exist for this registry), the routine must:
1. Verify the REPAIR patch has been applied (check patch history for REPAIR-AUDITWORD-RERUN on this registry). If not applied: halt with error — do not proceed.
2. On re-run, the STALE_TERM mechanism (Step A6) handles wa_term_inventory updates — it compares the incoming JSON against existing records and applies only the delta. This is the authoritative mechanism for updating term inventory on re-run. No separate delete/re-insert of wa_term_inventory records is required.
3. After audit_word completes, re-export the full word JSON (Step A11). The re-export confirms the updated state for the next pipeline stage (Verse Context).

**Post-audit_word detection (existing check retained):**

After every audit_word re-run, check for OWNER terms with verse records that have no corresponding verse_context entry:

```sql
SELECT DISTINCT mt.id, mt.strongs_number, mt.owning_registry_fk
FROM wa_verse_records vr
JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
JOIN mti_terms mt ON mt.id = vr.mti_term_id
WHERE ti.term_owner_type = 'OWNER' AND vr.delete_flagged = 0
  AND NOT EXISTS (
    SELECT 1 FROM verse_context vc
    WHERE vc.verse_record_id = vr.id AND vc.mti_term_id = mt.id
  );
```

For each term returned: set owning registry `verse_context_status = 'In Progress'`. Report to researcher.

Cascade delete_flag from verse records to verse_context when a verse is flagged:
```sql
UPDATE verse_context SET delete_flagged = 1
WHERE verse_record_id IN (SELECT id FROM wa_verse_records WHERE delete_flagged = 1)
  AND delete_flagged = 0;
```

**Claude Code expectation — Verse Context batch preparation routine:** When Claude Code prepares a Verse Context batch for a registry that previously had verse_context records (i.e. this is a re-run after a reset), the batch preparation routine must:
1. Confirm that all verse_context and verse_context_group records for this registry's OWNER terms are delete_flagged (the REPAIR patch should have done this — verify before constructing the batch).
2. Treat the registry as a fresh start — do not carry forward any prior contextual groupings into the new batch JSON. The batch JSON's `existing_groups` array for each term must reflect only active (delete_flagged = 0) groups — which after the reset will be empty.
3. Re-assess the wa_term_inventory records for this registry: confirm that mti_terms.status values are still appropriate (extracted/extracted_thin) after the audit_word re-run. If any terms now have NULL status (new terms added by the re-run), flag these to researcher for DataPrep re-classification before Verse Context proceeds.

---

## 12. Claude Code — Integrity Validation

Run after every patch application cycle:

```sql
-- Terms with delete/excluded status should have no active verse_context rows
SELECT mt.strongs_number, mt.status, COUNT(vc.id) as active_vc_rows
FROM mti_terms mt
JOIN verse_context vc ON vc.mti_term_id = mt.id
WHERE mt.status IN ('delete','excluded') AND vc.delete_flagged = 0
GROUP BY mt.id;
-- Expected: zero rows. Any result is an integrity violation — report to researcher.
```

---

## 13. Claude Code — Registry Completion Check and Re-export

Run after every VERSECONTEXT patch, for each registry whose OWNER terms appear in the batch.

### 13.1 OWNER term completion check

```sql
SELECT COUNT(*) as unclassified_owner_terms
FROM wa_term_inventory ti
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
WHERE wr.no = {registry_no}
  AND ti.term_owner_type = 'OWNER' AND ti.delete_flagged = 0
  AND mt.status IN ('extracted','extracted_thin')
  AND EXISTS (
    SELECT 1 FROM wa_verse_records vr
    WHERE vr.term_inv_id = ti.id AND vr.delete_flagged = 0
  )
  AND NOT EXISTS (
    SELECT 1 FROM verse_context vc
    WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
  );
-- If 0: all OWNER terms with verses are classified
```

### 13.2 XREF coverage check

```sql
-- XREF terms in this registry whose OWNER has not yet been classified
SELECT COUNT(*) as unresolved_xref_terms
FROM wa_term_inventory ti
JOIN wa_file_index fi ON fi.id = ti.file_id
JOIN word_registry wr ON wr.id = fi.word_registry_fk
JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
WHERE wr.no = {registry_no}
  AND ti.term_owner_type = 'XREF'
  AND ti.delete_flagged = 0
  AND NOT EXISTS (
    SELECT 1 FROM verse_context vc WHERE vc.mti_term_id = mt.id AND vc.delete_flagged = 0
  );
-- If 0: all XREF terms have OWNER classification available
```

### 13.3 Advancing status and re-exporting

When both checks return 0 for a registry:

```sql
UPDATE word_registry SET verse_context_status = 'Complete' WHERE no = {registry_no};
```

**Double-check verification (G06-F):** Immediately after writing `verse_context_status = Complete`, re-run both the OWNER completion check (Section 13.1) and the XREF coverage check (Section 13.2) for this registry. If either returns a non-zero count:
- Reverse the status write: `UPDATE word_registry SET verse_context_status = 'In Progress' WHERE no = {registry_no};`
- Report the inconsistency to the researcher with the query results showing what remains unclassified.
- Do not proceed with re-export until the inconsistency is resolved.

If both checks confirm zero: proceed with re-export.

Then immediately re-export the full word JSON:
```bash
python -m engine.engine --export-word --registry={registry_no}
```

This produces a fresh `wa-{nnn}-{word}-extract-{date}.json` carrying `verse_context_status = Complete` in its meta. **This re-export is what opens the DataPrep gate.** DataPrep reads this file, sees `verse_context_status = Complete`, and proceeds.

**Note on session_b_status:** This process does not update `session_b_status`. The value `Ready for Analysis` in the session_b_status vocabulary is set by `audit_word` (using COALESCE — only when current status is NULL), not by any Verse Context operation. The DataPrep gate check (WA-SessionB-DataPrep-Instruction Section 4.1) gates on `verse_context_status = Complete` — it does not require `session_b_status = Ready for Analysis`. No session_b_status write is needed here.

### 13.4 Completion report to researcher

For each registry reaching Complete, report:

```
Registry {nnn} — {word}:
  OWNER terms classified: {n} / {total}
  XREF terms covered: {n} (via OWNER classifications in registries: {list})
  verse_context_status: Complete
  Re-export: wa-{nnn}-{word}-extract-{date}.json produced
  Ready for: Session B DataPrep
```

For each registry remaining In Progress after this batch (partial registry split), report:

```
Registry {nnn} — {word}:
  OWNER terms classified this batch: {n}
  OWNER terms remaining: {n} (to be included in VCB-{next_batch_id})
  verse_context_status: In Progress — continuation expected
```

After all per-registry reports for this batch, produce a batch-level summary:

```
BATCH {batch_id} COMPLETION SUMMARY

Registries in this batch: {n}
  Reached Complete this batch: {n} — {list: nnn—word}
  Still In Progress: {n} — {list: nnn—word, reason}
    Of which: partial split (continuation in next batch): {n}
    Of which: all-verses-fail or other pending decision: {n}

Programme-wide Stage 1 progress:
  verse_context_status = Complete: {n} / 181 registries
  verse_context_status = In Progress: {n} registries
  Unclassified OWNER terms remaining: {n}
```

---

## 14. Stage 1 Completion

Stage 1 is complete when all 181 active registries have `verse_context_status = Complete`.

### 14.1 Monitoring query

```sql
SELECT verse_context_status, COUNT(*) as count
FROM word_registry
WHERE session_b_status IS NOT NULL
GROUP BY verse_context_status;
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
  verse_context_group records created: {n}
  verse_context records created: {n}
    - Anchor verses: {n}
    - Related verses: {n}
    - Set aside: {n}
  OWNER terms classified: {n}
  XREF terms covered: {n}

All 181 registries are now at verse_context_status = Complete.
All re-exports are current.

Programme state:
  session_b_status = Verse Context Reset: 181 registries
  verse_context_status = Complete: 181 registries
  DataPrep gate: OPEN for all 181 registries

Stage 2 — Session B Analysis may now begin.
Processing sequence: per pool/cluster batch order in WA-Registry-Management-Guide-v5.4 Section 7.
```

### 14.3 What happens next

After Stage 1 completion, the programme moves to Stage 2 — Session B Analysis. Processing proceeds in pool/cluster batch order as defined in WA-Registry-Management-Guide-v5.4 Section 7. The governing instruction for each stage is:

| Stage | Governing instruction |
|---|---|
| Session B DataPrep | WA-SessionB-DataPrep-Instruction-v5.4 |
| Session B Analysis | WA-SessionB-Analysis-Instruction-v5.3 |
| Session B Extraction | WA-SessionB-Extraction-Instruction-v5.4 |

DataPrep is triggered per registry as registries reach `verse_context_status = Complete`. It does not wait for all 181 to complete — registries that complete Verse Context early can begin DataPrep immediately.

---

## Annexure A — Startup Summary Template

```
Verse Context v1.8 startup complete.
Batch: {batch_id}
Governing instruction: WA-VerseContext-Instruction-v1.8-20260331.md

Terms in batch: {n}
Total verses: {n} | Unclassified: {n} | Previously classified: {n}

Term inventory:
  {strongs_number} ({transliteration}) — {gloss} — {n} verses ({n} unclassified)
    OWNER for: {owning_word} (registry {owning_registry_id})
    Existing groups: {n} | Previously classified verses: {n}
  [repeat for each term]

Notes on previously classified terms:
  {list any terms with term_classification_complete: true and whether revision seems warranted}

Ready to proceed. Beginning with {first_strongs_number} ({transliteration}).
```

---

## Annexure B — Per-Term Classification Summary Template

```
Term: {strongs_number} ({transliteration}) — {gloss}
mti_term_id: {integer}
OWNER for: {owning_word} (registry {owning_registry_id})
Total verses: {n} | Relevant: {n} | Set aside: {n}

Groups:
  {group_code} [{new / existing}]: "{context_description}"
    Anchors: {verse reference(s)}
    Related: {n} verses
    [repeat for all groups]

Revisions to prior classifications: {n}
  {describe each: what changed and why}
Dual-context verses: {n}
  {describe each: what two engagements are present}
Borderline retained: {n}
  {list references and note uncertainty}
Anchor integrity: confirmed — {n} active anchors across {n} groups

Ready for patch.
```

---

## Annexure C — VERSECONTEXT Patch Template

File naming: `wa-vcb-{batch_id}-patch-{YYYYMMDD}.json`

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1",
    "batch_id": "VCB-{nnn}",
    "produced_date": "{yyyy-mm-dd}",
    "produced_by": "WA-VerseContext-Instruction-v1.8",
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
      "description": "{Book Ch:V} — anchor, group {mti_term_id}-001: {context_description}"
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
      "description": "{Book Ch:V} — set aside, no inner-being engagement for {strongs_number}"
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

*WA-VerseContext-Instruction-v2.2-20260401 | Supersedes v2.1-20260401 | v2.2: (1) Section 3.5 added: Relevance filter for grammatical and functional particles — pass criteria (directs/intensifies/qualifies scope/discloses inner orientation) and fail criteria (purely syntactic/social register/temporal connector/procedural) stated explicitly; (2) Section 6.2 Step 1: All-verses-fail rule rewritten — individual inspection is now explicitly non-waivable for all terms regardless of corpus size; researcher confirmation no longer required for full-corpus grammatical particles or confirmed homographs where individual inspection is complete*
