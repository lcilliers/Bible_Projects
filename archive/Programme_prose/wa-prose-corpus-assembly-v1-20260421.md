# wa-prose-corpus-assembly-v1-20260421

> Framework B Soul Word Analysis Programme — Programme Prose Corpus (Working Assembly)
> Session reference: prose
> Session date: 2026-04-21 (last updated; preamble + chapter 1 six sub-sections all APPROVED; 1.3 wider-programme dropped per researcher message 13)
> Previous output: all approved draft files (see status table)
> Governed by: wa-global-general-rules [current]; closed-corpus rule (session `prose` message 8)

---

## Purpose of this document

This is the working assembly of the programme prose corpus. It collects approved prose bodies in reading order as they are agreed, outside the database, until they reach the gates that allow them to enter `prose_section` (schema enablement directive; PROSE patches). When that process completes, the DB becomes authoritative and this document becomes a working mirror — useful for drafting but no longer the source of truth.

This document also anticipates the automated compiled document that the prose store is designed to produce. Its structure — preamble at top, six macro areas in sequence, sub-sections in their agreed order — matches what that compiled output will look like.

**Closed-corpus rule in effect.** Per researcher direction, the prose corpus must be self-sufficient. Nothing essential to understanding the programme exists outside the prose sections and their metadata. Bodies in this assembly honour that rule: external references point outward, they do not substitute for content that should live in the prose itself.

---

## Document assembly status

| Area | Sub-section / record | Status | Word count | Source draft |
|---|---|---|---|---|
| 0 | `preamble` — Programme Preamble | **APPROVED** | 365 | wa-prose-draft-preamble-v2-20260421 |
| 1 | `prog_purp_mission` — Mission | **APPROVED** | 178 | wa-prose-draft-purp-mission-v2-20260421 |
| 1 | `prog_purp_scope` — Scope | **APPROVED** | 200 | wa-prose-draft-purp-scope-v1-20260421 |
| 1 | `prog_purp_this_inner_being_programme` — This Inner-Being Programme | **APPROVED** | 395 | wa-prose-draft-purp-thisprog-v1-20260421 |
| 1 | `prog_purp_defining_inner_being` — Defining Inner Being | **APPROVED** | 470 | wa-prose-draft-purp-definition-v1-20260421 |
| 1 | `prog_purp_science_and_bible` — Science and the Bible | **APPROVED** | 535 | wa-prose-draft-purp-scienceandbible-v1-20260421 |
| 1 | `prog_purp_expected_outcome` — Expected Outcome | **APPROVED** | 530 | wa-prose-draft-purp-outcome-v1-20260421 |
| 2 | (Research methodology sub-sections, 7) | not yet drafted | — | — |
| 3 | (Research approach sub-sections, 10) | not yet drafted | — | — |
| 4 | (Data architecture sub-sections, 9) | not yet drafted | — | — |
| 5 | (Data integrity & governance sub-sections, 6) | not yet drafted | — | — |
| 6 | (Instruction corpus sub-sections, 7) | not yet drafted | — | — |

Status values: `APPROVED` (researcher has accepted the body, ready for DB entry when gates clear); `under review` (body drafted, awaiting researcher response); `in drafting` (being written now); `not yet drafted` (placeholder only).

---

---

# Programme Preamble

*`prose_section_type.code` = `preamble` | `chapter_no` = 0 | `sort_order` = 1*

The programme prose describes the entire research programme — what it is, how it fits together, and how it intends to unfold. It is the programme's narrative memory: the account that a reader encountering the work for the first time can use to understand what the programme is, what it produces, and the disciplines by which it operates.

This prose is not the place for detailed instructions on how to perform specific elements of the work. Procedural content — the exact format of a patch, the step sequence for executing a directive, the completeness tests applied at an inflection point — lives in the instruction documents and the global rules, which are the programme's binding and procedural sources. The prose describes; the instructions bind. A drafter who finds themselves specifying how a task is performed, rather than what the task is and why it exists, has crossed into territory that belongs to an instruction document. This boundary is deliberate and load-bearing: the prose corpus is intended to stand on its own as a coherent description, and instructions are intended to stand on their own as the working procedures. Neither is a substitute for the other.

