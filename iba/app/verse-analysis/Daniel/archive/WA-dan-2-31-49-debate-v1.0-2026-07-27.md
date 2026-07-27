# Dan 2:31-49 -- Passage Debate

**Filename:** WA-dan-2-31-49-debate.md
**Date timestamp:** 2026-07-27
**Previous outputs referenced:** base data `dan-2-31-49-verse-span-meaning.md` (100% coverage,
286/286 non-particle spans, no `[AMBIGUOUS]` spans); method `WA-passage-read-guidance-v1.2-
2026-07-27.md`; interrogative `WA-interpretation-questions-v1.0-2026-07-26.md`; immediately
adjacent prior debate `WA-dan-2-17-30-debate-v1.1-2026-07-27.md` (re-read before writing this
one, per the corrected step 2 note (f)/corpus-continuity practice).

**Version:** 1.0 (first debate for this range; written directly, not left as the auto-generated
scaffold — see `report.passage_debate` for the mechanised skeleton this fills in)
**Change-control note:** New. First application of the v1.2 read guidance (with step 2 note (f),
the presumptive-candidate rule) to Dan 2:31-49 — the dream's interpretation and its immediate
aftermath. **Dan 2:33 has no `verse` row** (the chapter's verse table runs 1-32, 34-49, skipping
33). This is not a DB/import gap: `verse` rows are populated per onboarded Strong's term (STEP's
call3, one fetch per tracked term — `iba/app/handlers/raw.py:verses_one`), not by ingesting a
book wholesale, so a verse containing none of the terms onboarded so far simply has no row yet.
Noted in the insufficiencies register as a study-coverage boundary, not a data-quality problem.

---

## Preliminaries

**Working scope (declared as assumption, unchanged from prior debates).** An operation bears on
the inner being when the text or span-data names or denotes an *interior* dimension of a human —
state, faculty, disposition, affect, or volition — or a movement whose stated source or target is
such an interior dimension. Per step 2 note (f): every human mentioned — including a not-yet-
named future collective (2:39, 2:41-43) — is a presumptive candidate; a candidate that resolves
to nothing is recorded as an explicit silence, not omitted. Per step 2 note (d): verses whose
content is *only* non-human (metals, an image, a kingdom-as-institution) and not related to a
human within that clause are set aside — applied directly below at 2:32-33, 2:35, 2:39-40,
without minting a new fork for each (the corrected practice from the 2:17-30 revision).

**Reading rule applied.** No `[AMBIGUOUS]` spans in this range; not exercised.

**Corpus-continuity check.** `WA-dan-2-17-30-debate-v1.1` re-read in full before writing this
debate. Three threads from it bear directly on this range and are carried forward (not merged as
a shared log, per researcher direction — noted here only as continuity, not as an EQ merge):
(i) Dan 2:1's insufficiency #1 ("the content of the dream is not given") — **closed at 2:31-45**,
below; (ii) the passage-level fork (Dan 1:2: does divine sourcing reach only outcome/circumstance,
or also disposition?) — 2:37-38 is the single richest data point for this fork anywhere in the
corpus, addressed in full below; (iii) EQ-8 (content-sourcing vs. disposition-sourcing) — 2:37-38
bears on it as a data point, filed against this passage's own log, not resolved here.

---

## Dan 2:31 — the dream's content, finally given

> "You saw, O king, and behold, a great image. This image, mighty and of exceeding brightness, stood before you, and its appearance was frightening.

**Observation.** Daniel narrates the dream back to the king: "you saw" (H2370, *chazah* — to
see, behold, **to behold in a dream or vision**) "a great image" (H6755, *tselem*); its
appearance "was frightening" (H1763, *dechal* — to fear; Pael: to cause to be afraid; participle:
terrible).

**Operation 1 — the dream's content, disclosed (closes a standing insufficiency).**
- **Subject:** n/a — this is content, not an operation on a person in its own right.
- **Q7 (major linkage, not a fresh operation):** `WA-dan-2-1-16-debate` explicitly named, as
  insufficiency #1, that "the extract... does not give the dream's content; so *what* about the
  dream troubled the *ruach* cannot be weighed." That gap **closes here**: the content was the
  image itself, and per this verse, its own quality was *frightening*.

**Operation 2 — Nebuchadnezzar's fear-response, retrospectively explained.**
- **Subject:** Nebuchadnezzar.
- **Operation:** the image's "frightening" quality (H1763, a fear/terror lexeme) is predicated of
  the image's appearance grammatically, but the party who experienced that fright is Nebuchadnezzar
  — a re-narration, in Daniel's voice, of the very disturbance Nebuchadnezzar himself reported at
  2:1/2:3 (`WA-dan-2-1-16-debate`: "troubled... stated"). This is not a fresh interior operation so
  much as the **explanatory content** of an already-stated one — the "what" behind the "that."
