# Prose Extract — Programme — 2026-11-21

_Schema 3.40.0 · source: `prose_section_type` + `prose_section`._

---

## Summary

**Section types seeded:** 51  ·  **Content sections populated:** 51

---

# Programme

## Preamble

### Programme Preamble

> Opening orientation for the programme prose: what the prose is, the line between description and procedure, the six areas of the corpus and the style of the prose.

_`preamble`  ·  type id 35  ·  chapter_no 0  ·  sort 1_

*Section id 15 · status `draft` · v1469 · 564 words · author `claude_code`*

The programme prose describes the research programme: what it is, how it fits together, and how it operates. It is the programme's narrative description and the authoritative record of the programme, written to stand on its own: a reader encountering the work for the first time can use it to understand what the programme is, what it produces, and the disciplines by which it operates.

The prose is not the place for instructions on how to perform specific tasks. Procedural content, such as how a step is run, the format of a patch, or the checks a step must pass, lives in the application's configuration, `iba/app/USER-GUIDE.md` and `iba/app/GOVERNANCE.md`. The prose describes the programme; the application directs the work.

The corpus covers six areas. **Area 1** is the programme's purpose: the governing question, how the inner being is defined, where this study sits within the researcher's wider work, what a successful outcome looks like, the framework of enquiry that records each finding as an observation, and the relationship between Scripture and contemporary science as the two lenses through which the inner being is studied. **Area 2** is the research method: the five parts from the text and its data, through the vocabulary, the reading and the account, to publishing; the collection as the unit of study; the stages of the analysis, with the unit each reads, how volume and fallout are handled, where the programme stands and what is not yet defined; the role of science in the claims reading; the principles that govern every stage; and the constraints the programme deliberately accepts. **Area 3** is the disciplines, tools and evidential principles by which the programme operates: how findings are distinguished from hypotheses, how the researcher's authority and Claude's interpretation of the evidence divide, how continuity is kept across sessions, and how scope integrity is held. **Area 4** describes the data architecture: the two databases, the base data, the surfaces and collections, the node and the observation tables, the claims and the narrative, and the prose store. **Area 5** covers the governance that keeps the data correct over time: validation, the soft-delete discipline, consistency with sources, backup and schema discipline, failure protocols, the route by which a rule changes, and the alignment of documents with the configuration. **Area 6** describes the instruction corpus: where the rules live and how patches, directives, the operating guidance and the procedures of each part of the study are held.

Individual prose records within each area describe specific components in enough detail that a reader can understand the component without leaving the corpus. Where a record points outward to a rule, a document or a table, the pointer serves the reader reaching the binding source.

**On style.** The programme's prose is direct and factual. Every sentence is either a statement about the programme or carries information the reader needs. The prose avoids framing that introduces rather than states, motive attribution, rhetorical closings, and metaphors layered on facts. Where the researcher has articulated a principle in their own words, those words are used. Factual claims are traceable to their sources: the database, the configuration and the written record. A count is not written into the prose, because it goes stale; the prose points to the report that holds it. This style carries forward through every section of the corpus and is the reference register for all future prose additions and revisions.


## Programme purpose

### Mission

> The programme's originating mission — why the research began, the theological conviction that shaped its scope, and the two Framework documents it produced.

_`prog_purp_mission`  ·  type id 36  ·  chapter_no 1  ·  sort 2_

*Section id 2 · status `draft` · v92 · 178 words · author `claude_ai`*

This research programme began in January 2026 from a desire to understand the human spirit, soul, and body more deeply than existing accounts allowed. As the work developed, a conviction settled: an honest account of the human inner being is incomplete without a parallel account of the Holy Spirit. The two stand in relation to one another — the human inner life is shaped, inhabited, and addressed by the Spirit throughout Scripture — and neither can be studied at depth while leaving the other undefined.

The mission that followed was straightforward in statement and substantial in commitment: take a deep dive. Investigate both subjects on their own terms; let Scripture lead the evidence; hold the enquiry open long enough to reach findings rather than assumptions. The commitment produced two elaborate documents, each a collection of deep-dive studies in its own right:

- Framework A — *The Holy Spirit: Origin, Nature, Work, Character, and Interaction. A Five-Thousand-Year Investigation from Genesis to the Present Day.* An investigation of the Holy Spirit across the full biblical canon and beyond it into the receiving tradition.
- Framework B — *Spirit, Soul, and Body: The Composition of Human Beings. A Comprehensive Biblical and Scientific Investigation.* An investigation of the human person as Scripture describes the composition, and as scientific enquiry approaches the same subject from a different direction.


### Scope

> The scope of the study: the ESV surfaces of the groups behaviour and inner_being_state, each in one collection, and how scope is settled and changed.

_`prog_purp_scope`  ·  type id 37  ·  chapter_no 1  ·  sort 3_

*Section id 3 · status `draft` · v1387 · 252 words · author `claude_code`*

The study's scope is the vocabulary of the English Standard Version (ESV) that describes the workings of the human inner being. Each English word or phrase of the ESV is a *surface*. A surface is first sorted, by what it names, into one of four *surface groups*: behaviour, inner_being_state, entity or other. The surfaces of the groups behaviour and inner_being_state that occur in a verse are the study's scope, and each of them belongs to exactly one *collection*. A word that is neither a behaviour nor an inner-being state is not a surface of a collection; the entity and other surfaces enter the study only as the words that stand with a collection's surfaces in its verses.

