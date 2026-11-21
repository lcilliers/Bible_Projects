# #2524 "Role": what the record says, set against the programme prose (v1)

> 2026-11-21. Read-only; nothing is changed. Basis: every escalation_history version (164 escalations use the word; every snippet with its text is in `outputs/escalation/2524-role-in-the-escalation-record-v1-20261121.md`), the escalation documents (outputs/escalation, iba/docs, Workflow/Instructions, Logs), the live config (`cfg_column`, `cfg_behaviour_rule`, `cfg_setting reading.node_roles`) and the programme prose extract of 2026-11-20 (14 paragraphs use the word; see `outputs/escalation/2524-role-in-the-programme-prose-v1-20261121.md`). Statements marked **(inferential)** are my reading, not a ruling. I do not know which point you mean as the major one: section 1 lists my candidates in the order I think they matter, and section 4 asks.

## 1. What the record says that the programme prose does not say, or says differently

**1. Role is the verse's judgement, per occurrence, never a property of the word.** Rule 73 and the role guide v2 (`Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md` §2, §4.2): each word in a verse has a role in *that occurrence*, decided against the verse's *main inner-being operation*: **characteristic** (it behaves as a characteristic of the inner being), **qualifier / process-element** (it binds to a characteristic and gives it value or context in place), or **standalone**. "The role comes from this verse, never from the cluster tag." The same lemma can be a characteristic in one verse and a qualifier in another (Psa 1:1, 1:5: *counsel* and *judgment* are qualifiers there; *delight*, *meditation*, *wicked*, *righteous* are characteristics). Programme prose: the node paragraph says "the role of a node is the word's role in this finding, taken from this verse", which is the nearest it comes. It never names the main inner-being operation as what the role is measured against, never says the role is per occurrence, and never says that one word can hold different roles in different verses. The prose has no hit for "role guide", "per occurrence" or "main inner-being operation".

**2. A qualifier gives value in place, gets no account of its own, and what it gives is named.** Guide §2 and §4.3 (method §13b); rule 120 ("a word that only qualifies … is not analysed or described by itself: it is bound to the characteristic it qualifies, or excluded"); #2406 v3 R3 (spec 4.2): the role of a qualifier includes "what it gives the characteristic (grade, nature, impact, size, relation or other; there is no fixed list)". Example: *cried* is the characteristic, *aloud* a qualifier giving volume (Psa 3:4). Programme prose: "qualifier" appears seven times and is nowhere explained. Programme flow says behaviour "has qualifiers that define it", the only statement; it does not say a qualifier is bound to its characteristic or what it gives.

**3. Role decides what enters the study and in which group.** #2406 v7, approved 2026-11-09: a surface never a behaviour is `inner_being_state` if it has an inner-being role in some verse and **leaves the study group if it has none in any verse**; the surface-level group is `behaviour` if the surface is a characteristic in any verse (R1 and R3); the role is per verse, characteristic or qualifier, with the qualifier's gift named. The difference between verses is carried by the observations per verse, not by the group. Programme prose: it says a collection is built of the surfaces of the groups behaviour and inner_being_state, but I found no statement that role is what places a surface in or out of them. The word "engagement" occurs six times; I read one, which is about science, and not the others **(inferential: the engagement step is not described)**.

**4. Role is the filter of the deeper reading.** Researcher, #2161 v6, 2026-10-24: "the deeper reading of the verses in the next phase must definitely be filtered on the role of the words" and "the study should not be contaminated with the terms that have little or no bearing on the inner being". #2259 v9 (2026-10-30): the role filter of the deeper reading "belongs to the claims phase, which is not yet defined (#2315)". Programme prose: Programme flow says stage 4 is undefined and lists interventions including "reclassify a word whose role in this verse is not the one its collection gives it". It does not say that the role filter decides which verses and words go on to the deeper reading, nor that this is not built.

**5. The word "role" names three different columns, and the prose's "Terms" paragraph conflates two.**
- `verse_lexical.role` (cfg_column): since 2026-09-16 it is the strong's cluster codes copied onto each occurrence. Researcher, #2339 v13, 2026-10-31: "I thought ai designated the role to distinguish between characteristic, qualifyer and other, the only think that happened was that it carries the M-code … pritty useless", and the earlier statement that it shows whether a surface is a characteristic is withdrawn.
- `verse_span_index.role` (bible_research.db): an older analytic role set by campaign (standalone 63,719; characteristic 13,514; process-qualifier 7,155; qualifier 3,168; a long ad-hoc tail), on 27% of spans, set 2026-07-07 to 07-14.
- `ib_node.role`: the judgement of the verse, the one the guide and rule 73 mean.

