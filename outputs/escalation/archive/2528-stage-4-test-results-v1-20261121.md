# #2528 Stage 4 test results (v1, 2026-11-21)

`iba/app/tools/temp_2528_stage4_test_run.py` on a copy of the live `iba.db` made after the configuration was applied (never the live database itself). Two small test collections (backsliding, betray) were taken through stages 1 to 3 on the copy, then steps 3.1 to 3.3. 44 of 44 cases pass. Older tests on copies carrying the same configuration: 2505 47 of 47, 2507 12 of 12, 2509 24 of 24, 2503 16 of 16 (also run on the pre-change snapshot).

| case | what | result | evidence |
|---|---|---|---|
| C1 | layer.reading has 7 steps, the three of layer 3 (3.1, 3.2, 3.3) with the needs the design gives; stage 3 is layer-3, an enum value; 3.3 reads the pairings | PASS | ['S1', '1.1', '1.2', '2.1', '3.1', '3.2', '3.3'] |
| C2 | the three stage 4 items use only items of reading.observation_items, none of them the meaning; each has asks; layer.interventions has prompts | PASS | {'verse-working': ['role', 'polarity', 'object', 'enactment', 'party', 'circumstance', 'operation', 'chain', 'flag'], 'subgroup-working': ['operation', 'chain', 'circumstance', 'flag'], 'interworking': ['operation', 'chain', 'party', 'circumstance', 'flag']} |
| C3 | six rules IB-01 to IB-06 are active on the layer steps; the use text of collection_layer_item.step names 3.1 to 3.3 | PASS |  |
| C4 | the alignment check finds nothing wrong in layer.reading with the stage 4 items in it | PASS | [] |
| C5 | the alignment check finds a stage 4 item that uses the meaning item or an item that does not exist | PASS | ["layer.reading item 'verse-working' uses 'nonsense', which is not an item of reading.observation_items", "layer.reading item 'verse-working' (stage 4) uses the item meaning, which is the lexical work of stages 1 and 3"] |
| C6 | orec.write takes optional stage and stable_key (defaults None: the old reading is unchanged) | PASS | (conn, plan: 'list[dict]', reading_id: 'int / None', run_id: 'str', stage: 'str / None' = None, stable_key=None) -> 'dict' |
| G1 | step 3.1 on a collection with nothing done is refused, naming the steps of stage 3 that are not closed | PASS | step 3.1 of backsliding cannot be opened:
  6 surfaces are not placed in a subgroup or isolated: apostasy, backsliding, backslidings, fall away, falling away, wickedly departed
  the collection has no subgroup
  step 1.1 is not closed (every row answered and validated: LayerCheck)
  step 1.2 is not  |
| G2 | with 1.1 and 1.2 closed and 2.1 not opened, step 3.1 is still refused and names 2.1 | PASS | step 3.1 of backsliding cannot be opened:
  step 2.1 is not closed (every row answered and validated: LayerCheck) |
| G3 | stages 1 to 3 are closed on the test collection (setup) | PASS | {'S1': True, '1.1': True, '1.2': True, '2.1': True} |
| O1 | opening 3.1 makes one verse-working row for each subgroup and verse the subgroup has an occurrence in (equal to an independent query); opening again changes nothing | PASS | 14 rows; independent query gives 14 pairs; {'collection': 'backsliding', 'step': '3.1', 'demanded': 14, 'add': 14, 'retire': 0, 'revive': 0} |
| O2 | step 3.2 cannot open before 3.1 is closed | PASS | step 3.2 of backsliding cannot be opened:
  step 3.1 is not closed (every row answered and validated: LayerCheck) |
| P0 | the working file carries the reading rules (RG, RW, RS) once, from the rules of the retired reading steps | PASS | 42 |
| P1 | the working file holds at most pull_max_rows rows, each with the verse in its passage, the occurrences, the uses, the interventions, the node roles and a fill | PASS | 5 rows; layer-backsliding-3.1-20261121.json |
| R1a | refused whole, nothing written: restates the verse | PASS |  is refused, nothing written; problems:
  row 1 (ledger 596) finding 1: the text restates the verse ('they shall not defile themselves anymore with their'); say what the word does in it (B:131, RW-04) |
| R1b | refused whole, nothing written: is not an occurrence this row may name | PASS | the file is refused, nothing written; problems:
  row 1 (ledger 596) finding 1 nodes[1]: occurrence 1 is not an occurrence this row may name |
| R1c | refused whole, nothing written: parts.item is one of | PASS | the file is refused, nothing written; problems:
  row 1 (ledger 596) finding 1: parts.item is one of ['role', 'polarity', 'object', 'enactment', 'party', 'circumstance', 'operation', 'chain', 'flag'] |
| R1d | refused whole, nothing written: answered by findings | PASS | the file is refused, nothing written; problems:
  row 1 (ledger 596): the row is answered by findings (fill.findings): at least one, each with its kind, text, basis, parts and nodes |
