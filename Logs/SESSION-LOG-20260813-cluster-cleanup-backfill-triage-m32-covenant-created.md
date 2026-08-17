# SESSION LOG — 2026-08-13 — cluster taxonomy cleanup (M10b/M10c/M27/T2/T3), backfill-scope triage taxonomy, 1,000 backfill promotions, M32 Covenant cluster created, `report.cluster` findability fixes

Started as ad hoc cluster cleanup ("outside the app's structured operations," researcher's own
framing), grew into a real backfill-onboarding pass with 1,007 new `word`-origin strongs and a new
cluster. Closes on a methodology correction that governs the next phase.

## 1. M10b/M10c — near-empty stub clusters, traced and repopulated (BUILD.md n/a — outside-pipeline data work)

M10b had 1 strong, M10c had 3-4, despite rich `cluster.gloss` definitions — M10's own top-meanings
were full of exactly that vocabulary (abomination/wicked/unclean/defilement). Traced the cause:
IBA's cluster taxonomy inherited the old `bible_research.db`'s M10/M10b/M10c three-way split via
`old-system-migration`, but that split had already been reversed once, in the old system, by the
researcher's own 2026-06-23 ruling (`_apply_merge_m10bc_into_m10_20260623.py`: "the three-way split
was an artificial linear-partition"). The 2026-08-11 LLM allocation pass flagged the ambiguity
itself but never resolved it — every wickedness/defilement-shaped term got tie-broken toward parent
M10 (`"precedent conflict: M10[P1]; M10b[P2] | accepted"`, repeated).

Researcher chose **Option B** (repopulate, not re-merge). §7 of the review doc gave a refined split
after also pulling M27's full membership (it was a genuine grab-bag: moral-quality words that
overlap M10b, plus idolatry, plus ruin/devastation — three different senses under one label).
**Applied: 57 relocations** (27 M10→M10b, 14 M27→M10b, 15 M10→M10c, 1 M27→M10c), M27's Group
2/3 (idolatry, ruin/violence) and several ambiguous side-findings left untouched on instruction.
Snapshot `iba-20260813T024400Z-manual-cluster-relocation-m10bc-20260813.db`.

Full write-up: `iba/app/reports/m10bc-cluster-review-20260813.md`.

## 2. T2/T3 operation-verb cleanup — 13 more relocations

Researcher: move generic action-words that landed in a specific M-cluster (or T2) over to T3.
Checked all 304 `cluster_strong.operation=1` rows outside T3 by hand rather than moving on the flag
alone — 249 were genuinely cluster-specific and stayed (e.g. "to fear" in M01). **13 moved**,
including a notable one found by checking sibling variants first: `H7725G/I/J/K` ("to return"/
"turn back"/"again"/"pay", 850 combined freq) were sitting in M11 (Repentance) on a weak precedent
tie, while the actual repentance-sense sibling `H7725O` was already correctly in M45 — confirming
G/I/J/K were the plain physical-motion senses, misfiled. T2 itself had nothing to move (only 10
"to be" copula variants, correctly non-operation). Snapshot
`iba-20260813T072620Z-manual-cluster-relocation-t3ops-20260813.db`.

## 3. `report.cluster` — backfill vocabulary typed, not just counted (BUILD.md §110)

Researcher: analyse the ~9,562 untagged `backfill`-origin strongs with stem/type heuristics,
without hiding outliers behind a bare count. New `backfill_typology` section in
`lib/clusterreport.py`: structural typing (proper nouns 33%, grammatical markers 1%, closed-class
1% — all correctly out of scope) leaves a 65% "candidate vocabulary" residual, cross-matched
word-for-word (fixed a substring false-positive risk — "Devil"/"evil" — found during the M10b/M10c
pass) against every cluster's own gloss vocabulary. 1,117 hits tabulated by cluster; the 5,110
non-matching remainder stem-grouped, plus all 310 items at count≥100 listed individually. 3 new
CSVs persist full row-level detail (`_write_csv_direct()`, filesystem-only — not yet registered in
`cfg_report_csv_table`). No new `cfg_setting` rows either; 5 tunables run on Python defaults.

