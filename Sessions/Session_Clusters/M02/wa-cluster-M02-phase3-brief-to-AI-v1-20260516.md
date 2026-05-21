# M02 Phase 3 brief — Cluster constitution debate

**Audience:** Claude AI
**Governing instruction:** [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) §6 (Phase 3)
**Date:** 2026-05-16

---

## State of M02 at Phase 3 open

| Item | Count / value |
|---|---|
| Active terms | **47** (Hebrew + Greek) |
| Contributor registries | 12 |
| Active is_relevant verses | **671** (all with Phase 2 meanings) |
| Set-asides (is_relevant=0) | 56 |
| `verse_context.analysis_note` coverage | 671/671 (100%) |
| `cluster.status` | `Data - In Progress` (just transitioned by report generator per v2_2 §6.1) |
| Inherited VCGs (suppressed) | 73 |

Phases 1 (UT review) and 2 (Pass A meaning record) complete. Each term in the cluster now has its per-verse meaning corpus in the database. Phase 3 uses that corpus as analytical input.

---

## Your task per v2_2 §6

For each of the 47 terms in the constitution report's §2:

1. **Read the meaning corpus** (every is_relevant verse + its Phase 2 meaning, in canonical Bible order).
2. **Render a verdict:**
   - **STAYS** — the term's meaning corpus aligns with M02's characteristic (anger / wrath / indignation / jealousy / provocation / dispute / vexation).
   - **TRANSFERS-TO-{cluster}** — the term's corpus aligns with another cluster's characteristic. Name the destination cluster from §4 (e.g. `TRANSFERS-TO-M28-Envy`, `TRANSFERS-TO-M03-Grief`).
   - **BOUNDARY** — the corpus is supportive, qualifying, or undecided. The term is held in `M01-BOUNDARY`-style for researcher decision at closure.
3. **Record the rationale in the obslog**, rooted in *specific meanings from the corpus* (not gloss-list inference).

---

## Inputs

### Primary analytical input

[Sessions/Session_Clusters/M02/wa-cluster-M02-constitution-v1-20260516.md](wa-cluster-M02-constitution-v1-20260516.md) — the constitution report. **This is the only material you need for Phase 3.** It contains:

- §1 — Cluster characteristic statement + gloss list
- §2 — Per-term identity + meaning corpus for all 47 terms (Pass A verse meanings)
- §3 — Cross-term signals (Jaccard meaning-vocabulary overlap; this cluster shows no strong overlap pairs above threshold 0.30 — meanings are highly term-specific)
- §4 — Programme cluster catalogue (43 other M-clusters with status)

### Governing instruction

[Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md) — §6 in particular.

### Note

The constitution report header references `v2_0` of the instruction (template string). The active instruction is **v2_2** — same §6 process, with v2_1 / v2_2 refinements to later phases (no Phase 3 logic change).

---

## Suppressed by design (per v2_2 §2.3)

These are **not** in your input and **must not** influence your verdicts:

- Inherited VCGs (73 exist, will be dissolved at Phase 8 after researcher review).
- Sub-group structure (none yet — formed at Phase 5 *after* this debate).
- Anchor designations (Phase 1 provisional anchors are placeholders, not analytical claims).
- Prior Session B findings (24 reconciled in Phase 10, not Phase 3 input).

If you find yourself wanting to validate a verdict against any of these, the answer is in the verse meanings — not in the legacy structure.

---

## Special handling for M02

### 1. Multiple contributor registries — many TRANSFER candidates likely

M02's 47 active terms come from **12 owning registries**:

| Registry | Term count | Likely fit |
|---|---:|---|
| R4 anger | 20 | Core M02 |
| R56 envy | 5 | Some core (jealousy as anger), some M28 Envy |
| R152 strife | 5 | Likely STAYS (strife as anger-driven contention) |
| R51 distress | 4 | Possibly TRANSFER to M03/M24 if corpus is distress-not-anger |
| R178 wrath | 4 | Core M02 |
| R3 ambition / R87 indignation / R1 abomination / R71 grief / R103 love / R123 pride / R128 rebellion | 1–2 each | Each term needs its own corpus reading |

**The cross-registry origin is not evidence of misfit.** Many cross-listed terms are legitimate M02 members — anger vocabulary leaks across registries because anger touches grief, strife, envy, and wrath simultaneously. Judge from the corpus, not the source registry.

### 2. Jealousy (qa.na / qin.ah / qan.na / qan.no)

Hebrew jealousy vocabulary has two registers:
- **Divine zeal** — God's jealousy *for* his people, *for* his name's honor (Exo 20:5; Num 25:11; Deu 32:21) — a protective, possessive fury that is righteous and anger-adjacent.
- **Human envy** — possessive jealousy that competes with another (Pro 27:4; Eccl 4:4) — closer to M28 Envy.

These may STAY (if dominantly anger-adjacent in their corpus) or split — note in the rationale if a single term's corpus shows both registers, and let researcher decide. Default to STAYS for the term as a whole if anger-adjacent meanings dominate.

### 3. *riv* (H7379, strife/dispute/legal-controversy)

