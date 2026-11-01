# Escalation deep history

## #2347 — Close the study backlog, set up next phase
type=task source=researcher

**v1** (2026-11-01T09:03:35Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **short description (set this version):** Close the study backlog, set up next phase
> **comment (set this version):** Researcher, verbatim, session 389101b8, 2026-11-01: "after many turns we finally came to the end of a long journey of trying to systematically analyse all the verses in the study.  This turns out to be an unachievable objective within the scope of limited budget and AI's inability to come up with a method that sensibly can achieve the objective. in this session I will close all the open and on hold escalations and lay the foundation for the next phase of the study". Claude: plan (disposition of each open and parked escalation, then foundation for the next phase) sent to the researcher for approval before any closing (B:17).

**v2** (2026-11-01T14:07:29Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Researcher messages, verbatim, session 389101b8, 2026-11-01 (recorded at session close):
1. "you can register the local llm" (09:17) -- registrations proposed as #2348 and #2349; later put on hold, see 5.
2. "2345 yes;  2340 text approved; 2337 set on hold." (09:21) -- #2345 carries into the next phase; the #2340 rule text approved; #2337 on hold.
3. "threads: option A" (09:23) -- the 20 on-hold threads withdrawn, not superseded (superseding needs a successor).
4. "all the on hold threads can be closed down as superseded. non of the threads is relevant for the next phase, although the mechanism may still be used." (09:23)
5. "I am not ready to deal with 2350, 2349, and 2348 - the local llm deployment is on hold." (09:25) -- #2348, #2349, #2350 set on hold.
6. "Option A." (13:56) -- #2322 advisory findings acknowledged, clean-up left to the next phase (closed on #2322 v5).
7. "2341 ? did you read that or just work from memory" (13:58) -- Claude had not read #2341 in full; corrected in chat.
8. "remove the two live errors, they are not needed and does not need an escalation to reopen 2341" (14:03) -- iba/app/staging/pilot_local_llm moved to iba/app/staging/archive/pilot_local_llm; Validate shows no coherence error.
9. A question on why a SELECT over escalation ordered by id DESC seems not to sort (14:04): answered in chat; the query sorts correctly in iba/app/db/iba.db, so the cause is the query tool's display.
