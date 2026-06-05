# Verse meaning + keywords — exact instructions, v2_9 vs v3_0

> **Read-only extract, 2026-06-05.** The Pass-A / Phase-A sections (verse meaning + keywords) reproduced
> **verbatim** from each instruction, for inspection. Sources:
> `Workflow/archive/wa-sessionb-cluster-instruction-v2_9-20260526.md` §5 ·
> `Workflow/Instructions/wa-sessionb-cluster-instruction-v3_0-20260527.md` §5 (active; finalising).

---

## Exact differences at a glance

| | **v2_9 §5 (Phase 2 — Pass A)** | **v3_0 §5 (Phase A — Read + meaning)** |
|---|---|---|
| Scope | meaning record **only** | UT review **+** meaning **+** keywords |
| Keywords | **none — not mentioned at all** | `keywords` = **JSON list of 3–7 inner-being keywords** (since schema 3.25.0) |
| Relevance pass | (separate Phase 1 UT review) | **A.1 UT review** folded in: `is_relevant` + `ut_class ∈ {IB, CONTEXTUAL, OUT}` |
| Meaning column | `verse_context.analysis_note` | `verse_context.meaning_pass_a` **← doc says this; live column is `analysis_note`** |
| Meaning length | "1–2 sentences, ~250 chars" | "one-line meaning summary (~30–80 words)" |
| Batching | CC builds JSON batches of ~50 in canonical Bible order; group signal suppressed | per-verse API via `scripts/_run_pass_a_v{V}_*.py --cluster {code}` |
| Keyword structure | n/a | **unspecified** — no `[faculty][predicate]` rule (the 2-word form is emergent convention, not instructed) |
| Analytics | none | builds `wa-cluster-{code}-keyword-analytics-v1-{date}.md` |
| Exit gate | every is_relevant active row has `analysis_note` (SQL gate, must = 0 NULL) | every is_relevant=1 has `meaning_pass_a` non-null **and** `keywords` populated |

**Two things worth your eye:**
1. **Column-name divergence** — v3_0 prose names `meaning_pass_a`, but the live `verse_context` schema
   has **`analysis_note`** (no `meaning_pass_a` column). The M01 audit (B1a) reads `analysis_note` and
   found 945/945 populated; keywords (B1b) 0/945. So the doc and the schema disagree on the meaning field.
2. **Keyword spec is thin** — "3–7 inner-being keywords" with **no structural rule**. Yesterday's data
   showed they came out as 2-word `[faculty][predicate]` phrases, but that is *convention, not instruction* —
   directly relevant to the parked keyword-rules question.

---

## v2_9 §5 — Phase 2 — Pass A per-verse meaning record (verbatim)

> ## 5. Phase 2 — Pass A per-verse meaning record (CC, JSON template + API)
>
> **Purpose:** every `is_relevant=1` `verse_context` row receives a one-line meaning written to `verse_context.analysis_note`. The meaning answers: **what does this verse say about the inner-being characteristic the term names, in this verse's specific context?** Sub-groups, VCGs, and inherited structure are not visible to AI during this phase.
>
> **Owner:** CC. AI fills the `meaning` field in the JSON template.
>
> ### 5.1 Why this phase exists where it does
>
> The verse-meaning is a function of `(verse, term)`, not `(verse, term, sub-group)`. It does not depend on whether sub-groups have been defined yet — and recording meanings before sub-groups form prevents the inherited-structure contamination that v1_13's Phase 6 Pass A could not reliably prevent. Phase 3 (constitution debate) then has access to the meaning corpus, not just the gloss list, when deciding which terms belong in the cluster.
>
> **Pass A meanings are neutral by design (v2_5 note).** The §2.8 bias correction does NOT affect Pass A. The neutral-meaning rubric ("what does this verse say about the inner state the term names, in this verse's context") yields pure-human and God-directed meanings on equal footing. No re-running of Pass A is required when v2_5 amends the synthesis layer.
>
> ### 5.2 Inputs
>
> - All `verse_context` rows for the cluster's terms where `is_relevant=1` AND `delete_flagged=0` AND `analysis_note IS NULL`.
> - For each row: the linked `wa_verse_records` data (reference, verse_text, context_before, context_after, translation).
> - For each row's term: Strong's, transliteration, gloss, language.
>
> ### 5.3 Process
>
> 1. CC generates JSON batches of ~50 verses each in canonical Bible order across the whole cluster (not by term, not by sub-group — to suppress grouping signal in the batch boundaries). Each batch is labelled `"batch": "{N} of {total}"`.
> 2. CC sends each batch to the Claude API with a system prompt: cluster characteristic statement + meaning-record rubric (1–2 sentences, ~250 chars, plain English, verse-specific, no group framing) + strict-JSON output spec.
> 3. CC parses responses, validates that every `vc_id` is echoed back with a non-empty `meaning`, captures raw responses.
>
> ### 5.4 What is deliberately suppressed from input
>
> - `group_id`, `group_code`, VCG `context_description` — no inherited grouping visible.
> - `cluster_subgroup_id` — sub-groups don't exist yet, but even if they did they would not appear.
> - `is_anchor` — anchor designations are not relevant to meaning record.
> - Existing `analysis_note` — only NULL rows are sent; once filled, never re-sent.
> - Term co-membership lists — to prevent term-grouping anchoring within the cluster.
>
> ### 5.5 Output
>
> - UPDATE patch: one `verse_context.update` op per filled meaning. `match` on `id` (vc_id) + `delete_flagged=0`. `set` carries `{"analysis_note": "<meaning>"}`.
> - Pass A document: `Sessions/Session_Clusters/{code}/WA-{code}-passa-meanings-applied-v1-{date}.md` — per-batch counts, sample meanings, applied-patch reference.
> - Raw API responses archive: `Sessions/Session_Clusters/{code}/WA-{code}-passa-api-raw-responses-{date}.json`.
>
> ### 5.6 Hard gate before Phase 3
>
> ```sql
> SELECT COUNT(*) FROM verse_context vc
> JOIN mti_terms mt ON mt.id = vc.mti_term_id
> WHERE mt.cluster_code = '{code}'
> AND vc.is_relevant = 1
> AND COALESCE(vc.delete_flagged,0) = 0
> AND vc.analysis_note IS NULL;
> ```
>
> Must return **0** before Phase 3 begins. If non-zero, return to Phase 2 for the missing batch(es).
>
> ### 5.7 Post-check
>
> - Every is_relevant=1 active vc row in the cluster has `analysis_note` populated.
> - Meaning length distribution within expected range (50–400 chars typical).
> - No meaning text contains group-label markers (`[A]`, `[CLUSTER]`, VCG codes) — sentinel check; if present, the meaning was contaminated and needs re-running for that verse.
>
> **DB writes:** the UPDATE patch.
> **Cluster status:** unchanged.

