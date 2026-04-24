# VC Instruction — Substantive Ambiguities Needing Researcher Decision

**Date:** 2026-04-24
**Context:** Claude AI's v3_1 inspection (obslog [wa-global-vc_review-obslog-v1_0-20260424.md](../../data/imports/WA/Workflow/methodology_logs/wa-global-vc_review-obslog-v1_0-20260424.md) Entry 009) surfaced five items — A-01 through A-05 — that are not stale-text cleanup but **substantive semantic ambiguities**. v3_2 (the correction release) deliberately does not resolve them. This doc captures each item, shows the conflict, proposes options, and flags my recommendation for researcher ruling. **v3_3** of the VC instruction will incorporate the decisions.

---

## A-01 — JSON re-export vs DB-state-is-the-gate

**The conflict.** v3_1 §13.3 contains two statements that are mutually exclusive:

1. *"Re-renders of the per-term `.md`'s and any per-registry hybrid view are researcher-discretionary — they regenerate the same data from the canonical DB state; the state is already written."*
2. *"Then immediately re-export the full word JSON: `python -m engine.engine --export-word --registry={registry_no}` … This re-export is what opens the DataPrep gate."*

Statement 1 says the state is the gate. Statement 2 says the JSON re-export is the gate. Both cannot be right.

**Why it matters.** It affects what Claude Code must do on registry advancement. If DataPrep reads the DB state, the re-export is a convenience artefact. If DataPrep reads the JSON, the re-export is a required operation in the apply cycle.

**Three options:**

| Option | Semantics | Implication for CC |
|---|---|---|
| **(a)** DataPrep gate = DB state (`word_registry.verse_context_status = 'Complete'`) | JSON re-export is audit artefact only | Remove the "re-export is the gate" language; re-export becomes optional. Simpler. |
| **(b)** DataPrep still reads the per-registry JSON; re-export is still the gate | Per-term `.md` regen is discretionary; per-registry JSON regen is **not** | Preserve the re-export call as a required step in the apply cycle. The "discretionary" language applies only to the per-term `.md`. |
| **(c)** DataPrep reads DB state, and the full-word JSON re-export is dropped entirely | The JSON format is deprecated alongside the batch JSON | Cleanest, most aligned with v3_1's "DB state is the memory" direction; but: other tooling (Session B DataPrep, Dimension Review) may read the JSON today. Need to check before adopting. |

**My recommendation: (a).** It matches the v3_1 intent (DB is canonical; artefacts are views). The JSON re-export is retained as a convenience (researchers may still want the file on disk) but is not gating. This also sidesteps the operational cost of a re-export per-term-apply.

**Needs researcher decision:** which of (a), (b), (c)?

---

## A-02 — vc_status lifecycle: 'approved' semantics

**The gap.** v3_1 §7.8 and §13.1/§13.2 reference `mti_terms.vc_status IN ('complete', 'approved')` as the set of states that count as "done" for registry aggregation. But the instruction nowhere defines:

- What `'approved'` means, as distinct from `'complete'`.
- When it is set.
- Who sets it.

The M37 migration defined the controlled vocabulary (`not_done | to_revise | complete | approved`) and the applicator (VC-2) sets `'complete'` on successful per-term apply. Nothing sets `'approved'` today — yet the registry aggregation treats it as a valid terminal state.

**Three options:**

| Option | Who sets approved? | When? |
|---|---|---|
| **(a)** `'approved'` is set by a downstream stage (e.g. Dimension Review on cluster approval, or Session B on final analytical sign-off) | Dimension Review or Session B | After downstream validation confirms the term's classification stands |
| **(b)** `'approved'` is set by researcher directive only | Researcher via directive patch | When researcher explicitly signs off on a term's classification |
| **(c)** `'approved'` is aspirational; drop from the controlled vocab for now | — | Never, under v3_x. Revisit when a downstream mechanism exists. |

**My recommendation: (a) — set by Dimension Review at cluster approval.** Rationale: Dimension Review is the first downstream stage that reads a classified term's `verse_context_group` data and commits it to a dimensional placement. That commitment is a de-facto approval of the VC classification. DimReview's applicator flow could flip affected terms to `'approved'` when it marks a cluster stamped. This gives the vocabulary a concrete lifecycle.

**If we go with (a):** v3_3 documents `'approved'` is not written by VC; the DimReview instruction (separately) needs a companion edit to write it. v3_3 retains `'approved'` in the aggregation set so that already-approved terms are not accidentally downgraded.

**If (c):** Simplest — strip `'approved'` from the instruction and applicator code; aggregation only checks `'complete'`.

**Needs researcher decision:** which of (a), (b), (c)?

---

## A-03 — Prior-state posture when the input `.md` is stale

**The gap.** v3_1 §6.1 step 4 requires the classifier to state a per-term posture from the `.md`'s header block and flag any mismatch between the header's counts and the Existing verse_context groups table. But it does not address the freshness question:

What if the `.md` was rendered at time T, and between T and the classifier's session start, another session applied a patch that changed the term's prior state?

**Three options:**

