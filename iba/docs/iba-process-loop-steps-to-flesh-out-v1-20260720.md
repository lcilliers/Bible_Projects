# IBA process loop — the steps to flesh out (agenda)

> **Status: AGENDA / TERRAIN MAP. Not a design, not a decision.** Directed 2026-07-20.
> This enumerates the operations of the process loop (§13.2 of
> `iba-application-plan-v2-20260720.md`) that need specifying, so we can take them **one at a
> time**. Nothing here is settled; each item names *what the operation is* and *what is still open*.
> The process is the crux (§13.2: "the output structure and the process are one idea"); the
> concordance schema stays held open until this loop is nailed (§13.7).

---

## The loop, as you framed it

> pick a unit → screen → decide inclusion → analyse the operation →
> augment/reconcile prior work in the area → refine the rule
> — each step a resumable app operation.

Below, that shape is expanded into the discrete **app operations** it implies (some of your arrows
hide more than one operation), each mapped to where the plan already gestures at it. The numbering
is the working agenda order, not a claim that they run strictly in sequence.

---

## A. The loop operations (each needs its own spec)

### 1. `prepare-for-read` — pick the unit, produce the candidate list
- **What it is.** Unit = a **book chapter** (§13.3). Output = a **list of candidate characteristics**
  to focus on. This is "pick a unit + screen (coarse)".
- **Open:**
  - What exactly seeds the candidate list — the existing `span_candidate`/`candidate_seed`, or a
    fresh screen, or both?
  - Is the chapter the input unit *always*, or genre-routed (poetic two-phase, narrative scene)?
  - What's the output record — a transient worklist, or a persisted per-chapter candidate table?
  - Does this operation itself get resumed, or is it cheap enough to re-run whole?

### 2. `select-next` — resume: which characteristic/Strong do I work next
- **What it is.** The chapter yields many candidates; they are **not worked together** (§13.3).
  This operation answers "where did I leave off" and hands you the next unit of deep work.
- **Open:**
  - What is the queue keyed on — Strong? Strong-set? candidate row? char_key?
  - What states does a work-item move through (untouched → in-progress → recorded → reconciled →
    closed), and where is that state stored (Layer Control `worklist`)?
  - Ordering: by verse order, by frequency, by researcher pick?
  - This is the concrete home of your "resume mid-chapter" thread.

### 3. `build-passage` — the operating passage for the characteristic
- **What it is.** For the selected Strong(s), assemble the **operating passage** — the adjacent
  verses over which it operates, **anchored on the main verse** (§13.3). The passage is an *output*,
  built progressively as work reaches the chapter (§13.6.2), not pre-computed corpus-wide.
- **Open:**
  - How is the boundary set — the movement-segment fitness test (§5: arc + interlocks), and by what
    signal (discourse cue / API-proposed / supplied outline)? This is the §11 open item.
  - How does this relate to the existing `passages` table you want to **repurpose** (§13.6.2)?
  - Can one passage serve several characteristics (shared operating span)?
  - Provenance: passage is a derived, revisable output — what's its revision story?

### 4. `screen-inclusion` — the core study act: IB-in-context or not
- **What it is.** Decide whether the Strong, **in this context**, is inner-being (§13.1: "the IB
  concordance is essentially the span table with the non-IB elements removed"). Includes **Screen-0**
  (human IB = subject; God = arena) and the **three-bodies split** (IB / other-being / physical body).
- **Open:**
  - Is inclusion one decision or three parallel screens (one per body)?
  - What's recorded on a **reject** — a logged exclusion (so it isn't re-screened blindly next pass),
    or nothing?
  - Where does **role assignment** (characteristic / qualifier / standalone / uncertain) sit —
    here, or in analyse (step 5)?
  - What are the inclusion **rules**, and are they `cfg_*` rows (they must be)?

### 5. `analyse-operation` — the deep read + lexical
- **What it is.** Read the passage for what the characteristic **does** (movement: trigger →
  operation → effect; associations; seats; tensions) *and* decompose it into the preset lexicon
  **dimensions** at original-language level (§13.1 lexical layer; §4 steps 2+4). Multi-phase:
  prepare-lexicon → assemble-meaning → (record) → reconcile (§13.3).
- **Open:**
  - The phase split: are prepare-lexicon / assemble-meaning / reconcile separate resumable
    sub-operations or one API call (§4 couples 2–4)?
  - Read-fresh guard (§4: entry held back until reconcile) — how enforced in the operation?
  - What is the unit of the *observation* it emits — the **grain** (§13.1: a distinct observation of
    a characteristic in operation, anchored on the main verse, cross-referenced not duplicated)?
  - Which dimensions are mechanical-floor (pre-computed) vs API (lexical-phase-plan §2)?

