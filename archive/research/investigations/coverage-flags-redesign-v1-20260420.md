# Coverage Flags — Redesign Investigation — v1 — 2026-04-20

| Field | Value |
|---|---|
| Purpose | Capture researcher principle on coverage/volume flags; map scope; propose redesign |
| Trigger | Action Q investigation (OT-DBR-011/012) revealed `SMALL_VERSE_SAMPLE` classifier inconsistency; researcher articulated broader programme principle |
| Source | Researcher direction 2026-04-20 (captured in memory: `feedback_coverage_flags_philosophy.md`) |
| Scope | Cross-cutting — affects `wa_data_quality_flags` catalogue, `wa_session_research_flags`, `wa_term_inventory.evidential_status`, sweep pilot, flag_engine, instructions |
| Status | DRAFT v1.2 — M29/M30/M31 dry-run passed 2026-04-20 evening; researcher decisions absorbed on Q3/Q4/N4/N6/M30 classifier; awaiting go/no-go on live apply + clarification on one item |
| Produced | 2026-04-20 morning; extended through the day — three revisions (v1, v1.1, v1.2) |

---

## 1. The principle (researcher direction, 2026-04-20)

Coverage/volume flags were introduced early in the project to "limit volume and complexity" by downgrading attention where data was thin or a term looked marginal.

