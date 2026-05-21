# M07 Phase 5 — Sub-group formation — brief

**Date:** 2026-05-19
**Cluster:** M07 — Shame, Disgrace and Humiliation
**Phase:** 5 (Sub-group formation from clustering meanings)
**Audience:** Claude AI session (chat)
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §8

**Read this brief first.** The structural inputs are the updated constitution report + Phase 3 verdict document referenced below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M07/WA-M07-phase5-subgroup-brief-v1-20260519.md` | Primary task instructions |
| 2 | **Constitution report (v2, post-Phase-4)** — `Sessions/Session_Clusters/M07/wa-cluster-M07-constitution-v2-20260519.md` | §1 cluster characteristic statement + §2 per-term meaning corpora (34 terms — Phase 4 moved H2616B, H2617B to M05) |
| 3 | **Phase 3 verdict document** — `Sessions/Session_Clusters/M07/WA-M07-constitution-debate-v2-20260519.md` | The **cross-register flags** (8 STAYS-with-flag terms) are critical input to characteristic identification |
| 4 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §8 (Phase 5 disciplines; §8.0 characteristic-as-objective; §8.6 distribution hard gate) |
| 5 | **Science extract** — `Workflow/Sciences/wa-m07-shame-scienceextract-v1_0-20260513.md` | Programme-curated scientific framing of shame (helpful for characteristic identification) |
| 6 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-{current}.md` Ch.1 'Defining Inner Being' | Inner-being scope definition |
| 7 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

---

## Context

M07's term universe is now stable: **34 terms** remain after Phase 4 (`H2616B cha.sad` and `H2617B che.sed` transferred to M05 — accidental placement; the chesed root family carries the steadfast-love sense, not shame). Phase 3 v2 left **8 cross-register flags** on STAYS verdicts — these are direct input to Phase 5 characteristic identification.

527 Pass A meanings (Phase 2) are the **only analytical material** for sub-group design. Inherited VCGs, prior sub-group structure, anchors, and prior findings are explicitly suppressed (per v2_8 §2.3) so sub-groups emerge from the evidence-meanings, not from prior structure.

---

## THE PRIMARY OBJECTIVE — sub-groups represent characteristics (§8.0)

**This is the structural objective.** Read it carefully — it shapes every step that follows.

1. **A sub-group represents a characteristic** — a single inner-being faculty/state. The default is **1 sub-group : 1 characteristic**.
2. **Volume-split is the documented exception.** When a single characteristic's verse corpus would exceed the §8.6 distribution gate (40% of substantive verses), split it into multiple sub-groups by a documented split-axis. The characteristic identity persists across the splits.
3. **A sub-group serving two characteristics (SPLIT_SUBGROUP) is rare** — it arises when the same lexical sub-group contains different VCG registers serving different characteristics (M04-E precedent: *sa.s.von* → Joy register, *agalliao* → Suffering-Joy register, same sub-group). Flag any such case at Phase 5; Phase 7 separates the registers; Phase 8.7 records the observation.
4. **Cross-register flags from Phase 3 inform characteristic identification.** A term carrying a cross-register flag may suggest a characteristic that the cluster's primary register doesn't fully cover — design a sub-group around the relational dynamic the flag names.

**Why this discipline (rationale from M04 retrofit, 2026-05-18):** M04 v1 clustered sub-groups by raw meaning similarity without the characteristic frame. At Phase 8.7 we had to retrofit a 7-characteristic map across 17 sub-group links via a 4-version researcher debate. Some characteristics (Joy, Delight) spanned 4–5 sub-groups each — discoveries made downstream that should have been design inputs upstream. **M07 starts fresh under this discipline — design sub-groups to represent characteristics from the start.**

---

## Process

### Step 1 — Identify the characteristics

Read across the meaning corpora (§2 of the constitution report) and name the distinct **inner-being faculties / states** M07's evidence expresses. Aim for an analytically clean list — **typically 3 to 8 characteristics** for a cluster this size.

A characteristic is a single answer to: *"what specific inner-being faculty or state does this body of verses evidence?"* Examples from the M04 precedent: Joy, Gladness, Delight, Wonder. For M07, candidate characteristics might include (this is suggestive, not prescriptive — derive your list from the meanings):

- The painful inner state of exposure / inadequacy (the core *bosh / aischunē* shame)
- Public humiliation / abasement of pride (the *ka.lam / sha.phel* register — note `sha.phel` is BOUNDARY)
- Disgrace / dishonour as social-relational diminishment (the *qa.lon / atimia* register)
- Contempt-producing-shame (the M06-flagged `exoutheneō` dynamic the cross-register flag identifies)
- Speech-acts of reviling / silencing (the M42-flagged `loidoria / fimoō / kakologeō` dynamic)
- Indecency / shamefulness as moral judgment (the *aischros / aschēmosunē* register)
- Innocence as structural counter (the M12-flagged `niq.qa.von / qe.ha.von` dynamic — these STAY because verses show innocence as shield against shame)

