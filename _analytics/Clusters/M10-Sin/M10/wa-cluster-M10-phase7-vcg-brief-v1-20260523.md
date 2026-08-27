# M10 Phase 7 — VCG design within sub-groups — brief

**Date:** 2026-05-23
**Cluster:** M10 — Sin, Guilt and Transgression (post-split)
**Phase:** 7 (VCG design within sub-groups)
**Audience:** Claude AI session (chat)
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10

**Read this brief first.** The structural input is the per-sub-group meanings report below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M10/wa-cluster-M10-phase7-vcg-brief-v1-20260523.md` | Primary task instructions |
| 2 | **Per-sub-group meanings report** — `Sessions/Session_Clusters/M10/wa-cluster-M10-subgroup-meanings-v1-20260523.md` | Per sub-group, every is_relevant verse with its term + Phase 2 meaning, in canonical Bible order. **The only analytical material for VCG design** (inherited VCGs / anchors / findings explicitly suppressed per §2.3) |
| 3 | **Phase 5 sub-group design** — `Sessions/Session_Clusters/M10/files phase 5/wa-cluster-M10-subgroup-design-v1-20260523.md` | Sub-group definitions (characteristic-representations), cross-register flags, multi-faceted-term split rules |
| 4 | **Phase 6 directive** — `Sessions/Session_Clusters/M10/wa-cluster-M10-dir-002-phase6-subgroup-assign-v1-20260523.md` | Confirms final per-sub-group volumes after CC patches (chet, pa.sha) |
| 5 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10 (Phase 7 disciplines; **§10.7 staged write-out**; **§10.8 no-sampling pre-submission checklist**) |
| 6 | **Science extract** — `Workflow/Sciences/wa-m10-guilt-scienceextract-v1_0-20260513.md` | Programme-curated scientific framing — **Sections 1–2 only** (Guilt + Transgression). Section 3 (evil/wickedness) belongs to M10b; later sections on defilement belong to M10c. |
| 7 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-{current}.md` Ch.1 'Defining Inner Being' | Inner-being scope definition |
| 8 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

---

## Context

M10's sub-group structure landed at Phase 6 (applied 2026-05-23): **10 sub-groups, 1,325 is_relevant verses**, distributed cleanly (largest M10-B at 25.6%, well under 40% gate). Each sub-group represents a characteristic per v2_8 §8.0; no volume-splits were needed (the largest characteristic, sin-as-condition, sat comfortably within the gate).

| Sub-group | Characteristic | Terms | Verses | Cross-register flag |
|---|---|---:|---:|---|
| M10-A | Sin as committed act | 8 | 274 | M06 · M08 · M14 (term-level on slander, hypocrisy, deceit) |
| M10-B | Sin as moral condition / state | 12 | 339 | M11 (atonement-response on kip.pu.rim, chat.tat sin-offering) |
| M10-C | The sinner as moral character | 2 | 64 | — |
| M10-D | Guilt as inner-being state | 6 | 97 | M03 (on pu.qah) |
| M10-E | Iniquity as accumulated moral crime | 1 | 162 | — |
| M10-F | Transgression / rebellion | 7 | 147 | — |
| M10-G | Faithlessness / treachery | 3 | 101 | **M13 + M31** (covenant-breaking; all 3 terms) |
| M10-H | Perversion / corruption | 14 | 64 | M03 · M07 · M23/M35 (on cha.val/a.vah/nav.lut/fthora) |
| M10-I | Injustice | 6 | 72 | **M26** (Righteousness/Justice; 4 of 6 terms) |
| M10-BND | Boundary — analytically undecided | 6 | 5 | — |
| **Total** | | **65** | **1,325** | |

(Total terms = 65 because pa.sha and paraptōma carry both primary + secondary mti_term_subgroup links.)

Phase 7's task is to design **VCGs (verse_context_groups)** within each sub-group — finer-grained units that cluster verses with substantively similar inner-being content inside the sub-group's register.

### Scale note (vs M09)

M10 has roughly **12× M09's verse volume** (1,325 vs 109) across the same general workflow. Expect 80–120 VCGs total across 10 sub-groups. The four largest sub-groups (M10-B 339V, M10-A 274V, M10-E 162V, M10-F 147V) will each carry 10–20 VCGs; the smaller ones will carry 2–8. Pace accordingly.

