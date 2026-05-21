# M07 Phase 3 — Cluster constitution debate — brief

**Date:** 2026-05-19
**Cluster:** M07 — Shame, Disgrace and Humiliation
**Phase:** 3 (Cluster constitution debate)
**Audience:** Claude AI session (chat)
**Governing instruction:** `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_6-20260519.md` §6

**Read this brief first.** The structural input is the constitution report referenced below.

---

## Required inputs

| # | Document | Purpose |
|---|---|---|
| 1 | **This brief** — `Sessions/Session_Clusters/M07/WA-M07-phase3-constitution-brief-v1-20260519.md` | Primary task instructions |
| 2 | **Constitution report** — `Sessions/Session_Clusters/M07/wa-cluster-M07-constitution-v1-20260519.md` | §1 cluster characteristic statement + §2 per-term meaning corpora (36 terms with all Pass A meanings) + §3 cross-term signals + §4 programme cluster catalogue |
| 3 | **Governing instruction** — `Workflow/Instructions/wa-sessionb-cluster-instruction-v2_6-20260519.md` §6 (Phase 3 disciplines, §6.3.1 disallowed BOUNDARY reasons) |
| 4 | **Science extract** — `Workflow/Sciences/wa-m07-shame-scienceextract-v1_0-20260513.md` | Programme-curated scientific framing of shame (for later phases; helpful background here) |
| 5 | **Programme prose** — `Workflow/Programme/programme_prose/wa-programme-prose-extract-{current}.md` Ch.1 'Defining Inner Being' | Inner-being scope definition; the §1.1 in-scope examples block determines what counts as inner-being content |
| 6 | **Global rules** — `wa-global-general-rules` [current] | Programme discipline |

---

## Context

This is M07's first AI-facing analytical session. The cluster currently holds **36 terms** drawn from 14 contributing word registries (shame, humility, contempt, slander, evil, corruption, impurity, rejection, innocence, peace, anointing, compassion, meaning, flesh). Pass A (Phase 2) has just authored a per-verse inner-being meaning for **527 of 530 is_relevant verses** — that meaning corpus is the **only analytical material** the constitution debate works from. **Inherited VCG, sub-group structure, anchor designations, and prior session findings are explicitly suppressed** (per v2_6 §2.3) so the verdicts come from the verse-evidence-meanings directly, not from prior structure.

---

## Your task — per-term verdict

For each of the **36 terms** in §2 of the constitution report, read the term's full meaning corpus and assign exactly one verdict:

| Verdict | Meaning |
|---|---|
| **STAYS** | The term's meaning corpus aligns with M07's characteristic (Shame, Disgrace and Humiliation). Term remains in M07. |
| **TRANSFERS-TO-{cluster_code}** | The term's meaning corpus aligns with a different cluster's characteristic. Name the target cluster code from §4 (e.g. `TRANSFERS-TO-M05` for love-coded content; `TRANSFERS-TO-M09` for humility content). |
| **BOUNDARY** | The term's meaning corpus is supportive, qualifying, or genuinely undecided. Hold for researcher review. Cite the analytical question + which §6.3.1 valid reason applies. |

Each verdict must:
1. Cite specific verses or meaning patterns from the term's corpus.
2. Be grounded in the inner-being content of the meanings — not the gloss alone.

---

## Disallowed BOUNDARY reasons (per v2_6 §6.3.1)

BOUNDARY may **NOT** be assigned solely because:

- The term's meaning corpus is predominantly horizontal (human-to-human) rather than vertical (God-directed).
- The meanings describe sensory / material / circumstantial inner-being rather than overtly spiritual inner-being.
- The meanings include corrupt, illicit, or morally-negative inner-being content.
- The meanings describe an inner-being state you would prefer not to be in scope.

Inner being is the entire human inner life — no theological narrowing.

## Valid BOUNDARY reasons (cite one of these three)

1. **Cluster-membership undecided** — the term's meaning corpus is genuinely on the borderline between this cluster's characteristic and another's; transfer destination is unclear; researcher decision needed.
2. **Homonymic / polysemic spread** — the term's meaning corpus covers two or more distinct registers and the term may need sense-split treatment before a cluster decision.
3. **Supportive / qualifying register** — the term's meanings describe a state that enhances or qualifies the cluster's characteristic without itself carrying it as a primary characteristic.

Every BOUNDARY verdict names the analytical question AND cites one of the three valid reasons. Verdicts citing the disallowed grounds (§6.3.1) are returned for revision at Phase 4 input parse.

---

## Specific signals to attend to (M07 pre-debate notes from CC)

The Pass A pass already surfaced two clear cases worth attention:

### A. Homonymic concern — H2616B / H2617B (`cha.sad` / `che.sed`)

These two Strong's IDs are listed as separate M07 terms. Hebrew has at least two distinct roots that share the consonants `ch-s-d`:

- One root carries **"loyal love / steadfast love / lovingkindness"** — the dominant biblical sense, primarily M05-Love content (e.g. Jer 9:24's *che.sed* in steadfast love).
- The other root carries **"shame / reproach"** — a narrow sense (e.g. Pro 14:34's *che.sed* as reproach to a people).

Pass A meanings will show which sense each term's verses actually carry. Use those meanings to decide whether the M07 listing should be retained (transfer to M05? sense-split needed? both?).

### B. Cross-register terms

Several M07 terms come from non-shame home registries (impurity, contempt, slander, rejection, etc.). Their meaning corpora will tell you whether the term's content actually evidences shame as inner state, or whether the term sits primarily in another cluster:

- `katatomē` (G2699 mutilation) — Php 3:2 reference; Pauline rhetoric about circumcision. Inner shame or polemic?
- `loidoria` (reviling) — speech act of shaming. Shame-cluster content or speech-cluster content?
- `exoutheneō` (to reject as worthless) — contempt-as-rejection. M07 or another?

Don't pre-commit verdicts on these — read each term's meanings and decide.

### C. Likely STAYS terms (do not need extensive justification)

The following are extremely likely to STAY (clear primary shame vocabulary):

- `aischunē`, `aischunō`, `epaischunomai` family (G0152, G0153, G0808, G0150)
- `bosh`, `bo.shet`, `bu.shah`, `bosh.nah` (H0954 + variants — the dominant OT shame root)
- `kataischunō`, `entrepō`, `entropē` (G2617, G1788, G1791 — NT shame-related verbs/nouns)
- `ka.lam`, `ke.lim.mah`, `ke.lim.mut` (H3637 + variants — humiliation root)
- `cha.pher` (H2659 — be ashamed)

A one-sentence verdict for each is sufficient.

---

## Output format

Produce a single markdown document with this structure:

```markdown
# M07 Phase 3 — Constitution debate — verdicts

**Date:** 2026-05-19
**Cluster:** M07 — Shame, Disgrace and Humiliation
**Terms evaluated:** 36 / 36

## Summary table

| mti_id | Strong's | Translit | Gloss | Verses | Verdict |
|---:|---|---|---|---:|---|
| 324 | G0152 | aischunē | shame | 6 | STAYS |
| ... | ... | ... | ... | ... | ... |

## Per-term verdicts

### G0152 aischunē — shame (mti_id=324) — STAYS

Rationale: <1-3 sentences citing specific verses/meanings from §2>

### H2616B cha.sad — to shame (mti_id=???) — TRANSFERS-TO-M05

Rationale: <1-3 sentences explaining why the corpus is che.sed-as-loyal-love, not shame, citing specific verses>

### {translit} — {gloss} — BOUNDARY

Analytical question: <what the researcher needs to decide>
Valid reason cited: <one of cluster-membership-undecided / homonymic-polysemic-spread / supportive-qualifying-register>
Rationale: <1-3 sentences>

...

## Decision summary

- STAYS: <count>
- TRANSFERS-TO-{cluster}: <count per target>
- BOUNDARY: <count>
- Total: 36

## Cross-term observations (optional)

Any patterns worth flagging for Phase 5 (sub-group formation) — terms whose meaning corpora cluster together, terms whose ranges differ markedly, vocabulary families operating in parallel, etc. Brief notes only.
```

---

## Discipline

1. **Read each term's full meaning corpus** (§2 of the constitution report) before assigning a verdict. No shortcuts from gloss or transliteration.
2. **Verdicts are grounded in meanings**, not in the term's general lexical sense.
3. **No sub-group / VCG framing.** Phases 5 (sub-group) and 7 (VCG) handle that downstream; constitution debate is term-level.
4. **TRANSFERS targets must be valid cluster codes** from §4 of the constitution report. If you suspect a transfer destination isn't named in §4, raise as BOUNDARY with that question.
5. **BOUNDARY must cite one of the three valid reasons** (§6.3.1). Verdicts citing disallowed grounds are returned.

---

## After you finish

1. Save the verdict document as `Sessions/Session_Clusters/M07/WA-M07-constitution-debate-v1-20260519.md`.
2. Ping CC: "M07 Phase 3 constitution debate verdicts ready".
3. CC validates and builds the Phase 4 directive (term-transfer + BOUNDARY application) per v2_6 §7.

---

*End of brief. Load the constitution report (#2) and begin.*
