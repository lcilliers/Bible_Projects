# Session B Cluster instruction — Claude API automation feasibility

_Generated: 2026-05-08. Question: can the Claude API perform the
phases of `wa-sessionb-cluster-instruction-v1_1-20260507.md`?_

---

## Short answer

**Yes — most phases map cleanly to API workflows; one or two carry
real automation risk that the instruction itself acknowledges.** The
codebase already has a working precedent: `_exploratory_brief_verse_router_v1_20260504.py`
uses `claude-sonnet-4-6` with structured JSON output to classify verses
one-at-a-time for set-aside decisions. The pattern scales.

The question to settle is not *can* the API do it but *should each
phase be automated, semi-automated, or kept human-driven* — and that
varies by phase.

---

## What "doing the phases" actually means

The instruction defines 10 phases. Across them, the current process is:

1. **Claude AI in chat** reads input reports, produces output documents (review docs, debate docs, mapping docs, findings docs).
2. **Claude Code (this CLI)** consumes those documents and applies them to the SQLite DB via patches/directives.

API automation replaces step 1 (or part of it). Step 2 stays as-is —
the patch/directive applicator is correct and audited.

---

## Per-phase API feasibility

| # | Phase | Automatable? | Confidence | Notes |
|---|---|---|---|---|
| 1 | Comprehension | **Yes — fully** | High | Read the comprehensive report, summarise into obslog. Single LLM call. ~$0.10. |
| 2 | UT verse review | **Yes — already prototyped** | High | One API call per UT verse with structured-JSON output. The brief/thin verse routers already do this for single-term classification. Direct extension. |
| 3 | Characteristic debate | **Yes — single call, but high-stakes** | Medium | Read all glosses + cluster description, propose sub-groups. Output is provisional by design; control-read in Phase 4 catches errors. Worth automating, but treat output as hypothesis. |
| 4 | Control read | **Partial — needs human gate** | Medium | API can do the bidirectional reading and surface OQ-NNN items. The instruction explicitly requires researcher confirmation before the directive is authored. So: API drafts, researcher decides. |
| 5 | 250-word sub-group summaries | **Yes — fully** | High | One call per sub-group with that sub-group's verses as context. Trivial. |
| 6 | Group-verse mapping | **Yes — but with significant risk** | Medium-Low | The instruction's "conglomerate-group split" instruction (§9 last paragraph) — *"can the group's verses be answered uniformly by a single anchor verse, or do different subsets need different anchors?"* — is exactly the kind of nuanced read where LLMs drift. M06's split of group 1601 into 5 was the most consequential analytical act of that session, and it came from reading the verses, not from the labels. Automatable, but the output should be reviewed before Phase 7 application. |
| 7 | Mapping application (directive generation) | **Yes — fully** | High | Pure transformation: structured mapping doc → directive markdown. No analytical judgment. |
| 8 | **Catalogue pass** | **Yes — but THE big risk area** | Medium | 189 prompts × N sub-groups = ~1,300+ LLM calls per cluster. The instruction's *"fluency guard"* (§11) is explicit about the failure mode: *"Output that reads smoothly and is well-structured can still be entirely ungrounded"*. This is the canonical LLM failure mode. Automation is feasible but quality controls are mandatory (see §"Risk controls" below). |
| 9 | Findings recording (directive generation) | **Yes — fully** | High | Pure transformation: parts 1-4 → findings-record directive. The two-step structural+full-text loader is already coded; the API just produces the consolidated findings document. |
| 10 | Verification + gap resolution | **Yes — fully** | High | API consumes the verification report, drafts the verification-response document, drafts gap resolutions. Human reviews before the corrections directive is applied. |

---

## Architecture recommendation

Three layers, mapping to existing project conventions:

```
┌─ Layer 1: Per-phase scripts ─────────────────────────────────────┐
│   scripts/_phase_N_<name>_v1_<date>.py                           │
│   - Loads the phase's input reports                              │
│   - Constructs the prompt (system + user + tools)                │
│   - Calls anthropic.Anthropic().messages.create(...)             │
│   - Validates the response against the phase's expected shape    │
│   - Writes the phase's output document                           │
│   - Halts and reports on validation failure                      │
└──────────────────────────────────────────────────────────────────┘
        ↓ (output document)
┌─ Layer 2: Existing CC apply path ────────────────────────────────┐
│   scripts/apply_session_patch.py                                 │
│   scripts/_apply_<directive_name>.py                             │
│   - These already exist and are audited                          │
│   - No changes required                                          │
└──────────────────────────────────────────────────────────────────┘
```

- Each phase is its own script, just like the existing `_apply_*` scripts.
- Reuse the model + prompt patterns from `_exploratory_brief_verse_router_v1_20260504.py`.
- Use the **Anthropic Python SDK** with `anthropic.Anthropic()` and structured-output (JSON schema) where the phase produces a structured artefact.
- Use **plain markdown output** where the phase produces a document (e.g. Phase 5 summaries).

---

## Cost & model selection

### Per-phase rough costs

Using current pricing (claude-opus-4-7 ~$15/M input + $75/M output;
claude-sonnet-4-6 ~$3/M input + $15/M output):

| Phase | Calls | Approx input/call | Cost (Sonnet 4.6) | Cost (Opus 4.7) |
|---|---|---|---|---|
| 1 Comprehension | 1 | 1 MB report | ~$3 | ~$15 |
| 2 UT review | ~300 verses | ~5 KB each | ~$0.05 (with caching) | ~$0.20 (with caching) |
| 3 Debate | 1 | ~50 KB glosses + descriptions | ~$0.20 | ~$1 |
| 4 Control read | 1 | full comprehensive | ~$3 | ~$15 |
| 5 Summaries | ~7 sub-groups | ~50 KB sub-group context | ~$1 | ~$5 |
| 6 Mapping | ~7 sub-groups × ~200 verses | ~10 KB each | ~$25 | ~$120 |
| 7 Apply (directive gen) | ~7 | small | ~$0.50 | ~$2.50 |
| 8 **Catalogue pass** | **~1,300** | ~50 KB sub-group context + prompt | **~$200 (cached)** | **~$1,000 (cached)** |
| 9 Findings record | 1 | findings doc | ~$2 | ~$10 |
| 10 Verification | ~3-5 | small | ~$0.50 | ~$2.50 |

**Per-cluster end-to-end:** Sonnet ~**$235**, Opus ~**$1,170**.

**Prompt caching is the lever.** Phase 8's 1,300 calls all share the
same large sub-group context (~50 KB) — caching reduces Phase 8 costs
by ~5x. Without caching, costs roughly triple.

### Model recommendation

- **Phase 8 (catalogue pass) — Opus**. Quality of grounded analytical reasoning matters more here than for any other phase. The fluency guard is the central risk; Opus's instruction-following on "name the verse or mark S/G" is meaningfully better than Sonnet's. Worth the cost premium.
- **Phases 1, 2, 5, 7, 9, 10 — Sonnet**. Mostly transformation/summarisation; Sonnet is sufficient and 5x cheaper.
- **Phases 3, 4, 6 — Opus or supervised Sonnet**. Analytical judgment phases. If you're trusting the output, Opus. If a human will review every output, Sonnet is fine.

### 46-cluster total (rough order of magnitude)

- All-Sonnet: ~$235 × 46 = **~$10,800** for the whole programme
- Opus-Phase-8 only, Sonnet rest: ~**$1,200 × 46 = ~$55,000**
- All-Opus: ~$1,170 × 46 = **~$54,000**

These are programme-scale numbers — the comparison is to weeks of analyst time per cluster.

---

## Risk controls — the fluency guard problem

The instruction's §2 Operating Principle and §11 fluency guard are
exactly aimed at the LLM failure mode. The same principles must be
encoded in the automation:

### 1. Verse citation as hard requirement

For every E-coded response, the API must return a structured field:
```json
{
  "code": "E",
  "verse_refs": ["Psa 11:5", "Isa 1:14"],
  "group_refs": ["550-NEW-02"],
  "finding_text": "..."
}
```