A collection gathers surfaces of like meaning, whether synonyms, opposites or associated words, together with the derived forms and phrases that carry the same concept, and is named for the concept its members share. A verse is in scope when it holds an occurrence of a member surface of a collection. Each surface is linked to the Hebrew and Greek words (Strong's codes) behind it, so that the English the reader holds is read against the original text it translates.

Scope is settled from evidence. A change to a collection is made class by class, on a copy, with its effect predicted and checked, and every change is kept with its reason. A word found wrongly placed is moved and the move is processed, so that the completeness checks of the study continue to hold.


### This Inner-Being Programme

> What the programme is: its unit of study and of reading, its working agent and the researcher's authority, the application that controls it and its three levels of output.

_`prog_purp_this_inner_being_programme`  ·  type id 38  ·  chapter_no 1  ·  sort 4_

*Section id 4 · status `draft` · v1470 · 355 words · author `claude_code`*

The programme is the direct continuation of the work the two Frameworks began. Its intellectual frame is Framework B's; its scale and discipline are new. The earlier work was comprehensive and synthetic; this programme is corpus-level and analytical, and it is built from the bottom up on the evidence of the biblical text.

The unit of study is the *collection*, and the unit of reading within it is the *subgroup* of its surfaces. Each collection is taken through the whole path: its surfaces are grouped into subgroups, each subgroup is read in layers, first for lexical meaning and then for the working of the inner being, and claims are formulated from the inner-being observations. What the study finds for a collection becomes a chapter of the narrative that carries the account to its readers. Chapter 2 describes the stages, and its section on the programme flow states where the programme stands and what is not yet defined.

The programme has one working agent, Claude, directed by the researcher. Claude reads the evidence and, in most cases, decides what it settles; the researcher scrutinises that judgement and settles what the evidence cannot. Every interpretation is backed by evidence that can be traced to its verses and sources. A model on a local server is used as a controlled tool for judging words, and everything it gives is inferential until the researcher confirms it.

The whole programme is controlled by the IBA application. Every operation is a registered step, every rule is a configuration row, and every change keeps its state before and after. The project lives in its databases: the observations, claims and narrative held there are the project's results, and files are working documents or exports.

The programme's outputs have three levels. Observations tie what the text shows to its verses, words and surfaces. Claims are statements that go beyond the bare text, each held with its sources. The narrative is the programme-wide account of the human inner being as Scripture reveals it, assembled from the claims. The present prose is part of that account: the self-description that makes the programme readable as a whole.


### Defining Inner Being

> The programme's working definition of inner-being characteristics — verbatim, with the three boundary decisions embedded in it, the spirit/soul distinction it holds open, and the inclusion rule that governs its application.

_`prog_purp_defining_inner_being`  ·  type id 39  ·  chapter_no 1  ·  sort 6_

*Section id 5 · status `draft` · v95 · 470 words · author `claude_ai`*

Before any word could be examined, a prior question had to be settled: what is being studied when Scripture's "inner-being" vocabulary is read word by word? The answer is the programme's working definition of inner-being characteristics — a single sentence, carefully composed, precise enough to test any English word for inclusion in the scope, broad enough to capture the full range of what Scripture describes.

**The definition.** *Inner-being characteristics are the non-physical, internal states, capacities, and expressions that constitute a person's invisible life — encompassing how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God.*

This is a working definition, not a theological statement. Theological accounts of the soul and spirit have been abundantly written; this programme does not add another to the list. What the programme needed instead was an evaluative filter: a formula that could be applied to any word in the English language and return a reliable yes-or-no on whether its meaning qualifies as inner-being content. The definition is that filter.

Three decisions are embedded in the definition and govern how it is applied. First, the *non-physical* test: bodily processes, external behaviours, and material realities do not qualify unless they are used to express an internal state. Weeping qualifies when it is Scripture's language for inner grief; walking does not qualify when it is only physical locomotion. Second, the *internal* test: states that originate within the person — capacities, dispositions, operations of mind and heart. The boundary here is porous because inner states can be caused by external agents, including God, other people, and spiritual forces, and the programme's analysis expects and examines that permeability. Third, the *operational range* — thinks, feels, chooses, relates, orients — which names the full working field of the inner person. These are not five sealed domains but five dimensions of a single integrated life.

The definition deliberately holds spirit and soul together under the term "inner being". Inner being is the totality of the person's non-physical existence — everything that is not the body, encompassing spirit and soul together. Soulish characteristics are a subset of that totality — the specific functions and expressions that belong to the *psyche / nephesh*: thought, emotion, will, desire, conscience, self-awareness. All soulish characteristics are inner-being characteristics; not all inner-being characteristics are soulish. The spiritual dimension — the person's orientation toward God, the capacity for divine encounter, the operations of the spirit — belongs to the inner being without being reducible to soul function. Whether a given word belongs primarily to the soul domain, primarily to the spirit domain, or to the boundary between them is one of the research questions the programme is designed to answer — not a premise it brings to the text.

A governing rule of application extends the definition's reach. Borderline words are included, not excluded. Where a word sits close to the edge of the definition, the programme includes it and flags the borderline status for later review. The cost of over-inclusion is visible and recoverable; the cost of silent omission is invisible and not recoverable. Completeness is chosen over tidiness, and the filter errs on the side of admitting words that may later be ruled out rather than excluding words that should have been ruled in.


### Science and the Bible

> The programme's two-lens architecture — Scripture as primary lens, science as second lens — what each provides and cannot provide, the convergence and divergence framework, and the governing principles of their interaction.

_`prog_purp_science_and_bible`  ·  type id 40  ·  chapter_no 1  ·  sort 7_

*Section id 6 · status `draft` · v1389 · 671 words · author `claude_code`*

The subject this programme investigates — the human inner being — is not studied only by Scripture. Neuroscience, psychology, physiology, behavioural science, and other empirical fields examine the same territory from a different direction. The programme holds both accounts open, not by accident and not as a concession, but as a deliberate methodological stance: Scripture and science together provide a fuller picture of the human person than either one produces on its own.

The two accounts are not of equal weight in this programme. Scripture is the primary lens; science is the second lens. Framework B is biblical research — its primary data is the biblical text, its primary method is lexical and contextual analysis, its conclusions are grounded in and accountable to what Scripture says. The scientific literature is engaged to illuminate, ground, and sometimes challenge the biblical account, not to generate an independent parallel dataset of equal authority. The distinction matters because a co-equal scientific programme would require a second corpus-level effort as large as the biblical one; a second-lens engagement requires disciplined, targeted use of what science has already established.

Each lens provides what the other cannot. Scripture carries the theological frame that science has no instrument for: the human being created by God, bearing the divine image, corrupted by sin, being renewed by the Spirit. Scripture names the divine dimension — God as active agent within the inner life, who causes, sustains, judges, and transforms inner states. Scripture speaks of realities that empirical observation cannot reach: conscience, worship, the fear of the Lord, the operations of the Spirit, spiritual oppression and freedom. Science, for its part, provides empirical grounding — the observable expressions, biological substrates, and measurable patterns of inner life. Science describes how inner states are implemented in the body: the neurochemistry of fear, the physiology of grief, the neural correlates of shame, the brain-body systems through which cognition and emotion operate. Science offers phenomenological depth on what inner states feel like, how they develop, and what conditions produce or diminish them. And science provides a contemporary bridge: the programme's findings need to be readable by people living now, and scientific grounding gives them traction in present conversation.

Where the two accounts converge, the convergence is significant — two very different instruments pointing at the same reality. Where they diverge, the divergence is equally significant and is named rather than papered over. The programme identifies three kinds of convergence — phenomenological (the same experience described from different angles), mechanistic (science describing the how of what Scripture describes as a reality), and structural (the architecture of the inner life having the same shape in both accounts). It identifies three kinds of divergence — register divergence (the accounts addressing different levels of the same reality and only appearing to conflict), reductive divergence (a scientific account that loses dimensions the biblical account treats as primary), and genuine divergence (claims in actual tension that cannot be harmonised by reframing). The discipline is honest engagement, not forced harmonisation.

Three principles govern the interaction of the two lenses. Scripture is not subordinate to science, and science is not subordinate to Scripture; they are different instruments addressing different aspects of the same reality, and neither should be forced into the other's register. The scientific account addresses the creaturely dimension of the inner being — what can be observed, measured, described from outside — while the biblical account addresses the full dimension, including the theological and spiritual realities that are invisible to empirical observation. The goal is not harmonisation but honest engagement: where science says something the biblical account does not address, the observation is noted; where science says something that appears to contradict the biblical account, the apparent contradiction is examined carefully rather than quickly resolved in either direction.

In the programme's method the science reading is part of the claims reading. It is engaged after the biblical reading of a collection is complete, as the second lens, and not as a separate pass or in parallel with the biblical reading (Chapter 2).


### Expected Outcome

> What success looks like for a collection, for the corpus and for the programme, the intended audience and the three criteria by which the finished output is judged.

_`prog_purp_expected_outcome`  ·  type id 41  ·  chapter_no 1  ·  sort 8_

*Section id 7 · status `draft` · v1446 · 409 words · author `claude_code`*

Success for this programme has a definite shape. For a collection, it is a completed reading: its surfaces grouped into subgroups, every subgroup read in its verses for the lexical meaning of its surfaces and for how they relate to one another and to the other words of the verse, the working of the inner being read from those observations, and the claims formulated with their sources. A reader of the chapter that results gains a considered account of that part of the inner being, grounded in the evidence and open about what remains uncertain.

For the corpus, success is the accumulation of these readings across the collections, so that the inner-being vocabulary of the ESV is covered and the relations between collections become visible: the words that stand together, the collections that overlap or oppose, the places where one concept splits into two that had been conflated. These relations are found in the observations; they are not added on top of them.

For the programme as a whole, success is a sustained and defensible account of the human inner being as Scripture reveals it, assembled from the bottom up on the evidence of the biblical text and in honest engagement with what contemporary science observes of the same territory. It is not the final word on any of its subjects; it is a careful description, accountable to the evidence it rests on, open about its boundary cases, and structured so that later work can extend or correct it from the same base.

The programme's audience is not primarily academic, though the work should be defensible in an academic setting. The intended readers are people who care about the subject: teachers, practitioners and thoughtful readers who want a careful treatment of Scripture's vocabulary of the inner life. The work is theologically serious without being technical for its own sake, empirically grounded without being reductively scientific, and structured to be navigated as well as read through.

The programme is a success if three things are true of its completed output. First, the account is demonstrably grounded in the evidence: every substantive claim traces back to the verses, words and observations that produced it. Second, the account is open where the evidence is open: unresolved questions are named as unresolved and inferences are labelled as inferences. Third, the account is useful: it changes how a reader thinks about the subject and equips them to read Scripture's inner-being texts with sharper attention.


## Research methodology

### Research method

> The research method at a glance: its five parts from the text and its data to publishing, the collection as the unit of study, and the lens and sequencing commitments.

_`prog_meth_overview`  ·  type id 42  ·  chapter_no 2  ·  sort 9_

*Section id 8 · status `draft` · v1525 · 729 words · author `claude_code`*

The programme investigates what Scripture reveals about the human inner being. The method proceeds collection by collection from the biblical text, through a disciplined sequence that keeps data gathering, vocabulary, lexical reading, inner-being analysis and claim formulation apart, and that returns to the whole body of findings only through the claims built from them.

The method has five parts, each taking the output of the one before it and nothing else. **The text and its data.** Every verse of the Bible is held with its original-language words, their Strong's identities, meanings and a mechanical reading of the verse's structure that says nothing of what a word does for the inner being. This is the base data. **The vocabulary.** The English words and phrases of the ESV (the surfaces) are judged against the programme's working definition of the inner being, sorted into four surface groups, and the surfaces of the groups behaviour and inner_being_state are gathered into collections of like or related behaviour. **The reading.** A collection is too large to be read in one go, so it is divided into subgroups of its surfaces, and the subgroup is the unit of reading. Each subgroup is read in layers: first the lexical observations for its surfaces and their verses, then the lexical observations for how its surfaces relate in those verses, then the inner-being working made from both. Each finding is an observation tied to verses, words and surfaces by nodes, and each layer deposits its observations for the next layer to use. **The account.** Claims are formulated from the observations, each with its sources, and are told in the narrative, which follows the collections. **Publishing.** The narrative reaches its readers as an export from the database.

The collection is the unit of study. Each collection is taken through the whole path, and the account of a collection becomes a chapter of the narrative. Claude reads the evidence and decides in most cases; the researcher scrutinises that judgement and decides what the evidence cannot settle. No bulk or one-shot analysis, by Claude or by a model, produces the study result, because the nuances of the base data are too varied and interwoven to be reduced to a narrow band.

Scripture is the primary lens. The analytical work is work on the biblical text. Contemporary scientific literature on the inner life is held as a second lens and is engaged in the claims reading, after the biblical reading, as the section on science in action describes. Categories are not imposed on the data; they emerge from it, and a category that cannot be grounded in verse evidence is not one the programme uses. A finding that cannot be traced to a specific verse or lexical source is not a finding the programme records.

**The framework of enquiry.** The framework is the layered reading of a collection by its subgroups, in which each finding is recorded as an observation tied to the text. It serves one question: what the inner workings of the human being are as Scripture describes them, by characterising and grouping the inner characteristics, mapping their interrelationships, describing the spirit, soul and body boundary, and documenting the relational interfaces with God, other humans and other spiritual beings. It works as a discipline of consistent and complete enquiry: applied to every collection, it ensures that no part of the vocabulary is systematically missed and that findings are produced on the same footing across collections. What the framework could explore is open; the evidence determines what is found. Where Scripture is silent on an aspect, the silence is recorded and is not filled by inference or from other sources.

**The epistemological basis.** Scripture is the primary and governing source: what Scripture says is the finding. Original-language analysis, the Hebrew and Greek lexical and semantic study, is the primary evidential tool and is part of the Scripture source, not a separate one. The human sciences (psychology, moral philosophy, developmental psychology, sociology, anthropology, linguistics and hermeneutics) are an interpretive lens and a light sanity check. They are engaged in the claims reading, after the biblical reading, and add no content to a finding. Their engagement is selective and practical; a full treatment of any one field is a specialist's lifetime of work, and the programme does not attempt to replicate it. Everything produced by an AI is inferential until the researcher confirms it.


### Word selection: surfaces and collections

> How scope is built: the four surface groups, the surface cycle, the collections, and the caveats on each.

_`prog_meth_registry`  ·  type id 43  ·  chapter_no 2  ·  sort 10_

*Section id 9 · status `draft` · v1471 · 745 words · author `claude_code`*

The programme's scope is the set of surfaces: the English words and phrases of the ESV that name a behaviour or an inner-being state. A word enters the scope by being judged against the programme's working definition of the inner being, and that definition is the admission criterion.

The whole population of surfaces was sorted, by a process of deduction and likeness, into four surface groups: behaviour, inner_being_state, entity and other. The researcher's assessment is that this sorting is roughly nine in ten correct, within an accepted margin of error. The items placed wrongly are found in the deeper analysis and compensated for there; the sorting is not reopened to remove them first. Its purpose is to make the reading of the inner being's working possible: the first two groups hold the behaviours and states that are read, and the other two supply the words that stand with them in the verses.

Scope is built by the surface cycle, five modules that each read and write database tables and never a working file. The first, *group*, sorts each surface by what it names: behaviour (something a person does or undergoes, an act, feeling, thought, speech or choice), inner_being_state (a standing condition or characteristic of a person or of the inner being), entity (a thing that exists: a human, a plant or animal, God in all forms, an unseen power, or a part of any of these) or other (everything else). The second, *structure*, finds the base of a surface by the shape of the word. The third, *AI base*, proposes the base for the surfaces the shape leaves unmatched, through a model on a local server. The fourth, *resolve*, chooses the base from the evidence. The fifth, *collections*, forms the members of each core word's collection. Every change keeps its state before and after, together with the AI call and the prompt version that gave it, so that anything can be traced back. What a model gives is inferential until the researcher confirms it.

The surfaces of the groups behaviour and inner_being_state are then collated into collections by the likeness or relatedness of the behaviour they name. Each surface is connected, through the Strong's code of its base, with its verses, so a collection carries the verses of its surfaces and is the body of text from which the inner being's working is read. A collection is made by putting like words together: synonyms, opposites and gathered words. The base is only an instrument for gathering like words and is never the member; a derived form is a surface with a link of its own; a phrase is one concept and is placed in one collection. Each surface of the scope is in exactly one collection, and is in more than one only in rare circumstances and by the researcher's ruling. The name of a collection is formed from all its members as a concept that covers them. Collections whose members coincide or are close are combined, and a small collection is grouped with like-minded ones unless it is truly unique. Because each collection becomes a chapter of the narrative, it must make sense, must not overlap another, and must tell a coherent story.

A collection is used in three ways. It carries the verses that are read; it is the unit through which the stages are gated; and it becomes a chapter of the narrative.

**Caveats.** The sorting of the surfaces into groups is a judgement and not a measurement. Most of it was made by a model and is inferential until the researcher confirms it, a surface can be wrongly sorted, and a small remainder has not been judged. The surfaces judged are those reached through the Strong's codes that the earlier cluster method allocated; surfaces reached only through other codes have not been judged, and they reach the study only as words that stand with member surfaces. Whether that boundary stays or widens is the researcher's to decide. The collections are made from the surfaces as they are sorted, so an error in the sorting carries into a collection until the reading finds it and the word is moved by the procedure for changing a collection.

A verse is in scope when it holds an occurrence of a member surface of a collection. A word that is neither a behaviour nor an inner-being state, such as a generic evaluative, motion, quantity, speech or copula word, is not a surface of a collection.


### Programme flow

> The path from the Bible text to the finished account: the base data; the stages of the analysis with the unit each reads; the subgroup and its purpose; volume, gates and fallout; the inner-being layer; where the programme stands; what is unsolved and what is not yet defined.

_`prog_meth_flow`  ·  type id 44  ·  chapter_no 2  ·  sort 11_

*Section id 10 · status `draft` · v1544 · 4230 words · author `claude_code`*

The programme organises its work into three stages: **Base_data**, **Analysis** and **Publishing**. Each stage has its own live mechanism, governed by its own configuration. The database carries each stage's state, and work is taken up at the point the database shows it left off.

**Base_data** runs from the text of the Bible to the identification of the surfaces. It has three parts, each built on the one before.

*The text and its data.* Every verse of the Bible is taken from STEP Bible together with its Hebrew and Greek words, their Strong's identities, meanings and relations, and the verse's interlinear presentation is kept verbatim. The mechanical reading of each verse (`verse_lexical`) is derived once from it and records the verse's structural composition and nothing of what a word does for the inner being. This is built verse by verse, by book and range, before any collection exists, and it is complete before any collection is read. Collections play no part in how it is batched.

*The surfaces.* The English words and phrases of the ESV, each linked through its Strong's codes to the original words behind it, are the population the study draws on. The whole population is sorted, by deduction and likeness, into four surface groups: behaviour, inner_being_state, entity and other. The sorting is roughly nine in ten correct, by the researcher's assessment, within an accepted margin; the items placed wrongly are found in the deeper analysis and compensated for there. Its purpose is to make the reading of the inner being's working possible.

*The collections.* The surfaces of the first two groups are collated, by the likeness or relatedness of the behaviour they name, into collections. Each surface belongs to one collection, and through the Strong's code of its base it is connected with its verses, so that a collection carries the verses its surfaces occur in (Chapter 4).

*The engagement step.* A surface is sorted into its group by what it names, before its verses are read, and what it does in a verse is settled only by reading the verse. The engagement step, run on a collection before the collection is read, assesses each member surface in each verse it occurs in, by the role it takes there, and the surface's group then follows from the roles. A surface that is a characteristic in any of its verses is a behaviour, and the difference between its verses is carried by the observations of each verse and not by the group. A surface that is a characteristic in none but is a qualifier in some is an inner-being state. A surface with no inner-being role in any verse leaves the study group, and each such departure is raised as a question for the researcher. A surface judged to have no bearing in a verse is recorded as a silence with the role standalone, and those verses are reviewed again, so that a surface found on re-reading to have a significant role in conjunction with another surface is given that role. Everything the step assesses is inferential until the researcher confirms it. The roles are set out in Chapter 4, under the node.

**Analysis** reads the inner being's working from the verses of the collections. The objective is to read those verses and deduce from them how the inner being works. A whole collection cannot be read in one go: to understand both the lexical context of the words in a verse and the inner-being working of the many behaviours a verse or group of verses carries is not achievable in one pass. The work is therefore split into units, and the units are read in layers and in stages.

*The unit.* To make a collection digestible, its surfaces are grouped further into surface subgroups. The subgroup is the unit of reading. In this programme "surface group" means one of the four groups of the surfaces, and a group of the surfaces of one collection is a subgroup.

*The layers.* Each layer deposits its findings as observations, so that they are available to the next layer, and each collection is digested into observations of lexical meaning first and of the inner-being working afterwards. The subgroup is used first to complete the verse-lexical observations for its surfaces and their verses, then to complete the lexical observations for how its surfaces relate to one another and to the other words in those verses. The same subgroups, with the lexical observations they now have, are then used to formulate the inner-being observations: for specific behaviours, for groups of behaviours, and across subgroups and collections. Each cycle is a layer; each builds on the one before and uses its results. The lexical layers and the inner-being layer are separate processes and never run together, a step closes before the next opens, and every aspect a step demands is answered by an observation with its nodes, or by a recorded none with its reason. The steps the configuration holds, with what each asks, reads and leaves, are set out in Chapter 6, in the section 'The collection reading'; the rules that govern the observation and the node are in the configuration, and the section on the node in Chapter 4 describes how a node ties an observation to the text.

*The stages.* The configuration numbers the work of Analysis as five stages. The table gives, for each, what it is, the unit it works on and where it stands.

| Stage | What it is | The unit | Where it stands |
|---|---|---|---|
| 1. Lexical analysis of the words | Each word of a collection, a surface with its lettered Strong's code, is read in its verses and each sense the verses give it is recorded. Lexical only; the relations between words are base data and are not analysed here. | The word: one row of the ledger for each. A word whose occurrences are all function words (preposition, particle, pronoun, article, suffix and the like) has no row of its own, except a negator and a connective. | Built and tested. The first run on the first collection, thought, was withdrawn when the step was redesigned to record one observation for each sense a word has in its verses. The redesigned step has been run on 10 of the 177 words of thought; 167 stand open. The step is run for each collection, thought first. |
| 2. Grouping of the surfaces | The four surface groups, the collections, and the subgroups within a collection. The subgroups are judged from the dictionary meaning of their surfaces and state nothing of the inner being. | The surface within its collection: placed in a subgroup, or set aside with its reason. | The surface groups and the collections are made. The grouping tools are built and tested. No subgroup stands: the method that formed them for the first collection did not serve its purpose and is withdrawn, and the subgroups are formed again when collection processing starts. The ten subgroups and the 81 surfaces set aside that the withdrawn method left in the tables for thought are replaced then, and no step is opened on them. |
| 3. Verse-lexical observations | For each subgroup: its meaning (step 1.1), its enrichment from the Strong's codes of its surfaces (step 1.2), and what stands with it in the verses (step 2.1: pairings, qualifiers, entities, direction, the relation between subgroups, a double meaning). Lexical only. | The subgroup: every row is keyed to it. | Built in the application; never run. |
| 4. Inner-being analysis | The inner-being observations, made from the stage 3 observations: for specific behaviours, for groups of behaviours, and across subgroups and collections. It is the first step of formulating claims. | The subgroup, the same subgroups as stage 3, and across subgroups and collections. | Required. To be fully specified and built. The configuration already holds the rules of the inner-being reading (the observation items, the kinds of finding, the node roles, the method rules of the reading step and the nuance pointers). They were written for a reading by cluster or subgroup that did the lexical and the inner-being work in one pass; they are the base of the specification, to be cut to the scope of stage 4, placed on the collection, the subgroup and the ledger, and built as its steps. Not built as steps. |
| 5. Claims | The formulation of claims and the update of the claims register. | Not decided. | Not decided. |

That numbering was set before the order of the layers above was stated, and it is read against it. How the two are aligned is open, in particular where the grouping into subgroups falls in relation to the lexical analysis of the words: as the configuration holds it, the analysis of the words is a step that needs no grouping and closes before the grouping is read, while the researcher's order makes the subgroup the base unit of the first layer as well.

*What the subgroup is for.* The researcher's reasoning, recorded when the layered reading was defined, is this. A collection holds words that carry one concept in many forms, and its subgroups are the concepts inside it: surfaces of like meaning, such as the derivatives of one word that travel together. Gathering them lets a finding be stated once for the concept and not once for each surface, while the verses of every surface travel with it through the nodes, so that an observation made for the subgroup is found for each of its verses. In stage 3 the subgroup is the unit every observation is keyed to: its meaning, its enrichment from the Strong's codes of its surfaces, which links it to its usage in the verses, and then what stands with it in the verses, whether subgroups relate or are used interchangeably, the qualifiers, the entities and the direction the text states. Reading the subgroup also tests the grouping: where a grouping is found wrong it is reformed. In stage 4 the same subgroups carry the inner-being observations. A word is not analysed alone in the claims reading; it is bound with its partner, the characteristic, or it is excluded, and a word wrongly included in a collection is moved to entity or other and the move is processed, so that the completeness tests continue to hold. The lexical layers prepare the base data for the formulation of claims.

*Volume.* The collection is the unit of a sitting of the tools: every step of the layered reading is opened, pulled, recorded and checked for one named collection, and every gate is per collection. The grouping of a collection is one pass over its surfaces, judged from the dictionary meaning without the verses. The analysis of the words is the largest part of the work, one row for each word of the collection. Its pull writes every open row at once and limits only the evidence shown for a row, which is capped at a configured number of occurrences; the filled file is checked as a whole and written in one transaction, and a problem anywhere in it refuses the whole file. A row stays open until it is recorded and validated, so a collection can be left partly answered and the next pull returns what is left. The configuration sets no order in which the collections are taken, no number of rows for one sitting and no rule for resuming other than the open state of the ledger. A job that runs longer than a few minutes is started outside the working session, with a log, so that it can be checked, stopped and resumed.

*Gates.* A step closes only when every row it demands is answered by an observation with its nodes, or by a recorded none with its reason, and validated by the check; the next step does not open before it. The steps of stage 3 do not open until the grouping of the collection is finished: every surface placed or set aside with its reason, and every subgroup holding a surface. The closure of stage 3 is a gate for the collection, and stage 4 is not opened until stage 3 is complete; this is read as every step of stage 3 for the collection. A stage that finds an earlier observation wrong does not correct it in place: the case returns to the earlier stage, where a row answered again withdraws its earlier observation with its reason.

*What stage 3 leaves.* When stage 3 is complete a collection holds, for each subgroup, its meaning and its Strong's enrichment, which is never a none; a pairing for each partner collection with which it shares at least three verses; a qualifier, an entity and the direction the text states, where the verses show them; a relation for each pair of subgroups that share at least three verses; and a double meaning for each surface that carries two or more Strong's codes. Each is an observation with its nodes, each node carrying its verse, word, surface, collection and subgroup, and the set is the complete verse-lexical account of the collection. Stage 4 reads that account. What each of these observations states is what the dictionary, the verses and the stored structure show: the grammatical qualifier is a stage 3 observation, and what the qualifier gives the behaviour in place is a stage 4 observation.

*Fallout.* Some surfaces, words and aspects are not analysed, and the programme states what is done about each.

| What is not analysed | What is done |
|---|---|
| Surfaces of the groups entity and other | They are not members of any collection. They enter the study as the words that stand with a collection's surfaces, as nodes of the observation that covers them. A verse that holds only such surfaces is out of scope and is not touched. |
| A word wrongly included in a collection | It is found at any stage and moved by the procedure for changing a collection, and the move is processed so that the step reopens. |
| Surfaces wrongly sorted into the four groups, unjudged or set aside | They are found in the deeper analysis and compensated for there; the step that records them is not yet defined. |
| A surface whose meaning is not the collection's | It is set aside in the grouping with its reason, and stays in the index of the collection. |
| A function word | It is read with its unit and has no row of its own, except a negator and a connective. |
| A qualifier, an entity or a double meaning that is not present | A recorded none with its reason, where the step allows it. |
| An aspect of a Strong's code that the verses do not carry | It is not a conflict or an error; no observation need focus on a meaning that is not about the inner being. |
| Surfaces not yet placed in a subgroup | They stop stage 3 from opening for the collection until they are placed or set aside. |

*What the inner-being layer reads.* Stage 4 reads how the inner being works from the observations of stage 3. The researcher's placement is settled: how the inner being is read belongs to this layer, and what the readings show together, how workings are grained and linked, how states and transitions behave and how a characteristic emerges, belongs to the claims, where the answers are discovered from the observations. The order of the study is to finish reading the inner-being surface groups into observations and then to formulate the claims. The researcher has stated what is read: behaviour is not only acts or operations but also states and conditions, for example sin, righteousness, life and death; it has qualifiers that define it; and a characteristic such as anger or love is not a thing and is not defined in advance, being known only by inference from the collection of behaviours, processes, actions and movements that give it substance. The programme's record of how the working has been defined, from the first working definition to the layers, shows the same few parts recurring under different names: the bearer and the seat, the behaviour in its three forms of act, state and movement, the qualifiers, the source and the object, the effect, the link to other workings, the expression or what is hidden behind it, and the context of the passage. The lexical layers hold a home for few of these, and the inner-being layer needs one for the bearer, the state of a being, the transition, the effect, the expression, the context and the link. This is the record's reading and it is inferential until the researcher confirms it. The study has also defined the interventions that a reading triggers: read beyond the verse, in its passage, genre and speaker; read outward from the verse and not inward from a question; check the original; reclassify a word whose role in this verse is not the one its collection gives it; do not force a meaning and never close on 'not X'; record a discovery outside the verse separately. They are defined and are not yet carried into the layered reading. The test applied to every result is whether it is sensible, reasonable and defensible. The rules of this reading are already held in the configuration: nine items explored for every characteristic (meaning, role, polarity, object, enactment, party with its route, circumstance, operation with its chain, and a flag), eight kinds of finding, the node roles, the method rules of the reading step on how a verse is read and how a finding is written, and sixteen nuance pointers. Stage 4 is specified from them: what stages 1 and 3 now do is taken out, the rest is placed on the collection, the subgroup and the ledger, and the level across subgroups and collections and the interventions listed above are added.

*Role in the inner-being layer.* The role a word has in a verse is what the inner-being layer reads by. It is judged for each occurrence, from the verse and against what the verse is about, and never taken from the cluster tag, from the collection or from the part the word usually plays: the same word can be a characteristic in one verse and a qualifier in another, and a word that has no inner-being role in a verse is not forced into one (the node, in Chapter 4, sets out the roles). Two consequences are the researcher's. The role is the filter of the deeper reading: the deeper reading of the verses in the next phase is filtered on the role of the words, so that the study is not contaminated by words that have little or no bearing on the inner being; where that filter sits in the claims phase is not yet defined, and it is not built. And a role is never a verdict: a verse or an item is never closed as 'only a qualifier' or 'no bearing'. What is recorded is what the verse is, with every significance it carries, since a verse often carries two or three and none is dropped because it was not the one asked about.

*The claims.* Claims are formulated from the inner-being observations. The formulation of claims is not yet decided. The claims that exist come from an earlier method and are not yet tied to the collections; each is to be cross-linked to its collection and re-evaluated against the observations.

**Publishing** is the production of the essays and output that carry the results: the narrative, held in the database as chapters and sections, and exported for its readers.

**Where the programme stands.** The base data is complete for the Bible: every verse, its original-language data and its mechanical reading. The surfaces are sorted into the four groups, with a small remainder not yet judged, and the surfaces of behaviour and inner_being_state are gathered into collections. The reading, which is the centre of the study, has not properly started. The layered reading is built, and it was opened on the first collection, thought, but no collection has completed a stage, no subgroup stands, and no stage 3 observation exists. The observations in the database were made by earlier methods (documents captured, readings by cluster, by strand and by phase) and are held as gathered rows; each is re-read into the layers collection by collection, and one that cannot be made to comply with the rules of the observation and the node is retired with its nodes as a soft delete with its reason. The inner-being layer is required and is to be fully specified and built, from the inner-being reading rules the configuration holds; the claims are not decided. The account, the claims and the narrative, is a complete draft assembled from readings made under earlier units, so it cannot yet be said to rest on the collections. The process control, with its escalation record, compliance check and session close, is operating. The current counts are held in the reports and not in this prose.

**What stands unsolved.** These gaps are recognised in the record and are not closed.
- No check of content exists before a stage closes. The structural checks of the application have passed while the content was wrong, and each content gap found so far was found by the researcher reading one case by hand.
- No independent control of completeness operates on the study's universe. The earlier controls, a comparison with the primary lexica, a lemma inventory and a candidate net, were each built and retired.
- The surfaces judged are those reached through the Strong's codes that the earlier cluster method allocated. A large share of the occurrences in the text lie on other codes and reach the study only as words that stand with member surfaces. Whether that boundary stays or widens is the researcher's to decide.
- The layered design has not been run through a stage on any collection, so it has not met the test at which an earlier reading technique failed, consistency at scale.
- The recorders of the layered reading were audited against the rules after the first run failed and not before it.

**What is not yet defined.** The programme states what it does not yet know, so that it is not mistaken for settled.
- The order in which the collections are taken, and the size of one sitting of the reading, are not set.
- The method by which the subgroups are formed, and what a subgroup is for in stage 4. A subgroup is used twice, first in the verse-lexical observations and later in the inner-being observations, and each use has not been given its own statement of what a subgroup is.
- The alignment of the configuration's stage numbering with the order of the layers above.
- The specification of the inner-being layer, which is a required stage to be fully specified and built: what it reads, how it is done and what it leaves are to be completed from the inner-being reading rules the configuration holds and the observations of the lexical layers, together with how the working of the inner being is depicted systematically and checked, and how a reading is kept consistent from one read to the next.
- The grain of the inner-being reading. A node is an occurrence of a word, while a working is a relation among occurrences; how one working across several nodes is one record is not stated. The unit of a batch of the inner-being reading, and how the nuances and variances of a working are handled when the same word works differently in different verses, are also not stated.
- The filter of the deeper reading by role: which verses and words go on to the deeper reading because the word has an inner-being role in them, and where in the claims phase that is applied. The roles of the nodes written by earlier methods are not all set (Chapter 4, the node), and setting them has been handed to the collection reading.
- The formulation of claims from the inner-being observations.
- How the chapters of the narrative follow the collections beyond the chapter on the inner being at work, which is built by collection. The researcher has called one chapter for each collection enormous and has said that the groupings are not yet known and should come from the claims; the rules that name the collection as the chapter would then be amended.
- How the per-cluster science reviews held as reference files are used in the claims reading; loading them into a reading was never built.
- The surfaces that were sorted wrongly, not yet judged or set aside: the step that records them, whether a surface rightly in a collection but set aside is read afterwards, whether a pairing or a relation of fewer than three shared verses is meant to be left unread, and whether the surfaces that have no group set are in the collections or out of them.

The programme's methods have changed materially over its life, as its record shows, and this section describes what operates now.


### Science in action

> How the second lens is engaged: when science enters (in the claims reading), the six fields, the convergence and divergence framework and the decision not to build a scientific database.

_`prog_meth_science`  ·  type id 45  ·  chapter_no 2  ·  sort 12_

*Section id 11 · status `draft` · v1394 · 485 words · author `claude_code`*

The relationship between Scripture and contemporary science is described conceptually in the section on science and the Bible. This section describes how the scientific lens is engaged in the work.

The governing premise is the second-lens position. The scientific literature relevant to the inner being (psychology, neuroscience, physiology, behavioural science, developmental and cognitive psychology, and evolutionary biology) is vast, and treating it as a co-equal programme would demand a second corpus-level effort matching the biblical one. The programme does not attempt this. It requires representative and reliable coverage of the landmark findings in each relevant field, held alongside the biblical analysis as the second lens through which the same territory is read.

**When science enters the work.** The science reading is part of the claims reading. It is engaged after the biblical reading of a collection is complete, when claims are formulated, and never in parallel with it. Running the two together risks the scientific frame distorting the biblical reading before that reading is complete, particularly for words where the scientific literature is substantial, such as shame, fear and grief. A science chapter of the narrative is planned and deferred until the claims reading reaches it.

**The scientific fields.** The programme works with six fields. *Neuroscience* addresses the body-soul boundary and the somatic dimension. *Clinical and social psychology* addresses soul operations: emotion, attachment, moral psychology, shame and guilt, will, motivation and virtue. *Physiology and epigenetics* addresses the body and the transmission of patterns across generations. *Behavioural science* addresses the relational dimension, how inner states express in behaviour and social context. *Developmental and cognitive psychology* addresses the formation of character: cognitive development, moral development, conscience and self-regulation. *Genetics and evolutionary biology* addresses the created endowment: what is built into the human creature by nature.

**Convergence and divergence.** The scientific reading is organised by a framework of three kinds of convergence and three of divergence. Convergence can be phenomenological (the same experience described from different angles), mechanistic (science describing the mechanism of what Scripture describes as a reality) or structural (the same architecture of the inner life in both accounts). Divergence can be register divergence (the accounts address different levels of one reality and only appear to conflict), reductive divergence (a scientific account that loses dimensions the biblical account treats as primary) or genuine divergence (claims in actual tension that cannot be harmonised by reframing). Genuine divergence is named, not papered over.

**The no-database decision.** The programme does not build a structured scientific database to match its biblical one. A parallel database at that depth would be a second programme; the data types are not structurally equivalent, since biblical data is lexical and classifiable while scientific findings are arguments and interpretations that require judgement to apply; and the second-lens role does not need it. Scientific material is held as reference files and used in the claims reading, and everything drawn from it is labelled by its source.


### Publishing

> The output of the programme: the narrative held in the database as chapters and sections, how claims are told in it, and what publishing does and does not mean here.

_`prog_meth_publishing`  ·  type id 46  ·  chapter_no 2  ·  sort 13_

*Section id 12 · status `draft` · v1395 · 288 words · author `claude_code`*

Publishing is the output side of the programme: the production of the documents that carry its findings to its audience. The output is the narrative of the inner being.

The narrative is held in the database. It is made of chapters, and each chapter of sections whose text is a block; the chapter files are exports from the database. The table of chapters decides which chapters exist, their order and their purpose. The planned shape is an introduction; chapters on the question, on life and death, on the one inner person, and on the heart, the soul, the spirit, the flesh and the conscience; a chapter on where the words part; a chapter on the inner being at work, built by collection; further chapters on other sides, on what goes wrong, on other beings, on being made new, and on what lies beyond the named words; and a deferred slot for science.

Each claim is told in the narrative by a block, in full, in part or by pointer, and each claim keeps its sources and its verdict against the wording of the original essay from which the narrative began. The narrative follows the collections: each collection becomes a chapter of the narration.

Publishing here means the production of readable documents. It does not mean commercial publication, external release or any particular distribution channel; the narrative is copied to the inbox of the researcher's publishing site, and publication decisions of the external kind are outside the programme's method.

The database is the research. The narrative is the form in which the research reaches the reader, a curated presentation of the claims; where a reader's question is more specific than the narrative's treatment, the database supports the deeper look.


### Key methodological principles

> The principles that govern every stage, the lessons of the programme's course from which they come, the difficulty not yet resolved and the researcher's test.

_`prog_meth_principles`  ·  type id 47  ·  chapter_no 2  ·  sort 14_

*Section id 13 · status `draft` · v1472 · 1493 words · author `claude_code`*

The method rests on nine principles. They govern every stage of the work.

**Scope is defined against the inner-being definition.** The surfaces of the study are the words and phrases of the ESV judged against the programme's working definition of an inner-being characteristic, gathered into collections of like meaning, and settled from evidence before they are read.

**Base data is complete before reading.** The text, its original-language data and the mechanical reading of every verse are held before any collection is read, so that every collection is read against the same body of data.

**Words are not forced into preconceived categories.** Groups are formed from the meaning of the words and what the verses engage. A category that cannot be grounded in verse evidence is not a category the programme uses.

**Verses qualify by occurrence, not by interpretation.** A verse is in scope because it holds an occurrence of a member surface, irrespective of what the verse contributes.

**Every finding is substantiated by data.** A finding can be traced to a specific verse, word or pattern in the evidence. A statement that cannot be traced is not recorded; an AI's output is inferential until confirmed; no guessing, no assumptions and no made-up results.

**The lexical reading and the inner-being reading are separate.** What the words and the verse show is recorded first, in its own observations; what a word does for the inner being is read afterwards, from those observations, in a separate process. A step closes before the next opens, and no aspect is left open.

**The database is the analytical memory.** Every observation, node, claim and change is held in the database with its reason, and a change keeps its prior state. Re-reading replaces a finding with its reason recorded, so findings stay anchored to the evidence that produced them.

**Biblical lens primary, scientific lens secondary.** The biblical reading of a collection is completed before the science reading, which is part of the claims reading.

**Synthesis follows analysis, bottom-up.** Claims are formulated from the observations, and the narrative is assembled from the claims. Larger claims are not made before the smaller claims on which they rest.

**Where the principles come from.** The principles are the lessons of the programme's own course. Each was found when an earlier way of working failed on a concrete verse or word, and each is now enforced by a rule of the application. The programme began in January 2026 with the two Frameworks and the wish to understand spirit, soul and body. In February its scope was extended to an in-depth study of the soul within the inner being, with a registry of some two hundred words. A per-word programme followed: extraction of each word's data from STEP, a classification of its verses, and an analysis by dimensions. In May the registry and the dimensions gave way to clusters of like terms. In June the study was reset after a cold reading found that most of its claims imported a meaning the verses do not carry. Through the summer the base data was rebuilt from the verse upward, the application was built, and passages were read one at a time. In the autumn the English surface, as the reader meets it in the ESV, became what is studied, then the collection became the unit, and the collection began to be read in layers. The lessons are these.

- The verse in its context decides what a word means. A dictionary entry or a code offers candidates; one code read in all its occurrences showed senses that no dictionary entry held.
- A word in a verse is read with the other words of the verse, not alone.
- How a word's meaning changes with circumstance is a discovery and is recorded, as the face of the word.
- The English surface is what is studied, and the Strong's code is the lens on it: a surface can carry several codes and a code can sit under several surfaces.
- The kind of a surface is judged from the word itself: behaviour, inner-being state, entity or other.
- The unit of study is the collection. A registry of words and clusters of codes each failed as the unit.
- What the words and their structure show is distinct from what they do for the inner being, and each has its own observations.
- Analysis is not done in bulk. A model's grouping placed nearly all the surfaces it was given in one group, and a grouping made by pattern did not serve its purpose.
- Claims are derived from sources; the narrative is the story and is not cut into claims.
- The project lives in the databases. Rules held in documents, and instructions read afresh each session, drifted; every rule is therefore a configuration row.

The programme has moved between two views of its subject. It was first modelled as a list of named characteristics (February), then as clusters of like terms that carried them (May), then, after the reset of June, as movements and a relational web with the naming of characteristics set aside, then as characteristics read from the verse and typed there (July), and now as characteristics collated on surfaces and read in context. The present design is the third synthesis of these views, not the first. Two streams of learning ran through the course, one about the subject matter and one about the process. In the subject matter the lesson was always about grain: the registry word, the dimension, the cluster of like terms, the lemma and the Strong's code were each the wrong grain, and the working grain moved toward the occurrence in its verse, the surface in its verse.

The process lessons are as much premises of the programme as the lessons above.

- A rule that is not built into the mechanism is not a rule. The failure recurred: an AI claimed compliance with a rule it had not met, instructions left choices to the session, a completeness check created the records it then checked, validators checked structure while the values were wrong, and rules existed while the recorder did not enforce them. Each time the remedy was to move the rule from a document or a person into a mechanism that checks the content.
- Verification is independent of the maker and is measured at the unit that matters. A check that creates what it checks, or that checks existence and not content, proves nothing; completeness is measured against an independent source, at the verse.
- Content gaps have been found by the researcher reading one concrete case by hand, and the checks of the application passed in each of those cases. Every batch of a reading is therefore read by the researcher against the test below.
- Drift between what was decided and what the live documents say is a standing hazard. The answer is one home for each kind of content, with every other document pointing to it.
- Infrastructure is existential. The loss of the live database in June, through corruption on a cloud-synchronised drive, cost six weeks and could not be recovered because the work was not replayable; the work therefore lives in the databases, is backed up, and is replayable.
- An elaborate pipeline built before the method is known is paid for twice.

Beneath these lies a difficulty the programme has not resolved: to know what to look for, what is and is not a characteristic of the inner being, while discovering how such characteristics work, from the same verses. A list of characteristics, a registry of words and the Strong's codes that STEP returns each approached it, and the recognition that a characteristic is driven by its context was the turning point. Three difficulties sat inside it: the wish for completeness conflicts with choosing characteristics in advance, since a list chosen in advance cannot be complete; verses had to be read through the lens of specific characteristics, while the words that carry them are sometimes relevant and sometimes not; and some words become behavioural only when they operate together. The layers now keep apart the lexical meaning, the occurrences in the verses, the word in its verse and the collation of surfaces, so that each can be read on its own. How the working of the inner being is to be depicted systematically, and checked, is still being discovered. The test the researcher applies is whether the outcome is sensible, reasonable and defensible.

The principles are not independent. Defining scope against a definition makes a complete base meaningful. A complete base makes a uniform reading possible. A separate lexical reading makes the inner-being analysis answerable to evidence. The database as memory supports re-reading on the same footing as the first reading, and re-reading on a stable footing makes the bottom-up account possible. Because the data read at a re-run is the same data the prior run read, the method is reproducible.


### Key constraints

> The limits the programme accepts as commitments: scope bounded by the collections, the second-lens bound on science, no scientific database, no bulk analysis and no publication before the reading closes.

_`prog_meth_constraints`  ·  type id 48  ·  chapter_no 2  ·  sort 15_

*Section id 14 · status `draft` · v1397 · 391 words · author `claude_code`*

The principles described in the preceding section shape how the programme works. The constraints described here shape what it does not attempt.

**Scope is bounded by the collections.** The programme studies the surfaces of the groups behaviour and inner_being_state and their verses, and does not study other vocabulary except as the words that stand with them. The collections are open to evidence surfacing from within the corpus, by the procedure for changing a collection; they are not open to interpretive expansion from outside it.

**The scientific lens is bounded by the second-lens decision.** The programme does not engage the scientific literature at the depth of its biblical engagement. Its engagement is set by the claims reading and the reference material described in the section on science in action, for practical reasons (the scale of a parallel effort), methodological reasons (the data types are not equivalent) and structural reasons (the programme is biblical research, with science as the second lens).

**No structured scientific database.** The database holds the biblical research. Scientific material is held as reference files.

**Synthesis does not run ahead of its evidence.** A claim is formulated when the observations it rests on are complete. A chapter is assembled when its claims are formulated. The programme-wide account is assembled when the chapters are.

**The programme is corpus-level, not survey-level.** Each collection receives a full reading: every word read in its verses, every surface placed, every aspect each step demands answered.

**No bulk analysis.** No bulk or one-shot analysis, by Claude or by a model, is used to produce the study result. Item-by-item roles written in one pass, templated observation text and groups assigned by pattern are not a substitute for reading and articulating each discovery.

**No publication before closure of the reading.** A chapter is not produced from a collection whose reading is not closed; a chapter produced ahead of that would carry a retraction risk.

**Scope is not reopened on interpretive grounds.** A surface admitted to a collection is not re-examined for admission because an interpretive frame would exclude it, or because the reading has produced findings that conflict with a current view. Where findings raise a definition-level question, what the inner being is and where its edges lie, that question is handled at the level of the definition, and any change to a collection goes through its procedure.


## Research approach

### Traceability and evidential warrant

> The discipline that separates a finding from a hypothesis and an inferential statement: traceability to the data, the verse as the evidence, the database as the authority and verified state.

_`prog_disc_traceability`  ·  type id 49  ·  chapter_no 3  ·  sort 16_

*Section id 16 · status `draft` · v1398 · 563 words · author `claude_code`*

The programme records findings and it records hypotheses; the two are not the same. A finding is a statement that can be traced back to a specific verse, word, lexical source or observation in the database. A statement that cannot be traced that way is a hypothesis. Hypotheses are labelled as such or discarded. A hypothesis is upgraded to a finding when later evidence supports it on its own terms; when that happens, the hypothesis-form language is replaced with the evidence-grounded statement rather than left in place with the evidence tacked on.

The traceability requirement is the programme's working definition of evidential warrant. It governs every analytical output: the observations of each stage of the reading, the claims formulated from them, and the narrative told from the claims. The standing of a statement in the programme's record is a function of whether the data supports it, and the data that supports it is specifiable: a verse, a word, a lexicon entry, a node, an observation. Where the support is specifiable, the statement is a finding. Where it is not, it is a hypothesis.

Between finding and hypothesis sits a third category: the **inferential**. Where a statement is analytically plausible or theologically reasonable but is not directly supported by data, it is labelled inferential. Everything an AI produces, including Claude's own output, a subagent's report and a model's classification, is inferential until it is grounded in citable evidence or confirmed by the researcher. Inferential statements are retained because the work benefits from visible reasoning, but they are not presented as confirmed. An inferential label is an accurate description of the evidence state; it is not a softening of the statement. It does not quietly become a finding without the supporting evidence.

The verse leads. All analytical work begins by reading each verse in its passage, with the observations already recorded for it, and letting it say what it says, not with a category, a tradition or a prior interpretation. Groups and classifications emerge from the verse evidence; the verse is never bent to fit a pre-existing category. What the record says about a verse, such as a file's status or an item's wording, is not a reading of it.

A verse is in the programme's scope because it holds an occurrence of a member surface of a collection: lexical presence, not interpretive fit. A word is read in its verses, and a word that plays no role in any inner-being dynamic is not forced into one.

The current state of the database, queried live, is the authoritative data source for analytical work. Earlier outputs, such as drafts, reports and extracts taken before the latest query, are reference material. Where an earlier output conflicts with what the database holds now, the database is correct and the earlier output requires correction. This rule prevents the displacement by which an earlier framing becomes the working source in place of the data it was drawn from.

Database state is verified, not assumed. Before any operation whose outcome depends on database state, the state is checked. Memory of a previous session's state is not current state; recent is not current. A statement about what a column holds is made only from its recorded meaning or from a test over all its rows, never from a sample. **Every finding is substantiated by data: no guessing, no assumptions, no made-up results.**


### The two-AI division of responsibility

> The division of responsibility between the researcher and the single working agent, the controlled use of a local model, and the two mechanisms that carry the researcher's decisions.

_`prog_disc_two_ai`  ·  type id 50  ·  chapter_no 3  ·  sort 17_

*Section id 69 · status `draft` · v1399 · 356 words · author `claude_code`*

The programme runs on one working agent. Claude Code investigates, builds and operates the databases directly, in the same live conversation the researcher directs it in, and reads the evidence of each collection to interpret it. A model on a local server is used as a controlled tool for judging words in the surface cycle; its address and the way it is reached are configuration, the service is checked before its first call, and everything it gives is inferential until the researcher confirms it.

The researcher directs, decides and is accountable for every conclusion. Claude is expected to interpret the evidence it is given, and every interpretation is backed by evidence that can be traced: the verse, the word, the lexicon entry, the observation or the record from which it came. Claude does not leave it to the researcher to discover an interpretation that has no foundation. In most cases Claude's reading decides, and the researcher scrutinises that judgement and settles what the evidence cannot. Where a point requires a new decision, the work stops there: it is recorded as an open item and routed to the researcher with its evidence and options, and work resumes when the decision is made. Where Claude finds its own error against an already settled design, it corrects it, records what was wrong, and continues.

Two mechanisms carry the researcher's decisions. The `escalation` table (Chapter 5) is where every open item, anomaly or judgement call is raised the moment it surfaces and is tracked through to the researcher's own decision. `Config-Maintenance.ps1 -Step Propose` is the equivalent gate for a change to a configuration row, coherence-checked automatically and then paused for the researcher's decision, except in a developer session, where the change is made through a logged migration. Design or build work is never closed by Claude alone; only a mechanical correction against an approved design is.

Patches and directives remain the channels by which a change reaches `bible_research.db` (Chapter 6): Claude drafts and applies them, and every application is a distinct, auditable step from the work that produced it. The conversation, the escalation record and the patch are the record.


### Session continuity and memory discipline

> How continuity is kept across sessions: the databases as memory, the layers and limits of Claude's memory, and the mechanisms for starting, recording and closing a session.

_`prog_disc_session_continuity`  ·  type id 51  ·  chapter_no 3  ·  sort 18_

*Section id 18 · status `draft` · v1400 · 566 words · author `claude_code`*

The programme's analytical memory lives in the databases, `iba.db` and `bible_research.db` (Chapter 4): the text and its data, the surfaces and collections, the observations and nodes, the claims and the narrative, the configuration and the escalation record, and the programme prose that describes the whole. The database is where findings and interpretations are kept. It is not a storage layer beneath the research; it is the research's memory.

Claude Code does not live inside the database. It is an instrument applied to what it loads or queries in the current conversation, and at any moment it sees only that: the files of the session, the live query results, the configuration and governance bearing on the instruction. The database holds the authoritative record whether or not Claude is looking at it. Framing the right question against the right table is itself a research act.

Claude's memory arrives in layers that are not equivalent. The **chat context** carries the current conversation, bounded, with earlier content summarised as the window fills. The **persistent memory** holds only who the researcher is and a few pointers to data; it holds no rule and no project state. **Live database queries** are authoritative over any memory of prior state. **Training** is general knowledge, a pattern and not a record, and it does not substitute for reading the database. The record, and not Claude's memory, holds the researcher's earlier instructions and answers; it is read before a question is put, and a question the record already answers is not asked. What can feel like accumulated insight is retrieval from this programme's own record, pattern from training, or reasoning over what has been loaded; it is not a shared pool of knowledge across users or projects.

Continuity across sessions runs on controlled mechanisms. **Starting a session** (`/start-project`) checks the configuration, the database and the STEP connection, how the last session ended and the open escalations, and prints every general rule; Claude restates each in the session's compliance file, and the check must pass before work begins. The **escalation table** is the continuous record while a session runs: every open item, and every comment of the researcher that bears on an item, is recorded in the same turn with the researcher's words quoted verbatim. **`BUILD.md`** is the running build history for everything under `iba/app`, updated in the same unit of work as the code. **Closing a session** (`/session-close`) checks what the session did, decided and left open against the record; nothing is committed while a finding is open. It writes the **session log** (`Logs/SESSION-LOG-*.md`): the scope, every escalation touched by id with its outcome, every file changed, the decisions (the researcher's own and Claude's, each with where it was recorded), the open items carried forward, and the git state. The **project map** is kept current as part of the close. Between them, nothing substantive exists only in chat or only in a session that has since closed.

Prose written to the database is written to survive storage. It is self-contained (readable without the session that produced it), scoped (clear about what it refers to) and grounded (clear about the evidence it rests on). A content change reaches `bible_research.db` through a patch, a dry run first, and a configuration change through `Config-Maintenance.ps1 -Step Propose` or, in a developer session, a logged migration. A live re-query confirming the write is the source of truth for the next step.


### Tools and their roles

> The programme's instruments and their roles: STEP Bible, Claude Code, the IBA application, the two databases, the local model server and the working file formats.

_`prog_disc_tools`  ·  type id 52  ·  chapter_no 3  ·  sort 19_

*Section id 1040 · status `draft` · v1401 · 574 words · author `claude_code`*

The programme runs on a small set of tools, each with a defined role. Over time, as the programme wrestled with consistency and repeatability, the tool set moved from a range of scripts and instruction documents to an integrated application, the IBA App, which is a complete rebuild of the database and all its dependencies. The IBA App is described in the sections that follow.

**STEP Bible** is the source of biblical-language data. It provides the Hebrew and Greek words, the verses in which they occur, and the lexicon data for every word. STEP is the source of every lexical claim, and the raw layers are not re-derived.

**Claude Code** is the operational environment and the single working agent (see the section on the division of responsibility). It runs in the conversation the researcher directs: it reads the evidence, runs the registered steps of the app, executes queries against both databases, authors and applies patches, proposes and, once approved, applies configuration changes, and authors the programme's prose. Every database operation takes place in a tool the researcher can observe, and every consequential write is gated by an escalation or logged to an audit table (`cfg_change_detail`, `record_change_log`).

**The IBA App** is the control system that lets operations be performed consistently, with minimal deviation over time, and not renegotiated by hand each session. Every operation is a registered step run through one dispatcher, every rule is a configuration row (`cfg_*`), every write is checked against a write grant, and the rules reach Claude at the start of a session or at the first use of the operation they govern. It is the central process control for the entire project (Chapters 4 and 5).

**The databases.** `iba.db` holds the base data (the Bible text and its original-language data, the mechanical reading of each verse), the surfaces and collections, the observations, nodes and claims, the narrative, the configuration and the escalation record. `bible_research.db` holds the programme prose. Prose, whether the programme narrative or this description, lives in the databases under the same discipline as the evidence, so that every session has a consistent, queryable self-description and a single analytical memory.

**A local model server** is used through one controlled route to judge words in the surface cycle. How it is reached is configuration; it is checked before use; and what it returns is inferential.

**Markdown and JSON** are the working file formats: descriptive content such as reports, session logs and drafts in markdown, and structured content such as patches and extracts in JSON. A file is a working document or an export; only the results held in the databases are the project's results. A word-processor or PDF is produced only when the researcher requests it.

**The instruction corpus, then and now.** Process control first ran on instruction documents, one for each phase of the work. The many iterations of, and differences across, those documents led to the IBA App: control moved from prose interpreted afresh each session to configuration rows that a live check can read and enforce. Chapter 6 records which of the old instruction documents still describe something live.

The tools combine in the working arrangement. STEP feeds the base data; the surface cycle gathers the collections; Claude reads each collection through its stages and records the observations in the database under the app's controls; the claims and the narrative follow. Each tool is bounded, and together they are the whole of what the programme uses.


### Researcher decision authority

> The researcher's authority and accountability, Claude's expected interpretation of the evidence, the integrity of the sources and the declaration of AI use.

_`prog_disc_research_decisions`  ·  type id 53  ·  chapter_no 3  ·  sort 20_

*Section id 20 · status `draft` · v1402 · 514 words · author `claude_code`*

The researcher holds the intellectual responsibility for the programme. The research question, the design of the study, every methodological decision, and every conclusion are the researcher's, and the researcher is accountable for every claim and can defend it. The researcher directs every session, scrutinises Claude's judgement, corrects errors, overrides proposals, and settles what the evidence cannot.

Claude is the working agent and is expected to interpret the data and evidence it is given. Within the researcher's direction and the rules of the app, Claude reads the evidence of each collection and decides what it settles in the majority of cases; it builds and operates the app; it drafts the prose. Every interpretation is backed by trackable evidence, and Claude does not leave it to the researcher to discover an interpretation that is unfounded. Where a reading of the text is contested, Claude sets out the readings with their evidence. Where a rule's application is uncertain or a decision is new, Claude does not guess: it records the open item and routes it to the researcher, and it does not put to the researcher a question the record already answers.

The division at each decision point is concrete. Claude reads the evidence and records an observation or proposes a classification; the researcher accepts, corrects or rejects. Claude drafts prose; the researcher reviews, corrects or replaces. Claude constructs a patch or a configuration proposal; the researcher's decision, recorded on the escalation it was raised against, allows the change to be applied. At every decision point, the record of what was proposed, what was decided and what follow-up was logged is captured on the escalation itself (Chapter 5) or in the session log. The record is the auditable evidence of who decided what. The researcher's in-session direction supersedes stale text in a document until the document is updated.

**Integrity of content and primary sources.** The primary source for all lexical claims is STEP Bible, a scholarly tool for Hebrew and Greek biblical analysis; every word, Strong's number and verse record was drawn from STEP. Any change to the databases is held in a versioned, auditable mechanism with its decision history: the patch system and the change log for `bible_research.db`, `cfg_change_detail` for `iba.db`, and `ib_observation_change` for the observations. The chain from primary source to database entry to finding is traceable end to end, by design.

**Declaration of AI use.** AI is used for the reading of evidence, the drafting of observations and prose, the operation of the app, and, in the surface cycle, the judgement of words by a local model. The use is declared by function. The researcher is accountable for the results, every source claim is verifiable against STEP Bible and the auditable database, and no AI-supplied citation is accepted without verification. No confidential third-party material is processed through AI tools; the programme works on data the researcher owns and assembled.

The authority structure is the condition under which the research is conducted. Every discipline described in this chapter exists to give the researcher the auditable conditions under which decisions can be made, verified and defended.


### Scope and help-forward discipline

> The in-session discipline that keeps Claude on the task set: help forward within the researcher's scope, no autonomous extension of scope, and escalation and not guessing.

_`prog_disc_scope_integrity`  ·  type id 54  ·  chapter_no 3  ·  sort 21_

*Section id 21 · status `draft` · v1403 · 492 words · author `claude_code`*

The programme's architecture works only if Claude stays on the work the researcher has set. The disciplines described so far assume a working agent focused on the task in hand that does not drift. Without that focus, the architecture becomes a stage for generating volume; with it, the architecture produces research.

The operating default is **help forward**. Where the path the researcher has set is clear, Claude advances the work. It does not wait for instruction on each step within a task already scoped, and it does not pause to ask permission for steps the task evidently requires. A plan, once approved, is run to completion without re-confirming each step.

Help-forward is bounded. It means help on the task set, not the enlargement of it. Where Claude notices something that warrants attention but lies outside the task, such as a finding elsewhere that bears on this one, a document inconsistent with another, or follow-up work the result calls for, it records the matter in the same turn as an escalation (an open item, an anomaly or a judgement call) with the relevant words quoted verbatim, and the work continues on what was asked. A follow-up is put to the researcher as an item with its evidence; it is not undertaken until the researcher decides.

Scope is not extended autonomously. Where additional work appears warranted, it is flagged for the researcher's decision: *this is outside current scope; the researcher decides whether it enters scope*. Diagnosing a gap is not a licence to design and build the fix in the same pass. A design goes to the researcher as a decision first, and the work resumes when the design is settled.

The failure mode the discipline prevents is **drift**: the slow transformation of a focused task into something broader, shaped by pattern-matching and accumulated context and not by the researcher's direction. Drift looks plausible turn by turn and becomes visible only when the session is read end to end against what was asked. The discipline against it is turn by turn: each turn is bounded by what was asked and what was needed to answer it.

**Escalation**, not guessing, is the standing response to uncertainty. Where a rule's application is unclear, a scope question is ambiguous, or two readings of an instruction are defensible, Claude records the item and brings it to the researcher with the evidence and the options, after first reading the record for an answer already given. Guessing at what the researcher would want is drift under another label.

The positive work this discipline protects is exploration: reading widely within the task, considering alternative readings, setting out options with their evidence, and producing analytical material the researcher can evaluate. Scope integrity keeps each session recognisable as the session the researcher opened, and, with the authority structure that precedes it, is the foundation on which the record can be audited: what was asked, what was done, what was decided, and by whom.


## Data architecture

### The database as the programme's working memory

> The two databases as the programme's working memory: what each holds, the configuration store and STEP Bible as the primary source.

_`prog_data_database`  ·  type id 55  ·  chapter_no 4  ·  sort 22_

*Section id 22 · status `draft` · v1404 · 369 words · author `claude_code`*

The programme runs on two SQLite databases. `iba/app/db/iba.db` is the home for the project's process control and its working data: the base data (every table from the STEP extraction through the Strong's tables, the verses, meanings and the mechanical reading of each verse), the surfaces and collections, the observations and nodes, the claims and the narrative, the escalation record, and the `cfg_*` configuration store that governs how every step of the app behaves. `database/bible_research.db` is the home for the programme prose and its glossary, the store in which the programme's written account is authored.

