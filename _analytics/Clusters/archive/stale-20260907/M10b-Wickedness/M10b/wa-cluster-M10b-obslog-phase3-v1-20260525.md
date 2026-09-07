# M10b — Phase 3 obslog — 2026-05-25

**Cluster:** M10b — Wickedness, Evil and Abomination (post-split 2026-05-22)
**Phase:** 3 (Cluster constitution debate)
**Governing instruction:** `wa-sessionb-cluster-instruction-v2_8-20260519` §6

## Inputs read by AI

- Constitution report: `wa-cluster-M10b-constitution-v1-20260525.md` (17 terms, 514 Pass A meanings + keywords)
- Brief: `wa-cluster-M10b-phase3-constitution-brief-v1-20260525.md`
- Cross-register watch flagged: M10 (sin-act), M10c (defilement), M27 (idolatry / cosmic-evil / ruin), M03 (sorrow), M06 (hate/contempt)

## AI output

- File: `WA-M10b-phase3-constitution-verdicts-v1-20260525.md`
- Verdicts: **17 STAYS / 0 TRANSFERS / 0 BOUNDARY**
  - 2 STAYS with no cross-register flag: `G0947 bdeluktos`, `H7562 re.sha`
  - 15 STAYS with cross-register flag

## Cross-register flag distribution

| Destination | Terms flagged |
|---|---|
| **M27** (idolatry / cosmic-evil / concrete-evil-thing) | G0946 bdelugma, G2549 kakia (minor), G4189 ponēria, G4190 ponēros (substantial sub-corpus), H0205G a.ven, H4849 mir.sha.at, H8251 shiq.quts (primary), H8441 to.e.vah |
| **M10** (sin-act / forensic-verdict / legal-offense) | G0093 adikia, G0824 atopos, G2555 kakopoios, G5337 faulos, H7563 ra.sha (~5 forensic verses) |
| **M06** (contempt / hostile speech) | G0987 blasfēmeō |
| **M03** (distress / sorrow suffered) | G2549 kakia (Mat 6:34 only), H0205G a.ven, H7455 ro.a (Neh 2:2, Ecc 7:3) |
| **M10c** (cultic / ritual defilement) | H8251 shiq.quts (secondary), H8441 to.e.vah (primary co-flag) |

Several terms carry **two cross-register destinations** (a.ven: M03+M27 polysemy; shiq.quts: M27+M10c; to.e.vah: M10c+M27). These are real polysemic signals to be handled at Phase 5 sub-group design and Phase 7 VCG differentiation.

## §6.5 post-check

| Check | Result |
|---|---|
| Every term has a verdict | ✓ 17/17 |
| Every STAYS+flag names destination and source-cluster relationship | ✓ 15/15 |
| Every TRANSFERS passes §6.3.2 verse-level relationship test | ✓ N/A (0 transfers) |
| Every BOUNDARY cites §6.3.1 valid reason | ✓ N/A (0 boundaries) |
| No verdict validated against inherited VCGs | ✓ M10b had no inherited VCGs |
| No forbidden grounds (§6.3.1) cited | ✓ |

## Phase 4 status

**SKIPPED per §7.5** — no TRANSFERS and no BOUNDARY verdicts means no Phase 4 directive is authored. The status transition `Data - In Progress` → `Analysis - In Progress` defers to Phase 6 (verse-routing directive) per §7.6.

No DB writes from Phase 4 itself.

## Borderline disposition (1 of 1)

**Ezr 9:11 — H8441 to.e.vah** (Phase 1 borderline, parked):

- Parent verdict: **STAYS** (with M10c+M27 cross-register flags).
- Action: written to `verse_context` as `is_relevant=1` per the parent verdict (vc_id=66005).
- Patch: `wa-cluster-M10b-patch-vcnew-phase3-borderline-disposition-v1-20260525.json` (1 op).
- Follow-on Pass A meaning + keywords: `wa-cluster-M10b-patch-passa-meanings-borderline-v1-20260525.json` (1 op).
  - Meaning: *"The abominations of the surrounding peoples are portrayed as a pervasive moral contamination that has saturated the land entirely, framing wickedness as a spreading inner-communal corruption that defiles a shared space."*
  - Keywords: `moral contamination`, `defilement pervasive`, `corruption spreading`, `impurity communal`, `conscience warning`, `pollution filling`.

The verse's dual-register content (moral abomination + ritual uncleanness language) is itself evidence supporting the M10c cross-register flag at the term level.

## Cluster state post-Phase-3

- Active is_relevant rows: **515** (514 from Phase 2 + 1 from borderline disposition).
- §5.6 hard gate (NULL analysis_note): **0**.
- Cluster status: **`Data - In Progress`** (advances at Phase 6 per §7.6).
- Term universe: **17 / 17** retained (no transfers).

## Initial input to Phase 5 (cross-term observations from AI debate)

For Phase 5 (sub-group formation) consumption:

1. **Abomination family** — to.e.vah, shiq.quts, bdelugma, bdeluktos share the "moral-judgment-of-what-is-detestable-to-God" field across different sub-registers (full-range / idol-object-centred / sacrilegious-event / inner-disconnect).
2. **Wicked-person family** — ra.sha, re.sha, mir.sha.at, kakia, ponēros, ponēria form the largest coherent M10b evidence base. ra.sha alone (179 V) may trigger §8.6 volume-split.
3. **Structural opposite — M26 Righteousness** — wickedness/evil/abomination defined by contrast with the righteous across Job, Psalms, Proverbs, Romans, Sermon on the Mount. T6 (Structural Relationships) finding candidate for Phase 9.
4. **Cosmic-evil sub-corpus in ponēros** — significant enough that Phase 5 may want a separate sub-group for the personal-evil-character vs cosmic-evil-agent registers (M27 cross-register flag travels with the latter).
5. **a.ven polysemy** — VCG-level distinction needed at Phase 7 between the iniquity-as-wicked-character corpus (M10b primary) and the trouble/calamity register (M03/M27 cross-register).
6. **blasfēmeō bridges M10b and M06** — both registers are present and genuine; Phase 5 should name both in the sub-group description.

## Next

Phase 5 — sub-group formation (AI, chat). CC will regenerate a constitution report reflecting the now-stable term set (no change here: 17 terms in, 17 terms out) and produce a Phase 5 brief that consumes the cross-register flags above.
