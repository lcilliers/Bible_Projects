# Lexical-to-finding — a worked example

> Escalation #1378. Starting point: pick one real verse, pull its `verse_lexical` data exactly as
> it lives in the DB, and dissect it — what's actually there, what it can and can't tell you on its
> own, and what a genuine finding (not a restatement) would need to add. Nothing here is a
> conclusion; it's the dissection to react to.

## The example: Daniel 1:8

Chosen because it was already used as a worked example elsewhere in this session's catalogue
work, and because it happens to be a hard case, not an easy one — the inner-being word doesn't
even surface as its own English word.

> *Dan 1:8 (ESV) — But Daniel **resolved** that he would not defile himself with the king's food,
> or with the wine that he drank. Therefore he asked the chief of the eunuchs to allow him not to
> defile himself.*
>
> **Correction:** the quote originally posted here stopped after "drank" — only the first
> sentence. That's on me, not the data: the DB's `preview` field always carried the full two-
> sentence verse, and the span table below always covered all 15 positions across both sentences
> (positions 9–14 = "asked the chief of the eunuchs to allow him not to defile himself"). Truncating
> the quoted English while keeping the full span table made positions 9–11 look orphaned. Fixed —
> the quote now matches what the data actually spans.

## What `verse_lexical` actually holds for this verse

`iba.db`'s `verse` → `span` → `verse_lexical` chain, read exactly as stored (**15 spans, 25 live
`verse_lexical` rows** after filtering the version-aware `deleted` rows out — this table keeps
every prior version of a row when re-derived, so a raw unfiltered read of it shows this verse's
data *twice*: 50 rows total, 25 flagged `deleted=1` and 25 flagged `deleted=0`. Every superseded
row's content is byte-identical to its live replacement — same `strong`/`morph_code`/`role`/
`resolved_sense` — with `created_at` timestamps of `2026-08-06T19:15:05Z` (superseded) and
`2026-08-07T16:24:41Z` (live). That's a full-corpus rebuild that reproduced identical output the
next day, not a correction of anything — a small positive data point on stability, surfaced only
because the raw dump was pulled unfiltered. The raw dump is in the appendix at the end of this
document, exactly as returned from the database, so this claim can be checked rather than taken on
my word).

| pos | surface | strong | morph | role | gloss (`resolved_sense`, verbatim from STEP) |
|---|---|---|---|---|---|
| 0 | Daniel | H1840G | HNpm | content | Daniel — a prophet... (proper name) |
| 1 | **resolved** | H7760A | HVqw3ms | content | to set: make — to put, place, set, appoint... |
| 1 | **resolved** | H5921A | HR | content | upon — prep; upon, on the ground of, on account of... |
| 1 | **resolved** | **H3820A** | HNcmsc | content | **heart — inner man, mind, will, heart, understanding; inner part, midst; ... soul, heart (of man); mind, knowledge, thinking, reflection, memory; inclination, resolution, determination (of will); conscience; heart (of moral character); as seat of appetites; as seat of emotions and passions; as seat of courage** |
| 2 | that | H0834A | HTr | content | which — relative particle |
| 2 | that | H9023 | HSp3ms | function | his — 3ms possessive suffix |
| 3 | not | H3808 | HTn | content | not |
| 4 | defile | H1351 | HVti3ms | content | to defile, pollute, desecrate |
| 5 | king's | H4428G | HNcmsa | content | king |
| 5 | king's | H9009 | HTd | function | [the] — definite article |
| 6 | food | H6598 | HNcmsc | content | choice — portion of food for king, delicacies |
| 6 | food | H9003 | HR | function | in/on/with — prefix beth |
| 7 | wine | H3196 | HNcmsc | content | wine |
| 7 | wine | H9002 | HC | function | and — conjunctive vav |
| 7 | wine | H9003 | HR | function | in/on/with — prefix beth |
| 8 | drank | H4960 | HNcmsc | content | feast — feast, drink, banquet |
| 9 | asked | H1245 | HVpw3ms | content | to seek, require, desire, request |
| 9 | asked | H9023 | HSp3ms | function | his — 3ms possessive suffix |
| 10 | chief | H8269 | HNcmsc | content | ruler, prince, chief, chieftain, official |
| 10 | chief | H9006 | HR | function | from — prefix mem |
| 11 | eunuchs | H5631 | HNcmpa | content | official, eunuch |
| 11 | eunuchs | H9009 | HTd | function | [the] — definite article |
| 12 | allow | H0834A | HTr | content | which — relative particle |
| 13 | not | H3808 | HTn | content | not |
| 14 | defile himself | H1351 | HVti3ms | content | to defile, pollute, desecrate; to defile oneself |

## Finding the IB word

One span carries the inner-being word: **position 1, surface `resolved`, code_ordinal 2,
`H3820A` — leb, "heart."** It is not its own span. It shares a single combined `span` row (STEP's
own interlinear unit) with two other Strong's codes: `H7760A` ("to set/make") and `H5921A`
("upon"). All three are tagged `role=content`, `status=resolved`.

This is the whole reason it's a useful example: the English surface text never shows the word
"heart" at all. What the reader sees is one verb, "resolved." What the data shows is a three-word
Hebrew/Aramaic idiom — *set ... upon the heart* — that the translators collapsed into a single
English verb because that idiom's actual sense **is** "to resolve, to purpose, to determine." A
lexical scan that only looked for spans whose *surface* text contains an English inner-being word
would miss this verse's IB content entirely.

## Correction — "defile" was never even considered, and that's the actual finding

Researcher's challenge, verbatim: *"what about 'defile himself' — why did you decide it is not
included. why did you decide on resolved. resolve and not defile is companions — clearly showing
that not defiling is a choice."*

