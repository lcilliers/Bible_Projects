# Escalation deep history

## #2262 — Gap analysis counts any observation as read
type=issue source=researcher

**v1** (2026-10-24T04:56:06Z, Claude) state=raised next_action=review assigned_to=Claude
> **short description (set this version):** Gap analysis counts any observation as read
> **comment (set this version):** From #2260 (findings outputs/escalation/2260-observation-quality-findings-v1-20261024.md section 3). iba/app/lib/versecollate.py lines 166-170 mark a verse not read only when it has no observation of any kind and no strand face; iba/app/lib/reading.py (lines 50, 184-189) builds the gap JSON from the same test and marks verses analysed on it. No quality test: whether each M-code word occurrence has its Stage 1 word-level and relational answers, whether the observation names the word, is single-verse, carries a role. Presence counts are reported as coverage (e.g. outputs/escalation/2161-m72-reading-plan-v2-20261024.md section 2).
> **context (set this version):** outputs/escalation/2260-observation-quality-findings-v1-20261024.md

**v2** (2026-10-24T05:28:07Z, Claude) state=on-hold next_action=review assigned_to=Claude
> **comment (set this version):** Carried by the design proposed on #2268 (outputs/escalation/2268-reading-process-against-study-expectations-v1-20261024.md, gaps table). On hold until the researcher decides #2268; no separate fix is built for this item (B:105).

**v3** (2026-10-27T05:27:31Z, Claude) state=completed next_action=review assigned_to=Claude
> **comment (set this version):** Researcher, chat 2026-10-27 (verbatim): 'you can do the same with 2262 - 2267 they are all about capturing the observations from the files which are all essentially completed.'
> **resolution (set this version):** Closed on the researcher's instruction, chat 2026-10-27 (verbatim): 'they are all about capturing the observations from the files which are all essentially completed.' No separate fix was built under this item.
