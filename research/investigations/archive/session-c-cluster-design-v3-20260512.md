# Session C — design v3 (incorporates researcher rewrite of chapters)

**Date:** 2026-05-12
**Supersedes:** v2 (which had the old chapter structure and assumed per-word Session C continued)
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

The published study is a **plain-English book chapter** for an intelligent reader who has no familiarity with the project's analytical vocabulary. They will read it as they would read any serious essay on the Bible's treatment of a theme.

**Words the publication does NOT use** (project-internal jargon):

| Avoid | Use instead |
|---|---|
| cluster | "this study", "these related characteristics", "the family of characteristics" |
| sub-group | "characteristic", "facet", "form", "the way wisdom appears as a settled inner quality" |
| VCG / verse context group | "meaning group" (rarely needed), or describe inline ("the verses where wisdom names God's own attribute") |
| anchor verse | "key verse", "the central verse", "the verse that most clearly shows this" |
| finding | "what the evidence shows", "what the verses tell us", "the pattern" |
| tier / T0 / T1 … | thematic names (see §3) |
| catalogue prompt | not exposed |
| constitutional location | "where this lives in the inner person", "the inner home of …" |
| inner faculty | "the inner capacity", "the part of the person that …" |
| sub-group code / VCG code | not exposed in the prose (used in editing footnotes and the appendix only) |

**Words it does use:** wisdom, understanding, knowledge, inner life, inner person, heart, mind, will, conscience, God, Scripture, character, attribute, characteristic, evidence, pattern, theme.

**Tone:** essayistic, evidential, reverent without being devotional, clear about what is shown and what is silent.

---

## 3. Thematic names for the analytical tiers

The publication never refers to "T0" / "T2" etc. Internally (for the framework script and validation), tiers map to thematic lenses:

| Internal tier code | Thematic lens (used in chapter prose) |
|---|---|
| T0 | The divine pattern — what Scripture says about God in this characteristic |
| T1 | What the characteristic is (definition, name, kind, boundary, modes) |
| T2 | Where the characteristic lives in the inner person (heart / mind / will / faculty / body / spirit / soul) |
| T3 | Which inner capacities the characteristic engages (perception, thought, memory, feeling, conscience, will, agency) |
| T4 | How the characteristic moves — between God and the person, between persons, in covenant, against opposition |
| T5 | How the characteristic is formed, deepens, is tested, is transformed, points toward what is to come |
| T6 | How the characteristic relates to other inner characteristics — what it is paired with, opposed by, produced by, productive of |
| T7 | Methodological / evidential foundation (mostly invisible to the reader — surfaces only in the appendix) |

---

## 4. Chapter structure (researcher rewrite, 2026-05-12)

| Chapter | Title (working) | Length | Structure |
|---|---|---|---|
| 1 | What this study is | ~300–500 words | Opening: what these characteristics are, what they cover together, why they belong together, what they share, how they depend on each other. |
| 2 | The characteristics in this study | ~200–300 words per characteristic | One short section per characteristic. Names the characteristic, describes it briefly, says how it differs from the others. (For M15: 9 sections.) |
| 3 | The divine pattern | flexible | Cluster-wide narrative on how Scripture attributes these characteristics to God, with individual paragraphs for each characteristic where the pattern differs. |
| 4 | Where each characteristic lives in the person | ~800–1500 words per characteristic | One section per characteristic. Goes deep on where in the inner person it sits (heart/mind/will/etc.) and which inner capacities it engages. Draws T2 + T3 evidence. |
| 5 | How each characteristic works | ~800–1500 words per characteristic | One section per characteristic. How the characteristic moves between God and person, how it forms and deepens, what shapes it through suffering and time. Draws T4 + T5 + parts of T1 evidence. |
| 6 | How each characteristic relates to the others | ~400–800 words per characteristic | One section per characteristic. Adjacent characteristics, opposites, what produces it, what it produces, shared vocabulary. Draws T6. |
| 8 | What this study does not yet address | ~200–400 words | Honest accounting of what was deferred and what the verse evidence is silent on. |

**No Chapter 7** in this structure — the per-characteristic depth moves into chapters 4–6 (one lens per chapter, going through each characteristic in turn).

**Length does not constrain comprehensiveness.** The ranges above are descriptive guidance, not caps. For M15 (9 characteristics) the publication lands around 25,000–35,000 words. That is acceptable.

