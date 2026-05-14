# Session C — Cluster Publication Layer

## Framework B Soul Word Analysis Programme

**Status:** DRAFT v0_1 (2026-05-12)
**Test case:** M15 (Wisdom, Understanding and Knowledge)
**Governing instructions:**
- `wa-global-general-rules [current]`
- `wa-sessionb-cluster-instruction-v1_1-20260507.md` §2 operating principle (carried forward)
- `wa-directive-instruction [current]` (Session C produces no DB writes — instruction included only for context)

**Supersedes:** none. This is a new instruction. The legacy `wa-sessionc-instruction-v1_5-20260418.md` is the per-word-study Session C — it remains in force for word-scope publications and is not affected by this document.

**Foundation:** drawn from
- `outputs/markdown/tier-question-linkage-analysis-v1-20260507.md` (schema map)
- `outputs/markdown/cluster-finding-citation-model-design-v1-20260507.md` (deferred — citation table not yet implemented)

---

## 1. What this session is

Session C — Cluster Layer produces a **single reader-facing publication document for each completed cluster** — a coherent description of the cluster as a domain of inner-being, written for an intelligent non-specialist reader. It is the cluster equivalent of the per-word study: the same articulation discipline at a different scope.

It tells the story the cluster's verse evidence, sub-group structure, and findings collectively tell — what this inner-being domain *is*, how Scripture handles it, where its terms locate it constitutionally, what faculties it engages, what holds it together, and what bounds it. It draws directly from `cluster_finding` rows and from the supporting verse + VCG + sub-group + term inventory.

Session C produces no database writes. It is a publication layer.

---

## 2. Pipeline position

```
Session A         → per-word data extraction (JSON)
Session B (Cluster) → cluster analytical work: sub-groups, VCGs,
                      catalogue pass, cluster_finding population
Session C (Word)  → per-word publication layer (unchanged)
Session C (Cluster) → per-cluster publication layer (this instruction)
Session D         → cross-cluster synthesis (consumes Session C Cluster outputs)
```

A cluster reaches Session C Cluster only when it is at `cluster.status = 'Analysis Completed'`. M05, M06, M15 and M26 are the first four eligible clusters.

---

## 3. Operating principle (inherited)

> **Read every finding. Read every anchor verse. Read what they say. Let the structure of the report emerge from what the cluster's evidence shows. No assumptions from memory. No jumping to conclusions. Write on discovery.**
>
> Output that reads smoothly and is well-structured can still be entirely ungrounded. The test for every claim is not "does this sound right?" but **"which finding, which verse, which sub-group evidences this?"** If no specific item can be named, the claim does not belong in the publication.

The principle is identical to the cluster-instruction §2 principle that produced the findings in the first place. The fluency guard at Session C is the same guard that protected the findings.

**Cross-cluster contamination guard:** the document being written is about *this cluster*. Prior knowledge from other clusters may inform background framing but must not import claims unattested in this cluster's findings. A Session D synthesis layer (separate session) is where cross-cluster claims are made.

---

## 4. Inputs

For each cluster `M{NN}`, Session C Cluster reads:

| Source | Path | Purpose |
|---|---|---|
| Cluster identity | `cluster` table row | short_name, description, gloss (term list), status, version |
| Sub-group inventory | `cluster_subgroup` rows where `cluster_code=M{NN}` | label, core_description, term counts per sub-group |
| VCG inventory + anchors | `verse_context_group` + `verse_context` (`is_anchor=1`) joined via `vcg_term` | per-VCG context_description + anchor reference + anchor verse_text |
| Findings | `cluster_finding` rows where `cluster_code=M{NN}` | 1 row per (catalogue prompt × scope). Status: `finding` / `silent` / `gap` / `cluster_synthesis` |
| Catalogue | `wa_obs_question_catalogue` (T0–T7) | The 189 prompt definitions that framed the analytical work |
| Comprehensive | `wa-cluster-M{NN}-comprehensive-v{N}-{date}.md` | Reference; full per-term + verses background |
| Grouped report | `wa-cluster-M{NN}-grouped-v{N}-{date}.md` | Reference; verses by sub-group + VCG with anchors |

A pre-generated **input pack** is produced by the script `_generate_cluster_session_c_input_pack.py` (to be authored — see §9). The pack is a structured Markdown that gathers all of the above into a single self-contained reading document. AI consumes the input pack rather than running its own SQL.

**Inputs not used:**
- Raw `wa_verse_records` rows beyond what's already in anchor verses (would re-introduce text the findings already digested)
- `wa_session_b_findings` (registry-scope, different model)
- Source consolidated findings files (the markdown files Phase 9 parsed). The DB row is canonical; the markdown is provenance.

