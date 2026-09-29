# M02 unit 2: where the tokens went, and what to change

**Date:** 2026-09-29 · **Author:** Claude Code · **Status:** proposal for the researcher's decision (escalation raised alongside). Nothing has been changed yet.
**Source:** this session's own transcript (`~/.claude/projects/C--Bible-study-projects/8db5e0f3-….jsonl`), usage fields summed across 238 model calls. The token counts are exact. The cost shares are approximate: they use Anthropic's standard price ratios (cache read = 0.1× input, cache write = 1.25×, output = 5×).

## 1. What the numbers show

| Token type | Tokens | Share of cost (approx.) |
|---|---:|---:|
| Cache reads (the conversation re-read on every call) | 82,637,402 | **~63%** |
| Output (what I wrote) | 656,367 | ~25% |
| Cache writes (new material added to the conversation) | 1,224,886 | ~12% |
| Fresh input | 476 | ~0% |

**The conversation grew too large.**

| Quarter of the session | Average context per call | Output tokens |
|---|---:|---:|
| 1 (start-up, part A) | 122k | 72k |
| 2 (part A write-up, part B reading) | 285k | 210k |
| 3 (part B write-up, part C reading) | 442k | 245k |
| 4 (part C write-up) | 553k | 129k |

- **A call late in the session cost about 4.5× a call at the start**, because the whole conversation, including every verse printed during parts A and B, is re-read on every call. The peak was 584k tokens.
- **Once a verse is printed into the conversation, it is paid for again on every later call.**

## 2. Adjustments, ranked by expected saving

1. **One part per session, not three.** This is the largest saving, and it costs nothing in quality.
   - Close the session after each part: the handoff, commit and escalation are already written each time. Start the next part fresh from the handoff.
   - Part C would then have run at about the start-of-session context (~120k) instead of 450–550k.
   - **Expected: cache reads roughly halved or better for a three-part unit.**
2. **Keep bulk verse text out of the main conversation.**
   - **(a)** The context reader writes to a file. I then read the file in small pieces, and my working notes (already kept in a file) become the only thing carried forward.
   - **(b)** Or a subagent reads each chunk of ~30 verses and returns its notes. Its context is thrown away afterwards, so the verse text is never carried.
     - The catch: the subagent's reading is a second-hand reading, and it would need the method briefing each time.
     - **Option (b) needs your approval.** This project's standing practice is not to spawn subagents unasked.
3. **Merge overlapping context windows.** Neighbouring targets printed the same passage several times:
   - Deu 29:20–28 printed 4 times
   - Jer 32:29–32 printed 4 times
   - Lam 2:1–6 printed 5 times

   **The reader should print each passage once, marking every target in it.** This is a small script change, and it cuts the reading volume by roughly a quarter to a third.
4. **Tier the reading.** Many divine-side verses are formulas:
   - "the anger of the Lord was kindled against Israel"
   - "provoking me to anger with the work of their hands"
   - the Kings and Jeremiah series

   **Read these as verse-only, in a list, and give full context only to verses where a human speaks, acts or is described**: all B3/B6/B7, and divine verses whose context has a human response. This is a method change, so it is yours to rule on. It trades some context reading for speed on verses where context rarely changed the phenomenon.
5. **Write shorter.** Output was about a quarter of the cost.
   - The unit-2 document is about 1,800 lines, and it quotes almost every verse at length, although the ledger already holds each verse's text.
   - **A cap would halve the output with little loss:** two or three key quotations per phenomenon, and a verse list for the rest.
   - Keep each part as its own file and consolidate once, rather than re-issuing the whole document as v1 → v2 → v3.
6. **Make the tools permanent.**
   - The context reader and the citation finder were rebuilt from scratch this session (the unit-1 versions were lost with the scratchpad). The finder then needed two bug fixes, each followed by a full re-check.
   - **Registering them as utilities** (`governance.new_utility_registration_timing` requires this for anything reused) removes the rebuild and the re-checking.
   - The finder could also build its index once and save it, instead of re-parsing every batch file on every call.
7. **Smaller items:**
   - **The escalation stop-hook added a turn after most answers** while #1891 sat with Claude. It is now reassigned, so this stops.
   - The mechanical steps (extracts, counts, citation look-ups) could run on a cheaper model. The reading itself should stay on the current model.

## 3. What I suggest doing first

- **Adopt now, as simple and with no change to the method:** 1 (a session per part), 3 (merged windows) and 6 (register the two tools).
- **Rule on:** 2 (and whether a subagent is acceptable), 4 (tiered reading) and 5 (a length cap for the write-up).
- **Together, 1 and 3 alone should cut a unit of this size by well over half.**