**The study has disproven the premise.** Verse count has little correlation with analytical value. Context and contents drive significance. **Absence of expected evidence** can itself be a major analytical finding (a term the researcher expected to see but doesn't).

**Therefore:**

- Coverage information IS worth knowing — it may indicate a different analytical *approach* (close reading of one verse vs. pattern analysis over many).
- Coverage information MUST NOT be inconsistent, erroneous, or used to gate/limit inclusion.
- Flag names and descriptions MUST NOT carry implicit judgement ("thin", "small", "limited", "insufficient", "marginal").
- **Every coverage flag must be paired with a research-action route and with catalogue questions that drive active investigation — flags raise questions, not conclusions.**

This becomes a **programme-wide rule** recorded in `wa-global-general-rules`, applicable to all future flag design, not just a fix for the current family.

### 1.1 Proposed Global General Rules additions (researcher direction 1)

Three new rules for `wa-global-general-rules` (next version bump — v2.12):

**GR-EVIDENCE-001 — Coverage flags are informational only.**
Any flag whose primary signal is verse count, occurrence count, or sample-to-total ratio MUST be defined as informational — it describes the shape of the data, not its analytical value. Such flags MUST NOT be used as a gate for any processing step (audit, VC, DimReview, Session A/B/C/D).

**GR-EVIDENCE-002 — Absence of expected evidence is itself a research signal.**
When a term has no or minimal verse evidence, this is not a defect but a point of investigation. It MUST trigger defined research questions (see GR-EVIDENCE-003) before being treated as resolved.

**GR-EVIDENCE-003 — Coverage flags route to research actions and catalogue questions.**
Every coverage flag type MUST declare:
(a) one or more research-action routes from the controlled vocabulary in §4.7 (e.g. `R_STEP_EXHAUST_CHECK`, `R_EXTERNAL_BIBLE`, `R_AI_WIDER_CONTEXT`, `R_RELEVANCE_REVIEW`);
(b) one or more linked questions in `wa_obs_question_catalogue` via a junction table.
Raising the flag becomes an open-research-question state until the routed investigation is recorded or dismissed with rationale.

---

## 2. Current-state inventory — the coverage family

### 2.1 Flags in `wa_quality_flag_types` that touch coverage/volume

Live counts from `wa_data_quality_flags` (all, not filtered to active — column `delete_flagged` does not exist on this table):

| Flag code | Count | Current description (excerpt) | Classification |
|---|---:|---|---|
| `NO_VERSES` | 513 | "No verse records found for this term in the source data" | **Factual — keep** |
| `NO_WORD_ANALYSIS` | 7,492 | "No word-level analysis is available for this term" | **Factual — keep** (but is this really coverage? more like meta-completeness) |
| `PROSE_ONLY_MEANING` | 5,640 | "Meaning stored as single prose block — STEP medium_def contains no structured sense numbering" | **Structural diagnostic — keep** |
| `THIN_DATA` | 4,918 | "Fewer verse occurrences than expected; **analysis may be limited**" | **RENAME — embedded judgement** |
| `SMALL_VERSE_SAMPLE` | 2,973 | "Only a **partial sample** of available verses was captured" | **RENAME + semantics mismatch (OT-DBR-011)** |
| `HIGH_FREQUENCY_ANCHOR` | 278 | "High-frequency term: N occurrences. Verse sample **represents a subset**" | **RENAME — subtle downgrade framing** |
| `SPAN_FILTER_APPLIED` | (low) | "One or more verse records were discarded by span filter" | **Factual — keep** |
| `SPAN_RESOLUTION_CONFLICT` | (low) | "Queried Strong's not found in any verse span after suffix resolution" | **Factual — keep** |
| `CONCRETE_PHYSICAL` | 315 | Semantic — term denotes concrete physical | **Not coverage — out of scope** |

### 2.2 Research flags with coverage/volume framing

| Flag code | Total | Unresolved | Current description (excerpt) | Classification |
|---|---:|---:|---|---|
| `PH2_VOLUME_LIMITATION` | 52 | 52 | "Synthesis-level conclusions are **provisional**. Standard thresholds…" | **RENAME — most explicit downgrade language** |

### 2.3 Term-level evidential status

`wa_term_inventory.evidential_status` — controlled vocabulary: `confirmed` · `plausible` · `uncertain` · `instrumental` · `relational_only`

| Value | Count |
|---|---:|
| NULL | 7,009 |
| confirmed | 106 |
| plausible | 44 |
| uncertain | 5 |

Sparsely populated (155 of 7,164 active terms). Vocabulary implies a graded confidence-in-inclusion judgement. This IS a coverage/significance marker by another name and needs redesign consideration alongside the flags.

### 2.4 Engine constants that drive coverage flag thresholds

From `engine/constants.py`:

- `HIGH_FREQ_THRESHOLD = 500` → `HIGH_FREQUENCY_ANCHOR`
- `THIN_DATA_THRESHOLD = 20` → `THIN_DATA`
- `SMALL_VERSE_SAMPLE_THRESHOLD = 5` → `SMALL_VERSE_SAMPLE`

### 2.5 Scope of impact

- 182 of 213 registries carry at least one of the coverage flags (85%)
- Total flag rows to review/rename: **16,214** across 4 flag codes (THIN_DATA, SMALL_VERSE_SAMPLE, HIGH_FREQUENCY_ANCHOR, PH2_VOLUME_LIMITATION)

---

## 3. Consumers — where these flags are used

### 3.1 Engine

- `engine/flag_engine.py` — canonical writer for all derivable DATA_COVERAGE flags (SMALL_VERSE_SAMPLE, THIN_DATA, HIGH_FREQUENCY_ANCHOR, NO_VERSES, NO_WORD_ANALYSIS, PROSE_ONLY_MEANING, SPAN_FILTER_APPLIED, SPAN_RESOLUTION_CONFLICT)
- `engine/audit.py` — WR-16 audit check verifies derivable flags match expected state
- `engine/audit_word.py` — reads SPAN_FILTER_APPLIED / SPAN_RESOLUTION_CONFLICT for classification logic

### 3.2 Pilot

- `scripts/readiness_sweep_pilot.py:243–254` — emits Path 1 SMALL_VERSE_SAMPLE inserts (mismatched semantics — OT-DBR-011)

### 3.3 Instructions

Grep needed to confirm, but likely:

- `wa-sessionb-analysis-readiness` — almost certainly checks for coverage flags as part of the 6-step audit
- `wa-dimensionreview-instruction` — may reference THIN_DATA / SMALL_VERSE_SAMPLE as caveats
- `wa-versecontext-instruction` — may mention volume thresholds
- `wa-reference` — controlled-vocabulary definitions

### 3.4 Extracts

- `scripts/build_complete_extract.py` — includes `statistics` and `quality_flags` sections
- `scripts/_exploratory_sessionb_export_v1_20260415.py` (archived) — exported flag data
- Session A extract (when built) — likely to surface coverage info

### 3.5 Exposure points where downgrading could happen

- Session B Stage 1 (Analysis Readiness) 6-step audit — may treat THIN_DATA as a hard gate or caveat
- Pool analysis dataset — if it filters by coverage flags
- Dimension Review — if it skips certain terms
- Session A / C prose — if narrative explicitly says "only N verses found, results limited"

---

## 4. Proposed redesign — informational, not prescriptive

### 4.1 Design principles

1. **Factual, not judgmental.** Flag names describe *data shape*, not *analytical worth*.
2. **No gating.** No instruction or script may short-circuit analytical processing on the basis of a coverage flag.
3. **Bidirectional note.** For every flag that flags *low* coverage, consider whether an *absence-of-expected-coverage* cue is also useful (e.g. a term the researcher listed as expected but that has no verses in context).
4. **Threshold transparency.** If a threshold is used, the threshold value should be in the flag's description, so the researcher can evaluate whether the threshold is appropriate.
5. **Flag catalogue reviewed holistically.** Not every flag-by-flag fix — look at the full family at once to avoid piecemeal inconsistency.

### 4.2 Proposed flag renames (semantic preservation; new names are neutral)

Researcher direction 2 (2026-04-20): reframe `NO_VERSES` from "nothing to look at" to **"minimal biblical evidence for the term"** — an open-investigation state, not a terminal one. Reflected below.

| Current | Proposed | Description (proposed) |
|---|---|---|
| `NO_VERSES` | `VERSE_EVIDENCE_MINIMAL` | Minimal biblical evidence exists for this term in the extraction. Does NOT mean the term is irrelevant — triggers four research questions (see §4.9 question IDs Q-COV-01..04). Investigation is open until answered. |
| `SMALL_VERSE_SAMPLE` | `VERSE_EVIDENCE_CONCENTRATED` | Term has fewer than {THIN_DATA_THRESHOLD} confirmed verse records. Informational — verse count does not indicate analytical value. Routed to research actions per §4.7. |
| `THIN_DATA` | *merge into above* | `SMALL_VERSE_SAMPLE` + `THIN_DATA` semantics overlap. Consolidate into a single `VERSE_EVIDENCE_CONCENTRATED` with the threshold in the description. |
| `HIGH_FREQUENCY_ANCHOR` | `VERSE_EVIDENCE_HIGH` | Term has ≥{HIGH_FREQ_THRESHOLD} occurrences. Verse records captured are a structured subset per STEP API pagination — not a defect; informational. |
| `PH2_VOLUME_LIMITATION` | `VERSE_EVIDENCE_BREADTH_NOTE` | Term's active verse count is a subset of total occurrences. Recorded for researcher awareness — does NOT gate synthesis. |

Naming scheme: all renamed flags use `VERSE_EVIDENCE_*` prefix (replacing both `VERSE_COVERAGE_*` from earlier draft and the legacy mixed prefixes) to establish a consistent family. The word "evidence" replaces "coverage" per researcher direction 2 — framing shift from "how much data did we capture" to "what biblical evidence exists for this term's inner-being relevance".

### 4.3 Flags retained as-is (already factual)

- `SPAN_FILTER_APPLIED` — diagnostic; kept
- `SPAN_RESOLUTION_CONFLICT` — diagnostic; kept
- `NO_WORD_ANALYSIS`, `PROSE_ONLY_MEANING` — structural (meaning-data shape, not verse evidence); kept

(Note: `NO_VERSES` moves from "retained" to "renamed" per researcher direction 2.)

### 4.4 Flags to deprecate

- `SMALL_VERSE_SAMPLE` + `THIN_DATA` deprecated in favour of `VERSE_COVERAGE_CONCENTRATED` (merged).

### 4.5 evidential_status column

Two options:

a) **Retire the column** — rarely populated (155 of 7,164 rows); the graded vocabulary implies judgement; replaced by factual flags.
b) **Retain but redefine** — drop `uncertain` / `plausible` wording; shift to factual descriptors like `direct_reference` / `inferential_reference` / `contextual_reference`. Requires researcher redefinition.

