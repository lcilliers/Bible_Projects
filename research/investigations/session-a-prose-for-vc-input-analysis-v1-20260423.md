# Session A Prose as VC Input — Design Analysis

**Date:** 2026-04-23
**Purpose:** decide exactly what the per-word Session A `.md` must contain so that Claude AI can perform Verse Context classification reading *only* that document. Derived from a close read of [wa-versecontext-instruction-v2_8-20260418.md](../../data/imports/WA/Workflow/Framework_B/Session_B/wa-versecontext-instruction-v2_8-20260418.md).
**Status:** AWAITING APPROVAL. On approval → build `scripts/build_session_a_prose.py` → generate for the 5 BANKED registries → run a fresh VC pass.

---

## 1. Method

The VC instruction is the authoritative specification of what the AI must do. The content of the Session A `.md` is therefore derived from it by two questions:

1. **What does the AI actually do?** — gives the list of inputs it must have.
2. **What does the instruction say the AI does NOT do?** — gives the list of inputs to leave out, because including them risks contamination (the AI starts to do downstream work from Session A data).

Sections 2 and 3 answer those two questions. Section 4 maps the answers onto the six seeded Session A handles. Section 5 is the explicit exclusion list with reasons. Section 6 covers the workflow change this enables.

---

## 2. What the AI does in VC — inputs the `.md` must carry

From the VC instruction, the AI's per-term sequence is:

| Step | Instruction ref | What the AI does |
|---|---|---|
| 1. Read all verses | §6.2 Step 1 | Read every verse for the term before classifying. "Note the term's gloss and any existing_groups before beginning. Understand what the term means before filtering verses." |
| 2. Apply the filter | §3, §6.2 Step 2 | Per-verse: does **this term's use in this verse** engage inner being? Mark `is_relevant = 1` or `0`. If `0`, record a `set_aside_reason` from the controlled vocabulary. |
| 3. Group relevant verses | §6.2 Step 3 | Characteristic-perspective grouping. Reuse existing_groups where they fit; create new only when materially different. Write a one-sentence `context_description` per group. |
| 4. Designate anchors | §4, §6.2 Step 4 | 1–2 anchor verses per group. Must stand alone as evidence. Every term needs ≥1 anchor (rule R4). |
| 5. Flag dual-context | §6.2 Step 5 | Where one verse operates at two inner-being levels through the same term, assign to two groups. |
| 6. Revise prior classifications if warranted | §6.2 Step 2 revision rule | If existing classification misrepresents the term's function, supersede it. Note the reason. |

From this, the **minimum input per term** is:

- Term identity: `mti_term_id`, `strongs_number`, `transliteration`, `gloss`, `language`, `mti_status` (extracted vs extracted_thin)
- Owning registry identity: `owning_registry_id`, `owning_registry_word`, `registry_verse_context_status`
- Every verse: `verse_record_id`, reference (e.g. "Rom 2:24"), full ESV verse text, target word form, `span_strong_match` indicator, `delete_flagged` state
- Any prior `verse_context` state for each verse (so the AI can review/revise)
- Any existing `verse_context_group` rows for the term (so the AI can reuse or supersede, including dissolved groups — the AI should see dissolved to avoid recreating them)
- Term-level counts: `total_verses`, `unclassified_count`, `term_classification_complete`

**And one piece that the current batch JSON does not carry but the instruction assumes the AI holds in working memory:** the governing filter itself (§3) and the grouping model (§6.2 Step 3). These live in the instruction document. Two options for the `.md`:

- **Option A (purer):** trust the instruction is loaded separately. Session A `.md` carries data only.
- **Option B (belt-and-braces):** embed a short "filter rules applicable" block at the top of the `.md` quoting §3 and §6.2 Step 3, so even if the instruction is not re-loaded, the AI has the filter in hand.

**My recommendation: Option B.** It's a handful of paragraphs. It protects against the class of error where the AI tries to reconstruct the filter from memory or training. Costs almost nothing in token budget.

---

## 3. What the AI does NOT do in VC — inputs to exclude

§0 of the instruction is explicit:

> **What Verse Context does NOT do:**
> - Analyse the meaning of terms in depth — that is Session B Analysis
> - Draw conclusions about the word being studied — that is Session B Analysis
> - Produce cross-registry synthesis — that is Session D
> - Assign evidential status to terms — that is Session B Analysis
> - Classify XREF terms directly — XREF status is derived from OWNER classification

This produces a direct exclusion list for the Session A `.md`:

