# Lexical-stack pipeline — open-items stocktake

**Date:** 2026-09-16 · **Requested by:** researcher, this chat turn — "take stock to see what is
still open in the pipeline to allow us to achieve the objective." **Objective, as stated:** build
the DB schema, configs, run modules, utilities, input/output JSONs, reports, and DB-update routines
for the entire pipeline from Layer 1 lexical generation to analysis-stage synthesis.

This is a **stocktake against the live escalation table and the #1706 consolidated build
proposal** — it does not re-decide anything, and does not invent a synthesis beyond what's already
on record. Where #1706 itself is now stale against a decision made since it was last edited, that
is flagged as staleness, not silently corrected.

---

## 0. The one finding that changes the picture: #1706 is stale on the #1705 gate

**#1705 closed yesterday/this session** with a reversal (researcher, verbatim): *"I am now leaning
toward guiding llm with the questions, rather than imposing T3 on the process... this escalation
can be closed."* No `verb_argument` model-expansion (significance grading / multi-M-code relation /
referent-identity widening) is being designed or built. Direction instead: feed the LLM the role
data + the catalogue questions and let it interpret context itself — the opposite of "superimpose a
structure the LLM must resolve."

**#1706 (the master build proposal, still open at v5, `ready_for_approval`... actually `review`,
assigned to you) has not been updated to reflect this.** As it stands today, the document says:

- §2 item 3: "`verb_argument` needs a real model expansion... **Undesigned. Confirmed gating, not
  parallel**"
- §3, `verb_argument (D9)` row: "See #1705 — spun out as its own model-expansion project"
- §5: "#1705 (`verb_argument` model expansion) — genuinely undesigned... should probably run as its
  own design escalation"
- §7 item 7: "DONE, 2026-09-15. Gates, confirmed... the actual redesign... is still undesigned and
  is the real remaining work"
- Phase G banner: "does NOT include #1705... **#1705 gates** — moved out of this phase... Design it,
  then it becomes a real, numbered precondition on Phase F"

**All five of these are now wrong.** There is no more "design it" — the researcher decided not to
design it. Practical effect: **Phase F (stage 8 reading, and Phase C/stage 5's Layer 2 lexical
question-answering) is not gated on a `verb_argument` redesign any more.** That gate is gone. This
is a real unblock, not a cosmetic wording fix — worth fixing in #1706 itself before using it as the
execution reference, since a stale gate reads as still-blocking to anyone (including a future
session) working off the document rather than the escalation history.

**I have not edited #1706 yet** — flagging it here first since it's a content correction to a
document you're mid-review-cycle on, not a build action. Say the word and I'll update it in place
(§2/§3/§5/§7/Phase G, five spots) to record the closure and drop the gate.

---

## 1. What's actually settled and ready to build (no open design question)

