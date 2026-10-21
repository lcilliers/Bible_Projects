# Role-driven reading sequence — design capture

**Escalation:** #1704 (continues Phase 1's discovery into "what to do about it") · **Date:** 2026-09-15
**Status:** design proposal, researcher's own, captured verbatim + cross-checked live. **Not built. Decision required, not self-correctable.**

---

## 1. The researcher's model, verbatim

> "There is two parts to think about it: identifying it (which seems to be covered) and what to do
> about it. In each case this triggers a series of underlying observations unique to the type of
> cluster code role. Some of the observations are indeed already captured in the questions, others
> are still implied or silently ignored, expecting llm to think about it, which I think is risky.
>
> my thoughts on it is as following: a) llm recognise the role of the word b) depending in the role
> it then do discovery: i) is it the primary M-Cluster (strong is member of the subgroup) and set
> the word as the primary focal point of the context read - everything is considered in relation
> this strong ii) if it is another cluster M-code - this will require a relational observation to
> express how the M-code relate and operate together, it will also require a pointer observation to
> the other cluster iii) next in the reading sequence should be to find all the party-kind T-code
> roles. each of the party-kind have different questions. - this include things like source, target,
> impact, purpose, related words etc. iv) then the focus move the action words (T3) and its relation
> to each party-kind and include discovery of movement, force, negatives, descriptive words and the
> role of other key T-codes like names, places, natural objects, body parts etc. v) then the whole
> operation is reflected on in terms of the where is this happening (the faculty driver).
>
> I think this whole interrelationship between the roles and what it actual drives need to be much
> more explicit. The flow of questions is not in the order of the catalogue, the flow of the
> questions is driven by what is being explored and discovered. and that is framed by the roles of
> all the words in the verse."

The core architectural claim: **the reading process should be a role-driven walk, not a
catalogue-order walk.** Questions get answered as a byproduct of following the roles present in the
verse, not by iterating T0→T7 and hoping the LLM notices what's relevant. This is a direct response
to the risk named in the opening line — parts "implied or silently ignored, expecting the LLM to
think about it" — which is exactly what Phase 1c flagged (17 events, most either unwired or
relying on the LLM to infer connections no mechanism surfaces).

---

## 2. Step-by-step, cross-checked against what's live today

### (a) Recognise the role of the word

This is the same "role" concept established in [Phase 1b/1c](1704-analytic-event-inventory-phase1-discovery-v1-20260914.md)
and confirmed live this session: **role IS mechanically wired, but only for a minority of T-codes.**

| Wired today | Not wired today |
|---|---|
| T4/T7/T8/T9 (party_kind) via `cluster_strong` → `lib/lexical.py:load_code_classes`/`_layer1_fields` | T3 (operation flag exists on `cluster_strong.operation`, never read anywhere) |
| T5 (is_negator), same mechanism | T6 (connective note_type is a same-named but disconnected LLM vocabulary) |
| — | T2, T10, T11, T12, T13, T14, T15 (pure `cluster_strong` rows, zero consumption) |

So step (a) as stated — "recognise the role" — is only a solved problem for 5 of 13 T-codes. For
the rest, "recognising the role" means reading `cluster_strong` directly (or building the missing
Layer-1 carry-forward), since nothing surfaces it to the LLM automatically yet.

### (b)(i) Primary M-cluster → focal point

Checked live: **no strong currently carries more than one M-code** (0 of all `cluster_strong` rows
with `cluster_code LIKE 'M%'` have a duplicate strong). So this branch is not about one word
carrying multiple M-codes — it's about **multiple different words in the same verse each carrying a
different M-code**, and the reading pass needs to know which one is the "owner" (the
subgroup/characteristic this pass is actually running for) versus which are incidental. A code
routinely carries both an M-code and a T-code together (e.g. `G0080` = M14+T8) — that pairing is
exactly what steps (a)/(b) need to read off in one pass.

### (b)(ii) Other M-code → relational + pointer observation

