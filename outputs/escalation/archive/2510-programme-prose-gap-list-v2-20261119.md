# #2510 Programme prose: scope and gap list (v2, 2026-11-19)

Status: diagnosis and rewrite brief. Nothing in `bible_research.db` or any rule has been changed. This version corrects v1 against the researcher's review of 2026-11-19 (recorded verbatim at #2510 v18). Every verdict names its source; a statement that could not be checked says so.

## 1. What the prose is for, and the standard it is rewritten to

The programme prose is the authoritative record of the programme for an **external reader** (`governance.prose_canonical_authority`). It is rewritten to reflect the project as it now stands, to these standards (researcher, review of 2026-11-19):

1. **Current status only.** No retired or out-of-date information is carried in the live text. A retired method goes to its history home (the project map section 5, BUILD, git), not into the prose as a note (B:96).
2. **Silence is not ignored.** Where the prose says nothing about a part of the project that now exists (the collection, the surfaces and their groups, the layered reading, the node and observation rules, the narrative as built, the claims, the compliance and close routines), the rewrite adds it. Where the prose speaks of something that no longer exists, the rewrite removes it. Each subject of an old section is accounted for: kept, restated as it now stands, or removed with the place in the record that shows why.
3. **The study's own labels.** Section types and terms are the ones the study already uses (collection, surface, surface group, subgroup, observation, node, face, layer, stage, claim). No new label is invented where one exists. A section slot whose subject is gone is not given a new label; the subject that now plays its role is written under the label the study uses for it.
4. **One reading style.** The reading style of the rewritten sections is the style of the current record (plain, evidence-first, the form of the glossary and of `governance.programme_stages`), written to be read cold by an external reader, not the style of the August to September book.
5. **Counts are not written into prose.** A count goes stale; the text points to the report that holds it.

## 2. Scope

In the store the prose is four things (read from `bible_research.db` and `iba.db`, 2026-11-19):

| Part | Where | Size |
|---|---|---|
| The programme book, chapters 0 to 6 | `prose_section` of section types `preamble` and `prog_*` | 52 sections, all read; 2026-08-24 to 2026-09-18 |
| The programme glossary | `glossary_programme` | 107 sections (13 approved, 87 draft, 9 archived) |
| The contentious glossary | `glossary_contentious` | 2 sections |
| The concept pointers | `cfg_prose_concept` | 8 rows |

Out of scope: the older prose of source stages session_a to session_d, essay, findings and contributor (history prose). `CLAUDE.md`, `CHARTER.md`, `GOVERNANCE.md`, `BUILD.md` and `USER-GUIDE.md` are not edited here; the prose points to them. The working summary from which the prose is rewritten is `outputs/escalation/2510-project-map-v3-20261120.md`.

The word "collection" appears in 1 of 52 sections. The book was written before the collection model, the layered reading, the node rules, the narrative in the database and the compliance and close routines.

## 3. Section by section

Verdicts: **keep**, **amend** (sound core, named parts stale), **rewrite** (describes a method or mechanism no longer in use or says too little of what is now there).

### Chapters 0 and 1: purpose

