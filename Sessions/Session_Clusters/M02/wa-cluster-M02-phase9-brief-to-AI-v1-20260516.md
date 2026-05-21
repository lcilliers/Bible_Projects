# M02 Phase 9 brief — Catalogue prompts (findings authoring)

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §12 (Phase 9)
**Date:** 2026-05-16

---

## State of M02 at Phase 9 open

| Item | Count / value |
|---|---|
| Active terms | **43** |
| Active sub-groups | **7** (M02-A · M02-B · M02-C · M02-D · M02-E · M02-F · M02-BOUNDARY) |
| Active VCGs | **25** (Phase 7-designed, Phase 8-confirmed sole active phenomenology) |
| Active is_relevant verses (routed) | **641** |
| Anchors (definitional verses) | 53 (26 AI-designated VCG anchors + 27 provisional per-term anchors) |
| Set-asides (is_relevant=0) | 56 (Phase 1 outcome) |
| `cluster.status` | `Analysis - In Progress` |

**Phases 1–8 complete.** Phase 9 produces the consolidated findings document that Phase 11 loads to `cluster_finding`.

---

## Your task per v2_2 §12

Answer every prompt in the **T0–T7 catalogue (189 prompts, v2.1)** at:

- **Each active sub-group scope** (M02-A through M02-F; M02-BOUNDARY uses structural characterisation only — see §"Special handling")
- **Cluster scope** (`[CLUSTER]` synthesis across the whole cluster)

Per prompt × scope cell, author one of:

- **E** — evidenced finding. Name the verses or VCGs that support it.
- **S** — silent. Describe what the silence means.
- **G** — gap. Describe what data is missing.

Every E must cite specific verse references or VCG codes. The test is not "does this sound right?" but **"can I name the specific verse or group that evidences this?"** (§2.4)

---

## Inputs

### Primary analytical input (the data you ground every finding in)

[Sessions/Session_Clusters/M02/wa-cluster-M02-vcg-grouped-v1-20260516.md](wa-cluster-M02-vcg-grouped-v1-20260516.md) — VCG-grouped report. Per-sub-group → per-VCG → every member verse with reference, term, and Phase 2 meaning. Anchors flagged ⚓; dual-membership flagged ⇄. **This is the only verse-level analytical material you use for Phase 9.**

### Mandatory input for T7 prompts

The M02 cluster does not yet have a dedicated science extract (M01 had one). For T7 (Evidential and Methodological Foundation) prompts, ground your answers in the verse evidence + meaning corpus alone. Note where a science framework would be useful but is not yet available — those become candidates for a future M02 science extract addendum.

### Catalogue (the 189 prompts)

[Workflow/Tiers/wa-obs-catalogue-tiered-v2_1-20260513.md](../../../Workflow/Tiers/wa-obs-catalogue-tiered-v2_1-20260513.md) — the T0–T7 tier catalogue, v2.1.

### Governing instruction

[Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) — §12 in particular.

---

## Decisions already made — do NOT re-debate

1. **Sub-group structure (7 sub-groups)** is final.
2. **VCG structure (25 active VCGs)** is final. Don't propose adding, merging, splitting, or re-anchoring. M02-D-VCG-04 was designed at Phase 7 but ended up with 0 routed verses due to dual-membership precedence — it's a dangling empty VCG, do not author findings for it.
3. **Anchors (53 total)** are set.
4. **Term-to-sub-group placements** are final.
5. **Set-asides (56)** are final — those verses are out of scope.

---

## M02 sub-group reference (for orientation only)

| Code | Label | Verses | VCGs | Register |
|---|---|---:|---:|---|
| M02-A | Divine Wrath as Judicial Force | 109 | 5 | Settled judicial wrath; oaths; eschatological |
| M02-B | Burning Rage and Inner Heat | 263 | 7 | Largest — fire/kindling/heat metaphors |
| M02-C | Indignation and Moral Displeasure | 36 | 3 | Sustained moral verdict; sullen/brooding |
| M02-D | Provocation — Anger Aroused | 58 | 3 | Idolatry-as-provocation + recipient-side |
| M02-E | Jealousy, Zeal and Possessive Passion | 77 | 4 | Divine zeal vs human possessive jealousy split |
| M02-F | Strife, Quarrel and Contentious Anger | 16 | 2 | Anger-driven relational contention |
| M02-BOUNDARY | Pending Researcher Disposition | 82 | 1 | 6 BOUNDARY terms (antilogia, erethizō, zestos, ka.a.s, riv, tsur) |

---

## Special handling

### 1. M02-BOUNDARY sub-group — structural characterisation only

