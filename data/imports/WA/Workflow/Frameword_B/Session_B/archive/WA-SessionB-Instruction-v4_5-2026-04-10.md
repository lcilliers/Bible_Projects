# Session B — Data Audit, Remediation, Analysis, and Word Articulation
## Framework B Soul Word Analysis Programme
## Instruction v4.5 | 2026-04-10

---

## Change Log

v4.5 (2026-04-10): One governing principle added — Cross-Registry Vision (Section 2.0a). Session D flag-raising is not a Pass 6 task; it is a continuous discipline active throughout all analytical passes. Every piece of data read in Stage 2 — every verse, group description, sense structure, lexical entry, dimension assignment, somatic observation, or correlation signal — must be read with the question "what does this tell me about something beyond this registry?" active. The practical method for this discipline is codified in Section 2.0a and the requirement is embedded in each pass. Pass 6 is renamed Pass 6 — Correlation Audit and Connection Verification: its role is to verify that all signals are covered and fill gaps, not to generate all flags. Three integrity rules added: SB-11, SB-12, SB-13. Analytical principle added: "Cross-registry vision is always active." Arose from Reg 068 (grace) Session B, where correlation-layer flags were raised without re-reading anchor verses — producing data-confirmed pointers but missing the verse-level cross-border observations that Session D actually needs.

v4.4 (2026-04-10): Two amendments to consistency checks 10a and 10e arising from Reg 068 grace Session B gap 9 and gap 10 analysis. (1) Check 10a (root_gloss comparison): rule rewritten — a null root_gloss in correlations.root_families is not automatically an error. When a root code spans multiple registries with conflicting glosses, the extract script correctly sets null rather than arbitrarily choosing one. Claude AI must investigate the cause before treating a null or mismatch as a correction. If registry_count > 1, raise as an open item for cross-registry investigation; only flag as a patch error when the root is single-registry and the gloss is genuinely wrong. (2) Check 10e (xref signal vs term inventory): rule corrected to match the v4.3 inventory-level logic. The xref_sharing signal is built from wa_term_inventory.delete_flagged = 0, not from mti_terms.status. Terms with mti_terms.status = delete but delete_flagged = 0 in the inventory are correctly included. Claude AI must not flag mti-deleted terms as errors in the xref signal. The check now targets wa_term_inventory.delete_flagged = 1 as the correct error condition. Rationale: gap 9 was incorrectly raised in Reg 068 audit because 10e directed Claude AI to use mti_terms.status as the filter — the same error corrected in statistics fields by v4.3.

v4.3 (2026-04-10): Two corrections to statistics and registry block audit logic arising from Reg 068 grace Session B. (1) Section 2 (Statistics block) — active_term_count and xref_term_count: verification logic corrected from mti_terms.status to wa_term_inventory.delete_flagged. These fields count inventory-level activity, not MTI-level deletion status. A term can have mti_terms.status = delete while wa_term_inventory.delete_flagged = 0 — the cascade has not yet been applied and is a deferred operation in the Session B process. Claude AI must not subtract mti-deleted terms from these counts. (2) Section 1 (Registry block) — unique_term_count / shared_term_count / term_sharing_ratio: clarified that these are registry-level fields not present in the statistics block of the extract. They must not be audited as statistics block fields.

v4.2 (2026-04-10): Two amendments to Stage 1 audit arising from Reg 068 grace Session B — strongs_list handling. (1) Section 1 (strongs_list field): corrected the "flag any deleted term still listed" rule — deleted terms are present in the Session B export by CC design and their presence is expected and correct, not an error. Rule rewritten to verify consistency only. (2) Section 1 (strongs_list field): new mandatory deletion justification review added — for every delete-status term in the strongs_list, Claude AI must read the term's semantic content and verse corpus and make an independent analytical judgement on whether the deletion is justified, applying four explicit questions. Terms deleted on adequacy-of-coverage grounds are to be challenged when they name something structurally distinct from active terms. (3) Section 3 (Terms — Deleted terms row): rule corrected to match Section 1 — deleted terms in strongs_list are expected; the audit step is deletion justification review, not flagging as errors. (4) Step D spot-check: removed the check "strongs_list no longer contains deleted terms" — this is incorrect; deleted terms are retained in the strongs_list by design. Rationale: During Reg 068 grace audit, three correctly deleted terms (H2433, H2603B, H2606) were incorrectly flagged as errors; and two terms (H2600, H2594) whose deletions were analytically unjustified were identified only because the deletion justification review was applied. The previous instruction produced checkbox behaviour rather than analytical scrutiny.

v4.1 (2026-04-10): Two additions to Stage 1 audit. (1) Section 2 (Statistics block) extended with five correlation count fields (`correlation_xref_pair_count`, `correlation_cooccurrence_pair_count`, `correlation_dimension_pair_count`, `correlation_root_family_count`, `correlation_shared_anchor_count`) and a note on expected vs unexpected zero values for correlation counts relative to data state. (2) Section 10 (Consistency checks) added as a new mandatory audit section — seven checks (10a–10g) covering: root family completeness across all terms sharing a root; root family correlation signal consistency; dimension index vs verse context group correspondence; anchor verse presence per group; correlation xref signal vs mti status consistency; statistics correlation counts vs correlations block; and Session B classification completeness. Audit summary template updated to include consistency failure and root family gap sections. Section count in summary preamble updated from nine to ten.

v4.0 (2026-04-10): Complete redesign. Session B is now a multi-session, step-by-step operation running on demand against a single word. The session has three sequential stages: (1) Data audit and remediation — all data gaps identified and corrected before analysis begins, including triggering Dimension Review and Verse Context sub-processes where required; (2) Analytical passes — five-pass analysis against the clean, complete data; (3) Session C validation and update — the word study is validated against the completed data and corrected, including full correlation-confirmed connections in Section 5. The fundamental operating discipline is step-by-step: each step is completed and confirmed before the next begins. Every working detail is written continuously to the session log and observations log. No step anticipates or designs subsequent steps. Previous versions (v1–v3.1) are retained as reference.

