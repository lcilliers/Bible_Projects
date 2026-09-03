# Glossary continuous validation — design addendum (v1, revised)

**Date:** 2026-09-02 · **Escalation:** #1377. Addendum to
[`1377-1377-glossary-mechanism-design-v1-20260902.md`](1377-1377-glossary-mechanism-design-v1-20260902.md) (still
itself unapproved). Revised in place, same day, per a second round of researcher correction —
the first draft of this addendum scoped the mechanism too narrowly (documentation reads/writes
only) and got the "what happens on discovery" behaviour wrong (allowed same-turn autonomous
glossary edits). Both corrected below.

## What changed from the first draft, and why

1. **Scope was too narrow.** Restricted to `Read`/`Edit`/`Write` on documentation paths. The
   researcher's correction: *"the scope should include when terminology is used or applied in
   code design/script development/db explore operations etc."* The chronic failure this whole
   mechanism exists to fix doesn't only happen in prose — it happens every time a script or query
   picks WHICH database field answers a question, and there are several plausible-looking wrong
   answers (see the worked example below).
2. **Purpose was mis-stated.** The first draft framed this as a drift-DETECTOR (catch it after the
   fact). The actual purpose, per the researcher: *"the surfacing hook should in real life drive
   you or me to be much more definitive on what we use, and what is the intended use... it must
   not fall back into just being a glossary lookup for existence."* This is a precision-FORCING
   mechanism at the point of USE, not a lookup-and-report mechanism.
3. **The discovery behaviour was wrong.** The first draft let a "small, unambiguous" glossary
   change be proposed and applied in the same turn. The researcher's correction is unambiguous:
   *"the behaviour's first reaction on discovery of a non match, or lack of clarity must be to
   surface it in chat"* — and, critically, *"it is very likely that the contention is resolved by
   using a different term and continue with no change to the glossary... I would not think that
   any of the process of contention handling is independent of researcher."* Corrected below —
   no autonomous path exists any more, at any size of change.

## The worked example that makes the scope correction concrete

Researcher's own test case: *"if I ask you to extract all words of a particular meaning, what
would you select — the lemma, surface, subgloss etc."* Answered honestly, against the real
schema, to show why this matters: **"extract all words of meaning X" is not one query, it's at
least three, and they give different result sets:**

- All rows sharing a **Strong's number / lemma** (`mti_terms`/bare Strong's) — every sense the
  lemma ever carries, e.g. every occurrence of a polysemous root like `abad` regardless of whether
  a given occurrence means serve/minister/labour/burden.
- All spans with a matching **literal surface text** (`span.surface`) — the actual written word
  form, independent of which sense or even which Strong's number it resolves to.
- All occurrences sharing the same **grain** (`wa_verse_term_links.step_subgloss_code`) — the
  actual per-occurrence sense the new verse-analysis method treats as the real rollup unit,
  explicitly NOT the same as the bare lemma (`mti_terms.owning_word` is stated, in the method
  doc itself, to be unreliable for sense — see the `grain` Glossary entry already drafted).

Before this mechanism, a request like "extract all words of X meaning" could silently get answered
against whichever of these three a script happened to reach for — and each answer is defensible on
its own terms while being a genuinely different result set. **This is exactly the kind of moment
the mechanism has to catch: not "is 'grain' a word in the glossary," but "which of these three
things does 'words of a particular meaning' actually mean here, and have we both said so before
writing the query."**

## Mechanism, corrected

### Scope: two genuinely different situations, not one

1. **Touching an existing document that already uses project terminology** (reading it to work
   from it, or editing it) — the original case. A mechanical text match against the Glossary can
   usefully assist here (see below).
2. **Choosing which term/field/concept to use when writing a script, a query, a report, or doing
   ad hoc DB exploration** — the case the researcher's correction adds, and the harder one. This
   is not "does the file contain a word" — it is "which of several live candidates does the task
   actually mean," decided BEFORE anything is written, not discovered after the fact by scanning
   what got written. **No hook can do this** — a script cannot know that "extract all words of
   meaning X" is ambiguous among lemma/surface/grain without understanding the request. This has
   to be Claude's own discipline, under a standing rule, not a mechanical surfacing.

