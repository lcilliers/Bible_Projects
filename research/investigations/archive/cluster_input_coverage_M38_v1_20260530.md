# Cluster input coverage audit — M38

**Generated:** 2026-05-30 07:06

**Inputs audited:** 7 chapter input file(s) in `Sessions/Session_Clusters/M38/inputs/`
- `ch1`
- `ch2`
- `ch3`
- `ch4`
- `ch5`
- `ch6`
- `ch7`

---

## DB evidence inventory

| Evidence type | Total in DB |
|---|---|
| `cluster_finding` (active) | 1512 |
| ` - cluster-synthesis` | 189 |
| ` - per-characteristic` | 1323 |
| `cluster_subgroup` (active) | 7 |
| `characteristic` (active) | 7 |
| `verse_context_group` (active) | 45 |
| `verse_context.is_anchor=1` (active) | 45 |
| `cluster_observation` (active) | 17 |
| `mti_term_subgroup` links (active) | 0 |

### Findings by tier

| Tier | Total | Cluster-synth | Per-char |
|---|---|---|---|
| T0 | 96 | 12 | 84 |
| T1 | 192 | 24 | 168 |
| T2 | 248 | 31 | 217 |
| T3 | 264 | 33 | 231 |
| T4 | 192 | 24 | 168 |
| T5 | 168 | 21 | 147 |
| T6 | 192 | 24 | 168 |
| T7 | 160 | 20 | 140 |

### Findings by status

| Status | Count |
|---|---|
| cluster_synthesis | 189 |
| finding | 1160 |
| gap | 53 |
| silent | 110 |

---

## Coverage gaps

**Total missing evidence rows: 25**

### Findings (1512 scope-groups in DB, 8 not referenced)

**Missing by tier:** T5=8

**Missing by status:** cluster_synthesis=1, gap=7

**Missing by scope:** cluster-synth=1, per-char=7

First 30 missing finding scope-groups:

| question_code | tier | status | scope | char | preview |
|---|---|---|---|---|---|
| T5.7.3 | T5 | gap | char#124 | Healing wholeness through faith exercised | **[CHAR-3]** G — As noted in obs_id=367, T2.8 findings for Characteristic 3 are not available in the current evidence se |
| T5.7.3 | T5 | gap | char#127 | Salvation anticipated and hope sustained | **[CHAR-6]** G — T2.8's constitutional deposit finding is not available in this segment (Phase D, T4+T5 tier-pair). The  |
| T5.7.3 | T5 | gap | char#123 | Physical rescue from mortal danger | **[CHAR-2]** G — T2.8 data has not been supplied to this analytical segment. If T2.8 found no constitutional deposit for |
| T5.7.3 | T5 | gap | char#125 | Conscience cleansed through atonement received | **[CHAR-4]** G — T2.8 findings are not available in this segment. This prompt cannot be definitively answered as either  |
| T5.7.3 | T5 | gap | char#122 | Eschatological salvation received by faith | **[CHAR-1]** G — T2.8 findings are not present in this segment's evidence block. The deposit-consequence and generationa |
| T5.7.3 | T5 | gap | char#126 | Priestly mediation machinery of atonement | **[CHAR-5]** G — As noted in obs_id=366, T2.8 findings for Characteristic 5 (M38-E) are not available within this tier-p |
| T5.7.3 | T5 | gap | char#128 | Ransomed identity gratitude and memory | **[CHAR-7]** G — T2.8 findings are not available in this segment. As noted at obs_id=367, the evidence itself supports b |
| T5.7.3 | T5 | cluster_synthesis | synth | — | **[CLUSTER]** G — All seven characteristics record a gap at T5.7.3, none able to confirm or deny a T2.8 null finding bec |

### Sub-groups (non-BOUNDARY: 7, missing: 0)

All non-BOUNDARY sub-groups referenced.

### Characteristics (7 in DB, 0 missing)

All characteristic short_names referenced.

### Verse-context groups (45 in DB, 0 missing)

