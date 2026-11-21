# "Role" in the programme prose, and the current definition

> Extracted 2026-11-21 for the researcher to read. Part 1 is the glossary entry as it stands in `bible_research.db` (section 1066, contentious glossary). Part 2 is every paragraph of the programme prose extract (`Workflow/Programme/programme_prose/wa-programme-prose-extract-20261120.md`) that uses the word role or roles, under its section path. Nothing is changed.

## 1. The current definition (glossary_contentious, section 1066)

status `draft` · version `1306` · updated `2026-11-13T14:22:50Z`

[DEFINITION] The role of a word in an observation: what the word is for that finding, judged from its verse and never from a cluster tag. On a node the roles are characteristic and qualifier (relevant to the inner being), object, relational_target and enactment (they bear on the finding), and standalone, which records that the word was recognised and has no inner-being role (cfg_setting reading.node_roles; behaviour rule 130).

[BACKGROUND] Held in ib_node.role. It is a different column from verse_span_index.role, an older linguistic classification with an overlapping vocabulary. This entry is in the contentious glossary: the researcher settles it.

## 2. Where the programme prose uses the word (14 paragraphs)

### Programme / Preamble / Programme Preamble

The corpus covers six areas. **Area 1** is the programme's purpose: the governing question, how the inner being is defined, where this study sits within the researcher's wider work, what a successful outcome looks like, the framework of enquiry that records each finding as an observation, and the relationship between Scripture and contemporary science as the two lenses through which the inner being is studied. **Area 2** is the research method: the five parts from the text and its data, through the vocabulary, the reading and the account, to publishing; the collection as the unit of study; the stages of the analysis, with the unit each reads, how volume and fallout are handled, where the programme stands and what is not yet defined; the role of science in the claims reading; the principles that govern every stage; and the constraints the programme deliberately accepts. **Area 3** is the disciplines, tools and evidential principles by which the programme operates: how findings are distinguished from hypotheses, how the researcher's authority and Claude's interpretation of the evidence divide, how continuity is kept across sessions, and how scope integrity is held. **Area 4** describes the data architecture: the two databases, the base data, the surfaces and collections, the node and the observation tables, the claims and the narrative, and the prose store. **Area 5** covers the governance that keeps the data correct over time: validation, the soft-delete discipline, consistency with sources, backup and schema discipline, failure protocols, the route by which a rule changes, and the alignment of documents with the configuration. **Area 6** describes the instruction corpus: where the rules live and how patches, directives, the operating guidance and the procedures of each part of the study are held.

### Programme / Research methodology / Programme flow

*What the inner-being layer reads.* Stage 4 reads how the inner being works from the observations of stage 3. The researcher's placement is settled: how the inner being is read belongs to this layer, and what the readings show together, how workings are grained and linked, how states and transitions behave and how a characteristic emerges, belongs to the claims, where the answers are discovered from the observations. The order of the study is to finish reading the inner-being surface groups into observations and then to formulate the claims. The researcher has stated what is read: behaviour is not only acts or operations but also states and conditions, for example sin, righteousness, life and death; it has qualifiers that define it; and a characteristic such as anger or love is not a thing and is not defined in advance, being known only by inference from the collection of behaviours, processes, actions and movements that give it substance. The programme's record of how the working has been defined, from the first working definition to the layers, shows the same few parts recurring under different names: the bearer and the seat, the behaviour in its three forms of act, state and movement, the qualifiers, the source and the object, the effect, the link to other workings, the expression or what is hidden behind it, and the context of the passage. The lexical layers hold a home for few of these, and the inner-being layer needs one for the bearer, the state of a being, the transition, the effect, the expression, the context and the link. This is the record's reading and it is inferential until the researcher confirms it. The study has also defined the interventions that a reading triggers: read beyond the verse, in its passage, genre and speaker; read outward from the verse and not inward from a question; check the original; reclassify a word whose role in this verse is not the one its collection gives it; do not force a meaning and never close on 'not X'; record a discovery outside the verse separately. They are defined and are not yet carried into the layered reading. The test applied to every result is whether it is sensible, reasonable and defensible.

### Programme / Research methodology / Science in action