v3.1 (2026-04-09): "What to Attach" section updated — combined Session C file model introduced.

v3 (2026-04-09): Full redefinition as analytical composition session. Five passes formalised. Session B Analytical Brief introduced as Session D handoff.

v2 (2026-03-15): Somatic evidence pass added. Spirit-soul-body classification framework added.

v1 (prior): Original four-pass structure.

---

## What This Session Is

Session B is the quality gate for each word in the programme. It runs on demand against a single word and does not advance until the word is complete in three respects:

1. **Data complete.** Every field in the registry is correctly populated. Every data gap has been patched and confirmed. Verse context is sound. Dimension data has reached `CLAUDE_AI` confidence. All correlation signals can fire correctly from the clean data.

2. **Analysis complete.** A rigorous five-pass analysis has been conducted against the clean data, producing verified findings on meaning, divine dimension, somatic evidence, spirit-soul-body classification, and language accuracy.

3. **Word articulation complete.** The Session C word study has been validated and updated to reflect the complete data and analysis. Section 5 (connections) names every correlation-confirmed connection, characterises it accurately from the data, and raises the right questions for Session D — without drawing synthesis conclusions that require cross-word data Session B does not have.

Session B is a multi-session operation. A single session may cover only part of one stage. The session log is the continuous record across all sessions for this word.

---

## Pipeline Position

```
Session A  (data extraction → complete JSON)
    ↓
Session C  (primary word articulation → word study v1)
    ↓
Session B  (this session — multi-session operation)
    ├── Stage 1: Data audit and remediation
    │     ├── Audit: read JSON, identify all gaps
    │     ├── Patch: field-level corrections
    │     ├── Verse Context sub-process (if triggered)
    │     ├── Dimension Review sub-process (if triggered)
    │     └── Fresh extract: Claude Code re-exports clean JSON
    ├── Stage 2: Analytical passes (five passes against clean JSON)
    └── Stage 3: Session C validation and update
          ├── Validate word study against complete data
          ├── Rectify all errors, gaps, and omissions
          └── Update Section 5 with correlation-confirmed connections
    ↓
Session D  (cross-word synthesis → uses complete, clean word data)
```

---

## What to Attach at Session Start

- This instruction file
- The complete word data export: `wa-[nnn]-[word]-complete-[date].json`
- The Session C word study: `wa-[nnn]-[word]-word-study-v[n]-[date].md`
- For Stage 1 Dimension Review sub-process: `WA-DimensionReview-Instruction-v1.9-2026-04-09.md`
- For Stage 1 Verse Context sub-process: `WA-VerseContext-Instruction-v2.5-20260409.md`

Do not attach sub-process instruction documents until the sub-process is triggered. Do not load data beyond what the current step requires.

---

## Governing Disciplines

These disciplines apply without exception across all stages and all sessions.

**Step-by-step.** Each step is completed and confirmed before the next begins. Do not design, anticipate, or pre-empt future steps from the current step.

**Write on discovery.** Every finding, decision, gap, patch consequence, and open question is written to the observations log and session log at the moment it is determined. Nothing is accumulated in memory for later transcription.

**Data is authoritative.** Work strictly from what is in the JSON. Do not assume, infer from general knowledge, or overlook something because it appears to be another session's responsibility. If the data is wrong, fix it. If it is missing, flag it.

**No assumptions.** If a field is null, it is null — not implicitly populated. If a count looks wrong, check it. If a statement in the word study is not supported by the data in the JSON, it is unsupported.

**All changes through patches.** No field is updated by assertion. Every correction is encoded in a patch, reviewed, and applied by Claude Code. Claude AI produces directives and patches. Claude Code executes them.

**Load only what is needed.** Do not load more data into the working session than the current step requires. Large registries are read section by section. Verse records are read term by term.

**Session logs at every breakpoint.** A session log is produced whenever the session pauses, ends, or transitions between stages. The session log is the handoff document for the next session.

---

## What This Session Produces

| Output | Stage | Type |
|---|---|---|
| Observations log | All stages | Running analytical record — written continuously |
| Session log | All stages | Breakpoint summary — produced at every pause or end |
| Data audit findings | Stage 1 | List of every gap found, with patch consequence |
| Field-level patch(es) | Stage 1 | JSON patch(es) for Claude Code — one patch per correction set |
| Claude Code directive(s) | Stage 1 | Structured instructions for Claude Code operations |
| Verse Context sub-process outputs | Stage 1 (if triggered) | Per VC instruction |
| Dimension Review sub-process outputs | Stage 1 (if triggered) | Per DR instruction |
| Clean complete JSON | Stage 1 end | Re-exported by Claude Code after all corrections confirmed |
| Analytical brief | Stage 2 | Internal — structured findings for Session D input |
| Verse annotations | Stage 2 | For Session C Section 3 |
| Language annotations | Stage 2 | For Session C Section 4 |
| Session C word study (updated) | Stage 3 | v2 or higher — rectified and correlation-complete |

---

## Stage 1 — Data Audit and Remediation

### 1.1 Purpose

To identify every data gap, field error, stale value, and structural inconsistency in the word's complete JSON before any analysis is performed. To produce and apply corrective patches for every gap found. To trigger the Verse Context or Dimension Review sub-processes where the data requires it. To obtain a clean, complete JSON before Stage 2 begins.

Stage 2 does not begin until Stage 1 is fully complete and Claude Code has confirmed the clean extract.

### 1.2 Startup

Before reading any data:

1. State that this instruction has been read in full.
2. Confirm the word, registry number, and JSON filename being audited.
3. Initialise the observations log on disk with header, filename, date, instruction version, and input file references.
4. Initialise the session log on disk.
5. State the current session number (Session 1, Session 2, etc.) for this word.

### 1.3 Audit Sequence

Read the JSON one section at a time in the order below. After each section, write findings to the observations log before moving to the next section. Do not read ahead.

**Section 1 — Registry block**

Check every field in the registry record. For each field, determine: is it populated, is the value correct, is it consistent with other fields?

Fields to check:

