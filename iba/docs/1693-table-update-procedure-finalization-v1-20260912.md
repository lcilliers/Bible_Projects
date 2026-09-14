# Escalation #1693 — the table-update procedure — consolidated spec, for final sign-off

**Status:** consolidation for review, decision_required. Nothing built. This is where #1690/#1691/
#1692's separate "table-update procedure" sections converge — per the researcher's own framing,
**the table update is one operation, separate from any LLM session**, that reads a family's
finished JSON (process b's family/subgroup output, or process c/d/e's observation output) and
writes `cluster_subgroup`/`cluster_subgroup_strong`/`ib_observation`/`ib_node` rows. This document
is the operational spec for that one procedure; #1690/#1691/#1692 stay the table-shape specs it
writes into.

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
| `ib_observation` | assigns the permanent `id` (distinct from the LLM's own `source_json_serial`, which is kept alongside it); decides, per incoming observation, whether it's genuinely new, broadens an existing row's `obs_text`, or just adds another citation to an existing row — **this decision logic is the one piece of this whole design that is still completely undesigned, see §3** |
| `ib_node` | assigns `id`; denormalizes `cluster_code`/`cluster_subgroup_code`/`strong` onto each row, one row per referenced item when a citation names several of the same type (#1692 §4 item 2); **resolves `verse_reference` fresh against `iba.db.verse.reference`**, never trusting the LLM's JSON string directly; **NEW, 2026-09-14 (#1692 §3 item 5):** after load, validates every strong and every verse in the target subgroup's membership has at least one `ib_node` row across that session — an independent re-check of the LLM's own generation-time self-check (#1692 §2), not a trust-and-move-on |
| `ib_observation`/`ib_node`, from process (b) | **NEW, 2026-09-14, researcher's own words:** *"a placement_note that describes an observation about an item must find its way to ib_observations. That is why the responsibility of making the observation (LLM) and recording the observation in the right form and in the right place (load routine) is separated."* When loading process (b)'s output, a `cluster_subgroup_strong.placement_note` (or a cluster-wide note in that same JSON) that carries a genuine observation — not just a bookkeeping placement reason — is promoted into its own `ib_observation`/`ib_node` row(s), under the new `stage='subgroup'` value (#1691 §1/§9 item 8/10). **Mechanism undesigned:** how the procedure tells "this placement_note is just a reason" from "this placement_note is also an observation" apart is not decided here — a real, separate piece of the same/broaden/new problem in §3 below. |

## 3. The one piece with no design yet: same / broaden / new

**Outer structure partially resolved (researcher, 2026-09-13):** the procedure must first search
for a similar existing observation. If one is found, it adds a new `ib_node` row against that
existing observation (not a new `ib_observation` row). If none is found, it creates a new
`ib_observation` row together with its own new `ib_node` row. What remains undesigned is the
similarity test underneath that structure.

**Open reconciliation, not decided here:** §2's table above lists three possible outcomes for
`ib_observation` (genuinely new / broadens an existing row's `obs_text` / adds another citation to
an existing row); the researcher's structural answer above names only two (new observation+node,
or node-only against an existing observation). Left for the researcher to confirm whether
"broadens `obs_text`" is a sub-case of the node-only path (e.g. the procedure also merges wording
when it attaches a new node) or a third outcome not yet captured structurally — not assumed either
way here.

This is still the actual judgment call the whole two-pass architecture depends on:

1. **How is "this citation supports an existing observation" actually decided?** Exact text match
   is clearly insufficient (two independently-written claims about the same phenomenon will use
   different words). Options not yet weighed against each other: a similarity/embedding match; an
   LLM-judged comparison as part of the table-update procedure itself; a human-reviewed queue for
   anything below a confidence threshold; some combination.
2. **What happens on an ambiguous match** (a candidate could plausibly be 2+ existing
   observations)? Auto-pick the closest, always queue for review, or refuse and require the
   generation session to be more specific?
3. **Idempotency** — re-running the table-update procedure on the same family's JSON (e.g. after a
   correction) should not duplicate `ib_node` rows. This is currently blocked on `ib_node`'s own
   unresolved uniqueness defect (#1692 §4 item 1) — the `seq`-only key doesn't give the procedure
   anything reliable to check re-runs against yet.

## 4. What's already settled and doesn't need re-deciding here

- Verse-reference resolution: resolve fresh from `iba.db`, never trust LLM-authored text (#1682 §5,
  confirmed by the researcher).
- The LLM never assigns permanent ids, never checks for duplicates against the database, never
  decides edit-vs-new — all three are this procedure's job (#1691 §3, researcher's own framing).
- Denormalization happens here, at write time, not in the LLM's output.

## 5. What "finalized" would mean

§3 is the actual remaining work — a real algorithm, not a naming or column decision, and the
biggest single gap left across all four escalations. Everything else this procedure needs
(verse-reference resolution, denormalization, id assignment, the FLAG-as-signpost writing rule) is
already specified in #1690/#1691/#1692 and just needs implementing once #1692's `ib_node`
uniqueness defect and this document's §3 are both resolved.