### 6. `record` — write the observation (distinct from reconcile)
- **What it is.** **Recording ≠ reconciling** (§13.4). This operation writes the fresh observation
  (grain + lexical + relations) as fact, *before* any comparison to prior work.
- **Open:**
  - What is written and where — occurrence, finding, ve_lexical, relation rows (§6), all in one
    write, or staged?
  - Is a recorded-but-not-yet-reconciled observation a first-class state (so the loop can stop here
    and reconcile later)?
  - Idempotency: re-reading the same verse — does record append, or match-on-write first?

### 7. `reconcile` — augment prior work in the area
- **What it is.** Set the fresh observation against **related prior findings**: confirm / extend /
  adjust / contradict → each a finding, adjustments as **revisions** (§4 step 3; §13.4). Must emit a
  **reviewable output** — the changes + related data — so the *next* reconciliation sees what the
  last did (§13.4). LLM proposes, researcher approves the non-obvious (Q4).
- **Open:**
  - The **reconciliation rules** (§13.4 says these need defining) — what are the confirm/extend/
    adjust/contradict triggers?
  - What defines "the area" / "related prior findings" — same char_key? neighbour edges? same
    Strong-family? same passage? (this is your **"already worked"** thread — see Thread C).
  - The **surface + repair** mechanism: what does the reviewable output look like, where does it
    live (a reconciliation log / `consolidation_queue`), and what is the repair action?
  - Boundary vs `consolidate` (§7): reconcile is per-observation-on-write; consolidate is the
    periodic sweep. Where's the line?