The corpus covers six broad areas. It begins with the programme's purpose — the governing question, how inner being is defined, where this study sits within the researcher's wider work, and what a successful outcome would look like. It then describes the research methodology and the pipeline through which work moves, from word selection to publication. It sets out the disciplines, tools, and evidential principles by which the programme operates — how findings are distinguished from hypotheses, how the two-AI division of responsibility functions, how memory is managed across sessions. It describes the shape of the data the programme produces and the architecture that holds it — the registry, the terms, the verse groups, the dimensional profiles, the question catalogue. It covers the governance that keeps that data correct over time — the soft-delete discipline, validation standards, backup regime, patch-failure protocol. And it describes the instruction corpus itself: how rules and instructions are versioned, referenced, and updated, and how the programme's authority structure operates.

Within each area, individual prose records describe specific components in enough detail that a reader can understand the component without leaving the prose corpus. The corpus is designed to be self-sufficient as a narrative account of the programme — every piece of information a reader needs to understand what the programme is should be present here. Where a record points outward to a rule, an instruction, or a schema table, the pointer exists to allow the reader to reach the binding source, not to substitute for content the prose should itself contain.

---

---

# 1. Programme Purpose

*Macro area framing to be drafted after sub-sections complete.*

## 1.1 Mission

*`prose_section_type.code` = `prog_purp_mission` | `chapter_no` = 1 | `sort_order` = 2 | Status: APPROVED | Source draft: wa-prose-draft-purp-mission-v2-20260421*

This research programme began in January 2026 from a desire to understand the human spirit, soul, and body more deeply than existing accounts allowed. As the work developed, a conviction settled: an honest account of the human inner being is incomplete without a parallel account of the Holy Spirit. The two stand in relation to one another — the human inner life is shaped, inhabited, and addressed by the Spirit throughout Scripture — and neither can be studied at depth while leaving the other undefined.

The mission that followed was straightforward in statement and substantial in commitment: take a deep dive. Investigate both subjects on their own terms; let Scripture lead the evidence; hold the enquiry open long enough to reach findings rather than assumptions. The commitment produced two elaborate documents, each a collection of deep-dive studies in its own right:

- **Framework A — *The Holy Spirit: Origin, Nature, Work, Character, and Interaction. A Five-Thousand-Year Investigation from Genesis to the Present Day.*** An investigation of the Holy Spirit across the full biblical canon and beyond it into the receiving tradition.
- **Framework B — *Spirit, Soul, and Body: The Composition of Human Beings. A Comprehensive Biblical and Scientific Investigation.*** An investigation of the human person as Scripture describes the composition, and as scientific enquiry approaches the same subject from a different direction.

---

## 1.2 Scope

*`prose_section_type.code` = `prog_purp_scope` | `chapter_no` = 1 | `sort_order` = 3 | Status: under review | Source draft: wa-prose-draft-purp-scope-v1-20260421*

The advent of the Framework A and Framework B documents did not close the work. By February 2026, with both studies in a readable state, it had become clear that each would benefit from further research and refinement — in style and in depth. Further reading into Framework B's subject made the sharper point: the study had only touched the surface of what the soul actually consists of. A cursory overview counted some twenty-eight distinct characteristics — an order of magnitude short of what a careful treatment of the biblical evidence plainly contains.

That shortfall triggered a deliberate extension of scope: an in-depth exploration of the soul, set within the wider frame of the inner being so that soul, spirit, and body could be treated in their actual relation rather than in isolation. A thorough collation of Scripture's inner-being vocabulary was assembled — approximately two hundred English words, mapped to their Hebrew and Greek originals. That registry became the scope of the present focus of the programme. Every word in it is in scope; every word outside it is out of scope. The registry is the boundary, and the boundary is the basis on which everything downstream — verse selection, term classification, dimensional analysis, cross-registry synthesis — is defined.

---

## 1.4 This Inner-Being Programme

