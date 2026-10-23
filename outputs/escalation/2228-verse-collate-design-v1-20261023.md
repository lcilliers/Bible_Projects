# 2228 — Collating what is known, and the gaps, for a scope: design (v1)

Escalation: #2228 v23. Status: design, built in the same Developer Mode session under the researcher's
permission of 2026-10-23 ("you have permission to continue to build out 2228"). The choices marked
**default** are details of this design and can be changed in config or on review. Nothing here decides a
new matter of method; the points that would are held in section 5.

This is tools 3, 4 and 5 of `outputs/escalation/2228-discovery-scope-and-known-v3-20261022.md` (verse
extract, known-for-verses pack, gap report) as one tool, because they always run together on one scope
(rule 39, simple steps).

## 1. What it does

`Verse-Collate.ps1` takes a scope, given as the same selectors as `Verse-Scope.ps1` (resolved by it,
with its guard), and returns for every verse in it what the project already knows, and what is missing.
It reads only. It is the "collate the material, prevent rework" step that comes before recording.

## 2. What it collates, per verse (every source by one set-based query over the scope)

| Part | From | Holds |
|---|---|---|
| text | `verse.text` | the ESV text |
| words | `verse_lexical` joined to `cluster_strong` (M clusters) | the inner-being words in the verse: surface, strong, sense (`strong_sense.head`), cluster and its name |
| status | `verse_meta.status` | shown, but not counted as read (D1 of discovery v3) |
| observations | `ib_observation` (draft) through `ib_node` | id, stage, tag, the text, basis, the October disposition from `revisit_note` |
| strand hits | `reading_strand_hit` | strand, strong, surface, face or reason |
| claims | `narrative_claim_source` → `narrative_claim` | claim ref, text, status, and the blocks that tell it |
| narrative | `narrative_citation` → `narrative_section` | chapter and heading of every current block citing the verse |
| open items | thread items matched as `Escalation.ps1 Match` does (verse, the verse's M strongs, their clusters) | thread, item, kind and value, note |
| cluster files | `reading_ref` (tool 2) | file, section heading, line, how found, and **the line itself** (the verse extract): only the lines that name the verse are read, never a whole file |

**Lexicon, once per strong** (not repeated per verse): sense, the meaning tree's senses; for Greek the
Mounce entry. LSJ entries average 3.5 KB (up to 72 KB), so **default:** LSJ is flagged as available,
with its size, not copied into the pack.

## 3. The gaps, per verse

| Gap | Means |
|---|---|
| not read | no observation and no strand face on the verse (`analysed` alone does not count) |
| read in files only | the cluster files name the verse, but no observation holds it |
| hit unread | a strand hit with neither face nor reason |
| observed, no claim | an observation on the verse, but no current claim rests on the verse |
| claim not told | a current claim resting on the verse that no current block tells |
| open item | a matched open thread item |
| meaning missing | an inner-being word with no meaning tree, or a Greek word with no Mounce entry (`governance.base_data_spine`) |

"Observed, no claim" is judged at the verse, because no claim source names its observation yet (the
link back-fill of discovery v3 is not built; section 5).

## 4. Output and guard

- `outputs/verse-collate/<label>-<YYYYMMDD>.json`: the full record per verse, and the lexicon.
- `outputs/verse-collate/<label>-<YYYYMMDD>.md`: the gap counts, a compact line per verse (reference,
  words, counts of what is known, its gaps), and the lexicon list. The JSON is the record; the .md is
  for reading.
- **Guard:** the scope is limited by `verse_scope.max_verses` and `verse_scope.max_seconds`; collating
  adds `verse_collate.max_seconds` (**default** 120). Past it, the run stops and is refused: reform the
  scope.
- **Speed:** `ib_node` gets an index on `verse_reference` (it has none), so observations are found by
  verse in one indexed query.

Built as `iba/app/lib/versecollate.py`, `iba/app/handlers/versecollate.py`, `iba/app/ps/Verse-Collate.ps1`,
through `run.py`, work package `verse-collate`, config by `apply_logged`, tested on a copy.

## 5. Held for the researcher (not built)

1. **Recording by scope.** Recording today is only `Strand-Reading.ps1 -Step Record`, which takes a
   strand. Recording the gaps of any scope needs a record step keyed on the scope: how observations
   are grouped, what disposition and close gate apply. That is new method and is for the researcher
   to decide; a design follows for review.
2. **Claim source → observation link.** Which observation a claim rests on cannot be told
   mechanically from the verse alone; it is set when claims are finalised from the tables.
3. **#2235**, the key words of a scope and the reverse surface lookup.
