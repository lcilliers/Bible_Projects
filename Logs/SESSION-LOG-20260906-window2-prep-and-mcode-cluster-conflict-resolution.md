# Session Log — 2026-09-05/06 — Window 2 prep work + M-code cluster conflict resolution (and a late-session data-trust breakdown)

**Date:** 2026-09-05 into 2026-09-06 (one continuous session crossing midnight).
**Scope, one line:** Window 2 (HIB/IB) methodology consolidation and proposal work on escalation
#737; a Layer-1 `verse_lexical` conformance investigation on #1527 that found and fixed a real
weight/quality defect in `resolved_sense`; a long cluster-membership-quality investigation on
#1525 that resolved all 675 M-code double-tagging conflicts to zero via nine successive
resolution passes; and a late-session error (using a retracted table, `candidate_seed`, as if
live) that the researcher caught, corrected, and is right to distrust — logged honestly below, not
smoothed over.

---

## Escalations touched

- **#737** (IBA Debate-Pipeline / Window 2 methodology) — v11→v14. Produced the preparatory-work
  consolidation, the cluster-based methodology proposal (corrected once for deleted-record
  inclusion), a ranked opinion on cluster-submission-success criteria, and the cluster-size
  theory/assessment. Left `ready_for_approval` / with the researcher; not resolved this session.
- **#1524** (validate catalogue questions against Window 1 evidence) — raised, then held pending
  #737's own open items rather than worked blind. Still open.
- **#1525** (cluster membership/readiness evaluation) — the largest thread this session, v1→v17.
  First pass wrongly asserted "membership sound" and framed Layer-2 non-coverage as a blocker; both
  retracted on direct researcher correction. Became the home for the entire M-code duplicate-tag
  investigation: 675 double-tagged strongs found, resolved to **0** across nine passes (old-migration
  conflicts, self-duplicates, four whole-cluster merges, title-match, synonym-match, review_flag,
  heuristic-wins). `ready_for_approval` for the researcher to close.
- **#1526** (reading-strategy vs. cluster-size findings) — raised, a session-pacing/consistency
  proposal filed. One finding (the M58/M10b duplicate) was raised here in error and explicitly
  moved to #1525 per researcher correction ("fixing clusters belongs to 1525 not 1526"). Still open.