- **Source:** the image's world-historical, dread-inducing character (as content of the dream);
  ultimately, per 2:28-29, God-revealed content (`WA-dan-2-17-30-debate`).
- **Target:** reflexive — Nebuchadnezzar's own prior-stated disturbance, now explained.
- **Q9:** sufficient — this verse is itself the answer to the 2:1-16 debate's named insufficiency.

**Decision.** **Retain**: this verse closes 2:1-16's insufficiency #1 (dream content). Not a new
IB operation on its own terms, but the resolution of one already on record.

---

## Dan 2:32-33 — the image's composition (32 in DB; 33 absent)

> The head of this image was of fine gold, its chest and arms of silver, its middle and thighs of bronze, [v33 not in the DB — see insufficiencies]

**Observation.** Purely descriptive: head=gold, chest/arms=silver, middle/thighs=bronze. No human
or in-scope non-human party acts or is acted upon within this verse.

**Step 2 applied directly, per note (d).** Non-human content (a symbolic image's material
composition), not related to a human within this clause. **Set aside** — not escalated to a
fork; the image *becomes* relevant to a human (Nebuchadnezzar, identified with its head) only at
2:37-38, where it is retained.

**Q9 (insufficiency, new).** **Dan 2:33 has no `verse` row** — confirmed by direct query
(`SELECT ... FROM verse WHERE osisId='Dan.2.33'` returns no row; the chapter's verse set is
1-32, 34-49). Per Part B.7, this is named, not supplied from memory or an external translation.
Not a DB defect: no term onboarded so far occurs in 2:33, so STEP's per-term verse-fetch never
had reason to pull it. Its absence means the "legs of iron, feet of iron/clay" transition between
the upper metals (32) and the feet's role in 2:34's striking is read across a gap in this
extract's *coverage*, not a gap in the text's own logic — the *narrative* is not missing anything
(2:34 refers to "feet of iron and clay" as already established), only this extract's *DB row* for
that verse doesn't exist yet, pending a future term whose onboarding happens to touch it.

**Decision.** **Set aside** as non-human/circumstantial content. **Note** the missing verse row
for the researcher — a study-coverage boundary, not a debate-writing decision, and out of scope to
fix in this pass.

---

## Dan 2:34 — the stone, explicitly not of human origin

> As you looked, a stone was cut out by no human hand, and it struck the image on its feet of iron and clay, and broke them in pieces.

**Observation.** "cut out" (H1505, *gezar* — to cut, determine; Ithpaal: to be cut out) "by no"
(H3809, *la*) "human hand" (H3028, *yad* — hand; power, fig.). "struck" (H4223, *mecha*) the
image "on its feet" (H7271, *regel*), "broke them in pieces" (H1855, *dequq* — to break into
pieces, shatter).

**Operation 1 — the stone's origin, explicitly denied to be human.**
- **Subject:** the stone (non-human) — but the verse's own content is a claim *about* human
  agency, making it in-scope per step 2 note (b): the non-human party's nature is stated *in
  direct contrast to* a human.
- **Operation:** an explicit denial of human sourcing — "by no human hand" is not silence about
  the stone's origin, it is a **stated exclusion** of human agency, textually parallel to Dan
  2:11's "the gods, whose dwelling is not with flesh" (`WA-dan-2-1-16-debate`) — both statements
  locate a decisive event's source *outside* the human, though 2:11 was a claim made by the
  Chaldeans about what *cannot* be done, while 2:34 is the narrator's own statement about what
  *was* done and by whom (not) it was done.
- **Source:** explicitly **not** a human hand. By elimination (and confirmed at 2:44-45,
  "the God of heaven will set up a kingdom"), the source is God — though this verse itself states
  only the negative (not-human), not the positive (God) directly; the positive attribution
  comes two verses later at 2:44-45. Kept distinct: this verse denies one source, 2:44-45
  supplies the other.
- **Target:** the image, "on its feet of iron and clay" — and, per 2:31-38's identification of
  the image with a succession of human kingdoms (Nebuchadnezzar as the gold head), the ultimate
  target is human dominion/kingship as an institution.