**Appendices:**

- **A — Key verses table:** every key verse used in the chapters, organised by characteristic and meaning-group. Pure list, no prose.
- **B — Method:** a short paragraph at the back acknowledging the analytical method used to produce the study, written in plain English. No "tier" or "VCG" terms.

---

## 5. Data-source → chapter mapping (revised for new structure)

Each row of this table says: which DB data feeds which chapter or section.

| Data source | Feeds | Chapter / section | Role |
|---|---|---|---|
| `cluster.short_name` + `description` | Document title | Title block | CC (verbatim) |
| Cluster-synthesis findings at T0 + T1 (the cross-cutting claims) | Chapter 1 opening prose | Ch 1 (whole) | CC extracts; AI writes prose |
| `cluster_subgroup.label` + `core_description` (per characteristic) | Chapter 2 per-characteristic section | Ch 2 §2.x | CC populates label + description verbatim; AI writes the differentiating prose |
| Term inventory per characteristic (`mti_term_subgroup` + `mti_terms`) | Brief term-count in Ch 2; full lists in Ch 4–6 framing | Ch 2 §2.x, Ch 4–6 per-§ | CC (verbatim) |
| Key verse per meaning-group (`verse_context.is_anchor=1` + `verse_context_group` + `wa_verse_records.verse_text`) | Quoted in Ch 4–6 per-characteristic sections; full list in App A | Ch 4–6 per-§, App A | CC (verbatim verse_text); AI (chooses which to quote in prose) |
| Meaning-group context_descriptions (`verse_context_group.context_description`) | Inline phrasing in Ch 4–6 prose | Ch 4–6 per-§ | CC (pre-extracts); AI (weaves) |
| T0 cluster-synthesis findings | Ch 3 cluster-wide narrative spine | Ch 3 main body | CC (extract); AI (narrative) |
| T0 sub-group findings | Ch 3 per-characteristic variation paragraphs | Ch 3 (per-characteristic ¶s) | CC (extract per characteristic); AI (writes the "where it differs" paragraphs) |
| T2 + T3 sub-group findings | Ch 4 (per characteristic — the deep dive on where it lives + what it engages) | Ch 4 §4.1 through §4.9 | CC (extracts T2 + T3 per characteristic, organised by constitutional level + faculty); AI (synthesises into 800–1500 words per characteristic) |
| T4 + T5 + T1.4 sub-group findings | Ch 5 (per characteristic — how it works) | Ch 5 §5.1 through §5.9 | CC (extracts per characteristic, organised by direction + formation aspect); AI (synthesises into 800–1500 words per characteristic) |
| T6 sub-group findings | Ch 6 (per characteristic — relationships to others) | Ch 6 §6.1 through §6.9 | CC (extracts per characteristic, organised by relationship type); AI (synthesises into 400–800 words per characteristic) |
| T6 cluster-synthesis findings | Ch 3 closer (how characteristics tie together) and/or Ch 6 opener | Ch 3 closing or Ch 6 opening | CC (extracts); AI (weaves) |
| Silent findings | Ch 8 honest accounting | Ch 8 | CC (extracts list); AI (selects analytically significant silences, writes prose) |
| Gap findings | Ch 8 list of unfinished work | Ch 8 | CC (verbatim list) |
| Catalogue prompt text | Consumed by AI invisibly to know what each finding is answering | (no surface) | CC (provides in framework); AI (consumes) |
| Cluster metadata (`status`, `version`, dates, totals) | App B method note | App B | CC (verbatim) |

**Note on BOUNDARY characteristics:** BOUNDARY did not receive the full evidence pass (per the way Phase 8 was scoped). So BOUNDARY does not get sections in Chapters 4–6. Instead it gets:

- A short section in Chapter 2 acknowledging the supporting characteristics in this study
- A mention in Chapter 8 noting that these supporting characteristics were not studied at the full depth

---

## 6. The CC vs AI split — concrete

**CC produces a "framework file"** — a complete Markdown document where:

- Every header is in place
- Every table is fully populated from DB
- Every key verse is quoted verbatim with full text
- Every chapter has the supporting evidence pre-extracted and labelled
- Every paragraph that requires interpretative writing is marked with an explicit zone:

