# M01 Phase 9 brief — Catalogue prompts (findings authoring)

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_0-20260515.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_0-20260515.md) §12 (Phase 9)
**Date:** 2026-05-16

---

## State of M01 at Phase 9 open

| Item | Count / value |
|---|---|
| Active terms | 81 |
| Active sub-groups | **8** (M01-A · M01-B · M01-C · M01-D · M01-E · M01-F · M01-G · M01-BOUNDARY) |
| Active VCGs | **36** (Phase 7-designed, Phase 8-confirmed sole active phenomenology) |
| Active is_relevant verses (routed) | 941 |
| Anchors (definitional verses) | 89 (36 AI-designated VCG anchors + 53 provisional per-term anchors per R4 fallback) |
| Set-asides (is_relevant=0) | 81 (76 inherited + 1 Act 7:11 + 4 from Phase 7) |
| `cluster.status` | `Analysis - In Progress` |

**Phases 1–8 complete.** Phase 9 produces the consolidated findings document that Phase 11 loads to `cluster_finding`.

---

## Your task per v2_0 §12

Answer every prompt in the **T0–T7 catalogue (189 prompts, v2.1)** at:

- **Each active sub-group scope** (M01-A through M01-G; M01-BOUNDARY uses structural characterisation only — see §"Special handling" below)
- **Cluster scope** (`[CLUSTER]` synthesis across the whole cluster)

Per prompt × scope cell, author one of:

- **E** — evidenced finding. Name the verses or VCGs that support it.
- **S** — silent. Describe what the silence means.
- **G** — gap. Describe what data is missing.

Every E must cite specific verse references or VCG codes. The test is not "does this sound right?" but **"can I name the specific verse or group that evidences this?"** (§2.4)

---

## Inputs

### Primary analytical input (the data you ground every finding in)

[Sessions/Session_Clusters/M01/wa-cluster-M01-vcg-grouped-v1-20260516.md](wa-cluster-M01-vcg-grouped-v1-20260516.md) — VCG-grouped report. Per-sub-group → per-VCG → every member verse with reference, term, and Phase 2 meaning. Anchors flagged ⚓; dual-membership flagged ⇄. **This is the only verse-level analytical material you use for Phase 9.**

### Mandatory input for T7 prompts

[Workflow/Sciences/wa-m01-fear-scienceextract-v1_1-20260513.md](../../../Workflow/Sciences/wa-m01-fear-scienceextract-v1_1-20260513.md) — per-cluster science extract. Required for T7 (Evidential and Methodological Foundation) prompts. **Note:** the extract was produced under v1_13 methodology before some terms were moved out of M01. Researcher confirms the extract remains valid for Phase 9 use.

### Catalogue (the 189 prompts)

[Workflow/Tiers/wa-obs-catalogue-tiered-v2_1-20260513.md](../../../Workflow/Tiers/wa-obs-catalogue-tiered-v2_1-20260513.md) — the T0–T7 tier catalogue, v2.1.

### Governing instruction

[Workflow/Instructions/wa-sessionb-cluster-instruction-v2_0-20260515.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_0-20260515.md) — §12 in particular.

---

## Decisions already made — do NOT re-debate

1. **Sub-group structure (8 sub-groups)** is final. Don't propose renaming, merging, or splitting. If a verse seems to fit a different sub-group than where it's routed, that's a Phase 9 cross-routing observation worth noting — but findings are authored against the current routing.
2. **VCG structure (36 VCGs)** is final. Don't propose adding, merging, splitting, or re-anchoring VCGs. The VCG design is the verdict of Phase 7; any unease can be noted as a researcher-decision item in the body of your finding, not as a structural change request.
3. **Anchors (89 total)** are set. 36 were AI-designated as the most definitional verse per VCG; 53 are CC-set per the R4 fallback rule (first canonical is_relevant verse per anchorless term). The 53 provisional anchors will be revisited at Phase 12 closure; don't fight them now.
4. **Term-to-sub-group placements** (81 primary + 25 secondary including BOUNDARY) are final.
5. **Set-asides (81)** are final — those verses are out of scope for the human-inner-being programme. Don't try to incorporate them.

---

## Special handling

### 1. M01-BOUNDARY sub-group (12 terms, 18 verses, 1 placeholder VCG)

The BOUNDARY sub-group holds terms whose inclusion in M01 is provisionally suspended pending researcher review at Phase 12. **For Phase 9, treat M01-BOUNDARY differently:**

