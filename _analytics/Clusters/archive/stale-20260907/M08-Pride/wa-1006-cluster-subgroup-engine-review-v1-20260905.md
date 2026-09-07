# Escalation #1006 — review: the cluster → sub-group "engine," what it does, what it produces

**2026-09-05.** Direct instruction on #1006: *"cluster analysis is now reinstated. First review and
report on the cluster -> sub group engine in existence, remind me what it does and what does it
produce."* Investigated the live schema and every writer of it in `scripts/`/`archive/scripts/`
before answering — not restated from memory or from the #1005 synthesis alone.

## Headline: there is no single engine — it's ~15 bespoke, now-archived, per-cluster load scripts

Searched every non-archived and archived script for writes to `cluster_finding`/
`characteristic_subgroup`/`characteristic` and found no generic, reusable, currently-runnable
pipeline. What exists is a family of one-off scripts, one (sometimes several) per cluster, each
named for that cluster and phase — `_apply_m01_phase11_findings_load_20260516.py`,
`_apply_m04...`, `_apply_m08_dir024_phase9_findings_v1_20260512.py`, and so on — **every one of
them now in `archive/scripts/`**, none runnable as a standing tool today. `scripts/apply_session_
patch.py` (the live, general patch applier) recognises `CLUSTERING` only as a patch-TYPE label in
its exemption lists — it has no actual handler that writes `cluster_finding`/`cluster_subgroup`
rows. There is one still-non-archived, genuinely reusable utility,
`scripts/_apply_generic_characteristic_backfill_20260527.py` — see §3.

## 1. The schema (bible_research.db, live, all read-only checked just now)

```
cluster (49 rows: M01-M47 + FLAG + T2)
  └─ characteristic (277 rows) ── characteristic_subgroup (146 rows) ──┐
  └─ cluster_subgroup (175 rows) ─────────────────────────────────────┘
       └─ cluster_finding (19,997 rows)   -- the actual analytical findings
       └─ cluster_observation (276 rows)  -- cross-cluster/cross-phase notes
```

- **`cluster`** — one row per M-code, static reference (code/description/gloss/bucket/status).
- **`characteristic`** — a cluster's own named characteristics (e.g. M08/Pride's "Arrogant
  self-elevation," "Presumptuous defiance," ...), one row per characteristic, sequenced
  (`char_seq`).
- **`cluster_subgroup`** — a coarser bucket a characteristic can map into (`subgroup_code`/`label`/
  `core_description`), scoped to a cluster.
- **`characteristic_subgroup`** — the M:N link between the two, carrying `is_partial`/
  `partial_register_note` for a characteristic that only partly belongs to a sub-group.
