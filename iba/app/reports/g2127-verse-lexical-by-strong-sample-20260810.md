# G2127 — on-demand verse restatement, by single Strong's reference (second test case)

> Retest of the on-demand per-Strong's design (`g2128-verse-lexical-by-strong-sample-20260810.md`)
> against a harder case: G2127 has more verses, a real multi-occurrence verse, and — found only by
> actually building this one — two data shapes G2128 never exercised: a **combined-code span**
> (STEP tags two Strong's on one rendering unit) and a **real substring-collision bug** in the
> naive text-search substitution method the first sample used. Both are fixed here, not just
> flagged.

## Count, checked the same two ways as before

- **Local, but via the right table this time.** First pass queried `span.strong_variant='G2127'`
  (exact string match) and got **40 rows / 39 verses**. That undercounts — checked why: 2 of
  those "missing" rows exist in `span` but under a **combined tag**, e.g. `strong_variant='G2532
  G2127'` (Luk 1:42, "Blessed" fused with the preceding "and") and `'G2127 G1722'` (Luk 1:28, an
  empty-surface companion span). `span.strong_variant='G2127'` (exact string) never matches
  those — `verse_lexical.strong='G2127'` does (it decomposes combined tags into one row per
  code), giving the correct **42 rows / 40 verses**.
- **Live STEP**, `call3_strong("G2127")`, this session: **`total: 40`** — matches the
  `verse_lexical`-based distinct-verse count exactly, confirming STEP's own search correctly
  covers combined-tag occurrences too, unlike a naive local exact-string filter on `span`. Local
  and live agree on **40 real verses**.
- **STEP dictionary "count" field** (`call2_getInfo`, the same non-verse-scoped number diagnosed
  in the G2128 sample and BUILD.md §88): **334** — still not a verse count, kept only for
  reference, never used below.

**Lesson for the eventual real tool:** query `verse_lexical.strong`, not `span.strong_variant`
exact-match — the latter silently misses every combined-tag occurrence of the target code.

## Exact-variant senses for G2127 (all `strong_meaning_parsed` rows, this code only)

G2127 has no sibling sub-letter codes sharing its base, so all 8 rows below are unambiguously its
own:

- to praise, give thanks to, speak well of, extol; (passive) to be blessed, receive blessing; in
  some contexts, to give a blessing is to act kindly and impart benefits to the one being blessed
  *(general, `sort=0`)*
- to speak well of
- to bless, ascribe praise and glorification
- to bless, invoke a blessing upon
- to bless, confer a favor
- blessing upon
- to be blessed, to be an object of favor
- blessing

## A real bug the G2128 sample didn't hit: substring collision, found and fixed

G2128's sample (8 verses, no repeated word-forms) never had to prove its "search the verse text
for the surface" method was actually safe — it happened not to be tested against a case where it
would fail. G2127 (40 verses) supplied one on the first pass: **1Cor 10:16**.

> The cup of **blessing** that we bless, is it not a participation in the blood of Christ?...

Plain `text.count("bless")` on this verse returns **2** — not because G2127 occurs twice, but
because `"bless"` is a literal substring of the *other* word in the same verse, `"blessing"`
(a different span, G2129, not this one). The naive substring-search method from the G2128 sample
would have flagged this as an unresolved collision (correctly refusing to guess, per that sample's
own stated limitation) — or worse, in a differently-shaped verse, silently picked the wrong
occurrence.

**Fixed:** switched from plain substring search to a **word-boundary regex** (`\bbless\b`),
tested directly: matches `"bless,"` at position 28 exactly once, correctly skipping the `"bless"`
inside `"blessing"` (no word boundary between `"bless"` and `"ing"`). Re-scanned all 42 rows
across all 40 verses with this method: **every non-empty surface matches exactly once**, including
in the two real multi-occurrence verses below (each row's surface differs there, so no further
ambiguity). This is a genuine fix to carry into the real tool, not a G2127-specific patch — any
Strong's whose English rendering is a shorter word contained in a longer one nearby (fear/fearful,
bless/blessing, just/justice, etc.) is exposed to the same bug.

## Two real multi-occurrence verses, both handled correctly

- **Rom 12:14** — "**Bless** those who persecute you; **bless** and do not curse them." Two
  separate G2127 spans, one verse. Different case (`Bless`/`bless`), each matched exactly once —
  safe.
