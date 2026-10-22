# 2228 — Why a subset forces a whole-strand rebuild

Escalation: #2228 (from #2172). Status: diagnosis for your decision; nothing is built.
Researcher, chat 2026-10-22 (verbatim): "We cannot go into a complete rebuild everytime a subset is
being visited or revisited. there is something materially wrong in how the whole infrastructure is
fitting together and how the analytic process is recorded."

Read from the code: `iba/app/lib/strandreading.py`. The case: 26 rows of anger at the inner seat on
43 verses, recorded on strand anger.

## What is wrong

**1. The only unit of work is the whole strand.** Every step takes `-Strand` and nothing narrower.
- `related_blocks()` collects every narrative block that cites any verse where the strand has a hit,
  or that tells a claim resting on those verses or observations. For anger that is 178 blocks.
- `map_blocks()` refuses unless every one of those blocks is in the one mapping file ("is related to
  the strand and not mapped").
- So carrying 26 observations on 43 verses into the claims means mapping all 178 blocks.

**2. A mapping done once is not kept as a state.** Map records tellings, but not that a block was
mapped, against which version, or for which observations. The next visit to the strand cannot tell
what is already current. It has to map all 178 blocks again, even when only one verse changed.

**3. What was read is recorded inside one strand's silo.** An observation belongs to a strand
through that strand's hits (`strand_observations()`, the strand stage).
- The 26 inner-seat rows are about the heart, soul and spirit. They are grounded only on the anger
  words in their verses, so the inner-seat side has no record of them.
- The October life-death faces have the same problem: they sit on soul, spirit and heart words, and
  no strand holds those words.
- A verse read in two strands gets two unconnected sets of observations. `verse_meta.status`
  (analysed, citated) says a verse was read, not in which respect.

**4. "Done" exists only as the strand's close gate.** `account_gaps()` asks three questions of the
whole strand: every hit faced, every observation disposed, every matched item answered. No record
says "this verse's reading reached these claims, these blocks, these items". A revisit therefore has
no state to start from, only the strand's full gaps.

These four together are why a visit to a subset turns into a rebuild. Points 1 and 2 are about
scope; points 3 and 4 are about how the analysis is recorded.

## Directions, for your decision (none designed in detail, none built)

| # | Direction | What it changes |
|---|---|---|
| 1 | **A scope on every step.** Each step takes a set of verses or observations. Gather and Map cover only the blocks touching that set, and the gate is "every block touching this set is mapped". | A subset is carried alone. The strand stays as the lens it was read through. |
| 2 | **Mapping kept as a state.** A mapped block records its version and the observations it was mapped against. A revisit re-maps only blocks whose text changed, or whose verses gained observations since. | Revisiting costs the change, not the strand. |
| 3 | **Observations grounded on every inner word they speak of.** The strand stays a tag on the observation, not its container. The inner-seat rows would then be grounded on the heart, soul and spirit words too, and an inner-seat strand would find them. | One record per verse reading, seen from every strand it bears on. Ends the silo. |
| 4 | **"Done" recorded per verse and per observation:** reached a claim (which), held on an item (which), silent or withdrawn. The strand's account and close gate are built from these. | The completeness you asked for in #2172 becomes checkable per verse, not only per strand. |

Claude's reading: 1 and 2 fix the cost; 3 and 4 fix how the analysis is recorded. 3 and 4 are the
"material" part of what you named. They touch `recordingpass` and the claims register, not only the
reading steps.

## What stops meanwhile

- #2172 catch-up C (claims linked to observations, strand by strand) waits on this. Run on the
  present code, it would be the whole-strand rebuild you rejected.
- The 26 observations recorded today stay at draft. Nothing more is written on them until this is
  settled.

## Decision

| | Your choice | Comment |
|---|---|---|
| Which directions to design (1, 2, 3, 4, or a different framing) | | |
| Design now, or a wider review of how the tables fit together first | | |