## 4. Multi-strong span → cluster co-occurrence — a new analytical lens (exploratory, not built into the app)

Researcher's idea: spans carrying 2+ Strong's codes, mapped to their clusters' co-occurrence, might
show real cross-cluster association. First pass hit a real artifact — a naive union-of-tags count
made M03↔M27 look like the top pairing, entirely driven by one dual-tagged code (`H7451I`) sitting
alone in a span, not two different words co-occurring. Fixed (cross-cluster pairs only from two
*distinct* Strong's codes) and it evaporated. Corrected result: **M15 (Wisdom) ↔ M47
(Constitution): 19 spans**, the strongest genuine M–M pairing, plus two clean idioms the cluster
split doesn't represent as one unit (M21↔M33 = "ask peace" = "greet"; M26↔M30 = "guard the
charge"). Honest scale caveat stated in the report: this is a reading list, not yet statistics.

**Follow-up question, answered with data:** is M47 (Constitution) structurally like T3? Tested
directly — M47 (37 members, smallest-class cluster) has more distinct cross-cluster partners (19)
than any other M-cluster including ones 4-5× its size, zero own-doublet cohesion, and connects to
other clusters at 8-20× T2/T3's own per-member rate. Confirmed: M47 is the noun/seat side of the
same phenomenon T3 is the verb/operation side of ("wise of **heart**", "bitter of **soul**"), but
NOT literally T3 — left as an open architectural question, not resolved (its vocabulary is
arguably the most central naming of the inner being the whole programme studies, a real argument
*against* treating it as a utility bucket). Researcher: no change for now.

Both write-ups: `iba/app/reports/span-multistrong-cluster-cooccurrence-20260813.md`.

## 5. Backfill-scope triage — a 4-type taxonomy, from 3 hand-picked examples

Researcher picked 3 backfill content strongs, asked to see each one's verse-lexical context —
produced 4 different needed actions from 3 examples:

1. **Missing term** (circumcision family, 4 strongs, zero `word_registry` entry at all) — needs
   full `New-Word.ps1` onboarding, not a cluster-tag shortcut.
2. **STEP/Gal 5:6 claim — checked, not actually a bug.** `Step.call3_strong` (the endpoint the
   pipeline itself uses) returns Gal 5:6 among G0203's 17 verses; the raw per-verse STEP tagging
   agrees. What's inconsistent is `call2_getInfo`'s dictionary-style `mediumDef`, which only cites
   2 illustrative example refs, not a verse list — almost certainly what looked like "missing."
3. **G0240 "one another" → M44, real pipeline gap.** Read `strongreconcile.reconcile()` end to
   end: T2-classified backfill never promotes; T3 promotes with no word-link required ("T3 is
   inherently not word-specific," researcher's own words in the code comment); any real M-cluster
   classification requires a `word_strong` link or `reconcile()` refuses and it sits as a silent
   exception forever. G0240 is thematically M44 but structurally rides along with whatever verb is
   in view, same shape as T3 — three options laid out, none decided (left as-is per instruction).
4. **G0166 "eternal" → T2**, not M25 as first guessed — researcher corrected this one directly;
   the DB already had precedent (`H5769G`/`G0165H`, both "forever/eternity" already T2).

Write-up + the 4-type taxonomy table: `iba/app/reports/backfill-scope-triage-20260813.md`.

## 6. Types 1-3 actioned; type 4 left as-is — 1,007 new `word`-origin strongs

Researcher: "action 1-3... including where needed the full pulls." Ran the registered
`cluster.assign -Step Assign` sweep first (free, safe, idempotent) — found **zero** new matches,
confirming its exact-gloss-string precedent matcher has real recall limits against this pool.

- **Type 2 (424 strongs) → T2**, plain tag, no promotion (T2 never promotes).
- **Type 3 (1,150 strongs) → T3**, tagged then promoted via a fresh `-Step Assign` run (the real,
  registered mechanism, not a hand-rolled copy of it) — **1,000 promoted**, ~150 correctly held
  back by the pipeline's own sibling-conflict safety check.
- **Type 1 (circumcision)** — `New-Word.ps1`. Hit the app's own new-word approval gate
  (`registry.create pause-continue`); answered via `Escalation.ps1 -Action Answer -Word
  circumcision -Decision Yes` (escalation 641) since it directly executed what was already
  authorized, then resumed. STEP's own seed-search surfaced 8 related strongs (word id 185), not
  just the 4 originally found — but didn't surface `G0203`/`G0564` ("uncircumcision"/
  "uncircumcised") at all, so those two were linked in and origin-flipped by hand to close the loop
  on the exact pair that started this thread.

Snapshots: `iba-20260813T091056Z-manual-backfill-type2type3-tag-20260813.db`,
`iba-20260813T092701Z-manual-circumcision-family-completion-20260813.db`. `strong.origin='word'`:
3,769 → 4,769 (batch) → 4,776 (after the manual G0203/G0564 fix).

## 7. M32 Covenant — new cluster, filling the M32 taxonomy gap

Researcher: "circumcision will go to covenant cluster." No Covenant cluster existed; M32 was one
of two known gaps in the old numbering (M32/M40, per the 2026-08-11 obslog). Created `M32`
("Covenant and Circumcision"), moved 9 strongs: the 5 circumcision-family nouns left unclassified
after §6, plus 4 verb forms (`G4059`/`H4135A`/`H4135B` "to circumcise", `G1986` "to uncircumcise")
that had been sitting in T3 as generic operations before Covenant existed to hold them properly —
moving them now is the same move as §2's T3 cleanup, just newly possible. **Not moved, flagged
instead:** `G2699` "mutilation" (Phil 3:2's pejorative wordplay against circumcision) — left in M07
(Shame), a rhetorical-insult sense, not plain circumcision vocabulary; researcher's call if it
should move too. Snapshot `iba-20260813T103228Z-manual-create-m32-covenant-20260813.db`.

## 8. `report.cluster` — every per-cluster table sorted by `cluster_code` (BUILD.md §111)

Researcher: "difficult to find [a cluster] in the report. sort by cluster code." Three tables were
count-sorted (word-origin count, all-origin summary + its meaning subsections, backfill-crossmatch
hits-by-cluster) — changed all three `ORDER BY`/sort-keys to `cluster_code`. Per-*strong* tables
(gap list, closed-class list, crossmatch hits, residual outliers) correctly left count-sorted —
this was specifically about one-row-per-cluster tables.

## 9. `USER-GUIDE.md` — a real, total documentation gap closed

Researcher noticed `Cluster-Report.ps1` wasn't listed anywhere the guide documents commands.
Checked: **neither `Cluster-Report.ps1` nor `Cluster-Assign.ps1` were mentioned anywhere in the
whole file** — the entire cluster taxonomy/assignment mechanism (built 2026-08-11/12) had never
been documented. Added new §12g (full documentation of both tools, including the exact-match
matcher's low-recall caveat and a pointer to §5/§6's worked example), plus both commands added to
the §14 cheat-sheet and the §16 file inventory. Doc-only, no `BUILD.md` entry (no code/config
changed).

## Closing correction — governs the next phase

Researcher, reviewing the final report: **"I don't think we must auto re-assign the backfills.
this will have to take place as part of the analysis so the context can play its part."** Accepted
today's state as a checkpoint ("for now the cluster report is ok, although I can see a lot of
potential anomalies") but the anomalies are to be worked through **as part of verse-context
analysis going forward, not via another bulk classification pass**. Recorded as
`feedback_iba_backfill_cluster_assignment_via_analysis_not_bulk_automation` (project memory) — the
default answer to "clean up more backfill" from here is analysis-driven, not another
crossmatch/tag script, unless the researcher says otherwise.

## Left open, not silently dropped

- **5 circumcision-family strongs' cluster tag** was resolved this session (→ M32) — no longer
  open.
- **`G2699` "mutilation"** — left in M07, not moved to M32; researcher's call (§7).
- **G0240 "one another" / M44 word-link policy** (§5 point 3) — three options on the table, none
  chosen. Blocks any future M-cluster-but-word-independent backfill item from actually promoting
  until decided.
- **The ~5,000-item backfill residual** (Type-1/2/3 non-matches) — explicitly NOT a queue for more
  automation per the closing correction above; belongs to the analysis pipeline, not this thread.
- **`backfill_typology` section's 5 tunables + 3 CSVs** — not yet registered in `cfg_setting`/
  `cfg_report_csv_table`; noted as a formalise-later item in `BUILD.md` §110, still true.
- **M27/M10b description overlap** (M27 renamed candidate: "Idolatry, Ruin and Violence") —
  surfaced in §1's review, never actioned; description still reads "Evil, Wickedness and
  Abomination," near-duplicate of M10b's.

## Files touched (this session)

**New code:** none (no new `.py` modules — `clusterreport.py`'s `backfill_typology` section and
`_write_csv_direct()` helper are additions to an existing file, §3/§8).

**Modified code:** `iba/app/lib/clusterreport.py` (`backfill_typology` section + CSV writes, §3;
3 `ORDER BY`/sort-key changes, §8).

**Docs:** `iba/app/USER-GUIDE.md` (new §12g; §14/§16 updated, §9); `iba/app/BUILD.md` (§110, §111);
`iba/app/reports/m10bc-cluster-review-20260813.md`,
`iba/app/reports/span-multistrong-cluster-cooccurrence-20260813.md`,
`iba/app/reports/backfill-scope-triage-20260813.md` (new); `cluster-v3` through `cluster-v8`
(regenerated `report.cluster` runs across the session).

**Schema:** none (no new tables/columns — `cluster` gained a data row, M32, not a schema change).

**Config:** none via `configmaint.propose` this session — everything in §1/§2/§3/§6/§7/§8 was
direct ad hoc data work per the researcher's own "outside the app's structured operations"
framing at the start of the thread, snapshotted throughout, not routed through the formal
approval-gated config flow. §3's new report-rendering tunables and CSV registrations are the one
explicitly-flagged item that *should* eventually go through `configmaint.propose` if kept.

**Data:** `cluster` (+1 row: M32); `cluster_strong` (57 + 13 + 1,574 + 9 = 1,653 relocations/new
tags across §1/§2/§6/§7, net `cluster_strong` active rows now 7,391); `strong.origin`
(3,769 → 4,776 word-origin, +1,007: 1,000 via §6's T3 promotion cascade + 5 circumcision-family
nouns + 2 manually-fixed G0203/G0564 = 1,007); `word_registry` (+1: circumcision, id 185);
`word_strong` (+10: circumcision's 8 discovered seeds + G0203 + G0564).

**DB snapshots (5, all in `iba/app/db/snapshots/`):**
`iba-20260813T024400Z-manual-cluster-relocation-m10bc-20260813.db`,
`iba-20260813T072620Z-manual-cluster-relocation-t3ops-20260813.db`,
`iba-20260813T091056Z-manual-backfill-type2type3-tag-20260813.db`,
`iba-20260813T092701Z-manual-circumcision-family-completion-20260813.db`,
`iba-20260813T103228Z-manual-create-m32-covenant-20260813.db`.

**Memory:** `feedback_iba_backfill_cluster_assignment_via_analysis_not_bulk_automation.md` (new).

## Next

Nothing queued as a hard next-step — researcher: "will work on those as we progress." The closing
correction is the operative constraint for whatever comes next: backfill cluster assignment rides
on analysis work, not a standalone pass. G0240's word-link policy question (§5.3) is the one small
decision that would unblock a specific future case if it comes up again.
