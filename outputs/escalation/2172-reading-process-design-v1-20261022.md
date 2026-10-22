# 2172 — One reading process: September's records, October's reading

Escalation: #2172. Status: a design for your decision. Nothing is built.

Researcher, 2026-10-22 (verbatim): "while we are in developer mode, you need to focus on the
underlying methods that perform these operations and build it into a co-herent process with
safeguards.  you also need to build the same methods to be able identify and redo the gaps that was
created over sept and Oct.  I want a intelligent process that understand what it is doing, not a
mechanical tick the boxes approach."

It builds on the analysis you accepted: `outputs/escalation/2172-september-october-analysis-v1-20261022.md`.

## 1. The principle

The reading is done by me, in the session, as in October. That is where the judgement is. The app
does what the app is good at:
- it gives the reader everything already known before it reads;
- it records each finding as a grounded row;
- it checks the facts: the verse exists, the quote is in it, every hit was read, the finding
  reached a claim or was set aside for a stated reason;
- it shows the substance of any gap, not a count.

**A check refuses only on a fact.** Where judgement is needed (is this finding carried by that
claim?), the app puts the two texts side by side, and I or you decide. That is the line between
an intelligent process and box-ticking.

## 2. What exists and is reused (no new table)

| Existing method | What it already does | Its role here |
|---|---|---|
| `lib/lexicalscope.py` | cluster, word or strong list to the verse ids of every hit (span-based) | the pull |
| `lib/recordingpass.py` `record_batch` | the single writer of `ib_observation`/`ib_node`. It resolves every verse from iba.db, refuses an ungrounded occurrence, and decides same, broaden or new itself (never the LLM) | recording each reading |
| `escalation_thread_item` + `Escalation.ps1 -Action Match` | matches a strand's clusters, strongs and verses to the open items | the context pack, and where held findings go |
| `lib/narrativeregister.py` `record` | one weave from one JSON: claims with sources, tellings, refs, quote check | the weave |
| `narrative_citation`, `narrative_claim_source` | every verse the narrative cites or rests on | the "did it reach the narrative" check |
| `verse_meta.status` | exclude / citated / analysed | coverage |
| `run` / `run_batch` | what ran, and its run_id | ties a reading and a weave to their run |
| `cfg_method_rule` | the method rules per step, shown at the point of use | the October rulings (surface first, meaning before structure, #1918, #1930, #1943, rule 69, 70) become rows here |

The October scripts (pull, face-assign, quote check, reconciliation, chapter match) were retired
under #2200. Their logic returns as app steps built on the methods above, not as files in
`_analytics`.

## 3. The process: one work package, five steps

**Step 1. Scope and context** (`strand.context`, read-only)
- **Input:** a strand: a word family, cluster(s) or strong list, and its escalation.
- **The app writes one context file:**
  - every hit, with its ESV text;
  - every existing observation on those strongs and verses (September's included), with its
    status;
  - every claim resting on those verses, and the passage that tells it;
  - every open thread item that matches;
  - each verse's `verse_meta.status`.
- **Why:** the reader starts from what is known, and must say what it confirms, changes or
  withdraws. That is what stops redoing work and contradicting earlier findings blindly. The bulk
  text stays in the file, not in the chat (#1899).

**Step 2. Read** (me, in the session)
- The October method, unchanged in substance: read by surface, the whole passage around a key
  statement, a face for every hit, and for each key statement setting, meaning, implication
  (R marked), chain, parties.
- **Output:** the reading as observation JSON in the shape `record_batch` takes. The md ledger is
  produced *from* the rows (step 5), not written by hand.

**Step 3. Record** (`strand.record`, through `record_batch`)
- **Each observation is written** to `ib_observation` with the stage `strand-reading`, and each
  verse to `ib_node`.
- **The quote check runs here:** a quote not in its verse's ESV text is refused.
- **Each hit read is marked** `verse_meta.status = analysed`.
- **Any hit in scope with no face is listed by verse and text.** The reading is not complete while
  one is left without a stated reason ("mention only" is a reason).
- **An observation that corrects an earlier one** names it, and the earlier one is superseded
  (`supersedes_observation_id`), not left alongside.

**Step 4. Weave** (`Narrative-Register.ps1 -Action Record`, as now)
- **A claim names the observations it rests on** as well as its verses.
- **Each cited verse is marked** `citated`.
- **Every observation of the strand ends with a disposition**, through the existing
  `ib_observation.status`:
  - `resolved`: carried by a claim (named);
  - `open`: held, with a thread item;
  - `silent`: recorded, with nothing for the narrative, and why;
  - `withdrawn`: wrong, and why.
- **A correction observation** is resolved only when the passage or claim it corrects has
  changed.

**Step 5. Account** (`strand.account`, read-only; also at session-close)
- **One page per strand, computed from the tables:**
  - every observation and where it went: the claim and the passage text, or the reason it went
    nowhere;
  - every verse in scope and its status;
  - every claim that rests on the strand and whether its observations still stand.
- **Gaps are shown as text, not counts.** For example: "AG-41: anger turns when the act is dealt
  with; not carried by any claim; no reason given."
- **The strand's escalation cannot close while an observation has no disposition or a hit has no
  face** (the one hard gate). Everything else is shown for judgement.

## 4. Redoing the September and October gaps with the same methods

**A. Bring October's findings into the tables.**
- A one-off import reads the October ledgers: about 840 observation rows in 25 live files (series
  AG 240, LD 227, FE 205, AN 167, and others). Each row goes through `record_batch` (stage
  `strand-reading`), so it is grounded and quote-checked like a new one.
- A row the import cannot read cleanly is listed for me to fix by hand, not guessed.
- The batch readings in other formats (the `ot-*-reading` and `batchN-reading` files) are listed
  file by file. I record them through step 3 as a reading, not by a parser.

**B. Link what the narrative already says to what was read.**
- For each existing claim, the app proposes the observations that share its verses, side by side
  with the claim text.
- I confirm or reject each link on meaning, and the link is recorded as the claim's source. A match
  by verse alone is never accepted as a link.

**C. Then the account (step 5) shows the real gaps, strand by strand:**
- findings never carried (for example the flesh-and-body verses, #2162);
- corrections never applied (Heb 10:22, 1Co 6:19b-20, Neh 6:13, Psa 69:9);
- claims with no observation behind them (the narrative outran the reading);
- the 46 claims with no live telling and the 13 with no verse source;
- the 306 open thread items, each matched to findings that may settle it.

**D. September's observations** (6,527 draft: M67, M83, M49 and the word-level rows) are not re-run.
They are offered in step 1's context file whenever a strand touches their strongs. The reader
confirms, corrects or withdraws them there. So September's work is reused where it is right, and
retired where it was noise.

**E. Redo.** Each gap is redone through the same five steps, in the order you set. That redo is study
work, so it waits until you re-open the study. Parts A and B are the app's own catch-up and do not
read anything new.

## 5. What I need you to decide

| # | Decision | Options | Claude recommends |
|---|---|---|---|
| 1 | The October ledger row is an `ib_observation` row | yes / no | yes |
| 2 | Where its parts live: setting, meaning, implication, chain, basis, parties | a. new columns on `ib_observation` · b. all in `obs_text`, structured by line | a: the parts are what the account and the links read |
| 3 | A new stage value `strand-reading` (`cfg_enum`) | yes / no | yes |
| 4 | A claim may name an observation as a source: a new `narrative_claim_source_kind` value `observation` | yes / no | yes |
| 5 | A reading and a weave carry their `run_id` (a column on `ib_observation`) | yes / no | yes, so step 5 can say which reading a finding came from |
| 6 | The dispositions use the existing status values as in step 4 | yes / revise | yes |
| 7 | The one hard gate: no close with undisposed observations or unfaced hits | refuse / warn | refuse |
| 8 | Build order | the process (steps 1 to 5), then catch-up A and B, then the account across all strands | as listed |

**Size.** No new table: up to seven columns on `ib_observation` (the six parts and `run_id`),
two enum values, the strand work package (three steps
plus `Record`'s existing action), the one-off import, and the method rules into `cfg_method_rule`.
Tested on a copy, with a test plan per step. About two Developer Mode sessions for the process and
the catch-up.
