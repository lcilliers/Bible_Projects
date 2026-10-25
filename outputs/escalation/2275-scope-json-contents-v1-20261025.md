# #2275 What the scope JSON holds today: the collation (v1)

**Date:** 2026-10-25 · **Escalation:** #2275 (from #2268) · **Status:** an account from the code and a real file.
Nothing has been changed.

Researcher, chat 2026-10-25 (verbatim): *"I am affraid we need to go back to 0.c because it is clear to me you do not
have the scoping sorted out, else you would not have pitched D1 as word level. show me a summary of what the scope
json would contain (you called it something else.)"*

**The name.** At 0.C, `Reading.ps1 -Step Open` writes two files:
- **`<label>-collation.json`**: the scope and everything known about each of its verses;
- **`<label>-gaps.json`**: the pre-gaps.

The collation is the scope JSON. It is built by `iba/app/lib/versecollate.py` (`collate`) from the verse set that
`iba/app/lib/versescope.py` (`resolve`, the tool behind `Verse-Scope.ps1`) resolves. The example values below are
from the trial reading of #2273 (Jon 1:10, Jon 1:16, Psa 56:3), on a copy.

## 1. What it holds

**The scope** (`scope`):
- `request`: the request as given;
- `selectors`: each selector (cluster, subgroup, strand, word, strong, verse, chapter, claim, item, thread), with the
  verses it brought in;
- `not_resolved`: what did not resolve;
- `counts`.

**Per verse** (`verses[]`):

| Field | Holds | Source | Example (Psa 56:3) |
|---|---|---|---|
| `reference`, `osis`, `verse_id` | the verse | `verse` | Psa 56:3 |
| `routes` | how the scope reached the verse | versescope | the verse selector |
| `text` | the ESV text | `verse` | "When I am afraid, I put my trust in you." |
| `status` | the verse's coverage mark | `verse_meta.status` | analysed |
| `words` | the verse's words that carry an M-code: surface, strong, cluster, cluster name | `verse_lexical` joined to `cluster_strong` (M only) | afraid H3372G M01; trust H0982 M19 |
| `observations` | the observations on the verse with status `draft`: id, stage, tag, text, basis | `ib_observation` through `ib_node` | 1 (strand-reading) |
| `strand_hits` | the October strand hits on the verse: strand, strong, surface, face, reason | `reading_strand_hit` | fear, H3372G, face A |
| `claims` | the current or held claims resting on the verse, and where each is told | `narrative_claim_source`, `narrative_claim_telling` | none |
| `narrative` | the blocks citing the verse | `narrative_citation` | 5 blocks (10.1) |
| `open_items` | the open thread items that match the verse, its words or clusters | `escalation.match_open_items` | none |
| `file_lines` | the lines of study files that name the verse | `reading_ref` | 4 lines (the fear ledgers) |
| `gaps` | the collation's own gap labels | computed | "observed, no claim" |

**Per word, once** (`lexicon{strong}`):
- `sense`: the head gloss (`strong_sense`);
- `meaning`: the meaning-tree senses (`strong_meaning_tree`);
- `mounce`: the Mounce entry (`strong_lexicon`);
- `lsj_chars`: the length of the LSJ entry, not its text.

**For the whole scope:**
- `gaps`: gap counts;
- `files_changed_since_indexed`: study files changed since they were indexed;
- `counts`: verses, verses with a gap, observations, claims, file lines, open items, seconds.

## 2. What it does not hold, measured against "the base data + existing analytic data"

| Missing | Where it is in the tables |
|---|---|
| The verse's words that carry no M-code: T-codes (qualifiers T2, operations T3, negators T5, connectives T6, parties T7 to T9, body parts T14 …) and untagged words | `verse_lexical` (all rows), `cluster_strong` (T codes) |
| Per occurrence: position, morph, gloss, span | `verse_lexical`, `span` |
| The word's subgroup | `cluster_subgroup_strong` |
| The word's related words | `strong_related` (keyed on the exact code) |
| The LSJ text (only its length is given) | `strong_lexicon.lsj` |
| Observations that are not `draft` (resolved, open, silent), and each observation's nodes: which word, its role, its cluster | `ib_observation`, `ib_node` (build B4, #2276, is this) |
| The findings of the new readings (stage `reading`), with their kinds | `ib_observation`, `ib_node` |
| The passage around the verse | `verse` (B1 gives it only later, in the observe JSON) |
| The scope's objective | `reading.objective` (B1 holds it on the reading, not in the file) |

## 3. Where this leaves 0.C

- The collation is verse-based: one entry per verse, with what is known about it. That matches the researcher's
  instruction that reading is verse-based.
- It does not carry all the base data and all the existing analysis for each verse (§2). Its word list is the
  M-coded words only, so qualifiers and other T-code words do not reach the scope at all. B1 then added them only in
  the observe JSON.
- Design v1 of B3 pitched D1 as a read of one word across all its verses. That is a word-based reading, not a
  verse-based one, and it is withdrawn.