*`prose_section_type.code` = `prog_purp_this_inner_being_programme` | `chapter_no` = 1 | `sort_order` = 5 | Status: under review | Source draft: wa-prose-draft-purp-thisprog-v1-20260421*

The Soul Word Analysis Programme is the direct continuation of the work the two Frameworks began. It takes the registry of inner-being words — scope defined — and subjects each one to systematic examination: what the term means across its Hebrew and Greek originals, how it occurs across its verses, what contexts the occurrences share, what it contributes to the larger account of the inner person. The programme's intellectual frame is Framework B's; its scale and discipline are new. The earlier work was comprehensive and synthetic; this programme is corpus-level and analytical.

The unit of work is the word. For each word in the registry, the programme builds a complete analytical record — from the Strong's-level term data through the verse inventory and the occurrence contexts, into the characteristic patterns the verses reveal, through to a written word study and, beyond that, cross-registry synthesis. The work runs in phases. Each phase has a defined input, a defined output, and an inflection point at which the word is ready to move to the next phase. A word that has not satisfied the inflection point stays where it is; no phase is skipped; no assessment made at one phase is treated as final before the next phase confirms it.

The programme is organised around a two-agent architecture. The research judgement — what a verse is about, how a term functions in context, which dimensions of the inner being the evidence engages, what the written study should say — is held by the analytical agent working with the researcher. The database operations — extraction, classification persistence, patch application, extract production — are held by a separate operational agent. The separation is deliberate: analytical judgement is the programme's scarce resource, and the architecture protects it from the distraction of mechanical work. The two agents interact through structured artefacts — patches and directives — that make every database change reviewable by the researcher before it takes effect.

The programme's outputs have three orders. First-order outputs are the per-word records and written studies produced one word at a time. Second-order outputs are the cross-word syntheses that emerge when groups of words are examined together — clusters of related characteristics, recurrent patterns across the inner-being vocabulary, places where two frameworks of description illuminate each other. Third-order output is the programme-wide account that these syntheses contribute to: an in-depth description of the human inner being as Scripture reveals it, built from the bottom up on the evidence of every word in scope. The present prose corpus is itself part of that third-order work — the self-description that makes the programme's findings readable as a whole.

---

## 1.5 Defining Inner Being

*`prose_section_type.code` = `prog_purp_defining_inner_being` | `chapter_no` = 1 | `sort_order` = 6 | Status: under review | Source draft: wa-prose-draft-purp-definition-v1-20260421*

Before any word could be examined, a prior question had to be settled: what is being studied when Scripture's "inner-being" vocabulary is read word by word? The answer is the programme's working definition of inner-being characteristics — a single sentence, carefully composed, precise enough to test any English word for inclusion in the scope, broad enough to capture the full range of what Scripture describes.

**The definition.** *Inner-being characteristics are the non-physical, internal states, capacities, and expressions that constitute a person's invisible life — encompassing how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God.*

This is a working definition, not a theological statement. Theological accounts of the soul and spirit have been abundantly written; this programme does not add another to the list. What the programme needed instead was an evaluative filter: a formula that could be applied to any word in the English language and return a reliable yes-or-no on whether its meaning qualifies as inner-being content. The definition is that filter.

Three decisions are embedded in the definition and govern how it is applied. First, the *non-physical* test: bodily processes, external behaviours, and material realities do not qualify unless they are used to express an internal state. Weeping qualifies when it is Scripture's language for inner grief; walking does not qualify when it is only physical locomotion. Second, the *internal* test: states that originate within the person — capacities, dispositions, operations of mind and heart. The boundary here is porous because inner states can be caused by external agents, including God, other people, and spiritual forces, and the programme's analysis expects and examines that permeability. Third, the *operational range* — thinks, feels, chooses, relates, orients — which names the full working field of the inner person. These are not five sealed domains but five dimensions of a single integrated life.

