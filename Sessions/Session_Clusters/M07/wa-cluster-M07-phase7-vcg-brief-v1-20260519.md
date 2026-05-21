# M07 Phase 7 — VCG design within sub-groups — brief

**Date:** 2026-05-19
**Cluster:** M07 — Shame, Disgrace and Humiliation
**Phase:** 7 (VCG design within sub-groups)
**Audience:** Claude AI session (chat)
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10

**Read this brief first.** The structural input is the per-sub-group meanings report below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M07/WA-M07-phase7-vcg-brief-v1-20260519.md` | Primary task instructions |
| 2 | **Per-sub-group meanings report** — `Sessions/Session_Clusters/M07/wa-cluster-M07-subgroup-meanings-v1-20260519.md` | Per sub-group, every is_relevant verse with its term + Phase 2 meaning, in canonical order. **The only analytical material for VCG design** (inherited VCGs / anchors / findings explicitly suppressed per §2.3) |
| 3 | **Phase 5 sub-group design** — `Sessions/Session_Clusters/M07/WA-M07-subgroup-design-v1-20260519.md` | Sub-group definitions (characteristic-representations), cross-register flags, BOUNDARY notes |
| 4 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_8-20260519.md` §10 (Phase 7 disciplines; §10.7 staged write-out; §10.8 no-sampling pre-submission checklist) |
| 5 | **Science extract** — `Workflow/Sciences/wa-m07-shame-scienceextract-v1_0-20260513.md` | Programme-curated scientific framing of shame |
| 6 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-{current}.md` Ch.1 'Defining Inner Being' | Inner-being scope definition |
| 7 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

---

## Context

M07's sub-group structure landed at Phase 6: **9 sub-groups** (8 substantive + BOUNDARY), **363 is_relevant verses** distributed cleanly (M07-B largest at 32.7% — under the 40% gate). Each sub-group represents a characteristic per v2_8 §8.0:

| Sub-group | Characteristic | Verses | Cross-register flag |
|---|---|---:|---|
| M07-A | CHAR-1a Shame as unjust inner wound | 63 | — |
| M07-B | CHAR-1b Shame as moral consequence | 110 | — |
| M07-C | CHAR-1c Shame before God | 50 | — |
| M07-D | CHAR-2 Humiliation as enforced abasement | 50 | — |
| M07-E | CHAR-3 Dishonour as relational worth-denial | 15 | — |
| M07-F | CHAR-4 Shamefulness as moral judgment | 16 | — |
| M07-G | CHAR-5 Shame produced by contempt | 24 | **M06** (contempt source-side) |
| M07-H | CHAR-6 Innocence as structural counter | 8 | **M12** (purity register) |
| M07-BOUNDARY | (5 BOUNDARY terms) | 27 | — |
| **Total** | | **363** | |

Phase 7's task is to design **VCGs (verse_context_groups)** within each sub-group — finer-grained units that cluster verses with substantially similar inner-being content inside the sub-group's register.

---

## Your task — per sub-group, design VCGs

For each sub-group (in code order: M07-A → M07-B → ... → M07-H → M07-BOUNDARY), produce:

1. **VCG definitions** — provisional `group_code`, `context_description`, member verse list, one anchor verse.
2. **Per-sub-group design document** written to disk **immediately** after designing that sub-group (mandatory per §10.7 staged write-out — clears working context before moving on).
3. **Per-sub-group sum verification** — total member vc_ids across the sub-group's VCGs must equal the sub-group's verse count from the meanings report.

After all sub-groups are processed, produce the **unified VCG creation JSON** (one file covering all sub-groups).

---

## Process per sub-group (§10.2 + §10.7 staged write-out)

1. **Read** every verse-meaning in the sub-group's section of the meanings report. **Every row. No skipping. No sampling.**
2. **Cluster meanings into provisional VCGs.** A VCG groups verses with substantively similar inner-being content within the sub-group's characteristic. Typical sub-groups produce 2–8 VCGs.
3. **Name each VCG** with a provisional code (suggested format: `{subgroup_code}-VCG-{seq}`, e.g. `M07-A-VCG-01`) and a one-paragraph `context_description` written from the meanings.
4. **Designate ONE anchor verse per VCG** — the verse that most directly and definitionally evidences the phenomenon the VCG names. The anchor's vc_id must be in the VCG's member list.
5. **Note dual-membership verses** — verses that legitimately belong to two VCGs (within the same sub-group, or rarely across sub-groups). Flag explicitly.
6. **Write the per-sub-group design document to disk immediately:**
   `Sessions/Session_Clusters/M07/WA-M07-{subgroup_code}-vcg-design-v1-20260519.md`
7. **Verify sum.** Sum member vc_ids across the sub-group's VCGs. Must equal the sub-group's count from the meanings report. Record verification line at end of the document:

   ```
   **Verification**: VCG member sums = N1 + N2 + ... + Nk = TOTAL, matches M07-{X} input count of TOTAL ✓
   ```

8. Move to next sub-group; repeat.

---

## Cross-register flags — preserve at VCG level

**M07-G (Shame produced by contempt, M06 flag):** Within this sub-group, design VCGs that distinguish the contempt-projection dynamic where useful. For example: contempt-as-public-shaming (Mar 12:4 atimazō, Luk 23:11 exoutheneō) might be a distinct VCG from absence-of-respect-as-shame (Luk 18:2/4 entrepō) and verbal-attack-as-shaming (1Ti 5:14 loidoria). The M06 source-side flag is recorded in the sub-group description; each VCG's context_description can name how the contempt-shame dynamic operates in that VCG.

**M07-H (Innocence as structural counter, M12 flag):** 8 verses, 2 terms (niq.qa.von, qe.ha.von — same 4 verses each). Likely 1–2 VCGs at most. The M12 purity flag should be reflected in the context_description of each VCG: innocence-as-shield-against-shame is the M07 angle; the underlying purity content is the M12 angle.

---

## BOUNDARY sub-group (M07-BOUNDARY)

27 verses across 4 terms (sha.phel 24, katatomē 1, mish.chat 1, ni.dah 1). Per §8.4, BOUNDARY's VCG is **a single aggregating VCG** (e.g. `M07-BOUNDARY-VCG-01`) holding all 27 verses with a context_description naming the BOUNDARY status. The Phase 8.5 disposition (SET-ASIDE / ROUTE-TO-CLUSTER / PROMOTE-TO-SUBGROUP) will distribute these verses to their final placements.

**Anchor for the BOUNDARY VCG:** designate one verse with substantive inner-being content — for M07's BOUNDARY, an H8213 sha.phel verse (the bulk of the BOUNDARY corpus) is a good candidate (e.g. Pro 16:19 — "a lowly spirit with the poor", the verse that surfaced the M07/M09 split question most clearly).

---

## Output structure

### Per sub-group design document

`Sessions/Session_Clusters/M07/WA-M07-{subgroup_code}-vcg-design-v1-20260519.md`

```markdown
# M07-{X} VCG design — {sub-group label}

