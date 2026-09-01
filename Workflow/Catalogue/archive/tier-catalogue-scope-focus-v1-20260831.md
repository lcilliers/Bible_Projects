# Catalogue questions grouped by Scope focus

> Escalation #1007. For every active catalogue question, which of six things does it primarily
> focus on: **HIB characteristic**, **The verse**, **The HIB**, **Other non-human beings**,
> **Science**, or **None of these**?

## Which rows count as "active"

`wa_obs_question_catalogue` has two lifecycle signals that disagree on 58 rows (documented in
[`obs-catalogue-v2-20260829.md`](obs-catalogue-v2-20260829.md)): `status='active'` (239 rows) and
`deleted=0` (181 rows). This uses **`status='active' AND deleted=0`** — the same "live" definition
used throughout this escalation's prior work (the tier-catalogue mapping, the structural review) —
not bare `status='active'`, because the 58 disagreeing rows are soft-deleted despite still being
labelled active; treating them as "active" would silently pull in rows the catalogue itself has
marked gone. **181 rows.** If you meant literal `status='active'` including those 58, say so and
I'll rebuild against that set instead.

## What "HIB" means, and why that's the anchor for this classification

Confirmed from the IBA build record (`fix_hib_is_human_only_method_rule.py`, `BUILD.md`,
`debate-pipeline-technical-reference-20260806.md`), not assumed: **HIB = Human Inner Being** — a
named or implicit *human* subject. The rule is explicit and load-bearing: *"A non-human being can
NEVER itself be registered as a HIB."* That single line does the real work of separating two of
your six buckets — a question about God, an angel, or an adversarial spirit is categorically **not**
a question about a HIB, no matter how central it is to the characteristic's own analysis.

## How each of the 181 was classified

Read individually, not pattern-matched. The reasoning that recurred:

- **HIB characteristic** — the question's throughline subject is the characteristic ("the word")
  itself, operating in/through a person: what it is, how it behaves, what it produces, how it
  relates to other characteristics, its own vocabulary. This is the large majority (146/181) —
  consistent with the tier-catalogue mapping's own finding that the whole T0–T7 structure is
  built characteristic-first.
- **Other non-human beings** — the question's defining relational axis is God, an angelic being,
  or an adversarial spirit, not the human person. Two structural signals drove this: (a) T0's own
  section title is "Divine Image and Created Design" — every T0 question is *about* the
  characteristic's relation to God, not to the person as such; (b) T4's own three "Interface"
  components split cleanly by name — **Divine Interface** (God↔human) and **Spiritual Beings
  Interface** land here, **Human Interface** (giving/receiving/boundaries) does not, because both
  parties there are human — within HIB's own domain, not outside it. 19 rows.
- **The verse** — T7.2 ("Verse and Literary Interpretation") is the one component whose focus
  genuinely shifts to the verse as a literary/textual object — form, argument, setting, function —
  rather than to the characteristic's own behaviour. 6 rows.
- **The HIB** — the question is about the human person's own constitution/nature/agency as such,
  not about one characteristic operating in them. Only found in the Leviticus book-synthesis
  questions (`LEV-GEN-01/04/05` — "the inner being... the seat and locus," "the inner being IN
  OPERATION," "the inner being's own act"), never in the tiered T0–T7 set, which is always
  characteristic-first even at its broadest. 3 rows.
- **Science** — T7.3 ("Human Science Frameworks"), the one component explicitly about applying an
  external interpretive lens (psychology, sociology, etc.). 4 rows.
- **None of these** — a genuine residual: `WS-006` asks whether the programme's own registry
  structure (a design/organisational question, not a claim about the characteristic itself) holds
  together; `LEV-GEN-02`/`LEV-GEN-06` ask how atonement/redemption *mechanically operate* — ritual
  and theological process questions, not a characteristic of the inner being, the verse, the HIB,
  a non-human being, or a science lens. 3 rows.

**181 = 146 + 19 + 6 + 3 + 4 + 3, exactly** — every row landed in one bucket, none forced or
left over.

## Where I'm least confident — read these first

Marked ⚠ in the table below. Flagging plainly rather than presenting these as settled:

- **`T4.2` (Divine Interface — Human to God, 3 questions)** — grouped with `T4.1`/`T4.6` under
  "Other non-human beings" for consistency with the "Divine Interface" component name, but the
  case is weaker here than for `T4.1`: `T4.2` asks about the *person's own* movement (seeking,
  supplication, worship) with God as the direction, not the acting subject — arguably closer to
  "HIB characteristic" (a human disposition, God-directed) than `T4.1` (where God is the one
  acting). Worth a second look.