Same as M01 precedent. Per `**[BOUNDARY — H1234 translit]**` markers, provide per-term structural notes for each of the 6 BOUNDARY terms:
- G0485 antilogia (dispute — mixed register)
- G2042 erethizō (provoke/irritate — thin corpus, opposed valences)
- G2200 zestos (hot — Rev 3:15-16 fervor not anger)
- H3708B ka.a.s (vexation — anger/grief boundary)
- H7379 riv (strife — anger-driven contention vs legal-procedural split)
- H6696B tsur (provoke/besiege — empty active corpus)

A few cross-cutting BOUNDARY notes can use `**[BOUNDARY]**` (no term suffix) if the observation applies across multiple BOUNDARY terms. Do not do a full T0–T7 pass on M02-BOUNDARY.

### 2. Divine wrath in M02-A/B — programme scope reminder

M02 is heavily God-as-subject. The programme's scope is **human inner being**. Per Phase 7 review, no divine-inner-state set-asides were flagged for M02 — every divine-wrath verse describes the characteristic in operation (wrath as enacted force, judicial action, covenantal consequence), which is in scope. Continue this discipline at Phase 9 — analyse divine wrath as the characteristic's display, not as God's inner emotional life.

### 3. M02-E Jealousy register — 4 VCGs distinguishing zones

Phase 7 designed 4 VCGs for jealousy:
- M02-E-VCG-01 — God's jealousy as a defining attribute (qan.na, qan.no)
- M02-E-VCG-02 — God's protective jealousy in action (qin.ah)
- M02-E-VCG-03 — Human jealousy directed toward God (Phinehas, Elijah zeal)
- M02-E-VCG-04 — Human jealousy toward other humans (possessive envy)

The findings for M02-E should respect these distinct registers — your findings can use VCG-level scope markers (`[E-VCG-02]` etc.) when a finding applies to a specific VCG within M02-E rather than the whole sub-group.

### 4. M02-B is large (263 verses, 7 VCGs) — expect rich findings

The burning-rage / inner-heat sub-group has the most analytical density. Expect:
- Divine vs human burning anger distinctions (M02-B-VCG-01 vs others)
- Inner-state heat vs enacted heat
- Anger requiring restraint (M02-B-VCG-05)
- Recipient-experience of being under wrath (M02-B-VCG-07)

VCG-level scope markers are particularly useful here.

### 5. Dual-membership verses (15 cases, marked ⇄)

Verses with content straddling two VCGs. Primary VCG is shown in the grouped report; secondary VCG is recorded in DB notes. For Phase 9, cite a dual-membership verse under either VCG when authoring a finding — both are analytically defensible.

### 6. Cross-routing observations from Phase 7

AI's Phase 7 flagged 5 cross-routing cases (vc=95 Mar 3:5 anger-with-grief, vc=64926 Ecc 5:17 chronic state, vc=64773 Neh 4:7 hostility register, vc=64787 Isa 45:24 enemy rage at God, vc=862/865 Hannah grief from provocation). These are retained in primary sub-groups but worth being aware of for T6 distinction prompts.

---

## Output expected from you

### 1. Consolidated findings document, structured into 4 parts by tier (per v2_2 §12.5)

- `Sessions/Session_Clusters/M02/WA-M02-consolidated-findings-v1-20260516-part1.md` — **T0–T1** (12 + 24 = 36 prompts)
- `WA-M02-consolidated-findings-v1-20260516-part2-T2.md` — **T2** (31 prompts)
- `WA-M02-consolidated-findings-v1-20260516-part3-T3-T4.md` — **T3 + T4** (33 + 24 = 57 prompts)
- `WA-M02-consolidated-findings-v1-20260516-part4-T5-T7.md` — **T5–T7** (21 + 24 + 20 = 65 prompts)

### ⚠️ STAGED WRITE-OUT — mandatory

**Write each part to disk the moment that part is complete. Do NOT hold all four parts in memory and write them at the end.**

Process:

1. Complete part 1 (T0–T1, 36 prompts × scope cells).
2. **Write part 1 to file immediately.** Confirm the file exists on disk.
3. Complete part 2 (T2, 31 prompts × scope cells).
4. **Write part 2 to file immediately.** Confirm.
5. Repeat for parts 3 and 4.

Why: prior cluster runs have shown AI fighting context window pressure when carrying large analytical output. Staging the write-out clears working context between parts and produces durable artefacts even if a later part needs to be re-attempted. The cross-sub-group review pass happens **after** part 4 is written, by re-reading the four on-disk files.

### 2. Authoring discipline (parser-safe form — §12.4)

The Phase 11 loader parses these documents — **do not deviate from format**:

1. **One scope marker per line.** Each `**[scope]**` marker starts at the beginning of a line.
2. **Every prompt must carry at least one explicit scope marker.**
3. **One block per (prompt × scope).** Each (prompt, scope) cell appears at most once.
4. **Block separator.** A horizontal rule `---` on its own line marks the end of one prompt's findings.