### Important: M10-BND special VCG (mandatory)

The 5 verses in M10-BND (4 from H0205H a.ven + 1 from H2256D che.vel) MUST go into a **single dedicated VCG** for Phase 8.5 resolution. The 4 empty-corpus BOUNDARY terms (mash.chit, mash.chet, ma.she.chat, cha.loph) attach to M10-BND as members but contribute 0 verses to this VCG. Suggested:

- code: `M10-BND-VCG-01`
- label/context_description: "PHASE_8_5_FLAG — Phase 3 BOUNDARY-verdict terms pending resolution. The 5 verses come from a.ven (Deu 26:14; Job 5:6; Psa 90:10; Pro 22:8) and che.vel (Mic 2:10). Phase 8.5 will resolve each term to SET-ASIDE, ROUTE-TO-CLUSTER (M03 grief / M20 distress / M10c defilement candidates), or PROMOTE-TO-SUBGROUP."
- anchor: any of the 5 (e.g. Job 5:6)

This is the only sub-group that gets exactly one VCG by construction. The substantive sub-groups (M10-A through M10-I) carry only STAYS-verdict terms; no provisional / PHASE_8_5_FLAG verses to isolate within them.

### Multi-faceted terms — already resolved at Phase 6

Two terms (pa.sha, paraptōma) split across two sub-groups, but each individual vc_id is in **exactly one sub-group** after Phase 6 routing. No special handling needed at Phase 7. The verses appear in the meanings report under their resolved sub-group.

---

## Your task — per sub-group, design VCGs

For each sub-group (in code order: M10-A → M10-B → M10-C → M10-D → M10-E → M10-F → M10-G → M10-H → M10-I → M10-BND), produce:

1. **VCG definitions** — provisional `group_code`, `context_description`, member verse list, one anchor verse.
2. **Per-sub-group design document** written to disk **immediately** after designing that sub-group (mandatory per §10.7 staged write-out — clears working context before moving on).
3. **Per-sub-group sum verification** — total member vc_ids across the sub-group's VCGs must equal the sub-group's verse count from the meanings report (274 / 339 / 64 / 97 / 162 / 147 / 101 / 64 / 72 / 5).

After all sub-groups are processed, produce the **unified VCG creation JSON** (one file covering all sub-groups).

---

## Process per sub-group (§10.2 + §10.7 staged write-out)

1. **Read** every verse-meaning in the sub-group's section of the meanings report. **Every row. No skipping. No sampling.** Even for the large sub-groups (M10-B at 339 verses, M10-A at 274) — the volume is the work.
2. **Cluster meanings into provisional VCGs.** A VCG groups verses with substantively similar inner-being content within the sub-group's characteristic. Aim for VCGs of roughly 10–30 verses for large sub-groups; smaller sub-groups may have VCGs of 2–10. A 1-verse VCG is acceptable when the content is genuinely singular.
3. **Name each VCG** with a provisional code (format: `M10-{X}-VCG-{seq}`, e.g. `M10-A-VCG-01`) and a one-paragraph `context_description`.
4. **Designate ONE anchor verse per VCG** — the verse that most directly and definitionally evidences the phenomenon the VCG names. The anchor's vc_id must be in the VCG's member list.
5. **Note dual-membership verses** — verses that legitimately belong to two VCGs (rare; usually within the same sub-group). Flag explicitly.
6. **Write the per-sub-group design document to disk immediately:**
   `Sessions/Session_Clusters/M10/wa-cluster-M10-{subgroup_code}-vcg-design-v1-20260523.md`
7. **Verify sum.** Members must equal input count.
8. Move to next sub-group; repeat.

---

## Special considerations per sub-group

### M10-A (274V — Sin as committed act, 8 terms)

Mixed-term sub-group spanning **cha.ta** (201V — bulk of M10-A), **hamartanō** (37V), plus speech-act / mechanism terms (blasfēmia 18V, pa.sha political-revolt 9V, blasfēmos 4V, deleazō 3V, apostasia 1V, sunupokrinomai 1V). Expect VCGs to partition by *who is sinning against whom*: sin-against-God, sin-against-neighbour, sin-of-speech, sin-as-enticement, sin-as-political-rebellion (pa.sha secondary), hypocrisy-as-sin. Cross-register flags (M06, M08, M14) preserved on the specialised-term VCGs.

