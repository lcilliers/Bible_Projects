# Fear strand — handoff for the next chat

**Date:** 2026-10-01 · **State:** unit 1 woven (#1928 approved and applied) · **Next:** unit 2

## Working rhythm

Researcher, 2026-10-01: commit and close after each unit, to control tokens.

Each unit runs in this order:
1. pull
2. read by surface
3. ledger
4. researcher approval
5. weave
6. records
7. session-close (commit + push)

Then a new chat starts the next unit.

## Read first, in this order

1. `fear-strand-candidate-v2-20261001.md`: the reading order (§5) and the surface tables (§3A).
2. `fear-observation-ledger-v1-20261001.md`: the faces A–J and FE-01 to FE-46 (the format to copy), and "Woven — where".
3. `Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md`: the rules for chapter text.

## Data and method (do not re-derive)

**Data.** `fear-web-pull-v1-20261001.csv` (query: `fear-web-pull-query-v1-20261001.sql`, filter `<> 'M01'`). It holds every M01 hit in 916 verses, with the co-occurring clusters.

**Unit pull pattern.** See `fear-unit1-yare-family-pull-v1-20261001.csv`:
- one row per hit
- the full ESV text from iba.db `verse`
- a **face** column, so every verse is accounted for

**Read by surface first** (memory `feedback_surface_is_the_sensitivity_lens`). The Strong's suffix or gloss does not decide the face.

**The "negated" flag is approximate.** Assign faces by reading.

**Quote check.** Every added quote is checked against iba.db `verse`. The checker script was a scratchpad file, so rebuild it.
- Map OT and NT book names.
- Handle "19, 21" citations and quotes inside parentheses.

## Unit 2 scope

- *paḥad* H6343 "dread" (49 hits), H6342 "to dread" (24), H6345.
- The trembling words: H2729 / H2730 / H2731 *ḥārad*; H7264 *rāgaz* (its surfaces include raging, enraged, quarrel, deeply moved, disturbed: links to the anger strand); H7460–H7461; H2111–H2113; H2342A; and the other shudder/tremble entries in candidate v2 §3A.
- **Isa 8:13** ("Let him be your fear, and let him be your dread"), held over from FE-19.

**Units 3–4 (later):**
- terror / horror / desolation (incl. the §3A.3 non-fear surfaces)
- the Greek *phobos* group (incl. "respect")
- claim 9-4 (2Ti 1:7, "spirit of fear")

## Current versions after unit 1

- **Chapters:** 03 v4 · 06 v3 · 09 v4 · 10.1, 10.2, 10.5, 10.7, 10.8 v4 · 10.9, 10.10, 11, 12, 14 v5 · 13 v2 · 15 v3
- **Claim register:** v5
- **Index:** Structure log row added