**The no-database decision.** The programme does not build a structured scientific database to match its biblical one. A parallel database at that depth would be a second programme; the data types are not structurally equivalent, since biblical data is lexical and classifiable while scientific findings are arguments and interpretations that require judgement to apply; and the second-lens role does not need it. Scientific material is held as reference files and used in the claims reading, and everything drawn from it is labelled by its source.

### Programme / Research methodology / Key constraints

**No bulk analysis.** No bulk or one-shot analysis, by Claude or by a model, is used to produce the study result. Item-by-item roles written in one pass, templated observation text and groups assigned by pattern are not a substitute for reading and articulating each discovery.

### Programme / Research approach / Traceability and evidential warrant

A verse is in the programme's scope because it holds an occurrence of a member surface of a collection: lexical presence, not interpretive fit. A word is read in its verses, and a word that plays no role in any inner-being dynamic is not forced into one.

### Programme / Research approach / Tools and their roles

> The programme's instruments and their roles: STEP Bible, Claude Code, the IBA application, the two databases, the local model server and the working file formats.

The programme runs on a small set of tools, each with a defined role. Over time, as the programme wrestled with consistency and repeatability, the tool set moved from a range of scripts and instruction documents to an integrated application, the IBA App, which is a complete rebuild of the database and all its dependencies. The IBA App is described in the sections that follow.

### Programme / Data architecture / Terms

The verse-level lexical substrate is a further chain. `span` is the immutable source parse, one row for each tag of STEP's own interlinear presentation of a verse, kept verbatim so the parse can be re-derived; a combined-unit tag is kept as one row and is not split. `span_candidate` is the candidate stamp over a span. `verse_lexical` is the derived mechanical reading of the verse: one row for each Strong's code within a span, with the role of the word, the sense selected by stem and voice, and any ambiguity named and not resolved. It records the verse's structural composition and says nothing of what a word does for the inner being. It is derived once from the span and read from there; everything after it reads the derived row and does not derive again from `span` or `strong`.

### Programme / Data architecture / The node

> The node: how one observation is applied to a verse, a word and a surface, its roles, and the rules that keep nodes and observations consistent.

The programme anchors a finding to a specific piece of verse evidence by the **node**. A node applies one observation to one verse, one word and one surface: it carries the verse reference, the `verse_lexical` row of the occurrence (which fixes the surface, the Strong's code and the morph code), the collection and subgroup of the surface, the role the word has in the finding, and the stage that produced it. The node is how the study finds things: the observations of a collection are found through the collection on the node, and those of a subgroup through its subgroup.

The role of a node is the word's role in this finding, taken from this verse. Characteristic and qualifier are relevant roles; object, relational target and enactment bear on the finding; `standalone` records that the word was recognised and has no inner-being role on any other surface of the verse; `lexical` records that the word was read lexically and that its inner-being role has not been assessed. The nodes of stages 1 to 3 carry the role `lexical`, because those stages state nothing of the inner being.

### Programme / Data integrity & governance / Document validation and quality-flag architecture

For the reading, the **layer check** validates every answered row of a step against the tables (its stage, kind, nodes, roles, collection and every Strong's code of an enrichment) and reports what is open, what failed and what the data demands that has no row. The **grouping check** validates a grouping of surfaces and writes a scrutiny report for the researcher. A boundary check keeps the observations of the lexical stages free of what a word does for the inner being.

### Programme / Instruction corpus / The collection reading

| S1, the words | In the verses where each word of the collection stands, what does it mean in each, as the verse itself shows it? | The occurrences of the collection by surface and lettered Strong's code (`verse_lexical`), the sense tree, LSJ and Mounce entries of the code, the meaning prompts of the question catalogue, and the observations already recorded for those occurrences. | One ledger row for each word, except a word whose occurrences are all function words. The open rows are pulled into a working file with their evidence, Claude reads and fills each row, the record step checks the whole file and writes it in one transaction, and the check validates each answered row. | One observation for each sense the verses give the word, with the occurrences it holds for (every occurrence in some sense); an occurrence whose sense departs from the usual one is a face observation. Each has nodes of the role `lexical`. |

Every observation these steps leave states what the dictionary, the verses and the stored structure show, and carries no inner-being role. The inner-being layer has no step yet: what it reads, how it is done and what it leaves are still to be defined, and they are defined from the observations these steps leave.
