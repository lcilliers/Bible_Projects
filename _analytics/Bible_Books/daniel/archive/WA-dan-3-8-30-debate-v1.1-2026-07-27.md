# Dan 3:8-30 -- Passage Debate (v1.1)

**Filename:** WA-dan-3-8-30-debate-v1.1-2026-07-27.md
**Date timestamp:** 2026-07-27
**Previous outputs referenced:** supersedes `WA-dan-3-8-30-debate-v1.0-2026-07-27.md` (archived);
base data `dan-3-8-30-verse-span-meaning.md` (100% coverage, 382/383 non-particle spans; the one
uncovered span is H3673 "to gather/assemble," recurring from the prior debate — no entry in STEP
itself, not a registration backlog; no `[AMBIGUOUS]` spans); method
`WA-passage-read-guidance-v1.3-2026-07-27.md`; interrogative
`WA-interpretation-questions-v1.2-2026-07-27.md`; immediately adjacent prior debate
`WA-dan-3-1-7-debate-v1.1-2026-07-27.md`; action-word survey
`action-word-surfacing-20260727.md`.

**Version:** 1.1
**Change-control note (this revision).** Researcher-directed retrofit (2026-07-27): every
operation below now carries an explicit **Action-type** label (read-guidance v1.3 step 5 note
(a); interrogative v1.2 Q11/B.10), taken from `action-word-surfacing-20260727.md`'s existing
extraction. No prior conclusion, decision, or silence-finding is changed.

**Change-control note (v1.0, retained for provenance).** This run corrected a process error from
the immediately prior session: rather than inferring what to do from instruction docs and a prior
debate's style, the config layer was queried first — `cfg_work_package`/`cfg_step` for the
registered routine (`passage-debate-report` / `report.passage_debate`), then `cfg_setting` for
its inputs — before running `VerseSpanMeaning-Report.ps1` (base extract) and
`PassageDebate-Report.ps1` (scaffold) in that order, per the routine's own documented
prerequisite. The requested range was 3:8-30, but **Dan 3:23 and Dan 3:30 have no `verse` row** —
confirmed by direct query (`verse` rows for `Dan.3.*` run 1-22, 24-29; 28 rows, not 30). This is
not a DB/import gap, corrected after the researcher's clarification: `verse` rows are populated
per onboarded Strong's term (STEP's call3, one fetch per tracked term —
`iba/app/handlers/raw.py:verses_one`), not by ingesting a book wholesale, so a verse with no term
onboarded so far simply has no row yet — the same explanation as the Dan 2:33 gap already on
record from `WA-dan-2-31-49-debate`. Noted in the insufficiencies register as a study-coverage
boundary. The scaffold and base extract were generated only for the verses that actually exist
(3:8-22, 3:24-29); this debate covers that actual range.

---

## Preliminaries

**Working scope (declared as assumption, unchanged from prior debates).** An operation bears on
the inner being when the text or span-data names or denotes an *interior* dimension of a human —
state, faculty, disposition, affect, or volition — or a movement whose stated source or target is
such an interior dimension. Per step 2 note (f): every human mentioned — the Chaldeans, the three,
Nebuchadnezzar, the soldiers, the officials, the counselors — is a presumptive candidate, even
where their act looks purely procedural (gathering, binding, confirming). A candidate that
resolves to nothing is recorded as an explicit silence, not omitted (Part B.4).

**Reading rule applied.** No `[AMBIGUOUS]` spans in this range; not exercised.

