# Phase 1 Pilot Results + Capture-Table Architecture

**Document version:** v1
**Date:** 2026-04-27
**Author:** Claude Code, under researcher direction
**Linked predecessors:**
- [vc-corrective-strategy-v2-20260426.md](vc-corrective-strategy-v2-20260426.md)
- [db-capture-architecture-comparison-v1-20260427.md](db-capture-architecture-comparison-v1-20260427.md) — researcher approved Approach (a)
- `wa-obslog-ro-067-goodness-anlys-v2-20260426.md` — pilot input
**Pilot script:** [scripts/_pilot_parse_obslog_to_db_v1_20260427.py](../../scripts/_pilot_parse_obslog_to_db_v1_20260427.py)
**Pilot output:** [outputs/reports/words/wa-067-goodness-obslog-parse-manifest-v1-20260427.json](../reports/words/wa-067-goodness-obslog-parse-manifest-v1-20260427.json)
**Status:** Working analysis — informs Phase 2 design decisions

---

## Part 1 — Phase 1 Pilot Results

### 1.1 What the parser does

Reads a Session B obslog `.md` and extracts 8 categories of analytical content into a structured manifest. No DB writes (Phase 2 will be the writer). Validators check declared-vs-parsed counts; comparison mode regression-tests against applied patches.

### 1.2 Pilot run on reg 067 obslog v2

| Category | Parsed | Source location in obslog | Validation |
|---|---:|---|---|
| Q&A findings | **147** | `## Stage 2b Q&A Log — Section X` blocks | matches declared 147 ✓ |
| SD pointers | **10** | `## Complete SD Pointer Register` table + per-pointer detail blocks | matches declared 10 ✓ |
| Observations | **49** | `## Complete Observations Register` table | declared "OBS-001..049"; matches |
| Stage 2c chapters | **6** (48 KB body) | `## Stage 2c — Chapter N` blocks | all 6 captured |
| GAP questions | **8** | `[GAP-SX-NNN — PROPOSED ADDITION]` markers | matches AI's count |
| Word-specific questions | **6** | `[WORD-SPECIFIC-NNN — RNNN]` markers | matches AI's count |
| Review notes | **41** | inline `[QUESTION REVIEW NOTE: ...]` (23) + section summaries (18) | both kinds captured |
| Issues | **6** | `## Issues and Gaps Register` table | matches |
| Status update | `Analysis Complete` | `### Category F — Registry Status Update` block | extracted |

Parser ran clean on first format-aware pass (one fix needed: Section 3+ Q&A entries omit inline `Section:` field; parser uses surrounding H2 header as fallback). One stub marker on line 1493 caught and surfaced as warning rather than silently mis-parsed.

### 1.3 The coverage gap — what surfaced when we compared parser output to applied patches

The three goodness patches applied yesterday captured a small subset of what the obslog contains:

| Content | In obslog | Captured in 3 patches | Lost |
|---|---:|---:|---|
| ANSWERED + PARTIALLY ANSWERED Q&A | **141** | 22 | **119 (84%)** |
| Stage 2c chapters (~48 KB narrative) | **6** | 0 | **6 (100%)** |
| Observations | 49 | 0 | 49 (100%) |
| GAP questions (new catalogue entries) | 8 | 0 | 8 (100%) |
| Word-specific questions | 6 | 0 | 6 (100%) |
| Review notes | 41 | 0 | 41 (100%) |
| SD pointers | 10 | 10 | **0 ✓** |
| Status update | 1 | 1 | **0 ✓** |

**This validates risk #3 ("CC miss the capturing of important analytic observations") — except the loss happened under Approach (b).** Under Approach (b) only the well-defined, structured patch types (SD pointers, status) made it through cleanly. Everything narrative, free-form, or instruction-gap-blocked was lost.

The parser captures all 8 categories without instruction-gap dependencies. Phase 2's job is to write each category to the right table.

---

## Part 2 — Capture Tables Map

### 2.1 Where each obslog category goes

Mapping each parsed category to its target DB table(s). Schema sources confirmed by direct PRAGMA query 2026-04-27.

| # | Obslog category | Target table | Operation | Volume per word (reg 067 example) |
|---|---|---|---|---|
| 1 | Q&A findings | `wa_session_b_findings` (1 row per ANSWERED/PARTIAL Q&A) + `wa_finding_catalogue_links` (1 row per finding-question pair) + `wa_finding_entity_links` (1 row per finding-term/verse link) | INSERT | ~141 findings + ~141 catalogue links + ~300+ entity links |
| 2 | SD pointers | `wa_session_research_flags` (flag_code='SD_POINTER') | INSERT | 10 |
| 3 | Stage 2c chapters | `prose_section` (1 row per chapter, linked via `section_type_id` to `prose_section_type` codes `sb_s2c_ch1`..`sb_s2c_ch5`) | INSERT | 5 (Chapter 6 = SD pointer compendium, already in #2) |
| 4 | Observations | Currently no DB home — see §6.2 decision | TBD | 49 |
| 5 | GAP questions | `wa_obs_question_catalogue` (new universal-scope rows) | INSERT | 8 |
| 6 | Word-specific questions | `wa_obs_question_catalogue` (with `source_registry_no` = current registry) | INSERT | 6 |
| 7 | Review notes | Currently no DB home — see §6.2 decision | TBD | 41 |
| 8 | Status update | `word_registry.session_b_status` | UPDATE | 1 |

### 2.2 Surprise: prose_section_type already has the codes

A query against `prose_section_type` shows codes `sb_s2c_ch1` through `sb_s2c_ch5` already exist (rows 7-11). The instruction-gap CAT-C-001 noted in the obslog v2 was based on a DB-state-unknown moment; the codes are in place. Chapter 6 (Open Items / SD Pointers) doesn't need a `prose_section` row because its content IS the SD pointer table — already captured in `wa_session_research_flags`.

This means Phase 2 chapter writes are unblocked.

### 2.3 The two empty link tables — a quiet finding

`wa_finding_catalogue_links` (0 rows) and `wa_finding_entity_links` (0 rows) are the canonical link tables, schemed but never populated. Today's 195 active findings have NO catalogue links and NO entity links — they're orphaned in the sense that you can't query "all findings that answer Q042" or "all findings that cite Mic 6:8". Phase 2's writer should populate both link tables for the new findings; the historical 195 are a separate backfill question.

---

## Part 3 — Table Purpose: What Each Table Is FOR

This is the core of the researcher's question. Each table answers a different downstream question.

### 3.1 Findings + their links

| Table | Question it answers | Primary downstream consumer |
|---|---|---|
| `wa_session_b_findings` | "What did Session B conclude about word X?" | Session C (word study); future researcher recall |
| `wa_finding_catalogue_links` | "What catalogue questions does finding F answer?" / "How well-covered is question Q across the programme?" | Catalogue evolution; Stage 2b coverage reports |
| `wa_finding_entity_links` | "What terms/verses/groups does finding F cite?" / "What findings touch verse V?" | Verse-level reference work; cross-registry verse synthesis |

The two link tables are the bridge between findings (what was concluded) and (a) the question framework that drove them, (b) the data that grounded them. Without these populated, findings sit as text blobs you can search but not navigate structurally.

### 3.2 Research flags

`wa_session_research_flags` is the polymorphic flag table — one shape, many `flag_code` values:

| flag_code | Question it answers | Volume now |
|---|---|---:|
| `SD_POINTER` | "What cross-registry questions did Session B raise?" | 259 |
| `SB_FINDING` | "What Session-B-stage findings exist as flags (rather than findings table)?" | 35 |
| `PH2_*` family | "What data-quality/boundary/cross-ref issues need attention?" | ~25 |
| `VERSE_EVIDENCE_*` | "What verse-volume signals are flagged informationally?" | 52 |
| `DIMREVIEW_SESSION_D` | "What dimension-review items need Session D follow-up?" | 8 |

Note the dual residence: SB findings exist in BOTH `wa_session_b_findings` and as `SB_FINDING` flags here. This is intentional — flags are lightweight pointers that route to specific sessions; findings are the full analytical records. Phase 2's writer should pick the right table per finding type (the existing instruction has guidance, but it's been inconsistently applied — note that the 22 patched findings yesterday went to flags, not findings — that was Approach (b) cutting corners).