- **Q7:** directly answers, narratively, the boundary claim the Chaldeans made at Dan 2:11 (no
  one can show the king's matter "except the gods, whose dwelling is not with flesh") — the
  stone's not-by-human-hand origin is the same not-of-flesh category, now enacted rather than
  merely asserted.

**Decision.** **Retain** — a non-human-sourced operation, explicitly and deliberately excluding
human agency, targeting human kingship (the image). In scope per note (b): the non-human party
is described precisely *in relation to* what a human cannot do.

---

## Dan 2:35 — the metals scattered, the stone becomes a mountain

> Then the iron, the clay, the bronze, the silver, and the gold, all together were broken in pieces, and became like the chaff of the summer threshing floors; and the wind carried them away, so that not a trace of them could be found. But the stone that struck the image became a great mountain and filled the whole earth.

**Observation.** The metals "broken in pieces" (H1855), become "like the chaff" (H5784) that the
"wind" (H7308, *ruach* — the same lexeme rendered "spirit" at 2:1/2:3, here in its "wind" sense)
"carried... away" (H5376); "not a trace... found" (H0870 + H7912). The stone "became a great
mountain and filled the whole earth" (H4391, *mela* — to fill).

**Step 2 applied directly, per note (d).** No human party acts or is acted on within this verse;
the metals and the stone are both non-human, and the verse does not relate either to a human
within its own clauses (the relation to human kingship is established at 2:37-38 and 2:44-45,
not here). **Set aside.**

**Q9 (lexical note, not an insufficiency).** *Ruach* (H7308) here means "wind," not "spirit" —
the same root that carried Nebuchadnezzar's troubled interior at 2:1/2:3 (H7307G there) now
names the natural element that scatters the broken kingdoms. Not claimed as a deliberate
wordplay (the two are different `strong_variant` entries, and nothing in the text marks a
connection); noted only so the shared root is not silently missed nor over-read.

**Decision.** **Set aside** — non-human content, not related to a human within this verse.
Retained only as the symbolic vehicle whose *meaning* (human kingdoms) is supplied at 2:37-45.

---

## Dan 2:36 — the transition to interpretation

> "This was the dream. Now we will tell the king its interpretation.

**Observation.** "we will tell" (H0560, *amar* + H6925 *qodam* "before/to") — first-person
plural.

**Operation 1 — Daniel's (and the "we"'s) transition to interpreting.**
- **Subject:** grammatically "we" — Daniel is the sole speaker in every surrounding verse
  (2:27-30, 2:36-45), so this "we" is either a rhetorical/formal plural (Daniel speaking of
  himself), or a genuine inclusion of the three companions who prayed together at 2:17-18. The
  text does not disambiguate. Per Q8, both readings are recorded, neither imported as settled —
  the same discipline `WA-dan-2-17-30-debate` applied to 2:23's "me"/"us" shift.
- **Operation:** a movement — the narration (already given, 2:31-35) pivots to interpretation
  (2:37 onward).
- **Source:** Daniel (and possibly the three, by inclusion) — continuous with the composed,
  purposive pattern established since Dan 1:8/1:12-13 and Dan 2:16/2:24.
- **Target:** the king, as recipient of the interpretation to follow.
- **Q7:** if the wider ("we" = all four) reading is taken, this closes the collective-credit
  thread from 2:23 ("made known to **us**") into the collective's continuing role at the very
  moment of highest visibility (before the king) — a genuine but unresolved reading.

**Decision.** **Retain** as a movement-operation (transition to interpreting), with the
subject's collective-vs-individual scope recorded as an open referential question, not resolved.

---

## Dan 2:37-38 — the richest divine-sourcing statement in the corpus

> [2:37] You, O king, the king of kings, to whom the God of heaven has given the kingdom, the power, and the might, and the glory, [2:38] and into whose hand he has given, wherever they dwell, the children of man, the beasts of the field, and the birds of the heavens, making you rule over them all — you are the head of gold.

**Observation.** God "has given" (H3052, *yehav*, twice) Nebuchadnezzar "the kingdom" (H4437,
*malku*), "the power" (H2632, *shiltan* — authority, power of the king), "the might" (H8632B,
base-fallback *toqph* — strength, might), "the glory" (H3367, *yeqar* — honour, esteem); and,
"into whose hand" (H3028 + H9003), dominion "over" (H7981, *shelet* — to rule, have power) "the
children of man" (H1247I + H0606, *enash*), "the beasts of the field," and "the birds of the
heavens." Daniel then states directly: "you are the head of gold."

**Operation 1 — God's giving of kingdom/power/might/glory to Nebuchadnezzar.**
- **Subject:** God.
- **Operation:** a giving — the most extensive, explicit statement of divine sourcing directed
  at Nebuchadnezzar anywhere in the corpus so far.
- **Source:** God, explicitly and unambiguously stated ("the God of heaven has given").
- **Target:** Nebuchadnezzar — his **kingdom, power, might, and glory**. Every one of these four
  nouns names a *positional/circumstantial* attribute (rule, authority, strength-of-office,
  honour/esteem) — none names an interior disposition, character trait, or resolve. This is the
  decisive data point for the passage-level fork (Dan 1:2, restated at Dan 1:7-21/2:17-30): God's
  sourcing here is comprehensive in *scope* (everything a king could have, positionally) but
  uniform in *kind* (all outcome/circumstance, none of it disposition). This **strengthens,
  without conclusively proving** (silence is not proof of absence), the conservative reading of
  the fork over the wider one, at least as concerns Nebuchadnezzar specifically.

