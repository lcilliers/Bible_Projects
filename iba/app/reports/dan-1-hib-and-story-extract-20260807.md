# Dan 1 — HIB list + passage story, extracted live from the DB

> Read-only extract of `hib`/`verse_hib` (book='Dan', scoped to Dan.1.*) and `passage` id 37466
> (`Dan 1:1-21`, `rule='input-scope'`) as they stand right now — not a re-derivation, not the chat
> summary. For your review before `phenomenon.set`.

## Passage (Step 2 — `passage.build`)

**Ref:** Dan 1:1-21 · **passage_id:** 37466 · **rule:** input-scope · **created:** 2026-08-07T05:03:30Z

**story_summary:**

> In the third year of Jehoiakim king of Judah, Nebuchadnezzar of Babylon besieges Jerusalem; the
> Lord gives Jehoiakim into his hand along with vessels from God's house, which Nebuchadnezzar
> carries to Babylon and places in his own god's treasury. Nebuchadnezzar orders his chief eunuch
> Ashpenaz to select promising young Israelite nobles — among them Daniel, Hananiah, Mishael, and
> Azariah — for three years' training in Babylonian learning, renamed Belteshazzar, Shadrach,
> Meshach, and Abednego, and assigned the king's own food and wine. Daniel resolves not to defile
> himself with that food and, having found favor with Ashpenaz (by God's gift), persuades the
> steward Melzar to test him and his three companions on a ten-day vegetable-and-water diet
> instead. At the test's end the four look better-nourished than the youths who ate the king's
> food, so the steward continues the substitute diet. God gives all four learning and skill, and
> Daniel additionally the gift of understanding visions and dreams; when Nebuchadnezzar examines
> the trainees at the end of their training, he finds the four unmatched by anyone else, ten times
> better than all his magicians and enchanters. Daniel remains in that world until Cyrus's first
> year.

**feasibility_note:**

> The whole chapter is one continuous narrative unit — deportation and vessel-seizure (1-2),
> selection and provisioning (3-7), the test proposed and run (8-16), and its vindication (17-21)
> — with a stable core cast (Daniel and his three companions) tracked continuously from their
> introduction (v6) to the chapter close (v21), and no natural sub-chapter break: every later
> scene depends on the selection established in 3-7 and the test proposed in 8-13. Matches the
> same shape already found in the Dan 8/Jonah 1/Hos 1/Mic 1 visualization — a single scope read as
> a whole, not an algorithmic sub-division. A second, independent read would plausibly reach the
> same call: the chapter has one throughline (the four youths vindicated against the king's
> system), not multiple separable stories.

## HIBs in scope (Step 1 — `hib.set`, live `hib`/`verse_hib` rows, Dan.1.* only)

11 distinct HIBs. (`Daniel`'s full live verse list also includes 17 Dan 8 verses, not shown here —
same person, same row, extended not replaced; this extract is filtered to the Dan 1 scope only.)

| label | kind | verses (Dan 1) |
| --- | --- | --- |
| Nebuchadnezzar | named_individual | 1, 2, 3, 5, 10, 18, 19, 20 |
| Jehoiakim | named_individual | 1, 2 |
| Ashpenaz | named_individual | 3, 7, 9, 10, 18 |
| Melzar (the steward) | named_individual | 11, 12, 13, 14, 15, 16 |
| Daniel | named_individual | 6, 7, 8, 9, 10, 11, 12, 13, 17, 18, 19, 21 |
| Hananiah | named_individual | 6, 7, 11, 19 |
| Mishael | named_individual | 6, 7, 11, 19 |
| Azariah | named_individual | 6, 7, 11, 19 |
| King Cyrus | named_individual | 21 |
| the youths | unnamed_collection | 3, 4, 10, 13, 15 |
| the king's magicians and enchanters | unnamed_collection | 20 |

## Control total this fixes for Step 3 (`phenomenon.set`)

Every HIB × every verse it appears in, above = the exact number of phenomena-register entries
(including explicit "silent" ones) Step 3 must produce before it's done — 11 rows above, sum of
each row's verse count = the total. Nothing here decides what any phenomenon IS; that's Step 3's
own job, not run yet.
