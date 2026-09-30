# Session C — design v4 (Chapter 7 reinstated, citation discipline, appendix rewrite)

**Date:** 2026-05-12
**Supersedes:** v3
**Test case:** M15 (Wisdom, Understanding and Knowledge)

---

## 1. Pipeline (final)

```
Session A   →  per-word data extraction (JSON, registry-scope)
Session B   →  the analytical work that produces a complete cluster:
                groups of related characteristics, their meaning-groups,
                their key verses, and the full evidence record
Session C   →  the published study (this session — the only Session C)
Session D   →  cross-study synthesis that runs across multiple
                published studies
```

The per-word Session C is gone. The published study is the only Session C output.

---

## 2. Audience and language discipline

Plain-English book chapter for an intelligent reader who has no familiarity with the project's analytical vocabulary.

**Words the publication does NOT use:**

| Avoid | Use instead |
|---|---|
| cluster | "this study", "these related characteristics", "the family of characteristics" |
| sub-group | "characteristic", "facet", "form" |
| VCG / verse context group | "meaning group" (rare), or describe inline ("the verses where wisdom names God's own attribute") |
| anchor verse | "key verse", "the central verse" |
| finding | "what the evidence shows", "what the verses tell us", "the pattern" |
| tier / T0 / T1 … | thematic names (see §3) |
| catalogue prompt | not exposed |
| constitutional location | "where this lives in the inner person" |
| inner faculty | "the inner capacity", "the part of the person that …" |
| sub-group code / VCG code | not exposed in prose (used in editing notes and appendix only) |
| domain, findings | not exposed |

**Tone:** essayistic, evidential, reverent without being devotional, clear about what is shown and what is silent.

---

## 3. Thematic names for the analytical tiers

The publication never refers to "T0" / "T2" etc. Internally:

| Internal tier code | Thematic lens (used in chapter prose) |
|---|---|
| T0 | The divine pattern — what Scripture says about God in this characteristic |
| T1 | What the characteristic is (definition, name, kind, boundary, modes) |
| T2 | Where the characteristic lives in the inner person |
| T3 | Which inner capacities the characteristic engages |
| T4 | How the characteristic moves — between God and the person, between persons, in covenant, against opposition |
| T5 | How the characteristic is formed, deepens, is tested, is transformed |
| T6 | How the characteristic relates to other inner characteristics |
| T7 | The view from outside Scripture — what physical and clinical sciences observe |

T7 is treated in the publication as the **view from outside Scripture**: brief, evidential, and explicit about gaps. T7 is acknowledged as **under-developed** in Session B and earmarked for expansion in a later Session B pass.

---

## 4. Citation discipline (publication-wide)

**Every analytical claim in the publication is grounded by a quoted verse.** When the prose makes a claim about a characteristic, the relevant key verse is:

1. **Named in the prose** by reference (e.g. "as Pro 16:23 makes plain…")
2. **Quoted** — either inline or in a short indented block when the quote is long enough to warrant separation
3. **Attributed to its meaning-group context** where that context shapes the reading (e.g. "in the verses where wisdom is named as God's own attribute — most clearly at Dan 2:20 — …")

Conventions:

- Quote verbatim from `wa_verse_records.verse_text` (no paraphrase)
- Reference format: standard biblical citation (Pro 16:23, not "P-008")
- A characteristic's section in Chapters 4, 5, 6, 7 cites at least 2 key verses; deeper treatments cite more
- The same key verse can be cited in multiple chapters under different lenses
- No finding-id, no tier code, no prompt-id ever appears in the prose

This is enforced in the AI-WRITE zone instructions in the framework: each zone specifies which verses MUST be quoted in that zone's prose. The framework includes the verse text inline so AI does not have to re-source.

---

## 5. Chapter structure (v4)

| Chapter | Title (working) | Length | Structure |
|---|---|---|---|
| 1 | What this study is | ~300–500 words | Opening: what these characteristics are, what they cover together, why they belong together, what they share, how they depend on each other. |
| 2 | The characteristics in this study | ~200–300 words per characteristic | One short section per characteristic. Names it, describes it, says how it differs from the others. |
| 3 | The divine pattern | flexible | Cluster-wide narrative on how Scripture attributes these characteristics to God, with per-characteristic paragraphs for variation. |
| 4 | Where each characteristic lives in the person | ~800–1500 words per characteristic | Per characteristic. Where in the inner person it sits and which inner capacities it engages. T2 + T3. |
| 5 | How each characteristic works | ~800–1500 words per characteristic | Per characteristic. Movement between God and person, formation, modes. T4 + T5 + parts of T1. |
| 6 | How each characteristic relates to the others | ~400–800 words per characteristic | Per characteristic. Adjacents, opposites, what produces it, what it produces. T6. |
| 7 | **The view from outside Scripture** | ~400–500 words per characteristic (or per group of related characteristics) | Per characteristic (or grouped where the science overlaps). Short overview of what human and clinical sciences observe about the corresponding human capacity, with explicit reflection on synergies, gaps, and differences from the biblical picture. Acknowledges that this lens is under-developed in Session B and is earmarked for a later pass. Draws T7. |
| 8 | What this study does not yet address | ~200–400 words | Honest accounting of gaps and silences (now also names the T7 expansion as future work). |