---

## v3_0 §5 — Phase A — Read + meaning (verbatim)

> ## §5. Phase A — Read + meaning
>
> **Owner:** CC (programmatic, via API). No AI chat session.
>
> **Purpose:** for every cluster verse, classify whether it is inner-being-relevant (UT review) and, where it is, record its Pass A meaning and a set of inner-being keywords.
>
> **Single CC operation, two passes wrapped together.**
>
> ### §5.1 A.1 — UT verse review
>
> For each verse-record in the cluster's term set, classify:
>
> - `IB` — verse evidences cluster-relevant inner-being content
> - `CONTEXTUAL` — verse is in the term set but the term in this verse refers to outer-being / circumstantial / non-IB content
> - `OUT` — verse is mis-routed (term sense in this verse does not belong to the cluster at all)
>
> CC runs the UT classifier (`scripts/_run_ut_classifier_v{V}_*.py --cluster {code}`) which calls the Anthropic API per verse. Output: `verse_context.is_relevant ∈ {1, 0}` and `verse_context.ut_class ∈ {IB, CONTEXTUAL, OUT}`.
>
> UT review uses Pass A heuristics-only at this stage — full meaning derivation happens at A.2 for IB verses.
>
> ### §5.2 A.2 — Pass A meaning + keywords
>
> For each verse classified `IB` at A.1, CC runs the Pass A classifier (`scripts/_run_pass_a_v{V}_*.py --cluster {code}`) which calls the API once per verse and writes:
>
> - `verse_context.meaning_pass_a` — one-line meaning summary (~30–80 words)
> - `verse_context.keywords` — JSON list of 3–7 inner-being keywords (since schema 3.25.0 — per [feedback_phase2_passa_emits_keywords])
>
> Once A.2 completes, CC builds the cluster's keyword analytics report — `wa-cluster-{code}-keyword-analytics-v1-{date}.md` — frequency tables, top tokens, top co-occurrence pairs, per-term keyword density, per-sub-group top keywords (when sub-groups exist; for fresh clusters this section is omitted).
>
> ### §5.3 Output
>
> - `verse_context` rows updated (is_relevant, ut_class, meaning_pass_a, keywords).
> - `wa-cluster-{code}-keyword-analytics-v1-{date}.md`.
> - `wa-cluster-{code}-pass-a-summary-v1-{date}.md` — per-term verse counts, IB / CONTEXTUAL / OUT breakdown, sample meanings.
>
> ### §5.4 Pre-check
>
> - `cluster.status` ∈ {`Not started`, `Data - In Progress`}.
> - Cluster has terms assigned (`wa_term_inventory` rows where `cluster_code=?`).
>
> ### §5.5 Post-check
>
> - Every verse in the cluster's term set has `ut_class` set.
> - Every `is_relevant=1` verse has `meaning_pass_a` non-null and `keywords` populated.
> - Keyword analytics report written.
>
> ### §5.6 Status transition
>
> `Not started` or `Data - In Progress` → `Data - In Progress` (no change if already there; the formal transition happens at end of Phase B).