### M10-B (339V — Sin as moral condition, 12 terms)

The biggest sub-group. **chat.tat H2403B** (159V) and **hamartia G0266** (105V) dominate. Plus paraptōma non-Adam verses (9V), chet (33V), hamartēma (4V), cha.ta.ah (8V + 2V across two sub-entries), rish.ah (4V), al.vah (1V), and the atonement pair kip.pu.rim (8V) + chat.tat sin-offering (4V). Expect VCGs to partition by: sin-as-burden, sin-as-enslaving-power, sin-as-universal-human-condition, sin-as-death-state, sin-as-cultic-burden, atonement-response (carry M11 cross-register flag), sin-as-multigenerational-weight, wickedness-as-state.

### M10-C (64V — Sinner as moral character, 2 terms)

Tight character family — **hamartōlos** (45V Greek) + **chat.ta** (19V Hebrew). Partitioning likely by: sinner as social-moral category, sinner as person owning identity, sinners as constituted/imputed status, habitual extreme sinners (Sodom, Amalekites, kingdoms).

### M10-D (97V — Guilt as inner-being state, 6 terms)

**a.sham** (31V) + **a.von guilt** (27V) + **a.von punishment** (18V) + **ash.mah** (17V) + **a.shem** (3V) + **pu.qah** (1V, M03 cross-register). VCGs likely partition by: guilt-recognition-by-conscience, guilt-as-weight-borne, guilt-exposed-by-God, guilt-removed-by-divine-action, punitive-burden-of-guilt.

### M10-E (162V — Iniquity as accumulated crime, 1 term)

**Single-term sub-group** — a.von H5771G crime sub-entry only. With 162V from one term, expect VCGs to partition by *kind of iniquity*: generational inheritance, personal burden carried, corporate weight, heart-seated, communal rotting, accumulated debt before God, hidden-vs-exposed iniquity, idol-related iniquity.

### M10-F (147V — Transgression / rebellion, 7 terms)

**pe.sha** (90V) + **pa.sha rebellion-against-God** (28V) + paraptōma Adam-paradigm (5V) + parabasis (7V) + parabatēs (5V) + parabainō (4V) + sa.rah (8V). Partition by: transgression-against-God, transgression-of-law, Adam-paradigm-transgression, wilful-political-rebellion-as-pattern, revolt-as-prophetic-language.

### M10-G (101V — Faithlessness / treachery, 3 terms)

**ba.gad** (39V) + **ma.al verb** (34V) + **ma.al noun** (28V). M13/M31 cross-register on every VCG. Partition by: covenant-betrayal-toward-God, marital/relational-treachery, sacrilege (Achan; priestly trespass), generational/national unfaithfulness.

### M10-H (64V — Perversion / corruption, 14 terms)

Many small-corpus terms — the most diverse term-set in M10. Partition by: perversion-of-speech, perversion-of-justice, perversion-of-the-mind, perversion-of-the-way (cognitive/moral inversion), sexual-perversion (te.vel), self-corruption (ftheirō, fthora, sur), lewdness-with-shame-exposure (nav.lut, M07 cross-register), corruption-paired-with-grief (cha.val, a.vah twist, M03 cross-register).

### M10-I (72V — Injustice, 6 terms)

**av.lah** (32V) + **a.vel** (20V) + **adikos** (11V) + **av.val** (5V) + **adikēma** (3V) + **a.vil** (1V). M26 cross-register on every VCG (every term in this sub-group has the M26 flag). Partition by: judicial-injustice, relational-injustice, character-marked-by-injustice, accumulated-unjust-acts.

### M10-BND (5V)

Single VCG per §10's special handling. See "Important" section above.

---

## Cross-register flag preservation

When a VCG carries one or more cross-register-flagged terms, its `context_description` must explicitly name the flag(s). Examples:

- M10-B atonement-response VCG: "atonement as priestly response to sin-as-state — primary register M11 (Repentance/Forgiveness/Restoration)"
- M10-G VCGs: "treachery as covenant-breaking sin — M13 (Truth/Faithfulness) and M31 (Faith/Unbelief) cross-register"
- M10-I VCGs: "injustice as opposite of righteousness — M26 (Righteousness/Justice) cross-register"
- M10-H specific VCGs: M03 flag for cha.val/a.vah, M07 flag for nav.lut, M23/M35 flag for fthora bodily-decay verses

