# Progressive, relational verse-reading — researcher's design correction, 2026-09-17

**Continues #1706.** Raised examining `2Cor.7.11` directly (7 M-code words colliding in one
verse, zero cross-cluster observation produced — see chat, and
`1706-stage1-prompt-visibility-v1-20260917.md`). Researcher's own words, verbatim, this chat turn:

> "verse-reading is not just about the cluster word, it is about the M-code words. This verse will
> be read by 7 clusters. The previous observation for this word will be available to llm
> progressively in each cluster and each cluster must not re-invent or duplicate but must see [if]
> the focus change... At every point let me ask — which points, what does the other verses around
> it say."

## 1. The core correction to Stage 1's current design

**Verse-reading is not an isolated read of one home strong against a fixed 14-question
template.** A verse with N distinct M-code words gets read N times — once per cluster whose member
strong occurs there (`2Cor.7.11` = 7 times: `M67`/`M03`/`M02`/`M01`/`M18`/`M26`/`M12`). The current
build (`versereadinggenerate.py`) already gives the LLM every M-code word's `cluster_codes` via
`roles_in_verse` — the raw data is present — but nothing in the catalogue questions or instructions
ever asks about the *relationship between* the M-code words themselves. That's the actual gap, not
a missing data field.

## 2. Progressive, non-duplicating, focus-shifting — the worked example

Researcher's own chain, `2Cor.7.11`, verbatim in substance:

- **`M67` pass (earnestness, the current live run):** the question in focus is *what role does
  earnestness play in relation to the other M-codes present* — "in this case it involves almost
  every other one."
- **`M03` pass (grief, not yet run):** the focus shifts. Grief is first qualified as *godly*, then
  *earnestness becomes the measure of it* — "godly grief drives this relentless focus
  (earnestness)." Same verse, same 7 words, genuinely different question being asked of it.
- **`M18` pass (longing/zeal, not yet run):** focus shifts again — "what role did godly grief do
  for longing, and did earnestness make a difference" — a THIRD distinct relational question over
  the identical verse data.
- **"And so forth"** — the pattern generalizes to every remaining cluster pass (`M02`/`M01`/`M26`/
  `M12`) that will eventually read this same verse.

**Each pass must see what earlier passes already found for this verse and build on it, not
re-derive or duplicate it.** This requires Stage 1 to carry state ACROSS cluster-passes over the
same verse — something the current build does not do at all; each `lexical.meaning` run is
currently blind to every other cluster's own reading of the same shared verses.

## 3. The concrete casualty this design gap already produced

`G0627` ("eagerness to clear [yourselves]," *apologia*) carried no M-code and no operation tag at
all (`T2`, generic) — invisible to every mechanism in the pipeline. Researcher: *"eagerness to
clear is a missed opportunity. if this is not highlighted then there is nothing else that will
catch it."* Fixed same turn, mechanically (a clear instruction, not a judgement call): reclassified
`T2`→`T3` (`reclassify_g0627_to_t3_v1_20260917.py`, matching `#1598`'s own established
reclassification precedent/rationale format), Layer 1 refreshed for its 8 live occurrences. This
doesn't fix the design gap — it fixes one symptom of it (a real operation word was structurally
unable to be noticed before). The design gap itself (§1/§2 above) is what actually needs building.

## 4. What's decided vs what still needs specifying — not assumed either way

**Decided, in the researcher's own words above:**
- Verse-reading's real object is the M-code words' relationships to each other, not one isolated
  home word.
- State must carry progressively across cluster-passes over the same verse (no duplication, focus
  shifts per pass).
- `G0627`-class gaps (an operation word with no tag at all) must be structurally impossible to miss
  — the reclassification above is the immediate fix; whether a systematic sweep for similar cases
  is warranted is not raised here, flagged as worth asking.

**Not yet specified — genuinely open, not guessed at:**
1. **Mechanism for "available progressively" — PARTLY NARROWED, same session, evaluating `M0.1.2`'s
   output (generalizes to the whole `M0.1`/`M0.5` word-level battery, not that one question).**
   Researcher's own words: *the FIRST read of a verse must answer these questions for EVERY M-code
   strong present, not just the current pass's own home strong.* Increases effort at the first
   encounter (that pass now front-loads lexical answers for every characteristic-word in the verse,
   not one) but reduces effort AND enriches findings every later cluster-pass over the same verse —
   no need to re-derive already-captured per-word facts, freeing that later pass to spend its effort
   on the relational/progressive question instead (§2 above). Still open: the exact retrieval
   mechanism itself (does a later pass query `ib_observation`/`ib_node` live for what's already
   recorded, or a different shape) — the FIRST pass's own widened responsibility is decided, the
   plumbing that lets a later pass find and reuse it is not.
