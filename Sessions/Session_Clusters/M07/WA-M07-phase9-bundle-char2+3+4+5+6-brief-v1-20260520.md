# M07 Phase 9 — Bundle (char2+3+4+5+6) — brief

**Cluster:** M07 — Shame, Disgrace and Humiliation
**Characteristics in this bundle:** 2 (Humiliation as enforced abasement), 3 (Dishonour as relational worth-denial), 4 (Shamefulness as moral-evaluative judgment), 5 (Shame produced by contempt and rejection), 6 (Innocence as structural counter to shame)
**Total verses across the bundle:** ~135
**Total prompts to author:** 945 (= 189 × 5 separate passes)
**Task date:** 2026-05-20
**Audience:** Claude AI session

**Read this brief first.** Structural input is in a separate file referenced below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M07/WA-M07-phase9-bundle-char2+3+4+5+6-brief-v1-20260520.md` | Primary task instructions |
| 2 | **Structural input** — `Sessions/Session_Clusters/M07/WA-M07-phase9-bundle-char2+3+4+5+6-input-v1-20260520.md` | Per-characteristic data blocks + shared 189-prompt catalogue + carry-forward observations |
| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_5-20260518.md` | §12 Phase 9 disciplines; §12.4 parser-safe form |
| 4 | **Science extract** — `Workflow/Sciences/wa-m07-shame-scienceextract-v1_0-20260513.md` | Programme-curated scientific lens for T7.3 (human science framework) prompts — ensures consistent framing across clusters and reviewers |
| 5 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260506.md` Ch.1 'Defining Inner Being' | Inner-being scope definition (background) |
| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

> The full 189-prompt T0–T7 catalogue is reproduced inside the structural input. No separate catalogue file required.

---

## Why this is a bundle (not a single characteristic)

This package covers **multiple characteristics** to save on session setup overhead. The data for each characteristic is kept distinct in the structural input — sub-groups, VCGs, and verses are grouped under their own characteristic block (§2.A, §2.B, …). **Do not pool evidence across characteristics.** Each 189-prompt pass uses ONLY that characteristic's evidence.

> Per researcher direction 2026-05-19: *"you can combine more than one characteristic in the dataset, but keep the grouping of the sub group distinctly separate into characteristics, and be clear in the guide to do separate batches of going through the catalogue."*

---

## How to work this bundle — separate batches

You will do **5 separate 189-prompt batches**, one per characteristic, in the order listed below. Each batch is fully bounded to its own characteristic — do not reuse another characteristic's evidence within a batch.

| Batch | Characteristic | Sub-groups | Verses | Output file (you produce) |
|---|---|---|---:|---|
| 2 | Humiliation as enforced abasement | M07-D | ~72 | `Sessions/Session_Clusters/M07/WA-M07-phase9-char2-Humiliation-as-enforced-abasement-findings-v1-20260520.md` |
| 3 | Dishonour as relational worth-denial | M07-E | ~15 | `Sessions/Session_Clusters/M07/WA-M07-phase9-char3-Dishonour-as-relational-worth-denial-findings-v1-20260520.md` |
| 4 | Shamefulness as moral-evaluative judgment | M07-F | ~16 | `Sessions/Session_Clusters/M07/WA-M07-phase9-char4-Shamefulness-as-moral-evaluative-judgment-findings-v1-20260520.md` |
| 5 | Shame produced by contempt and rejection | M07-G | ~24 | `Sessions/Session_Clusters/M07/WA-M07-phase9-char5-Shame-produced-by-contempt-and-rejection-findings-v1-20260520.md` |
| 6 | Innocence as structural counter to shame | M07-H | ~8 | `Sessions/Session_Clusters/M07/WA-M07-phase9-char6-Innocence-as-structural-counter-to-shame-findings-v1-20260520.md` |

Complete each batch fully (189 prompts + self-check) and check it against the discipline list BEFORE moving to the next batch. Each output is a standalone findings file.

---

## Output format (applies to every batch)

Per prompt, one block; parser-safe form per v2_5 §12.4:

```
**T#.#.# — question text excerpt (optional)**

**[CHAR-N]** E — Finding text. Cite specific verses / VCGs / sub-groups from the characteristic's evidence block. Quote verse phrases that evidence the answer. The finding must be self-contained for a Session C reader.