The prose "Terms" paragraph says `verse_lexical` holds "the role of the word", in the same passage as "says nothing of what a word does for the inner being". Read next to the node paragraph, a reader takes the first as the second. The glossary entry names the second and third and not the first. **(inferential)** This may be the point you mean.

**6. The vocabulary has drifted from three values to seven.** Guide and rule 73: characteristic, qualifier / process-element, standalone. Config `reading.node_roles` and `ib_node.role`: relevant = characteristic, qualifier; bears on = object, relational_target, enactment; recognised = standalone; lexical = lexical. Researcher, #1995, 2026-10-11: "you need to integrate the terminology with the existing terminology in the study, we are not defining new concepts." The added values come with the node design of #2273/#2274 (the `ib_node.role` column source). The glossary entry (section 1066) lists the first six and omits `lexical`; the programme node paragraph lists all seven. The guide still says it is in force and cites the glossary *role* entry for its three-value definition.

**7. Rule 73 is inactive in config.** `cfg_behaviour_rule` 73 (*read-verse-by-role-of-each-mcode-word*) has active = 0 and enforcement "context_delivered", while the role guide v2 states "in force on the researcher's instruction". Rule 120 (active) carries the qualifier statement. Nothing active carries the per-occurrence principle or "never from the cluster tag" except the node column note and rule 130 **(inferential; I did not check why 73 was set inactive, the history is in cfg_change_detail)**.

**8. Party role is an observation, not a field.** Researcher, #2273 v8, 2026-10-24: "I do not agree that parties is a new table. the party role in the verse is an observation. That means that there will be one observation for instance 'evil spirit acting towards the IB' and many verses and many characteristics affected (terms)". The design's party table and enum were dropped. Programme prose: the node paragraph lists `relational target` and `enactment` as roles; it does not say a party's role is written as an observation.

**9. Most nodes have no role yet.** #2484 v21 hand-over, 2026-11-13: nodes with no role 14,001; observations with no relevant-role node 7,332. #2498: roles set on the 29 live fear findings (132) and 12 roles corrected on document 92. Programme prose states the role rules as if they hold; it does not say role is unset on most nodes.

**10. A role label is never a verdict.** Guide §4.9 (#2168): "A verse or an item is never closed as 'not a fear face', 'only a qualifier' or 'no bearing'." Programme flow has "never close on 'not X'", without the role label.

## 2. Where the work on role was done

| Where | What it holds |
|---|---|
| `Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md` | the guide: terms, reading sequence, qualifier handling, worked cases (2Pe 2:13, 2Cor 7:11, Lam 4:6, Psa 1) |
| `Workflow/Instructions/archive/wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md` (40 uses) | the July 2026 cycle that first defined role |
| #1590, #1592, #1594, #1607, #1704, #1706, #1719, #1810 and their documents in iba/docs | the lexical-layer role: the Greek article tag bug, the six-point column map, the role-driven reading sequence, role data presentation, role staleness, the rebuild |
| #1995, #2168, rule 73 | the role guide and its three amendments (outward reading, the original, never "not X") |
| #2161, #2259 (design v2) | the role filter of the deeper reading, the rules map, what is not joined up |
| #2268 and `outputs/escalation/2268-role-guide-v2-plotted-into-config-v3-20261024.md` | every statement of the guide plotted against config |
| #2273, #2274, #2318 (specification v5), #2323 | node roles, party role as observation, relevance tests, the tag as type of observation |
| #2339 | verse_lexical.role found to carry only cluster codes |
| #2406 (design v3) | surface-level group from role; R1 to R4; relevant / bears_on / not_relevant |
| #2427, #2484, #2498 | God's anger in collection anger, roles set on live findings, the no-role classes |
| #2509 v4 | the researcher: "you did not respect the boundaries between lexical work and inner being work" (nodes of stages 1 to 3 carry the role `lexical`) |

## 3. What I am not claiming

- That each point is an error in the prose: it may say a point in words I did not search for. I searched for the word role and a few related terms.
- That the missing major point is one of these. I have your signal and the record to go on.
- That the glossary entry, the guide and the config agree. They do not (points 5, 6 and 7).

## 4. For you

Which of points 1 to 10 is the one I missed? If none, say what it is and I will search the record for it.