Recommend (a) — retire. Low population + judgment-implying vocabulary + not consumed by analytical code make this the cleaner move.

### 4.6 Threshold reconsideration

Current `SMALL_VERSE_SAMPLE_THRESHOLD = 5` and `THIN_DATA_THRESHOLD = 20` — these are values from the early volume-management era. Given the new principle, they become **annotation thresholds**, not gating thresholds. Their numeric values are less critical because nothing acts on them.

Recommend: keep the numeric thresholds unchanged, but document them as "awareness thresholds — trigger a `VERSE_EVIDENCE_CONCENTRATED` annotation below this count; no gating effect".

### 4.7 Research-action routing (researcher direction 3)

Each flag must declare one or more research-action routes. Proposed controlled vocabulary:

| Code | Route | When to apply |
|---|---|---|
| `R_STEP_EXHAUST_CHECK` | Was the STEP search fully exhausted for this term? Re-run discovery with broader criteria. | Low/minimal evidence found — could pagination / filter logic have missed verses? |
| `R_EXTERNAL_BIBLE` | Researcher-driven Bible research outside STEP (other translations, original-language lexica, concordances). | Where STEP was exhausted but researcher expected more. |
| `R_AI_WIDER_CONTEXT` | AI explores term usage in wider historical/cultural/linguistic context (e.g. modern science, ANE literature, LXX/Targums, early Christian writings). | For terms that appear modern / technical / not obviously biblical. |
| `R_RELEVANCE_REVIEW` | Re-evaluate whether the term is genuinely in scope for inner-being study. May result in registry deprecation, retention with rationale, or escalation to researcher decision. | When the other three routes return null — absence of evidence is the finding. |

**Storage:** new column `wa_quality_flag_types.research_actions TEXT` — semicolon-separated list of route codes (e.g. `"R_STEP_EXHAUST_CHECK;R_EXTERNAL_BIBLE;R_RELEVANCE_REVIEW"`). Migration M29 sets it per flag type.

**Flag → route proposed mapping:**

| Flag | Routes |
|---|---|
| `VERSE_EVIDENCE_MINIMAL` (formerly NO_VERSES) | All four: STEP_EXHAUST + EXTERNAL_BIBLE + AI_WIDER_CONTEXT + RELEVANCE_REVIEW |
| `VERSE_EVIDENCE_CONCENTRATED` (formerly SMALL_VERSE_SAMPLE + THIN_DATA) | STEP_EXHAUST + AI_WIDER_CONTEXT (re: why so few?) |
| `VERSE_EVIDENCE_HIGH` (formerly HIGH_FREQUENCY_ANCHOR) | AI_WIDER_CONTEXT (re: how to sample responsibly) |
| `VERSE_EVIDENCE_BREADTH_NOTE` (formerly PH2_VOLUME_LIMITATION) | STEP_EXHAUST + AI_WIDER_CONTEXT |
| `SPAN_FILTER_APPLIED` · `SPAN_RESOLUTION_CONFLICT` | (diagnostic, no research route — retain) |

### 4.8 Term introduction-source tracking (researcher direction 4)

**New concept — not currently in schema.** Registry-word sources are recorded (in `word_registry.source_reference` or similar), but **term-level introduction sources are not tracked**. This is the gap researcher direction 4 addresses.

The same English concept can surface multiple terms via several paths; each path has different analytical weight. Without tracking, we can't:
- Re-evaluate terms that entered via lower-confidence paths (e.g. STEP meaning-block text scrape)
- Identify candidates for promotion to standalone registries (the reverse of what has happened informally)
- Audit consistency of term-inclusion decisions
- Retrace why a term is present when we revisit a registry

**Proposed column on `wa_term_inventory`:**

| Column | Type | Purpose |
|---|---|---|
| `term_introduction_source` | TEXT | Controlled vocabulary (see below) |
| `term_introduction_rationale` | TEXT | Free-text explanation — why this term for this registry |
| `term_introduction_date` | TEXT | ISO-8601 UTC |

**Controlled vocabulary for `term_introduction_source`:**

| Code | Meaning |
|---|---|
| `step_keyword` | Surfaced by STEP's English keyword → Strong's search |
| `step_association` | STEP's "related terms" cluster for the primary Strong's |
| `step_meaning_block` | Extracted from STEP's meaning/definition prose |
| `step_subgloss` | From STEP's sub-gloss expansion |
| `researcher_external` | Researcher added from external Bible research |
| `ai_proposed` | AI-surfaced during analytical session, researcher-approved |
| `registry_elevation` | Originally a term under another registry; promoted to standalone registry — but this row represents the *opposite* direction: a registry-level word that later was re-introduced as a term under another registry for cross-reference |
| `legacy_unknown` | Term predates this provenance tracking — introduction source not recorded |

**Migration (M30 candidate, can parallel M29):**

1. Add the three columns to `wa_term_inventory` with NULL default
2. Backfill `legacy_unknown` for all existing ~7,164 active terms
3. Set `term_introduction_date = raised_date` where derivable; NULL otherwise
4. Researcher-driven reclassification sweep (post-migration) — walk through legacy_unknown terms to promote them to more specific codes where feasible

**Effect:** unlocks future analytical questions like "show all terms added via step_meaning_block with 0 active verses — are they still justified?" and "which step_keyword terms have been elevated to registry-level in other programmes — should the same happen here?"

### 4.9 Question catalogue integration (researcher direction 5)

Coverage flags become triggers for **catalogue questions**, not static annotations. This requires:

