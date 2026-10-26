# #2298 bulk run: all 80 M clusters mapped by surface (#2286 U8)

Date: 2026-10-26. Escalation #2298. Developer Mode session 3646374f. Run live through
`iba/app/ps/Surface-Map.ps1` (Pairs, Apply, Tail, Check) after the pilot was accepted (#2298 v5:
P1 a, P2 a, P3). Facts are from live `iba/app/db/iba.db` and the API usage log. **Every placement made
in session is my judgement (inferential); every API placement is the model's, also inferential.**

## 1. What is now in the tables

| measure | value |
|---|---|
| M clusters mapped | **80 of 80**: no unallocated pair, no stale pair |
| (code, surface) pairs | 13,411 in `surface_subgroup` |
| placed in session (Claude) | 4,218: the head of every cluster, the corrections, and the empty-surface pairs |
| placed by the API | 9,025 (the tail) |
| inherited (B5) | 168: M49 41, M83 104, M67 23. M67's 24th inherited pair was corrected (G3636 "trouble") |
| subgroups | 396 of kind `group`, 5 `qualifier`, 80 `not_this_sense`, 80 `anomaly` |
| two-sense pairs | 108 |
| anomaly group | **147 pairs**, to clear by hand (M72 26; M23, M45, M65 9 each; M58 8; the rest 5 or fewer) |

**Checks after the run:**
- `Cluster-Assign.ps1 -Step Validate` (RUN-20261026_060633_626): the surface mapping shows 0 stale
  pairs, 0 partly mapped clusters and none unmapped. The older findings are within the baseline
  approved on #1707.
- `Config-Maintenance.ps1 -Step Validate` (RUN-20261026_060633_900): ok, identical to #2270.

**What this changes for reading.** The U4 gate (#2294, G-a) refused every M cluster until it was
mapped. As of now no M cluster has an unallocated or stale pair, so `Reading.ps1 -Step Open` no
longer refuses on mapping.

## 2. The qualifier groups (E4, B3)

These five groups mostly qualify something else, so they are never opened as a home scope:
- M18 "good, better, well";
- M05 "good, better, right";
- M34 forever, ever, always (duration);
- M46 abundance, many, great (quantity);
- M58 "bad" (*ra'* as a quality).

## 3. Time and cost

| item | value |
|---|---|
| pilot (on a copy, 2026-10-25) | $0.65 |
| live API tail calls (2026-10-26) | 79 calls, **$10.82** (1,032,095 tokens in, 514,688 out). The 79 are one per cluster, less M49 and M83 (fully inherited, no tail), plus one refused M11 call |
| largest single call | M47, 359 pairs, 21,778 output tokens, $0.44 (ceiling 32,000, cap $1.00) |
| system clock | 404 `cluster-surface-map` runs from 04:12:52 to 06:05:32 UTC (the `run` table): 1 h 53 min for 80 clusters, session pass included |

## 4. Faults found and fixed during the run (my own, self-corrected under B:44, recorded on #2298)

| # | fault | fix |
|---|---|---|
| F6 | `-Cluster` was upper-cased, so `M10c` became `M10C`, which is not a cluster | `iba/app/handlers/surfacemap.py` `_cluster` looks the code up without case and uses the table's spelling |
| F7 | M11's API reply put a sentence before its JSON with no code fence, so the reply was refused whole ($0.10 spent, nothing written) | `parse_tail` takes the outermost `{…}` when the reply does not parse whole. Test T7g added; U3 suite 31 of 33 (the 2 others by design) |
| F8 | my scratch runner read `Surface-Map.ps1`'s output from the pipeline, but the script writes to the host, so the runner stopped after each preview (M03 to M05) | runner simplified to call the four steps and rely on the steps' own refusals. A scratch tool, not part of the app |

**Found, not fixed (a design choice, B:105):** #2301. `run.py` snapshots iba.db before every run and
prunes to `retention.snapshot_keep_count` (5), so the named pre-run snapshots of #2292 to #2298 are
gone. For the rest of the bulk run I set the documented loop escape `IBA_NO_SNAPSHOT=1` and kept one
copy outside the pruned folder (the scratchpad, after M13). Everything the run wrote is new rows in
`surface_subgroup` and new `cluster_subgroup` rows, each with its run id.

## 5. How the session pass was done

- **Per cluster:** I read the head pairs (code, surface, hits, gloss, two sample references), set the
  groups by the sense the renderings carry, and placed each pair, giving a reason for every exception.
  The specs are in `outputs/escalation/2298-bulk-files/` (21 files, one per batch).
- **`not_this_sense`:** every cluster has one. It holds what the cluster's codes carry that is not
  its sense. Examples:
  - literal height in M08 Pride;
  - *nuach* "put", "set" and "laid" in M33 Rest;
  - *mashal* "proverb" in M35 Being Tested;
  - the rooster's crowing in M84.

  These stay in the cluster, untouched (B:70); the reading meets them as context.
- **Two-sense:** a pair was flagged where one rendering clearly carries two senses across its verses,
  for example *ṭôb* "good", *ra'ah* "displeased" and *kasah* "covered".

**Limit.** The API's 9,025 tail placements were not reviewed pair by pair. Only M18's were, in the
pilot. They are provisional (C3), and the claims step moves a pair with its reason (B:122).

## 6. For your decision

| # | point | facts | options | my recommendation *(inferential)* | your answer |
|---|---|---|---|---|---|
| Q1 | The bulk mapping | section 1 | accept / amend | | |
| Q2 | Clearing the 147 anomaly pairs (B2) | they are mostly particles, numerals, pronouns, names and stray marks the API could not place. M72's 26 are on the king and reign words ("indeed", "years", "thirty-three", "he", "^") | a) Claude clears them in session as one unit, each to a group or `not_this_sense` with a reason, through Apply files. b) you clear them. c) leave them until a reading meets them | a | |
| Q3 | The size check (D1: flag a group over 30%) | **72 groups in 65 clusters** are over 30%. Almost always it is the cluster's core sense, carried by its main word: M51 love 96%, M21 asking 77%, M32 covenant 76%, M54 law 71%, M78 servant 73%. The 30% was set on M18, whose largest group held 24% | a) keep 30% and read the flags as "the core sense", splitting none. b) name the clusters you want split. c) change the check, for example flag only a group holding several codes, or raise the share | a, with the list kept in each cluster's check report; the reading of a large core group is itself segmented by scope (S1, RM-03) | |
| Q4 | #2301, snapshots pruned by run snapshots | section 4 | on #2301 | | |
