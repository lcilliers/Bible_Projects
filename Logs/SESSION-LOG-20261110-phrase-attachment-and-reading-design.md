# Session log 2026-11-10 -- Phrases attached to collections, collections confirmed, reading by collections designed

Session: `77a059b4-65ef-4409-8675-22c064cc23f7` (standard mode, started 2026-11-10 13:09 UTC)

## 1. Scope

2026-11-10. Escalation #2437: the 1166 multi-word phrases of collection a were connected to collections (English-word route for all, own-Strong's-code route for the 249 the first route does not reach), with the leftovers flagged for inspection; built and run live in standard mode. All 277 collections were set `confirmed`. Escalations #2436, #2447, #2392, #2366, #2368, #2379, #2357 were settled or closed on the researcher's instructions. #2448 (the final reading based on observations by collection) was designed (v1 approved, v2 awaiting) and put on hold until #2412 (engagement on the collections) is completed; #2412 continues in a separate chat.

## 2. Escalations

- #2437 raised-then-worked v2 to v18: decisions D1 to D4, E1 to E4 and the Strong's route recorded verbatim, step built, run live, closed (completed, v18).
- #2438 to #2442 (step collection.attach_phrases, its refusal route, tier phrase, flag kind phrase_no_match, event action attach_phrase): proposed, approved, applied, completed. #2443 and #2444 withdrawn (a proposal of mine carried an empty value; nothing applied). #2445 and #2446 (recorded meaning of the tier and flag-kind columns): applied, completed.
- #2449 (Validate: 2 value-quality errors): resolved as self_correctable; #2450 to #2454 (enum rows gathered, gather, relink, unlink, engagement_no_verses): approved, applied, completed.
- #2455 (retire reading.whole_cluster_reading_start): applied, completed.
- #2436 closed (A, A, A applied); #2447 raised and closed (structure evidence refreshed, 11 base changes applied).
- #2392, #2366, #2368, #2379, #2357 closed on the researcher's instructions.
- #2448 raised, designed (v1, v2), put on hold (v9); #2412 updated v21 (carried to a separate chat).

## 3. Files

- Code: `iba/app/lib/collectionbuild.py` (`attach_phrases`), `iba/app/handlers/collectionbuild.py`, `iba/app/ps/Collection-Build.ps1` (`-Action AttachPhrases`).
- Documents: `iba/app/BUILD.md` (entry 480), `iba/app/USER-GUIDE.md` (AttachPhrases paragraph), `iba/docs/ps tools worksheet.xlsx` (new tab Engagement; AttachPhrases in the Collection-Build action hint).
- Outputs (`outputs/escalation/`): `2437-phrase-attachment-step-design-v2-20261110.md`, `2437-phrase-attachment-detail-v2-20261110.csv`, `2437-phrase-no-match-v1-20261110.csv`, `2448-reading-by-collections-survey-v1-20261110.md`, `2448-reading-by-collections-design-v1-20261110.md`, `2448-reading-by-collections-design-v2-20261110.md`; superseded versions in `outputs/escalation/archive/`.
- Data (`iba/app/db/iba.db`): 3134 `collection_link` rows of tier phrase on 1094 phrases; 72 open `surface_flag` rows (phrase_no_match); 277 collections confirmed (277 `surface_event` rows, action confirm); 81 base changes and 5 repoint corrections, then 11 further base changes and 52 evidence rows added, 89 superseded; the five enum rows, the on_fail row, the step row and the retired setting through `configmaint.propose`.
- Run state: `Logs/compliance/COMPLIANCE-20261110-77a059b4.md`; `iba/app/reports/session-close-v332-20261110.md`.

## 4. Decisions

- Researcher: attach every phrase that matches a collection ("all the phrases that have a match to a collection must simply be connected"): recorded in #2437 v9 and `iba/app/BUILD.md` entry 480.
- Researcher: no new table, a phrase is linked to a collection or not (E2): recorded in #2437 v10.
- Researcher: add the Strong's route, only for the 249 no English word reaches: recorded in #2437 v12 and v13.
- Researcher: accept E3 and E4, build in standard mode: recorded in #2437 v14 and #2438 v3.
- Researcher: all 277 collections confirmed ("Yes, confirm all"): recorded in the 277 `surface_event` rows (action confirm) and #2412 v21.
- Researcher: #2436 A, A, A (observation 20534 kept, 13 verse-less members kept, previews applied): recorded in #2436 v4 and #2447 v3.
- Researcher: #2392, #2366, #2368, #2379 closed; #2357 approved (versioning acknowledged until the narrative is rebuilt): recorded in #2392 v8, #2366 v4, #2368 v3, #2379 v13, #2357 v25.
- Researcher: the final reading is based on observations by collection; design C1 to C7 approved; #2448 on hold until #2412 is completed: recorded in #2448 v4, v7, v9.
- Claude, self_correctable: registered the enum values stored earlier today and not registered (gathered, gather, relink, unlink, engagement_no_verses) after Validate found them; recorded in #2449 v2 and #2450 to #2454.
- Claude, self_correctable: two proposals with an empty value withdrawn and re-proposed; recorded in #2443 v2, #2444 v2 (withdrawn) and #2445 v4, #2446 v4.
- Claude: the Strong's route is noisy for shared codes (each link's reason names the code and the word); recorded in #2437 v18 and `iba/app/BUILD.md` entry 480.

## 5. Open items

- #2412: engagement on the collections, with the researcher; continues in a separate chat (the Ollama test after 9am).
- #2448: on hold until #2412 is completed; design v2 (including the migration to rebuild the reading table, standard mode asked) is unanswered.
- #2456: the 72 phrases flagged phrase_no_match, for the researcher to inspect.
- #2457: stored verse counts below STEP's counts for H1431, G4433, G5219 and H1396, not explained (Claude).
- #2458: SC16 counts a hook refusal as a script failure (Claude).
- #2376, #2377 and #2387 stay parked.

## 6. Git

(written after the first commit)