### 3.3 Catalogue + flag-question link

| Table | Question it answers | Primary downstream consumer |
|---|---|---|
| `wa_obs_question_catalogue` | "What questions drive Stage 2b for any/this word?" | Stage 2b drivers; readiness `.md` Section L |
| `wa_flag_type_question_link` | "When a specific flag type fires, which questions become applicable?" | Conditional Stage 2b for words with specific flags (Evidence-Flag Research Questions are routed this way) |

The catalogue is generative — Stage 2b output (GAP/WS questions, review notes) feeds back into the catalogue, growing or refining it. The catalogue is a living artefact of programme methodology.

### 3.4 Dimension index

| Table | Question it answers | Primary downstream consumer |
|---|---|---|
| `wa_dimension_index` | "What dimension does each verse-context group express, with what confidence?" | Session D cluster synthesis; dimension-review work |
| `wa_session_b_dimensions` | "What is the registry-level dimension review record?" | Registry-level dimension audit |

`wa_dimension_index` is per-group; `wa_session_b_dimensions` is per-registry (a higher-level summary). Population is sparse (only 2 rows in `wa_session_b_dimensions`) — programme has been operating on the per-group view primarily.

### 3.5 Verse Context (already populated)

| Table | Question it answers |
|---|---|
| `verse_context` | "How is each verse classified for each term it occurs in?" (relevant / set-aside / anchor) |
| `verse_context_group` | "What characteristic-perspective groups did this term's classification produce?" |

These predate the obslog work. Phase 2 doesn't write to them — but the obslog references them constantly (anchor verses, group codes). Phase 2 reads them to validate that finding-entity links resolve.

### 3.6 Prose

| Table | Question it answers |
|---|---|
| `prose_section` | "What programme-level / session-level prose has been written for this registry / cluster / programme?" |
| `prose_section_type` | "What prose section types exist?" (handles the codes) |

`prose_section` carries Session A per-term renders, Session B Stage 2c chapters, Session C word studies, Session D cluster synthesis, plus programme-level governance prose. It's versioned (`supersedes_id` / `superseded_by_id`). For Stage 2c chapters specifically — codes 7-11 (`sb_s2c_ch1`..`sb_s2c_ch5`) are the targets.

### 3.7 Session D tables

| Table | Question it answers | Volume now |
|---|---|---:|
| `session_d_runs` | "What cross-registry synthesis runs have happened?" | 0 |
| `session_d_observations` | "What structural observations did a synthesis run produce?" | 0 |
| `session_d_term_links` / `session_d_verse_links` | "What terms/verses link across registries within a synthesis run?" | 0 |

All empty — Session D hasn't run yet. The 259 SD pointers from Session B work are queued waiting for synthesis. Once Session D runs, it reads SD pointers + findings + dimension index, and writes results to these tables.

---

## Part 4 — Inter-Relationships (the FK graph)

```
                                ┌─────────────────────────┐
                                │     word_registry       │
                                │  (the ~214 word anchor) │
                                └────────┬────────────────┘
                                         │
        ┌────────────────┬───────────────┼────────────────┬───────────────┐
        ▼                ▼               ▼                ▼               ▼
  wa_session_           wa_session_  wa_session_       prose_section     verse_context
  research_flags        b_findings   b_dimensions                            +group
  (polymorphic)         (per-Q&A)    (per-reg dim)     (narrative)       (~41k vc rows)
        │                  │                                │
        │                  │                                │
        │                  ├──── wa_finding_                ├──── prose_section_type
        │                  │     catalogue_links            │      (76 codes incl.
        │                  │     (currently empty!)         │       sb_s2c_ch1..5)
        │                  │            │
        │                  │            ▼
        │                  │     wa_obs_question_
        │                  │     catalogue (206 Qs)
        │                  │            ▲
        │                  │            │
        │                  │     wa_flag_type_
        │                  │     question_link
        │                  │     (12 routes)
        │                  │
        │                  └──── wa_finding_
        │                        entity_links
        │                        (currently empty!)
        │                              │
        │                              ▼
        │                        mti_terms / wa_verse_records / verse_context_group
        │
        └─── (cross_registry_id) ──── back to word_registry (cross-reg pointers)


                                wa_dimension_index
                                (per-group dim assignment)
                                       ▲
                                       │
                                verse_context_group
                                       ▲
                                       │
                                  mti_terms

Session D tables (currently empty) read from:
  - wa_session_research_flags (SD pointers)
  - wa_session_b_findings (findings to synthesise)
  - wa_dimension_index (dimension landscape)
```

**The two empty link tables are the load-bearing missing edges.** Without `wa_finding_catalogue_links`, the catalogue → findings relationship is undocumented. Without `wa_finding_entity_links`, you can't query findings by verse or term. Phase 2 must populate both for new findings; backfilling the historical 195 is a separate question.

---

## Part 5 — How the Data Will Be Used in Future

This is the user's central question. Six concrete use cases, each driving different table queries:

### Use case A — Future researcher returns to a registry to recall what was concluded

**Question:** "Six months from now, what did I conclude about goodness?"

**Path:**
1. `word_registry` — get registry overview, status, inference_note, word_synopsis
2. `wa_session_b_findings` WHERE registry_id=67 — read all findings (including narrative chapter findings if Phase 2 writes chapters as a finding type, or `prose_section` if as separate prose rows)
3. `wa_session_research_flags` WHERE registry_id=67 — open SD pointers + flags
4. `wa_dimension_index` JOIN `verse_context_group` WHERE term in registry — group dimensions

**Quality of recall:** depends entirely on whether the link tables are populated. With them: trace any finding back to its source verses + catalogue questions. Without them: read narrative blobs and hope they're informative.

**Implication for Phase 2:** populate the link tables.

### Use case B — Session C produces the word study (reader-facing)

**Question:** "Write the goodness word study using all Session B work."

**Path:**
1. `prose_section` WHERE registry_id=67 AND `section_type_id` IN (sb_s2c_ch1..ch5) — the 5 chapters, in order, as foundation
2. `wa_session_b_findings` WHERE registry_id=67 AND finding_type IN (selected types) — supplementary findings not in chapters
3. `verse_context` JOIN `verse_context_group` — the verse evidence
4. The result is written back to `prose_section` with section_type_id IN (sc_v1_ch1..ch5)

**Implication:** Stage 2c chapters as `prose_section` rows is the natural fit. Session C READS these directly. If chapters were not in `prose_section`, Session C has nowhere to read the analytical foundation from.

### Use case C — Session D cross-registry synthesis

**Question:** "What does cluster C10 (registries 67 + others) reveal about goodness/kindness/etc.?"

**Path:**
1. `wa_session_research_flags` WHERE flag_code='SD_POINTER' AND registry_id IN (cluster registries) — synthesis seeds
2. `wa_session_b_findings` JOIN `wa_finding_entity_links` — findings touching shared verses across cluster
3. `wa_dimension_index` GROUP BY dimension WHERE owning_registry_no IN (cluster registries) — cluster's dimensional shape
4. `verse_context` for shared anchor verses across cluster