2. **Order independence.** The worked example runs `M67`→`M03`→`M18`, but is that a REQUIRED
   sequence (earnestness must be read before grief), or does any pass, in any order, just check
   what's already there and adapt — meaning `M03` could equally run first and `M67` would then be
   the one building on `M03`'s prior findings?
3. **"Must not duplicate" — enforced how.** Is this a recording-pass concern (same/broaden/new
   logic, `#1693` §3, already built for `ib_observation` generally) applied across clusters too, or
   does the PROMPT itself need to show prior findings and instruct the LLM not to repeat them
   (a different mechanism, upstream of recording)?
4. **The closing question, PARTLY ANSWERED same session, researcher dug further into `2Cor.7.11`
   itself.** Not "does every node routinely pull its immediate surrounding verses" as originally
   framed — checked directly and that's not what's needed. The verse's own phrase "at every point"
   is itself a clue pointing outside the verse; a plain read of the immediately adjacent verses does
   **not** resolve it — the actual answer is in `2Cor.7.2`, further back, part of a whole line of
   thought Paul is building across the chapter, not proximity. Researcher's own words: this is
   *"why it is so important to surface the clues"* (if nothing flags "at every point" as a pointer,
   the link to 7.2 is never found), and it confirms *"the passage read is dead"* (the already-parked
   Window 2 mechanism) for this purpose. **See §6 below — this belongs to synergy (Stage 5), not a
   Stage 1 fixed-window lookup.**
5. **NEW — no catalogue question targets "alternative meaning."** Researcher's own words: where a
   verse's `surface`/contextual sense diverges from the base lemma's general `stepGloss`, the
   nuance driving that divergence in THIS context, its impact here, and how it compares against the
   word's other occurrences, must be actively teased out. **Checked live, confirmed real**: all 21
   live `M0.x` questions read — `M0.5.3` (semantic range) is the closest, but asks about the term's
   general breadth, not which specific slice THIS occurrence draws on or why. Nothing else touches
   it. **Directly explains the earlier tag-distribution finding** (`alternative-meaning`/`surface-
   gloss-divergence` exist in the tag vocabulary but are used in ~0% of 203 observations) — the tags
   exist, nothing asks the question that would surface them. Noted in passing, not claimed
   significant: `M0.2`/`M0.3`/`M0.4`/`M0.6` exist live in the catalogue but aren't part of Stage 1's
   current question set (`M0.1`/`M0.5`/`D7.7` only) at all. Not decided: whether the fix is a new
   catalogue question or a reworded `M0.5.3` — a content/catalogue call, not made here.
6. **NEW — the "qualifier" role has been lost, and this is not a new idea.** Researcher's own
   words: words indicating a state, measure, or other enhancer of an M-code word (a colour/physical
   descriptor used idiomatically, e.g. "red face") aren't currently being teased out at all. **Not
   a fresh proposal — a real thread from `#1598` (2026-09-08), explicitly parked, never resumed**:
   *"a qualifier-type T-code group... needs its own content-defined boundary (degree/intensity
   terms, manner-of-action terms)"*; *"the qualifier role stays BLOCKED until [the] reallocation
   reaches at least the verb and adjective/adverb buckets."* **Confirmed live: no qualifier
   cluster/T-code exists today.** Concrete example already in hand, tying directly back to the
   researcher's own `M67`→`M03` chain (§2 above, "godly grief drives earnestness"): `G2316`
   ("godly," qualifying "grief" in `2Cor.7.11`) is tagged only `T7` (Party-Divine) — its actual
   function, qualifying grief specifically as GODLY and not just any grief, is invisible to the
   current role scheme entirely. Not decided: reviving `#1598`'s own blocked design (what the
   content-defined boundary should be, one T-code group or several) is itself a real, separate call.

## 5. Not touched yet

No code changed for the progressive-reading mechanism itself — this is a genuine redesign of
Stage 1's core loop (which cluster-passes see which prior state), not a prompt-wording tweak, and
`M67`'s own verse-reading run already happened under the OLD, isolated design. Flagging rather than
building against an unconfirmed mechanism.