```markdown
<!-- AI WRITE: Chapter 4, §4.3 (Knowledge as inner content)
     LENGTH: ~800-1500 words
     SOURCE: T2 + T3 findings for M15-C (below), plus the key verses
     FOCUS: Where does the inner content of knowing live in the person?
            Which inner capacities does it engage?
            What does the evidence pattern across these verses show?
     AVOID: any of the project's analytical jargon (see §2)
     CITE: by key verse only (e.g. "as Hos 6:3 makes plain…"). Do not cite
           finding-id or tier code in the prose. -->

[CC pre-populates the T2 + T3 evidence blocks here — one block per
prompt the AI needs as input, each labelled in a way the AI can read
but a publication reader won't see in the final form because these
blocks are stripped at finalisation.]
```

**Two-stage rendering:**

1. **Framework stage:** CC produces the framework file. AI reads it, writes prose into every marked zone.
2. **Finalisation stage:** CC runs a finalisation pass — strips the evidence blocks, strips the AI-WRITE markers, strips any internal cross-references that should not appear in the publication. Result: clean publication.

This lets the AI see all the evidence it needs to write each zone while keeping it OUT of the published output.

**AI never reads the DB or runs SQL.** AI sees only the framework file. CC handles all DB extraction.

---

## 7. First-stab skeleton of the published study (M15, cleaned of jargon)

What follows is the **final published form** — what the reader sees, after finalisation strips the evidence blocks and AI-write markers. This is what a non-specialist reader would actually pick up.

---