So the design is now: a **narrow mechanical aid** for situation 1 (kept, scoped down further, see
below), and a **standing behavioural discipline** for situation 2, which is the one that actually
addresses the researcher's own worked example and the deeper, chronic problem.

### The standing discipline (situation 2 — the primary mechanism now)

Before writing any script, query, extraction, or report that selects data by a term which has
more than one live candidate meaning in the project (lemma vs. grain vs. surface; characteristic's
five grains; scope's four column-level senses; any term already in the Glossary with more than
one entry) — **state, explicitly, in chat, which one is intended, before writing the code.** This
is not a Glossary lookup for existence; it is naming the specific choice being made and checking
it against the researcher's actual intent, exactly as the worked example above requires. If the
Glossary doesn't yet have an entry disambiguating the candidates, that absence itself is the
signal to ask, not a reason to guess.

### The mechanical aid (situation 1 — kept, narrower than the first draft)

A `PostToolUse` hook on `Read`/`Edit`/`Write`, scoped to narrative/documentation paths
(`Workflow/**/*.md`, `docs/**/*.md`, `iba/docs/**/*.md`, root governance `.md` files) — unchanged
from the first draft, still useful as a low-cost reminder for the prose-touching case, but
explicitly **not** the primary mechanism any more, and explicitly **not** extended to code/query
files — a hook flagging every `.py`/`.ps1`/SQL touch containing a word like "term" or "word" would
fire on nearly everything and drown the signal, which is exactly the "just a lookup for existence"
failure mode the researcher warned against. Code/query precision is handled by the standing
discipline above, not by scanning what got written afterward.

## Behaviour on discovery — corrected, no autonomous path

Whenever either mechanism surfaces a non-match, a genuine ambiguity, or a term used two different
ways:

1. **First reaction is always a plain-chat surface to the researcher** — a real question, stated
   plainly, per the project's own standing interaction protocol (`docs/interaction-preferences.md`,
   `AskUserQuestion` banned, plain chat text instead). Never a silent decision, never an automatic
   escalation raised on Claude's own authority, never a same-turn glossary edit — no exception for
   size or apparent obviousness.
2. **The expected, common resolution is: pick a more precise term for THIS task and continue —
   the Glossary itself does not change.** Per the researcher: *"it is very likely that the
   contention is resolved by using a different term and continue with no change to the
   glossary."* Most surfaced ambiguities should end here.
3. **Only if the discussion surfaces a genuinely new or missing Glossary concept** does it become
   a Glossary content change — and that change goes through the **existing, already-well-defined
   prose CRUD cycle** (`Prose.ps1` export → edit → import, per `1377-glossary-mechanism-design-v1`
   §3) exactly like any other prose edit. Nothing new is being built for this step; it reuses what
   already exists.
4. **No step in this process is independent of the researcher** — not the decision that a term
   is ambiguous, not the choice of which precise term to use instead, not any Glossary change.
   Claude's job is to surface the contention clearly and propose candidates; the researcher
   decides.

## What this does NOT do (unchanged from the first draft, still true)

- Does not retroactively check documents/scripts nobody ever revisits — the deep-discovery
  register question (§ below) is unaffected by this correction.
- Does not replace judgement with a script's opinion at any point.
- Is not a hard block anywhere — every step above is a chat surface-and-discuss, never a gate.

## Open questions (yours, not assumed) — revised

1. **Where does the standing discipline (situation 2) actually get recorded** so it's followed
   consistently rather than relying on memory? Candidates: a `cfg_behaviour_rule`, a line in
   `docs/interaction-preferences.md`, or both (a behaviour rule for the mechanism, the interaction
   doc for the "surface in chat first" protocol it now explicitly reuses). Not decided.
2. **Path scope for the remaining mechanical hook** (situation 1) — same open question as the
   first draft, now explicitly narrowed to prose/documentation only, not code.
3. **Does the deep-discovery register still run** as a slower background pass for material this
   mechanism will never touch (situation 2 has no "touch" to trigger on for cold archive prose
   that's never queried or read again)? Unchanged open question from the first draft.

## Build status

Not built. Awaiting approval alongside the base design and this addendum together.
