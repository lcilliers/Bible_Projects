# Escalation deep history

## #1847 — Small pre-existing node-level duplicate citations
type=issue source=researcher

**v1** (2026-09-22T20:18:19Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Small pre-existing node-level duplicate citations
> **comment (set this version):** Found while verifying #1846: 2 verses (2Cor.8.16, 2Pet.1.5) have observations that are correctly consolidated at the observation level (1 canonical row each) but still carry 2 ib_node rows citing the IDENTICAL occurrence underneath -- residue from earlier today's #1832/#1834 dedup rework (created 11:19-12:31, before that fix's final form). Not a live bug -- newer runs don't add more (confirmed: today's 20:57 run touched both verses again and added zero new duplicate nodes, the skip-if-already-cited check works). This is cosmetic clutter (double-citation of the same word), not a wrong finding. Worth a small one-time cleanup pass (dedupe identical ib_node rows sharing the same observation_id+strong+verse_reference+surface+morph_code, keep one) once you'd like it done -- not urgent, small scope. Not building without your call, per the no-offline-script-touches-old-data principle (#1824 Fix 3) -- this would need to go through a real rerun or a narrowly-scoped, reviewed migration.
> **context (set this version):** Scale unknown corpus-wide -- only found by chance while spot-checking #1846's output. Could scope-check the full extent if useful before deciding.

**v2** (2026-09-23T08:39:29Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  this should wash out with reruns after sorting out the questions and code handling the interpretation 
> **context (set this version):**   

**v3** (2026-09-23T08:45:13Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Checking your expectation ('this should wash out with reruns') against what I just verified for the unrelated #1856 case: it won't wash out on its own. fully_covered_verse_ids treats a verse as done once every expected item has a live node, with no check for staleness -- so 2Cor.8.16 and 2Pet.1.5 won't get re-touched by a normal rerun unless something else already has a reason to rerun that verse. The dedup CODE itself is already fixed (#1832/#1834) -- this is only 2 known verses with residual duplicate ib_node rows under an already-consolidated observation, not a live bug, not corpus-wide. Given the tiny scale, my recommendation is to leave it rather than spend a forced rerun solely to clear it -- flagging honestly rather than letting 'should wash out' stand uncorrected.
> **resolution (set this version):** No fix applied -- recommending leave-as-is given the negligible scale (2 known verses, not a live bug). Your call to approve that or ask for a targeted -Force clear.

**v4** (2026-09-23T08:58:45Z, Claude) state=in-progress next_action=review assigned_to=Researcher
> **comment (set this version):** Corrected my prior handling -- actually investigated instead of recommending leave-as-is. Real scope: 27 duplicate groups across the 2 verses (not 2 rows), ~30 redundant ib_node rows, all under already-correct observations. Confirmed a reread will NOT clear this (ib_node has no soft-delete column, and record_one_observation only skips re-adding a node when one exists -- it never removes existing redundant ones). Fix is fully scoped and ready: iba/app/migration/dedupe_ib_node_2verses_v1_20260923.py, keeps earliest node per duplicate group, deletes the rest. Not yet run -- this is a physical DELETE (no soft-delete field exists on this table, unlike every other fix today), so I want your explicit yes before running it, not a judgement call I'm punting for lack of a decision.
> **resolution (set this version):** Migration written and ready, not yet executed. Awaiting go-ahead specifically because it's a physical delete.
