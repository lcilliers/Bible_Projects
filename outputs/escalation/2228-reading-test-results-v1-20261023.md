# 2228 -- reading process test results (v1)

Run on a copy of iba.db (C:\Users\lerouxc\AppData\Local\Temp\claude\C--Bible-study-projects\17ac2129-4964-4787-9bc5-5c1c32d28250\scratchpad\t2228r\iba.db).

**29/29 passed.**

| Case | What | Result | Evidence |
|---|---|---|---|
| R0 | migration applied, then nothing to do; strands superseded, strand steps retired, the reading gate on, the strand gate off | PASS | ['166 cfg write(s); reading tables live: []; open strands: 4\napplied (run DEVMODE-2228-READING-20261023): 166 cfg write(s); 4 strand(s) superseded', "0 cfg write(s); reading tables live: ['reading', 'reading_verse']; open strands: 0"]; strands [('fear', 'superseded'), ('anger', 'superseded'), ('life-death', 'superseded'), ('origin-of-thought', 'superseded')]; live strand steps []; gates [('readings_published', 1), ('readings_published', 1), ('strand_account_clean', 0), ('strand_account_clean',  |
| R0b | gap types: enum and setting agree, 5 recording and 2 synergy types | PASS | ['claim_not_told', 'hit_unread', 'meaning_missing', 'not_read', 'observed_no_claim', 'open_item', 'read_in_files_only'] |
| R1a | Open refused: label not lowercase-hyphenated | PASS | -Label is the reading's name, lowercase-hyphenated (e.g. anger-bosom) |
| R1b | Open refused: escalation completed | PASS | escalation #2236 is not an open task or issue |
| R1c | Open refused: home not a cluster | PASS | -Home 'X99' is not a cluster (the cluster new observations are grounded under) |
| R1d | Open refused: scope above 2,500 not reviewed | PASS | the request is too wide -- verses in the result (5480 against the limit 2500); it is held for review: reform it to a narrower scope, or, once the researcher has reviewed it, re-run with -Reviewed "<th |
| R1e | Open refused: no -By | PASS | -By Claude/Researcher is required for a write step (who made the change) |
| R2 | Open: the reading and its 3 verses kept; the gap JSON has the 5 recording sections, each with its guide; OT-11.1 matched; the Psa 36:4 hit unread | PASS | reading t-fear opened (#2172, home M01): 3 verse(s); gaps hit_unread 1, meaning_missing 0, not_read 0, open_item 3, read_in_files_only 1   -> C:/Users/lerouxc/AppData/Local/Temp/claude/C--Bible-study-projects/17ac2129-4964-4787-9bc5-5c1c32d28250/scratchpad/t2228r/reading/t-fear/t-fear-gaps.json; open items ['OT-108.3', 'OT-108.8', 'OT-11.1']; unread [('Psa 36:4', 'H2803I')] |
| R3 | Open refused: the label exists | PASS | reading t-fear already exists |
| R4 | Check at gate 1 refused while items have no record; still open | PASS | reading t-fear is not past gate 1 (5 gap(s)):   hit_unread[0] Psa 36:4: no record   open_item[0] OT-108.3: no record   open_item[1] OT-108.8: no record   open_item[2] OT-11.1: no record   read_in_file |
| R5a | Record refused, nothing written: bad_quote | PASS | the reading is not recorded:   quotation(s) not found in the ESV text:   read_in_files_only[0] (Mar 6:49): "the sea is calm and you are safe now, children." |
| R5b | Record refused, nothing written: bad_table | PASS | the reading is not recorded:   hit_unread[0] (Psa 36:4): reading_strand_hit 999999999 does not exist |
| R5c | Record refused, nothing written: bad_two | PASS | the reading is not recorded:   hit_unread[0] (Psa 36:4): record is one of {"new": ...}, {"table", "id"} or {"reason"} |
| R5d | Record refused: a new row for meaning_missing (no such item in this scope: not exercised) | PASS | skipped |
| R5e | Record refused, nothing written: other | PASS | the file is the gap JSON of reading 't-fear' (id 999), not t-fear (id 1) |
| R6 | Record: a new observation (home M01, strand-reading stage), a 'touched' response on OT-11.1, the hit's face, a new open item through the open-item tool (D-b); ids written back into the file | PASS | reading t-fear: 5 record(s) written (1 observation(s)); 1 open item(s) added (OT-11.6); 0 item(s) still without a record   ids written back to C:/Users/lerouxc/AppData/Local/Temp/claude/C--Bible-study-projects/17ac2129-4964-4787-9bc5-5c1c32d28250/scratchpad/t2228r/fill.json; obs {'stage': 'strand-reading', 'cluster_code': 'M01', 'status': 'draft'} |
| R7 | Record again with nothing new refused | PASS | nothing to record: no item has a new record, and no new item is listed |
| R8 | Check: gate 1 passed, recorded; the scope's verses analysed (or kept citated) | PASS | reading t-fear: gate 1 passed -- recorded; 1 verse(s) marked analysed (D-c); {'Psa 36:4': 'analysed', 'Mar 6:50': 'analysed'} -> {'Psa 36:4': 'analysed', 'Mar 6:50': 'analysed'} |
| R9 | D-c: 'analysed' cannot be set by hand | PASS | run_set_status refused |
| R10 | Synergy: built from the tables -- the new observation, OT-11.1 and the new item listed; built_at matches | PASS | reading t-fear: synergy built from the tables -- 4 observation(s), 0 claim(s), 5 block(s), 4 open item(s)   -> C:/Users/lerouxc/AppData/Local/Temp/claude/C--Bible-study-projects/17ac2129-4964-4787-9bc5-5c1c32d28250/scratchpad/t2228r/reading/t-fear/t-fear-synergy.json |
| R11 | Check at gate 2 refused before Apply (the new observation not carried, OT-11.1 open) | PASS | reading t-fear is not past gate 2 (8 gap(s)):   observation 11832 (draft): no current claim carries it and it has no disposition   observation 12409 (draft): no current claim carries it and it has no disposition   observation 12424 (draft): no current claim carries it and it has no disposition   obs |
| R12a | Apply refused: a synergy JSON not built from this reading's tables | PASS | the file is not the synergy JSON built from the tables for reading t-fear (built_at '2026-01-01T00:00:00Z', the reading's '2026-10-23T11:42:57Z'): run Synergy |
| R12b | Apply refused: superseded without naming the carrier | PASS | the synergy is not applied:   open_items[0] (OT-108.3): superseded names the item or escalation that carries it (OT-nn.n or #nnnn) |
| R13 | Apply: new claim on the observation, told in a block; OT-11.1 carried forward (superseded); chapter recorded | PASS | reading t-fear: 1 new claim(s) (C-331), 0 adjusted, 0 withdrawn, 0 held; 4 observation(s) disposed; 1 telling(s); no block rewritten; 4 open item(s) settled (OT-108.3 closed, OT-108.8 closed, OT-11.1 superseded, OT-11.6 closed). Next: Reading.ps1 -Step Check   published: register.md, changes.md, citations.md |
| R14 | Check: gate 2 passed, synergised | PASS | reading t-fear: gate 2 passed -- synergised (Reading.ps1 -Step Publish next) |
| R15 | the anchoring escalation cannot close while the reading is not published | PASS | reading(s) not published: t-fear (synergised) |
| R16 | Publish: the touched chapters in the inbox byte-identical; published; the escalation's gate clear | PASS | reading t-fear: gate 3 passed -- published; 1 chapter(s) touched (00), 0 newly published (-); all in the inbox byte-identical   published: register.md, changes.md, citations.md |
| R17 | Account written | PASS | -> C:\Users\lerouxc\AppData\Local\Temp\claude\C--Bible-study-projects\17ac2129-4964-4787-9bc5-5c1c32d28250\scratchpad\t2228r\reading\t-fear\t-fear-account-v1-20261023.md   reading t-fear: published; 0 |
| R18 | configmaint.validate hard checks on the copy (a migration not yet archived set aside) | PASS | none |