**Operation 2 — God's giving of dominion over creation.**
- **Subject:** God.
- **Operation:** a further giving — dominion "into whose hand" over "the children of man, the
  beasts of the field, and the birds of the heavens... making you rule over them all."
- **Source:** God, explicitly.
- **Target:** Nebuchadnezzar's rule, extended now to humanity generally ("the children of man" —
  Q8, the widest human collective addressed anywhere in this corpus) and to non-human creation.
  Again circumstantial (a scope of rule), not dispositional.
- **Q7 (bears on EQ-8, filed against `WA-dan-2-17-30-debate`, not merged here):** EQ-8 asked
  whether the text distinguishes divine sourcing of interior *content* (broader, reaching a pagan
  king, e.g. 2:28-29's revealed thoughts) from sourcing of interior *disposition* (narrower, so
  far attested only for the faithful). 2:37-38 adds a *third* category neither EQ-8 nor the
  original fork fully anticipated: divine sourcing of **circumstantial dominion** (kingdom, rule,
  scope of authority) — which, like content-sourcing, reaches Nebuchadnezzar without restriction,
  but which is not "content" in 2:28-29's cognitive sense either. Filed as a refinement for the
  whole-book read, not resolved here.

**Operation 3 — Daniel's identity-conferral: "you are the head of gold."**
- **Subject:** Daniel (speaking; relaying, per 2:28's framing, a divinely-sourced interpretation,
  not his own invention).
- **Operation:** a movement — an interpretive identification, mapping Nebuchadnezzar onto the
  image's head. Structurally comparable to Dan 1:7's renaming (an external party conferring a new
  identity-frame on a human) but categorically different: 1:7 imposed a literal new *name*;
  here Daniel confers a symbolic *self-understanding* — telling Nebuchadnezzar what/who he
  represents within a divine scheme of history.
- **Source:** Daniel, as interpreter (with God as the ultimate source of the interpretation
  itself, per 2:28).
- **Target:** Nebuchadnezzar's own self-understanding/identity — an operation on how the king is
  to understand his own place, not merely a fact stated about him.
- **Q1/Q2 (Nebuchadnezzar, receiving this):** how does the king take being told he is "the head
  of gold" — the first and greatest, but explicitly one link in a chain that inferior kingdoms
  will follow? No interior response is recorded at 2:37-38 itself; his response is deferred to
  2:46-47, where it arrives dramatically (see below). Named as a forward-pointer, not filled here.

**Decision.** **Retain** all three operations. Operations 1-2 are the single strongest data point
in the corpus for the "outcome/circumstance, not disposition" side of the passage-level fork.
Operation 3 opens a forward-pointer to 2:46-47.

---

## Dan 2:39-40 — successor kingdoms (circumstantial)

> [2:39] Another kingdom inferior to you shall arise after you, and yet a third kingdom of bronze, which shall rule over all the earth. [2:40] And there shall be a fourth kingdom, strong as iron, because iron breaks to pieces and shatters all things. And like iron that crushes, it shall break and crush all these.

**Observation.** Successive kingdoms described by material/character (bronze; iron, strong,
crushing) and by scope of rule ("over all the earth").

**Step 2 applied directly, per note (d) and note (f) together.** These verses name future human
collectives (Q8: the peoples of three successive kingdoms) only generically, by the kingdom's
institutional character, not by any human's interior. Per note (f) they are still a presumptive
candidate — but applying Q1-Q9 to "a kingdom... strong as iron... crushes" yields nothing beyond
the same circumstantial/political-character pattern already fully treated at 2:37-38 (Operation
1's finding: God's kingdom-giving is uniformly positional, never dispositional). Repeating that
finding for each successor kingdom would not surface anything new.

**Decision.** **Set aside** as a stated IB operation in its own right; **retained** only as
further instances of the same circumstance-only pattern established at 2:37-38, not re-argued
verse by verse.

---

## Dan 2:41-43 — the divided kingdom, and a human social operation within it

> [2:41] And as you saw the feet and toes, partly of potter's clay and partly of iron, it shall be a divided kingdom, but some of the firmness of iron shall be in it, just as you saw iron mixed with the soft clay. [2:42] And as the toes of the feet were partly iron and partly clay, so the kingdom shall be partly strong and partly brittle. [2:43] As you saw the iron mixed with soft clay, so they will mix with one another in marriage, but they will not hold together, just as iron does not mix with clay.

**Observation.** "mixed" (H6151, *arav*) recurs three times (metal-mixing, 2:41/2:43); at 2:43 it
is applied to humans directly: "they will mix with one another **in marriage**" (H2234, *zera* —
seed, offspring — the idiom for intermarriage/dynastic union), but "will not hold together"
(H1693, *devaq* — to cleave, cling).