The definition deliberately holds spirit and soul together under the term "inner being". Inner being is the totality of the person's non-physical existence — everything that is not the body, encompassing spirit and soul together. Soulish characteristics are a subset of that totality — the specific functions and expressions that belong to the *psyche / nephesh*: thought, emotion, will, desire, conscience, self-awareness. All soulish characteristics are inner-being characteristics; not all inner-being characteristics are soulish. The spiritual dimension — the person's orientation toward God, the capacity for divine encounter, the operations of the spirit — belongs to the inner being without being reducible to soul function. Whether a given word belongs primarily to the soul domain, primarily to the spirit domain, or to the boundary between them is one of the research questions the programme is designed to answer — not a premise it brings to the text.

A governing rule of application extends the definition's reach. Borderline words are included, not excluded. Where a word sits close to the edge of the definition, the programme includes it and flags the borderline status for later review. The cost of over-inclusion is visible and recoverable; the cost of silent omission is invisible and not recoverable. Completeness is chosen over tidiness, and the filter errs on the side of admitting words that may later be ruled out rather than excluding words that should have been ruled in.

---

## 1.6 Science and the Bible

*`prose_section_type.code` = `prog_purp_science_and_bible` | `chapter_no` = 1 | `sort_order` = 7 | Status: under review | Source draft: wa-prose-draft-purp-scienceandbible-v1-20260421*

The subject this programme investigates — the human inner being — is not studied only by Scripture. Neuroscience, psychology, physiology, behavioural science, and other empirical fields examine the same territory from a different direction. The programme holds both accounts open, not by accident and not as a concession, but as a deliberate methodological stance: Scripture and science together provide a fuller picture of the human person than either one produces on its own.

The two accounts are not of equal weight in this programme. Scripture is the primary lens; science is the second lens. Framework B is biblical research — its primary data is the biblical text, its primary method is lexical and contextual analysis, its conclusions are grounded in and accountable to what Scripture says. The scientific literature is engaged to illuminate, ground, and sometimes challenge the biblical account, not to generate an independent parallel dataset of equal authority. The distinction matters because a co-equal scientific programme would require a second corpus-level effort as large as the biblical one; a second-lens engagement requires disciplined, targeted use of what science has already established.

Each lens provides what the other cannot. Scripture carries the theological frame that science has no instrument for: the human being created by God, bearing the divine image, corrupted by sin, being renewed by the Spirit. Scripture names the divine dimension — God as active agent within the inner life, who causes, sustains, judges, and transforms inner states. Scripture speaks of realities that empirical observation cannot reach: conscience, worship, the fear of the Lord, the operations of the Spirit, spiritual oppression and freedom. Science, for its part, provides empirical grounding — the observable expressions, biological substrates, and measurable patterns of inner life. Science describes how inner states are implemented in the body: the neurochemistry of fear, the physiology of grief, the neural correlates of shame, the brain-body systems through which cognition and emotion operate. Science offers phenomenological depth on what inner states feel like, how they develop, and what conditions produce or diminish them. And science provides a contemporary bridge: the programme's findings need to be readable by people living now, and scientific grounding gives them traction in present conversation.

Where the two accounts converge, the convergence is significant — two very different instruments pointing at the same reality. Where they diverge, the divergence is equally significant and is named rather than papered over. The programme identifies three kinds of convergence — phenomenological (the same experience described from different angles), mechanistic (science describing the how of what Scripture describes as a reality), and structural (the architecture of the inner life having the same shape in both accounts). It identifies three kinds of divergence — register divergence (the accounts addressing different levels of the same reality and only appearing to conflict), reductive divergence (a scientific account that loses dimensions the biblical account treats as primary), and genuine divergence (claims in actual tension that cannot be harmonised by reframing). The discipline is honest engagement, not forced harmonisation.

Three principles govern the interaction of the two lenses. Scripture is not subordinate to science, and science is not subordinate to Scripture; they are different instruments addressing different aspects of the same reality, and neither should be forced into the other's register. The scientific account addresses the creaturely dimension of the inner being — what can be observed, measured, described from outside — while the biblical account addresses the full dimension, including the theological and spiritual realities that are invisible to empirical observation. The goal is not harmonisation but honest engagement: where science says something the biblical account does not address, the observation is noted; where science says something that appears to contradict the biblical account, the apparent contradiction is examined carefully rather than quickly resolved in either direction.

