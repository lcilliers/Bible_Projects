# wa-prose-records-list-v1-20260421

> Framework B Soul Word Analysis Programme — Programme-Stage Prose Records Working List
> Session reference: prose
> Session date: 2026-04-21
> Previous output: wa-prose-obslog-v1-20260421 (session obslog; contains the session control trail and decisions)
> Governed by: wa-global-general-rules [current]; wa-directive-instruction-v1_2-20260421 §10 (schema enablement pattern); wa-patch-instruction-v2_3-20260421 §2.4 + §3 (PROSE patch structure)

---

## Change Control — v1

| Change | Section |
|---|---|
| New document. Initial list of programme-stage prose records to populate in `prose_section`, scoped to `prose_section_type.source_stage = 'programme'` rows. | All |

---

## Purpose

To enumerate the prose records to be drafted for the `prose_section` table in this session and subsequent sessions. Scope is programme-wide content only — the 8 seeded `prose_section_type` rows flagged `source_stage = 'programme'` in the M34 seed, plus any additional programme-stage types the researcher accepts.

This list is the planning artefact. It does not draft any body content; body drafting happens per-section in subsequent sessions. Every body entering the DB will travel via the v1_2 §10.4 path: one schema enablement directive followed by one or more PROSE patches.

---

## Status of the underlying schema

**Blocker.** `prose_section.registry_id` is declared `INTEGER NOT NULL REFERENCES word_registry(id)` in schema v3.14.0. Programme-wide prose has no registry. No reserved `word_registry` row exists as a sentinel. This blocks any insert for a programme-stage section until the column is relaxed.

**Resolution path per wa-directive-instruction-v1_2 §10.2.** One schema enablement directive relaxes the NOT NULL (retaining the FK), rebuilds the FTS5 companion, and confirms via three queries. After confirmation, PROSE patches insert programme-wide rows with `registry_id = NULL`.

**Status.** Directive not yet produced. First deliverable after this list is approved.

---

## Section 1 — The 8 seeded programme-stage types (from M34)

Source: `wa-programme-prose-extract-20260421.json` → `programme_prose.types[]`, all with `section_count = 0`.