- **`WS-003`/`WS-004`** (Goodness Extensions, obs_id 217/218) — each anchored to a specific verse
  or liturgical pattern, but classified "HIB characteristic" because the question's payload is
  what that evidence shows *about the characteristic* (goodness), not about the verse's own
  literary form. Could be argued either way.
- **`LEV-CLN-01`–`06`** (6 questions) — classified "HIB characteristic" by treating
  clean/unclean as a characteristic-shaped state operating on the person, matching the pattern of
  every other Extensions section. It's a book-specific ritual-purity concept rather than an
  inner-being trait in the usual sense, so "The HIB" or "None of these" are both defensible
  alternate readings.
- **`LEV-GEN-02`/`LEV-GEN-06`** (atonement, redemption) — classified "None of these" as
  theological-mechanism questions, but could instead be read as "HIB characteristic" if atonement/
  redemption are treated as characteristics acting on the person (their own outer limit,
  mechanism, and effect are exactly what T1/T5-shaped questions elsewhere ask of "the word").

## Summary

| Bucket | Count |
|---|---|
| HIB characteristic | 146 |
| Other non-human beings | 19 |
| The verse | 6 |
| The HIB | 3 |
| Science | 4 |
| None of these | 3 |
| **Total** | **181** |

## Full listing, by bucket

## HIB characteristic (146)

