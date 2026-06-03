# Session C Cluster — design v2

**Date:** 2026-05-12
**Supersedes:** the v0_1 draft instruction (which wrongly assumed per-word Session C continues).
**Test case:** M15 (Wisdom, Understanding and Knowledge).
**Builds on:** `tier-question-linkage-analysis-v1-20260507.md` (schema map) + `cluster-finding-citation-model-design-v1-20260507.md` (deferred).

This document is the prerequisite to the instruction itself. It establishes:

1. The revised pipeline (per-word Session C is gone).
2. The **data-source → chapter mapping table** — what each part of the published report draws from.
3. The CC vs AI division of labour — CC builds the mechanical scaffold, AI writes the interpretative prose.
4. A **first-stab skeleton** of the published study output for M15, with both CC-generated content and AI-write zones explicit.

---

## 1. Revised pipeline position

```
Session A   →  per-word data extraction (JSON, registry-scope)
Session B   →  cluster analytical work — sub-groups, VCGs, anchors,
                189-prompt catalogue pass, cluster_finding population
Session C   →  CLUSTER PUBLICATION (this session)
                — the single reader-facing layer
Session D   →  cross-cluster synthesis (consumes Session C output)
```

The per-word `wa-sessionc-instruction-v1_5-20260418.md` is **superseded**, not retained. Published word studies will not be produced going forward. The cluster publication is the only Session C output.

---

## 2. Data-source → chapter mapping

Each row of this table says: *which data in the cluster's analytical output feeds which paragraph or chapter of the published report*. The mapping is one-way (analytical output → publication). The publication adds no new content; it expresses what the analysis already established.

| Data source | Table / column | Feeds | Chapter / section | Role |
|---|---|---|---|---|
| Cluster identity | `cluster.short_name`, `description` | Document title + Chapter 1 opening line | Title, Chapter 1 ¶1 | CC (verbatim) |
| Cluster term list | `cluster.gloss` (parsed) | Vocabulary scope statement | Chapter 2 ¶1 | CC (verbatim) |
| Sub-group inventory | `cluster_subgroup.subgroup_code`, `label`, `core_description` | Sub-group map table + per-sub-group orientation | Chapter 2 §2.2 (table), Chapter 7 §-headers | CC (table); AI (introductory ¶ for the map) |
| Term-to-sub-group mapping | `mti_term_subgroup` + `mti_terms.strongs_number/transliteration/gloss` | Per-sub-group term inventory; cluster-wide term count | Chapter 2 §2.2 (counts), Chapter 7 per-§ (term lists) | CC (verbatim list) |
| VCG inventory | `verse_context_group.group_code`, `context_description` joined via `vcg_term` to sub-group | Per-sub-group VCG list with one-sentence context_description | Chapter 7 per-§ (VCG list) | CC (verbatim list); AI (synthesis ¶ across the VCGs of one sub-group) |
| Anchor verses | `verse_context.is_anchor=1` joined to `wa_verse_records.reference + verse_text` and `verse_context_group.group_code` | Anchor quotation in per-sub-group section + full anchor catalogue | Chapter 7 per-§ (1 anchor quoted in prose); Appendix A (every anchor verbatim) | CC (verbatim verse_text); AI (chooses which 1 anchor to quote in prose where multiple exist) |
| Cluster-synthesis findings | `cluster_finding` where `cluster_subgroup_id IS NULL` AND `finding_status='cluster_synthesis'` (23 rows for M15) | The cross-cutting claims that hold across all sub-groups — what the cluster ITSELF says | Chapter 1 (orientation), Chapter 3 (T0 syntheses), Chapter 4 (T2/T3 syntheses), Chapter 5 (T4/T5 syntheses), Chapter 6 (T6 syntheses) | CC (extract per tier); AI (interpretative weaving) |
| T0 sub-group findings | `cluster_finding` where prompt LIKE 'T0.%' AND `cluster_subgroup_id IS NOT NULL` AND `finding_status='finding'` | Per-sub-group evidence of divine attribution / image-bearing / typology | Chapter 3 main body | CC (organises by tier and prompt); AI (synthesises into prose) |
| T1 sub-group findings | `cluster_finding` where prompt LIKE 'T1.%' | Definition material — what the characteristic is, named, kind, boundary | Distributed: Chapter 2 (naming, T1.1), Chapter 5 (modes-of-operation, T1.4), Chapter 6 (boundary, T1.3) | CC (organises); AI (synthesises) |
| T2 sub-group findings | `cluster_finding` where prompt LIKE 'T2.%' | Constitutional location (spirit / soul / heart / mind / will / body) per sub-group | Chapter 4 main body | CC (organises by constitutional level); AI (synthesises) |
| T3 sub-group findings | `cluster_finding` where prompt LIKE 'T3.%' | Inner-faculty engagement (perception, cognition, memory, affect, will, conscience…) per sub-group | Chapter 4 main body | CC (organises by faculty); AI (synthesises) |
| T4 sub-group findings | `cluster_finding` where prompt LIKE 'T4.%' | Directional operation (God→human, human→God, person→person, group→outsider, spiritual beings) | Chapter 5 main body | CC (organises by direction); AI (synthesises) |
| T5 sub-group findings | `cluster_finding` where prompt LIKE 'T5.%' | Formative / transformative dimension — sequence, suffering, sanctification, eschatology | Chapter 5 main body | CC (organises by formation aspect); AI (synthesises) |
| T6 sub-group findings | `cluster_finding` where prompt LIKE 'T6.%' | Structural relationships with adjacent characteristics | Chapter 6 main body | CC (organises by relationship type); AI (synthesises) |
| T7 sub-group findings | `cluster_finding` where prompt LIKE 'T7.%' | Evidential / methodological foundation — vocabulary architecture, anchor verses, literary form | Chapter 7 per-§ (briefly), Appendix B (method note) | CC (mostly mechanical); AI (light synthesis only) |
| Silent findings | `cluster_finding` where `finding_status='silent'` | Honest acknowledgement of where the cluster's evidence is mute on a prompt | Chapter 8 (silences) | CC (extract); AI (selects which silences are analytically significant and weaves into Ch 8) |
| Gap findings | `cluster_finding` where `finding_status='gap'` | Honest acknowledgement of work not yet done (e.g. LXX) | Chapter 8 (gaps) | CC (verbatim list) |
| Catalogue prompt text | `wa_obs_question_catalogue.question_text` | Used invisibly — AI consumes the prompt text to understand what each finding answers; the publication does NOT quote prompts | (no direct surface) | CC (provides in input pack); AI (consumes for context only) |
| Sub-group description | `cluster_subgroup.core_description` | Per-sub-group orienting paragraph | Chapter 7 per-§ ¶1 | CC (verbatim quotable); AI (may incorporate) |
| Verse text (full) | `wa_verse_records.verse_text` (for anchors only) | Anchor verse quotation; selected supporting quotations | Chapter 3-7 selected quotes, Appendix A | CC (verbatim); AI (chooses which to quote) |
| Cluster metadata | `cluster.last_updated_date`, `version` | Frontmatter | Document header | CC (verbatim) |

