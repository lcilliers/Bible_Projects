# Claude Code Directive
## Registry 064 — forgiveness
## GOD_AS_SUBJECT Flag Inserts
**Produced by:** WA-SessionB-Instruction-v4.7 — Stage 2 Pass 2
**Date:** 2026-04-12
**Directive ref:** wa-064-forgiveness-sessionB-cc-directive-v1-2026-04-12.md

---

## Context

Per WA-Reference Section 13.3, the `wa_term_inventory.god_as_subject` field is redundant. The authoritative record for God-as-subject is the `mti_term_flags` table using flag_id 1 (GOD_AS_SUBJECT). This directive instructs Claude Code to insert the correct flag records.

Session B Pass 2 analysis established that 5 of the 7 terms in registry 064 (forgiveness) have God as the primary or significant acting subject in their verse corpus, but have `god_as_subject = 0` in wa_term_inventory. This is the known programme-wide automation gap.

---

## Terms requiring GOD_AS_SUBJECT flag

| Term | Strong's | Basis |
|---|---|---|
| G0859 (*aphesis*) | G0859 | Groups 879-001 and 880-001: forgiveness as God's act and gift throughout; "forgiveness of sins" consistently given by God through Christ |
| G0863H (*aphiēmi* — to release: forgive) | G0863H | Group 5377-001 (26 verses): Jesus/God as primary acting subject; Jesus pronounces forgiveness as a divine prerogative |
| H5545 (*sālach*) | H5545 | Groups 5379-001/002/003: exclusively God as subject in all 49 OT occurrences; this is the defining lexical characteristic of *sālach* |
| H5546 (*sallāch*) | H5546 | Group 5380-001 (Psa 86:5): single occurrence, used exclusively of God ("you are forgiving") |
| H5547 (*selichah*) | H5547 | Group 880-001 (Psa 130:4, Dan 9:9, Neh 9:17): forgiveness as a divine possession ("with you there is forgiveness"; "to the Lord belong mercy and forgiveness") |

---

## Required action

For each term above, insert a record into `mti_term_flags` with:
- `flag_id`: 1 (GOD_AS_SUBJECT)
- `mti_term_id`: the `mti_terms.id` for the relevant term (to be looked up by Strong's number and owning registry)
- `flag_value`: 1
- `notes`: "Set by Session B Pass 2 analysis — wa-064-forgiveness 2026-04-12"

Please confirm the mti_terms.id for each Strong's number before inserting, and confirm completion with a count of inserted records (expected: 5).

---

## Note on G0863G and G0863I

These two terms do NOT require the GOD_AS_SUBJECT flag:
- G0863G (to release: leave): human subjects throughout the leave/abandon corpus
- G0863I (to release: permit): mixed subjects; Jesus does permit in some verses but this is not a consistent divine-attribute use; the permit sense is not a God-as-subject dominated usage

---
