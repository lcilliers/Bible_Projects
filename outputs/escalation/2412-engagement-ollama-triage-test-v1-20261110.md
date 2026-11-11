# #2412 — Ollama triage test v1 (model against Claude's reading)

Basis: sample of 334 items (seed 2412, up to 15 for each collection and truth class) from the 4636 items Claude assessed in seven collections (aloud, call, deal, new, anger, godly, choose), reopen decisions applied. Prompts engagement.triage v1 (A) and engagement.triage_b v1 (B), model qwen3:30b, `ai_call` rows module engagementask. All model answers are inferential (B:4). Items answered by both prompts: 30 of 334 (9%).

## Prompt A alone

- Claude bearing, model bearing: 15; Claude bearing, model none (a miss): 0
- Claude none, model none: 0; Claude none, model bearing (an over-read): 15
- agreement on bearing versus none: 15 of 30 (50%); misses 0 of 15 (0%) of Claude's bearing items; over-reads 15 of 15 (100%) of Claude's none items

## Prompt B alone

- Claude bearing, model bearing: 15; Claude bearing, model none (a miss): 0
- Claude none, model none: 0; Claude none, model bearing (an over-read): 15
- agreement on bearing versus none: 15 of 30 (50%); misses 0 of 15 (0%) of Claude's bearing items; over-reads 15 of 15 (100%) of Claude's none items

## The two prompts together

- same three-way answer: 26 of 30 (87%); same bearing-or-none: 30 of 30 (100%)
- where they agree on bearing-or-none, the answer matches Claude: 15 of 30 (50%)
- where both say none, Claude also says none: 0 of 0
- the 0 items they differ on would go to Claude's reading

## By Claude's class (prompt A answers)

| Claude | inner_being | outward_act | none |
|---|---|---|---|
| relevant (4) | 3 | 1 | 0 |
| bears_on (11) | 3 | 8 | 0 |
| none (15) | 7 | 8 | 0 |

## By collection (bearing versus none, prompt A)

| collection | items | agree |
|---|---|---|
| aloud | 30 | 15 of 30 (50%) |

## Disagreements with Claude (15 items; first 60)

| collection | surface | vl_id | Claude | A | B | Claude's reason | model's quote (A) |
|---|---|---|---|---|---|---|---|
| aloud | aloud | 1378464 | none | outward_act | outward_act | A herald's public proclamation of a decree; no inner operation. | the herald proclaimed aloud,  |
| aloud | aloud | 1313584 | none | outward_act | outward_act | A summons to the armies with a signal; no inner operation. | cry aloud to them |
| aloud | quiet | 1207912 | none | inner_being | inner_being | The realm of Jehoshaphat was quiet: the state of a realm. | So the realm of Jehoshaphat was quiet, for his God gave him rest all around. |
| aloud | aloud | 1378800 | none | outward_act | outward_act | A proclaimed order to cut down the tree in the vision; no inner operation. | proclaimed aloud and said thus: |
| aloud | silence | 1236284 | none | outward_act | inner_being | Whether Job's babble can silence men: outward silencing, no inner operation. | Should your babble silence men, |
| aloud | silence | 1519743 | none | inner_being | inner_being | Silence in heaven for half an hour: a described hush; no inner operation is named. | there was silence in heaven for about half an hour. |
| aloud | silent | 1440586 | none | inner_being | inner_being | Zechariah to be silent and unable to speak: an imposed muteness as sign. | you will be silent and unable to speak until the day that these things take place, because you did not believe my words, which will be fulfilled in their time. |
| aloud | quiet | 1344170 | none | inner_being | inner_being | 'How can it be quiet when the Lord has given it a charge': the sword again. | How can it be quiet when the Lord has given it a charge? |
| aloud | silence | 1103896 | none | outward_act | outward_act | A command to be silent so Ehud can speak privately: outward command. | And he commanded, “ Silence.” And all his attendants went out from his presence. |
| aloud | quiet | 1180270 | none | outward_act | outward_act | The city was quiet after Athaliah's death: the state of a city. | the city was quiet after Athaliah had been put to death with the sword at the king’s house. |
| aloud | quiet | 1319604 | none | inner_being | inner_being | The sword of the Lord asked to be quiet: a figure for a weapon. | Ah, sword of the Lord! How long till you are quiet? |
| aloud | uttered | 1321353 | none | outward_act | outward_act | The words the Lord uttered against the land; a divine pronouncement, no human inner operation. | I will bring upon that land all the words that I have uttered against it, everything written in this book, which Jeremiah prophesied against all the nations. |
| aloud | silence | 1272293 | none | inner_being | inner_being | The land of silence: death, not an inner operation. | my soul would soon have lived in the land of silence. |
| aloud | uttered | 1262882 | none | outward_act | outward_act | The judgments God uttered: a divine pronouncement remembered; no inner operation. | his miracles, and the judgments he uttered, |
| aloud | quiet | 1311310 | none | inner_being | inner_being | 'Quiet resting places': places. | quiet resting places |
