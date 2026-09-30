# Programme Prose — Architecture v2 Recommendations

**Document version:** v1
**Date:** 2026-04-27
**Author:** Claude Code, under researcher direction
**Companion:** [data/exports/reference/wa-programme-prose-extract-20260427.md](../../data/exports/reference/wa-programme-prose-extract-20260427.md) — current state of all 50 programme prose sections
**Architecture source:** [db-capture-phase1-results-and-table-architecture-v1-20260427.md](db-capture-phase1-results-and-table-architecture-v1-20260427.md) Parts 10-12

---

## Purpose

While you review the current programme prose extract, this document drafts the Architecture v2 updates needed for the programme prose. Four existing sections need versioned updates and one new section is proposed. Each draft below is suitable for direct insertion into the `prose_section` table once approved.

The v2 architecture changes that programme prose must reflect:

1. **CC's role expanded** — readiness output, obslog parser, Phase 2 writer, analytic status generator, anomaly detection
2. **Session B obslog-to-DB pipeline** — the canonical path for analytical capture
3. **Findings as a lifecycle journal** — open / resolved_qa / resolved_sd / not_relevant / superseded
4. **Catalogue completeness** — every universal question gets a coverage row per word
5. **Anchor verse analyses returning to verse records** — `verse_context.analysis_note`
6. **Chapter-data citation audit** — `wa_prose_section_citations`
7. **Two-input model for revision sessions** — readiness `.md` + analytic status `.md`

---

## Section 1 — `prog_instr_session_b_readiness` v1 → v2 (major shift)

### Why this section needs updating

The v1 prose describes Stage 1 as an AI-led data audit with patches, directives, and a Stage 1 Completion Record. Under v2, Stage 1 is a CC operation — CC generates a `readiness .md`+`.json`, validates field-level destinations, populates §N Open Items, and runs pre-flight integrity checks. AI's role is minimal at this stage.

### Proposed v2 prose draft

```text
The Session B Analysis Readiness instruction governs the readiness phase of
Session B — the stage that prepares a word for analytical work. Under
Architecture v2 (effective 2026-04-27) this phase is owned end-to-end by
Claude Code: AI's involvement is limited to receiving the readiness output
and proceeding into Analysis Output.

Claude Code generates two paired artefacts per registry: a readiness `.md`
(human-readable, structured into 14 sections covering registry overview,
term inventory, lexical foundation, XREF terms, group landscape with
dimensions, correlation signals, existing flags and findings, thin-evidence
flags, verbatim verse text, legacy-VC notice, generic catalogue with
embedded JSON, readiness verification, and open Session B items) and a
readiness `.json` (machine-readable mirror). The structure is deterministic
— same DB state produces byte-identical output modulo timestamp — and the
generation can be re-run any time the database state changes.

The §N Open Session B Items section carries forward every `wa_session_b_findings`
row at status `open` for the registry — Stage 2a observations from prior
sessions that have not yet resolved, plus any anomalies CC raised during
post-write validation of past obslogs. Each open item must reach one of
four outcomes by the close of the upcoming analytical session: resolution
via a Q&A pair, conversion to an SD pointer, raising as a new GAP catalogue
question, or marking as no-longer-relevant with reason. The instruction
treats §N as non-negotiable; an analytical session that closes leaving §N
items open has not closed cleanly.

Pre-flight integrity checks run before the readiness output is issued. CC
verifies anchor count consistency, dimension assignment coherence, term-
status integrity, and group description versus dimension drift. When an
inconsistency surfaces, CC writes a `wa_session_b_findings` row at status
`open` with a `DATA_ANOMALY_*` finding type — making the anomaly visible
to AI in the next session's §N. This bidirectional channel between CC's
data validation and AI's analytical review is the mechanism by which the
database and the analytical record stay coherent.

For revision sessions — when a registry has been analysed before and is
being revisited — CC produces an additional artefact: the analytic status
`.md`+`.json` companion, capturing lifecycle summary, resolved Q&A pairs,
resolved SD pointers, not-relevant findings, prior chapters, anchor-verse
analytical notes, and open items. AI for revision sessions reads both the
readiness output (current data) and the analytic status (prior analysis)
and produces an obslog reflecting any shifts.

Analysis Readiness is a discipline of preparation — under v2, it is the
discipline of producing a data artefact that prompts AI to deal with every
field it presents and to resolve every open item carried into the session.
It does not itself produce analytical output; it produces the readiness
state and the open-item agenda.
```

