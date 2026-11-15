# #2505 Test results: the layered reading of a collection (v1, 2026-11-15)

Run on copies of iba.db that hold the migrations (never the live database): `iba/app/tools/temp_2505_layers_test_run.py` (36 cases), and the regression runs of `temp_2502_evidence_pairs_test_run.py` (19 cases) and `temp_2503_collection_index_test_run.py` (16 cases). The case text is in each tool; evidence is cut to 330 characters.

## Layered reading (temp_2505)

| case | what | result | evidence |
|---|---|---|---|
| C1 | layer.reading is registered with 3 steps and 8 items; stages layer-1 and layer-2; the four kinds are enum values | PASS | steps ['1.1', '1.2', '2.1'] |
| C2 | every item kind is an ib_observation.tag value and every step's items are defined | PASS |  |
| C3 | ib_node.subgroup_id and the ledger table exist and are registered in cfg_column | PASS |  |
| C4 | five steps registered with a routed condition; B:119/B:120 reworded; RO13 inactive; three new rules active | PASS |  |
| G1 | the real collection thought: LayerOpen 1.1 is refused (grouping unfinished; the lexical gate is stated) | PASS | step 1.1 of thought cannot be opened:
  the lexical gate fails: 282 of 394 member occurrences carry no lexical node with a role (the lexical observations come first; Engagement.ps1 -Action Pull -Collection thought -Missing)
  33 surfaces are not placed in a subgroup or isolated: conceive, conflictin |
| G2 | an unknown step and an unknown collection are refused | PASS |  |
| G3 | the test collection with no lexical nodes and nothing placed is refused, naming the lexical gate and the grouping | PASS | step 1.1 of backsliding cannot be opened:
  the lexical gate fails: 13 of 15 member occurrences carry no lexical node with a role (the lexical observations come first; Engagement.ps1 -Action Pull -Collection backsliding -Missing)
  6 surfaces are not placed in a subgroup or isolated: apostasy, backs |
| G4 | with a lexical node on every member occurrence the lexical gate passes | PASS | 15 of 15 |
| G5 | gate passes but nothing is placed: still refused, naming the unplaced surfaces and the missing subgroup | PASS | step 1.1 of backsliding cannot be opened:
  6 surfaces are not placed in a subgroup or isolated: apostasy, backsliding, backslidings, fall away, falling away, wickedly departed
  the collection has no subgroup |
| G6 | one surface still unplaced: refused | PASS | step 1.1 of backsliding cannot be opened:
  1 surfaces are not placed in a subgroup or isolated: wickedly departed |
| G7 | step 1.2 cannot open before 1.1 is closed | PASS | step 1.2 of backsliding cannot be opened:
  step 1.1 is not closed (every row answered and validated: LayerCheck) |
| N1 | placing surfaces set subgroup_id on their existing nodes (placement refresh) | PASS | 6 of 6 nodes of the alpha surfaces carry a group |
| N2 | an isolated surface's nodes carry no group | PASS | [<sqlite3.Row object at 0x0000026461F20E50>] |
| O1 | opening 1.1 makes one group-definition row for each of the 2 groups; opening again changes nothing | PASS | {'collection': 'backsliding', 'step': '1.1', 'demanded': 2, 'add': 2, 'retire': 0, 'revive': 0} then {'collection': 'backsliding', 'step': '1.1', 'demanded': 2, 'add': 0, 'retire': 0, 'revive': 0} |
| P1 | the working file holds the 2 open rows, each with the evidence and an empty fill | PASS | layer-backsliding-1.1-20261115.json |
| R1 | a file with none on a group definition, a short text and a bad basis is refused whole, nothing written | PASS | the file is refused, nothing written; problems:
  row 1 (ledger 1): group-definition cannot be recorded as none; it needs an observation
  row 2 (ledger 2): the observation text is missing or under 40 characters
  row 2 (ledger 2): basis must be one of ['read', 'stated'] |
| R2 | an unknown ledger row is refused | PASS |  |
| R3 | the preview checks and writes nothing | PASS | {'observed': 2, 'none': 0, 'nodes': 14, 'withdrawn': 0} |
| R4 | 2 observations of stage layer-1 and kind group; each has exactly the occurrences of its group as nodes, each with a role, a collection and the group | PASS | {'observed': 2, 'none': 0, 'nodes': 14, 'withdrawn': 0}; nodes [<sqlite3.Row object at 0x0000026462149DE0>, <sqlite3.Row object at 0x0000026462149BA0>]; want {1: 6, 2: 8} |
| R5 | the ledger rows are observed with their observation and not yet validated | PASS |  |
| K1 | LayerCheck validates both rows and closes step 1.1; later steps have no rows | PASS | {'rows': 2, 'validated': 2, 'open': 0, 'failed': [], 'not_in_ledger': [], 'closed': True} |
| R6 | the same file again is refused once the rows are validated | PASS |  |
| K2 | a node removed from a layer observation: the row fails with the number missing, validated is cleared, the step is not closed | PASS | ['group-definition / alpha: its nodes do not match the data: 1 occurrences missing, 0 not demanded'] |
| K3 | with 1.1 not closed, step 1.2 stays refused | PASS | step 1.2 of backsliding cannot be opened:
  step 1.1 is not closed (every row answered and validated: LayerCheck) |
