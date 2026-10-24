# #2268 Rulings R1 to R12: review file (v1)

**Date:** 2026-10-24 · **Escalation:** #2268 · **For:** the researcher's rulings, before the alignment design is written. Nothing has been changed.

Researcher, chat 2026-10-24 (verbatim): *"#2268: write R1 to R12 as one review file with the options and a decision blank for each."*

**How to use this file.** Each ruling gives:
- what is in tension, with both sides named;
- the options, with what each would mean;
- Claude's view, labelled **inferential** (B:4): a reading of the evidence, not a confirmed fact, and not a substitute for your ruling;
- a decision blank: write the option letter, or your own wording.

The evidence for each is in the three #2268 files:
- the inventory (`2268-analytic-process-config-inventory-v1-20261024.md`);
- the overlay (`2268-config-overlay-on-reading-process-v1-20261024.md`), with its codes C (conflict), W (era wording) and P (gap);
- the guide plotting (`2268-role-guide-v2-plotted-into-config-v1-20261024.md`).

**Order.** R1 sets the frame for R9 to R12. R3 bears on R2, R6 and R8. R4 and R5 are independent.

---

## R1 Where the study method lives

**In tension:**
- `governance.rules_must_be_config_driven`: no rule may live only in a document.
- `cfg_control_home` study_method: the home of "how study work is done" is `Workflow/Instructions/`, one file per subject. B:73 ends "Full guide: Workflow/…". Three settings name a file as the method's authority: `method.passage_read_guidance_path`, `method.interpretation_questions_path` and `narrative.inner_being_style_guide_path`. (Overlay C2.)

**Your instruction already settles it for the role guide** ("should all be captured in configs and should not live on its own"). R1 asks whether the same holds for every method file.

| Option | What it means |
|---|---|
| **A** | Every method moves into cfg rows: method rules on the reading steps, quality checks at the gates, allowed values, column meanings. The control map's study_method home becomes those tables. A method file is retired, or becomes a view generated from the rows (R12). |
| **B** | Rules and checks move into cfg rows. A file may stay as an explanation that restates no rule, as the control map's description already requires ("the file explains, it does not restate"). Each file is stripped of its rules. |
| **C** | As now: the files stay the authority, and the config points to them. |

**Claude's view (inferential):** A. Under B a second home stays open, and that is how the role guide drifted from config. C contradicts `governance.rules_must_be_config_driven`.

**Decision R1:** ______

---

## R2 What B:84 means for the reading process