1. **New catalogue questions** in `wa_obs_question_catalogue` — one set per flag + research-action route pairing. Researcher-authored for wording; CC applies via PROSE/CATALOGUE patch type.
2. **New junction table** `wa_flag_type_question_link (flag_type_id, question_id, context_note)` — maps each flag code to the question IDs it routes to.
3. **Consuming code** updated: when a term's flag is raised, the extract / Session B prompt includes the linked catalogue questions as "open questions for this term" — answered via normal Q&A partitioning.

**Proposed starter questions for `VERSE_EVIDENCE_MINIMAL` (formerly NO_VERSES) per direction 2:**

| ID (proposed) | Question | Expected research action |
|---|---|---|
| Q-COV-01 | Is this term's meaning covered by another term with similar meaning in the inner-being scope? | Cross-registry lookup |
| Q-COV-02 | Is this term a modern concept / neologism with no substantive biblical antecedent? | AI wider-context exploration |
| Q-COV-03 | Does the absence of biblical evidence itself have analytical significance for the inner-being picture? | Researcher exegesis |
| Q-COV-04 | Is this term simply not relevant to inner-being study? If so, should the term be deprecated from this registry? | Relevance review → registry update |

**Starter questions for `VERSE_EVIDENCE_CONCENTRATED` (formerly THIN_DATA / SMALL_VERSE_SAMPLE):**

| ID (proposed) | Question | Expected route |
|---|---|---|
| Q-COV-05 | Was STEP's verse capture exhausted for this term? (Was any pagination / filter step incomplete?) | STEP exhaust check |
| Q-COV-06 | What do the few verses that exist establish about the term's inner-being contribution? | Close reading |
| Q-COV-07 | Does the narrow verse set concentrate in a particular literary genre / historical period / speaker? | Context analysis |

**Storage pattern:**

```sql
CREATE TABLE wa_flag_type_question_link (
  id INTEGER PRIMARY KEY,
  flag_type_id INTEGER NOT NULL REFERENCES wa_quality_flag_types(id),
  question_id INTEGER NOT NULL REFERENCES wa_obs_question_catalogue(id),
  context_note TEXT,
  active INTEGER NOT NULL DEFAULT 1,
  UNIQUE (flag_type_id, question_id)
);
```

**Effect:** Every flag raised now carries its investigation plan. Claude AI's Session B output includes the linked questions as mandatory Q&A items (already the pattern for wa_obs_question_catalogue per SC-03/SC-04). No change to Session B workflow — just more explicit question surfacing.

---

## 5. Migration and consumer update plan

