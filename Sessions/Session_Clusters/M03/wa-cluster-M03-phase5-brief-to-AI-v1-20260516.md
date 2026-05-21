# M03 Phase 5 brief — Sub-group design

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §8 (Phase 5)
**Date:** 2026-05-16

---

## State of M03 at Phase 5 open

| Item | Count |
|---|---|
| Active terms (post-Phase-4) | **78** |
| Of which: STAYS (regular) | 50 |
| Of which: BOUNDARY (designated at Phase 3) | **28** (much higher than M01's 12 or M02's 5 — reflects vocabulary breadth) |
| Active is_relevant verses | ~595 (after the 11 transferred terms left with their verses) |
| `cluster.status` | `Analysis - In Progress` (flipped at Phase 4 per v2_2 §7.6) |

Phases 1–4 complete. Phase 5 designs M03's sub-group structure from the Phase 2 meaning corpus.

---

## Your task per v2_2 §8

For each verse-meaning in the constitution report's §2 meaning corpora:

1. **Read every verse-meaning across the 78-term cluster** (term by term).
2. **Identify provisional clusters of meaning** — groups of verses (potentially spanning multiple terms) that evidence substantially similar inner-being content within M03's grief / sorrow / lament / mourning / anguish / bitterness / weeping / groaning register.
3. **Name each provisional sub-group**:
   - `subgroup_code` — `M03-A`, `M03-B`, etc.
   - `label` — short descriptive name
   - `core_description` — one paragraph written *from the meanings*, not from prior labels
4. **Note multi-faceted terms** — primary + secondary sub-group placements.
5. **Design a `M03-BOUNDARY` sub-group** — the 28 BOUNDARY terms from Phase 3 go here. Brief description noting the analytical question.
6. **Produce a verse-to-sub-group mapping** — every is_relevant vc row gets one sub-group assignment.

---

## Inputs

### Primary analytical input

[Sessions/Session_Clusters/M03/wa-cluster-M03-constitution-v2-20260516.md](wa-cluster-M03-constitution-v2-20260516.md) — the **updated** constitution report (v2, post-Phase-4) showing the now-stable 78-term cluster. The 11 transferred terms are no longer present.

### Governing instruction

[Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) — §8.

---

## Decisions already made — do NOT re-debate

1. **The 78 terms are M03's final analytical set.** Don't propose transfers; don't re-instate transferred terms.
2. **The 28 BOUNDARY terms** go in `M03-BOUNDARY`. Don't propose placing them in characteristic-bearing sub-groups (without explicit rationale to override the Phase 3 boundary verdict).
3. **The 326 set-asides are out of scope.**
4. **Anchors** are Phase 1 provisional placeholders.

---

## Special handling for M03

### 1. M03 is the most diverse cluster yet — likely 7–9 sub-groups + BOUNDARY

