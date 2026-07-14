# WA — Thematic Exploration E4 (Preliminary): Direction and Target

**File:** WA-explore-E4-direction-target-prelim-1.0-2026-07-13.md
**Date:** 2026-07-13
**Version:** 1.0 (PRELIMINARY — scope declared in §1)
**Author:** le Roux Cilliers
**Corpus:** `psalms_story_combined.md` (sha1 `9ede65e2…`; 2,048 sections, 46 themes)
**Prior outputs:** `WA-explore-inner-seat-heart-soul-spirit-1.0-2026-07-13.md`; `WA-explore-other-uncategorised-1.0-2026-07-13.md`; `WA-session-log-corpus-and-E1-1.0-2026-07-13.md`

---

## 0. A correction to my own prior claim — issued first, because it changes the method

In the session log (§C.4) I stated that the corpus contains **"at least three distinct generations of story."** I inferred that from two data points. **It is wrong, and it understated the problem.**

A marker-coverage map was run across **all 46 themes, all 2,048 sections**. The result:

| Template marker | `inner-seat-heart-soul-spirit` | **All 45 other themes** |
|---|---|---|
| *"Its reach is …"* (the direction/target field) | 75% | **0%** |
| *"does not reach out to anything beyond itself"* | 24% | **0%** |
| *"The … is caught up in this"* (seat slot) | 83% | **0%** |
| Declared-silence closer | 100% | **0%** |
| External-dependency marker | 4% | **0%** |
| Transliteration (*nefesh*, *leb*, *ruach*, *basar*) | 64% | **0%** |

**Not three generations. Two — and radically lopsided.** Exactly **one theme** (167 sections, 8% of the corpus) was written to a structured template with explicit fields. The other **45 themes (1,881 sections, 92%)** are free prose carrying **no fields at all**. Within `inner-seat` there is a further sub-split: 64% carry a transliteration, 36% do not.

**The methodological consequence for E4 is immediate and non-negotiable.** There is **no direction field, anywhere, in 92% of the corpus.** E4 cannot be run as a query, a count, or an extraction. It can only be run by **reading**. Any attempt to count direction mechanically across the free-prose themes would be measuring my own regex, not the Psalms — a mistake I nearly made earlier in this session and disowned then.

**This correction also generalises.** The error was not the estimate itself; it was extrapolating a corpus-wide structural claim from two themes without running the cheap check that settles it. The check took one command.

---

## 1. Scope of this preliminary — stated plainly

**Read exhaustively, every section individually:**

| Theme | Sections |
|---|---|
| `inner-seat-heart-soul-spirit` (E1) | 167 |
| `other-uncategorised` | 55 |
| `seeking-inquiring` | 35 |
| `lifting-bearing` | 21 |
| `being-heard-listening` | 20 |
| **Total read** | **298 of 2,048 (14.6%)** |

The three new themes were chosen because each names a movement that is **intrinsically directed** — you seek *something*, you lift *toward* something, you listen *to* someone. If direction is doing analytical work anywhere, it will be visible there. They are not a random sample and are not offered as one.

**Not read: 1,750 sections across 41 themes.** Everything below is provisional on that.

---

## 2. Observation — direction is the corpus's own discriminator, and it says so

### 2.1 `seeking-inquiring`: the same verb, opposite objects, in the same psalm

The corpus does not merely record that seeking has different objects. It **marks the opposition explicitly**:

- Seeking **God**: *"those who seek the Lord lack no good thing"* `[seeking-inquiring | Psa 34:1-22 | #1]`; *"you who seek God, let your hearts revive"* `[Psa 69:26-32 | #1]`; *"With my whole heart I seek you"* `[Psa 119:1-18 | #1]`.
- Seeking **a life, to end it**: *"Ruthless men seek my life"* `[Psa 54:1-7 | #1]`, `[Psa 86:9-17 | #1]`; *"those who seek to destroy my life"* `[Psa 63:1-11 | #2]`.
- **And the corpus itself sets them against each other:** *"it is set deliberately against the psalmist's own seeking of God at the psalm's opening. He reaches for God; they reach for his ruin… the dark twin of devotion"* `[Psa 63:1-11 | #2]`. And again: *"In the very same psalm it stands opposite the enemies who seek his life: one seeking leads to gladness, the other to shame"* `[Psa 70:1-5 | #2]`.

**One verb. One psalm. Two objects. Opposite outcomes.** The movement is identical; only the target differs.

### 2.2 `lifting-bearing`: the corpus states the principle outright