| obs_id | Code | Section | Question | Borderline? |
|---|---|---|---|---|
| 187 | `C-001` | Compassion Extensions | Does the evidence for the word include a significant cluster of prohibition contexts — and if so, what does the frequency of the word's prohibition reveal about its default status in the inner being? |  |
| 188 | `C-002` | Compassion Extensions | Does any verse depict the word winning an inner contest with a competing disposition — and if so, what does this reveal about the word's relationship to other inner-being characteristics that it must overcome? |  |
| 189 | `C-003` | Compassion Extensions | Does the evidence assign the word an explicitly everlasting or permanent temporal character — in direct contrast to the momentary character of a competing or opposing disposition? |  |
| 192 | `C-006` | Compassion Extensions | Does any verse name the violation of the word by the very person who most characteristically bears it — and if so, what does this reveal about the word's resilience or fragility under external pressure? |  |
| 193 | `C-007` | Compassion Extensions | Has the word acquired a standardised or institutionalised social form — a normative outward expression that names what the characteristic looks like when it is embodied in social practice? |  |
| 148 | `F-001` | Forgiveness Extensions | Does the word have an outer limit — a condition or state in which it is explicitly withheld or cannot operate — and what does that outer limit reveal about the word's nature? |  |
| 149 | `F-002` | Forgiveness Extensions | Can the structure of the word's action be misused or inverted — can the same act-structure produce a wrong result — and what is the evidence? |  |
| 150 | `F-003` | Forgiveness Extensions | Is there a vertical-horizontal structural interdependence in the word's operation — does reception from God structurally enable extension toward others? |  |
| 151 | `F-004` | Forgiveness Extensions | Is the word's primary grammatical subject restricted — is it used exclusively or primarily with one type of subject (divine, human, or other)? |  |
| 152 | `F-005` | Forgiveness Extensions | What is the mechanism through which the word is administered or conveyed — and what is the relationship between the outward mechanism and the inner reality it produces? |  |
| 153 | `F-006` | Forgiveness Extensions | Does the word operate unconditionally — or does it have stated conditions under which it is granted or withheld? |  |
| 154 | `F-007` | Forgiveness Extensions | Is the word a single act or a compound of distinct component acts — and if compound, what are the components and are they always simultaneous? |  |
| 155 | `F-008` | Forgiveness Extensions | What does the word make possible in a relationship that would otherwise be closed or broken — and what relational cycle does it break? |  |
| 156 | `F-009` | Forgiveness Extensions | Does the word function as a prerequisite or enabling condition for another spiritual act or practice — and if so, which one and why? |  |
| 157 | `F-010` | Forgiveness Extensions | Are the downstream inner-being effects of the word proportional to the degree or magnitude of the word received — does more of the word produce more of the effect? |  |
| 158 | `F-011` | Forgiveness Extensions | Does the word share vocabulary with adjacent characteristics — or does it occupy an isolated lexical space? What does the degree of sharing or isolation suggest about the word's relationship to adjacent characteristics? |  |
| 159 | `F-012` | Forgiveness Extensions | Is the word named in Scripture as a divine possession or attribute — something that belongs to God — distinct from an act God performs? What does that naming imply about access to the word? |  |
| 160 | `F-013` | Forgiveness Extensions | What practices, disciplines, or ongoing inner acts feed or sustain the human capacity to extend the word to others? |  |
| 161 | `F-014` | Forgiveness Extensions | Is the word a terminal inner-being state — one in which the person rests — or a transitional one that characteristically produces movement to a further state? What is the evidence either way? |  |
| 215 | `WS-001` | Goodness Extensions | Does the comparative wisdom idiom (Group 884-004 — better-than sayings) operate as a distinct mode of goodness, or is it a subset of moral character? |  |
| 216 | `WS-002` | Goodness Extensions | What is the analytical relationship between agathōsunē (G0019 — goodness) and chrēstotēs (G5544 — kindness) as co-OWNER terms of this registry? Are they aspects of a single characteristic or genuinely distinct inner-being phenomena sharing a registry? |  |
| 217 | `WS-003` | Goodness Extensions | What does the Haman instance (Est 5:9 — tov-lev, glad of heart) reveal about the difference between genuine inner well-being and morally ungrounded inner pleasure? | ⚠ |
| 218 | `WS-004` | Goodness Extensions | What does the liturgical repetition of "the Lord is good, his steadfast love endures forever" (appearing as a refrain across Psalms 106, 107, 118, 136) reveal about goodness as a confessional and community-forming declaration? | ⚠ |
| 162 | `L-001` | Love Extensions | Does the word hold a foundational position relative to other inner-being characteristics — does it govern, generate, or organise them? |  |
| 163 | `L-002` | Love Extensions | Where the word has distinct modes of operation, are those modes held simultaneously or do they operate sequentially? |  |
| 164 | `L-003` | Love Extensions | Does the word have an inherent directionality — is it always oriented toward an object — and what does the choice of object determine about the word's moral character? |  |
| 165 | `L-004` | Love Extensions | Can the word function as an identity diagnostic — does what a person does with this word reveal what kind of person they are? |  |
| 166 | `L-005` | Love Extensions | Does the word operate at a level below conscious attention or deliberate will — and if so, what does this imply about its depth in the inner being? |  |
| 167 | `L-006` | Love Extensions | Does the vocabulary of the word include a systematic taxonomy of its own misdirected forms — and if so, what structural logic organises that taxonomy? |  |
| 168 | `L-007` | Love Extensions | Can the word increase or grow in the inner being — and if so, by what means? |  |
| 169 | `L-008` | Love Extensions | Does the word have a definitional outward expression — a form that constitutes what the word is rather than merely evidencing it? |  |
| 170 | `L-009` | Love Extensions | Is the word named in Scripture as constitutive of the divine essence — what God is — rather than merely as a divine attribute or act? |  |
| 171 | `L-010` | Love Extensions | Does the word's structural opposite operate under the same moral logic as the word itself — can the contrary also be either rightly or wrongly directed? |  |
| 172 | `L-011` | Love Extensions | What is the relationship between the word as an inner disposition and the word as an outward act — are they competitors, co-expressions, or in a different structural relationship? |  |
| 173 | `L-012` | Love Extensions | Does the word carry an epistemic dimension — is knowing and being known a structural component of the word's operation? |  |
| 174 | `L-013` | Love Extensions | Does the word function as a publicly legible signal — a means by which something about the inner community or person is read by those outside? |  |
| 175 | `L-014` | Love Extensions | Does the word produce a reorganisation of social dynamics — and if so, in what direction does it reorganise them? |  |
| 177 | `M-002` | Mercy Extensions | Does the word require a structural asymmetry between giver and receiver — is the positional difference (greater-to-lesser, strong-to-weak) a precondition of the word's operation, or can it operate between equals? |  |
| 181 | `M-006` | Mercy Extensions | Has the word been given an architectural or material realisation in Israel's worship — a physical structure in which the word is spatially located — and if so, what does that materialisation reveal about the word's character and the nature of access to it? |  |
| 182 | `M-007` | Mercy Extensions | Does the word share its structural logic (such as gratuitousness or disproportionality) with an apparently contrary reality — does the same principle that governs the word also appear in something that seems to contradict it? |  |
| 184 | `M-009` | Mercy Extensions | What is the causal relationship between the word as an inner disposition and the structural mechanism through which it operates — does the disposition produce the mechanism, or does the mechanism produce the disposition? |  |
| 185 | `M-010` | Mercy Extensions | What does a documented directional reversal in a key vocabulary term reveal about the word's theological significance — what claim about the nature of the divine-human relationship is encoded in the reversal? |  |
| 236 | `T1.1.1` | T1 — Definition | What is the characteristic called in the programme, and what does the name signal about its essential nature? |  |
| 237 | `T1.1.2` | T1 — Definition | What do the primary Hebrew and Greek terms show at the definitional level? |  |
| 238 | `T1.1.3` | T1 — Definition | What directional, relational, or constitutional implication does the name carry? |  |
| 239 | `T1.2.1` | T1 — Definition | What kind of inner-being phenomenon is the characteristic — an act, a disposition, a condition/status, a quality, or something else? |  |
| 240 | `T1.2.2` | T1 — Definition | Is the characteristic simple in structure, or does it combine constituent elements; if compound, which? |  |
| 242 | `T1.3.1` | T1 — Definition | What stands against the characteristic as its structural opposite — the inner-being reality that excludes it? |  |
| 243 | `T1.3.2` | T1 — Definition | What does the characteristic exclude or resist at its edge? |  |
| 244 | `T1.3.3` | T1 — Definition | Where does the characteristic end and another thing begin — what is it not? |  |
| 245 | `T1.4.1` | T1 — Definition | In what distinct mode(s) does the characteristic operate within the inner person in this verse — including its grammatical/stem form and the manner of functioning? |  |
| 246 | `T1.4.2` | T1 — Definition | Does the mode of operation vary by context, direction, or constitutional level; if so, how? |  |
| 247 | `T1.4.3` | T1 — Definition | Does the characteristic operate through a communicative or speech-based mode (commanded, addressed, spoken); if so, how? Record it, or record none. |  |
| 248 | `T1.5.1` | T1 — Definition | What first or most immediate inner-being response does this verse show following the characteristic? Record it, or record none. |  |
| 249 | `T1.5.2` | T1 — Definition | Across the verses, is that immediate response consistent or varied? |  |
| 251 | `T1.6.1` | T1 — Definition | What does the characteristic produce in the inner being over time in this verse — what states, qualities, capacities, or orientations does it establish? Record it, or record none. |  |
| 253 | `T1.6.3` | T1 — Definition | How does the sustained effect differ from the immediate response (T1.5)? |  |
| 254 | `T1.7.1` | T1 — Definition | Under what inner conditions does the characteristic take hold or operate rightly? |  |
| 255 | `T1.7.2` | T1 — Definition | Under what inner conditions is the characteristic blocked, distorted, resisted, or not taken up — including, where the evidence shows it, distortion or interference by another spirit (adversarial or angelic)? |  |
| 256 | `T1.7.3` | T1 — Definition | What is the inner-being state of the person in whom the characteristic is present but does not take hold? |  |
| 260 | `T2.1.1` | T2 — Constitutional Location and Boundaries | At which constitutional level(s) does this verse locate the characteristic — from {spirit, soul, heart, mind, other soul-subset, a named body part} — and how is each engaged? Record every level evidenced, or none. |  |
| 261 | `T2.1.2` | T2 — Constitutional Location and Boundaries | Across the verses, what does the pattern of engaged and absent levels indicate — the characteristic's depth and seat, the levels it never engages, and (for any body link) whether the link is emphatic, functional, expressive, indicative, or mediating? |  |
| 288 | `T2.10.1` | T2 — Constitutional Location and Boundaries | Does the characteristic move across constitutional levels (spirit→soul→body), or onto the person from an external source — including another spirit (angelic or adversarial) — or in another direction; and if so in what sequence or pattern? If no movement, record none. |  |
| 279 | `T2.7.1` | T2 — Constitutional Location and Boundaries | Where a body link exists (from the T2.1.1 audit), in which direction does it run — soul/spirit expressing through the body, the body feeding back to the soul, or both — and what follows from that direction? If no body link, record none. |  |
| 285 | `T2.9.1` | T2 — Constitutional Location and Boundaries | Where does this verse say the characteristic originates — generated within the person, received from another person, bestowed by God, carried generationally, introduced by another spirit (angelic or adversarial), or not stated? |  |
| 286 | `T2.9.2` | T2 — Constitutional Location and Boundaries | Across the verses, is the origin single or multiple, and does it change with context? |  |
| 291 | `T3.1.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage the perceptive faculty — the inner senses (hearing, sight, taste, touch, smell) and spiritual discernment — and if so, which inner sense and how? Record none if it does not. |  |
| 292 | `T3.1.2` | T3 — The Inner Faculties | How does the characteristic affect perception in the person here — and record no effect if none is evidenced. |  |
| 293 | `T3.1.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with perception indicate about the characteristic's nature? |  |
| 318 | `T3.10.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage conscientiousness — the integrated response of moral awareness, volition, and action — and if so, how? Record none if it does not. |  |
| 319 | `T3.10.2` | T3 — The Inner Faculties | How does the characteristic affect conscientiousness in the person here — and record no effect if none is evidenced. |  |
| 320 | `T3.10.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with conscientiousness indicate about the characteristic's nature? |  |
| 321 | `T3.11.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage the relational capacity — the constitutional equipment for genuine connection with another person — and if so, how? Record none if it does not. |  |
| 322 | `T3.11.2` | T3 — The Inner Faculties | How does the characteristic affect relational capacity in the person here — and record no effect if none is evidenced. |  |
| 323 | `T3.11.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with relational capacity indicate about the characteristic's nature? |  |
| 294 | `T3.2.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage the cognitive faculty — knowing, understanding, discerning — and if so, how? Record none if it does not. |  |
| 295 | `T3.2.2` | T3 — The Inner Faculties | How does the characteristic affect cognition in the person here — and record no effect if none is evidenced. |  |
| 296 | `T3.2.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with cognition indicate about the characteristic's nature? |  |
| 297 | `T3.3.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage the memory faculty — the holding and retrieving of inner-being reality across time — and if so, how? Record none if it does not. |  |
| 298 | `T3.3.2` | T3 — The Inner Faculties | How does the characteristic affect memory in the person here — and record no effect if none is evidenced. |  |
| 299 | `T3.3.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with memory indicate about the characteristic's nature? |  |
| 300 | `T3.4.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage the affective faculty — feeling and emotional experience — and if so, how? Record none if it does not. |  |
| 301 | `T3.4.2` | T3 — The Inner Faculties | How does the characteristic affect the affective faculty in the person here — and record no effect if none is evidenced. |  |
| 302 | `T3.4.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with affect indicate about the characteristic's nature? |  |
| 303 | `T3.5.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage the creative faculty — imagination and the capacity to originate — and if so, how? Record none if it does not. |  |
| 304 | `T3.5.2` | T3 — The Inner Faculties | How does the characteristic affect creativity in the person here — and record no effect if none is evidenced. |  |
| 305 | `T3.5.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with creativity indicate about the characteristic's nature? |  |
| 306 | `T3.6.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage the volitional faculty — the capacity to choose — and if so, how? Record none if it does not. |  |
| 307 | `T3.6.2` | T3 — The Inner Faculties | How does the characteristic affect volition in the person here — including its capacity, its interaction with other characteristics, and the constraints under which it operates — and record no effect if none is evidenced. |  |
| 308 | `T3.6.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with volition indicate about the characteristic's nature? |  |
| 309 | `T3.7.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage the agency faculty — the capacity to act, initiate, and make happen — and if so, how? Record none if it does not. |  |
| 310 | `T3.7.2` | T3 — The Inner Faculties | How does the characteristic affect agency in the person here — and record no effect if none is evidenced. |  |
| 311 | `T3.7.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with agency indicate about the characteristic's nature? |  |
| 312 | `T3.8.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage the moral-evaluation faculty — the capacity to assess against a standard of right, wrong, good, and true — and if so, how? Record none if it does not. |  |
| 313 | `T3.8.2` | T3 — The Inner Faculties | How does the characteristic affect moral evaluation in the person here — and record no effect if none is evidenced. |  |
| 314 | `T3.8.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with moral evaluation indicate about the characteristic's nature? |  |
| 315 | `T3.9.1` | T3 — The Inner Faculties | In this verse, does the characteristic engage the conscience — the acute inner witness of sin, guilt, and conviction — and if so, how? Record none if it does not. |  |
| 316 | `T3.9.2` | T3 — The Inner Faculties | How does the characteristic affect conscience in the person here — and record no effect if none is evidenced. |  |
| 317 | `T3.9.3` | T3 — The Inner Faculties | Across the verses, what does the pattern of engagement and non-engagement with conscience indicate about the characteristic's nature? |  |
| 332 | `T4.3.1` | T4 — Relational Interfaces | In this verse, is the characteristic extended by one person toward another, and if so how does it operate in that extension? Record none if it is not. |  |
| 333 | `T4.3.2` | T4 — Relational Interfaces | What inner conditions or orientations in the giver accompany genuine extension of the characteristic? |  |
| 334 | `T4.3.3` | T4 — Relational Interfaces | What does the evidence show a person must have received or become before they extend the characteristic? |  |
| 336 | `T4.4.1` | T4 — Relational Interfaces | In this verse, is the characteristic taken up by a person from another, and if so how does it operate in that uptake? Record none if it is not. |  |
| 337 | `T4.4.2` | T4 — Relational Interfaces | What inner conditions accompany or block uptake of the characteristic from another person? |  |
| 338 | `T4.4.3` | T4 — Relational Interfaces | What is the inner-being state of the person who meets the characteristic from another but does not take it up? |  |
| 340 | `T4.5.1` | T4 — Relational Interfaces | Does the evidence show the characteristic operating differently within existing relational bonds versus across relational distance or difference; if so, how? |  |
| 341 | `T4.5.2` | T4 — Relational Interfaces | Does the characteristic operate within covenantal contexts only, or does it cross covenantal boundaries, as the evidence shows? |  |
| 342 | `T4.5.3` | T4 — Relational Interfaces | What does the evidence show about the relational scope of the characteristic — who is included and who is not? |  |
| 348 | `T5.1.1` | T5 — Formative and Developmental Dimension | In this verse, does the characteristic produce transformation in the person, and if so does it change the person's condition, their orientation to their condition, or both? Record none if no transformation is shown. |  |
| 349 | `T5.1.2` | T5 — Formative and Developmental Dimension | Is the transformation reversible or irreversible in the evidence? |  |
| 351 | `T5.2.1` | T5 — Formative and Developmental Dimension | Does this verse describe a sequence of inner states the characteristic moves the person through — a before, during, and after — and what are those states? Record none if no sequence is shown. |  |
| 354 | `T5.3.1` | T5 — Formative and Developmental Dimension | In this verse, by what mechanism does the characteristic produce change — discipline, encounter, gradual formation, sudden transformation, or other? Record none if no mechanism is shown. |  |
| 355 | `T5.3.2` | T5 — Formative and Developmental Dimension | Does the mechanism differ across contexts in the evidence; if so, how? |  |
| 357 | `T5.4.1` | T5 — Formative and Developmental Dimension | In this verse, does the characteristic operate in relation to suffering or affliction — as a response to it, a product of it, or a context for it? Record none if no such relation is shown. |  |
| 358 | `T5.4.2` | T5 — Formative and Developmental Dimension | What does the evidence show suffering doing to the characteristic in the person — and record no such effect if none is shown. |  |
| 360 | `T5.5.1` | T5 — Formative and Developmental Dimension | In this verse, does the characteristic participate in the longer arc of character formation and sanctification — shaping the person over time — and what does the evidence show of its role in that arc? Record none if no such participation is shown. |  |
| 363 | `T5.6.1` | T5 — Formative and Developmental Dimension | In this verse, is the characteristic oriented toward an eschatological fullness — a future state toward which its present operation points — and what does its present experience anticipate of that fullness? Record none if no such orientation is shown. |  |
| 369 | `T6.1.1` | T6 — Structural Relationships with Other Characteristics | Which adjacent characteristics appear alongside this one in the verse evidence, and how frequently? Record none if no significant co-occurrence appears. |  |
| 370 | `T6.1.2` | T6 — Structural Relationships with Other Characteristics | What does the co-occurrence pattern show about this characteristic's place in the inner-being landscape? |  |
| 372 | `T6.2.1` | T6 — Structural Relationships with Other Characteristics | Does the evidence show this characteristic consistently preceding, following, or accompanying another in a sequence; if so, which and how? Record none if no sequence appears. |  |
| 373 | `T6.2.2` | T6 — Structural Relationships with Other Characteristics | What does the sequence show — is the relationship causal, developmental, or correlational? |  |
| 375 | `T6.3.1` | T6 — Structural Relationships with Other Characteristics | Does this characteristic produce another in the evidence, and if so which, and by what mechanism? Record none if none is shown. |  |
| 376 | `T6.3.2` | T6 — Structural Relationships with Other Characteristics | Is this characteristic produced by another, and if so which? |  |
| 377 | `T6.3.3` | T6 — Structural Relationships with Other Characteristics | Is this characteristic a constituent element of another, or another a constituent of this one? |  |
| 379 | `T6.4.1` | T6 — Structural Relationships with Other Characteristics | Which vocabulary terms, if any, does this characteristic share with other characteristics in the programme? Record none if none is shown. |  |
| 380 | `T6.4.2` | T6 — Structural Relationships with Other Characteristics | Does the sharing extend to root-level architecture — a shared root generating terms across two or more characteristics? |  |
| 381 | `T6.4.3` | T6 — Structural Relationships with Other Characteristics | What does the vocabulary sharing show about the conceptual relationship between the characteristics? |  |
| 383 | `T6.5.1` | T6 — Structural Relationships with Other Characteristics | Which adjacent characteristic most closely resembles this one, and what precisely distinguishes them? |  |
| 384 | `T6.5.2` | T6 — Structural Relationships with Other Characteristics | Where the evidence shows apparent overlap, what is the precise boundary? |  |
| 385 | `T6.5.3` | T6 — Structural Relationships with Other Characteristics | Is the distinction from the nearest neighbour one of degree, kind, direction, or constitutional level? |  |
| 393 | `T7.1.1` | T7 — Evidential and Methodological Foundation | What are the primary Hebrew and Greek terms for this characteristic, and what do their root meanings show? |  |
| 402 | `T7.1.10` | T7 — Evidential and Methodological Foundation | What does the full vocabulary arc show about the characteristic's complete semantic range? |  |
| 394 | `T7.1.2` | T7 — Evidential and Methodological Foundation | What is the grammatical range of the primary term (noun, verb, adjective, participle), and what does that range show about how the characteristic operates? |  |
| 395 | `T7.1.3` | T7 — Evidential and Methodological Foundation | What is the semantic range of the primary term — across what breadth of meaning does it operate? |  |
| 396 | `T7.1.4` | T7 — Evidential and Methodological Foundation | Does the vocabulary include terms distinguishing distinct aspects — disposition versus act, received versus given, condition versus quality? Record which, or none. |  |
| 397 | `T7.1.5` | T7 — Evidential and Methodological Foundation | Does the vocabulary include a term for the structural opposite or absence of this characteristic? Record it, or none. |  |
| 398 | `T7.1.6` | T7 — Evidential and Methodological Foundation | Does the vocabulary include a person-type term — one for the person who habitually possesses or exercises this characteristic? Record it, or none. |  |
| 399 | `T7.1.7` | T7 — Evidential and Methodological Foundation | Does the vocabulary include a supplication or seeking term — one for the act of seeking this characteristic from another? Record it, or none. |  |
| 400 | `T7.1.8` | T7 — Evidential and Methodological Foundation | What does the relationship between the OT Hebrew and NT Greek vocabulary show about continuity or development of the characteristic across the Testaments? |  |
| 401 | `T7.1.9` | T7 — Evidential and Methodological Foundation | Is there a term newly coined in the NT period for this characteristic; if so, what does the coinage show? Record it, or none. |  |
| 413 | `LEV-CLN-01` | leviticus | Why is it necessary to be clean? (what does cleanness enable / uncleanness cost) | ⚠ |
| 414 | `LEV-CLN-02` | leviticus | Where does the concept of "unclean" come from? (source + root sense) | ⚠ |
| 415 | `LEV-CLN-03` | leviticus | Why cover the unclean rather than scrub it clean? (reset x source_domain) | ⚠ |
| 416 | `LEV-CLN-04` | leviticus | Is the need to be clean IB-desire, external expectation, or prerequisite? | ⚠ |
| 417 | `LEV-CLN-05` | leviticus | Does awareness of unclean come into play? | ⚠ |
| 418 | `LEV-CLN-06` | leviticus | Is clean status past-only, or also forward-standing? | ⚠ |