The `cfg_*` store holds every rule the app's code obeys: which step may write which table, what a step's failure path is, what a controlled vocabulary's allowed values are, what a report's structure is. The principle is that the code decides nothing; every choice is a row that a live check can read. The configuration layer is part of the data architecture, not a separate concern, because it makes the behaviour of the base data and of the reading traceable and changeable without a code edit. Chapter 5 describes the governance mechanism in full; this chapter describes what the two databases hold. The record of what each table is for, and what each column holds, is kept in the database itself (`cfg_table` and `cfg_column`) and is read before a table is used.

Neither database is the primary source for the Hebrew, Greek and Aramaic material the programme works with. STEP Bible remains the source every Strong's number, gloss, meaning parse and verse reference traces back to. The base data in `iba.db` is the programme's verified, structured copy of what STEP returns, a working record built from it and not a replacement for it.

The sections that follow work through what each database holds: the registry of onboarded words and the surface and collection tables that hold the scope, the term and lexical substrate, the verse layer, the node, the observation tables, the question catalogue, the claims and narrative, and the prose store. A table this chapter does not name is not part of the current architecture, whatever its history. Tables kept only as the record of earlier methods are not read by the current study.


### Surfaces, collections and the registry

> Where scope is held: the surface and collection tables, the subgroup tables, and the thin registry that onboards a new word.

