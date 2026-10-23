# 2228 — The reading process: gaps recorded, synergy from the tables, published (design v1)

Escalation: #2228 v25. Status: **design for your review; nothing is built** (rule 105). It carries out
your decisions D.1 and D.2 of 2026-10-23 (verbatim on #2228 v25) on top of the tools already built:
`Verse-Scope.ps1` (the scope), `Reading-Index.ps1` (the cluster files) and `Verse-Collate.ps1` (what
is known, and the gaps). The facts about today's code are from `iba/app/lib/strandreading.py` and
`iba/app/lib/narrativeregister.py`.

## 1. The shape: one reading, three gates

A **reading** is the work on one scope. It is opened from a scope request, served by the escalation
that anchors it, and closes through three gates in order:

| Gate | Phase | The reading is past the gate when |
|---|---|---|
| **1 Recorded** | Record the gaps | every item in the reading's **gap JSON** carries the id of the row that recorded it, or a stated reason |
| **2 Synergised** | Claims and narration, **from the tables** (B:114) | the **synergy JSON**, built by reading the tables for the scope, is cross-referenced: every observation to a claim (or a disposition), and every claim to a narrative block (or held with a reason) |
| **3 Published** | Publishing | the narrative chapters the reading touched are published from the database, and their current files are in the learning4comfort inbox, byte-identical |

States: `open` → `recorded` → `synergised` → `published` (closed). Gate 2 cannot start before gate 1,
which is the session break you foresaw. Each gate is checked by the tool, not asserted.

**A strand becomes one kind of reading:** a scope of a word family. The four existing strands keep
their rows, and their observations and faces are read like any other table source. (D-a, section 6.)

## 2. Gate 1: the gap JSON (D.1)

`Reading.ps1 -Step Open -Label <name> <scope selectors> -Escalation <id>` resolves the scope (the
2,500 review applies), collates it, and writes the reading's gap JSON: **one section per gap type**,
each section carrying its own instruction, so every type is considered and nothing is skipped.

```json
{
  "reading": "anger-bosom", "escalation": 2172, "scope": { "...": "the resolved request" },
  "sections": {
    "not_read": {
      "guide": "A verse with no observation and no strand face. Read it; record what it states about the inner being, or the reason it holds nothing.",
      "records_in": "ib_observation",
      "items": [
        { "verse": "Ecc 7:9", "words": ["anger (H3708A, M02)"], "known": "file lines: 3",
          "record": null }
      ]
    },
    "read_in_files_only": { "guide": "...", "records_in": "ib_observation", "items": [] },
    "hit_unread":         { "guide": "...", "records_in": "reading_strand_hit", "items": [] },
    "meaning_missing":    { "guide": "...", "records_in": "strong_meaning_tree | strong_lexicon", "items": [] },
    "open_item":          { "guide": "...", "records_in": "escalation_thread_item_response", "items": [] }
  }
}
```

- **Writing back.** Each item's `record` is filled with the reading, then written by
  `Reading.ps1 -Step Record -File <gap JSON>`. One of:
  - **`{"new": {…the observation, face or response…}}`:** written to its table. The id is written back as `{"table": "ib_observation", "id": 12510}`.
  - **`{"table", "id"}`:** an existing row that already covers the item.
  - **`{"reason": "…"}`:** nothing to record, and why.

  The file keeps every id, so the JSON is the reading's record of what was done.
- **The gap types are config,** not code: `cfg_enum reading_gap_type`, each with its guide text, phase
  (recording or synergy) and the table it records into. This is the template. Adding a gap type
  learned later is a config row. The two synergy gaps (`observed_no_claim`, `claim_not_told`) are not
  in the gap JSON; they are gate 2's work.
- **The writes reuse what exists:** observations through the strand Record code (grounding,
  quotation checked against the ESV text, `supersedes`), faces on `reading_strand_hit`, responses on
  thread items, meaning pulls through the spine route.
- **Gate 1 check:** `Reading.ps1 -Step Check` passes when every item has a `record` with an id that
  exists, or a reason. The reading then moves to `recorded`, and its verses are marked `analysed`
  (D-c).

## 3. Gate 2: synergy from the tables (D.2)

`Reading.ps1 -Step Synergy` starts by **reading all the tables for the scope**, never memory or the
conversation, and writes the synergy JSON:

| Section | From the tables | To be filled |
|---|---|---|
| `observations` | every observation on the scope, with any recorded at gate 1 | `claim`: an existing claim ref, a new claim (key), or a disposition (held on an item, silent, withdrawn) with a reason |
| `claims` | every current claim resting on the scope's verses or observations | `told_in`: the block(s), or `held` with a reason; `edit` / `withdraw` where the observations change it |
| `blocks` | every narrative block citing the scope or telling those claims, with its text | the rewritten text, where the claims change it |

`Reading.ps1 -Step Apply -File <synergy JSON>` writes these changes with the code that already does
it:
- **claims:** new, edited or withdrawn. Each claim source names its **observation**, filling the
  claim source → observation link that is empty today.
- **blocks:** rewritten whole, through `narrativeregister.rewrite`.
- **citations:** re-derived.

The ids go back into the file. **Gate 2 check:** every observation in the scope is cross-referenced to
a claim or disposition, and every claim to a block or a stated hold. Then `synergised`.

## 4. Gate 3: published

`Reading.ps1 -Step Publish`:
1. publishes the chapters the reading touched from the database (`publish_chapter`, as Rewrite does now)
2. runs the copy to the learning4comfort inbox (`Copy-NarrativeToLearning4Comfort.ps1`)
3. checks that each touched chapter's current file is in the inbox, byte-identical (the copy keeps no
   log, so the check reads the files)

Then `published`, and the reading closes.

## 5. What is built (after your approval)

- **Tables:** `reading` (label, escalation, request, state, the gate times) and `reading_verse` (the
  scope at opening, so a reading keeps its verses even if the base data moves).
- **Config:** `cfg_enum reading_gap_type` with guide text, phase and target table, and the gate checks.
- **Library and handlers:** `iba/app/lib/reading.py` and its handlers, through `run.py`, work package
  `reading`. Steps: `Open`, `Record`, `Check`, `Synergy`, `Apply`, `Publish`, `Account`.
- **Code reused:** strand Record (observations, faces), Derive (claims, dispositions), Rewrite
  (blocks), `publish_chapter`, and the collation.
- **Docs and tests:** USER-GUIDE, BUILD.md, the worksheet, and a test plan on a copy for each step and
  gate, including refusals (a gate passed out of order; a `record` id that does not exist; a synergy
  JSON not built from the tables of this reading).

## 6. Points for your decision

| # | Question | Recommendation | Your choice |
|---|---|---|---|
| D-a | The strand steps Map, Derive and Rewrite, which gate on a whole strand: retire them in favour of the reading's gates, with the four open strands finishing as readings? | retire; keep `Define`, `Context` and `Record` while those four are finished | |
| D-b | Open items found while recording: raised through the open-item tool of #2236 once it exists, until then as today? | yes | |
| D-c | `analysed` on `verse_meta`: set only at gate 1 by a reading (with D1, Bible_Books readings do not count)? | yes | |
| D-d | Approve this design for the build? | | |
