# The L1/L2 gap — what it was designed to capture vs what I measured vs the data

> Study of the WA-L1*/WA-L2* + L1/L2 discovery docs (2026-06-14), prompted by: *"there is a BIG gap somewhere — my understanding is that L1/L2 was designed to satisfy a large portion of the verse meaning, and then synergy pulls it together using the L1/L2 results."* Every claim below is cited.
>
> **Bottom line: your understanding is correct and the design backs it. The "gap" is three distinct things, and the loudest one was a framing error in *my* v3 — I measured the wrong yardstick and made L1/L2 look empty.**

---

## 1. What L1/L2 was actually designed to capture (your understanding, confirmed)

The pipeline that ran is a **2-layer model**:
- **L1** = mechanical verse-aware **typing + relevance gate + triage** — settles only the clean single-sense case, defers ambiguity (`wa-p2-l2-decision-design-v1` §1: *"L1 settles only the clean single… L1 does not route, pair, or resolve — it types and defers"*).
- **L2** = the **verse-read = meaning** pass that produces **~14 separately-identifiable tier findings per term-in-verse** (sense · type · compound · mode · location · origin · faculty · attributed-to-God · purpose · typology · response · produces · relational-direction · literary-setting) **plus a collating meaning paragraph** (`wa-verse-read-meaning-plan-v1` §6; `wa-verse-read-pilot-review-M01-v1`). The `finding` rows' `l2_*` provenance literally encodes this.

This **is** a large, structured capture of the verse-grounded meaning. The M01 run produced **1036/1036 verses · 2,750 meaning paragraphs · 61,342 tier findings across 47 clusters** (`wa-verse-read-M01-review-v1`). So L1/L2 did **not** capture "almost nothing" — it captured the verse-meaning floor at scale.

**And the hand-off to synergy is designed exactly as you said:** verse findings **roll up** into cluster findings (`wa-l2-rollup-m01-v1`: *"aggregates the cluster's verse findings per tier into a CLUSTER-level finding"*); the L1 sweep rolls up into a cross-cluster map that *decides the synergy frame* (`wa-v3_2-l1-l2-architecture-synthesis-v1` §6); the verse-read's fan-out **pre-seeds 47 clusters**. "After L1/L2, synergy pulls it together using the L1/L2 results" — confirmed.

**One precision (the only place your phrasing needs a nuance):** the docs scope L2 to *"the lexically-answerable identify-tiers… the rest are cluster roll-ups"* (`wa-l2-finding-schema-design-v1` §8) — ~5–6 catalogue tiers per verse. So L1/L2 captures the **verse-grounded meaning floor** (the 14 fields: *what each term means here, its type/mode/location/faculty/origin/effect/direction*); the **cross-verse, relational, theological meaning** (T0/T4/T5/T6 and the *"what does it reveal/over time"* clauses) is the **synergy layer built on top of** L1/L2. Both are "the meaning of the verses" — split by grain, not a shortfall.

---

## 2. The BIG gap is three things — named

### Gap A — *my v3 measured the wrong yardstick* (the false alarm; mine to own)
My v3 evaluated *"do the VE points satisfy the 189 **catalogue questions**"* and led with *"L1 **mechanical** satisfies ≈ 2."* Both framings are misleading:
- L1/L2 was **never designed to satisfy the catalogue questions directly** — the catalogue is ~60% synthesis (BEYOND) **by design** (`wa-l2-findings-catalogue-coverage-v1`). Measuring L1/L2 against it guarantees a low score that means nothing.
- Leading with **L1-mechanical-only** (~2) hid that **L1+L2 together** capture the 14-field floor (61,342 findings on M01). The ~113 I tagged "NONE/SYNTH" are the **designed synergy layer that consumes L1/L2** — not a failure.
- Net: v3 made a working, at-scale capture look empty. **That was the alarm, and it was my framing, not the system.** The correct yardstick is *"do L1/L2 fill the 14 verse-meaning fields per term-in-verse"* — and they do.

### Gap B — *a real terminology collision* (systemic, unreconciled)
"L1/L2" means **two different things** across the authoritative docs, and **no document reconciles them**:
- **The L1–L8 roll-up ladder** (`wa-cluster-rollup-design.md` §1): **L2 = sub-group formation**; the deep verse read is **L3**; tier findings land at **L5**.
- **The verse-read implementation** (what produced the `l2_*` data): **L2 = the deep verse read** itself.
- So the implementation's "L2" = the ladder's **L3 + L5**. The same doc even contradicts itself (§1 spine: L2 = sub-group formation; §5: *"L2 is the 'second round' that finalises the residue"* = the deep read). This collision is almost certainly **why the picture reads as broken** — the `l2_*` data, the v2 catalogue (VE frame), and the L1–L8 design are three vocabularies for overlapping things, never aligned.

### Gap C — *the data state* (the real, separate implementation gap)
Even though L2 produced 61k+ findings, the DB capture is **partial and mis-wired**, and the run was **stopped**:
- `l2_mechanical` (~146k) carries **`cluster_code` NULL on every row** — the mechanical layer is not linked to any characteristic, so it can't be retrieved per cluster.
- `l2_api` is **partial / fan-out only** — full only where M01/M15 read; most clusters have incidental coverage.
- The run was **stopped 2026-06-11** for the *meaning-duplicates-then-fabricates* defect (a 2026-06-11 memory diagnosis that **post-dates** all these design docs — the docs only encode the *guard* that was later found insufficient: `wa-verse-read-meaning-plan-v1` §6 *"the paragraph is a collation… not a replacement… self-audit checks every tier element is represented"*).
- Stated residue at roll-up: **173 verses lexically unresolved** (`wa-l2-rollup-m01-v1`, T7.1.3); 5% free-text-omission self-audit flag.

---

## 3. So, reconciled

| Layer | grain | what it captures | status |
|---|---|---|---|
| **L1** (mechanical typing/triage) | term-in-verse | relevance, type-vector, sense-narrow, residue flag | built; prototype failed once, reverted; `l2_mechanical` NULL-clustered |
| **L2** (verse-read = meaning) | term-in-verse | the **~14-field verse-meaning floor** + meaning paragraph | ran on M01 (61k findings) + M15; **stopped 06-11** for meaning defect; `l2_api` partial |
| **Synergy** (roll-up L5→L8 / catalogue BEYOND) | VCG→sub-group→cluster→study | cross-verse, relational, dynamic, theological meaning — **built on L1/L2** | designed; **parked** pending the verse-read fix |

**Your model is right.** L1/L2 captures the verse-grounded meaning floor (a large, 14-field structured capture), and synergy is designed to consume it. The three gaps are: **(A)** my v3 mis-measured it against the catalogue and made it look empty — own that and discard that framing; **(B)** a genuine, unreconciled "L1/L2" terminology collision that makes the whole thing read as broken; **(C)** the real data gap — the mechanical layer is NULL-clustered, `l2_api` is partial, and the run was stopped for the meaning-quality defect.

> What v3 *should* have measured, and what a corrected version would: **for each of the 14 verse-meaning fields, did L1/L2 fill it, and is that fill clean / linked / complete in the DB** — not "does it answer a synthesis-level catalogue question." That re-frames "L1 in compliance with the catalogue" as *"L1/L2 fills the verse-meaning floor that the catalogue's identify-tiers read from,"* which is the achievable, designed objective.