_`prog_data_registry`  ·  type id 56  ·  chapter_no 4  ·  sort 23_

*Section id 23 · status `draft` · v1405 · 302 words · author `claude_code`*

The scope of the study is held in the surface and collection tables of `iba.db`. `surface_term` holds each surface, the English word or phrase of the ESV, with its surface group (behaviour, inner_being_state, entity or other), the reason for it, who judged it and its state, together with its base. `surface_derivation` records how a derived form relates to its base, `surface_event` keeps every change to a surface with its state before and after, `surface_flag` holds the flags raised against surfaces, and `ai_call` keeps each call to the local model with the prompt version that gave it. What a model judged stays inferential until the researcher confirms it.

`collection` holds the collections: a name, a status (confirmed, merged or retired) and the core word it is formed around. `collection_link` places each surface as a member by tier (core, synonym, opposite, gathered or phrase), keeps the link a surface holds in its own right, and flags a link that is shared. `collection_listing` holds the listed candidates. A collection's members carry the verses. `collection_subgroup` and `collection_subgroup_surface` hold the subgroups of a collection and the index of its surfaces, each with its state: placed in a subgroup, set aside with a reason, or not yet placed.

`word_registry` is the entry point for onboarding a new word of the base data: a row carries the English headword, why it entered, and its onboarding state. It is deliberately thin and answers one question: whether this word is in an onboarding run, and where that run stands. The record of the study's scope is not the registry; it is the surfaces and collections above. A word's analytical record is not accreted onto a registry row; it is built in the tables the rest of this chapter describes, keyed on the Strong's code, the surface, the collection and the node.


