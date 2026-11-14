# #2486 What a claim does: the claim work-up, draft v2 for discussion (2026-11-13)

Status: a draft for the researcher to correct and extend. Replaces v1 (`outputs/escalation/archive/2486-what-claims-do-draft-v1-20261113.md`): section 3a is new, and section 5 point 1 is answered. Not a rule, not built. It follows `outputs/escalation/2486-reading-c-367-outcome-v1-20261113.md` (section 5) and sits beside `outputs/escalation/2486-claim-objectives-and-definition-draft-v2-20261113.md` (what a claim is) as its other half: what the work of making a claim covers. Counts are from the trial copy `iba/app/db/snapshots/trial-2486/iba-trial-2486.db`; readings are inferential (B:4).

## 1. The researcher's list (2026-11-13, in the researcher's order)

Verbatim: "your proposals §5 is a good start. what this exercise is pointing out is we need to give more attention to what claims should be doing. There is likely a long list. compare verses with the same surface; check if same surface with different strongs have any significance; if surface is different from the root, why, does it have any significance for the inner being, does the surface bind with any other surface in the verse - are there any other verses with the same binding - what does it mean for the inner being; are there any other bindings in other verses - how does that compare - what does it mean; does the surface appear with any other behaviours - what does it mean; does other verses in the same collection behave differently - what is the impact; what does the surface do to or from the entities - what is the impact; are there any qualifyers (types, actions, enhancers) that plays a part - does in differ in different circumstances; does the behaviours relate to or bind with other collections; are there any perculiar or specific consistencies or discrepancies across the behaviours."

## 2. What exists today, and what does not

- For **observations** the app has a configured list: `cfg_setting reading.observation_items` holds the nine items an observation is explored for, with `reading.nuance_pointers`; each applicable item is its own observation (B:131, USER-GUIDE section on Record).
- For **claims** there is no such list. The register has the claim's text, `beyond_text`, verdict and sources; nothing says what a claim must have looked at. The list above is the claim side of what `reading.observation_items` is for observations.
- The same shape would fit: a configured list of **claim work-up items**, each with a key, the question, the evidence the app prepares from the tables, what the researcher and Claude decide in the reading, and what is recorded on the claim. The list is config, so it can grow (the researcher expects it to).

## 3. The questions, grouped by the level they feed (my grouping, to correct)

| # | Question (researcher's words, shortened) | Level it feeds | What the stored data already gives | What needs the reading |
|---|---|---|---|---|
| 1 | Compare verses with the same surface | surface | all occurrences of the surface by verse (collection evidence tool) | what the verses show together |
| 2 | Same surface with different Strong's: any significance | surface | the Strong's code of each occurrence | what each word adds |
| 3 | Surface differs from the root: why, any significance for the inner being | surface | the base of the surface and how it was derived (`surface_term`, `surface_derivation`) | the significance |
| 4 | Does the surface bind with another surface in the verse; other verses with the same binding; what it means | interaction | words in the same verse and, where read, the nodes tied in one observation | what "binding" is (see section 5); the meaning |
| 5 | Other bindings in other verses: how they compare, what they mean | interaction | the same, across verses | the comparison |
| 6 | Does the surface appear with other behaviours; what it means | across | the collections of the other words in the same verses (via nodes) | the meaning |
| 7 | Do other verses of the same collection behave differently; the impact | across | the verses of the collection and their observations | the difference and its impact |
| 8 | What does the surface do to or from the entities; the impact | interaction | the entity words (`party_kind`) in the verse; party and link findings where read | the direction and the impact |
| 9 | Qualifiers (types, actions, enhancers): their part; does it differ by circumstance | interaction | node roles (qualifier) and the observation items (polarity, mode, object, enactment) where read | the part and the circumstance |
| 10 | Do the behaviours relate to or bind with other collections | across | collections sharing verses and observations | the relation |
| 11 | Peculiar or specific consistencies or discrepancies across the behaviours | meta | counts and lists across the collection | what is peculiar and what it means |

Added from the C-367 reading, applying to every claim: **12** scope (all occurrences of its surfaces, or a stated sample); **13** the stance of each evidence link (supports, qualifies, contradicts); **14** completeness against the verses where its surfaces occur (with and without the entity).

Many answers to these questions are themselves claims of the level shown: a question answered becomes a claim, or confirms or restates one. That is why the work-up is not a checklist separate from claims; it is how claims are found and tested.

## 3a. Binding is not one thing (the researcher's answer, 2026-11-13)