---

## 5. Output document — structure

One Markdown file per cluster per version:

`Sessions/Session_Clusters/M{NN}/wa-cluster-M{NN}-publication-v{n}-{date}.md`

**Suggested chapter structure** (the AI may compress or refactor where the cluster's evidence supports it; the section ORDER below is fixed):

### Chapter 1 — Opening
What this cluster is. The inner-being domain it covers. Why it matters. Length: ~300–500 words. Tone: orienting, accessible. Draws from cluster `description` + cluster_synthesis findings at the T0 tier.

### Chapter 2 — The terrain
The terms that carry the cluster — how many, what languages, the sub-group map. The reader leaves this chapter knowing what vocabulary the cluster covers and how that vocabulary subdivides analytically. Length: ~400–800 words. Draws from `cluster_subgroup` labels + descriptions, term counts, the gloss list.

### Chapter 3 — The divine pattern
What Scripture attributes to God in this domain (T0 tier findings). Where God is silent on a sub-group's mode of the characteristic. The chapter establishes whether and how this is a divine attribute, with the human characteristic imaging it. Length: ~600–1000 words. Drawn from T0 findings + cluster_synthesis findings at T0.

### Chapter 4 — The human person
Where this characteristic sits constitutionally in the human person (T2 tier findings: spirit, soul, heart, mind, will, body, faculty locations). Which inner faculties it engages (T3 tier: perception, cognition, memory, affect, will, conscience, etc.). Length: ~800–1500 words. Drawn from T2 + T3 findings across sub-groups.

### Chapter 5 — Operation
How this characteristic actually functions in the life of the person — given to God, given to others, received, formed through experience, deepened through suffering, oriented toward eschatological fullness (T4 + T5 tier findings). Length: ~800–1500 words.

### Chapter 6 — Structural relationships
How this cluster relates to other inner-being characteristics (T6 tier findings). What is its structural opposite, its nearest neighbour, what produces it, what it produces. Length: ~400–800 words. T6 findings — may surface placeholders for Session D synthesis.

### Chapter 7 — Sub-group-by-sub-group treatments
A short section per sub-group (M{NN}-A, B, C, …). Each section:
- Names the sub-group, its label and short description
- Quotes its anchor verse(s) — at least one
- Summarises its analytical character drawing from its VCG context_descriptions and sub-group-scoped findings
- Length per sub-group: ~200–400 words. For a 9-sub-group cluster like M15, this chapter is ~2000–3000 words total.

### Chapter 8 — What we did not address
Honesty section. The `gap` findings — what's parked (e.g. LXX work for M15's T7.1.8). Any `silent` patterns that should be acknowledged rather than glossed over. Length: ~200–400 words.

### Appendix A — Verse anchor catalogue
Compact list of every anchor verse with reference + the VCG it anchors + verse text. Generated; not narrative.

### Appendix B — Method note
A short paragraph stating the analytical method: "This publication draws from N findings recorded against M catalogue prompts; the findings are joined to V verse anchors per sub-group. The findings were produced under wa-sessionb-cluster-instruction v1_1." Length: ~100 words.

---

## 6. Composition rules

**6.1 Citation discipline.** Every substantive claim in chapters 3–7 must trace to one or more specific findings or anchor verses. The format `(M15-A T0.1.1)` references the finding for sub-group M15-A on prompt T0.1.1. The format `[Dan 2:20]` references a verse. Both citation styles appear inline in the prose, parenthetically. The Appendix A roll-up provides the resolved verse text.

**6.2 No invented evidence.** If a sub-group's findings are silent on a prompt, the chapter must not claim what the sub-group "would have said". Silence is recorded as silence — Chapter 8 lists silences explicitly.