M01 produced 7 substantive + BOUNDARY (8 total). M02 produced 6 substantive + BOUNDARY (7 total). M03 has:
- 78 active substantive terms (more than M02's 38 substantive)
- Multiple distinct registers visible in the term set:
  - **Lament / verbal mourning** (sa.phad, ko.ven, koptō, pen.the.o, mis.ped, mar.ze.ach, ta.a.niy.yah)
  - **Weeping / tears** (ba.khah, da.ma, klaiō, klauthmos, dim.ah, be.khi, be.khit, be.kheh)
  - **Groaning / sighing** (a.nach, a.na.qah, a.na.chah, ne.ha.mah, ne.a.qah, stenagmos, stenazō, sustenazō, sullupeō)
  - **Inner pain / ache** (ya.gon, ka.av, ke.ev, makh.ov, a.tsav, che.vel-B-pain, makh.ov)
  - **Anguish / pressure** (odunē, odunaō, sunochē, me.tsu.qah)
  - **Bitterness of soul** (me.mer, mam.ror, mo.rah, mor.rah, ma.ror, pikrainō)
  - **Inner-being sorrow** (lupeō, perilupos, penthos, tu.gah, de.a.von, e.vel, a.val, a.vel)
  - **Distress** (tsar — distress register, tsa.rah)

Expect **7–9 substantive sub-groups + 1 BOUNDARY** = 8-10 total. Larger than M01/M02. Don't artificially inflate count; let the meanings group.

### 2. Bitterness register

After Phase 4 transfers (pikria → M02, pikros → M28), the remaining bitterness terms (me.mer, mam.ror, mo.rah, mor.rah, ma.ror, pikrainō) are all genuine inner-soul-bitterness — should form a coherent sub-group or be folded into broader sorrow.

### 3. Tear / weeping vocabulary (large family)

8 weeping-related terms (klaiō, klauthmos, ba.khah, da.ma, dim.ah, be.kheh, be.khi, be.khit). Likely one cohesive sub-group focused on the somatic-tear register.

### 4. Lament / mourning ritual

7 mourning-related terms (sa.phad, mis.ped, koptō, pen.the.o, penthos, mar.ze.ach, ta.a.niy.yah). These name the social/ritual outworking of grief — likely one sub-group focused on lament-as-outer-act.

### 5. tsa.rah (H6869B) — CC-default STAYS

This term was missing from AI's debate; CC defaulted to STAYS based on its corpus (87% relevant, distress/affliction register). Treat as a normal M03 STAYS term in Phase 5.

### 6. 28 BOUNDARY terms

Place in M03-BOUNDARY sub-group with brief description. These include labor-pain imagery (cha.val, ōdinō already STAYS), pressure register (thlibō, ponos, skullō, stenochōreō), agony register (basanizō ×2, basanos), distress homonyms (ra.ah-distress:harm), mixed-register vexation (a.mal, e.tsev, o.tsev, its.tsa.von, ka.as-vexation if present), faintness (dav.va, cha.lah), complaint (si.ach), torment (ma.a.tse.vah), tossing (ne.dud). Researcher decision at Phase 12.

---

## Output expected from you

### 1. Sub-group design document

`Sessions/Session_Clusters/M03/WA-M03-subgroup-design-v1-20260516.md`

Per sub-group block (including BOUNDARY):

```markdown
## M03-X — {label}

**Core description:** One paragraph written from the meanings.

**Terms (primary):** {list of mti_ids + strongs + translit}
**Terms (secondary, if any):** {multi-faceted terms with primary elsewhere}

**Representative meanings (3-5 verses):**
- {reference} — {meaning excerpt}
```

### 2. Mapping JSON

`Sessions/Session_Clusters/M03/WA-M03-subgroup-mapping-v1-20260516.json`

```json
{
  "cluster_code": "M03",
  "generated_at": "...",
  "subgroups": [
    {
      "subgroup_code": "M03-A",
      "label": "...",
      "core_description": "...",
      "sort_order": 1,
      "term_placements": [
        {"mti_term_id": N, "strongs": "...", "translit": "...", "placement": "primary"},
        ...
      ]
    }
  ],
  "verse_assignments_by_term": {
    "note": "All is_relevant vc rows for each mti_term_id route to the sub-group listed below.",
    "mti_term_id_to_subgroup": {
      "<mti_id>": "M03-X",
      ...
    }
  }
}
```

Every active is_relevant=1 vc row's mti_term_id must be in the mapping. Sort subgroups by `sort_order` (A first, BOUNDARY last).

### 3. Obslog entries

Append per-sub-group entries to the existing M03 obslog file.

### ⚠️ STAGED WRITE-OUT — mandatory

1. Draft sub-group design document → **write to disk immediately.**
2. Derive mapping JSON → **write to disk immediately.**
3. Append obslog entries → **save.**

---

## Discipline reminders

1. **Sub-groups emerge from meanings, not from gloss-list categories.**
2. **One verse, one primary sub-group.** Multi-faceted terms get secondary placements at the *term* level.
3. **BOUNDARY is structural-only.** No characteristic-bearing analysis of BOUNDARY terms at Phase 5.
4. **No inherited VCG influence.** Suppressed per v2_2 §2.3.
5. **Output to new files, not in-place edits.**

---

## When you're done

CC will:

1. Validate your mapping JSON (every is_relevant vc has an assignment; every sub-group has ≥1 term).
2. Apply the Phase 6 directive (INSERT cluster_subgroup rows, populate mti_term_subgroup, UPDATE verse_context.cluster_subgroup_id).
3. Generate the Phase 7 input report.

---

## Provenance

- Updated constitution report (primary input): [wa-cluster-M03-constitution-v2-20260516.md](wa-cluster-M03-constitution-v2-20260516.md)
- Phase 3 debate: [wa-cluster-m03-debate-v1-20260516.md](wa-cluster-m03-debate-v1-20260516.md)
- Phase 4 applied: [WA-M03-dir-001-term-transfer-applied-v1-20260516.md](WA-M03-dir-001-term-transfer-applied-v1-20260516.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md)
- Validation methodology: [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)

---

*End of Phase 5 brief.*
