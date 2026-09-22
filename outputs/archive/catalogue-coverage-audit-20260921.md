# Catalogue coverage audit — every question, every row, validated against the live DB

> Escalation #1806 deliverable (researcher instruction, this chat, verbatim: 'prepare a md which shows every question in the catalogue and confirm how and and with what level of accuracy, is the question covered in the pipeline... it must be validated against the database and you must disclose every row'). 103 rows in `wa_obs_question_catalogue`, every one disclosed below and in the paired CSV -- none summarised from memory. Coverage mechanism re-read fresh from live code this session: `versereadinggenerate.py` (Stage 1), `charreadinggenerate.py`/`subgroupgenerate.py` (Stages 2-3), `charanswergenerate.py` (Stage 4).

## Summary by mechanism

| mechanism | count | meaning |
|---|---|---|
| DYNAMIC-STAGE1 | 14 | Stage 1, prefix-matched (M0.1%/M0.5%) -- auto-updates with the catalogue |
| PINNED-STAGE1 | 2 | Stage 1, exact hardcoded code (D7.7.1, M0.6.5) -- works today, not auto-updating |
| DYNAMIC-STAGE4 | 52 | Stage 4, scope-matched -- auto-updates with the catalogue |
| STRUCTURALLY-UNREACHABLE | 27 | No stage's query, by any mechanism, ever selects this -- a permanent gap as built |
| EXCLUDED-SCIENCE-EXTRACT | 4 | Deliberately filtered out pending science-extract wiring (escalation #1805) |
| RETIRED | 4 | deleted=1 in the live catalogue |
| INACTIVE-STATUS | 0 | status != 'active' |

## Summary by scope × mechanism

| scope | DYNAMIC-STAGE1 | DYNAMIC-STAGE4 | EXCLUDED-SCIENCE-EXTRACT | PINNED-STAGE1 | RETIRED | STRUCTURALLY-UNREACHABLE |
|---|---|---|---|---|---|---|
| Characteristic (HIB behaviour) | 0 | 19 | 4 | 1 | 0 | 0 |
| Characteristic relational | 0 | 17 | 0 | 0 | 0 | 0 |
| Other non-human beings | 0 | 12 | 0 | 0 | 0 | 0 |
| Science | 0 | 0 | 0 | 0 | 4 | 0 |
| The HIB | 0 | 4 | 0 | 0 | 0 | 0 |
| The verse | 0 | 0 | 0 | 1 | 0 | 4 |
| Verse-context | 0 | 0 | 0 | 0 | 0 | 10 |
| Word/term (lexical) | 14 | 0 | 0 | 0 | 0 | 13 |

**Reading this table:** a nonzero `live_observation_count` for a `STRUCTURALLY-UNREACHABLE` or `EXCLUDED-*` row would be a genuine surprise (it would mean something answered it despite no query selecting it) — checked below, flagged inline if found. A zero count for a `DYNAMIC`/`PINNED` row is expected and NOT a gap by itself if that scope's owning stage hasn't run yet for any cluster (Stage 4 has only ever run for M49/M67/M83).

**No surprises**: every `STRUCTURALLY-UNREACHABLE`/`EXCLUDED-SCIENCE-EXTRACT`/`RETIRED`/`INACTIVE-STATUS` row has exactly 0 live observations, confirming the code-level classification matches live data with no exception.

## Full disclosure — every row

All 103 rows. Full question text is in the CSV (`catalogue-coverage-audit-20260921.csv`, same folder) — truncated to 90 chars here for table width.

| question_code | scope | status | del | mechanism | stage | live_obs | text |
|---|---|---|---|---|---|---|---|
| D1.1.1 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 24 | In this verse, what does the characteristic reveal about the person's perception, belief, ... |
| D1.1.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Across the verses, does the characteristic consistently precede a judgement or belief, fol... |
| D10.1.1 | Verse-context | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | Does this verse state any purpose, role, or effect the characteristic serves in the person... |
| D10.1.2 | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 15 | Across the evidence, is there any orientation toward a future fullness — something the per... |
| D10.2.1 | Verse-context | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | What first or most immediate inner-being response does this verse show following the chara... |
| D10.2.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Across the verses, is that immediate response consistent or varied? |
| D10.3.1 | Verse-context | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | What does the characteristic produce in the inner being over time in this verse — what sta... |
| D10.3.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | How does the sustained effect differ from the immediate response (D10.2)? |
| D10.4.1 | Verse-context | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | In this verse, does the characteristic produce transformation in the person, and if so doe... |
| D10.4.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 15 | Is the transformation reversible or irreversible in the evidence? |
| D10.5.1 | Verse-context | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | Does this verse describe a sequence of inner states the characteristic moves the person th... |
| D10.6.1 | Verse-context | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | In this verse, by what mechanism does the characteristic produce change — discipline, enco... |
| D10.6.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Does the mechanism differ across contexts in the evidence; if so, how? |
| D11.1.1 | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Across the evidence, does the characteristic's role read as belonging to created design, t... |
| D11.2.1 | Characteristic (HIB behaviour) | active | 0 | EXCLUDED-SCIENCE-EXTRACT | none | 0 | Per the cluster's science extract, does genetics/evolutionary biology treat this character... |
| D12.1.1 | Characteristic (HIB behaviour) | active | 0 | EXCLUDED-SCIENCE-EXTRACT | none | 0 | Per the cluster's science extract, what does behavioural science show about how the charac... |
| D2.1.1 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 28 | In this verse, what is the felt quality of the characteristic -- is it shown as a settled ... |
| D2.1.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Across the verses, is the felt quality consistent, or does it vary by context? |
| D3.1.1 | Verse-context | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | In what distinct mode(s) does the characteristic operate within the inner person in this v... |
| D3.1.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Does the mode of operation vary by context, direction, or constitutional level; if so, how... |
| D3.1.3 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 16 | Does the characteristic operate through a communicative or speech-based mode (commanded, a... |
| D3.2.1 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Under what inner conditions does the characteristic take hold or operate rightly? |
| D3.2.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 15 | Under what inner conditions is the characteristic blocked, distorted, resisted, or not tak... |
| D3.2.3 | The HIB | active | 0 | DYNAMIC-STAGE4 | char-answers | 13 | What is the inner-being state of the person in whom the characteristic is present but does... |
| D4.1.1 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Does the evidence show the characteristic operating differently within existing relational... |
| D4.1.2 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Does the characteristic operate within covenantal contexts only, or does it cross covenant... |
| D4.1.3 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | What does the evidence show about the relational scope of the characteristic — who is incl... |
| D5.1.1 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | Across the characteristic's verses, is the characteristic ever predicated of God himself (... |
| D5.1.2 | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | What does the pattern of presence/absence found in D5.1.1 indicate for the characteristic'... |
| D5.2.1 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | In this verse, does the characteristic operate in the person's movement toward God — seeki... |
| D5.2.2 | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 13 | What inner posture does this movement require, as the evidence shows? |
| D5.2.3 | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 13 | What does the human-to-God direction of the characteristic show about the person's relatio... |
| D5.3.1 | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | From the characteristic's God-relation (D5.1/D7.6) and its role (D10.1/D11.1), what aspect... |
| D5.3.2 | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Across the evidence, is the characteristic shared between God and the person, or an exclus... |
| D5.3.3 | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Where the characteristic is present or absent in a person, what does that indicate about t... |
| D6.1.1 | Verse-context | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | At which constitutional level(s) does this verse locate the characteristic — from {spirit,... |
| D6.1.2 | The HIB | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Across the verses, what does the pattern of engaged and absent levels indicate — the chara... |
| D6.2.1 | The HIB | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Where a body link exists (from the D6.1.1 audit), in which direction does it run — soul/sp... |
| D6.3.1 | The HIB | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Does the characteristic move across constitutional levels (spirit→soul→body), or onto the ... |
| D7.1.1 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | In this verse, does the characteristic operate from God toward the human person, and if so... |
| D7.1.2 | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | On what basis does God extend the characteristic — conditional, unconditional, covenantal,... |
| D7.1.3 | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 13 | What does God's extension of the characteristic show about his disposition toward the huma... |
| D7.2.1 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | In this verse, is the characteristic extended by one person toward another, and if so how ... |
| D7.2.2 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 13 | What inner conditions or orientations in the giver accompany genuine extension of the char... |
| D7.2.3 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 12 | What does the evidence show a person must have received or become before they extend the c... |
| D7.3.1 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | In this verse, is the characteristic taken up by a person from another, and if so how does... |
| D7.3.2 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | What inner conditions accompany or block uptake of the characteristic from another person? |
| D7.3.3 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 13 | What is the inner-being state of the person who meets the characteristic from another but ... |
| D7.4.1 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | In this verse, does the characteristic operate in relation to other spiritual beings — ang... |
| D7.4.2a | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | Does an adversarial-being code ever appear as an acting party in a verse carrying this cha... |
| D7.4.2b | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 13 | What does that pattern show about the characteristic being a site of adversarial activity? |
| D7.4.3a | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | Does an angelic-being code ever appear as an acting party in a verse carrying this charact... |
| D7.4.3b | Other non-human beings | active | 0 | DYNAMIC-STAGE4 | char-answers | 13 | What does that pattern show about the characteristic being communicated, strengthened, or ... |
| D7.5.1 | Verse-context | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | Where does this verse say the characteristic originates — generated within the person, rec... |
| D7.5.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Across the verses, is the origin single or multiple, and does it change with context? |
| D7.6.1 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | In this verse, is the characteristic predicated of God or otherwise related to God; if so,... |
| D7.7.1 | Characteristic (HIB behaviour) | active | 0 | PINNED-STAGE1 | verse-reading | 598 | Where this verse contains an action or movement word tagged as an Operation in the cluster... |
| D9.1.1 | Characteristic (HIB behaviour) | active | 0 | EXCLUDED-SCIENCE-EXTRACT | none | 0 | Per the cluster's science extract, what does neuroscience or physiology show about the mec... |
| D9.2.1 | Characteristic (HIB behaviour) | active | 0 | EXCLUDED-SCIENCE-EXTRACT | none | 0 | Per the cluster's science extract, does the scientific literature show the characteristic ... |
| F0.1.1 | Verse-context | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | In this verse, does the characteristic engage or is affected by specific faculties — the i... |
| F0.1.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Across the verses, what does the pattern of engagement and non-engagement with the faculti... |
| M0.1.1 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 846 | What is the characteristic called in the programme, and what does the name signal about it... |
| M0.1.2 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 240 | What do the primary Hebrew and Greek terms show at the definitional level? |
| M0.1.3 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 239 | What directional, relational, or constitutional implication does the name carry? |
| M0.2.1 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 15 | What kind of inner-being phenomenon is the characteristic — an act, a disposition, a condi... |
| M0.2.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Is the characteristic simple in structure, or does it combine constituent elements; if com... |
| M0.3.1 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | What stands against the characteristic as its structural opposite — the inner-being realit... |
| M0.3.2 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | What does the characteristic exclude or resist at its edge? |
| M0.3.3 | Characteristic (HIB behaviour) | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Where does the characteristic end and another thing begin — what is it not? |
| M0.4.1 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | What is the grammatical/stem form of the characteristic's primary term in this verse? |
| M0.5.1 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 803 | What are the primary Hebrew and Greek terms for this characteristic, and what do their roo... |
| M0.5.10 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 216 | What does the full vocabulary arc show about the characteristic's complete semantic range? |
| M0.5.11 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 681 | Where this occurrence's surface form/contextual sense diverges from the base lemma's gener... |
| M0.5.2 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 246 | What is the grammatical range of the primary term (noun, verb, adjective, participle), and... |
| M0.5.3 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 230 | What is the semantic range of the primary term — across what breadth of meaning does it op... |
| M0.5.4 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 214 | Does the vocabulary include terms distinguishing distinct aspects — disposition versus act... |
| M0.5.5 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 220 | Does the vocabulary include a term for the structural opposite or absence of this characte... |
| M0.5.6 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 219 | Does the vocabulary include a person-type term — one for the person who habitually possess... |
| M0.5.7 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 215 | Does the vocabulary include a supplication or seeking term — one for the act of seeking th... |
| M0.5.8 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 213 | What does the relationship between the OT Hebrew and NT Greek vocabulary show about contin... |
| M0.5.9 | Word/term (lexical) | active | 0 | DYNAMIC-STAGE1 | verse-reading | 212 | Is there a term newly coined in the NT period for this characteristic; if so, what does th... |
| M0.6.1 | The verse | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | What is the function of the primary term within its primary verse -- (a) what role does it... |
| M0.6.2 | The verse | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | What is the logical structure of the key arguments in the verse evidence — premises and co... |
| M0.6.3 | The verse | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | Does any verse function as the primary anchor — the one most fully and directly expressing... |
| M0.6.4 | The verse | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | What does the primary anchor verse show that no other verse shows? |
| M0.6.5 | The verse | active | 0 | PINNED-STAGE1 | verse-reading | 769 | What role does this characteristic play in relation to the OTHER M-code characteristics pr... |
| T7.3.1 | Science | active | 1 | RETIRED | none | 0 | Which human-science framework (psychology, moral philosophy, developmental psychology, soc... |
| T7.3.2 | Science | active | 1 | RETIRED | none | 0 | Where the framework illuminates the verse evidence — making a finding more coherent or com... |
| T7.3.3 | Science | active | 1 | RETIRED | none | 0 | Where the verse evidence and the framework diverge, what does the divergence show? |
| T7.3.4 | Science | active | 1 | RETIRED | none | 0 | Does the framework surface any aspect of the characteristic the verse evidence has not yet... |
| X0.1.1 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Which adjacent characteristics appear alongside this one in the verse evidence, and how fr... |
| X0.1.2 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | What does the co-occurrence pattern show about this characteristic's place in the inner-be... |
| X0.2.1 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Does the evidence show this characteristic consistently preceding, following, or accompany... |
| X0.2.2 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | What does the sequence show — is the relationship causal, developmental, or correlational? |
| X0.3.1 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Does this characteristic produce another in the evidence, and if so which, and by what mec... |
| X0.3.2 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Is this characteristic produced by another, and if so which? |
| X0.3.3 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Is this characteristic a constituent element of another, or another a constituent of this ... |
| X0.4.1 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | Which vocabulary terms, if any, does this characteristic share with other characteristics ... |
| X0.4.2 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | Does the sharing extend to root-level architecture — a shared root generating terms across... |
| X0.4.3 | Word/term (lexical) | active | 0 | STRUCTURALLY-UNREACHABLE | none | 0 | What does the vocabulary sharing show about the conceptual relationship between the charac... |
| X0.5.1 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Which adjacent characteristic most closely resembles this one, and what precisely distingu... |
| X0.5.2 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Where the evidence shows apparent overlap, what is the precise boundary? |
| X0.5.3 | Characteristic relational | active | 0 | DYNAMIC-STAGE4 | char-answers | 14 | Is the distinction from the nearest neighbour one of degree, kind, direction, or constitut... |