- Do **not** do a full T0–T7 pass on M01-BOUNDARY as a regular sub-group.
- Instead, produce **per-term structural characterisation** notes (per §12.4 marker `**[BOUNDARY — H1234 translit]**`) describing for each BOUNDARY term what its inner-being content is (or isn't) — enough to support Phase 12 researcher decision on retain-in-M01 / transfer-to-another-cluster / set-aside.
- A few cross-cutting BOUNDARY notes can use `**[BOUNDARY]**` (no term suffix) if the observation applies across multiple BOUNDARY terms.

### 2. Dual-membership flagged verses (32 verses, marked ⇄ in grouped report)

Some verses' meanings straddle two VCGs (e.g. a verse evidencing both reverential fear and acute fear). The grouped report routes each to its primary VCG, with secondary VCG(s) recorded in DB notes. **For Phase 9:** cite a dual-membership verse under either VCG when authoring a finding — both are analytically defensible. Note the dual-membership in your finding body if relevant.

### 3. Cross-cluster term transfers (informational)

Phase 4 transferred 13 terms from M01 to other clusters (M02 Anger, M03 Anxiety/Distress, M10 Guilt, M24 Astonishment, etc.) where their meaning fit better. **For Phase 9:** the science extract was authored before this transfer; you may notice the extract discusses words that are no longer in M01. **Ignore those parts** of the extract — they don't apply to your Phase 9 findings. Only ground in the meanings present in the grouped report.

### 4. R4 provisional anchors (53)

Many VCGs have only one AI-designated anchor (the most-definitional verse) but span multiple terms. Per the R4 rule (every term with relevant verses must have ≥1 anchor), CC designated the first canonical-order verse per anchorless term as a provisional anchor. These are marked ⚓ in the grouped report alongside AI-designated anchors. **For Phase 9, treat all ⚓ verses as anchors regardless of provenance.**

---

## Output expected from you

### 1. Consolidated findings document, structured into 4 parts by tier

Per v2_0 §12.5:

- `Sessions/Session_Clusters/M01/WA-M01-consolidated-findings-v1-20260516-part1.md` — **T0–T1** (12 + 24 = 36 prompts)
- `WA-M01-consolidated-findings-v1-20260516-part2-T2.md` — **T2** (31 prompts)
- `WA-M01-consolidated-findings-v1-20260516-part3-T3-T4.md` — **T3 + T4** (33 + 24 = 57 prompts)
- `WA-M01-consolidated-findings-v1-20260516-part4-T5-T7.md` — **T5–T7** (21 + 24 + 20 = 65 prompts)

### ⚠️ STAGED WRITE-OUT — mandatory

**Write each part to disk the moment that part is complete. Do NOT hold all four parts in memory and write them at the end.**

Process:

1. Complete part 1 (T0–T1, 36 prompts × scope cells).
2. **Write part 1 to file immediately.** Confirm the file exists on disk before continuing.
3. Complete part 2 (T2, 31 prompts × scope cells).
4. **Write part 2 to file immediately.** Confirm.
5. Repeat for parts 3 and 4.

Why this matters: prior cluster runs have shown AI fighting context window pressure when carrying large analytical output across many prompts. Staging the write-out clears working context between parts and produces durable artefacts even if a later part needs to be re-attempted. The cross-sub-group review pass (§"Cross-sub-group review pass" below) happens **after** part 4 is written, by re-reading the four on-disk files — not by re-reading in-memory output.

If you find yourself near a context limit mid-part, prefer writing what you have for that part and asking CC for a continuation, rather than truncating or compressing other parts.

### 2. Authoring discipline (parser-safe form — §12.4)

The Phase 11 loader parses these documents — **do not deviate from format**:

1. **One scope marker per line.** Each `**[scope]**` marker starts at the beginning of a line.
2. **Every prompt must carry at least one explicit scope marker.** Forbidden: writing a brief cluster-wide statement under the prompt header without any `**[...]**` marker.
3. **One block per (prompt × scope).** Each (prompt, scope) cell appears at most once.
4. **Block separator.** A horizontal rule `---` on its own line marks the end of one prompt's findings.

#### Marker catalogue (recognised by the loader)

| Marker | Meaning |
|---|---|
| `**[A]**` or `**[A — Label]**` | finding for sub-group M01-A (similarly B–G) |
| `**[A, B, C]**` (comma-separated) | finding shared across listed sub-groups; loader expands to one row per letter |
| `**[CLUSTER]**` or `**[CLUSTER — all sub-groups]**` | cluster-level synthesis |
| `**[BOUNDARY — H1234 translit]**` | per-term structural characterisation for a BOUNDARY term |

#### Inline outcome codes (inside the scope marker's body)

- Body starts `E — text` or has no leading code → `finding` (or `cluster_synthesis` if scope is CLUSTER)
- Body starts `S — text` → `silent`
- Body starts `G — text` → `gap`

#### Authoring example

```markdown
### T1.1.1 — What is the inner-being content of this characteristic?

**[A]** E — In M01-A the inner-being content is fear-of-God as enduring orientation: the disposition that
governs the whole inner life (Pro 1:7 anchor; M01-A-VCG-02 Pro 1:7, 9:10, 15:33; Deu 6:2; Job 1:1).
This is not a reactive emotion but a settled posture that shapes conduct, worship, and identity.

**[B]** E — In M01-B the inner-being content is acute fear in response to immediate threat or
encounter (Gen 28:17 anchor; M01-B-VCG-01 cluster on theophanic encounter; M01-B-VCG-03 on enemy
threat). Distinct from M01-A reverential register: this is involuntary, situation-evoked.

**[C]** S — M01-C terror has no separate "what is the inner-being content" finding because the
sub-group's content IS the terror itself; T1.2 covers the further qualification.

...

**[CLUSTER]** E — Across M01 the inner-being content is fear in its full register: from acute startle
(M01-B) to enduring reverential orientation (M01-A), with overwhelming-force (M01-C), inner-collapse
(M01-D), somatic trembling (M01-E), anticipatory dread (M01-F), and timid shrinking (M01-G) marking
distinct phenomenological zones within the same characteristic.

---
```

### 3. Self-contained requirement

Each of parts 1–4 must be readable without reference to any other file:

- Every prompt answered with full text per scope — not structural labels or cross-references like "see [B]".
- Every E response includes specific verse reference(s) or VCG code(s) in the body.
- A Session C reader should be able to write the cluster publication using only these four parts.

### 4. Cross-sub-group review pass

After all sub-group passes are complete, read across the full set of findings before writing the cluster-level entries. Look for:

- **Cluster-level patterns** — findings that appear in the same form across all/most sub-groups → record once as `[CLUSTER]`.
- **Structural relationships** between sub-groups — causal sequences, constitutive relationships, asymmetries (especially relevant for T6 prompts).
- **Absences significant in totality** — a prompt silent across all sub-groups is a cluster-level finding.
- **Internal contradictions** — resolve by returning to verse evidence before producing the part 4 document.

Findings surfaced here are added at their relevant prompt location (not appended as an addendum).

---

## Discipline reminders

1. **Verse-grounded only.** Output that reads smoothly and is well-structured can still be entirely ungrounded. The test is not "does this sound right?" but "can I name the specific verse or VCG that evidences this?" If no verse can be named, mark **S** or **G**.

2. **Use the grouped report, not memory.** The grouped report is your data. Do not write findings from general theological knowledge of the Hebrew or Greek words. Cite from the 941 verses we routed.

3. **Anchors are weighted evidence, but not the only evidence.** Anchors are the single most-definitional verse per VCG (or per term, for provisional anchors). For a prompt, the supporting evidence includes the anchor plus the wider VCG; cite both.

4. **Don't fight Phase 7 decisions.** If a VCG feels misnamed or a verse seems mis-routed, note your concern in the body of the finding but author the finding against the current structure. Researcher reviews structural change requests at Phase 12.

5. **Output to new files, not in-place edits.** Produce the 4-part v1 documents per the filenames in §"Output expected", not in-place modifications.

6. **Stage the write-out — one part to disk before starting the next.** Each part (1, 2, 3, 4) must be written to its own file the moment it is complete. Do not accumulate parts in working context and write them at the end. Memory pressure across 189 prompts × multiple scopes has caused prior runs to truncate or compress later output. Staging the write-out clears context between parts and produces durable artefacts.

7. **Citation discipline.** Cite verses by reference (e.g. `Pro 1:7`) and VCGs by their `group_code` (e.g. `M01-A-VCG-02`). Don't cite by vc_id or by inherited VCG ids (those are gone).

8. **Science extract caveat.** The science extract (v1_1) was authored before some terms moved out of M01. Use it for T7 prompts — but ignore content discussing terms not present in your grouped report.

---

## Output naming summary

Per v2_0 §12.5, these four files together compose the Phase 9 consolidated findings:

```
Sessions/Session_Clusters/M01/
  WA-M01-consolidated-findings-v1-20260516-part1.md         (T0–T1)
  WA-M01-consolidated-findings-v1-20260516-part2-T2.md      (T2)
  WA-M01-consolidated-findings-v1-20260516-part3-T3-T4.md   (T3 + T4)
  WA-M01-consolidated-findings-v1-20260516-part4-T5-T7.md   (T5 + T6 + T7)
```

---

## When you're done

CC will:

1. Parse the four consolidated-findings parts against the catalogue (validates: 189 prompts × scope cells, parser format, anchor citation discipline).
2. Generate the **inherited-findings carry-over report** (Phase 10 input) — every unresolved Session B finding, SD pointer, and research flag attached to the cluster's contributor registries.
3. Bring Phase 10 brief to you for inherited-finding reconciliation (per-row disposition).
4. Phase 11: load consolidated findings into `cluster_finding`.
5. Phase 12: cluster closure + status flip to `Analysis Completed`.

---

## Provenance

- VCG-grouped report (primary input): [wa-cluster-M01-vcg-grouped-v1-20260516.md](wa-cluster-M01-vcg-grouped-v1-20260516.md)
- Science extract: [wa-m01-fear-scienceextract-v1_1-20260513.md](../../../Workflow/Sciences/wa-m01-fear-scienceextract-v1_1-20260513.md)
- Tier catalogue: [wa-obs-catalogue-tiered-v2_1-20260513.md](../../../Workflow/Tiers/wa-obs-catalogue-tiered-v2_1-20260513.md)
- Phase 7 applied (VCG creation): [WA-M01-dir-003-vcg-creation-applied-v1-20260516.md](WA-M01-dir-003-vcg-creation-applied-v1-20260516.md)
- Phase 8 applied (dissolution): [WA-M01-dir-004-vcg-dissolve-applied-v1-20260516.md](WA-M01-dir-004-vcg-dissolve-applied-v1-20260516.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_0-20260515.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_0-20260515.md)

---

*End of Phase 9 brief.*