All VCG codes referenced.

### Anchor verses (45 active anchors in DB, 0 not referenced)

All anchor verse references appear in chapter inputs.

### Cluster observations (17 in DB, 17 not in any chapter input)

**Observations are not currently included by the input generator.** If they should drive prose, the generator needs to route them to a chapter.

- id=260 type=design-note status=open target=D — G1431 dōrea cross-register flag: Primary M38; cross-register relationship with M39 Blessing — grace-as-gift vocabulary (Act 10:45, Rom 5:15, 2Cor 9:15) overlaps
- id=261 type=design-note status=open target=D — G1434 dōrēma cross-register flag: Primary M38; cross-register relationship with M39 Blessing — the single verse (Rom 5:16) is structurally identical to the dōre
- id=262 type=design-note status=open target=D — G2433 hilaskomai cross-register flag: Primary M38; cross-register relationship with M02 Anger — both verses evidence wrath-facing as the structural opposite tha
- id=263 type=design-note status=open target=D — G2434 hilasmos cross-register flag: Primary M38; cross-register relationship with M02 Anger — wrath-averted is the structural opposite present in both verses (1
- id=264 type=design-note status=open target=D — G2435 hilastērios cross-register flag: Primary M38; cross-register relationship with M31 Faith — Rom 3:25 names faith as the inner faculty through which propiti
- id=265 type=design-note status=open target=D — G2436 hileōs cross-register flag: Primary M38; cross-register relationship with M12 Purity/Holiness — Heb 8:12 describes conscience cleared and sins no longer r
- id=266 type=design-note status=open target=D — G4990 sōtēr cross-register flag: Primary M38; cross-register relationship with M18 Hope — multiple verses engage the inner faculty of hope as the primary respon
- id=267 type=design-note status=open target=D — G4991 soteria cross-register flag: Primary M38; cross-register relationship with M18 Hope — eschatological orientation pervades the corpus (Heb 9:28: 'the inner
- id=268 type=design-note status=open target=D — G4992 sōtērion cross-register flag: Primary M38; cross-register relationship with M18 Hope — Luk 2:30 ('hope fulfilled, producing readiness to depart in peace')
- id=269 type=design-note status=open target=D — H3444 ye.shu.ah cross-register flag: Primary M38; cross-register relationship with M18 Hope — the corpus is heavily weighted toward hope-sustained as the inner 
- id=270 type=design-note status=open target=D — H6299 pa.dah cross-register flag: Primary M38; cross-register relationship with M37 Calling — several verses ground ransom in God's covenantal election and iden
- id=271 type=design-note status=open target=D — M38 cluster is multi-characteristic under v3_0: M38 is multi-characteristic — 7 distinct characteristics (eschatological salvation, physical rescue, healing-spi
- id=272 type=design-note status=open target=D — M38-A approaches the 40% distribution gate (39.0%): M38-A (Eschatological salvation received by faith) holds 121/310 = 39.0% of cluster verses, right against th
- id=273 type=design-note status=open target=D — Emergent characteristic — Salvation anticipated and hope sustained (M38-F): M38-F was not part of the working cluster characteristic statement; it emerged from 
- id=274 type=design-note status=open target=D — sōzō sense-split honoured at sub-group level: Researcher direction (BOUNDARY resolution) required sōzō's three discriminable senses to operate distinctly. The B
- ... and 2 more

### Sub-group term inventory (0 term-links in DB, 0 not in chapter inputs)

### VCG context descriptions (45 in DB, 45 not in chapter inputs)

**VCG context descriptions (the meaning-group definitions) are not surfaced in chapter inputs.** These define what each meaning-group is about. AI must rely on inferring from the anchor verses + their analysis_note.
- 45 VCGs have a `context_description` in the DB that is not in the chapter inputs.

---

## Verdict

FAIL — DB evidence is not fully represented in the 7 chapter input files. See gaps above. Either update the generator to include the missing evidence, or update the publishing instruction to explicitly exclude these row types.