- **#1527** (Layer 1 `resolved_sense` conformance) — raised, root-caused directly in
  `lib/lexical.py` (not guessed), corrected per explicit researcher instruction ("I do not trust
  fixes... back to basics") into a pure specification document with no reconciliation, then a
  second document itemizing Layer 1/Layer 2 by value produced from the actual design-decision
  documents. The fix itself (see below) was then designed, validated small, and run corpus-wide.
  `ready_for_approval`.
- **#1528** (`cfg_table.inactive` not set for retracted candidate tables) — raised after the
  `candidate_seed` error (below), expanded from 2 to 3 affected tables
  (`candidate_seed`/`span_candidate`/`lemma_inventory`) by a corrected detection query, three
  `configmaint.propose` runs filed and correctly left un-self-approved. `ready_for_approval`.

## Files created or changed

**Documents (`iba/docs/`):**
- `737-window2-preparatory-work-consolidation-v1-20260905.md`
- `737-window2-cluster-based-methodology-proposal-v1-20260905.md` (corrected in place for
  deleted-record inclusion)
- `737-cluster-submission-success-criteria-opinion-v1-20260906.md`
- `737-cluster-size-theory-and-assessment-v1-20260906.md`
- `1525-cluster-membership-readiness-evaluation-v1-20260906.md` (corrected in place twice)
- `1526-session-pacing-consistency-proposal-v1-20260906.md`
- `1527-layer1-verse-lexical-definition-reference-v1-20260906.md`
- `1527-layer1-layer2-specification-by-value-v1-20260906.md`

**Analytics extracts (`_analytics/clusters/`):**
- `M42-Prayer-Petition/m42-layer1-full-extract-v1-20260906.jsonl` (regenerated once after the
  first attempt was written as one broken 54MB single line)
- `M46-Wealth-Riches/m46-layer1-full-extract-v1-20260906.jsonl`,
  `m46-mcode-surface-report-v1-20260906.md`
- `m-code-conflicts-241-remaining-v1-20260906.csv` through `-remaining-v4-20260906.csv` (four
  successive snapshots as the conflict count fell 241→208→145→134)

**Code:**
- `iba/app/lib/lexical.py` — `resolved_sense` no longer duplicates the raw `stepGloss` dictionary
  dump; scoped to M-code cluster members only (`load_mcode_strongs`, new); `gloss_consistent_in_verse`
  repointed to key on `surface` instead of `resolved_sense` (the latter is a pure function of
  `(strong, morph_code)` with no per-occurrence signal, so the old check could never fire).

**Migrations (`iba/app/migration/`, all one-off, `cluster`/`cluster_strong` `category='data'`,
`writer='migration'` regime, each backed up first):**
`retire_m10b_into_m58_v1_20260906.py` · `resolved_sense_mcode_only_v1_20260906.py` ·
`retire_old_migration_mcode_conflicts_v1_20260906.py` ·
`resolve_old_migration_self_duplicates_v1_20260906.py` · `merge_m29_into_m18_v1_20260906.py` ·
`merge_m38_into_m45_v1_20260906.py` · `merge_m17_into_m16_v1_20260906.py` ·
`merge_m27_into_m55_v1_20260906.py` · `resolve_mcode_conflicts_by_name_match_v1_20260906.py` ·
`resolve_mcode_conflicts_synonym_match_v1_20260906.py` ·
`resolve_mcode_conflicts_review_flag_v1_20260906.py` ·
`resolve_mcode_conflicts_heuristic_wins_v1_20260906.py`

**`iba/app/BUILD.md`** — entries #237–#248, one per migration above plus the corpus-wide
`resolved_sense` rebuild.

**`iba/app/db/iba.db`** — live data changes: M10b/M29/M38/M17/M27 retired (merged into
M58/M18/M45/M16/M55 respectively); 675→0 M-code double-tagged strongs; 532,747 `verse_lexical`
rows rebuilt under the corrected `resolved_sense`/`gloss_consistent_in_verse` logic. Nine `.bak`
snapshots taken before each write pass, named `iba.db.pre-1525-*`/`pre-1527-*`.

## Decisions made

**Researcher's own decisions** (not self-correctable, made explicitly by the researcher):
- Retire M10b→keep M58; merge M29→M18, M38→M45, M17→M16, M27→M55 (each a specific
  keep/retire direction the researcher named directly).
- `gloss_consistent_in_verse` keys on `surface`, not `resolved_sense` (a decision the researcher
  said was made previously; applied and recorded here).
- `resolved_sense` scoped to M-code words only, not T-code — explicit researcher diagnosis and
  instruction, including the "I do not want a compromised resolved_sense" framing that shaped the
  fix design.
- The 21-strong self-duplicate list — full per-strong keep ruling given directly (cluster B in
  every case except `G4993`).
- The final 120-strong batch — "heuristic-family-grouping item wins, the other one goes."

**Claude's own calls, flagged as such at the time, not attributed to the researcher:**
- `G0611`/`H6032` "to answer" resolved to `M41 Being Heard` rather than the researcher's named
  `M42` target, because `M42` wasn't one of those two codes' actual conflicting options.
- The title-match/corpus-score/synonym-match tiered methods used to resolve the 22+11-strong
  blocks were Claude's own design, corrected once live after the researcher pointed out the first
  version's flat gloss-corpus scoring gave `M22`/`M42` an artificial tie on "song."

## The late-session error — logged honestly

Investigating a "how many strongs lack a cluster" question, Claude used `candidate_seed` as the
reference "curated word-origin pool" and reported 21 gaps. The researcher pushed back hard,
correctly: `candidate_seed`'s entire operational subsystem was retracted 2026-07-23 (confirmed in
`cfg_candidate_rule`'s own live row and in BUILD.md), but `cfg_table.inactive` was never flipped
for `candidate_seed` itself — so Claude's own "is this table active" check came back clean and
gave false confidence in month-old, dead data. A second wrong table (`word_strong` misuse) and a
confused re-derivation followed before the researcher's own domain knowledge (`strong.origin`
'word'/'backfill' as the real signal) got the investigation back on solid ground — though even
that ended with unresolved loose threads (1,311 `origin='word'` strongs with no `word_strong`
link; 29 `word_strong`-linked strongs that are `origin='backfill'`; 408 `verse_lexical` strongs
missing from `strong` entirely) that the researcher was not able to reconcile against prior work
believed to have already anchored "the raw data is complete." **The researcher ended the thread
concluding something is still wrong and asked to start fresh next session rather than keep
re-deriving trust turn by turn.** The one thing that did come out of this cleanly is escalation
#1528 (the `cfg_table.inactive` governance gap, genuinely real and now filed with three pending
fixes) — but the underlying "is the raw data actually complete" question itself is **not**
resolved and should not be assumed answered by anything in this session.

## Open items carried into next session

1. **Re-establish "is the raw data complete" from scratch** — from whatever originally anchored
   that conclusion, not from any number produced in this session's last hour.
2. Escalations #737, #1524, #1525, #1526, #1527, #1528 all still open, `ready_for_approval` or
   awaiting direction where noted above.
3. #1528's three `configmaint.propose` runs awaiting researcher approval (run_ids in the
   escalation's own resolution field).
4. #1528 item 3 (a standing `configmaint.validate` check for retracted-but-unflagged tables) not
   yet built.
5. The 1,311 / 29 / 408 counts from the late-session investigation — unresolved, flagged, not
   trusted by either party as final.

## Git state

Committed and pushed, branch `main`: commit `e07edaa2d40dff72df3ec1a5093123bffb891169`
(2026-09-06 17:46:15 +0100), pushed `4eb5403e..e07edaa2` to `origin/main`. `git status` clean
afterward. One push warning, not a block: `_analytics/Clusters/M42-Prayer-Petition/m42-layer1-
full-extract-v1-20260906.jsonl` is 54.41MB, over GitHub's *recommended* 50MB (not the 100MB hard
limit that has blocked pushes before) — worth trimming or moving to Git LFS at some point, not
urgent.