```markdown
# Wisdom, Understanding and Knowledge
## A study of how Scripture treats the inner life of cognition, perception and word

---

## 1. What this study is

[~400 words of AI-written opening prose. Names what the inner life of
the mind covers in Scripture — the characteristics by which a person
knows, perceives, understands, deliberates, holds thoughts, reflects,
and receives the word as it engages the inner being. Says why these
characteristics belong together: they all describe the cognitive-
perceptive dimension of the inner person; they all depend on God as
their source; they all stand under his judgement when claimed
autonomously; they all carry traces of his own character. Closes
with a sentence previewing what follows.]

---

## 2. The characteristics in this study

The Bible's vocabulary for the inner life of the mind organises into
nine related characteristics. Each is a distinct way the inner person
takes hold of, holds, or expresses what is known and what is true.

### 2.1 Wisdom as a settled inner character

[~250 words. Wisdom (chokh.mah, sofia) as the whole-person quality
that orients perception, decision, and conduct. Cites Dan 2:20 and
Pro 16:23 as touchpoints. Distinguishes from understanding (next
section) by its constitutive, character-shaping nature.]

### 2.2 Understanding as the inner faculty of perception

[~250 words. Understanding (bin, te.vu.nah, suniēmi, sunesis) as the
inner capacity to grasp what is being revealed or communicated.
Distinguishes from wisdom by its receptive nature.]

### 2.3 Knowledge as inner content and covenant knowing

[~250 words. Knowledge (da.at, ya.da, gnōsis, oida) as both content
held within the knowing self and the relational orientation of
knowing God. Names the dual sense — informational and covenantal.]

### 2.4 Discernment and practical judgement

[~250 words. The applied perceptive act — sa.khal, diakrinō — that
distinguishes right from wrong, traces consequences, evaluates
thoughts. The action edge of perception.]

### 2.5 Deliberative planning and purposive intent

[~250 words. The forward-orientation of the inner will — ya.ats, boulē,
purposeful intention. How the inner person forms a plan and holds it.]

### 2.6 Meditative and reflective inner activity

[~250 words. The inner turning of the mind on what has been received —
si.ach, ha.gut, dialogismos. The activity of pondering, the inner
dialogue of self-reasoning.]

### 2.7 Inner thought-content

[~250 words. The formed thoughts the mind holds — noēma, ennoia,
ra.yon — as objects that can be guarded, captured, led astray, or
disclosed. The mind's static content.]

### 2.8 The Word that engages the inner being

[~250 words. The word (logos) as it enters, dwells in, addresses,
and shapes the inner person. The newest of the nine characteristics
in our analytical structure, and the most distinct in its scope.]

### 2.9 Supporting characteristics

[~150 words. Briefly acknowledges a small set of supporting
characteristics — translation, training, the office of teaching, the
act of insisting — that play a part in the inner life of cognition
without themselves being inner-being characteristics. Notes these
are not treated at full depth in chapters 4 through 6.]

---

## 3. The divine pattern

[~1500–2500 words of AI-written prose. The cluster-wide arc:

Across the verse evidence for almost every characteristic in this
study, the same pattern holds. The characteristic is first God's own
attribute, then the human person's image of that attribute. Wisdom is
named as belonging to God himself (Dan 2:20); the wise person bears
the imprint of that divine quality. Understanding is named as God's
own — his understanding is unsearchable (Isa 40:28); the human faculty
of understanding images that infinite divine attribute in finite form.

[Continues for each characteristic, citing key verses, building the
case that this is fundamentally a cluster of divine attributes that
the human inner being is created to image and participate in.]

[Includes a paragraph on the exception — meditative and reflective
activity (M15-F) is the one characteristic in this study where Scripture
is largely silent on God's own meditation. This silence is itself a
finding: meditation is named as the characteristically creaturely
response to what God has given.]

[Closes by drawing the cluster-wide implication: when these
characteristics work together in the human person, they constitute
the inner being's participation in God's own knowing.]

---

## 4. Where each characteristic lives in the person

[Each section is 800–1500 words. CC pre-extracts the evidence
specific to that characteristic; AI writes the synthesis prose.]

### 4.1 Wisdom: a settled inner orientation seated in the heart

[~1000 words. Where the verse evidence shows wisdom lives in the
person — the heart primarily (Pro 16:23: "the heart of the wise
makes his speech judicious"); the constituted person as a whole
(the chokh.mah of Bezalel is a Spirit-given inner endowment);
the inner capacity that shapes the eye and the lip. Which inner
capacities does wisdom engage — perception (the wise see what
others miss), cognition (the wise reason rightly), memory (the
wise hold counsel), affect (the wise are restrained in anger),
agency (the wise act effectively).]

### 4.2 Understanding: the perceptive faculty of the receptive mind

[~1000 words. Heart-located (Pro 8:5: "you simple ones, learn
prudence; O fools, learn sense"); engages perception primarily,
cognition derivatively; can be hardened (Heb 5:11–12). The receptive
character of understanding sets it apart from the constitutive
character of wisdom.]

### 4.3 Knowledge: inner content held in the knowing self

[~1000 words. Lives in the inner person as both held content
(da.at as something one possesses) and as relational orientation
(knowing God as a state of the heart and soul). Engages memory,
cognition, and conscience.]

### 4.4 Discernment and practical judgement

[~1000 words. The applied edge of understanding. Where it lives,
which faculties it engages, how the evidence shows it operating.]

### 4.5 Deliberative planning and purposive intent

[~1000 words.]

### 4.6 Meditative and reflective inner activity

[~1000 words.]

### 4.7 Inner thought-content

[~1000 words.]

### 4.8 The Word that engages the inner being

[~1000 words. Logos as it enters the inner person (Col 3:16: "the
word of Christ dwell in you richly"); blinds and renews; the inner-
being-addressing force of divine speech.]

---

## 5. How each characteristic works

[Each section 800–1500 words. Same structure — per characteristic,
how it moves between God and person, how it is formed and deepens
through time and through suffering, how it modes of operation differ
across contexts.]

### 5.1 Wisdom: received from God, grown through fear of him, expressed through speech and conduct
### 5.2 Understanding: gained by seeking, deepened by suffering, blocked by hard-heartedness
### 5.3 Knowledge: covenant knowing as the operative form; informational knowing as its derivative
### 5.4 Discernment in action: trained through practice, sharpened by trial
### 5.5 Deliberative planning: divine purpose as the model, human counsel as its image
### 5.6 Meditation: the inner response to what God has given — by remembering, by pondering, by inner self-reasoning
### 5.7 Inner thought-content: what can be guarded, what can be corrupted, what can be brought captive
### 5.8 The Word's inner work: bringing salvation, dividing the inner being, guarding the heart

---

## 6. How each characteristic relates to the others

[Each section 400–800 words. Per characteristic — what is adjacent,
what is opposite, what produces it, what it produces.]

### 6.1 Wisdom in relation to understanding, discernment, and folly
### 6.2 Understanding in relation to wisdom, knowledge, and hardness
### 6.3 Knowledge in relation to wisdom, faith, and spiritual ignorance
### 6.4 Discernment in relation to understanding and conscience
### 6.5 Planning and intent in relation to wisdom, providence, and adversarial scheming
### 6.6 Meditation in relation to memory, prayer, and the word
### 6.7 Inner thought-content in relation to heart, will, and adversarial influence
### 6.8 The Word in relation to wisdom, knowledge, and the inner faculties

---

## 8. What this study does not yet address

[~300 words of honest accounting. Two strands:

- The Greek-of-the-Hebrew (the LXX) treatment of each characteristic's
  vocabulary remains parked. A specific Logos Bible Software research
  session will pick that up.

- One area of cross-characteristic comparison (how characteristics
  share inner dimensions with each other) requires further
  data-gathering before it can be addressed.

- Identifies the consistent silences in the verse evidence that are
  themselves analytically significant — most prominently, that the
  meditative inner activity of the human person is largely silent
  about God's own meditation, marking that activity as characteristically
  creaturely.]

---

## Appendix A — Key verses by characteristic

[Generated table: 55 rows. Columns: Characteristic | Meaning-group |
Reference | Hebrew/Greek + transliteration | Verse text. No prose.]

---

## Appendix B — Method note

[~150 words of plain-English prose acknowledging that the study draws
from a structured analytical record covering 189 lines of inquiry
across the verse evidence for each characteristic, with key verses
selected as evidential foundation. The analytical record is held in
the project's database and is the source for every claim in the
chapters above. No claim in the chapters above is made without specific
verse evidence behind it.]
```