Verbatim: "The problem with binding is that it is complex and not a single answer: binding to the same type of word (behaviour to behaviour) is very different from binding to an entity or object, and is different from binding to an action or status, and is different from a binding to a qualifyer. the binding can be in the same verse, or before or after. In some cases a binding is expected, and can be searched for, in other cases the binding is implicit or silent, and in other cases it is alogoric or pictorial ('like the wind' or as in our thought example 'a breath'. All of this can only really be known by understanding the context, and looking how similar words are operating, and then search or inferring what is expected."

My reading of it (inferential): a binding is a finding with four dimensions, not a stored relation.

| Dimension | Values the researcher names | What the app holds today |
|---|---|---|
| Partner type | the same type of word (behaviour to behaviour); an entity or object; an action or status; a qualifier | node roles (`reading.node_roles`: characteristic and qualifier; object, relational target, enactment; standalone) and observation items (role, object, enactment, party, circumstance, operation, chain). Behaviour to behaviour exists only as the chain (a link of operations). Roles are empty on 14,065 of 68,406 live nodes |
| Reach | the same verse, before, after | a node carries its verse, so an observation can span verses; a partner in the next or previous verse is not typed (the tag list has `needs_adjacent_verse_context`) |
| Mode | expected and found; implicit or silent; figurative or pictorial | not held. The tag `silence` means something else: a word with no inner-being bearing in that occurrence. A partner that is expected and absent has no place |
| Expectation | what to look for, from how similar words operate | not held |

The expectation is the key. It is learned from the collection: how its members operate across their verses (which partner types they take, in which reach, in which mode). Each occurrence is then compared with that profile and falls into one of: found as expected, expected but silent, figurative, or unexpected. A silent partner is data, as the register already treats absence elsewhere (C-156: 17 of 24 verses with such a wish name no inner word).

Who does what: the app can prepare the explicit part (words in the verse and in the verses before and after, partner type where the role is filled, and the profile counts per collection once roles are filled). Reading with the researcher decides implicit, silent and figurative, and the expectation; these stay inferential until confirmed (B:4), and are recorded as findings, not guessed by pattern (B:127).

A worked example from the trial: Psa 94:11, "the thoughts of man ... are but a breath". The observation level says what the verse says, a figurative binding of thoughts to a breath (the surface "breath" sits in observation 18484 with no collection and in 20456 with the collection thought). The claim level says what that means for the inner being: thought is creaturely and passing (the key-statement 12422 already states this, which is claim wording stored as an observation, as in the trial findings).

## 4. A first try on one surface: "thoughts" (read-only)

- **Question 1:** 47 occurrences in 44 verses.
- **Question 2:** 15 different Strong's codes behind one surface: H4284 (19), G1261 (7), H7476 (6), G1761 (3), H7454 (2) and ten more with one each. So one English surface is several different words; whether they differ for the inner being is open.
- **Question 3:** "thoughts" is the plural inflection of the base "thought" (derived by structure). That the surface differs from its root only by number is what the data says; any further significance would be the reading's.
- **Question 10:** in the 44 verses that have a node, the collections that share them are thought (38), heart (14), evildoer (13), know (9), fear (5), intend (4) and a few with two each.
- **Questions 4 to 9 and 11** need observations with roles and nodes on every occurrence. They cannot be run yet: 258 of the 394 occurrences of the collection `thought` have no live node, and node roles are empty on 14,065 of 68,406 live nodes.

So questions 1 to 3 and 10 to 14 can be prepared by the app from what is stored; 4 to 9 and 11 depend on the surface having been read first.

## 5. Questions for the researcher

1. **Binding** (questions 4 and 5): answered in section 3a, not one thing. Open: which values of partner type, reach and mode actually occur. I propose to find them by classifying the bindings of a few occurrences of one surface by hand with the researcher, then write the list (config) from what is found, not before.
2. **The list**: correct, reorder or extend section 3. The aim is a config list in the same way as the observation items, so it can grow.
3. **Order of the work**: read a surface first (observations with roles on all its occurrences), then work up its claims. The trial would then run questions 1 to 14 on one surface end to end ("thoughts" is the obvious one, since C-367 has shown its gaps).
4. **Where it lives**: as a step of the reading process (`Reading.ps1`, between Observe and Synergy, or inside Synergy), the app preparing the evidence for each question from the tables and the reading recording the answers on the claim.

## 6. Not done

No rule, config row, schema or document changed; no claim marked or changed; nothing live written.
