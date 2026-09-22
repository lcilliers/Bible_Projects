# Catalogue question wording review — every question, current vs. revised

> Escalation #1814 deliverable (spawned from #1806). Researcher instruction, this chat, verbatim: 'prepare a list of current / revised wording of each question. If you are not making a change to the wording then clearly state that the you have read the text of the question and it is fully compliant.' Every one of the 103 catalogue rows is judged individually below — none skipped, none assumed compliant without reading.

## The convention this review applies (derived, per your own instruction anticipating this question — stated explicitly for your confirmation or correction, not assumed settled)

Every question's text, standing alone — without relying on a sibling question, the DB `scope` column, or anything outside the wording itself (**Stage 1/`verse-reading`, the highest-volume stage, shows the LLM only `question_code` + `question_text` — confirmed live, no `scope` field at all** — so the wording genuinely is the only carrier of this information for that stage) — must:

1. **Name its evaluation subject explicitly** — the verse being read; the word/strong itself; the characteristic; the subgroup; a comparison across verses; across subgroups; across clusters; across characteristics; across non-human-being phenomena; or (the 4 science-extract questions) the cluster's science extract.
2. **State its answer grain explicitly**, via one of a small, consistent set of openers:
   - `In this verse, ...` — the single verse currently being read
   - `Across the verses, ...` / `Across the evidence, ...` / `Across the characteristic's verses, ...` — aggregate across the characteristic's whole verse set
   - a distinct **definitional category** (mostly `M0.1.x`/`M0.5.x`) genuinely about the programme's own naming/vocabulary, not verse evidence — legitimately exempt from a verse/aggregate marker, but should be recognisable as this category, not merely silent
3. **Cite a sibling question by its exact code** when depending on its finding (`per D5.1.1`, `(D10.2.1)`) — never a bare pronoun (`that`, `this`, `the mechanism`) standing in for an unnamed prior result. Several existing questions already do this correctly (`D5.3.1`, `D6.2.1`, `M0.6.4`) — that's the model to follow.
4. **Plain language only** — no raw DB/schema identifiers (column names, internal tag codes like `role-T3`, `stepGloss`) inside the question text.
5. **No pipeline-process instructions embedded in the question** (e.g. "build on prior passes, don't duplicate") — that belongs in the stage's own prompt-assembly code, never the catalogue text.
6. **One clear ask per question**, or the established `Does X exist? Record it, or none` existence-check shape — not a compound bundling several distinct sub-questions, and not one sentence enumerating a large taxonomy inline.

**This is a proposed convention, not an assumed-approved one** — every verdict below follows from it, so if you'd correct or extend it, the per-row verdicts would need re-running against the revision, not just the wording.

## Summary

| verdict | count |
|---|---|
| COMPLIANT | 51 |
| REVISE | 48 |
| RETIRED | 4 |

### Issue types among REVISE rows

| issue_type | count |
|---|---|
| grain-missing | 21 |
| grain-vague(evidence) | 17 |
| subject-missing | 11 |
| grain-vague | 4 |
| jargon | 4 |
| compound | 3 |
| subject-partial | 1 |
| run-on | 1 |
| jargon-density | 1 |
| mixed-grain | 1 |
| process-instruction-mixed | 1 |
| subject-vague | 1 |

Full CSV (all 103 rows, current + revised text, no truncation): `catalogue-question-wording-review-20260921-v2.csv` (same folder).

## Full list — every question

### D1.1.1 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** cognitive
- **current:** In this verse, what does the characteristic reveal about the person's perception, belief, or judgement -- what do they perceive, believe true, or conclude? Record it, or record none.
- **rationale:** Subject (the characteristic) and grain (in this verse) both explicit.

### D1.1.2 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** cognitive
- **current:** Across the verses, does the characteristic consistently precede a judgement or belief, follow one, or both?
- **rationale:** Subject + grain (across the verses) explicit.

### D10.1.1 — COMPLIANT

- **scope:** Verse-context | **window:** action-impact
- **current:** Does this verse state any purpose, role, or effect the characteristic serves in the person — what it leads the person to be, do, or become? Record it if stated; otherwise record none.
- **rationale:** Subject + grain (this verse) explicit.

### D10.1.2 — REVISE

- **scope:** Other non-human beings | **window:** action-impact
- **current:** Across the evidence, is there any orientation toward a future fullness — something the person moves toward, not only what they currently are? Record it, or record none.
- **revised:** Across the characteristic's verses, does it show any orientation toward a future fullness the person moves toward, not only what they currently are? Record it, or record none.
- **rationale:** Original never names 'the characteristic', and 'across the evidence' doesn't say from which verses. OPEN QUESTION (not resolved here): should this be FILTERED to only verses where D10.1.1 found a stated purpose/effect, or is it a genuinely independent aggregate claim? Not confident enough in the content relationship to assert a filter -- used the safer unfiltered aggregate.

### D10.2.1 — COMPLIANT

- **scope:** Verse-context | **window:** action-impact
- **current:** What first or most immediate inner-being response does this verse show following the characteristic? Record it, or record none.
- **rationale:** Subject + grain (this verse) explicit.

