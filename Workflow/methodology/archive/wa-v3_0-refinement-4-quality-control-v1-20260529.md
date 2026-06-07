# v3_0 refinement — 4. Quality control

**Date:** 2026-05-29
**Status:** Discussion document. No instruction-doc changes yet.
**Reading time:** ~20 minutes
**Index:** [wa-v3_0-refinement-0-index-v1-20260529.md](wa-v3_0-refinement-0-index-v1-20260529.md)

---

## The problem, deeper

M38's v2_5 audit ran after Phase E was complete and the essay was rendered. It surfaced four issues:

1. **1 RESCUE candidate** — Act 27:34 G4991 *soteria*, set aside on the ground "physical survival not spiritual salvation". This is a bias-flag rescue: it conflicts with the inner-being-full-scope memory, which says salvation includes the physical/bodily register.
2. **5 missing anchor flags** — five Greek terms (G2436 *hileōs*, G2433 *hilaskomai*, G4992 *sōtērion*, G1431 *dōrea*, G1434 *dōrēma*) had no `is_anchor=1` on any of their VCG verses. A Phase B.3 hygiene oversight.
3. **177 ungrounded findings** — 177 char-scope E-coded findings whose `finding_text` had no explicit verse / VCG / anchor reference (most are silent-marker cross-references like "see T0.1.2, the corpus is silent on this").
4. **1747 completeness-gap items** — mostly a v2_5/v3_0 schema mismatch (false positive); the v3_0 catalogue doesn't produce sub-group-scope cells the way v2_5 expected.

Of these, items 1 and 2 are real quality issues that should have been caught inside the phase that produced them. Item 3 is partly real (silent-marker findings could be richer) and partly a false positive (silent-markers are intentionally terse). Item 4 is mostly script vs schema drift.

The deeper problem: **the audit's design as a post-pipeline integrity check meant issues got caught only after they had been quoted in prose**. The essay quoted some of these underlying findings; any correction now creates rework on prose that was already rendered.

This is the audit-after-prose problem the memory saved yesterday names. The structural fix is: hygiene checks live inside each phase that produces output; the end-of-D audit then runs a smaller, integration-focused pass; Phase E starts only after that audit clears.

But there's a deeper question hiding in here: **what does "quality" mean at each phase?** The hygiene checks are concrete — "anchor designated", "verse reference in finding_text". But quality isn't just hygiene. M38 also had:

- The bias-flag rescue (Act 27:34) — a *judgment* quality issue, not a hygiene one. A script could have flagged the suspicious set-aside reason; only you can decide whether it's actually a rescue.
- The sub-group truncation issue (M38-E description starting with "ka.phar") — a *generator bug*, not a hygiene one. Surfaced because the input file looked wrong; could have been caught by a validator on the input file.
- The 177 silent-marker findings — a *richness* issue, not a hygiene one. The findings are valid silent-markers; whether they're rich enough to support prose is a different question.

So quality has at least three layers:

1. **Hygiene** — structural correctness. Scripts catch this. Examples: anchor designated, verse reference present, q_code matches catalogue, no schema drift.
2. **Bias** — alignment with stated principles. Scripts can flag candidates; you decide. Examples: set-aside reason not in forbidden grounds, sub-group not a parking lot, vocabulary not narrowly spiritualised.
3. **Richness** — fitness for downstream use. Scripts can measure thinness; only you can decide what's rich enough. Examples: finding has enough verse references to support cited claims, silent-marker has enough rationale to be more than a cross-reference.

The refinements that follow address all three layers, with the heaviest investment in hygiene (cheapest, most automatable) and the structural bias-flagging that makes judgment decisions cheap.

---

## The model

### Three quality layers and where they belong

| Layer | What it catches | When it runs | Who decides |
|---|---|---|---|
| **Hygiene** | Structural correctness | At the end of every phase that produces output | Automatic |
| **Bias** | Alignment with stated principles (researcher-defined) | At the end of relevant phases (mostly A, B.1, B.2) | Surfaces candidates; researcher decides |
| **Richness** | Fitness for downstream use | At the end of Phase D, before Phase E | Surfaces measurements; researcher decides whether to invest in enrichment |