## Other non-human beings (19)

| obs_id | Code | Section | Question | Borderline? |
|---|---|---|---|---|
| 224 | `T0.1.1` | T0 — Divine Image and Created Design | In this verse, is the characteristic predicated of God or otherwise related to God; if so, in what relation (God as the one who bears it, acts, gives it, or is its object)? Record the relation, or record that it is not related to God here. |  |
| 225 | `T0.1.2` | T0 — Divine Image and Created Design | Across the characteristic's verses, is it ever borne by God himself or only by the creature, and what does that pattern of presence or absence indicate for its place in the human person and in the divine image? |  |
| 227 | `T0.2.1` | T0 — Divine Image and Created Design | Does this verse state any purpose, role, or effect the characteristic serves in the person — what it leads the person to be, do, or become? Record it if stated; otherwise record none. |  |
| 228 | `T0.2.2` | T0 — Divine Image and Created Design | Across the evidence, does the characteristic's role read as belonging to created design, to the fallen condition, to both, or as not determinable? |  |
| 229 | `T0.2.3` | T0 — Divine Image and Created Design | Across the evidence, is there any orientation toward a future fullness — something the person moves toward, not only what they currently are? Record it, or record none. |  |
| 230 | `T0.3.1` | T0 — Divine Image and Created Design | From the characteristic's God-relation (T0.1) and its role (T0.2), what aspect of the divine likeness, if any, does it instantiate in the person? Record the aspect, or record none. |  |
| 231 | `T0.3.2` | T0 — Divine Image and Created Design | Across the evidence, is the characteristic shared between God and the person, or an exclusively creaturely analogue to something in God? |  |
| 232 | `T0.3.3` | T0 — Divine Image and Created Design | Where the characteristic is present or absent in a person, what does that indicate about the condition of the divine image in them — or is no such indication evidenced? |  |
| 233 | `T0.4.1` | T0 — Divine Image and Created Design | Does this verse use the characteristic typologically — pointing beyond the immediate to a covenantal, eschatological, or christological reality; if so, which, and in which direction (the divine instance establishing the pattern, or the human pointing toward the divine)? Record the use and direction, or record none. |  |
| 324 | `T4.1.1` | T4 — Relational Interfaces | In this verse, does the characteristic operate from God toward the human person, and if so how? Record none if it does not. | ⚠ |
| 325 | `T4.1.2` | T4 — Relational Interfaces | On what basis does God extend the characteristic — conditional, unconditional, covenantal, or responsive — as the evidence shows? | ⚠ |
| 326 | `T4.1.3` | T4 — Relational Interfaces | What does God's extension of the characteristic show about his disposition toward the human person? | ⚠ |
| 328 | `T4.2.1` | T4 — Relational Interfaces | In this verse, does the characteristic operate in the person's movement toward God — seeking, supplication, worship, covenant — and if so how? Record none if it does not. | ⚠ |
| 329 | `T4.2.2` | T4 — Relational Interfaces | What inner posture does this movement require, as the evidence shows? | ⚠ |
| 330 | `T4.2.3` | T4 — Relational Interfaces | What does the human-to-God direction of the characteristic show about the person's relationship with God? | ⚠ |
| 344 | `T4.6.1` | T4 — Relational Interfaces | In this verse, does the characteristic operate in relation to other spiritual beings — angelic or adversarial — and if so how? Record none if it does not. |  |
| 345 | `T4.6.2` | T4 — Relational Interfaces | Is the characteristic a site of adversarial activity — something that can be attacked, distorted, or weaponised by adversarial powers — as the evidence shows? |  |
| 346 | `T4.6.3` | T4 — Relational Interfaces | Is the characteristic communicated, strengthened, or mediated through angelic ministry in the evidence? |  |
| 421 | `LEV-GEN-03` | leviticus | Does Leviticus reveal a divine interior (God's disposition)? |  |

## The verse (6)

| obs_id | Code | Section | Question | Borderline? |
|---|---|---|---|---|
| 403 | `T7.2.1` | T7 — Evidential and Methodological Foundation | What is the function of the primary term within its primary verse — what role does it play in the sentence and argument? |  |
| 404 | `T7.2.2` | T7 — Evidential and Methodological Foundation | What literary form carries the primary verse evidence (narrative, psalm, wisdom, prophecy, epistle, apocalyptic), and what does that form require for responsible interpretation? |  |
| 405 | `T7.2.3` | T7 — Evidential and Methodological Foundation | What is the logical structure of the key arguments in the verse evidence — premises and conclusions? |  |
| 406 | `T7.2.4` | T7 — Evidential and Methodological Foundation | What contextual setting carries the primary verse evidence (judicial, liturgical, covenantal, communal, eschatological), and what does that setting show? |  |
| 407 | `T7.2.5` | T7 — Evidential and Methodological Foundation | Does any verse function as the primary anchor — the one most fully and directly expressing the characteristic's essential character? Record it, or none. |  |
| 408 | `T7.2.6` | T7 — Evidential and Methodological Foundation | What does the primary anchor verse show that no other verse shows? |  |

## The HIB (3)

| obs_id | Code | Section | Question | Borderline? |
|---|---|---|---|---|
| 419 | `LEV-GEN-01` | leviticus | What is the inner being in Leviticus - the seat and locus (nephesh vs heart)? |  |
| 422 | `LEV-GEN-04` | leviticus | What does Leviticus surface as the inner being IN OPERATION (book synthesis)? |  |
| 423 | `LEV-GEN-05` | leviticus | What is the inner being's own act / the way back (affliction, confession, humbling)? |  |

## Science (4)

| obs_id | Code | Section | Question | Borderline? |
|---|---|---|---|---|
| 409 | `T7.3.1` | T7 — Evidential and Methodological Foundation | Which human-science framework (psychology, moral philosophy, developmental psychology, sociology, anthropology, or other) serves as the most useful interpretive lens for this characteristic? |  |
| 410 | `T7.3.2` | T7 — Evidential and Methodological Foundation | Where the framework illuminates the verse evidence — making a finding more coherent or complete — what does it show? |  |
| 411 | `T7.3.3` | T7 — Evidential and Methodological Foundation | Where the verse evidence and the framework diverge, what does the divergence show? |  |
| 412 | `T7.3.4` | T7 — Evidential and Methodological Foundation | Does the framework surface any aspect of the characteristic the verse evidence has not yet addressed, and does that absence call for further verse investigation? |  |

## None of these (3)

| obs_id | Code | Section | Question | Borderline? |
|---|---|---|---|---|
| 220 | `WS-006` | Goodness Extensions | Does the programme's tri-registry distribution of the TOV root family (goodness as quality in R67, doing good in R65, relational pleasantness in R103) produce a coherent analytical triad for Session D, or does it create artificial boundaries that need to be addressed at synthesis? |  |
| 420 | `LEV-GEN-02` | leviticus | How does atonement work - the blood/life mechanism? | ⚠ |
| 424 | `LEV-GEN-06` | redemption | How does REDEMPTION (gaal kinsman-redeemer / padah ransom) operate, and how does it relate to atonement? | ⚠ |

