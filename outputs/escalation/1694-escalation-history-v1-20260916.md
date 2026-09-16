# Escalation deep history

## #1694 — 37 M-codes in cluster_strong have no cluster table row
type=issue source=researcher

**v1** (2026-09-12T07:28:01Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** 37 M-codes in cluster_strong have no cluster table row
> **comment (set this version):** Found live while investigating #1683/#1690 (M10 family-vs-legacy-subgroup comparison, outputs/markdown/1682-m10-family-vs-legacy-subgroup-comparison-v1-20260912.md §4) -- not a small edge case: cluster_strong (iba.db) has 99 distinct cluster_code values; 51 have no corresponding row in the cluster catalogue table (bible_research.db). 37 of the 51 are M-codes -- M32, and the entire M48-M84 range -- with real, non-trivial row counts (M55: 72 rows, M72: 54, M73: 51). CLAUDE.md's own directory map only documents M01-M46/FLAG/T2. The other 14 unregistered codes are T3-T15 (some very large, T3: 2,586 rows, T8: 1,787) -- NOT flagged as the same kind of gap here, since escalation #1606's own T-code sweep work treats T3-T15 as an active, already-tracked classification, separate from the M-code cluster catalogue. Question: should M32/M48-M84 be registered in cluster per governance.tables, or is there a reason this range was never catalogued (e.g. superseded, a different classification scheme entirely, pending a batch registration)?
> **context (set this version):** Surfaced during #1683/#1690 investigation. Related: escalation #1598 (Reallocation of M/T-code clusters) may be the origin of this range -- not confirmed.