**Implication:** SD pointers are the index into Session D's work. They're already well-captured. Findings need link-table population for entity-based cross-registry queries.

### Use case D — Programme-level coverage and quality reports

**Question:** "How many words have completed Stage 2b? What's the catalogue coverage rate? Which words have unresolved high-priority flags?"

**Path:**
1. `word_registry` — status counts
2. `wa_session_b_findings` GROUP BY registry_id — finding counts per registry
3. `wa_session_research_flags` WHERE resolved=0 AND priority='HIGH' — open priority items
4. `wa_finding_catalogue_links` GROUP BY question_id — catalogue coverage rate

**Implication:** Without `wa_finding_catalogue_links`, the coverage-rate query produces 0 — looks like nothing has been answered, even though we have 195 findings.

### Use case E — Catalogue evolution (methodology iteration)

**Question:** "What new questions has the programme generated? Which existing questions need rewording?"

**Path:**
1. `wa_obs_question_catalogue` WHERE date_added > <last review> — new entries
2. The review notes (currently homeless) — wording corrections to existing questions

**Implication:** This use case has been silently failing — review notes have no DB home, so wording-improvement work since the catalogue stabilised has been lost. Phase 2 needs a decision on §6.2.

### Use case F — Quality / methodology audit

**Question:** "Are findings consistent with their source observations? Do all chapters cite findings? Are SD pointers properly grounded?"

**Path:**
1. `wa_session_b_findings` JOIN `wa_finding_entity_links` — verify every finding has at least one entity link
2. `wa_finding_catalogue_links` — verify every finding answers a catalogue question
3. `wa_session_research_flags` — verify SD pointers have evidence_basis

**Implication:** Quality auditing depends entirely on the link tables being populated.

---

## Part 6 — Fragmentation Risk + Mitigation (your risk #2)

**The risk you flagged:** "data and result visibility is fragmented throughout multiple interrelated tables and fields. This makes evaluation and review much more difficult."

**Real.** Recall path for "everything about goodness" requires joins across at minimum: `word_registry`, `wa_session_b_findings`, `wa_finding_catalogue_links`, `wa_finding_entity_links`, `wa_session_research_flags`, `wa_dimension_index`, `verse_context_group`, `prose_section`, `mti_terms`. Nine tables.

**Mitigation options:**

### 6.1 Build an "analytical view" SQL view

A `v_registry_analytical_summary` SQL view that joins the standard set and produces:
- registry header
- finding count by type
- open flag count by code
- chapter availability
- group/dimension landscape

One query, one result set. Phase 2 should ship this as part of the writer pilot.

### 6.2 Build a "registry recall .md" generator

Mirror to the readiness output: a script that produces a single `.md` per registry containing all analytical content (findings, chapters, SD pointers, review notes) for human reading. Update on demand. Path:

```
outputs/reports/words/wa-{NNN}-{word}-analytical-recall-{date}.md
```

This is an output of CC reading the DB, not the DB capturing — but it solves the human-side fragmentation directly. The readiness output already does this for input; the recall output does it for retrospective review.

### 6.3 Schema homes for the two homeless categories

Your decision needed on:

| Category | Option A | Option B |
|---|---|---|
| **Stage 2a observations** (49 per word) | Store as `wa_session_b_findings` rows with `finding_type='OBSERVATION'`, no entity links required | Create `wa_session_b_observations` table |
| **Question review notes** (41 per word) | Store as flags on existing `wa_obs_question_catalogue` rows (add `review_note` column) | Create `wa_obs_question_review_notes` table |

For both: Option A reuses existing tables, less schema churn but mixes observation types. Option B is cleaner separation, more tables.

**Recommend Option A for both.** Reduces table count, observations and findings already share most fields, and the `finding_type` field cleanly distinguishes them. Catalogue review notes can live as a dedicated column on the catalogue row (a small migration).

---

## Part 7 — Phase 2 Design Implications

What Phase 2 (the writer) must do, informed by this analysis:

1. **Map every parsed manifest entry to its target table** per §2.1.
2. **Populate both link tables** (`wa_finding_catalogue_links`, `wa_finding_entity_links`) for new findings — they are not optional.
3. **Use the existing `prose_section_type` codes for Stage 2c chapters** — `sb_s2c_ch1` through `sb_s2c_ch5`. Chapter 6 has no prose row (its content is the SD pointer table).
4. **Pre-write validation:**
    - Compare expected counts (from manifest meta) against what will be written
    - Confirm all referenced entities (mti_term_ids, verse_record_ids, group_ids) exist in DB
    - Confirm all referenced catalogue questions (obs_id) exist
    - Confirm registry_id resolves
    - Confirm no duplicates against existing rows (idempotency: re-running on same obslog must be safe)
