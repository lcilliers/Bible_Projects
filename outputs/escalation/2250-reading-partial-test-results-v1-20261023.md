# 2250 -- reading gate 2, items read in part: test results (v1)

Run on a copy of iba.db (C:\Users\lerouxc\AppData\Local\Temp\claude\C--Bible-study-projects\0e1dad0b-9f09-4558-ae0f-a900ebc06b67\scratchpad\t2250\iba.db).

**5/5 passed.**

| Case | What | Result | Evidence |
|---|---|---|---|
| P0 | set-up: opened, recorded, gate 1 passed, synergy built; OT-11.1 reaches past the 3 verses, the new item (Mar 6:50) lies inside | PASS | ['reading t-part opened (#2172, home M01): 3 verse(s); gaps hit_unread 1, meaning_', 'reading t-part: 6 record(s) written (1 observation(s)); 1 open item(s) added (OT', 'reading t-part: gate 1 passed -- recorded; 1 verse(s) marked analysed (D-c)', 'reading t-part: synergy built from the tables -- 4 observation(s), 0 claim(s), 5']; past {'OT-108.3': True, 'OT-108.8': True, 'OT-108.18': True, 'OT-11.1': True, 'OT-11.6': False} |
| P1 | Apply refused: touched on an item whose target lies wholly inside the reading | PASS | the synergy is not applied:   open_items[4] (OT-11.6): its target lies wholly inside the reading -- settle it closed, withdrawn, superseded or forward (touched is for an item read in part, #2250) |
| P2 | Apply refused: touched with no found | PASS | the synergy is not applied:   open_items[3] (OT-11.1): touched needs found |
| P3 | Apply with OT-11.1 not settled, then Check at gate 2 refused naming OT-11.1 | PASS | reading t-part: 1 new claim(s) (C-331), 0 adjusted, 0 withdrawn, 0 held; 4 observation(s) disposed; 1 telling(s); no block rewritten; 4 open item(s) settled (OT / reading t-part is not past gate 2 (1 gap(s)):   OT-11.1: still open (settle it: closed, withdrawn, superseded or forward; or touched when its target reaches past the reading) |
| P4 | Apply: OT-11.1 touched (read in part) and still open; gate 2 passed, synergised | PASS | reading t-part: 1 new claim(s) (C-332), 0 adjusted, 0 withdrawn, 0 held; 4 observation(s) disposed; 1 telling(s); no block rewritten; 1 open item(s) settled (OT-11.1 touched). Next: Reading.ps1 -Step  / reading t-part: gate 2 passed -- synergised (Reading.ps1 -Step Publish next) / ('touched', 'Mar 6:49-50 read: the troubling is answered by his word before the calm (reading t-part, #2228 gate 2, read in part)') |
