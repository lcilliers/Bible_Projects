# Scaling the verse-read + do we need sub-groups / VCGs in between?

> **Design proposal · v1 · 2026-06-08 · CC.** Batch 1 (`wa-m01-findings-batch1`) proved the typed-relationship
> finding. Two open questions before scaling: (A) do we keep the intermediate structures (VCGs, sub-groups),
> and (B) how do we run the read at scale across ~17,266 characteristic verses. Recommendations + decision
> points for **researcher markup**. No build started.

---

## A. Do we need sub-groups / VCGs *between* verse and finding?

**What batch 1 showed:** the sub-groups (modes of fear) **fell out as a roll-up over the findings** — they
emerged *after* reading, not before. And the old **VCG's job (group verses by contextual sense)** is now done
*inside the finding* — the fear↔reverence shade that a VCG used to separate is resolved at the read and lands
as the finding's **mode/effect**.

**Proposal — collapse the middle layers:**

```
OLD (V3_2):  verse → Phase-A VCG grouping → sub-groups → characteristic → cluster
NEW:         verse → FINDING (typed relationship + mode)  →  [roll-ups computed FROM findings]
                                                              ├─ mode  (= the old VCG sense-group)
                                                              ├─ sub-group / characteristic
                                                              └─ cluster view
```

- **VCG as a *pre-structure*: not needed.** Its function (sense-grouping) is absorbed into the finding's
  `mode`. A "VCG" becomes simply *"all verses whose finding shares a mode"* — a roll-up category, computed,
  not formed up front.
- **Sub-groups / characteristics: keep, but as roll-ups AFTER findings** (emergent), never imposed before —
  the checkpoint test, which batch 1 passed.

**Caveat (honest):** this is one 14-verse batch. It must hold when verses get messier — a 194-verse term, a
dense cross-cluster verse, a set-aside. **Validate on a fuller M01 slice before locking the collapse.**

**Why this is safe to try:** removing the pre-grouping can't lose data — every verse still gets a finding;
the groupings are recomputable from findings at any time. If a pre-grouping turns out to help, it can be
re-introduced as a read-batching aid (below) without changing the record.

## B. How to run the read at scale

The **read is the bottleneck** — assembling and rolling-up are mechanical; turning a verse into a finding is
judgement. Pipeline:

```
1. ASSEMBLE   (CC, mechanical, done)  — _assess_verse_assembly per term/cluster → typed arrays
2. MECHANICAL (CC, mechanical)        — sense-branch via morph · type · clear tier identifications →
                                        candidate per-term findings + complexity signals
3. TRIAGE     (CC judgement)          — evaluate the mechanical OUTCOME's adequacy:
                                        · simple/clean    → ACCEPT (no API)            [most verses]
                                        · clearly inadequate → API read to complete
                                        · CC can't judge  → RESEARCHER decides (accept / API)
4. APPLY      (CC, mechanical)        — validate + write findings to DB  [needs finding schema]
5. ROLL-UP    (CC, derived/read-only) — findings → modes → sub-groups → cluster view
   + DE-DUP across the whole run: a cross-cluster verse is read ONCE (first to reach it); later batches
     skip it — its finding is already there, co-owned.
   + Each verse-read emits per-term findings for ALL in-scope terms, saved to each term's cluster;
     augments + corrects existing cluster findings ([[feedback_characteristic_is_typed_term_in_verse]]).
```

**Triage detail ([[feedback_l2_mechanical_api_triage]]):** the mechanical-vs-API choice is a **judgement on
the adequacy of the mechanical outcome**, not a fixed input rule — default **mechanical-accept**, API the
exception, researcher resolves the uncertain middle. First-draft adequacy signals: unresolved multi-sense ·
within-stem shade ambiguity · relevance/metaphor doubt · interacting multi-term array · morph-type vs
keyword-type conflict · homonym · sibling-span pairing.

**Read-batch unit = the TERM** (what batch 1 used). A term's verses share its meaning, so reading them
together gives consistent findings and lets the term's modes surface. Each read still emits the **complete**
finding for the verse (all its typed partners), so term-batching is just the entry order, not a blinker.

**Who does the READ at scale?** CC-interactive (what I did in batch 1) gives high continuity but **does not
scale** to ~17k verses in sessions. The established division ([[feedback_cc_only_pipeline_verdict]],
[[feedback_chat_vs_api_for_classification]]) is **AI chat reads batches → CC applies**. Recommend: **AI chat
for the read** (CC assembles, AI reads ~30–50-verse batches into findings, CC validates + applies), with CC
spot-reading a sample per cluster for quality.

**Throughput reality:** ~17,266 unique char-verses; M01 = 930. At ~40/batch that's ~23 batches for M01,
~430 for the corpus (cross-cluster de-dup keeps it to *unique* verses). Finite, but real — this is the main
spend of the project, so the per-batch format must be tight before scaling.

## C. Finding schema (needed for APPLY)

Minimal typed-relationship finding row:
`verse · thing_a · type_a · relationship · effect · thing_b · type_b · mode · [cross_cluster?] · provenance`.
A single-faculty verse (no partner) is `thing_b = NULL` (a state/mode finding). Cross-cluster verses get one
row co-owned by both clusters (not two). Relationship-type is an **emergent controlled vocabulary** (batch 1
seeded ~10: lack→eminent, evocation, displacement, production, instrument, response, reverence→devotion,
guilt→dread, imposed-state, memory-of). It grows then stabilises.

## Decision points (please mark up)

- **D1 — Collapse VCG + pre-sub-group into roll-ups?** (recommend **yes**, validate on a fuller M01 slice
  first.) `____`
- **D2 — Read at scale via AI chat batches** (CC assembles + applies + spot-checks)? Or keep CC-interactive
  for now and accept it's slow? `____`
- **D3 — Read-batch unit = TERM?** (vs canonical-order, vs a meaning-group.) `____`
- **D4 — Finding schema fields** as in §C — add/remove? `____`
- **D5 — Build the evolved pipeline now** (assemble → chat-read → apply → roll-up, with the finding schema
  migration), or **validate on a bigger M01 slice first** (e.g. all of one large term like `ya.re`) before
  committing the build? `____`

**My recommendation:** **D5 = validate first.** Do one more, *harder* M01 slice (all of `ya.re`, 194 verses —
the messy, multi-sense, cross-cluster-heavy case) *before* building the pipeline, to confirm the
layer-collapse and the finding format survive the hard case. Then build.