### D10.2.2 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** action-impact
- **current:** Across the verses, is that immediate response consistent or varied?
- **revised:** Across the verses where an immediate inner-being response was found (per D10.2.1), is it consistent or does it vary by context?
- **rationale:** 'that immediate response' unrestated; D10.2.1 has an explicit 'record none' gate, and this question only makes sense for the verses where a response WAS found -- filtered, not blanket 'across the evidence'.

### D10.3.1 — COMPLIANT

- **scope:** Verse-context | **window:** action-impact
- **current:** What does the characteristic produce in the inner being over time in this verse — what states, qualities, capacities, or orientations does it establish? Record it, or record none.
- **rationale:** Subject + grain (this verse) explicit.

### D10.3.2 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** action-impact
- **current:** How does the sustained effect differ from the immediate response (D10.2)?
- **revised:** At the characteristic level, how does its sustained effect (D10.3.1) differ from its immediate response (D10.2.1)?
- **rationale:** Compares two ALREADY-aggregated findings (D10.3.1, D10.2.1) to each other, each drawn from a possibly-different verse subset -- this is characteristic-level synthesis, not a fresh verse scan, so 'across the verses' would itself be imprecise here.

### D10.4.1 — COMPLIANT

- **scope:** Verse-context | **window:** action-impact
- **current:** In this verse, does the characteristic produce transformation in the person, and if so does it change the person's condition, their orientation to their condition, or both? Record none if no transformation is shown.
- **rationale:** Subject + grain (this verse) explicit.

### D10.4.2 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** action-impact
- **current:** Is the transformation reversible or irreversible in the evidence?
- **revised:** Across the verses where transformation was found (per D10.4.1), is it reversible or irreversible?
- **rationale:** Researcher caught this one directly: original revision ('in the evidence') still didn't say WHAT evidence or from which verses. D10.4.1 gates on 'record none if no transformation is shown' -- this question only applies to the verses where transformation WAS found. Filtered, explicit, no floating 'evidence'.

### D10.5.1 — COMPLIANT

- **scope:** Verse-context | **window:** action-impact
- **current:** Does this verse describe a sequence of inner states the characteristic moves the person through — a before, during, and after — and what are those states? Record none if no sequence is shown.
- **rationale:** Subject + grain (this verse) explicit.

### D10.6.1 — COMPLIANT

- **scope:** Verse-context | **window:** action-impact
- **current:** In this verse, by what mechanism does the characteristic produce change — discipline, encounter, gradual formation, sudden transformation, or other? Record none if no mechanism is shown.
- **rationale:** Subject + grain (this verse) explicit.

### D10.6.2 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** action-impact
- **current:** Does the mechanism differ across contexts in the evidence; if so, how?
- **revised:** Across the verses where a mechanism of change was found (per D10.6.1), does it differ by context, and if so how?
- **rationale:** D10.6.1 gates on 'record none if no mechanism is shown' -- filtered to those verses, same pattern as D10.4.2.

### D11.1.1 — REVISE

- **scope:** Other non-human beings | **window:** origin
- **current:** Across the evidence, does the characteristic's role read as belonging to created design, to the fallen condition, to both, or as not determinable?
- **revised:** Across the characteristic's verses, does its role read as belonging to created design, to the fallen condition, to both, or as not determinable?
- **rationale:** CORRECTED from an earlier wrong COMPLIANT verdict -- I had accepted 'across the evidence' as an explicit grain marker; it isn't (evidence OF WHAT, from which verses?). No specific parent gate to filter by -- plain aggregate.

### D11.2.1 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** origin
- **current:** Per the cluster's science extract, does genetics/evolutionary biology treat this characteristic (or its precursor) as part of innate human endowment, and how does that relate to D11.1's created-design/fallen-condition finding?
- **rationale:** Science-extract question family (D9.1.1/D9.2.1/D11.2.1/D12.1.1) -- internally consistent shared convention ('Per the cluster's science extract...'), properly cross-cites D11.1 by code. Its own 'verse evidence' phrase is precise here (contrasting a NAMED separate source, the science extract, against verse evidence specifically) -- a legitimate use, unlike a bare floating 'the evidence' elsewhere. Flag: this family's grain doesn't map onto the verse/aggregate/subgroup/cluster taxonomy at all (it's cluster-level science literature) -- a structural question for #1805's build, not a wording defect here.

### D12.1.1 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** scientific
- **current:** Per the cluster's science extract, what does behavioural science show about how the characteristic expresses socially -- cooperatively or competitively -- and does the verse evidence show a comparable social pattern?
- **rationale:** Same science-extract family as D11.2.1 -- see that entry's note.

### D2.1.1 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** affective
- **current:** In this verse, what is the felt quality of the characteristic -- is it shown as a settled disposition or a transient response, and what emotion-language or bodily-feeling language, if any, accompanies it? Record it, or record none.
- **rationale:** Subject + grain (this verse) explicit.

### D2.1.2 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** affective
- **current:** Across the verses, is the felt quality consistent, or does it vary by context?
- **revised:** Across the verses where a felt quality was found (per D2.1.1), is it consistent, or does it vary by context?
- **rationale:** 'the felt quality' unrestated; D2.1.1 gates on 'record it, or record none' -- filtered to the verses where a felt quality was found.

