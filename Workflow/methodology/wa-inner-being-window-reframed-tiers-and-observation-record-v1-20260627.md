# The inner-being WINDOW (reframed tiers) + the observation record (DB capture)

- **File:** wa-inner-being-window-reframed-tiers-and-observation-record-v1-20260627.md · **2026-06-27 · Author:** Claude Code (recording researcher direction).
- **Builds on:** the verse-fan-out operating model, the completeness criterion (Exo 1:13 §9), the multi-contributor spiderweb. Proposal stage — the dimension set is a *starting, revisable* frame, to be refined by doing.

## 1. Two corrections that prompted this
- **A verse spawns one fan-out track PER inner-being operation, not one per verse.** Exo 1:13 starts **two**: *ruthlessness* (`perek`) and *enslavement* (`abad` Hiphil) — they fan out in different directions and intersect only at the rare coupling (perek+abad = 3 verses: Exo 1:13-14, Lev 25:46).
- **Observations must be captured as structured DB records**, not prose. The structure = a reframed tier.

## 2. The reframe: tiers as a QUESTIONING WINDOW, not a sorting grid
- **OLD tiers (T0–T7):** bins to *sort* terms/findings *into* (characteristic-level categories) — imposed, the debunked grid.
- **NEW window:** a fixed set of **questions the window asks OF each verse** to surface its inner-being involvement comprehensively. From **classification → interrogation.** The questions don't pre-decide the answer; they ensure the *full sweep* (the completeness criterion).
- It stays **open and revisable** — a `W+ discovery` slot feeds new questions back (emergence; never a sealed grid).

## 3. The WINDOW — the dimension-questions (starting set)
| dim | the question | (Exo 1:13 example) |
|---|---|---|
| **W0 Relevant?** | is the verse inner-being relevant, and *how* (not via the surface tag)? | yes — via ruthlessness + enslavement, NOT the tagged "serve" |
| **W1 What is present?** | which inner-being operation(s)/state(s)? *(may spawn multiple tracks)* | TWO: ruthlessness; enslavement |
| **W2 Source / from where?** | antecedent / driver / cause (incl. from context) | dread (v.12) |
| **W3 Seat / borne by whom?** | the seat or bearer | the Egyptians (actor); no named seat in-verse |
| **W4 Operation / what does it do?** | the act/movement (+ stem signal) | ruthless cruelty (*be-perek*); causative enslaving (`abad` **Hiphil**) |
| **W5 Object / on whom-what?** | the target/patient | the people of Israel |
| **W6 Process / how does it unfold / morph?** | the movement/transition chain | dread → ruthlessness⟷enslavement → bitterness (**Piel**) → serving (**Qal**) |
| **W7 Impact / what does it produce?** | the effect / produced state | enslaved + bitter state in Israel |
| **W8 Coupling / what binds with it?** | relations to other operations/terms | ruthlessness ⟷ enslavement (manner binds the Hiphil); both = power-over-weak |
| **W9 Colour / valence?** | moral register, where evident in-verse | condemned ruthless-enslavement (cf. Lev prohibition; cf. devotional serve-God) |
| **W+ Discovery** | anything the current questions don't capture | `abad` "cause-to-serve" is **valence-neutral** — oppressive / devotional / sin-burdening-God (Isa 43) — a new consideration |

**Completeness** = every W0–W9 *swept* (answered or marked silent) + W+ checked. **Complete ≠ resolved** — most answers may be `needs-corroboration`.

## 4. The OBSERVATION RECORD (proposed DB capture)
Each answer is an **observation row** — the dimensions ARE the schema:
```
observation(
  id,
  verse_id, reference, span_word_index, term_strongs,   -- WHERE (verse + span/term)
  track,            -- the fan-out track (e.g. 'ruthlessness','enslavement')
  dimension,        -- W0..W9 / W+   (the reframed tier)
  observation_text, -- the content
  status,           -- resolved | needs-corroboration | silent
  provenance,       -- mechanical | researcher | logos | claude-chat | scholarship
  basis,            -- the citation/morphology/contributor it rests on
  links,            -- related observation/verse ids (the spiderweb threads)
  created
)
```
- One verse → many observations (per track × per dimension). The `verse` table stays the anchor; observations link back to it and to spans/terms.
- `status` carries the resolved-vs-open distinction; `provenance` carries the multi-contributor witness; `basis` grounds it; `links` are the fan-out threads.
- **Focus points emerge** as recurring observations sharing a dimension/track across verses; **convergence** across `provenance` raises confidence.

## 5. Exo 1:13 — the window filled (both tracks) = the records we'd write
**Track: ruthlessness** — W0 relevant✔ · W2 dread *[needs-corrob]* · W4 cruelty(be-perek) *[resolved/morph]* · W5 Israel · W8 couples enslavement · W9 condemned *[needs-corrob]*.
**Track: enslavement** — W1 present✔ · W4 cause-to-serve(`abad` Hiphil) *[resolved/morph]* · W5 Israel · W6 causal chain *[resolved/morph]* · W7 bitter+enslaved state(`marar` Piel) *[resolved/morph]* · W8 couples ruthlessness · W9 valence-neutral operation *[needs-corrob, W+ discovery]*.
→ All dimensions swept across both tracks ⇒ **Exo 1:13 is COMPLETE** (surfaced), with its open observations (`needs-corroboration`) routed to the related verses (perek's 6; abad-Hiphil's 8; the conceptual ruthlessness/enslavement sets).

## 6. To confirm before building
- The **dimension set** (W0–W9 + W+) — keep, cut, rename, add? It must stay *revisable*.
- The **observation table** schema (§4) — fields right? Where it lives (new `observation` table, anchored on `verse`).
- Whether `track` is free-text or controlled.
- Then: build the table, capture Exo 1:13's observations as the first real records, and the fan-out has a memory.
