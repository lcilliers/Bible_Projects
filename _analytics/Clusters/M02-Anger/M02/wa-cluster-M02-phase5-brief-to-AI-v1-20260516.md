# M02 Phase 5 brief — Sub-group design

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §8 (Phase 5)
**Date:** 2026-05-16

---

## State of M02 at Phase 5 open

| Item | Count / value |
|---|---|
| Active terms (post-Phase-4) | **43** |
| Of which: STAYS (regular) | 38 |
| Of which: BOUNDARY (designated at Phase 3) | 5 |
| Active is_relevant verses | **667** (after the 4 transferred terms left; ~7 verses moved with them) |
| `cluster.status` | `Analysis - In Progress` (flipped at Phase 4 per v2_2 §7.6) |

**Phases 1–4 complete.** Phase 5 designs the cluster's sub-group structure by clustering the Phase 2 meaning corpus.

---

## Your task per v2_2 §8

For each verse-meaning in the constitution report's §2 meaning corpora:

1. **Read every verse-meaning across the 43-term cluster** (term by term).
2. **Identify provisional clusters of meaning** — groups of verses (potentially spanning multiple terms) that evidence substantially similar inner-being content within M02's anger/wrath/indignation/jealousy/provocation/dispute/vexation register.
3. **Name each provisional sub-group**:
   - `subgroup_code` — `M02-A`, `M02-B`, etc. (canonical, no transliterations)
   - `label` — short descriptive name (e.g. "Burning Anger / Inner Heat" or "Divine Wrath as Judicial Action")
   - `core_description` — one paragraph written *from the meanings*, not from prior labels or gloss-list inference
4. **Note multi-faceted terms** — terms whose verses span more than one provisional sub-group. These get primary + secondary sub-group records.
5. **Design a `M02-BOUNDARY` sub-group** — the 5 BOUNDARY terms from Phase 3 go here. Brief description identifies the analytical question (e.g. "terms whose corpus is mixed/thin/edge-case — pending researcher disposition at Phase 12").
6. **Produce a verse-to-sub-group mapping** — every is_relevant vc row gets one sub-group assignment.

---

## Inputs

### Primary analytical input

[Sessions/Session_Clusters/M02/wa-cluster-M02-constitution-v2-20260516.md](wa-cluster-M02-constitution-v2-20260516.md) — the **updated** constitution report. Note this is v2, regenerated post-Phase-4 to reflect the now-stable 43-term cluster. The 4 transferred terms (eritheia → M28, zid → M08, ma.rar → M03, tsa.rah → M24) are no longer in this report.

### Governing instruction

[Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) — §8 in particular.

### Note

The constitution report header references `v2_0` of the instruction (template string). The active instruction is **v2_2** — same §6 process for the report's structure, and §8 governs your sub-group design.

---

## Decisions already made — do NOT re-debate

1. **The 43 terms are M02's final analytical set.** Phase 3 + Phase 4 finalised which terms belong to M02. Don't propose new transfers; don't try to re-instate transferred terms.
2. **The 5 BOUNDARY terms** (antilogia, erethizō, zestos, ka.a.s, riv) go in `M02-BOUNDARY`. Don't propose placing them in characteristic-bearing sub-groups.
3. **The 56 set-asides** (is_relevant=0) are out of scope. They are not in the meaning corpus and should not be in your sub-group design.
4. **Anchors** are provisional placeholders from Phase 1. They have no analytical weight at Phase 5 — ignore.

---

## Special handling for M02

### 1. Jealousy register — God-zeal vs human envy

The Hebrew jealousy family (qa.na, qin.ah, qan.na, qan.no) all STAYED in M02. Their corpora include both:
- **Divine zeal / protective jealousy** — God's jealousy *for* his people / his name (Exo 20:5; Num 25:11; Deu 32:21).
- **Human zeal as anger-driven possessiveness** — Pro 27:4 (jealousy fiercer than wrath); Eccl 4:4 (envy as a driver of work).

These may form one sub-group (jealousy as a unified phenomenon) or split into two (divine zeal vs human envy-zeal). **Judge from the meaning corpus.**

### 2. Burning / heat metaphors

Many terms share fire/burning imagery for anger:
- cha.rah (kindle) · cha.ron (burning anger) · cho.ri (burning) · che.mah (heat/wrath) · zal.a.phah (scorching) · re.gaz (rage/quake)

These are likely a single sub-group ("burning anger" / "inner heat") OR may split by:
- inner-state heat (the person becoming hot inside)
- enacted heat (heat that erupts into action)
- divine vs human heat

### 3. Wrath as judicial / eschatological action

orgē (G3709) and qe.tseph (H7110A) carry both inner-state and enacted-judgment registers. Decide whether these form a distinct "wrath as divine judicial action" sub-group, or whether they belong with the burning-anger sub-group.

### 4. Strife / dispute / quarrel — relational anger

eris (G2054) · thumomacheō · logomachia · filoneikos · mats.tsah · mats.tsut · me.ri.vah are strife / quarrel / dispute terms. Most are anger-driven contention — may form a "strife / quarrel" sub-group focused on the relational outworking of anger.

### 5. Provocation / vexation

