# #2406 — design of the step before narration: what is engaged in the inner being (v2, for approval)

Nothing is built (B:105). This version records the researcher's decisions D1 to D5 and the design that follows from them, with the questions still open. Basis: `outputs/escalation/2406-aloud-collection-split-and-surfaces-v1-20261109.md` (the exploration). Table facts were read from the live `cfg_table` / `cfg_column` meanings, `iba/app/USER-GUIDE.md` section 8.2 and the code; proposals are mine and inferential (B:4).

## The decisions (researcher, verbatim, 2026-11-09, chat)

> "D1 - I will support your method, it seems to be a mechanical call on how to code works to safeguard processing; D2 - if it serves both at the same time - then the assignment is behaviour (behaviour by definition would include state) however, if it is one type in some verses, and another in other verses, then it become separate observations for the separate verses. D3 - it starts off with one observation per surface, but recognising that it may be nuanced in other verses, which means it becomes another observation for the same surface wich may apply to one or more verses. D4 record as observation. note it relates to the surface, not the whole verse. if the verse have multiple surfaces it may be read a few times before all surfaces in the verse set aside the entire verse. D5. Initially claude will do this reading and writing, and updating the DB. The ultimate aim is to structure the prompts for ollama so ollama can perform the bulk operation. I suggest that the first step in the process is a pull of the collection and its relevant data into a working file to isolate it from the db and prevent ai changing its ways everytime a collection is past in. Note that the current observations for the verses must be past in to be taken into account."

## The step, in order

1. **Pull (new, read-only):** one collection into a working file: the collection, its links and tiers, its member surfaces, each surface's verses with the ESV text, and for each verse the observations and nodes already recorded (`ib_observation`, `ib_node`), so earlier findings are taken into account. The file isolates the work from the database; the assessment reads the file, not the tables.
2. **Assess each surface from its verses:** one sentence of what the surface does for the inner being. One observation per surface (D3). Where the surface does something different in other verses, that is another observation for the same surface, applied to those verses only (D2, D3).
3. **Write (by Claude, D5):** the observation and one node per verse where it is true, through the reading process's recording (`observationrecord.py`), with the reason of any change kept in `ib_observation_change`.
4. **Group (D1, D2):** the draft `surface_group` of the surface is replaced in one write by the assessment's result, the old value kept in `surface_event`, so the surface never sits at NULL. A surface that serves both act and state in the same verses is `behaviour`. A surface that is one type in some verses and another in others gets separate observations for the separate verses.
5. **Review of what was left out (D4):** the verses of the collection not covered by any surface assessment are read again, surface by surface. What is found is recorded as an observation about the **surface** in that verse, not the whole verse; where the surface has no inner-being bearing in the verse, that is the observation. A verse is set aside as a whole only when every surface in it has been set aside, which may take several readings of the verse.
6. **Later (D5):** the prompts are structured so that `qwen3:30b` can do the bulk. The working file, one collection at a time, is what keeps a prompt's input the same shape for every collection; the prompt is written and tested only after Claude has done the first collections.

## What this needs built (outline, to be detailed after approval)

- a **pull** step for a collection into a working file (a `ps` entry point, a handler, a lib, `cfg_utility` / `cfg_step` rows and settings for its folder and limits; B:41, B:62);
- a way to **open a reading on a collection** (the reading process opens on a cluster or subgroup today, `Reading.ps1 -Step Open`; a collection scope is new, or the pull file stands in for the scope JSON);
- the **group replacement** write with its `surface_event` row (like `set_group` in `iba/app/lib/surfacegroup.py`), refused unless an assessment observation exists for the surface;
- a **check** that every member surface of the collection has an assessment observation and every collection verse has been covered or set aside, with a report at a configured path;
- **USER-GUIDE.md and BUILD.md** entries, and a **test plan** run on a copy of the database (B:46, B:29): collections with a single-type surface, a mixed surface, a shared surface, a verse with several surfaces, a verse with none included, and a refusal when no assessment exists.

## Still open (my questions, none decided)

- **R1. What the group of a mixed surface is.** D2 says separate observations per verse when a surface is one type in some verses and another in others, but `surface_term.surface_group` has one value per surface. Does the group then follow the larger set of verses, stay as the draft, or is the group read from the observations and the column kept only for the surface cycle? (This is where the surface cycle's use of the column, in my v1, still bites.)
- **R2. The observation kind.** The kinds of a finding are face, qualification, party, statement, link, use, term and silence (`reading.observation_parts`); the surface sentence is closest to `use` or `statement`. And "no inner-being bearing" for a surface in a verse has no kind of its own (silence is stated as not used by Analysis_phase_1). Which kinds, or is a new kind or tag wanted?
- **R3. Node roles.** The roles of a new node are characteristic, qualifier, or for a surface that bears on the act: object, relational target, enactment. Which role does a surface take when the finding is about the surface itself?
- **R4. The pull's reach.** The export used so far lists member surfaces only. Should the working file also carry the collection's associated, possible-opposite and set-aside words, and their verses, for the review in step 5?

## Approval sought

Approve this design for building (the outline above), and answer R1 to R4, or tell me which of them to settle in the detailed design after you have seen it.