| R1e | refused whole, nothing written: cannot be recorded as none | PASS | the file is refused, nothing written; problems:
  row 1 (ledger 596): verse-working cannot be recorded as none; it needs findings |
| R3 | a verse with no observation of the item operation is refused | PASS | the file is refused, nothing written; problems:
  row 1 (ledger 596): the verse has no observation of the item operation (the verse always has one, RS-10) |
| R4 | a characteristic with an item neither observed nor stated absent is refused, naming the item | PASS |  problems:
  row 1 (ledger 596): occurrence 1348562 is a characteristic: the item 'role' needs an observation with a node on it, or items_absent saying why the verse shows none (10 characters or more) |
| R5 | the stage 1 to 3 role lexical is refused on a stage 4 node | PASS | the file is refused, nothing written; problems:
  row 1 (ledger 596): observation 22129 has a node with no valid stage 4 role ('lexical') |
| R6 | the preview checks and writes nothing | PASS | {'observed': 5, 'none': 0, 'nodes': 5, 'withdrawn': 0} |
| R7 | one observation for each row, stage layer-3, kind statement, a stable key tying it to its ledger row; each has a node for every occurrence of its row with a role, a collection and a subgroup | PASS | {'observed': 5, 'none': 0, 'nodes': 5, 'withdrawn': 0}; nodes {596: 1, 597: 1, 598: 1, 599: 1, 600: 1} |
| R8 | the ledger rows are observed, carry the stated-absent items, and are not yet validated | PASS |  |
| R9 | the same file again is not accepted once the rows are recorded and unvalidated rows are re-recordable: it withdraws and writes again (re-record) | PASS |  |
| K1 | LayerCheck validates the recorded rows; the step is not closed while rows are open | PASS | {'rows': 14, 'validated': 5, 'open': 9} |
| K2 | after every row is recorded, step 3.1 closes | PASS | [] |
| K3 | no standalone node on this collection to remove (every row has a single occurrence) | PASS |  |
| K5 | an observation withdrawn from a stage 4 row: the row fails (its observations are missing) and the step is not closed | PASS | ['verse-working / alpha / Ezek.37.23: its observations are missing or withdrawn'] |
| K6 | restored: step 3.1 closes again | PASS |  |
| E1 | the pull shows an earlier inner-being observation of the verse with its nodes and flags | PASS | [] |
| E4 | an earlier observation with a node on the verse that the file does not answer is refused (RS-04: none is passed over) | PASS | , nothing written; problems:
  row 1 (ledger 596): earlier observation 22143 has a node on this verse and needs an action in `existing` (accept, modify, delete, merge or leave, with its reason; RS-04) |
| E2 | an action on an earlier observation needs its reason | PASS | dger 596): earlier observation 22143 has a node on this verse and needs an action in `existing` (accept, modify, delete, merge or leave, with its reason; RS-04) |
| E5 | an earlier observation accepted is kept on the row: the ledger names it and the check passes the row | PASS | row_state:{"absent": {"1348562": {"chain": "the verse shows none of this item; test of the stated-absent rule", "circumstance": "the verse shows none of this item; test of the stated-absent rule", "enactment": "the verse shows none of this item; test of the stated-absent rule", "flag": "the verse shows none of this item; test of |
| E3 | the earlier observation is deleted with its reason kept in ib_observation_change and the row is answered again | PASS |  |
| O3 | step 3.2 opens after 3.1 closes with one row for each subgroup that has occurrences | PASS | {'collection': 'backsliding', 'step': '3.2', 'demanded': 2, 'add': 2, 'retire': 0, 'revive': 0} |
| P2 | the 3.2 working file shows the observations of step 3.1 the row may rest on | PASS | 6 |
| R10 | a 3.2 finding that rests on no observation of the step below is refused | PASS | the file is refused, nothing written; problems:
  row 1 (ledger 610): observation 22146 rests on no observation of the step below (a traced node on each) |
| K7 | LayerCheck validates the 3.2 rows and closes step 3.2 | PASS | [] |
| O4 | step 3.3 opens after 3.2 closes; its rows equal the pairs of subgroups and the partner collections that reach the thresholds | PASS | 1 rows demanded: ['collection:sin'] |
| K8 | every 3.3 row answered as none with its reason validates | PASS | {'rows': 1, 'validated': 1, 'open': 0, 'failed': [], 'not_in_ledger': [], 'closed': True} |
| M1 | moving a surface to another group makes stage 4 rows fail or missing and step 3.1 is no longer closed | PASS | failed ['verse-working / alpha / Hos.14.4: the data no longer demands this aspect (LayerOpen retires it)'] missing ['missing: verse-working / gamma Hos.14.4'] |
| R2 | an occurrence of a row with several occurrences left with no node is refused (every occurrence is read), nothing written | PASS | 3 occurrences; ten; problems:
  row 1 (ledger 648): 2 of 3 occurrences carry no node with a role (every occurrence is read; one with nothing for the inner being is standalone) |
| R11 | the same row with a node on every occurrence (one characteristic, the others standalone) is recorded and validates | PASS | [] |

44 of 44 pass