This theme does not leave it to inference. It **articulates the rule**:

- *"The same rising motion that is beautiful when the soul reaches up to God becomes pride when it reaches up for itself"* `[lifting-bearing | Psa 131:1-3 | #1]`.
- *"there is a quiet irony in it: lifting the eyes is a beautiful thing when it looks up to God for help, but the same lifting becomes proud ambition when it strains after greatness beyond one's place"* `[Psa 131:1-3 | #2]`.

That is the clearest statement in anything I have read that **the inner movement is not intrinsically good or evil — it takes its moral character from its object.**

The theme then works the same motion across the full range of targets:

| Direction of the lift | Section |
|---|---|
| soul lifted **to God** | `[Psa 25:1-3 \| #1]`, `[Psa 86:2-7 \| #1]`, `[Psa 143:1-12 \| #1]` |
| soul lifted **to an idol / falsehood** — and *refused* | `[Psa 24:3-10 \| #1]` |
| hands lifted **to God** | `[Psa 63:1-11 \| #1]`, `[Psa 134:1-2 \| #1]` |
| hands lifted **to God's commandments** — *"the way a worshipper reaches out to God himself"* | `[Psa 119:42-63 \| #1]` |
| eyes lifted **to God / to the hills** | `[Psa 121:1-5 \| #1]`, `[Psa 123:2-4 \| #1]` |
| horn lifted **to self** — forbidden: *"no one lifts himself up; it is God who lowers one man and raises another"* | `[Psa 75:4-10 \| #1]` |
| head lifted **by God** — *"the honest, granted kind of being lifted up — the very thing pride tries to seize for itself but never truly earns"* | `[Psa 110:1-7 \| #1]` |
| heart **not** lifted — a chosen non-movement | `[Psa 131:1-3 \| #1, #2]` |

Note `[Psa 119:42-63 | #1]` particularly: hands lifted **toward the commandments** as if toward God. An **object substitution** in which the corpus treats the substitute as legitimate — the word standing where God stands.

### 2.3 `being-heard-listening`: direction runs **both ways**, and God is on the receiving end

This is the finding I did not expect, and it may be the most consequential.

- **Human → God** (the assumed default): *"Today, if you hear his voice"* `[being-heard-listening | Psa 95:4-11 | #1]`; *"I will hear what God the LORD will speak"* `[Psa 85:1-13 | #1]`.
- **God → human, as a plea**: *"Oh, that my people would listen to me!"* — the corpus reads it as *"God's grief and love spoken together"* `[Psa 81:11-12 | #2]`; and *"If only you would listen to me!"* — *"It is God asking, almost pleading, to be listened to"* `[Psa 81:4-9 | #3]`.
- **Refusal, as a settled direction**: *"they would not listen because they would not yield"* `[Psa 81:11-12 | #1]`.
- **Human → human**: *"the ear here is turned toward a human voice teaching, not toward God speaking directly"* `[Psa 78:4-6 | #1]` — the corpus flags the redirection itself.
- **Outward emission, not reception**: *"make his praise heard"* — *"not about taking a sound in but about giving one out"* `[Psa 66:1-9 | #1]`.

**And a pair that settles the argument.** Two sections record the *same act* — deliberately stopping one's own ears — with **opposite valence, determined entirely by what is being shut out**:

- The wicked: *"like a snake that plugs its own ears so no charmer's voice can reach it… they stop their own ears on purpose, shutting out every appeal and every correction"* `[Psa 58:1-5 | #1]`.
- The righteous: *"the psalmist deliberately acts like a man who is deaf and mute — he simply will not hear their charges or answer them. This is a choice, not a disability… He holds his silence and leaves his defense to God"* `[Psa 38:1-20 | #1]`.

Same movement. Same faculty. Same deliberateness. **Opposite meaning — because the object differs.**

---

## 3. Observation — a provisional taxonomy of directions

Drawn from the 298 sections read. Offered as a working instrument, not a classification grid.