| Section | Verdict | Evidence |
|---|---|---|
| preamble | amend | Area 6 is the "instruction corpus" of Session A to D documents, which chapter 6 itself says no longer exist as such. Style paragraph stays. |
| prog_purp_mission | keep | Origin; no mechanism named. |
| prog_purp_scope | rewrite | Names the registry of about 200 words as the boundary. Live scope: the surfaces of the groups behaviour and inner_being_state, each in one collection (B:129). |
| prog_purp_this_inner_being_programme | rewrite | "The unit of work is the word"; two-agent architecture. Live unit: the collection (B:127); one working agent. |
| prog_purp_defining_inner_being | keep | The researcher's definition, verbatim; pointed to by `cfg_prose_concept`. Not touched without the researcher. |
| prog_purp_science_and_bible | amend | The two-lens position stands. The science reading is part of the claims reading (researcher, 2026-11-19): the section says where it sits, in the claim formulation (stage 5), not as a separate pass. |
| prog_purp_expected_outcome | amend | Success per word, corpus, programme. The outcome by collection (chapter 10 of the narrative is built by collection, B:127) is absent. |
| **prog_purp_observations_framework** | **rewrite** | Read in full (21,706 characters; section 128, draft, v204). It describes the per-word tier framework T0 to T7 and the standing question catalogue (lineage L2, `outputs/escalation/2510-inner-being-definition-lineage-v1-20261119.md`; `wa_obs_question_catalogue`, whose questions are prompts and never answers to force, #2268 R17), with the tiers answered in "Session B" and "Session D". That method is retired: the unit is no longer the word, and no observation carries a tier. See section 3a. |

### 3a. What the rewrite of the observations framework must state

The section is the programme's account of its framework of enquiry. In the current project the framework is:

- **The collection reading in stages** (`governance.programme_stages`, B:132, `cfg_setting layer.reading`): stage 1 the lexical analysis (words by surface and lettered Strong's code, an observation for each sense the verses give); stage 2 the grouping of the surfaces by dictionary meaning; stage 3 the verse-lexical observations (steps 1.2 and 2.1: Strong's enrichment, pairings, qualifiers, entities, direction, group relations, double meaning); stage 4 the inner-being analysis made from the stage 3 observations; stage 5 the claim formulation. Stages 1 to 3 state what the dictionary, the verses and the stored structure show; none states what a word does for the inner being (B:132, B:133).
- **The observation and the node** as the record of a finding (B:130, B:131): an observation founded in the verse, never a repeat of it, with a node for each occurrence it holds for; the ledger (`collection_layer_item`) so that no aspect is left open (B:134).
- **The epistemological basis**, which stands from the old section and is stated as it now operates: Scripture is the primary and governing source; its silence on an aspect is recorded and not filled; the original-language study is the primary evidential tool; the human sciences are an interpretive lens, **part of the claims reading** and not a parallel pass.

Each subject of the eight tiers is accounted for, so that nothing the old section says is silently dropped. Where the record shows a subject now lives somewhere, the section says where; where it was retired, the section omits it and the project map section 5 carries the history.

| Old subject | Where it stands now (source) | State of evidence |
|---|---|---|
| T0 divine image and created design | Part of the researcher's definition of the inner being (`prog_purp_defining_inner_being`) and of the claims reading; no observation item carries it | To be confirmed from the definition lineage section 2 when the section is drafted |
| T1 definition | The group definition (step 1.1) and the Strong's enrichment (step 1.2), by dictionary meaning only | Read: `layer.reading` |
| T2 location, T3 faculties, T4 interfaces, T5 formation, T6 relations to other characteristics | Questions of the inner-being analysis (stage 4) and the claims (stage 5); stage 4 is not yet built. The record of what stage 4 will hold is `outputs/escalation/2510-stage4-ib-observations-draft-v1-20261119.md` | Stage 4 undefined in config; stated as such, not filled |
| T7 evidential foundation | The epistemological basis above; the lexicon read at stage 1, the verse read in context | Read: B:131, B:132 |

Anything in the old section that the rewrite cannot place from the record is listed for the researcher with the evidence searched; it is not carried forward as if current.

### Chapter 2: method

| Section | Verdict | Evidence |
|---|---|---|
| prog_meth_overview | rewrite | Registry, collation, "dimensions", standing catalogue per word. Live: surfaces, groups, collections, the layered reading (stages 1 to 5), narrative. |
| prog_meth_registry | rewrite | Four-stage registry build to about 200 words. Replaced by the surface cycle (CHARTER section 5; tables `surface_term`, `surface_derivation`, `collection`). |
| prog_meth_flow | rewrite | Names the debate pipeline and the cluster model as the two mechanisms. `governance.programme_stages` names the stages. |
| prog_meth_science | rewrite | Ties the scientific pass to "Session B steps 7 to 8". Settled: the science reading is part of the claims reading (researcher, 2026-11-19; the narrative's science chapter is a deferred slot, project map). |
| prog_meth_publishing | rewrite | Per-word studies and syntheses. Live: the narrative held as blocks in `iba.db` (`governance.narrative_home`), chapters by collection. |
| prog_meth_principles | amend | Principles 1, 2, 4, 6 and 9 name the old method; 3, 5, 7, 8 are consistent with B:4 and B:34. |
| prog_meth_constraints | amend | "Scope is bounded by the registry" and "no per-word publication" name the old unit. |

### Chapter 3: disciplines

| Section | Verdict | Evidence |
|---|---|---|
| prog_disc_traceability | amend | Core matches B:1, B:4, B:34. Names Verse Context groups and dimensions as the stages. |
| prog_disc_two_ai | amend | One working agent: accurate. Names `report.book_narrative_generate`; the narrative generator is inactive (project map). |
| prog_disc_session_continuity | amend | Missing: the compliance file, `/start-project`, session-close, thread audit. Memory holds only who the researcher is and data pointers. |
| prog_disc_tools | rewrite | Two AI agents, Session A and the standing catalogue at Stage 4 of the cluster pipeline. |
| **prog_disc_research_decisions** | **amend** | Settled (researcher, 2026-11-19): **Claude is expected to interpret the given data and evidence.** Every interpretation is backed by trackable evidence (the record, B:34, B:4); Claude does not leave it to the researcher to discover an unfounded interpretation. The researcher scrutinises Claude's judgement and decides what the evidence cannot settle (B:127). The sentence "Claude did not interpret Scripture" is removed. |
| prog_disc_scope_integrity | amend | "Does not propose what to do next" against recorded follow-ups and `wrap_up` (E:5, close). Checked against the rules before amending. |

### Chapter 4: data architecture

Live counts (read-only, 2026-11-19) are in the report, not the prose.

| Section | Verdict | Evidence |
|---|---|---|
| prog_data_database | amend | "Twenty tables" of config: the database holds 43 `cfg_` tables. |
| prog_data_registry | amend | Missing the surface and collection tables that now hold scope. |
| prog_data_terms | amend | Counts stale; structure right. |
| prog_xref_architecture | rewrite | Cluster membership as the grouping. Replaced by the collection and the surface. |
| prog_data_verses | rewrite | Passage register of 18,558 rows. **Settled from the record, not asked:** the register was built, retired 2026-07-26, repurposed 2026-07-27 as a verse-fanout record and redefined on HIB-continuity 2026-08-05 (project map section 2); 42 passages remain, all of the debate, which is history (the `passage` table is kept as history, not used by the current study). The section is rewritten without the passage register as a live mechanism. |
| prog_anchor_verse | amend | Same figures; the mechanism is history. |
| prog_data_dimensions | rewrite | Five-stage cluster-reading pipeline, retired (`cluster_subgroup` use text; #2228). |
| prog_data_questions | amend | The catalogue is prompts, never answers to force (#2268 R17). |
| prog_data_synthesis | rewrite | Stage 5 "char-synergy" of the cluster pipeline. Stage 5 is now the claim formulation, not yet decided. |
| prog_data_prose_store | amend | Omits the glossary and the `ApplyPatch` step in `Prose.ps1`. |
| prog_data_obslog_pipeline | amend | Heading and body disagree; the debate writers are retired. |

### Chapter 5: integrity and governance

| Section | Verdict | Evidence |
|---|---|---|
| prog_validation_standard | amend | Missing: compliance check, session-close checks, Spine-Check, thread audit. |
| prog_delete_discipline | keep | Consistent with B:51, B:130. |
| prog_field_authority | amend | Mechanism right; names `finding`. |
| prog_backup_discipline | amend | Named snapshots (`iba/app/db/snapshots/kept/`) not described. |
| prog_patch_failure_protocol | keep | Matches `cfg_on_fail`. |
| prog_instruction_override_protocol | amend | Cites `CLAUDE.md` section 10; the file now holds pointers only. |
| prog_doc_impl_alignment | amend | Missing the control map (`cfg_control_home`), rule 135, B:99. |

### Chapter 6: instruction corpus

| Section | Verdict | Evidence |
|---|---|---|
| prog_instr_global_rules | rewrite | `CLAUDE.md` is now a pointer file; rules print at `/start-project`. |
| prog_instr_reference | keep | Points to `cfg_enum`, `cfg_column` and the config report. |
| prog_instr_patches, prog_instr_directives | amend | The authoritative documents named are in `Workflow/Instructions/archive/`. |
| prog_instr_claudecode | rewrite | `/start-project`, `Start-Iba.ps1` and point-of-use rules now do this work. |
| prog_instr_registry_guide | keep | States honestly there is none. |
| prog_instr_session_a, session_b_readiness, session_b_output, session_c, session_d, verse_context, dimension_review | rewrite | Each body says "no live process" or names a retired mechanism. Retired content is removed (standard 1); what now plays those roles is written under the labels the study uses (standard 3). No new section type is invented; if the existing types cannot carry a subject, that is raised as a finding with the evidence, not put as a question about labels. |

### Glossary and pointers

| Part | Verdict | Evidence |
|---|---|---|
| Programme glossary | amend | Has collection, surface, surface group, observation, node, subgroup, base, face, verse lexical, layer, stage. No entry for claim, engagement or narrative. `cluster` is defined only as M-code cluster. 87 of 107 are drafts. |
| `cfg_prose_concept` | amend | All 8 resolve; they name cluster-era terms; none for collection, the layered reading, the node and observation model or the narrative. |

## 4. Checked facts that are errors in the text today

1. The two instruction documents named authoritative in chapter 6 are in `Workflow/Instructions/archive/`.
2. `prog_instruction_override_protocol` cites `CLAUDE.md` section 10; the file has no numbered sections.
3. `prog_instr_global_rules` describes `CLAUDE.md` as a compact rule reference; the file says it holds pointers only.
4. Row counts in chapters 4 and 5 differ from the live tables.
5. `prog_data_database` says twenty `cfg_` tables; the database holds 43.

## 5. Order of work

The researcher pre-approved changes on 2026-11-19. Order: the project map checked by the researcher; chapters 1 and 2; chapter 4, then 5, 3, 6; the glossary entries for claim, engagement and narrative, then the `cfg_prose_concept` pointers. Each step goes through `Prose.ps1` (dry run, then `ApplyPatch`), sections entering as draft.

## 6. What remains for the researcher

Nothing in this version is put to the researcher as a question of vocabulary, the science pass, the passage register or Claude's role: points A, B, C and D of v1 are settled by the researcher's review and by the record (section 3). Items the record cannot place from evidence are named in section 3a and are raised with the evidence searched.
