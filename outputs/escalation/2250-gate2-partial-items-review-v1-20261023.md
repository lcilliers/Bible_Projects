# #2250 -- Reading gate 2 forces settling open items that reach past the scope

Found opening reading `m64-choose` (#2247 batch A: M64 Will & Resolve, the choose words, 185
verses; `outputs/reading/m64-choose/m64-choose-gaps.json`).

Researcher 2026-10-23 (#2247 v3), verbatim: "It seems to me that this reading is focussed on giving
context of thought as the central theme rather that other dimensions that may come out of the same
verses.  this may mean that verses that may have multiple dimensions of interpretation (e.g. what is
the will, how does the verses elaborate on the IB) may need to be pushed forward in new open items."

## What a reading does with other dimensions (from the config and the gap JSON)

- **Not thought-led.** The gap guides (`cfg_setting reading.gap_types`) ask what each verse "states
  about the inner being". For the 171 verses the October files read, they ask that the files'
  reading be carried into a table. The origin-of-thought framing belongs only to OT-108.18, which
  is read in batch C.
- **Dimensions already registered come to the reading.** Every open item whose target shares a verse
  with the scope is matched, and gate 1 records what the reading found for it. Batch A matched 15,
  and most are not about thought:
  - OT-92.1: what God's choosing says of God, for 13.1;
  - OT-92.3: God's replies to the one who chooses;
  - the M18, M72, M07 and M08 catch-up items;
  - five anger pairings (OT-103);
  - OT-03.1: spirit and soul at death;
  - OT-05.29: raise and arise.
- **A new dimension a verse opens is pushed forward**, as you supposed. It is recorded as a
  `new_items` entry at gate 1 (`Open-Item.ps1` shape): what to read for, its verses, when it comes
  back. "What is the will" is the subject of batches A and B themselves (choosing, willing), so it is
  recorded there as observations, not pushed on.

## The gap: settling at gate 2

Gate 2 (`iba/app/lib/reading.py`, `SETTLE`, line 51) passes only when every matched open item is
closed, withdrawn, superseded or carried forward. "Carried forward" supersedes the item and raises
a successor. None of the 15 items lies wholly inside batch A:

| item | its verses in batch A | its target |
|---|---|---|
| OT-108.3 (M64 catch-up) | 185 | the M64 files |
| OT-92.1 (God's choosing, for 13.1) | 124 | 166 verses |
| OT-108.4 (M72 catch-up) | 26 | the M72 files |
| OT-108.8 (M18 catch-up) | 21 | the M18 files |
| OT-108.5 (M08) / OT-108.7 (M07) | 4 / 3 | their files |
| OT-92.3 (God's replies) | 3 | 8 verses |
| OT-03.1, OT-05.29, OT-103.4, .8, .9, .12, .25, .39 | 1 each | 9 to 124 verses |

As built, batch A's gate 2 would supersede all 15 and raise 15 successors, and batches B, C and D
would do the same to whatever they match. The open items would be renumbered after every reading,
each successor carrying a part of the same question.

## Options (decision)

- **A. Read in part (recommended).** An item whose target reaches past the reading may be settled as
  `touched`: what the reading found for its verses is recorded (gate 1 already writes it), and the
  item stays open under its own handle. It is closed in the reading that reads its last verses, or
  in synergy when the reading answers it whole. Gate 2 still refuses an item that lies wholly inside
  the scope and is left open. Change: `iba/app/lib/reading.py` (the gate 2 check and Apply's
  `settle`), using each item's target against the reading's verses; a test plan; USER-GUIDE.md
  sec 8.2.
- **B. As built.** Every matched item is settled in each reading; an item reaching past it is
  carried forward to a successor. Nothing to build, but there are many successor items, and one
  question is spread over several handles.
- **C. Match less.** Only items wholly inside the scope are matched for settling. The rest get a
  `touched` response at gate 1 and are listed as "read in part", outside gate 2. Simpler than A, but
  an item that the reading does answer in full cannot be closed here unless it lies wholly inside.

Batch A's recording (gate 1) does not depend on this choice. It can go ahead now, and the choice is
needed before its Apply.

Decision: ______
