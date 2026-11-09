# #2406 — the aloud collection: the behaviour / inner-being-state split, and what each surface does

Read-only exploration for escalation #2406. Everything the models decided is inferential (B:4); the verse readings in part b are mine and also inferential. Related open items: #2376 (narration, on hold), #2388 (builds the collections), #2379 (surface analysis); nothing here changes them. Sources: `collection` id 138, `collection_link`, `surface_term`, `ai_call`, `cfg_ai_prompt` (`group.word` v3), the `cfg_column` meanings of `surface_term.surface_group` and `group_state`, and the verses of `_analytics/surfaces/exports/collection-members-verses-v2-20261108.csv` (collection `aloud`).

## What the collection holds

Collection `aloud` (id 138, status indicative, opposite pole word `silently`). Member surfaces are the surfaces whose base is a placed base (tier core, synonym or opposite). There are 8, with 153 distinct verses (the export has 172 rows, one per verse and Strong's code; I did not reconcile this with the "approx 157" in your message).

| tier | surface | group | verses |
|---|---|---|---|
| core | aloud | behaviour | 22 |
| synonym | uttered | behaviour | 15 |
| opposite | silence | behaviour | 21 |
| opposite | quiet | inner_being_state | 36 |
| opposite | quieted | inner_being_state | 3 |
| opposite | quietly | inner_being_state | 5 |
| opposite | quietness | inner_being_state | 3 |
| opposite | silent | inner_being_state | 48 |

So behaviour holds 3 surfaces and 58 verses; inner_being_state holds 5 surfaces and 95 verses. The core word and its synonym are behaviour; every opposite is inner_being_state except `silence`.

## a) Why this split, and can it be relied on

**What made the split (checked in the tables).** Each of the 8 surfaces has exactly one group decision: one call of `qwen3:30b` on 2026-11-06 06:30 (9 to 11 seconds each), prompt `group.word` v3, state `judged`. None was corrected or confirmed by the researcher. The prompt gives the model only the English word, with no verse and no collection: behaviour is an act or experience, inner_being_state is a standing condition or characteristic. The prompt asks for a reason only for `other`, so for these 8 the only reasons stored are:
- quiet: "describes a state of calmness or stillness in the inner being"
- quietly: "describes a manner of being, not an action or entity"
- silent: "reflects a state of being, not an action"
- silence: "an act of refraining from speech"

The collection step did not decide any group. `aloud` was built from the in-scope words (behaviour and inner_being_state together are the study of the inner being, per the `surface_group` column meaning), so the split inside the collection is the word-level group label and nothing more.

**Can anything in it be relied on? Not for what this step needs, on the evidence I have.**
1. **The label is a judgement on the bare word, not on how the verses use it.** `silent` is labelled a state, yet in the 48 verses I read all but two or three are acts of keeping silent or commands to be silent ("they kept silent", "be silent", "he remained silent"); the exceptions are the silent stone (Hab 2:19) and the silent dogs (Isa 56:10). `silence` is labelled an act, yet several of its verses are conditions (the land of silence, "sit in silence").
2. **The same base is split in 26% of the table.** Of 711 bases with two or more in-scope surfaces (a full count over `surface_term`), 184 have surfaces in both groups. In this collection `silence` and `silent` share the base `silent` and sit in different groups. Examples from the same count: keep / keeping (behaviour) and kept (inner_being_state); make / makes and made; destroy / destroying and destroyed; sin / sinned and sinful; help / helped and helpless. I looked at 12 of the 184 only; in those 12 the form that goes to inner_being_state is usually a past participle or an adjective. That pattern is inferential and was not tested over all 184.
3. **The label cuts across the collection's own pairing.** The collection pairs aloud with quiet and silent as opposites (speech heard against speech withheld). The label puts the heard side in behaviour and most of the withheld side in inner_being_state, so it does not follow the meaning contrast the collection was built on.
4. **Some of it may carry information.** The label does separate words that name an outward doing (aloud, uttered) from words that name a settled calm (quietness, the quiet of a land or a people). I cannot say how far that holds, because no sample of the group decisions has been checked against the verses.

**For the step before narration:** the group label should not decide on its own whether a surface is engaged in the inner being; the verses should.

## b) One sentence for each of the 8 surfaces

Read from all the verses of each surface (texts in `C:\Users\lerouxc\AppData\Local\Temp\claude\1ed3be72874aa8d4\14d28a94-80d5-4ecc-a20f-b556cfb2642c\scratchpad\aloud-verses.txt`, taken from the export).

- **aloud** (22): marks an inner state of grief, distress, appeal or proclamation as voiced so that others hear it (weeping aloud, crying aloud to the Lord, proclaiming aloud), and once the withholding of it (Eze 24:17, "sigh, but not aloud").
- **uttered** (15): marks what is in a person, or in God, as brought out in words or voice, whether vows, falsehood, rebellion, words not understood, or judgment.
- **silence** (21): marks speech held back, by a person in waiting, grief, awe or submission, or imposed on others, and also the state of the dead ("land of silence").
- **quiet** (36): marks the settled calm of a person, a people, a land or the sea (rest, security, no fear, no strife), and the command to be calm or hold back speech.
- **quieted** (3): marks a person or a crowd made calm by another, or one's own soul calmed and quieted (Psa 131:2).
- **quietly** (5): marks the manner of an act as restrained and unobtrusive, in submission, in doing one's work, in discretion toward another, or in waiting on the Lord.
- **quietness** (3): marks settled rest and trust as the result of righteousness and as the ground of strength, set against toil and striving.
- **silent** (48): marks a person withholding speech, as submission (Isa 53:7), fear or shame (Neh 5:8), awe before the Lord (Zep 1:7), wisdom (Pro 17:28), or obedience to a command, or a failure to speak up (Est 4:14), and God's silence toward a person who calls (Psa 28:1).

## Not done

No change to any table, group or collection and no new AI call. I did not test the label over the whole table against verse use, and I did not decide which of the 8 surfaces a step that checks engagement in the inner being would keep or drop; that is the design of #2406 itself, a decision for you.
