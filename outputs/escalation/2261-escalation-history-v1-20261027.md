# Escalation deep history

## #2261 — Reading records observations in the strand-ledger shape
type=issue source=researcher

**v1** (2026-10-24T04:56:06Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Reading records observations in the strand-ledger shape
> **comment (set this version):** From #2260 (findings outputs/escalation/2260-observation-quality-findings-v1-20261024.md section 1). iba/app/lib/recordingpass.py record_strand_observations (lines 571-601), used by iba/app/lib/reading.py at gate 1, writes every observation with stage strand-reading, tag key-statement, no question code, no window, no word role, and strong null unless the words are one code. The rows are multi-verse summaries (6.5 verses per reading observation, max 42), not per-occurrence, span-grounded observations: cfg_method_rule 108, 112, 119, 121 and cfg_behaviour_rule 73 are not met. Gate 1 must write observations to the observation rules.
> **context (set this version):** outputs/escalation/2260-observation-quality-findings-v1-20261024.md

**v2** (2026-10-24T05:28:07Z, Claude) state=on-hold next_action=review assigned_to=Claude
> **comment (set this version):** Carried by the design proposed on #2268 (outputs/escalation/2268-reading-process-against-study-expectations-v1-20261024.md, gaps table). On hold until the researcher decides #2268; no separate fix is built for this item (B:105).
