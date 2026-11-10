# Escalation deep history

## #2437 — Attach multi-word phrases to a collected head word
type=task source=researcher

**v1** (2026-11-10T13:07:04Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Attach multi-word phrases to a collected head word
> **comment (set this version):** Researcher (verbatim): 'the multi word bases should all be associated with anther base that is already in a collection, if not, why not.' then 'yes, create this as an escalation so we can close this session'. Finding: 1166 phrases (788 inner_being_state, 378 behaviour) are in no collection. In the base step (iba/app/lib/surfaceresolve.py line 66) a phrase is marked phrase_not_tested and is its own base; nothing links it to a head word, and the collection steps ran on single-word bases only. A rough exact-word match (small words skipped, no stemming): 788 phrases contain a word placed or shared in a collection; 237 only words that are listed_only or set_aside; 112 only words with an empty state (out of scope or other group); 29 no word matching a surface (inflected forms such as blotted out). To decide, as a new design to come to the researcher first: a step that finds the head word of each phrase (with inflection handled) and attaches the phrase to that word's collection, how phrases whose head word is out of scope or only listed are treated, and whether phrases then go through Engagement with that collection. Not designed or built yet.