---

## 1.7 Expected Outcome

*`prose_section_type.code` = `prog_purp_expected_outcome` | `chapter_no` = 1 | `sort_order` = 8 | Status: under review | Source draft: wa-prose-draft-purp-outcome-v1-20260421*

Success for this programme has a definite shape. At the level of the individual word, it is a written study that treats the word on its own terms — what the term means across its Hebrew and Greek originals, how its occurrences distribute across Scripture, what contexts and characteristics the verses reveal, how the term engages the spirit-soul-body continuum, how the biblical account and the relevant scientific literature relate at the point this word occupies. The study stands on its own: a reader encountering a single word study gains a considered account of that aspect of the inner being, grounded in the evidence and transparent about what remains uncertain.

At the level of the corpus, success is the accumulation of these studies into a set that covers the inner-being vocabulary comprehensively, together with the cross-word syntheses that become possible only once the individual work is complete. When a word has been studied, its relationship to adjacent words — the ones it overlaps with, the ones it opposes, the ones that cause or are caused by it — becomes newly visible. When groups of words have been studied, patterns across the vocabulary emerge: clusters of related characteristics, recurrent structural features, places where two concepts turn out to be different angles on a single reality or where one concept splits into two that had been wrongly conflated. These syntheses are not added on top of the word studies; they are latent in them, and cross-registry analysis is the instrument that surfaces them.

At the level of the programme as a whole, success is a sustained and defensible account of the human inner being as Scripture reveals it — assembled from the bottom up, word by word, on the evidence of the biblical text, in honest engagement with what contemporary science observes of the same territory. Such an account is not the final word on any of its subjects; no such word is achievable from inside a research programme. It is, rather, a careful description that is accountable to the evidence it is built on, open about its boundary cases and unresolved questions, and structured so that subsequent work — the researcher's or another's — can extend or correct it from the same base.

The programme's audience is not primarily academic, though the work should be defensible in an academic setting. The intended readers are people who care about the subject — teachers, practitioners, thoughtful readers who have encountered Scripture's vocabulary of the inner life and want a careful treatment of it. The work is written for them: theologically serious without being technical for its own sake, empirically grounded without being reductively scientific, slow enough to treat its subject with respect, structured enough to be navigated rather than merely read through.

The programme will be judged a success if three things are true of its completed output. First, the account it produces is demonstrably grounded in the evidence — every substantive claim can be traced back to the verses, terms, and contextual patterns that produced it. Second, the account is open where the evidence is open — unresolved questions are named as unresolved, inferences are labelled as inferences, and the reader is trusted to work with provisional findings rather than protected from them. Third, the account is useful — it changes how someone reading it thinks about the subject, gives them vocabulary and distinctions they did not previously have, and equips them to read Scripture's inner-being texts with sharper attention.

---

---

# 2. Research Methodology

*All sub-sections not yet drafted.*

---

# 3. Research Approach

*All sub-sections not yet drafted.*

---

# 4. Data Architecture

*All sub-sections not yet drafted.*

---

# 5. Data Integrity & Governance

*All sub-sections not yet drafted. Items 29 (`prog_validation_standard` → `prog_gov_validation`) and 33 (`prog_patch_failure_protocol` → `prog_gov_patch_failure`) have v1 drafts on disk requiring rework under the closed-corpus rule.*

---

# 6. Instruction Corpus

*All sub-sections not yet drafted.*

---

---

## Assembly discipline

New approved bodies are inserted in their agreed sequence position. The status table at the top of this document is updated in the same edit. Every addition carries a reference back to its source-draft file for audit. Superseded versions move to a *Superseded* section at the foot of this document (to be created when needed) — never silently overwritten.

When the corpus is complete enough for the seeding and schema-enablement patches, this document becomes the reading-order authority used to construct the CATALOGUE_POPULATION patch (section types + metadata) and the PROSE patches (bodies) that transfer the corpus into `prose_section`.

---

*wa-prose-corpus-assembly-v1-20260421 | Working assembly of approved programme prose bodies*