## 6. A named workstream for synergy (Stage 5) — "discovery mode," not a fixed window

Researcher's own words, same turn: one of synergy's own workstreams must be **picking up a
clue/pointer observation and entering a discovery mode — reading forward and backward around the
verse to discover the implications of the pointer.** Explicitly named as *"a very different method
of reading and discovery"* from the standard per-verse/per-cluster walk — not a fixed N-verse
adjacent window (§4 item 4's original framing), an open-ended search guided by the pointer itself,
which in the `2Cor.7.11` case had to reach back to `2Cor.7.2` to resolve.

**Not designed further here** — Stage 5 (`char-synergy`) isn't even fully designed yet (`#1695`/
`#1698` still open, checked live before this doc was written). Recorded as a concrete, real
requirement that design will need to satisfy, not invented or built now.

## 7. Test cases flagged for future stages — watch these when built, not before

- **`2Cor.7.11`** — the original 7-M-code collision this whole doc grew from (§1-§6).
- **`2Cor.8.16`** — researcher instruction: watch this one specifically at `char-answers` (Stage 4)
  for how "location" is handled. *"thanks be to God, who put into the heart of Titus the same
  earnest care I have for you."* Checked live: `G4710` ("earnest care") is one word, `M67`, not
  two — but the verse still carries 3 M-codes (`thanks`=`M50`, `heart`=`M47`, `earnest care`=`M67`).
  `heart` (`G2588`) is tagged only `M47`, no `T14` (Body-Parts), despite functioning here in an
  explicitly locative/vessel sense — ties directly to the faculty-reflection question (`#1701`
  v5/`#1704` §5 decision 4, "where in the being did this happen"), which this verse answers
  literally in its own text with nothing currently tagging the locative signal.

## 8. `ib_observation.window` — current definition is a duplicate of `stage`, needs redefining

Found examining why the column is empty in the researcher's own export (`verse-reading-
observations.csv`). Live definition (`#1691`, 2026-09-13, predates the current 5-stage naming):
a 4-value pipeline-stage enum (1=lexical analysis, 2=verse-context reading, 3=answering catalogue
questions, 4=multi-cluster synergising) — `cfg_column.filled_by=NULL`, nothing has ever written it.

**Researcher's correction, this chat turn**: this is a direct duplication of `stage` — `stage`
already identifies which pipeline stage produced a row; `window` re-stating the same thing adds
nothing. **Redefinition**: `window` should be the ANGLE an item is being looked at from — meaning;
action/impact; qualifying; etc. — a content-classification dimension, not a pipeline tracker.

**Structural implication, not yet decided**: if window is the analytical angle, the catalogue
QUESTIONS themselves should be groupable by window (each question already implies one — `M0.1.1`
"what is it named" and `D7.7.1` "operation-party relation" are naturally different angles). If that
grouping is registered at the catalogue level (`wa_obs_question_catalogue`), `window` becomes
DERIVABLE from `question_code` rather than needing to be stored, duplicated, on every
`ib_observation` row at all — a normalization question. **Not built** — redefining `window`'s
meaning and whether/how it's stored is a real schema+catalogue decision, recorded for review only.

## 9. `tag` vs `window` — the current tag vocabulary conflates two different dimensions

Researcher's own words, same turn, sharpening §8: **`window` is WHAT and HOW we are looking (the
lens); `tag` is the PECULIAR thing found through that lens.** The live `tag` vocabulary currently
mixes both into one flat field:

- `instance-meaning` is currently a *tag*, but it's actually a *window* — the real tag under the
  meaning window would be something specific, e.g. "surface and stepGloss differ" (this **is** the
  `alternative-meaning`/`surface-gloss-divergence` gap already flagged, §4 item 5).
- `cross-cluster-significance` is currently a *tag*, but it's actually a *window* too — the real
  tags living under it would be outcomes like "tightly related" vs "no direct connection."

**This directly explains the earlier tag-distribution finding** (95% of 203 observations collapsed
into `instance-meaning`/`answered-no-flag`) — those aren't real findings at all, they're window
labels being used as tags, carrying no discriminating information by construction. Researcher's own
words: *"tags/window can be very powerful — need more thought."* **Explicitly not resolved** —
added to the outstanding list, not designed or built here.