ka.as (provoke to anger) · paroxunō · parorgizō · ma.rar · re.gaz · be.esh (be displeased) · na.phal (fall: angry) · qa.tsaph · za.am · za.aph · ka.a.s (BOUNDARY) — these name the dynamic of being provoked / kindled / vexed. Possibly one "provocation / vexation" sub-group.

### 6. tsur (H6696B) — no active relevant corpus

This term has no is_relevant verses after Phase 1 (all 28 UT verses were set-aside as the rock/cliff homonym). Despite that, Phase 3 STAYED the term per the corpus-empty STAYS rule (v2_2 §6.4.x). For Phase 5: place it in whatever sub-group best fits its lexical sense as "provoke / besiege", but note that **no verses route to it**. The placement is structural-only.

### 7. Subgroup count expectation

M01 produced 7 substantive + BOUNDARY = 8 sub-groups for 81 terms. M02's 43 terms with strong internal coherence (largely all anger-register) may produce **fewer sub-groups — perhaps 5–7 substantive + BOUNDARY**. Don't artificially inflate the count.

---

## Output expected from you

### 1. Sub-group design document

`Sessions/Session_Clusters/M02/WA-M02-subgroup-design-v1-20260516.md`

Format (one block per sub-group, including BOUNDARY):

```markdown
## M02-X — {label}

**Core description:** One paragraph written from the meanings, naming the inner-being phenomenon
this sub-group captures. Should be readable without reference to the term list.

**Terms (primary):** {list of mti_ids + strongs + translit}
**Terms (secondary, if any):** {list — multi-faceted terms whose primary lives elsewhere
but whose corpus partially evidences this sub-group}

**Representative meanings (3-5 verses):**
- {reference} — {meaning excerpt}
- ...
```

### 2. Mapping JSON

`Sessions/Session_Clusters/M02/WA-M02-subgroup-mapping-v1-20260516.json`

Machine-readable verse-to-sub-group assignment, format:

```json
{
  "cluster_code": "M02",
  "generated_at": "2026-05-16T...",
  "subgroups": [
    {
      "subgroup_code": "M02-A",
      "label": "...",
      "core_description": "...",
      "sort_order": 1,
      "term_placements": [
        {"mti_term_id": 37, "strongs": "G3709", "translit": "orgē", "placement": "primary"},
        ...
      ]
    },
    ...
  ],
  "verse_assignments": {
    "<vc_id>": "M02-X",
    ...
  }
}
```

Every is_relevant=1 vc row in M02 must be in `verse_assignments`. Sort `subgroups` by `sort_order` (A first, BOUNDARY last).

### 3. Obslog entries

Append per-sub-group entries to `wa-obslog-M02-constitution-v1-20260516.md` (the existing obslog file).

### ⚠️ STAGED WRITE-OUT — mandatory

Same discipline as M01 Phase 9 / Phase 10:

1. Draft sub-group design document → **write to disk immediately.**
2. Derive mapping JSON from the design → **write to disk immediately.**
3. Append obslog entries → **save.**

Do not accumulate all three in working context. The volume here is moderate (43 terms + ~7 sub-groups + 667 verse assignments), but the discipline applies regardless.

---

## Discipline reminders

1. **Sub-groups emerge from meanings, not from gloss-list categories.** "All terms with 'wrath' in the gloss go in sub-group A" is gloss-list inference — wrong. Read the meanings, find substantive analytical clusters.

2. **One verse, one primary sub-group.** Multi-faceted terms may have secondary sub-group placements at the *term* level, but each verse goes to exactly one primary sub-group.

3. **Verse-level dual membership at term level.** If a term's verses split between two sub-groups, the term has primary placement in the dominant sub-group + secondary placement in the other. CC handles primary/secondary at Phase 6 from your mapping.

4. **BOUNDARY is structural-only.** No characteristic-bearing analysis of BOUNDARY terms at Phase 5. The 5 BOUNDARY terms get listed in M02-BOUNDARY with brief notes; Phase 9 catalogue prompts don't run on them (per the M01 precedent).

5. **No inherited VCG influence.** 73 inherited VCGs exist for M02 terms; they're suppressed per v2_2 §2.3. Don't try to validate sub-groups against them.

6. **Output to new files, not in-place edits.** Produce v1 documents per the filenames above.

---

## When you're done

CC will:

1. Validate your mapping JSON (every is_relevant vc has an assignment; every sub-group has ≥1 term).
2. Apply the Phase 6 directive — INSERT `cluster_subgroup` rows, populate `mti_term_subgroup`, UPDATE `verse_context.cluster_subgroup_id` for every routed verse.
3. Generate the Phase 7 input report — per-sub-group verse-and-meaning report for VCG design.

---

## Provenance

- Updated constitution report (primary input): [wa-cluster-M02-constitution-v2-20260516.md](wa-cluster-M02-constitution-v2-20260516.md)
- Phase 3 debate: [wa-cluster-M02-debate-v1-20260516.md](wa-cluster-M02-debate-v1-20260516.md)
- Phase 4 applied: [WA-M02-dir-001-term-transfer-applied-v1-20260516.md](WA-M02-dir-001-term-transfer-applied-v1-20260516.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md)

---

*End of Phase 5 brief.*