### Terms

> The term layer: the Strong's tables, the span and the mechanical reading of the verse, with the key each is held on.

_`prog_data_terms`  ·  type id 57  ·  chapter_no 4  ·  sort 24_

*Section id 24 · status `draft` · v1531 · 363 words · author `researcher`*

The term layer lives in `iba.db`, as a chain of small, single-purpose tables, each named for the processing layer it represents.

`word_strong` is the discovery record: one row for each pair of an English word and a Strong's code that STEP's word search returned. It carries the link only, with no term detail, and determines which Strong's codes an onboarding run touches.

`strong` is the term's identity: one row for each Strong's code, unique and global to the whole study. Meaning is deliberately not carried on this row; it is normalised into its own tables, `strong_sense`, `strong_meaning_tree`, `strong_lexicon`, `strong_lsj_parsed` and `strong_mounce_parsed`, which hold the sense hierarchy and the LSJ and Mounce enrichment. `strong_related` carries the associative and root-family relationships between codes and is keyed on the exact lettered code, never on the base code.

`lemma_inventory` is the independent substrate over which the seed net runs, imported from the earlier study and deliberately not derived from the registry, so that it works as a completeness control. `candidate_seed` is the over-inclusive candidate assessment built from it, a potential and not a definite decision about whether a lemma belongs in scope, with the lexical stage as the real test.

The verse-level lexical substrate is a further chain. `span` is the immutable source parse, one row for each tag of STEP's own interlinear presentation of a verse, kept verbatim so the parse can be re-derived; a combined-unit tag is kept as one row and is not split. `span_candidate` is the candidate stamp over a span. `verse_lexical` is the derived mechanical reading of the verse: one row for each Strong's code within a span, with the cluster codes of the Strong's code in its `role` column (an association copied onto the occurrence, and not the role a word has in a finding, which is set out under the node), the sense selected by stem and voice, and any ambiguity named and not resolved. It records the verse's structural composition and says nothing of what a word does for the inner being. It is derived once from the span and read from there; everything after it reads the derived row and does not derive again from `span` or `strong`.


### Ownership and cross-registry references