---

## 3. CC vs AI division of labour

**CC produces (deterministic, mechanical):**

- Document title + frontmatter
- Chapter / section headers (every chapter, every sub-section)
- Every table (sub-group map, term inventories, VCG lists, anchor catalogue)
- Every verbatim quotation block (anchor verses with `verse_text`, finding text where quoted)
- The structural skeleton of Chapter 7 — one §-header per sub-group, with each section pre-populated with sub-group label, core_description, term list, VCG list, anchor verse(s), and the raw findings grouped by tier
- Chapter 8's mechanical lists (every gap row, every silence prompt code)
- Appendix A in full (anchor catalogue)
- Appendix B in full (method note boilerplate filled with this cluster's numbers)
- "AI-write" zones marked clearly with placeholders like `<!-- AI: paragraph here synthesising T2 findings for M15-B -->`

**AI produces (interpretative writing):**

- Chapter 1: the 300–500 word opening prose — what the cluster IS and why it matters
- Chapter 2: connective prose around the CC-produced map
- Chapter 3: synthesis of T0 findings into 600–1000 words on the divine pattern
- Chapter 4: synthesis of T2 + T3 findings into 800–1500 words on constitutional location + faculty engagement
- Chapter 5: synthesis of T4 + T5 + parts of T1 findings into 800–1500 words on operation
- Chapter 6: synthesis of T6 findings into 400–800 words on structural relationships
- Chapter 7: 250–400 words per sub-group interpreting its findings (one paragraph per AI-write zone, multiple zones per sub-group)
- Chapter 8: 200–400 words of honest accounting prose around the CC lists

The pipeline:

```
1. CC reads DB → produces a "publication framework" .md file with all
                 tables, lists, headers, verbatim quotes, AND clearly-
                 marked AI-write zones embedded in place.
2. AI receives the framework → writes the prose into each marked zone.
3. CC validates the final document against §-self-checks.
```

The framework file is the equivalent of a "fill-in-the-blanks" template, but the blanks are paragraph-shaped and the surrounding text is fully resolved DB content. AI never reads SQL; CC never writes prose.

---

## 4. First-stab published-output skeleton (M15)

What follows is what the **CC-generated framework file** would look like for M15, with AI-write zones marked. This is a *visual mock-up* — not the actual file, which the input-pack script will eventually produce.

---

```
# M15 — Wisdom, Understanding and Knowledge
## A cluster study of the inner-being domain of cognition, perception, and word

**Cluster:** M15 (Wisdom, Understanding and Knowledge)
**Status:** Analysis Completed (2026-05-12, version v6)
**Sub-groups:** 9 (M15-A through M15-H + BOUNDARY)
**Terms:** 85 (43 Hebrew, 42 Greek)
**Anchor verses:** 55
**Findings recorded:** 1,724 (1,454 finding / 238 silent / 23 cluster-synthesis / 9 gap)

---

## Chapter 1 — What this cluster is

<!-- AI: 300–500 word opening prose.
     - Name the inner-being domain in plain English
     - Locate it in the wider landscape of inner-being characteristics
     - Pull from the strongest cluster_synthesis findings at T0.1.1 and T1.1
     - Frame why a reader should care — what's at stake in understanding this domain
     - End on a sentence that previews the structure of what follows -->

---

## Chapter 2 — The terrain

### 2.1 The vocabulary

The cluster spans 85 Strong's terms — 43 Hebrew, 42 Greek — that collectively
name the inner faculties and content of cognition, perception, comprehension,
deliberation, and the word as it engages the inner being.

<!-- AI: 1–2 paragraphs framing what's in the term list and what's notable
     about its shape. Draw from cluster.gloss and the sub-group structure
     to characterise the breadth without listing every term. -->

### 2.2 The sub-group map

The 85 terms organise into 9 analytical sub-groups, each naming a specific
mode in which this domain operates in the inner being.

| Sub-group | Label | Terms | Verses |
|---|---|---:|---:|
| M15-A | Wisdom as holistic inner character and orientation | 18 | 312 |
| M15-B | Understanding as inner perceptive faculty | 25 | 315 |
| M15-C | Knowledge as inner content and covenantal knowing | 10 | 576 |
| M15-D | Discernment and practical judgment | 12 | 179 |
| M15-E | Deliberative planning, counsel, and purposive intent | 20 | 200 |
| M15-F | Meditative and reflective inner activity | 14 | 68 |
| M15-G | Inner thought-content — the mind's formed thoughts | 10 | 27 |
| M15-H | Logos — the word as inner-being engagement | 1 | 43 |
| BOUNDARY | Functional, supporting, and cluster-reassignment candidates | 13 | 14 |

<!-- AI: 1 paragraph noting what the map shows analytically — the
     asymmetry (M15-C has the most verses; M15-G the fewest); the new
     M15-H sub-group for logos; the BOUNDARY treatment. Keep terse. -->

---

## Chapter 3 — The divine pattern

<!-- AI: 600–1000 words synthesising T0 findings (Divine image, created
     purpose, image-bearer expression, typological significance).

     Material to draw from:
     - 8 sub-group T0 findings (M15-A through M15-H), 12 prompts each
     - T0 cluster_synthesis findings (3 of the 23)
     - Anchor verses where divine attribution is evident

     Suggested narrative arc:
     - Open with the cluster_synthesis at T0.1.1: "across all sub-groups
       there is a consistent pattern…"
     - Show how each sub-group's evidence carries that pattern
     - Note the M15-F silence (meditative activity not attributed to God)
       — the one exception
     - Close on what this means for the human image-bearer -->

**Findings supporting Chapter 3:**

```
[CC will pre-populate this section with the 8 T0 findings per sub-group +
the 3 T0 cluster_synthesis findings, formatted as quotable evidence blocks
that the AI prose can cite by short reference, e.g. (M15-A T0.1.1).]
```

---

## Chapter 4 — The human person

<!-- AI: 800–1500 words synthesising T2 (constitutional location) +
     T3 (inner faculties) findings.

     Suggested narrative arc:
     - T2 constitutional location: what the verse evidence shows
       about WHERE in the inner being this domain lives
       (spirit / soul / heart / mind / will / body / faculty)
     - T3 faculty engagement: WHICH inner faculties this domain engages
       (perception, cognition, memory, affect, will, conscience…)
     - The asymmetric pattern: heart and mind are the primary seats;
       spirit-level engagement is mostly silent
     - Per-faculty story arc -->

**Findings supporting Chapter 4:**

```
[CC pre-populates: 31 T2 prompts × 8 sub-groups (where authored);
24 T3 prompts × 8 sub-groups (where authored); plus T2/T3 cluster_synthesis.]
```

---

## Chapter 5 — Operation

<!-- AI: 800–1500 words on T4 (direction) + T5 (formation) + selected T1.4
     (modes of operation).

     Suggested arc:
     - T4: how this domain operates relationally (God→human, human→God,
       person→person, in covenant, in adversarial encounter)
     - T5: how it is formed in the person — through teaching, through
       suffering, through sanctification, oriented toward eschatology
     - Selected T1.4 material on modes -->

**Findings supporting Chapter 5:**

```
[CC pre-populates T4 + T5 + T1.4 findings, organised by direction and
formation aspect.]
```

---

## Chapter 6 — Structural relationships

<!-- AI: 400–800 words on T6 — what is the cluster's structural opposite,
     its nearest neighbour, what produces it, what it produces, vocabulary
     sharing. Where Session D synthesis will most directly land. -->

**Findings supporting Chapter 6:**

```
[CC pre-populates T6 findings + T6 cluster_synthesis.]
```

---

## Chapter 7 — The nine sub-groups

[CC pre-populates one §-section per sub-group with the structure below.
AI fills the interpretive paragraphs.]

### 7.1 M15-A — Wisdom as holistic inner character and orientation

**Description:** Terms that name wisdom as a constituted holistic quality
of the inner person — a settled orientation of the whole person that
shapes perception, decision, and character. Includes the structural
opposite (unwise). Spirit-given, covenantally oriented, morally
constitutive.

**Terms (18):** [CC lists every Strong's + transliteration + gloss
inline, comma-separated, with primary terms in bold.]

**VCGs (10):**
- M15-A-VCG01 — Wisdom as God's own attribute
- M15-A-VCG02 — Wisdom as inner endowment given by God to a named recipient
- M15-A-VCG03 — Wisdom as the settled inner character of the wise person
- M15-A-VCG04 — The inner mind set on something
- M15-A-VCG05 — Inner concord between persons
- M15-A-VCG06 — Wisdom claimed as one's own
- M15-A-VCG07 — Worldly wisdom under judgment
- M15-A-VCG08 — The inner faculty of grasping / comprehending
- M15-A-VCG09 — Covenantal wisdom: rooted in fear of the Lord
- M15-A-VCG10 — Inner forming faculty for sacred design

**Anchor:** Dan 2:20 (M15-A-VCG01, H2452 chokh.mah) — "Blessed be the
name of God forever and ever, to whom belong wisdom and might."

<!-- AI: 250–400 words interpretive prose:
     - What this sub-group's evidence collectively shows about wisdom-as-character
     - Which VCGs carry the load and how they relate to each other
     - 1–2 quoted phrases from the strongest sub-group-scoped findings
     - Tie back to Chapter 3's divine pattern -->

**Sub-group-scoped findings (selected for Chapter 7 prose):**

```
[CC pre-populates 5–10 of the strongest findings for this sub-group,
chosen by tier coverage — at least one from T0, T2, T3, T5.]
```

### 7.2 M15-B — Understanding as inner perceptive faculty
... [same pattern]

### 7.3 M15-C — Knowledge as inner content and covenantal knowing
... [same pattern]

### 7.4 M15-D — Discernment and practical judgment
... [same pattern]

### 7.5 M15-E — Deliberative planning, counsel, and purposive intent
... [same pattern]

### 7.6 M15-F — Meditative and reflective inner activity
... [same pattern]

### 7.7 M15-G — Inner thought-content
... [same pattern]

### 7.8 M15-H — Logos: the word as inner-being engagement
... [same pattern — note that the core_description is currently empty in DB
     and needs filling before this section can be authored]

### 7.9 BOUNDARY — Functional, supporting, and cluster-reassignment candidates

<!-- AI: 1 paragraph treating BOUNDARY as a special case:
     - These terms support the cluster but are not themselves
       inner-being characteristics
     - No full catalogue pass applied per cluster instruction §11
     - Briefly note what role they play (translation, training,
       teaching, simile, insistence, etc.) -->

---

## Chapter 8 — What we did not address

### 8.1 Gaps (work parked for follow-up)

The catalogue pass left 9 findings marked `gap`:

- **T7.1.8 LXX investigation** (one per active sub-group A–H, 8 rows):
  the LXX rendering of each sub-group's Hebrew vocabulary against the
  later Greek tradition is parked pending a Logos Bible Software
  research session.
- **T6.7.3 dimensional sharing** (M15-A): full dimensional-sharing
  data requires CC queries against the flag system (FLAGS M15-008,
  010, 012, 014).

### 8.2 Significant silences

<!-- AI: 1–2 paragraphs interpreting the consistent silences across
     M15. The most analytically significant from the catalogue pass:
     - M15-F's silence at T0 (meditative activity not attributed to God)
     - Whatever else the silent pattern in cluster_synthesis names
     This is a finding, not a deficiency. -->

---

## Appendix A — Anchor verses (55)

[CC produces a table: sub-group code | VCG code | reference | Strong's + transliteration | verse text. One row per anchor. No prose.]

---

## Appendix B — Method

<!-- CC boilerplate, parameterised by cluster numbers -->
This publication draws from 1,724 findings recorded against 189
catalogue prompts across 8 tiers (T0–T7). The findings are joined to
55 verse anchors across 9 sub-groups. The findings were produced under
wa-sessionb-cluster-instruction v1_1; the publication is produced under
wa-sessionc-cluster-instruction [version pending finalisation]. The
analytical methodology, including the operating principle ("Read every
verse, write on discovery, fluency is not a quality signal"), is
documented in those instructions.
```

---

## 5. What the instruction (yet to be drafted) needs to cover

With the data-mapping table and the first-stab skeleton in place, the instruction itself becomes shorter and more concrete. It needs to specify:

- **The framework-generator contract.** What CC produces, exact section structure, what an AI-write zone looks like.
- **The AI-write contract.** What goes in each zone, length budget, citation discipline, fluency guard.
- **Self-check rules.** Before submission: every AI-write zone filled; every claim cites a finding-id or anchor; word counts within ±25%; no claims unattested in this cluster's analytical output.
- **Lifecycle.** v1 from cluster Analysis Completed; v2 from Session D synthesis fold-in.
- **Inputs.** Just the framework file, nothing else. AI does not read raw DB or SQL.

---

## 6. Open questions before drafting the instruction

These need researcher decisions:

1. **Length envelope.** The skeleton above lands around 6,000–10,000 words for a 9-sub-group cluster. Acceptable? Set a hard upper?
2. **Reader audience.** Plain-English intelligent-non-specialist (as the per-word Session C was)? Or a slightly more technical reader who can absorb sub-group / VCG references comfortably?
3. **Chapter 7 ordering.** Alphabetical by sub-group code (M15-A first) or analytical primacy (most-central sub-group first — e.g. M15-A for wisdom-cluster, or whichever sub-group is most foundational)?
4. **Cluster_synthesis findings.** Quote verbatim where they appear (preserves authoritative voice) or paraphrase into prose flow (preserves readability)? Or do both — quote the load-bearing one(s), weave the rest?
5. **BOUNDARY section size.** Single paragraph in Chapter 7.9 (current skeleton) or a separate Chapter 8.3?
6. **M15-H description gap.** M15-H currently has no `core_description` in DB. Fill before publishing M15? (Suggested: yes — AI authors a one-sentence description, applied via small directive.)
7. **Cross-cluster references.** When Chapter 6 (structural relationships) names another characteristic (e.g. M16 Folly as M15's structural opposite), do we wait for the other cluster's publication or footnote it as "under-investigated" for now?

---

## 7. Suggested next step

Once you sign off on:
- The data-source → chapter mapping table (§2)
- The CC/AI split (§3)
- The skeleton shape (§4)
- The open questions in §6

… I can:

1. Re-draft the instruction (v0_2) to align with this design.
2. Author `_generate_cluster_session_c_framework.py` — the script that produces the M15 framework file with AI-write zones.
3. Run it for M15. The output is the file that would go to Claude AI to author the prose.

Step 2 is the concrete test of whether this design holds.