5. **Transactional commit:** all-or-nothing per session. Pre-write validation passes → backup → commit. Failure rolls back cleanly.
6. **Audit log:** record what was written, with provenance to the obslog file path + version + parser version. Future researcher can trace any DB row back to its source obslog.
7. **Post-write verification:** count check (rows written = manifest count), foreign-key-integrity check (no orphans), catalogue-link integrity check (every finding has a link, every link has a finding).
8. **Mitigation for DB single-point-of-failure (your risk #1):** every Phase 2 run takes a labeled backup before writing; backups are testable (a restore drill can be scripted). The engine already has rolling-10 backup discipline; Phase 2 layers an explicit named snapshot per session.

---

## Part 8 — Open Decisions for Researcher

To unblock Phase 2 implementation:

1. **Schema home for Stage 2a observations** — `wa_session_b_findings` with `finding_type='OBSERVATION'` (CC recommendation), or new table?
2. **Schema home for review notes** — column on catalogue row (CC recommendation), or new table?
3. **Stage 2c chapters as `prose_section` rows** — confirm `sb_s2c_ch1..ch5` codes are correct targets. Chapter 6 (Open Items) — is its content fully captured by SD pointers, or is there value in a `prose_section` row for the chapter narrative itself?
4. **Backfill of historical 195 findings into link tables** — out of scope for Phase 2, or part of it?
5. **Build the `v_registry_analytical_summary` SQL view as part of Phase 2** — yes/no.
6. **Build the analytical-recall `.md` generator as part of Phase 2** — yes/no.

---

## Part 9 — Recommended next step

Phase 2 spec doc covering: writer architecture, table-by-table operations, validation gates, error handling, idempotency design. Then build + pilot on reg 067 obslog v2. Pilot success criterion: re-running the writer on the same obslog produces no new rows (idempotency); running it on a fresh obslog populates all 8 categories; comparison against the existing 3 patches shows the writer captures the 119+ Q&A + 6 chapters + 49 obs + 14 questions + 41 notes that the patches missed.

Once that pilot is clean, the writer scales to the remaining ~190 words.

---

*Drafted 2026-04-27 by Claude Code under researcher direction. Phase 1 (parser/validator) is built. Phase 2 (writer) is gated on the 6 open decisions above.*

Researcher observations:

 - I cannot see where and how AI integrated the anchor verses, verse context groups into the analytic results
 - I cannot see how the dimensions played a role in the analytic result
 - the destination of the observations is into the wa_session_b_findings.  Ultimately wa_session_b_findings must be 'resolved' or 'no longer relevant' and cross linked to a Question and answer, or session D pointer.  Session B findings is a log of the open questions that have not yet been converted to a finding, almost a open task list of research tasks.
 - I am concerned that the process_section and the catalogue Q&A gets out of sync.  not sure how best to audit it.  in essence, there should be no substantial statement in the prose_section (accross all chapters) that is not substantiated by the data, and there should be no Q&A that is not captured in the prose.
 - I am uncertain of the capturing of the anchor verse analysis - it seems to be only captured in the prose.  perhaps these findings must find its way back into the verse records

---

## Part 10 — CC Response to Researcher Observations

The five observations together reframe the data model significantly. My initial mapping in §2.1 was correct schemas-wise but missed the **integrative discipline** the analytical pipeline demands. Each observation surfaces a specific gap.

### 10.1 Observation 1 — Anchor verses + verse-context groups in analytic results

**Researcher concern:** "I cannot see where and how AI integrated the anchor verses, verse context groups into the analytic results."

**The gap.** Today the AI's anchor-verse readings (Unit 7) and group descriptions are **referenced** in chapters and Q&A answers (e.g. "884-001 doxological group, anchor Psa 34:8 reveals…") but not **linked** at the row level. The chapter prose mentions the group code; nothing in the DB says "finding F is about group 884-001" or "Q&A Q042 cites Mic 6:8 as primary anchor".

**The fix.** `wa_finding_entity_links` is the existing schema home — it carries `entity_type` (term / verse / group), `entity_id`, `entity_strongs`. Phase 2 must populate this for every finding and Q&A:

- Each Q&A's `anchor_verses` field (already parsed: e.g. "Psa 119:68, Gen 1:31, Mic 6:8") → resolves to verse_record_ids → `wa_finding_entity_links` rows with entity_type='verse'
- Each Q&A's referenced group_codes (parsed from answer text where present) → resolves to verse_context_group.id → entity_type='group' rows
- Each Q&A's referenced strongs → mti_term_id → entity_type='term' rows

After Phase 2: a query "show me all findings touching Mic 6:8" produces every Q&A and chapter reference.

**Implication.** Phase 2 parser needs to ALSO extract anchor-verse references from chapter bodies, not just Q&A `anchor_verses` fields. Reasonable, the pattern is regex-detectable.

### 10.2 Observation 2 — Dimensions in the analytic result

**Researcher concern:** "I cannot see how the dimensions played a role in the analytic result."

**The gap.** Same shape as 10.1, but for dimensions. `wa_dimension_index` carries the per-group dimension assignment. Findings and chapters reference dimensions ("dimension: Volition 04 — resolved goodness") but no DB row links a finding to the dimension it speaks to.

**The fix.** Add `entity_type='dimension'` to `wa_finding_entity_links`. Then for each finding/Q&A, parse references like "Cognition 03", "Volition 04", "dimension: Moral Character 05" and write the link.

Alternative: a dedicated `wa_finding_dimension_links` table. **Recommend the existing entity link** — simpler, same purpose. The `entity_type` field already supports this extension.

**Specific use case this unlocks:** Session D's cluster synthesis. Today: "show me all findings about dimension Cognition" → no path. After Phase 2: a 3-table join across findings × entity_links × dimension_index returns the answer in one query.

### 10.3 Observation 3 — `wa_session_b_findings` as open-task journal, not finding store

**Researcher reframing:** "Session B findings is a log of the open questions that have not yet been converted to a finding, almost a open task list of research tasks. Ultimately wa_session_b_findings must be 'resolved' or 'no longer relevant' and cross linked to a Question and answer, or session D pointer."

**This is a fundamental shift in my model.** I had `wa_session_b_findings` as the *findings* table — final analytical outputs. Your model is sharper:

- `wa_session_b_findings` = **observations / open tasks** journal. Each row is a Stage 2a observation OR a not-yet-resolved Stage 2b item.
- Each finding's lifecycle: **open → resolved or not_relevant**.
- A 'resolved' finding is **cross-linked** to its resolution: either a Q&A pair (via `wa_finding_catalogue_links`) or an SD pointer (via `wa_session_research_flags`).
- A 'not_relevant' finding is closed without resolution, with reason captured.

**Implication for the data model:**

The existing `wa_session_b_findings` schema already has the fields needed: `status`, `obsolete_reason`, `superseded_by_id`, `related_finding_id`. The lifecycle vocabulary should be:

| status value | Meaning |
|---|---|
| `open` | Stage 2a observation, not yet processed in Stage 2b |
| `resolved_qa` | Resolved via a Q&A pair (catalogue link populated) |
| `resolved_sd` | Resolved via an SD pointer (flag link populated) |
| `not_relevant` | Closed without analytical pickup; `obsolete_reason` captures why |
| `superseded` | Replaced by a more precise finding (`superseded_by_id` populated) |

**The Q&A pair lives in `wa_finding_catalogue_links`.** Looking at that table's columns: `finding_id`, `question_id`, `coverage`, `status`, `session_b_note`, `validated_date`, `validated_by`. The Q&A's *answer* text fits naturally in `session_b_note`. The `coverage` field captures whether the answer is full / partial / not-applicable. The `validated_date` records when the answer was reviewed.

**So the data model becomes:**

```text
wa_session_b_findings (the journal)
  ├── status='open'    — Stage 2a observation, raw
  ├── status='resolved_qa' ─→ wa_finding_catalogue_links ─→ wa_obs_question_catalogue
  │                            └── session_b_note = answer text
  ├── status='resolved_sd' ─→ wa_session_research_flags (flag_code='SD_POINTER')
  │                            └── description = SD pointer text
  └── status='not_relevant' (closed, with reason)
```

**A Q&A pair, in this model, is a row in `wa_finding_catalogue_links`.** The Q&A's question is the catalogue question; the Q&A's answer is in `session_b_note`; the Q&A's source observation is the linked finding.

**This is cleaner than my original mapping.** Phase 2 writer becomes:

1. **Parse Stage 2a observations** → INSERT to `wa_session_b_findings` with status='open', finding_type='OBSERVATION'
2. **Parse Stage 2b Q&As** → for each ANSWERED/PARTIAL Q&A:
   - Identify the source observation(s) the answer draws on (parser extracts OBS-NNN refs from answer text)
   - INSERT to `wa_finding_catalogue_links` with finding_id (the source observation's id), question_id, coverage, session_b_note=answer
   - UPDATE the source observation's status='resolved_qa'
3. **Parse SD pointers** → for each:
   - INSERT to `wa_session_research_flags` with flag_code='SD_POINTER'
   - If the SD pointer was raised from a specific observation (parser detects "OBS-NNN" in evidence_basis), UPDATE that observation's status='resolved_sd' and link via `related_finding_id`
4. **NOT_APPLICABLE Q&As** → no resolution row, but the catalogue question itself is recorded as 'not applicable' for this registry. Could be a `wa_finding_catalogue_links` row with `status='not_applicable'` and no `finding_id`.

This needs a small schema clarification: can `wa_finding_catalogue_links.finding_id` be NULL? The current FK suggests no — all links must reference a finding. If we want NOT_APPLICABLE rows, we need a NOT_APPLICABLE finding type or to allow NULL finding_id.

### 10.4 Observation 4 — `prose_section` ↔ Q&A drift; how to audit

**Researcher concern:** "There should be no substantial statement in the prose_section (across all chapters) that is not substantiated by the data, and there should be no Q&A that is not captured in the prose."

**This is a bidirectional coherence requirement.** Two specific audits:

**(i) Chapter → finding/Q&A.** Every substantive claim in a chapter must trace to either a finding or a Q&A. Mechanism: chapter prose explicitly cites finding IDs (e.g. "DIM-67-001") and Q&A codes (e.g. "OBS-026 → Q003"). The parser extracts these citations; the audit query checks each cited ID exists.

**(ii) Q&A/finding → chapter.** Every analytically significant Q&A or finding must be referenced somewhere in chapter prose. Mechanism: for each finding/Q&A, search across the chapters for its ID. If any answered Q&A has zero chapter references, that's an audit miss.

**Recommend a new table for this auditability:**

```sql
CREATE TABLE wa_prose_section_citations (
  id INTEGER PRIMARY KEY,
  prose_section_id INTEGER NOT NULL REFERENCES prose_section(id),
  cited_finding_id INTEGER REFERENCES wa_session_b_findings(id),
  cited_qa_link_id INTEGER REFERENCES wa_finding_catalogue_links(id),
  cited_sd_pointer_id INTEGER REFERENCES wa_session_research_flags(id),
  citation_form TEXT,  -- the literal text in the prose, e.g. "OBS-026", "DIM-67-001", "Q&A-003"
  delete_flagged INTEGER DEFAULT 0
);
```

Phase 2's parser populates this when ingesting chapters. The audit is then a single SQL query:

```sql
-- Findings cited in no chapter
SELECT f.id, f.finding_type, f.finding
  FROM wa_session_b_findings f
  WHERE f.registry_id = ?
    AND f.status IN ('resolved_qa', 'resolved_sd')
    AND NOT EXISTS (SELECT 1 FROM wa_prose_section_citations c WHERE c.cited_finding_id = f.id)
```

And the reverse:

```sql
-- Chapter citations that don't resolve to a real finding/Q&A/SD pointer
SELECT c.* FROM wa_prose_section_citations c
  WHERE c.cited_finding_id IS NOT NULL
    AND NOT EXISTS (SELECT 1 FROM wa_session_b_findings f WHERE f.id = c.cited_finding_id);
```

**Cost: one new table, well-scoped. Benefit: continuous audit of the prose-data coherence.**

### 10.5 Observation 5 — Anchor verse analysis returning to verse records

**Researcher concern:** "I am uncertain of the capturing of the anchor verse analysis — it seems to be only captured in the prose. Perhaps these findings must find its way back into the verse records."

**This is the deepest analytical layer.** Stage 2a Unit 7 produces a structured reading per anchor verse (the cross-registry vision questions, the inner-being observation, the SD pointer triggers). Today this lives only in the obslog narrative.

**Two options:**

**Option (a) — `verse_context.analysis_note` column.** Add a column to the existing `verse_context` table. Per-verse, per-term analytical commentary co-located with the verse classification. When a future researcher reads `verse_context` for Mic 6:8 in registry 67, they see both the classification (group 884-002, anchor=true, is_relevant=1) AND the analytical note ("the verse frames goodness as God-told, not human-derived").

**Option (b) — new `wa_verse_analysis` table.** Per-verse-per-term analytical record. More schema, but separate from VC classification (which is a verse_context concern).

**Recommend (a).** Reuses existing schema, the analytical note is naturally per-verse-per-term (same key as `verse_context`). Migration: ALTER TABLE add column. Phase 2 parser extracts the Unit 7 anchor-verse readings and writes them to the column.

**Implication for chapter content:** Chapter 3 (Annotated Verse Evidence) becomes essentially a generated view of `verse_context.analysis_note` for anchor verses, ordered by group. This solves observation 4 for Chapter 3 specifically — there is no risk of chapter prose drifting from verse data, because the chapter IS the verse data.

For Chapters 1, 2, 4, 5 — the synthesis chapters — the audit-via-citations approach (10.4) applies.

### 10.6 Updated data model summary

```text
                                wa_session_b_findings
                                (open / resolved_qa / resolved_sd /
                                 not_relevant / superseded)
                                      ▲   ▲
                ┌─────────────────────┘   └────────────────┐
                │                                          │
       wa_finding_catalogue_links                  wa_session_research_flags
       (the Q&A pairs:                             (SD pointers + flags:
        question + answer +                        flag_code SD_POINTER, SB_FINDING,
        coverage + validation)                     PH2_*, evidence flags)
                │                                          ▲
                ▼                                          │
       wa_obs_question_catalogue                    wa_finding_entity_links
       (the question framework)                     (term / verse / group / dimension)
                                                          ▲
                                                          │
                                                  wa_session_b_findings
                                                  + wa_finding_catalogue_links
                                                  (i.e. the findings AND the Q&A
                                                   links both link to entities)


       prose_section (chapters)
                │
                ▼
       wa_prose_section_citations  (NEW)
                │
                ▼
       (cited finding / Q&A link / SD pointer)


       verse_context.analysis_note  (NEW column)
       (per-verse-per-term analytical commentary,
        feeds Chapter 3 directly)


       wa_dimension_index
                ▲
                │ (linked from findings/Q&As via entity_links
                │  with entity_type='dimension' or via
                │  wa_dimension_index.id)
                │
       wa_session_b_findings + wa_finding_catalogue_links
```

### 10.7 Schema changes summary (revised)

| Change | Purpose | Cost |
|---|---|---|
| New column: `verse_context.analysis_note TEXT` | Anchor-verse analytical commentary per-verse-per-term | Migration: 1 ALTER TABLE |
| New table: `wa_prose_section_citations` | Audit prose ↔ findings coherence | Migration: 1 CREATE TABLE + 3 FKs |
| New column on `wa_obs_question_catalogue`: `review_note TEXT` (per researcher Option A) | Capture wording/validity notes inline | Migration: 1 ALTER TABLE |
| Lifecycle vocabulary on `wa_session_b_findings.status` | open / resolved_qa / resolved_sd / not_relevant / superseded | No schema change; controlled vocab only |
| Possibly: allow `wa_finding_catalogue_links.finding_id` NULL for NOT_APPLICABLE Q&As | Question dispositions without source finding | Schema check |
| Extend `wa_finding_entity_links.entity_type` vocab to include 'dimension' | Findings linked to dimensions | No schema change; controlled vocab only |

### 10.8 Phase 2 writer scope (revised)

The writer becomes more sophisticated than my §7 list — but each step maps to a clear DB write.

```text
For each Stage 2a observation:
  INSERT wa_session_b_findings (status='open', finding_type='OBSERVATION', term_id=...)

For each Stage 2b Q&A (ANSWERED or PARTIALLY):
  For each source observation OBS-NNN cited in answer:
    INSERT wa_finding_catalogue_links (finding_id=<source>, question_id=<obs_id>,
                                        session_b_note=<answer text>,
                                        coverage='full|partial', status='validated')
    UPDATE wa_session_b_findings SET status='resolved_qa' WHERE id=<source>
  For each anchor verse cited:
    INSERT wa_finding_entity_links (finding_id=<source>, entity_type='verse',
                                     entity_id=<vr_id>)
  For each group code cited:
    INSERT wa_finding_entity_links (finding_id=<source>, entity_type='group',
                                     entity_id=<group_id>)
  For each dimension cited:
    INSERT wa_finding_entity_links (finding_id=<source>, entity_type='dimension',
                                     entity_id=<dim_index_id>)

For each Stage 2b Q&A (NOT_APPLICABLE):
  INSERT wa_finding_catalogue_links (finding_id=NULL, question_id=<obs_id>,
                                      coverage='not_applicable',
                                      session_b_note='<rationale>')

For each SD pointer:
  INSERT wa_session_research_flags (flag_code='SD_POINTER', ...)
  If raised from observation OBS-NNN:
    UPDATE wa_session_b_findings SET status='resolved_sd', related_finding_id=...

For each Stage 2c chapter:
  INSERT prose_section (section_type_id=<sb_s2c_chN>, registry_id=..., body=...)
  Parse chapter body for citation patterns (OBS-NNN, Q&A-NNN, DIM-NN-NNN, SP-NNN)
  For each citation:
    INSERT wa_prose_section_citations (...)

For each Unit 7 anchor verse reading:
  UPDATE verse_context SET analysis_note=<text>
    WHERE verse_record_id=<...> AND mti_term_id=<...>

For each GAP question:
  INSERT wa_obs_question_catalogue (scope='universal', source_word=<this word>, ...)

For each WORD-SPECIFIC question:
  INSERT wa_obs_question_catalogue (scope=?, source_registry_no=<this registry>, ...)

For each review note on existing question:
  UPDATE wa_obs_question_catalogue SET review_note=<append> WHERE obs_id=<...>

For status update:
  UPDATE word_registry SET session_b_status=<...> WHERE no=<...>
```

This is comprehensive. The writer is more complex but produces a properly-integrated DB state where:
- Findings track their lifecycle (observation → resolution)
- Every Q&A is linked to its source observation, its catalogue question, and its evidence (verses/groups/dimensions)
- Chapter prose is audited against the findings/Q&As that ground it
- Anchor-verse analyses are returned to the verse records

### 10.9 Updated open decisions

Revised list — the schema changes above are now the load-bearing decisions:

1. **Approve `verse_context.analysis_note` column** (anchor-verse analyses return to verse records — observation 5).
2. **Approve `wa_prose_section_citations` table** (chapter ↔ findings audit — observation 4).
3. **Approve `wa_obs_question_catalogue.review_note` column** (Option A for review notes).
4. **Confirm lifecycle vocabulary on `wa_session_b_findings.status`** — open / resolved_qa / resolved_sd / not_relevant / superseded.
5. **Approve `wa_finding_entity_links.entity_type='dimension'`** vocab extension.
6. **Decide `wa_finding_catalogue_links.finding_id` nullability** — current FK is NOT NULL; needs check if NOT_APPLICABLE Q&As should still create rows.
7. **Backfill of historical 195 findings into the new lifecycle / link tables** — out of scope for Phase 2 pilot, addressed separately?

Once approved, Phase 2 spec doc is straightforward. I'll draft once you decide.

---

*Updated 2026-04-27 by Claude Code in response to researcher observations. The data model in §10.6 is the proposed Phase 2 target.*

next review researcher observations:

 - schema changes approved, good thinking.
 - catalogue findings - i think we should record a no finding against each question (except for word specific questions). This will allow us to monitor any questions that is not surfacing, and also backfill questions that emerge later.
 - I can clearly see that part of the data validation and readiness phase will be to re-align some of the data to land in the correct buckets, especially if AI need to review them.
 - There should be a section in the .md input for the analytics that highlights all the open session B questions with a priority to reconsider these questions - outcomes could be a) a Q&A answer, b) a follow up research question that triggers base line investigation c) a session D pointer d) marking the open item as no longer relevant.  The outcome must be linked and recorded on the session B item.
 - We could use the Session B findings open items for you to populate anomalies when you do data validations that need to be considered or resolved by AI.  The Session B findings becomes the key for AI to understand the status of the analytics when a revision of analytics are pushed towards AI.
 - we need to design the output of the analytics as a separate .md that can be presented to AI in the case of a revision.  In such a case there would be two inputs - the data (current .md extract) and analytic status (the result of previous analytics)
 - The prose section citations should be included in the work of AI during analysis.
 - Can you recheck that every data field has a destination and purpose in the input .md.  What we must validate is that the .md prompts AI to deal with it, and that the outcome is that you can 'resolve' it - it either finds a home in the findings, or the data must be resolved by mark it as deleted or changes the flags.