| Option | Posture authoritative from | Freshness check |
|---|---|---|
| **(a)** The `.md` (render-time authoritative) | Classifier works against the `.md` as loaded; freshness is CC's responsibility before hand-off | Claude Code re-renders at session start if the term has changed since last render. CC tracks `mti_terms.vc_status_updated_at` vs the `.md`'s generation timestamp. |
| **(b)** Live DB (read-time authoritative) | Classifier queries live DB state at session start; posture is from live counts | Classifier has DB access. Counter to database-as-memory principle (snapshot discipline). |
| **(c)** Explicit per-session freshness protocol: CC regenerates all session `.md`s at session start as a mandatory step | Same as (a), with mandatory regeneration | Simplest guarantee; small cost (a few seconds of render per term). |

**My recommendation: (c) — mandatory per-session `.md` regeneration.** Cheap; deterministic; eliminates the staleness question. v3_3 §5.1 would include a trigger: "At the start of every classification session, regenerate the session's per-term `.md`s — deterministic, negligible cost, guarantees posture-to-DB consistency."

**Needs researcher decision:** which of (a), (b), (c)?

---

## A-04 — Session composition: how does CC know the session's term list?

**The gap.** v3_1 describes the session as researcher-composed (1..N terms), with `_patch_meta.terms_covered` naming the terms in the output patch. But the instruction does not specify how CC **learns the intended composition before the patch arrives** — i.e. which per-term `.md`s to render at session start.

**Three options:**

| Option | Mechanism |
|---|---|
| **(a)** Researcher names the terms when requesting renders (verbal / chat) | "CC, render per-term `.md`s for mti=6132, 6135, 6137 as session VCB-045" — CC renders, assigns batch_id, returns file list. |
| **(b)** CC renders on demand term-by-term; session identity crystallises only when the patch lands | CC makes no pre-session record; the session's identity is an artefact of the patch's `_patch_meta.batch_id` and `terms_covered`. |
| **(c)** A "session manifest" JSON artefact that CC produces before session start | A small document `wa-vcb-{batch_id}-manifest-{date}.json` listing the terms, registry memberships, and renders. The classifier sees it at startup. |

**My recommendation: (a) — researcher names terms at render-request time.** Simplest, matches current operational pattern, no new artefact. CC's render output announces the session id (`VCB-{nnn}`), and that id is used in all subsequent session outputs including the patch. If a session manifest is later desired for provenance, it can be generated retrospectively from the output artefacts.

**Needs researcher decision:** which of (a), (b), (c)? If (a), no new instruction text needed — v3_1 already describes it implicitly. A small §5.1 clarification might be added for the record.

---

## A-05 — Orphan-group check when cross-term verse movement occurs

**The gap.** v3_1 §6.2 Step 6 orphan-group check is per-term — it looks at pre-existing active groups for the term being classified and checks whether any now have zero active verses. But what if the classification moves verses **across terms** — e.g. a homograph split reassigns verses from `mti_term_id=A` to `mti_term_id=B`?

**Observation.** `verse_context.mti_term_id` is a FK, so "moving a verse between terms" is semantically: delete the old row (or soft-delete), insert a new row keyed to the other mti_term_id. Two separate operations, each in a different term's scope. The orphan-group check on term A would see the old group drained (correctly flagging orphan); the orphan-group check on term B would see its new group populated (correctly).

**So the check works in principle.** The instruction just doesn't spell out that cross-term movement is possible via this delete-then-insert pattern. A classifier unaware of the mechanism might try to "move" a verse without understanding it as two operations.

**Two options:**

| Option | Resolution |
|---|---|
| **(a)** Document cross-term movement as a delete-then-insert pattern in §6.2 | Adds one paragraph: "Cross-term verse movement (e.g. a homograph split reassigning verses) is a delete-on-one-term + insert-on-another-term operation. Each term's orphan-group check then naturally covers the draining and the filling. The session's patch must carry both operations; pre-submission validation will then correctly show zero orphans and correct new assignments." |
| **(b)** Cross-term movement is rare; leave unspecified and handle ad-hoc | Trust the pre-submission validation to catch issues; rely on the researcher to raise cross-term cases. |

**My recommendation: (a).** Cheap to document; prevents a class of confusion; doesn't add a new operation type. v3_3 gets the paragraph addition in §6.2 Step 6.

**Needs researcher decision:** (a) or (b)?

---

## Summary — five decisions for the researcher

| Item | My recommendation | Researcher ruling |
|---|---|---|
| A-01 DataPrep gate | (a) DB state is the gate | |
| A-02 `'approved'` lifecycle | (a) Dimension Review writes it on cluster stamp | |
| A-03 Stale-`.md` freshness | (c) Mandatory per-session regeneration | |
| A-04 Session composition | (a) Researcher names terms at render-request time | |
| A-05 Cross-term verse movement | (a) Document the pattern in §6.2 | |

On approval / redirection, v3_3 of the VC instruction incorporates the decisions. Each decision can be ruled independently — they don't interact.

---

*Produced 2026-04-24 after the v3_1 inspection (obslog Entry 009). These items are the only substantive ambiguities remaining after the v3_2 correction release; the 21 Category-1 stale-text items, the 3 Category-2 broken references, and the 3 Category-4 editorial items are all addressed in v3_2.*
