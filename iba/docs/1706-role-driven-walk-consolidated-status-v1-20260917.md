# Role-driven walk — gathered, synergised, what's outstanding

**Continues #1706.** Per researcher instruction, 2026-09-17: *"next is to resolve role - so gather
and synergise, then we can figure out what is outstanding."* Full history read: escalation #1704
(14 versions, the design escalation), #1705 (7 versions, its verb_argument spinoff), the design doc
(`1704-role-driven-reading-sequence-design-v1-20260915.md`), and #1706's own §4A/Phase G. Nothing
new decided here — this is the gather-and-synergise pass, findings only.

---

## 1. The model itself — researcher's own words, #1704 §1 (2026-09-15)

A role-driven reading sequence, not a catalogue-order (T0→T7) walk: **(a)** recognise the role of
the word, then branch: **(b)(i)** primary M-cluster word → the focal point everything else is read
in relation to; **(b)(ii)** a different M-code word present → a relational observation (how the two
interact) *and* a separate pointer observation (where the other cluster's own reading lives);
**(b)(iii)** sweep every party-kind-tagged word, ask each its own question set (source/target/
impact/purpose/related words); **(b)(iv)** action words (T3) read against every nearby party-kind
*and* referent-identity word (places/objects/body-parts/etc.); **(b)(v)** a final reflection — where
in the being did this happen (the "faculty" question).

## 2. Confirmed decisions — #1704 §5 (2026-09-15), still standing

1. **The five-step sequence is confirmed, progressive** (each step's findings drive the next), and
   — the hard part — **it must structurally force the LLM through the walk, not rely on advisory
   prompt wording.** Researcher's own reasoning: "silently ignore what it reads" is the exact
   failure mode already diagnosed (#1704 Phase 1c: most of 17 discovered analytic events were
   either unwired or relied on the LLM inferring a connection nothing surfaces).
2. **Pointer observations are their own, always-separate kind** — out-of-scope-referencing, never
   resolved inline, accumulating as the raw material for the not-yet-built synergy stage (#1695/
   #1698). Relational observations (how two M-codes interact, in-scope) are a *different* kind, not
   the same thing loosely flagged.
3. `verb_argument` (the mechanism step (b)(iv) leans on) confirmed inadequate for the full load —
   spun into its own escalation (#1705). **See §3 — this is where the story gets complicated.**
4. **Faculty (step (b)(v)) is a reflection made once, at the end of the read, at subgroup level** —
   not a per-strong tag. This dissolved #1701's "conceptually wrong" objection to the old retired
   Inner-Faculties tier. **Built:** `T2.11` (Faculty Engagement) authored, #1701 now `completed`.
5. **(b)(i) clarified against live data:** 0 strongs carry more than one M-code — so this branch is
   about *multiple different words* in the same verse each carrying a *different* M-code, not one
   word wearing two hats.
6. **T2.1 (constitutional vocabulary: spirit/soul/heart/mind) — turned out not to be a gap at all.**
   Checked live: it's `M47`, an ordinary cluster (38 strongs), not a missing T-code. Its mechanism is
   the same cross-cluster co-occurrence event as T5.4/T6.1-3 (see §4 — not yet rebuilt).

## 3. The real tension, found gathering this — #1705's closure walked back part of §2 item 3

`#1705` set out to design `verb_argument`'s expansion (significance grading, incidental-to-core-
driver; relation to *multiple* M-codes at once — real research was done: live scenario verses
pulled for every T-code combination, 21,160 candidate verses identified). **It did not land there.**
Researcher's own closing words (#1705 v6, 2026-09-15 evening): *"I am concerned that we are trying
to over engineer the mechanical compilation of the verse, and then trying to induce it into
analysis in relation to the verbs... it is not likely the right strategy to try and set a pattern in
place to force it into an inner being role which it was never intended to be. I am now leaning
toward guiding llm with the questions, rather than imposing T3 on the process. I may revisit this
judgement after seeing how llm interpret and handle the questions, but will hold my judgement until
we had some results out of the new pipeline."* Effect: no rigid pre-imposed T3/verb_argument
structure was built; `verb_argument`'s `cfg_method_rule` (id 63) is still, checked live today, its
original narrow trigger/impact-pair definition, unchanged.

**Why this matters beyond just `verb_argument`:** §2 item 1 says the *whole* five-step sequence must
be structurally forced, not advisory. §3's closure says, for step (b)(iv) specifically, forcing a
rigid pattern onto T3 risks over-engineering and misrepresenting what verbs actually are in this
study. These aren't necessarily contradictory (one is about *sequencing discipline*, the other about
*T3's own internal schema*) — but the researcher's own words ("I may revisit this judgement," "hold
my judgement until we had some results out of the new pipeline") explicitly point at **exactly this
moment** — `verse_meaning`/Phase C is that new pipeline. The `1706` build doc's own Phase G
correction (2026-09-16) already noted #1705 "does not gate Phase F" and punted the actual T3
mechanism to "#1711's design output" — but #1711's actual resolution (checked, v11) never touched
T3/operation-surfacing or the forced-walk question at all. **The can was kicked forward twice, not
answered either time.**

## 4. Built vs. not — a plain scorecard

| Piece | Status |
|---|---|
| Faculty reflection (step v) | **Built** — `T2.11` authored, #1701 completed |
| T2.1 constitutional vocabulary | **Resolved as non-gap** — it's `M47`; mechanism (co-occurrence event) identified, not yet rebuilt |
| Cross-cluster co-occurrence event (`_assess_cross_cluster_cooccurrence.py`, #729) | **Still inactive** — checked live, no `cfg_step` registered for it at all |
| (b)(ii) relational/pointer split | Decided as two observation kinds — **not yet reflected in any tag**: today's tag work registered a pointer-shaped tag (`cross-cluster-significance`), no *relational* counterpart drafted |
| (b)(iii) party-kind sweep / `directional-party-frame` | Identified as the single highest-value gap (18 questions) and marked "buildable now" (#1704 Phase 3 Group A) — **not built**, no new mechanism found in code/config |
| (b)(iv) T3/`verb_argument` | **Explicitly NOT redesigned** — #1705 closed without a schema change, direction deferred to real pipeline results |
| The forced-walk mechanism itself, for `reading` (process c) | Confirmed as a requirement, but **"not yet written into #1682's process spec as a structural requirement"** (checklist rule 14's own words) |
| The forced-walk's applicability to `verse_meaning` (Phase C) | **Never actually decided** — flagged by #1706 §4A as #1711's job, #1711 didn't address it |

## 5. What's genuinely outstanding — needs your call

**Item 1 RESOLVED later the same session this doc was written, 2026-09-17 — found live 2026-09-17
in a LATER session, checking `Logs/SESSION-LOG-20260917.md` after the researcher asked whether
this work made it into the escalations. It hadn't — recorded properly now, against `#1706` (v32),
since `#1704`/`#1705` were both already closed before this decision was made.** Researcher's own
words, per the session log: *"no further mechanical role work necessary... the question is
expanded to explore the impact of the roles."* Effect: no structural/mechanical enforcement of the
5-step walk is being built; the resolution approach is expanding the catalogue questions
themselves to explore role-impact, matching the same question-driven-not-imposed-structure
direction #1705 v6 had already leaned toward for `verb_argument` specifically, now generalized to
the whole walk. **Open, genuinely unclear from the record:** was this "expand the questions"
already carried out via the same session's 12-dimension catalogue realignment (`#1712`), or is it
a distinct, still-pending action? Not found either way checking `#1712`'s own method doc — needs
the researcher's confirmation, not a guess.

1. ~~Does "structurally forced, not advisory" (§2 item 1) still stand as originally stated~~ —
   **RESOLVED, see above: no, superseded by the question-driven-expansion approach.**
2. **Does the role-driven walk apply to `verse_meaning` at all?** It was designed for `reading`
   (process c, post-subgroup, family-scoped). `verse_meaning` runs earlier, per-cluster, pre-
   subgroup — the same open question #1706/#1711 left hanging, now sharpened by §3's tension: even
   if the walk applies in principle, how much of it should be mechanically forced on a *first* run
   of a genuinely new pipeline, per your own "hold judgement until we have results" instinct?
3. **The relational/pointer split needs its "relational" tag counterpart** — today's tag session
   only produced the pointer half (`cross-cluster-significance`). Should I draft one, and does it
   belong in `ib_observation.tag` alongside it?
4. **Is `directional-party-frame` (party-kind sweep) in scope for this build**, or reserved for
   `reading`'s own later build? It's marked buildable now, but "buildable" was assessed against
   `reading`, not `verse_meaning`.
5. **T3-operation-surfacing's actual resolution approach** — given §3, is the expectation now that
   T4.1–T4.5 etc. simply get answered as ordinary catalogue questions with no dedicated structural
   event at all, or is some lighter-weight (non-"imposed") mechanism still wanted?
6. **`#729` reactivation** (T2.1/M47 and T5.4/T6.1-3's shared mechanism) — still nobody's build item
   on record. Worth a decision on whose scope this falls into.