Refine, combine, or split these from the actual meaning evidence. The cross-register flags are reminders that these dynamics belong in M07 with the flag noting the other-register dimension.

### Step 2 — Map each characteristic to its evidence

For each characteristic, note which **terms' verses primarily evidence it**. Some terms will be primary carriers; others will be secondary (their corpus splits across characteristics, or they're flagged cross-register).

### Step 3 — Design sub-groups to carry the characteristics

- **Default**: one sub-group per characteristic. Use natural codes (`M07-A`, `M07-B`, ...).
- **Volume-split**: if a characteristic's verse evidence would exceed 40% of M07's substantive corpus (the §8.6 gate), split that characteristic into multiple sub-groups by a named split-axis. Common axes: OT vs NT-distinctive, present vs eschatological, vertical (toward God) vs horizontal (interpersonal), individual vs communal, righteous vs corrupt, presence vs absence-as-curse.
- Each sub-group's `core_description` explicitly names: (a) the characteristic it represents, (b) the split-axis if it's part of a volume-split, (c) the inner-being content from the meanings.

### Step 4 — Assign every verse to exactly one sub-group

For each of the 527 Pass A meanings (across the 34 terms), record the sub-group assignment. Mapping form: `{vc_id: subgroup_code}`. Output as JSON for CC's Phase 6 apply.

### Step 5 — BOUNDARY sub-group

5 BOUNDARY terms remain in M07 from Phase 3 (G2699 katatomē, H4893A mish.chat, H5206 ni.dah, H8213 sha.phel, H8400 te.val.lul). Their verses route to a `M07-BOUNDARY` sub-group with a brief description naming the analytical questions. **BOUNDARY carries only verses of BOUNDARY-verdict terms** (§8.4.1) — never residual verses of STAYS-verdict terms.

### Step 6 — Flag SPLIT_SUBGROUP cases

If any sub-group on closer inspection contains VCG-level registers serving different characteristics (rare), flag it in the output with the analytical question. Phase 7 (VCG design) will separate the registers; Phase 8.7 will record the SPLIT_SUBGROUP observation.

### Step 7 — Multi-faceted terms

Some terms' verses span multiple sub-groups. Record primary + secondary assignments per term in the mapping. This is normal; not an error.

---

## Outputs

1. **Sub-group design document** — `Sessions/Session_Clusters/M07/WA-M07-subgroup-design-v1-20260519.md`. Structure:
   - §1 Characteristics identified (named, defined, evidence-rooted)
   - §2 Sub-group design — one section per sub-group with `subgroup_code`, `label`, `core_description` naming the characteristic + split-axis if applicable
   - §3 Multi-faceted terms (primary + secondary sub-group records)
   - §4 SPLIT_SUBGROUP flags if any
   - §5 Verse-to-sub-group mapping table
2. **Mapping JSON** — `Sessions/Session_Clusters/M07/WA-M07-subgroup-mapping-v1-20260519.json` — `{vc_id: subgroup_code}` for every is_relevant verse. CC uses this for the Phase 6 mechanical apply.

---

## Discipline

1. **Read every verse-meaning** before designing sub-groups. No shortcuts from gloss or transliteration.
2. **Characteristic-first design** (§8.0). Don't cluster by meaning-similarity until you've named the characteristics the cluster expresses.
3. **The 40% distribution gate is a volume-split trigger, not a fail signal.** If a characteristic carries >40% of the corpus, split it into multiple sub-groups with a named axis — don't fragment characteristics that should remain single. CC validates the gate post-design.
4. **Cross-register flags travel forward.** When a flagged term lands in a sub-group, the flag is preserved in the rationale for Phase 7/9 consumption.
5. **No BOUNDARY parking** (§8.4.1). Residual verses of STAYS-verdict terms (e.g. "horizontal shame", "non-divine disgrace") go to substantive sub-groups, not BOUNDARY.

---

## After you finish

1. Save the sub-group design document + mapping JSON to the paths above.
2. Ping CC: "M07 Phase 5 sub-group design ready".
3. CC runs `scripts/_validate_cluster_phase5_distribution_v1_20260517.py --cluster M07`. PASS → Phase 6 directive. FAIL (>40% gate) → re-submission with finer-grained volume-split.

---

*End of brief. Load the constitution report (#2), the Phase 3 verdict document (#3 — pay attention to cross-register flags), and §8 of the v2_8 instruction. Begin with characteristic identification.*
