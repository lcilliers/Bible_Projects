# Role data — what it must contribute, and how to present it to the LLM

**Continues #1706.** Per researcher instruction, 2026-09-17: *"It is important to look at the
history, because it gives insight on the issue - but it is not the resolution. what is necessary
is to think through: what must the roles contribute to the analysis and how should the role data
be presented to llm to achieve those objectives. this is a multi-dimension objective because the
same data is reused from different angles. We need to get the balance right, not to try and be too
narrowly focused - it cuts other perspectives out, and not to be too sparse, because then llm will
do its own thing and is highly likely to miss stuff."*

This is a design proposal, not a decision — everything below is a recommendation for your
judgment, grounded in the previous gather (`1706-role-driven-walk-consolidated-status-v1-
20260917.md`) but genuinely thinking forward from it, not restating it.

---

## 1. What role data actually is, concretely, at the point a read happens

Per strong, in a verse, the live (or plannable) role-bearing facts are: which M-code cluster(s) it
belongs to (`cluster_strong.cluster_code`, multiple rows possible — carried forward onto
`verse_lexical.role` as a JSON array since Phase B); `party_kind` (T4/T7/T8/T9 — divine/human/
angelic); `is_negator` (T5); the `operation` flag (T3 — exists on `cluster_strong`, never read by
any code today); and whatever other T-code tags a strong carries (T2, T6, T10–T15) — checked live,
#1704: these exist as raw `cluster_strong` rows but are consumed by **no code at all** today. That
last fact matters directly for §3 below.

## 2. What each angle actually needs — the "contribution," not just the data

Five angles reuse the same underlying facts differently (the "multi-dimension" point):

1. **Primary-focus determination** — needs to know, of every word carrying an M-code in this verse,
   which one is *this run's own* cluster (the one being read) versus a different one. Contribution:
   an anchor to organize the whole read around.
2. **Relational + pointer** — needs the *other* M-code(s) present, and enough to state how they
   interact (relational) versus simply where to point (pointer) — these are different outputs from
   the same fact (another M-code is present), not different inputs.
3. **Party-kind sweep** — needs every party-kind-tagged word found as a set, up front, before any
   one of them is questioned — the sweep-then-ask sequencing #1704 flagged as its own requirement,
   not just a per-word check.
4. **Action/operation (T3) reading** — needs the operation word(s) plus everything *nearby* that
   could be its argument: party-kind words AND referent-identity words (T10–T14) in the same verse
   — the widest-reaching angle, since it reads everything else in relation to itself.
5. **Faculty reflection** — needs none of the per-word role data directly; it's a reflection over
   the *completed* read, at subgroup level, asked once at the end (already resolved, `T2.11`).

**The design implication:** angles 1–4 all draw on the *same* per-word role bundle, just asking a
different question of it. That argues for **one canonical structured annotation, not four separate
extracts** — duplicating the same facts four ways would be exactly the "too sparse to need but too
narrow per-angle" failure in a different disguise (redundant, easy for values to drift out of sync
with each other across the four copies).

## 3. Proposed shape — one role-annotated word list, walked five ways

**Present, once per verse (or per verse-batch), a structured list of every role-bearing word**,
carrying its full tag bundle — M-code(s), party_kind, is_negator, operation flag, and *every* other
T-code tag it carries, even the ones no code consumes today. Grouped by what it enables, not left
as a flat column dump:

```
roles_in_verse: [
  {strong, surface, cluster_codes: [...], is_home_cluster: bool,
   party_kind: "...", is_negator: bool, is_operation_word: bool,
   other_t_codes: [...]}
]
```

Then a **fixed walkthrough instruction** — not a free "consider the roles" prompt — that requires
the pass to visit this same list from each of the five angles in turn and account for what it found
(or explicitly found nothing) before concluding. This is the direct answer to "not too sparse": the
checklist forces coverage of every angle; it is the direct answer to "not too narrow": every T-code
tag is in the one shared list, not filtered down to only the mechanically-wired subset (T4/T5/T7/
T8/T9) — deliberately including T2/T3/T6/T10–T15 even though nothing currently *acts* on them
automatically, because excluding them would silently reproduce the exact gap #1704 spent five
phases diagnosing.

## 4. A proposed reconciliation of the §2/§3 tension found in the previous doc

The earlier doc flagged real tension between "the walk must be structurally forced" (#1704 Decision
1) and "don't impose a rigid pattern on T3" (#1705's closure). Thinking it through rather than just
reporting it: these read as compatible once split into two different things that were being
conflated —
- **Force the *looking*** (the checklist: did this pass actually visit every angle for every
  word, and record what it found, including "found nothing here") — this is what stops the LLM
  silently skipping something, the actual failure mode #1704 diagnosed.
- **Don't force the *shape of what's reported*** (a rigid trigger/impact/significance-grading
  schema imposed on every T3 finding regardless of whether the verb actually fits it) — this is
  what #1705 pulled back from, and rightly: forcing structure onto answers before real data shows
  what structure they actually need is the "over-engineering" concern in your own words.

**Proposed resolution**: the checklist forces *coverage* (every angle, every word, nothing silently
skipped); it does not force *output structure* beyond the ordinary observation shape (`tag`/
`obs_text`/`traces`) already common to every stage. A T3 finding gets reported as an ordinary
observation, tagged appropriately, in as much or as little structure as that instance actually
warrants — not slotted into a pre-built significance-grading form. **This is my own synthesis, not
a re-statement of anything already decided — flagging for your confirmation, not asserting it as
settled.**

## 5. Does this apply the same way at `verse_meaning` as at `char-reading`?

The shape doesn't need to differ — only the anchor does. At `char-reading` (post-subgroup), "home"
means the current family/subgroup. At `verse_meaning` (pre-subgroup, this build), subgroups don't
exist yet, so "home" can only mean the current *cluster* — angle 1 (primary focus) still works, just
one grain coarser. Angles 2–4 (relational/pointer, party-kind sweep, T3 reading) don't depend on
subgroup existing at all — they're verse-local. **Recommendation: the same role-annotation shape and
the same five-angle checklist apply at both stages**, anchored to whichever scope unit that stage
actually has (cluster at `verse_meaning`, subgroup at `char-reading`) — not two separate designs.
Flagging as a recommendation your read on §6 open items should confirm, not a decision made here.

## 6. Status

1–2. **Reserved for you, genuinely** — not resolved here. §1's `#1705` closing words are explicit:
*"I may revisit this judgement... will hold my judgement until we had some results out of the new
pipeline."* That's a deliberate, stated deferral, not an open item I have grounds to decide myself.
3. **RESOLVED, 2026-09-17** — include `T2`/`T3`/`T6`/`T10`–`T15` in the shared role list from the
   first real run. Grounds: the programme's own stated bias, found reading the prose (Chapter 1,
   registry construction): *"The cost of over-inclusion is visible and recoverable; the cost of
   silent omission is invisible and not recoverable."* `#1704`'s entire five-phase mission was
   uncovering exactly this kind of silent, invisible gap from premature narrowing — starting
   narrower here would risk repeating it. Not a judgement call requiring your input; the
   programme's own principle already answers it.
4. Still queued — write the forced-walk requirement into `#1682`'s process spec once §§1–2 are
   settled (they gate this, this doesn't gate them).