**Operation 1 — a predicted human social/political operation (new candidate, per note (f)).**
- **Subject:** the rulers/peoples of the divided kingdom — a future, generic, unnamed collective
  (Q8), the most tentative subject in this range (prophesied, not yet existing).
- **Operation:** an attempted political unification through intermarriage ("mix... in marriage"),
  predicted to fail to cohere ("will not hold together"). This is squarely a human social act
  (dynastic marriage as statecraft), not merely a metallurgical metaphor left unexamined — per
  note (f), it must be carried into the interrogative rather than dismissed as "just the metal
  imagery continuing."
- **Source:** the parties themselves — their own (future, prospective) political strategy;
  self-sourced in the sense that intermarriage is something people do, not something done to
  them, though the *prophecy* of it is sourced to God via Daniel's interpretation (2:28-45).
- **Target:** each other — a mutual alliance-seeking that the text predicts will fail.
- **Q3:** the *act* (attempted unification) is stated as a future certainty ("shall be," matching
  2:44-45's "the dream is certain"); any *interior* behind the marriages (dynastic ambition,
  desire for stability) is inferred, not stated, and remains thin regardless — the text is
  interested in the outcome (non-cohesion), not the motive.
- **Q9:** insufficient to say more; this is as far as the text's own interest in this operation
  goes. Recorded, not filled further.

**Decision.** **Retain** as a thin but genuine human-social operation — checked per note (f)
rather than folded silently into the metal-imagery already set aside at 2:39-40.

---

## Dan 2:44-45 — the eternal kingdom, and Daniel's own certainty

> [2:44] And in the days of those kings the God of heaven will set up a kingdom that shall never be destroyed, nor shall the kingdom be left to another people. It shall break in pieces all these kingdoms and bring them to an end, and it shall stand forever, [2:45] just as you saw that a stone was cut from a mountain by no human hand, and that it broke in pieces the iron, the bronze, the clay, the silver, and the gold. A great God has made known to the king what shall be after this. The dream is certain, and its interpretation sure."

**Observation.** "the God of heaven will set up" (H6966I, *qum* Aphel) "a kingdom that shall
never be destroyed" (H2255, *chabal*). "A great God has made known" (H3046, *yeda* Aphel) "to the
king what shall be after this." "The dream is certain" (H3330, *yatsiv* — truth, reliable,
certain) "and its interpretation sure" (H0540, *aman* — trustworthy).

**Operation 1 — God's eternal kingdom (positive attribution completing 2:34's negative one).**
- **Subject:** God.
- **Operation:** setting up an indestructible kingdom, which will "break in pieces all these
  kingdoms" — the positive counterpart to 2:34's negative "by no human hand": that verse denied
  human sourcing; this one supplies the actual source, explicitly.
- **Source:** God, explicitly ("the God of heaven").
- **Target:** the succession of human kingdoms (2:37-43), which this kingdom ends.
- **Q7:** closes the 2:34 thread (source denied there, supplied here) and echoes 2:11's
  flesh/divine boundary claim (`WA-dan-2-1-16-debate`) — again circumstantial (a kingdom set up,
  other kingdoms ended), not a statement about any individual's disposition.

**Operation 2 — divine revelation, again, to the king (restating 2:19/2:28-29).**
- **Subject:** God.
- **Operation:** making known "what shall be after this" — the same revelatory-content operation
  already established for Nebuchadnezzar at 2:28-29 (`WA-dan-2-17-30-debate`), now reconfirmed at
  the interpretation's close.
- **Source:** God.
- **Target:** Nebuchadnezzar.

**Operation 3 — Daniel's own stated certainty (his interior, explicit).**
- **Subject:** Daniel.
- **Operation:** an epistemic/confessional state — Daniel asserts, in his own voice, that "the
  dream is certain, and its interpretation sure." This is a **stated** interior (a claimed
  certainty), not inferred, continuous with his composed, confident pattern since Dan 1:8/2:16.
- **Source:** Daniel himself, though his certainty's ultimate ground (per 2:19/2:28) is the
  revelation he received, not his own unaided judgement — the same self-effacing move he will
  make explicitly at 2:30 (`WA-dan-2-17-30-debate`, "not because of any wisdom that I have").
- **Target:** the king, as the one being assured.

**Decision.** **Retain** all three operations. Operation 3 is a clean, stated instance of
Daniel's own interior, closing his speech on the same confident note it began (2:16, 2:36).

---

## Dan 2:46 — the king falls, and worships

> Then King Nebuchadnezzar fell upon his face and paid homage to Daniel, and commanded that an offering and incense be offered up to him.

