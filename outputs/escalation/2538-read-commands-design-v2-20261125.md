# #2538: one command for each read — design (v2, 2026-11-25)

Your requirement (#2538 v55, verbatim): "in simple terms, you need to build each sub process as a separate command, which feeds you with exactly the instruction to read, and what to do with it. The next command then picks up the result from the database and do the same".

- **The steps:** specification v5. **The reads:** `outputs/escalation/2538-read-types-and-packaging-v1-20261125.md` (R1 to R13).
- **The reader is Claude in a session (CP-08).** No model call is built.
- Nothing is built yet.

## 1. The shape of every command

Each sub-process has one command, run in two halves.

**`Read`: the command gives Claude one package, written to `layer.working_dir` and named in the output.**
- **Instruction:** what to read, how, the rules this read must keep (each by id, with its working text), and what to do with each result. It is held in config, one block for each read type, `cfg_setting layer.read_types` (new). The package never carries the whole specification.
- **Data:** exactly what the read uses, for its unit only, pulled from the database with indexed lookups. That includes the results of earlier commands as the database holds them.
- **Answer template:** the file Claude fills, in the shape the recorder takes.
- **Limits:** every pull is timed and sized. A pull over its limit (in config) stops and names itself.

**`Record`: the command takes Claude's answer file and stores it.**
- It runs the recorder's checks. A file with one fault is refused whole, with every fault listed, and nothing is written.
- It writes observations, nodes, traces, markers and old-observation answers in one transaction, and stamps the ledger.
- It closes the read when every ledger row of the unit is answered and validated.
- It prints the next command to run, with its arguments.

The next command reads only from the database. Nothing is carried in a session's memory or in a scratch file.

## 2. The commands, in order (command 3 of v1, ReadOldWords, is part of command 2)

The older observations are answered with the words, not by a command of their own: the recorder refuses a word whose older observations are not answered (RW-13), and the reading must see them (RW-09). An older observation on no word's occurrences is answered by the sweep (command 7).

Each is `.\iba\app\ps\Collection-Build.ps1 -Action <command> -Collection <name>`. The loop commands also take `-Subgroup <name>`, and `Record` takes `-File <answer>`.

| # | command (Read / Record) | read | unit | picks up from the database | Claude returns | writes |
|---|---|---|---|---|---|---|
| 1 | GroupPull / GroupRecord (exist) | R1 name and define subgroups | collection | surfaces, WordNet seed groups | name, definition, placement or set-aside with reason | collection_subgroup, collection_subgroup_surface, surface_event |
| 2 | ReadWords / RecordWords | R2 word in its verses, R3 the older observations on its occurrences | subgroup, words in batches | the subgroup's words, each occurrence's verse and structure, sense head, meaning range, lexicon (trimmed); the older observations on the words' occurrences, each shown once (RW-09) | one observation for each distinct use, with its occurrences; faces; an answer for each older observation shown (keep, restate, merge, consume, delete_neither, carry, defer) | B1 observations and nodes; older answers, consumptions, deletions; ledger S1 and old-observation rows |
| 4 | ReadSenses / RecordSenses | R4 senses (1.1) | subgroup | the B1 observations of the subgroup (commands 2 and 3) | senses: name, text, the B1 observations each carries, each exactly once | 1.1 group observations, nodes, traces to B1 |
| 5 | ReadEnrichment / RecordEnrichment | R5 codes of a sense (1.2) | sense | each sense (command 4) and the lexicon of its codes | one enrichment text for each sense | 1.2 observations, traces to 1.1 |
| 6 | ReadStructure / RecordStructure, with `-Item pairing\|qualifier\|entity\|direction\|double-meaning` | R6 what stands with the subgroup | ledger row | the shared verses' structure lines with positions and partner collection, the WordNet control, the senses (command 4) | findings, each with its verses; or none with reason where allowed | 2.1 observations, nodes, traces to the senses |
| 7 | ReadSweep / RecordSweep | R7 what is still unmarked | subgroup | the old observations still NULL after commands 3 to 6 | evidence, inner being, or neither (deleted) | markers, deletions |
| 8 | CheckEvidence, then ReadEvidence / RecordEvidence | R8 truth and coherence | subgroup | all evidence observations of the subgroup with their verses; the code check's report | a list of untrue or contradictory observations, with each repair | repairs; the evidence gate opens C1 |
| 9 | ReadElements / RecordElements | R9 elements, R10 old inner-being | subgroup (a big one split by sense) | the evidence by marker (senses first) and the verse text | findings on the nine items, with traces and roles; answers to old inner-being observations | 3.1 observations; ends the loop for the subgroup |
| 10 | ReadBehaviours / RecordBehaviours | R11 | collection | all 3.1 observations | behaviours gathering their elements; every element gathered or declared not | 3.2 observations |
| 11 | ReadMatches / RecordMatches | R12 | match (batched) | the observations whose nodes carry more than one collection; the shared verses | one observation for each match | 3.3 observations; partner gate |
| 12 | CheckInnerBeing, then ReadRepairs / RecordRepairs | R13 | failing observation | the code check's list and the evidence of each subgroup | trace found, restated, or deleted with reason | repairs; the collection's completion |

Commands 2 to 9 run for one subgroup, then the next subgroup. Each `Record` prints which command comes next. `LayerNext` already reads the ledger and names it at any time.

## 3. What is built on what exists

- **Kept:**
  - the ledger (`collection_layer_item`), `open_step`, the recorder `record` with all its checks, `check`, the gates, and the marker at creation (`iba/app/lib/layerreading.py`, `layerinner.py`, `buildvalidate.py`);
  - GroupPull and GroupRecord.
- **New:**
  - the instruction block for each read type in config;
  - one `Read` and one `Record` handler for each command, each pulling only its own unit's data;
  - the size and time limit on every pull, also in config.
- **Changed:**
  - today's `LayerPull` gives one file for a whole step, mixing reads, with every verse of the subgroup in the header. The `Read` commands replace it in the loop. `LayerPull` stays for audit.
- **Each command is built and tested on a copy before the next.** Tests cover a known answer file that passes, a faulty one that is refused whole, the next command picking up what the last wrote, and the pull's size and time.

## 4. What is not decided here

- The working text of each instruction block. It is drafted from specification v5 for each read type and shown to you with the first build of each command.
- Thought's existing S1, 1.1 and 1.2 records were written by the session before these commands existed. Whether they are kept or rolled back to the snapshot before them is your decision. The commands work either way, since they pick up whatever the database holds.

## 5. Approval sought

The shape (section 1) and the list and order of the commands (section 2). On approval, command 2 (ReadWords / RecordWords) is built first and tested on a copy of thought, subgroup "meditating and pondering". Its instruction block and a real package go to you before command 3 is started.
