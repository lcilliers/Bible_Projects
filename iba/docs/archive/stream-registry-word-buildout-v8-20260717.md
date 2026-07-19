# The new-word run — v8 · decisions, and the recommendation to build

> **v8 · 2026-07-17.** Answers the researcher's v7 replies. Folds O1–O7 into the design and makes
> the build-vs-detail call. **No config loaded yet — this is the last design step before authoring,
> pending the go.**

---

## 1. The choice you raised — my recommendation: **build**

> *"we must make a choice to continue to add individual items to create, or to proceed with the
> actual build and think through what is missing at that stage… it definitely does not have all the
> items."*

You are right that it is not complete, and I do not think it can be made complete by more prose.
**Recommendation: stop enumerating and build the raw slice.** Reasons, from this session's own
evidence:

- **Building has surfaced more than thinking, every time.** The vacuous `tree_shared` test, the
  backspace-corrupted regex, the head/tree split, `D101` being the surface word not the meaning —
  none came from a design doc. All came from running code against real data. The design docs found
  the *shape*; the build found the *truths*.
- **The raw stream is proven end to end** on `peace` and `hypocrisy` — 883 verses, 11,756 spans,
  parse-check 35/35. It is the one part solid enough to author.
- **The cost of a wrong config is low.** It is a new DB (nothing touches the study data), and a
  config edit is a cheap `cfg_apply` round-trip. The cost of a wrong *design doc* is that we keep
  discovering the same thing three ways (the meaning defect took three docs to state correctly).
- **Best practice for uncertainty is a vertical slice.** Build one word, raw only, config + code +
  the new tables, and let the build force every missing item into the open — then iterate. The
  design docs become the *running record*, updated as gaps surface, not a front-loaded attempt to
  foresee them.

**What "build" concretely means (§5).** Not the whole app — the smallest complete slice: the raw
tables + the raw config + a runnable raw module, over one word, writing real rows. It will fail in
ways this doc cannot predict, which is the point.

If you prefer to keep designing, the next docs would be registry (yours) and the meaning
normalisation (O4) — but I would build first.

---

## 2. Your answers, resolved

| # | your answer | resolved into |
|---|---|---|
| **O1+O2** | *"L1's only purpose is to show which strongs were returned from the STEP word search. these strongs are the basis for L2."* | **L1 `word_strong` = (word, strong) only.** No definition fields. It is the discovery record; L2 is the strong. My v7 reading confirmed. |
| **O3** | *"particles have their own row, each span have a row. Simplifies the parsing."* | **`span` is one row per CODE, not per word** — see §3. Removes the `particles` list and the multi-value `strong_variant`. |
| **O4** | *"the meaning block is complex and large… normalise into a separate table or tables. we definitely do not want to scan the whole block every time."* | **The meaning normalises out of `strong`** — see §4. |
| **O5** | *"word status reflects the processing stages of the registry — simplified. clustering complete is achieved on a TERM level, not word level."* | `enum.word_status` = registry stages only; **`clustered` is NOT a word status.** Clustering is per-term; "all this word's terms are clustered" is a **validation gate reading term-level status**, not a word state. |
| **O6** | *"VS Code interface… a message to the terminal could work. chat to capture feedback, or a message window."* | **`escalation` channel = a terminal/VS-Code message; answer captured via chat or a simple message window.** Low-tech, no external service. |
| **O7** | *"what is best practice for resumability… the interaction is a loop in the program with conditions for exit and continue."* | §6 — best practice, and it matches your read. |

---

## 3. O3 — `span` is one row per code

The interlinear aligns a surface word to **N codes**:

```
'earth'  strong='H0776G H9002 H9009'  morph='HNcfsa HC HTd'   ← 3 codes, 3 morphs, one word
```

**Old master:** one row for "earth", the codes crammed into one field.
**Your rule:** each code is its own row. So:

| position | surface | strong_variant | morph_code | is_particle |
|---|---|---|---|---|
| 0 | earth | `H0776G` | `HNcfsa` | no |
| 1 | earth | `H9002` | `HC` | yes |
| 2 | earth | `H9009` | `HTd` | yes |

**`span` — revised:**

`id` · `verse_fk` · **`position`** (running code index in the verse — **the key with verse_fk**) ·
`surface` (the word this code belongs to; repeats) · `strong_variant` (**one** code, → L2) ·
`morph_code` (**one**, aligned) · `is_particle` · `built_at` · `deleted`