**Length does not constrain comprehensiveness.** For M15 (9 characteristics) the publication lands around 28,000–40,000 words including Ch 7.

---

## 6. Appendices (v4)

### Appendix A — Terms in this study

**Two layers.** Each characteristic gets two sub-tables:

**Layer 1: Key characteristic terms.** The terms in `mti_term_subgroup` for each characteristic that carry the core meaning. Columns:

- Strong's number
- Hebrew / Greek + transliteration
- Primary gloss
- Brief description of what the term carries in this study (CC pre-extracts; AI writes the brief description from term meanings + cluster context)

**Layer 2: Supportive terms.** Terms in the inventory that provide additional meaning but do not carry the core characteristic. Columns: same as Layer 1.

### Appendix B — Key verses

A complete table of every key verse cited in the chapters. Columns:

| Characteristic | Meaning-group | Reference | Hebrew/Greek | Transliteration | Verse text | **Meaning of the term in this study** |

The "Meaning of the term in this study" column is the per-verse contextual meaning — how the term functions in *this* verse in the context of *this* characteristic. CC pre-extracts from `verse_context.contextual_meaning` (or equivalent column) and from the meaning-group description; AI writes a tight one-line where needed.

### Appendix C — Method note

~150 words plain-English. Acknowledges the structured analytical record, the verse evidence base, and that no claim in the chapters is made without specific verse evidence behind it.

---

## 7. Data-source → chapter mapping (v4)

| Data source | Feeds | Chapter / section | Role |
|---|---|---|---|
| `cluster.short_name` + `description` | Document title | Title block | CC (verbatim) |
| Cluster-synthesis findings at T0 + T1 | Chapter 1 opening prose | Ch 1 | CC extracts; AI writes |
| `cluster_subgroup.label` + `core_description` | Chapter 2 per-characteristic section | Ch 2 §2.x | CC verbatim; AI writes differentiating prose |
| Term inventory per characteristic | Ch 2 §2.x, Ch 4–7, App A | CC verbatim |
| Key verses (`verse_context.is_anchor=1`) + verse_text | Quoted in Ch 3–7 sections; App B | CC verbatim; AI selects quotes for prose |
| Meaning-group `context_description` | Inline phrasing in Ch 4–7 | CC pre-extracts; AI weaves |
| T0 cluster-synthesis findings | Ch 3 cluster-wide spine | CC extract; AI narrates |
| T0 sub-group findings | Ch 3 per-characteristic paragraphs | CC per characteristic; AI writes variation paragraphs |
| T2 + T3 sub-group findings | Ch 4 per characteristic | CC per characteristic; AI synthesises |
| T4 + T5 + T1 sub-group findings | Ch 5 per characteristic | CC per characteristic; AI synthesises |
| T6 sub-group findings | Ch 6 per characteristic | CC per characteristic; AI synthesises |
| T7 sub-group findings + general clinical-science context | Ch 7 per characteristic (or group) | CC extracts T7 findings; AI brings external science knowledge and writes reflection |
| T6 cluster-synthesis findings | Ch 3 closer and/or Ch 6 opener | CC extract; AI weaves |
| Silent findings + Gap findings | Ch 8 honest accounting | CC list; AI writes prose |
| Cluster metadata | App C | CC verbatim |
| `verse_context.contextual_meaning` per anchor verse | App B "meaning of the term in this study" column | CC extracts; AI tightens to one line if missing |
| Term gloss + transliteration | App A Layer 1 & 2 | CC verbatim |
| Term in-study description | App A Layer 1 & 2 | CC pre-extracts source; AI writes the brief |

**BOUNDARY characteristics** are acknowledged in Chapter 2 §2.9 ("supporting characteristics") and noted in Chapter 8 as not treated at full depth. They do not get sections in Chapters 4–7. Their terms appear in Appendix A Layer 2 (supportive terms).

---

## 8. CC vs AI split — concrete

**CC produces a framework file** — a complete Markdown document where:

- Every header is in place
- Every table is fully populated from DB
- Every key verse is quoted verbatim with full text
- Every chapter has the supporting evidence pre-extracted and labelled
- Every paragraph requiring interpretative writing is marked with an explicit AI-WRITE zone

