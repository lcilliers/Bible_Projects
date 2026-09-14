# Escalation #1693 — the recording pass — consolidated spec, for final sign-off

**Name, 2026-09-14 — researcher's own request** (*"we need to get a nice name for this routine:
load/reconcile pass is clumsy. what do you suggest"*): renamed throughout this document to **the
recording pass** — the researcher's own description of it, almost verbatim (*"this routine records
the analytic work into a coherent and consistent set of knowledge elements as observations"*), so
the name states what it does rather than how ("load/reconcile" described mechanism; "recording"
describes purpose). Not yet finally confirmed — flagged for your review along with everything else
here. File name/escalation title left as-is for now; rename those too once you confirm.

**Status:** consolidation for review, decision_required. Nothing built. This is where #1690/#1691/
#1692's separate "table-update procedure" sections converge — per the researcher's own framing,
**recording is one operation, separate from any LLM session** (*"it is separate from the generation
of knowledge (analytics stages) to force a division of duties and improve overall quality
control"* — researcher, 2026-09-14), that reads a family's finished JSON (process b's family/
subgroup output, or process c/d/e's observation output) and writes
`cluster_subgroup`/`cluster_subgroup_strong`/`ib_observation`/`ib_node` rows. This document is the
operational spec for that one procedure; #1690/#1691/#1692 stay the table-shape specs it writes
into.

**DB location, 2026-09-13 (DB fork, #737/#1682): this procedure operates entirely within `iba.db`.
It must never read or write `bible_research.db` at any step.** All four tables it writes
(`cluster_subgroup`, `cluster_subgroup_strong`, `ib_observation`, `ib_node`) and everything it
resolves fresh against (`iba.strong`, `iba.cluster`, `iba.verse`) live there — see #1690/#1691/#1692
for each table's own DB-location note. One open exception, not yet resolved: `ib_observation.
question_code`'s source catalogue, `wa_obs_question_catalogue`, is still `bible_research.db`-only
(#1691 §7a) — this procedure does not currently need to write there, only #1691's process (a)/(b)
input-assembly step reads it, and that read is exactly the open question #1691 §7a raises, not
resolved here either.

**Guiding principle, researcher's own words, 2026-09-14** (from #1692, `ib_node`'s own banner):
*"everything can relate to anything, but the relation must be evidence based, supported by
observations, and must be meaningful. This places a major responsibility on #1693 to record
correctly, maintain appropriately, verify and validate on every turn, and self check as a matter
of primary accountability."* This is this procedure's own charter, not a suggestion — the §3
same/broaden/new logic and the new coverage check below both exist because of it, not as
add-ons.

## 0. Run structure (researcher's decision, 2026-09-13)

Each cluster-process run is three components, always run together as one unit, not staged
separately or on a deferred trigger:

(a) prepare and assemble the input JSON;
(b) run the sub-process — one of reading / answer / synergy (process c/d/e);
(c) run this DB-update procedure.

Step (c) fires immediately after (b) produces its JSON — it does not wait for a separate,
later-triggered batch run. This tightens §1 below: this procedure's input is always the JSON just
produced by the immediately-preceding sub-process run in the same unit of work, not an accumulated
batch of files picked up separately.

**★ NEW, 2026-09-13 — see #1697 + #1690 §3a** (two-level status/gating, same sign-off pack).
**Corrected this round: two levels, not one.** `cluster.status` is a rollup, not an independent gate
for subgroup-scoped stages — reading/answer/process (b) check and advance
`cluster_subgroup.status` (#1690 §3a); `cluster.status` itself only moves as a *consequence*.
Concretely, before step (b) runs:
- **Process (b)** (subgroup allocation) — genuinely cluster-grain: confirm `cluster.status=
  'ready_for_subgroup_allocation'` directly (including refusing if reset to `strongs_reassigned`
  since (a)'s input JSON was assembled).
- **Reading/answer** — subgroup-grain: confirm the target `cluster_subgroup.status` matches
  (`ready_for_reading`/`ready_for_answer`), not `cluster.status`.
- **Synthesis** — cluster-grain again (cross-family, no subgroup scope): confirm `cluster.status=
  'ready_for_synthesis'` directly. **★ OPEN GAP, 2026-09-14, not resolved here:** researcher confirms
  synthesis/synergy (process e) is actually cross-CLUSTER, not just cross-subgroup within one
  cluster (#1691 §9 item 9) — a single `cluster.status` check is a single-cluster precondition, and
  doesn't obviously generalize to "every cluster this synthesis run involves is ready." Raised as
  its own escalation, not designed here.

**As part of step (c)**, once this procedure's own writes succeed: advance the subgroup's own status
(reading/answer) or the cluster's (process b/synthesis) per the matched precondition above, **then
recompute the cluster-level rollup** — check whether every subgroup in that cluster (excluding
`FLAG`) has now reached the level needed for `cluster.status` to advance too, and apply that
advance (or regression, if a sibling subgroup had fallen back to `re_read_needed`) in the same
write. Not designed further here — full rule at #1697 §3, subgroup enum at #1690 §3a.

## 1. What it takes as input

- Process (b)'s family/subgroup JSON (§2, `iba/docs/1690-...md`).
- Process (c)/(d)/(e)'s observation JSON, each observation carrying its own `source_json_serial`
  (§2 item 1, `iba/docs/1691-...md`) and its supporting node segments (§2 item 2, same doc).

## 2. What it does, per table (pulled from #1690/#1691/#1692, not re-decided here)

| Table | Responsibility |
|---|---|
| `cluster_subgroup` | assigns `id`; resolves strongs against `iba.strong` (was `mti_terms.id`, changed 2026-09-13 DB fork — #1690 §2.2); writes the `FLAG` signpost as a same-cluster subgroup (confirmed, #1690 §3 item 3) |
| `cluster_subgroup_strong` | (was `mti_term_subgroup`, renamed 2026-09-13 — #1690) enforces `UNIQUE(strong)` — one strong, one family; also carries the required `placement_note` reason for any `FLAG` placement, and excludes `FLAG` members from the next reading-stage input (#1690 §3 item 3) |
| `ib_observation` | assigns the permanent `id` (distinct from the LLM's own `source_json_serial`, which is kept alongside it); decides, per incoming citation, whether it's genuinely new (incl. one that *expands on* an existing observation — RESOLVED 2026-09-14 as its own new row, not an edit, see §3), or aligns with an existing row closely enough that only superficial wording differs (edited in place) — **the similarity judgment itself is governed by §3's rules, not a from-scratch algorithm** |
| `ib_node` | assigns `id`; denormalizes `cluster_code`/`cluster_subgroup_code`/`strong` onto each row, one row per referenced item when a citation names several of the same type (#1692 §4 item 2); **resolves `verse_reference` fresh against `iba.db.verse.reference`**, never trusting the LLM's JSON string directly; **NEW, 2026-09-14 (#1692 §3 item 5):** after load, validates every strong and every verse in the target subgroup's membership has at least one `ib_node` row across that session — an independent re-check of the LLM's own generation-time self-check (#1692 §2), not a trust-and-move-on |
| `ib_observation`/`ib_node`, from process (b) | **NEW, 2026-09-14, researcher's own words:** *"a placement_note that describes an observation about an item must find its way to ib_observations. That is why the responsibility of making the observation (LLM) and recording the observation in the right form and in the right place (load routine) is separated."* When loading process (b)'s output, a `cluster_subgroup_strong.placement_note` (or a cluster-wide note in that same JSON) that carries a genuine observation — not just a bookkeeping placement reason — is promoted into its own `ib_observation`/`ib_node` row(s), under the new `stage='subgroup'` value (#1691 §1/§9 item 8/10). **Mechanism undesigned:** how the procedure tells "this placement_note is just a reason" from "this placement_note is also an observation" apart is not decided here — a real, separate piece of the same/broaden/new problem in §3 below. |

## 3. Same / broaden / new — RESOLVED, researcher's rules, 2026-09-14

**The reconciliation gap flagged since v6 is now closed.** §2's table used to list three possible
`ib_observation` outcomes (genuinely new / broadens an existing row's `obs_text` / adds another
citation to an existing row) against a structural answer that only named two. The researcher's
rules below collapse this cleanly into exactly two write actions, with the previously-ambiguous
"broaden" case now assigned a side:

1. **Outer structure (confirmed 2026-09-13, unchanged):** search first for a similar existing
   observation.
2. **If the difference is genuinely superficial** (the same underlying claim, different wording) —
   **align it: edit the existing observation's `obs_text` in place**, and add the new citation's
   `ib_node` row(s) against that same `observation_id`. Researcher's own words: *"superficial
   differences create noise — if it's possible, then align the differences into a single
   observation ([the recording pass] has the right to edit an existing item for alignment)."* This
   is the one case that edits `obs_text` after creation.
3. **If it genuinely EXPANDS on an existing observation** (adds real, new substance building on it,
   not just different wording of the same claim) — **RESOLVED: this is a NEW `ib_observation` row**,
   never an edit to the original. Researcher's own words: *"a observation that expands on an
   existing observation is regarded as a new observation."* The link back to what it expands on is
   `ib_node.traced_observation_id` (the existing "grounded in another observation" column, #1692
   §1) on the new observation's own node row(s) — exactly the same mechanism already designed for
   any other observation-to-observation reference, not a new column.
4. **If in doubt, create it as separate.** Researcher's own words: *"I don't want to over
   complicate this test... differences matter, don't fuzz them away."* Default to a new
   `ib_observation` row whenever the match isn't clearly superficial-only (rule 2) — never guess
   two claims together.
5. **The similarity test itself:** not a pure text match (two independent claims about the same
   thing will use different words), but not a heavy semantic/ML pipeline either. Researcher's own
   words: *"it is not a direct text match only, it does include judgement, mainly use heuristics
   and simple meaning."* A lightweight heuristic + plain-meaning comparison, not a from-scratch
   similarity engine.
6. **When to ask the researcher:** only when the recording pass's own judgment call is genuinely
   material, never as a routine habit. Researcher's own words, verbatim: *"it is ok to ask
   researcher for a judgement, but only if CC considers a judgement call as material (don't ask me
   just because you are trained to always ask at least 3 items for clarification — if you know the
   answer, don't ask.)"* This answers the old "ambiguous match" question directly: an ambiguous
   candidate is not, by itself, a reason to queue for researcher review — only a genuinely material
   one is; otherwise rule 4 (default to new) applies and the pass keeps moving.
7. **Idempotency / duplicates — resolved as a deliberate asymmetry, not a hard guarantee.**
   Researcher's own words: *"there is a risk of duplication in such cases — and would rather have a
   duplicate, than none at all."* The pass is NOT required to guarantee zero duplicates on a re-run;
   losing a real observation is the worse failure. **One case IS worth catching cheaply, not left to
   chance:** *"if the wording of the observation, and the ib_node references are all the same, then
   it is an obvious duplicate"* — an exact match on both `obs_text` and the full set of `ib_node`
   references is a true duplicate and should be recognized as a no-op, not re-inserted. Anything
   short of that exact match falls back to rules 2–4 above, with duplication as the accepted
   fallback risk, not a defect to eliminate at all costs.

**Not decided here, deliberately left to implementation:** the exact heuristic(s) under rule 5 —
per rule 4's own instruction not to over-engineer this, a first working version is expected to be
simple (e.g. strong+verse+surface exact match as the "obvious duplicate" fast path, a plain string-
similarity threshold for everything else) and refined from real behaviour, not fully specified in
advance of any real data existing.

## 4. What's already settled and doesn't need re-deciding here

- Verse-reference resolution: resolve fresh from `iba.db`, never trust LLM-authored text (#1682 §5,
  confirmed by the researcher).
- The LLM never assigns permanent ids, never checks for duplicates against the database, never
  decides edit-vs-new — all three are this procedure's job (#1691 §3, researcher's own framing).
- Denormalization happens here, at write time, not in the LLM's output.

## 5. What "finalized" would mean

**Narrowed, 2026-09-14.** §3 (same/broaden/new) — the biggest single gap left across all four
escalations — now has a complete rule set from the researcher; what's left there is deliberately
NOT specified further (§3's own closing note: a first heuristic implementation, refined from real
behaviour, not designed in advance). #1692's `ib_node` uniqueness defect (the old blocking
dependency) is resolved and that table approved (2026-09-14). The `placement_note` promotion
mechanism (§2 table, process (b) row) is the one still-open sub-piece, folded into this same §3
family of decisions. Everything else this procedure needs (verse-reference resolution,
denormalization, id assignment, the FLAG-as-signpost writing rule, the two-level status check/
advance) is already specified in #1690/#1691/#1692/#1697. Once you confirm the name (banner above)
and review this document: ready for the same sign-off as #1690/#1692.
