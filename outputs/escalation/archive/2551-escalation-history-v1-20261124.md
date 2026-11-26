# Escalation deep history

## #2551 — Design: correction table for stored span errors (#2541 A)
type=task source=researcher

**v1** (2026-11-24T12:57:23Z, Claude) state=on-hold next_action=review assigned_to=Claude
> **short description (set this version):** Design: correction table for stored span errors (#2541 A)
> **comment (set this version):** Researcher approved option A in principle on #2541 v5: a small correction table keyed on span_id and code_ordinal (field, stored value, corrected value, reason, escalation), read by lexical.py when it writes a verse_lexical row, each application recorded in cfg_change_detail; span stays immutable. Covers 1Cor 2:11 G3588 empty morph, Eze 19:10 H1961 surface, Rom 4:19 G3756 negation target. Condition: the schema comes back as a design here before any build.
