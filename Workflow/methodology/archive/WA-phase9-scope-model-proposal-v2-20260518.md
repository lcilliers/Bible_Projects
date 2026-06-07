# Phase 9 scope model — proposal v2 (layered evidence aggregation)

**Date:** 2026-05-18
**Author:** CC
**Supersedes:** [WA-phase9-scope-model-proposal-v1-20260518.md](WA-phase9-scope-model-proposal-v1-20260518.md) (v1 retained for record; rejected by researcher per points captured in §1 below)
**Status:** PROPOSAL FOR DECISION. Not applied. Decision blanks at §10 for researcher mark-up.

**Required inputs**:

| # | Document | Purpose |
|---|---|---|
| 1 | This proposal | The layered architecture |
| 2 | v1 proposal (linked above) | Background; the model this supersedes |
| 3 | `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_5-20260518.md` §10 (Phase 7 VCG design), §12 (Phase 9 findings) | The phases this model reshapes |

---

## 1. What's wrong with v1 — researcher critique

Four specific issues with v1's cluster-primary single-pass model:

1. **"Anything that asks AI to read through a large body of verses is deemed to fail."** v1 said "AI reads the cluster's 1,116 verses and authors 189 cluster-scope findings." This is exactly the bulk-read pattern that produced M01's three Phase 6 restarts, M04's bias-driven set-asides, and the original Phase 9 dilution. The runaway-bus problem.

2. **"The questions are multi-dimensional — a single verse may answer multiple questions."** v1's top-down structure (189 prompts × scope) forces AI to revisit the same verse multiple times across different prompt cells, producing artificial separation of what is naturally one verse making multiple analytical contributions.

3. **"Not sure how the VCGs are helping with the positioning."** v1 used VCGs as a navigation tool only. They don't drive any analytical step. Their analytical potential is wasted.

4. **"Perhaps the direction of travel must change. And getting answers in layers."** Direction-of-travel correction: not "many prompts, AI reads everything" but "many small atomic readings → aggregate into layers."

5. **"The most difficult thing is to contain AI — the runaway bus."** Architecture must structure each AI session to be small, bounded, and resistant to overreach.

## 2. The right insight — bottom-up evidence aggregation

Stop asking AI to read large bodies. Build findings UP from the evidence in successive bounded layers, each layer working with the distilled output of the previous layer.

**The unit of bottom-up synthesis is the VCG.** A VCG is already a small bounded group of verses (typically 5–30) with substantively similar inner-being content. It's the natural AI-tractable unit:

- Small enough for AI to read carefully (verse text + Pass A meaning + VCG context_description)
- Cohesive enough that AI's synthesis isn't diluted by mixing registers
- Numerous enough across a cluster (~48 in M04) that they collectively cover the evidence

Each higher layer works with **already-distilled** output, not raw verse text. AI is contained at every level.

## 3. Proposed architecture — four layers

```
                  Pass A  Layer 0 — Verse-level meaning record (existing; done at Phase 2)
                            ↓ already populated in verse_context.analysis_note
                   ┌────────────────────────────────────────────┐
                   │ Layer 1 — VCG-level synthesis              │
                   │   per VCG: phenomena + prompt-tags         │
                   │   AI session = ONE VCG at a time           │
                   │   ~48 VCGs × small per-VCG work            │
                   └────────────────────┬───────────────────────┘
                                        ↓ VCG findings stored
                   ┌────────────────────────────────────────────┐
                   │ Layer 2 — Cluster-level prompt aggregation │
                   │   per prompt: synthesise VCG findings      │
                   │   AI session = ONE TIER (T0..T7) at a time │
                   │   189 prompts grouped into 8 tiers         │
                   │   reads VCG findings, NOT raw verses       │
                   └────────────────────┬───────────────────────┘
                                        ↓ cluster findings stored
                   ┌────────────────────────────────────────────┐
                   │ Layer 3 — Selective sub-group synthesis    │
                   │   only where publication-driven or where   │
                   │   register is structurally distinct        │
                   │   AI reads sub-group's VCG findings (small)│
                   └────────────────────┬───────────────────────┘
                                        ↓
                   ┌────────────────────────────────────────────┐
                   │ Coverage checks (CC mechanical):           │
                   │   - Every VCG has Layer 1 output           │
                   │   - Every is_relevant verse cited at L1    │
                   │   - Every catalogue prompt has L2 row      │
                   │   - Every L2 finding cites ≥1 VCG          │
                   └────────────────────────────────────────────┘
```

