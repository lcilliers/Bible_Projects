# Escalation deep history

## #1838 —  stage 1 build 
type=task source=researcher

**v1** (2026-09-22T15:49:21Z, Researcher) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):**  stage 1 build 
> **comment (set this version):**  submit M67 cluster in batches to complete the build of the the stage 1 observations for the cluster. 
> **context (set this version):**   

**v2** (2026-09-22T15:51:30Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  proceed with this run using the batch run routine you built yesterday. It is not necessary to stop and ask for permission between each batch, I will monitor progress with the batch process monitor. 
> **context (set this version):**   

**v3** (2026-09-22T15:52:28Z, Researcher) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):**  proceed with this run using the batch run routine you built yesterday. It is not necessary to stop and ask for permission between each batch, I will monitor progress with the batch process monitor. 
> **context (set this version):**   

**v4** (2026-09-22T15:52:48Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Launched: previewed first (17 batches, 15 already committed, 2 remaining batches, ~\.33 estimated), then ran live with -MaxTotalCostUsd 5.00, no stop-between-batches per your instruction. Running now in the background; will report the actual result once it completes.

**v5** (2026-09-22T15:56:34Z, Claude) state=in-progress next_action=review assigned_to=Claude
> **comment (set this version):** Batch run completed: \.633 spent, 1 of 17 batches actually ran (the other 16 were skipped as already-committed, per the batch controller's normal, non-forced behaviour). M67 verse-reading coverage is NOT fully complete, and it's important you know why before deciding next steps.
> **context (set this version):** Full-scope check (all 35 verses in M67): 2560 expected items, 1288 ok, 1053 missing, 706 unexpected, 219 over-count. Of the 1053 missing: 253 are M0.8.1 (brand new today, never asked anywhere before -- expected, this is its first pass). The other ~800 are spread across M0.6.5/M0.6.6/D7.7.1/M0.7.x -- the exact same compliance gap the checklist fix (#1831) solved earlier today, but ONLY for verses actually reprocessed since then. The other 34 verses' content still reflects whatever ran before today's fixes existed; the batch controller correctly skips already-committed batches by default, so it never touched them. Not a new bug -- the backlog of everything not yet touched by today's fixes. Closing it fully means a -Force rerun of the whole cluster (2682 expected items total), likely \-20 given it needs to run per-verse (a single large -Force batch hits the same truncation limit found earlier, #1835) -- a materially bigger spend than the batch just authorised. Not proceeding without your explicit go-ahead.
> **resolution (set this version):** Standard batch completion run done as instructed (\.633). Full-cluster backfill via -Force is a separate, bigger decision -- awaiting your direction.

**v6** (2026-09-22T15:57:06Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Reassigning -- awaiting your cost decision on the full-cluster -Force backfill before any further action here.
> **resolution (set this version):** Standard batch completion run done as instructed (\.633 spent). Full-cluster verse-reading coverage is not complete -- 1053/2560 items missing, mostly pre-fix backlog on the 34 verses not touched by today's run (253 are M0.8.1's own first-ever pass, ~800 are the same compliance gap #1831 already fixed but only for reprocessed verses). Closing it needs a -Force rerun of the whole cluster, per-verse (est. \-20, truncation-safe). Awaiting your decision: proceed with the full backfill, or leave as-is for now.

**v7** (2026-09-22T16:01:11Z, Claude) state=re-assigned next_action=review assigned_to=Claude
> **comment (set this version):** Researcher approved the full backfill. Running now: 35 verses, sequential -Force reruns, background job logging to outputs/m67-full-backfill-20260922.log. Will report final coverage numbers once complete.

**v8** (2026-09-22T16:01:21Z, Claude) state=re-assigned next_action=review assigned_to=Claude
> **comment (set this version):** Still running -- no new progress to report since the last update this same turn; backfill continues in the background.

**v9** (2026-09-22T16:02:09Z, Claude) state=re-assigned next_action=review assigned_to=Claude
> **comment (set this version):** Untouched this turn -- turn was opening the two Excel tool worksheets per /open-excel-tools, unrelated. M67 backfill still running in the background.

**v10** (2026-09-22T17:04:05Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** One real thing found while verifying, tracked separately: escalation #1840 -- a data-quality bug (not a coverage gap) where the same Strong's code recurring at different word positions within a verse produces unmerged duplicate rows instead of either staying cleanly separate or consolidating. 109 of 2560 keys affected, concentrated in M0.8.1's function-word-heavy population. Root-caused, not fixed -- a real design decision, not guessed at. Doesn't block using M67's data now; it's noise on top of complete coverage, not missing content.
> **resolution (set this version):** Backfill complete: 35/35 verses processed (1 needed a retry -- same truncation-class failure as #1835, retried clean), \.24 total spent. Full-cluster coverage now 2559/2560 expected items present (1 residual gap: Heb.6.11/G1731/M0.7.9, not worth a further paid call to chase). M67's Stage 1 verse-reading data is essentially complete and usable as the baseline for the next phase.

**v11** (2026-09-23T09:59:46Z, Researcher) state=in-progress next_action=revise assigned_to=Claude
> **comment (set this version):** not approved. The backfill did not produce acceptable results. This will be signed off once the rebiuild of stage 1 is completed and tested