| Exclude | Why |
|---|---|
| Session B analytical output: per-word narratives, findings, dimensional placements | VC is upstream of Session B. Including these lets the AI do Session B reasoning while it should be doing Session B-free verse filtering. |
| Session D cross-registry synthesis or pointers | Cross-registry work is downstream. Including it lets the AI form inter-word opinions during a per-word classification pass. |
| Evidential status on terms (`evidential_status`) | §0: assigned at Session B, not here. |
| Derived or analytical flags (PH2_*, SB_*, SD_*) | Same reason — these are Session B/D products. |
| Dimensional profiles (cluster, dimension, group-to-dimension mapping) | Dimension Review is a separate stage downstream of VC. Including its outputs pre-commits the classifier to an existing dimensional frame — which is the wrong order (dimensions are formed from classifications, not the reverse). |
| Pool analysis data, cross-registry correlations | Programme-wide synthesis; not per-word VC input. |
| Session C prose drafts (reader-facing word studies) | Far downstream; unrelated to classification. |

**Borderline items — defensible either way:**

| Item | Keep? | Reasoning |
|---|---|---|
| `wa_meaning_parsed` / `wa_meaning_sense` / `wa_meaning_stem` / `wa_lsj_parsed` (lexical layer) | **Yes — keep** | §6.2 Step 1 explicitly instructs the AI to "understand what the term means before filtering verses". Gloss alone is a bare label; the lexical layer is what lets the AI hold the term's semantic range in mind. This is not analysis — it's STEP-sourced lexical data. |
| XREF term presence (list of Strong's that appear in this registry's inventory as XREF, with which registry OWNs them) | **Yes — keep (informational)** | The AI doesn't classify XREFs, but knowing they exist prevents two classes of error: (a) treating an XREF term's verses as if they needed classifying here, and (b) failing to notice when a term's full analytical home is elsewhere (relevant for the `wrong_face` set-aside reason per §3.6). |
| Registry `word_synopsis` (researcher-authored) | **Yes — keep if populated** | Gives the AI the inner-being frame of the specific word being analysed. Distinct from Session B analysis — this is the researcher's one-paragraph definition of the word's scope. |
| Registry `inference_note` | **Yes — keep if populated** | Researcher-authored scoping note. Same reason as synopsis. |
| Quality flags (`wa_data_quality_flags`) — informational post-M29 | **Yes — keep** | VERSE_EVIDENCE_CONCENTRATED, VERSE_EVIDENCE_MINIMAL etc. tell the AI where the corpus may be thin or concentrated. Informational only; does not drive classification decisions. |
| Observation catalogue questions linked to this registry's flags | **Marginal — keep in sa_s1_d6 Questions** | Questions surface what needs investigation. VC's classification may answer some; some are for later stages. No harm including them; they guide what the AI notices. |
| Term-level phase 2 flags (`wa_term_phase2_flags`) | **No** | These are set by Session B. Pre-contamination risk. |
| Related words (`wa_term_related_words`) | **Yes — keep** | STEP-sourced lexical data, not analytical. Helps the AI hold the term's semantic neighbourhood. |
| Root family (`wa_term_root_family`) | **Yes — keep** | Same as above. |

---

## 4. Mapping onto the six seeded Session A handles

The DB already has six `prose_section_type` rows seeded for `source_stage = 'session_a'`. The analysis above maps onto them as follows:

### `sa_s1_d1` — Session A, Word Summary

**Purpose:** one-page orientation to this word, no verses, no term-level detail.

**Content:**
- Registry identity: `no`, `word`, `cluster_assignment`, `language mix` (Hebrew/Greek term counts)
- Programme status: `phase1_status`, `phase1_term_count`, `verse_context_status`, `session_b_status`
- `word_synopsis` (if populated)
- `inference_note` (if populated)
- Total OWNER terms, total XREF terms, total active verses
- Top-line data-quality flags (informational): e.g. "VERSE_EVIDENCE_CONCENTRATED on 3 OWNER terms" — pointer only
- **Explicit statement of what this `.md` is for** — e.g. "This document is the Session A input for Verse Context classification of registry 35 covetousness. It contains all STEP-sourced data for this registry's OWNER terms and is self-sufficient for the VC classification task."

### `sa_s1_d2` — Session A, Meaning

**Purpose:** lexical context for every OWNER term so the AI can "understand what the term means before filtering verses".