### D3.1.1 — COMPLIANT

- **scope:** Verse-context | **window:** operational
- **current:** In what distinct mode(s) does the characteristic operate within the inner person in this verse — the manner of its functioning?
- **rationale:** Subject + grain (in this verse) explicit, though mid-sentence rather than leading -- acceptable.

### D3.1.2 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** operational
- **current:** Does the mode of operation vary by context, direction, or constitutional level; if so, how?
- **revised:** Across the characteristic's verses, does its mode of operation (per D3.1.1) vary by context, direction, or constitutional level; if so how?
- **rationale:** 'the mode of operation' unrestated; D3.1.1 has no 'record none' gate (always produces an answer) so no filtering is needed -- plain aggregate.

### D3.1.3 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** operational
- **current:** Does the characteristic operate through a communicative or speech-based mode (commanded, addressed, spoken); if so, how? Record it, or record none.
- **revised:** Across the characteristic's verses, does it ever operate through a communicative or speech-based mode (commanded, addressed, spoken); if so how? Record it, or record none.
- **rationale:** Subject is explicit but no verse/aggregate marker anywhere in the sentence.

### D3.2.1 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** operational
- **current:** Under what inner conditions does the characteristic take hold or operate rightly?
- **revised:** Across the characteristic's verses, under what inner conditions does it take hold or operate rightly?
- **rationale:** No grain marker at all; no specific single parent to filter by.

### D3.2.2 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** operational
- **current:** Under what inner conditions is the characteristic blocked, distorted, resisted, or not taken up — including, where the evidence shows it, distortion or interference by another spirit (adversarial or angelic)?
- **revised:** Across the characteristic's verses, under what inner conditions is it blocked, distorted, resisted, or not taken up -- including, where shown, distortion or interference by another spirit (adversarial or angelic)?
- **rationale:** 'where the evidence shows it' is a buried, vague secondary clause, not a leading grain statement; no single parent to filter by.

### D3.2.3 — REVISE

- **scope:** The HIB | **window:** operational
- **current:** What is the inner-being state of the person in whom the characteristic is present but does not take hold?
- **revised:** Across the verses where the characteristic is present but blocked, resisted, or not taken up (per D3.2.2), what is the inner-being state of the person?
- **rationale:** Directly reuses D3.2.2's own described case ('not taken up') as its subject -- filtered to those verses, cited by code rather than left as a bare implicit continuation.