| Direction | Description | Evidence |
|---|---|---|
| **D1 — Godward** | movement aimed at God | `[seeking-inquiring \| Psa 63:1-11 \| #1]`; `[lifting-bearing \| Psa 25:1-3 \| #1]` |
| **D2 — God-originated** | the inner being as **object**: acted upon by God | E1 §4 — created, restored, redeemed, cut off, turned, given over: `[inner-seat \| Psa 23:1-6 \| #1]`, `[inner-seat \| Psa 76:7-12 \| #1]`, `[inner-seat \| Psa 81:11-12 \| #1]` |
| **D3 — Against another** | aimed at a human, to harm | `[seeking-inquiring \| Psa 54:1-7 \| #1]`; `[other \| Psa 58:1-5 \| #1]` |
| **D4 — Toward another, for good** | aimed at a human, to benefit | `[seeking-inquiring \| Psa 122:1-9 \| #1]` (Jerusalem's good); `[other \| Psa 112:1-10 \| #1]` (giving to the poor); `[other \| Psa 72:1-5 \| #2]` (defending the weak) |
| **D5 — Reflexive / self-ward** | the self acting on itself | self-address `[inner-seat \| Psa 42:1-11 \| #5]`; self-exaltation `[lifting-bearing \| Psa 75:4-10 \| #1]`; self-restraint `[lifting-bearing \| Psa 131:1-3 \| #1]` |
| **D6 — Toward a thing or abstraction** | object is neither God nor person | peace `[seeking-inquiring \| Psa 34:1-22 \| #2]`; riches `[inner-seat \| Psa 62:4-12 \| #1]`; God's word `[lifting-bearing \| Psa 119:42-63 \| #1]`; an idol `[lifting-bearing \| Psa 24:3-10 \| #1]`; Zion's rubble `[other \| Psa 102:12-16 \| #1]` |
| **D7 — Null / no object** | the movement has no target, or the target is declared absent | 41 of 167 inner-seat sections: *"does not reach out to anything beyond itself; the movement stays within"*; and the **absence of direction as itself the finding**: *"the proud man does not seek God at all"* `[seeking-inquiring \| Psa 10:1-8 \| #1]`, `[Psa 53:1-6 \| #1]`, `[Psa 119:151-176 \| #1]` |

**D2 and D7 are the two that a naïve model would miss.** D2 because it inverts the assumed agency — the inner being is frequently the thing done *to*, not the thing doing. D7 because a null object is not a gap in the record; in `[Psa 10:1-8 | #1]` and `[Psa 119:151-176 | #1]` **the absence of direction is the substance of the observation** — it is why salvation is far from the wicked.

---

## 4. Observation — direction can reverse, and reversal is a movement in its own right

- **Enemies wished into Godward seeking:** the psalmist prays their faces be filled with shame *"so that they might seek your name"* — *"even enemies are wished into seeking God, their shame the door to it"* `[seeking-inquiring | Psa 83:15-18 | #1]`.
- **Seeking compelled by judgment:** *"When God began to kill them, then they sought him"* — the corpus holds the tension open: *"the seeking looks wholehearted, yet it was the blow that produced it"* `[seeking-inquiring | Psa 78:29-35 | #1, #2]`. Direction correct; antecedent coerced.
- **The searchlight turned inward:** having judged others, *"the self turns the searchlight inward"* `[inner-seat | Psa 139:21-24 | #1]`.
- **Sorrow to joy on the same act of carrying:** the farmer bears seed out weeping and grain home shouting — *"It is the very same act of carrying — but everything inside him has changed"* `[lifting-bearing | Psa 126:5-6 | #1, #2]`.

---

## 5. Interpretation — held lightly, and it is a claim about the model

**5.1 Direction may not be one edge among nine. It may be the edge that constitutes the movement.**

The evidence for this is now considerably stronger than when `other-uncategorised` first raised it:

- The corpus **states the principle outright**, twice, in `lifting-bearing` `[Psa 131:1-3 | #1, #2]`.
- It **demonstrates it structurally** in `seeking-inquiring` — one verb, two objects, opposite outcomes, marked as opposites within a single psalm `[Psa 63:1-11 | #2]`, `[Psa 70:1-5 | #2]`.
- It **demonstrates it at the finest grain** in `being-heard-listening` — the identical deliberate act of stopping the ears, righteous in one section `[Psa 38:1-20 | #1]`, damning in another `[Psa 58:1-5 | #1]`.
- And the **28 "same word bent to opposite ends" instances** across the corpus (mapped this session; 9 in `other-uncategorised` alone) say the same thing from the lexical side — delight, judging, doing, working, steadiness, all running both ways.

If this holds across the unread 85%, the implication for the movement model is structural: **you cannot characterise a movement without its object.** Antecedent, manner, intensity and effect describe a movement; **direction determines which movement it is.** Seeking-God and seeking-a-life-to-kill are not one movement with two settings. They may be two movements sharing a verb.

**5.2 The inner being is at least as often patient as agent.** D2 is not a marginal category. Combined with E1 §4 — the seat created, restored, redeemed, cut off, turned, bowed, given over, gladdened by wine — the picture is of an interior that is **acted upon** by God, by enemies, by hard labour, by bread, by grief. A model built only on what the inner being *does* would miss half of what the corpus records.

**5.3 The corpus permits object-substitution without comment.** Hands lifted to the commandments *"the way a worshipper reaches out to God himself"* `[lifting-bearing | Psa 119:42-63 | #1]`. The word occupies the place God occupies, and the corpus does not flag it as a problem. Whether that is a theological claim in the Psalms or an artefact of the narrator is **a referral candidate**, not a finding.

---

## 6. Reflection — consequence, and where this could go wrong

**The most useful consequence.** If direction constitutes the movement, then the 46 families are cutting the corpus along the *wrong axis* — they group by verb (seeking, lifting, listening) when the verb is precisely the thing that does **not** determine what is happening. That is not an argument for re-cutting them. It is an argument that the family, as the researcher has already said, is a convenience — and it may be a convenience that actively obscures the thing being looked for. The **movement**, defined as verb-plus-object, cuts across families by construction.

**Where this could go wrong — and I want this on the record.** The three themes I read were **selected because they are directional**. Seeking, lifting and listening are transitive by nature. It would be a serious error to conclude from them that direction constitutes movement *generally*, when the sample was chosen for exactly the property being tested. The finding is real within these themes. **It is not yet a corpus finding, and I am not treating it as one.**

The honest test is a theme where direction is **not** structurally obvious — `faint-despair-languishing` (51), `shame-confusion` (24), `rest-stillness-peace` (10), `joy-gladness` (95). If direction is doing constitutive work *there*, in movements that look like states rather than acts, the claim strengthens sharply. If it is not, the claim narrows to transitive movements and stays useful but bounded.

**For different readers.** D4 — movement aimed at another human for their good — is thinly attested in what I have read (generosity, defending the poor, seeking a city's welfare). Whether that thinness is real or an artefact of my theme selection matters a great deal to any reader who comes to the Psalms looking for an ethic of neighbour-love. I cannot yet say which it is.

**On application — no conclusion drawn.** 14.6% of the corpus has been read.

---

## 7. Referral candidates

1. **Object-substitution** `[lifting-bearing | Psa 119:42-63 | #1]` — hands lifted to the commandments as to God. Theological claim, or narrator's flourish? Source-level.
2. **Compelled seeking** `[seeking-inquiring | Psa 78:29-35 | #1, #2]` — direction Godward, antecedent coerced by judgment. Is this one movement or two? A clean test of whether antecedent and direction are separable edges.
3. **The 24% "no reach" sections in `inner-seat`** — 41 sections declaring *"the movement stays within."* Is a genuinely objectless inner movement possible, or is D7 a template default? **This rests on the same template-reliability question as E1's headline finding**, and the two should be settled together.
4. **Near-identical sections across themes:** `[seeking-inquiring | Psa 63:1-11 | #1]` and `[love-devotion | Psa 63:1-11 | #1]` both carry the "same word bent" device on the same passage. Cross-theme duplication, again.

---

## 8. What this preliminary cannot deliver

- **No corpus-wide claim.** 298 of 2,048 sections read, from 5 of 46 themes, **three of them selected for the property under test.**
- **No verse-level or lemma-level binding.** As before.
- **No mechanical extraction is possible.** The direction field exists in one theme out of forty-six. E4 in full must be **read**, section by section, across 1,881 sections of free prose. There is no shortcut and I will not pretend there is one.

---

## 9. Proposed scope for E4 in full

1. **Adversarial test first** — read `faint-despair-languishing` (51), `shame-confusion` (24), `rest-stillness-peace` (10): themes where direction is *not* structurally obvious. If §5.1 survives these, it is a real finding. If it does not, it narrows honestly.
2. Then the large themes by weight: `praise-extol-sing` (167), `prayer-petition-crying-out` (103), `joy-gladness` (95), `desire-longing-appetite` (72).
3. Then the remainder.
4. **The D7 / template-reliability question (§7.3) should be settled at source before any of it**, because it determines whether "no object" is evidence or artefact.

---

## Change control

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-13 | First issue. **Preliminary.** Corrects the "three generations" claim from the session log to **two, radically lopsided** (§0). Exhaustive read of `seeking-inquiring` (35), `lifting-bearing` (21), `being-heard-listening` (20), building on E1 (167) and `other-uncategorised` (55). 298 of 2,048 sections read. |
