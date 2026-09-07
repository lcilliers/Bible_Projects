# M03 Phase 3 brief — Cluster constitution debate

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §6 (Phase 3)
**Date:** 2026-05-16

---

## State of M03 at Phase 3 open

| Item | Count / value |
|---|---|
| Active terms | **89** (Hebrew + Greek) |
| Contributor registries | 16 |
| Active is_relevant verses | **759** (all with Phase 2 meanings except 11 gaps — see §"Special handling") |
| Set-asides (is_relevant=0) | 326 |
| `verse_context.analysis_note` coverage | 748 / 759 (98.5%) |
| `cluster.status` | `Data - In Progress` (just transitioned by report generator per v2_2 §6.1) |
| Inherited VCGs (suppressed) | 114 |

Phases 1 (UT review) and 2 (Pass A meaning record) complete. The per-term meaning corpora are now in the database. Phase 3 uses that corpus as analytical input.

---

## Your task per v2_2 §6

For each of the 89 terms in the constitution report's §2:

1. **Read the meaning corpus** (every is_relevant verse + its Phase 2 meaning, in canonical Bible order).
2. **Render a verdict:**
   - **STAYS** — the term's meaning corpus aligns with M03's characteristic (grief / sorrow / lament / mourning / anguish / bitterness / weeping / groaning).
   - **TRANSFERS-TO-{cluster}** — the term's corpus aligns with another cluster's characteristic. Name the destination from §4.
   - **BOUNDARY** — the corpus is supportive, qualifying, mixed-register, or undecided. The term is held in M03-BOUNDARY for researcher decision at Phase 12.
3. **Record the rationale in the obslog**, rooted in *specific meanings from the corpus*.

---

## Inputs

### Primary analytical input

[Sessions/Session_Clusters/M03/wa-cluster-M03-constitution-v1-20260516.md](wa-cluster-M03-constitution-v1-20260516.md) — the constitution report. Per-term identity + meaning corpus for all 89 terms. **This is the only material you need for Phase 3.**

### Governing instruction

[Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) — §6 in particular.

### Note

The constitution report header references `v2_0` of the instruction (template string). The active instruction is **v2_2** — same §6 process for Phase 3.

---

## Suppressed by design (per v2_2 §2.3)

These are **not** in your input and **must not** influence your verdicts:

- Inherited VCGs (114 exist; dissolved at Phase 8 after researcher review)
- Sub-group structure (none yet — formed at Phase 5)
- Anchor designations (Phase 1 provisional anchors are placeholders)
- Prior Session B findings

If you find yourself wanting to validate a verdict against any of these, the answer is in the verse meanings — not in the legacy structure.

---

## Special handling for M03

### 1. Multiple contributor registries — many TRANSFER candidates likely

M03's 89 active terms come from **16 owning registries** — the most heterogeneous cluster yet. Distribution:

| Registry | Term count | Notes |
|---|---:|---|
| R5 anguish | 16 | Core M03 |
| R151 sorrow | 12 | Core M03 |
| R51 distress | 11 | Mixed — overlap with M03 distress sense + future Distress cluster |
| R71 grief | 10 | Core M03 |
| R2 agony | 7 | Likely core; some may be M24 Weakness if pure-physical |
| R13 bitterness | 7 | Mixed — bitterness-of-soul (M03) vs literal-bitter-taste (set-aside likely already done) |
| R113 mourning | 7 | Core M03 |
| R188 weeping | 7 | Core M03 |
| R72 groaning | 5 | Core M03 |
| R23 compassion, R30 contrition, R31 corruption, R86 impurity, R108 meditation, R131 rejection, R158 terror | 1 each | Edge — most likely TRANSFERS or BOUNDARY |

### 2. The 4 terms with no active relevant corpus (after Phase 1)

These had all UT verses set-aside in Phase 1:

| Strong's | Translit | Gloss | Source registry | Note |
|---|---|---|---|---|
| G0930 | basanistēs | torturer | R23 compassion | Literal torturer; not inner-grief register |
| H1795 | dak.kah | crushing | R2 agony | Physical-crushing register, not inner |
| H2254C | cha.val | be in labour | R72 groaning | Literal labour-pain (not metaphorical travail-grief) |
| H6735C | tsir | pang | R5 anguish | Physical pang/messenger, not inner anguish |

These typically get **STAYS with note "no active relevant corpus"** OR **TRANSFER** to another cluster. Render a verdict per the v2_2 §6.4 corpus-empty rule.

### 3. ka.as (vexation/grief) — anger vs sorrow register

`ka.as` Hebrew has dual register: it's used in **M02 anger** corpus (`H3707` ka.as verb = "provoke to anger", `H3708B` ka.a.s noun = "vexation"). If `ka.as` terms appear in M03's term set, they need careful corpus-reading — the M03 register would be vexation-as-sorrow rather than vexation-as-anger.

### 4. Bitterness register — M03 vs anger