---

## Part 11 — CC Response to Researcher Observations (Round 2)

The eight new observations together complete a **closed-loop analytical system**. Each has a clear schema/process implication.

### 11.1 Schema changes approved

Acknowledged. Phase 2 migration plan:

| Migration | Action |
|---|---|
| M40 | `ALTER TABLE verse_context ADD COLUMN analysis_note TEXT` |
| M41 | `CREATE TABLE wa_prose_section_citations (...)` with FKs to prose_section, wa_session_b_findings, wa_finding_catalogue_links, wa_session_research_flags |
| M42 | `ALTER TABLE wa_obs_question_catalogue ADD COLUMN review_note TEXT` |
| M43 | Allow `wa_finding_catalogue_links.finding_id` to be NULL (for NO_FINDING coverage rows) |
| Vocab | Extend `wa_session_b_findings.status` to {open, resolved_qa, resolved_sd, not_relevant, superseded}; extend `wa_finding_entity_links.entity_type` to {term, verse, group, dimension}; extend `finding_type` to include 'OBSERVATION' and 'DATA_ANOMALY'; extend `coverage` to include 'no_finding' |

These migrations are tracked in `engine/migrations.py` per the existing engine pattern. Sequencing them as M40-M43 keeps the schema_version progression clean.

### 11.2 Catalogue completeness — record no_finding for every universal question