**Length:** ~2,750 chars (was 1,250).
**Operation:** new `prose_section` row with version=2; supersede v1.

---

## Section 2 — `prog_instr_session_b_output` v1 → v2 (citation + §N discipline)

### Why this section needs updating

The v1 prose describes patches, the Stage 1 Completion Record gate, and patch-based closure. Under v2, AI produces a comprehensive obslog and CC's writer parses it into the DB. The prose needs to reflect citation discipline (mandatory), the §N resolution discipline, and the obslog-only output.

### Proposed v2 prose draft

```text
The Session B Analysis Output instruction governs the analytical production
stage of Session B — where a word is read in depth and the programme's
principal analytical output is written. Under Architecture v2 (effective
2026-04-27), this stage takes the readiness `.md` (and, for revision
sessions, also the analytic status `.md`) as input and produces a single
comprehensive obslog `.md` as output. There are no AI-submitted patches.

The stage retains its three sub-stages. Stage 2a is the comprehensive
reading — every verse in the registry read against the full verse context
and the dimensional profile, with observations captured to the obslog as
they arise. Stage 2b is the Q&A partitioning — findings from the reading
are linked to catalogue questions, producing answers against existing
universal questions, raising new GAP questions where the catalogue does
not yet cover the surfaced pattern, and marking questions as not-applicable
where the word's evidence does not engage the question's domain. Stage 2c
is the analytic word output — five chapters of analytical prose (Word
Characteristic Summary, Word Impact Description, Annotated Verse Evidence,
Original Language Vocabulary, Connections and Research Pointers) plus a
sixth section (Open Items) that compiles SD pointers for Session D.

Two disciplines are mandatory under v2. The first is citation discipline:
every Stage 2b answer must cite its source observation as an OBS-NNN
reference inline; every Stage 2c chapter substantive claim must cite at
least one source — an OBS-NNN, a Q&A code, an SD pointer code, or an
existing finding ID. Without these citations, CC's parser cannot link
the answer to its evidence and the audit trail breaks. The second is the
§N open-item discipline: every open Session B finding carried forward
into the session — visible in §N of the readiness `.md` — must reach a
resolution outcome before session close. The obslog records the chosen
outcome path (Q&A, new GAP question, SD pointer, not-relevant) for each
open item; CC's parser reads these closures and updates the lifecycle
state.

The obslog is the canonical artefact. Claude Code parses it into the
database after the session: chapters write to the prose store, Q&A pairs
populate the catalogue-link table, observations land as new findings,
SD pointers and dimension references become flag and entity-link rows,
anchor-verse analytical readings return to the verse_context table, new
catalogue questions enter the question store, and review notes append to
existing catalogue rows. Every category of analytical content has a
defined target table; nothing the obslog records is silently dropped.

Closure is the writer's status_update operation, advancing
`word_registry.session_b_status` to Analysis Complete. Session C opens on
the chapter prose; Session D is notified of the SD pointers. Where
Readiness prepares, Output produces — together they remain the pair, but
under v2 their delivery mechanism is the obslog-to-DB capture pipeline,
not the patch flow.
```

**Length:** ~3,000 chars (was 1,371).
**Operation:** new `prose_section` row with version=2; supersede v1.

---

## Section 3 — `prog_disc_two_ai` v1 → v2 (CC's expanded role)

### Why this section needs updating

The v1 prose describes patches and directives as the only structured artefacts between AI and CC. Under v2, the obslog is the third structured artefact — the canonical analytical handoff. CC's role expanded substantially (readiness output, parser, writer, analytic status, anomaly detection). The prose needs to reflect this without losing the core "two-AI division" framing.

### Proposed v2 prose draft (incremental — keep first 3 paragraphs as-is, replace last paragraph)

Keep the first three paragraphs of v1 unchanged (they describe the analytical/operational division clearly). Replace the closing paragraph with:

```text
The two agents interact through three structured artefacts: **patches**,
**directives**, and **obslogs**. Patches remain the instrument for
discrete database changes — Verse Context corrections, REPAIR work,
dimension review writes — under the existing patch instruction. Directives
remain the instrument for operations outside the patch format — schema
migrations, ad-hoc queries, structural operations. Under Architecture v2
(2026-04-27), the **obslog** joins them as the canonical artefact for
analytical sessions: Claude AI produces a comprehensive obslog `.md` and
Claude Code parses it into the database via the Phase 2 writer pipeline.
The writer maps every category of analytical content — observations,
Q&A pairs, chapters, SD pointers, anchor-verse analyses, new catalogue
questions, review notes, status updates — to its DB target table, with
pre-write backup, transactional commit, and post-write validation.

The researcher sits at the gate between the two agents. Patches and
directives are reviewed before Claude Code applies them. Obslogs follow
the same discipline — Claude AI produces the obslog, the researcher
reviews the analytical work, Claude Code parses it into the database.
Under v2 this workflow is more integrated: Claude Code's role expanded
to include the readiness output generation that prompts AI's analytical
work, the analytic status generation that supports revision sessions,
and the anomaly detection that surfaces data inconsistencies as open
findings for AI to address in the next session. The bidirectional
channel — AI's analytical observations and CC's data anomalies both
landing as `wa_session_b_findings` rows for resolution — is the
mechanism that keeps the analytical record and the database coherent.
```

**Length:** ~1,650 chars added (replacing ~750ch). Net section: ~4,750ch (was 3,838).
**Operation:** new `prose_section` row with version=2; supersede v1.

---

## Section 4 — `prog_data_questions` v1 → v2 (lifecycle + coverage + link tables)

### Why this section needs updating

The v1 prose describes the catalogue and findings as the analytical output, with a join recording which findings answer which questions. Under v2, the model is sharper:

- Findings are an open-task journal (lifecycle: open / resolved_qa / resolved_sd / not_relevant / superseded)
- Q&A pairs live in `wa_finding_catalogue_links` (with the answer in `session_b_note`)
- Coverage column carries `full` / `partial` / `not_applicable` / `no_finding`
- `wa_finding_entity_links` populated for every Q&A — linking findings to verses, groups, dimensions
- The link tables that were schemed but empty are now actively populated

### Proposed v2 prose draft (keep first 2 paragraphs, expand the rest)

Keep the first two paragraphs of v1 (catalogue overview + scope distinction). Replace the section discussing `wa_session_b_findings` with:

```text
`wa_session_b_findings` is the programme's analytical journal. Under
Architecture v2 (2026-04-27) it operates as an open-task lifecycle
register: each row is an analytical observation or a CC-raised data
anomaly that progresses through a defined lifecycle. The `status` field
takes five values. A finding at `open` is a working observation
awaiting resolution — typically a Stage 2a observation captured during
a comprehensive reading, or a `DATA_ANOMALY_*` row CC wrote during
post-write validation. A finding at `resolved_qa` has been linked to a
catalogue question through `wa_finding_catalogue_links` — the question
is the question, the source observation is the source, and the answer
is recorded in the link's `session_b_note` field. A finding at
`resolved_sd` has been converted to an SD pointer for Session D's
cross-registry synthesis. A finding at `not_relevant` has been closed
without analytical pickup, with reason captured. A finding at
`superseded` has been replaced by a more precise finding through the
`superseded_by_id` reference. Every analytical session works through
its open findings: the obslog records the chosen outcome path for each,
and Claude Code's writer updates the lifecycle state.

The Q&A architecture under v2 lives in two tables. The catalogue
question is the question; the link in `wa_finding_catalogue_links` is
the Q&A pair — finding_id pointing to the source observation, question_id
pointing to the catalogue row, `session_b_note` carrying the answer
text, and `coverage` taking one of four values. `full` records an
ANSWERED Q&A with substantive evidence. `partial` records a PARTIALLY
ANSWERED Q&A with qualification. `not_applicable` records a question
the word's evidence does not engage — the link has no source finding
(the table allows a null finding_id under M43) but records the
not-applicable disposition with rationale. `no_finding` is filled by
Claude Code's catalogue completeness sweep for any universal question
not addressed by the analytical session — it surfaces silent misses
and creates the backfill ledger for questions added to the catalogue
later. With these four coverage values, every universal question for
every analysed word produces a coverage row; the catalogue's coverage
across the programme can be queried in a single SQL pass.

`wa_finding_entity_links` is the layer that grounds findings in the
data. For every Q&A, Claude Code's writer creates entity-link rows
recording which terms (mti_term_id), verses (verse_record_id), groups
(verse_context_group.id), and dimensions (wa_dimension_index.id) the
answer cites. The link table answers two queries that the prose alone
cannot: which findings touch a particular verse — readable from the
verse-link rows — and which findings speak to a particular dimension —
readable from the dimension-link rows. Session D's cross-registry work
reads from these link tables to discover findings that share verses or
dimensions across registries.

The catalogue is generative. New questions arise from analytical work:
GAP questions identify gaps in the programme's standing line of
inquiry; word-specific extension questions surface the inquiries that
a particular word's evidence made worth indexing for future passes
on the same word. Under v2 these new questions enter `wa_obs_question_catalogue`
through the writer pipeline, with `catalogue_version` field carrying
the introduction marker (e.g. `v2.1-R067`). Review notes raised against
existing questions land in the catalogue row's `review_note` column —
the column added by migration M42 — preserving the audit trail of
wording and validity observations that prior versions had no schema
home for.
```

