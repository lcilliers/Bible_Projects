# #2268 The config overlaid on the new analytic process: gaps and conflicts (v1)

**Date:** 2026-10-24 · **Escalation:** #2268 · **Status:** findings only. Nothing has been changed.

Researcher, chat 2026-10-24 (verbatim): *"So now overlay this extract onto the new analytic process and show gaps and conflicts.  I can already see several configs that actually refers to a previous era, although the rules may be correct, the wording and alignment no longer fits."*

**Sources.**
- The inventory: `outputs/escalation/2268-analytic-process-config-inventory-v1-20261024.md`.
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
| Rows marked Fits | 26 | across the steps (§2); some rows group several settings, and B:114 and E:16 appear at two steps |
| Era wording (rule substance may stand) | 31 | listed as W1 to W31 (§4) |
| Conflicts | 14 | listed as C1 to C14 (§3) |
| Gaps | 15 | listed as P1 to P15 (§5) |
| Reading routes outside the new process | 3 | D1 to D3, with 100 method rules and 18 quality checks (§6) |

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

## 3. Conflicts (C1 to C14)

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

## 4. Era wording (W1 to W31)

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

## 5. Gaps (P1 to P15)

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

## 6. The three other reading routes against the new process

| Route | Era | Method rules / checks | How it relates to the new process |
|---|---|---|---|
| D1 Stage 1 (`lexical.meaning`, `lexical.relational`) | September, LLM generator | 23 rules; rules 71, 74, 111, 112, 114, 116, 120 and 121 speak of "the LLM" or "the model" | its observations reach a reading through `ib_observation` (`draft` only, C4). Its per-cluster scope (rules 72, 115) conflicts with B:84 (C1). Its observation rules (108 to 112, 119 to 121) are the quality bar a reading lacks (P12). Not run for M64 |
| D2 characteristic stages (`cluster.subgroup`, `cluster.reading`, `cluster.answer`) | September, LLM generator | 32 rules; rules 86, 94, 96, 99, 106 and 107 speak of the model or "this build" | reaches a reading through `ib_observation`. Per subgroup, which conflicts with B:84 (C1). Rules 88 and 91 to 95 (three sources, every instance states what it is, difference as its own observation, morph read) bind only here |
| D3 passage method (`hib.set` to `closing.set`) | August, debate | 37 rules (rules 13, 25, 27, 31, 33 and 39 speak of the debate or its phases) and all 18 quality checks; `method.*` document paths | writes `hib`, `phenomenon` and `operation`, which a reading never collates (P6). Its quality checks (warrant, stated or inferred, full lexical range, genuinely inner-being) are the only reading-quality checks in config |

No row says whether D1 to D3 are live routes, steps that come before a reading, or retired (C14, P2).

## 7. What needs your decision before any rewording

The era rewording (W1 to W31) and the config corrections (C4, C5, C12) follow from what is settled. The following are new decisions (B:44) and need your ruling first:

| # | Decision | From |
|---|---|---|
| R1 | Where the study method lives: cfg rows, or the Workflow files kept as the control map says | C2 |
| R2 | What B:84's "no backfill" and "no cluster reading" mean now | C1 |
| R3 | The standing of routes D1 to D3 against the reading process | C14, P2 |
| R4 | Whether opening a reading under an escalation is the instruction to write narrative (B:85, B:72) | C10, C11 |
| R5 | One vocabulary for where a verse or observation goes (placements, or gate 2 dispositions) | C6 |
| R6 | The scope of B:68 (Stage 1 only, or every observation) | C7 |
| R7 | Where reading output is filed | C8 |
| R8 | Whether the debate tables are to move to research_db | C13 |