Bitterness vocabulary (`pikros`, `pikria`, `mar`, `me.rir`, `mam.ror`) can describe:
- Inner soul-bitterness from sorrow (M03)
- Bitterness as anger-adjacent acrimony (potentially M02 Anger)
- Literal bitter taste / Passover bitter herbs (set-aside)

Phase 1 already set aside the literal-bitter cases. Distinguishing inner-sorrow-bitterness (STAYS) from anger-bitterness (TRANSFERS-TO-M02) is the judgement here.

### 5. Labor-pain imagery (ōdinō, cha.val, etc.)

Birth-pain words have dual register: literal labour pains (often set-aside) vs metaphorical inner travail (often M03 grief-anguish). Where the metaphorical reading dominates in the corpus, STAYS in M03. Where corpus is mixed, BOUNDARY may be appropriate.

### 6. Distress register split (R51 distress)

11 terms from R51 distress. Some will be M03 (grief-distress), some may be M24 Weakness (suffering-distress), some may be M02 Anger (vexation-distress). Multi-faceted register — read each term's corpus.

### 7. Single-term contributing registries (likely TRANSFER candidates)

- R23 compassion → if not M03, → future M05/M11 Compassion-Mercy or similar
- R30 contrition → if not M03, → future Repentance cluster
- R31 corruption → likely not M03 (corruption is M27 Evil register typically)
- R86 impurity → likely M27 Evil or M12 Purity (negative form)
- R108 meditation → likely future Meditation/Counsel cluster (M17)
- R131 rejection → likely future Hate or Rejection cluster
- R158 terror → already in M01 cluster (now closed) — likely TRANSFERS-TO-M01

These need verdicts but probably aren't core M03.

### 8. 11 verses without analysis_note (Phase 2 gaps)

3 verses dropped in Phase 2 JSON-edge cases + 8 pre-existing unwritten meanings = 11 verses lack analytical content. These are scattered across terms (not concentrated). When you encounter a term with a gap-verse in its corpus, judge the term's overall corpus from the meanings you can see; the gap-verses don't dominate any single term's verdict.

---

## Decisions already made — do NOT re-debate

1. **The 89 terms are M03's term universe.** Phase 1 finalised which verses are is_relevant.
2. **The 326 set-asides are out of scope.** Don't try to incorporate them.
3. **Provisional anchors from Phase 1** are placeholders; ignore.
4. **11 borderline verses from Phase 1** are held in the log, not in the DB. You won't see them.

---

## Output expected from you

### 1. Constitution debate document

`Sessions/Session_Clusters/M03/wa-cluster-M03-debate-v1-20260516.md`

Format (one block per term, in §2 order):

```markdown
### {strongs} {transliteration} — {gloss}

**Verdict:** STAYS  (or TRANSFERS-TO-M02-Anger, or BOUNDARY)
**Rationale:** Reading the meaning corpus, this term names ... (specific meanings cited).
The inner-being content is M03-register: grief / lament / etc.

---
```

For TRANSFERS-TO-{cluster}, name the destination cluster code + short name from the constitution report's §4 (e.g. `TRANSFERS-TO-M02-Anger`). For BOUNDARY, briefly note what makes the term ambiguous.

### 2. Obslog entries

Standard obslog file: `wa-obslog-M03-constitution-v1-20260516.md` (or append to the existing M03 obslog if one exists).

### 3. Cross-routing flags document (if any surfaced)

`Sessions/Session_Clusters/M03/WA-M03-phase3-cross-routing-flags-v1-20260516.md` — if you notice during the debate that a verse seems mis-routed to its current term, flag here.

---

## Discipline reminders

1. **Verdict from the meaning corpus only.** Read each verse meaning. Decide.
2. **No gloss-list inference.** A term's transliteration meaning ≠ its corpus verdict.
3. **Don't compare to inherited VCGs.** Suppressed by design.
4. **STAYS is the default for borderline.** Use BOUNDARY for genuine edge cases, TRANSFER only when the corpus clearly fits another cluster.
5. **Set-aside is NOT a Phase 3 verdict.** Phase 1 already set verses aside. Phase 3 decides on terms.
6. **Output to new files, not in-place edits.**

---

## When you're done

CC will:

1. Parse your debate document for verdicts.
2. Validate that every term has a verdict.
3. Apply Phase 4 (term transfers + BOUNDARY designation).
4. Generate Phase 5 input (sub-group design report) for your next chat involvement.

---

## Provenance

- Constitution report (primary input): [wa-cluster-M03-constitution-v1-20260516.md](wa-cluster-M03-constitution-v1-20260516.md)
- Phase 1 applied: [WA-M03-UT-verse-review-api-v1-20260516.md](WA-M03-UT-verse-review-api-v1-20260516.md)
- Phase 2 applied: [WA-M03-passa-meanings-applied-v1-20260516.md](WA-M03-passa-meanings-applied-v1-20260516.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md)
- M01 closed: precedent for closure pattern
- M02 closed: precedent + validated methodology
- Validation methodology: [Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md](../../../Workflow/methodology/WA-blind-verification-methodology-v1-20260516.md)

---

*End of Phase 3 brief.*
