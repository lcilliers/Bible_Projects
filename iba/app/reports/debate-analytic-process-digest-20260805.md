# The debate analytic process — digested, reframed around the workflow (not the source documents)

**Date:** 2026-08-05. **Purpose:** the researcher judged the prior document-by-document summary
unsatisfactory — this reframes `WA-passage-read-guidance-v1.5`, `WA-interpretation-questions-v1.4`,
and the HIB/operation parts of `WA-verse-reading-technique-v4` around **what actually happens and
in what order**, using the researcher's own step skeleton as the backbone. Every rule below is
traced to where it comes from (`[v1.5 §]`, `[v1.4 Q#/B.#]`, `[v4 T#]`, `[BUILD §]`, or a named
session lesson) — nothing here is invented; this is a re-sequencing, not new content. Design/schema
implications are kept separate, at the end, and are **not yet built**.

**Terminology fix, applied throughout this document (per this session's direction):** "the
lexical" = the mechanical base-reading routine, referred to in recent dev discussion as
`span_reading`/T1-T3 — that dev-only name is retired from here on. **T1-T3 does not belong to the
debate process at all** — it is a separate, upstream routine the debate only checks for
completeness before starting. Only T4 onward is debate territory, and even T4/T5 fold into the
steps below rather than standing as their own stage.

---

## Failure modes the AI must actively guard against, every pass

Named directly by the researcher, added here because these are exactly the ways a technically
correct-looking process quietly produces a bad result — each one maps to a specific control below,
not just a caution to "be careful."

- **(a) Trying to do everything at once.** Steps 0-7 are deliberately discrete. Do not run lexical
  fetch, HIB identification, phenomenon registration, operation-writing, description, and DB-write
  as one undifferentiated pass "while reading the passage." Each step is its own action with its
  own output, checked before the next begins — the same discipline the app already enforces
  mechanically elsewhere (`chained=0` work packages: each step invoked and completed on its own,
  never auto-run together).
- **(b) Passages too large, made up of disconnected verse sets.** This is precisely what Step 2's
  HIB-continuity boundary exists to prevent — a passage's boundary must fall where the tracked HIB
  continuity actually breaks, not be stretched to fill a round chapter count. A small, tightly
  HIB-continuous passage is correct; a large passage papering over a real subject change is not,
  regardless of how convenient the chapter boundary looks.
- **(c) Trying to drive synergy across passages, or even chapters.** Explicitly out of scope for
  this process at every level: a Q7 linkage connects two *specific, already-registered*
  phenomena/operations within the *same* passage — never license to narrate a pattern across a
  whole range (Step 3/Step 7). Cross-passage and cross-book synthesis belongs only to the
  whole-book-read step and whatever comes after it — not to any individual passage's debate. The
  moment a thought reaches for "this connects to the broader chapter/book argument," it goes to the
  emergent-questions log, not into the phenomenon or operation being written.
- **(d) Not following all the sub-processes for each HIB and each phenomenon.** Nothing here is
  optional-by-omission — every HIB from Step 1 needs a phenomenon entry (even if the entry is
  "silent") in every verse of the passage it appears in, and every phenomenon needs an operation
  (even if the decision is "set aside"). See the working record below — this is the control that
  catches a silently-skipped HIB or phenomenon.
- **(e) Losing track during processing.** Long passages, long sessions, and context clearing all
  create real risk of re-deriving state from memory instead of from what was actually written down.
  The working record (below) exists specifically so state can always be read back from disk/DB,
  never reconstructed from what the AI "remembers" doing — matching this project's standing rule
  that the written record, not memory, is the source of truth.

---

## Step 0 — Get the lexical for every verse in scope

Before anything else: the lexical (base reading — full lexical range per span, morph-driven
stem/voice, role classification content-vs-function) must already exist, current, for every verse
the debate is about to cover. This is **not a debate step** — it is a **prerequisite gate**, run
and confirmed once per scope before Step 1 begins. `[t1-t3-design-decisions-20260805.md: "T1-T3 =
mechanical, deterministic, no interpretation... runs standalone, independent of T4-T9... no
awareness of what reads it downstream"]`

**Rule:** the lexical must be *complete in grammatical fact* for the scope — nothing downstream
touches raw span/strong/morph data again; if the lexical is incomplete for any verse in scope, stop
and build it first, do not proceed with a partial base. `[t1-t3-design-decisions-20260805.md,
"producer/consumer contract"]`

---

## Step 1 — Identify every Human Inner Being (HIB) across the verses in scope

Read every verse in scope (working from the lexical's row-level data, not the English gloss printed
above it — `[v4 T1]`) and list every human present in it. This is a **scope-wide sweep**, done
before any passage boundaries are drawn.

**Who counts as a HIB — the presumptive-candidate rule.** Every human mentioned — named or
collective, major or minor, however briefly — is a presumptive candidate: anyone who acts,
undergoes an act, thinks, speaks, refrains from acting, or is simply named as present. This holds
even where the act looks purely outward, administrative, locational, or incidental — the inner-being
content may be *hidden behind* the act, with only the act stated in the text. `[v1.5 step2 note f]`
Only "human" gets HIB status: a non-human being is in scope **only** where its state/characteristics
bear directly on a human in the same context — otherwise the verse is set aside entirely. `[v1.5
step2 notes b, d; v4: "Other non-human beings is likely to be stamped as agent. Only human being
words is stamped IB"]`

**Collectives stay collective.** A tribe, nation, "youths," "gentiles," etc. is recorded as one HIB
representing the collection — not decomposed into individuals — and any later operation involving
it is a movement to/from a collection, not an individual. `[v1.5 step2 note c; v1.4 Q8]`

**Referential/implied HIBs are named, not skipped.** Where a party is unnamed but implied by the
verse or wider passage — not always locally in this same verse — name it as a referential HIB;
never assert an inferred identity as settled fact. `[v1.5 step2 note e; v1.4 Part B.2/B.3]`

**Referent cruxes get resolved explicitly, here, before phenomenon work starts.** Where a pronoun or
unnamed party is genuinely ambiguous — several readings all grammatically live (e.g. "we" in Obad
1) — do not silently pick the obvious English reading: enumerate every live reading, give the
textual grounds for each, adopt one explicitly (stating whether this is a directed/researcher call
or this pass's own default), and keep the rejected alternatives on record. `[v4 T4]` This is the
one piece of former "T4" that survives as its own discipline — folded into HIB identification, not
a separate stage.

**Output of this step:** a flat list of every HIB in the scope, each tagged stated/named vs.
referential, with referent-crux resolutions recorded where they occurred. No phenomenon, no
operation yet.

---

## Step 2 — Divide the verses into passages, boundary = HIB continuity

A passage is a run of consecutive verses bound together by **continuity of the HIBs in focus** —
not an arbitrary chapter/verse-count chunk. Verses stay in one passage while the same HIB(s)
continue to be what the text is tracking; the boundary falls where the cast of HIBs genuinely
changes, not at a chapter number.

**Confirmed — this redefines what a passage is.** The prior model's passage boundary was
characteristic-driven (`passage.default_rule = "char-continuity"`, verses sharing a candidate
Strong's-code base); the redefinition here shifts the anchor to the HIB itself — the passage exists
because the same inner being(s) are being tracked, not because the same lexical characteristic
recurs. Same shape of rule, different anchor — see B4 below for what this means for
`passage.build`.

**Known gap, flagged plainly:** this app already has a mechanism for exactly this shape of rule —
`passage.build` / `passage.default_rule = "char-continuity"` ("run continues while consecutive
verses share ≥1 candidate base-strong") — but it is **dormant, retired 2026-07-26**
(`passage.rule`/`passage.source`/`passage.default_rule`/`passage.min_shared_strongs` all `NULL`/
inactive on every live row). It was strong-continuity, not HIB-continuity, but the underlying idea —
verses that share their tracked subject stay in one run, boundaries fall where that subject
changes — is the same idea this step now asks for, in HIB terms rather than Strong's-code terms.
Today, passage ranges are still chosen by hand (`-Chapters`/`-Range`, operator judgement) — this
step's rule is currently **applied by the analyst's own reading, not mechanized.** Whether to
revive `passage.build` reshaped around HIB-continuity, or leave this a judgement call the analyst
makes before invoking the debate for a chosen range, is a real open decision (see "What this
requires to build," below) — not resolved by this digest.

---

## Step 3 — Per passage: identify the inner-being phenomenon for every HIB, verse by verse (Phase 1 — complete before Step 4 begins)

For every verse in the passage, for every HIB present in it (from Step 1's list): isolate the
inner-being **phenomenon** — a state, disposition, or characteristic of that party's inner life.
`[v1.5 step3]` A phenomenon may be hidden behind a stated act or a refrained-from act, with only the
act recorded in the text — naming what the act is taken to evidence is exactly this step's job.
`[v1.5 step3 note e]`

**Record why, not just what.** For every phenomenon isolated, record the specific textual warrant
that grounds it (the verb, clause, or stated silence) and whether it is stated or inferred. This is
its own register entry — written **before**, and independently of, any operation. `[v1.5 step3b]`

**The phase-separation rule — the single most load-bearing discipline in the whole method.**
Step 3 must be completed for the **entire passage** before Step 4 (operations) begins for *any*
verse in it — not interleaved verse-by-verse. This is not a stylistic preference: it is the direct
fix for a real, observed failure. The Amos 1-3 debate — produced under the same multi-chapter
batching this app now uses — drifted from identifying a phenomenon per verse into identifying a
*general/textual* pattern across the whole range (a repeated oracle formula, a claimed
"ring-composition," a book-wide "thesis") and constructing operations to fit that pattern instead.
Running phenomenon-then-operation verse-by-verse reopens exactly this drift, because
operation-writing momentum bleeds into how the *next* verse's phenomenon gets identified. `[v1.5
change-control note, v1.4 change-control note — both dated 2026-08-02, both responding to the same
researcher review]` **Multi-chapter batched passages need the most vigilance here** — the larger
the range in one file, the easier it is for a literary/structural observation to masquerade as the
passage's own analytical content. `[v1.5 step6 note b]`

**A genuine literary/structural/genre observation is not a phenomenon.** If, while reading, a
recurring formula, structural device, or expected-but-textually-absent genre element is noticed,
it does **not** go into the phenomena register — it is logged once as an emergent question (Step 7)
for its own dedicated study later. `[v4 T5; v1.4 Part B.12, Q10]`

**How this gets controlled — not just instructed.** A written rule alone did not hold under the
Amos 1-3 drift, so the phase boundary between Step 3 and Step 4 needs an actual gate, not just an
instruction to sequence things correctly:

- At Step 2, when a passage is created, the **control total** is fixed: every HIB (Step 1) crossed
  with every verse it appears in in this passage = the exact number of phenomena-register entries
  (including explicit "silent" entries) Step 3 must produce before it can be considered done. This
  number is known in advance — it does not depend on trusting the analysis pass to remember to
  cover everything.
- Step 4 (operations) is **blocked from starting** until that control total is met and recorded —
  a real check against the working record (below), not a self-report. This is the same shape of
  gate the app already uses elsewhere (a step that checks a precondition and fails cleanly rather
  than proceeding on trust — e.g. `report.passage_debate`'s own `BaseExtractMissing` check today).
- The working record (see B5, "What this requires to build") is what makes this checkable at all —
  without a persistent, external list of what Step 3 owes and what it's delivered so far, "is Phase
  1 actually complete for the whole passage" has no answer except memory.

**Output of this step, per passage:** the phenomena register — complete for every HIB in every
verse of the passage, each entry carrying its textual warrant and stated/inferred status — before
Step 4 opens.

---

## Step 4 — Per passage: for each registered phenomenon, generate its operation (Phase 2 — a separate pass)

Only now, with Step 3 complete for the whole passage, generate an operation for each phenomenon
already in the register. **An operation may only originate from an already-registered phenomenon —
never identify a fresh phenomenon while writing one.** If writing the operation reveals that no
genuine phenomenon actually underlies it, that is a signal the Step 3 entry was mis-identified — go
back and correct or strike it; do not paper over the mismatch by writing an operation that quietly
reframes what the register said. `[v1.5 Phase 2 intro; v1.4 Part B.12]`

For each phenomenon, state what the verse says about it, in these parts (the researcher's
"source/process/target," mapped onto the method's existing four-part shape — the HIB itself is the
subject, so the analytical work is the other three):

- **Process** — is this a state/status, or a movement (come from / go to / impact on / emerge / go
  away / become evident)? `[v1.5 step3 note b; v1.4 Q6]`
- **Source** — where does it come from: self / another human / a non-human being / an object or
  situation? Keep **source of the interior state** and **source of enablement to act** distinct —
  a non-human being (e.g. the Lord) may be the stated source of an outcome or an enablement
  without the text sourcing the actor's own disposition; extending sourcing from outcome to
  interior is an interpretive step to flag, never to assume. `[v1.4 Q4, Part B.5]`
- **Target** — what does it impact: another operation, a human, a non-human being, a collective, an
  object/situation, or none? `[v1.4 Q5]`

Every operation also carries an **action-type label** — a short, natural, verb-based tag ("gave,"
"summoned/complied," "worshiped," "renamed," "bound and cast") — recorded regardless of whether the
phenomenon behind it resolved as stated, inferred, or a recorded silence. It is a label for later
cross-passage/cross-book comparison, not a taxonomy — no controlled vocabulary is being built by
recording it. `[v1.5 step5 note a; v1.4 Q11, Part B.10]`

**Interrogative discipline while doing this (Q1-Q12) — tools that serve this step, not steps of
their own:** is the party a focused inner being even where only an outward act is stated (Q1)?
What interior could underlie the stated act, and is it stated or inferred (Q2/Q3 — re-applying
Step 3's own stated/inferred call once the operation exists)? Is there sufficient data to weigh this
operation's significance, or must an insufficiency be named (Q9)? Where a human operation shares
action-type/vocabulary with, or is directly juxtaposed against, a stated divine operation *in this
same passage*, record the point of comparison/difference/inversion — but **only** where the text's
own juxtaposition or wording anchors it; a merely plausible resemblance is logged as an emergent
question, never asserted or theologically elaborated (Q12; `[v1.5 step5 note b; v1.4 Part B.11]`).
**Silence is itself a valid, recorded result** — "no phenomenon found, silent" is not an omission,
it is a finding. `[v1.4 Part B.4]` **Referential debates** (unnamed/implied parties from Step 1)
are conducted and recorded here too, if not already resolved — never imported as fact. `[v1.4 Part
B.2/B.3]`

**Output of this step, per passage:** one operation (process/source/target/action-type,
stated-or-inferred throughout) per phenomenon in the register.

---

## Step 5 — Describe the operation, per HIB, per verse, in the passage

Write the actual analytical prose that carries Steps 3-4's structured findings: what the text/
lexical data states (with Strong's codes cited — this is where the lexical from Step 0 is actually
read into the debate, not re-derived by hand); the operation and its parts; the interrogative
findings that bear on it; and a **decision** — retain / set aside as a stated-but-not-inner-being
operation / retain as a referential aspect / recorded silence. `[v1.4 Part C items 2-3]`

**Quick mechanical cross-check available here (former T6/T7/T9), not itself analysis:** every word
that explicitly names a human can be flagged *IB*; the noun causing the action can be flagged
*Agent* (a HIB can be an Agent for another HIB); every action verb can be flagged *Action*. These
are indicative highlights only, preliminary and non-conclusive — they do not decide which IB is
affected by which Agent or how it relates to a process; that judgement is exactly what Steps 3-4
already did properly. `[v4 T6, T7, T9]` Former T8 ("Process" stamp) is not a separate check — it is
already what Step 4's "process" question does directly.

---

## Step 6 — Create a DB record for each operation

**New this session, and a real change from how this has worked to date.** The result of the debate
— the phenomena register and the operations built from it — must be captured as structured DB
records, not left as prose inside an `.md` file with only a coarse `scaffold`/`filled` status
pointer (which is all `passage.debate_status` tracks today). The `.md` document becomes a
**generated extract off those DB records**, not the primary artifact — the same relationship the
lexical already has to `report.span_reading`: DB is the source of truth, the Markdown is a render,
produced on demand, never itself written to directly.

**Scope of the generated report:** a passage, or a book (a collection of passages) — generated
*after* the passage(s)' analysis is actually complete, not as a live working document during
analysis. This is a genuine shift from today's model, where `report.passage_debate` writes the
*working* scaffold the analyst fills in by hand. Under this model, the working/analysis surface and
the published report surface are two different things — **not yet designed** (see "What this
requires to build").

**Confirmed scope, per researcher clarification:** this is the IBA app's own equivalent of the
main study's `finding`/`characteristic`/`cluster_observation` model — a genuinely fresh design for
`iba.db`, not a port of those (closed, legacy, different-DB) tables. `iba.db` has no operation-level
analytical table today; this is new ground, sized to what Steps 3-5 above actually produce (HIB,
phenomenon, textual warrant, stated/inferred, process, source, target, action-type, decision) —
scoped and drafted only once B3 below is actually taken up.

---

## Step 7 — Passage-level and book-level closing sections (unchanged in substance, resequenced here for completeness)

Once Steps 3-6 are done for the whole passage:

- **Passage-level linkages (Q7).** What linkages run between this passage's own operations? Where a
  linkage is absent, surface the absence rather than passing over it silently. A linkage connects
  two *specific, already-registered* phenomena/operations — it is never license to narrate a pattern
  across a whole multi-chapter file as the debate's own content (the same anti-drift boundary as
  Step 3). `[v1.4 Q7, Part B.12]`
- **Insufficiencies register.** Data the lexical/base data does not carry, named, not filled from
  outside knowledge. `[v1.4 Q9, Part B.7]`
- **Emergent questions log.** Interpretive forks (not researcher decisions to make now — carried
  forward and weighed against the corpus as it grows, `[v1.4 Part B.9]`) and genuine literary/
  structural/genre observations (Step 3/T5's diversions) are filed here — per passage, never merged
  with another passage's log, resolved (if at all) only at the whole-book read. `[v1.4 Q10, Part
  B.12]`
- **Debate quality validation (Phase 3).** A closing re-examination, once the whole passage is
  assembled: for each phenomenon (or at minimum a representative sample across the passage) — is it
  genuinely an inner-being phenomenon, not a textual/structural pattern in disguise? Does its Step 3
  justification actually warrant it from the verse's own text? Does its Step 4 operation track
  faithfully back to it? **Correct any failure found before the passage debate is considered done —
  do not merely log it for later.** `[v1.5 step6, Phase 3; v1.4 Part C item 7]`
- **Open decisions / next steps.** `[v1.4 Part C item 8]`
- **Whole-book read** (separate, existing, unaffected step) — once at least one passage in a book is
  filled, gathers every filled passage's emergent-questions/linkages together for a book-level look.
  Not re-derived here; unchanged.

---

## Process logging — confirmed already in place

Checked directly: the `run` table (`run_id`, `work_package`, `state`, `started_at`/`ended_at`,
`outcome`) and `escalation` table (tied to `run_id`, question/answer/state) already back every step
invocation in this app — every example command in this whole document (`Chapter-Generate.ps1`,
`VerseSpanReading.ps1`, etc.) already runs through this logging, nothing new needed here. This
answers the "I hope this is already in place" check directly: yes.

---

## What this requires to build — status per researcher's direction, 2026-08-05

None of this is applied yet. Status below reflects the researcher's direction this round; design
work on B3/B4/B5 has not started.

**B1 — Terminology rename. Confirmed, proceed.** `span_reading`/T1-T3 language retired in favour
of "the lexical" throughout config, code, and docs (table, work package, step, column names). A
real but mechanical rename.

**B2 — App-wide report versioning. Confirmed, proceed — as config.** A single `cfg_setting` (not a
per-step convention, not hardcoded in `reportkit.py`) so every report writer versions its output
filename on regenerate instead of archiving-and-overwriting. Applies to `reportkit.write_report`
generally, not just the debate output.

**B3 — Operation-level DB schema (Step 6). Confirmed, proceed.** New table(s) to hold the
phenomena register and operations as structured rows (HIB, phenomenon, textual warrant, stated/
inferred, process, source, target, action-type, decision), keyed to passage/verse. This is a fresh
design for `iba.db` (not a port of the main study's closed `finding`/`characteristic` model — see
Step 6 above) and needs to carry the Step 3 control-total/phase-gate fields the "how this gets
controlled" note above depends on. Real design work, not yet sketched.

**B4 — Passage-boundary rules. Redefine, and wire into the debate process itself.** Two parts,
both directed: (i) redefine the passage rule around HIB-continuity (Step 2's "confirmed"
redefinition above, replacing the retired characteristic-based `char-continuity` rule); (ii)
passage creation/update must happen **as part of running the debate process**, not as a separate
manual pre-step the operator has to remember to run first. Concretely: this likely means reviving
something in the shape of the old `passage.build` mechanism, reshaped around HIB-continuity, wired
in as an early step of the debate work package itself (not a standalone tool run beforehand) — so
a debate run always works from a passage that's actually current for its scope, not a stale or
hand-picked range.

**B5 — Working record for process control. Proposed shape, not yet confirmed.** Building directly
on the researcher's own instinct ("perhaps a working record must be created... list of passages;
list of HIBs; list of phenomena; control totals... the md or json is used to manage the process
control") — and this is also the actual mechanism Step 3's control question depends on, so B3
and B5 are not separable. Proposed shape:

- A **per-passage control record**, created at Step 2 (passage creation) and updated through Steps
  3-6 — plausibly a JSON sidecar (machine-checkable, easy to diff) mirrored by control columns on
  the DB `passage`/operation rows (the JSON is the readable working view; the DB columns are what
  code actually gates on — same "DB is truth, file is a view" principle as everything else this
  session).
- Contents: the passage's HIB list (Step 1, filtered to this passage); the verse × HIB control
  total Step 3 must satisfy; running counts (phenomena registered so far vs. total expected;
  operations written so far vs. phenomena count; DB rows actually committed vs. expected) — enough
  to answer "what's done, what's left, does it reconcile" **by reading the record, not by
  re-deriving state from memory** (directly the fix for failure mode (e)).
- This is the same artifact that answers failure mode (d) — a HIB or phenomenon with no
  corresponding line in the control total is a visible gap, not a silent omission.

Not yet built. Given B3 and B5 share the same underlying schema work, proposing to design them
together in one pass, once confirmed — rather than B3 first and B5 bolted on after.