**Sub-group:** {code} ({characteristic})
**Verses in scope:** {N}
**Cross-register flag:** {M-something or None}

## VCG {code}-VCG-01 — {short name}

**Description:** {one-paragraph context_description from the meanings}

**Anchor:** vc_id={X} — {Reference} — {one-line rationale: why this verse anchors the VCG}

**Members ({N} verses):**
- vc=X — Reference — Strong's translit — {one-line meaning excerpt}
- ... (every member listed)

## VCG {code}-VCG-02 — {short name}

...

## Dual-membership notes

(Any verses flagged for dual VCG membership; usually empty)

**Verification**: VCG member sums = N1 + N2 + ... + Nk = TOTAL, matches M07-{X} input count of TOTAL ✓
```

### Unified VCG creation JSON

After all sub-groups: `Sessions/Session_Clusters/M07/WA-M07-vcg-creation-v1-20260519.json`

```json
{
  "_meta": {
    "cluster": "M07",
    "phase": 7,
    "date": "2026-05-19",
    "total_subgroups": 9,
    "total_vcgs": <N>,
    "total_verses": 363
  },
  "subgroups": {
    "M07-A": {
      "vcgs": [
        {
          "provisional_code": "M07-A-VCG-01",
          "description": "...",
          "verses": [<every vc_id>],
          "anchor_vc_id": <vc_id>
        },
        ...
      ]
    },
    ...
  }
}
```

Field name **must** be `verses` (not `key_verses`, not `members`, not "representative" — complete arrays per §10.8).

---

## Discipline (§10.7 + §10.8)

1. **Read every verse-meaning** for each sub-group. No sampling. No "representative members." No "the rest follow the same pattern." Discipline reading is enforced by the staged write-out pattern.
2. **Stage by sub-group.** Don't try to hold all 9 sub-groups in working memory. After M07-A: write design doc to disk, verify sum, log obslog entry, then move to M07-B. Repeat.
3. **Sum verification per sub-group.** Members must sum to the input count exactly. If they don't, fix before moving on.
4. **Anchor in members.** Every `anchor_vc_id` must be in its VCG's `verses` array.
5. **No phantom vc_ids.** Every vc_id used in your output must be in the meanings report (i.e. a real M07 is_relevant vc).
6. **No vc_id in two VCGs** unless explicitly flagged as dual-membership in the design document.
7. **BOUNDARY VCG aggregating only** — single VCG covering all 27 BOUNDARY verses; Phase 8.5 will distribute them.
8. **Preserve cross-register flags** in M07-G and M07-H VCG descriptions where they shape the analytical content.

---

## Pre-submission checklist (§10.8, AI verifies before declaring complete)

- [ ] 9 design documents on disk (one per sub-group: 8 substantive + 1 BOUNDARY).
- [ ] Each design doc carries a sum-verification line.
- [ ] Unified JSON written with field name `verses` (complete arrays).
- [ ] Every `anchor_vc_id` is in its VCG's `verses` array.
- [ ] Union of all `verses` per sub-group equals the sub-group input count.
- [ ] Total `verses` across the cluster = 363.
- [ ] No vc_id in two VCGs (unless dual-membership flagged).
- [ ] Every vc_id used is a real M07 is_relevant vc from the meanings report.
- [ ] BOUNDARY VCG contains every is_relevant vc of every BOUNDARY term (27 verses).

CC will validate every item before applying. Failures send Phase 7 back for resubmission with a delta report.

---

## After you finish

1. Confirm pre-submission checklist passes (run §10.8 yourself).
2. Ping CC: "M07 Phase 7 VCG design ready" with the file list.
3. CC validates against the DB (§10.9), then builds the Phase 7 directive (`wa-cluster-M07-dir-003-vcg-create-v1-{date}.md`).

---

*End of brief. Load the meanings report (#2). Process sub-groups in code order. Stage write-outs.*
