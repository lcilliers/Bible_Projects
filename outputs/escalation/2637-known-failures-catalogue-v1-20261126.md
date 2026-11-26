# #2637 Known failures of the reading package: the regression catalogue (v1, 2026-11-26)

Source: every escalation raised by a `collection.*` step, first version, `escalation.context` `full_message`; 68 escalations, 75 distinct problem lines after ids and quoted text are normalised. Query: `SELECT id, at_step, context FROM escalation e WHERE at_step LIKE 'collection.%' AND version = (SELECT min(version) FROM escalation e2 WHERE e2.id = e.id)`. The manual interventions on boast are in `outputs/escalation/2637-manual-interventions-boast-boasting-v1-20261126.md`.

Each class below becomes at least one regression case in the #2637 test suite: the case feeds the failing input and expects either the pre-check to name it before the record, or the package to make it impossible.

| # | Class | Lines | Steps | Root cause | How the build anticipates it |
|---|---|---|---|---|---|
| K1 | Occurrence not one the row may name | 44 | 3.1 | The packet does not list which occurrences each observation covers | The packet gives each observation's covered occurrences; the form builds the nodes from the observations a finding rests on (X1, X2) |
| K2 | Text restates the verse (copy limit) | 35 | S1, 2.1, 3.1 | The limit is checked only at record | CheckAnswer measures each text against its verses and names the run of words (X3) |
| K3 | Grounds not words of the verses or lexicon | 30 | S1, 1.2, 2.1 | The rule (one unbroken phrase of one verse; lexicon words for 1.2) is not stated | The rule printed in the packet; CheckAnswer names the nearest matching phrase of the verse (X3, X4) |
| K4 | An observation not rested on nor in not_used | 20 | 3.1 | The form does not list every observation | The form lists every observation with a disposition slot (X2) |
| K5 | Text names none of its verses | 11 | S1, 1.2, 2.1 | Reference forms not stated; common forms refused | Common forms accepted and normalised; the packet's form printed (X4) |
| K6 | Qualification needs qualifier and characteristic | 8 | 3.1 | Partner occurrences not allowed in 3.1 | The researcher's G3 decision: partner occurrences allowed for a qualification judged to bear on the working (§5 of the plan) |
| K7 | Normal progress raised as a hard error | 13 | read_words, read_senses, read_enrichment, read_structure, read_sweep, read_evidence | "Nothing to read" and "next step is X" exit as errors and raise escalations | Exit 0 with the next command; no escalation (X5) |
| K8 | Form and parameter errors | 10 | 3.1, evidence, 2.1 | Field names, allowed values and action parameters not in the form | The form carries every field with its allowed values; actions with their parameters (X2, X4) |
| K9 | Older-observation answers refused | 7 | S1, 2.1 | merge needs identical text; consume needs carriers in later packets; deferral text length; traces to repair first | merge on meaning (C4); consume across the subgroup (C6); the limits printed; traces repaired by the package (X2, X4) |
| K10 | Crashes | 6 | ask, export_members, evidence, layer_check, read_enrichment, record_evidence | File held by another process; database locked; a scan where a lookup was meant; a key error; a missing answer file | Trapped: retry on lock (configured count and wait), a named message for a missing file, the traceback kept in the failure log (X8) |
| K11 | Package too large | 1 (and A1 of boast) | 3.1 | One package for a whole subgroup | Split into numbered parts by size (X1) |
