# Phase 5 distribution validation — M08

**Verdict:** ⛔ FAIL — Phase 5 must be re-submitted
**Generated:** 2026-05-20T18:33:15Z
**Mapping (resolved):** `Sessions\Session_Clusters\M08\WA-M08-subgroup-mapping-resolved-v1-20260520.json`
**Mapping (AI source):** `Sessions\Session_Clusters\M08\files phase 5\WA-M08-subgroup-mapping-v1-20260520.json`
**Threshold:** any single substantive sub-group ≤ 40.0% of substantive corpus

---

## Sub-group distribution

| Sub-group | Verses | % of substantive | Type | Status |
|---|---:|---:|---|---|
| `M08-A` | 151 | 51.2% | Characteristic | ⛔ EXCEEDS THRESHOLD |
| `M08-F` | 122 | — | Holding (non-characteristic) | ⚠ §8.0 observation |
| `M08-C` | 70 | 23.7% | Characteristic | ok |
| `M08-G` | 52 | — | Holding (non-characteristic) | ⚠ §8.0 observation |
| `M08-B` | 45 | 15.3% | Characteristic | ok |
| `M08-E` | 17 | 5.8% | Characteristic | ok |
| `M08-D` | 12 | 4.1% | Characteristic | ok |
| `M08-BOUNDARY` | 1 | — | BOUNDARY | excluded from gate |
| **TOTAL substantive** | **295** | 100.0% | | |
| **TOTAL holding** | **174** | — | | |
| **TOTAL BOUNDARY** | **1** | — | | |
| **GRAND TOTAL** | **470** | | | |

## §8.6 gate diagnosis

- Biggest substantive sub-group: **M08-A** with **151 verses** (**51.2%** of substantive)
- Next biggest: `M08-C` (70 verses, 23.7%)

## §8.0 structural observation — holding sub-groups

⚠ **Two non-characteristic holding sub-groups are present** in this Phase 5 design:

- `M08-F` (122 verses) — Cross-Register Holding — Divine Majesty and God-Directed Exaltation
- `M08-G` (52 verses) — Marginal / Narrative Holding — Non-Evidenced Pride Verses

Total holding verses: **174** (37.0% of all assignments).

### Rationale (from AI design §5)

M08's polysemic height vocabulary (rum, ga.on, ga.vah, ga.a.vah, ha.lal, ma.rom, etc.) carries genuine dual reference: same lexeme used for human pride AND for divine majesty / God-directed glorying. Phase 1 filtered most divine-majesty uses, but ~120 surfaced as `is_relevant` to M08 because the verse carries M22-register content that requires post-Phase-5 routing. Similarly, archō has 48 temporal-narrative-marker uses that have no inner-being content at all.

Per v2_8 §6.3.2, these terms STAY in M08 because *some* verses evidence M08-relational content. But not every verse of a STAYS term is itself a pride verse. The AI's design routes those non-M08 verses to two holding sub-groups:

- **M08-F** (cross-register holding) — verses with M22-register content, awaiting Phase 8.5 ROUTE-TO-CLUSTER M22 or SET-ASIDE decision.
- **M08-G** (marginal/narrative holding) — verses with no inner-being content (narrative markers, neutral assertiveness), awaiting Phase 8.5 SET-ASIDE decision.

### Compliance question for researcher

v2_8 §8.0 states: *"A sub-group represents a characteristic. Default 1:1; volume-split via §8.6 40% gate is the documented exception."*

Holding sub-groups are a **third pattern** not yet documented in v2_8. They emerge naturally from the M08-specific reality of polysemic vocabulary surviving Phase 1, but they violate the "sub-groups represent characteristics" rule literally read.

**Three resolution options for researcher consideration:**

1. **Accept (default).** Treat M08-F / M08-G as documented holding-pen sub-groups for cross-register content. Phase 8.5 resolves them (ROUTE-TO-CLUSTER M22 or SET-ASIDE). Codify the pattern in v2_9 of the instruction (new §8.4.2 — "Cross-register holding sub-groups for polysemic vocabulary").

2. **Set-aside at Phase 5.** Mark the holding-sub-group verses as `set_aside_reason="non-M08-content (M22-register OR no-inner-being)"` via a Phase 5.5 patch, before Phase 6 routing. Removes the holding sub-groups from the cluster structure. Loses the audit trail of which terms contributed which residuals.

3. **Push back to AI.** Ask AI to re-route these verses into existing substantive sub-groups (e.g. M08-A as "self-elevation including divine majesty by contrast"). Risks distorting characteristic definitions and reduces analytical clarity.

**Recommended (CC):** Option 1 — the holding-sub-group pattern is honest, preserves audit trail, and aligns with v2_8 spirit (Phase 8.5 was already the documented BOUNDARY-resolution mechanism; extending it to polysemic-residual resolution is a natural fit).

## Unmatched split references

✓ All split references match `is_relevant=1` verse_context rows.

---

## Phase 6 readiness

The §8.6 gate fails. Phase 5 must be re-submitted.

---

*End of validation report.*