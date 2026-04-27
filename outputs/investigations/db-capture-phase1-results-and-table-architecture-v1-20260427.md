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
