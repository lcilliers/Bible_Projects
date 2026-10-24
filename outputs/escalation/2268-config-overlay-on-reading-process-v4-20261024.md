# #2268 The config overlaid on the new analytic process: gaps and conflicts (v4)

**Date:** 2026-10-24 · **Escalation:** #2268 · **Status:** findings only. Nothing has been changed.

Researcher, chat 2026-10-24 (verbatim): *"So now overlay this extract onto the new analytic process and show gaps and conflicts.  I can already see several configs that actually refers to a previous era, although the rules may be correct, the wording and alignment no longer fits."*

**What this version covers.** It includes gap discovery and gap analysis (§2.GAP) and the observation record (§2.OBS), following the researcher's correction of 2026-10-24. **v3** follows the rulings R1 to R3:
- §0 maps the reading process's steps (N0 to N10) onto the phases of `outputs/escalation/2268-analytic-process-and-reading-plan-v1-20261024.md`;
- C1 and C2 are settled;
- C25, C26 and P32 are added;
- D1 to D3 in §6 are now phases of the process, and the passage method is retired.

**v4** applies the rulings on R3a to R3d, R4 and R7 to R12, and adds §8.

**Read §2.OBS and §6 with this caution.** They treat `ib_observation` as one record under one rule set. It holds two bodies of work, the September catalogue work and the October ledger work, each with its own method (`outputs/escalation/2268-ledger-work-and-observations-v1-20261024.md`). C17 to C19 and C22 are restated on that footing in the rulings review v4 (R14, R15, R19).

Earlier versions are in `outputs/escalation/archive/`.

## 0. The reading process's steps, on the phases

| Step (`Reading.ps1`) | Phase | What changes under the phases |
|---|---|---|
| N0 Anchor | 0.C | the reading's purpose is stated (P1) |
| N1 Scope | 0.C | a cluster is segmented, not read whole (R2) |
| N2 What is known | 0.GAP pre | at quality depth, not presence; gathers work already done (RO3, RO5) |
| N3 Gap JSON | 0.GAP pre | gaps written into the tables (R13), not only the file |
| – | D1, D2, D3 | table readings before any verse is read; no step in `Reading.ps1` today (C26, P32) |
| N4 Read and record | D4 observe | every word's role and every significance, per verse in its passage (RO2) |
| N5 Gate 1 | D4 observe | a quality check (guide §7), not presence |
| N6 Synergy | D4 claims, with 0.GAP post | one read (RO7) |
| N7 Apply | D4 claims and narrate | |
| N8 Gate 2 | D4 claims, with 0.GAP post | gaps closed or opened recorded |
| N9 Publish | Publish | |
| N10 Account | Publish | |

The tables of §2 below keep their N-step headings; read each against this map.

**Sources.**
- The adjusted process: `outputs/escalation/2268-analytic-process-and-reading-plan-v1-20261024.md`.
- The inventory: `outputs/escalation/2268-analytic-process-config-inventory-v3-20261024.md`.
- The observation rules document: `iba/docs/ib-observation-governing-rules-checklist-v1-20260916.md`.
- The coverage and lifecycle code: `iba/app/lib/stage1coverage.py`, `clusterstatus.py`, `versemeta.py`, `recordingpass.py`, `threadaudit.py`.
- The new process as designed: `outputs/escalation/2228-reading-process-design-v2-20261023.md`.
- The new process as built: `iba/app/lib/reading.py`, `versescope.py` and `versecollate.py`.
- Live rows of `iba.db`, read-only.

**The verdicts used:**
- **Fits:** the wording and the target match the new process.
- **Era:** the rule's substance may be right, but it speaks of a previous way of working (strands, ledgers, units, `_analytics` reading files, chapter files, LLM generator stages, debates), so its wording and alignment no longer fit.
- **Conflict:** it contradicts the new process or another config row, and both sides are named.
- **Gap:** the new process has a step that no config governs.

"Not delivered" means the rule does not reach the step's tool (inventory §0.1).

## 1. In short

| | Count | Where |
|---|---|---|
| Rows marked Fits | 26 | across the steps (§2), not counting §2.GAP and §2.OBS; some rows group several settings, and B:114 and E:16 appear at two steps |
| Era wording (rule substance may stand) | 37 | W1 to W37 (§4); W32 and W33 are from the guide plotting |
| Conflicts | 26 | C1 to C26 (§3); C15 is from the guide plotting; C1 and C2 are settled by R2 and R1 |
| Gaps | 32 | P1 to P32 (§5); P16 to P22 are from the guide plotting |
| Phases D1 to D3, and the retired passage method | 4 | 100 method rules and 18 quality checks, none delivered (§6) |

**The two v2 findings in brief.**
- **Gaps.** The study finds gaps in seven places that no config relates to one another:
  - a reading's gap JSON;
  - the collation's presence test;
  - `verse_meta.status`;
  - Stage 1 coverage;
  - `cluster.status`;
  - the file index;
  - the narrative register and the thread audit.

  No config says what a gap is study-wide. No table records a gap or its state, and nothing measures "enough".
- **The observation record.** One table, `ib_observation` with its grounding `ib_node`, is written by eight steps along two write paths that follow different rules. Its rule set is a document (the checklist), not config. Its status values mean one thing in config and another at gate 2, and it has no status flow and no change history.

Most of the study's rules were written for the strand and ledger era (October), and some for the LLM-generator era (September) or the passage-debate era (August). The reading process replaced the strand steps (#2228 D-a) but no rule was reworded for it. A reading never sees the rules worded for strands, because they are delivered only on `_analytics/**` (inventory §0.1).