The hygiene layer is where most of the M38 audit findings actually belong. Items 2 (missing anchors) and most of item 3 (ungrounded findings) are hygiene issues that should have been caught at B.3 and D respectively.

The bias layer is where M38's item 1 (RESCUE candidate) belongs. It can't be auto-fixed because it requires judgment. But it can be auto-flagged so the judgment happens at the cheapest moment (during Phase A, not after Phase E).

The richness layer is what's currently missing. M38 had no measure of whether the per-characteristic findings were rich enough to support fluent prose. Hindsight says some were, some weren't — the silent-marker findings in particular were terse enough that the essay struggled to integrate them.

### Per-phase hygiene checks — the table

The full table of hygiene checks I'd propose, with the new checks marked:

| Phase | Hygiene check | Action on failure |
|---|---|---|
| Phase A — UT review | Set-aside reasons match §4.5.1 forbidden grounds | **Surface as bias-flag rescue candidates** |
| Phase A — UT review | All relevant verses classified | Auto-retry for missed verses |
| Phase A — Pass A | Coverage gap (relevant verses without meaning) | Auto-retry for missed verses |
| Phase A — Pass A | Empty meanings | Surface for researcher (could be genuine empty or a generation failure) |
| Phase B.1 — Constitution | All terms have verdicts | Auto-retry |
| Phase B.1 — Constitution | BOUNDARY reasons in valid grounds set | Re-prompt for invalid reasons |
| Phase B.1 — Constitution | Forbidden vocabulary in reasoning | Re-prompt |
| Phase B.2 — Sub-group design | 40% distribution ceiling | Surface as warning |
| Phase B.2 — Sub-group design | BOUNDARY-not-parking-lot | Surface as warning |
| Phase B.2 — Sub-group design | All relevant verses assigned exactly once | Auto-repair coverage gaps |
| Phase B.2 — Sub-group design | All assignments are to known sub-groups | Auto-repair |
| Phase B.3 — VCG design | All VCs have group_id | Auto-repair |
| **Phase B.3 — VCG design** | **Anchor verse designated per term** *(NEW)* | Auto-designate single-verse-term anchors; surface multi-verse anchor-missing |
| Phase B.3 — VCG design | No orphan terms | Auto-repair |
| Phase B.3 — VCG design | All sub-groups have ≥1 VCG | Surface for researcher |
| Phase C apply | Transaction success | Roll-back on partial failure |
| Phase C apply | Status flip verified | Surface for researcher |
| Phase D Stage A | Every characteristic has expected count of findings | Re-run missing |
| Phase D Stage A | All q_codes present and match catalogue | Re-run missing; remap if order-preserved |
| **Phase D Stage A** | **`finding_text` has verse, VCG, or anchor reference for E-coded findings** *(NEW)* | Surface ungrounded findings (don't auto-fix; researcher judges) |
| Phase D Stage A | Outcome codes valid (E/S/G only) | Re-prompt for invalid |
| Phase D Stage B | All cluster-scope rows present (one per catalogue prompt) | Re-run missing |
| **Phase D Stage B** | **`finding_text` has verse, characteristic, or sub-group reference** *(NEW)* | Surface ungrounded findings |
| Phase D Stage B | Outcome codes valid | Re-prompt |
| End of Phase D | **Full audit (v3_0-aware version)** | Verdict gates Phase E |

The two new checks (anchor designation in B.3; verse reference in finding_text in D.A/D.B) directly address M38's audit findings #2 and #3. If these had been in place during M38, items #2 and #3 would have been caught at the producing phase.

### The richness measurement — for Phase E gate

The third layer (richness) needs measurement at the end of Phase D before Phase E starts:

For each characteristic and the cluster-synthesis level, compute:
- Average finding length (words)
- % of findings with ≥2 verse citations
- % of findings with ≥1 explicit cross-characteristic reference
- % of findings that are silent-marker (terse, cross-reference only)

These are diagnostics, not gates. They tell you whether the findings are dense enough to support fluent prose. If, for example, 40% of cluster-synthesis findings are silent-marker cross-references, the chapter authors will struggle to integrate. You can decide to re-run thin findings, or proceed knowing the prose will lean on the richer findings.

### Bias-watch as quality control

The feedback memories already encode several bias-watch disciplines:

- `feedback_inner_being_full_scope` — inner being is not narrowly spiritual
- `feedback_setaside_verses_inform_word_meaning` — set-aside verses still inform meaning
- `feedback_boundary_resolution_required` — BOUNDARY is not parking
- `feedback_phase3_verse_level_relationship_test` — verse-by-verse check for TRANSFERS
- `feedback_phase5_subgroups_represent_characteristics` — sub-groups represent characteristics

These are quality rules. Some can become automated hygiene checks:

| Memory | Becomes hygiene check at | What it checks |
|---|---|---|
| `inner_being_full_scope` | Phase A UT | Set-aside reasons matching "not spiritual" / "merely physical" / "secular" patterns → surface as RESCUE candidates |
| `setaside_verses_inform_word_meaning` | Phase A UT | Set-aside meanings still present in DB (not just deleted); contribute to keyword analytics → surface if missing |
| `boundary_resolution_required` | Phase B.2 | No verses left at BOUNDARY-pending at end of B.2 → blocking |
| `phase3_verse_level_relationship_test` | Phase B.1 | TRANSFERS verdicts have verse-by-verse check evidence → blocking if missing |
| `phase5_subgroups_represent_characteristics` | Phase B.2 | Each sub-group has a characteristic mapping; multiple sub-groups per characteristic only when §8.6 gate triggered → blocking |

Encoding bias-watch into automated checks is the way the discipline scales. The memory says "do X"; the hygiene check enforces X. You stop having to remember; the script remembers for you.

---

## Concrete proposals

### A. Per-phase hygiene scripts — extend existing or new

Existing validators exist for B.1, B.2, B.3 (the M38-era versions). They check structural correctness. The refinement extends them with the new checks and adds new validators for D.A and D.B which currently have only ad-hoc checks.

**Pattern:** each phase's API runner ends with a call to `validate_phase_output(phase, output)`. The validator returns a structured result:

```python
@dataclass
class ValidationResult:
    passed: bool
    blocking_failures: list[Failure]
    warnings: list[Warning]
    bias_flags: list[BiasFlag]  # judgment-gate candidates
    metrics: dict[str, float]   # richness measurements
```

The runner script handles each category:
- `blocking_failures` → propose-validate-repair (Document 3)
- `warnings` → log to obslog; continue
- `bias_flags` → write to URGENT.md; pause as judgment gate
- `metrics` → log to obslog; surface in dashboard

### B. The v3_0-aware audit script

The existing v2_5 audit script produced 1747 false-positive completeness-gap items on M38. A v3_0-aware version would:

1. Read the v3_0 catalogue structure (per-characteristic + cluster-scope, not the v2_5 expectation including sub-group scope).
2. Run the same rule checks (forbidden setaside, boundary parking, evidence grounding, etc.) but calibrated against v3_0 expectations.
3. Skip checks that don't apply to v3_0 (the completeness gap calculation in particular).

**Path:** `scripts/_audit_cluster_against_instruction_v30_v1_{date}.py`

The script's output is structured the same way as v2_5 (markdown report + action plan) but the rules are v3_0-aligned.

This needs building. The v2_5 audit is ~500 lines; the v3_0 version probably similar.

### C. End-of-D audit as Phase E gate

In v3_0 today, Phase E starts when Phase D finishes. Under the refinement, Phase E starts when the end-of-D audit clears.

The flow:
1. Phase D Stage B writes the last cluster_finding row, status flips to `Analysis Complete`.
2. CC runs the v3_0 audit automatically.
3. Audit verdict is one of:
   - **PASS** — no real issues. Phase E proceeds automatically (with Phase E.0 vision document being the first sub-phase).
   - **BOUNDED-FIXES with real issues** — surface to researcher. URGENT.md describes the issues with options. Researcher decides: patch now, defer with note, proceed and patch later.
   - **PHASE-RESTART verdict** — block. Surface to researcher with explicit "this needs Phase X re-run" framing.

The audit becomes a structural input to Phase E even when it passes: each chapter author can see which findings (if any) were flagged for thinness or other issues, and can choose to lean on richer findings instead.

### D. Richness diagnostics in the dashboard

At end of Phase D, the dashboard adds a section:

```markdown
## Finding richness diagnostics

| Scope | n findings | Avg length | ≥2 verse cites | Silent-marker |
|---|---:|---:|---:|---:|
| M36-CHAR-1 | 189 | 215 words | 78% | 12% |
| M36-CHAR-2 | 189 | 198 words | 71% | 18% |
| M36-CHAR-3 | 189 | 235 words | 82% | 9% |
| ... | | | | |
| Cluster synthesis | 189 | 280 words | 88% | 6% |

**Observations:**
- M36-CHAR-2 has 18% silent-markers (highest); chapters drawing from this characteristic may need to lean on the richer findings or accept thinner treatment.
- Average finding length 215+ words across the cluster; this is healthy.
- ≥2 verse cites in 78% of E-coded findings (cluster average); thresholds for good prose support are ~70%+.
```

The researcher can decide at this gate whether to invest in regenerating thin findings or accept the prose impact.

### E. Forbidden vocabulary as a hard check

The shared style document lists forbidden vocabulary for prose. The hygiene check in Phase E should be a hard gate, not a soft suggestion:

For each chapter draft:
- Scan for: "cluster", "sub-group", "VCG", "verse context group", "anchor verse" (use as standalone, not "key verse"), "finding", "tier", "T0"…"T7", "catalogue prompt", "M{NN}-X", "domain"
- If any present in prose (outside of code blocks or quoted scaffolding), surface as a hard block.

The chapter must be revised before final assembly. This catches the kind of vocabulary slip that happens when an author draws from findings written in programme vocabulary.

Implementation: a forbidden-vocabulary scanner runs at the end of each chapter authoring, and on the full assembled book.

### F. The relationship between hygiene checks and feedback memories

When a new feedback memory is written that encodes a methodology rule, it should be evaluated for:

1. **Can it be automated?** If yes, write the hygiene check and remove from memory (or keep memory as historical context).
2. **Does it require judgment?** If yes, keep in memory and surface in the obslog at relevant phases.

The risk of memories accumulating without being folded into the instruction is real (Document 3 covered this). The hygiene-check route is the cleanest folding mechanism — turning a remembered rule into an enforced rule.

For example, `feedback_phase9_tier_by_tier_mandatory` (tier-by-tier execution in Phase D Stage A) is a methodology rule. The hygiene check would verify that each tier's output is written to file before the next tier's call is made. Automating it removes the need to remember.

---

## Open uncertainties

1. **Whether the silent-marker richness threshold (12%? 18%?) actually correlates with prose quality.** No empirical data yet. M36 will start to provide it.

2. **Whether bias-flagging is reliable enough not to spam.** The "set-aside reason matches 'not spiritual'" check will fire on every cluster with set-asides; most won't be real rescues. The question is whether researcher fatigue makes the flag get ignored. Counter-strategy: surface only the strongest matches, not every match.

3. **Whether the v3_0 audit script can be built cleanly.** The v2_5 audit's 1747 false positives suggest the rules need careful re-thinking, not just a renaming. Building it well takes longer than building it poorly.

4. **What "richness" actually measures in practice.** The proposal lists four diagnostics. They might not be the right four. A finding can be terse and still rich (if it's terse because the truth is simple); a finding can be long and thin. Calibrate as M36 runs.

5. **Whether forbidden-vocabulary scanning catches subtle drift.** Direct vocabulary is easy; circumlocutions ("that family of inner-being phenomena we call …") are harder. The scanner catches the easy cases; the consistency pass (Document 2) catches more.

6. **Whether the bias-watch memories should migrate to instruction now or after.** Migrating them risks losing context (the why); keeping them risks drift. Per Document 3, the proposal is "after this batch, review for migration".

---

## Questions for your review

1. **The three quality layers (hygiene / bias / richness) — does this taxonomy match how you think about quality?** Or is it cutting wrong?

2. **The full hygiene-check table** — are the new checks (anchor designation in B.3; verse reference in finding_text in D.A/D.B) the right ones? Are there others to add?

3. **Richness diagnostics** — are the four proposed measurements right? (Avg length, ≥2 verse cites, ≥1 cross-char reference, % silent-marker.) Anything else worth measuring?

4. **The v3_0 audit script** — build now (before M36) or defer (run v2_5 with caveats)? Building before M36 is ~1 day of CC time; running v2_5 leaves M36 with the same false-positive noise.

5. **Bias-flagging UX** — surface every match, or only the strongest? "Strongest" needs a definition. "Every match" risks fatigue.

6. **End-of-D audit as hard gate for Phase E** — adopt as the rule, or keep audit advisory and let researcher decide whether to proceed?

7. **Forbidden vocabulary as a hard chapter-block** — adopt as hard block, or surface as warning?

8. **Feedback-memory migration to hygiene checks** — start now (one or two memories), wait until end of batch, never (treat memories as the live methodology repository)?

---

## What changes in v3_0 instruction if this is adopted

- New §X.10 "Quality layers" — name the three layers and where each applies.
- New §X.11 "Per-phase hygiene checks" — the table above, with the new checks.
- New §X.12 "End-of-D audit gate" — Phase E entry condition.
- New §X.13 "Richness diagnostics" — Phase E entry surface.
- New §X.14 "Forbidden vocabulary scan" — Phase E.4 hard gate.
- Modify each phase section to reference the hygiene checks it owns.

## What CC needs to build

- Per-phase hygiene scripts (extend existing B.1/B.2/B.3 validators; build new D.A and D.B validators).
- The two new checks (anchor designation; finding_text verse reference) — built into B.3 and D.A/D.B validators respectively.
- v3_0-aware audit script — `scripts/_audit_cluster_against_instruction_v30_v1_{date}.py`.
- Richness diagnostics script — runs at end of Phase D; writes to dashboard.
- Forbidden-vocabulary scanner — runs on each chapter draft and on full book.
- Bias-flag detection patterns — set-aside reason patterns, distribution thresholds, parking-lot detection.

Estimated build time:
- Per-phase hygiene script extensions: ~2 hours.
- v3_0-aware audit script: ~6 hours (this is the big one).
- Richness diagnostics + bias-flag detection + forbidden-vocab scanner: ~2 hours combined.

Total: ~10 hours of CC engineering. The v3_0 audit script alone is most of it. If deferred, total drops to ~4 hours and M36 runs with v2_5 audit caveats (acceptable, since the false positives are now known).

---

## Cross-document connection

This document's checks rely on the obslog (Document 1's binding artefact) and on the propose-validate-repair loop (Document 3) for the auto-repair pattern. Adopt this document without Document 3 and the auto-repair flow becomes ad-hoc; adopt it without Document 1 and the failures aren't surfaced in the dashboard.

The deepest interlock is with Document 2 (prose). The richness diagnostics specifically support better prose. The forbidden-vocabulary scan is the final gate on prose. The bias-watch flagging produces the rescue candidates that the chapter authors avoid quoting because they're flagged. Without prose-side refinement (Document 2), this document's quality improvements stop short of where they should land.

---

*Document 4 of 4. The four together describe the full refinement. After your review, decisions land and v3_0 instruction edits begin.*