| Field | What to check |
|---|---|
| `word`, `no`, `id` | Present and consistent |
| `cluster_assignment` | Populated |
| `verse_context_status` | Must be `Complete` before Stage 1 can proceed |
| `session_b_status` | Note current value |
| `dim_review_status` | If null → Dimension Review sub-process will be required |
| `dim_review_version` | If null → Dimension Review not yet run |
| `sb_classification` | If null → not yet assigned; will be addressed in Stage 2 Pass 4 |
| `sb_classification_reasoning` | If null → not yet assigned |
| `unique_term_count` / `shared_term_count` / `term_sharing_ratio` | These are registry-level fields, not statistics block fields — they do not appear in the statistics block of the extract. Note their values as recorded. Do not attempt to verify or correct them as part of the statistics audit. |
| `strongs_list` | Cross-check every Strong's number against the terms array. Deleted terms are present in the Session B export by CC design — their presence in the strongs_list is expected and correct, not an error. Verify consistency: every entry in the strongs_list must have a corresponding term in the terms array with a recorded mti.status. Then apply the **deletion justification review** (see below) to every delete-status term. Flag any count that does not match the term's active verse records. |

**Deletion justification review — mandatory for every delete-status term in the strongs_list:**

For each term where mti.status = delete, read the term's semantic content, sense structure, and verse corpus and answer all four questions:

1. Does this term name an inner-being characteristic, mechanism, or structural property relevant to this registry — even indirectly?
2. Does the exclusion_reason field contain a documented analytical rationale? If exclusion_reason is null, treat the deletion as unreviewed and apply greater scrutiny.
3. Could the inner-being content this term carries be relevant to Session D cross-registry synthesis, even if it does not fit the registry's primary analytical face?
4. Is the deletion based on semantic irrelevance, or on adequacy-of-coverage by other active terms? Adequacy-of-coverage is a weaker justification — challenge it when the term names something structurally distinct from what the active terms cover.

If the review finds that a deleted term carries analytically significant inner-being content not fully covered by active terms, flag it for researcher review with a full analytical statement. Do not simply accept the deletion. |
| `dimensions` | Note what is recorded; this is the pre-review label |

Write all findings to observations log. Record each field as: `OK`, `GAP: [description]`, or `ERROR: [description]`.

---

**Section 2 — Statistics block**

Check every count in the statistics block against the actual data in the JSON.

Fields to check:

| Field | How to verify |
|---|---|
| `term_count` | Count all terms in the terms array |
| `active_term_count` | Count terms in the terms array where `wa_term_inventory.delete_flagged = 0`. This is inventory-level activity — it is NOT filtered by `mti_terms.status`. A term can have `mti_terms.status = delete` (programme-wide deletion pending cascade) while still having `delete_flagged = 0` in the inventory. The cascade of mti deletion status to inventory delete_flagged is a deferred operation in the Session B process. Do not subtract mti-deleted terms from this count. |
| `owner_term_count` | Count terms where `term_owner_type = OWNER` and `wa_term_inventory.delete_flagged = 0` |
| `xref_term_count` | Count terms where `term_owner_type = XREF` and `wa_term_inventory.delete_flagged = 0`. Same logic as active_term_count — inventory-level, not MTI-level. |
| `verse_count` | Count all verse records across all terms |
| `active_verse_count` | Count verse records where `delete_flagged = 0` |
| `verse_context_group_count` | Count groups in verse_context.groups |
| `verse_context_record_count` | Count context records across all groups |
| `anchor_verse_count` | Count records where `is_anchor = 1` |
| `dimension_index_count` | Count rows in dimension_index |
| `research_flag_count` | Count records in session_research_flags |
| `session_b_finding_count` | Count records in session_b.findings |
| `cross_registry_link_count` | Count records in cross_registry_links |
| `correlation_xref_pair_count` | Count entries in `correlations.xref_sharing` |
| `correlation_cooccurrence_pair_count` | Count entries in `correlations.verse_cooccurrence` |
| `correlation_dimension_pair_count` | Count entries in `correlations.dimension_overlap` |
| `correlation_root_family_count` | Count entries in `correlations.root_families` |
| `correlation_shared_anchor_count` | Count entries in `correlations.shared_anchor_verses` |

Any discrepancy between the statistics block and the actual data is an error. Record it with the correct value.

**Note on correlation counts and data state:** `correlation_dimension_pair_count = 0` is expected when `dim_review_status` is null — the dimension overlap signal requires `CLAUDE_AI` confidence, which the Dimension Review sub-process produces. Record as expected gap, not error, if Dimension Review has not yet run. All other correlation counts of zero when the word has an active verse corpus are unexpected and must be investigated.

---

**Section 3 — Terms**

For every term in the terms array:

| Check | What to look for |
|---|---|
| `status` in mti block | `extracted`, `extracted_thin`, or `delete` — note any unexpected values |
| `term_owner_type` | `OWNER` or `XREF` — consistent with programme records |
| `god_as_subject` | 0 or 1 — check against verse evidence summary; flag if likely wrong |
| `somatic_link` | 0 or 1 — check against known somatic evidence; flag if likely wrong |
| `meaning` / `meaning_numbered` | Note where null or prose-only; flag where sense structure could be specified |
| `quality_flags` | List all present; note any that require action |
| `phase2_flags` | List all present |
| `root_family` | Check that every active term carrying a documented root code has a root_family record. Where a term belongs to a root family by etymology — identifiable from shared lexical root with other terms in the registry — but has no root_family record, that is a gap. Flag it. |
| Deleted terms | Delete-status terms are present in the Session B export by CC design — this is expected and correct. For each delete-status term, apply the deletion justification review specified in Section 1 (strongs_list audit). Record the outcome for each: deletion confirmed or deletion challenged with analytical rationale. |

---

**Section 4 — Verse context groups**

For every group in `verse_context.groups`:

| Check | What to look for |
|---|---|
| `context_description` | Present and non-null |
| `classification_counts` | anchor + related + set_aside counts are internally consistent |
| Anchor designation | At least one context record has `is_anchor = 1` per group |
| Group codes | No duplicates; consistent with dimension_index references |