## 2. The overlay, step by step

The new process (from #2228 design v2 and the code). Open items run across all of it.

| Step | What happens | Tool |
|---|---|---|
| **N0** Anchor | a reading opened with a label, an anchoring escalation and a home cluster | `Reading.ps1 -Step Open` |
| **N1** Scope | selectors resolved to verses; size and time guards | `versescope` |
| **N2** What is known | per verse: text, M-code words, draft observations, strand hits, claims, blocks, matched open items, file lines, lexicon | `versecollate`, `Reading-Index.ps1` |
| **N3** Gap JSON | one section per recording gap type, each with its guide | `reading.gap_types` |
| **N4** Read and record | observations, faces on strand hits, responses on open items, new open items | `Reading.ps1 -Step Record` |
| **N5** Gate 1 | every item has a row or a reason; verses marked `analysed` | `Reading.ps1 -Step Check` |
| **N6** Synergy | the synergy JSON built from the tables | `Reading.ps1 -Step Synergy` |
| **N7** Apply | claims new, edited or withdrawn; observation dispositions; tellings; holds; blocks rewritten; open items settled | `Reading.ps1 -Step Apply` |
| **N8** Gate 2 | every observation carried or disposed, every claim told or held, every matched item settled | `Reading.ps1 -Step Check` |
| **N9** Publish | the touched chapters published from the database, copied to the learning4comfort inbox, checked byte-identical | `Reading.ps1 -Step Publish` |
| **N10** Account | the reading read back from the tables | `Reading.ps1 -Step Account` |
| **X** Open items | matched at N2, read at N4, settled at N7 | `Open-Item.ps1`, `Escalation.ps1` |

### N0 Anchor and purpose

| Config | Verdict | What does not fit |
|---|---|---|
| `governance.study_status` | Fits | names `Reading.ps1` and its gates |
| `governance.programme_stages` | Fits | names the old Session A to D labels only as former names |
| B:84 fan-out-progressive-strands | Era, Conflict | the strand is the unit, where the new unit is a reading of a scope (W1); "no backfill of earlier work" and "no cluster reading is started as such" (C1) |
| `cfg_control_home` study_method | Conflict | the method's home is `Workflow/Instructions/` files (C2) |
| `cfg_control_home` study_state | Era | "strand escalations" and "the reading_strand tables" (all four strands superseded); it does not name `reading` or `reading_verse` (W2) |
| `cfg_control_home` study_output | Era | names `outputs/strand-reading/` (retired) and not `outputs/reading/` (W3) |
| (none) | Gap | a reading records no purpose or question (P1), and no row says which reading route applies (P2) |

### N1 Scope

| Config | Verdict | What does not fit |
|---|---|---|
| B:113 bare Strong's decomposed | Fits | delivered at `Verse-Scope.ps1` and `Reading.ps1` |
| `verse_scope.*` (3) | Fits | |
| B:111 filters are working aids | Fits | not delivered |
| B:95 verse sets only through the raw layer | Era | "a strand's verse sets" (W4); not delivered |
| B:94 gloss scan across codes before a theme | Era, Gap | "before a theme is read … no strand ever pulled" (W5); no tool scans glosses across codes for a scope (P3; #2235 on hold) |
| B:93 strand checks its M47 verses | Era, Gap | "for each strand as it is taken up … the record is on OT-09" (W6); no step of the new process carries the inner-seat check (P4) |
| B:110 surface is the sensitivity lens | Era, Gap | "in any strand or word pull" (W7); the scope and collation give no surface-per-Strong's table (P5) |
| B:91, B:116, B:73: read the verse in its whole passage | Conflict | the scope holds only the verses selected, and the passage is left to "a judgement call made outside this tool" (`versescope.py` docstring) (C3) |
| E:16 thread check before work | Fits | open items are also matched at Open |

### N2 What is known

| Config | Verdict | What does not fit |
|---|---|---|
| B:114 synergise from the tables | Fits | delivered |
| B:71 reuse what is already extracted | Era | "the strand folder's existing pulls", "ledgers, face-combination CSVs" (W8); its point (2), the set-based M-code link, is what `versecollate` does; not delivered at `Verse-Collate.ps1` |
| `reading_index.roots` | Era | indexes "the origin-of-thought strand folder, so the verses its October ledger cites come up" (W9); a deliberate bridge (#2216), but worded for strands |
| `versecollate.py:82` (code), reading only `status='draft'` observations | Conflict | gate 2 moves observations to `open`, `resolved` or `silent` (`set_disposition`). Those then drop out of what is known at the next reading, and their verses can come up as "not read" again. Today 80 `strand-reading` observations are `resolved` and 31 `open` (C4) |
| (none) | Gap | the passage method's tables (`hib`, `phenomenon`, `operation`, `passage_*`) are not collated, so readings made by route D3 are invisible to a reading (P6) |
| (none) | Gap | no T-codes, meaning text, LSJ text or renderings across verses (finding 5 of the findings file) (P7) |
| B:61 inactive is never an active input; `reading_strand` all superseded | Era | strand hits of four superseded strands still come up as `hit_unread` gaps (W10) |

### N3 Gap JSON

| Config | Verdict | What does not fit |
|---|---|---|
| `cfg_enum reading_gap_type` | Fits | |
| `reading.gap_types` | Era, Gap | the guide reads "no observation and no strand face", and a whole gap type (`hit_unread`) serves superseded strands (W11); no gap type looks at the quality of what is recorded: role, single verse, Stage 1 coverage (P8) |

### N4 Read and record

| Config | Verdict | What does not fit |
|---|---|---|
| B:116 read the verse first | Fits | delivered |
| B:4 inferential, not confirmed | Fits | the record's `basis` (`read` or `stated`) carries it |
| B:37 derive from the instruction document | Fits | the "instruction document" is a Workflow file (C2) |
| B:73 read by the role of each M-code word | Era, Conflict | written for strands: "a strand pulls verses", "the strand's own word", "each strand's read-back" (W12); its `enforced_by` names guide v1 (`…-v1-20261011.md`) while its text names v2 (C5); not delivered |
| B:72 route verses A, B, C | Era, Gap | "each verse in a strand … recorded in the ledger" (W13); the record has no route field (P9) |
| B:69 let Scripture speak | Era | "a new insight … goes to the strand ledger first" (W14), where it now goes to an observation; not delivered |
| B:70 cluster tags are loose | Era, Gap | "records that association in its ledger" (W15); the record has nowhere to put a cross-cluster association (P9) |
| B:89 change of character recorded | Era, Gap | "every strand records each word's faces"; the ledger file is `_analytics/cross-cluster-web/origin-of-thought/…change-of-character-*` (W16); faces are kept only on `reading_strand_hit`, a table of superseded strands, so faces have no home (P10) |
| B:109 read verses before asking | Era | "whether a word belongs in a strand" (W17); its substance fits |
| B:79 a placement for every verse in a reading file | Era, Conflict | placements in reading, ledger and weave files under `_analytics` (W18). A reading's record is now its JSON under `outputs/reading/`, and session-close SC5(d) checks only `_analytics` files. Two vocabularies cover one job: `session_close.placement_kinds` (told, claim, data, forward, held, parked, context) and gate 2's dispositions (claim; held on an item; silent; withdrawn; told; hold) (C6) |
| B:68 Stage 1 corrections only through a real rerun | Conflict | an observation is corrected only by `record_one_observation` from a fresh LLM answer. `Reading.ps1` Record writes observations by `record_strand_observations` (Claude's reading, with `supersedes` withdrawing the earlier row), and gate 2 changes their status by `set_disposition` (C7) |
| `ib_observation.tag_guidance` | Era, Gap | "given to the model by every LLM-calling generator stage" (W19); not given to a reading, and `key-statement` has no entry (#2263) (P11) |
| `cfg_enum ib_observation.stage` `strand-reading` | Era | the stage of retired steps, written by every reading (#2264) (W20) |
| `strand_reading.output_dir` | Era | the setting of a retired work package, still live (W21) |
| `report.cluster_folder_naming_convention` | Conflict | "ALL output relating to a cluster (analysis, readings …) is filed in that cluster's subfolder", where `reading.output_dir` files every reading under `outputs/reading/<label>` (C8) |
| `cfg_method_rule`, `cfg_quality_check` | Gap | no row for any `reading.*` step: the observation rules sit only on route D1 and D2 steps (P12) |

### N5 Gate 1 and N8 Gate 2

| Config | Verdict | What does not fit |
|---|---|---|
| `cfg_enum verse_meta_status` (analysed, citated) | Fits | |
| (none) | Gap | no quality check for either gate; both measure presence (P13) |
| B:92 no unnecessary holding | Era | "while the strand is busy with them" (W22); no gate measures a hold against it |

### N6 Synergy

| Config | Verdict | What does not fit |
|---|---|---|
| B:114 | Fits | |
| (none) | Gap | the synergy JSON gives an observation's text and meaning only, not its setting, implication, chain, parties, basis or tag (P14) |

### N7 Apply

| Config | Verdict | What does not fit |
|---|---|---|
| B:76 claim register kept in iba.db | Fits | names `Reading.ps1 -Step Apply` |
| B:112 narrative is story, claims are derived | Fits | not delivered |
| B:91 narration probes, not restates | Fits | not delivered |
| B:77 claims register keeps the narrative honest | Fits, Era | text fits; `enforced_by` names `Narrative-Register.ps1 Record` (a retired step), a one-off life-death cross-check script, and CLAUDE.md (W23) |
| B:86 narrative reset and weave record | Conflict | "the narrative is … in chapter files under `_analytics/…`; each strand updates the chapter files it touches (version bump) … `Narrative-Register.ps1 -Action Record`" (retired). `governance.narrative_home` says the narrative is the blocks in iba.db, the files are exports, "never in a chapter file" (C9) |
| B:85 prose only on instruction | Conflict | "Claude writes no prose (… a narrative chapter file) without a specific instruction", where gate 2 rewrites narrative blocks as routine reading work (C10) |
| B:72, last sentence | Conflict | "Routing a strand's verses into the narrative waits for the researcher's direction", where gate 2 requires every claim told or held (C11) |
| B:87 chapter text rules | Era | "unchecked original material stays in marked Held sections" of the chapter text (W24); claims now carry `held`, and quotes are checked by `narrative.quote_min_words` |
| B:88 weave, not fit | Era | "every observation from a strand gets a recorded placement" is gate 2's cross-reference; "Method: `_analytics/essay/…weave-method…*`" is a file authority (W25) |
| B:90 weaving carries meaning | Era, Gap | "applies … the ledger work"; "full verse lists stay in the ledger" (W26). There is no ledger now, and no config says where a phenomenon's full verse list lives (P15) |
| B:69 (narrative half) | Era | not delivered (W14) |
| `narrative.inner_being_style_guide_path` | Era | its use names "strand write-ups, book narratives" (W27); the style authority is a file (C2) |
| `narrative.*` paths under `_analytics/essay/` | Fits | they are the exports |

### N9 Publish and N10 Account

| Config | Verdict |
|---|---|
| B:78 chapters change only through the register | Fits |
| `narrative.copy_source_dir`, `narrative.learning4comfort_inbox_dir` | Fits |
| `governance.no_direct_github_publish` | Fits |

### X Open items and threads

| Config | Verdict | What does not fit |
|---|---|---|
| B:115 open item has a clear purpose | Fits | delivered |
| E:16, E:18 | Fits | |
| `open_item.*` (3) | Fits | |
| B:74 open threads carried as escalations | Era | "moves only when a strand reaches it", "before every unit pull of a strand", "raised as threads at every ledger approval" (W28); a reading now matches items at Open and settles them at gate 2 |
| `escalation.worked_strand_escalations` | Era | the thread audit (T-d) counts a *strand* as worked; readings are not counted (W29) |
| `escalation.thread_register_path` | Fits | a generated file under `_analytics/cross-cluster-web/` |

### Rows outside the steps

| Config | Verdict | What does not fit |
|---|---|---|
| B:13 don't assume which database | Conflict | "bible_research.db (prose + analytic findings)", where `governance.scope_research_db` says "prose-only … findings fully owned by iba.db" (C12) |
| `governance.scope_iba_db` | Conflict | "a few analysis tables (debate/passage control) are expected to migrate back to research_db", against `governance.scope_research_db` "prose-only" (C13) |
| B:7, B:8, B:9: cost cap, usage log, model | Era | each `enforced_by` verifies `narrative.generate` (retired; its settings inactive). The live API call sites are `lexical.meaning`, `lexical.relational` and `cluster.*` (`lexical.llm_*`), whose enforcement is not recorded (W30) |
| `governance.past_precedent_investigation_signals_missing_config` | Fits | its use text cites a debate-era incident as origin only |

### §2.GAP Gap discovery, updating and gap analysis

The reading process discovers gaps only for its own scope (N2, N3) and closes them at its gates (N5, N8). Around it, six other mechanisms each measure "not yet read" or "not yet complete" their own way.

| Where a gap is found | What counts as a gap | How it is updated | Config | Verdict |
|---|---|---|---|---|
| A reading's gap JSON (`reading.py` Open) | per verse in scope: not read, read in files only, strand hit unread, meaning missing, open item; at gate 2: observed with no claim, claim not told | the item gets a row id or a reason; the file is the record | `reading.gap_types`, `cfg_enum reading_gap_type` | Fits as a per-reading list; Era (W11); presence only (P8) |
| The collation (`versecollate.py`) | a verse with no `draft` observation and no strand face is "not read" | recomputed each run | none (in code) | Conflict C4 (draft only); presence only |
| Verse coverage marks (`verse_meta.status`) | NULL is not read; `analysed` is gate 1 passed; `citated` is cited in a rewritten block; `exclude` | gate 1 and Apply (`versemeta.mark`), or `VerseMeta.ps1` | `cfg_enum verse_meta_status`; `cfg_column verse_meta.status` | Conflict C20 (written by application code); 4,008 analysed, 32 citated, 25,722 not set |
| Stage 1 coverage (`stage1coverage.py`) | an expected verse, strong and question triple with no live `verse-reading` node (MISSING), a node not expected, a duplicate | recomputed after each `lexical.meaning` / `lexical.relational` run; report per run | `report.stage1_coverage_validation_pattern`; method rules 123, 125 | route D1 only; not related to a reading (C23) |
| Cluster lifecycle (`clusterstatus.py`) | a cluster advances past `t_cluster_assignment_completed` only when every member strong has `verse-reading` coverage | on each D1/D2 run | `cfg_enum cluster.status`, `cluster_subgroup.status`; method rules 77, 118, 123 | 92 of 95 clusters still at that first status; a reading neither reads nor moves it (C23) |
| Per-strong traceability and per-question completeness | every occurrence cited; every battery question answered | after each D2 write | method rules 96, 107 | route D2 only |
| The file index (`Reading-Index.ps1`) | a verse named in a study file with no observation | rebuilt when a file's hash changes | `reading_index.*` | Era (W9); a bridge to the old files |
| The spine and readiness | a strong with no meaning; a verse with no span | `Spine-Check.ps1`, `lexical.readiness` | `spine.*`, method rules 68, 69, 126 | Fits (base data) |
| The narrative register | "a verse in neither the narrative nor the register is a missing reading area" (B:77) | `Narrative-Register.ps1 -Action Find -NotInNarrative`, on demand | B:77 | no step runs it as part of a reading (P24) |
| Open items and threads | items not worded, past their review age; thread audit T-a to T-g | `Open-Item.ps1 -Action Review`; `Escalation.ps1 -Action ThreadAudit` at start | `open_item.review_age_days`, `escalation.worked_strand_escalations` | T-d counts strands (W29) |
| Inner seat and gloss scans | M47 verses dropped by word; theme words in uncoded T-codes | none | B:93, B:94 | no tool (P4, P3) |

**What no config governs (gaps P23 to P25, P31):**
- **P23:** a study-wide definition of a gap. `reading_gap_type` covers one reading, and the other measures are separate.
- **P24:** a study-wide gap analysis: what is unread or below the rules across the whole study, by word, cluster, chapter or thread. No step produces it. B:114 says "the gaps are recorded into the tables", but there is no table of gaps.
- **P25:** a sufficiency measure: when a verse, a word, a scope or a cluster has been read enough.
- **P31:** how a gap is reopened. When an observation is withdrawn, or found short of the rules (#2265 to #2267), nothing marks its verses unread again. `verse_meta.status` `analysed` stays.

### §2.OBS The observation record: `ib_observation` and `ib_node`, end to end

**The record.** An observation is one row in `ib_observation`: its text, meaning, stage, tag, window, meaning source, status, basis, parties, setting, implication and chain. It is grounded by one or more `ib_node` rows, each on a verse, strong, surface and morph, and optionally on a cluster, subgroup, catalogue question or another observation. B:84 calls `ib_node` "the central linkage", and the checklist §0.8 says "everything can relate to anything, but only on evidence".

**Live state.**

`ib_observation`, by stage:

| Stage | Rows | Written by |
|---|---|---|
| `verse-reading` | 10,595 (4,953 withdrawn) | route D1 |
| `char-answers` | 748 | route D2 |
| `char-reading` | 118 | route D2 |
| `char-subgroup` | 19 | route D2 |
| `strand-reading` | 773 | the reading process and the #2172 catch-up |

`ib_node`: 16,901 rows. 10,595 `verse-reading` and 748 `char-answers` observations carry a catalogue question. No `strand-reading` observation carries a question code, a window or a meaning source.

| Part of the process | What happens | Config | Verdict |
|---|---|---|---|
| Who writes | eight steps (`cfg_write_grant`): D1, D2, the reading's Record and Apply, the enhancer | `cfg_write_grant` | Fits as grants |
| The write path, API routes | `record_one_observation`: the recording pass decides same / broaden / new by text similarity; verses resolved fresh; tag, stage, question code validated | checklist §0.1 to §0.5; `cluster.recording_similarity_threshold`; B:68 | the checklist is a document (P26) |
| The write path, the reading | `record_strand_observations`: Claude's observation is written as given; `supersedes` withdraws an earlier row; no similarity match; stage `strand-reading`, tag `key-statement` | none specific | Conflict C19 with checklist §0.2 and B:68 (C7) |
| Grounding | one `ib_node` per verse and strong given | checklist §0.7 (coverage checked twice) | the reading does no coverage check (P29) |
| Stage | six values | `cfg_enum ib_observation.stage`; `cfg_column` use lists five; `cfg_table` use names the retired `strand_reading.record` / `derive` as writers | Conflict C17; Era W35 |
| Node source stage | live values are the five stage names | `cfg_column ib_node.source_stage`: "reading / answer / synthesis" | Conflict C16 (a correction) |
| Tag | 21 values; definitions given to the LLM stages | `ib_observation.tag_guidance`, `tag_stage_excluded` | Era W19; P11 |
| Window, meaning source | from the catalogue question; the three meaning sources | `cfg_enum ib_observation.window`, `meaning_source`; method rules 70, 88, 113 | the reading fills neither (P9, guide §4.6a) |
| Catalogue question | `question_code` on observation and node | `wa_obs_question_catalogue` (116 rows, in iba.db); its `cfg_table` use says 92 rows and an FK "not enforced yet … once write paths are built (Phase F)" | Era, Conflict C21; the reading answers no catalogue question |
| Status | six values: draft, needs-corroboration, open, silent, withdrawn, resolved | `cfg_column ib_observation.status` (#1782): `resolved` = "cleared for inclusion in analysis"; `open` = "no current writer … pending the researcher's call on whether to retire it" | Conflict C18 with gate 2, which uses `resolved` for carried by a claim and `open` for held on an item; no status flow (P27) |
| Correction | D1: only through a fresh LLM answer (B:68); the reading: `supersedes` and dispositions; the enhancer: rule-based bulk updates | B:68; `cfg_observation_enhancer_rule` (2 rules) | C7, C19; no change history on either table (P28) |
| Synthesis | checklist §4: a synthesis observation is append-only, carries `revisit_note`, traces to what it was read from; stage `char-synergy` | `cfg_enum` stage `char-synergy` (no writer); no status `superseded` | gate 2 is the synergy, but it writes claims, not synthesis observations (P30, C22) |
| What "read" means | an observation's presence | none | C23 |
| The home of an observation | `ib_observation.cluster_code` = the reading's `home_cluster`, for every observation of the reading | `cfg_column reading.home_cluster` | Conflict C24 with the guide §4.8 ("the home follows the main operation", per verse) |

**The observation rules live in a document.** `iba/docs/ib-observation-governing-rules-checklist-v1-20260916.md` calls itself "every rule governing the production or recording of an `ib_observation`/`ib_node` row, at any stage, in one place". It says it "goes stale the moment a decision is made elsewhere and not added here". It was written for routes D1 and D2 and has not been updated since 2026-09-16: it knows no reading process and no `strand-reading` stage. Its cross-cutting section 0 is not held by any config row, except in part:
- §0.4 iba.db only: B:67;
- §0.5a and §0.5b, flags carried, not resolved inline: method rules 74, 104 and 116, on D1 and D2 steps only;
- §0.6, can't-resolve recorded: the tag `could-not-resolve`.

The rest is not held anywhere: §0.1 single writer, §0.2 the recording pass decides edit or new, §0.3 run structure, §0.5 verses resolved fresh, §0.7 node coverage checked twice, and §0.8 relations only on evidence (P26).

## 3. Conflicts (C1 to C26)

C1 is settled by R2 (B:84 retired and replaced by configs; backfill becomes gathering work already done). C2 is settled by R1 (rules in config; a file is the authority only for the programme and inner-being definitions, with a config pointer). Both stay listed until the design carries them out.

| # | One side | The other side | Needs |
|---|---|---|---|
| C1 | B:84: no backfill of earlier work; no cluster reading started as such | the `read_in_files_only` gap type and `reading_index.roots`, built to carry the October file readings in (#2216 option B); the #2172 catch-up; the home cluster each reading needs; the per-cluster routes D1 and D2 | your ruling on what B:84 now means |
| C2 | `governance.rules_must_be_config_driven` | `cfg_control_home` study_method (home: `Workflow/Instructions/` files); B:73, B:88 and 3 settings name a file as the method authority | your ruling: the method moves into cfg rows, or the control map keeps files as its home |
| C3 | B:91, B:116, B:73: the verse is read in its whole passage | the scope and gap JSON hold only the selected verses; the neighbour-verse review was left outside the tool | design |
| C4 | gate 2 dispositions (`open`, `resolved`, `silent`) | `versecollate.py:82` reads only `draft` observations | code fix (execution against the settled design) |
| C5 | B:73's text names guide v2 | B:73's `enforced_by` names guide v1 | config correction |
| C6 | B:79 placements, `session_close.placement_kinds`, SC5(d) on `_analytics` files | gate 2's dispositions and tellings, recorded in tables and the reading JSON | your ruling: one vocabulary |
| C7 | B:68: observations corrected only through a fresh LLM answer | reading Record (Claude-written, `supersedes`) and gate 2 `set_disposition` | your ruling on B:68's scope (Stage 1 only?) |
| C8 | `report.cluster_folder_naming_convention`: all cluster readings in the cluster folder | `reading.output_dir`: `outputs/reading/<label>` | your ruling |
| C9 | B:86: the narrative is chapter files, updated by strands through `-Action Record` | `governance.narrative_home`: the blocks in iba.db, files are exports | B:86 reworded to the narrative home |
| C10 | B:85: Claude writes no narrative without a specific instruction | gate 2 rewrites blocks as routine reading work | your ruling: does opening a reading under an escalation give that instruction? |
| C11 | B:72: routing a strand's verses into the narrative waits for your direction | gate 2 needs every claim told or held | your ruling, with C10 |
| C12 | B:13: bible_research.db holds analytic findings | `governance.scope_research_db`: prose only | config correction |
| C13 | `governance.scope_iba_db`: debate tables to migrate to research_db | `governance.scope_research_db`: prose only | your ruling |
| C14 | the four reading routes D1 to D4, each writing observations its own way | no row relates them (§6) | your ruling |
| C15 | the `not_read` gap guide ("the reason it holds nothing") and gate 1's 10-character reason | role guide §4.9: never close on "not X" (guide plotting) | design |
| C16 | `cfg_column ib_node.source_stage`: "reading / answer / synthesis" | the live rows: the five stage names | config correction |
| C17 | `cfg_column ib_observation.stage` lists five stages; `cfg_table ib_observation` names `strand_reading.record` / `derive` as writers | `cfg_enum` has six stages (with `strand-reading`); the live writers are `reading.record` and `reading.apply` | config correction, after R14 |
| C18 | `cfg_column ib_observation.status` (#1782): `resolved` = cleared for inclusion in analysis; `open` = set by no writer, pending your call on retiring it | gate 2 (`set_disposition`): `resolved` = carried by a current claim; `open` = held on an open item | your ruling |
| C19 | checklist §0.1 and §0.2: only the recording pass writes, and it decides edit or new | the reading's Record: Claude's observation written as given, Claude choosing `supersedes`, no similarity match | your ruling, with R6 |
| C20 | `cfg_column verse_meta.status`: researcher-set, "written only by VerseMeta.ps1 -Step SetStatus, never by application code" | gate 1 marks `analysed` and Apply marks `citated` (`cfg_write_grant` `reading.check`, `reading.apply`; #2228 D-c) | config correction (D-c is your ruling) |
| C21 | `cfg_table wa_obs_question_catalogue`: 92 rows, FK not enforced until "Phase F" write paths are built; `cfg_column` question_code: "restore once #1696 lands" | the catalogue has 116 rows in iba.db, and the write paths are built | config correction; FK a design point |
| C22 | checklist §4.2: a superseded synthesis observation takes status `superseded` | `cfg_enum ib_observation.status` has no `superseded`; `supersedes` sets `withdrawn` | your ruling, with R14 |
| C23 | four measures of "read": collation presence, `verse_meta` `analysed`, Stage 1 coverage, `cluster.status` | none relates them; a verse can be "read" by one and not by another | your ruling |
| C24 | the reading: every new observation homed in the reading's `home_cluster` | the role guide §4.8: a verse's home follows its main operation | your ruling |
| C25 | R1: "No operating rule should be hard coded in scripts" | rules in the reading's code: the gap kinds (`versecollate.py:24`, beside `reading.gap_types`); `draft` as the only status that counts as read (`versecollate.py:82`); M-codes only (`versecollate.py:70`, which keeps T-codes from a reading); Mounce for Greek only (`reading.py:198`, `versecollate.py:182`); a 10-character minimum reason or response (`reading.py:292`, `307`); the settle kinds and read-in-part mark (`reading.py:53`, `54`); the reading's stage and tag (`recordingpass.py:571`) | config rows, in the design |
| C26 | the phase order: table phases D1 to D3 before any verse text is read (D4) | `Reading.ps1` goes from the gap JSON straight to reading verses (gate 1); no step reads the scope's word-level, characteristic or claim data first | design |

## 4. Era wording (W1 to W37)

Each of these is a rule or setting whose substance may still be right, but which speaks of a way of working that has been replaced.

| # | Config | Speaks of | Would speak of |
|---|---|---|---|
| W1 | B:84 | a strand as the unit of analysis | a reading of a scope |
| W2 | `cfg_control_home` study_state | strand escalations, the `reading_strand` tables | readings (`reading`, `reading_verse`) |
| W3 | `cfg_control_home` study_output | `outputs/strand-reading/` | `outputs/reading/` |
| W4 | B:95 | a strand's verse sets | a reading's scope |
| W5 | B:94 | a theme pulled by a strand | the scope of a reading |
| W6 | B:93 | each strand taken up; OT-09 | each reading (or its retirement) |
| W7 | B:110 | a strand or word pull | the scope and collation |
| W8 | B:71 | strand folder pulls, ledgers, face CSVs | the collation and the tables |
| W9 | `reading_index.roots` | the origin-of-thought strand folder, the October ledger | the file readings still to be carried in |
| W10 | B:61 against `reading_strand_hit` | hits of superseded strands as live gaps | |
| W11 | `reading.gap_types` | "no strand face"; `hit_unread` | |
| W12 | B:73 | a strand pull, the strand word, each strand's read-back | a reading and the words of its scope |
| W13 | B:72 | each verse in a strand, recorded in the ledger | each verse of a reading, recorded in a table |
| W14 | B:69 | the strand ledger first | an observation first |
| W15 | B:70 | the association recorded in the ledger | |
| W16 | B:89 | every strand records faces; the ledger file | |
| W17 | B:109 | whether a word belongs in a strand | |
| W18 | B:79 | reading, ledger and weave files of a strand | |
| W19 | `ib_observation.tag_guidance` | LLM-calling generator stages | every route that records observations |
| W20 | stage `strand-reading` | retired steps | (#2264) |
| W21 | `strand_reading.output_dir` | a retired work package | |
| W22 | B:92 | while the strand is busy | while the reading is open |
| W23 | B:77 `enforced_by` | the `-Action Record` step, a one-off script, CLAUDE.md | the gate 2 check |
| W24 | B:87 | Held sections in chapter text | held claims |
| W25 | B:88 | an observation from a strand; a method file | gate 2 |
| W26 | B:90 | ledger work; verse lists in the ledger | |
| W27 | `narrative.inner_being_style_guide_path` | strand write-ups, book narratives | |
| W28 | B:74 | strand reaches, unit pulls, ledger approvals | reading Open and gate 2 |
| W29 | `escalation.worked_strand_escalations` | a strand counted as worked | |
| W30 | B:7, B:8, B:9 `enforced_by` | the retired `narrative.generate` call site | the live `lexical.*`, `cluster.*` call sites |
| W31 | 22 method rules (§6) | "the LLM", "the model", "this build", "Stage 1/2/3", debate scaffold | |
| W32 | the role guide's audience line, §5.1, §5.6d | strands | readings |
| W33 | the role guide's sources | retired memory files; a design doc now in `archive/` | the rules #2184 mapped them to |
| W34 | `cfg_table ib_node` | "the cluster-reading pack's own grounding table … checked at LLM generation time" | every route's grounding |
| W35 | `cfg_table ib_observation` | writers `strand_reading.record`, `strand_reading.derive` | `reading.record`, `reading.apply` |
| W36 | `cfg_column` of `ib_observation` `setting`, `meaning`, `implication` ("October ledger part"), `run_id` ("the Strand-Reading run"), `revisit_note` ("until step C sets the status") | the October ledgers and the strand steps | the reading's record |
| W37 | the checklist document | routes D1 and D2 only ("the LLM", processes b to e) | every route that writes an observation |

## 5. Gaps (P1 to P32)

| # | Step | What no config governs |
|---|---|---|
| P1 | N0 | the purpose or question of a reading |
| P2 | N0 | which reading route applies to which work |
| P3 | N1 | a gloss scan across all codes for a scope (#2235) |
| P4 | N1 | the inner-seat (M47) check by word |
| P5 | N1, N2 | the surface table per Strong's |
| P6 | N2 | the passage method's tables in what is known |
| P7 | N2 | the T-codes, meaning text, LSJ text and renderings given to the reader |
| P8 | N3 | a gap type for observations short of the rules |
| P9 | N4 | the record's fields for main operation, role, bindings, relational and pointer, route, association |
| P10 | N4 | a home for faces now that strands are retired |
| P11 | N4 | tag guidance for a reading, and `key-statement` |
| P12 | N4 | method rules for the reading steps |
| P13 | N5, N8 | quality checks at the gates |
| P14 | N6 | the full observation in the synergy JSON |
| P15 | N7 | where a phenomenon's full verse list lives, once there is no ledger |
| P16 to P22 | N4, N6, N7 | from the guide plotting: faculty; reading every row and T-codes; trial first; the qualifier exception and what a qualifier gives; paired and opposite acts; the qualifier table; the T11 party kind |
| P23 | GAP | a study-wide definition of a gap |
| P24 | GAP | a study-wide gap analysis, and a home where gaps are recorded and kept current |
| P25 | GAP | a sufficiency measure: when a verse, word, scope or cluster is read enough |
| P26 | OBS | the observation rules (checklist §0) in config, for every route, the reading included |
| P27 | OBS | a status flow for `ib_observation.status`: who sets each value, and when |
| P28 | OBS | a change history for `ib_observation` and `ib_node` |
| P29 | OBS, N4 | a grounding coverage check for a reading: every verse and word in scope grounded, or its reason |
| P30 | OBS, N6 | how gate 2's synergy relates to the synthesis stage (`char-synergy`) and checklist §4 |
| P31 | GAP | how a gap is reopened when an observation is withdrawn or found below the rules |
| P32 | all | the phases, their order, and what each reads and does not read (RO1 to RO9 of the process file) |

## 6. D1 to D3 and the passage method against the new process

Under the phases (process file §2), the labels below have new meanings:
- **D1** is the word-level phase (Stage 1);
- **D2** is the characteristics phase;
- **D3** is now the claims-and-characteristics phase. The passage method described as "D3" in the table below is **retired** (R3 feedback), and its rules are to be gathered into D4.

D1 and D2 are table readings that come before D4. Who performs them (the API steps, or Claude in a session) is R3c.

| Route | Era | Method rules / checks | How it relates to the new process |
|---|---|---|---|
| D1 Stage 1 (`lexical.meaning`, `lexical.relational`) | September, LLM generator | 23 rules; rules 71, 74, 111, 112, 114, 116, 120 and 121 speak of "the LLM" or "the model" | its observations reach a reading through `ib_observation` (`draft` only, C4). Its per-cluster scope (rules 72, 115) conflicts with B:84 (C1). Its observation rules (108 to 112, 119 to 121) are the quality bar a reading lacks (P12). Not run for M64 |
| D2 characteristic stages (`cluster.subgroup`, `cluster.reading`, `cluster.answer`) | September, LLM generator | 32 rules; rules 86, 94, 96, 99, 106 and 107 speak of the model or "this build" | reaches a reading through `ib_observation`. Per subgroup, which conflicts with B:84 (C1). Rules 88 and 91 to 95 (three sources, every instance states what it is, difference as its own observation, morph read) bind only here |
| D3 passage method (`hib.set` to `closing.set`) | August, debate | 37 rules (rules 13, 25, 27, 31, 33 and 39 speak of the debate or its phases) and all 18 quality checks; `method.*` document paths | writes `hib`, `phenomenon` and `operation`, which a reading never collates (P6). Its quality checks (warrant, stated or inferred, full lexical range, genuinely inner-being) are the only reading-quality checks in config |

No config row yet says any of this (C14, P2, P32). The R3 feedback settles the direction; R3a to R3d settle the detail.

## 7. What needs your decision before any rewording

The era rewording (W1 to W37) and the config corrections (C4, C5, C12, C16, C20, C21) follow from what is settled. The following are new decisions (B:44) and need your ruling first:

| # | Decision | From |
|---|---|---|
| R1 | **Decided:** rules in config; a file is the authority only with a config pointer (the programme and inner-being definitions) | C2 |
| R2 | **Decided:** B:84 retired and replaced by configs; backfill becomes gathering work already done | C1 |
| R3 | **Repositioned** as the reading definition and the phases; R3a to R3d in the rulings review v3 | C14, P2, C26, P32 |
| R4 | Whether opening a reading under an escalation is the instruction to write narrative (B:85, B:72) | C10, C11 |
| R5 | One vocabulary for where a verse or observation goes (placements, or gate 2 dispositions) | C6 |
| R6 | The scope of B:68 (Stage 1 only, or every observation) | C7 |
| R7 | Where reading output is filed | C8 |
| R8 | Whether the debate tables are to move to research_db | C13 |
| R9 to R12 | The study's terms; the worked cases; the July method file; the guide once carried | guide plotting |
| R13 | What a gap is, study-wide; where gaps are recorded and kept current; when a gap reopens; what "enough" means | P23 to P25, P31, C23 |
| R14 | What each `ib_observation.status` value means now, and who sets it | C18, C22, P27 |
| R15 | One rule set for every observation write (the checklist §0, in config), and how a reading's write fits it | C19, P26, P29 |
| R16 | Where an observation of a reading is homed: the reading's cluster, or the main operation of its verse | C24 |
| R17 | Whether a reading answers catalogue questions (question code, window, meaning source), or the catalogue stays with the API routes | §2.OBS, P9 |

## 8. Rulings applied (v4)

| Ruling | Settles | Adds |
|---|---|---|
| R1 | C2, and the files as method authority | C25 (hard-coded rules) to carry into config |
| R2 | C1 (B:84) | RO3, RO8 |
| R3a to R3d | C14, P2, C26 (the phase order), P32 (the phases into config) | D1 and D2 per word and cluster on their own schedule; D3 reads claims; the API steps retired; RO1 to RO9 adopted |
| R4 | C10, C11 (narrative authority): Claude's call, no pre-publishing approval, the narrative style predefined in config, each block fitting its chapter's story | B:72's narrative sentence, B:85 to B:88, B:90 and B:91 to retire or replace |
| R7 | C8: reading files under the home cluster's folder | **C27:** `reading_index.roots` indexes `_analytics/Clusters`, so a reading's own files would be indexed as earlier file readings |
| R8 | C13, C12 | |
| R9 | terms: glossary canonical, controlled values in config pointing to it | **P33:** nothing checks that the glossary is current |
| R10 | worked cases in a config table, kept current | |
| R11 | the July method file: relevant parts to config, then archived | |
| R12 | a generated guide, reviewed by the researcher after the rules are restated | |

Still open: R5, R6 and R13 to R19 (`outputs/escalation/2268-rulings-review-v4-20261024.md`).