The validator script then verifies that each cited verse exists in the
sub-group's verse set. If a citation can't be resolved, the response
is rejected and rewritten as S (silent) automatically — or routed for
human review.

### 2. No-prior-clusters context

The prompt must explicitly forbid drawing on prior cluster findings.
Phase 8 prompts include the cross-cluster contamination guard from §2.

### 3. Two-pass evaluation

For each prompt, run **two independent calls** (different temperatures
or different models). Compare:
- If both produce E with overlapping verse citations → high confidence
- If both produce S → confident silence
- If they disagree → flag for human review

This roughly doubles cost but catches the "fluent but ungrounded" case
that single calls can't self-detect.

### 4. Validation against existing M05 / M06 / M15 baseline

M05 (1,517 findings), M06 (1,516 findings) are already analysed by the
human-in-chat process. Run Phase 8 automation on a subset of M05's
prompts × sub-groups and compare against the recorded findings. If
the API can reproduce the recorded findings to ~80% match, that's a
quality floor. Below that → tune prompts, pick a stronger model, add
review steps.

### 5. The conglomerate-split detection (Phase 6)

The hardest call. The decision to split a group requires reading 100+
verses and judging whether one anchor can cover them all. Two options:

- **Option A** — Have the API produce the mapping with split proposals; require human confirmation before Phase 7 directive is generated.
- **Option B** — Have the API produce ONLY the mapping; force every existing group to remain unsplit; let a separate review pass flag splits. This is more conservative.

Recommend A. Splits are too consequential to rubber-stamp.

---

## What to build first — a 3-week prototype path

### Week 1 — extend the existing verse-router

Build `_phase2_ut_review_v1.py` modelled directly on
`_exploratory_brief_verse_router_v1_20260504.py`. Run on M15's UT
verses (313 of them). Compare output to the existing manually-produced
`WA-M15-UT-verse-review-v1-20260508.md`. If matches well, this is the
cheapest, lowest-risk phase to automate first.

### Week 2 — phase 5 + phase 7 + phase 9 generators

These three are pure transformation: read structured input, produce
structured output. Low risk. Build all three. They become directive-
generators as a side effect.

### Week 3 — phase 8 prototype on one sub-group

Pick M15-A (Wisdom as holistic inner character, 12 terms). Run the
189-prompt catalogue pass on it. Compare against M05-A's existing
M05 catalogue findings (the cross-cluster-contamination warning is
relevant — they're different characteristics, but the analytical
quality should be comparable). This is the riskiest phase; if quality
holds, the rest of automation follows.

After week 3, decide: full programme automation, partial automation
(human-in-loop on the risky phases), or refine and try again.

---

## Where API automation does NOT replace humans

Even with full automation, four things must remain researcher-driven:

1. **Borderline judgments in Phase 2** — the instruction explicitly says these need researcher decision.
2. **OQ-NNN resolutions in Phase 4** — open questions are flagged by the API but resolved by the researcher.
3. **Cluster reassignments** — moving a term between clusters is researcher-confirmed (e.g., the M32 dissolution we just did).
4. **Cluster status flips to `Analysis Completed`** — explicit researcher confirmation required before the status flip (§13 Step 5).

The API automates the analysis; the researcher remains the decision
authority on scope, splits, and closure.

---

## Recommendation

Yes, build this — but stage it. Phase 2 first (proven-pattern
extension, low risk, immediate cost savings on the 30+ remaining
clusters). Phase 5/7/9 next (pure transforms). Phase 8 last with
heavy quality controls because that's where the instruction's
fluency guard matters most.

Phases 3, 4, 6 should remain human-supervised even when automated —
their outputs feed into directives that affect the DB, and the
analytical judgment they require is exactly what LLMs systematically
fail on under the fluency-guard test.

The programme-scale economics are favourable even at full Opus pricing
($55k for ~46 clusters) compared with the human-analyst-time cost of
the same work — and the human can stay in the analytical loop on the
high-stakes phases while automating the rote ones.