**6.3 Cluster_synthesis findings carry the cross-cutting claims.** The 23 (in M15's case) cluster_synthesis findings are the most analytically dense. Chapters 1, 3, 4, 5 lean heavily on them. Per-sub-group chapters (Chapter 7) lean on the sub-group-scoped findings.

**6.4 Tone.** Plain accessible English. No technical jargon without unpacking. Hebrew/Greek terms cite transliteration + gloss on first appearance. Verse references in standard form (`Dan 2:20`, `1Cor 1:24`).

**6.5 Reader assumption.** The reader is an intelligent non-specialist. They know what wisdom or knowledge or righteousness mean colloquially. They do not know the term cha.kham or the sub-group structure or the catalogue. The publication makes the analytical structure approachable without reducing it to popularisation.

---

## 7. Lifecycle and versions

**v1 — Initial publication.** Drafted from the input pack alone. The first reader-facing form of the cluster.

**v2 — Session D-informed.** When Session D produces cross-cluster synthesis findings touching this cluster, v2 is regenerated to fold them into Chapter 6 (Structural relationships) and where appropriate Chapter 4 / 5. v2 cites Session D findings explicitly.

**v3 — Final corrections.** Only if researcher review of v1/v2 produces material corrections that warrant a new version rather than minor in-place edits.

Filenames per `wa-global-general-rules` GR-FILE-003 / GR-FILE-007 / GR-FILE-009:
- v1: `wa-cluster-M{NN}-publication-v1-{YYYYMMDD}.md`
- v2: `wa-cluster-M{NN}-publication-v2-{YYYYMMDD}.md`
- v3: `wa-cluster-M{NN}-publication-v3-{YYYYMMDD}.md`

---

## 8. Self-checks before submission

Before the AI hands a Session C Cluster publication to the researcher, it confirms:

| Check | Required |
|---|---|
| Every sub-group has a section in Chapter 7 | Yes |
| Every sub-group's section quotes at least one anchor verse | Yes |
| Every chapter 3–7 claim has a finding or verse citation | Yes |
| Chapter 8 lists every `gap` finding and any consistent silence pattern | Yes |
| Word count per chapter falls inside the stated range (±25%) | Soft target |
| No claims unattested in the cluster's findings or anchors | Hard rule |
| File saved with correct version filename | Yes |
| The publication is self-contained — readable without the comprehensive report | Yes |

A failed self-check stops the submission. The AI fixes, then re-checks.

---

## 9. Tooling — to be authored

This instruction depends on:

1. `_generate_cluster_session_c_input_pack.py` — produces a single Markdown input pack per cluster, gathering sub-group, VCG, anchor, finding, and term-meaning detail in the order the publication will consume. Pack is read-only.
2. `_validate_cluster_publication.py` — a post-write checker for §8 self-checks, producing a YES/NO per check with cited evidence.

Both scripts are scaffolding for the publication workflow; neither writes to the DB. Authoring these is a prerequisite to first M15 publication.

---

## 10. M15 first run — concrete plan

1. Author `_generate_cluster_session_c_input_pack.py`. Run for M15. Verify the pack is self-contained.
2. Author M15 publication v1 against the pack. Tone test: read Chapter 1 aloud — does it land for the non-specialist?
3. Run `_validate_cluster_publication.py` against the v1. Address any failed checks.
4. Researcher review. Iterate the instruction (this document) based on what worked and what didn't.
5. Once M15 holds together, run the same process for M06, M05, M26 in turn. Each gives further evidence of where the instruction needs to firm up or relax.

---

## 11. Open questions

These need researcher decisions before the first run:

1. **Length envelope** — the per-chapter word-count ranges above add up to a ~6,000–10,000-word document for a 9-sub-group cluster. Acceptable? Too long? Should we set a hard upper limit?
2. **Anchor citation style** — inline parenthetical only, or footnotes at chapter end?
3. **Chapter 7 ordering** — alphabetical sub-group code, or analytical primacy (most-central sub-group first)?
4. **Cluster_synthesis findings in Chapter 1** — quote the strongest 2–3 verbatim, or weave them into prose? (Recommended: weave; quote only the load-bearing one.)
5. **BOUNDARY sub-group treatment** — does it get a Chapter 7 section, or is it handled in a single paragraph in Chapter 8? (BOUNDARY's data shape is different: structural-note only, no 189-prompt coverage.)
6. **Session D fold-in (v2)** — does v2 re-issue the whole publication, or only the affected chapters? File-discipline implication.
7. **Citation table dependency** — if `cluster_finding_citation` lands later (per the 2026-05-07 design doc), the inline citation format may simplify. Decide whether to plan for that or freeze on the current schema.

---

## 12. Relationship to the legacy per-word Session C

The per-word Session C instruction (`wa-sessionc-instruction-v1_5-20260418.md`) produces one document per registry-word. That work remains valid and is not superseded — word-level publications continue to exist independently.

Cluster Session C is a parallel layer at a different scope. A cluster publication does NOT replace the per-word studies for the cluster's terms. Both layers will eventually exist; they reference each other.

---

*Draft v0_1 — 2026-05-12. Author: Claude Code, building on the 2026-05-07 design discussion. First test case M15 (Wisdom). Open questions in §11 require researcher decision before the first run.*
