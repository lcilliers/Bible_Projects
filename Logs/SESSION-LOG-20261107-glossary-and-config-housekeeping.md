# Session log 2026-11-07: glossary and config housekeeping

Session id: d41a94c7-0638-41c1-9edf-a1bc3177d568 (standard mode, 2026-11-06 to 2026-11-07)

## 1. Scope

Start routine (STEP started, compliance file); then #2364 (cfg coherence), #2357 (config housekeeping), the programme glossary and its currency check (#2367), the approved config changes, and the supersession of the three surface-cycle streams.

## 2. Escalations

- #2364: resolved (self_correctable); validation re-run showed no coherence errors.
- #2357: updated v14 to v19 (options, outcomes, the researcher's messages); open with the researcher (item 6 ruling).
- #2367: raised, worked, built; completed (v10).
- #2368 raised (whole-cluster reading rules, on hold); #2369 to #2371, #2373, #2374, #2375 raised as proposals, approved, applied, completed.
- #2372 raised (surface group: prompt says entity, data says being), with the researcher.
- #2361: completed on the researcher's instruction.
- #2376 (Rebuild narrative) and #2377 (Assemble narration chapter scope) raised; #2354, #2360, #2359 superseded.
- #2363 left open on hold, as instructed.

## 3. Files

- iba/app/lib/cfgquality.py, iba/app/handlers/configmaint.py, iba/app/lib/cfgreport.py (glossary currency check)
- iba/app/BUILD.md (section 467), iba/app/USER-GUIDE.md (section 4)
- iba/docs/ps tools worksheet.xlsx (Node-Resolve tab and Index row)
- archive/patches/wa-prose-glossary-surface-terms-v1-20261106.json (applied: 8 entries in database/bible_research.db prose_section 1128 to 1135)
- outputs/escalation/2357-config-housekeeping-options-v1-20261106.md; outputs/escalation/2367-glossary-check-design-v2-20261106.md; outputs/escalation/2367-glossary-surface-term-entries-v1-20261106.md; outputs/escalation/archive/2367-glossary-check-design-v1-20261106.md
- Logs/compliance/COMPLIANCE-20261106-d41a94c7.md; generated reports (config report, escalation list and audit, session-close report)

## 4. Decisions

- Researcher: the glossary is not config and Claude keeps it up to date without per-entry approval; recorded as rule B:126 in cfg_behaviour_rule (#2373 v4) and its scope link (#2375 v4).
- Researcher: flag a draft-only glossary entry in the check; recorded in iba/app/BUILD.md section 467 and #2367 v9.
- Researcher: delete ollama.max_codes_per_call; recorded in #2369 v4.
- Researcher: whole-cluster reading rules will change, kept as a setting; recorded in #2368 v1.
- Researcher: supersede #2354, #2360, #2359 by #2376 and #2377; recorded in #2377 v2.
- Researcher: close #2361; recorded in #2361 v24.
- Claude, self-correctable: the first #2367 finding (no glossary home) was wrong and corrected; recorded in #2367 v3 and outputs/escalation/2367-glossary-check-design-v2-20261106.md.
- Claude: noderesolve and surfacebase marked config_exempt after reading them; recorded in #2370 v4 and #2371 v4.

## 5. Open items

- #2357 (researcher): item 6 ruling on narrativeregister.py hand-built version names.
- #2368 (researcher): rules for whole-cluster reading, on hold.
- #2372 (researcher): entity vs being in the group prompt.
- #2376, #2377 (researcher): scope and work packages for the narrative rebuild and the chapter scope.
- #2363 (Claude, on hold): until the analytics of the chapter scopes are set.
- #2365 (researcher): six spine gaps unverified while STEP was down; STEP is up now, re-check not yet run.
- #2357 (researcher): all 15 glossary entries of the currency check are draft; the check lists them until approved.

## 6. Git

(written after the first commit)