Columns:
- **code** — `prose_section_type.code` (UNIQUE)
- **label** — display label
- **what it covers** — my reading of the description field
- **current source** — where the content presently lives (from the description's own pointer)
- **status of source** — whether a coherent source text exists or the content is scattered

| # | code | label | what it covers | current source | status |
|---|---|---|---|---|---|
| 1 | `prog_anchor_verse` | Programme — Anchor Verse Definition | Definition of anchor verses; dual purpose (analytical anchor + verse-context seed); minimum requirements | wa-reference [current] §16; wa-dimensionreview-instruction [current] §4.2 | Source exists in two places; mirror risk already present |
| 2 | `prog_xref_architecture` | Programme — XREF Architecture | OWNER / XREF term semantics; verse_context inheritance; canonical-row rule; cross-registry link pattern | wa-reference [current] §17; wa-registry-management-guide [current] | Scattered across two docs |
| 3 | `prog_validation_standard` | Programme — Document Validation Standard | Inflection-point completeness; gap-status discipline; cross-doc consistency; dry-run gate assessment | wa-reference [current] §18 | Single source; readiness for transfer is high |
| 4 | `prog_delete_discipline` | Programme — Soft-Delete Discipline | `delete_flagged` semantics; cascade rules; no physical deletes in automated flows; audit-trail retention | Referenced in wa-patch-instruction [current] §5.4; no consolidated home yet | **No consolidated source** — content to be assembled |
| 5 | `prog_field_authority` | Programme — Field Authority Rules | `mti_term_flags` canonical for somatic / god_as_subject; deprecation notes; which field wins on conflict | GR-DATA-003, GR-DATA-005 (global rules); wa-reference [current] | Rules carry the binding; prose needs narrative consolidation |
| 6 | `prog_backup_discipline` | Programme — Backup Discipline | Per-migration backup; per-patch backup; retention period; restoration procedure | wa-patch-instruction [current] §13.7 (rollback); wa-claudecode-instruction [current] (backup routines) | Partial; retention and restore procedures likely live in CC docs I do not yet have in context |
| 7 | `prog_patch_failure_protocol` | Programme — Patch Failure / REPAIR Protocol | What to do when a patch is rejected; failure patches; mid-pool recovery | wa-patch-instruction [current] §9 (REPAIR catalogue) and §9.x (failure path) | Single source; readiness for transfer is high |
| 8 | `prog_instruction_override_protocol` | Programme — Instruction Override Protocol | How instruction overrides are declared; logged in observations; recorded in handoff documents | Scattered — referenced in GR-OBS-001, GR-PROC-004, various instruction documents | **No consolidated source** — content to be assembled |

### Observations on Section 1

- **Three readiness tiers.** Items 3 and 7 are single-source — the prose draft is substantially a consolidation and light rewrite of an existing section. Items 1, 2, 5, 6 are multi-source — drafting is a synthesis task. Items 4 and 8 have no consolidated source — drafting is closer to original composition from rule bodies and scattered references.
- **Mirror risk already present in the seeds.** Item 1 is described as "currently mirrored in wa-reference §16 and wa-dimensionreview-instruction §4.2". Once the DB version is authoritative (per your stated objective), those two source sections become outdated mirrors. A protocol is needed for retiring or pointer-updating the source sections after prose ingestion. **Flagged.** This is a direction question, not authorship.
- **No `prose_section_type.id` in the extract.** The extract carries `code` but not the integer `id` the PROSE patch will need as `section_type_id`. CC will resolve the id from the code at patch apply time. Not a blocker for this list.

---

## Section 2 — Candidate additional programme-stage types (accept / reject)

The 8 seeded types cover disciplines, protocols, and field conventions. Reviewing the rule registry, reference snapshot, and memory, I identify gaps where programme-level content exists but has no prose-store home. These are candidates only — your accept/reject decides which move into `prose_section_type` via a CATALOGUE_POPULATION or prose-type-insert operation before any content drafting.

| # | proposed code | proposed label | what it would cover | where content currently lives | argument for | argument against |
|---|---|---|---|---|---|---|
| A | `prog_governing_question` | Programme — Governing Question | The foundational question: what Scripture reveals about characteristics, operations, interrelationships of the human inner being (spirit/soul/body) | GR-PROG-002 | The programme's defining frame belongs in the authoritative memory, not only in a rule record | Duplicates GR-PROG-002 directly; may be redundant |
| B | `prog_two_ai_architecture` | Programme — Two-AI Role Architecture | CA decides/interprets; CC executes; patches + directives as sole DB-change mechanisms; boundary discipline | GR-PROG-005; wa-patch-instruction §1; wa-directive-instruction §1 | Core programme design principle; currently inferred from rules and instruction scope statements, no narrative home | Risks becoming a mirror of GR-PROG-005 |
| C | `prog_dimension_vocabulary` | Programme — Dimension Vocabulary and Origin | The 11-dimension set; data-derived discipline (not imposed); governance of extension | wa-reference [current] §DIMENSION_LABEL vocabulary; GR-PROG-003; DR-13 extension rule | Closes the gap between rule (data-derived) and vocabulary (11 labels) — neither source tells the origin story | Vocabulary is operationally captured in `wa_vocab_member`; prose may be surplus |
| D | `prog_pipeline_architecture` | Programme — Pipeline Phase Architecture | Session A → VCB → Dimension Review → Session B (Readiness + Output) → Session C → Session D; phase boundaries and handoffs | Memory + multiple instruction documents | No single document tells the phase story end-to-end; new arrivals (or future-Claude) reconstruct it from fragments | Large scope — risk of becoming long; could split into multiple types |
| E | `prog_cluster_architecture` | Programme — Cluster Architecture | Clusters as processing units (C01–C22); cluster is not a classification of likeness; reassignment protocol | wa-registry-management-guide [current]; memory | Prevents recurrent misunderstanding of what clusters are for | Already lives in one source document; may be adequate there |
| F | `prog_obslog_discipline` | Programme — Obslog Discipline | Obslog as authoritative record; continuous write; verbatim researcher capture; log-precedes-chat in accelerated exchanges | GR-OBS-001, GR-TEMPO-001, GR-CAD-001, GR-RD-007 | Pattern of failure in this area is documented; a consolidated prose record would serve both human and future-Claude use | Heavy overlap with four rules; borderline duplication |
| G | `prog_file_naming_convention` | Programme — File Naming Convention | Full pattern family: `[prefix]-[reference]-[description]-v[n]-[YYYYMMDD].[ext]`; programme-wide vs registry-scoped; lowercase rule; compact date | GR-FILE-001 through GR-FILE-009; wa-reference §1; wa-patch-instruction §2 | The conventions are scattered across 6 rules, reference, and two instructions — prose would consolidate them | Same content is already highly structured in the rules registry |

### Recommendation on Section 2 candidates

Authorship view — these are not equal in value. Items **D** (pipeline architecture) and **B** (two-AI architecture) are the strongest additions: both have no narrative home today and both are genuinely reconstructed-from-fragments by readers. Item **G** (file naming) is the strongest *weak* case — the rules already carry the binding content and a prose mirror would add little. Items **A**, **C**, **E**, **F** are borderline; each is a judgement call about whether the prose store should mirror rules that already stand alone.

**Direction required from researcher.** Accept/reject for each of A–G. Items accepted will need `prose_section_type` rows created (via a separate patch or directive) before they can be drafted. That step can be bundled with the schema enablement directive or run afterwards — your call.

---

## Section 3 — Proposed drafting order

Assuming Section 1 only (8 seeded), plus whatever Section 2 items you accept:

**Tier 1 — single-source, transfer-and-polish (earliest, lowest risk):**
1. `prog_validation_standard` (#3)
2. `prog_patch_failure_protocol` (#7)

**Tier 2 — multi-source consolidation:**
3. `prog_anchor_verse` (#1) — short, foundational to Session A and Verse Context
4. `prog_xref_architecture` (#2) — directly supports registry management work
5. `prog_field_authority` (#5)
6. `prog_backup_discipline` (#6) — depends on CC documentation I may need you to surface

**Tier 3 — compose-from-fragments:**
7. `prog_delete_discipline` (#4)
8. `prog_instruction_override_protocol` (#8)

**Any accepted Section 2 items:** to be slotted per their source-readiness tier on acceptance.

Rationale — the order front-loads the items whose drafting is mostly consolidation and lowest interpretive risk, so the mechanics of the directive + PROSE-patch pipeline get exercised on easy content before harder synthesis work. It also sequences foundational concepts (anchor verse, XREF) before derived ones (delete discipline, override protocol) which reference them.

---

## Section 4 — The full flow per section (reference)

For each prose record, the working pattern will be:

1. **Draft session** (this type of session, extending the current one). Body drafted in markdown; reviewed with researcher; approved wording committed.
2. **Schema enablement directive** — once, for the whole programme-prose effort. Relaxes `prose_section.registry_id NOT NULL`, rebuilds FTS5, confirms via three queries. Per wa-directive-instruction-v1_2 §10.2–§10.3.
3. **PROSE patch** — carries the insert operation for the approved body. `registry_id = NULL`, `section_type_id = {id-lookup}`, `status = 'draft'`, `author = 'claude_ai'`, body text, source_file pointer. Per §10.4 and wa-patch-instruction-v2_3 §2.4 + §3.
4. **CC applies patch; returns confirmation** — row present, FTS indexed, word_count correct.
5. **Researcher reviews** the inserted row; promotes `status` from `draft` → `in_review` → `approved` via an update-patch when ready.
6. **Retirement of source-section mirrors** (Section 1 #1, #2, etc.) — open protocol question. Flagged above.

One directive at step 2 covers the whole session's worth of PROSE patches. Step 3 recurs per section; steps 4–5 recur per section.

---

## Items requiring researcher direction before drafting begins

1. **Accept/reject Section 2 candidates A–G.** Determines whether `prose_section_type` needs additional rows.
2. **Mirror retirement protocol.** For Section 1 items that name specific source-document sections (§16, §17, §18 of reference; §4.2 of dimension review): once prose is authoritative in the DB, what happens to those sections — retire, pointer-only, retain as mirror? Direction question.
3. **Confirm drafting order.** Accept the Tier 1 → Tier 2 → Tier 3 ordering, or redirect.
4. **Confirm per-section patch granularity.** v1_2 §10.4 illustrates an 8-insert omnibus PROSE patch. Your "one by one" pacing suggests one patch per section. Both are valid; confirm preference.

No directive or patch produced this turn. Those follow researcher sign-off on this list.

---

*wa-prose-records-list-v1-20260421 | First output for session reference `prose`*