---

## 8. What changed from v2 → v3

| Item | v2 | v3 |
|---|---|---|
| Pipeline | Assumed per-word Session C continued | Per-word Session C removed |
| Audience | "Intelligent non-specialist" but used jargon | Plain English; explicit list of jargon to avoid |
| Length envelope | 6,000–10,000 words capped | No cap; comprehensiveness wins |
| Chapter 4 | T2+T3 across all sub-groups (one chapter) | Per-characteristic deep dive (9 sections in one chapter) |
| Chapter 5 | T4+T5 across all sub-groups | Per-characteristic, 9 sections |
| Chapter 6 | T6 across all sub-groups | Per-characteristic, 9 sections |
| Chapter 7 | Per-sub-group brief treatments | **Removed** — absorbed into 4-6 |
| Chapter 8 | Honest accounting | Same |
| Tier names | "T0", "T2", etc. exposed | Thematic names only; tier codes invisible to the reader |
| BOUNDARY | Section in Chapter 7 | Section in Chapter 2; no Chapters 4–6 treatment |
| Length for M15 | ~6k–10k | ~25k–35k |

---

## 9. What needs the researcher's call before the instruction can be drafted

Three remaining questions:

1. **Cluster-wide synthesis pulled forward into Chapter 1.** The cluster-synthesis findings (M15 has 23) are the most analytically dense items in the analytical record. The current skeleton uses them in Chapter 1, Chapter 3 spine, and Chapter 6 closer. Should they be more prominent in Chapter 1 (a long opening that establishes the cluster-wide arc), or stay distributed?

2. **Filling M15-H's missing description.** The Logos characteristic has no `core_description` in DB. Before the publication can include §4.8 / §5.8 / §6.8, that description must be authored and applied. Suggest: I draft a one-sentence description, you approve, small directive applies it.

3. **Cluster-synthesis findings in their published voice.** When AI weaves these 23 findings into chapters, should the prose acknowledge them ("the evidence shows a consistent pattern …") or quote them where strongest ("As the evidence across these characteristics together makes plain: …")? Possibly a mix; possibly a stylistic choice for the AI.

---

## 10. Suggested next step

If the chapter structure and the data mapping in this v3 hold, I can:

1. Fill M15-H's description (one-line author + one-directive apply).
2. Author `_generate_cluster_session_c_framework.py` — produces the framework file for M15. Output: a single complete framework `.md` with all evidence pre-extracted and all AI-write zones marked.
3. Run it. The output is what would be passed to Claude AI to author the prose.

The framework file is the concrete test of whether this design holds. If something is awkward to assemble or read in the framework, the design needs to flex; the cleanup is cheap at design stage, expensive after AI writes the prose.