Phase 1 set aside 12 of 15 UT verses for riv as legal/judicial dispute context (not anger-driven). The remaining is_relevant corpus for riv may be small. If the relevant corpus genuinely shows anger-driven contention, STAYS. If it's largely legal-procedural without inner anger heat, BOUNDARY or TRANSFER may be warranted — but check the verses, not the assumption.

### 4. *tsur* (H6696B) — already entirely set-aside in Phase 1

All 28 UT verses for *tsur* (provoke/besiege sense in this Strong's) were set-aside as the rock/cliff homonym. The term has no active is_relevant verses. Per v2_2, terms with no active relevant corpus need a verdict: **STAYS with note "no active relevant corpus after Phase 1"** is acceptable; researcher may set-aside the term entirely at Phase 4 if you prefer.

### 5. Strong's homonyms — multiple terms with same transliteration

The constitution report's §2 has:
- za.am (H2194 verb + H2195 noun) — two separate Strong's entries
- za.aph (H2196 verb + H2197 noun)
- che.ma (H2528) + che.mah (H2534)
- ka.as (verb) + ka.a.s (noun)

These are distinct terms with distinct corpora. Render a verdict per Strong's, not per transliteration.

---

## Decisions already made — do NOT re-debate

1. **The 47 terms are M02's term universe**. Phase 1 (UT review) finalised which verses are is_relevant. Don't try to re-classify verses.
2. **The 56 set-asides are out of scope** (Phase 1 outcome). Don't try to incorporate them.
3. **Provisional anchors from Phase 1** are placeholders; Phase 7 may move them. Ignore anchor info if you happen to see it.

---

## Output expected from you

### 1. Constitution debate document

`Sessions/Session_Clusters/M02/wa-cluster-M02-debate-v1-20260516.md`

Format (one block per term, in the order they appear in §2):

```markdown
### {strongs} {transliteration} — {gloss}

**Verdict:** STAYS  (or TRANSFERS-TO-M28-Envy, or BOUNDARY)
**Rationale:** Reading the meaning corpus, this term names anger-driven inner heat
(Exo 32:19 — Moses' anger kindled; Num 25:3 — divine wrath against Baal of Peor;
2Sa 6:7 — God's anger against Uzzah). The inner-being content is uniformly
M02-register: kindling, burning, eruption against offense. STAYS.

---
```

For TRANSFERS-TO-{cluster}, name the destination cluster code + short name from §4 (e.g. `TRANSFERS-TO-M28-Envy`). For BOUNDARY, briefly note what makes the term ambiguous (mixed register, thin corpus, edge case).

### 2. Obslog entries

Each verdict gets a brief obslog entry. Standard obslog file: `wa-obslog-M02-constitution-v1-20260516.md`.

### 3. Cross-routing flags document (if any surfaced)

`Sessions/Session_Clusters/M02/WA-M02-phase3-cross-routing-flags-v1-20260516.md` — if you notice during the debate that a verse seems mis-routed to its current term (rare but possible), flag here. CC may apply small corrections alongside Phase 4.

---

## Discipline reminders

1. **Verdict from the meaning corpus only.** Read each verse meaning. Decide. The gloss list in §1 is for orientation, not verdict-driving.
2. **No gloss-list inference.** "qa.na means jealousy, jealousy is envy, therefore TRANSFER to M28" is gloss-list reasoning. The Hebrew jealousy corpus may evidence God-as-subject anger-zeal — that's M02 territory. Read the verses.
3. **Don't compare to inherited VCGs.** They're suppressed precisely because they bias the verdict.
4. **STAYS is the default for borderline cases** where the corpus is genuinely ambiguous between M02 and another cluster — use BOUNDARY when there's a real edge case, TRANSFER only when the corpus clearly fits another cluster's characteristic.
5. **Set-aside is NOT a Phase 3 verdict.** Phase 1 already set verses aside. Phase 3 decides on terms, not verses.
6. **Output to new files, not in-place edits.** Produce v1 documents per the filenames above.

---

## When you're done

CC will:

1. Parse your debate document for verdicts (STAYS / TRANSFERS-TO-{code} / BOUNDARY).
2. Validate that every term in the constitution report has a verdict.
3. Apply Phase 4 (term transfers + BOUNDARY designation) — TRANSFERS terms get their `mti_terms.cluster_code` updated; BOUNDARY terms get placed in `M02-BOUNDARY` sub-group at Phase 6.
4. Generate Phase 5 input (sub-group design report) for AI's next chat involvement.

---

## Provenance

- Constitution report (primary input): [wa-cluster-M02-constitution-v1-20260516.md](wa-cluster-M02-constitution-v1-20260516.md)
- Phase 1 applied: [WA-M02-UT-verse-review-api-v1-20260516.md](WA-M02-UT-verse-review-api-v1-20260516.md)
- Phase 2 applied: [WA-M02-passa-meanings-applied-v1-20260516.md](WA-M02-passa-meanings-applied-v1-20260516.md)
- Governing instruction: [wa-sessionb-cluster-instruction-v2_2-20260516.md](../../../Workflow/Instructions/wa-sessionb-cluster-instruction-v2_2-20260516.md)

---

*End of Phase 3 brief.*
