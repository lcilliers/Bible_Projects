# Fear strand — handoff for the next chat

**Date:** 2026-10-01 · **State:** units 1 (#1928) and 2 (#1929) woven · **Next:** unit 3 (terror, horror, desolation)

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
2. `fear-observation-ledger-v1-20261001.md` (faces A–J, FE-01 to FE-46) and `fear-observation-ledger-unit2-v1-20261001.md` (faces K–T, FE-47 to FE-85): the format to copy, and "Woven — where". Unit 3 continues from FE-86 and face U.
3. `Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md`: the rules for chapter text.

## Data and method (do not re-derive)

**Data.** `fear-web-pull-v1-20261001.csv` (query: `fear-web-pull-query-v1-20261001.sql`, filter `<> 'M01'`). It holds every M01 hit in 916 verses, with the co-occurring clusters.

**Unit pull pattern.** See `fear-unit1-yare-family-pull-v1-20261001.csv`:
- one row per hit
- the full ESV text from iba.db `verse`
- a **face** column, so every verse is accounted for

**Read by surface first** (memory `feedback_surface_is_the_sensitivity_lens`). The Strong's suffix or gloss does not decide the face.

**The "negated" flag is approximate.** Assign faces by reading.

**Quote check.** Every added quote is checked against iba.db `verse` with `fear-quote-check-v1-20261001.py` (rebuilt in unit 2; kept in this folder). Run it on a ledger, or on a chapter file with `--prose`.
- It handles "19, 21" citations, ranges, the book carried forward, [bracketed insertions] and quotes running across verses.
- `--prose` checks chapter files (full book names mapped). Known noise on older lines: a bare "(143:3)" can be read against the wrong carried-forward book.

## Unit 2 (done)

- *paḥad* and the Hebrew trembling and shuddering words. Ledger: `fear-observation-ledger-unit2-v1-20261001.md` (FE-47 to FE-85); data: `fear-unit2-pahad-trembling-pull-v1-20261001.csv`.
- Scope decision: every Hebrew M01 entry glossed tremble / trembling / quivering / shudder / shuddering, including H6206.

## Unit 3 scope

- terror / horror / desolation: H0367, H4288, H8047G/H, H1091, H2851, H4032, H2189 and the other terror and horror entries in candidate v2 §2, with the §3A.3 non-fear surfaces
- Build the pull from iba.db as in unit 2 (`fear-unit2-pahad-trembling-pull-v1-20261001.csv` is the pattern), not by filtering the web pull.

**Unit 4 (later):**
- the Greek *phobos* group (incl. "respect") and Greek trembling (G5156, G5141, G1790)
- claim 9-4 (2Ti 1:7, "spirit of fear")

## Current versions after unit 2

- **Chapters:** 03 v5 · 05 v3 · 06 v4 · 09 v4 · 10.1, 10.2, 10.5, 10.7 v5 · 10.8 v4 · 10.9, 10.10, 11, 12, 14 v6 · 13 v3 · 15 v4
- **Claim register:** v6
- **Index:** Structure log row added