This is a potential M29 migration (post OT-DBR-009 dedup, or parallel — they don't conflict).

### 5.1 Proposed migration M29 — coverage flag redesign

1. **Rename `wa_quality_flag_types`** rows per §4.2 — all use `VERSE_EVIDENCE_*` prefix: `NO_VERSES` → `VERSE_EVIDENCE_MINIMAL`; `SMALL_VERSE_SAMPLE` → `VERSE_EVIDENCE_CONCENTRATED`; `THIN_DATA` marked deprecated (link to new code via `deprecation_note`); `HIGH_FREQUENCY_ANCHOR` → `VERSE_EVIDENCE_HIGH`; `PH2_VOLUME_LIMITATION` → `VERSE_EVIDENCE_BREADTH_NOTE`.
2. **Update descriptions** per §4.2 — strip "thin/small/limited" language; replace with factual shape description + pointer to research actions.
3. **Add `research_actions` column** to `wa_quality_flag_types` (TEXT, semicolon-separated codes) — populate per §4.7 mapping.
4. **Merge THIN_DATA + SMALL_VERSE_SAMPLE rows**: for terms flagged with both, consolidate into single `VERSE_EVIDENCE_CONCENTRATED`. Migration policy: rename the SMALL_VERSE_SAMPLE row in place; delete the THIN_DATA row where the term also has SMALL_VERSE_SAMPLE; otherwise rename THIN_DATA → VERSE_EVIDENCE_CONCENTRATED.
5. **Re-run `flag_engine.py`** post-rename to verify new codes are written correctly.
6. **(Optional)** Drop `evidential_status` column if §4.5 option (a) approved.

### 5.2 Proposed migration M30 — term introduction-source tracking

1. Add three columns to `wa_term_inventory`: `term_introduction_source TEXT`, `term_introduction_rationale TEXT`, `term_introduction_date TEXT`.
2. Backfill `term_introduction_source = 'legacy_unknown'` for all ~7,164 active terms.
3. Researcher-driven reclassification sweep (post-migration) — walk through legacy_unknown terms to promote where feasible.
4. Add CHECK constraint on `term_introduction_source` (controlled vocabulary per §4.8).

### 5.3 Proposed migration M31 — flag-question linking

1. Create `wa_flag_type_question_link` table per §4.9 DDL.
2. Researcher authors Q-COV-01..07 (or equivalent) — added to `wa_obs_question_catalogue` via CATALOGUE patch.
3. Populate junction rows linking each new flag type to its catalogue questions per §4.9 mapping.

### 5.4 Dependency graph for M29/M30/M31

- M29 (coverage redesign) is standalone — can run independently
- M30 (provenance) is independent of M29 — can run in parallel or either order
- M31 (flag-question linking) depends on M29 (new flag codes exist) **and** on researcher authoring catalogue questions
- All three independent of OT-DBR-009 (mti_terms dedup)

Ordering suggestion: M29 + M30 in parallel (single migration session); M31 after researcher authors the catalogue questions (separate session).

### 5.5 Consumer updates

| Consumer | Change |
|---|---|
| `engine/flag_engine.py` | Update flag codes to new names; merge SMALL_VERSE_SAMPLE + THIN_DATA logic into VERSE_EVIDENCE_CONCENTRATED writer |
| `engine/audit.py` WR-16 | Update expected-flag set |
| `engine/audit_word.py` | Update SPAN_FILTER_APPLIED handling (no change expected — that flag unaffected); populate `term_introduction_source` when adding new terms (post M30) |
| `scripts/readiness_sweep_pilot.py` R.B | Rewrite the ratio-based Path 1 emitter per OT-DBR-011; remove gating logic if any |
| Instruction docs | Sweep for "thin", "small", "limited" language in analytical framing; rephrase to neutral evidence language |
| `wa-reference` | Update flag catalogue definitions |
| `wa-global-flags` | Update any tracked flags |
| `wa-global-general-rules` | Add GR-EVIDENCE-001/002/003 (§1.1) |

### 5.6 Data migration policy — decision needed

For existing flag rows: do we **rename in place** (preserving flag_id + metadata) or **re-derive** (drop old, write new)? Rename in place is safer and faster; re-derive gives a clean slate but loses audit history.

Recommend rename in place.

---

## 6. Interaction with the five open OT items

| OT item | Interaction |
|---|---|
| OT-DBR-009 (mti_terms dedup) | Independent. Can proceed in parallel. |
| OT-DBR-011 (SMALL_VERSE_SAMPLE classifier) | **Absorbed into this redesign.** Close OT-DBR-011 on redesign approval. |
| OT-DBR-012 (dominant_subject='NONE') | Independent. Path 2 directive approach still applies. |
| OT-DBR-013 (pilot Path 1 audit) | **Expanded scope.** Full pilot audit should also check for "gating" logic tied to coverage flags. |
| OT-DBR-005/007/008 (LOW) | Unaffected. |

---

## 7. Decisions — status after 2026-04-20 PM researcher direction

### 7.1 Resolved by direction

| # | Question | Resolution |
|---|---|---|
| 1 | Approve the principle in §1 as programme-wide rule? | **APPROVED** — going to `wa-global-general-rules` as GR-EVIDENCE-001/002/003 (§1.1) at next version bump (v2.12). |
| 2 | Confirm rename scheme §4.2? | **EXPANDED** — added NO_VERSES rename; shifted prefix from `VERSE_COVERAGE_*` to `VERSE_EVIDENCE_*` per researcher direction 2 (framing: "what biblical evidence exists" not "how much was captured"). |
| 6 | "Absence of expected evidence" warrant own flag? | **SUBSUMED** — now the core reframe of `NO_VERSES` → `VERSE_EVIDENCE_MINIMAL`, bundled with catalogue questions Q-COV-01..04 per direction 2 + 5. No separate flag needed. |

### 7.2 New scope added by direction (new open items)

| # | Question | Source direction |
|---|---|---|
| N1 | Controlled vocabulary for `term_introduction_source` in §4.8 — do the 8 proposed codes cover the real paths, or are there more to add? | Direction 4 |
| N2 | Do we want `term_introduction_rationale` to be free-text or itself a controlled vocabulary (e.g. "matches root family", "co-occurs in >5 passages with primary anchor", etc.)? | Direction 4 |
| N3 | Research-action route vocabulary in §4.7 — are the four proposed codes the right set, or additional routes needed? | Direction 3 |
| N4 | Researcher authoring of Q-COV-01..07 (or revised) for `wa_obs_question_catalogue` — when / how? The catalogue patch type needs these before M31 can link. | Direction 5 |
| N5 | Scope of legacy backfill for `term_introduction_source` — is `legacy_unknown` acceptable for all 7,164 terms, or should CC attempt heuristic classification during backfill? | Direction 4 |
| N6 | Retroactive routing — for the 16,214 existing flag rows, do we enforce the new research-action + catalogue-question workflow retroactively, or only for new flag insertions post-M29? | Direction 3 + 5 |

### 7.3 Still open from v1 draft

| # | Question | Status |
|---|---|---|
| 3 | Keep or retire `evidential_status` column per §4.5? | OPEN |
| 4 | Merge policy for SMALL_VERSE_SAMPLE + THIN_DATA per §5.1 item 4 — what happens to rows with both? | OPEN (recommend consolidate into VERSE_EVIDENCE_CONCENTRATED) |
| 5 | When to execute — M29+M30+M31 parallel with OT-DBR-009, or sequentially after? | OPEN |

---

## 8. Recommended next move

**Action Q remains PAUSED.** OT-DBR-011/012 are subsumed into M29 redesign.

Sequencing suggestion:

1. Researcher resolves §7.2 and §7.3 open items (can be done async — no blocking dependency)
2. CC drafts formal Change Plan for M29 + M30 + M31 (new document) — reviewable before execution
3. Researcher authors Q-COV-01..07 (or revised set) — can happen in parallel with step 2
4. Execute M29 + M30 as one migration session (dry-run first); M31 after catalogue questions land
5. Re-run programme scan after migration → scorecard v3

**In the meantime — proceed to Action S** (Session A extract generator — M4 unblocker). S is completely independent of the evidence-flag redesign and unblocks the BANKED 5 from sitting idle.

---

*Draft v1.1 — 2026-04-20 PM. Researcher directions 1–5 absorbed. Awaiting decisions on §7.2 + §7.3.*

---

## 12. Decisions absorbed — 2026-04-20 evening (v1.2)

M29/M30/M31 dry-ran cleanly on DB copy (schema 3.10.0 → 3.11.0). Before live-applying, researcher reviewed the proposed defaults on open items. This section records the resulting decisions.

### 12.1 Q3 — `evidential_status` column fate

**DECISION: KEEP** the column.

**Repurposed semantic**: `evidential_status` will track the **need for further research** and the **outcome of that research** against a term. This integrates with the new `research_actions` routes on flag types (§4.7) and the Q-COV catalogue questions (§4.9).

**Proposed new vocabulary** (researcher authors final wording; CC proposal below for review):

| Code | Meaning |
|---|---|
| `pending_further_research` | Flag has triggered a research route; investigation queued but not yet performed |
| `research_in_progress` | Investigation active |
| `research_confirmed_inner_being` | Research complete — term IS in scope for inner-being study |
| `research_excluded_not_applicable` | Research complete — term is not in scope; registry-level action may follow |
| `research_alternative_term_found` | Research complete — another term better covers this meaning |
| `research_no_biblical_substance` | Research complete — modern concept; no biblical antecedent |
| `research_extends_study` | Research complete — new analytical paths opened; recorded for follow-on |
| `research_not_required` | No flag → no research need (default; equivalent to NULL) |

Existing 155 populated rows with old vocabulary (`confirmed`/`plausible`/`uncertain`/`instrumental`/`relational_only`) — need policy decision: **drop into `research_not_required`** (treat as no-op legacy) OR **map individually** to new vocabulary. 155 rows is small enough that researcher can review the mapping manually.

**OPEN QUESTION Q-12-1 (researcher):**

Should this new vocabulary be added to the programme controlled-vocabulary reference (`data/imports/WA/Workflow/Framework_B/Session_B/wa-reference [current]`)?

CC recommendation: **yes**. `wa-reference` already hosts controlled vocabularies (per CLAUDE.md §10); the 8 new codes belong alongside the existing sets. A small PROSE/patch adds them.

### 12.2 Q4 — row merge policy

**DECISION: Option 1 approved** — merge + delete overlap (already implemented in M29 dry-run). 2,831 overlap rows hard-deleted; 2,087 remaining THIN_DATA rows repointed to the merged flag_id. `(file_id, term_id)` is the FK tuple that identifies "same term-in-file"; overlap rows carried the same underlying semantic split across two codes, so collapse is correct. No information loss beyond the legacy code distinction (intentional).

### 12.3 N4 — Q-COV catalogue questions

**DECISION: approved original 7 + 5 new questions authored.**

Final set of **12 Q-COV catalogue questions** to be inserted into `wa_obs_question_catalogue` via a CATALOGUE patch:

#### For `VERSE_EVIDENCE_MINIMAL` (4 questions — approved as drafted)

| Code | Question |
|---|---|
| Q-COV-01 | Is this term's meaning covered by another term with similar meaning in the inner-being scope? |
| Q-COV-02 | Is this term a modern concept / neologism with no substantive biblical antecedent? |
| Q-COV-03 | Does the absence of biblical evidence itself have analytical significance for the inner-being picture? |
| Q-COV-04 | Is this term simply not relevant to inner-being study? If so, should the term be deprecated from this registry? |

#### For `VERSE_EVIDENCE_CONCENTRATED` (3 questions — approved as drafted)

| Code | Question |
|---|---|
| Q-COV-05 | Was STEP's verse capture exhausted for this term? (Was any pagination / filter step incomplete?) |
| Q-COV-06 | What do the few verses that exist establish about the term's inner-being contribution? |
| Q-COV-07 | Does the narrow verse set concentrate in a particular literary genre / historical period / speaker? |

#### For `VERSE_EVIDENCE_HIGH` (3 questions — researcher-authored 2026-04-20)

| Code | Question |
|---|---|
| Q-COV-08 | `VERSE_EVIDENCE_HIGH` indicates that many verses in the Bible carry the same evidential value. Does the surrounding context of the verse provide any further differential value? |
| Q-COV-09 | Does the high frequency repeat itself in both Old and New Testament? Is there any analytic value in this finding? |
| Q-COV-10 | Does the high frequency correlate to the term's importance for understanding the inner being? |

#### For `VERSE_EVIDENCE_BREADTH_NOTE` (2 questions — researcher-authored 2026-04-20)

| Code | Question |
|---|---|
| Q-COV-11 | The term's usage in the verse has multiple analytic coverages — does the context around the verse impact the meaning so as to let us understand the different nuances better? |
| Q-COV-12 | Has the breadth been captured in the inter-relationships and correlations with other terms and words? |

#### Junction-table wiring

Per the researcher's principle, the flag-to-question links are **explicit and assessment-specific**:

| Flag code | Linked Q-COV codes |
|---|---|
| `VERSE_EVIDENCE_MINIMAL` | Q-COV-01, Q-COV-02, Q-COV-03, Q-COV-04 |
| `VERSE_EVIDENCE_CONCENTRATED` | Q-COV-05, Q-COV-06, Q-COV-07 |
| `VERSE_EVIDENCE_HIGH` | Q-COV-08, Q-COV-09, Q-COV-10 |
| `VERSE_EVIDENCE_BREADTH_NOTE` | Q-COV-11, Q-COV-12 |

M31 created the `wa_flag_type_question_link` junction. Population of these 12 mappings happens via a CATALOGUE patch once the Q-COV questions are inserted into `wa_obs_question_catalogue`.

### 12.4 N6 — routing methodology (revised from "prospective vs retroactive")

**Researcher's methodology (2026-04-20):** The concept isn't "open question state per term stored in DB". Instead:

> The intent is to drive the analytic process through the questions. If the prose reaches AI and the questions are not present, then it is likely to not be considered. So the linking of questions to the flag values must be **explicit in the prose**. Only questions with answers should reside in the database.

**What this means structurally:**

- `wa_obs_question_catalogue` — catalogue of questions (reference)
- `wa_flag_type_question_link` — maps flag types to catalogue questions (reference)
- **No "open question per term" table** — there is no materialised queue of open questions in the DB
- **Prose output is the carrier** — when Session A (or B input) extract is generated, the generator looks up the flag's linked questions via the junction and **renders them inline** alongside the flag mention. AI reads them as explicit tasks.
- **Answers land as findings** — when Session B produces an answer to a linked question, that answer is stored in `wa_session_b_findings` with `wa_finding_catalogue_links` tying the finding to the specific catalogue question.

**Effect on existing rows:** no retroactive action required. Existing flag rows are simply data. The next time a registry's prose is generated, linked questions appear. No 5,800-row backlog flood.

**Effect on Session A generator (`generate_session_a_extract.py`):** needs enhancement — when it renders a flag in Section 3 Terms, it should also inline the linked catalogue questions below the flag. Enhancement scope is small — lookup via the junction, render as a bullet list.

**Effect on Session B pool dataset assembly:** same pattern — when pool dataset mentions a flag, embed the linked questions as tasks for the analyst.

### 12.5 M30 — legacy_unknown pivot

**DECISION: approved — revise M30 to columns-only; blanket backfill removed.**

- M30 revised: adds the three columns, no backfill
- Classifier heuristic added per researcher: "**Term with specific pattern in meaning**" → new code `derived_from_meaning`
- Updated controlled vocabulary (9 codes) in §4.8:

| Code | Meaning |
|---|---|
| `step_keyword` | Surfaced by STEP's English keyword → Strong's search |
| `step_association` | STEP's "related terms" cluster for the primary Strong's |
| `step_meaning_block` | Extracted from STEP's meaning/definition prose |
| `step_subgloss` | From STEP's sub-gloss expansion |
| `derived_from_meaning` | **NEW 2026-04-20** — Term identified from pattern analysis of existing term's `meaning` field |
| `researcher_external` | Researcher added from external Bible research |
| `ai_proposed` | AI-surfaced during analytical session, researcher-approved |
| `registry_elevation` | A term under another registry was promoted to standalone registry status; this row represents the reverse-import as a term back under another registry |
| `legacy_unknown` | Introduction source not recoverable from available signals — last-resort fallback |

### 12.6 M30 classifier — build specification

Classifier script to produce: `scripts/classify_term_introduction_source.py`

**Approach**:
1. Walk every active `wa_term_inventory` row
2. Apply heuristics in priority order:
   - OWNER term whose strongs matches `word_registry.strongs_list` primary anchor → `step_keyword`
   - OWNER term whose strongs appears in the STEP-related-terms tree for the primary → `step_association`
   - Term whose `meaning` field content matches a pattern (e.g., references to another registry's anchor term) → `derived_from_meaning`
   - Term with `source=bulk_patch` on phase2 flags → requires additional signal to distinguish `researcher_external` vs `ai_proposed`
   - XREF term → inherit the OWNER's classification
   - Otherwise → `legacy_unknown`
3. Emit a markdown report: `outputs/term-introduction-classification-proposals-20260420.md`
4. Report is read-only; researcher reviews + optionally amends
5. Once reviewed, a second script (or patch) applies the classifications to the DB

**First run scope**: OWNER terms only (~5,518 terms). XREFs in a second pass after OWNER classification is stable.

### 12.7 Open items requiring researcher input

| # | Item | What CC needs |
|---|---|---|
| Q-12-1 | Add 8 new `evidential_status` codes to `wa-reference [current]`? | Yes/no + wording review |
| Q-12-2 | Map legacy 155 `evidential_status` rows to new vocabulary? | Policy: bulk-map to `research_not_required`, OR review individually |
| Q-12-3 | Approve 8 new `term_introduction_source` codes + classifier heuristic order | Vocabulary review + any heuristic tweaks |
| Q-12-4 | CATALOGUE patch for Q-COV-01..12 — format + timing | Confirm CC should author the patch now or wait |
| Q-12-5 | Enhancement to `generate_session_a_extract.py` to inline linked questions beneath flag mentions | Approve scope + priority |

---

*v1.2 — 2026-04-20 evening. Decisions absorbed, 5 open items queued for next researcher turn.*

---

## 13. Execution plan — v1.3 (researcher decisions on §12.7 absorbed 2026-04-20 evening)

All 5 open items (Q-12-1..Q-12-5) approved. Execution sequence below. Each step produces an explicit outcome captured here (§14 execution record).

### 13.1 Sequenced steps

| Step | Description | Output / artefact |
|---|---|---|
| 1 | Apply M29 to live with per-migration backup | backup + flag rename + merge + research_actions |
| 2 | Apply M30 to live with per-migration backup | backup + 3 new columns (NULL-populated) |
| 3 | Apply M31 to live with per-migration backup | backup + junction table + schema → 3.11.0 |
| 4 | Regenerate schema JSON (export_database_schema.py) | `data/schema/database-schema-v3.11.0-20260420.json` |
| 5 | Update CLAUDE.md §3 + §17 for renamed flags + new columns | CLAUDE.md updated |
| 6 | Map 155 legacy `evidential_status` rows: `confirmed` → `research_not_required`; else → `pending_further_research` with legacy note | UPDATE + audit captured here |
| 7 | Author CATALOGUE patch: insert Q-COV-01..12 into `wa_obs_question_catalogue` | `data/imports/WA/Patches/wa-catalogue-q-cov-20260420.json` |
| 8 | Apply CATALOGUE patch | 12 new catalogue rows |
| 9 | Author junction patch: insert 12 `wa_flag_type_question_link` rows mapping flag types to questions per §12.3 | `data/imports/WA/Patches/wa-flag-question-link-20260420.json` |
| 10 | Apply junction patch | 12 junction rows active |
| 11 | Build `scripts/classify_term_introduction_source.py` (OWNER-first pass, report-only) | classifier script + `outputs/term-introduction-classification-proposals-20260420.md` |
| 12 | Enhance `scripts/generate_session_a_extract.py` to inline flag-linked questions below flag mentions (Section 3) | enhanced generator |
| 13 | Re-generate 5 BANKED Session A extracts | 5 refreshed `.md` files |
| 14 | Update `wa-reference [current]` with new vocabularies (evidential_status 8 codes + term_introduction_source 9 codes + Q-COV question codes reference) | reference file updated |

### 13.2 Q-12-2 legacy evidential_status mapping rule (researcher-approved)

Per 2026-04-20 evening direction: *"research not required — only assign this if the item clearly does not need any further enquiry. Else researcher review o/s."*

Applied mapping:

| Old value | Count | New value | Rationale field |
|---|---:|---|---|
| `confirmed` | TBD | `research_not_required` | "Legacy status `confirmed` → clear, no further enquiry" |
| `plausible` | TBD | `pending_further_research` | "Legacy status `plausible` — researcher review outstanding (M29 2026-04-20)" |
| `uncertain` | TBD | `pending_further_research` | "Legacy status `uncertain` — researcher review outstanding (M29 2026-04-20)" |
| `instrumental` | TBD | `pending_further_research` | "Legacy status `instrumental` — researcher review outstanding (M29 2026-04-20)" |
| `relational_only` | TBD | `pending_further_research` | "Legacy status `relational_only` — researcher review outstanding (M29 2026-04-20)" |

Counts to be filled in §14 step 6 execution record.

### 13.3 Stop-the-line checkpoints

Between steps 3 (M31 live) and step 4 (regen schema): verify schema version = 3.11.0 and all expected rows present.

Between step 10 (junction apply) and step 12 (generator enhancement): verify `wa_flag_type_question_link` has 12 active rows with correct flag-question mapping.

After step 13 (regenerate extracts): visual spot-check on r62 fellowship — the Session A Section 3 Terms should now show linked Q-COV questions underneath flag mentions.

---

## 14. Execution record — 2026-04-20 evening

All 14 steps completed in a single session. Live DB moved from schema 3.10.0 → 3.11.0. Outcomes:

| Step | Outcome |
|---|---|
| 1 (M29 live) | PASS — backup `bible_research_pre_M29_20260420_101542.db`; 2,831 overlap rows de-duped; 2,087 THIN_DATA repointed; 4 flag codes renamed; THIN_DATA id=2 deprecated; research_actions populated for 4 types; 52 research-flag rows renamed |
| 2 (M30 live) | PASS — backup pre-M30; 3 columns added to `wa_term_inventory`; no backfill (per revised policy) |
| 3 (M31 live) | PASS — backup pre-M31; `wa_flag_type_question_link` + 2 indexes created; schema → 3.11.0 |
| 4 (schema JSON) | PASS — `data/schema/database-schema-v3.11.0-20260420.json` generated |
| 5 (CLAUDE.md) | PASS — header timestamp, §3 schema + Table Group 18, §4 EXPECTED_SCHEMA_VERSION + thresholds, §10 programme state, §17 flag vocabulary all updated |
| 6 (legacy evidential_status) | PASS — backup pre-remap; 106 `confirmed` → `research_not_required`; 49 `plausible`/`uncertain` → `pending_further_research`; rationale captured in `retention_note` |
| 7-8 (CATALOGUE patch) | PASS — `wa-catalogue-q-cov-20260420.json` authored + applied; 12 Q-COV rows inserted (obs_id 195–206) |
| 9-10 (junction) | PASS — backup pre-junction; 12 `wa_flag_type_question_link` rows active covering 4 flag types |
| 11 (classifier) | PASS — `scripts/classify_term_introduction_source.py` built; first run on 212 registries/3,706 OWNER terms. Distribution: step_association=3,378 (91.2%), legacy_unknown=260 (7.0%), step_keyword=67 (1.8%), derived_from_meaning=1. Report: `outputs/term-introduction-classification-proposals-20260420.md` — researcher review recommended for the 260 legacy_unknown cases |
| 12 (generator enhancement) | PASS — `generate_session_a_extract.py` now queries `research_actions` + inlines linked Q-COV questions beneath evidence-flag mentions in Section 3 |
| 13 (regenerate BANKED) | PASS — all 5 BANKED extracts refreshed; word counts +7–9% vs prior (room for questions). r206 vulnerability spot-check confirms Q-COV-05..07 inline under VERSE_EVIDENCE_CONCENTRATED for G1128 |
| 14 (wa-reference v5.7) | PASS — `wa-reference-v5_7-20260420.md` created; §8 rewritten (evidence family + deprecated codes), §8a new (research-action routes), §8b new (Q-COV catalogue reference), §9.4 new (term_introduction_source vocabulary), §10 reframed (research need/outcome tracker + legacy mapping record) |

### 14.1 Artefacts produced this session

- Migration backups: `pre_M29`, `pre_M30`, `pre_M31`, `pre_catalogue_qcov`, `pre_flag_question_junction`, `pre_evidential_remap`
- `engine/migrate.py` — M29/M30/M31 added; constants bumped to 3.11.0
- `engine/constants.py` — EXPECTED_SCHEMA_VERSION = "3.11.0"
- Patch: `data/imports/WA/Patches/wa-catalogue-q-cov-20260420.json` (auto-archived post-apply)
- Script: `scripts/classify_term_introduction_source.py` (1 new, read-only)
- Script: `scripts/generate_session_a_extract.py` (enhanced)
- Report: `outputs/term-introduction-classification-proposals-20260420.md` (212 registries, 3,706 terms)
- Reference: `data/imports/WA/Workflow/Framework_B/Session_B/wa-reference-v5_7-20260420.md` (supersedes v5_6)
- 5 refreshed Session A extracts in `outputs/session_a/`
- Schema JSON: `data/schema/database-schema-v3.11.0-20260420.json`
- CLAUDE.md updated

### 14.2 Outstanding follow-ons (second pass)

- Researcher review of 260 `legacy_unknown` classifier cases in the proposals report
- Researcher confirmation / tweaking of the 8-code `evidential_status` vocabulary (added to §10 but not yet rules-ratified)
- Programme-level rules: add `GR-EVIDENCE-001/002/003` to `wa-global-general-rules` (v2.12 bump) per §1.1
- OT-DBR-012 (dominant_subject='NONE') — now has a home in the workflow: when a group hits NONE, link Q-COV-03-equivalent questions in Session A? Or handle via DimReview (Action U) as already queued
- Classifier second pass: XREFs inherit OWNER classifications (not run yet)
- Apply researcher-reviewed `term_introduction_source` values to DB (post-review)

### 14.3 Q closed

Action Q of programme control v1 — coverage-flag redesign — **CLOSED** 2026-04-20 evening. OT-DBR-011 absorbed and resolved as part of this work. Schema 3.11.0 stable on live.

---

*v1.3 — 2026-04-20 evening, post-execution. All 14 steps closed; Q fully closed; outstanding follow-ons logged for second pass.*

