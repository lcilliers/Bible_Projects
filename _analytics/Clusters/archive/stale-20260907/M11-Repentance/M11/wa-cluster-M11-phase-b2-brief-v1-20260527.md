# M11 Phase B.2 — Sub-group design brief

**Cluster:** M11 — Repentance, Forgiveness and Restoration
**Date:** 2026-05-27
**Governing instruction:** [`wa-sessionb-cluster-instruction-v3_0-20260527.md`](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v3_0-20260527.md) §6.2
**Phase A status:** ✅ Complete (288/288 IB verses have Pass A + keywords)
**Phase B.1 status:** ✅ Complete (15/15 STAYS verdicts, 2 with cross-register flag, 1 marginal — researcher accepted under v3_0 multi-characteristic framing)

---

## §1. Required-inputs declaration

| Input | Path | Purpose |
|---|---|---|
| Governing instruction | `Workflow/Instructions/wa-sessionb-cluster-instruction-v3_0-20260527.md` §6.2 | B.2 process, disciplines, output specs |
| Global rules | `Workflow/Instructions/wa-global-general-rules-*.md` [current] | GR-* programme discipline |
| B.1 verdicts | `wa-cluster-M11-phase3-constitution-verdicts-v1-20260526.md` | STAYS verdicts + cross-register flags + Phase 5 design notes |
| Constitution report | `wa-cluster-M11-constitution-v1-20260526.md` | Per-term Pass A meaning corpus (the analytical material) |
| Keyword analytics | `wa-cluster-M11-keyword-analytics-v1-20260526.md` | Structural scaffolding for axis discovery |
| Pass A apply log | `WA-M11-passa-meanings-applied-v1-20260526.md` | Pass A coverage confirmation |
| Out of scope | — | DB writes (B.2 writes none — they fire at Phase C apply) |

---

## §2. Task

Design the cluster's sub-group structure under v3_0 §6.2.

**Decision context (researcher-confirmed 2026-05-27):** M11 stays under v3_0's "sub-groups represent characteristics" framing as a **multi-characteristic cluster**. The Phase 3 analysis identified Release / Atonement / Turning as three distinct mechanisms; under v3_0 these are read as distinct inner-being **characteristics** (1:1 sub-group : characteristic), not as one characteristic with three mechanisms.

**Out-of-scope:**
- VCG design — that is B.3 work, one sub-group at a time, mandatory write-out between sub-groups.
- Term transfers — none required (all 15 STAYS).
- BOUNDARY designation — H5749A ud is STAYS-marginal per B.1; placed in M11-D (Turning) as the structural-opposite per Phase 3 §6.3.2.
- Re-running B.1 — verdicts stand.

---

## §3. Pre-decisions carried in from B.1

1. **All 15 terms STAYS** — no transfers.
2. **2 cross-register flags** retained for B.3 VCG design attention:
   - **G0863G afiēmi (leave)** — 32V, primary register M30/M29 (volitional-detachment) for majority; M11-relational verses include Mat 5:24, Heb 6:1, Rev 2:4, 1Cor 7:11. B.3 will VCG-separate.
   - **G0863I afiēmi (permit)** — 18V, primary register M29 (permission/volition) for majority; M11-relational verses are Mat 27:50 + Joh 18:8 (atonement-register).
3. **G0863I split-handling pre-decision (B.2):** vc=17636 (Joh 18:8) and vc=17641 (Mat 27:50) → M11-A (Atonement); remaining 16 → M11-C (Release, broader sense). Per Phase 3 §6.3.2 these two verses ARE M11-A characteristic content (self-substitution / atoning surrender), not Release.
4. **H5749A ud** (Psa 119:61, structural-opposite of repentance) → M11-D (Turning). Marginal status preserved as a `cluster_observation` for B.3/Phase D awareness.

---

## §4. Output expected

Per v3_0 §6.2.4:

| File | Purpose |
|---|---|
| `WA-M11-subgroup-design-v1-20260527.md` | Sub-group list with code, label, core_description, evidence basis, distribution |
| `WA-M11-subgroup-mapping-v1-20260527.json` | `{vc_id: subgroup_code}` for every is_relevant=1 verse (288 total) |

---

## §5. CC stage gate (B.2 → B.3)

Before B.3 starts, CC validator must PASS:

- Every IB vc_id has a sub-group assignment (288/288).
- Every sub-group has a core_description written from meanings.
- **§6.2.7 distribution gate** — no substantive sub-group holds >40% of cluster's substantive verses.
- **§6.2.6 BOUNDARY-not-a-parking-lot** — N/A for M11 since B.1 produced 0 BOUNDARY verdicts.

Validator: `scripts/_validate_cluster_phase_b2_v3_20260527.py --cluster M11` (new for v3_0).

---

## §6. Status after B.2 complete

Cluster.status stays at `Parked - Methodology Review` until Phase C apply (the un-parking happens at Phase C with the structural write). The B.2 → B.3 gate PASS is the analytical-readiness signal; Phase C reads B.1+B.2+B.3 artefacts and applies in one transaction.

---

*Brief v1 — 2026-05-27. v3_0 first-test execution.*