| Item | State | What's settled |
|---|---|---|
| Layer 1 rebuild shape (#1592/#1607) | design closed | Full corpus-wide rebuild, `role` redesigned to full `cluster_strong.cluster_code` array, `ambiguity_note`/`language` dropped, `resolved_sense` dropped entirely (moves to Layer 2) |
| `iba.cluster.status` lifecycle (#1697) | v6, `ready_for_approval` → Researcher | All 5 open items resolved this session — ordinal spellings, 1–2 vs 3–8 split, `ready_for_observations` rollup rule, manual-only `strongs_reassigned` handling, backfill rule. Needs your sign-off + `ALTER TABLE`/`cfg_enum` registration. |
| `cluster_subgroup`/`cluster_subgroup_strong` (#1690) | completed 2026-09-13 | DDL approved, build held only for the rest of the pack |
| `ib_observation` (#1691) | v18, in-progress, design-complete per its own §4/§9 | Not itself closed as an escalation yet — technically still open at `review`/Researcher despite #1706 calling it design-complete |
| `ib_node` (#1692) | completed 2026-09-14 | DDL approved |
| The recording pass (#1693) | completed 2026-09-14 | Same/broaden/new logic fully specified |
| Catalogue migration (#1696) | v10, `ready_for_approval` → Researcher | 98 candidate rows reviewed, migration approved in principle ("migration can proceed") but explicitly held until #1706 closes — genuinely blocked on your own sequencing, not a design gap |
| Lexical readiness Leg 3 (#1606) | completed 2026-09-15 | All 111 zero-allocation strongs classified; readiness check itself still needs registering as a persisted `cfg_method_rule` (Phase A item 1, not yet built) |

**Note on the pack:** #1706 §4 says "all 6 pack items are now design-complete," which is true
content-wise, but three of the six (#1682, #1683, #1691) are **still open escalations** at
`in-progress`/`review` rather than closed or `ready_for_approval` — worth closing them out
explicitly (or bundling them into the #1706 sign-off) rather than leaving them to linger as
separately-tracked items once their content is folded into the master proposal.

---

## 2. Genuinely open design gaps — real blockers on the build list

These are undesigned, not just unbuilt — #1706 Phase C names three of them directly:

1. **Layer 2's stage name/value** (`ib_observation.stage`) — candidate `meaning` or `lexical`, not
   chosen (#1706 Phase C item 13).
2. **Layer 2's scope grain** — per-strong corpus-wide in one pass, or per-cluster — not stated
   (#1706 Phase C item 14).
3. **Which catalogue question(s) Layer 2 links to** — candidates named (T1.1, T7.1) but not
   confirmed (#1706 Phase C item 15). This is now blocked behind #1696 landing in `iba.db` for the
   real FK to exist at all.
4. **Synergy-stage (process e) gating precondition** (#1706 §1 stage 10, #1695 raised-but-untouched)
   — deliberately deferred by you until build+test through the answer stage (stage 9) is complete.
   Correctly parked, not overdue.
5. **#1698 — synthesis stage is cross-cluster, `cluster_code` gap.** Still `in-progress`,
   `next_action=revise`, assigned to you since 2026-09-14 — a real open design question underneath
   item 4 above (the synergy stage needs a cluster_code home that doesn't currently exist), not yet
   folded into #1706's own treatment of stage 10.

---

## 3. Open items that touch the pipeline but aren't yet folded into #1706 at all

| # | What | Where it bites |
|---|---|---|
| #1658 | `cfg_table` has no way to register a view safely | The pipeline is about to register several new tables (`verse_meta`, `cluster_subgroup`, `ib_observation`, `ib_node`) and depends on existing views (`vw_strong_meaning_raw` for Layer 2). If any of those need view-shaped registration, this gap bites directly. Untouched since raised 2026-09-10. |
| #1665 | `cfg_*` structurally coherent, advisory findings need your input | Includes an orphaned `cfg_enum` group (`lexical_code_class`) — worth checking against the Layer 1 `role` redesign before it's registered, since that's exactly the kind of enum this rebuild will touch. Untouched since raised. |
| #1694 | 37 M-codes in `cluster_strong` have no `cluster` table row | Direct readiness-gate relevance: Phase D (cluster/subgroup readiness gates) assumes every `cluster_strong` code resolves to a real cluster row. Untouched since raised 2026-09-12 — not referenced anywhere in #1706. |
| #1700 | Answer-stage catalogue questions risk interpretive drift | In-progress, per-question review method built and running (T1/T2/T4/T5/T6 done per v7/v8) but **not finished** — T3 and beyond not confirmed done. This is exactly the catalogue the answer stage (process d / stage 9) will use; worth finishing before stage 9 executes for real. |
| #1702 | Cluster T-codes and answer-stage question coverage | Raised, untouched since 2026-09-14 — same catalogue-quality thread as #1700, not yet folded in. |
| #1703 | Adjacent-verse-context flag-not-fetch untested at scale | In-progress (v2) — a real open question about the reading stage's (stage 8) verse-fetch mechanism at full corpus scale, not referenced in #1706's stage-8 description. |
| #1701 | Inner-faculties framing | In-progress v4 — your core question was resolved via #1704 this session (cross-ref recorded), but the escalation itself is still open; #1706 §1 stage 11 already reflects the resolved framing correctly, so this is a closing formality, not an open design gap. |

---

## 4. Adjacent but not part of this pipeline's critical path

Flagged only so nothing gets silently assumed relevant: **#737** (debate-pipeline migration —
gated, last touched 2026-09-13, re-assigned to you), **#1526** (reading-strategy-vs-cluster-size —
correctly on-hold per your own instruction since 2026-09-07), **#1544** (soft-delete archive
routine — on-hold), **#1699** (IB Node Web visualization mockup — a jump-start request, not a
pipeline dependency). None of these block Layer 1→synthesis; none need action for this stocktake.

Also out of scope for this objective entirely: #770/#784/#1022/#1385/#1386/#1387 (search redesign,
prose management, citation mechanism, content_index redesign, Obsidian integration, USER-GUIDE
rewrite) — all on-hold, all unrelated to the lexical/analysis pipeline.

---

## 5. Bottom line

The design work is close to done — #1706 §4's "all 6 pack items design-complete" reads as accurate
content-wise, and this session removed what would have been the single biggest remaining gate
(`verb_argument`). What's left before Phase A/B execution can actually start:

1. **Fix #1706's five stale #1705-gate references** (§0 above) — a document correction, small.
2. **Close the sign-off loop** on #1682/#1683/#1691 (content-complete but still open as
   escalations) alongside #1697's and #1696's `ready_for_approval` sign-offs — one bundled
   decision, per the pack's own existing convention.
3. **Decide Phase C items 13–15** (Layer 2 stage name, scope grain, catalogue question links) —
   the one genuinely new, undesigned piece of the core pipeline.
4. **Register Phase A item 1** (lexical readiness as a persisted `cfg_method_rule` check) — build
   item, not a decision.
5. Optionally fold in #1658/#1665/#1694/#1700/#1702/#1703 — none block Phase A/B start, but #1694
   (orphan M-codes) and #1658 (view registration) are the two most likely to bite once table/view
   registration for the new pipeline tables actually starts.

Nothing in this stocktake is a recommendation to change any design — it's a factual position report
against the escalation table and #1706 as they stand right now.
