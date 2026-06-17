# VE corpus rollout — staged execution plan (for approval) — v1 — 2026-06-17

**Prefix:** wa · **Document type:** Execution plan (gated) · **Status:** ⛔ PAUSED 2026-06-17 — superseded pending engine compliance. The researcher's questions surfaced that this plan rolls reads over a **non-compliant iteration-1 engine** (reads compensate for stubbed mechanical rules). See [wa-ve-engine-compliance-audit-v1-20260617.md](wa-ve-engine-compliance-audit-v1-20260617.md) §5 for the revised sequencing (Phase 0 = engine alignment first). The cost/step structure below is reusable for the *rescoped* Phase 2 reads.

**Goal (researcher request).** Roll out the M01 lexical work to the whole corpus: (1) rerun the base lexical, then (2) submit the open read items **by type, one at a time, through the API** to enhance the corpus — with a **self-audit + confirmation of completeness after each step** before proceeding to the next.

**Corpus scale.** 40,739 units · 48 clusters · current base = v2 mechanical (ran 2026-06-16). Reads so far = **M01 pilot only**.

---

## A. Two decisions that shape the plan (need your call)

### Decision 1 — does the base rerun fold in the M01 review's generator fixes?
The base generator (`_apply_generate_ve_lexical_v2.py`) is **deterministic** and already ran corpus-wide today. **Rerunning it with no code change reproduces identical output — a no-op.** It only adds value if I first implement the M01 review's mechanical fixes:
- **I1** — de-dup multi-value fields (the `location=['heart','heart','heart']` artefact).
- **I2** — enforce C-5 `divine_involvement=giver → origin=received-from-outside`.
- **I3** — N1 `object` precision (drop determiners/quantifiers "all/the/your/every").

**Recommendation: do Step 0 (implement I1–I3), validate on M01, then rerun base corpus-wide.** Otherwise skip Steps 0–1 entirely and go straight to the read rollout on the existing base.
→ **Your call: (a) implement I1–I3 then rerun base, or (b) skip the base rerun, reads only.**

### Decision 2 — order of the read field-types
The reads are independent enhancements; I propose **ascending size** (de-risk the pipeline on the smallest first, biggest last):
`location (1.5k) → cause (9.8k) → divine-involvement (11.8k) → object-type (14k) → valence (40.7k)`.
Alternative = resolution-order (01b §3: divine → location → … → cause → valence) if you'd rather reads land in dependency order. → **Your call (default = ascending size).**

---

## B. Cost & time estimate (the whole rollout)

Basis: M01 cause pilot = 297 items, 88.9 s, **$0.18** (~$0.0006/item, ~0.3 s/item, batched 200).

| Step | Items | Est. cost | Est. time |
|---|---|---|---|
| 0. Generator fixes I1–I3 (code + M01 validate) | — | ~$0 (CC) | ~30–45 min |
| 1. Base rerun corpus-wide | 40,739 units (no API) | ~$0 (compute) | ~10–20 min |
| 2. location read | 1,532 | ~$1 | ~10 min |
| 3. cause read | 9,813 | ~$6 | ~50 min |
| 4. divine-involvement read | 11,758 | ~$7 | ~60 min |
| 5. object-type read | 14,055 | ~$9 | ~70 min |
| 6. valence read | 40,739 | ~$25 | ~3.5 h |
| **Total** | **~77,900 API items** | **~$45–80** | **~7–9 h** of API runtime (unattended, batched) |

Cost is a real constraint (protocol §6). The single biggest item is **valence (40.7k, ~$25)** because its package submits *every* unit; worth confirming it's wanted at full corpus scope before Step 6.

---

## C. The gated procedure (one step at a time; STOP + confirm after each)

Each step: **dry-run → review → live → self-audit → write audit result to file → report "complete" → WAIT for your go.**

### Step 0 — Generator fixes (if Decision 1 = a)
- Implement I1/I2/I3 in `_apply_generate_ve_lexical_v2.py` (+ the derivation helpers).
- **Audit gate:** rerun M01 only (1,036 units, dry then live); confirm `location` triple-heart gone, `origin` filled on the 2 Deu 11:25 giver rows, no determiners in `object`; M01 review counts re-validate. **Complete = the three fixes verified on M01, no regressions.**

### Step 1 — Base rerun, corpus-wide
- `python scripts/_apply_generate_ve_lexical_v2.py --live` (snapshot auto; circuit-breaker on).
- **Audit gate:** (a) pre-run snapshot exists; (b) all 40,739 units rebuilt, row counts sane vs baseline; (c) **read-preservation verified** — the M01 `*_read_api` rows survived (the generator preserves them); (d) circuit-breaker clean; (e) spot-check 10 verses founded. **Complete = corpus rebuilt, M01 reads intact, audit clean.**

### Steps 2–6 — Read field-types, one at a time
Per field, a **corpus driver** loops the 48 clusters: `build_field_api_package` (or cause pipeline) → `_run_cause_api` → `_apply_field_from_api --field X` (dry-run, then live).
- **Audit gate per field:** (a) **coverage** — submitted = applied + NONE + no-row, no silent drops; (b) **provenance** — every applied row tagged `<field>_read_api` (survives future rebuilds); (c) **founded** — applied values cite the verse; (d) **representative sample** — N=20 read values checked against the verse text (judgement); (e) **distribution sanity** — value spread vs the M01 pilot shape, no degenerate "all NONE" / "all one value"; (f) **reversibility** confirmed (reads are UPDATE/INSERT-with-provenance, revertible). **Complete = coverage reconciles, sample passes, distribution sane.** Audit written to `wa-ve-corpus-rollout-audit-{field}-20260617.md`. Then STOP, report, wait.

Field-specific notes:
- **cause** uses its own pipeline (`build_cause_api_package` / `_run_cause_api` / `_apply_cause_from_api`); the other four use the generalised `build_field_api_package` / `_apply_field_from_api`.
- **valence** (Step 6) inserts a row per unit (where=None) — largest + costliest; final confirmation before launch.

---

## D. Safety, reversibility, governance

- **Snapshot** before the base rerun (generator does it automatically); reads are **reversible** (provenance-tagged UPDATE/INSERT; the apply scripts are documented reversible).
- **Whole-verse reset (P6)** on base rerun preserves `*_read_api` values — confirmed in the generator source (line 94–97). So Step 1 will not erase Steps 0/2–6 reads if re-run later, and the M01 pilot reads survive.
- **Per-step commit** (feedback: commit incrementally) — one commit after each completed+audited step, so the rollout is resumable after any interruption.
- **Out of scope for this rollout (queued separately):** I7 (compound as first-class analytical output), I8 (faculty R2 co-term reading), I9 (response/effect in the analysis template) — these are Step-3 *analysis/enrichment* concerns, not base/read generation.

---

## E. What I need from you to start

1. **Decision 1** — (a) fixes + base rerun, or (b) reads-only on existing base.
2. **Decision 2** — field order (default = ascending size).
3. **Go for Step 0** (or Step 2 if Decision 1 = b). I will execute **only that one step**, audit it, report complete, and wait for your go before the next — as requested.

*No code run, no DB change, no API spend yet. This document is the plan only.*