Note any group with no anchor verse — this is a structural gap.

---

**Section 5 — Dimension index**

For every row in `dimension_index`:

| Check | What to look for |
|---|---|
| `dimension` | Populated and from the approved vocabulary |
| `dimension_confidence` | Note the value — `KEYWORD_WEAK` means Dimension Review required |
| `dominant_subject` | If null → not yet assigned; Dimension Review required |
| `manual_override` | 0 = open; 1 = locked |
| `context_description` | Must match the corresponding `verse_context_group.context_description` |

If any row has `dimension_confidence = KEYWORD_WEAK` or `dominant_subject = null` → record as a Dimension Review trigger. The Dimension Review sub-process (Section 1.5) will be required.

---

**Section 6 — Session B block**

| Check | What to look for |
|---|---|
| `session_b.dimensions` | If null → Session B dimension data has not been written; note for Stage 2 |
| `session_b.findings` | Count and list; note any that are unresolved |

---

**Section 7 — Session D block**

| Check | What to look for |
|---|---|
| `session_d.sd_pointer_flags` | Count; note any resolved or unresolved |
| `session_d.runs` | Count |

---

**Section 8 — Research flags**

Read every entry in `session_research_flags`. For each:
- Note the flag code, label, priority, session target, and resolved status
- Flags with `resolved = 0` and `session_target = B` require action in Stage 2
- Flags with `resolved = 0` and `session_target = D` are carried forward to Session D — record but do not act on in Stage 2

---

**Section 9 — Cross-registry links**

If `cross_registry_link_count = 0` — record as expected gap; these are populated during Session D. No action required in Stage 1.

---

**Section 10 — Consistency checks**

These checks verify that the extract is internally consistent — that what one part of the data implies exists in another part actually does. A consistency failure is a gap even if no individual field appears obviously wrong.

Work through each check in sequence. Write findings to the observations log.

**10a — Root family completeness**

For every root code that appears in any term's `root_family` array, check that all other terms in this registry that share the same lexical root also carry that root code. Evidence for shared roots comes from: the related_words lists (terms listed as related to each other), transliteration patterns (shared root consonants), and the word study's Section 4 language description where available.

For each root code found:
- List all terms in this registry carrying it
- Identify any active terms that share the root but have no root_family record
- Flag any missing records as gaps requiring patch

Also check: does `root_gloss` in the `wa_term_root_family` records match the `root_gloss` shown in `correlations.root_families` for the same root code? A null root_gloss in the correlations block is not automatically an error — it may reflect the extract script's correct response to conflicting glosses across multiple registries sharing the same root code. If a mismatch or null is found, investigate the cause before treating it as a correction: check whether the root code spans multiple registries (registry_count > 1) and whether those registries carry different root_gloss values. If yes, the null is honest and the resolution requires cross-registry investigation — raise it as an open item, not a patch. If the root code is single-registry and the correlations gloss differs from the term records, that is a genuine error requiring a CC directive.

**10b — Root family correlation signal consistency**

For each root code carried by terms in this registry, check whether it appears in `correlations.root_families`. If a root code is present on multiple terms but does not appear in the correlation signal:
- If `registry_count = 1` (grace-only root) → expected; record as such
- If `registry_count` should be >= 2 but root is absent from the signal → unexpected; flag for Claude Code investigation

**10c — Dimension index vs verse context group consistency**

For every group in `verse_context.groups`, there must be a corresponding row in `dimension_index` with the same `group_code`. Check that:
- Every verse context group has a dimension index entry
- Every dimension index entry has a corresponding verse context group
- The `context_description` in the dimension index row matches the `context_description` in the verse context group — these must be identical; any divergence is an error

**10d — Anchor verse consistency**

For every group in `verse_context.groups`, confirm that at least one context record has `is_anchor = 1`. A group with no anchor verse cannot be analytically reviewed in Dimension Review Phase C. Flag any such group.

Cross-check: the `anchor_verse_count` in the statistics block should equal the count of context records where `is_anchor = 1` across all groups. Verify this.

**10e — Correlation xref signal vs term inventory consistency**

Read `correlations.xref_sharing`. For each partner registry listed, the shared strongs terms are drawn from the active term inventory (wa_term_inventory.delete_flagged = 0) — not from mti_terms.status. This is the same inventory-level logic that governs active_term_count and xref_term_count in the statistics block. A term with mti_terms.status = delete but wa_term_inventory.delete_flagged = 0 is correctly included in xref_sharing signals — its inventory-level deletion cascade has not yet been applied. Do not flag such terms as errors in the xref signal. Check:
- Is the shared_term_count consistent with the number of items in `shared_strongs`? If not, that is an error.
- Are there any terms in `shared_strongs` that have wa_term_inventory.delete_flagged = 1? If so, flag — those should not appear in the signal.

**10f — Statistics correlation counts vs correlations block**

Cross-check the five correlation count fields in the statistics block against the actual lengths of the five arrays in `correlations`. These must match exactly. Any discrepancy is an error in the statistics block.

**10g — Session B classification consistency**

If `registry.sb_classification` is populated, check that `registry.sb_classification_reasoning` is also populated and non-null. A classification without reasoning is incomplete. Conversely, if `session_b.dimensions` is null but `sb_classification` is populated, note that the registry-level classification exists but the Session B dimensions table has not been written — this is a partial write gap.

---

After completing all ten sections (Sections 1–9 and the consistency checks in Section 10), write an audit summary to the observations log:

```
## AUDIT SUMMARY — Registry [nnn] ([word]) | [date]

### Fields confirmed OK
[list]

### Gaps requiring field-level patch
[For each gap: field name | current value | correct value | patch action]

### Consistency failures requiring patch
[For each failure: check reference (10a–10g) | what is inconsistent | patch action]

### Verse Context sub-process required?
[ ] Yes — reason: [state which groups or terms triggered this]
[ ] No

### Dimension Review sub-process required?
[ ] Yes — reason: [state which groups triggered this — all KEYWORD_WEAK / null dominant_subject]
[ ] No

### Statistics corrections required?
[ ] Yes — [list each field and correct value]
[ ] No

### strongs_list — deletion justification review
[ ] All deletions confirmed — no reinstatement required
[ ] Reinstatement required — [list each term, analytical basis, and reinstatement action]

### strongs_list — inventory corrections required?
[ ] Yes — [list corrections: missing active terms, count errors]
[ ] No

### Root family gaps
[ ] Yes — [list each term and root code missing]
[ ] No

### Open items requiring researcher decision
[list any items Claude AI cannot resolve from the data alone]
```