| K4 | the pull after a failure holds just the failed row | PASS | ['alpha'] |
| K5 | re-recorded: the earlier observation is withdrawn, the new one validates, step 1.1 closes | PASS | {'observed': 1, 'none': 0, 'nodes': 6, 'withdrawn': 1} |
| E1 | 1.2 opens once 1.1 is closed; the enrichment observations carry a node for every Strong's code of the group; step 1.2 closes | PASS | {'collection': 'backsliding', 'step': '1.2', 'demanded': 2, 'add': 2, 'retire': 0, 'revive': 0}; {'observed': 2, 'none': 0, 'nodes': 14, 'withdrawn': 0} |
| L1 | 2.1 opens after 1.2 is closed; the ledger rows equal the aspects the data demands | PASS | [<sqlite3.Row object at 0x0000026461DA00A0>, <sqlite3.Row object at 0x0000026461DA0190>, <sqlite3.Row object at 0x0000026461DA0040>, <sqlite3.Row object at 0x0000026461DA0070>, <sqlite3.Row object at 0x0000026461DA0130>] |
| L2 | every 2.1 row answered as none (with reason) validates; step 2.1 closes | PASS | {'rows': 10, 'validated': 10, 'open': 0, 'failed': [], 'not_in_ledger': [], 'closed': True} |
| L3 | an entity row recorded as observed without a route is refused | PASS |  |
| M1 | moving a surface to another group moves the group on all of its nodes | PASS | (9, 9) |
| M2 | the moved surface makes the earlier layer rows fail or the step reopen (the data demands a new group row), not stay validated | PASS | failed ['group-definition / alpha: its nodes do not match the data: 0 occurrences missing, 2 not demanded'] missing ['missing: group-definition / gamma'] |
| M3 | NodeGroups preview on the copy: every node agrees with the index | PASS | {'changed': 0, 'unchanged': 62120, 'set': 0, 'cleared': 0} |
| M4 | the index check names nodes whose group differs from the index | PASS | [[8, 62112]] |
| M5 | the refresh repairs them and keeps each change with its reason | PASS | {'changed': 8, 'unchanged': 62112, 'set': 8, 'cleared': 0} |
| W1 | the shared node writer helper returns the group of a placed surface and None for no collection | PASS |  |

36 of 36 pass


## Regression: evidence report pairings (temp_2502)