**Corpus-continuity check.** `WA-dan-3-1-7-debate.md` re-read in full before writing this debate.
Four threads from it bear directly on this range, carried forward:
(i) the open referential question (insufficiency #5, 3:1-7) — whether Shadrach, Meshach, and
Abednego fall within the eight-fold official class of 3:2-3 — is **substantially closed at 3:12**,
below;
(ii) 3:7's totalising "all the peoples, nations, and languages... fell down and worshiped," left as
an open passage-boundary tension, is **directly confronted at 3:12**'s accusation — a genuine
textual tension surfaced, not harmonised;
(iii) EQ-12 (does coerced compliance ever reveal or say anything about disposition?) is tested by
contrast: this range supplies the corpus's clearest case of principled *non*-compliance under the
identical threat, sharpening rather than resolving EQ-12;
(iv) EQ-13 (the *seged*-reversal, Dan 2:46 → 3:5-7) and EQ-14 (does the narrative evaluate
Nebuchadnezzar's use of his God-given dominion?) are both tested further below, at 3:15, 3:26, and
3:28-29.

---

## Dan 3:8-9 — the accusation is brought

> Therefore at that time certain Chaldeans came forward and maliciously accused the Jews. They
> declared to King Nebuchadnezzar, "O king, live forever!

**Observation.** "certain" (H1400, *gevar*) "Chaldeans" (H3779) "came forward" (H7127, *qerav* —
to approach, draw near) and "maliciously accused" (H7170, *qerats* — slanderous charges + H0399,
*akhal* — lit. "to eat/devour," idiom: to devour someone's pieces = to slander) "the Jews"
(H3062). They then formally address the king with the customary court greeting, "O king, live
forever" (H2418 + H5957).

**Operation 1 — the Chaldeans' hostile accusation.**

- **Action-type:** came forward, accused.
- **Subject:** "certain Chaldeans" — a named professional/ethnic class, not previously an actor in
  ch. 3 but the same class ("Chaldeans," H3779) whose collective incapacity opened the book's
  central boundary-claim at Dan 2:10-11 (`WA-dan-2-1-16-debate`), and whom Daniel was placed over
  as "chief prefect" at Dan 2:48-49.

- **Operation:** a deliberate, hostile speech-act — the *akhal*-idiom ("devour their pieces") is
  itself an interior-laden lexeme, naming malice, not mere reporting.

- **Q2 (implied interior).** What disposition motivates this accusation? `[INFERRED]`: professional
  resentment or rivalry, given the class's own prior public humiliation (2:10-11) and subsequent
  subordination to Daniel and, by extension, to men of the very group (Jewish exiles) that produced
  him. Not stated in the text; named as inference, not fact (Part B.3).

- **Source:** the Chaldeans themselves — self-sourced hostility, though its ultimate motive
  (envy, genuine legal zeal, or both) is not stated.

- **Target:** "the Jews" — here a collective ethnic/religious designation, narrowed at 3:12 to the
  three specifically (Q8: a collective label used to indict named individuals).

- **Q7 (major linkage).** Directly continues the class-reversal thread already flagged at Dan 2:48
  (`WA-dan-2-31-49-debate`, linkage 5): the class disqualified and then subordinated now moves
  against the very men (Jews) who displaced it. The clearest data point yet for that thread.

**Operation 2 — the formal court address (minimal interior content).**

- **Action-type:** "O king, live forever" (formal greeting).
- **Subject:** the Chaldeans, collectively.
- **Operation:** a ceremonial greeting formula, preceding the accusation's substance (3:10-12).
  Per note (f), traced as a candidate but yielding little beyond convention — no stated or clearly
  inferable interior beyond ordinary court protocol.

- **Decision.** **Retain** Operation 1 as a stated hostile act with inferred motive (professional
  reversal-driven resentment), linked to the Dan 2:48 thread. **Set aside** Operation 2 as
  formulaic, yielding no further interior content of its own.

---

## Dan 3:10-11 — the decree cited back to the king

> You, O king, have made a decree, that every man who hears the sound of the horn, pipe, lyre,
> trigon, harp, bagpipe, and every kind of music, shall fall down and worship the golden image.
> And whoever does not fall down and worship shall be cast into a burning fiery furnace.

**Observation.** The Chaldeans recite the king's own decree (H7761G, "made/set" a "decree" H2942)
verbatim in substance — the same instrument-list, the same *nephal* (H5308) + *seged* (H5457)
pairing, the same furnace-penalty (H7412 + H3345 + H5135 + H0861) as Dan 3:5-6.

**Operation 1 — the Chaldeans' strategic citation of the king's own law.**

- **Action-type:** cited (the king's own decree).
- **Subject:** the Chaldeans.
- **Operation:** not a fresh act in its own right so much as legal groundwork — establishing the
  decree's binding force before naming its violators. Per note (f), still a presumptive candidate:
  the choice to *quote the king's own words back to him*, rather than simply naming the charge, is
  itself a rhetorical act.

- **Q2.** `[INFERRED]`: a calculated, procedurally careful approach — building an airtight case the
  king himself cannot dispute, since it is his own law. Not stated as motive; inference only.

- **Q7.** Verbatim reuse of 3:5-6's content, word for word in substance — no new interpretive
  content of its own; the operative new content begins at 3:12.

**Decision.** **Set aside** as a citation, not a fresh IB operation — retained only as evidentiary
groundwork for 3:12's accusation, per note (f)'s discipline of still tracing it rather than
skipping silently.

---

## Dan 3:12 — the accusation's substance, and a passage-boundary tension resolved

> There are certain Jews whom you have appointed over the affairs of the province of Babylon:
> Shadrach, Meshach, and Abednego. These men, O king, pay no attention to you; they do not serve
> your gods or worship the golden image that you have set up."

**Observation.** The three are named and their office specified: "appointed" (H4483, *manah*)
"over the affairs" (H5673, *avidah*) "of the province of Babylon" (H4083 + H0895) — echoing Dan
2:49's exact phrasing. The charge: they "pay no attention to" (H7761H, idiom) the king, "do not
serve" (H6399, *pelach* — serve, worship, revere) "your gods," and do not "worship" (H5457,
*seged*) "the golden image... set up" (H6966I).

**Operation 1 — the three's non-compliance, reported by their accusers.**

- **Action-type:** (reported) non-compliance — pay no attention, do not serve/worship.
- **Subject:** Shadrach, Meshach, and Abednego — named individually in ch. 3 for the first time,
  though here characterized in the third person by opponents, not yet in their own voice (that
  comes at 3:16-18).

- **Operation:** a reported refusal — non-service, non-worship — of a decreed act.
- **Q3.** The *act* of non-compliance is stated (by the accusers, as fact); the *interior* behind
  it (fidelity, conviction, defiance) is not yet given in this verse — that arrives, in their own
  words, at 3:16-18. Named here as a forward-pointer, not filled.

- **Source:** the three themselves — a self-sourced refusal, as characterized by a hostile
  third party.

- **Target:** "your gods" and "the golden image" — the objects of refused reverence; by
  implication, the king's own authority and the decree of 3:4-6.

- **Q7 (major linkage — closes an open referential question).** `WA-dan-3-1-7-debate`'s
  insufficiency #5 asked whether the three fall within the eight-fold official class enumerated at
  3:2-3. **This verse answers it, substantially**: they are identified by an office matching Dan
  2:49's language exactly ("over the affairs of the province of Babylon") — but they are **not**
  listed among the eight ranked titles (satraps, prefects, governors, counselors, treasurers,
  justices, magistrates, officials) either here or at 3:27's parallel list. Their office is
  administratively real but textually distinct from the enumerated class.

- **Q7 (major linkage — the 3:7 tension, confronted not harmonised).** `WA-dan-3-1-7-debate` flagged
  Dan 3:7's "all the peoples, nations, and languages... fell down and worshiped" as an open
  passage-boundary tension, given the three's likely inclusion in "the province of Babylon." This
  verse **confirms the tension is real, not resolved by inclusion**: the accusation's entire
  premise is that these three did *not* comply. Two readings are recorded, neither asserted as
  settled (Part B.1-2): (a) 3:7's "all" is summary/hyperbolic narration of the general event, not a
  literal claim admitting no exception; (b) the three's exception was real and immediate, and 3:7
  narrates the mass event while remaining silent (not false) about this one dissent, surfaced only
  now because it was reported. The text itself does not disambiguate; both are held open.

**Decision.** **Retain** as the passage's evidentiary turning point. The interior behind the
refusal is a named forward-pointer (resolved at 3:16-18); the 3:7/3:12 tension is surfaced and
left open, per Part B.1, not smoothed over.

---

## Dan 3:13 — Nebuchadnezzar's fury, and a summons

> Then Nebuchadnezzar in furious rage commanded that Shadrach, Meshach, and Abednego be brought.
> So they brought these men before the king.

**Observation.** "furious" (H2528, *chemah*) "rage" (H7266, *regaz*) — a doubled rage-vocabulary,
pairing the same *chemah* used of his fury at Dan 2:12 with a second, intensifying near-synonym.
"commanded" (H0560) they "be brought" (H0858/H0858 Hophal).

**Operation 1 — Nebuchadnezzar's stated fury.**

- **Action-type:** furious, commanded (they be brought).
- **Subject:** Nebuchadnezzar.
- **Operation:** an explicit, **stated** (not inferred) interior state — anger — continuing a
  documented pattern: furious at the wise men's incapacity (Dan 2:12, `WA-dan-2-1-16-debate`), now
  furious at three specific men's defiance. The doubled vocabulary (*chemah* + *regaz*, versus
  2:12's *chemah* alone) marks this instance as textually more intense than the earlier one.

- **Source:** the accusation just reported (3:8-12) — an explicit, stated trigger.
- **Target:** Shadrach, Meshach, and Abednego, summoned to appear.
- **Q7.** Third documented instance of Nebuchadnezzar's volatile temper (Dan 2:12 → here → 3:19
  below, each more intense) — an established characteristic, not a one-off.

**Decision.** **Retain** as a stated, escalating instance of an established characteristic.

---

## Dan 3:14 — the king's interrogation

> Nebuchadnezzar answered and said to them, "Is it true, O Shadrach, Meshach, and Abednego, that
> you do not serve my gods or worship the golden image that I have set up?

**Observation.** "Is it true" (H6656 + interrogative H9008) — a direct question, addressed to the
three by name, restating the charge from 3:12 in the king's own first person ("my gods... I have
set up").

**Operation 1 — the king's judicial questioning.**

- **Action-type:** interrogated ("is it true?").
- **Subject:** Nebuchadnezzar.
- **Operation:** a question, not (yet) a sentence — giving the accused an opportunity to confirm,
  deny, or explain.

- **Q2.** `[INFERRED]`, two readings held open, neither settled (Part B.2): (a) a genuinely
  procedural act, some measure of restraint surviving his stated fury (3:13); (b) simply reciting
  the charge before pronouncing the inevitable sentence, fury undiminished. The text gives no
  further marker either way.

- **Source:** Nebuchadnezzar, continuing from 3:13.
- **Target:** Shadrach, Meshach, and Abednego, directly addressed.

**Decision.** **Retain** as a judicial speech-act; the disposition behind it (measured vs. merely
procedural) recorded as open, not resolved.

---

## Dan 3:15 — the ultimatum, and Nebuchadnezzar's defiance

> Now if you are ready when you hear the sound of the horn, pipe, lyre, trigon, harp, bagpipe, and
> every kind of music, to fall down and worship the image that I have made, well and good. But if
> you do not worship, you shall immediately be cast into a burning fiery furnace. And who is the
> god who will deliver you out of my hands?"

**Observation.** A conditional second chance ("well and good," lit. "good") followed by the
restated penalty, and closing with a direct rhetorical challenge: "who is the god [H0426] who
will deliver [H7804] you out of my hands [H3028]?"

**Operation 1 — the offer of a second chance.**

- **Action-type:** offered (a second chance).
- **Subject:** Nebuchadnezzar.
- **Operation:** offering the three a further opportunity to comply — `[INFERRED]` some
  combination of genuine reluctance to destroy valuable, trusted administrators, and/or continued
  confidence the threat alone will secure compliance. Not stated; inference only.

- **Target:** the three.

**Operation 2 — the king's rhetorical defiance of "the god."**

- **Action-type:** "who is the god who will deliver you" (defiance).
- **Subject:** Nebuchadnezzar.
- **Operation:** an explicit, **stated** disposition — open boastful defiance, denying in advance
  that any deity could rescue the three from his power. This is the single strongest statement of
  Nebuchadnezzar's own interior pride/self-sufficiency anywhere in the corpus.

- **Source:** Nebuchadnezzar's own confidence — `[INFERRED]` as flowing from the very
  circumstantial dominion God gave him at Dan 2:37-38 (`WA-dan-2-31-49-debate`), though the verse
  itself does not draw that connection; named as inference, testing EQ-14 (does the narrative ever
  evaluate how that dominion is used?).

- **Target:** "the god" — generically phrased, but in context aimed at whichever deity the three
  serve.

- **Q7 (major linkage).** This is the corpus's sharpest reversal yet of Nebuchadnezzar's own
  2:46-47 confession ("your God is God of gods and Lord of kings... a revealer of mysteries"). The
  same man who prostrated and confessed now rhetorically denies any god's power over him. Also
  echoes, in an inverted register, the Chaldeans' own boundary-claim at Dan 2:11 ("the gods, whose
  dwelling is not with flesh, [can do this]") — there the claim excluded human capacity in favour
  of the divine; here the king's claim excludes divine capacity in favour of his own. Both
  instances are answered by subsequent narrative events (2:34/2:44-45 for the first; 3:24-28
  below for the second).

**Decision.** **Retain** both operations. Operation 2 is flagged as the passage's peak statement of
Nebuchadnezzar's pride, set up for direct reversal at 3:28.

---

## Dan 3:16-18 — the three's reply: stated resolve, unconditioned by outcome

> Shadrach, Meshach, and Abednego answered and said to the king, "O Nebuchadnezzar, we have no need
> to answer you in this matter. If this be so, our God whom we serve is able to deliver us from the
> burning fiery furnace, and he will deliver us out of your hand, O king. But if not, be it known to
> you, O king, that we will not serve your gods or worship the golden image that you have set up."

**Observation.** "we have no need" (H2818A, *khashach*) "to answer" (H8421I) — a refusal to
plead their case. "our God whom we serve" (H6399, *pelach*, the same lexeme the accusation used
at 3:12) "is able" (H3202, *yekhal*) "to deliver" (H7804, *shezav*). "But if not" (H2006A + H9002)
— an explicit conditional — "we will not serve... or worship" (H6399, H5457).

**Operation 1 — a stated refusal to plead, itself a disposition.**

- **Action-type:** declined to answer/plead.
- **Subject:** the three, addressed collectively but speaking with one voice (Q8: a small,
  named collective, unlike the anonymous mass collectives elsewhere in this book).

- **Operation:** declining to defend themselves — a stated posture of composed resolve, not fear
  or negotiation.

- **Q7.** Structurally comparable to Daniel's own composed confidence before the king at Dan 1:8,
  2:16, 2:27 (`WA-dan-2-1-16-debate`, `WA-dan-2-17-30-debate`) — a shared characteristic across
  Daniel and the three.

**Operation 2 — stated trust in God's ability to deliver (contingent clause).**

- **Action-type:** stated trust ("our God is able to deliver us").
- **Subject:** the three.
- **Operation:** an explicitly **stated** (not inferred) interior — trust that their God is able
  to rescue them, and will.

- **Source:** "our God whom we serve" — explicitly named, not inferred.
- **Target:** the anticipated furnace and the king's own power ("out of your hand").

**Operation 3 — stated resolve to refuse, explicitly unconditioned by the outcome.**

- **Action-type:** stated resolve ("but if not, we will not serve").
- **Subject:** the three.
- **Operation:** the passage's single richest stated interior — an explicit declaration that their
  refusal to serve/worship stands **even if** God does not deliver them ("But if not..."). This
  is a **stated**, first-person disposition held distinct from, and not contingent upon, the
  *circumstantial* outcome of rescue.

- **Source:** the three's own resolve/fidelity — explicitly self-attested, though its ultimate
  ground (per 3:28 below) is God-honoured, not self-generated in isolation.

- **Target:** the king; the demanded worship, refused absolutely.
- **Q4 (the passage's clearest data point on the standing corpus-wide fork).** Part B.5 requires
  source-of-state and source-of-enablement be kept distinct; this passage supplies the cleanest
  possible separation of *disposition* from *circumstance* anywhere in the corpus: the three's
  fidelity (disposition) is explicitly held constant regardless of whether God's rescue
  (circumstance) occurs. This bears directly, and with unusual textual clarity, on the fork
  tracked since Dan 1:2 (does divine/human sourcing reach disposition or only circumstance?) —
  here inverted to the human side: a human disposition is shown, in the text's own words, as
  *not* contingent on a favourable circumstantial outcome. Tracked per B.9, not resolved here, but
  this is flagged as the single strongest data point the corpus has produced on this question so
  far.

**Decision.** **Retain** all three operations. Operation 3 is the passage's central finding —
carried forward as the corpus's clearest disposition/circumstance data point.

---

## Dan 3:19 — fury intensified, and a lexical note

> Then Nebuchadnezzar was filled with fury, and the expression of his face was changed against
> Shadrach, Meshach, and Abednego. He ordered the furnace heated seven times more than it was
> usually heated.

**Observation.** "filled" (H4391) "with fury" (H2528, *chemah* — third occurrence: 2:12, 3:13,
here). "the expression" (H6755, *tselem* — **the same word rendered "image" throughout this
chapter**) "of his face... changed" (H8133).

**Operation 1 — Nebuchadnezzar's fury, now at its peak.**

- **Action-type:** filled with fury (furnace heated 7x).
- **Subject:** Nebuchadnezzar.
- **Operation:** a third, most intense instance of the established fury-pattern, now paired with
  a physical, embodied sign (his face's *tselem* itself changing).

- **Q9 (lexical note, not an insufficiency, paralleling the *ruach*-note at Dan 2:35).** The word
  for the "expression" of Nebuchadnezzar's face is H6755, *tselem* — the identical lexeme used for
  the golden "image" throughout this chapter (3:1, 3:2, 3:3, 3:5, 3:7, 3:10, 3:12, 3:14, 3:15,
  3:18). The king's own face becomes, lexically, an "image" that is altered by rage, at the exact
  narrative moment his golden *tselem* is being defied. Not claimed as deliberate wordplay — the
  `strong_variant` entries are simply the ordinary lexical range of one root — but flagged so the
  shared root is not silently missed.

- **Q7.** The instruction to heat the furnace seven times hotter than usual exceeds any practical
  requirement for execution — evidence of the *intensity* of the disposition (rage exceeding
  rational bounds) rather than of any additional stated interior content.

**Decision.** **Retain** as the peak instance of the fury-pattern; lexical note on *tselem*
recorded, not over-read.

---

## Dan 3:20-21 — binding and casting in

> And he ordered some of the mighty men of his army to bind Shadrach, Meshach, and Abednego, and to
> cast them into the burning fiery furnace. Then these men were bound in their cloaks, their
> tunics, their hats, and their other garments, and they were thrown into the burning fiery
> furnace.

**Observation.** "mighty men" (H2429 + H1401) of the army "bind" (H3729) and "cast" (H7412) the
three, fully clothed, into the furnace.

**Operation 1 — the soldiers' compliant execution of the order (recorded as silence).**

- **Action-type:** bind, cast in.
- **Subject:** "the mighty men of his army" — a new human candidate, per note (f).
- **Operation:** compliance with a lethal order.
- **Q2/Q3.** Their own interior (duty, reluctance, indifference) is `[not stated]` — recorded as
  silence, consistent with the earlier officials' unstated compliance at Dan 3:2-3.

- **Source:** the king's command.
- **Target:** the three.

**Operation 2 — the three's own interior at the moment of being bound and cast in (recorded as
silence, forward-pointer).**

- **Action-type:** (bound, cast in) — acted upon, not acting.
- **Subject:** Shadrach, Meshach, and Abednego.
- **Operation:** `[not stated]` — the text gives their stated resolve (3:16-18) before this moment
  and their vindicated preservation after it (3:25-27), but not their interior *during* it (fear,
  continued composure, prayer). Per note (f), named as a candidate despite the verse's silence,
  with a forward-pointer to 3:25's outcome.

**Decision.** **Retain** Operation 1 as a recorded silence. **Retain** Operation 2 as a recorded
silence with an explicit forward-pointer — the gap between stated resolve and stated outcome is
itself worth naming, not passed over.

---

## Dan 3:22 — the soldiers' deaths, an asymmetry in the narrative's attention

> Because the king's order was urgent and the furnace overheated, the flame of the fire killed
> those men who took up Shadrach, Meshach, and Abednego.

**Observation.** "urgent" (H2685, *chatsaph*) order; the furnace "overheated" (H3493 + H0228);
"killed" (H6992, *qetal*) "those men who took up" (H5267) the three.

**Operation 1 — the soldiers' deaths, a side-effect of the furnace's excess.**

- **Action-type:** (killed by the flame) — acted upon, not acting.
- **Subject:** the soldiers who cast the three in.
- **Operation:** death by the very fire meant for the three — a fatal consequence of 3:19's
  excessive (sevenfold) heating.

- **Q9 (an emergent question, not filled from outside the text).** The narrative states the
  soldiers' deaths factually, with no stated interior for them (fear, resignation) and — notably —
  no further narrative interest in them at all; contrast the sustained attention given to the
  three's preservation across 3:24-27. This asymmetry is observed, not evaluated: the text simply
  does not comment on it. Named as a candidate for the whole-book read (below), not resolved here.

- **Source:** the furnace's own excess, itself sourced to Nebuchadnezzar's rage-driven order
  (3:19) — a genuine collateral consequence of the king's stated fury.

- **Target:** the soldiers, incidentally.

**Decision.** **Retain** as a recorded fact with an explicit narrative asymmetry (soldiers'
deaths vs. the three's preservation) flagged as an emergent question, not resolved.

---

## [Dan 3:23 — no `verse` row]

Confirmed by direct query: `verse` rows for `Dan.3.*` run 1-22, then 24-29 — no row for
`Dan.3.23`. Not a DB/import gap: `verse` rows are populated per onboarded Strong's term (STEP's
call3), not by ingesting a book wholesale — no term onboarded so far occurs in 3:23, so it has no
row yet, the same explanation as the Dan 2:33 gap already on record for `WA-dan-2-31-49-debate`.
A study-coverage boundary, noted in the insufficiencies register below.

---

## Dan 3:24 — Nebuchadnezzar's astonishment

> Then King Nebuchadnezzar was astonished and rose up in haste. He declared to his counselors, "Did
> we not cast three men bound into the fire?" They answered and said to the king, "True, O king."

**Observation.** "astonished" (H8429, *tevah* — be startled, alarmed) "rose up in haste" (H6966G +
H0927, *behal* — dismay, hurry). He addresses "his counselors" (H1907, *hadabar* — a term distinct
from the eight-fold class of 3:2-3/3:27).

**Operation 1 — Nebuchadnezzar's stated astonishment, a turning point.**

- **Action-type:** astonished, rose in haste.
- **Subject:** Nebuchadnezzar.
- **Operation:** an explicit, **stated** interior — alarm/astonishment, sharply displacing the
  rage/defiance of 3:13-19. A third documented instance of Nebuchadnezzar being visibly shaken
  (Dan 2:1/2:3's troubled *ruach*; Dan 2:46's prostration; here), each triggered differently
  (a dream; Daniel's interpretation vindicated; now an inexplicable sight).

- **Source:** what he sees in the furnace (made explicit at 3:25) — the immediate trigger.
- **Target:** n/a (a state, not yet a movement upon another party); his subsequent address to the
  counselors is a separate act.

**Operation 2 — the counselors' confirmation (recorded as silence on their own interior).**

- **Action-type:** confirmed ("True, O king").
- **Subject:** "his counselors" (H1907) — a new/renamed advisory group, distinct from the eight-fold
  official class.

- **Operation:** a factual confirmation ("True, O king") — their own interior (alarm, disbelief)
  is `[not stated]`, recorded as silence, consistent with the pattern of unstated official reaction
  established at 3:3 and continued at 3:27 below.

**Decision.** **Retain** Operation 1 as a stated turning-point interior. **Retain** Operation 2 as
a recorded silence.

---

## Dan 3:25 — the fourth figure, and Nebuchadnezzar's own theological language

> He answered and said, "But I see four men unbound, walking in the midst of the fire, and they are
> not hurt; and the appearance of the fourth is like a son of the gods."

**Observation.** "I see" (H2370, *chazah* — the same lexeme used of Daniel's dream-visions) "four
men unbound" (H8271), "walking" (H1981) "unhurt" (H2257). "the appearance... of the fourth is like
a son of the gods" (H1821 "be like" + H1247I "son-of" + H0426 "gods").

**Operation 1 — Nebuchadnezzar's own perception and unprompted theological characterization.**

- **Action-type:** sees, names ("like a son of the gods").
- **Subject:** Nebuchadnezzar.
- **Operation:** a stated perception, escalating immediately into spontaneous theological
  interpretation — "like a son of the gods." Unlike 2:47's confession (which followed Daniel's own
  interpretation being vindicated), this theological language is Nebuchadnezzar's own, unprompted
  by any human interpreter.

- **Q4 (source).** Source of the *perception* itself: his own eyes, stated directly ("I see").
  Source of the *interpretive category* ("son of the gods"): `[INFERRED]` — his own religious
  framework (a polytheistic, "sons of the gods" idiom), not yet the fuller, more specific
  confession that follows at 3:28 ("the God of Shadrach, Meshach, and Abednego"). The two are kept
  distinct: a tentative, generic theological description here, a specific, named confession later.

- **Q7.** Bears on the divine-sourcing/content fork (EQ-8, `WA-dan-2-31-49-debate`): is this
  spontaneous perception a further instance of God-given revelatory *content* reaching a pagan king
  (as at 2:28-29), now supplied without any human mediator at all? Tracked, not resolved.

**Decision.** **Retain** as a stated, unprompted theological perception — the passage's first
step in Nebuchadnezzar's reversal from 3:15's defiance toward 3:28's full confession.

---

## Dan 3:26 — the summons out, and a different mode of honour

> Then Nebuchadnezzar came near to the door of the burning fiery furnace; he declared, "Shadrach,
> Meshach, and Abednego, servants of the Most High God, come out, and come here!" Then Shadrach,
> Meshach, and Abednego came out from the fire.

**Observation.** Nebuchadnezzar "came near" (H7127) and names the three "servants" (H5649, *eved*)
"of the Most High God" (H5943, *illay*) — a stronger, more specific ascription than 3:25's generic
"son of the gods." "come out... come here" (H0858 + H5312).

**Operation 1 — Nebuchadnezzar's address, a progression in his own confession.**

- **Action-type:** summons, names ("Most High God").
- **Subject:** Nebuchadnezzar.
- **Operation:** naming the three's God directly, by a specific and elevated title ("Most High
  God"), continuing the escalation from 3:25's tentative language toward 3:28's full doxology.

- **Q7.** A different register of honour than 2:46: there, Nebuchadnezzar physically prostrated
  (*seged*) before Daniel; here, he summons the three respectfully, by name and by their God's
  title, but the text does not describe prostration. Noted as a distinct mode, not conflated with
  2:46's fuller act.

**Operation 2 — the three's emergence (recorded as silence on their own interior).**

- **Action-type:** came out (from the fire).
- **Subject:** Shadrach, Meshach, and Abednego.
- **Operation:** "came out from the fire" — their vindication, stated as bare fact; their own
  interior at this moment (relief, continued composure, gratitude) is `[not stated]`, closing the
  forward-pointer opened at 3:20-21 without filling it — the silence itself is the closing note.

**Decision.** **Retain** Operation 1 as a further step in Nebuchadnezzar's confession-arc.
**Retain** Operation 2 as a recorded silence — the three's vindication is narrated from outside,
never from within.

---

## Dan 3:27 — the officials' forensic inspection

> And the satraps, the prefects, the governors, and the king's counselors gathered together and saw
> that the fire had not had any power over the bodies of those men. The hair of their heads was not
> singed, their cloaks were not harmed, and no smell of fire had come upon them.

**Observation.** The eight-fold class (abbreviated here to four ranks + "the king's counselors,"
H1907) "gathered together" (H3673, again no STEP entry) and "saw" (H2370). Exhaustive physical
detail: hair (H8177) not singed (H2761), cloaks (H5622) not harmed (H8133), no smell (H7382) of
fire had "come upon" (H5709) them.

**Operation 1 — the officials' witnessing (recorded as silence on their own interior).**

- **Action-type:** gathered, inspected (forensic confirmation).
- **Subject:** the official class (Q8: the same collective as 3:2-3, here named with four ranks
  plus the king's counselors, not the full original eight — `[not stated]` whether this is the
  same complete body or a narrower group).

- **Operation:** forensic confirmation — the narrative's own interest is in proving the miracle's
  completeness to the reader; the officials' own interior response (astonishment, conviction,
  mere procedural duty) is `[not stated]`.

- **Q9.** Whether this witnessing produced any change of disposition in the officials — contrast
  Nebuchadnezzar's own explicit confession at 3:28 — is not addressed. Named as an open question,
  not filled from outside the text.

- **Q9 (insufficiency, carried from 3:2-3).** H3673 has no entry in STEP itself — a permanent
  source limitation, not a registration backlog — its second occurrence in the Daniel corpus so
  far.

**Decision.** **Retain** as a recorded silence — physical evidence exhaustively stated, interior
response entirely unstated, in explicit contrast to the king's own confession that immediately
follows.

---

## Dan 3:28 — the doxology, and the corpus's clearest disposition-honoured-by-God statement

> Nebuchadnezzar answered and said, "Blessed be the God of Shadrach, Meshach, and Abednego, who has
> sent his angel and delivered his servants, who trusted in him, and set aside the king's command,
> and yielded up their bodies rather than serve and worship any god except their own God.

**Observation.** "Blessed be" (H1289, *berakh*) "the God of Shadrach, Meshach, and Abednego, who
has sent his angel [H4398] and delivered [H7804] his servants, who trusted [H7365, *rechats*] in
him, and set aside [H8133] the king's command, and yielded up [H3052, *yehav*] their bodies rather
than serve and worship any god except their own God."

**Operation 1 — Nebuchadnezzar's full, explicit theological confession.**

- **Action-type:** blessed ("the God of Shadrach, Meshach, and Abednego").
- **Subject:** Nebuchadnezzar.
- **Operation:** a stated doxology — the fullest, most specific confession yet, completing the
  arc from 3:25's tentative "son of the gods" through 3:26's "Most High God" to this explicit,
  first-person blessing of "the God of Shadrach, Meshach, and Abednego."

- **Q7 (major linkage — 3:15 directly reversed).** Nebuchadnezzar's own rhetorical question at
  3:15 ("who is the god who will deliver you out of my hands?") is now answered, by himself, in
  the negative of his own former position: there is such a God, and the king was wrong.

**Operation 2 — God's rescue explicitly linked to the three's stated disposition (the passage's
central theological finding).**

- **Action-type:** delivered (rescue tied to "who trusted in him").
- **Subject:** God (per Nebuchadnezzar's own confession).
- **Operation:** a rescue ("sent his angel and delivered") explicitly grounded, in the king's own
  words, in the three's disposition — "**who trusted in him**, and set aside the king's command,
  and yielded up their bodies rather than serve." This is not circumstantial giving of the kind
  found at Dan 2:37-38 (kingdom, power, might, glory — uniformly circumstantial, per
  `WA-dan-2-31-49-debate`); here, a divine act (rescue) is directly and explicitly tied, by a
  human speaker's own testimony, to a human's interior disposition (trust, resolve).

- **Q4/Q7 (the strongest data point yet on the standing fork).** The fork tracked since Dan 1:2
  (does divine/human sourcing ever reach disposition, or only circumstance?) has, until now,
  accumulated mostly circumstantial evidence on the "circumstance-only" side (2:37-38's giving) or
  left the question open (EQ-8, EQ-10). **This verse is the first place in the corpus where a
  divine action is explicitly and directly linked, by an eyewitness's own testimony, to a human's
  prior-stated disposition** — 3:16-18's resolve, external confirmed here almost word for word
  ("trusted in him... rather than serve"). Tracked per B.9, not resolved as settled doctrine here,
  but flagged as the single clearest positive data point the corpus has produced.

- **Q7.** This is also a rare instance (Part B.1) of one human's stated confession (Nebuchadnezzar,
  here) directly and specifically corroborating another party's previously self-reported interior
  state (the three, at 3:16-18) — an unusual cross-confirmation worth noting as such.

**Decision.** **Retain** both operations as the passage's theological centre — Operation 2 flagged
explicitly for the whole-book read as the strongest data point yet on the disposition/circumstance
fork.

---

## Dan 3:29 — a decree in reverse

> Therefore I make a decree: Any people, nation, or language that speaks anything against the God
> of Shadrach, Meshach, and Abednego shall be torn limb from limb, and their houses laid in ruins,
> for there is no other god who is able to rescue in this way."

**Observation.** "I make a decree" (H7761G + H2942 — the identical construction as 3:10's "made a
decree"), addressed to "Any people, nation, or language" (H5972, H0524, H3961 — the identical
three-term formula as 3:4, 3:7, 3:29) that "speaks anything against" (H0560 + H7960) "the God of
Shadrach, Meshach, and Abednego."

**Operation 1 — Nebuchadnezzar's new decree, structurally mirroring 3:5-6 in reverse.**

- **Action-type:** decreed (protection of the true God's honour).
- **Subject:** Nebuchadnezzar.
- **Operation:** a decree, in the same legal form as 3:5-6/3:10-11 (a command + a severe penalty
  formula, addressed to the same universal "peoples, nations, languages"), but substantively
  inverted: rather than compelling worship of his own image on pain of death, he now forbids
  blasphemy against the three's God on pain of death. A precise distinction, not glossed over
  (Part B.6): this is a **prohibition of insult**, not a **command to worship** — Nebuchadnezzar
  does not decree that the empire must worship Daniel's God, only that it may not speak against
  him. A narrower, though still severe, decree.

- **Source:** Nebuchadnezzar's own authority — the same enablement/office exercised at 3:1-2 and
  3:4-6, now placed in service of a conviction opposite to the one that opened the passage.

- **Target:** "any people, nation, or language" — the identical universal addressee as 3:4-7.
- **Q7 (the passage's key structural finding).** The decree-with-death-penalty form appears twice
  in this range (3:5-6/3:10-11, and here), identical in shape, opposite in substance — the
  clearest structural mirror in the whole range, and the fullest reversal-arc traced for a single
  character across this book so far: 3:1's self-assertive gold image → 3:15's rhetorical defiance
  → 3:28's confession → 3:29's protective decree.

- **Q7 (tests EQ-14).** `WA-dan-3-1-7-debate`'s EQ-14 asked whether the narrative ever evaluates
  Nebuchadnezzar's *use* of his God-given dominion. This verse is evidence, though still not an
  explicit narratorial verdict (Part B.3): the same dominion once used to compel worship of a
  golden image is now used to protect the honour of the true God — a change in use, narrated
  without editorial comment, left for the reader (and the whole-book read) to weigh.

**Decision.** **Retain** as the passage's structural and theological close — the decree-form
reversal is the clearest finding in this range, tracked forward, not concluded, per B.9.

---

## [Dan 3:30 — no `verse` row]

The requested range was 3:8-30; confirmed by direct query, `Dan.3.30` has no `verse` row (the
chapter's verse set is 1-22, 24-29 — 28 rows total, not 30). Not a DB/import gap: no term
onboarded so far occurs in 3:30, so STEP's per-term verse-fetch never had reason to pull it — a
study-coverage boundary, not a versification note or a scope decision made in writing this
debate. The base extract and scaffold were generated only for the verses that exist, and this
debate's actual covered range is **3:8-29**.

---

## Passage-level linkages (Q7)

1. **The class-reversal thread, extended (Dan 2:48 → 3:8):** the Chaldeans, disqualified and
   subordinated to Daniel, now move against the Jewish exiles who displaced them — the clearest
   data point yet for this thread.
2. **The 3:1-7 open questions, substantially closed (Dan 2:49 → 3:12):** the three's office is
   confirmed ("over the affairs of the province of Babylon," matching 2:49 exactly) but shown
   distinct from the eight-fold enumerated class; 3:7's "all... worshiped" is confronted, not
   harmonised, by 3:12's naming of an explicit exception.
3. **Nebuchadnezzar's fury, a documented pattern (Dan 2:12 → 3:13 → 3:19):** three escalating
   instances of the same characteristic, the third paired with an embodied sign (his own *tselem*
   changing) and an excessive, non-instrumental penalty (sevenfold heat).
4. **The disposition/circumstance fork's clearest data point (Dan 1:2 → 2:37-38 → 3:16-18 →
   3:28):** the three state their fidelity as unconditioned by rescue (3:16-18); Nebuchadnezzar's
   own confession then explicitly ties God's rescue to that very disposition (3:28) — the
   strongest positive evidence yet that the standing fork's answer may lean toward "disposition is
   reached and honoured," tracked per B.9, not settled.
5. **The *seged*/confession reversal, completed (Dan 2:46-47 → 3:5-7 → 3:15 → 3:25-26 → 3:28-29):**
   worship received (2:46) → worship demanded (3:5-7) → divine power denied (3:15) → tentative
   theological language (3:25) → specific confession (3:26) → full doxology and a reversed decree
   (3:28-29). The fullest single-character reversal arc in the corpus so far.
6. **An unresolved narrative asymmetry (Dan 3:22 vs. 3:24-28):** the soldiers who die casting the
   three in receive no further narrative interest or stated interior, in sharp contrast to the
   sustained attention paid to the three's preservation — surfaced, not adjudicated.
7. **A rare cross-confirmed interior (Dan 3:16-18 → 3:28):** the three's self-reported trust is
   independently corroborated, almost verbatim, by Nebuchadnezzar's own later testimony — an
   unusual case of one human's stated interior being externally confirmed by another.

## Insufficiencies register

1. **Dan 3:23 and Dan 3:30 have no `verse` row** — confirmed by direct query; the chapter's verse
   set is 1-22, 24-29. Not an import gap: `verse` rows are populated per onboarded Strong's term,
   and no term onboarded so far occurs in either verse — the same study-coverage boundary as the
   previously-flagged Dan 2:33 gap, corrected in that debate too. No action needed.
2. **H3673 ("to gather/assemble") has no entry in STEP itself**, its second occurrence in this
   book (Dan 3:2-3, and now 3:27) — a permanent source limitation, not a registration backlog.
3. **No interior is given for the Chaldeans' precise motive (3:8), the soldiers' compliance
   (3:20-21), the counselors' confirmation (3:24), or the officials' forensic witnessing (3:27).**
   All recorded as silence, not filled.
4. **The three's own interior at the actual moment of being bound and cast into the furnace
   (3:20-21) is never narrated** — their stated resolve (3:16-18) and their vindicated
   preservation (3:25-27) bracket a genuine narrative silence at the central moment itself.
5. **Whether the officials' witnessing (3:27) produced any change of disposition in them** is not
   addressed, in explicit contrast to Nebuchadnezzar's own stated confession (3:28).

## Emergent questions log (filed against this passage only — not merged across passages, resolved if at all at the whole-book read)

- **EQ-15 (new).** The soldiers' deaths (3:22) receive no further narrative attention. Is this
  simply incidental to advancing the miracle account, or does the corpus elsewhere show a pattern
  of selective narrative attention that might bear on how "silence" should be weighted generally
  (cf. Part B.4)? Worth testing at the whole-book read.

- **EQ-16 (new, sharpens EQ-12 from `WA-dan-3-1-7-debate`).** EQ-12 asked whether coerced
  compliance ever reveals disposition. This range supplies the corpus's clearest *contrast* case:
  principled non-compliance under the identical threat. Does the existence of this contrast case
  make it *more* reasonable to read Dan 3:7's mass compliance as disposition-neutral (since a
  disposition-driven alternative was clearly available and taken by some), or does it not bear on
  that question at all? Tracked, not resolved.

- **EQ-17 (new).** Nebuchadnezzar's theological language escalates in three stages within a few
  verses (3:25 "a son of the gods" → 3:26 "the Most High God" → 3:28 "the God of Shadrach,
  Meshach, and Abednego"). Is this escalation itself significant (a tracked conversion-arc), or is
  it simply increasing narrative specificity without theological weight? Worth testing against any
  later reversion (e.g., Dan 4's later narrative, outside this range).

## Open decisions / next steps

1. **Dan 3:23 and Dan 3:30's missing `verse` rows are a study-coverage boundary, not a data
   issue** — they will appear if and when a future onboarded term happens to occur in them; no
   action needed now, consistent with how the Dan 2:33 case was corrected.
2. **The disposition/circumstance fork (Dan 1:2)** — tracked, not a researcher decision, per B.9.
   3:16-18/3:28 together are now the strongest data point on record; carried to the whole-book
   read, alongside 2:37-38's circumstantial-only counter-evidence.
3. **EQ-15/EQ-16/EQ-17** — filed against this passage; carried to the whole-book read.
4. **The next debate in this book** should pick up at Dan 3:31 (Dan 4:1 in some versification
   schemes) or wherever the book's own chapter/verse structure next continues, checking the actual
   DB verse set first (per this session's corrected practice) rather than assuming a range.