**Observation.** "fell" (H5308, *nephal*) "upon his face" (H0600, *anaph*); "paid homage" (H5457,
*seged* — to prostrate oneself, do homage, **worship**); commanded "an offering" (H4504, *minchah*
— including, per the tree, "oblation... to God") and "incense" (H5208, *nichoach* — a "soothing"
offering) be "offered up" (H5260, *nesakh* — to pour out, offer sacrifice) "to him" — to Daniel.

**Operation 1 — Nebuchadnezzar's prostration and cultic ordering, directed at Daniel.**
- **Subject:** Nebuchadnezzar.
- **Operation:** this is the single most intense embodied-interior act attributed to
  Nebuchadnezzar in the whole corpus — not merely inferred from an outward act (as at Dan 1:1's
  siege-resolve or Dan 2:25's haste), but a physical description (full prostration) paired with a
  lexeme (*seged*, "do homage, **worship**") that names the interior stance directly, the same
  way *leb* named Daniel's resolve at Dan 1:8. Per step 2 note (f), this is about as clear a
  "stated, not inferred" interior as the method distinguishes — the *content* of the reverence
  (worship, submission, terror, gratitude, or some fusion) is still not fully determinable, but
  that *some* posture of worship/reverence is present is as directly stated as the text gets.
- **Source:** the king's own reaction — to what, precisely, is a genuine referential question:
  to Daniel personally, to Daniel's God as revealed through him, or to the whole event (dream,
  interpretation, the vindication of 2:11's boundary claim) at once. The text does not
  disambiguate; all three readings are recorded, none imported as settled (Part B.2).
- **Target:** Daniel — a human being is the stated object of prostration and of a commanded
  cultic offering ("to him"). This creates a real theological tension the text itself does not
  resolve: the very next verse (2:47) has the king praising Daniel's *God*, not Daniel, as "God
  of gods" — so is 2:46's homage to Daniel a category confusion (worshipping the messenger),
  court protocol toward a newly-revealed favourite (an extreme version of ordinary royal
  homage-giving), or something the text leaves genuinely ambiguous? Surfaced as an open
  referential debate, not resolved (Part B.1-3) — no reading is imported from outside the text.

**Operation 2 — Daniel's own interior in receiving this (recorded as silence, per note (f)).**
- **Subject:** Daniel.
- **Operation:** `[not stated]` — the text gives no reaction from Daniel to being prostrated
  before and having cultic offerings ordered in his honour. Does he accept, protest, redirect the
  honour to God, or say nothing at all? Per note (f), this is exactly the kind of candidate that
  must be raised even though the verse's grammar gives Daniel no verb of his own here — the whole
  weight of the verse falls on Nebuchadnezzar's action, and Daniel's response (if any) is a
  recorded absence, not a non-question.
- **Q9:** insufficient — nothing in this range answers it. Named, not filled (Part B.4), and
  explicitly not filled from any external source (e.g. how comparable scenes resolve elsewhere in
  the corpus) — that would be importing content this document does not itself carry.

**Decision.** **Retain** Operation 1 as the corpus's clearest embodied-interior statement for
Nebuchadnezzar, with its target-ambiguity (Daniel personally vs. Daniel's God vs. the whole
event) recorded as open referential debate. **Retain** Operation 2 as an explicit recorded
silence — Daniel's reaction to being worshipped is simply absent from the text.

---

## Dan 2:47 — the king's confession, and a tension with 2:30

> The king answered and said to Daniel, "Truly, your God is God of gods and Lord of kings, and a revealer of mysteries, for you have been able to reveal this mystery."

**Observation.** "Truly" (H7187, *qoshet* — truth); "God of gods" (H0426 repeated); "Lord of
kings" (H4756, *mare*); "a revealer of mysteries" (H1541, *gelah*); "you have been able" (H3202,
*kehal*) "to reveal this mystery" (H1541 again).

**Operation 1 — the king's theological confession (stated).**
- **Subject:** Nebuchadnezzar.
- **Operation:** an explicit, first-person confession — Daniel's God named "God of gods and Lord
  of kings, and a revealer of mysteries." A **stated** interior (a confessed belief), not
  inferred, in the king's own words — the strongest theological statement placed in
  Nebuchadnezzar's own mouth anywhere in the corpus so far.
- **Source:** the king himself, as speaker — though prompted by the whole preceding sequence
  (2:1-45).
- **Target:** Daniel (addressed); the confession's content targets God.

