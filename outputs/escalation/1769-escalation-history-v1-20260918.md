# Escalation deep history

## #1769 — Filler/placeholder obs_text not caught by validation
type=issue source=researcher

**v1** (2026-09-18T14:06:43Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Filler/placeholder obs_text not caught by validation
> **comment (set this version):** Found during a systematic quality sweep across the corpus (researcher's request, this chat turn: check completeness/quality/purpose/orphans/inconsistencies). One observation (id 4655, M83, strong G3212, stage=verse-reading, question_code=D7.7.1) has obs_text='placeholder' and meaning_source='n/a' -- both literal filler values, zero ib_node grounding. recordingpass.py's own InvalidObservationText check (_DEGENERATE_OBS_TEXT regex) only catches 'none/n-a/null/nothing/-' patterns -- 'placeholder' doesn't match, so it wrote cleanly with no rejection.
> **context (set this version):** Low volume today (1 of several thousand observations checked), but same CLASS of gap as #1765's grounding issue -- a content-less write the validation layer was specifically built to catch, missing a pattern. Not building a fix this turn (researcher asked for escalations to dig into separately, not auto-fixes) -- proposed direction: broaden the regex/heuristic to also catch generic filler tokens (placeholder, todo, tbd, xxx, lorem ipsum, etc.), or consider a length+substance heuristic instead of an enumerated pattern list, which is more future-proof against a filler word this list doesn't anticipate.

**v2** (2026-09-18T17:09:57Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  proceed to investigate per your discovery 
> **context (set this version):**   