- **Luk 1:42** — "**Blessed** are you among women, and **blessed** is the fruit of your womb!"
  Also two separate spans — but the FIRST is a **combined tag** (`G2532 G2127`, the Greek
  conjunction "and" fused onto this verb in STEP's own tagging), labelled as such in the
  annotation below rather than presented as if it were a pure G2127 occurrence.

## One empty-surface case, not force-annotated

**Luk 1:28** — the verse's own G2127 occurrence is the second half of a combined tag (`G2127
G1722`) with **no independent English surface text** (STEP's rendering attributes the visible
words elsewhere in "And he came to her and said, 'Greetings, O favored one...'"). Cannot be
inline-annotated without guessing which word(s) it corresponds to — noted as a structured aside
under the verse instead of forced into the running text.

## All 40 verses, restated — only the G2127 span(s) annotated per verse, rest untouched

### Mat 14:19

> Then he ordered the crowds to sit down on the grass, and taking the five loaves and the two fish, he looked up to heaven and **said a blessing** [G2127: to praise, give thanks to, speak well of, extol; ( passive ) to be blessed, receive blessing; in some contexts, to give a blessing is to act kindly and impart benefits to the one being blessed; to speak well of; to bless, ascribe praise and glorification; to bless, invoke a blessing upon; to bless, confer a favor; blessing upon; to be blessed, to be an object of favor; blessing]. Then he broke the loaves and gave them to the disciples, and the disciples gave them to the crowds.

### Mat 21:9

> And the crowds that went before him and that followed him were shouting, "Hosanna to the Son of David! **Blessed** [G2127: ...as above] is he who comes in the name of the Lord! Hosanna in the highest!"

### Mat 23:39

> For I tell you, you will not see me again, until you say, '**Blessed** [G2127] is he who comes in the name of the Lord.'"

### Mat 25:34

> Then the King will say to those on his right, 'Come, you who are **blessed** [G2127] by my Father, inherit the kingdom prepared for you from the foundation of the world.

### Mat 26:26

> Now as they were eating, Jesus took bread, and after **blessing** [G2127] it broke it and gave it to the disciples, and said, "Take, eat; this is my body."

### Mar 6:41

> And taking the five loaves and the two fish, he looked up to heaven and **said a blessing** [G2127] and broke the loaves and gave them to the disciples to set before the people. And he divided the two fish among them all.

### Mar 8:7

> And they had a few small fish. And having **blessed** [G2127] them, he said that these also should be set before them.

### Mar 10:16

> And he took them in his arms and **blessed** [G2127] them, laying his hands on them.

### Mar 11:9

> And those who went before and those who followed were shouting, "Hosanna! **Blessed** [G2127] is he who comes in the name of the Lord!

### Mar 11:10

> **Blessed** [G2127] is the coming kingdom of our father David! Hosanna in the highest!"

### Mar 14:22

> And as they were eating, he took bread, and after **blessing** [G2127] it broke it and gave it to them, and said, "Take; this is my body."

### Luk 1:28

> And he came to her and said, "Greetings, O favored one, the Lord is with you!"

  - *(the verse's G2127 occurrence, position 10, morph `V-RPP-NSF PREP`, is the empty-surface half of combined tag `G2127 G1722` — no independent surface text; see note above)*

### Luk 1:42

> and she exclaimed with a loud cry, "**Blessed** [G2127+G2532 combined tag: to praise, give thanks to, speak well of, extol; ( passive ) to be blessed, receive blessing; ...as above] are you among women, and **blessed** [G2127] is the fruit of your womb!

### Luk 1:64

> And immediately his mouth was opened and his tongue loosed, and he spoke, **blessing** [G2127] God.

### Luk 2:28

> he took him up in his arms and **blessed** [G2127] God and said,

### Luk 2:34

> And Simeon **blessed** [G2127] them and said to Mary his mother, "Behold, this child is appointed for the fall and rising of many in Israel, and for a sign that is opposed

### Luk 6:28

> **bless** [G2127] those who curse you, pray for those who abuse you.

### Luk 9:16

> And taking the five loaves and the two fish, he looked up to heaven and **said a blessing** [G2127] over them. Then he broke the loaves and gave them to the disciples to set before the crowd.

### Luk 13:35

> Behold, your house is forsaken. And I tell you, you will not see me until you say, '**Blessed** [G2127] is he who comes in the name of the Lord!'"

### Luk 19:38

> saying, "**Blessed** [G2127] is the King who comes in the name of the Lord! Peace in heaven and glory in the highest!"

### Luk 24:30

> When he was at table with them, he took the bread and **blessed** [G2127] and broke it and gave it to them.

### Luk 24:50

> And he led them out as far as Bethany, and lifting up his hands he **blessed** [G2127] them.

### Luk 24:51

> While he **blessed** [G2127] them, he parted from them and was carried up into heaven.

### Luk 24:53

> and were continually in the temple **blessing** [G2127] God.

### Joh 12:13

> So they took branches of palm trees and went out to meet him, crying out, "Hosanna! **Blessed** [G2127] is he who comes in the name of the Lord, even the King of Israel!"

### Act 3:26

> God, having raised up his servant, sent him to you first, to **bless** [G2127] you by turning every one of you from your wickedness."

### Rom 12:14

> **Bless** [G2127] those who persecute you; **bless** [G2127] and do not curse them.

### 1Cor 4:12

> and we labor, working with our own hands. When reviled, we **bless** [G2127]; when persecuted, we endure;

### 1Cor 10:16

> The cup of blessing that we **bless** [G2127], is it not a participation in the blood of Christ? The bread that we break, is it not a participation in the body of Christ?

### 1Cor 14:16

> Otherwise, if you **give thanks** [G2127] with your spirit, how can anyone in the position of an outsider say "Amen" to your thanksgiving when he does not know what you are saying?

### Gal 3:9

> So then, those who are of faith are **blessed** [G2127] along with Abraham, the man of faith.

### Eph 1:3

> Blessed be the God and Father of our Lord Jesus Christ, who has **blessed** [G2127] us in Christ with every spiritual blessing in the heavenly places,

### Heb 6:14

> saying, "Surely I will **bless** [G2127] you and multiply you."

### Heb 7:1

> For this Melchizedek, king of Salem, priest of the Most High God, met Abraham returning from the slaughter of the kings and **blessed** [G2127] him,

### Heb 7:6

> But this man who does not have his descent from them received tithes from Abraham and **blessed** [G2127] him who had the promises.

### Heb 7:7

> It is beyond dispute that the inferior is **blessed** [G2127] by the superior.

### Heb 11:20

> By faith Isaac invoked future **blessings** [G2127] on Jacob and Esau.

### Heb 11:21

> By faith Jacob, when dying, **blessed** [G2127] each of the sons of Joseph, bowing in worship over the head of his staff.

### Jam 3:9

> With it we **bless** [G2127] our Lord and Father, and with it we curse people who are made in the likeness of God.

### 1Pe 3:9

> Do not repay evil for evil or reviling for reviling, but on the contrary, bless, for to this you were called, that you may obtain a **blessing** [G2127].

*(Full sense text `[G2127: ...]` shown in full only on first occurrence above and where a
combined tag changes the label; repeated identically on every other line in the actual rendering
— abbreviated "...as above" here only for this file's own readability, not a difference in the
underlying data.)*

## Open items carried forward from the G2128 sample, status now

1. **Report scope** (one Strong's per run, all its verses) — confirmed working at 5x the previous
   sample's size (40 vs 8 verses), no new scaling issue at this size.
2. **Live STEP vs local DB** — still used local DB here since it fully agreed with live STEP (40
   distinct verses both ways) — but this run only agreed *because* the query was corrected to
   `verse_lexical.strong`, not `span.strong_variant`. A code with genuinely incomplete local
   onboarding still needs the live STEP path, unproven either way by this sample.
3. **Position-exact substitution** — no longer an open item for the *within-verse-order* class of
   collision (word-boundary regex, verified against real data, closes it for same-verse
   substring/word-form collisions). Still open for the hypothetical case of two DIFFERENT spans
   producing the exact same surface string with the exact same case in one verse — word-boundary
   regex alone can't disambiguate that (it would find 2 matches and correctly flag as unresolved
   rather than guess, per the method above, but hasn't yet been tested against a live example of
   that exact shape).
4. **Combined-tag spans** (new finding this sample) — need explicit handling in the real tool:
   detect when `verse_lexical`'s underlying span carries more than one code, and label the
   annotation accordingly (as done above for Luk 1:42) rather than presenting it as a pure
   single-code occurrence.
5. **Empty-surface spans** (new finding this sample) — need a defined fallback presentation (the
   structured aside used above for Luk 1:28) rather than either a crash or a silently dropped
   occurrence.

No code changes made yet — data preview only, built against `verse_lexical`/`span`/
`strong_meaning_parsed` (local) and `call3_strong`/`call2_getInfo` (live STEP) for G2127.