**In tension (overlay C1, W1):**
- B:84 says "no cluster reading is started as such" and "capture is focused … with no generic whole-scope task and no backfill of earlier work".
- Against it:
  - the `read_in_files_only` gap type, and `reading_index.roots`, which you approved to carry the October file readings into the tables (#2216 option B);
  - the #2172 catch-up imports;
  - the home cluster every reading needs;
  - the per-cluster routes D1 and D2 (R3).
- B:84's unit is the strand, which is retired (#2228 D-a).

| Option | What it means |
|---|---|
| **A** | Keep the principle, reworded for readings: the inner being is a web; a reading takes one scope, explored for a stated purpose, and the fan-out follows from what it finds; cluster codes are anchors, not goals, so no reading is opened to cover a cluster as such. **Carrying an earlier reading from a file into the tables is not backfill** and is allowed (it is what `read_in_files_only` does). Re-running analysis over earlier work for its own sake stays excluded. |
| **B** | Drop "no backfill" and "no cluster reading" and keep only the web and fan-out picture. |
| **C** | Keep B:84 as it reads: retire `read_in_files_only` and the file index, and stop the catch-up. |

**Claude's view (inferential):** A. It keeps your progressive-reading principle and names the one kind of catch-up you have already approved.

**Decision R2:** ______

---

## R3 The standing of the other three reading routes

**In tension (overlay C14, P2, §6):** four routes each read verses and write observations, and no config row relates them.

| Route | What it is | Rules it carries |
|---|---|---|
| D1 | Stage 1 word-level and relational reading (`lexical.meaning`, `lexical.relational`): per cluster, through the API | 23 method rules, including the observation rules: concise, verse-specific, span-grounded, read all three meaning sources |
| D2 | the characteristic stages (`cluster.subgroup`, `cluster.reading`, `cluster.answer`): per subgroup, through the API | 32 method rules: every instance states what it is; a difference is its own observation; morph actively read |
| D3 | the passage method (`hib.set` to `closing.set`): per book and passage | 37 method rules and all 18 quality checks (warrant, stated or inferred, full lexical range); its tables are never collated by a reading (P6) |
| D4 | the reading process (`Reading.ps1`) | none (P12) |

The declared process is D4 (`governance.study_status`). The quality rules sit on D1 to D3.

| Option | What it means |
|---|---|
| **A** | D4 is the one reading process. D1 becomes an input the reading draws on: the Stage 1 answers for the words in scope are collated. D2 and D3 are retired as routes. The rules of D1 to D3 that carry the role guide's substance are carried into method rules and quality checks on the reading steps. Their existing observations and tables stay as sources the collation reads, D3's included. |
| **B** | D4 is the one reading process, and D1 to D3 are all retired as routes, with the same carrying of their rules and with their outputs kept as sources. Stage 1 is no longer run. |
| **C** | All four stay live, with a rule for when each applies, for example D1 before any reading of a cluster's words, D3 for a whole passage, and D4 for a scope. |

**Claude's view (inferential):** A or B. Both give one process with one rule set, and B is simpler. Whether Stage 1's per-occurrence answers through the API are still wanted as input (A) is a question of method that only you can settle. M64 has no Stage 1 answers (#2260).

**Decision R3:** ______

---

## R4 Who authorises the narrative a reading writes

**In tension (overlay C10, C11):**
- **B:85:** "Claude writes no prose (… a narrative chapter file) without a specific instruction."
- **B:72:** "Routing a strand's verses into the narrative waits for the researcher's direction."
- **Gate 2** (`Reading.ps1 -Step Apply`) tells every claim or holds it, and rewrites the narrative blocks, as routine reading work.
- **B:106:** a workflow Claude designs adds no per-item approval steps by default.

| Option | What it means |
|---|---|
| **A** | Opening a reading under an escalation is the instruction: gate 2 writes claims, tellings and blocks. You review through the published chapters (gate 3) and the reading's escalation. B:85 and B:72 are reworded to say so. |
| **B** | Gate 2 writes claims and tellings, but a block rewrite waits for your go-ahead on the reading's escalation before Apply writes it: one approval per reading, not per block. |
| **C** | B:85 as it stands: Claude drafts each rewrite, and you approve it before it is written. |

**Claude's view (inferential):** A fits B:106 and the gate design. B is the choice if you want to see narrative changes before they are written. This is your call about your own text.

**Decision R4:** ______

---

## R5 One vocabulary for where a verse or observation goes

**In tension (overlay C6, W18):**
- **B:79** and `session_close.placement_kinds` give every verse in a reading, ledger or weave *file* one placement: told, claim, data, forward OT-nn.n, held #nnnn, parked, or context. Session-close SC5(d) checks them, in `_analytics` files only.
- **Gate 2** records, in tables, every observation as carried by a claim or disposed (held on an item, silent, withdrawn), and every claim as told or held.
- Two vocabularies cover one job.

| Option | What it means |
|---|---|
| **A** | Gate 2's vocabulary is the one, extended by the two placements it lacks: **data** (route C: assessed, not for the narrative) and **context** (named only as another verse's setting). B:79 and SC5(d) then apply only to the `_analytics` files still to be carried in, and retire when they are. |
| **B** | The placement kinds become the vocabulary, and gate 2's dispositions are renamed to them. |
| **C** | Both stay, with a mapping between them in config. |

**Claude's view (inferential):** A. The tables are the record now. C keeps two names for one fact.

**Decision R5:** ______

---

## R6 The scope of B:68

**In tension (overlay C7):**
- **B:68:** every correction to `ib_observation` happens only through `record_one_observation` processing a fresh LLM answer.
- **The reading process** writes observations through Claude's reading (`record_strand_observations`, with `supersedes`), and changes their status at gate 2 (`set_disposition`).
- B:68 was written for Stage 1 (route D1).

| Option | What it means |
|---|---|
| **A** | B:68 is limited to the observations of the API routes (D1, D2, if they stay under R3). A reading's observations are corrected only through the reading: a new observation that supersedes the old, or a disposition at gate 2, each with its reason. No standalone edit script is allowed for either. |
| **B** | B:68 applies to every observation, and the reading may not supersede or dispose. Gate 2 as designed cannot then run. |

**Claude's view (inferential):** A. Its last clause keeps B:68's real point, that no script edits observations without a reading behind it.

**Decision R6:** ______

---

## R7 Where a reading's files are filed

**In tension (overlay C8):**
- `report.cluster_folder_naming_convention`: "ALL output relating to a cluster (analysis, readings …) is filed in that cluster's subfolder."
- `reading.output_dir`: every reading under `outputs/reading/<label>/` (its gap JSON, collation and synergy JSON).

| Option | What it means |
|---|---|
| **A** | `outputs/reading/<label>/`, as now. A reading is a scope, not a cluster, and may cross many. The cluster folder rule is reworded to exclude readings. |
| **B** | Under the home cluster's folder (`_analytics/Clusters/<home>/readings/<label>/`), with `reading.output_dir` changed. |

**Claude's view (inferential):** A. A reading's scope is not one cluster (B:84, R2).

**Decision R7:** ______

---

## R8 The passage-method tables and the research database

**In tension (overlay C13):**
- `governance.scope_iba_db`: "a few analysis tables (debate/passage control) are expected to migrate back to research_db".
- `governance.scope_research_db`: research_db is "prose-only".
- B:13 calls research_db "prose + analytic findings" (C12, a correction either way).

| Option | What it means |
|---|---|
| **A** | They stay in iba.db. The migration sentence is removed, research_db stays prose-only, and B:13 is corrected. |
| **B** | They move to research_db, and research_db's scope is widened to say so. |
| **C** | Follows R3: if route D3 is retired, its tables stay in iba.db as sources a reading collates (A). |

**Claude's view (inferential):** A, or C if R3 retires D3. Both leave research_db prose-only, as it is today.

**Decision R8:** ______

---

## R9 Where the study's terms live

**In tension (guide plotting §2):** the guide's terms are used in rules but defined nowhere in config:
- role, characteristic, operation, main IB operation, qualifier;
- relational observation, pointer observation, face, route, faculty, party-kind T-codes.

Seven have glossary entries in the prose store (ids 1089, 1047, 1043, 1066, 1048, 1046, 1069), all at status `draft`. Only *inner being* has a `cfg_prose_concept` pointer. The prose is yours (B:85), and `governance.prose_canonical_authority` makes it the canonical authority on the programme's concepts.

| Option | What it means |
|---|---|
| **A** | The glossary is the definition. Each term gets a `cfg_prose_concept` pointer, delivered at `Reading.ps1`. The missing glossary entries (main IB operation, relational, pointer, face, route, faculty) are drafted for you to write or approve. |
| **B** | The definitions live in config: the controlled values as `cfg_enum` (roles, routes), with their meanings in a setting (as `ib_observation.tag_guidance` does for tags) and in `cfg_column` use text. |
| **C** | Both. The glossary stays canonical, and `cfg_enum` and `cfg_column` carry the controlled values, each pointing to its glossary entry. The words a record may hold are thus checked, and their meaning has one home. |

**Claude's view (inferential):** C. It is the existing pattern (`governance.prose_canonical_authority` with `cfg_prose_concept`), plus the controlled values a record needs. The glossary drafts stay yours to approve.

**Decision R9:** ______

---

## R10 Where the worked cases live

**In tension (guide plotting §3 §6):** the guide's four worked cases (2Pe 2:13, 2Cor 7:11, Lam 4:6, Psa 1:1 and 1:5) teach how the rules apply. No config table holds an example.

| Option | What it means |
|---|---|
| **A** | A config table of worked examples: the rule or check each illustrates, the verse, what the reading found and why. Each is delivered with its rule at first use, so the example arrives where the rule does. |
| **B** | In the glossary, as your prose under the term each illustrates. |
| **C** | A teaching document that config points to, holding no rule. |

**Claude's view (inferential):** A. The Lam 4:6 case is the failure the rules guard against (reading inward, nearly closing on "not X"), and it is worth most at the point of use. C reopens the gap R1 closes.

**Decision R10:** ______

---

## R11 The July method file the guide draws on

**In tension (guide plotting §2):** the guide's definition of role rests on `Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md` §13 and §14. That file is the July "live lexical process" (genre treatment, self-learning loop, index-driven build, poetic and discourse-shaped books), much of it from earlier eras.

| Option | What it means |
|---|---|
| **A** | Carry §13 and §14 into config with the guide, and archive the file. |
| **B** | Review the whole file: what is still live goes into config (genre treatment, poetic and discourse books may bear on reading in a passage), and the rest is archived with a note of what was carried. |
| **C** | Leave it as it is. |

**Claude's view (inferential):** B. A file left with live rules in it is the same gap as R1.

**Decision R11:** ______

---

## R12 The guide itself, once its content is in config

**In tension (guide plotting §1):** once the 57 statements are in cfg rows, the guide would restate them (B:3, single authority), and B:73 still points to it.

| Option | What it means |
|---|---|
| **A** | Archive the guide (B:96), and reword B:73 to point to the cfg rows. |
| **B** | Replace it with a **generated** reading guide, written from the cfg rows by a tool and never edited by hand, the way the claim register is exported. You keep one readable page, and it cannot drift. The current guide is archived. |
| **C** | Keep the guide alongside the config. |

**Claude's view (inferential):** B. It keeps a readable whole, which the guide gives and scattered rows do not, without a second home. C contradicts your instruction.

**Decision R12:** ______

---

## After the rulings

Claude records your rulings verbatim on #2268, then writes the alignment design for your approval before any change. The design will:
- carry the whole guide into config (R1, R9 to R12);
- reword the era configs (W1 to W33);
- settle the conflicts (C1 to C15);
- fill the gaps (P1 to P22).