**Operation 2 — the king's attribution of the ability to Daniel personally (tension surfaced).**
- **Subject:** Nebuchadnezzar.
- **Operation:** "**you** have been able to reveal this mystery" — the king credits the ability
  to Daniel, personally, in the very same breath as praising Daniel's God as its source. This
  sits in direct, textually-grounded tension with Dan 2:30 (`WA-dan-2-17-30-debate`), where
  Daniel himself explicitly denied that his own wisdom was the reason ("not because of any
  wisdom that I have more than all the living... in order that... the king... may know"). The
  king's confession, read strictly, re-attributes to Daniel exactly the personal credit Daniel
  had just deflected. The text does not flag this as a contradiction, correct the king, or have
  Daniel respond to it — surfaced as an unresolved tension, not smoothed over (Part B.1).
- **Source:** the king's own perception/gratitude.
- **Target:** Daniel.

**Decision.** **Retain** both operations. The tension between Operation 2 and Daniel's own 2:30
self-denial is a genuine textual observation, left open rather than harmonised.

---

## Dan 2:48 — Daniel's promotion

> Then the king gave Daniel high honors and many great gifts, and made him ruler over the whole province of Babylon and chief prefect over all the wise men of Babylon.

**Observation.** "gave" (H3052) "high honors" (H7236, *rebah* — to grow great) and "many great
gifts" (H4978); "made him ruler" (H7981) "over the whole province of Babylon" and "chief prefect"
(H5460, *cagan*) "over all the wise men of Babylon."

**Operation 1 — the king's reward.**
- **Subject:** Nebuchadnezzar.
- **Operation:** `[INFERRED]` — the reward itself (honours, gifts, rulership) is stated; the
  king's own interior driving it (gratitude, continued awe from 2:46-47, or political
  calculation in securing a proven interpreter's loyalty) is not stated, only inferred.
- **Source:** Nebuchadnezzar, continuous with 2:46-47's confessed reverence.
- **Target:** Daniel — an elevation of circumstance/status, human-to-human (distinct from the
  divine circumstantial-giving pattern of 2:37-38, though structurally similar in shape).

**Operation 2 — Daniel's own interior in receiving the promotion (recorded as silence).**
- **Subject:** Daniel.
- **Operation:** `[not stated]` — no reaction (gratitude, humility, acceptance, reluctance) is
  given. Per note (f), raised as a candidate rather than silently passed, given how carefully
  Daniel's interior has been tracked elsewhere in this same passage (2:36, 2:44-45).
- **Q7:** the specific offices given — "ruler over the whole province of Babylon," and "chief
  prefect over all the wise men of Babylon" — place Daniel over precisely the professional class
  (the *chartummim*/wise men) whose incapacity was the passage's starting boundary-claim (Dan
  2:10-11, `WA-dan-2-1-16-debate`). A pointed structural reversal: the class that said the task
  was impossible for "flesh" is now headed by the one flesh-and-blood man who did it.

**Decision.** **Retain** Operation 1 (inferred royal favour); **retain** Operation 2 as a
recorded silence.

---

## Dan 2:49 — Daniel's request for his friends

> Daniel made a request of the king, and he appointed Shadrach, Meshach, and Abednego over the affairs of the province of Babylon. But Daniel remained at the king's court.

**Observation.** "made a request" (H1156, *bĕʿah* — the same root as 2:18's "seek" and 2:23's
"asked"); the king "appointed" (H4483, *manah*) Shadrach, Meshach, and Abednego "over the affairs
of the province of Babylon." "Daniel remained" (H8651 + H9003, idiom "at the door/gate/court of
the king").

**Operation 1 — Daniel's petition on behalf of his companions.**
- **Subject:** Daniel.
- **Operation:** a request — the same interior-laden verb (*bĕʿah*, ask/seek/request/desire/
  pray) that carried the four's joint petition at 2:18 and Daniel's own thanksgiving-context at
  2:23. Here Daniel uses his newly-elevated position not for further self-advancement but to
  secure his three companions' promotion.
- **Source:** Daniel — `[INFERRED]` loyalty/solidarity toward the three who prayed with him at
  2:17-18, though not stated explicitly as his motive; well-supported by the whole passage's arc
  (they sought mercy *together*, 2:18; the answer was given to Daniel *and* "us," 2:23).