Honest answer: there was no principled decision. The selection above applied one silent,
unstated test — **does the word's own STEP gloss stack contain classic inner-being vocabulary
(heart, mind, will, soul, conscience...)?** `H3820A` passes that test on its face. `H1351`
("defile" — gloss: *"to defile, pollute, desecrate; to defile oneself"*) does not; its gloss reads
as ritual/behavioural, not psychological, so it was never even weighed as a candidate. That is
exactly the "IB-related vs. not, decided how?" gap this session already flagged as structurally
missing (#1378's own origin) — and this example just demonstrated it happening in real time,
inside the very document meant to dissect it.

The researcher's point is sharper than "you missed a word." **"Resolved" and "not defile" are not
two separate findings — they are one unit of meaning.** A resolve is always a resolve *about*
something; stripped of its object, "Daniel's heart engaged an act of will" says nothing a reader
could use — it names a psychological category with no content. What makes this verse a moral/
volitional finding at all is that the content of what was resolved was **not to defile himself**.
The inner-being word (`H3820A`, via the idiom) supplies the *faculty* engaged (the will); the
non-inner-being word (`H1351`, "defile") supplies the *object* that faculty was directed at. Read
apart, neither carries the finding. Read together, they do.

This means the lexical-self-containment test used above (does *this word's own gloss* carry
inner-being vocabulary) is too narrow on its own — not as an edge case, but structurally, for
every verse where an inner-being act is a verb of volition (resolve, choose, desire, refuse,
purpose) governing a clause that names what was chosen. That pattern is not rare; it may be the
normal shape a choice takes in narrative prose. A finding-generation approach scoped to single
spans/lexemes, screened only by whether *that* word's own gloss looks like inner-being vocabulary,
would systematically produce empty, content-free findings for every one of them — exactly the
"regurgitate raw data" failure #1378 exists to avoid, just arrived at by omission rather than by
printing the gloss stack verbatim.

**Revised finding**, incorporating this: *In Dan 1:8, leb (H3820A), read through the idiom "set
upon the heart," identifies the volitional/resolve sense of the inner-being faculty engaged — but
the finding is only complete with its governed clause: what was resolved was **not to defile
himself** (H1351, twice in the verse — once as the content of the resolve, once repeated as the
content of the request made of the chief eunuch). The inner-being content of this verse is not
"Daniel had an inner disposition of resolve" in the abstract; it is "Daniel's will was engaged in
choosing against ritual defilement" — a moral choice, not a bare mental state. Neither half of that
reading is available from either word's own lexical data in isolation.*

This is now the leading evidence in this document for what #1378 is actually asking: not "which
single words are inner-being words" but **how an inner-being word and its companion words
function as one reading unit** — verb-of-volition-plus-object being the concrete pattern this
example surfaced, not asserted in the abstract.

## What the raw data can tell you, and what it can't

**What it hands you directly, no interpretation required:**
- Which Strong's code is present (`H3820A`) and that it's a real content word, not a particle.
- Its grammatical form: `HNcmsc` — noun, common gender, masculine, singular, **construct** state. Construct state means this word is grammatically bound to something else in the clause (a possessive/relational chain) — it is not standing alone.
- Its full semantic range, as STEP's lexicon carries it: a stack of roughly ten distinct glosses, from "inner man" and "mind" through "seat of emotions" to "seat of courage."
- What it's grouped with at the span level: `H7760A` + `H5921A` on the same surface token.

**What none of that data states outright, because a gloss stack is a menu, not a decision:**
- *Which one* of those ten senses is actually active in this verse. "Heart" the organ, "heart" the
  seat of emotion, "heart" the conscience, and "heart" the faculty of will are all in the same
  gloss field, undifferentiated. A finding that just prints the gloss stack has not said anything
  a raw lookup couldn't already show.
- That the word's actual grammatical role here is *not* "a heart" as a free-standing noun, but the
  object of a fixed idiom. The construct-state tag is a clue toward this, not a statement of it —
  it says "bound to something," not "bound inside a resolve-idiom."

**What resolves the ambiguity, and where it comes from:**
The disambiguating evidence is the **span grouping itself** — `H7760A` ("set") + `H5921A`
("upon") + `H3820A` ("heart") combined on one surface token, translated as a single English verb.
That combination is the textual signature of the Hebrew idiom "to set (something) upon the heart,"
whose settled sense — confirmed by the translators' own collapse into "resolved" — is squarely the
*"inclination, resolution, determination (of will)"* entry in `H3820A`'s own gloss stack, not any
of the other nine. The disambiguation is traceable: it rests on the combined-span evidence plus the
translators' own lexical choice recorded in `span.surface`, not on an outside judgment call
invented for this document.

A finding built from `H3820A`'s own fields alone, then, is closer to: *"In Dan 1:8, leb (H3820A) is
read through the fixed idiom 'set upon the heart,' which the data (combined span + the STEP gloss's
own 'inclination, resolution, determination of will' entry) identifies as the volitional/resolve
sense of the term — not its emotional, moral-conscience, or physical senses, which are equally
present in the term's general semantic range but not evidenced by this verse."* That sentence is
traceable to specific fields and says something a bare field dump does not — **but it is still
incomplete**, for the reason the "Correction" section above states: it names the faculty engaged
without naming what it was engaged in. The actually complete finding is the "Revised finding" given
there, which adds `H1351` ("defile") as the resolve's necessary object.

## What each piece of data actually contributed

| Field | Role it played in reaching the finding above |
|---|---|
| `verse_lexical.strong` | Identifies which specific term is in play — the starting point, not the answer. |
| `verse_lexical.morph_code` | Construct state signals "this word is bound to something" — narrows the search for what disambiguates it, without disambiguating it itself. |
| `verse_lexical.role` | Confirms this is a real lexical item (content), not a particle to set aside. |
| `verse_lexical.resolved_sense` (the gloss stack) | Supplies the *candidate set* of possible senses — necessary, but on its own indistinguishable from any other occurrence of leb anywhere in the corpus. |
| `span.surface` | The single most useful field here — the translators' own collapse of the idiom into one English verb *is* their sense-selection, recorded as data. |
| the span-grouping itself (which Strong's codes share one span) | The structural signal that this is an idiom, not three independent words — without this, nothing here would be distinguishable from a bare noun occurrence. |
| `verse_lexical.ambiguity_note` (empty in this case) | Where populated elsewhere, this is presumably where the data itself flags "this one isn't resolvable from the fields alone" — worth checking what it actually holds on rows where it's not null. |

## Structured dissection: learn / question / watch for

Per researcher instruction: dissect the *whole* verse's lexical data on three axes. **Deliberately
held to the lexical layer** — Strong's codes, morph, role, span-grouping, recurrence within the
verse — and deliberately stopping short of verse interpretation (what Daniel's resolve means, why
he made it, what it shows theologically). That line is Phase 2 territory; this section does not
cross it, even where a question below gestures toward it.

### What can we learn from the lexical layer (all 15 spans)

- **Content vs. function is a real, mechanical filter.** 16 of the 25 live rows are `role=content`,
  9 are `role=function` (possessive suffixes, articles, prefixes, the conjunctive vav). Setting the
  function-role rows aside loses no lexical substance — it's a legitimate first pass, not a
  simplification that risks losing something.
- **Combined spans are the norm in this verse, not the exception.** 8 of the 15 spans carry more
  than one Strong's code (positions 1, 2, 5, 6, 7, 9, 10, 11); only 7 are single-code. Roughly half
  the verse's grammar runs through construct chains, prefixes, and idioms. That's a calibration
  fact worth having before treating any one combined span as specially significant — combination
  alone isn't rare enough to be a signal by itself; it's what finding a *content-diverging* gloss
  on a combined span (like "resolved") is checked against.
- **Recurrence is directly readable, no interpretation needed.** `H1351` ("defile") occurs at
  position 4 *and* position 14 — identical lemma, morph, role, status. The lexical layer hands you
  this repetition for free.
- **The same (Strong's, morph) pair can carry two different English surface glosses in one verse.**
  `H0834A` (relative particle, morph `HTr`) occurs at position 2, glossed "that," and again at
  position 12, glossed "allow" — same code, same morphology, different translator's word. The data
  shows you the collision instantly; it does not explain it.
- **Nothing in this verse is unresolved.** Every content-role row carries `status='resolved'` and
  every `ambiguity_note` is empty. That's itself worth recording — a verse where the raw material
  is clean is a structurally different case from one where the data is telling you it doesn't know.
- **The IB-relevant content, read strictly off the table:** `H3820A` (heart, inside the "resolved"
  idiom) and `H1351` (defile, twice). `H1245` ("asked," position 9) sits closer to the boundary than
  either — its own gloss stack includes "desire, demand" alongside the plainer "seek, request" —
  see below.

### What questions should be asked to tease it out

- For every **combined span**: what are its component codes, and does the translators' surface
  gloss diverge from a literal code-by-code reading? (This is what surfaced "heart" hiding inside
  "resolved" — the one test that did real work in this example.)
- For every **content-role code**: does it recur elsewhere in the same verse, and if so, do
  role/morph/gloss stay consistent across occurrences, or does something shift? (Surfaces both the
  `H1351` repetition and the `H0834A` double-gloss above.)
- Where a code's own gloss stack **straddles the inner-being boundary** — `H1245`'s "desire, demand"
  sitting inside a broader "seek/request" gloss — does *this verse's* span/morph evidence support
  the volitional sense being active, or only the plain-request sense? The lexical layer poses that
  question for "asked" in this verse; it does not answer it from the fields alone.
- Where the **same (Strong's, morph) pair is glossed two different ways** in one verse (`H0834A`),
  is that a genuine attested double-sense, or a translation-alignment artifact that shouldn't be
  used as evidence for anything until checked?
- Does **stripping every function-role span** still leave the content-role spans forming a coherent
  clause (subject/verb/object), or does removing something like the possessive suffix on "asked"
  (`H9023`, "his") lose the link that confirms Daniel — not someone else — is the one asking?

### What to watch out for

- **Construct state is not an IB-signal by itself.** Five different content words in this one verse
  carry `HNcmsc` (heart, food, wine, drank, chief) — most plainly non-IB. It says "bound to
  something," nothing more.
- **Absence from the English surface is not absence from the lexical content.** "Heart" never
  appears as English text in this verse at all. A scan gated on surface-text keyword matching would
  miss it entirely — the span/strong data is the real census, the English reading is not.
- **Repetition is cheap to detect and not self-interpreting.** Twice-stated "not defile" could be
  genuine emphasis or could be the ordinary shape of a resolve-then-request narrative pattern —
  flagging it is a lexical-layer act; deciding what it means is not.
- **A same-code/different-gloss collision (`H0834A`) is a live data-quality risk**, not just a
  curiosity — an automated rollup that treats two occurrences of one Strong's code as one piece of
  repeated evidence could be wrong here, and this is exactly the kind of thing that needs checking
  before being trusted at scale, not assumed clean because the `status` field says `resolved`.
- **The idiom-collapse in this verse was an unusually favourable case.** The next honest test is a
  verse where the IB word is a plain, non-idiomatic occurrence with no combined-span crutch — to see
  whether the lexical layer still carries enough to disambiguate a sense, or whether that case needs
  something the current fields don't carry at all.

## The discipline, applied properly: every term, same question

Researcher's correction, verbatim: *"you missed the third IB word 'ask', not because you missed
the ESV version, but because you did not read, or reread the verse-lexical data... it is almost as
if the discipline is read every lexical term in the verse, and ask what does it do vir[à-vis]
understanding the inner being."*

Accurate. The earlier passes cherry-picked the terms that already looked IB-shaped and treated the
rest as settled. `H1245` ("asked") got a passing mention in the questions list, not the same read
`H3820A` got. Below is that same read, applied to **every one of the 25 live rows**, no skipping.

| pos | code | surface-in-context | What it does for the inner-being reading, read on its own terms |
|---|---|---|---|
| 0 | H1840G | Daniel | Names *who* the inner-being subject is. Not IB content itself — the anchor everything else attaches to. |
| 1 | H7760A | resolved (1/3) | "To set/place/appoint." Not IB vocabulary by its own gloss — but it's the **operative verb** of the idiom; the act of installing something (the following two codes) into place. |
| 1 | H5921A | resolved (2/3) | "Upon." Pure structural glue binding the verb to its target. No independent contribution. |
| 1 | H3820A | resolved (3/3) | **Heart** — the IB faculty itself. Core vocabulary, already established. |
| 2 | H0834A | that | Relative particle opening the resolve-clause. Grammar, no independent IB content — but see position 12, same code. |
| 2 | H9023 | that('s) | Possessive suffix, 3ms. Confirms the resolve is *Daniel's* — entity-linking, not content. |
| 3 | H3808 | not | **Missed the first time.** Not IB-vocabulary by gloss (it has none to speak of) — but it marks the resolve as a **refusal**, not a pursuit. A vocabulary-based scan would never catch this: negation has no semantic content of its own to gloss, yet it decides what *kind* of volitional act this is. |
| 4 | H1351 | defile | Object/content of the resolve — already established as the companion term. |
| 5 | H4428G | king's | Names the source of the temptation. Not IB, but sets the **stakes**: this is royal provision being refused, not an ordinary meal. |
| 5 | H9009 | king's | Article. No contribution. |
| 6 | H6598 | food | Gloss is specifically "**choice** — portion of food for king, delicacies," not generic food. Sharpens what's being refused: not bread-and-water fare, but the king's delicacies. Companion-content, same role as "defile." |
| 6 | H9003 | food | Prefix (in/on/with). No contribution. |
| 7 | H3196 | wine | Second temptation-object, same role as food. |
| 7 | H9002 | wine | Conjunction (and). No contribution. |
| 7 | H9003 | wine | Prefix. No contribution. |
| 8 | H4960 | drank | **A genuine catch from reading the gloss rather than trusting the English.** The gloss is "**feast** — feast, drink, banquet" — this is a *noun* (a feast/banquet occasion), not the verb "drank." The English smooths it into a verb; the lexical data says the wine belongs to a royal **feast**, not a casual drink. Sharpens the social/ceremonial weight of what's refused, same direction as "king's" and "choice." |
| 9 | H1245 | asked | **The missed term.** Gloss: "to seek, require, **desire**, exact, request... to **desire**, demand... to ask, request." This sits in the same semantic family as volition/will. Read for what it does: this is the resolve **moving outward** — the inner act at position 1 doesn't stay internal, it produces Daniel *seeking* something from another person. Genuinely IB-relevant on the discipline's own terms, not merely "close to the boundary." |
| 9 | H9023 | asked('s) | Possessive suffix again — confirms Daniel is still the one acting. Entity-linking, not content. |
| 10 | H8269 | chief | Names the addressee's rank. Not IB, but stakes-context again — Daniel is petitioning someone with real authority over him, not a peer. |
| 10 | H9006 | chief | Prefix (from). No contribution. |
| 11 | H5631 | eunuchs | Names the addressee's office. Stakes-context, same role as "chief." |
| 11 | H9009 | eunuchs | Article. No contribution. |
| 12 | H0834A | allow | **Same code and morph as position 2, different English gloss.** If this really is carrying a permission-sense here (the way "allow" reads), it means the outward-seeking act at position 9 is aimed specifically at securing *legitimate permission* — the resolve is being pursued through the social structure, not around it. That reading rests on an unverified data point (the same code/morph pair glossed two different ways in one verse) — held as a flagged possibility, not asserted, per the data-quality watch-item already raised. |
| 13 | H3808 | not | Same function as position 3 — marks the *content of the request* as also a refusal-target, restating what position 3 already established rather than adding new polarity information. |
| 14 | H1351 | defile himself | Repeated object/content — same role as position 4. |

### What the full read adds, beyond what the earlier passes caught

- **A second IB-family verb** (`H1245`, "asked") showing the inner resolve produces outward,
  social-seeking behaviour — not just an internal state. This changes the shape of the finding: it
  isn't only "Daniel's will was engaged in refusing X," it's "Daniel's will engaged in refusing X,
  *and* that refusal was pursued through a specific outward act of seeking permission from
  authority" — a fuller reading than either "resolved" or "asked" gives alone.
- **Polarity (`H3808`, "not") is IB-relevant and vocabulary-blind.** No gloss-based screen would
  ever flag a negation particle as inner-being content, because it has no semantic content of its
  own — yet it is what makes this a refusal rather than a pursuit. Any mechanism that scores terms
  by whether their own gloss "looks like" inner-being vocabulary will systematically miss polarity
  every time, on every verse, not just this one.
- **Reading the gloss instead of trusting the English surface caught a second thing** beyond the
  "heart" idiom: `H4960` ("drank") is lexically a noun for a feast/banquet, not the drinking act
  itself — sharpening the social stakes of the refusal the same way "king's" and "choice" (food) do.
- **A taxonomy of roles a term can play, relative to one inner-being act, emerges from doing this
  properly** — richer than a binary "IB word / not an IB word":
  - **Core IB vocabulary** — the faculty/state itself (`heart`).
  - **Outward-enactment verb** — a second act in the same semantic family, showing the inner
    movement produce external behaviour (`asked`).
  - **Object/content** — what the IB act is directed at or against (`defile`, `food`, `wine`).
  - **Polarity/modifier** — characterizes the *kind* of act without being IB-vocabulary itself
    (`not`).
  - **Stakes/social scaffolding** — the authority, audience, or ceremony surrounding the act,
    context rather than content (`king's`, `choice`, `feast`, `chief`, `eunuchs`).
  - **Entity-linking** — confirms which person the act belongs to (`his`, the proper name).
  - **Pure grammar** — genuinely contributes nothing to the IB reading (articles, conjunctions,
    bare prepositions).

That taxonomy — not just "which single word is the IB word" — is what actually applying the
discipline to every term surfaced. Still an open question whether it holds beyond this one verse,
but it's a sharper starting shape for #1378 than "find the heart-word" was.

## Articulating a finding per taxonomy role

Not every role in the taxonomy earns the *same kind* of finding — some are the finding, some
shape it, some are structured fields rather than prose, and one earns nothing at all. Working
through each, grounded in this verse's actual instances, not in the abstract.

**1. Core IB vocabulary — `heart` (H3820A).** This is the finding itself: which faculty is
engaged, in which specific sense, on what evidence.
> *Leb* (heart, H3820A) is engaged in its volitional sense — "inclination, resolution,
> determination of will" — evidenced by the combined-span idiom "set ... upon the heart"
> (`H7760A`+`H5921A`+`H3820A`, surface "resolved"), which selects that sense out of the term's
> wider range (mind, conscience, emotion, courage) that this verse gives no evidence for.

**2. Outward-enactment verb — `asked` (H1245).** Not a separate, free-standing finding about a
different faculty — it's a *continuation* clause on the same finding: the inner act does not stay
internal.
> The resolve above is carried into outward action: Daniel *seeks/requests* (H1245 — "seek,
> desire, demand, request") permission from the chief of the eunuchs. The volitional act named in
> (1) produces a specific social petition, not merely an internal state that stops at the heart.

**3. Object/content — `defile`, `food`, `wine`.** Does not get its own finding at all — it is the
**content clause** the core finding is incomplete without. Articulated as part of (1), not
alongside it:
> ...specifically, what was resolved was **not to defile himself** with the king's food or the
> wine of his feast (`H1351`, `H4428G`+`H6598`, `H3196`+`H4960`) — the faculty-finding above is
> empty without this clause; this is not a second finding, it is (1)'s missing half.

**4. Polarity/modifier — `not` (H3808, ×2).** Also not its own finding — but it is not safely
folded into prose either, because it changes the finding's *type*, not just its wording. This
argues for a **structured field** on the finding record (e.g. `polarity: refusal`), not only a
sentence: a downstream query asking "which resolves in this corpus are refusals vs. pursuits"
needs this queryable, not buried in a paragraph.

**5. Stakes/social scaffolding — `king's`, `choice` (food), `feast` (H4960's actual sense),
`chief`, `eunuchs`.** Not IB content and not a finding on its own — but discarding it loses real
information about how costly the refusal was (royal provision, a feast occasion, a request made of
someone with real authority over Daniel). This reads as a **context annotation** on the finding,
not a finding in its own right and not silently dropped either:
> Context: the refusal is of royal, feast-grade provision; the request is made of an authority
> figure (the chief of the eunuchs), not a peer.

**6. Entity-linking — `his`, `Daniel`.** Not analytical content at all — this is **metadata**: who
the finding is about. It belongs as a field (`subject: Daniel`), the same way `verse_context_id`
or `mti_term_id` already are, not as a sentence competing with the actual content.

**7. Pure grammar — articles, conjunctions, bare prepositions.** Earns **no role**, and that's the
correct outcome, not a gap. Confirming a category is finding-inert is itself useful — it's what
keeps the eventual mechanism from manufacturing content out of function words just because every
row got looked at.

### What this suggests about the finding's actual shape

Laid out this way, positions 1–4 (heart, resolved-idiom, not, defile/food/wine) look like **one**
finding with several required parts — subject, faculty, polarity, content, evidence — not five
independent findings. Positions 9–12 (asked, chief, eunuchs, allow) look like either a second,
*linked* finding (the enactment) or an extension of the first — genuinely open which. Either way,
the shape emerging is closer to a **structured record** (subject / faculty+sense / polarity /
content / enactment / context / evidence-fields) than to a single free-text sentence per span. That
is a real design implication, not just a description exercise — flagged as such, not decided here.

## Second correction — "stakes/scaffolding" was discarded too fast

Researcher's correction, verbatim: *"your stakes/scaffolding — the other party — could have real
significance in the inner being debate (your discarding it before considering it is not right)...
Daniel's disposition toward the king, his perception that his resolve will be dishonourable towards
the king triggered the follow-up action to ask permission. This frames the whole context of the
resolve; it also drives the trigger for the decision to ask."*

This is the same mistake as the `H1245` miss, wearing a different disguise. There, the discipline
failed because the vocabulary-screen test (does the word's own gloss look psychological?) doesn't
catch a term that carries IB content through what it *does* rather than what it *names*. Here, the
same thing happened at the category level: "king," "chief," "eunuchs" got sorted into
"stakes/scaffolding = context, not content" on sight, because none of them look like inner-being
vocabulary either — without ever testing them against the programme's own working definition,
which is sitting right there in Ch.1 of the prose: inner-being characteristics are *"how a person
thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God."*
**"Relates" is one of the five named dimensions.** A term naming the other party in a relational
transaction is a direct candidate for that dimension — not context around the finding, a candidate
component of it — and it was dismissed without that test ever being run.

**Splitting the category, not just relabelling it:**

- **Relational target — `king` (H4428G) and `chief of the eunuchs` (H8269+H5631).** Daniel's
  resolve is not enacted privately; it is carried, via the outward-seeking act (`H1245`, "asked"),
  into a transaction with a specific authority figure. The king is the source of the provision being
  declined; the chief eunuch is the party actually petitioned. That the inner act engages *another
  person* at all — and does so through a request rather than unilateral action — is a structural,
  lexically-observable fact: the sequence is resolve (position 1) → outward request (position 9) →
  named addressee (positions 10–11). That much is traceable to the data.
- **Severity/quality modifiers — `choice` (delicacies, H6598) and `feast` (H4960).** These describe
  the *object's* weight, not a relational orientation — no other party is named or implied by them.
  These stay lower-order context, not promoted alongside the relational terms — but that's now a
  tested distinction, not an assumed one.

**Where the lexical-layer boundary actually sits, on this correction:** the *structural* fact — an
authority figure is named, and the resolve is pursued through a relational transaction with that
figure rather than acted on alone — is supportable from the fields (sequence + addressee + verb of
request). The *motive* the researcher's illustration proposes — that Daniel perceived unilateral
refusal as **dishonourable to the king**, and that this perception is what triggered the request —
is a plausible and well-formed reading, but it is not itself stated by any field in this table. No
gloss, morph, or span-grouping here names honour, shame, or a perception of dishonour. Holding the
line the researcher set at the start of this thread (lexical path, not full verse interpretation):
the relational *structure* belongs in the finding; the honour-motive *reading* is real analytical
work, but it is Phase 2 — it uses this Phase 1 structure as its evidence rather than being
identical to it.

**The generalizable fix, not just this instance:** the discipline cannot stop at "does this term's
own gloss look psychological." It has to test every term against the programme's own five-part
definition directly — thinks / feels / chooses / relates / orients-toward — because a term can
carry inner-being content by *what relation it establishes* without ever carrying inner-being
*vocabulary*. That's a second, independent way a term earns a role beyond the "outward-enactment"
pattern `H1245` already demonstrated — worth carrying forward as its own standing check, not
folded into the polarity/scaffolding lesson it happened to surface inside.

## Third correction — Phase 1 demoting a role means Phase 2 never sees it

Researcher, verbatim: *"the phase 2 work would never have picked it up if the phase 1 work demote
or hide it."* And: *"there is nothing in the verse that enlightens the reason, and this will
happen time and time again because the inner being operations described in the bible is not
declarative, it is discoverable — it is there, it should be there, it is not named but it is
expected."*

This corrects the taxonomy itself, not just one category's placement in it. The write-up above
still ranked roles — "core finding" at the top, "context annotation... not a finding in its own
right" for the relational-target role, language like "lower-order" for severity terms. That ranking
is the actual danger the researcher is naming: if Phase 1 records the relational-target role as a
lesser annotation — present, but deprioritized, folded into a footnote rather than a structured,
queryable field — then whatever does Phase 2's discovery work never has it in front of itself as
material to reason over. A role that Phase 1 buries is a role Phase 2 can't discover from,
regardless of how good Phase 2 turns out to be. The demotion isn't a harmless simplification; it's
a point of loss with nothing downstream that can recover it.

**The second sentence explains why this will keep happening, not just this once.** Scripture's
inner-being content is not, in general, *declared* — stated in vocabulary a lexical scan can catch.
It is *discoverable*: present in what a person does, whom they engage, in what sequence, under what
constraint — expected to be there by the shape of the narrative, without ever being named. `H4428G`
("king") and `H8269`+`H5631` ("chief of the eunuchs") never carry a word for honour, respect, or
fear anywhere in their own gloss stacks — nothing in this verse's lexical data enlightens *why*
Daniel sought permission rather than refusing outright or acting covertly. That absence is not a
gap in this particular verse's data quality; it is the expected condition of working from Scripture
this way, and the corpus will present it "time and time again," per the researcher's own framing —
not an occasional edge case to special-case around.

**What this changes, concretely, about the taxonomy:** the roles are not "important" and
"contextual" — they split instead on **what Phase 1 can assert versus what Phase 1 can only
preserve**:

- **Declared roles** — Phase 1 can name the specific sense directly, on lexical evidence (`heart`'s
  volitional sense, evidenced by the idiom; `asked`'s outward-seeking sense).
- **Structural roles** — Phase 1 cannot assert a sense or a motive, but it can and must preserve the
  *structural fact* with full fidelity: that a relational transaction occurred, with whom, in what
  sequence, under what polarity. `king`, `chief of the eunuchs`, and the polarity marker `not` all
  belong here. Undeclared is not the same as unimportant — it is very often exactly where the
  "expected but unnamed" content the researcher describes actually lives, and it is the *only*
  category positioned to carry it forward.

Both categories are first-class, equally persisted fields on the finding record — not a core
finding plus lesser annotations trailing behind it. Phase 1's job on the structural roles is
completeness, not interpretation: get the relational target, the addressee, the sequence, the
polarity onto the record intact, every time, whether or not anything in the current verse explains
them. Whether they mean what the researcher's honour/dishonour reading proposes is Phase 2's
question to ask of that preserved structure — a question it can only ask if Phase 1 handed the
structure over rather than filtering it out as background.

## Primary operation and the operation chain

Researcher's framing, verbatim: *"the primary operation is resolve[,] this lead to not defile and
triggered the ask against the backdrop of daniel's disposition (not stated but could be confirmed
from adjacent verses...). this concept of primary and other operations is well illustrated here. in
the next verse this chain would look different."*

"Relational" here is not being-to-being (the addressee work above) — it's **a chain**: one
operation producing or triggering the next, within one inner-being subject. Checking whether this
verse's own grammar supports that chain, not just asserting it:

**It does, and the data marks it specifically.** `H7760A` ("resolved") carries morph `HVqw3ms` and
`H1245` ("asked") carries `HVpw3ms` — both tagged with Hebrew narrative's **waw-consecutive**
marker (the `w`), the grammatical device that explicitly signals "and *then*, as the next event in
sequence." `H1351` ("defile"), by contrast, carries `HVti3ms` — a different stem, embedded inside
the "that... not" clause the resolve governs, not a main sequential verb at all. The morphology
itself distinguishes two tiers: **resolve** and **ask** are both flagged as main-chain narrative
operations; **not-defile** sits *inside* the first one as its content, grammatically riding along
rather than standing as an independent link. That's a real, lexical-layer basis for the chain
concept — not the same shape the researcher proposed (a three-link resolve→not-defile→ask
sequence), closer to a two-node chain (**resolve → ask**) with not-defile as node one's payload —
offered as what the data supports, not substituted silently for the researcher's own framing. Both
readings agree on the load-bearing fact: resolve *produces* ask; that's the chain, however its
nodes get counted.

**The backdrop — Daniel's disposition — is a third, distinct kind of material, and it's honestly
placed outside this verse's data.** Nothing in Dan 1:8's own span/verse_lexical rows names a
perception of defilement-risk (Leviticus) or a demonstrated courtesy toward the king. The
researcher's own framing already marks this correctly: *not stated, but confirmable from adjacent
verses* — which is a claim about the **passage**, not about this verse's lexical layer. That keeps
faith with the lexical-path discipline this whole document has been holding to: the chain (resolve
→ ask, evidenced by wayyiqtol tagging) is this verse's own data; the backdrop that would explain
*why* the chain has this particular shape is a separate, cross-verse question — real work, but a
different kind of work, requiring the neighbouring verses' own data before it's more than a
plausible hypothesis.

**The generalizable point, stated as the researcher framed it:** the chain is not a fixed template
imposed on every verse — a different verse might show a single isolated operation with no chain at
all, or a chain of different length and shape, discovered from *that* verse's own sequencing and
morphology each time, not assumed in advance. Dan 1:8 happens to illustrate a clean two-node case
because its grammar marks the sequence explicitly; that won't be true everywhere.

**Not yet done, flagged rather than assumed:** pulling Dan 1:9–16 (or wherever the passage
continues) to actually test the backdrop hypothesis against real data, rather than leaving it as an
unexamined plausibility, is a natural next step — but it's cross-verse work this document hasn't
done, and it wasn't asked for yet. Worth doing on your say-so, not started here.

## Toward a repeatable procedure — and what's still genuinely open

Researcher's own framing: still working out how this rigour becomes a **repeatable process** that
doesn't depend on live, turn-by-turn prompting to catch what a first pass misses; how it gets
**documented so a later reader can actually pick it up**; and — separately — **what Phase 2 would
even be asked to do** with what Phase 1 now produces. Not answering any of these; laying out what
this session's own trail actually supports toward each, so the thinking has something concrete to
push against.

### What's extractable as a checklist, directly from what just happened

Every correction in this document had the same shape: a test that wasn't run. That's promising —
it means the discipline is closer to an enumerable list of tests than to an unrepeatable judgment
call. Read back against the actual misses:

1. **Enumerate every live row. No pre-filtering by role or gloss before the tests below run.**
2. **Declared-vocabulary test** — does the row's own gloss carry inner-being vocabulary directly?
   (Caught `heart`.)
3. **Idiom/combined-span test** — is this row part of a multi-code span whose surface gloss
   diverges from a literal per-code reading? If so, which sense does the combination select?
   (Caught `heart`'s specific sense, via "resolved.")
4. **Outward-enactment test** — does the row's gloss carry a volitional/appetitive sense (desire,
   seek, will, choose), even where its contextual sense looks like a plain action? (This is the one
   that was skipped the first time — caught `asked` only on the second, deliberate pass.)
5. **Relational test** — does the row name or imply another party, tested against the programme's
   own "relates" dimension, not against vocabulary? (This is the one skipped *twice* — first on
   `asked`'s addressee, then again on `king`/`chief`/`eunuchs` themselves, sorted into "context"
   without the test ever running.)
6. **Polarity test** — is the row a negation or modifier attached to a declared or structural
   operation? (Caught `not` — invisible to every vocabulary-based test by design, since negation
   has no gloss content of its own.)
7. **Sequencing/chain test** — does the row's morphology carry a narrative-sequencing marker (here,
   waw-consecutive) linking it to another operation as "and then"? (Surfaced the resolve→ask chain,
   and — as a side effect — that "not defile" is content riding on resolve, not an independent
   chain link.)
8. **Inert check** — confirm, explicitly, that a row contributes nothing beyond grammar (articles,
   conjunctions, bare prepositions) — recorded as checked-and-empty, not silently skipped.

Two more things this session's own trail supports, not just the eight tests:

- **Every row's result is a structured field, not a ranked sentence.** The repeated failure mode
  wasn't missing data — the data was always there in the raw dump — it was **encoding a role as
  prose-only or as "lesser context"** before its significance had actually been tested. A
  checklist that writes a field per row, run mechanically, doesn't have that failure mode; a
  narrative summary that improvises which rows deserve a sentence does.
- **Two distinct kinds of "still open" need separate labels, not one generic flag.** This document
  now carries two different open items: the `H0834A` same-code/different-gloss collision (a
  **data-quality** question — is the underlying alignment right?) and the honour/disposition
  hypothesis (a **discovery** question — does other evidence support it?). Conflating them into one
  "flag" bucket would send both to the same downstream process, when they plausibly need different
  ones — a data-quality flag looks like #1377/DB-integrity territory; a discovery flag looks like
  Phase 2's actual job. Worth keeping them typed separately from the point they're first raised,
  not sorted out after the fact.

### What Phase 2 might be asked to do — options, not a decision

Given what Phase 1, run this way, would actually hand over — declared findings, structural/chain
fields, and two differently-typed flags — three candidate jobs for Phase 2 are visible from here,
not mutually exclusive, and none of them decided:

- **A. Re-apply the same discipline at wider aperture.** Run the identical per-term checklist
  across the rest of the passage (or every verse touching this characteristic), and see whether a
  flagged hypothesis — like the honour/disposition reading — gets corroborated by a pattern across
  that wider set. Phase 2 as *more of Phase 1*, not a different kind of work.
- **B. Targeted flag resolution.** Take each discovery-flag individually and go looking for the
  specific corroborating evidence it names — here, the Leviticus dietary-purity background and
  Daniel's demonstrated conduct toward the steward in the following verses — a surgical task list
  driven by what Phase 1 flagged, rather than a broad reread.
- **C. Characteristic-level rollup.** Take every verse's declared+structural findings for one
  characteristic (e.g. every verse touching resolve/volition) and look for patterns across the
  whole set — the sense "Phase 2" carried earlier in this session, before the chain concept
  surfaced, and a genuinely different question from either A or B.

The data-quality flag (`H0834A`) likely isn't Phase 2's job under any of these three — it reads as
a DB-integrity question closer to #1377's territory, resolved by checking the underlying STEP
alignment, not by reading more verses.

Nothing above is proposed as settled — it's what's visible from this one worked example, offered
as material for the thinking that's still in progress, not a substitute for it.

## Two more threads, checked against what already exists

### Genre/mode as a fixed, per-verse output

Researcher: reading discipline differs materially by genre (prose / narrative / declarative /
possibly others), this should be a **fixed output recorded for every verse read**, and it likely
determines **which checklist items even apply**.

This isn't new ground — it was already built once, just not where the live architecture currently
looks. `bible_research.db`'s `verse` table carries a populated `genre` column right now: six
values across 25,634 rows — `prophetic` (5,490), `law/narrative` (5,254), `narrative` (5,113),
`poetic/wisdom` (4,761), `epistle` (2,641), `gospel-narrative` (2,375) — the same genre-awareness
principle the 2026-07-02 verse-first method named (*"genre-aware — prose = cross-verse items on,
poetic = two-phase"*). **`iba.db`'s live `verse` table has no such column at all** — it carries
`osisId`, `reference`, `preview`, `step_version`, `text`, nothing genre-related. The concept exists
in the superseded database, on the superseded model, and did not carry forward when the base layer
moved to `iba.db`.

**And checking Dan 1:8's own tag surfaced a real limitation worth naming, not just confirming the
field exists:** it's tagged `prophetic` — because Daniel is a prophetic book — despite this
specific verse being a narrative episode (Daniel's court-narrative resolve), not prophetic oracle.
That reads as a **book-level** assignment, not a verse-level one. If genre is meant to select which
checklist tests apply *per verse* — the sequencing/chain test mattered here because this verse is
narrative, wayyiqtol-marked — a book-level tag would misroute every narrative-within-a-prophetic-
book verse (Daniel's opening chapters are full of these) and probably every comparable case
elsewhere (narrative asides in epistles, etc.). Worth having in view before deciding whether the
old `genre` column is reusable as-is, ported as-is, or needs re-deriving at verse grain for
`iba.db`.

### The entry-point problem, and what this verse's own dissection already answered

Researcher: *"we struggled with what is the entry point into the verse... I would hardly pick up
this verse because of the word ask or defile... that should lead back to the theme of the verse —
resolve. So somehow the theme/primary concept (and there could be more than one) should be
recorded."*

This names a real failure mode a term-driven scan would hit: a process studying the term "ask"
(`H1245`) or "defile" (`H1351`) would find Dan 1:8 as one of that term's occurrences — correctly, on
the term-presence test — but recording it *as an "ask" verse* or *a "defile" verse* would be
misleading. The primary-operation work above already gives a traceable answer for this specific
case: `resolve` is the verse's entry point because it's the chain's origin (nothing precedes it;
everything else — the content clause, the outward act — is downstream of it, evidenced by the
wayyiqtol sequencing already established). `ask` and `defile` aren't false leads; they're real
occurrences that correctly **point back** to `resolve` as the theme, rather than each standing as
its own independent theme.

That suggests a concrete, checkable field: alongside whatever term brought a reader or a process to
a verse, the finding record needs its own **primary-operation/theme field**, populated from the
chain analysis itself (the operation with nothing upstream of it), not from which search or
term-scan happened to surface the verse. The researcher's own caveat — *"there could be more than
one"* — matters directly here: this verse's chain has exactly one origin, but a verse could just as
well carry two independent, unchained operations, in which case it would need two theme entries, not
a forced single answer. Whether that's one field or a small set is itself part of what's still
open — flagged, not settled.

## Two more threads, checked against real data

### Language/testament as an explicit field, not an inferred one

Researcher: language/testament should be recorded explicitly on the finding — "implicit does
not trigger the mind" — and Hebrew vs. Greek morphology should be expected to play out
differently and must each be looked at on their own terms.

Checked, not assumed. `strong.language` exists and is populated (`Hebrew` for both
`H3820A` and `H7760A`) — but it lives on the **term identity table**, one join away from
`verse_lexical`/`span`, the tables the finding is actually built from. At the point a finding
is assembled, language is not sitting on the record — it has to be fetched. That is precisely
the "implicit" the researcher is naming.

The Hebrew/Greek difference is real and structural, confirmed by pulling both side by side:

| | Hebrew (`H3820A`/`H7760A`, this verse) | Greek (sample, elsewhere in the DB) |
|---|---|---|
| morph scheme | `HVqw3ms` — stem/binyan + **wayyiqtol** (waw-consecutive) + person/gender/number | `V-PAP-NPM`, `N-NSF`, `A-ASN` — part-of-speech + tense-voice-mood + case/number/gender |
| what marks narrative sequence | the waw-consecutive tag itself — this is what the chain test (above) actually keyed on | no equivalent tag; Greek marks sequence through tense-stem (aorist vs. present), voice, and participle-vs-finite-verb structure, or conjunctions like καί/δέ |

**Consequence for the checklist, not just a note:** the sequencing/chain test as built above
is Hebrew-specific — it was derived from, and only tested against, one Hebrew/Aramaic verse.
It does not port to Greek unchanged; a Greek verse needs its own version of that test, built
from Greek's own morphological signals, not the Hebrew one applied by analogy. Testament/
language recorded explicitly on the finding is what would trigger which version of the test
runs — exactly the researcher's point about implicit facts not triggering attention.

### Exploring the meaning itself — testing `strong_related` against `resolved`

Researcher: "Dan 1:8 may not be a good example — but let's test it: what are the other words
in the meaning that STEP relates to resolved?" Run against both codes carrying the idiom.

**`H3820A` (heart) — 14 related codes.** Genuinely mixed, not a clean list:
- `H1079` *bal* — "mind"
- `H3820B` *lev* — "Leb"
- `H3821` *lev* — "heart"
- `H3823A` *la.vav* — "to encourage"
- `H3823B` *lib.bev* — "to bake"
- `H3824` *le.vav* — "heart"
- `H3826` *lib.bah* — "heart"
- `H3834` *le.vi.vah* — "cake"
- `H6965A` *qa.ma* — "[Leb]-kamai"
- `H6965B` *qum* — "to arise: rise"
- `H6965H` *qum* — "to arise: raise"
- `H6965I` *qum* — "to arise: establish"
- `H6965J` *qum* — "to arise: attack"
- `H6965K` *qum* — "to arise: guard"

Sorted by what they actually are, not taken as one undifferentiated block:
- **Same-concept spelling/dialect variants** — `H3821`, `H3824`, `H3826` are all just "heart"
  in different forms (Aramaic *lev*, *levav*, *libbah*). Confirms the concept, adds no new
  information.
- **A genuine semantic relative** — `H3823A` *la.vav*, "to encourage" — a real derived verb
  (literally "to heart" someone) sitting in the same volitional/heart semantic field. This
  is the one entry that would actually be worth following up.
- **Coincidental root-sharing, not meaning-related** — `H3823B`/`H3834` ("to bake"/"cake") and
  the whole `H6965A`-`K` cluster ("to arise/raise/establish/attack/guard") share consonants
  with *leb* but carry no semantic connection to heart at all. The `H6965A` entry glosses
  "[Leb]-kamai" — a compound place-name that happens to *contain* "leb" as one syllable —
  which is almost certainly why the whole 'arise' cluster got linked in: one shared
  compound name, not a real semantic relation.

**`H7760A` ("to set") — 12 related codes**, mostly other cataloguing entries for the *same*
root (*śûm*), and genuinely useful for a different reason: several carry senses **not present
in `H7760A`'s own gloss stack** — "to set: accuse", "to set: consider", "to set: appoint",
"to set: name". The anchor code's own gloss field undersells the root's full range; the
related-term table fills that in.

**What this suggests about 'explore the meaning' as a checklist item:** it is a real,
worthwhile pull — but it needs the same per-row discipline as everything else in this
document, not a bulk import. Each related code needs sorting into (a) same-concept variant
(no new information), (b) genuine semantic relative (worth recording), or (c) coincidental
root-sharing (worth explicitly discarding, not silently trusting). Taking `strong_related`
as a block would have pulled "to bake" and "to arise" into a heart/volition finding with
no more justification than sharing three consonants.


## Correction — "bake" was dismissed too fast, and "defile" run the same way

Researcher: raw related-word lists aren't themselves useful in a finding — but the pattern
*setting/appointing/fixing/baking-in* is a materially different reading of "resolved" than "made a
decision," and asked for the same analysis on "defile," for interest.

**The correction first.** Earlier this document sorted `H3823B` ("to bake") into "coincidental
root-sharing, not meaning-related" alongside "cake." That was wrong, or at least asserted with more
confidence than it earned. Checked properly this time: `H3823B` carries `lemma_key = H3823` — the
**same lemma_key as `H3823A`, "to encourage."** STEP's own lexicographic structure treats
"encourage" and "bake" as two senses of *one* root, not a spurious consonant overlap. That's the
disambiguating test this document should have run the first time: same `lemma_key` = one root,
multiple senses (real); a `strong_related` link with *different* `lemma_key` values = homonymy —
same letters, unrelated origin — a distinction `strong_related` alone doesn't make, but
`strong_meaning_tree.lemma_key` does. Traced through: heart (`H3820A`) → related → "encourage"
(`H3823A`) → **same root as** → "bake" (`H3823B`). Real, traceable, not coincidental — the
researcher's instinct held, my dismissal didn't.

**What the researcher built from it, stated plainly as a reading, not re-asserted as if the data
proves it:** that *"resolved"* rests on a semantic field of *setting/appointing/fixing/baking
something into the heart* — materially different from "made a decision," closer to something
installed at the center of the person. That reading is well-formed and the lexical family now
genuinely supports it (this isn't the "bake" dismissal standing anymore) — but "where God and man
meet" and "baked in" as theological claims about what the heart *is* go beyond what any field here
states. That's real analytical work, properly the researcher's, sitting on top of a now-verified
lexical foundation rather than on a coincidence.

**`H1351` ("defile"), the same analysis, for interest — and it comes out differently.** Only 5
related codes, and every one clusters around one Hebrew root, *ga'al* (גאל):

| Code | Form | Gloss |
|---|---|---|
| `H1350A` | *ga.al* | to redeem: redeem |
| `H1350B` | *ge.u.lay* | redemption |
| `H1350H` | *ga.al* | to redeem: avenge |
| `H1350I` | *ga.al* | to redeem: relative |
| `H1352` | *go.el* | defilement |

The same consonants (ga'al) carry both "to redeem" (the kinsman-redeemer root — Boaz's role in
Ruth, God as redeemer) and "to defile" — the very root Daniel's resolve is stated against in this
verse. **Checked against `lemma_key`, the way "bake" should have been checked the first time:**
`H1351` ("defile") carries its own `lemma_key = H1351`; `H1352` carries its own `lemma_key = H1352`;
`H1350A` has no `strong_meaning_tree` row to check at all. None of the three share a lemma_key with
each other. Unlike heart/bake, this reads as the *other* case — **homonymy, not one root with
branching senses:** same letters, standard Hebrew lexicography treats "redeem" and "defile" as
separate, unrelated roots that happen to share a spelling, not two senses of one word. Worth having
that distinction on record precisely because it looks, on the surface, like the same kind of
striking pattern the heart/bake connection turned out to be — and on the data available, it isn't.
Whether a deliberate redeem/defile wordplay is nonetheless active in how this root is used
elsewhere in the canon is a real question — just not one this lexical-family check can answer
either way; it would need actual usage evidence, not root-structure alone.

## Retraction — the lemma_key test doesn't actually discriminate, and the design implication

Researcher: redeem and defile *do* relate — the same word, opposite poles, context selects which
applies — and understanding "defiled" is helped by knowing its other side is "redeemed." Also: this
whole level of analysis should be built into `verse_lexical` intrinsically, not reconstructed by
hand each time.

**The lemma_key test fails its own control case.** The claim "different `lemma_key` = homonymy, not
a real relation" was tested against exactly one positive case (heart/bake sharing `lemma_key`
`H3823`) and then applied with unearned confidence to redeem/defile. Checking it against a case
inside this document's own pulled data that should obviously pass: `H1351` ("defile," the verb) and
`H1352` ("defilement," the noun) are **undeniably the same root** — a bare verb/noun pair from
identical consonants — yet they carry **different** `lemma_key` values in this table (`H1351` and
`H1352` respectively). If the test called that a non-relation, the test is wrong, not the relation.
`lemma_key` tracks Strong's own numbering/lettering convention — whether STEP happened to group
several senses under one lettered entry or split them into separate base numbers — not a
philological verdict on whether two roots are historically related. It should not have been used
to override what `strong_related` itself already asserted. That's the actual mistake, and it's the
same shape as the "bake" dismissal: distrusting curated data with a second-order test that turned
out to be unreliable, and doing it with *more* confidence the second time, not less.

**Retracted:** "reads as homonymy, not branching senses" does not hold up. What the data actually
supports is narrower and more honest: `strong_related` links defile (`H1351`) to redeem
(`H1350A`/B/H/I) and to defilement (`H1352`) — STEP's own curators judged these related enough to
cross-reference — and this document has no reliable DB-native test that overrides that judgment.
Whether the connection is one root with a genuine polar/Janus-word duality (redeem ↔ defile,
disambiguated by context, as the researcher frames it) or a documented near-homonym biblical writers
exploited rhetorically is a real question with real scholarly discussion behind it (Isaiah, Malachi,
and Lamentations all use the "defile" sense of this root) — not one this session's tooling can
settle, and not one it should have pretended to settle either way.

### The design implication, named plainly

Researcher: *this level of analysis... should intrinsically be built in as part of verse-lexical.
verse-lexical must work harder to put the context of the word... understanding the word in relation
to its usage and articulating it for digestion when human analysis uses the lexical.*

That is a direct statement of what #1378 exists to work out — not a side comment. What this session
did by hand for two words (pull `strong_related`, cross-check `strong_meaning_tree`, sort real
relations from noise, articulate what the family shows) is exactly the kind of enrichment the
researcher is saying `verse_lexical` should carry natively, so a reader — human or the next
session — gets it as part of the record, not as a bespoke investigation repeated from scratch every
time a word looks interesting. Flagged as a real architectural direction for #1378, not designed or
built here — worth its own explicit next step when the researcher is ready to turn from exploring
examples to specifying what the enriched record actually needs to hold.

## Open, not concluded

This is one worked example, chosen partly because it's a favourable case. Whatever pattern holds
here is a hypothesis about the mechanism, not yet a design. Next candidate move — not yet
decided — would be to run the same dissection against one or two harder cases (a plain
non-idiomatic content word; a word whose `ambiguity_note` is actually populated) before drawing any
general shape.

## Appendix — raw, unfiltered dump

Exactly as returned from `iba.db`, no filtering, no curation — the ground truth for every claim
made above and the raw material for judging whether `verse_lexical` is solid or needs revision.

### `span` — all 15 rows, all columns

| id | position | surface | strong_variant | morph_code | is_particle | built_at | deleted |
|---|---|---|---|---|---|---|---|
| 715475 | 0 | Daniel | H1840G | HNpm | 0 | 2026-07-25T12:40:40Z | 0 |
| 715476 | 1 | resolved | H7760A H5921A H3820A | HVqw3ms HR HNcmsc | 0 | 2026-07-25T12:40:40Z | 0 |
| 715477 | 2 | that | H0834A H9023 | HTr HSp3ms | 0 | 2026-07-25T12:40:40Z | 0 |
| 715478 | 3 | not | H3808 | HTn | 0 | 2026-07-25T12:40:40Z | 0 |
| 715479 | 4 | defile | H1351 | HVti3ms | 0 | 2026-07-25T12:40:40Z | 0 |
| 715480 | 5 | king’s | H4428G H9009 | HNcmsa HTd | 0 | 2026-07-25T12:40:40Z | 0 |
| 715481 | 6 | food | H6598 H9003 | HNcmsc HR | 0 | 2026-07-25T12:40:40Z | 0 |
| 715482 | 7 | wine | H3196 H9002 H9003 | HNcmsc HC HR | 0 | 2026-07-25T12:40:40Z | 0 |
| 715483 | 8 | drank | H4960 | HNcmsc | 0 | 2026-07-25T12:40:40Z | 0 |
| 715484 | 9 | asked | H1245 H9023 | HVpw3ms HSp3ms | 0 | 2026-07-25T12:40:40Z | 0 |
| 715485 | 10 | chief | H8269 H9006 | HNcmsc HR | 0 | 2026-07-25T12:40:40Z | 0 |
| 715486 | 11 | eunuchs | H5631 H9009 | HNcmpa HTd | 0 | 2026-07-25T12:40:40Z | 0 |
| 715487 | 12 | allow | H0834A | HTr | 0 | 2026-07-25T12:40:40Z | 0 |
| 715488 | 13 | not | H3808 | HTn | 0 | 2026-07-25T12:40:40Z | 0 |
| 715489 | 14 | defile himself | H1351 | HVti3ms | 0 | 2026-07-25T12:40:40Z | 0 |

### `verse_lexical` — all 50 rows (25 live + 25 superseded), all columns

Sorted by span position, then `code_ordinal`, then `id` (so the superseded/live pair for
each row sits together).

| id | span_id | pos | surface | ord | strong | morph | role | status | created_at | deleted | resolved_sense |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 7082 | 715475 | 0 | Daniel | 0 | H1840G | HNpm | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: Daniel — A prophet living at the time of Exile and Return, first mentioned at Ezk.14.14;; referred to as Daniel (דָּנִיֵּאל, דָּנִאֵל), or Daniel (Aramiac דָּנִיֵּאל, דָּנִאֵל), or Belteshazzar (בֵּלְטְשַׁאצַּר), or Belteshazzar (Aramiac בֵּלְטְשַׁאצַּר), or [ ] (KJV= Daniel) or Daniel (Δανιήλ). |
| 10631 | 715475 | 0 | Daniel | 0 | H1840G | HNpm | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: Daniel — A prophet living at the time of Exile and Return, first mentioned at Ezk.14.14;; referred to as Daniel (דָּנִיֵּאל, דָּנִאֵל), or Daniel (Aramiac דָּנִיֵּאל, דָּנִאֵל), or Belteshazzar (בֵּלְטְשַׁאצַּר), or Belteshazzar (Aramiac בֵּלְטְשַׁאצַּר), or [ ] (KJV= Daniel) or Daniel (Δανιήλ). |
| 7083 | 715476 | 1 | resolved | 0 | H7760A | HVqw3ms | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: to set: make — to put, place, set, appoint, make; to put, set, lay, put or lay upon, lay (violent) hands on; to set, direct, direct toward; to extend (compassion) (fig); to set, ordain, establish, found, appoint, constitute, make, determine, fix; to set, station, put, set in place, plant, fix; to make, make for, transform into, constitute, fashion, work, bring to pass, appoint, give |
| 10632 | 715476 | 1 | resolved | 0 | H7760A | HVqw3ms | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: to set: make — to put, place, set, appoint, make; to put, set, lay, put or lay upon, lay (violent) hands on; to set, direct, direct toward; to extend (compassion) (fig); to set, ordain, establish, found, appoint, constitute, make, determine, fix; to set, station, put, set in place, plant, fix; to make, make for, transform into, constitute, fashion, work, bring to pass, appoint, give |
| 7084 | 715476 | 1 | resolved | 1 | H5921A | HR | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: upon — prep; upon, on the ground of, according to, on account of, on behalf of, concerning, beside, in addition to, together with, beyond, above, over, by, on to, towards, to, against; upon, on the ground of, on the basis of, on account of, because of, therefore, on behalf of, for the sake of, for, with, in spite of, notwithstanding, concerning, in the matter of, as regards; above, beyond, over (of excess); above, over (of elevation or pre-eminence); upon, to, over to, unto, in addition to, together with, with (of addition); over (of suspension or extension); by, adjoining, next, at, over, around (of contiguity or proximity); down upon, upon, on, from, up upon, up to, towards, over towards, to, against (with verbs of motion); to (as a dative) |
| 10633 | 715476 | 1 | resolved | 1 | H5921A | HR | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: upon — prep; upon, on the ground of, according to, on account of, on behalf of, concerning, beside, in addition to, together with, beyond, above, over, by, on to, towards, to, against; upon, on the ground of, on the basis of, on account of, because of, therefore, on behalf of, for the sake of, for, with, in spite of, notwithstanding, concerning, in the matter of, as regards; above, beyond, over (of excess); above, over (of elevation or pre-eminence); upon, to, over to, unto, in addition to, together with, with (of addition); over (of suspension or extension); by, adjoining, next, at, over, around (of contiguity or proximity); down upon, upon, on, from, up upon, up to, towards, over towards, to, against (with verbs of motion); to (as a dative) |
| 7085 | 715476 | 1 | resolved | 2 | H3820A | HNcmsc | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: heart — inner man, mind, will, heart, understanding; inner part, midst; midst (of things); heart (of man); soul, heart (of man); mind, knowledge, thinking, reflection, memory; inclination, resolution, determination (of will); conscience; heart (of moral character); as seat of appetites; as seat of emotions and passions 1a10) as seat of courage |
| 10634 | 715476 | 1 | resolved | 2 | H3820A | HNcmsc | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: heart — inner man, mind, will, heart, understanding; inner part, midst; midst (of things); heart (of man); soul, heart (of man); mind, knowledge, thinking, reflection, memory; inclination, resolution, determination (of will); conscience; heart (of moral character); as seat of appetites; as seat of emotions and passions 1a10) as seat of courage |
| 7086 | 715477 | 2 | that | 0 | H0834A | HTr | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: which — A: 1) (relative part.); which, who; that which; (conj); that (in obj clause); when; since; as; conditional if; B: Beth+ 1) in (that) which; (adv); where; (conj); in that, inasmuch as; on account of; C: Mem+ 1) from (or than) that which; from (the place) where; from (the fact) that, since; D: Kaph+; (conj.), according as, as, when; according to that which, according as, as; with a causal force: in so far as, since; with a temporal force: when |
| 10635 | 715477 | 2 | that | 0 | H0834A | HTr | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: which — A: 1) (relative part.); which, who; that which; (conj); that (in obj clause); when; since; as; conditional if; B: Beth+ 1) in (that) which; (adv); where; (conj); in that, inasmuch as; on account of; C: Mem+ 1) from (or than) that which; from (the place) where; from (the fact) that, since; D: Kaph+; (conj.), according as, as, when; according to that which, according as, as; with a causal force: in so far as, since; with a temporal force: when |
| 7087 | 715477 | 2 | that | 1 | H9023 | HSp3ms | function | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: his — Personal possessive pronoun - suffix for nouns, adjectives and passive participles: 3rd person masculine singular |
| 10636 | 715477 | 2 | that | 1 | H9023 | HSp3ms | function | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: his — Personal possessive pronoun - suffix for nouns, adjectives and passive participles: 3rd person masculine singular |
| 7088 | 715478 | 3 | not | 0 | H3808 | HTn | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: not — not, no; not (with verb-absolute prohibition); not (with modifier-negation); nothing (subst); without (with particle); before (of time); Aramaic equivalent: la (לָא "not" H3809) |
| 10637 | 715478 | 3 | not | 0 | H3808 | HTn | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: not — not, no; not (with verb-absolute prohibition); not (with modifier-negation); nothing (subst); without (with particle); before (of time); Aramaic equivalent: la (לָא "not" H3809) |
| 7089 | 715479 | 4 | defile | 0 | H1351 | HVti3ms | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: to defile — to defile, pollute, desecrate; to defile oneself |
| 10638 | 715479 | 4 | defile | 0 | H1351 | HVti3ms | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: to defile — to defile, pollute, desecrate; to defile oneself |
| 7090 | 715480 | 5 | king’s | 0 | H4428G | HNcmsa | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: king — king; Aramaic equivalent: me.lekh (מֶ֫לֶךְ "king" H4430) |
| 10639 | 715480 | 5 | king’s | 0 | H4428G | HNcmsa | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: king — king; Aramaic equivalent: me.lekh (מֶ֫לֶךְ "king" H4430) |
| 7091 | 715480 | 5 | king’s | 1 | H9009 | HTd | function | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: [the] — Prefix hé article: "the" for a subject, not object |
| 10640 | 715480 | 5 | king’s | 1 | H9009 | HTd | function | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: [the] — Prefix hé article: "the" for a subject, not object |
| 7092 | 715481 | 6 | food | 0 | H6598 | HNcmsc | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: choice — portion of food for king, delicacies |
| 10641 | 715481 | 6 | food | 0 | H6598 | HNcmsc | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: choice — portion of food for king, delicacies |
| 7093 | 715481 | 6 | food | 1 | H9003 | HR | function | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: in/on/with — Prefix beth: in, among, with |
| 10642 | 715481 | 6 | food | 1 | H9003 | HR | function | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: in/on/with — Prefix beth: in, among, with |
| 7094 | 715482 | 7 | wine | 0 | H3196 | HNcmsc | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: wine — wine |
| 10643 | 715482 | 7 | wine | 0 | H3196 | HNcmsc | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: wine — wine |
| 7095 | 715482 | 7 | wine | 1 | H9002 | HC | function | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: and — Conjunctive vav - i.e. followed by prefix, suffix or non-verb (conjunctive) (‘and/but’) |
| 10644 | 715482 | 7 | wine | 1 | H9002 | HC | function | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: and — Conjunctive vav - i.e. followed by prefix, suffix or non-verb (conjunctive) (‘and/but’) |
| 7096 | 715482 | 7 | wine | 2 | H9003 | HR | function | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: in/on/with — Prefix beth: in, among, with |
| 10645 | 715482 | 7 | wine | 2 | H9003 | HR | function | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: in/on/with — Prefix beth: in, among, with |
| 7097 | 715483 | 8 | drank | 0 | H4960 | HNcmsc | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: feast — feast, drink, banquet; feast, banquet; drink; Aramaic equivalent: mish.teh (מִשְׁתֶּה "feast" H4961) |
| 10646 | 715483 | 8 | drank | 0 | H4960 | HNcmsc | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: feast — feast, drink, banquet; feast, banquet; drink; Aramaic equivalent: mish.teh (מִשְׁתֶּה "feast" H4961) |
| 7098 | 715484 | 9 | asked | 0 | H1245 | HVpw3ms | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: to seek — to seek, require, desire, exact, request; to seek to find; to seek to secure; to seek the face; to desire, demand; to require, exact; to ask, request |
| 10647 | 715484 | 9 | asked | 0 | H1245 | HVpw3ms | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: to seek — to seek, require, desire, exact, request; to seek to find; to seek to secure; to seek the face; to desire, demand; to require, exact; to ask, request |
| 7099 | 715484 | 9 | asked | 1 | H9023 | HSp3ms | function | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: his — Personal possessive pronoun - suffix for nouns, adjectives and passive participles: 3rd person masculine singular |
| 10648 | 715484 | 9 | asked | 1 | H9023 | HSp3ms | function | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: his — Personal possessive pronoun - suffix for nouns, adjectives and passive participles: 3rd person masculine singular |
| 7100 | 715485 | 10 | chief | 0 | H8269 | HNcmsc | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: ruler — prince, ruler, leader, chief, chieftain, official, captain; chieftain, leader; vassal, noble, official (under king); captain, general, commander (military); chief, head, overseer (of other official classes); heads, princes (of religious office); elders (of representative leaders of people); merchant-princes (of rank and dignity); patron-angel; Ruler of rulers (of God); warden |
| 10649 | 715485 | 10 | chief | 0 | H8269 | HNcmsc | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: ruler — prince, ruler, leader, chief, chieftain, official, captain; chieftain, leader; vassal, noble, official (under king); captain, general, commander (military); chief, head, overseer (of other official classes); heads, princes (of religious office); elders (of representative leaders of people); merchant-princes (of rank and dignity); patron-angel; Ruler of rulers (of God); warden |
| 7101 | 715485 | 10 | chief | 1 | H9006 | HR | function | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: from — Prefix mem: from |
| 10650 | 715485 | 10 | chief | 1 | H9006 | HR | function | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: from — Prefix mem: from |
| 7102 | 715486 | 11 | eunuchs | 0 | H5631 | HNcmpa | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: eunuch — official, eunuch |
| 10651 | 715486 | 11 | eunuchs | 0 | H5631 | HNcmpa | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: eunuch — official, eunuch |
| 7103 | 715486 | 11 | eunuchs | 1 | H9009 | HTd | function | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: [the] — Prefix hé article: "the" for a subject, not object |
| 10652 | 715486 | 11 | eunuchs | 1 | H9009 | HTd | function | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: [the] — Prefix hé article: "the" for a subject, not object |
| 7104 | 715487 | 12 | allow | 0 | H0834A | HTr | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: which — A: 1) (relative part.); which, who; that which; (conj); that (in obj clause); when; since; as; conditional if; B: Beth+ 1) in (that) which; (adv); where; (conj); in that, inasmuch as; on account of; C: Mem+ 1) from (or than) that which; from (the place) where; from (the fact) that, since; D: Kaph+; (conj.), according as, as, when; according to that which, according as, as; with a causal force: in so far as, since; with a temporal force: when |
| 10653 | 715487 | 12 | allow | 0 | H0834A | HTr | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: which — A: 1) (relative part.); which, who; that which; (conj); that (in obj clause); when; since; as; conditional if; B: Beth+ 1) in (that) which; (adv); where; (conj); in that, inasmuch as; on account of; C: Mem+ 1) from (or than) that which; from (the place) where; from (the fact) that, since; D: Kaph+; (conj.), according as, as, when; according to that which, according as, as; with a causal force: in so far as, since; with a temporal force: when |
| 7105 | 715488 | 13 | not | 0 | H3808 | HTn | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: not — not, no; not (with verb-absolute prohibition); not (with modifier-negation); nothing (subst); without (with particle); before (of time); Aramaic equivalent: la (לָא "not" H3809) |
| 10654 | 715488 | 13 | not | 0 | H3808 | HTn | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: not — not, no; not (with verb-absolute prohibition); not (with modifier-negation); nothing (subst); without (with particle); before (of time); Aramaic equivalent: la (לָא "not" H3809) |
| 7106 | 715489 | 14 | defile himself | 0 | H1351 | HVti3ms | content | resolved | 2026-08-06T19:15:05Z | 1 | stepGloss: to defile — to defile, pollute, desecrate; to defile oneself |
| 10655 | 715489 | 14 | defile himself | 0 | H1351 | HVti3ms | content | resolved | 2026-08-07T16:24:41Z | 0 | stepGloss: to defile — to defile, pollute, desecrate; to defile oneself |