Present the audit summary to the researcher before producing any patches. Do not proceed to remediation until the researcher has reviewed the summary.

---

### 1.5 Remediation — Sequence

Remediation proceeds in the following order. Each step is completed and confirmed before the next begins.

**Step A — Field-level patches**

Produce a patch for all field-level corrections identified in the audit. This includes:
- `strongs_list` corrections (adding reinstated terms, correcting counts — deleted terms are retained by design)
- Statistics block corrections
- `god_as_subject` and `somatic_link` corrections where the audit identified clear errors
- Any other field corrections that do not require sub-process input

Deliver patch to researcher. Wait for Claude Code confirmation before proceeding to Step B.

**Step B — Verse Context sub-process (if triggered)**

If the audit identified verse context gaps — missing group descriptions, missing anchor designations, groups with no context description, or structural grouping errors — invoke the Verse Context sub-process.

Apply the rules and procedures from `WA-VerseContext-Instruction-v2.5-20260409.md`, scoped to the affected terms and groups for this word only. Produce the required patch. Deliver to Claude Code. Wait for confirmation.

Do not proceed to Step C until the Verse Context sub-process is complete and confirmed.

**Step C — Dimension Review sub-process (if triggered)**

If the audit identified dimension gaps — `KEYWORD_WEAK` confidence on any group, null `dominant_subject` on any group, or null `dim_review_status` on the registry — invoke the Dimension Review sub-process.

Apply the rules and procedures from `WA-DimensionReview-Instruction-v1.9-2026-04-09.md`, scoped to this word's groups only. The full Phase A (cluster coherence) is not required — begin at Phase B (group quality review) for this word's groups, then proceed through Phase C (dimension discernment) for each group.

The output is a dimension patch covering:
- `dimension` confirmed or corrected for every group
- `dimension_confidence` updated to `CLAUDE_AI` for every group
- `dominant_subject` assigned for every group
- `dim_review_status` set to `Complete` on the registry record
- `dim_review_version` set to the governing instruction version

Deliver patch to researcher. Wait for Claude Code confirmation before proceeding to Step D.

**Step D — Fresh extract**

Once all patches from Steps A, B, and C have been applied and confirmed by Claude Code, direct Claude Code to produce a new complete JSON export for this word.

```
CC DIRECTIVE — FRESH EXTRACT
Registry: [nnn] — [word]
Action: Produce fresh complete export
Filename: wa-[nnn]-[word]-complete-[date].json
Reason: All Stage 1 patches applied and confirmed. Stage 2 requires clean data.
Confirm: All fields, statistics, dimension index, and session_b block must reflect applied patches.
```

Do not begin Stage 2 until the fresh extract is in hand and has been spot-checked against the audit findings.

**Step D spot-check**

Read the fresh extract. Verify:
- Every gap identified in the audit is now resolved
- Statistics block values match the actual data
- Dimension index shows `CLAUDE_AI` confidence on all groups
- `dominant_subject` populated on all groups
- `dim_review_status = Complete` on the registry record
- `strongs_list` reflects the correct active and delete-status term inventory — no spurious entries, no missing active terms

Write the spot-check result to the observations log. If any gap remains, produce a further patch before proceeding.

---

## Stage 2 — Analytical Passes

### 2.0 Startup

Stage 2 begins only after:
- Stage 1 is fully complete
- The fresh extract has been received and spot-checked
- The session log records Stage 1 completion

State at the start of Stage 2: "Stage 1 complete. Fresh extract confirmed. Beginning Stage 2 against `[filename]`."

The six passes are conducted in sequence. Each pass is completed before the next begins. Findings from each pass are written to the observations log before the pass closes.

---

### 2.0a — Cross-Registry Vision (Governing Discipline for All Passes)

**This discipline is active throughout every pass. It is not a Pass 6 task.**

Every piece of data read in Stage 2 is read twice: once for what it says about this word, and once for what it says about something beyond this word. The second reading is the source of Session D flags.

**The standing questions — active whenever any data is read:**

1. **The verse question:** What inner-being states does this verse name, imply, or presuppose beyond the one that generated its group classification? A verse may encode a sequence (grace precedes repentance), a condition (pride must yield before grace can operate), a contrast (grace vs. self-sufficiency), or a co-presence (grace and fear appearing together) that is not captured by the group it belongs to. Read for all of these.

2. **The multi-term question:** When a verse contains vocabulary that belongs to more than one registry, have all the registries it implicates been considered? A verse anchored in grace that also mentions fear, strength, knowledge, or calling may carry inner-being content for those registries that no correlation signal will surface automatically.

3. **The structural question:** Does the relationship between two inner-being states visible in this verse — causal, sequential, oppositional, co-constitutive — represent something that Session D needs to examine across the programme corpus? Not just "these two words co-occur" but "this verse shows that one cannot be fully understood without the other."

4. **The absence question:** What is conspicuously absent from this verse that you would expect to find? The absence of a term in a context where it would be expected is as analytically significant as its presence.

5. **The dimension question:** Does the dimension assigned to this group appear in a very different cluster, and does its presence in both places reveal something about how that dimension operates across the inner-being landscape?

**How to raise flags from this reading:**

Whenever any of the five questions above produces an observation, write a Session D pointer immediately to the observations log — do not accumulate for later. The pointer must contain:
- The specific verse, group, or data point that generated the observation
- The registries implicated (by number and word)
- The analytical question for Session D — stated as a question, not a conclusion
- Why this cannot be answered within this registry's data alone

**What Pass 6 does with this material:**