### Layer 0 — Verse-level Pass A meaning (existing)

Already populated by Phase 2 in `verse_context.analysis_note`. No change.

### Layer 1 — VCG-level synthesis (new, replaces Phase 9 sub-group sweep)

**AI input per session: ONE VCG.**

Per VCG, AI receives:

- The VCG's `context_description` (what the VCG names)
- The VCG's member verses (5–30 typical): reference + verse_text + Pass A meaning
- The 189-prompt catalogue as a checklist (NOT as prompts to answer one-by-one — as a multi-dimensional vocabulary AI can tag against)

AI produces:

- **Phenomena list** — 3–10 substantive phenomena the VCG evidences (the analytical synthesis)
- **Prompt-tags per phenomenon** — for each phenomenon, the catalogue prompt codes it speaks to (typically 1–5 prompts per phenomenon; some phenomena tag multiple prompts because they're multi-dimensional)
- **Anchor verse** — the verse most directly evidencing each phenomenon (often the VCG's existing anchor; AI may re-anchor a specific phenomenon to another member)

Output per VCG: ~10–20 lines of structured output. ONE AI session per VCG. Cluster has ~48 VCGs → ~48 small AI sessions (or batched into ~8–12 sessions of 4–6 VCGs each — still bounded and tractable).

**Containment for Layer 1:** AI never sees more than one VCG's verses at a time. AI's task is bounded (synthesise this small set; tag prompts). Pass A meanings are already done so AI doesn't re-read verse interpretation — only the synthesis step.

### Layer 2 — Cluster-level prompt aggregation (replaces Phase 9 cluster sweep)

**AI input per session: ONE TIER (T0..T7) of prompts + the VCG findings tagged to those prompts.**

For each catalogue prompt:

- Gather all Layer-1 phenomena that tagged this prompt across all VCGs
- Each prompt typically has 2–8 VCGs that tagged it (some prompts: 0 = silence; some prompts: 15+ = high-density characteristic-defining prompts)
- AI receives the gathered VCG-tagged phenomena (NOT raw verses) and synthesises a cluster-level finding

AI produces per prompt:

- A cluster-scope finding citing the relevant VCGs/phenomena
- Outcome code: E (evidenced — VCGs synthesised), S (silent — no VCG tagged this prompt; AI confirms the silence is analytically meaningful), G (gap — no VCG tagged it but the prompt should have evidence; surfaces for researcher review)

Output: 189 cluster-scope rows. **One AI session per tier (8 tiers).** Each session works with ~25–35 prompts' worth of VCG findings — bounded; AI reads distilled material, not raw verses.

**Containment for Layer 2:** AI never reads raw verses. AI works with already-distilled VCG findings (each ~10–20 lines). Even the busiest prompt has fewer than 20 VCG findings to synthesise per row.

### Layer 3 — Selective sub-group synthesis (optional)

For sub-groups flagged by researcher (e.g., publication-driven — each sub-group warrants a Session C chapter):

- AI takes the sub-group's VCG findings (already done at Layer 1)
- AI synthesises sub-group-level findings for the prompts where the sub-group has analytically distinct content vs the cluster pattern
- AI session reads the sub-group's VCG outputs (small) + the cluster-level findings for context

Output: variable — researcher-driven by which sub-groups warrant Session C chapter-depth treatment.

## 4. Why this addresses each v1 critique

| Issue | How v2 addresses it |
|---|---|
| AI reading large verse bodies fails | AI never reads more than one VCG at a time at Layer 1 (5–30 verses). At Layer 2 AI reads no verses — only distilled VCG findings. |
| Multi-dimensional verses | At Layer 1, AI tags a phenomenon to multiple prompts. A verse contributes to whichever phenomena its VCG names; no artificial separation. |
| VCGs help with positioning | VCGs become THE primary analytical unit. They organise evidence into AI-tractable chunks. Their analytical work drives Layer 1 entirely. |
| Direction of travel — answers in layers | Layered by design — verses → VCG → cluster → (optional sub-group). Each layer is distilled before feeding the next. |
| Containing AI — runaway bus | Every AI session is bounded: one VCG (Layer 1), one tier (Layer 2), one sub-group (Layer 3 if flagged). AI cannot run away because the input has hard scope limits at every step. |

## 5. New schema — what's stored where

| Layer | Stored in | Notes |
|---|---|---|
| Layer 0 (Pass A) | `verse_context.analysis_note` | Existing |
| Layer 1 (VCG synthesis) | NEW: `vcg_finding` table OR overload `cluster_finding` with `cluster_subgroup_id=NULL, group_id=<vcg_id>` rows | See §6 for the storage decision |
| Layer 2 (cluster aggregation) | `cluster_finding` rows with `cluster_subgroup_id=NULL` and `group_id=NULL` (CLUSTER scope) | Existing column structure |
| Layer 3 (sub-group selective) | `cluster_finding` rows with `cluster_subgroup_id=<sg_id>` | Existing column structure |

## 6. Storage decision — where do Layer 1 (VCG) findings live?

Two options:

**Option A — Overload `cluster_finding` with VCG scope.**
- A row with `cluster_subgroup_id=NULL, group_id=<vcg_id>` represents a VCG-scope finding.
- Existing schema; no migration.
- Loader at §14.4 needs an update to handle this scope type.

**Option B — New `vcg_finding` table.**
- Separate table cleanly distinguishes "atomic VCG synthesis" from "aggregated cluster/sub-group findings".
- One migration.
- Better data shape — VCG findings are typically multi-tag (a single phenomenon tags multiple prompts), which doesn't fit cluster_finding's UNIQUE constraint on (obs_id, cluster_code, cluster_subgroup_id, vcg_scope, version) cleanly.

Recommendation: **Option B** — a dedicated `vcg_finding` table avoids constraint contortions and keeps the analytical model clean.

Proposed `vcg_finding` schema:

```
vcg_finding
  id PRIMARY KEY
  vcg_id NOT NULL (FK verse_context_group.id)
  phenomenon_seq INTEGER NOT NULL  -- ordering within the VCG
  phenomenon_text TEXT NOT NULL     -- the substantive synthesis
  anchor_vc_id INTEGER              -- which verse most directly evidences this phenomenon
  source TEXT, version TEXT, notes TEXT
  delete_flagged INTEGER, created_at, last_updated_date
  UNIQUE (vcg_id, phenomenon_seq, version)

vcg_finding_prompt_tag (m:n between vcg_finding and wa_obs_question_catalogue)
  vcg_finding_id NOT NULL FK
  obs_id NOT NULL FK
  delete_flagged, created_at
  UNIQUE (vcg_finding_id, obs_id)
```

This shape captures: a VCG has multiple phenomena; each phenomenon tags multiple prompts. Clean. The Layer-2 aggregator joins on prompt_tag to gather per-prompt evidence.

## 7. Workload estimate for M04

**Layer 1 (per VCG):**

- M04 has 48 VCGs.
- AI session per VCG: ~10–20 min (read VCG + author phenomena + tag prompts).
- Batchable: 4–6 VCGs per chat session → 8–12 sessions for M04.
- Output: ~250–400 `vcg_finding` rows (avg 5–8 phenomena per VCG) + ~750–1,500 prompt tags.

**Layer 2 (per tier):**

- 8 tiers × 1 session each = 8 sessions.
- Per session: AI reads VCG findings tagged to that tier's prompts (small; bounded).
- Output: 189 cluster_finding rows.

**Layer 3 (optional):**

- 0 by default. Researcher flags specific sub-groups for chapter-depth treatment.
- Per flagged sub-group: 1–2 AI sessions.

**Total M04 workload:** ~16–20 AI sessions for the full Phase 9 under v2 (Layers 1 + 2 + optional 3).

Compare to strict matrix model: would have been ~30–50 sessions for 189 × 16 sub-groups + cluster = 3,213 cells.

**vs v1 proposal:** v1 said 3–4 sessions, but each was unbounded (read 1,116 verses) — predicted to fail. v2 is more sessions but each is small and tractable.

## 8. Completeness checks under v2

Four checks replace the strict matrix:

1. **Pass A completeness** — every is_relevant verse has `analysis_note`. (existing)
2. **VCG-level coverage** — every VCG has at least one `vcg_finding` row. CC join: VCGs LEFT JOIN vcg_finding; flag VCGs with no findings.
3. **Verse-level coverage** — every is_relevant verse is cited as anchor_vc_id of at least one `vcg_finding`, OR is a member of a VCG with vcg_findings, OR is explicitly cited in a vcg_finding's phenomenon_text. (Auto-check via CC parser.)
4. **Cluster-level prompt completeness** — every active catalogue prompt has at least one cluster_finding row. (existing §15.2 check 2, narrowed.)

## 9. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Layer 1 produces inconsistent prompt-tagging (one VCG tags T6.1.2; another tags T6.1.1 for similar content) | Brief at Layer 1 includes a checklist of the 189 prompts grouped by tier; AI is asked to tag from the full vocabulary. Some inconsistency is acceptable — the Layer 2 aggregator catches near-duplicates. |
| Layer 2 finds that some prompts have zero VCG tags — completeness gap | Three responses: (a) confirm silence (the cluster genuinely doesn't evidence this prompt — write a `silent` row); (b) flag as gap for researcher review (the cluster should evidence it; needs re-scan); (c) re-open Layer 1 for VCGs that might tag the prompt under closer reading. |
| VCG findings overlap heavily across VCGs (e.g., 12 VCGs all tag T1.1.1) | This is fine and expected — the aggregator distils them. It's exactly the "many VCGs evidence the same thing" pattern that the strict matrix forced into per-cell duplication. Layer 2 consolidates into one cluster row. |
| Researchers / Session C readers lose easy access to per-sub-group findings | Sub-group findings exist where Layer 3 is invoked. Where Layer 3 isn't invoked, sub-group-level analysis is reconstructable by joining VCG findings via vcg_term → mti_term_subgroup. CC can produce a "sub-group findings view" report on demand. |
| Schema migration adds risk to closed clusters | New `vcg_finding` table is additive; doesn't touch `cluster_finding`. Closed clusters' existing cluster_finding rows stay valid. v2_6 audit could flag closed clusters as "no vcg_finding rows" — informational, not corrective. |

## 10. Decisions needed from researcher

| # | Question | Options | Your decision |
|---|---|---|---|
| 1 | Adopt the v2 layered architecture for M04's Phase 9 completion? | YES / NO / ADJUST | _[YES / NO / ADJUST: ...]_ |
| 2 | Storage option — overload cluster_finding (A) or new vcg_finding table (B)? | A / B | _[A / B]_ |
| 3 | For M04 specifically: preserve existing v2_4-era sub-group cluster_finding rows in M04-A through M04-J, OR retire them under the new model? | PRESERVE / RETIRE / REPLACE-SELECTIVELY | _[PRESERVE / RETIRE / REPLACE: ...]_ |
| 4 | Hold v2_6 instruction draft until M04 Phase 9 v2 validates the model? | YES (validate first) / NO (draft now in parallel) | _[YES / NO]_ |
| 5 | Layer 1 batching — one VCG per chat session, or batch 4–6 VCGs per session? | ONE / BATCH-OF-4-6 / OTHER | _[ONE / BATCH / OTHER: ...]_ |
| 6 | Layer 3 sub-group treatment for M04 — flag any sub-groups for full chapter-depth treatment now, or defer until Session C planning? | FLAG-NOW (list) / DEFER | _[FLAG-NOW: ... / DEFER]_ |

## 11. Step 6 path under v2

If you accept v2 (Q1 = YES), Step 6 reshapes as:

**Step 6.1 — Schema migration (if Q2 = B):** CC creates `vcg_finding` + `vcg_finding_prompt_tag` tables. Small migration, additive.

**Step 6.2 — Layer 1 (VCG synthesis):** For each of M04's 48 VCGs, AI runs a Layer-1 session (or 8–12 batched sessions). AI produces phenomena + prompt-tags per VCG.

**Step 6.3 — Layer 2 (cluster aggregation):** AI runs 8 sessions (one per tier T0..T7), reading VCG findings only, producing 189 cluster-scope cluster_finding rows.

**Step 6.4 — Coverage checks:** CC runs the four completeness checks; produces a gap report.

**Step 6.5 — Layer 3 (optional):** If sub-groups flagged in Q6, AI runs per-sub-group sessions.

**Step 6.6 — Stop and review** before Phase 10.

Total: ~16–20 AI sessions, each bounded.

---

*End of v2 proposal. Mark decisions in §10 and ping me.*