- **Target:** the king (petitioned); Shadrach, Meshach, and Abednego (the beneficiaries).
- **Q7 (closing observation, not a fresh operation):** the three are named here exclusively by
  their Babylonian names (Shadrach, Meshach, Abednego) — the imposed identity from Dan 1:7 is now
  simply how the narrative refers to them, unremarked. The renaming-operation's own interior
  question (`WA-dan-1-1-7-debate-v1.1`: the four's unstated response to being renamed) is never
  answered in words anywhere in the corpus, but this verse is the closest the text comes to a
  *behavioural* answer: whatever the four felt about the names, the narrative itself has fully
  naturalised them by this point, with no friction shown.

**Operation 2 — Daniel's own continuing status.**
- **Subject:** Daniel.
- **Operation:** a state — "remained at the king's court," closing his personal arc for this
  chapter (distinct from the three, now posted to provincial affairs).
- **Source / Target:** n/a (a status, not a movement upon another party).

**Decision.** **Retain** Operation 1 (Daniel's petition, inferred loyalty); **retain** Operation 2
as a closing status.

---

## Passage-level linkages (Q7)

1. **Dream-content thread closed (Dan 2:1 → 2:31):** the disturbance's content, left as an
   insufficiency in `WA-dan-2-1-16-debate`, is finally supplied.
2. **The flesh/divine boundary, asserted then enacted (Dan 2:11 → 2:34 → 2:44-45):** the
   Chaldeans' claim that only "gods... not with flesh" could do this is answered first narratively
   (Daniel does it, `WA-dan-2-1-16-debate`'s own forward-pointer) and now cosmologically (a stone
   "by no human hand" becomes the very kingdom that ends all human kingdoms).
3. **The passage-level fork's richest data point (Dan 1:2 → 2:37-38):** God's giving of kingdom,
   power, might, glory, and dominion to Nebuchadnezzar is comprehensive in scope and uniformly
   circumstantial in kind — bears heavily (without conclusively resolving) on the "outcome vs.
   disposition" fork first raised at Dan 1:2.
4. **Nebuchadnezzar's interior arc extended (Dan 2:1/2:3/2:5/2:8-9/2:12 → 2:29-30 → 2:46-47):**
   troubled → resolved → suspicious → furious → (cognitive content, stated) → now full
   prostration/worship and an explicit theological confession — the fullest interior arc traced
   for any figure across both chapters.
5. **The comparison-class thread, closed by reversal (Dan 1:20 → 2:27 → 2:48):** outperformed,
   then flatly disqualified, and now Daniel is placed in authority *over* that same class.
6. **A tension surfaced, not resolved (Dan 2:30 ↔ 2:47):** Daniel's self-denial of personal
   merit meets the king's attribution of personal ability in the very next scene.
7. **The renaming-operation's behavioural (non-verbal) closure (Dan 1:7 → 2:49):** the four's
   unstated response to being renamed is never given in words, but by 2:49 their Babylonian names
   are simply how the text refers to them — the closest thing to an answer the corpus provides.

---

## Insufficiencies register

1. **Dan 2:33 has no `verse` row** (the chapter's rows run 1-32, 34-49). Not an import gap: verses
   are populated per onboarded Strong's term, and no term onboarded so far occurs in 2:33 — a
   study-coverage boundary, not a data-quality problem. Noted for the researcher, not fixed here.
2. **The object of Nebuchadnezzar's worship at 2:46** — Daniel personally, Daniel's God via
   Daniel, or the whole revealed event — is not disambiguated by the text. Recorded as open
   referential debate.
3. **Daniel's own reaction to being worshipped (2:46) and to being promoted (2:48)** — both
   entirely unstated. Recorded as silence, not filled from outside the document.
4. **The "we" of 2:36** — Daniel alone, or Daniel plus the three companions — not disambiguated.

## Emergent questions log (filed against this passage only; resolved, if at all, at the
whole-book read — not merged with other passages' logs)

- **EQ-10 (new).** 2:37-38 introduces a category of divine sourcing this corpus hasn't
  distinguished yet: **circumstantial dominion** (kingdom, rule, scope of authority) as opposed
  to both interior *disposition* (favour, resolve, character — EQ-6) and interior *content*
  (revealed thoughts/visions — EQ-8). All three reach Nebuchadnezzar in some form across Dan 1-2;
  only disposition-sourcing remains unattested for him. Whether this three-way distinction
  (disposition / content / dominion) is the right taxonomy, or whether dominion is just a species
  of "enablement" already covered by Part B.5, is worth testing at the whole-book read.
- **EQ-11 (new).** 2:47's attribution of ability to Daniel personally, right after 2:30's
  self-denial, is left unresolved by the text. Does a pattern exist elsewhere (in later chapters,
  or the wider corpus) of other characters crediting Daniel personally for what he attributes to
  God? Worth watching.

## Open decisions / next steps

1. **Dan 2:33's missing `verse` row is a study-coverage boundary, not a data issue** — it will
   appear if and when a future onboarded term happens to occur in it; no action needed now.
2. **Scope fork — tracked, not a decision awaiting a ruling** (Dan 1:2; corrected 2026-07-27 per
   the researcher's direct correction — "it is not a researcher decision. It will either emerge
   from the broader study or not" — codified in `WA-interpretation-questions-v1.1` Part B.9).
   2:37-38 is now the strongest single data point on record for the narrow (outcome/circumstance-
   only) reading; carried forward like an emergent question, not settled here or by researcher
   ruling — the whole-book read is what will actually answer it, if anything does.
3. **EQ-10/EQ-11** — filed against this passage; carried to the whole-book read.