**This is simpler, and it fixes a real problem.** `strong_variant` is now a clean FK to one L2
strong — no splitting a list at every join. And "and the Spirit" vs "the Spirit" is now a queryable
row (`H9002` present at that word's positions), not a substring. The cost is more rows — but the
canon is fixed at ~500k codes, built once.

⚠ `(verse, position)` stays the key, because position is now per-**code**, so no two rows share it.

---

## 4. O4 — the meaning is normalised out of `strong`

`strong` stops holding the `mediumDef` blob. Split by how the study *uses* it:

**`strong`** — the identity, unchanged bar the meaning:
`id` · `strongNumber` · `accentedUnicode` · `stepGloss` · `stepTransliteration` · `count` ·
`freqList` · `deleted`

**`strong_sense`** — the sense head, **the span's meaning** (the thing analytics reads):
`id` · `strong_fk` · `head` · `is_own_lemma` · `deleted`
*(one per strong; `head` is the first line of `mediumDef`, or the gloss where the code is its own lemma)*

**`strong_meaning_tree`** — the definition tree, structured (only scanned when the broader range is needed):
`id` · `lemma_key` · `sense_code` (`1)`, `1a)`) · `parent_code` · `sense_text` · `sort` · `deleted`
*(keyed on the lemma — shared across its senses, which is what the prototype proved: one tree per lemma)*

**`strong_lexicon`** — LSJ / Mounce (Greek, large, rarely scanned):
`id` · `strong_fk` · `lsj` · `mounce` · `deleted`

**Why this shape:** the prototype showed the **head is the span's meaning** (one field, read
constantly) and the **tree is the lemma's range** (large, read rarely). Normalising by *access
frequency* is exactly your point — the constantly-read head is a small column; the rarely-read tree
and LSJ are separate rows you only touch on demand.

⚠ This revives the *idea* of the old `wa_meaning_parsed`/`_sense` tables — but done right: keyed
correctly (tree on the lemma, sense on the strong) and fed by the right field (`mediumDef`, not a
`medium_def`-only vocab_map that defaulted language to Hebrew 7,739 times).

---

## 5. What the build slice is

If you say go, the first build is **raw, one word, real rows** — nothing downstream:

1. **The new DB** — create just these tables: `word_registry` (minimal), `word_strong`, `strong`,
   `strong_sense`, `strong_meaning_tree`, `strong_lexicon`, `strong_verse`, `verse`, `span`. With
   `use` + `expectation` on every column (the schema config).
2. **The raw config** — `raw.json` entities + the `records` node; `step.json` `may_source`;
   `pipeline.json` the 5 raw steps.
3. **The raw module** — a real `module.raw` that runs the 5 steps over one word and writes the rows,
   built from the prototype code (which already does the fetch and parse correctly).
4. **Run it on `hypocrisy`** and read the tables.

**What it will force into the open:** the handler contract, the run record's real columns, the
add-rule vocabulary, `enum.on_fail`, and every column whose `use`/`expectation` we have not yet
written — surfaced by the build refusing to proceed without them, not guessed.

---

## 6. O7 — resumability, best practice

Your read is right: it is a **program loop with exit/continue conditions**, not a chat. Best
practice makes the pause survivable:

- **The run has persisted state** — `run` record with `state (running · paused · done · failed)` and
  `resume_point` (which step, over what). Written to the DB, not held in memory.
- **On `pause-continue`:** write an `escalation` row (question + preset details), set the run
  `paused` at `resume_point`, and **stop the loop** — do not spin.
- **The answer arrives** (terminal/window, O6) and is written to the `escalation` row.
- **Resume** is re-running the work package: it reads the run state, sees `paused` + an answered
  escalation, and continues from `resume_point`. Idempotent — a re-run of a completed step is a
  no-op because the rows already exist (global dedup).

**Why persisted, not just an in-memory loop:** a pause can outlive the process (you answer an
approval an hour later, or after a restart). If the state is in memory, a pause that waits is a
process that hangs. If the state is in the DB, the run simply *stops*, and *resume* is a fresh
invocation that picks up where it left off. That is the difference between a loop and a resumable
workflow — and it is why `run.json` needs the `state`/`resume_point` columns (O7 was a real blocker).

---

## 7. Awaiting

**One decision:** build the raw slice (§5), or keep designing (registry + O4 detail). I recommend
build. Nothing is authored until you say.