This maps directly onto `cross_family_or_cluster_flags`, the answer-stage flag already named in
Phase 1a Vector C (`{statement, related_family, related_cluster}`) — currently prototype-only, no
config or DB home (same gap #1691 v16 names for process (b)'s ad hoc observations). The researcher's
model sharpens it: it should be **two separate observation shapes**, not one flag —
a *relational* observation (how the two M-codes interact) and a *pointer* observation (where the
other cluster's own reading can be found) — not a single freeform statement. Worth carrying this
distinction into #1691's observation-table design directly, not treating it as a new idea alongside
`cross_family_or_cluster_flags` — it's a refinement of the same gap.

### (b)(iii) Party-kind sweep, per-party question sets

This is exactly Phase 1c's **`directional-party-frame`** event (the single largest gap in the
catalogue — 18 questions across T0.1/T2.9/T4.1–T4.5) plus T4.6/T9 (spiritual beings, wired via
`party_kind` but zero findings ever, per #1700). The model adds a concrete requirement Phase 1c
didn't state explicitly: this has to be a **systematic sweep of every party-kind-tagged word in the
verse**, not a one-off check — find all of them first, then ask each one's distinct question set
(source/target/impact/purpose/related words). That sequencing detail (sweep-then-ask, per role) is
new and belongs in the event's own definition, not just its trigger logic.

### (b)(iv) Action words (T3) in relation to each party-kind, plus other referent T-codes

This is **`T3-operation-surfacing`** (Phase 1c's deepest gap, #1702) — but generalised beyond what
Phase 1c described. Phase 1c framed T3 only against T5.1/T5.3 (mechanism of change). This model
makes T3 the *pivot* of the whole action reading: the operation word's relation to **every**
nearby party-kind word AND every nearby referent-identity word (T10 places, T11 corporate, T12
objects, T13 natural-world, T14 body-parts). That's a wider job than the existing `verb_argument`
note_type currently models — `verb_argument` (config id 63) is defined as trigger(agent)/
impact(patient) `verse_lexical_id` pairs, which naturally carries party_kind pairing, but has never
been asked to carry a *referent-identity* argument (a T14 body-part, a T13 natural object) the way
this model requires. Worth flagging as a concrete widening of `verb_argument`'s own design, not a
new event — and a second confirmation that `verb_argument`'s near-total non-use (1 live example
ever, #1606/#1607) is the actual blocker underneath several of these steps at once, not just (b)(iii)'s.

### (b)(v) Faculty driver — where is this happening

This reopens, rather than resolves, an **already-open tension**: Phase 1c named T2.1 (Spirit-Level
Location: spirit/soul/heart/mind) as having **no T-code referent class at all**, because the one
prior attempt — the catalogue's own retired T3/Inner-Faculties tier — was retired as conceptually
wrong (#1598, and #1701's entity-vs-process critique, still open, `in-progress`, parked on the
researcher's own decision). Step (v) restates the same need from a different angle: not "what
T-code tags this word as a faculty" but "as a final reflective step, where in the being did this
whole action take place."

That reframing may actually be the resolution to #1701, not just another instance of the same
problem: **if "faculty" is a step-5 *reflection/synthesis* observation produced at the end of the
role-driven walk — not a lexical referent-identity tag sitting on a strong the way T10–T15 are — the
"conceptually wrong" objection to the old Inner-Faculties tier (treating faculties as fixed entities
you tag) may not apply to a process-level "where did this happen" judgement made after the fact.**
Flagging this connection for the researcher's own call — #1701 stays open and this doesn't decide
it, but the two items are clearly the same design question approached from two directions and
should be resolved together, not separately.

---

## 3. What this changes about the Phase 1 event list

Nothing already-identified in Phase 1c is displaced. What this adds:

1. **Sequencing is itself part of the design**, not an implementation detail — role discovery drives
   which events fire and in what order, per verse, rather than the catalogue's T0→T7 order
   controlling anything. This is the single biggest structural addition — Phase 1/1b/1c inventoried
   *what* events are missing; this names *how* a reading pass should actually walk a verse to
   produce them.
2. **(b)(ii)'s relational/pointer split** sharpens `cross_family_or_cluster_flags` into two distinct
   observation shapes — feeds directly into #1691's table design.
3. **(b)(iv)'s widening of `verb_argument`** to carry referent-identity arguments (T10–T14), not
   only party_kind pairs — a concrete design requirement for #1606/#1607's `verb_argument` build,
   not just "wire it up."
4. **(b)(v) reopens #1701** with a specific candidate resolution (faculty-as-reflection-step, not
   faculty-as-tag) rather than leaving it a bare tension.

## 4. Open for researcher decision (nothing here is built or self-correctable)

- Confirm/adjust the five-step sequence itself (a–v) as the controlling shape for the reading
  process design already underway at #1682/#1691.
- Confirm the (b)(ii) relational+pointer split as two DB-level observation kinds, not one flag.
- Confirm `verb_argument` should be widened to carry referent-identity arguments, and whether that
  changes its config definition (id 63) or needs a second note_type.
- Weigh in on the #1701 reframing (faculty-as-reflection-step) — does that dissolve the tension, or
  is there a reason faculties still need to be a per-strong tag?

This document doesn't propose a build order or touch any code/config. It's the grounding record
for #1704's next turn.

---

## 5. Researcher decisions, this round (2026-09-15) — recorded verbatim

> "I strongly believe that the reading sequence matter (five step sequence) and that progressive
> findings drive the further discovery. we simply must ensure that llm does not pick and choose, and
> silently ignore what it reads; it must follow a discovery path. the pointer observation kind must
> always sit on the side (as a separate observation) to point to discovery or further action outside
> of the scope of the verse or subgroup. this is what will drive intra-verse/subgroup/cluster
> synergies later on. verb-argument it is current definition fall far short. it must be expanded.
> verb operation is rich, extremely important for the study and not well understood. the same verb
> operates in relation to many different M-codes and its impact varies from incidental (nothing to
> discover or report) to actually be a core IB characteristic that drives a host of other activities
> and characteristics. at the moment verb-argument must carry this full load. regarding faculty:
> asking the question at the wrong time will give the wrong answer, therefore, it should be
> considered at the end of the read, on be an observation at subgroup level. the question driving
> this must be re-introduced (it would look differently that the ones that have been retired)."

### Decision 1 — sequence CONFIRMED, and it must be enforced, not suggested

The five-step sequence stands as the controlling shape, and each step's findings drive what the next
step looks for (progressive discovery, not five independent checks). Critical addition: this cannot
be advisory prompt wording the LLM is free to skim past — the process design (#1682's actual step
spec) has to structurally force the walk (e.g. an explicit per-role checklist the pass must work
through and account for before moving to synthesis), because "silently ignore what it reads" is
precisely the failure mode already diagnosed in Phase 1c (17 events, most either unwired or relying
on the LLM to infer a connection nothing surfaces). **Carries into #1682's process design as a hard
requirement, not a style preference.**

### Decision 2 — pointer observations are CONFIRMED as a separate, always-present observation kind

Relational observations stay in-scope (describe how two M-codes interact within this verse/
subgroup). Pointer observations are explicitly **out-of-scope-referencing** — they exist to queue
discovery or action that belongs to a *different* verse, subgroup, or cluster, not to resolve it
inline. This is the raw material for the not-yet-built synergy/cross-cluster stage (#1695 "Design:
cluster-reading synergy stage", #1698 "Synthesis stage is cross-cluster: cluster_code gap") — pointer
observations accumulate during subgroup-level reading and get consumed later, they are not answered
at the point they're raised. **Carries into #1691's observation-table design as a required kind,
distinct from relational.**

### Decision 3 — `verb_argument` is confirmed inadequate, needs a real model expansion (spun out separately, see below)

Current definition (agent/patient `verse_lexical_id` pair) cannot carry the actual load: the same
verb/operation can relate to **multiple different M-codes at once**, and its significance ranges
from incidental (nothing worth reporting) to a **core inner-being characteristic that drives a host
of other activities and characteristics**. This is a substantially bigger redesign than "add
referent-identity arguments" (§2 (b)(iv) above) — it needs its own significance/impact grading and
multi-M-code relation modelling. Raised as its own escalation (see below) rather than folded into
the #1704 corrective-action list, given its weight ("not well understood," the researcher's own
framing).

### Decision 4 — faculty CONFIRMED as an end-of-read, subgroup-level observation; #1701 reframing accepted

"Asking the question at the wrong time will give the wrong answer" — faculty is not a per-strong
referent tag (dissolving the "conceptually wrong" objection to the old Inner-Faculties tier) and not
even a per-verse observation; it is a **reflection made once, at the end of the read, at subgroup
level**. This resolves #1701's core "where do faculties belong" question. Still open: the actual
catalogue question driving this reflection needs to be **authored fresh** ("it would look
differently than the ones that have been retired") — not decided or drafted here, a genuine Phase 2/3
action item.
