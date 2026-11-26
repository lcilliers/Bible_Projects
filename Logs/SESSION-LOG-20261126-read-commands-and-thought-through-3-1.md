# Session log 20261126: one command for each read (#2538), and the ten subgroups of thought read through step 3.1, developer mode

Session id: `760131f7-a5d4-44b5-92a0-7c28ca0a4683` (started 2026-11-25, window base commit `cbd46aa8dcb46fb95e5ee10283311450498641a6`).

## 1. Scope

2026-11-25 to 2026-11-26. Developer Mode session on #2538: the read commands built and applied one at a time, then all ten subgroups of thought read through step 3.1 on live with them.

The researcher required each sub-process of the layered reading to be its own command, which feeds the reader exactly the instruction to read and what to do with it, the next command picking the result up from the database (#2538 v55). Built, tested on copies, shown to the researcher and applied live one at a time on his approval: ReadWords/RecordWords (S1), ReadSenses/RecordSenses (1.1), ReadEnrichment/RecordEnrichment (1.2), ReadStructure/RecordStructure (2.1), the two gates of 2.1 with ReadSweep/RecordSweep (B4) and ReadEvidence/RecordEvidence (B5), and ReadElements/RecordElements (3.1). Then, on "lets continue to complete all the sub groups for thought in this chat" (#2538 v82), all ten subgroups of thought were read through step 3.1 on live with these commands, each answer previewed with -Check. The reader throughout is Claude in the session (CP-08); no model is called.

## 2. Escalations

- #2538: updated throughout (in progress); v42 to v83 carry the researcher's words verbatim, each build, each approval and each subgroup; v83 the end state (all ten subgroups through 3.1, next the collection steps 3.2 and 3.3).
- #2560, #2565: raised (approvals to run archived migrations on test copies), approved, completed. #2568: raised, approved (standing approval for test copies for the rest of #2538); open while #2538 continues.
- #2609: raised (the 3.1 package cap raise, 160000 to 400000, for "thinking and thought"); the live apply was stopped by the permission check, handed to the researcher, approved ("Approve, apply live", v3), applied and completed (v4).
- #2576: raised (the meaning of the party routes A, B and C); with the researcher.
- #2618: raised (a 3.1 record that deletes earlier readings leaves dead traces that reopen another subgroup's evidence gate); open.
- Resolved self-correctable, each fixed in the reading or the code: #2552, #2553, #2557, #2559, #2561 to #2564, #2566, #2567, #2569 to #2575, #2577 to #2608, #2610 to #2617 (the read-order and empty-sweep notices among them; #2591 the step limit fixed in code; #2608 the cap fixed through #2609).

## 3. Files

- Code: `iba/app/lib/readcommands.py` (the read commands), `iba/app/handlers/collectionbuild.py`, `iba/app/ps/Collection-Build.ps1`, `iba/app/lib/layerreading.py` (gates in derive, pull and check; `trace_targets` by key), `iba/app/lib/layerloop.py` (the order gate and LayerNext naming the read command), `iba/app/lib/strandreading.py` (quote check cached), `iba/app/lib/collectionvalidate.py`, `iba/app/lib/lexicalalignment.py`.
- Migrations, applied live and in `iba/app/migration/archive/`: `readwords_2538_v1_20261125.py`, `senses_2538_v1_20261125.py`, `enrichment_2538_v1_20261126.py`, `structure_2538_v1_20261126.py`, `gates_2538_v1_20261126.py`, `elements_2538_v1_20261126.py`, `elementscap_2538_v1_20261126.py`.
- Tests on copies: `iba/app/tools/temp_2538_readwords_test_run.py`, `temp_2538_readsenses_test_run.py`, `temp_2538_readenrichment_test_run.py`, `temp_2538_readstructure_test_run.py`, `temp_2538_gates_test_run.py`, `temp_2538_elements_test_run.py`, `temp_2538_loop_order_test_run.py`, `temp_2509_grouping_test_run.py`.
- Documents: `iba/app/BUILD.md` entries 574 to 587, `iba/app/USER-GUIDE.md`, `iba/docs/project-map.md`, `iba/docs/ps tools worksheet.xlsx` (the -Item column), and in `outputs/escalation/` the instruction-and-package reviews of each command and the 3.1 answers `2538-readelements-*-answer-v1-20261126.json` for all ten subgroups.
- Data (iba.db): thought read through S1 to 3.1 for every subgroup (ledger `collection_layer_item`, observations and nodes written by the recorders).

## 4. Decisions

The researcher's decisions:
- One command for each read, the next picking up from the database: recorded in #2538 v55; the design approved in #2538 v57.
- Each command applied live on his approval: #2538 v60 (ReadWords), v62 (ReadSenses), v65 (ReadEnrichment), v68 (ReadStructure), v74 (the gates), v78 (ReadElements).
- Read 2.1 live, build the gates first, run the next subgroup, complete all subgroups of thought: #2538 v70, v72, v80, v82.
- The 3.1 package cap raised to 400000 in `cfg_setting` layer.read_types: approved in #2609 v3, applied in #2609 v4.

Claude's self-correctable fixes, made and closed:
- `trace_targets` finds the ledger row by key: iba/app/BUILD.md entry 584, #2591 v2.
- Dead traces dropped through RecordEvidence: #2610 v2; the gap raised as #2618 v1.

## 5. Open items

- #2538 (Claude): the collection steps 3.2 (behaviours) and 3.3 of thought; they have no read command yet.
- #2576 (researcher): what routes A, B and C mean, so that party findings can be written.
- #2618 (Claude): the 3.1 recorder should drop or re-point traces to an earlier reading it deletes, or a sheet action should drop a dead trace.
- #2568 (Claude): the standing test-copy approval, open while #2538 runs.

## 6. Git