- **`cluster_finding`** — one row per analytical finding: `finding_text`, tagged to `cluster_code`
  always, `characteristic_id`/`cluster_subgroup_id` when assigned, `vcg_scope` (which verse-context
  group it's about), `finding_status`, `source_file` (the markdown it was loaded from).
- **`cluster_observation`** — cross-cutting notes (e.g. M08's confirmed cross-cluster observations
  pointing at M22/M23, named in the #1005 synthesis) — `observation_type`/`source_phase`/
  `target_phase`/`status`/`resolution_note`.

## 2. What actually produced the 19,997 `cluster_finding` rows

`cluster_finding.source_file` (110 distinct values, all real, all checked) resolves overwhelmingly
to hand-authored per-characteristic markdown under `Sessions/Session_Clusters/{CLUSTER}/`, e.g.:

```
Sessions/Session_Clusters/M04/WA-M04-phase9-char1-Exultation-findings-v1-20260518.md
Sessions/Session_Clusters/M08/files phase 9/wa-cluster-M08-phase9-char1-Arrogant-self-elevation-findings-v1-20260521.md
```

The actual analytical work — reading verses, writing the finding — was Claude AI prose, one
markdown file per characteristic, per the old Session C-era pipeline (CLAUDE.md §8's "Phase 3
DB sync" step, pre-dating both the 2026-06-25 method reset and the 2026-08-15 IBA split). A
bespoke, cluster-named `_apply_..._phase9/10/11_findings_*.py` script then parsed that cluster's
own markdown files and inserted the rows — one script per cluster (occasionally per phase within a
cluster), never a shared parser. All of them are now in `archive/scripts/`, none runnable
standing-tool-style today; running one again would need un-archiving it and checking it still
matches the live schema (not attempted — out of scope for a review).

## 3. The one exception: a real, still-live, generic (but narrow) utility

`scripts/_apply_generic_characteristic_backfill_20260527.py` (not archived) — for exactly 9 named
pre-v2.6 legacy clusters (M01, M02, M05, M06, M15, M20, M26, M39, M46) that had `cluster_subgroup`
rows but no `characteristic` rows yet, it auto-derives a 1:1 characteristic per substantive
sub-group (excluding `*-BOUNDARY`), inserts the `characteristic_subgroup` link, and backfills
`cluster_finding.characteristic_id` for findings already tied to that sub-group. Idempotent per
cluster (aborts a cluster that already has characteristic rows), per-cluster transactions. This is
the closest thing to a real "engine" in the system — but it's a one-time migration-gap backfill for
a named, closed list of clusters, not an ongoing mechanism for new work.

## 4. What it produces, in practice — the actual coverage today

| measure | value |
|---|---|
| clusters with ≥1 `characteristic` row | 35 of 49 |
| clusters with ≥1 `cluster_finding` row | **15 of 49** |
| `cluster_finding` rows total | 19,997 |
| — with a `characteristic_id` | 17,662 (88%) |
| — with a `cluster_subgroup_id` | **7,282 (36%)** — 12,715 (64%) have none |
| `finding_status` breakdown | `finding` 16,284 · `silent` 1,806 · `cluster_synthesis` 1,784 · `gap` 123 |

So: the mechanism (when it ran) produced a genuine per-verse-group analytical finding, tagged to a
cluster and usually a characteristic — but the finer sub-group tag is the minority case (36%), and
the whole apparatus only ever ran to completion for 15 of the 49 clusters. This matches the #1005
synthesis's own point (b)/(c) directly: not finished, and not just a collation problem — M08's own
June-21 pass, for instance, was confirmed loaded only to its "bare characteristic definitions,"
its actual analytical substance from that pass never having gone through a load script at all.

## 5a. Follow-up (2026-09-05, same day): the "loosely grouped strongs" the researcher recalled

Direct follow-up: *"a while ago... when we were doing debates, you grouped the strongs in a
cluster loosely into sub groups... put your hand on those scripts to see if they have any
reusable logic."* Found — this is a different, separate mechanism from §1-4 above (which is the
OLD `bible_research.db` characteristic/sub-group system). This one is genuinely from the windows-
debate week (2026-08-11 to 08-13): the register's own W10 names it directly — *"Loosely
gloss-coupled groupings as workspaces"* (`iba/docs/windows debate/WA-inner-being-windows-register-
v2_3-2026-08-12.md`).

**Live and reusable: `iba/app/lib/clusterassign.py`, `match_precedent()`.** Built 2026-08-12
(`iba/app/reports/cluster-assign-build-spec-20260812.md`), still wired into `raw.py`'s backfill
path and the new-word chain, not archived. What it does: given a code's STEP gloss, exact-string
match (trimmed, case-insensitive, never substring) against either **P1** an existing
`cluster_strong`-linked code's own gloss, or **P2** a cluster's own worked-example gloss list
(`cluster.gloss`). Only returns a match when it resolves to exactly ONE cluster — a gloss that
matches two clusters at once is a conflict, deliberately left unresolved rather than guessed.
Config-driven exclusion of `FLAG`'s gloss list from voting (it's an uncertainty bag, not a
signal). This is genuinely reusable as-is for a **cluster_subgroup** classification pass too — the
same technique (exact gloss precedent, single-match-only) would apply unchanged if pointed at
`cluster_subgroup`/`characteristic_subgroup` instead of `cluster`/`cluster_strong`.

**What is NOT recoverable: the graded/"loose" half.** The same 2026-08-11 session also used a
TF-IDF profile scorer to RANK candidates for the harder, ambiguous middle tier (this is where
scores like the M10bc review's `"M10:7.4, M27:7.1, M10b:6.7"` came from). The session log records
it explicitly rejected for confident auto-assignment (*"too noisy... mis-fired on short glosses,
wanted 'brother' → Deceit"*) and kept only as a sorting aid for human review. Searched every
non-archived and archived script for it — **it was never saved as reusable code**, only its
one-time output survives, baked into the `wa-global-cluster-alloc-medium/low-*.json` files under
`iba/docs/cluster assignment process/`. If a graded/ranked (not just binary-match) sub-grouping
pass is wanted, that scorer would need re-building, not recovering.

## 5b. Actually run against M08 (2026-09-05, same day) — result

Direct follow-up: *"can we take a cluster like m08 and subgroup with this tool. show me the
result."* Ran it, both literally and in a deliberately permissive variant of the same principle,
against M08's real 87 strongs (`iba.db`) and its real 8 `cluster_subgroup` rows (`bible_research.db`,
A1/A2/A3/A4/B/C/D/E, `wa-m08-1005...` pilot's "5 characteristics/8 sub-groups").

**Attempt 1 — the tool exactly as built.** `match_precedent`'s P2 parser expects `cluster.gloss`'s
own shape: `"term (translit), term (translit), ..."`. Run against M08's subgroup `label`/
`core_description` text, it does not fail cleanly — it "parses," but what it extracts is fragments
of prose (`"; the king's heart not to be raised above his brothers"`, `"char-1 split"`), not gloss
terms, because that text is analytical description, not a worked-example list. **Not usable as-is,
and not a bug to fix** — feeding it through anyway would need the subgroup descriptions rewritten
into gloss-lists first, which would strip out exactly the interpretive content (see below) that is
the actual basis for these particular sub-groups.

**Attempt 2 — same principle, applied as permissively as the technique allows** (plain whole-word
overlap between a strong's gloss and a subgroup's own text, single-subgroup-match-only, same
defer-on-conflict rule): **11 of 87 strongs (13%) got a clean single-subgroup match**; the other 76
were either no-signal (39, no word overlap at all) or conflict (37 — the same generic words like
"pride"/"boast"/"conceit" appear across several subgroups' own descriptions, so they don't
distinguish anything). The two Strong's codes literally glossed `"pride"` (G2745/G2746) hit ALL 8
subgroups at once — the single strongest possible case for how little a bare gloss constrains
which of these particular sub-groups a word belongs to.

**Why, concretely:** M08's sub-groups are not drawn on lexical/gloss lines at all — they're drawn
on an interpretive dimension (WHERE the pride is seated: heart / eyes-and-bearing / national-
collective / general-individual; or WHAT FORM it takes: willful defiance / verbal boasting /
cognitive inflation / power-based). That's a property of the VERSE a word occurs in, not of the
Strong's code itself — the identical Hebrew/Greek word for "proud" can be heart-seated in one verse
and power-seated in another. This independently reproduces, with fresh live evidence, exactly what
the #1005 M08 pilot already found by a different route (§1 above): *"a real per-verse interpretive
READ... that has no live equivalent anywhere in `iba.db`'s current lexicon layer, which is
deliberately mechanical-only."* A code-level gloss-precedent tool — however it's tuned — cannot
produce this sub-grouping, because the thing being sub-grouped on isn't a code-level property.

## 5. Bottom line, for the "cluster analysis reinstated" instruction

There is no engine to restart — there was never a generic one running continuously; there was a
disciplined but fully manual, one-script-per-cluster pipeline that stopped partway through the
corpus (15 of 49 clusters actually finding-loaded) and was archived once the method reset
(2026-06-25) and later the IBA split (2026-08-15) moved the live analytical work elsewhere.
Reinstating "cluster analysis" is therefore a scope decision, not a restart-a-service action: either
(a) revive the per-cluster load pattern for the remaining 34 clusters against this same legacy
schema, or (b) treat this schema as historical input only and design fresh against whatever the
windows-debate Phase (a) produces (per #1006's own original seeding from #1005) — the two are not
the same task and the #1005 synthesis's own point (e) ("the how still needs defining") is exactly
this fork, unresolved either way.
