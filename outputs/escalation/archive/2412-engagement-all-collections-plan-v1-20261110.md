# #2412 — engagement on all collections, run without a break (plan v1)

Basis: the researcher's instruction of 2026-11-10 (quoted below); the engagement process as run on aloud, call, deal, new, anger, godly and choose (`iba/app/USER-GUIDE.md` 8.18; `outputs/escalation/2406-engagement-step-design-v3-20261109.md`); read-only counts from `iba/app/db/iba.db` taken 2026-11-10 (scripts in the session scratchpad). The cost figures are my estimates from file sizes, inferential (B:4).

## The instruction (researcher, verbatim)

> "next is 2412. it seems that you are really successful with the engagement and I think you can proceed without having to break between each collection. Can you run it in batches or in a loop to prepare all the observations and isolate all the surfaces that is not part of inner being as per the process you have been following up to now. the collections are still being prepared and there are 20 to go and will be completed in approx 4 hours."

## What the tables show (read 2026-11-10)

- 260 live collections: 6 fully engaged (aloud, call, choose, deal, godly, new), 24 partly (through surfaces shared with an engaged collection, or one surface such as enrage that has no verse), 229 not started, 1 with no member surface (supply).
- 1,781 member surfaces; 69,167 distinct verse items among them; 4,599 already assessed; **64,568 still to assess**. Per collection among those still to do: median 184 items, 90th percentile 976, largest saying 7,122, then instruct 2,204, die 2,198, build 1,880, share 1,858.
- The collection build is running (`Logs/longrun/collection-batch.progress.json`): 200 of 223 sub-groups done, 18 left, estimated finish 08:40 today. Its newest links can add member surfaces to a collection; engagement is per surface, so a late surface is assessed afterwards without redoing the rest.

## What a loop can and cannot do

The app steps (Pull, Record, Group, Review, Close, Check) are mechanical and can be chained. The assessment itself is my reading of each verse, with a reason, and no script can do it (the Ollama route was abandoned by the researcher on 2026-11-09). So the loop is me working through the collections one after another in this session, with no stop between collections, in chunks inside a collection as for call and godly. A subagent per collection adds nothing for sequential writing and raises the chance of a locked database.

## Cost (B:20), inferential

From the files of call (833 items): the pull file was 1.1 MB (about 330 tokens an item to read), the assessment 357 KB (about 105 tokens an item to write), the review 84 KB. For 64,568 items that is roughly 20 million tokens read and 7 million written, plus the reviews, over many hours and several context compactions. It is a large run, not a light one. Two things lower it without changing the method: (1) read a leaner view of the pull (surface, reference, text, existing observations of the verse) rather than the full file, and (2) take the largest collections last, so that the number of collections done at any stop is as high as possible.

## Order and rhythm

1. The 24 partly engaged collections first (only their remaining surfaces).
2. The not-started collections from the smallest to the largest by items; the collections whose build is still running last within their size.
3. After each collection: Pull, assess in chunks, Record -Check then Record, Group -Check then Group, Review, Close, Check; one line of result per collection appended to #2412 and nothing else in chat.
4. A surface that leaves the study group (group `other`) is raised by the app as one escalation per collection and is never unlinked (R4, the researcher's rule of 2026-11-09): this is how the surfaces that are not part of the inner being are isolated. I decide none of them; they accumulate as decision items for the researcher.
5. A collection that looks malformed is raised as a question on the collection, as the process requires, and the run goes on to the next.

## Risks

- **Database lock.** My writes (Record, Group, Close) are short single transactions, but the build failed on M77_stumbling with `database is locked` on 2026-11-08, the moment a session was writing. Each of my writes may collide with the build's. I retry a refused write once after a pause and record it; the researcher may prefer to hold writes until the build ends at about 08:40.
- **Context.** The session compacts as it works; each collection's state is in the tables and its working files, so a resume starts from `Engagement.ps1 -Action Check`.
- **Volume of decisions.** If many surfaces leave the group the escalation list grows quickly; one escalation per collection, as the app does.