> How overlap of vocabulary is handled: each surface in one collection, the collection a node carries, and the keying of the term layer on the Strong's code.

_`prog_xref_architecture`  ·  type id 28  ·  chapter_no 4  ·  sort 25_

*Section id 25 · status `draft` · v1436 · 232 words · author `claude_code`*

Inner-being vocabulary overlaps, and the architecture answers the question of overlap at the level of the surface and the collection. Each surface of the scope is a member of exactly one collection. A surface carries the collection of its own link where it has one, and otherwise the collection of its base: a derived form is a surface with a link of its own, so it is read by that link. A node carries the one collection of its surface by this rule.

Every table of the term layer is keyed on the Strong's code or the span, never on a registry row. A term's record accumulates at the Strong's-code level from the start, so there is no per-word copy of that record to reconcile across words that share a term. `word_strong` is a many-to-many link, because a Strong's code can be discovered through more than one English word, but this raises no question of ownership: the record a Strong's code accumulates does not live under any one word.

An English surface relates to the original text through its Strong's codes, and a surface that carries more than one sense in the verses is read by the code of each sense. `strong_related` is keyed on the exact lettered code. The base of a surface is an instrument for gathering like words into a collection and never the member of a collection itself.


### Verses and the context layer

> The verse layer: the verse table, when a verse is in scope, and how every observation is tied to its verse.

_`prog_data_verses`  ·  type id 58  ·  chapter_no 4  ·  sort 26_

*Section id 26 · status `draft` · v1437 · 173 words · author `claude_code`*

`iba.db`'s `verse` table carries the addressable identity of a verse: its `osisId`, its reference, and the full interlinear HTML of STEP kept verbatim so that `span` can be re-derived. Every verse of the Bible is held, and each has its mechanical reading in `verse_lexical` (the previous section).

A verse is in the study's scope when it holds an occurrence of a member surface of a live collection. The entity and other surfaces of an in-scope verse are in scope as nodes of the observation that covers them; a verse that holds only entity or other surfaces is out of scope and is not touched. The scope is read from the tables: an analysis reads tables and never a working file.

The verse is the place where every observation is tied to the text. Each observation is applied to its verses, words and surfaces by nodes (the section on the node), and a reading of a verse begins with the verse itself, read in its passage with all the observations already recorded for it.


### The node

> The node: how one observation is applied to a verse, a word and a surface, its roles, and the rules that keep nodes and observations consistent.

_`prog_anchor_verse`  ·  type id 27  ·  chapter_no 4  ·  sort 27_

*Section id 27 · status `draft` · v1540 · 964 words · author `researcher`*

