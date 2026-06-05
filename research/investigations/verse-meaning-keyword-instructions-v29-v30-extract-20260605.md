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

---

# Governing & guiding inputs for Pass A (beyond the instruction text)

> Added 2026-06-05. The instruction §5 is only part of what governs Pass A. The rules below — from the
> settled **foundations**, programme **memory**, the v2_9 **bias clause**, and the new **Seven Principles**
> methodology — also bind or guide how meanings and keywords are produced. **Several are NOT yet written
> into v3_0 §5** (flagged ⚠️) and should be, as v3 finalises.

## A. Verse meaning is the ground truth (foundations §c + the two governing principles)

- **The verse meaning and context is the data and rules all analytics.** Cluster structure, characteristics,
  sub-groups, VCGs defer to what the verse says; when a lens and a verse meaning conflict, the verse wins.
  (`wa-study-foundations.md` §c; memory `feedback_two_governing_principles` P1; `reference_analysis_rules_finding_lifecycle`.)
- **All observations, however disjointed, must be recorded — bias-screening is forbidden** (P2). Pass-A
  application, verbatim from memory: *"when writing a verse meaning under a cluster's anchor term, if the
  verse evidences additional inner-being content beyond the cluster's characteristic, name it explicitly in
  the meaning. Do not compress for cluster-frame."* The M11 review showed bias compounds Pass A → sub-group
  → VCG → findings; naming the extra content at Pass A arrests it.
- **Surface contested / multiple readings; silence is a valid answer; no guessing** (foundations §c). A
  verse's meaning is interpretable and may read differently from different perspectives — that is surfaced,
  never hidden. ⚠️ *Not in v3_0 §5.*

## B. Scope & neutrality — Pass A is neutral by design (inner-being full scope; v2_9 §2.8)

- **Inner being = the entire human inner life** — moral, sensory, relational, material, illicit, vertical
  *and* horizontal — **no theological narrowing**. The inclusion bar is *"is an inner-being state evidenced
  in this verse?"* — never *"is it the right kind?"* (memory `feedback_inner_being_full_scope`.)
- **The spiritualising bias lives in the SYNTHESIS layer, NOT in Pass A.** v2_9 §2.8 (verbatim): *"NOT in
  Pass A meaning records (Phase 2). Verse meanings authored by API-driven Pass A are neutral; they capture
  pure-human content faithfully. The foundational data is sound."* So the §2.8 no-spiritualisation guard
  applies to Phases 1/3/5/7/8 — Pass A's job is the neutral capture that keeps the data sound.
- **Caveat (2026-06-04 finding):** "neutral by design" is the *intent*; the bias-trap exploration found
  Pass-A-layer transgressions anyway (reflexive `eschatological`, category slips, physical-rescue readings).
  So neutrality is the standard Pass A must *meet*, not a guarantee — hence the Group-E audit.

## C. The Seven Principles of Biblical Interpretation (the new governing methodology)

`Workflow/methodology/Seven_Principles_of_Biblical_Interpretation.md` — *"will guide the approach to verse
meaning"* (researcher, 2026-06-05). The disciplined workflow a sound meaning should reflect:

1. **Establish the text** (textual criticism) — what the verse actually says.
2. **Original language** — meaning *in use*, governed by grammar/syntax; **avoid etymologising** and
   **illegitimate totality transfer** (don't load every possible sense into one occurrence). *Bears directly
   on keyword discipline — a keyword must reflect the sense in THIS verse, not the term's whole range.*
3. **Historical-cultural context** · 4. **Literary context** · 5. **Genre** (poetry ≠ chronicle ≠ apocalyptic).
6. **Canonical / theological** (analogy of Scripture).
7. **"What it meant" → "what it means"** (meaning vs significance).
- **Governing posture:** where scholars genuinely disagree, *"present the options, not adjudicate them as
  though settled."* This matches foundations §c (surface contested readings) and directly indicts the
  reflexive `eschatological` pattern (a Principle-6 fulfilment question being pre-decided at Pass A).
- ⚠️ *None of this is yet reflected in the v3_0 §5 meaning rubric* — currently a single neutral one-liner.

## D. Keyword discipline (the format rules live in MEMORY, not in v3_0 §5)  ⚠️

v3_0 §5.2 only says *"3–7 inner-being keywords."* The actual format discipline is in
`feedback_keyword_discovery_interim_phase` + `feedback_phase2_passa_emits_keywords` (verbatim):

- **3–7 keywords**, **one or two words only**, **space-separated when paired, NEVER hyphenated**.
- **Open-class only** (verbs, nouns, pronouns; adjectives where they name an inner state); **no particles,
  no proper names, no sentences**.
- **Atomic and compositional — the SAME word reused across verses when the same operation is in view**, so
  the clustering/analytics step works.
- Purpose: the keyword **pool** reveals the inner-being **faculty axes** present in the corpus (independent
  of gloss-level term names); it is the structural input to Phase 5 sub-group design.

**Conflict with observed data (2026-06-04):** the live keywords violate this — hyphenated forms
(`god-saving`), and the emergent `[faculty][predicate]` 2-word shape isn't the instructed form. The
discipline was specified but not enforced/normalised. This is the parked keyword-rules question
(`project_keyword_analytics_revision_parked`): post-hoc normalise now vs controlled vocabulary at source —
and **whether to write the format rules into v3_0 §5.2** so the data is born analysable.

## E. The meaning contract & set-aside (brief classifier; set-aside informs meaning)

- **Per-verse brief contract** (`feedback_brief_classifier_pass`): one short plain-English sentence
  (**≤25 words**) on what the verse says about the inner-being characteristic via that term, **or**
  `set_aside` with one reason. Set-aside enum: `no_inner_being | physical_only | spatial_only | unclear`
  (`wrong_face` dropped). No morphology essay, no group framing. *(v2_9 said ~250 chars / 1–2 sentences;
  v3_0 says ~30–80 words — reconcile the length spec.)*
- **Set-aside still informs the word's meaning** (`feedback_setaside_verses_inform_word_meaning`): write
  `set_aside_reason` as an **evidence-based, verse-specific contribution to the term's semantic record**, not
  a curt dismissal — it characterises the term's non-inner-being senses.

## F. Evidence signal & downstream quality gates

- **Evidence completeness** (`feedback_evidence_signal_completeness`): judge a term's live evidence on
  `wa_verse_records.term_id` (99.99% complete) + active `verse_context`, **not** `mti_term_id` (98%, legacy
  NULLs). Validate "empty", never assert it. (Bears on which verses enter Pass A at all.)
- **Pass A quality is audited downstream** by the cluster audit **Group E** (E1 keyword well-formedness ·
  E2 normalisation duplicates · E3 interpretive-label corroboration · E4 anchor sense-fitness · E7 anchor
  meaning-coverage · E8 credit self-limiting meanings) — surfacing now, active in the meaning-keyword audit
  phase (`wa-cluster-audit-aspect-spec` §E; `project_audit_sequencing_clusters_then_meaning`).
- **The verse-meaning corroboration angle** (`project_next_action_audit_surface_verses`): anchor each
  meaning to its lexical sense + translations; surface contested readings; flag divergence — the standing
  audit angle on the meaning layer.

## Open items for v3 finalisation (what to write into §5)

1. **Field name:** §5 says `meaning_pass_a`; live column is `analysis_note` — reconcile.
2. **Keyword format rules** (D) — move from memory into §5.2; decide hyphen/normalisation policy.
3. **Meaning rubric** — currently a neutral one-liner; decide how much of the **Seven Principles** posture
   (esp. *present-don't-adjudicate* contested readings, and sense-in-this-verse) it should carry.
4. **Length spec** — reconcile v2_9 (~250 chars) vs v3_0 (~30–80 words).
5. **Surface-contested + name-extra-content** (A, P2) — write the "do not compress for cluster-frame" rule
   into the Pass A rubric explicitly.