**Researcher direction:** "we should record a no finding against each question (except for word specific questions). This will allow us to monitor any questions that is not surfacing, and also backfill questions that emerge later."

**Implementation.** Phase 2 writer, after processing all Q&As from the obslog:

```text
For each universal question Q in wa_obs_question_catalogue (147 generic):
  IF Q was answered/partial in this session:
    (link already created with coverage='full|partial')
  ELSE IF Q was explicitly NOT_APPLICABLE in this session:
    INSERT wa_finding_catalogue_links (finding_id=NULL, question_id=Q.obs_id,
                                        coverage='not_applicable',
                                        session_b_note=<rationale from obslog>)
  ELSE (Q was not addressed in the obslog at all):
    INSERT wa_finding_catalogue_links (finding_id=NULL, question_id=Q.obs_id,
                                        coverage='no_finding',
                                        session_b_note='Question not surfaced during analysis.')

For word-specific questions (source_registry_no = current registry):
  Only ANSWERED rows recorded (these are intrinsically scoped — coverage by presence).
```

**Volume.** 147 universal coverage rows per word × ~200 words = ~29,400 rows when programme completes. Plus the actual answered findings on top. Acceptable — enables the monitoring use case.

**Use cases unlocked:**

```sql
-- Questions consistently not surfacing across the programme
SELECT q.obs_id, q.question_code, q.question_text,
       COUNT(*) FILTER (WHERE l.coverage='no_finding') AS not_surfaced,
       COUNT(*) FILTER (WHERE l.coverage='not_applicable') AS not_applicable,
       COUNT(*) FILTER (WHERE l.coverage IN ('full','partial')) AS answered
  FROM wa_obs_question_catalogue q
  JOIN wa_finding_catalogue_links l ON l.question_id = q.obs_id
  WHERE q.scope='universal'
  GROUP BY q.obs_id
  ORDER BY not_surfaced DESC;

-- Backfill identification — when a new question Q is added later:
-- find every word's analysis where Q was not yet considered
SELECT registry_id FROM word_registry
  WHERE id NOT IN (
    SELECT DISTINCT f.registry_id FROM wa_finding_catalogue_links l
    LEFT JOIN wa_session_b_findings f ON f.id = l.finding_id
    WHERE l.question_id = <new_q_obs_id>
  );
```

Each is a single query — no joins-from-hell.

### 11.3 Data validation/realignment phase

**Researcher observation:** "part of the data validation and readiness phase will be to re-align some of the data to land in the correct buckets, especially if AI need to review them."

**Confirmed.** CC's Phase 2 workflow has three distinct sub-phases:

1. **Pre-write validation** — does the parsed manifest reference real entities? Are required fields present?
2. **Write** — transactional commit per session.
3. **Post-write validation + realignment** — examine the freshly-written rows for anomalies, consistency issues, schema drift; realign where possible (e.g. moving a record from one bucket to another); raise items AI must address as 'open' findings (see §11.5).

The realignment phase is where CC catches things like:
- A finding linked to an entity that doesn't exist (orphan detection)
- A chapter citing an OBS-NNN that wasn't parsed (parser miss → AI investigation)
- A verse classification with a dimension assignment that contradicts the group's dimension (cross-table inconsistency)
- A flag raised but never resolved with no path forward

These get either auto-corrected (where deterministic) or raised as open findings for AI review in the next session.

### 11.4 New §N in readiness .md — Open Session B Items

**Researcher direction:** "There should be a section in the .md input for the analytics that highlights all the open session B questions with a priority to reconsider these questions — outcomes could be a) a Q&A answer, b) a follow up research question that triggers base line investigation c) a session D pointer d) marking the open item as no longer relevant. The outcome must be linked and recorded on the session B item."

**Implementation.** Add §N to the readiness output generator. Sourced from `wa_session_b_findings WHERE registry_id = ? AND status = 'open'`.

Each open item rendered in the .md:

```markdown
### Open finding `F-NNN` — [finding_type]
- **Raised:** [date] · **By:** [session_raised | data_validation] · **Priority:** [HIGH/MEDIUM/LOW]
- **Term/entity context:** [term_id / verse_record_id / group_id if applicable]
- **Item:** [finding text]
- **Required outcome (one of):**
  - (a) Resolve via Q&A: link to a catalogue question + record answer
  - (b) Raise as follow-up research question (new GAP question)
  - (c) Convert to SD pointer (cross-registry research target)
  - (d) Mark as no_longer_relevant with reason

**This item must be addressed in this analytical session.** Outcome will be recorded on `wa_session_b_findings.status` and linked accordingly.
```

The analytical instruction tells AI: §N items are not optional — every one must be resolved (lifecycle forward) before session close. This keeps `wa_session_b_findings` from accumulating stale 'open' rows.

### 11.5 Bidirectional channel — CC raises anomalies via findings

**Researcher direction:** "We could use the Session B findings open items for you to populate anomalies when you do data validations that need to be considered or resolved by AI."

**Implementation.** CC's post-write validation phase produces 'open' findings of type `DATA_ANOMALY` or similar. Examples of what CC might raise:

| CC-detected anomaly | finding_type | What AI must decide |
|---|---|---|
| Verse classified as anchor in `verse_context.is_anchor=1` but the anchor isn't cited in any chapter | `DATA_ANOMALY_ANCHOR_UNCITED` | Should the anchor designation be removed, or should it be cited in an upcoming chapter revision? |
| Group dimension assignment contradicts group description content | `DATA_ANOMALY_DIMENSION_DRIFT` | Reaffirm dimension, or correct via VCGROUP patch + dim review? |
| Q&A linked to a catalogue question, but the answer doesn't reference any anchor verse from the term | `DATA_ANOMALY_ANSWER_UNGROUNDED` | Re-ground the answer, or flag the question as poorly fitted? |
| Term has 0 active verses but `mti_terms.status='extracted'` | `DATA_ANOMALY_EMPTY_TERM` | Mark for delete (term-status fix), or investigate verse extraction? |
| Anchor-verse analysis_note exists but the verse is no longer marked is_anchor | `DATA_ANOMALY_ORPHAN_ANALYSIS` | Restore anchor designation, or move the analysis to a different anchor? |

Each appears in §N of the next readiness output. AI addresses each with one of the four outcome paths. Findings close cleanly.

**This is the closed-loop:** CC observes data state → raises items → AI analyses → resolves to Q&A / SD pointer / not_relevant → CC captures resolution → next loop. Findings table stays accurate as the working register.

### 11.6 Revision input architecture — two .md inputs

**Researcher direction:** "we need to design the output of the analytics as a separate .md that can be presented to AI in the case of a revision. In such a case there would be two inputs — the data (current .md extract) and analytic status (the result of previous analytics)."

**Two-input model:**

| Input | Source | Purpose |
|---|---|---|
| **Readiness `.md` (data)** | Generated from current DB state — same as today's pilot | "Here is the data as it stands now." |
| **Analytic Status `.md` (analysis)** | Generated from prior analytical work in DB — findings, Q&As, chapters, SD pointers, citations | "Here is what we previously concluded, with provenance." |