| case | what | result | evidence |
|---|---|---|---|
| T1 | the setting holds its five keys | PASS | ['bands', 'collection_status', 'morph_class', 'qualifier', 'top_n'] |
| T2 | a missing collection.evidence_pairs refuses and names the key | PASS | refused |
| T3 | the verse view holds every live verse_lexical row of the member verses | PASS | view 6576 direct 6576 |
| T4 | the rows marked member are exactly the member occurrences | PASS | 394 member rows of 394 occurrences |
| T5 | rows are in Scripture order and word order | PASS | 6576 rows |
| T6 | the entity and negator types agree with verse_lexical | PASS | 0 disagreements over 6576 rows |
| T7 | every pairing's distance, band and side agree with the positions and the setting | PASS | 2757 pairings, 0 wrong |
| T8 | the pairings are all member by typed-neighbour combinations in a verse | PASS | expected 2757 built 2757 |
| T9 | a sample of 40 neighbour collections traces to confirmed collections by link or base | PASS | 40 sampled, 0 untraced |
| T10 | the read status agrees with the live nodes of 120 sampled rows | PASS | 0 wrong |
| T11 | links at the code and surface levels equal the pairings | PASS | code 2757 surface 2757 pairings 2757 |
| T12 | the four new sheets are in the workbook | PASS | ['Read me', 'Collection', 'Links', 'Members', 'Occurrences', 'Verse view', 'Pairings', 'Pairing summary', 'Verse observations', 'Strongs codes', 'Meaning trees', 'Related terms', 'LSJ senses', 'Mounce', 'Cluster assignments', 'Placements', 'Observations', 'Observation nodes', 'Withdrawn observations', 'Change history', 'Claims', |
| T13 | sheet rows: Verse view = verse_lexical rows; Pairings = pairings; Pairing summary = counted rows; Verse observations = nodes | PASS | 6576/6576 2757/2757 3693/3693 1838/1838 |
| T14 | the reading column is empty on the pairings and the summary | PASS | empty |
| T15 | no cell of any sheet is stored as a formula (text starting with '=' is text) | PASS | 0 formula cells |
| T16 | the Markdown has section 3a with its five subsections, between sections 3 and 4 | PASS | found |
| T17 | qualifier candidates appear among the pairings | PASS | 642 pairings with a qualifier candidate |
| T18 | a verse report is built as before, without pairing sheets | PASS | ['Read me', 'Verses', 'Occurrences', 'Strongs codes'] |
| T19 | the smallest collection (uncircumcised) builds with 66 occurrences | PASS | 494 pairings |

19 pass, 0 fail; files in C:\Users\lerouxc\AppData\Local\Temp\claude\374f3c6c8735d697\58e035fd-4cd5-440d-ba63-65b2f1a988f5\scratchpad\o2\t2502


## Regression: index and subgroups (temp_2503; I2a failed on a precondition of the test, corrected afterwards)

| case | what | result | evidence |
|---|---|---|---|
| I1 | both tables exist and are registered (cfg_table 2, cfg_column 22, three steps) | PASS | tables ['collection_subgroup', 'collection_subgroup_surface'] cfg_table 2 cfg_column 22 steps ['collection.index', 'collection.subgroup', 'collection.index_check'] |
| I2a | the preview counts the member surfaces as an independent query does | FAIL | preview {'expected': 3437, 'live': 3437, 'add': 0, 'retire': 0} independent 3437 |
| I2b | the fill writes exactly those rows, all unplaced, whole surface, no subgroup | PASS | rows 3437 states [('unplaced', 3437, 3437, 3437)] |
| I3 | a second fill adds and retires nothing | PASS | {'expected': 3437, 'live': 3437, 'add': 0, 'retire': 0} |
| I4 | a surface whose link is removed is retired with an event; it returns on the next fill | PASS | retired 1 live after 0 events 1 back 1 added 1 |
| I5 | a subgroup is made with an event; a bad collection, an empty name, no reason and a duplicate are refused | PASS | refusals ["'nosuchword' is not a confirmed collecti", '-Name is required: the name of the subgr', '-Reason is required: why the subgroup is'] dup collection thought already has a subgrou |
| I6 | three surfaces placed whole in a subgroup, with events | PASS | [('placed', 1, None), ('placed', 1, None), ('placed', 1, None)] |
| I7 | each bad placement is refused and nothing is written | PASS | {'unknown surface': "'zzzz' is not in the index of collection thought (", 'no reason': "-Reason is required: why (the researcher's instruc", 'no group': "collection thought has no subgroup 'test-nosuch': ", 'no surface': '-Surface is required: one or more surfaces of the ', 'strong not carried': "'think' has no occurrence with S |
| I8 | placing one sense splits the surface into a row for each Strong's code; naming no code on a split surface is refused | PASS | codes ['G1261', 'G1270', 'G1271', 'G1761', 'G3540', 'G3588', 'H1697I', 'H1902H', 'H4093', 'H4209', 'H4284', 'H5587B', 'H7454', 'H7476', 'H8312'] states [('G1261', 'placed'), ('G1270', 'unplaced'), ('G1271', 'unplaced'), ('G1761', 'unplaced'), ('G3540', 'unplaced'), ('G3588', 'unplaced'), ('H1697I', 'unplaced'), ('H1902H', 'unpla |
| I9 | an isolated surface has the state isolated and no subgroup | PASS | [('isolated', None)] |
| I10 | a surface that is in another collection is refused for this one | PASS | precious |
| I11a | the checker finds nothing wrong in the filled and placed index; its shared-flag finding equals a direct count | PASS | clean True shared flags without a second link 0 direct 0 |
| I11b | seeded faults (a duplicate, a whole and a code row, a placed row with no subgroup, a member with no row) are each found | PASS | {'duplicate-live-row': 1, 'split-rule-broken': 1, 'placement-does-not-agree': 1, 'member-with-no-index-row': 1} |
| I12a | member occurrences carry the subgroup of their surface, and a split surface by its Strong's code | PASS | {'': 345, 'test-plotting': 19, 'test-meditation': 23, 'test-thinking': 7} |
| I12b | the sheets carry the subgroup columns and the summary has a subgroup level; the reading column is still empty | PASS | levels ["Strong's code", 'collection or type', 'subgroup', 'surface'] |
| I12c | the Markdown states how many member occurrences are placed and shows the subgroup level | PASS | found |

15 pass, 1 fail; files in C:\Users\lerouxc\AppData\Local\Temp\claude\374f3c6c8735d697\58e035fd-4cd5-440d-ba63-65b2f1a988f5\scratchpad\o3\t2503