---
```

**Scope marker** is `**[CHAR-N]**` where **N is the characteristic number for that batch** (e.g., `**[CHAR-3]**` for the Gladness batch, `**[CHAR-7]**` for the Suffering-Joy batch). CC's loader uses this to set characteristic_id on each row, so it MUST match the current batch's characteristic.

**Outcome codes:**
- **E** — evidenced; cite specific verses / VCGs
- **S** — silent; describe the analytical significance of the absence
- **G** — gap; describe what data would be needed to answer

---

## Discipline (per v2_5 §12)

1. **Read every verse-meaning in the structural input for the current batch.** No sampling. The Pass A meanings condense each verse's inner-being content — read them all for the batch's characteristic.
2. **Per prompt, ground in specific evidence.** Every E finding names verses, VCGs, or sub-groups. The test for a good answer is *can I name what evidences this?*
3. **Fluency is not a quality signal** (v2_5 §2.4). Plausible-sounding text without specific citations is rejected.
4. **No sub-group-scope findings.** All findings at characteristic scope. Where evidence differs by sub-group within a characteristic, the finding text names the sub-group(s) inline.
5. **No cross-characteristic mixing.** Evidence from another characteristic's block is OFF-LIMITS for the current batch. If a cross-characteristic observation is significant, note it in the Self-check for that batch — do NOT embed cross-batch findings.
6. **No cluster-scope findings.** Cluster synthesis runs after all 7 characteristics finish.
7. **Self-check before submitting each batch** — confirm 189 prompts have rows; confirm every E names evidence; confirm the `[CHAR-N]` marker matches the batch.

---

## Carry-forward observations (apply per-batch)

These analytical hints were raised at characteristic-mapping time. Two statuses are shown: **OPEN** means action and flag at end of batch; **CONFIRMED** means already validated by an earlier Phase 9 batch — included here as context that may matter for the current batch's evidence selection.

### For Characteristic 5 (Shame produced by contempt and rejection)

**INTER_RELATIONSHIP — M07-G shame ↔ M06 contempt as relational complements** — **OPEN**

> Phase 3 v2 cross-register analysis (per v2_7 §6.3.2 verse-level relationship test) confirmed the M07-G sub-group holds the shame-recipient face of a contempt-shame dynamic whose source-side (contempt-projection) lives in M06. Every verse in M07-G's 24-verse corpus (especially the 11 exoutheneō verses) evidences contempt as the active mechanism producing shame in the recipient. The two characteristics are relational complements: M06 contempt produces; M07-G shame receives. Phase 9 T6 (Structural Relationships with Other Characteristics) should make this M06 ↔ M07 relationship explicit; M06's eventual Phase 9 will see the same dynamic from the contempt side.

At end of this batch, flag whether the observation surfaced as expected.

### For Characteristic 6 (Innocence as structural counter to shame)

**INTER_RELATIONSHIP — M07-H innocence ↔ M12 purity as structural counters to shame** — **OPEN**

> Phase 3 v2 cross-register analysis flagged niq.qa.von and qe.ha.von with M12 (purity/holiness) as the terms' primary register; they remain in M07 because every verse evidences the innocence-shame polarity directly (innocence as shield, innocence in tension with experienced shame, incapacity-for-innocence sustaining the shamed condition). Phase 9 T6 should articulate the M07 ↔ M12 cross-cluster relationship: innocence is the inner moral state that protects against guilt-shame; its absence sustains the condition shame names.

At end of this batch, flag whether the observation surfaced as expected.

---

## Self-check template (use at the end of EACH batch's findings file)

```markdown
## Self-check

- Prompts answered: 189 / 189 ✓
- E findings naming specific evidence: <count>
- S findings: <count>
- G findings: <count>
- Carry-forward observations addressed: <list>
- Unexpected analytical patterns surfaced: <list>
```

---

## After you finish each batch

1. Save the batch's findings to its own file (filename in the table above).
2. Ping CC: "M07 Char N (<name>) Phase 9 findings ready" — once per batch.
3. CC parses, validates, applies that file to cluster_finding with the right characteristic_id.
4. Begin the next batch.

If a batch is too large to fit in a single response, split it into segments by tier-pair (T0+T1, T2+T3, T4+T5, T6+T7) — same convention used for Char 2.

---

*End of brief. Load the structural input (#2) and begin Batch 1.*