### D4.1.1 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** Does the evidence show the characteristic operating differently within existing relational bonds versus across relational distance or difference; if so, how?
- **revised:** Across the characteristic's verses, does it operate differently within existing relational bonds versus across relational distance or difference; if so how?
- **rationale:** CORRECTED from an earlier wrong COMPLIANT verdict -- 'the evidence show' is not an explicit grain marker (doesn't say which verses).

### D4.1.2 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** Does the characteristic operate within covenantal contexts only, or does it cross covenantal boundaries, as the evidence shows?
- **revised:** Across the characteristic's verses, does it operate within covenantal contexts only, or does it cross covenantal boundaries?
- **rationale:** Same correction as D4.1.1 -- 'as the evidence shows' is vague.

### D4.1.3 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** What does the evidence show about the relational scope of the characteristic — who is included and who is not?
- **revised:** Across the characteristic's verses, what is its relational scope -- who is included and who is not?
- **rationale:** Same correction as D4.1.1/D4.1.2.

### D5.1.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** relational
- **current:** Across the characteristic's verses, is the characteristic ever predicated of God himself (not just present in a verse where God is also mentioned)?
- **rationale:** Subject + grain (across the characteristic's verses) explicit and clean. NOTE: scope tag is 'Word/term (lexical)' but this is a cross-verse characteristic-content question, not a lexical one -- a scope-label mismatch worth flagging to #1806, not a wording defect.

### D5.1.2 — REVISE

- **scope:** Other non-human beings | **window:** relational
- **current:** What does the pattern of presence/absence found in D5.1.1 indicate for the characteristic's place in the human person and in the divine image?
- **revised:** At the characteristic level, what does the pattern of presence/absence found in D5.1.1 indicate for the characteristic's place in the human person and in the divine image?
- **rationale:** D5.1.1 is already a characteristic-level (not per-verse) binary finding -- this synthesises that finding, not a fresh verse scan. Properly cites D5.1.1 by code (good practice). NOTE: scope tag 'Other non-human beings' does not match this question's actual content (human person / divine image) -- flag to #1806.

### D5.2.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** relational
- **current:** In this verse, does the characteristic operate in the person's movement toward God — seeking, supplication, worship, covenant — and if so how? Record none if it does not.
- **rationale:** Subject + grain (in this verse) explicit. NOTE: scope tag 'Word/term (lexical)' mismatches this verse-content/relational question -- same pattern as D5.1.1, flag to #1806.

### D5.2.2 — REVISE

- **scope:** Other non-human beings | **window:** relational
- **current:** What inner posture does this movement require, as the evidence shows?
- **revised:** Across the verses where God-ward movement was found (per D5.2.1), what inner posture does it require?
- **rationale:** 'this movement' unrestated; D5.2.1 gates on 'record none if it does not' -- filtered to the verses where it was found.

### D5.2.3 — REVISE

- **scope:** Other non-human beings | **window:** relational
- **current:** What does the human-to-God direction of the characteristic show about the person's relationship with God?
- **revised:** Across the verses where God-ward movement was found (per D5.2.1), what does that direction show about the person's relationship with God?
- **rationale:** Same filter as D5.2.2 -- same underlying finding.

### D5.3.1 — REVISE

- **scope:** Other non-human beings | **window:** relational
- **current:** From the characteristic's God-relation (D5.1/D7.6) and its role (D10.1/D11.1), what aspect of the divine likeness, if any, does it instantiate in the person? Record the aspect, or record none.
- **revised:** At the characteristic level, from its God-relation (D5.1/D7.6) and its role (D10.1/D11.1), what aspect of the divine likeness, if any, does it instantiate in the person? Record the aspect, or record none.
- **rationale:** Synthesises FOUR already-characteristic-level findings (D5.1, D7.6, D10.1, D11.1) -- characteristic-level synthesis, not a verse scan. Model citation practice otherwise (cites all four by code).

### D5.3.2 — REVISE

- **scope:** Other non-human beings | **window:** relational
- **current:** Across the evidence, is the characteristic shared between God and the person, or an exclusively creaturely analogue to something in God?
- **revised:** At the characteristic level, is it shared between God and the person, or an exclusively creaturely analogue to something in God?
- **rationale:** CORRECTED from an earlier wrong COMPLIANT verdict -- 'across the evidence' doesn't say which verses. Follows directly from D5.3.1's own characteristic-level finding -- synthesis grain, not a verse scan.

### D5.3.3 — REVISE

- **scope:** Other non-human beings | **window:** relational
- **current:** Where the characteristic is present or absent in a person, what does that indicate about the condition of the divine image in them — or is no such indication evidenced?
- **revised:** At the characteristic level, where it is present or absent in a person, what does that indicate about the condition of the divine image in them -- or is no such indication evidenced?
- **rationale:** General characteristic-level framing, not tied to one specific gated parent -- synthesis grain.

### D6.1.1 — COMPLIANT

- **scope:** Verse-context | **window:** constitutional
- **current:** At which constitutional level(s) does this verse locate the characteristic — from {spirit, soul, heart, mind, other soul-subset, a named body part} — and how is each engaged? Record every level evidenced, or none.
- **rationale:** Subject + grain (this verse) explicit.

### D6.1.2 — COMPLIANT

- **scope:** The HIB | **window:** constitutional
- **current:** Across the verses, what does the pattern of engaged and absent levels indicate — the characteristic's depth and seat, the levels it never engages, and (for any body link) whether the link is emphatic, functional, expressive, indicative, or mediating?
- **rationale:** Subject + grain (across the verses) explicit; compound but coherent.

### D6.2.1 — REVISE

- **scope:** The HIB | **window:** constitutional
- **current:** Where a body link exists (from the D6.1.1 audit), in which direction does it run — soul/spirit expressing through the body, the body feeding back to the soul, or both — and what follows from that direction? If no body link, record none.
- **revised:** Across the verses where a body link exists (per D6.1.1), in which direction does it run -- soul/spirit expressing through the body, the body feeding back to the soul, or both -- and what follows from that direction? If no body link, record none.
- **rationale:** Already has its own conditional ('where a body link exists') -- just needed 'evidence' swapped for 'verses' and the D6.1.1 citation kept explicit.

### D6.3.1 — REVISE

- **scope:** The HIB | **window:** constitutional
- **current:** Does the characteristic move across constitutional levels (spirit→soul→body), or onto the person from an external source — including another spirit (angelic or adversarial) — or in another direction; and if so in what sequence or pattern? If no movement, record none.
- **revised:** Across the characteristic's verses, does it move across constitutional levels (spirit->soul->body), or onto the person from an external source -- including another spirit (angelic or adversarial) -- or in another direction; and if so in what sequence or pattern? If no movement, record none.
- **rationale:** Subject explicit; no single parent gate to filter by -- plain aggregate.

### D7.1.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** relational
- **current:** In this verse, does the characteristic operate from God toward the human person, and if so how? Record none if it does not.
- **rationale:** Subject + grain (this verse) explicit.

### D7.1.2 — REVISE

- **scope:** Other non-human beings | **window:** relational
- **current:** On what basis does God extend the characteristic — conditional, unconditional, covenantal, or responsive — as the evidence shows?
- **revised:** Across the verses where God-to-human extension was found (per D7.1.1), on what basis does God extend the characteristic -- conditional, unconditional, covenantal, or responsive?
- **rationale:** CORRECTED from an earlier wrong COMPLIANT verdict -- 'as the evidence shows' is vague. D7.1.1 gates on 'record none if it does not' -- filtered to those verses.

### D7.1.3 — REVISE

- **scope:** Other non-human beings | **window:** relational
- **current:** What does God's extension of the characteristic show about his disposition toward the human person?
- **revised:** Across the verses where God-to-human extension was found (per D7.1.1), what does God's extension show about his disposition toward the human person?
- **rationale:** Same filter as D7.1.2 -- same underlying finding.

### D7.2.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** relational
- **current:** In this verse, is the characteristic extended by one person toward another, and if so how does it operate in that extension? Record none if it is not.
- **rationale:** Subject + grain (this verse) explicit.

### D7.2.2 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** What inner conditions or orientations in the giver accompany genuine extension of the characteristic?
- **revised:** Across the verses where person-to-person extension was found (per D7.2.1), what inner conditions or orientations in the giver accompany it?
- **rationale:** D7.2.1 gates on 'record none if it is not' -- filtered to those verses.

### D7.2.3 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** What does the evidence show a person must have received or become before they extend the characteristic?
- **revised:** Across the verses where person-to-person extension was found (per D7.2.1), what must a person have received or become before they extend the characteristic?
- **rationale:** CORRECTED from an earlier wrong COMPLIANT verdict -- 'the evidence show' is vague. Same filter as D7.2.2.

### D7.3.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** relational
- **current:** In this verse, is the characteristic taken up by a person from another, and if so how does it operate in that uptake? Record none if it is not.
- **rationale:** Subject + grain (this verse) explicit.

### D7.3.2 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** What inner conditions accompany or block uptake of the characteristic from another person?
- **revised:** Across the characteristic's verses, what inner conditions accompany or block uptake of the characteristic from another person?
- **rationale:** Covers BOTH the accompany and block outcomes explicitly -- filtering to only D7.3.1's 'yes' verses would exclude half the question's own scope, so plain aggregate is correct here, not a filtered subset.

### D7.3.3 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** What is the inner-being state of the person who meets the characteristic from another but does not take it up?
- **revised:** Across the verses where a person meets the characteristic from another but does not take it up (per D7.3.1/D7.3.2), what is their inner-being state?
- **rationale:** Names the specific (negative-case) subject explicitly and cites both relevant siblings, rather than leaving 'does not take it up' as an unfiled implicit continuation.

### D7.4.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** relational
- **current:** In this verse, does the characteristic operate in relation to other spiritual beings — angelic or adversarial — and if so how? Record none if it does not.
- **rationale:** Subject + grain (this verse) explicit.

### D7.4.2a — REVISE

- **scope:** Word/term (lexical) | **window:** relational
- **current:** Does an adversarial-being code ever appear as an acting party in a verse carrying this characteristic?
- **revised:** Across the characteristic's verses, does an adversarial spiritual being ever appear as an acting party in a verse carrying this characteristic?
- **rationale:** 'adversarial-being code' is raw internal terminology (T4 role-tag), not plain language; 'ever appear... in a verse' buries the aggregate grain inside the sentence.

### D7.4.2b — REVISE

- **scope:** Other non-human beings | **window:** relational
- **current:** What does that pattern show about the characteristic being a site of adversarial activity?
- **revised:** At the characteristic level, what does the pattern of adversarial-being presence (per D7.4.2a) show about the characteristic being a site of adversarial activity?
- **rationale:** D7.4.2a is already an aggregate ('ever appear... across verses') finding -- this synthesises that pattern, characteristic-level grain, not a fresh verse scan.

### D7.4.3a — REVISE

- **scope:** Word/term (lexical) | **window:** relational
- **current:** Does an angelic-being code ever appear as an acting party in a verse carrying this characteristic?
- **revised:** Across the characteristic's verses, does an angelic being ever appear as an acting party in a verse carrying this characteristic?
- **rationale:** 'angelic-being code' is the same jargon issue as D7.4.2a.

### D7.4.3b — REVISE

- **scope:** Other non-human beings | **window:** relational
- **current:** What does that pattern show about the characteristic being communicated, strengthened, or mediated through angelic ministry?
- **revised:** At the characteristic level, what does the pattern of angelic-being presence (per D7.4.3a) show about the characteristic being communicated, strengthened, or mediated through angelic ministry?
- **rationale:** Same synthesis-grain reasoning as D7.4.2b.

### D7.5.1 — COMPLIANT

- **scope:** Verse-context | **window:** origin
- **current:** Where does this verse say the characteristic originates — generated within the person, received from another person, bestowed by God, carried generationally, introduced by another spirit (angelic or adversarial), or not stated?
- **rationale:** Subject + grain (this verse) explicit.

### D7.5.2 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** origin
- **current:** Across the verses, is the origin single or multiple, and does it change with context?
- **revised:** Across the characteristic's verses, is its origin (per D7.5.1) single or multiple, and does it change with context?
- **rationale:** 'the origin' unrestated; D7.5.1 has no 'record none' gate (always produces an answer, including 'not stated') so no filtering needed -- tightened 'the verses' to 'the characteristic's verses' for precision.

### D7.6.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** relational
- **current:** In this verse, is the characteristic predicated of God or otherwise related to God; if so, in what relation (God as the one who bears it, acts, gives it, or is its object)? Record the relation, or record that it is not related to God here.
- **rationale:** Subject + grain (this verse) explicit.

### D7.7.1 — REVISE

- **scope:** Characteristic (HIB behaviour) | **window:** action-impact
- **current:** Where this verse contains an action or movement word tagged as an Operation in the cluster's role classification (the tag is `role-T3` in `cluster.cluster_code` -- consult that tagging directly, not this question's own memory of it), what is that word's relation to the parties present -- who initiates it and toward whom or what is it directed? Record none if no such operation word is present.
- **revised:** In this verse, where an action or movement word is classified as an Operation for this cluster, what is that word's relation to the parties present in the verse -- who initiates it, and toward whom or what is it directed? Record none if no such operation word is present.
- **rationale:** Original exposes raw schema identifiers ('the tag is `role-T3` in `cluster.cluster_code`') and a meta-instruction to 'consult that tagging directly, not this question's own memory of it' -- both belong in the prompt-assembly layer, not the catalogue text. Subject + grain (this verse) are otherwise fine and preserved.

### D9.1.1 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** scientific
- **current:** Per the cluster's science extract, what does neuroscience or physiology show about the mechanism underlying this characteristic, and does the verse evidence engage or diverge from that mechanism?
- **rationale:** Science-extract family, see D11.2.1's note.

### D9.2.1 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** scientific
- **current:** Per the cluster's science extract, does the scientific literature show the characteristic (or its pattern) transmitted generationally, and does the verse evidence show anything comparable (covenant, inheritance, generational language)?
- **rationale:** Science-extract family, see D11.2.1's note.

### F0.1.1 — REVISE

- **scope:** Verse-context | **window:** faculty
- **current:** In this verse, does the characteristic engage or is affected by specific faculties — the inner senses (hearing, sight, taste, touch, smell), spiritual discernment, the cognitive faculty (knowing, understanding, discerning), the memory faculty (the holding and retrieving of inner-being reality across time), the affective faculty (feeling and emotional experience), the creative faculty (imagination and the capacity to originate), the volitional faculty (the capacity to choose), the agency faculty (the capacity to act, initiate, and make happen), the moral-evaluation faculty (the capacity to assess against a standard of right, wrong, good, and true), conscience (the acute inner witness of sin, guilt, and conviction), conscientiousness (the integrated response of moral awareness, volition, and action), or relational capacity (the constitutional equipment for genuine connection with another person) — and if so, which faculty/faculties and how? Record none if it does not.
- **revised:** In this verse, does the characteristic engage or get affected by any inner-being faculty (the senses, spiritual discernment, cognition, memory, affect, creativity, volition, agency, moral evaluation, conscience, conscientiousness, or relational capacity), and if so which and how? Record none if it does not.
- **rationale:** At 980 characters this is the single longest question in the catalogue by a wide margin (next-longest is 395) -- one run-on sentence carrying full inline definitions of all 11 faculties. Revised text keeps subject+grain (this verse) but moves full faculty DEFINITIONS out of the question text -- FLAG: this assumes the faculty glossary is defined once elsewhere and available to the LLM; if it is NOT currently shown anywhere else in the prompt, the full definitions need to live in the shared system instructions, not be silently dropped. Confirm before applying.

### F0.1.2 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** faculty
- **current:** Across the verses, what does the pattern of engagement and non-engagement with the faculties indicate about the characteristic's nature?
- **rationale:** Subject self-descriptive ('the pattern of engagement...with the faculties' names its own topic); grain (across the verses) explicit.

### M0.1.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** What is the characteristic called in the programme, and what does the name signal about its essential nature?
- **rationale:** Programme-definitional question (the characteristic's own name/naming), not verse-evidence-grounded -- a distinct, legitimate category from the verse/aggregate taxonomy. Self-contained and clear as-is.

### M0.1.2 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** What do the primary Hebrew and Greek terms show at the definitional level?
- **rationale:** Definitional-lexical, same category as M0.1.1.

### M0.1.3 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** What directional, relational, or constitutional implication does the name carry?
- **rationale:** Definitional, same category.

### M0.2.1 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** meaning
- **current:** What kind of inner-being phenomenon is the characteristic — an act, a disposition, a condition/status, a quality, or something else?
- **rationale:** Definitional (characteristic-level classification), same category.

### M0.2.2 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** meaning
- **current:** Is the characteristic simple in structure, or does it combine constituent elements; if compound, which?
- **rationale:** Definitional, same category.

### M0.3.1 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** meaning
- **current:** What stands against the characteristic as its structural opposite — the inner-being reality that excludes it?
- **rationale:** Definitional, same category.

### M0.3.2 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** meaning
- **current:** What does the characteristic exclude or resist at its edge?
- **rationale:** Definitional, same category.

### M0.3.3 — COMPLIANT

- **scope:** Characteristic (HIB behaviour) | **window:** meaning
- **current:** Where does the characteristic end and another thing begin — what is it not?
- **rationale:** Definitional, same category.

### M0.4.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** What is the grammatical/stem form of the characteristic's primary term in this verse?
- **rationale:** Subject + grain (in this verse) explicit -- a per-occurrence lexical question, correctly distinguished from its purely-definitional M0.1-3 siblings.

### M0.5.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** What are the primary Hebrew and Greek terms for this characteristic, and what do their root meanings show?
- **rationale:** Definitional-lexical (vocabulary-wide), same category as M0.1.x.

### M0.5.10 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** What does the full vocabulary arc show about the characteristic's complete semantic range?
- **rationale:** Definitional summary, same category.

### M0.5.11 — REVISE

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** Where this occurrence's surface form/contextual sense diverges from the base lemma's general stepGloss, what nuance is that divergence carrying in THIS context, what is its impact here, and how does it compare against the word's other occurrences? Record none if this occurrence sits squarely within the base gloss with no notable shift.
- **revised:** In this verse, where this occurrence's meaning diverges from the term's usual sense elsewhere, what nuance does that divergence carry here, and how does it compare to the word's other occurrences? Record none if this occurrence matches the term's usual sense.
- **rationale:** Original exposes raw schema term 'stepGloss'. STRUCTURAL FLAG beyond wording: this question mixes two grains in one ask -- a per-occurrence divergence check AND a cross-occurrence comparison. Recommend splitting into two questions (one per-verse existence check, one cross-verse comparison triggered only when divergence is found) rather than a wording fix alone -- flagged for the researcher's decision, not applied here.

### M0.5.2 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** What is the grammatical range of the primary term (noun, verb, adjective, participle), and what does that range show about how the characteristic operates?
- **rationale:** Definitional, same category.

### M0.5.3 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** What is the semantic range of the primary term — across what breadth of meaning does it operate, including any idiomatic, analogical, or otherwise implied meaning carried by its use in combination with other terms?
- **rationale:** Definitional, same category.

### M0.5.4 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** Does the vocabulary include terms distinguishing distinct aspects — disposition versus act, received versus given, condition versus quality? Record which, or none.
- **rationale:** Definitional, same category.

### M0.5.5 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** Does the vocabulary include a term for the structural opposite or absence of this characteristic? Record it, or none.
- **rationale:** Definitional, same category.

### M0.5.6 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** Does the vocabulary include a person-type term — one for the person who habitually possesses or exercises this characteristic? Record it, or none.
- **rationale:** Definitional, same category.

### M0.5.7 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** Does the vocabulary include a supplication or seeking term — one for the act of seeking this characteristic from another? Record it, or none.
- **rationale:** Definitional, same category.

### M0.5.8 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** What does the relationship between the OT Hebrew and NT Greek vocabulary show about continuity or development of the characteristic across the Testaments?
- **rationale:** Definitional, same category.

### M0.5.9 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** meaning
- **current:** Is there a term newly coined in the NT period for this characteristic; if so, what does the coinage show? Record it, or none.
- **rationale:** Definitional, same category.

### M0.6.1 — COMPLIANT

- **scope:** The verse | **window:** literary
- **current:** What is the function of the primary term within its primary verse -- (a) what role does it play in the sentence, and (b) what role does it play in the verse's own argument, if a connective/chain edge shows one?
- **rationale:** Subject + grain (its primary verse) explicit; compound (a)/(b) is one coherent ask about function.

### M0.6.2 — REVISE

- **scope:** The verse | **window:** literary
- **current:** What is the logical structure of the key arguments in the verse evidence — premises and conclusions?
- **revised:** Across the characteristic's verses, what is the logical structure of its key arguments -- premises and conclusions?
- **rationale:** 'in the verse evidence' is ambiguous between the single primary/anchor verse and the whole verse set -- original doesn't disambiguate.

### M0.6.3 — COMPLIANT

- **scope:** The verse | **window:** literary
- **current:** Does any verse function as the primary anchor — the one most fully and directly expressing the characteristic's essential character? Record it, or none.
- **rationale:** Subject + grain (does ANY verse, scanning across all) explicit.

### M0.6.4 — COMPLIANT

- **scope:** The verse | **window:** literary
- **current:** What does the primary anchor verse show that no other verse shows?
- **rationale:** Subject explicit -- reuses the DEFINED TERM 'primary anchor verse' from M0.6.3 by name, not a bare pronoun; this is the right way to reference a sibling finding without embedding a raw code citation.

### M0.6.5 — REVISE

- **scope:** The verse | **window:** relational
- **current:** What role does this characteristic play in relation to the OTHER M-code characteristics present in this verse? Build on whatever earlier cluster-passes over this SAME verse already found (given as prior context) -- do not re-derive or duplicate their findings; the focus shifts to what THIS characteristic's own vantage point adds. Record none if no other M-code characteristic is present.
- **revised:** What role does this characteristic play in relation to the OTHER M-code characteristics present in this verse? Record none if no other M-code characteristic is present.
- **rationale:** Subject + grain (in this verse) are fine. The removed middle sentence ('Build on whatever earlier cluster-passes... do not re-derive or duplicate') is a PIPELINE-PROCESS instruction, not part of the analytical question -- it belongs in versereadinggenerate.py's own _instructions() prompt text (a CODE change), not the catalogue question_text. Flagging as a build item, not resolving here.

### T7.3.1 — RETIRED

- **scope:** Science | **window:** None
- **current:** Which human-science framework (psychology, moral philosophy, developmental psychology, sociology, anthropology, or other) serves as the most useful interpretive lens for this characteristic?
- **rationale:** Retired from the live catalogue (deleted=1) -- not reviewed, not live input to any stage.

### T7.3.2 — RETIRED

- **scope:** Science | **window:** None
- **current:** Where the framework illuminates the verse evidence — making a finding more coherent or complete — what does it show?
- **rationale:** Retired from the live catalogue (deleted=1) -- not reviewed, not live input to any stage.

### T7.3.3 — RETIRED

- **scope:** Science | **window:** None
- **current:** Where the verse evidence and the framework diverge, what does the divergence show?
- **rationale:** Retired from the live catalogue (deleted=1) -- not reviewed, not live input to any stage.

### T7.3.4 — RETIRED

- **scope:** Science | **window:** None
- **current:** Does the framework surface any aspect of the characteristic the verse evidence has not yet addressed, and does that absence call for further verse investigation?
- **rationale:** Retired from the live catalogue (deleted=1) -- not reviewed, not live input to any stage.

### X0.1.1 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** Which adjacent characteristics appear alongside this one in the verse evidence, and how frequently? Record none if no significant co-occurrence appears.
- **revised:** Across the characteristic's verses, which adjacent characteristics appear alongside this one, and how frequently? Record none if no significant co-occurrence appears.
- **rationale:** CORRECTED from an earlier wrong COMPLIANT verdict -- 'in the verse evidence' is the same vague pattern as 'across the evidence' elsewhere.

### X0.1.2 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** What does the co-occurrence pattern show about this characteristic's place in the inner-being landscape?
- **revised:** At the characteristic level, what does its co-occurrence pattern (per X0.1.1) show about its place in the inner-being landscape?
- **rationale:** X0.1.1 is already an aggregate ('how frequently... across verses') finding -- this synthesises that pattern, characteristic-level grain.

### X0.2.1 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** Does the evidence show this characteristic consistently preceding, following, or accompanying another in a sequence; if so, which and how? Record none if no sequence appears.
- **revised:** Across the characteristic's verses, does it consistently precede, following, or accompany another characteristic in a sequence; if so which and how? Record none if no sequence appears.
- **rationale:** CORRECTED from an earlier wrong COMPLIANT verdict -- 'does the evidence show' is vague.

### X0.2.2 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** What does the sequence show — is the relationship causal, developmental, or correlational?
- **revised:** At the characteristic level, what does its sequence pattern (per X0.2.1) show -- is the relationship causal, developmental, or correlational?
- **rationale:** X0.2.1 is already aggregate -- synthesis grain, same reasoning as X0.1.2.

### X0.3.1 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** Does this characteristic produce another in the evidence, and if so which, and by what mechanism? Record none if none is shown.
- **revised:** Across the characteristic's verses, does it produce another characteristic, and if so which, and by what mechanism? Record none if none is shown.
- **rationale:** CORRECTED from an earlier wrong COMPLIANT verdict -- 'in the evidence' is vague.

### X0.3.2 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** Is this characteristic produced by another, and if so which?
- **revised:** Across the characteristic's verses, is it produced by another characteristic, and if so which?
- **rationale:** No grain marker in the original; this is evidence sought WITHIN this characteristic's own verses (signs of being produced by another), same grain as X0.3.1, not a characteristic-level synthesis.

### X0.3.3 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** Is this characteristic a constituent element of another, or another a constituent of this one?
- **revised:** Across the characteristic's verses, is it a constituent element of another characteristic, or another a constituent of this one?
- **rationale:** Same reasoning as X0.3.2.

### X0.4.1 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** relational
- **current:** Which vocabulary terms, if any, does this characteristic share with other characteristics in the programme? Record none if none is shown.
- **rationale:** Subject + grain (in the programme, cross-characteristic) explicit.

### X0.4.2 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** relational
- **current:** Does the sharing extend to root-level architecture — a shared root generating terms across two or more characteristics?
- **rationale:** Subject reasonably self-descriptive ('the sharing' + 'across two or more characteristics' restates the cross-characteristic grain).

### X0.4.3 — COMPLIANT

- **scope:** Word/term (lexical) | **window:** relational
- **current:** What does the vocabulary sharing show about the conceptual relationship between the characteristics?
- **rationale:** Subject self-descriptive ('the vocabulary sharing... between the characteristics').

### X0.5.1 — COMPLIANT

- **scope:** Characteristic relational | **window:** relational
- **current:** Which adjacent characteristic most closely resembles this one, and what precisely distinguishes them?
- **rationale:** Subject + grain (cross-characteristic comparison) explicit.

### X0.5.2 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** Where the evidence shows apparent overlap, what is the precise boundary?
- **revised:** At the characteristic level, where comparison with its nearest neighbour (per X0.5.1) shows apparent overlap, what is the precise boundary between them?
- **rationale:** 'the evidence shows apparent overlap' floated without naming overlap WITH WHAT until X0.5.1 is read. This is a cross-characteristic comparison (against the nearest neighbour identified in X0.5.1), not a verse-evidence scan -- characteristic-level grain.

### X0.5.3 — REVISE

- **scope:** Characteristic relational | **window:** relational
- **current:** Is the distinction from the nearest neighbour one of degree, kind, direction, or constitutional level?
- **revised:** At the characteristic level, is the distinction between this characteristic and its nearest neighbour (per X0.5.1) one of degree, kind, direction, or constitutional level?
- **rationale:** Cross-characteristic comparison, same grain as X0.5.2; reuses X0.5.1's defined term correctly.