### 8. `refine-rule` — feed learning back without a bulk sweep
- **What it is.** When a read teaches you the rule was wrong/incomplete, change the rule (a `cfg_*`
  row) — **but locality, not bulk-update** (§13.2: bulk-update is the study's most-repeated failure).
- **Open:**
  - How does a rule change **propagate** to already-worked areas *without* triggering a global
    re-run? (this is your rule-propagation thread — see Thread D.)
  - Is a rule change versioned, and do prior observations record which rule-version produced them
    (so a refinement can target only the affected ones)?
  - Who authors the refinement — LLM-proposed, researcher-approved, same as consolidation?

---

## B. Cross-cutting threads (not steps — properties that thread through all of A)

### Thread U — the unit, per operation, and resume mid-chapter
Ties to steps 1–3. The unit is **not one thing** (§13.3): chapter for prepare, Strong(s)-over-passage
for analyse, the passage itself an output. **To flesh out:** a single table of *operation → input unit
→ output unit → resumable-on-what → state field*, so "resume mid-chapter" has a concrete home
(step 2's worklist).

### Thread R — record vs reconcile vs augment (three verbs, kept distinct)
Ties to steps 6–7. **To flesh out:** a crisp definition of each and the transition between them —
*record* = write the fresh fact; *reconcile* = compare to prior + emit revisions/review; *augment* =
the net effect on the entry (richer definition, appended findings). Confirm they are three actions,
not one, and name what each is allowed to touch.

### Thread C — what makes an area "already worked" (so back-fill knows what to deepen)
Ties to steps 2, 7, 8. **To flesh out:** the definition of an "area" and its worked-state — is it a
characteristic (char_key), a passage, a Strong-family, a chapter? What marks it done-enough that
returning means *deepen*, not *redo*? What signal tells back-fill *where the gaps are* (missing
dimension, unreconciled observation, stale rule-version)?

### Thread D — rule refinement without a bulk sweep
Ties to step 8. **To flesh out:** the propagation model. Options to weigh (not decide now):
rule-versioning + targeted re-visit of only affected observations; lazy re-evaluation on next
natural return to the area; a flagged "affected by rule-change" worklist. The whole point of the
growing concordance (§13.2) is that this is possible at all — so this thread is where the process
either honours or betrays the design.

---

## C. Proposed order to work through this

1. **Thread U first** (the unit/resume table) — it grounds steps 1–3 and unblocks everything.
2. **Steps 4–5** (screen-inclusion, analyse-operation) — the core study act; defines the grain.
3. **Thread R + steps 6–7** (record vs reconcile) — the augment-in-place machinery.
4. **Thread C** (already-worked) — needed before back-fill/reconcile is real.
5. **Step 8 + Thread D** (rule refinement / propagation) — last, because it depends on all above.

Steps 1–3 collapse into your `prepare-for-read`; steps 4–7 into `analyse-characteristic`
(§13.3) — so the two operations the plan already names are the containers, and this list is their
internals.

---

## What I need from you

Not to design any of these yet — just: **is this the complete set of steps and threads, and is the
order in §C the right one to open them in?** Add, cut, or re-order. Then we take the first one apart.

##########################################

researcher comments

Deciding on the entry point
there is not a single entry point
each entry point can be described as a study unit
Types include:
Bible Book : study unit is one of the following
genre dependent (poem, narrative)
chapter
A verse: this is triggered by a need to know what the verse is already saying, and to complete the study of the verse
An extract from the three concordances (cross verse for a specific characteristic)

Definition of completeness - when is it done
	when all the verses are covered in the concordance
AND is encapsulated by a lexicon
AND is have a meaning that is signed off, or cross referenced to a signed off meaning
verse State of completion - this is across all chars in the verse
Not started
In progress (there is some evidence, but incomplete
Not relevant (verse is excluded from all output indexes)
Concordance complete
Lexical complete/in progress
Meaning complete /in progress

Bulk operations - a number of operations can / or should be performed in bulk
Raw data
STEP data pull - initial (done)
STEP Data pull for strongs - on discovery of a strong or new word - new-word process
Seed update
Initial Seed assembly - (done manually)
Seed update - when a seed is missing, or need to be withdrawn, a process need to be in place to add/remove the seed, and automatically set-characteristics
span to IB Characteristic concordance
Initialise candidate characteristic - set-characteristic - done
Initialise concordances - one off bulk operation to create the first version of the three concordances. Resolve issue to split span in three concordances
Update candidate characteristic - any update to a span char state must flow through all the related tables and references
Rule refinements
this need more definition, but the app should trigger the need to refine completed works, the implications could be diverse.

Concordance table (columns to include) (maybe the concordance is not a physical table, but just a view)
Gloss, Strong, transliteration,  related words (maybe initially this is the registry word),Verse References

Reports and extracts - the following reports and extracts must be set in the app
Concordance (extracted from all three) options: exclude verse references; exclude related words (this view need to be tested)
Study unit status
Char status
Register status
Book Status
Validations & errors

It is important to note that I am re-introducing the register as a collection by organising the concordance by register.  This may necessitate some changes to the register item naming as the detail may not co-incide with the current name.  The other possibility is to do it around the clusters.

Meaning operations - this is the heart of the IB Process loop (these comments are in reference to IBA process loop - steps to flesh out
The meaning operations affects a number of tables
span - update role
concordances
passages (study unit)
lexicals
Operations
Meaning
Operations is a key new concept and table. for each char analysis, the char is affected / affects/ have a status/ come from / go to interacts or co-exist with other chars etc. (the dimensions). The operations table simply list each of these operations. Collectively these operations describe the characteristic in motion.

Researcher operations
Bulk operations
new-word
set-characteristic
initialise concordances
Specific operates
add / remove seed
add / remove candidate characteristic
reassignment of strong to another registry
start new study unit
interactively work with study unit
start new char focus
interactive feedback (not sure about this one)
get reports
 
Comments on document:
A1 - prepare-for-read 
will depend on nature of study unit.
Book + poem + short = study unit
Book + poem + long = devide poem in logical units = multiple study units
Book + narrative = split book in narratives = each becomes study unit
Book + chapter = split chapter into sections = each becomes study unit
Verse = get context from study unit previous assigned, if none, get genre, then follow book + genre rule
Characteristic = get verses and report. Researcher to select verses to study - follow verse pattern.
output of prepare-for-read - report with
text of study unit verses
candidate list of characteristics (include existing analysis if already exist)
DB update
study unit  - char - analytic status (new table)
verse - study unit (new index ???)
if prepare-for-read selected
check if study unit already started - options: create new, revise, select next char (present status of char)

A2 - select-next - researcher select a char to focus on. (allow a list also as input)
Deep read the study unit with the char in focus
Get existing information from a) the concordances, b) the lexicals, c) the operations
if non-existent then generate lexicals for all chars in the study unit - analyse-operation
i think this should include all the chars in the study unit, not only the char in focus

Check if any other char in the context have a interrelationship with the char in focus (screen-inclusion)
the rest of the analysis is performed for the char in focus on any other chars in direct relation to it
synergise the operations (new table)
validate the existing information (reconcile)
generate new meaning paragraph (new table)
Update the DB (record)
span - update role
study unit (passage) - update status
concordances - validate (check if role changes took place, amongst other checks)
lexicals - update / delete if replaced or not valid, save new
update - existing operations 
create - new operations
save to meaning to DB if changed
refine the rules (refine-rule)

