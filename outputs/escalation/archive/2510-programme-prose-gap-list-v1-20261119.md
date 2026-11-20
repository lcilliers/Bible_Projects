# #2510 Programme prose: scope and gap list (v1, 2026-11-19)

Status: diagnosis only. Nothing in `bible_research.db` or any rule has been changed. Every verdict below was checked against a source named in its row. Where a statement could not be checked it says so, and it is not counted as stale.

## 1. Scope (defined from the record, not put to the researcher)

The programme prose is what `governance.prose_canonical_authority` names the canonical authority on what the project is about. In the store it is four things:

| Part | Where | Size | Last changed |
|---|---|---|---|
| The programme book, chapters 0 to 6 | `prose_section` of section types `preamble` and `prog_*` (source_stage programme) | 52 sections (51 in the extract; the Observations Framework, 21,706 characters, is the 52nd and is not yet read) | 2026-08-24 to 2026-09-18 |
| The programme glossary | section type `glossary_programme` | 107 sections (13 approved, 87 draft, 9 archived) | 2026-11-15 |
| The contentious glossary | section type `glossary_contentious` | 2 sections | 2026-11-13 |
| The concept pointers | `cfg_prose_concept` in `iba.db` | 8 rows | last change not checked |

Out of scope: the older prose of source stages session_a to session_d, essay, findings and contributor. That is history prose, not description of the programme. The documents `CLAUDE.md`, `iba/app/CHARTER.md`, `GOVERNANCE.md`, `BUILD.md` and `USER-GUIDE.md` are not edited here; the prose is checked against them and points to them. The project map (`outputs/escalation/2510-project-map-v1-20261119.md`) is the working summary from which the prose is rewritten.

The programme book is the whole task in practice: it was last written before the collection model, the layered reading, the node rules, the narrative in the database and the compliance and close routines existed. The word "collection" appears in 1 of its 52 sections.

## 2. The pattern across the book (counts from a text search of the 52 programme sections)

