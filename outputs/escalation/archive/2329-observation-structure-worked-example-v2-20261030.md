# 2329: the observation structure as I understand it, worked on one verse (2026-10-30, v2)

Standard session 698fb0d0. Researcher, chat 2026-10-30 (verbatim), first: 'the re-evaluation show exactly how far the observations are off. I my humble opinion: for each verse a) get every surface with role characteristic b) for every surface with role characteristic isolate the 9 items related the specific characteristic (this may include other characteristics in the same verse, and qualifiers. qualifyers may be shared accross characteristics in the verse.) c) each applicable item of the 9 items to explore is a separate observation. in some cases the same observation will be shared across the surfaces. this is dealth with in the nodes. d) observations are not regurgitating the entire verse text e) I am not expecting to see the same text for all 9 items, that means you have not understood it.'

Then: 'regarding the before - after: both of those observations will be added by the claims process that will be reading passages for exactly that reason. However, if you are not looking at the operation from a perspective to ask what is the state / happens before the operation, and what happens after it, then the operation item is incomplete. the operation is action description - it looks like that is what your type party is aiming at, but not sure that it is what happens.'

This file shows my understanding on one verse before anything is changed, so the researcher can say where it is wrong. Nothing in the database or the code was touched. It replaces v1.

## 1. My understanding, and how it differs from what is built

- **The nine items** are those of the approved spec 4.2 (`outputs/escalation/2318-analysis-phase-1-specification-v5-20261030.md`): (1) the surface and its meaning here with the evidence, (2) its role, (3) polarity, (4) content or object, (5) enactment, (6) the other party and the sequence, (7) the circumstance, (8) the chain and the primary operation, (9) typed flags.
- **One observation per applicable item, per characteristic.** An item the verse does not show gets no observation. An observation true of several characteristics (a circumstance, a chain, a qualifier) is written once and applied to each by its nodes.
- **The operation is an action description.** Item 8 records the primary operation as a statement-kind observation (D-b): who does what to what, in a short sentence, not the verse again. I left it out of v1.
- **The operation is looked at from before and after, as the verse itself states them.** What the verse states before the operation (a prompt, state or purpose) and after it (the outward act or the result) is recorded under the sequence, the chain, the enactment and the operation. Where the verse states none, a discovery flag (item 9) says so and says that the passage has to be read. The passage-level before and after are added by the claims process, which reads passages for that reason.
- **What was wrong in #2329's `before` and `after`.** They were parts of items 4 and 5, filled from the neighbouring verses of the sheet's window. That is the claims process's reading, written in Phase 1 and repeated on every observation of the verse.
- **The typed party** (`acts`, `acted_on`, from `party_kind`) classifies who acts and who is acted on. It does not describe what happens, and it was not asked for. The action description is the operation statement; the party observation (item 6) names the other party and the order. I would leave the typed kinds out.
- **What is built does the reverse of the structure.** Per verse one observation holds all the items as parts, then a link and a party observation repeat the same text; 118 of the 136 verse-level rows on the 39 verses repeat another observation's text, and the observation texts restate the verse (for example #20641: 'Joseph asks Pharaoh's officers in custody why their faces are downcast today').

## 2. Judg 13:6 worked

Verse: 'Then the woman came and told her husband, "A man of God came to me, and his appearance was like the appearance of the angel of God, very awesome. I did not ask him where he was from, and he did not tell me his name,"' (the verse is not copied into any observation below).

Surfaces with role characteristic: awesome (H3372H), ask (H7592, negated), tell (H5046, negated). Qualifiers: very (H3966) on awesome; not (H3808) on ask and on tell. Meaning rows from `strong_meaning_tree`.

| # | Item | Characteristic | Observation (kind) | Nodes |
|---|---|---|---|---|
| A1 | 1 meaning | awesome | Awesome here describes what was seen, with the sense of inspiring awe (tree H3372 1b2 'to cause astonishment and awe, be held in awe', 1b3 'to inspire reverence or godly fear or awe'); the root's other senses are fear and revere. (face) | awesome |
| A2 | 2 role | awesome | 'Very' raises the awe to a high degree (tree H3966 1 'exceedingly, much'). (qualification) | very (qualifier), awesome |
| A3 | 4 object | awesome | What carries the awe is his appearance, likened to the appearance of the angel of God. (statement) | awesome, appearance (object) |
| A4 | 8 operation | awesome | Her report ascribes awe to the man of God's appearance: something perceived and named, not an act towards him. (statement) | awesome, woman |
| A5 | 6 party | awesome | The woman speaks of the awe; the man of God is the one seen. (party) | awesome, woman, man of God |
| A6 | 9 flag | awesome | Discovery: whose awe it is, hers or general, and what it led to for her, is not stated; the passage is needed. (flag) | awesome |
| K1 | 1 meaning | ask | The verb is the one of enquiring (tree H7592 1a3 'to enquire, enquire of'). (face) | ask |
| K2 | 3 polarity | ask | 'Not' makes it a refusal: she records that she did not enquire. (statement, refusal) | not (qualifier), ask |
| K3 | 4 object | ask | What was not enquired is where he was from. (statement) | ask, man of God |
| K4 | 8 operation | ask | She did not enquire of him about his origin. (statement) | ask, woman, man of God |
| K5 | 6 party | ask | The woman did not ask; the man of God was not asked. (party) | ask, woman, man of God |
| T1 | 1 meaning | tell | The verb is to tell or report (tree H5046 1a1 'to tell, announce, report'). (face) | tell |
| T2 | 3 polarity | tell | 'Not' makes it a refusal on his side: he did not tell. (statement, refusal) | not (qualifier), tell |
| T3 | 4 object | tell | What was not told is his name. (statement) | tell, name (object) |
| T4 | 8 operation | tell | He did not tell her his name. (statement) | tell, man of God, woman |
| T5 | 6 party | tell | The man of God did not tell; the woman was not told. (party) | tell, man of God, woman |
| S1 | 7 circumstance | awesome, ask, tell | All three are said in her report to her husband. One observation, shared. (statement) | awesome, ask, tell |
| S2 | 8 chain | awesome, ask, tell | In her report, his coming, the awe of his appearance, the not-asking and the not-telling are stated in that order, with no cause between them. One observation, shared. (link) | awesome, ask, tell |
| S3 | 9 flag | ask, tell | Discovery: the verse states no state or purpose before the not-asking or the not-telling and no result after them; the passage is needed. One observation, shared. (flag) | ask, tell |

Items with no observation here: polarity of awesome (not an act of pursuit or refusal) and enactment (no outward act is stated for any of the three).

Nineteen observations for three characteristics, against five today. S1, S2 and S3 are the shared ones; A2 is a qualifier carried by its own nodes. The texts differ because the items differ.

## 3. What I do not know

- Whether nineteen observations for a verse with three characteristics is the density you intend. The count per verse, and the time and cost of it, are not measured; your estimate of about 60 days (#2320 v30) predates this structure.
- Whether the kinds I used (face, qualification, statement, party, link, flag) are right for each item, or each item has its own kind.
- Whether A4, K4 and T4 (the operation as a sentence) are what you mean by the action description, or the operation is more than who does what to what.
- Whether a discovery flag is the right way to tell the claims process where the passage must be read.

## 4. If this is right

I would redo one verse in this structure on a copy (Judg 13:6 first), show it with the nodes, and only then the rest of the 39, with `before`, `after` and the typed party removed and the 132 existing observations checked and accepted, modified or soft deleted (RS-04). No other verse of m21-asking runs.
