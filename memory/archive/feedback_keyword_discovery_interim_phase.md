---
name: feedback-keyword-discovery-interim-phase
description: Interim two-stage discovery phase for surfacing under-split characteristics inside large sub-groups before Phase 7
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7401fa55-df1f-434c-9ff3-b60b0138422f
---

**Status update 2026-05-23:** keyword extraction is now embedded in Phase 2 Pass A. The Pass A script (`_run_passa_via_api_v1_20260515.py`) emits both `analysis_note` and `keywords` per verse in a single API call; written to `verse_context.keywords` (JSON array; schema 3.25.0). Phase 5 brief now lists the cluster-level keyword analytics report as a structural input alongside the constitution report. For clusters going through Pass A from 2026-05-23 onwards, the discovery script below is no longer needed; the keywords arrive in the DB directly. The discovery script + DB loader (`_load_keywords_to_db_v1_20260523.py`) remain as **backfill tools** for legacy clusters whose Pass A predates the embedding — needed only when a closed cluster is reopened or revised. See [[feedback-phase2-passa-emits-keywords]] for the embedded flow.

---

**Original methodology note (retained for the backfill calling pattern):**

When a legacy Phase 5 sub-group's verse corpus is large (typically >150V) AND there is reason to suspect the AI smoothed over inner-being-faculty distinctions during characteristic identification, run a two-stage keyword discovery pass **before committing to Phase 7 VCG design** — not a Phase 7 process workaround.

**Stage 1 — per-verse emergent keyword extraction.** For every is_relevant verse in the target sub-group, the API returns 3–7 inner-being keywords that emerge from the verse text + Pass A meaning + span (`wa_verse_records.target_word`). Keywords must be:

- One or two words only (space-separated when paired, never hyphenated)
- Open-class only (verbs, nouns, pronouns; adjectives where they name an inner state)
- No particles, no proper names, no sentences
- Atomic and compositional — the SAME word reused across verses when the same operation is in view (so the clustering step works)

Reference script: `scripts/_keyword_discovery_subgroup_v1_20260523.py --cluster {CODE} --subgroup {CODE-X}`. Cost: ~$0.25 per 250-verse sub-group, ~6 minutes wall time.

**Stage 2 — keyword-pool clustering.** Frequency table + token families + within-verse co-occurrence pairs across the keyword pool surface candidate inner-being faculty axes. Reference script: `scripts/_keyword_cluster_analysis_v1_20260523.py --cluster {CODE} --subgroups …`. Output reveals whether the sub-group genuinely names ONE faculty (high concentration on 1–2 token families) or multiple (broad token-family distribution with distinct co-occurrence clusters).

**Why this is necessary.** At cluster-scale (hundreds of verses per sub-group), the AI's Phase 5 characteristic identification can smooth over distinct inner-being faculties under gloss-level labels ("sin as committed act", "sin as moral condition"). The keyword pass is more rigorous because it forces per-verse engagement and produces atomic, clusterable tokens rather than impressionistic group descriptions. M10 precedent (2026-05-23): keyword pass confirmed AI had under-split M10-A (10 faculty axes vs 1 claimed) and M10-B (12 axes vs 1 claimed), but was approximately right on M10-F (2 main faculties matching AI's claim).

**When to invoke.** Symptoms: (a) sub-group volume >150V AND (b) sub-group description bundles operationally distinct ideas (e.g. "as state OR as condition OR as universal" within one description). Don't invoke routinely — most coherent sub-groups (single lexical family, tight register) survive Phase 7 without this pass.

**What it informs.** Stage 2 output drives a focused Phase 5 revision delta — the existing sub-groups split into multiple characteristic-aligned ones. Phase 6 then re-applies for the changed sub-groups only (other sub-groups untouched). After the revision, Phase 7 VCG design proceeds at right-sized sub-groups with no working-memory strain.

Related: [[feedback-phase5-subgroups-represent-characteristics]] (the §8.0 principle this pass enforces); [[feedback-methodology-cycle-cost]] (the trade-off: the discovery cost is bounded and saves Phase 7 cycles later).
