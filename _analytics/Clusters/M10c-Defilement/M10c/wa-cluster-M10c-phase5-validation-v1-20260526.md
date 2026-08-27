# M10c — Phase 5 validation report — 2026-05-26

**Cluster:** M10c — Defilement and Impurity (8 terms · 263 V)
**Phase:** 5 (sub-group formation)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §8
**Validator:** CC
**AI outputs validated:**

- `Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-design-v1_0-20260526.md`
- `Sessions/Session_Clusters/M10c/wa-cluster-M10c-subgroup-mapping-v1_0-20260526.json`

## §1 Summary verdict

**ACCEPT.** All structural checks PASS. 3 verse-mapping gaps identified and resolved by CC from Pass A meaning content (documented in Phase 6 obslog).

## §2 Structural checks

| Check | Rule | Result |
|---|---|---|
| Sub-group count | 3–6 expected; M10c falls inside | ✓ 5 sub-groups |
| §8.6 distribution gate | each ≤ 40% of substantive verses → ≤ 105 for 263V | ✓ all PASS (max M10c-A=93) |
| Characteristic representation | sub-groups designed to represent characteristics (≥ 1:1 default) | ✓ each sub-group has a coherent inner-being content statement |
| Cross-register inheritance | flags from Phase 3 carried forward | ✓ each sub-group records relevant M12/M10/M11/M27 ties |
| Inner-being framing | sub-group descriptions framed as inner-being condition, not external label | ✓ all five descriptions lead with "inner-being condition…" or equivalent |
| Multi-faceted term handling | terms split across sub-groups when meaning evidence supports it | ✓ 4 of 8 terms multi-faceted (ta.me verb, ta.me adj, akathartos, nid.dah) |

## §3 §8.6 distribution detail

Substantive verse threshold: `0.40 × 263 = 105.2` → cap at 105.

| Sub-group | Verses | % | Gate |
|---|---:|---:|---|
| M10c-A — Bodily-contact | 93 | 35.4% | ✓ PASS |
| M10c-B — Categorical | 40 | 15.2% | ✓ PASS |
| M10c-C — Moral-inner | 26 | 9.9% | ✓ PASS |
| M10c-D — Corporate/covenantal | 83 | 31.6% | ✓ PASS |
| M10c-E — External spiritual agency | 21 | 8.0% | ✓ PASS |

The M10c-A vs M10c-B split (ritual register) is the §8.6-triggered design: had ritual contact + ritual category been combined, the merged sub-group would be 133V = 50.6%, exceeding the gate.

## §4 Mapping validation

### §4.1 Coverage

- AI mapping claims coverage for 263 verses
- Per-verse-range entries enumerate 260 distinct (mti, ref) pairs after live-DB resolution
- **3 gap verses** had no entry in any `verse_ranges`:

| vc_id | mti | Strong's | Reference | Pass A meaning summary | CC routing |
|---:|---:|---|---|---|---|
| 21468 | 5581 | H2930A (ta.me verb) | Num 5:3 | "shall not defile their camp, in the midst whereof I dwell" — camp/sanctuary defilement, divine presence | **M10c-D** (corporate/covenantal) |
| 21583 | 920 | H2931 (ta.me adj) | Hag 2:13 | "one defiled by a corpse touches food → unclean" — bodily-contact contagion teaching | **M10c-A** (bodily-contact) |
| 21706 | 918 | H5079 (nid.dah) | Zec 13:1 | "a fountain opened … for sin and impurity" — corporate cleansing of covenant community | **M10c-D** (corporate/covenantal) |

Rationale: each gap was resolved by reading the Pass A meaning and applying it to the sub-group definitions. No new sub-group required. Gap fixes encoded in `scripts/_apply_m10c_phase6_subgroup_assign_20260526.py` as `GAP_FIXES` dict.

### §4.2 Per-term assignment pattern

4 term-level (single sub-group; whole term population homogeneous in semantic register):
- akatharsia (G0167, 10V) → M10c-C
- miasmos (G3394, 1V) → M10c-C
- molunō (G3435, 3V) → M10c-C
- molusmos (G3436, 1V) → M10c-C

4 per-verse-range (multi-register usage within one term):
- ta.me verb (H2930A, 128V) → A=50, D=63, B=15
- ta.me adj (H2931, 66V) → A=28, B=21, D=11, C=6
- akathartos (G0169, 30V) → E=21, C=5, B=4
- nid.dah (H5079, 24V) → A=15, D=9

This pattern matches the Phase 3 finding: Hebrew defilement vocabulary spans ritual / corporate / metaphorical registers; NT defilement vocabulary concentrates in moral-inner with akathartos uniquely carrying the unclean-spirit register.

## §5 Cross-register flag carry-forward

Phase 3 cross-register flags (all 8 terms had M12 universal flag) are preserved in sub-group descriptions:

| Sub-group | Structural opposite | Other cross-register ties (inherited) |
|---|---|---|
| M10c-A | M12 (purity) | M11 (cleansing as response) |
| M10c-B | M12 (purity / discernment) | — |
| M10c-C | M12 (purity of inner person) | M10 (sin-act), M11 (cleansing), M29 (desire), M08 (pride), M09 (consecration) |
| M10c-D | M12 (purity of sacred space, name, covenant) | M10 (sin), M10b (abomination — idolatry contexts), M07 (shame — Lam) |
| M10c-E | M12 (wholeness post-expulsion) | M27 (evil — unclean spirits as cosmic-evil agents) |

## §6 Decision

Accept Phase 5 outputs. Proceed to Phase 6 apply with the documented 3 gap-fix routings.
