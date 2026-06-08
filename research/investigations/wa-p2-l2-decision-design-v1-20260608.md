# P2 / L2 decision design — scenario taxonomy + STEP-sufficiency (M01 evidence)

> **Investigation · v1 · 2026-06-08 · CC.** Answers the researcher's design questions (2026-06-08): the
> qualifier "pull-through" belongs in **L2**; does the L2 STEP meaning suffice for the multi-dimensional
> decisions; and should L2 split into *qualifier+term · multi-term-same-cluster · multi-cluster* (and are
> those the only scenarios)? Evidence: `scripts/_assess_p2_verse_scenarios.py` typing every M01 verse.
> Companion data: [wa-p2-l2-scenario-typing-M01-v1-20260608.md](wa-p2-l2-scenario-typing-M01-v1-20260608.md).
> **Read-only — no design committed yet; for researcher markup.**

---

## 1. The L1 / L2 boundary (confirmed)

- **L1 — verse-aware establishment + TYPING.** Per in-scope occurrence: apply the STEP sense, run the
  **relevance-in-context** gate (set aside the Song-6 class), flag **single vs multi sense** (residue), and
  assign the verse a **type-vector** (how many in-cluster chars / other-cluster chars / qualifiers it holds).
  L1 settles only the **clean single** case mechanically. **L1 does *not* route, pair, or resolve** — it
  *types* and defers.
- **L2 — the decision modules** (the "pull-through"): runs on the typed verses; reads to decide; writes the
  routes/pairs/findings.

This reconciles "L1 must be verse-aware" (it re-evaluates relevance and reads the verse's term array to type
it) with "the pull-through is L2" (the routing/judgement is L2). L1's old sin was *applying meaning uniformly*
— that is exactly what moves to typing-only.

## 2. Decision-scenario taxonomy

A verse = a reference + its array of in-scope occurrences. Relative to the cluster under analysis:

| | Scenario | Trigger | Decision / action |
|---|---|---|---|
| **S0** | set-aside / relevance | occurrence not the characteristic in context (metaphor, wrong pole) | set aside; record reason (still informs word meaning) |
| **S1** | clean single | 1 in-cluster char · single sense · no other · no qualifier | **none — pure L1 mechanical** |
| **S2** | sense-resolution | in-cluster char has >1 STEP top-level sense | choose the sense the verse activates |
| **S3** | same-cluster multi | ≥2 in-cluster chars in the verse | **pair** (sibling span) vs **distinct** co-present |
| **S4** | qualifier + char | a T2 qualifier co-present with an in-cluster char | route the **qualifier occurrence** into this cluster; record the modified meaning |
| **S5** | cross-cluster | an other-cluster char co-present with an in-cluster char | reciprocal finding in each; multi-belong; combined meaning |
| **S6** | qualifier-orphan | qualifier with **no** char in the verse | no route (eventual noise) — not reachable from a cluster's own ref-set |

**The researcher's three are S4 · S3 · S5.** The evidence adds **two more decisions** they did not name:
**S2 sense-resolution** (pervasive) and **S0 relevance/set-aside** (the Song-6 gate). S6 is bookkeeping.

## 3. M01 evidence — the distribution (930 verses, 1044 in-cluster occurrences)

| Scenario | Verses | % |
|---|---|---|
| S1 clean single (**pure L1**) | 39 | **4%** |
| S0 set-aside / relevance | 79 | 8% |
| S2 sense-resolution | 781 | 84% |
| S3 same-cluster multi | 96 | 10% |
| S4 qualifier + char | 414 | 45% |
| S5 cross-cluster | 597 | 64% |
| **COMPOUND (>1 decision in one verse)** | **688** | **74%** |

### Three findings that decide the architecture

1. **Pure-mechanical L1 settles ~4% of verses.** The "apply STEP meaning mechanically" idea is real but
   *rare*. 96% of M01 verses need an L2 judgement. **L1's value is the *typing + relevance gate*, not the
   meaning-stamp.** This is why the first L1 build failed: it stamped meaning on the 96%.

