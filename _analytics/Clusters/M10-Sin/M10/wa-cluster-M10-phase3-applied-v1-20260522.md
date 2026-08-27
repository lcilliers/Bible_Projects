# M10 Phase 3 — Constitution debate — applied record

**Date:** 2026-05-22
**Cluster:** M10 — Sin, Guilt and Transgression (post-split)
**Phase:** 3 (Constitution debate) — applied
**Source verdict file:** `Sessions/Session_Clusters/M10/wa-m10-phase3-constitution-verdicts-v1-20260522.md`
**Apply script:** `scripts/_apply_m10_phase3_verdicts_20260522.py`
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §6

---

## Verdict summary

| Verdict | Count | Notes |
|---|---:|---|
| STAYS (no flag) | 44 | Core sin/guilt/transgression vocabulary |
| STAYS (with cross-register flag) | 13 | Cross-register flags travel to Phase 5/7 |
| BOUNDARY | 6 | Recorded as cluster_observation rows for Phase 8.5 |
| TRANSFERS | 0 | No accidental placements found |
| **Total verdicts** | **63** | All terms evaluated |

(AI's summary table reported 14 STAYS-with-flag and 8 BOUNDARY; cross-counting the row table gives 13 + 6. Counting discrepancy noted but immaterial.)

Cross-register flag distribution:

| Target cluster | Terms carrying flag |
|---|---|
| M03 (Grief) | H2254B cha.val, H5753A a.vah, H6330 pu.qah |
| M06 (Hate/Contempt) | G0988 blasfēmia, G0989 blasfēmos |
| M07 (Shame) | H5040 nav.lut |
| M08 (Pride) | G4942 sunupokrinomai |
| M11 (Repentance/Forgiveness) | H2403H chat.tat (sin-offering), H3725 kip.pu.rim |
| M13 (Truth/Faithfulness) | H0898 ba.gad, H4603 ma.al, H4604 ma.al |
| M14 (Deceit) | G1185 deleazō |
| M23 / M35 (Strength/Testing) | G5356 fthora |
| M26 (Righteousness/Justice) | G0094 adikos, H5766A a.vel, H5766B av.lah, H5767 av.val |
| M31 (Faith/Unbelief) | G0646 apostasia, H0898 ba.gad, H4603 ma.al, H4604 ma.al |

---

## DB actions applied

### Action 1 — Mic 2:10 cha.val Phase 1 borderline resolved

| Action | Detail |
|---|---|
| INSERT verse_context | vc_id=65871; vr_id=232182 (Mic 2:10); mti_id=4648 (H2254B cha.val); `is_relevant=1`; `is_anchor=0` |
| Pass A meaning | "Uncleanness actively destroys the land's fitness as a resting place, making it unlivable — the destructive force is so severe it compels departure, showing sin's power to corrupt …" |
| Patch | `wa-cluster-M10-patch-passa-meanings-v3-mic2-10-20260522.json` (applied) |

Rationale: parent term H2254B cha.val verdict is STAYS; the borderline verse follows the parent into the active corpus.

### Action 2 — Pro 12:21 a.ven Phase 1 borderline parked

| Action | Detail |
|---|---|
| No vc row inserted | Verse remains held outside the DB |
| Reason | Parent term H0205H a.ven verdict is BOUNDARY. Phase 8.5 will dispose of the term and the verse together. |

### Action 3 — Six BOUNDARY terms recorded as cluster_observation rows

For Phase 8.5 to resolve. `observation_type='INTEGRATION_NOTE'`, `source_phase='phase_3_constitution_debate'`, `target_phase='phase_8_5_boundary_resolution'`, `status='open'`.

| Term | Corpus state | Resolution path candidates |
|---|---|---|
| H0205H a.ven (evil: trouble) | 4 relevant + 1 parked borderline | Set-aside, route to M03 / M20, or sense-split |
| H2256D che.vel (destruction) | 1 verse (Mic 2:10 area) | Route to M10c (defilement), or set-aside |
| H2475 cha.loph (destruction) | 0 relevant (all set-aside) | Set-aside; possibly soft-delete term |
| H4889 mash.chit (destruction) | 0 relevant (12 set-aside) | Set-aside; mostly physical-destruction |
| H4892 mash.chet (destruction) | 0 relevant | Set-aside |
| H4893B ma.she.chat (corruption) | 0 relevant | Set-aside |

### Action 4 — No TRANSFERS

Zero terms move out of M10. No `mti_terms.cluster_code` changes.

### Action 5 — chet (H2399) false-gap correction

The AI flagged H2399 chet as missing from §2 of the constitution report. **This was a working-memory error** — chet IS in §2 (lines 965–1008 of `wa-cluster-M10-constitution-v1-20260522.md`), with 33 relevant verses and full Pass A meanings. Verdict inferred as STAYS (primary OT sin-noun vocabulary, all 33 meanings sin-act/state content); the inference is correct, only the AI's claim of an "omission in the report generation" is wrong.

No DB action needed for chet. The corrected verdict is folded into the STAYS-no-flag count above.

---

## M10 post-Phase-3 state

| Metric | Value |
|---|---|
| `cluster.M10.status` | `Data - In Progress` (unchanged by Phase 3) |
| Active OWNER mti_terms | 63 |
| Verse_context rows (active) | 1,478 (was 1,477; +1 from Mic 2:10 insert) |
| `is_relevant=1` | 1,325 (was 1,324; +1) |
| With Pass A meaning | 1,325 / 1,325 ✓ |
| BOUNDARY terms (Phase 8.5 backlog) | 6 |
| Cross-register-flagged terms | 13 (flags travel to Phase 5/7) |
| Phase 3 cluster_observation rows | 6 (BOUNDARY terms) |

---

## Phase 4 / Phase 5 readiness

M10's term constitution is now established:

- 57 STAYS terms with verse corpora → analytical input for sub-group design at Phase 5.
- 6 BOUNDARY terms held for Phase 8.5 (don't contribute verses to sub-group design; their 4 + 1 = 5 active verses are negligible against the 1,325 base).
- 13 cross-register flags feed Phase 5 sub-group-design considerations (e.g. the M26 injustice cluster of 4 terms is a natural sub-group axis; the M11 atonement-response pair groups together).

The Phase 5 sub-group design should respect:

1. **Sin family (Hebrew)** — cha.ta 201v, chat.tat 159v: large enough to need §8.6 distribution-gate handling. Possible axes: sin-as-act vs sin-state vs sinner-as-character.
2. **Guilt family** — a.sham, a.shem, ash.mah, a.von (×3 sub-entries), plus chet: clusters around guilt-recognition characteristic.
3. **Transgression family** — pe.sha 90v, pa.sha 37v, parabasis/paraptōma (NT). Rebellion-against-God dimension.
4. **Faithlessness-as-sin** — ba.gad, ma.al verb/noun: cross-register with M13/M31; possible dedicated sub-group.
5. **Injustice register** — a.vel, av.lah, adikos, av.val, a.vil, adikēma: M26 cross-register; injustice-as-sin sub-group candidate.
6. **Perversion register** — a.vah×2, sa.laph, ho.phekh, la.zut, mut.teh, tah.pu.khah, te.vel: moral-perversion sub-group.
7. **Atonement response** — kip.pu.rim, chat.tat sin-offering: M11 cross-register; small sub-group of remedy-terms.

Ready for Phase 4 (transfers — no-op since zero TRANSFERS) and Phase 5 (sub-group design).

---

*M10 Phase 3 applied 2026-05-22.*