**Content per OWNER term:**
- Header: `strongs_number` · `transliteration` (with pronunciation guide where available from `wa_lsj_parsed`) · `gloss` · `language`
- `wa_term_inventory` meaning fields (verbatim, no paraphrase — this is STEP's own text)
- Parsed meaning (`wa_meaning_parsed` body if present)
- Meaning senses (`wa_meaning_sense` rows if present) — numbered list
- Meaning stems (`wa_meaning_stem` rows if present) — if applicable
- LSJ notes (`wa_lsj_parsed` fields for Greek terms) — if applicable
- Related words (`wa_term_related_words`) — Strong's + gloss
- Root family (`wa_term_root_family`) — Strong's + transliteration + gloss

### `sa_s1_d3` — Session A, Verses

**Purpose:** the complete verse corpus. This is the bulk of the `.md` and the object of classification.

**Content per OWNER term** (grouped under a term header that repeats the Strong's and gloss so the AI can read term-then-verses without cross-referencing):
- For every active `wa_verse_records` row (delete_flagged = 0):
  - `verse_record_id`
  - Reference (canonical form: `Book Ch:V`, e.g. `Rom 2:24`)
  - Full ESV verse text
  - Target word form (the specific English word(s) in the verse tagged to this Strong's)
  - `span_strong_match` indicator (1 = confirmed by STEP span filter)
  - Any existing `verse_context` record for this (verse, term) pair: group_code, is_relevant, is_anchor, is_related, set_aside_reason, notes. **Present as "prior classification" so the AI can review and revise per §6.2 Step 2.**
- Summary counts: total verses, unclassified count, `term_classification_complete` state

**If there are delete_flagged verses:** append as a short "Historical verses (delete_flagged = 1)" subsection per term for completeness. The AI is told in §5.3 that "verses: include ALL verse records for the term, classified and unclassified alike — Claude AI may revise prior classifications".

### `sa_s1_d4` — Session A, Terms

**Purpose:** the programme-wide term landscape for this registry — OWNER and XREF.

**Content:**
- OWNER term table: `mti_term_id` · `strongs_number` · `transliteration` · `gloss` · `language` · `mti_status` · `total_verses` · `unclassified_count`
- XREF term table: `strongs_number` · `transliteration` · `gloss` · `language` · `OWNER registry (no + word)` · status of OWNER's VC classification (Complete / In Progress / not started)
- Note: **XREF terms are not classified here.** Their verses are delete_flagged in this registry and their programme-wide classification is inherited from the OWNER. See §0.2 of the VC instruction.

### `sa_s1_d5` — Session A, Pointers

**Purpose:** structural context — what else this registry connects to — without bleeding analytical content from Session D.

**Content:**
- Cross-registry links from `wa_cross_registry_links` (if populated) — target registry, link type, note
- XREF terms re-stated here as cross-registry pointers (their OWNER registries are the pointers)
- `register_of_OWNER_registries_whose_terms_appear_here_as_XREF` — useful for the AI to know "this registry borrows term X from registry Y" where Y is already classified (so the AI can look up an existing OWNER classification via the batch's `existing_groups` block, if applicable)

**Deliberately NOT included:** Session D clusters, pointer topics, synthesis findings.

### `sa_s1_d6` — Session A, Questions

**Purpose:** surface open questions to the AI — questions the programme has recorded against this registry but not yet answered.

**Content:**
- Catalogue questions (`wa_obs_question_catalogue` rows linked to this registry's flags via `wa_flag_type_question_link`). These are the Q-COV-01..12 family and any others tied to this registry's specific data-quality flags.
- Informational note: "These questions are recorded against this registry. Classification work may surface answers; many will be closed at Session B." — tells the AI these are for awareness, not for it to answer here.

**Deliberately NOT included:** Session B analytical Q&A content, Session C reader questions, Session D synthesis questions.

---

## 5. Explicit exclusion list (for the script specification)

The script must NOT read from or render into the Session A `.md`:

- `wa_term_phase2_flags` — Session B output
- `wa_session_research_flags` except where a flag has an explicit Session A / VC application (most will not qualify)
- `wa_session_b_findings`
- `wa_session_b_dimensions`
- `wa_dimension_index` (dimensional placements)
- `verse_context_group` or `verse_context` **for registries where VC is being re-run fresh** — **but keep them for registries where VC is being reviewed/revised.** The script should take a `--include-prior-vc` flag (default: true when prior records exist, false when none do).
- `session_d_*` tables (runs, links, observations)
- Any `prose_section` rows of `source_stage` other than `session_a` for this registry (the programme prose is loaded separately, not inlined here)
- Any Session C `prose_section` rows

---

## 6. The workflow change this enables

**Current workflow** (per v2.8 §5): Claude Code builds a batch JSON spanning up to 2,500 verses across many terms (possibly spanning multiple registries), Claude AI classifies the batch. This is a *batching* strategy — necessary when the per-word context would be too small to be efficient.

**Proposed workflow with Session A `.md`:** Claude Code builds one `.md` per registry. Claude AI classifies one registry at a time reading its `.md`. The batching concern inverts — now the concern is per-registry size (a registry with 2,000 verses will be a substantial `.md`).

**Implications:**

1. **Per-registry feels like the right grain** for the 5 BANKED registries, which are small (25–128 active verses each — very manageable in one document).
2. **Large registries may still need splitting** — e.g. soul (182), love (103), heart (183) have term counts and verse counts in the hundreds. For those, the `.md` may need to be split per term group or per-term.
3. **The `_build_vc_batch.py` batching logic doesn't vanish**; it becomes a tool for splitting large registries across multiple documents. For the pilot, we target small registries where a single per-registry `.md` is sufficient.
4. **Patch format is unchanged.** The AI still produces a `VERSECONTEXT` patch; Claude Code still applies it through the standard applicator. Only the *input* to the AI changes.

---

## 7. Candidate structure for the `.md`

```markdown
# Session A — Registry {NNN} {Word}

**Generated:** {YYYY-MM-DD HH:MM}
**Source:** `data/bible_research.db`  (deterministic render, no analytics)
**Governing instruction:** wa-versecontext-instruction [current]
**Produced by:** `scripts/build_session_a_prose.py`

---

## About this document

This document is the Session A input for **Verse Context classification** of
registry {NNN} {word}. It contains all STEP-sourced data for this registry's
OWNER terms and is self-sufficient for the VC classification task.

Read the VC instruction ([wa-versecontext-instruction [current]]) in full
before beginning. This document is the data. The instruction is the method.

(Optionally embed Section 3 filter + §6.2 Step 3 grouping rules here as
a short "Method reminder" block — Option B in §2 of the analysis.)

---

## Word Summary
{sa_s1_d1 content — one page, orientation}

## Meaning
{sa_s1_d2 content — per OWNER term lexical layer}

## Verses
{sa_s1_d3 content — the corpus, grouped by term}

## Terms
{sa_s1_d4 content — OWNER + XREF tables}

## Pointers
{sa_s1_d5 content — cross-registry structure}

## Questions
{sa_s1_d6 content — open catalogue questions}

---

## Patch construction summary (for reference)

When you produce the VERSECONTEXT patch, the expected structure is:
{short reminder of the patch format per VC §7}
```

Each heading corresponds to a `prose_section` row in the DB — so the same `.md` can be round-tripped into the prose store if desired (Session A rows, `author = 'claude_code'`, status = 'draft', `session_a_replace` for refreshes).

---

## 8. Decisions to confirm before building the script

1. **Option A vs Option B on the filter embedding** — my recommendation is B (embed Section 3 and §6.2 Step 3 into every Session A `.md`). Confirm or redirect.
2. **`--include-prior-vc` default** — on by default when records exist, off otherwise. Confirm or redirect.
3. **Dual output:** write the `.md` to disk *and* populate `prose_section` rows via `session_a_replace` so the DB is also refreshed? Or `.md` only for now and add prose-store writes once the format is proven? My recommendation: `.md` only for the pilot; add DB writes once we've confirmed the format works end-to-end.
4. **Large-registry splitting policy** — for the pilot we target the 5 BANKED registries (small); defer the split policy decision until one of the large registries is needed.
5. **Target pilot set:** 5 BANKED registries — 35 covetousness, 62 fellowship, 134 renewal, 206 vulnerability, 207 blindness (spiritual). Confirm.

---

## 9. Next steps (on approval)

1. Build `scripts/build_session_a_prose.py` per the design above.
2. Generate the five `.md` files for the BANKED registries; store under `data/exports/session_a/` (or the equivalent folder — confirm naming/location convention).
3. Spot-check one `.md` against a current batch JSON for the same registry to verify no critical field is missing.
4. Attach one `.md` to a Claude AI VC session; AI produces a VERSECONTEXT patch reading only the `.md` (plus the instruction).
5. Apply the patch via the standard applicator.
6. Evaluate: did the `.md`-driven classification produce results comparable to or better than the batch-JSON-driven classification?

If pilot clean → scale: write Session A prose for all 182 non-excluded registries, then begin the programme-wide VC re-run that `Phase_B_Verse_Context` in `tasks.md` names.

---

*Design analysis produced 2026-04-23 to scope the Session A prose renderer for VC input.*