For an INITIAL analysis: only the readiness .md (analytic status doesn't exist yet).

For a REVISION: both. AI sees current data + prior analysis; identifies what's changed, what needs updating, what new conclusions are warranted.

**Analytic Status .md structure (proposed):**

```markdown
# wa-{NNN}-{word} — Analytic Status (revision input)

## Section 1 — Lifecycle summary
- Findings: open (N), resolved_qa (N), resolved_sd (N), not_relevant (N), superseded (N)
- Q&A coverage: full (N) / partial (N) / not_applicable (N) / no_finding (N) of 147 universal
- SD pointers: open (N), addressed (N)
- Chapters: present (yes/no, version)
- Last analytical session: [date], session_b_status: [...]

## Section 2 — Resolved findings (Q&A pairs)
For each resolved_qa finding:
- The original observation
- The catalogue question it answered
- The full answer (from session_b_note)
- Citations (entity links: verses, groups, dimensions)
- Provenance: which obslog produced it

## Section 3 — Resolved findings (SD pointers)
For each resolved_sd finding:
- Original observation
- The SD pointer it became
- Cross-registry target

## Section 4 — Not_relevant findings
With reasons.

## Section 5 — Stage 2c chapter content
Each chapter with citation manifest (cited findings, Q&As, SD pointers, observations).

## Section 6 — Anchor verse analytical notes
Per-verse-per-term analysis_note content from verse_context.

## Section 7 — Open items (carried forward from prior session)
[Same as readiness §N — for revision continuity.]
```

Generated by a new script `_build_analytic_status_v1_*.py`. Run on demand or before a revision session.

### 11.7 Prose citation discipline in analysis instructions

**Researcher direction:** "The prose section citations should be included in the work of AI during analysis."

**Implementation.** The Stage 2c writing instruction must require explicit citation in chapter prose. Pattern:

> Each substantive claim in a Stage 2c chapter MUST cite at least one of:
> - An OBS-NNN observation (Stage 2a working note)
> - A Q&A code (e.g. Q&A-042, Q042) — pointing to the answered Q&A pair
> - An SD pointer (SP-NNN)
> - A finding ID (e.g. DIM-67-001)
>
> Citations appear in the chapter body inline (e.g. "(OBS-026, Q042)"). The `wa_prose_section_citations` table is populated by parser at Phase 2 capture, indexing every citation.
>
> A chapter with substantive claims that lack citations fails the post-write coherence audit (§10.4). The audit query enumerates uncited substantive paragraphs.

This becomes a section in `wa-sessionb-analysis-output v1_2`.

### 11.8 Field-level destination audit — every field has a home and a prompt

**Researcher direction:** "Can you recheck that every data field has a destination and purpose in the input .md. What we must validate is that the .md prompts AI to deal with it, and that the outcome is that you can 'resolve' it — it either finds a home in the findings, or the data must be resolved by mark it as deleted or changes the flags."

**Walkthrough of the readiness `.md` against this requirement.** For each section, what data fields appear, how they prompt AI, and what the resolution path is:

| §  | Data field | Prompts AI to | Resolution path |
|---|---|---|---|
| A | `verse_context_status`, `session_b_status`, `dim_review_status`, `cluster_assignment`, `sb_classification` | Confirm status fields are coherent for analysis stage | If incoherent → DATA_ANOMALY finding raised by AI |
| A | `inference_note`, `word_synopsis`, `description` | Read as researcher framing context | Synthesised into chapter narrative; cited where used |
| A | `phase1_term_count`, `phase1_verse_count` | Cross-check against current OWNER + XREF counts | If mismatch → flag (anomaly or already-known) |
| B | Stage 1 Completion Record gates | Confirm each gate before Stage 2a | Any 'partial' gate → AI declares acceptance with caveat or raises blocking finding |
| C | Per OWNER term: strongs, gloss, vc_status, md_v, verses, groups, vc_rows | Each term must be analysed in Units 2-7 OR explicitly noted as not-on-topic | Each → at minimum, observations register entry; may → finding/Q&A |
| C | Legacy-VC term (vc_status='not_done') | Apply materiality protocol (ANALYSIS_VC_UNVERIFIED_MATERIAL flag if material) | → flag if material, otherwise note in audit trail |
| D | meaning_parse, senses, root family, related words, LSJ | Use for Unit 3 lexical foundation | → MEANING_OBSERVATION or ETYMOLOGY findings |
| E | XREF terms (each) | Consider cross-registry implications in Unit 2 | → SD pointer if cross-registry signal, else observation |
| F | Each group: code, description, dimension, anchor count | Read in Unit 4 landscape | → observation about characteristic; if dimension contradicts, raises DIM finding |
| F | NULL dimension | Must be addressed | → DIMREVIEW finding or AI proposes assignment |
| G | XREF sharing, verse co-occurrence, shared anchors | Use for Unit 5 cross-registry vision | → SD pointers from shared anchors; observations from co-occurrence |
| H | Existing session_b_findings | Read in Unit 6/9, decide each: confirm / question / supersede | → updated finding status (one of the 5 lifecycle values) |
| H | Open SD pointers + flags | Same as findings | → resolution path |
| I | Phase2 thin-evidence flags | Read in Unit 8, dispose each: confirmed / uncertain / inapplicable | → finding with disposition |
| J | Each verse with classification + target_word + verse_text | Anchor verses get full Unit 7 reading; non-anchors reviewed | → analysis_note on `verse_context` for anchors; observations for patterns |
| K | Legacy-VC notice | Apply materiality protocol per finding produced | → ANALYSIS_VC_UNVERIFIED_MATERIAL flag where material |
| L | Generic catalogue (147) | Each must produce a coverage row | → catalogue_link with coverage in {full, partial, not_applicable, no_finding} |
| L | Registry-specific catalogue questions (if any) | Each must be answered | → catalogue_link with coverage |
| M | Verification gates | Confirm gates before close | If any fail → AI raises blocker |
| **N (new)** | **Open Session B items** | **Each must be resolved this session** | **→ Q&A / SD pointer / no_longer_relevant** |

**Conclusion:** every data field in the readiness .md has a destination and a prompt. The §10.8 writer scope, the §11.4 §N section, and the §11.5 anomaly-bidirectional channel together guarantee that nothing the .md presents is silently passed over.

**Two implementation gaps to close in the readiness generator:**

1. **§N "Open Session B Items" section** — needs to be added (queries `wa_session_b_findings WHERE status='open' AND registry_id=...`).
2. **Field-level "prompt" annotations** — for some fields, the .md should include a brief "AI must:" line so the AI's analytical pass doesn't have to remember the protocol from the instruction. E.g. each Legacy-VC term gets an inline "AI must apply materiality test if any finding cites this term's classification."

Both are small additions to the v5 readiness generator (next iteration).

### 11.9 Closed-loop analytical system — the full picture

```text
┌─────────────────────────────────────────────────────────────┐
│                       DATABASE                              │
│  word_registry · mti_terms · verse_context · groups         │
│  wa_session_b_findings (lifecycle journal)                  │
│  wa_finding_catalogue_links (Q&A pairs + no_finding cov)    │
│  wa_finding_entity_links (term/verse/group/dimension)       │
│  wa_session_research_flags (SD pointers + flags)            │
│  wa_obs_question_catalogue (the question framework)         │
│  prose_section + wa_prose_section_citations (chapters)      │
│  wa_dimension_index (per-group dimension)                   │
└─────┬───────────────────────────────────────────────────────┘
      │
      │ (1) CC reads + validates
      ▼
┌─────────────────────────────────────────────────────────────┐
│  READINESS `.md` + `.json` (data input)                     │
│  §A-§M existing + §N Open Session B Items (new)             │
│  Every field has a prompt + destination (§11.8)             │
└─────┬───────────────────────────────────────────────────────┘
      │
      │ (2a) for INITIAL analysis: just data input
      │ (2b) for REVISION: + analytic status .md (§11.6)
      ▼
┌─────────────────────────────────────────────────────────────┐
│              CLAUDE AI ANALYTICAL SESSION                   │
│  Stage 2a observations (Unit 1-9)                           │
│  Stage 2b Q&A (147 universal + word-specific)               │
│  Stage 2c chapters (with citation discipline §11.7)         │
│  Open items resolution (§11.4 — every §N item resolved)     │
│  ── output: comprehensive obslog .md ──                     │
└─────┬───────────────────────────────────────────────────────┘
      │
      │ (3) CC parses + validates obslog
      ▼
┌─────────────────────────────────────────────────────────────┐
│  PARSER → MANIFEST .json + VALIDATION .md (Phase 1, built)  │
└─────┬───────────────────────────────────────────────────────┘
      │
      │ (4) CC writes to DB (Phase 2)
      ▼
┌─────────────────────────────────────────────────────────────┐
│   DB UPDATES — per the §10.8 writer scope:                  │
│   - findings, links, flags, prose, citations,               │
│     analysis_notes, catalogue entries                       │
│   - lifecycle states updated                                │
└─────┬───────────────────────────────────────────────────────┘
      │
      │ (5) CC post-write validation + realignment
      ▼
┌─────────────────────────────────────────────────────────────┐
│   CC RAISES ANOMALIES as 'open' findings (§11.5)            │
│   Carried into next session's §N                            │
└─────────────────────────────────────────────────────────────┘
      │
      │ (6) Cycle continues for revision sessions
      ▼
   (back to step 1)
```

Every artefact has a producer and consumer. Every analytical observation has a lifecycle path. No data hides; nothing is silently passed over.

### 11.10 Updated open decisions for Phase 2

Revised list — consolidated from §10.9 and the new observations:

1. ✅ **Schema migrations M40-M43** — researcher approved.
2. **Catalogue completeness — record no_finding rows for unanswered universal questions.** Approved direction; CC default coverage values: 'full', 'partial', 'not_applicable', 'no_finding'.
3. **CC-raised anomaly finding_types** — should they be a controlled list (e.g. `DATA_ANOMALY_*` family) or free-form? CC default: controlled list, growing as patterns emerge.
4. **§N section in readiness output** — to add to v5 readiness generator. Confirm: source query is `wa_session_b_findings WHERE status='open'` for the registry; rendered with the four resolution paths.
5. **Analytic status .md generator** — confirm priority. CC recommendation: build alongside Phase 2 writer, since it shares the same DB queries.
6. **Field-level "AI must:" prompts in readiness .md** — confirm yes for next generator iteration.
7. **Backfill of historical 195 findings** — out of scope for Phase 2; addressed once the writer is stable.
8. **Phase 2 spec doc draft** — once items 2-6 are confirmed, ready to write.

---

*Updated 2026-04-27 by Claude Code in response to researcher observations Round 2. The system in §11.9 is the proposed end-state.*