2. **The decisions compose — 74% of verses trigger more than one.** e.g. `1Cor 2:3` (*fobos+tromos*, a
   qualifier, and M24 present) is S3 **and** S4 **and** S5 at once; `1Sa 14:15` is a 3-term same-cluster
   array with M27 alongside. **So the three processes cannot be three disjoint passes over separate verse
   sets** — a single verse routinely needs qualifier-routing *and* cross-cluster *and* sense-resolution
   together. The right shape is **type → apply each applicable module → synthesise the verse's combined
   contribution.** The researcher's instinct (the *logic* differs per scenario) is correct; the modules are
   co-resident in a verse, not partitioned across verses.

3. **STEP-signal sufficiency is asymmetric** (the direct answer to "will L2 STEP meaning suffice"):

   | Decision | STEP signal | Present on M01 | Verdict |
   |---|---|---|---|
   | S3 pairing / S4 qualifier-attach | `span_strong_match` | **100%** | **STEP-decidable now** — sibling spans and qualifier attachment are carried in the span match |
   | S2 sense-resolution | `morph_code` / `stem` | **0%** | **Not yet** — M55 added the columns but **no STEP morph backfill has run**; until it does, sense-resolution needs a read |
   | S5 cross-cluster relation | (none) | — | STEP gives each term's sense but **not the relation between them** → **needs a read** |

## 4. Recommended L2 architecture (for markup)

```
L1  (per verse): establish STEP sense · relevance gate (S0) · single/multi flag · TYPE-VECTOR
                 └─ emits clean S1 (4%) done; everything else typed for L2

L2  (per typed verse): run the applicable MODULES, then synthesise
      ├─ M-sense  (S2)  resolve the active sense        [needs morph backfill, else read]
      ├─ M-pair   (S3)  sibling-span pair vs distinct    [span match present]
      ├─ M-qual   (S4)  route qualifier occurrence in     [span match present]
      ├─ M-cross  (S5)  reciprocal / multi-belong          [needs read]
      └─ SYNTHESISE: one combined verse contribution + the spawned routes/findings
```

- **Not three passes — three modules + a synthesiser**, gated by the type-vector. A verse with type-vector
  `(in=2, other=1, qual=1, multisense=Y)` runs M-sense + M-pair + M-qual + M-cross then synthesises.
- The user's "split L2 into three" is honoured at the **module** level (distinct logic, distinct writes);
  the **74% compound** rate is why they must share one verse-pass and a synthesis step.

## 5. Prerequisite surfaced: the STEP morph backfill

`morph_code` / `stem` are **0% populated** — the M55 columns exist but the per-verse STEP morphology has not
been pulled. **Sense-resolution (S2, 84% of verses) cannot be STEP-automated until this backfill runs.**
This is the single highest-leverage data task before L2: with morph present, the dominant decision (which
sense of *ya.re* / *pachad*) becomes mechanical; without it, 84% of verses carry a manual sense pick.
Recommend a **STEP morph backfill** as the next prototype (read STEP per verse → populate
`wa_verse_records.morph_code` / `stem`), validated on M01 before any L2 build.

## 6. Open decisions for the researcher

1. **Architecture:** accept "type → modules → synthesise" (not three disjoint passes)? §4.
2. **Scenario set:** accept S0 + S2 as decisions alongside the named S3/S4/S5? Any scenario still missing?
3. **Morph backfill first?** Make the STEP morph pull the next prototype, so S2 (84%) is STEP-backed before
   L2 is built? §5.
4. **Qualifier-attach test:** is `span_strong_match` equality the right mechanical signal for "the qualifier
   enhances *this* char" (S4), or must M-qual always read the verse? (Prototype can measure how often the
   qualifier shares the char's span.)

---

*State: T2 cleanup items 1–2 applied (480 active; 106 never-co-occur soft-deleted, reversible). V3_2
execution still parked. No L2 build started — this design + the morph-backfill question go to the researcher
first.*