**Marker catalogue (recognised by the loader):**

| Marker | Meaning |
|---|---|
| `**[A]**` or `**[A — Label]**` | finding for sub-group M02-A (similarly B–F) |
| `**[A, B, C]**` (comma-separated) | finding shared across listed sub-groups |
| `**[E-VCG-02]**` | VCG-level scope (v2_2 §14.4 — preserved by loader) |
| `**[E-VCG-01/03/04/05]**` | multi-VCG scope (slash-separated; loader handles semicolon-joined storage) |
| `**[CLUSTER]**` or `**[CLUSTER — all sub-groups]**` | cluster-level synthesis |
| `**[BOUNDARY — H1234 translit]**` | per-term structural characterisation for a BOUNDARY term |

**Inline outcome codes:**
- `E — text` (or no leading code) → finding (or `cluster_synthesis` if scope is CLUSTER)
- `S — text` → silent
- `G — text` → gap

### 3. Self-contained requirement

Each of parts 1–4 must be readable without reference to any other file:
- Every prompt answered with full text per scope.
- Every E response includes specific verse reference(s) or VCG code(s) in the body.
- A Session C reader should be able to write the cluster publication using only these four parts.

### 4. Cross-sub-group review pass

After all sub-group passes are complete, read across the full set of findings before writing CLUSTER-level entries. Look for:
- Cluster-level patterns recurring across sub-groups → record once as `[CLUSTER]`.
- Structural relationships between sub-groups (causal sequences, asymmetries — relevant for T6).
- Absences significant in totality.
- Internal contradictions — resolve by returning to verse evidence.

---

## Discipline reminders

1. **Verse-grounded only.** Output that reads smoothly and is well-structured can still be entirely ungrounded. Test: "can I name the specific verse or VCG that evidences this?" If no verse can be named, mark **S** or **G**.

2. **Use the grouped report, not memory.** Cite from the 641 verses we routed; don't write findings from general theological knowledge of anger vocabulary.

3. **Anchors are weighted evidence, not the only evidence.** Anchors are the single most-definitional verse per VCG (or per term). For a prompt, the supporting evidence includes the anchor plus the wider VCG.

4. **Don't fight Phase 7 decisions.** If a VCG feels misnamed or a verse mis-routed, note your concern in the body but author against the current structure. Researcher reviews at Phase 12.

5. **Output to new files, not in-place edits.**

6. **Stage the write-out** — one part to disk before starting the next.

7. **Citation discipline.** Cite verses by reference (e.g. `Exo 32:19`) and VCGs by their `group_code` (e.g. `M02-B-VCG-01`). Don't cite by vc_id or by inherited VCG ids (those are gone).

8. **VCG-level scope markers are encouraged.** When a finding genuinely applies to specific VCGs within a sub-group rather than the whole sub-group, use `[E-VCG-02]` etc. — the v2_2 loader preserves VCG specificity as queryable structure (per Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md trust framework).

---

## Note on validation

The Session B Cluster pipeline has been validated via the blind verification methodology recorded at [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md). M01 testing showed AI does not fabricate findings — 0 empty pick lists across 272 findings tested, 90.6% target precision under maximum distractor pressure. The methodology may be re-applied to M02 if findings appear suspect; the researcher's discretion governs.

Your Phase 9 work should maintain the verse-grounded discipline that produced those validation results.

---

## When you're done

CC will:

1. Parse the four consolidated-findings parts against the catalogue (189 prompts × scope cells, parser format, anchor citation discipline).
2. Generate the **inherited-findings carry-over report** (Phase 10 input).
3. Bring Phase 10 brief for inherited-finding reconciliation.
4. Phase 11: load consolidated findings into `cluster_finding` (with VCG-level scope support per v2_2 §14.4).
5. Phase 12: cluster closure.

---

## Provenance

- VCG-grouped report (primary input): [wa-cluster-M02-vcg-grouped-v1-20260516.md](wa-cluster-M02-vcg-grouped-v1-20260516.md)
- Tier catalogue: [wa-obs-catalogue-tiered-v2_1-20260513.md](../../../Workflow/Tiers/wa-obs-catalogue-tiered-v2_1-20260513.md)
- Phase 7 applied (VCG creation): [WA-M02-dir-003-vcg-create-applied-v1-20260516.md](WA-M02-dir-003-vcg-create-applied-v1-20260516.md)
- Phase 8 applied (dissolution): [WA-M02-dir-004-vcg-dissolve-applied-v1-20260516.md](WA-M02-dir-004-vcg-dissolve-applied-v1-20260516.md)
- Inherited VCG archive (durable record): [WA-M02-inherited-vcg-archive-v1-20260516.md](WA-M02-inherited-vcg-archive-v1-20260516.md)
- Validation methodology: [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md)

---

*End of Phase 9 brief.*