---

## Output structure

### Per sub-group design document

`Sessions/Session_Clusters/M10/wa-cluster-M10-{subgroup_code}-vcg-design-v1-20260523.md`

10 files total: M10-A, M10-B, M10-C, M10-D, M10-E, M10-F, M10-G, M10-H, M10-I, M10-BND.

Structure of each:

```markdown
# M10-{X} VCG design

**Sub-group:** {X} — {label}
**Verse count (Phase 6):** {N}
**Characteristic:** CHAR-{n} ({name})
**Cross-register flag (if any):** {flag}

## VCGs

### M10-{X}-VCG-01 — {provisional name}

**context_description:** ...

**Anchor:** vc_id={N} ({reference})

**Members ({count}):**
- vc_id={N} {reference} ({strongs} {translit}) — {short meaning excerpt}
- ...

---

(repeat per VCG)

## Sum verification

VCG members sum: {sum}
Expected: {N}
Result: PASS / FAIL
```

### Unified VCG creation JSON

After all sub-groups: `Sessions/Session_Clusters/M10/wa-cluster-M10-vcg-creation-v1-20260523.json`

```json
{
  "_meta": {
    "cluster": "M10",
    "phase": 7,
    "date": "2026-05-23",
    "total_subgroups": 10,
    "total_vcgs": <N>,
    "total_verses": 1325
  },
  "subgroups": {
    "M10-A": {
      "vcgs": [
        {
          "provisional_code": "M10-A-VCG-01",
          "description": "...",
          "verses": [<every vc_id>],
          "anchor_vc_id": <vc_id>
        }
      ]
    }
  }
}
```

Field name **must** be `verses` (not `key_verses`, not `members` — complete arrays per §10.8).

---

## Discipline (§10.7 + §10.8)

1. **Read every verse-meaning** for each sub-group. No sampling. The biggest sub-groups (M10-B 339, M10-A 274) require careful reading — this is the work.
2. **Stage by sub-group.** Don't try to hold all 10 sub-groups in working memory. After M10-A: write design doc, verify sum, move to M10-B. Repeat.
3. **Sum verification per sub-group.** Members must equal input count.
4. **Anchor in members.** Every `anchor_vc_id` must be in its VCG's `verses` array.
5. **No phantom vc_ids.** Every vc_id used must be in the meanings report.
6. **No vc_id in two VCGs** unless explicitly dual-membership flagged (rare).
7. **M10-BND single VCG** holding all 5 BOUNDARY verses — do NOT subdivide.
8. **Preserve cross-register flags** in VCG descriptions for M10-B (atonement → M11), M10-D (pu.qah → M03), M10-G (all → M13/M31), M10-H (specific terms → M03, M07, M23/M35), M10-I (all → M26), plus the specialised-term flags in M10-A (M06, M08, M14).

---

## Pre-submission checklist (§10.8, AI verifies before declaring complete)

- [ ] 10 design documents on disk (one per sub-group).
- [ ] Each design doc carries a sum-verification line.
- [ ] Unified JSON written with field name `verses` (complete arrays).
- [ ] Every `anchor_vc_id` is in its VCG's `verses` array.
- [ ] Union of all `verses` per sub-group equals input count (274 / 339 / 64 / 97 / 162 / 147 / 101 / 64 / 72 / 5).
- [ ] Total `verses` across cluster = 1,325.
- [ ] No vc_id in two VCGs (unless dual-membership flagged).
- [ ] M10-BND has exactly one VCG carrying all 5 verses; the 4 empty-corpus BOUNDARY terms attach as members without verse contributions.
- [ ] Cross-register flags preserved per the list above.

CC will validate every item before applying. Failures send Phase 7 back for resubmission with a delta report.

---

## After you finish

1. Confirm pre-submission checklist passes.
2. Ping CC: "M10 Phase 7 VCG design ready" with the file list.
3. CC validates against the DB (§10.9), then builds the Phase 7 apply directive.

---

*End of brief. Load the meanings report (#2). Process sub-groups in code order. Stage write-outs.*