**Length:** ~3,400 chars added; net section: ~9,600ch (was 6,200).
**Operation:** new `prose_section` row with version=2; supersede v1.

---

## Section 5 — NEW section: `prog_data_obslog_pipeline`

### Why a new section

The obslog-to-DB capture pipeline is now a load-bearing programme mechanism but no existing prose section describes it. It belongs as a peer of `prog_data_database`, `prog_data_terms`, etc. — under the data architecture group.

### Proposed new section text

```text
Architecture v2 introduces a structured pipeline by which Session B
analytical work is captured into the database. Where the patch flow
moved discrete database changes from AI to CC, the obslog flow moves
analytical content — observations, Q&A pairs, chapters, SD pointers,
anchor-verse readings, new questions, review notes — from a
comprehensive obslog `.md` to its DB target tables in a single
transactional pass.

The pipeline runs in three phases. Phase 1 is parsing: Claude Code
reads the obslog and produces a structured manifest in JSON, validated
for completeness against declared counts. Phase 2 is writing: each
manifest category is dispatched to its target table — observations
become `wa_session_b_findings` rows, Q&A pairs become
`wa_finding_catalogue_links` rows with entity links to verses and
groups and dimensions, chapters become `prose_section` rows under
section_type codes `sb_s2c_ch1` through `sb_s2c_ch5`, anchor-verse
analytical readings update `verse_context.analysis_note`, new
questions enter `wa_obs_question_catalogue`, review notes append to
existing catalogue rows, and SD pointers and status updates land in
their respective tables. Phase 3 is validation and anomaly raising:
post-write, Claude Code verifies row counts, foreign-key integrity,
and the catalogue-link coherence; data inconsistencies surface as
`DATA_ANOMALY_*` findings at `status='open'`, carried into the next
analytical session for AI to address.

Idempotency is structural. The writer's per-category logic checks for
existing rows before inserting — re-running on the same obslog produces
no duplicates. The pipeline is transactional: pre-write backup,
single-transaction commit, all-or-nothing on failure. The schema
supports this with M40 through M43, the four migrations that landed
the architecture: a `verse_context.analysis_note` column for anchor-
verse commentary, a `wa_prose_section_citations` table for the chapter-
to-evidence audit trail, a `wa_obs_question_catalogue.review_note`
column for catalogue maintenance, and a `wa_finding_catalogue_links.finding_id`
nullability change to support the no-finding and not-applicable
coverage states.

Two further artefacts complete the pipeline. The readiness `.md` and
`.json`, generated before the analytical session, present every data
field in the registry's current state with a clear destination and a
prompt for the analyst — the field-level destination audit guarantees
that nothing the readiness presents is silently passed over. The
analytic status `.md`, generated for revision sessions, captures the
prior analytical state — lifecycle summary, resolved Q&A pairs,
resolved SD pointers, prior chapters, anchor analyses, open items —
so that revision work has both the current data and the prior analysis
in view. Together the readiness output, the obslog, and the analytic
status form a closed loop: data state in, analytical work, capture to
DB, anomalies surfaced for next session, revision input ready.
```

**Length:** ~3,100 chars.
**Operation:** new `prose_section` row + new `prose_section_type` row with code `prog_data_obslog_pipeline` and label "Programme — Obslog-to-DB capture pipeline".

---

## Implementation order (when researcher approves)

1. Insert new `prose_section_type` row for `prog_data_obslog_pipeline` (single migration).
2. Insert v2 `prose_section` rows for the 4 affected sections + the new section. Mark v1 rows superseded via `superseded_by_id`.
3. Re-run `scripts/build_programme_prose_extract.py --include-body --also-markdown` to produce the updated extract.
4. Update [tasks.md](../../tasks.md) item G to checked.

The five edits together capture all v2 architectural shifts in the programme prose. Subject to your approval.

---

*Drafted 2026-04-27 by Claude Code under researcher direction. The current state is in the companion programme-prose extract. The proposed v2 changes are the five sections above.*