Pass 6 verifies that the correlation signals are covered and that no data-confirmed connection is missing a flag. It does not generate all flags. By the time Pass 6 runs, the observations log should already contain Session D pointers from every pass that found cross-border content. Pass 6 is the verification and gap-fill pass, not the generation pass.

**The discipline stated as a rule:**

> Reading a verse and asking only "what does this tell me about this word?" is an incomplete reading. Every analytical act in Stage 2 includes the cross-registry question. If a verse reveals an inner-being relationship that involves another registry, that relationship is flagged for Session D — regardless of whether a correlation signal fired for it.

---

---

### Pass 1 — Meaning and Semantic Range

**Purpose:** Establish a complete and accurate picture of what each owner term means, how its meaning varies across its usage range, and where the boundaries of the word's semantic territory lie.

**Method:**
- For each owner term, read the full Mounce definition, all BDB senses, and the LSJ entry where available
- Read the context group descriptions for that term — these are the programme's own semantic clustering of the verse evidence
- Identify the primary sense, any secondary senses, and any edge or boundary senses
- Note where the translation range reveals semantic breadth that a single gloss obscures
- Note where different senses in the same term create internal tensions

**Database write-back:** For each owner term, confirm or update `meaning_numbered` where the sense structure can be specified more precisely than a prose-only block. Produce a patch if updates are required.

**Session C check:** Compare findings against Section 1 (Characteristic Summary) and Section 2 (Impact Description). Note every statement that is confirmed, complicated, or contradicted.

**Cross-registry reading (Section 2.0a):** While reading sense structures and group descriptions, note: does any sense of this word presuppose, enable, or oppose an inner-being state that belongs to another registry? Does the semantic boundary of this word reveal something about where one inner-being characteristic ends and another begins? Raise Session D flags immediately on discovery.

**Purpose:** Establish the pattern of divine involvement — where God is the subject, where the word describes a characteristic of God, and how the divine dimension shapes the human dimension.