The programme anchors a finding to a specific piece of verse evidence by the **node**. A node applies one observation to one verse, one word and one surface: it carries the verse reference, the `verse_lexical` row of the occurrence (which fixes the surface, the Strong's code and the morph code), the collection and subgroup of the surface, the role the word has in the finding, and the stage that produced it. The node is how the study finds things: the observations of a collection are found through the collection on the node, and those of a subgroup through its subgroup.

Where an observation refers to several variants, such as verses, surfaces or Strong's codes, it has a node for each variant. A live observation has at least one live node, and a node cannot exist without a live observation. Two live nodes of one observation whose indexing columns are all the same are either incomplete or a duplicate: an incomplete node is completed, and a duplicate is withdrawn with its reason. A node is withdrawn, never physically deleted.

The role of a node is what the word is for the finding the observation states, and it is judged by reading the verse. It is judged for each occurrence, against what the verse is about, the inner-being operation it carries, and never taken from the cluster tag, from the collection the surface is in, from the word's other occurrences or from the part the word usually plays. The same surface can therefore be a characteristic in one verse and a qualifier in another. Each role is its own observation, applied by its nodes to the verses where that role holds, and the difference between the verses is carried by those observations and not by the surface's group.

The roles fall into four sets. Two are relevant to the inner being. A **characteristic** is a word that behaves as a characteristic of the inner being: it carries the main inner-being operation of the verse, and it is the word the finding is about. A **qualifier** binds to a characteristic and gives it value or context in place: its manner, measure, strengthening, ground, cause, object or setting, or the negator that makes an act a refusal, and there is no fixed list. The observation of a qualifier states what it gives the characteristic; the word has no account of its own from that verse, and it is carried as a face of the word and as an interrelationship. In 'I cried aloud to the Lord', *cried* is the characteristic and *aloud* a qualifier giving volume, unless the verse treats the loudness as a purpose or effect of its own, in which case it is part of the characteristic. A word that only qualifies, or that has no inner-being role of its own, is not analysed by itself: it is bound to the characteristic it qualifies, or excluded. Three roles bear on the finding without being its characteristic or qualifier: the **object** (what the act is directed at, or its content), the **relational target** (the party the act engages) and the **enactment** (the outward act the inner act produces). `standalone` records that the word was read in the verse and holds nothing for the inner being: it is neither a characteristic, nor a qualifier of one, nor the object, relational target or enactment of one, and it binds to nothing, as a function word does, or a word that no characteristic in the verse reaches. It is a role and not an absence of one: it is a judgement of the reading, made for each occurrence, and where a standalone word proves to qualify a characteristic it is a qualifier of it. `lexical` records that the word was read lexically and that its inner-being role has not been assessed; the nodes of stages 1 to 3 carry it, because those stages state nothing of the inner being.

A party's role is an observation and not a field of the node. 'An evil spirit acting towards the inner being' is one observation, applied by its nodes to every verse and word it affects; the programme keeps no table of parties. A role is never a verdict: a verse is not closed as 'only a qualifier' or 'no bearing', and what is recorded is what the verse is (Chapter 2, the inner-being layer).

The study's earlier method named three roles, characteristic, qualifier (or process-element) and standalone, and they remain the core. The node adds the object, the relational target and the enactment for the words that bear on a finding, and `lexical` for the words not yet assessed. Two other columns are also called role and are not the role of a node: `verse_lexical.role` holds the cluster codes of the word's Strong's code copied onto each occurrence, an association with no reading of the verse in it, and `verse_span_index.role` in `bible_research.db` holds an older analytic role set by earlier campaigns, on part of the spans and with a vocabulary that grew by use. Neither is read as the role of a word in a finding.

The role is required on a node that names a word, but it is not set on every node. On 2026-11-21, of the 68,426 live nodes, 11,926 had no role: all of them nodes written by earlier methods. A word judged to have no bearing in a verse is written to its observation, as a silence, with the role standalone, and a re-evaluation of the verse reconsiders it; a word that proves to have a significant role in conjunction with another surface is given that role. Setting the earlier-method roles has been handed to the collection reading, which has not yet reached it, and a role found wrong on an earlier-method node is corrected there.


### The analytical grouping: collections and subgroups

> The analytical grouping: the collection, the subgroup, the observation tables and the ledger of the layered reading.

_`prog_data_dimensions`  ·  type id 59  ·  chapter_no 4  ·  sort 28_

*Section id 28 · status `draft` · v1545 · 360 words · author `claude_code`*

The programme's analytical grouping is the collection and, within it, the subgroup. A collection gathers surfaces of like or related behaviour (Chapter 2). A subgroup is a group of the surfaces of one collection, made so that the collection can be read in units: the subgroup is the unit of reading, and its surfaces are read together in each layer. The verses of a subgroup's surfaces travel with it through the nodes, so that an observation made for the subgroup is found for each of its verses. The concept tables of an earlier method are retired and the collection takes their place. The method that grouped the surfaces of the first collection did not serve the purpose the subgroups are for and is withdrawn; the subgroups are formed again when collection processing starts.

The readings of a collection are recorded in the observation tables. `ib_observation` holds one finding, with its stage, its kind (for example term, face, group, enrichment, pairing or relation), its text and its status. `ib_node` holds the occurrences the observation applies to (the previous section). `ib_observation_change` keeps every change to an observation with its reason, so that a withdrawal is a soft delete that can be explained. `collection_layer_item` is the ledger of the layered reading: one row for each aspect a step of the reading demands for a collection, which is closed by an observation with its nodes or by a recorded none with its reason, and is then validated by the check.

The values of the stage of an observation are `lexical` (stage 1), `layer-1` and `layer-2` (stage 3). The observations of stage 4, the inner-being analysis, are to be fully specified and built; their stage value is set when the stage is built. Observations made by earlier methods are kept as the history of those methods; a live observation must comply with the rules of the observation and the node, and one that cannot be revived to comply is retired with its nodes as a soft delete with its reason.

The reading process of the app (`Reading.ps1`) takes a reading of one scope through three gates (recorded, synergised, published) and is being aligned to collections.


### The question catalogue and findings

> The standing catalogue of questions as prompts, the findings of the programme as observations, and the kept record of earlier methods.

_`prog_data_questions`  ·  type id 60  ·  chapter_no 4  ·  sort 29_

*Section id 70 · status `draft` · v1411 · 286 words · author `claude_code`*

The standing catalogue of questions is `wa_obs_question_catalogue` in `iba.db`. Its questions are prompts that direct the reading toward what a word's occurrences may show; they are never answers to force, and a prompt that does not apply to a word is not answered. Step S1 of the layered reading draws on its prompts of the meaning window when a word is read in its verses. A reader must check which table a piece of work queries and must not assume that a table name alone identifies it, because a table of the same name exists in the other database as the record of an earlier method.

The findings of the programme are the observations of the previous section. Each is tied to its verses by nodes and is founded in the verse. An observation never repeats the verse text, beyond the number of consecutive verse words the configuration allows, and the same wording and meaning is never held as two observations: a second live observation with the same text is a duplicate and is withdrawn with its nodes moved to the first.

Observations of earlier methods are kept as the record of those methods. Their kinds, tags and parts need not be consistent or a full read, provided they comply with the rules of the observation and the node. The collections are read again, in the stages of Chapter 2, to enhance them. The researcher's earlier instructions and answers, and the reasons for each change, are in the escalation record and the observation change log, and are read there before a question is put.

The universal finding store and the flags of earlier methods are kept as history and are not read by the current study.


### Claims and the narrative

> Claims and the narrative: the claim tables, the narrative chapters and sections, and how claims are bound to the observations that found them.

_`prog_data_synthesis`  ·  type id 61  ·  chapter_no 4  ·  sort 30_

*Section id 30 · status `draft` · v1548 · 274 words · author `claude_code`*

The account of the programme is built from the observations upward through two tables of claims and a narrative, all in `iba.db`. `narrative_claim` holds each **claim**: a statement derived from sources, the verses and, later, the science reading, that goes beyond their mere text, held in its own plain wording. A quotation is not a claim. `narrative_claim_source` holds the sources of each claim and its verdict against the wording of the original essay: stands, restated, widened, corrected or new. `narrative_claim_telling` records how the narrative tells each claim: in full, in part or by pointer. Each claim is therefore traceable to its sources and to the place in the narrative where it is told.

`narrative_chapter` is the authority for which chapters exist, their order and their purpose. `narrative_section` holds the sections of each chapter, whose text is a block; `narrative_citation` holds the citations and `narrative_update` the record of updates to the narrative. The chapter files are exports from the database; the database is the home of the narrative.

The claims are formulated from the observations in stage 5 of the reading, which is not yet decided. What is established is that a claim is bound to the observations and nodes that found it, and that the claims of a collection are formulated after its inner-being analysis (stage 4), which is to be fully specified and built. The existing claims come from an earlier method and are not yet cross-linked to the collections; that cross-linking, and the re-evaluation of each claim against the observations, belongs to the work of stages 4 and 5. Larger claims are not made before the smaller claims on which they rest.


### The prose store

> The prose store: the section types, the sections and the glossaries, the system-versioned lifecycle, and the steps of Prose.ps1.

_`prog_data_prose_store`  ·  type id 62  ·  chapter_no 4  ·  sort 31_

*Section id 31 · status `draft` · v1413 · 386 words · author `claude_code`*

The prose store is `bible_research.db`'s database-canonical mechanism for authored narrative and for the programme prose, including this chapter. `prose_section_type` is the dictionary of stable named slots prose can be written into, and it is controlled vocabulary: a new type is created only on the researcher's instruction naming its code and its place in the book. `prose_section` is the content, one row for each titled section, carrying its body, its version and its status (draft, in review, approved or archived). The programme glossary and the contentious glossary are kept in the same store, as sections of their own types; Claude keeps the programme glossary up to date and its entries enter as draft, while an entry in the contentious glossary is the researcher's to settle.

The store's lifecycle is system-versioned: a section that is superseded is updated in place, and its prior content is kept in `record_change_log`, whose payload holds what a change overwrote and whose row is pointed to by the section's version. No edit is silently lost and the full history is queryable. `record_change_log` is a project-wide change-audit log, and a prose write produces its log row in the same transaction as the write.

`prose_section_verse_link`, `prose_section_dimension_link` and `prose_section_finding_link` connect a prose row to the verses, dimensions and findings it discusses, so that a query can start from the evidence and find the prose that discusses it, or the reverse.

The store carries its own quality-flagging mechanism. A flag raised against the corpus is followed by a proposal that searches the active corpus for a literal match and previews the replacement, and an approved fix is applied as a patch, the same mechanism that carries every other prose change.

`Prose.ps1` is the registered front door onto the store: `Extract` for programme-prose extracts, `Search` for a search of the active sections, `ExportChapter` and `ImportChapter` for the editable-Markdown round trip, `Flag`, `FlagFixPropose` and `FlagFixApply` for the quality workflow, `SetStatus` for the review status of a section, and `ApplyPatch`, which applies a reviewed patch in one transaction or not at all and is run as a dry run first. Every step reads its configuration from `cfg_prose` and not from a constant. The database remains canonical: a draft file is the input, the patch reads it, the patch step writes it, and any extract is regenerated from the database afterward.


### Capture mechanisms

> The capture mechanisms: prose through the Prose.ps1 round trip, observations through the layered reading, and open items through the escalation table.

_`prog_data_obslog_pipeline`  ·  type id 77  ·  chapter_no 4  ·  sort 32_

*Section id 66 · status `draft` · v1414 · 318 words · author `claude_code`*

The programme's capture mechanisms are three, each serving a different kind of work, and they share one discipline: a write to a database is always a distinct, auditable step from the work that produced it, and the record of that write outlives the session that made it.

First, for programme prose and the glossary: the `Prose.ps1` round trip described in the previous section. A chapter is exported to editable Markdown, the body under each section's fixed heading is edited, the import generates a patch, and the patch is applied through the dry run first and then the live apply. No step in that chain writes to the database directly.

Second, for the observations of the reading: each step of the layered reading is run through the app. A working file is pulled for the open rows of the ledger with their evidence, Claude reads and fills each row, and the record step checks the whole file (a problem anywhere refuses all) and writes the observations, their nodes and the ledger answers in one transaction. The check then validates every answered row against the tables. A row answered again withdraws its earlier observation with its reason in `ib_observation_change`. The grouping of the surfaces is run in the same way, with its own validation and a scrutiny report for the researcher.

Third, for anomalies, judgement calls and anything requiring a decision that the running code cannot make on its own: the `escalation` table, described in the next chapter. An item is raised with the researcher's own words quoted verbatim, an explicit resolution kind and a next action, and is tracked to closure through `Escalation.ps1`.

Where a step that a routine needs is not registered in the app, reconstructing it from past output files is itself the signal that a required step is missing and is not a puzzle to solve from precedent; the missing step is registered and built first.


## Data integrity & governance

### Document validation and quality-flag architecture

> The standing checks that tell a session whether the application, the record and the study are coherent, and the quality flags of the prose store.

_`prog_validation_standard`  ·  type id 29  ·  chapter_no 5  ·  sort 104_

*Section id 32 · status `draft` · v1415 · 483 words · author `claude_code`*

The programme's validation architecture is `iba.db`'s own, and it operates continuously and not only at phase boundaries. Five standing checks together tell a session whether the app, the record and the study are coherent.

`configmaint.validate` sweeps the whole `cfg_*` configuration store and the data it governs. It covers enum violations (a value that should be drawn from a `cfg_enum` list but is not), orphan configuration (a `cfg_*` row that nothing reads), inactive-reference coherence (something still pointing at a row marked inactive), write-grant completeness (every writer that touches a table holds a grant for it), stale `filled_by` claims, report-path persistence (every quality-check step writes its output where configuration says), the currency of the glossary against the terms it must define, and documentation-currency checks that tie `GOVERNANCE.md` and `BUILD.md` back to the configuration they describe. Each concern was added when a real gap was found, not designed in advance.

The **compliance check** (`Compliance.ps1`) runs at the start of every session: Claude restates in its own words every general rule in force, with the work in hand, and the check must pass before work begins; evidence for each engaged rule is added as the session produces it, and the close checks it.

The **session-close checks** compare what the session did, decided and left open against the record, and nothing is committed while a finding is open. `Spine-Check.ps1` checks the spine of the project's own records, and the **thread audit** (`Escalation.ps1 -Action ThreadAudit`) checks the threads of open items for handles that do not resolve, items without a note, referred items closed while the thread item is open, and registers out of date.

For the reading, the **layer check** validates every answered row of a step against the tables (its stage, kind, nodes, roles, collection and every Strong's code of an enrichment) and reports what is open, what failed and what the data demands that has no row. The **grouping check** validates a grouping of surfaces and writes a scrutiny report for the researcher. A boundary check keeps the observations of the lexical stages free of what a word does for the inner being.

Gap status is expressed as a controlled vocabulary wherever the schema has one: `cfg_enum` names every allowed value of every enumerated column, and the enum check catches a value that has drifted outside its declared set.

**Quality flags.** `wa_quality_flag_types` and `wa_data_quality_flags` serve the prose store: a `PROSE_QUALITY` flag names a concern about the prose corpus generally, such as a stale terminology reference, without being tied to one section at raise time, because the section is found by search at fix time (`Prose.ps1 -Step FlagFixPropose`). A flag names that attention is due, not an analytical conclusion, and it does not block anything on its own. Where a flag concerns a genuine judgement call and not a mechanical fix, it is raised as an escalation instead, the mechanism described in the section on instruction override.


### Soft-delete discipline

> The soft-delete discipline across both databases, its table-level form, and the rule against hard deletes.

_`prog_delete_discipline`  ·  type id 30  ·  chapter_no 5  ·  sort 105_

*Section id 33 · status `draft` · v1222 · 310 words · author `claude_code`*

The programme does not physically delete rows as a matter of course, and the discipline spans both databases. `iba.db`'s base-data and process-control tables carry a uniform `deleted` column; `bible_research.db`'s analytical tables carry `delete_flagged` (or, on some tables, `delete_flag`). Both are the same convention under different names: the row stays in the database, queryable for audit, excluded from active queries by a filter on the flag.

A table-level form of the same discipline sits above the row-level one. `cfg_table.inactive` marks a whole table as superseded, not just individual rows within it — the mechanism by which the project's own governance record can state precisely which of a database's tables are the live source of truth and which are not, without deleting or hiding either.

The prose store's own lifecycle mechanism is Model A: system-versioned temporal tables (escalation #836, 2026-08-24). A revision mutates the row in place under SQLite's own system-versioned mechanism rather than inserting a new row and chaining it by hand; nothing is silently lost, the full history is queryable, and the guarantee now comes from the database engine itself rather than application bookkeeping.

The discipline is not absolute. A hard delete is reserved for content that genuinely has no future reader and has no live consumer to preserve continuity for — a decision made deliberately when it happens, not a default falling-through. Soft-delete is the default because the programme revisits its own work and needs the trail that decision-making left behind.

Soft-delete is not the same as set-aside: a row marked not-relevant to the current analytical scope is a different fact from a row marked removed from scope entirely. The purpose of the whole discipline is continuity under revision — the programme revisits words, re-derives readings, and rebuilds mechanisms; a database that deleted rows as its understanding changed would lose the very trail that makes its current state defensible.


### Record consistency with sources

> How the record stays consistent with its sources: field authority, observation-reference consistency and STEP data provenance.

_`prog_field_authority`  ·  type id 31  ·  chapter_no 5  ·  sort 106_

*Section id 34 · status `draft` · v1416 · 358 words · author `claude_code`*

The programme's research record is a derived record, resting on STEP Bible for lexical and verse data and on the researcher's own judgement for the analysis. Three disciplines keep the record consistent with those sources.

**Field authority.** The mechanism for declaring which field wins when two hold the same information is `cfg_column`: every column of every table, in both databases, is listed with a `use` text and, where relevant, a `source`, an `expectation` and a `filled_by`. `expectation` is enforced at write time (value-quality and enum checks, part of `configmaint.validate`); `source` and `filled_by` are recorded and checked for non-emptiness; `use` is documentation. Before a table or column is used for a count, a finding, a claim or a design, its recorded meaning is read in `cfg_table` and `cfg_column`, and a statement about what a column holds is made only from that text or from a test over all its rows. Where the recorded text is missing or thin, that is raised as a finding and the column is not assumed. Where the schema carries the same fact in two places, the `inactive` flag on the `cfg_table` row of each copy declares which copy wins. A column added to an existing data table is registered in `cfg_column` by the stated procedure before it is used.

**Observation-reference consistency.** An observation that is revised or withdrawn is not overwritten or deleted: its change is kept in `ib_observation_change` with the reason, and a replacing observation points to the one it supersedes. A reference to an observation is a reference to its identity, and its meaning is read by following the chain and not assumed fixed.

**STEP data provenance.** STEP Bible remains the primary source for every Strong's number, gloss, meaning parse and verse reference in the corpus. The live provenance record for the base data in `iba.db` is the `run` table together with `cfg_connection` and `cfg_api`, which record what STEP route was called, under what configuration, and what came back.

The governing principle is the same for all three: the record is derived and not primary, and its integrity depends on the chain from source to stored row staying traceable across every revision.


### Backup and schema migration discipline

> Backup and schema migration discipline for each database, and the named snapshots kept before a change to the collections or the observations.

_`prog_backup_discipline`  ·  type id 32  ·  chapter_no 5  ·  sort 107_

*Section id 35 · status `draft` · v1417 · 273 words · author `claude_code`*

Each of the programme's two databases carries its own backup and versioning discipline, governed by one principle: every state-changing operation is recoverable, and every schema or configuration change is traceable to a specific, dated event.

**`bible_research.db`.** `schema_version` carries the schema's own migration history, each entry a numbered migration with a description and an applied timestamp. `apply_session_patch.py` takes a backup of the whole database before every live write, automatically, as part of applying a patch. Off-repository durability is handled outside the patch mechanism by a daily backup of the database file and a daily mirror of the whole project, each alerting on failure.

**`iba.db`.** Configuration versioning is `cfg_meta.config_version`; every whole-reload event is logged to `cfg_change_log`; and every row-level change to configuration is logged to `cfg_change_detail` with its table, operation, `where` and `set` clauses, the before-state and when it was applied. `run.py` takes a pre-run database snapshot before every new run, and `retention.snapshot_keep_count` governs how many of these are kept before the oldest is pruned. A routine that would take a snapshot on every iteration of a large batch can suppress it deliberately where the cost is disproportionate to the risk. A named snapshot is taken before a change to the collections or to the observations and is kept (`iba/app/db/snapshots/kept/`), so that the change can be rehearsed on a copy, its counts predicted and checked, and, if it fails, undone from a known state.

The principle that unifies both disciplines: a change without a recoverable prior state is a risk the programme does not accept, and a change without a record of what changed and when is a change the programme cannot later account for.


### Patch and directive failure protocol

> The failure protocol: dry-run rejection of patches, routing of failures by cfg_on_fail in the application, and escalation of what cannot be resolved mechanically.

_`prog_patch_failure_protocol`  ·  type id 33  ·  chapter_no 5  ·  sort 108_

*Section id 36 · status `draft` · v1225 · 261 words · author `claude_code`*

Patches and directives remain the two channels by which changes reach `bible_research.db`. `apply_session_patch.py`'s dry-run mode, used before every live apply, is the standing rejection check: a patch that violates a schema constraint or a controlled-vocabulary rule is caught before it ever reaches the live database.

`iba.db` runs a parallel failure protocol, built around `cfg_on_fail` rather than around patch review. Every step in the app's run sequence has a registered `(step, condition) → path` entry: `report-stop` halts the run and surfaces the failure; `pause-continue` and `report-continue` let the run proceed past a non-fatal condition while still surfacing it; `self-heal` lets a step correct a known, narrow condition on its own. Changing how a specific failure is handled is itself a config change — moving `cfg_on_fail` for a given `(step, condition)` from one path to another through `Config-Maintenance.ps1 -Step Propose` changes the app's behaviour with no code touched.

Where a failure — on either side of the split — cannot be resolved by a mechanical retry or a rejected patch, it is raised as an escalation. An escalation carries a `resolution_kind`: `decision_required` for a genuine judgement call that must go to the researcher and stops there, or `self_correctable` for a condition Claude can fix and record, with the fix itself named in the resolution.

The protocol's governing principle: no failure is allowed to leave either database in an inconsistent, unrecorded state. The mechanism enforcing it is split along the same line as the databases themselves — patch review for `bible_research.db`'s analytical content, `cfg_on_fail` routing and escalation resolution for `iba.db`'s process-control and base-data operations.


### Instruction override and cross-document reference discipline

> How the researcher's direction travels: configuration changes by proposal and approval, the escalation table for everything else, and where the rules live.

_`prog_instruction_override_protocol`  ·  type id 34  ·  chapter_no 5  ·  sort 109_

*Section id 37 · status `draft` · v1418 · 447 words · author `claude_code`*

**Instruction override.** The researcher's in-session direction is authoritative and does not wait on document revision to take effect. The path it travels for a configuration row is `Config-Maintenance.ps1 -Step Propose`, the one sanctioned route in a standard session. A proposed change names the table, the operation, the `where` and `set` clauses, and a question stating why the change is wanted and what it affects; the command runs a coherence check and pauses, printing a run id. The researcher answers through `Escalation.ps1 -Action Update`, moving the raised escalation through `ready_for_approval` to `approved` (or `reject` or `revise`), each with a resolution; only then does the same Propose command, re-run against the same run id, commit the write, logged row by row to `cfg_change_detail`. In a Developer Mode session, which the researcher chooses when the session starts and which is never switched within it, the app is built or fixed without the per-row approval gate, through one idempotent logged migration; every rule still applies. An override approved this way is from then on no longer an override: it is the rule the configuration holds, and every part of the app that reads it sees the new value with no code edit.

For anything that is not a configuration value, such as a genuine open question, a discovered anomaly, a clarification needed or a piece of work assigned across a session boundary, the `escalation` table is the single project-wide mechanism (`governance.escalation.scope`), covering the whole project. An escalation carries a type, a state that moves from `raised` through `re-assigned`, `on-hold` or `in-progress` to a terminal state, a `next_action` and a `resolution_kind` (`decision_required` or `self_correctable`). The researcher's words that bear on an item are recorded on it verbatim in the same turn. `Escalation.ps1` is the operational front door, with the actions Raise, Update, History, List, Correction, ResolveSelfCorrectable and EscalateToDecision. Open items that are pointers from an analysis in hand to related work are registered with their origin and anchor, scoped to specific verses, and cleared at some point.

**Where the rules live.** `CLAUDE.md` is a pointer file: it holds no rules, no state and no history. The rules, settings and procedures of the project are configuration rows, printed at the start of a session or delivered at the first use of the operation they govern, and the control map (`cfg_control_home`) names the home of each kind of content. Where a document and its home disagree, the home wins.

The two disciplines together describe a cleanly split system: a configuration rule is proposed, coherence-checked, approved by explicit decision and committed with a full audit trail; a genuine open question or anomaly, anywhere in the project, is raised, tracked and resolved through the escalation table.


### Documentation–implementation alignment

> The principle that rules, schema, documents and prose are not assumed to be synchronised, and the rules that keep them aligned.

_`prog_doc_impl_alignment`  ·  type id 63  ·  chapter_no 5  ·  sort 110_

*Section id 38 · status `draft` · v1419 · 409 words · author `claude_code`*

The programme's rules, its database schema, its instruction documents and the prose that describes the work are four surfaces that must stay in alignment for the record to be trustworthy. Alignment is not a state the programme can declare once and rely on afterward, and the principle is itself a configuration-governed rule.

`governance.rules_must_be_config_driven` states it directly: no operational or process rule may exist only in `GOVERNANCE.md`, `BUILD.md`, `USER-GUIDE.md` or memory without a referenced `cfg_*` row recording it as the evidence that the configuration control is in operation; any deviation found requires an escalation. On a new instruction, the first thing established is that the rules governing it are fully captured and correctly interpreted in the configuration. `governance.governance_md_on_rule_change` pairs it on the documentation side: a rule change is set in `cfg_*` first and `GOVERNANCE.md` updated in the same unit of work. `governance.build_md_on_code_change` runs the equivalent check for code: any change under `iba/app` updates `BUILD.md` in the same unit of work. The control map `cfg_control_home` states, for each kind of content, its one home: content lives in its kind's home only, and any other document points to it and does not restate it.

A further rule closes the loop: `governance.past_precedent_investigation_signals_missing_config`. If running an already-registered instruction requires first reconstructing how it was done in the past, by reading `BUILD.md` history, diffing archived output files or inferring a missing step from precedent, instead of a live configuration row saying what to run, that investigation is itself the signal that a required mechanism is missing, and the response is to stop and close the gap, not to proceed on the reconstructed precedent. A table or mechanism is added by the stated procedure, and a column added to an existing data table is registered before it is used.

The record is the project's memory. The researcher's earlier instructions and answers are in the escalation record and the session logs, and are read there before a question is put; a question the record answers, or that later work made moot, is not asked.

Where a mismatch between surfaces is detected, the response is consistent in shape: the mismatch is named, an escalation is raised if it is not a mechanical fix, and the resolution updates whichever surface was wrong in the same unit of work, with the change recorded in `cfg_change_detail` or `BUILD.md` as appropriate. A mismatch is not left open on the assumption that documentation will eventually catch up to practice, or practice to documentation.


## Instruction corpus

### Global rules

> Where the programme's binding rules live: configuration rows, printed at the start of a session or delivered at first use.

_`prog_instr_global_rules`  ·  type id 64  ·  chapter_no 6  ·  sort 111_

*Section id 39 · status `draft` · v1420 · 244 words · author `claude_code`*

The programme's binding rules are rows of the configuration store in `iba.db`, and they live nowhere else. `CLAUDE.md` at the project root is a pointer file: it holds no rules, no state and no history, and where it and a rule's home disagree, the home wins. `iba/app/GOVERNANCE.md` is the mechanism document for the rule store: how a `cfg_*` row is changed, what is enforced and what is still a convention. The control map (`cfg_control_home`) names the one home of each kind of content.

The rules are `cfg_setting` (scalar rules, each attributed to a module), `cfg_enum` (controlled vocabularies), `cfg_behaviour_rule` with `cfg_behaviour_class` (the classes chat, terminal, sqlite, documentation, filing, llm_output, development and study_method, each with its own rules for how operational behaviour in that class is expected to run), the escalation rules, and the other `cfg_*` tables described in Chapter 5. Each rule is a typed row, readable and changeable through exactly one path (`Config-Maintenance.ps1 -Step Propose`, or a logged migration in a Developer Mode session), and enforced by code that reads it.

A session starts with `/start-project`, which prints every general rule and has Claude restate each in the session's compliance file. The other rules reach Claude at the first use of the operation they govern, so that a rule is read when it is needed. `governance.rules_must_be_config_driven` binds every other rule: no operational or process rule may exist only in prose or in memory, without a `cfg_*` row as the evidence that it governs something.


### Reference

> The live reference layer: the enumerations, the column definitions and the configuration report that other documents point to.

_`prog_instr_reference`  ·  type id 65  ·  chapter_no 6  ·  sort 112_

*Section id 40 · status `draft` · v1229 · 101 words · author `claude_code`*

The programme's live reference layer is `iba.db`'s own: `cfg_enum` holds every controlled vocabulary project-wide, `cfg_column` holds every field's definition, and `iba/app/config/CONFIG-REPORT.md` is the auto-regenerated snapshot of every value in the config store — settings by module, STEP API routes, every work package's steps, the write-grant table, the schema, the enums, book order, and the change log. The report is never hand-edited; it is regenerated from the database.

Any controlled-vocabulary question is answered by pointing at this live reference rather than by restating a value inline — the concentration this achieves is what keeps a vocabulary change from requiring a document-by-document update.


### Patches

> The patch mechanism of bible_research.db: its format, the PROSE operation and the dry-run gate.

_`prog_instr_patches`  ·  type id 66  ·  chapter_no 6  ·  sort 113_

*Section id 41 · status `draft` · v1421 · 153 words · author `claude_code`*

The patch mechanism is live for `bible_research.db`: a JSON object with a `_patch_meta` header, an `operations` array of typed operations against named tables, and a `_patch_summary` footer. `scripts/apply_session_patch.py` is the applicator and is run as a dry run before every live application. The format reference is held in the archived instruction document `Workflow/Instructions/archive/wa-patch-instruction-v2_11-20260507.md`.

The operation type in use is `PROSE` (insert, supersede and set_status against `prose_section`), the mechanism by which every revision of the programme prose and the glossary is made; `Prose.ps1 -Step ApplyPatch` applies a reviewed patch in one transaction or not at all. `REPAIR` operations, for cascading resets, remain part of the format.

Patches are authored, reviewed and applied in distinct steps: authored by Claude, reviewed by the researcher where review is warranted, and applied by the app. `_patch_meta.researcher_approval` tracks the approval state, pending until it is reviewed. No patch reaches `bible_research.db` without passing through this format and its dry-run gate.


### Directives

> The directive mechanism of bible_research.db, and how a schema change reaches iba.db.

_`prog_instr_directives`  ·  type id 67  ·  chapter_no 6  ·  sort 114_

*Section id 42 · status `draft` · v1422 · 129 words · author `claude_code`*

The directive mechanism is live for `bible_research.db`: a plain-language instruction with five required elements (a title and identifier, what is to be done and why, the operations asked for, the expected outcome, and the confirmation to be returned), used where a change cannot be captured as a declarative patch, most often schema preparation ahead of a patch that depends on it. The format reference is held in the archived instruction document `Workflow/Instructions/archive/wa-directive-instruction-v1_4-20260506.md`. The schema of `iba.db` changes through the app's own migration scripts under `iba/app/migration/`, each recorded in `BUILD.md` in the same unit of work (`governance.build_md_on_code_change`).

Directives and patches are equal peers within their shared scope: together they are the exhaustive set of ways `bible_research.db` changes, and a directive, like a patch, does not reach the database without review.


### Claude Code operating guide

> Where the operating guidance for Claude Code lives: the start and close routines, the point-of-use rules and the application documents.

_`prog_instr_claudecode`  ·  type id 68  ·  chapter_no 6  ·  sort 115_

*Section id 43 · status `draft` · v1423 · 165 words · author `claude_code`*

The operational guidance for how Claude Code works is held in the application and its documents. `/start-project` and `Start-Iba.ps1` check the configuration, the data and the STEP connection, report how the last session ended, and print the general rules; the point-of-use rules deliver every other rule when an operation is first used; and `/session-close` checks and records the end of a session. `iba/app/USER-GUIDE.md` is the entry point for using each tool of the app, `iba/app/GOVERNANCE.md` explains how configuration governs the code, `iba/app/BUILD.md` records what changed and why and is read only to assess a past state, and `iba/app/CHARTER.md` states what the app is for. This chapter holds the patch and directive mechanisms and the prose-store operations of the `bible_research.db` side.

These do the work of a single operating guide. The rules are not held in a document that can lag: they are configuration rows that print at the start of a session and arrive at the point of use, and the documents point to them.


### Registry management guide

> The registry management guide: none is held, and why.

_`prog_instr_registry_guide`  ·  type id 69  ·  chapter_no 6  ·  sort 116_

*Section id 44 · status `draft` · v1424 · 114 words · author `claude_code`*

`iba.db`'s `word_registry` is a deliberately thin table (the word, its source, its status and timestamps), described in Chapter 4. It is the entry point for onboarding a new word of the base data and has not needed a dedicated reference guide, because it does not carry the depth of state that would call for one. The scope of the study is held in the surface and collection tables, whose procedures are in the sections that follow and in `iba/app/USER-GUIDE.md`.

There is, at present, no registry-management guide. This is named as a gap and not papered over: if the registry accretes more fields as the method matures, a guide will need writing at that point.


### Base data

> How the base data is built: the entry point for a new word and the mechanical reading of the verse.

_`prog_instr_session_a`  ·  type id 70  ·  chapter_no 6  ·  sort 117_

*Section id 54 · status `draft` · v1425 · 87 words · author `claude_code`*

The mechanism for getting Hebrew, Greek and Aramaic word data from STEP into a structured, addressable form is the base-data layer of `iba.db`, described in Chapter 4. The entry point for a new word is `iba\app\ps\New-Word.ps1`, governed by `cfg_step` and `cfg_work_package`, and the mechanical reading of each verse is built by the lexical build of the app. The operational detail lives in the configuration the app reads at each step, per the mechanism Chapter 5 describes, and not in a written procedure a reader follows by hand.


### The collection reading

> How a collection is read through the layered reading: the routines, the order of the steps and the ledger.

_`prog_instr_verse_context`  ·  type id 71  ·  chapter_no 6  ·  sort 118_

*Section id 55 · status `draft` · v1546 · 756 words · author `claude_code`*

The collection is read through the layered reading, run with `Collection-Build.ps1` (`LayerOpen`, `LayerPull`, `LayerRecord` and `LayerCheck`) over the steps and items of `cfg_setting layer.reading`. A step is opened only when the previous one is closed. As the configuration holds it, the lexical analysis of the words (step S1) closes before the grouping of the surfaces is read, and the grouping is finished before the steps that follow; the order of Chapter 2 governs, and the alignment of the two is open. The rows each step demands are the ledger `collection_layer_item`, derived from the data, and each is answered by an observation with its nodes or by a recorded none with its reason. The stages and steps are described in Chapter 2, and the rules that govern them are configuration rows, delivered at the first use of the routine. The evidence on which a collection is read, its member occurrences, its sense and its pairings, is produced by the collection evidence report from the tables.

**The steps the configuration holds.** The ledger of the reading holds four steps today, each opened for one collection only when the one before it is closed. For each, the table gives what it asks, what it reads, how it is done and what it leaves.

| Step | What it asks | What it reads | How it is done | What it leaves |
|---|---|---|---|---|
| S1, the words | In the verses where each word of the collection stands, what does it mean in each, as the verse itself shows it? | The occurrences of the collection by surface and lettered Strong's code (`verse_lexical`), the sense tree, LSJ and Mounce entries of the code, the meaning prompts of the question catalogue, and the observations already recorded for those occurrences. | One ledger row for each word, except a word whose occurrences are all function words. The open rows are pulled into a working file with their evidence, Claude reads and fills each row, the record step checks the whole file and writes it in one transaction, and the check validates each answered row. | One observation for each sense the verses give the word, with the occurrences it holds for (every occurrence in some sense); an occurrence whose sense departs from the usual one is a face observation. Each has nodes of the role `lexical`. |
| 1.1, the groups | What do the surfaces of this subgroup mean, as the dictionary gives their meaning? | The subgroups of the collection, each surface placed in one or set aside with its reason, and the lexicon entries of their codes. Opens only when S1 is closed and every surface is placed or set aside. | One ledger row for each subgroup, taken through the same pull, fill, record and check. | One observation for each subgroup stating the meaning its surfaces share, with a node for each occurrence of its surfaces. |
| 1.2, the Strong's enrichment | What do the Strong's codes of this subgroup say, and does the grouping stand against them? | The lexicon entries of the subgroup's codes. | One ledger row for each subgroup. | One observation for each subgroup giving a short definition from the lexicon and naming the codes that link it to its usage. |
| 2.1, the pairings | What do the other words of the verses show with this subgroup: the words of other collections that stand with it, qualifiers and the words they reach, entities, the direction the text states, the relation between subgroups, a double meaning? | The typed pairings of the evidence report for the collection, and the thresholds the configuration sets for how many shared verses a pairing or a relation needs. | One ledger row for each pairing, qualifier, entity, direction, relation or double meaning the data demands; a recorded none with its reason is allowed where the step permits it. | Observations of the kinds pairing, relation and face, with nodes for the member occurrences and the partner occurrences. |

Every observation these steps leave states what the dictionary, the verses and the stored structure show, and carries no inner-being role. The inner-being layer (stage 4) has no step yet. It is required and is to be fully specified and built: the rules of the inner-being reading that the configuration already holds (the observation items, the kinds of finding, the node roles, the method rules of the reading step and the nuance pointers) are its base, and it reads the observations these steps leave.


### The grouping of the surfaces

> How the surfaces of a collection are grouped: the grouping routines, the status of the method, and how a collection is changed.

_`prog_instr_dimension_review`  ·  type id 72  ·  chapter_no 6  ·  sort 119_

*Section id 47 · status `draft` · v1462 · 178 words · author `claude_code`*

The grouping of the surfaces of a collection is run with `Collection-Build.ps1`: `Index` fills the index of the member surfaces, `GroupPull` writes the working file with the evidence of each surface (its Strong's codes with their lexicon evidence, its occurrences and its link), `GroupRecord` validates the whole file and writes the groups and placements in one transaction with a scrutiny report for the researcher, and `Subgroup` makes the researcher's corrections, each with its reason. The method rules are in the configuration. The method these tools carry did not serve the first collection it was run on and is withdrawn; the subgroups are formed again when collection processing starts. The surfaces are first sorted and gathered into collections by the surface cycle of five modules (Chapter 4), whose map is generated into the configuration report. A change to the collections is made class by class, tried on a copy under a named snapshot, with the counts predicted and checked, and with every change kept in `surface_event`. The procedures are in `iba/app/USER-GUIDE.md` and the rules in `GOVERNANCE.md` and the configuration.


### Readiness of a step

> How a step of the reading is made ready: opening it, pulling its rows and the working file.

_`prog_instr_session_b_readiness`  ·  type id 73  ·  chapter_no 6  ·  sort 120_

*Section id 67 · status `draft` · v1428 · 76 words · author `claude_code`*

A step of the reading is made ready by its opening: `LayerOpen` refuses until the previous step is closed and the grouping is finished, and then derives from the data the rows the step demands. `LayerPull` writes the working file of the open rows, each with its evidence and an empty place to fill. The escalation table's `next_action` and `resolution_kind` mechanism (Chapter 5) covers the adjacent but distinct need of tracking an open item to closure.


### Recording observations

> How the reading's output is recorded and checked: the record step, the layer check and the other capture mechanisms.

_`prog_instr_session_b_output`  ·  type id 74  ·  chapter_no 6  ·  sort 121_

*Section id 68 · status `draft` · v1429 · 104 words · author `claude_code`*

The reading's output is the observation, written directly to the database and not assembled into a separate document. `LayerRecord` checks the whole file (a problem anywhere refuses all) and writes the observations, their nodes and the ledger answers in one transaction; `LayerCheck` validates each answered row against the tables and writes a versioned report naming the gates, what is open and what failed. Each observation states what the dictionary, the verses and the stored structure show (Chapter 2). The other capture mechanisms are those of the last section of Chapter 4: the `Prose.ps1` round trip for prose, and the `escalation` table for judgement calls.


### The narrative

> The reader-facing output: the narrative built by collection, its export, and the claims told in it.

_`prog_instr_session_c`  ·  type id 75  ·  chapter_no 6  ·  sort 122_

*Section id 50 · status `draft` · v1430 · 97 words · author `claude_code`*

The reader-facing output is the narrative of the inner being, held in the database as chapters and sections and built by collection (Chapter 4). Claims are told in it, each with its sources. The narrative is exported from the database, and the export is copied to the inbox of the researcher's publishing site by `Copy-NarrativeToLearning4Comfort.ps1`; there is no direct publishing to GitHub. External publication decisions are outside the programme's method. The cross-linking of the existing claims to the collections, and the update of the narrative to follow them, is part of the claim formulation of stage 5.


### Claims and synthesis across collections

> Synthesis across collections and the claims: what is established, and what is deferred and not built.

_`prog_instr_session_d`  ·  type id 76  ·  chapter_no 6  ·  sort 123_

*Section id 51 · status `draft` · v1547 · 78 words · author `claude_code`*

Synthesis across collections, the relations between the words and concepts of the inner being as a whole, is found in the observations of the collections and in the claims formulated from them. The inner-being analysis made from the verse-lexical observations (stage 4) is a required stage that is to be fully specified and built; the formulation of claims (stage 5) is not yet decided. Neither is built. The study does not carry a separate synthesis process alongside them.


---
*Generated 2026-11-21T06:39:33Z.*