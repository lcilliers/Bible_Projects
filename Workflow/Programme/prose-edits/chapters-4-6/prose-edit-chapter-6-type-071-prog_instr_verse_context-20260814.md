# Prose Edit — Programme — Chapter 6

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 55 -->
<!-- PROSE_SECTION_TYPE: prog_instr_verse_context -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Verse Context -->
<!-- PROSE_SORT_ORDER: 118 -->
<!-- PROSE_VERSION: 3 -->
<!-- PROSE_SOURCE_FILE: outputs/investigations/vc-four-patch-design-v1-20260424.md -->

## Verse Context

Verse Context is the stage at which the programme turns the verse corpus into classified evidence. For every active Hebrew or Greek term the programme investigates — every OWNER term in the registry — a reader passes through all of the verses in which that term occurs in the ESV and asks a single question about each verse: does this verse, through the use of this term, say something about the inner being? The verses that answer yes are grouped by the inner-being characteristic they engage; one or two verses in each group are designated as anchors — verses that make the group's meaning evident without requiring surrounding context. The verses that answer no are set aside with a controlled reason (purely physical, purely spatial, purely narrative, or wrong-face — the verse carries inner-being content but through a different term). Classification is uniform across the programme; every OWNER term is treated identically regardless of its registry.

Verse Context is explicitly not the interpretive stage. It does not analyse the term in depth, does not draw conclusions about the word being studied, does not assign evidential weight, and does not place terms on dimensions or into cross-registry syntheses. All of that is downstream work, and downstream work reads from the classifications Verse Context produces — the groups, the group descriptions, the anchors, the set-asides. What Verse Context produces is the evidential substrate on which Session B, Session C, and Session D all rest.

Two disciplines make Verse Context trustworthy as evidence. The first is that the filter operates at term level, not at verse level: a verse about covenant renewal may use a given term in a purely legal sense with no inner-being engagement through that specific term — the verse's overall theme does not admit the term to the registry if the term itself does not carry inner-being content there. The second is that groups are formed from the perspective of the inner-being characteristic the verse cluster is primarily about, not from what the term does — so a property term that serves different characteristics across its corpus is grouped by the characteristic it serves in each cluster, not by the term's grammatical or syntactic behaviour. Both disciplines trace directly to the evidence-first principle: the programme's findings are the programme's findings only if the verses, read at term level, under characteristic-perspective grouping, support them.

A verse-reading classifier does more than classify. It notices things. Some are observations about the term being classified — a verse that reveals a previously-unidentified inner-being connection, a theological question worth examining at Session B, a cross-reference that would enrich the analytical stage. Others are signals about the shape of the programme's data — a verse whose use of a term points at a parallel or contrast in another term or another registry, a thematic link that will matter when Session D does its cross-registry synthesis. Under the programme's discipline, every such observation must be captured at the moment of reading, not deferred to the stage that will eventually consume it.

A Verse Context session therefore produces up to **four distinct output classes**, each written to the database at the same moment the classifier leaves the session. The first two record the classification itself: **new classifications** (first-time groups and verse_context rows for terms being seen for the first time) and **revisions** (updates to existing classifications — group descriptions refined, groups dissolved when their verses are reassigned, anchors promoted or demoted). The third captures **Session B observations** — analytical signals the classifier notices that deserve special attention when Session B eventually analyses this word. The fourth captures **cross-term or cross-registry pointers for Session D** — signals that a term's use here connects to another term or registry in a way worth examining at the synthesis stage. All four are written as rows in the database; together they are the complete record of what the session produced. The downstream stages that will read them — Session B, Session D — find their input already there, queryable, at the moment the session closes.

A registry's Verse Context work is complete when every one of its OWNER terms has been classified and every one of its XREF terms has an OWNER whose classification is complete. At that point the registry's evidential substrate is intact and the programme moves the word into Dimension Review and then into the interpretive stages. The completion signal is the database itself: the registry's `verse_context_status` reaches Complete as a consequence of every one of its OWNER and XREF-via-OWNER terms reaching the complete state. Without Verse Context complete, no interpretive claim about a word can be grounded; that is the reason Verse Context precedes everything downstream.

Because a registry may be reset — when a downstream change obsoletes prior classifications, when the filter and grouping model have evolved, or when new evidence requires a fresh reading — Verse Context runs are re-runnable. The stage's record is the current classification; every prior classification is subject to review when the work is re-opened. A re-evaluation carries a stricter discipline than a fresh run: every pre-existing classification is reviewed against the current method; every pre-existing group is accounted for at close (retained with verses, dissolved, or carried without verses with a documented reason); no prior record is left unexamined by implicit pass-through. The record is always what the current work supports, and what the current work supports is always traceable to the verses.

---