**Method:**
- Read all verses where God is the named or implied subject of the term's action
- Identify the dominant pattern: does God primarily give this characteristic, model it, command it, withhold it, restore it, or pour it out?
- Identify the divine-human relationship: is the human characteristic derivative (received from God), responsive (answering to God's action), or parallel (operating by the same principle)?
- Note any eschatological dimension — is the full expression of this characteristic presented as a future gift?

**Database write-back:** Update `god_as_subject` for any term where the audit or pass analysis reveals an incorrect value. Add `FRAMEWORK_SIGNAL` phase2 flag where the divine-human relationship has direct implications for the spirit-soul-body classification.

**Session C check:** Verify Sections 1 and 2 statements about the ultimate source of the characteristic. Confirm or correct.

**Cross-registry reading (Section 2.0a):** The divine dimension is one of the most productive sources of cross-registry flags. When God acts in a verse — giving grace, commanding love, withholding mercy, pouring out a spirit — ask: what other inner-being states are implicated in the same divine act? Does the pattern of divine involvement with this word reveal a structural relationship with another characteristic that Session D needs to examine? Raise flags immediately.

**Purpose:** Produce a structured annotation for every anchor verse, ready for incorporation into Session C Section 3.

**Method:**
- Extract every anchor verse (all context records where `is_anchor = 1`) with their context group descriptions
- For each anchor verse, write an annotation of 3–6 sentences that:
  - Names what this verse does that the plain summary statement could not fully carry
  - Draws on the verse's specific language, grammar, or context to make a precise observation
  - Connects the verse to the broader semantic picture established in Pass 1
  - Notes anything surprising, complex, or theologically significant that a plain reading might pass over
  - Is written in accessible language — no Strong's numbers, no technical notation

- Additionally: read all verse records for each owner term. Flag any non-anchor verse that:
  - Contains a usage not represented by any anchor verse
  - Directly contradicts or complicates a statement in Sections 1 or 2 of the word study
  - Contains significant somatic language relevant to Pass 4

**Output format:**
```
REFERENCE: [book chapter:verse]
STRONG'S: [term identifier]
CONTEXT GROUP: [group code]
ANCHOR: yes / supplementary
ANNOTATION: [3–6 sentences]
SESSION C FLAG: [confirm / correct / deepen / add] — [which statement this addresses]
```

**Database write-back:** Tag each anchor verse record with annotation status. Add `VERSE_ANNOTATION_COMPLETE` flag when all anchors are annotated.

**Cross-registry reading (Section 2.0a) — this is the primary pass for cross-registry observation.** Every anchor verse is read for cross-border content. For each anchor verse, after writing the annotation, apply the five standing questions from Section 2.0a explicitly:
- What other inner-being states does this verse name, imply, or presuppose?
- Does this verse show a sequence, condition, contrast, or co-presence between inner-being states that implicates another registry?
- Does this verse contain vocabulary that belongs to more than one registry — and if so, have all implicated registries been considered?
- Is anything conspicuously absent?
- Does the verse as a whole encode a structural inner-being relationship that Session D needs to examine?

Any observation that passes any of these questions becomes a Session D pointer, written immediately to the observations log. This is the pass where the most flags will be generated — do not defer.

**Purpose:** Establish the bodily dimension of the word and assign the provisional spirit-soul-body classification.

**4a — Somatic scan.** Read all verse records for owner terms. For each verse containing body-part reference, physical posture, physiological reaction, or somatic expression, record:
- The verse reference
- The body part or somatic expression named
- Classification: `origin` (body is where this word begins) / `expression` (body manifests it) / `instrument` (body performs it) / `absence` (purely interior state)

Body-part vocabulary to scan for includes: heart, soul, spirit, eye, face, mouth, lip, hand, knee, foot, breath, bowels, bones, flesh, skin, tears, weeping, prostration, fasting, sackcloth.

**4b — Somatic pattern summary.** Describe the somatic signature:
- Which body parts are most associated with this word?
- Is somatic expression concentrated or diffuse?
- Is the body the origin or the expression of the word's movement?
- What does the somatic evidence suggest about the spirit-soul-body level?

**4c — Spirit-soul-body provisional classification.** Assign one of:
- `Spirit-primary` — originates in the spirit; received from God; above natural human capacity
- `Soul-primary` — characteristic of the inner life; distinctively human; within natural experience
- `Body-primary` — primarily expressed through or triggered by the physical body
- `Spirit-soul interface` — received at spirit level, expressed at soul level
- `Soul-body interface` — felt inwardly, expressed outwardly through the body
- `Trichotomy-spanning` — operates across all three dimensions simultaneously

Provide reasoning drawn from the somatic evidence and meaning analysis.

**Database write-back:** Update `somatic_link` for any term where somatic evidence warrants it. Add `SOMATIC_FLAG_RECOMMENDED`, `SPIRIT_SOUL_BOUNDARY`, or `BODY_SOUL_BOUNDARY` phase2 flags as warranted. Write provisional classification to `sb_classification` and reasoning to `sb_classification_reasoning`. Produce patch if updates are required.

**Session C check:** Review Section 1 statements about origin or manner of the characteristic. Confirm, deepen, or correct.

**Cross-registry reading (Section 2.0a):** Somatic evidence is cross-registry by nature — the same body-state (fasting, prostration, weeping, raised hands) appears across many registries. When somatic evidence is found, ask: does this body-state appear in other registries, and does its presence in both places reveal something about the shared inner-being ground? A body-state that appears in grace, repentance, and mourning simultaneously may be encoding the same inner-being posture — Dependence/Creatureliness — across three registries. Raise flags for these cross-somatic patterns.

**Purpose:** Audit Section 4 of the word study (Critical Terms Review) for accuracy and completeness.

**5a — Accuracy audit.** Read Section 4 against the lexical data in the JSON. Check:
- Are stated senses accurate and complete against Mounce / BDB / LSJ?
- Are occurrence counts correct? (Cross-check `occurrence_count` field against `strongs_list` counts — these measure different things; distinguish them clearly)
- Are related words correctly described?
- Are root relationships correctly stated?
- Are classical (pre-biblical) usages from LSJ that would inform the review missing?
- Does the semantic synthesis observation hold up?

**5b — Completeness audit.** Check:
- Are all owner terms covered?
- Are significant associated words adequately described?
- Are there related words list entries that warrant more attention?
- Are there observations in LSJ entries that were not surfaced?

**5c — Language annotations.** For each correction, addition, or deepening:
```
TERM: [Strong's number and transliteration]
TYPE: correction / addition / deepening
ANNOTATION: [the specific observation, stated precisely]
SESSION C FLAG: [which statement or section this addresses]
```

**Database write-back:** No new fields updated in this pass. If the audit reveals a Strong's number error or incorrect gloss in the MTI, flag separately for researcher correction.

**Cross-registry reading (Section 2.0a):** Etymology and semantic range are cross-registry by nature. When a term's root family, classical usage, or semantic boundary is examined, ask: does this etymology connect to vocabulary in another cluster? Does the semantic range of this term overlap with a term in a different registry in a way that raises a structural question about the boundary between two inner-being characteristics?

---

### Pass 6 — Correlation Audit and Connection Verification

**Purpose:** Verify that every correlation signal in the clean extract has been addressed by a Session D pointer, and raise flags for any signals not yet covered. This pass does not generate all flags — that work happens continuously throughout Passes 1–5. Pass 6 is the verification and gap-fill pass.

**Important:** By the time this pass runs, the observations log should already contain Session D pointers generated during Passes 1–5 from direct reading of verses, group descriptions, and lexical data. If Pass 6 finds that the observations log has very few Session D pointers at this point, that is a signal that the cross-registry discipline in Section 2.0a was not applied during the earlier passes — not that the word has few connections.

**Method:**

Read every correlation signal in the extract:
- `xref_sharing` — which registries share terms with this word, and which specific terms
- `verse_cooccurrence` — which registries co-occur in verses with this word, and counts
- `dimension_overlap` — which registries share confirmed dimensions (requires `CLAUDE_AI` confidence — now available after Stage 1)
- `root_families` — which registries share root families
- `shared_anchor_verses` — which registries share anchor verses, and which specific verses

For each signal, record:
- The partner registry number and word
- The signal type(s) present
- The specific evidence (shared terms, shared verses, shared dimensions, shared roots)
- Whether the connection is within the same cluster or cross-cluster

After reading all signals, produce a ranked connection summary:

```
CONNECTION: Reg [nnn] ([word])
SIGNALS: [list signal types present]
EVIDENCE: [specific shared terms / verses / dimensions / roots]
CLUSTER: same / cross — [clusters named]
NATURE: [one sentence describing what kind of connection this is]
```

**Session C check:** Compare against the existing Section 5 connections table. For each connection:
- Is it present in Section 5? If not → add
- Is the nature characterisation accurate? If not → correct
- Is the priority rating justified by the signal strength? If not → revise
- Is the key question still the right question given the data? Confirm or update

Flag any connection in Section 5 that is not confirmed by any correlation signal — these are inferential and must be labelled as such.

**Final gap-fill:** After completing the signal audit, review the full Session D pointer list in the observations log. For each pointer raised in Passes 1–5, confirm it is grounded in specific data. For each correlation signal, confirm it has at least one pointer. If any signal has no pointer, raise one now with the specific evidence and the analytical question it generates.

---

### 2.1 Analytical Brief (Handoff to Session D)

After completing all six passes, produce the Session B Analytical Brief. This is an internal document, not reader-facing.

**Sections:**

1. **Registry summary** — word, registry number, term count, verse count, Session B date, clean extract filename
2. **Meaning findings** — primary semantic picture, significant tensions, senses underrepresented or missing from Session C
3. **Divine dimension summary** — dominant pattern of divine involvement, divine-human relationship, eschatological dimension
4. **Somatic signature** — body-part vocabulary, somatic classification summary, provisional spirit-soul-body assignment with confidence level (high / medium / low)
5. **Spirit-soul-body provisional classification** — one sentence with brief reasoning
6. **Session C corrections and additions** — every place where Session B found a statement needing correction, addition, or deepening, with specific reference to which section and which statement
7. **Correlation-confirmed connections** — every connection confirmed by Pass 6, with signal evidence and nature characterisation
8. **Cross-word questions for Session D** — the open analytical questions that require cross-word data, with specific verse or term evidence that generates each question. These are questions only — Session B does not attempt to answer them.
9. **Open items** — anything the six passes raised but could not resolve from this registry's data alone

---

## Stage 3 — Session C Validation and Update

### 3.1 Purpose

To produce an updated Session C word study that accurately reflects the complete data and the Session B analysis. The updated word study is the final published articulation of this word in the programme — it must be correct, complete, and honest about what is known and what is not yet known.

### 3.2 Validation Process

Read every section of the existing Session C word study against the Session B findings. For each section, identify:
- Statements confirmed by the data — mark as confirmed
- Statements that need correction — produce corrected text
- Statements that need deepening — produce additional text
- Statements that need removal — flag with reason
- Gaps where required content is missing — produce new text

### 3.3 Section 5 — Connections

Section 5 is the section most directly shaped by Session B's work. It must be completely rewritten if necessary to reflect the correlation-confirmed picture.

**Section 5 must:**
- Name every connection confirmed by a correlation signal (Pass 6), with the signal type and specific evidence stated
- Name every inferential connection that is not confirmed by a correlation signal, and label it explicitly as inferential
- For each connection, characterise its nature accurately from the data
- For each connection, state the open question for Session D — the specific analytical question that cross-word data is needed to answer
- Not draw synthesis conclusions about what the connections mean — that is Session D's work

**Section 5 must not:**
- State a connection as confirmed when it is only inferential
- Omit a connection that is confirmed by signal data
- State a priority rating that is not justified by the signal evidence
- Answer questions that require Session D data to answer

### 3.4 Output

The updated word study is produced as a new version:
- Filename: `wa-[nnn]-[word]-word-study-v[n+1]-[date].md`
- Change note appended to the internal Session C completion note section

---

## Analytical Principles

**Cross-registry vision is always active.** Every analytical act in Stage 2 includes the question: what does this data tell me about something beyond this word? Session D flags are raised continuously throughout all passes — not accumulated for Pass 6. A verse read without asking what it reveals about other inner-being states is a verse incompletely read. The discipline is stated fully in Section 2.0a.

**The data is authoritative.** Every finding must be traceable to a specific verse record, term entry, lexical source, or correlation signal in the JSON. Do not import general theological knowledge to fill gaps.

**Emergence, not imposition.** The spirit-soul-body classification, somatic signature, semantic picture, and connection characterisations must emerge from the evidence. Do not assign a classification and then select evidence to support it.

**Session C documents are not sacred.** Session B exists to correct, deepen, and complete them. An accurate document that has been corrected is more valuable than an accessible document that contains errors.

**Correlation signals confirm connections; they do not explain them.** Pass 6 reads what the data shows. The nature characterisation is Claude AI's analytical reading of the signal. The explanation of what the connection means is Session D's work.

**Inferential is not confirmed.** Where a connection is theologically plausible but not supported by a correlation signal, it is inferential. Label it as such. Do not upgrade it.

**Phase 2 flags are recommendations, not conclusions.** Flag what the data warrants. Do not over-flag.

**Somatic evidence is observational, not interpretive.** Record what the verses say about bodily involvement before interpreting what it means.

---

## Integrity Rules

| Rule | Requirement |
|---|---|
| SB-1 | Stage 2 does not begin until Stage 1 is fully complete and the fresh extract is confirmed |
| SB-2 | Stage 3 does not begin until Stage 2 is fully complete and the analytical brief is written |
| SB-3 | No patch is applied without researcher review |
| SB-4 | No dimension may reach `CLAUDE_AI` confidence without the Dimension Review sub-process completing Phase B and Phase C for that group |
| SB-5 | Every session log must record the current stage, the last completed step, and the next step |
| SB-6 | The observations log is the complete analytical record — the session log is a summary. If there is a conflict between them, the observations log governs |
| SB-7 | Section 5 of the updated word study must not contain a confirmed connection that is not supported by at least one correlation signal |
| SB-8 | Section 5 of the updated word study must not omit a connection that is supported by a correlation signal |
| SB-9 | Cross-word synthesis conclusions are not permitted in Session B outputs — questions only |
| SB-10 | `dominant_subject` must be assigned for every dimension index group before Stage 2 begins |
| SB-11 | Session D pointers must be raised at the moment of discovery during any pass — not accumulated for Pass 6 |
| SB-12 | Every anchor verse must be read against all five standing questions in Section 2.0a before its pass closes |
| SB-13 | Pass 6 must not be the only pass that generates Session D pointers — if it is, Stage 2 must be repeated from Pass 1 |

---

## Naming Conventions

| File type | Pattern | Example |
|---|---|---|
| Session log | `wa-[nnn]-[word]-sessionB-log-v[n]-[date].md` | `wa-068-grace-sessionB-log-v1-2026-04-10.md` |
| Observations log | `wa-[nnn]-[word]-sessionB-observations-v[n]-[date].md` | `wa-068-grace-sessionB-observations-v1-2026-04-10.md` |
| Field-level patch | `wa-[nnn]-[word]-sessionB-patch-v[n]-[date].json` | `wa-068-grace-sessionB-patch-v1-2026-04-10.json` |
| Dimension Review patch (from sub-process) | `wa-dim-[cluster]-[nnn]-patch-v[n]-[date].json` | `wa-dim-c17-068-patch-v1-2026-04-10.json` |
| CC directive | `wa-[nnn]-[word]-sessionB-cc-directive-v[n]-[date].md` | `wa-068-grace-sessionB-cc-directive-v1-2026-04-10.md` |
| Analytical brief | `wa-[nnn]-[word]-sessionB-brief-v[n]-[date].md` | `wa-068-grace-sessionB-brief-v1-2026-04-10.md` |
| Updated word study | `wa-[nnn]-[word]-word-study-v[n]-[date].md` | `wa-068-grace-word-study-v3-2026-04-10.md` |

All filenames lowercase.
