# Prose Edit — Programme — Chapter 2

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file becomes permanent provenance once imported (its archived path is -->
<!-- recorded as record_change_log.change_source, escalation #836) -- do not delete -->
<!-- by hand; the import step archives it automatically on success. -->
<!-- PROSE_EXPORT_SECTION_IDS: 8,9,10,11,12,13,14 -->

<!-- PROSE_SECTION_ID: 8 -->
<!-- PROSE_SECTION_TYPE: prog_meth_overview -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Research methodology -->
<!-- PROSE_CHAPTER_NO: 2 -->
<!-- PROSE_SECTION_TITLE: Research method -->
<!-- PROSE_SORT_ORDER: 9 -->
<!-- PROSE_VERSION: 1447 -->

## Research method

The programme investigates what Scripture reveals about the human inner being. The method proceeds collection by collection from the biblical text, through a disciplined sequence that keeps data gathering, vocabulary, lexical reading, inner-being analysis and claim formulation apart, and that returns to the whole body of findings only through the claims built from them.

The method has five parts, each taking the output of the one before it and nothing else. **The text and its data.** Every verse of the Bible is held with its original-language words, their Strong's identities, meanings and a mechanical reading of the verse's structure that says nothing of what a word does for the inner being. This is the base data. **The vocabulary.** The English words and phrases of the ESV (the surfaces) are judged against the programme's working definition of the inner being, sorted into four surface groups, and the surfaces of the groups behaviour and inner_being_state are gathered into collections of like or related behaviour. **The reading.** A collection is too large to be read in one go, so it is divided into subgroups of its surfaces, and the subgroup is the unit of reading. Each subgroup is read in layers: first the lexical observations for its surfaces and their verses, then the lexical observations for how its surfaces relate in those verses, then the inner-being working made from both. Each finding is an observation tied to verses, words and surfaces by nodes, and each layer deposits its observations for the next layer to use. **The account.** Claims are formulated from the observations, each with its sources, and are told in the narrative, which follows the collections. **Publishing.** The narrative reaches its readers as an export from the database.

The collection is the unit of study. Each collection is taken through the whole path, and the account of a collection becomes a chapter of the narrative. Claude reads the evidence and decides in most cases; the researcher scrutinises that judgement and decides what the evidence cannot settle. No bulk or one-shot analysis, by Claude or by a model, produces the study result, because the nuances of the base data are too varied and interwoven to be reduced to a narrow band.

Scripture is the primary lens. The analytical work is work on the biblical text. Contemporary scientific literature on the inner life is held as a second lens and is engaged in the claims reading, after the biblical reading, as the section on science in action describes. Categories are not imposed on the data; they emerge from it, and a category that cannot be grounded in verse evidence is not one the programme uses. A finding that cannot be traced to a specific verse or lexical source is not a finding the programme records.

---

<!-- PROSE_SECTION_ID: 9 -->
<!-- PROSE_SECTION_TYPE: prog_meth_registry -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Research methodology -->
<!-- PROSE_CHAPTER_NO: 2 -->
<!-- PROSE_SECTION_TITLE: Word selection and the registry -->
<!-- PROSE_SORT_ORDER: 10 -->
<!-- PROSE_VERSION: 1448 -->

## Word selection: surfaces and collections

The programme's scope is the set of surfaces: the English words and phrases of the ESV that name a behaviour or an inner-being state. A word enters the scope by being judged against the programme's working definition of the inner being, and that definition is the admission criterion.

The whole population of surfaces was sorted, by a process of deduction and likeness, into four surface groups: behaviour, inner_being_state, entity and other. The researcher's assessment is that this sorting is roughly nine in ten correct, within an accepted margin of error. The items placed wrongly are found in the deeper analysis and compensated for there; the sorting is not reopened to remove them first. Its purpose is to make the reading of the inner being's working possible: the first two groups hold the behaviours and states that are read, and the other two supply the words that stand with them in the verses.

Scope is built by the surface cycle, five modules that each read and write database tables and never a working file. The first, *group*, sorts each surface by what it names: behaviour (something a person does or undergoes, an act, feeling, thought, speech or choice), inner_being_state (a standing condition or characteristic of a person or of the inner being), entity (a thing that exists: a human, a plant or animal, God in all forms, an unseen power, or a part of any of these) or other (everything else). The second, *structure*, finds the base of a surface by the shape of the word. The third, *AI base*, proposes the base for the surfaces the shape leaves unmatched, through a model on a local server. The fourth, *resolve*, chooses the base from the evidence. The fifth, *collections*, forms the members of each core word's collection. Every change keeps its state before and after, together with the AI call and the prompt version that gave it, so that anything can be traced back. What a model gives is inferential until the researcher confirms it.

The surfaces of the groups behaviour and inner_being_state are then collated into collections by the likeness or relatedness of the behaviour they name. Each surface is connected, through the Strong's code of its base, with its verses, so a collection carries the verses of its surfaces and is the body of text from which the inner being's working is read. A collection is made by putting like words together: synonyms, opposites and gathered words. The base is only an instrument for gathering like words and is never the member; a derived form is a surface with a link of its own; a phrase is one concept and is placed in one collection. Each surface of the scope is in exactly one collection, and is in more than one only in rare circumstances and by the researcher's ruling. The name of a collection is formed from all its members as a concept that covers them. Collections whose members coincide or are close are combined, and a small collection is grouped with like-minded ones unless it is truly unique. Because each collection becomes a chapter of the narrative, it must make sense, must not overlap another, and must tell a coherent story.

A verse is in scope when it holds an occurrence of a member surface of a collection. A word that is neither a behaviour nor an inner-being state, such as a generic evaluative, motion, quantity, speech or copula word, is not a surface of a collection.

---

<!-- PROSE_SECTION_ID: 10 -->
<!-- PROSE_SECTION_TYPE: prog_meth_flow -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Research methodology -->
<!-- PROSE_CHAPTER_NO: 2 -->
<!-- PROSE_SECTION_TITLE: Programme flow -->
<!-- PROSE_SORT_ORDER: 11 -->
<!-- PROSE_VERSION: 1449 -->

## Programme flow

The programme organises its work into three stages: **Base_data**, **Analysis** and **Publishing**. Each stage has its own live mechanism, governed by its own configuration. The database carries each stage's state, and work is taken up at the point the database shows it left off.

**Base_data** runs from the text of the Bible to the identification of the surfaces. It has three parts, each built on the one before.

*The text and its data.* Every verse of the Bible is taken from STEP Bible together with its Hebrew and Greek words, their Strong's identities, meanings and relations, and the verse's interlinear presentation is kept verbatim. The mechanical reading of each verse (`verse_lexical`) is derived once from it and records the verse's structural composition and nothing of what a word does for the inner being. This is built verse by verse, by book and range, before any collection exists, and it is complete before any collection is read.

*The surfaces.* The English words and phrases of the ESV, each linked through its Strong's codes to the original words behind it, are the population the study draws on. The whole population is sorted, by deduction and likeness, into four surface groups: behaviour, inner_being_state, entity and other. The sorting is roughly nine in ten correct, by the researcher's assessment, within an accepted margin; the items placed wrongly are found in the deeper analysis and compensated for there. Its purpose is to make the reading of the inner being's working possible.

*The collections.* The surfaces of the first two groups are collated, by the likeness or relatedness of the behaviour they name, into collections. Each surface belongs to one collection, and through the Strong's code of its base it is connected with its verses, so that a collection carries the verses its surfaces occur in (Chapter 4).

**Analysis** reads the inner being's working from the verses of the collections. The objective is to read those verses and deduce from them how the inner being works. A whole collection cannot be read in one go: to understand both the lexical context of the words in a verse and the inner-being working of the many behaviours a verse or group of verses carries is not achievable in one pass. The work is therefore split into units, and the units are read in layers and in stages.

*The unit.* To make a collection digestible, its surfaces are grouped further into surface subgroups. The subgroup is the unit of reading.

*The layers.* Each layer deposits its findings as observations, so that they are available to the next layer, and each collection is digested into observations of lexical meaning first and of the inner-being working afterwards. The subgroup is used first to complete the verse-lexical observations for its surfaces and their verses, then to complete the lexical observations for how its surfaces relate to one another and to the other words in those verses. The same subgroups, with the lexical observations they now have, are then used to formulate the inner-being observations: for specific behaviours, for groups of behaviours, and across subgroups and collections. Each cycle is a layer; each builds on the one before and uses its results. The lexical layers and the inner-being layer are separate processes and never run together, a step closes before the next opens, and every aspect a step demands is answered by an observation with its nodes, or by a recorded none with its reason.

*The claims.* Claims are formulated from the inner-being observations. The formulation of claims is not yet decided.

The configuration numbers this work as stages 1 to 5 (the lexical analysis of the words, the grouping of the surfaces, the verse-lexical observations, the inner-being analysis, the claims). That numbering was set before the order above was stated, and it is read against it. How the two are aligned, in particular where the grouping into subgroups falls in relation to the lexical analysis of the words, is open. The grouping method used for the first collection did not serve its purpose and is withdrawn: the subgroups are formed again when collection processing starts, and the inner-being layer is still being defined.

**Publishing** is the production of the essays and output that carry the results: the narrative, held in the database as chapters and sections, and exported for its readers.

**What is not yet defined.** The programme states what it does not yet know, so that it is not mistaken for settled.
- The order in which the collections are taken, and the size of one sitting of the reading, are not set.
- The inner-being layer: what it reads, how it is done and what it leaves are to be defined from the observations of the lexical layers, together with how the working of the inner being is depicted and checked.
- The formulation of claims from the inner-being observations. The claims that exist come from an earlier method and are not yet tied to the collections.
- How the chapters of the narrative follow the collections beyond the chapter on the inner being at work, which is built by collection.
- The surfaces that were grouped wrongly, not yet judged, set aside or not placed are found in the deeper analysis and compensated for there; the step that records them is not yet defined.
- The alignment of the configuration's stage numbering with the thread above, and the method by which the subgroups are formed.

The programme's methods have changed materially over its life, as its record shows, and this section describes what operates now.

---

<!-- PROSE_SECTION_ID: 11 -->
<!-- PROSE_SECTION_TYPE: prog_meth_science -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Research methodology -->
<!-- PROSE_CHAPTER_NO: 2 -->
<!-- PROSE_SECTION_TITLE: Science in action -->
<!-- PROSE_SORT_ORDER: 12 -->
<!-- PROSE_VERSION: 1394 -->

## Science in action

The relationship between Scripture and contemporary science is described conceptually in the section on science and the Bible. This section describes how the scientific lens is engaged in the work.

The governing premise is the second-lens position. The scientific literature relevant to the inner being (psychology, neuroscience, physiology, behavioural science, developmental and cognitive psychology, and evolutionary biology) is vast, and treating it as a co-equal programme would demand a second corpus-level effort matching the biblical one. The programme does not attempt this. It requires representative and reliable coverage of the landmark findings in each relevant field, held alongside the biblical analysis as the second lens through which the same territory is read.

**When science enters the work.** The science reading is part of the claims reading. It is engaged after the biblical reading of a collection is complete, when claims are formulated, and never in parallel with it. Running the two together risks the scientific frame distorting the biblical reading before that reading is complete, particularly for words where the scientific literature is substantial, such as shame, fear and grief. A science chapter of the narrative is planned and deferred until the claims reading reaches it.

**The scientific fields.** The programme works with six fields. *Neuroscience* addresses the body-soul boundary and the somatic dimension. *Clinical and social psychology* addresses soul operations: emotion, attachment, moral psychology, shame and guilt, will, motivation and virtue. *Physiology and epigenetics* addresses the body and the transmission of patterns across generations. *Behavioural science* addresses the relational dimension, how inner states express in behaviour and social context. *Developmental and cognitive psychology* addresses the formation of character: cognitive development, moral development, conscience and self-regulation. *Genetics and evolutionary biology* addresses the created endowment: what is built into the human creature by nature.

**Convergence and divergence.** The scientific reading is organised by a framework of three kinds of convergence and three of divergence. Convergence can be phenomenological (the same experience described from different angles), mechanistic (science describing the mechanism of what Scripture describes as a reality) or structural (the same architecture of the inner life in both accounts). Divergence can be register divergence (the accounts address different levels of one reality and only appear to conflict), reductive divergence (a scientific account that loses dimensions the biblical account treats as primary) or genuine divergence (claims in actual tension that cannot be harmonised by reframing). Genuine divergence is named, not papered over.

**The no-database decision.** The programme does not build a structured scientific database to match its biblical one. A parallel database at that depth would be a second programme; the data types are not structurally equivalent, since biblical data is lexical and classifiable while scientific findings are arguments and interpretations that require judgement to apply; and the second-lens role does not need it. Scientific material is held as reference files and used in the claims reading, and everything drawn from it is labelled by its source.

---

<!-- PROSE_SECTION_ID: 12 -->
<!-- PROSE_SECTION_TYPE: prog_meth_publishing -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Research methodology -->
<!-- PROSE_CHAPTER_NO: 2 -->
<!-- PROSE_SECTION_TITLE: Publishing -->
<!-- PROSE_SORT_ORDER: 13 -->
<!-- PROSE_VERSION: 1395 -->

## Publishing

Publishing is the output side of the programme: the production of the documents that carry its findings to its audience. The output is the narrative of the inner being.

The narrative is held in the database. It is made of chapters, and each chapter of sections whose text is a block; the chapter files are exports from the database. The table of chapters decides which chapters exist, their order and their purpose. The planned shape is an introduction; chapters on the question, on life and death, on the one inner person, and on the heart, the soul, the spirit, the flesh and the conscience; a chapter on where the words part; a chapter on the inner being at work, built by collection; further chapters on other sides, on what goes wrong, on other beings, on being made new, and on what lies beyond the named words; and a deferred slot for science.

Each claim is told in the narrative by a block, in full, in part or by pointer, and each claim keeps its sources and its verdict against the wording of the original essay from which the narrative began. The narrative follows the collections: each collection becomes a chapter of the narration.

Publishing here means the production of readable documents. It does not mean commercial publication, external release or any particular distribution channel; the narrative is copied to the inbox of the researcher's publishing site, and publication decisions of the external kind are outside the programme's method.

The database is the research. The narrative is the form in which the research reaches the reader, a curated presentation of the claims; where a reader's question is more specific than the narrative's treatment, the database supports the deeper look.

---

<!-- PROSE_SECTION_ID: 13 -->
<!-- PROSE_SECTION_TYPE: prog_meth_principles -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Research methodology -->
<!-- PROSE_CHAPTER_NO: 2 -->
<!-- PROSE_SECTION_TITLE: Key methodological principles -->
<!-- PROSE_SORT_ORDER: 14 -->
<!-- PROSE_VERSION: 1461 -->

## Key methodological principles

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

Beneath these lies a difficulty the programme has not resolved: to know what to look for, what is and is not a characteristic of the inner being, while discovering how such characteristics work, from the same verses. A list of characteristics, a registry of words and the Strong's codes that STEP returns each approached it, and the recognition that a characteristic is driven by its context was the turning point. The layers now keep apart the lexical meaning, the occurrences in the verses, the word in its verse and the collation of surfaces, so that each can be read on its own. How the working of the inner being is to be depicted systematically, and checked, is still being discovered. The test the researcher applies is whether the outcome is sensible, reasonable and defensible.

The principles are not independent. Defining scope against a definition makes a complete base meaningful. A complete base makes a uniform reading possible. A separate lexical reading makes the inner-being analysis answerable to evidence. The database as memory supports re-reading on the same footing as the first reading, and re-reading on a stable footing makes the bottom-up account possible. Because the data read at a re-run is the same data the prior run read, the method is reproducible.

---

<!-- PROSE_SECTION_ID: 14 -->
<!-- PROSE_SECTION_TYPE: prog_meth_constraints -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_CHAPTER: Research methodology -->
<!-- PROSE_CHAPTER_NO: 2 -->
<!-- PROSE_SECTION_TITLE: Key constraints -->
<!-- PROSE_SORT_ORDER: 15 -->
<!-- PROSE_VERSION: 1397 -->

## Key constraints

The principles described in the preceding section shape how the programme works. The constraints described here shape what it does not attempt.

**Scope is bounded by the collections.** The programme studies the surfaces of the groups behaviour and inner_being_state and their verses, and does not study other vocabulary except as the words that stand with them. The collections are open to evidence surfacing from within the corpus, by the procedure for changing a collection; they are not open to interpretive expansion from outside it.

**The scientific lens is bounded by the second-lens decision.** The programme does not engage the scientific literature at the depth of its biblical engagement. Its engagement is set by the claims reading and the reference material described in the section on science in action, for practical reasons (the scale of a parallel effort), methodological reasons (the data types are not equivalent) and structural reasons (the programme is biblical research, with science as the second lens).

**No structured scientific database.** The database holds the biblical research. Scientific material is held as reference files.

**Synthesis does not run ahead of its evidence.** A claim is formulated when the observations it rests on are complete. A chapter is assembled when its claims are formulated. The programme-wide account is assembled when the chapters are.

**The programme is corpus-level, not survey-level.** Each collection receives a full reading: every word read in its verses, every surface placed, every aspect each step demands answered.

**No bulk analysis.** No bulk or one-shot analysis, by Claude or by a model, is used to produce the study result. Item-by-item roles written in one pass, templated observation text and groups assigned by pattern are not a substitute for reading and articulating each discovery.

**No publication before closure of the reading.** A chapter is not produced from a collection whose reading is not closed; a chapter produced ahead of that would carry a retraction risk.

**Scope is not reopened on interpretive grounds.** A surface admitted to a collection is not re-examined for admission because an interpretive frame would exclude it, or because the reading has produced findings that conflict with a current view. Where findings raise a definition-level question, what the inner being is and where its edges lie, that question is handled at the level of the definition, and any change to a collection goes through its procedure.

---