- 19 sections mention clusters, 22 the registry, 12 per-word work, 9 Session B and 9 the debate pipeline. These are the unit and mechanisms of the old method.
- The unit of study is now the collection (B:127, B:129; `governance.programme_stages`). The scope is now the surfaces of the groups behaviour and inner_being_state, each in one collection, not the registry of about 200 words.
- Cluster and subgroup are retired from nodes and observations (#2495, rules B:130 and B:131); `cluster_subgroup` is described in its own recorded use as the product of a retired pipeline. The five-stage cluster-reading pipeline of chapter 4 is that retired pipeline.
- About 25 sections carry live row counts in their text. Every count I compared is out of date (section 3). A count in prose goes stale; the rewrite points to the report that holds it.
- Three sections cite files or documents that are not where the prose says they are (section 4).

## 3. Section by section

Verdicts: **keep** (accurate), **amend** (sound core, named parts stale), **rewrite** (describes a method or mechanism no longer in use), **replace** (a section whose subject is gone; its slot is reused for what now plays that role, which may need a decision, section 6).

### Chapter 0 and 1: purpose

| Section | Verdict | Evidence |
|---|---|---|
| preamble | amend | Maps six areas; area 6 is the "instruction corpus" of Session A to D documents, which chapter 6 itself says no longer exist as such. Style paragraph stays. |
| prog_purp_mission | keep | History of the origin; no mechanism named. Not checked against the researcher's own account. |
| prog_purp_scope | rewrite | Says the registry of about 200 words "is the boundary". Live: `word_registry` is "the study's entry point; scope of a new-word run" (cfg_table); the scope is the surfaces of the two groups, in collections (B:129). |
| prog_purp_this_inner_being_programme | rewrite | "The unit of work is the word"; two-agent architecture; three orders of output per word. Live unit is the collection (B:127); one working agent. |
| prog_purp_defining_inner_being | keep | The researcher's definition, verbatim; pointed to by `cfg_prose_concept`. Not touched without the researcher. |
| prog_purp_science_and_bible | keep | Conceptual two-lens position; no mechanism named. |
| prog_purp_expected_outcome | amend | Success is described per word, corpus, programme. The outcome by collection (chapter 10 of the narrative is built by collection, B:127) is absent. |
| prog_purp_observations_framework | not read | 21,706 characters; it is the 52nd programme section and is not in the 51-section extract. Read and checked in the rewrite. |

### Chapter 2: method

| Section | Verdict | Evidence |
|---|---|---|
| prog_meth_overview | rewrite | Registry, collation, analysis, "dimensions", standing catalogue per word, synthesis. Live path: surfaces, groups, collections, the layered reading (stages 1 to 5, `layer.reading`), narrative. |
| prog_meth_registry | rewrite | Four-stage registry build to about 200 words. Replaced by the surface cycle (CHARTER section 5: group, structure, AI base, resolve, collections; tables `surface_term`, `surface_derivation`, `collection`). |
| prog_meth_flow | rewrite | Rewritten in September to three stages, but the Analysis paragraph names the debate pipeline "49 of 18,558 passages" and the cluster model as the two mechanisms. `governance.programme_stages` now names five analysis stages and the collection reading. |
| prog_meth_science | amend | The operational part ties the scientific pass to "Session B steps 7 to 8"; Session B has no live process. The second-lens principle stands; where the pass now sits is not recorded (open question for the researcher, section 6). |
| prog_meth_publishing | rewrite | Per-word studies at Session C and syntheses at Session D. Live: the narrative held as blocks in `iba.db` (`governance.narrative_home`), chapters by collection. |
| prog_meth_principles | amend | Principles 1, 2, 4, 6 and 9 (registry completeness, uniform catalogue per word, re-run through Session A to D) name the old method. Principles 3, 5, 7, 8 (inductive, evidence-first, biblical lens first, bottom-up) are consistent with B:4 and B:34. |
| prog_meth_constraints | amend | "Scope is bounded by the registry" and "no per-word publication" name the old unit. The second-lens and no-science-database constraints stand. |

### Chapter 3: disciplines

| Section | Verdict | Evidence |
|---|---|---|
| prog_disc_traceability | amend | Core (finding, hypothesis, inferential; database state verified) matches B:1, B:4, B:34. Names Verse Context groups and dimensions as the stages. |
| prog_disc_two_ai | amend | One working agent: accurate. Names `report.book_narrative_generate` with model `claude-sonnet-5` and the narrative as one API generation; B:127 says no bulk or one-shot generation produces the study result. Whether that step is still live is not checked. |
| prog_disc_session_continuity | amend | Three continuity mechanisms (session log, escalation, BUILD) are right. Missing: the compliance file, `/start-project`, session-close (SC checks), thread audit. Says memory "carries facts, feedback and project state"; memory now holds only who the researcher is and data pointers (MEMORY.md index). |
| prog_disc_tools | rewrite | Describes "two AI agents under researcher direction", Session A and the standing catalogue at Stage 4 of the cluster pipeline. |
| prog_disc_research_decisions | keep | Authority of the researcher; consistent with B:44, B:105. The statement "Claude did not interpret Scripture" sits beside B:127 (Claude reads the evidence and decides in most cases, the researcher scrutinises): the two read differently and are for the researcher to reconcile (section 6). |
| prog_disc_scope_integrity | amend | "Does not propose what to do next" against the current practice of recorded follow-ups and `wrap_up` (E:5, the session close). To be checked against the rules, not assumed in conflict. |

### Chapter 4: data architecture

Live counts used (queried 2026-11-19 from `iba.db`, read-only): `cluster` 96, `passage` 42, `verse_passage` 777, `hib` 21, `phenomenon` 121, `collection` 278 (169 confirmed, 86 merged, 23 retired), `verse_lexical` 1,520,168, `span` 378,182, `strong` 15,455, `strong_related` 88,467, `word_strong` 4,621, `cluster_strong` 15,682, `wa_obs_question_catalogue` 116, `cfg_` tables 43.

| Section | Verdict | Evidence |
|---|---|---|
| prog_data_database | amend | "Twenty tables" of config: there are 43 `cfg_` tables. Names the debate tables as the analysis layer. |
| prog_data_registry | amend | 180 rows: still true. Missing the surface and collection tables that now hold scope. |
| prog_data_terms | amend | Counts stale: verse_lexical 960,064 (live 1,520,168), span 391,417 (378,182), strong 15,293 (15,455), strong_related 87,535 (88,467), word_strong 4,874 (4,621). Structure described is right. |
| prog_xref_architecture | rewrite | Cluster membership of a Strong's code as the grouping; `cluster_strong` 7,609 rows (live 15,682). Replaced by the collection and the surface. |
| prog_data_verses | rewrite | Passage register of 18,558 rows, `verse_passage` 25,690, `hib` 63, `phenomenon` 177, "49 passages with a debate status". Live: `passage` 42, `verse_passage` 777, `hib` 21, `phenomenon` 121. The reason for the fall from 18,558 to 42 is not in anything I have read; to be found in BUILD before the text is written. |
| prog_anchor_verse | amend | Same passage and hib figures; mechanism may be live in a small form. |
| prog_data_dimensions | rewrite | The five-stage cluster-reading pipeline (verse-reading, char-subgroup and others) and "validated on M67". The steps are retired (`cluster_subgroup` use text; #2228 retired strand steps). |
| prog_data_questions | amend | Live catalogue is 116 rows (prose: 103). Whether Stage 4 still queries it is not checked; its recorded use says its questions are prompts, never answers to force (#2268 R17). |
| prog_data_synthesis | rewrite | Stage 5 "char-synergy" as the cluster pipeline's last stage. In the collection reading stage 5 is "claim formulation, not yet decided" (`governance.programme_stages`). |
| prog_data_prose_store | amend | 108 section types (live 110, 1,058 sections). Omits the glossary and the `ApplyPatch` step now in `Prose.ps1`. |
| prog_data_obslog_pipeline | amend | Heading names an obslog pipeline the body no longer describes; body names the debate writers. |

### Chapter 5: integrity and governance

| Section | Verdict | Evidence |
|---|---|---|
| prog_validation_standard | amend | `configmaint.validate` described correctly. Missing: compliance check, session-close checks, Spine-Check, thread audit. Debate status as the inflection point is stale. |
| prog_delete_discipline | keep | Soft delete on both databases; consistent with B:51, B:130. |
| prog_field_authority | amend | Mechanism (`cfg_column`) is right. Names `finding` and the `run` count 1,871 (live `run` 7,896). |
| prog_backup_discipline | amend | Counts and "currently 5" snapshots not re-checked; named snapshots (`iba/app/db/snapshots/kept/`) are now used and not described. |
| prog_patch_failure_protocol | keep | `cfg_on_fail` and the patch dry run match the config. |
| prog_instruction_override_protocol | amend | Cites `CLAUDE.md` section 10 for the `[current]` convention; `CLAUDE.md` is now a pointer file with no sections of rules. |
| prog_doc_impl_alignment | amend | The four rules are right. Missing the control map (`cfg_control_home`), rule 135 (adding a column) and the rule that the record is the memory (B:99). |

### Chapter 6: instruction corpus

| Section | Verdict | Evidence |
|---|---|---|
| prog_instr_global_rules | rewrite | Says `CLAUDE.md` is the compact reference with file map and conventions. The current `CLAUDE.md` says it holds pointers only and no rules; the rules print at `/start-project`. |
| prog_instr_reference | keep | Points to `cfg_enum`, `cfg_column` and the config report. |
| prog_instr_patches | amend | Names `wa-patch-instruction-v2_11-20260507.md` as the authoritative reference; the file is in `Workflow/Instructions/archive/`. |
| prog_instr_directives | amend | Same: `wa-directive-instruction-v1_4-20260506.md` is archived. |
| prog_instr_claudecode | rewrite | States no unifying guide exists; `/start-project`, `Start-Iba.ps1` and the point-of-use rules now do that work. |
| prog_instr_registry_guide | keep | States honestly there is none. Re-check when the scope table is written up. |
| prog_instr_session_a, session_b_readiness, session_b_output, session_c, session_d, verse_context, dimension_review | replace | Each section's body already says "no live process" or names a retired mechanism. The slots should carry what plays those roles now (base data, the collection reading and its stages, the narrative). Reusing a section type under a new label is a vocabulary change (section 6). |

### Glossary and pointers

| Part | Verdict | Evidence |
|---|---|---|
| Programme glossary | amend | Has entries for collection, surface, surface group, observation, node, subgroup, base, face, verse lexical, layer and stage (collection reading). No entry for claim, engagement or narrative. `cluster` is defined only as M-code cluster. 87 of 107 are drafts. #2506 records 1 glossary currency finding; I have not run the check. |
| `cfg_prose_concept` | amend | All 8 pointers resolve. Section 1066 (`role`) is a draft. Pointers name cluster-era terms (M-code cluster, T2, T3). No pointer for collection, the layered reading, the node and observation model, or the narrative. |

## 4. Checked facts that are errors in the text today

1. `wa-patch-instruction-v2_11-20260507.md` and `wa-directive-instruction-v1_4-20260506.md` are called authoritative; both are in `Workflow/Instructions/archive/`.
2. `prog_instruction_override_protocol` cites `CLAUDE.md` section 10; the file now has no numbered sections.
3. `prog_instr_global_rules` describes `CLAUDE.md` as a compact rule reference; its own first line says it holds pointers only.
4. Row counts in chapters 4 and 5 differ from the live tables for every table compared (listed above).
5. `prog_data_database` says twenty `cfg_` tables; the database holds 43.

## 5. Order of work (the researcher pre-approved changes on 2026-11-19: "changes are pre-approved")

1. The project map first (v1 written), checked by the researcher.
2. Chapters 1 and 2 (purpose and method), since the other chapters inherit the unit of study and the scope from them.
3. Chapter 4 (data), then 5, then 3, then 6.
4. The glossary entries for claim, engagement and narrative, then the `cfg_prose_concept` pointers.
5. The upkeep of the map at session close, as the researcher decided (D3): a config row and a check, built under its own design.

Each step is written through `Prose.ps1` (a dry run, then `ApplyPatch`), sections entering as draft; counts are not written into prose.

## 6. Points that are the researcher's to settle, not to guess

- **A.** The section types of the Session A to D slots in chapter 6 carry old labels. Reusing a type under a new label changes controlled vocabulary; a new type needs the researcher's instruction naming its code (B:55). Which of the two is wanted.
- **B.** Where the scientific second-lens pass sits in the collection reading. The record I read names no step for it.
- **C.** `prog_disc_research_decisions` (Claude never interpreted Scripture, never decided) against B:127 (Claude reads the evidence and decides in the majority of cases, the researcher scrutinises). Which wording the programme states.
- **D.** The fall of the passage register from 18,558 rows to 42: whether the debate pipeline is a live mechanism, a retained pilot or history. It decides whether chapter 4 keeps a section on it. I will look for the answer in BUILD and the escalation record first.

Everything else in section 3 I will write from the record.
