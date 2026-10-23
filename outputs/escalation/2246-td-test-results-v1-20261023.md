# #2246 T-d date rule -- test results

Run on a copy of iba.db (C:\Users\lerouxc\AppData\Local\Temp\claude\C--Bible-study-projects\0e1dad0b-9f09-4558-ae0f-a900ebc06b67\scratchpad\t2246\iba.db); strong used for cases 3 and 4: G0275.

| case | result | got | expected |
|---|---|---|---|
| 1 real: the five OT-108 items are not T-d | pass | [] | [] |
| 2 synthetic: cluster item opened before the strand is T-d | pass | True | True |
| 3 synthetic: strong item opened before the strand is T-d | pass | True | True |
| 4 synthetic: strong item opened after the strand is not T-d | pass | False | False |
| 5 synthetic: cluster item opened a day before the strand is T-d | pass | True | True |
| 6 the other four real items stay clear | pass | [] | [] |

6/6 pass