```markdown
<!-- AI WRITE: Chapter 4, §4.3 (Knowledge: inner content held in the knowing self)
     LENGTH: ~1000-1500 words
     SOURCE: T2 + T3 evidence below for M15-C, plus the key verses listed
     FOCUS: Where does inner content of knowing live? Which capacities engage?
     CITE: at least 2 key verses verbatim from the list below; reference by
           biblical citation (e.g. Hos 6:3). Do not name finding-ids or
           tier codes.
     AVOID: jargon — see §2 of design doc.
-->

[CC pre-populates the T2 + T3 evidence blocks here, one per finding, each with the relevant key verses inlined.]
```

**Two-stage rendering:**

1. **Framework stage:** CC produces the framework file. AI reads it, writes prose into every marked zone.
2. **Finalisation stage:** CC strips the evidence blocks and AI-WRITE markers. Result: clean publication.

**AI never reads the DB.** AI sees only the framework file.

---

## 9. First-stab skeleton (M15, final published form)

```markdown
# Wisdom, Understanding and Knowledge
## A study of how Scripture treats the inner life of cognition, perception and word

---

## 1. What this study is
[~400 words. The inner life of the mind in Scripture, why these
nine characteristics belong together, how they depend on God as
source, how they image divine attributes.]

---

## 2. The characteristics in this study
### 2.1 Wisdom as a settled inner character (~250w)
### 2.2 Understanding as the inner faculty of perception (~250w)
### 2.3 Knowledge as inner content and covenant knowing (~250w)
### 2.4 Discernment and practical judgement (~250w)
### 2.5 Deliberative planning and purposive intent (~250w)
### 2.6 Meditative and reflective inner activity (~250w)
### 2.7 Inner thought-content (~250w)
### 2.8 The Word that engages the inner being (~250w)
### 2.9 Supporting characteristics (~150w)

---

## 3. The divine pattern
[~1500-2500w. Cluster-wide arc with per-characteristic paragraphs.]

---

## 4. Where each characteristic lives in the person
[8 sections, ~1000w each. T2+T3.]

---

## 5. How each characteristic works
[8 sections, ~1000w each. T4+T5+T1.]

---

## 6. How each characteristic relates to the others
[8 sections, ~600w each. T6.]

---

## 7. The view from outside Scripture
[8 sections (or grouped), ~450w each. Plain summary of what human and
clinical sciences observe about each cognitive capacity (cognition for
wisdom, perception for understanding, knowledge representation for
knowledge, executive function for discernment and planning, default-
mode reflection for meditation, working memory for thought-content,
language processing for the word). For each: synergies with the
biblical picture, gaps, differences. Closes by noting that the
analytical record's view from outside Scripture is under-developed at
present and is earmarked for a future Session B pass to expand.]

---

## 8. What this study does not yet address
[~300w honest accounting. Names the LXX gap, cross-characteristic
dimension comparisons, the under-developed view from outside Scripture,
and the meaningful silences in the verse evidence.]

---

## Appendix A — Terms in this study
[Per characteristic, two sub-tables: Key characteristic terms and
Supportive terms. Each row: Strong's | Hebrew/Greek | Transliteration |
Gloss | Brief description in this study.]

---

## Appendix B — Key verses
[Single table covering every quoted verse. Columns:
Characteristic | Meaning-group | Reference | Hebrew/Greek |
Transliteration | Verse text | Meaning of the term in this study.]

---

## Appendix C — Method note
[~150w on the analytical method, no jargon.]
```

---

## 10. What changed from v3 → v4

| Item | v3 | v4 |
|---|---|---|
| Chapter 7 | Removed | **Reinstated** as "The view from outside Scripture" — T7 lens, per characteristic, ~400–500w each |
| T7 thematic name | "Methodological / evidential foundation (mostly invisible)" | "The view from outside Scripture — what physical and clinical sciences observe" |
| Citation discipline | Implicit | §4 makes it explicit — every claim grounded by quoted verse, framework instructs the AI |
| Appendix A | Key verses table | **Terms in this study** — two layers (key + supportive), per characteristic |
| Appendix B | (was the method note) | **Key verses** — with extra column "Meaning of the term in this study" |
| Appendix C | — | **Method note** (moved from B) |
| BOUNDARY treatment | Section in Ch 2 | Same, plus Layer 2 (supportive terms) of App A |
| Length estimate | 25k–35k for M15 | 28k–40k for M15 (Ch 7 adds ~3–4k) |
| T7 status | Not surfaced | Acknowledged as **under-developed**, earmarked for Session B expansion |

---

## 11. Next step (already in flight)

Authoring `_generate_cluster_session_c_framework_v1_20260512.py` and running it for M15. The output is the AI input file: a single complete framework `.md` with every evidence block pre-extracted and every AI-WRITE zone marked. That output is what gets handed to Claude AI to author the prose. The framework will surface any structural awkwardness now, before AI writes anything expensive.
