# WA-M03-dir-001-term-transfer-applied-v1-20260516

**Phase 4 (v2_2):** Term transfers + status transition
**Apply timestamp:** 2026-05-16T17:51:25Z
**Loader:** [scripts/_apply_m03_phase4_term_transfer_20260516.py](../../../scripts/_apply_m03_phase4_term_transfer_20260516.py)
**Directive id:** `DIR-20260516-015`
**Governing instruction:** wa-sessionb-cluster-instruction-v2_2-20260516 §7
**Source:** Phase 3 debate ([wa-cluster-m03-debate-v1-20260516.md](wa-cluster-m03-debate-v1-20260516.md))

---

## Outcome

**11 terms transferred · 28 BOUNDARY recorded · cluster.status flipped.**

Verdict tally from AI's Phase 3 debate (88 verdicts) + CC default for 1 missing term:

| Verdict | Count |
|---|---:|
| STAYS | 49 (AI) + 1 (CC default for H6869B tsa.rah) = **50** |
| TRANSFERS | 11 |
| BOUNDARY | 28 |
| **Total** | **89** |

## Transfers applied

| mti_id | Strong's | Translit | Gloss | From → To | Rationale |
|---:|---|---|---|---|---|
| 1094 | G0580 | apobolē | deprivation | M03 → **M11 Repentance** | Loss-as-deprivation; repentance-register |
| 4683 | G0929 | basanismos | torment | M03 → **M35 Testing** | Testing/trial register, not inner grief |
| 4685 | G0930 | basanistēs | torturer | M03 → **M27 Evil** | Agent of torture, not inner experience |
| 744 | G1312 | diafthora | decay | M03 → **M25 Life** | Bodily decay/corruption — life-register |
| 705 | G4088 | pikria | bitterness | M03 → **M02 Anger** | Anger-bitterness register |
| 4784 | G4089 | pikros | bitter | M03 → **M28 Envy** | Bitter envy register |
| 1153 | H0928 | be.ha.lah | dismay | M03 → **M01 Fear** | Fear-dismay register |
| 105 | H1670 | de.a.vah | dismay | M03 → **M01 Fear** | Fear-dismay register |
| 7558 | H1795 | dak.kah | crushing | M03 → **M24 Weakness** | Physical-crushing (suffering register) |
| 237 | H7451I | ra.ah | distress: evil | M03 → **M27 Evil** | Evil/calamity sense (homonym) |
| 5162 | H8383 | te.u.nim | toil | M03 → **M36 Service** | Service/labor register |

## CC default for missing verdict

**H6869B tsa.rah** (distress) — AI omitted this term from the debate. CC defaulted to **STAYS** per:
1. v2_2 §6 brief discipline: "STAYS is default for borderline"
2. Phase 1 evidence: 48 of 55 UT verses classified as relevant (87%) — corpus is dominantly distress/affliction (squarely M03 register)
3. Term name aligns with M03 characteristic (anguish/distress)

## 28 BOUNDARY terms (recorded, no DB write)

Per v2_2 §7.4, BOUNDARY designation is recorded in the debate obslog; placement in M03-BOUNDARY sub-group happens at Phase 6. These 28 terms include:

- Greek (5): basanizō ×2 (torture/anguish), basanos (torment), thlibō (press), ponos (travail), skullō (trouble), stenochōreō (press upon), sumpaschō (suffer with)
- Hebrew (21): dav.va (faint), cha.val (be in labour), che.vel-pain, cha.lah (be weak), mu.a.qah (distress), ma.a.tse.vah (torment), ma.tsoq (distress), ma.rar (provoke), ne.dud (tossing), a.mal (trouble), e.tsev (toil), o.tsev (pain), its.tsa.von (toil), pid (disaster), tsoq (distress), tsu.qah (anguish), tsir (pang), qe.pha.dah (anguish), ra.ah-distress:harm, si.ach (complaint)

The 28 BOUNDARY count is significantly higher than M01 (12) or M02 (5) — reflecting M03's vocabulary breadth and the high incidence of mixed-register terms (labor-pain imagery, distress homonyms, vexation register dual-faceted).

## Cluster counts (pre → post)

| Cluster | Pre | Δ | Post |
|---|---:|---:|---:|
| M03 (source) | 89 | −11 | **78** |
| M01 Fear (closed) | 81 | +2 | 83 |
| M02 Anger (closed) | 43 | +1 | 44 |
| M11 Repentance | future | +1 | 1 |
| M24 Weakness | 74 | +1 | 75 |
| M25 Life | future | +1 | 15 |
| M27 Evil | future | +2 | 19 |
| M28 Envy | future | +1 | 39 |
| M35 Testing | future | +1 | 25 |
| M36 Service | future | +1 | 19 |

Note: M01 and M02 are already in `Analysis Completed` status. These 3 incoming terms (be.ha.lah + de.a.vah → M01; pikria → M02) will need to be marked as "Analysis Completed (Terms Added)" status — see follow-up below.

## Status transitions

- `cluster.status M03`: `Data - In Progress` → **`Analysis - In Progress`** (Op N inline per v2_2 §7.6)
- M01 and M02 cluster statuses NOT automatically updated to "Analysis Completed (Terms Added)". This follows-up — researcher may flag for re-opening if needed.

## Health checks (all PASS)

| Check | Expected | Actual |
|---|---|---|
| Source M03 active terms post-transfer | 78 | 78 ✓ |
| Transferred terms by destination | M01=2, M02=1, M11=1, M24=1, M25=1, M27=2, M28=1, M35=1, M36=1 | matches ✓ |
| cluster.status M03 | `Analysis - In Progress` | `Analysis - In Progress` ✓ |

## Provenance

- Phase 3 debate: [wa-cluster-m03-debate-v1-20260516.md](wa-cluster-m03-debate-v1-20260516.md)
- Apply script: [scripts/_apply_m03_phase4_term_transfer_20260516.py](../../../scripts/_apply_m03_phase4_term_transfer_20260516.py)
- Pre-apply backup: `backups/bible_research_backup_*_DIR-20260516-015.db`

---

## Next step — Phase 5 (AI sub-group design)

CC regenerates the constitution report (v2, post-Phase-4) showing the 78-term stable cluster, then writes the Phase 5 brief.

*End of applied report.*
