# Phase 5 distribution validation — M08 (v2 resubmission)

**Verdict:** ✅ PASS — Phase 6 may proceed after Phase 5.5 set-aside patch applies
**Generated:** 2026-05-20T18:59:36Z
**v2 source:** `Sessions\Session_Clusters\M08\files phase 5 a\WA-M08-subgroup-mapping-v2-20260520.json`
**v1 resolved (carry-forward source):** `Sessions\Session_Clusters\M08\WA-M08-subgroup-mapping-resolved-v1-20260520.json`
**v2 resolved:** `Sessions\Session_Clusters\M08\WA-M08-subgroup-mapping-resolved-v2-20260520.json`
**Threshold:** any single substantive sub-group ≤ 40.0% of substantive corpus

---

## Sub-group distribution (resolved from v2 mapping against DB)

| Sub-group | Char | Verses | % of substantive | Predicted | Diff | Status |
|---|---|---:|---:|---:|---:|---|
| `M08-A1` | CHAR-1 (Arrogant self-elevation) | 32 | 10.8% | 34 | -2 | ok |
| `M08-A2` | CHAR-1 (Arrogant self-elevation) | 11 | 3.7% | 11 | +0 | ok |
| `M08-A3` | CHAR-1 (Arrogant self-elevation) | 40 | 13.6% | 37 | +3 | ok |
| `M08-A4` | CHAR-1 (Arrogant self-elevation) | 68 | 23.1% | 69 | -1 | ok |
| `M08-B` | CHAR-2 (Presumptuous defiance) | 45 | 15.3% | 45 | +0 | ok |
| `M08-C` | CHAR-3 (Boasting and self-display) | 70 | 23.7% | 70 | +0 | ok |
| `M08-D` | CHAR-4 (Vain conceit) | 12 | 4.1% | 12 | +0 | ok |
| `M08-E` | CHAR-5 (Pride of power and position) | 17 | 5.8% | 17 | +0 | ok |
| `M08-BOUNDARY` |  | 1 | — | 1 | +0 | BOUNDARY |
| **TOTAL substantive** | | **295** | 100.0% | 295 | +0 | |
| **set_aside (Phase 5.5)** | | **174** | — | 174 | +0 | not in §8.6 denom |
| **TOTAL BOUNDARY** | | **1** | — | 1 | +0 | excluded |
| **GRAND TOTAL** | | **470** | | 470 | +0 | |

## §8.6 gate diagnosis

- Biggest substantive sub-group: **M08-C** with **70 verses** (**23.7%** of substantive)
- Next biggest: `M08-A4` (68 verses, 23.1%)

## §8.0 structural observation

✓ All sub-groups represent characteristics:

- M08-A1 / M08-A2 / M08-A3 / M08-A4 = CHAR-1 (Arrogant self-elevation), volume-split by **seat-of-pride** axis per §8.6.
- M08-B = CHAR-2 (Presumptuous defiance).
- M08-C = CHAR-3 (Boasting and self-display) — M22 cross-register flag carried to Phase 7.
- M08-D = CHAR-4 (Vain conceit).
- M08-E = CHAR-5 (Pride of power and position) — M23 cross-register flag carried to Phase 7.
- M08-BOUNDARY = G0193 akratēs (§6.3.1 reason 3).

**Phase 5.5 set-aside:** 174 vc_ids (174 resolved) marked for `set_aside_reason` application:

- M22_REGISTER: 122 vc_ids — `"non-M08 content — M22-register (divine majesty / God-directed exaltation); term STAYS in M08 via other verses (v2_8 §6.3.2)"`
- NO_INNER_BEING: 52 vc_ids — `"non-M08 content — narrative marker / neutral assertiveness; no inner-being state evidenced in this verse as an individual unit of analysis"`

## Carry-forward / set-aside integrity check

| Check | Result |
|---|---|
| Carry-forward vc_ids (B/C/D/E/BOUNDARY) match v1 resolved | ✓ 145/145 |
| set_aside M22_REGISTER vc_ids match v1 M08-F | ✓ 122/122 |
| set_aside NO_INNER_BEING vc_ids match v1 M08-G | ✓ 52/52 |
| M08-A split coverage (151 v1 M08-A vc_ids → A1/A2/A3/A4) | ✓ 151/151 |
| Unmatched/defaulted-to-A4 | 9 |

### Defaulted vc_ids (no term-level rule, fall to M08-A4)

| mti_id | reference | note |
|---:|---|---|
| 165 | Isa 37:23 | no-rule-default-A4 |
| 165 | Isa 26:5 | no-rule-default-A4 |
| 165 | 2Ki 19:22 | no-rule-default-A4 |
| 165 | 2Ki 19:23 | no-rule-default-A4 |
| 165 | Isa 37:24 | no-rule-default-A4 |
| 165 | Psa 56:2 | no-rule-default-A4 |
| 165 | Psa 73:8 | no-rule-default-A4 |
| 165 | Psa 75:5 | no-rule-default-A4 |
| 165 | Psa 10:5 | no-rule-default-A4 |

---

## Phase 6 readiness

§8.6 gate **PASS**. **Phase 6 may proceed** once the Phase 5.5 set-aside patch has applied to the 174 vc_ids. Recommended sequence:

1. CC builds Phase 5.5 set-aside patch from `set_aside_vc_ids` in the resolved v2 JSON.
2. Apply patch (`UPDATE verse_context SET is_relevant=0, set_aside_reason=? WHERE id IN (...)`) under DB transaction.
3. Post-apply check: M08 is_relevant count drops from 470 to 296 (295 substantive + 1 BOUNDARY).
4. CC builds Phase 6 directive from `vc_id_to_subgroup` in the resolved v2 JSON.
5. Phase 6 routes the 296 vc_ids to their respective sub-groups via `verse_context_group` rows.

---

*End of v2 validation report.*