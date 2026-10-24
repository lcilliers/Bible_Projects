# #2268 The reading process, checked against what the study expects (v1)

**Date:** 2026-10-24 · **Escalation:** #2268 · **Status:** findings only. Nothing has been changed.

Researcher, chat 2026-10-24: *"my observation from the previous session is that you have not digested, and incorporated the expectations of the study into the new analytic process. … Im not at all convinced that you have the real reason why you are doing each step at the center of the step - for you it is just a process of tick and turn and sign off."*

**The observation is confirmed.** The reading process (`Reading.ps1`, #2228) checks that something was written at each step. It does not check that what was written meets the study's method, and most of that method never reaches the process at all. Each answer below comes from the live code and from `iba.db`, read-only, on 2026-10-24.

## 0. What the study expects of a reading

The fullest statement is a document, not a config: `Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md`, which was approved by you on 2026-10-11 and again on 2026-10-19 (#1995, #2168). It sets out:
- **§1, the purpose.** A reading asks what the inner being is doing in the verse and how the words in it work together. It is never "a verse about the strand's word".
- **§3, the steps before reading.** Use what is already extracted, the surface table, earlier readings of the same verses, and the open threads.
- **§4.0 to §4.9, the sequence for one verse.**
  - Read outward from the verse.
  - Read it in its passage and genre.
  - Find the main inner-being operation and give every M-coded word its role.
  - Read the strand word in that role, then the relations between words, the pointers, the parties and the route.
  - Look at the original and note the face.
  - Never close on "not X".
- **§4.8, what is recorded for each verse.** The main operation, each word's role, what each qualifier gives, the strand word's role and face, the relational and pointer observations, the parties, the route and the home.
- **§5, reading a collection.** Progressive across strands, grouped by the main operation, one account per phenomenon, with the faculty considered last.
- **§7, the checks before a reading is handed over.**

`cfg_behaviour_rule` B:73 compresses this guide into one paragraph and ends: *"Full guide: Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md"*. So the method's authority is a file. That is why a note from the last session (`outputs/escalation/2259-role-filtered-reading-design-v2-20261024.md` line 21) cites the Workflow guide: the config itself sends the reader there. Under `governance.rules_must_be_config_driven`, the sequence, the record fields and the hand-over checks should be cfg rows. They are not.

Other study expectations also sit outside config:
- **The 29 study principles from the retired memory files.** Their standing under the fan-out method has not been settled (#2190, on hold; `outputs/escalation/2184-memory-dispositions-v1-20261021.md` §3).
- **Methods held as file paths.** `cfg_setting` `method.passage_read_guidance_path`, `method.interpretation_questions_path` and `narrative.inner_being_style_guide_path` each point to a Workflow file as the authority for a method.

## (a) When a gap is recorded, which rules apply

**The rules delivered at `Reading.ps1`.** `cfg_rule_scope`, scope_kind `ps`, gives this set:

| Rule | What it covers |
|---|---|
| B:76, B:77, B:78 | the claim register and narrative chapters |
| B:113 | bare Strong's codes are decomposed to their derivatives |
| B:114 | synergising is done from the tables |
| B:115 | each open item has a clear purpose |
| B:116 | the verse is read first |
| `governance.narrative_home` | where the narrative lives |

None of these governs **what an observation must contain**.

**The study rules not delivered at `Reading.ps1`.** Each is scoped only to the path `_analytics/**` or `_analytics/essay/**`:

| Rule | Subject |
|---|---|
| B:69 | let Scripture speak; no imputed synthesis |
| B:70 | cluster tags are loose; no re-tagging |
| B:71 | reuse what is already extracted; set-based M-code link |
| B:72 | route each verse: A (other beings), B (with the HIB), C (data only) |
| **B:73** | **read each verse by the role of each M-code word** |
| B:84 | fan-out, progressive strands |
| B:85 to B:87, B:90, B:91, B:112 | narrative and prose rules |
| B:88, B:89 | weave, not fit; a change of character is recorded |
| B:92 to B:95 | no unnecessary holding; M47 checks; gloss scan; raw layer |
| B:109 to B:111 | read before asking; surface is the lens; filters are working aids |

The study used to be done in files under `_analytics/`, so these rules reached the work when those files were edited. The recast moved the work into `iba.db` (through `Reading.ps1`) and into `outputs/reading/`, but their delivery was not moved with it. **Since #2228, none of these rules has reached a reading.**

**The method rules (`cfg_method_rule`).** This table holds 121 active rows, including the observation rules:
- concise and verse-specific: 108 to 110 and 119
- span-grounded: 112 and 121
- read all three meaning sources: 70, 88 and 113
- every instance states what it is: 91
- a difference is its own observation: 93
- morph is actively read: 95

`cfg_rule_scope` has **no `M:` reference at all**, so no method rule is delivered at any point. Each method rule is also tied to a step (`lexical.meaning`, `lexical.relational`, `cluster.reading` and so on) that `Reading.ps1` never runs. No method rule exists for the reading process.

**What the code enforces when an observation is recorded.** `iba/app/lib/strandreading.py:349-382` (`check_observations`) checks five things:
- `text` and `meaning` are not empty
- `basis` is `read` or `stated`
- each verse given contains the Strong's given
- every quotation is in the ESV text
- each key is unique

`iba/app/lib/recordingpass.py:571-601` then writes the row with stage `strand-reading` and tag `key-statement`. That is the October ledger shape (#2261, #2263, #2264).

**Answer to (a).** A recorded gap meets only those five structural checks. The study's rules for an observation did not reach the reading process, and nothing in it checks them.

## (b) When verses are read, which rules apply and what data is used

**The rules.** The same set as in (a). B:116 (read the verse first) does reach the process. B:73, which says *how* to read, does not.

**What the reader is given.** `Reading.ps1 -Step Open` writes two files:
- the gap JSON, `<label>-gaps.json` (`iba/app/lib/reading.py:177-214`), which the reader works from;
- the collation JSON (`iba/app/lib/versecollate.py`), the fuller record of the same scope.

| What the guide asks the reader to use | In the gap JSON? | In the collation JSON? |
|---|---|---|
| The verse text | yes | yes |
| The M-coded words (surface, Strong's, cluster) | yes | yes |
| The passage around the verse (§4.1) | **no** | **no** |
| The T-codes: parties, operations, negators, connectives, body (§4.5, §4.6) | **no**: the word query takes only `cluster_code LIKE 'M%'` | **no** |
| The meaning of each word: `strong_meaning_tree`, `strong_lexicon` (§4.6a, method rule 70) | **no** | the sense head and the meaning-tree text; Mounce; **only the length of the LSJ entry, not its text** |
| The ESV renderings of the same Strong's across its verses (§4.6a, B:110) | **no** | **no** |
| Earlier readings of the verse (§3.3) | only a count: `"known": "file lines: N"` | the file lines, draft observations (stage, tag, text, basis), claims, blocks |
| Earlier observations on the verse | **no**: a verse with any observation is not a gap, so it gets no item and is not read again | draft observations only (`status='draft'`) |

**What is done with the content.** For a verse that is "not read", the reader writes:
- `text`, `meaning` and `basis`
- optionally `setting`, `implication`, `chain` and `parties`
- the verse and Strong's pairs it rests on

That shape has **no field** for the main inner-being operation, the role of each M-coded word, what a qualifier gives, the relational and pointer observations kept apart, the route, the face, the home, or a catalogue question. Those are exactly the items the guide's §4.8 says to record. The record shape therefore cannot hold a reading done by the method, and nothing pushes the reader toward the method.

**At gate 2** (`Reading.ps1 -Step Synergy`, `reading.py:495-559`), the synergy JSON gives each observation's `text`, `meaning`, stage, status, verses and the claims that carry it. It does not give `setting`, `implication`, `chain`, `parties`, `basis`, `tag`, `strong` or `question_code`. Claims are then derived from that.

**Answer to (b).** The verse is read from its own text and its M-code words. The passage, the T-codes, the meaning tables, the surface renderings and the earlier observations are either not given or kept apart from what the reader works from. The content goes into a free-text row whose shape does not follow the study's reading sequence.

## (c) When gaps are evaluated, what is measured

| Check | Code | What it measures | Measured against |
|---|---|---|---|
| A verse is "not read" | `versecollate.py:168-170` | presence: no observation of any kind and no strand face | nothing qualitative |
| Meaning missing | `versecollate.py:181-183` | presence: no meaning-tree rows, or (for Greek) no Mounce entry | nothing qualitative |
| Gate 1 | `reading.py:384-399` | every item has a row that exists, or a reason of **10 characters or more** | nothing qualitative |
| Gate 2 | `reading.py:440-463` | every observation is carried by a claim or disposed; every claim is told or held; every open item is settled | counts reach zero |

None of the guide's §7 hand-over checks is applied: roles given, strand word read in its role, home follows the main operation, bindings recorded, earlier readings used, "I read" marked, parties and route recorded. Nor are the method rules: single-verse, span-grounded, the three meaning sources.

**Answer to (c).** No quality check is made. "Sufficient" means a count reached zero, and the measure is that something was written, not the study's question. This is the finding of #2260 §3 (#2262), here traced through every gate.

## (d) How scope and approach are decided

**What the code asks for.** `Reading.ps1 -Step Open` (`reading.py:152-176`) needs:
- a label
- an escalation that anchors the reading
- a home cluster
- verse selectors (cluster, strand, word, Strong's, verse, chapter, claim, observation, item or thread)

The only limits on scope are size: `verse_scope.max_verses` 2,500 (held for review), and the time guards `verse_scope.max_seconds` 30 and `verse_collate.max_seconds` 120.

**What nothing asks for or records:**
- **What the reading is to find out:** the question about the inner being it serves, or which strand, characteristic or open question.
- **Why this scope:** why these verses, and how they relate to earlier readings. B:84 (progressive strands) and B:73 §5 (progressive reading across strands) do not reach the process.
- **Which approach:** the config holds three reading methods side by side, and no rule says which applies when:
  1. The passage method: `cfg_method_rule` steps `hib.set`, `phenomenon.set` and `operation.set`, from `method.passage_read_guidance_path`.
  2. The word pipeline: `lexical.meaning`, `lexical.relational`, `cluster.reading` and `cluster.answer`. Stage 1 has not run for M64 (#2260 §2).
  3. The role reading of B:73 and its guide.

The written record shows the result: the #2161 plan sizes the M72 work by how many verses have an observation (`outputs/escalation/2161-m72-reading-plan-v2-20261024.md` §2). Those are presence counts (#2260).

**Answer to (d).** Scope is set by selectors and capped by size. The purpose of the reading, the reason for its scope and the choice of method are not asked for, recorded or checked. So each step can be passed without the reason for it ever being stated.

## Where this leaves things

The recast (#2228) rebuilt the mechanics: scope, collation, gates and tabled writes. It moved the work from `_analytics/` files into `iba.db`. It did not carry the study's method with it:
- the delivery of the study rules stayed on the old paths;
- the reading method stayed in a Workflow file;
- the record shape stayed the October ledger's;
- the gates check that rows exist.

Every reading since then has passed its gates on those terms. Those readings are #2247 (M64: choose, willing, plan, dedicate) and the #2172 catch-up imports.

**The gaps found here** (several sit under items already raised):

| # | Gap | Already raised as |
|---|---|---|
| 1 | The study rules are delivered only on `_analytics/` paths and never reach `Reading.ps1` or `Verse-Scope.ps1` | new |
| 2 | No `cfg_method_rule` row is delivered anywhere, and no method rule exists for the reading process | new |
| 3 | The reading method (purpose, sequence, record, hand-over checks) lives in a Workflow guide, not in cfg rows; B:73 points to the file; three method settings name files as their authority | new |
| 4 | The record shape has no fields for the main operation, roles, bindings, relational and pointer observations, route, face or home | #2261 (partly) |
| 5 | The gap JSON gives no passage, T-codes, meaning text or renderings; the collation gives LSJ only by its length | new |
| 6 | A verse with any observation is never put back in front of the reader | #2262 (partly) |
| 7 | The gates measure presence and a 10-character reason, with no quality check | #2262 |
| 8 | A reading records no purpose, no reason for its scope and no choice of method; three methods sit in config with no rule for when each applies | new |
| 9 | Synergy gives the observation's text and meaning only, so claims are drawn from a narrowed view | new |
| 10 | The tag `key-statement` and the stage `strand-reading` | #2263, #2264 |
| 11 | 29 study principles from the retired memory files are not settled in config | #2190 (on hold) |

All eleven are recorded on #2268 by reference to this file. Under B:105, none of them is a fix to build until a design has been through you.
