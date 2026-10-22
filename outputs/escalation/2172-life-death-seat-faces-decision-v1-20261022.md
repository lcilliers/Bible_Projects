# 2172 — Life-death faces on soul, spirit and heart words: where they go

Escalation: #2172. Status: your decision; nothing is written yet.
Researcher, chat 2026-10-22 (verbatim): "put the life-death faces decision to me with options."

## What the faces are

In October, two life-death units gave a face to each hit of an inner-seat word in a death or life
verse. Catch-up B recorded those units' observations on the life and death words in the same
verses. It did not place the faces, because the words they belong to are not life-death strand
words.

| File | Faces | Verses | Words | Face kinds |
|---|---|---|---|---|
| `_analytics/Clusters/M25 - life-death/life-death-q2-faces-v1-20261004.csv` | 123 | 111 | mostly *nep̄eš* (soul, life) and *pneuma* or *rûaḥ* (spirit, breath) | 11 (S01 to S11) |
| `_analytics/Clusters/M25 - life-death/life-death-q3-faces-v1-20261004.csv` | 23 | 21 | *lēḇ* and *kardia* (heart) | 10 (H01 to H10) |

The face kinds read as statements about the inner seat at death. Examples: S03 "The soul dies, or
asks to die" (15), S05 "The soul delivered from death while living" (17), S02 "The spirit and breath
at death" (9), H03 "The heart dies before the body" (2), H09 "The heart in narratives of killing
(data)" (8). S11 "Not the inner being" (9) and H10 "Idiom: the heart of the seas" (1) mark hits as
outside the inner being.

**Checked in iba.db:**
- Of the 146 faces, one sits on a word that belongs to a strand. The rest belong to no strand: no
  strand has been defined for soul, spirit or heart (M47 Inner Seat).
- No open item names these files. M47 has open items on other threads (#2006.11, #2095.2,
  #2103.4), not for these faces.
- **A limit:** each face is tied to its word by position in the verse. About one in ten positions
  lands on a neighbouring token (for example the object marker H0853). Whichever option you choose,
  each face is re-checked against its verse when it is placed.

## Options

| Option | What happens | Effect |
|---|---|---|
| **A. An open item for the inner-seat strand** | One open item on thread OT-108 names both files. `Escalation.ps1 -Action Match` finds it when a strand on soul, spirit or heart is defined. That strand's Record then places each face on its own hit, re-checked against the verse. | Nothing is lost, and no strand is started for this alone (rule 84: a strand is taken in turn, with no backfill). The faces wait until that strand is read. |
| **B. Define an inner-seat strand now, only to hold them** | `Strand-Reading.ps1 -Step Define` for the soul, spirit and heart words, then `Context` writes every hit of those words. The 146 faces go on their hits. | The faces are placed now, but the strand is opened with thousands of unread hits it was not started to read. |
| **C. Record them as observations on the life-death strand** | Each face kind becomes an observation grounded on the life or death word in its verses. | It duplicates what catch-up B already recorded from the same units, and grounds statements about the soul on the death word. |
| **D. Leave them in the files** | No record. The two CSVs stay as they are. | The October faces are reachable only by finding the files: the gap #2172 names. |

**Claude recommends A.** It keeps the faces findable at the point where they are used. It follows
the way the October readings were registered (OT-108.3 to OT-108.9), and it starts no strand for
the sake of the record.

## Decision

| | Your choice | Comment |
|---|---|---|
| A, B, C or D | | |
