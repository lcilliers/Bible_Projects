# Cluster anomaly audit — results, fixed vs. escalated

**Escalation #1714.** Researcher instruction, this chat turn: *"turn to 1714 and complete the
cluster anomalies."* Ran the full proposed sweep against all 80 live M-clusters. Fixed what was
mechanically clear; escalating what genuinely needs a decision, not guessed at.

## Method note, stated honestly

The first automated pass (name-vs-vocabulary keyword matching) produced too many false positives to
trust directly — English synonyms don't share substrings with a cluster's own name (`M06` "Malice &
Enmity" tagged with "scorn/contempt/hatred" has zero literal overlap with "malice"/"enmity" but is
completely correct). That approach was abandoned rather than reported as if reliable. What actually
worked: a **targeted homonym/collision sweep** (does a cluster's tagged vocabulary share an English
word with its own theme in an unrelated sense), cross-checked against `stepTransliteration` and
lexicon data before acting — the same method that caught `M18` while generating its science extract.

## Fixed directly (clear mechanical bugs, not judgement calls)

**`M18` (Desire & Longing) — 4 strongs removed** (soft-deleted, not hard-deleted): `G2375` "long
shield", `G2863` "be long-haired", `G3118` "long-lived", `H6446` "long-sleeved" — all the
physical-length sense of "long," nothing to do with desire.

**`M62` (Truth & Sincerity) — 5 strongs removed**, a second, previously-unconfirmed collision found
running the same sweep corpus-wide: `G2279` (*ēchos*, "echo/noise"), `G5353` (*fthongos*, "musical
tone"), `G4537` (*salpizō*, "to sound a trumpet"), `H1998` (*hemyah*, "roar/noise"), `H8088A`
(*shema*, "report/something heard") — all the audible-noise sense of "sound." `G0573` (*haplous*,
"single/sincere" — Matthew 6:22's "sound eye") checked and correctly left alone — genuinely the
right sense.

Migration: `iba/app/migration/fix_cluster_keyword_collisions_v1_20260917.py`, applied live.

## Checked clean

- **0 strongs tagged to more than one M-cluster** — no literal cross-cluster duplicate tags exist.
  The `M12`/`M13` integrity overlap (§ below) is conceptual, not a duplicate-tag bug.
- **`M32`** ("Covenant") flagged by the first-pass heuristic as a name/vocabulary mismatch (only
  circumcision vocabulary, zero covenant-making terms) — checked and cleared: `cluster.description`
  already reads "Covenant and Circumcision," and covenant-*making* vocabulary is correctly held
  separately at `M44` (Covenant & Fellowship). A deliberate split, not an anomaly.
- Broader homonym sweep (kind/tender/plot/turn/mind/trust/rest/charge/watch/bear/form, etc.) — every
  other hit checked and confirmed thematically correct.

## Round 2 — the 4 "escalated" items, checked properly instead of asked

Researcher, verbatim: *"you surfaced obvious errors, and only if you really need my judgement, then
ask, else fix."* Re-checked each — none actually needed a judgement call:

1. **`M59`/`M60`.** The missing vocabulary wasn't absent from the corpus — it existed, mistagged.
   `M59` "Release & Reconciliation": the 6 real reconciliation strongs (*katallassō* family) were
   sitting at `M05` (whose scope narrowed to "Kindness & Friendship" earlier this session) — moved
   5 of them to `M59` (`G0786` "irreconcilable" stays at `M06`, its sense is persistent hostility,
   not reconciliation-achieved). `M60` "Confession & Forgiveness": the 2 confession strongs existed
   but were only role-tagged (`T2`/`T3`), never M-cluster-tagged — added as `M60` tags, role tags
   left untouched (different axis). Both verified live afterward: `M59` now genuinely carries
   reconciliation vocabulary alongside release/leaving; `M60` genuinely carries confession
   alongside forgiveness/atonement.
2. **`M67`.** Same pattern — 7 more real idleness/diligence strongs existed, sitting untagged at
   the M-cluster level (only in the giant `T2` "Supplementary" bucket). Added. `M67` now has 9
   strongs, not 2.
3. **`M47` `cluster.gloss` staleness.** Not a 1-cluster problem after all — the field wasn't just
   missing `nous` (already correctly excluded per a real 2026-09-06 researcher ruling, escalation
   #1525, that a strong lives in exactly one M-cluster), it was listing only 8 of 38 actual live
   members. Regenerated from live membership, matching the corpus's own established
   `gloss (transliteration)` format — not the different format my first attempt would have used,
   which was checked and rejected before writing anything (see note below).
4. **`M12`/`M13`.** Checked properly, not deferred: 0 strongs are tagged to both (confirmed in
   round 1's sweep) — there is no duplicate-tag bug. The overlap is two legitimately adjacent
   clusters (integrity vs. faithfulness) both carrying real, distinct vocabulary. Nothing to fix.

**One format mistake caught before it did damage**: a first attempt to regenerate every cluster's
stale-looking `gloss` field would have silently replaced `M01`'s good, already-correct
`english-gloss (transliteration)` field with a worse `transliteration (code)` format — a real bug
in my own fix, not the data's. Caught by comparing the *code set* mentioned against live membership
(not exact string match) before writing anything; only `M47` was actually stale. Also fixed `M05`'s
`gloss` field, which the `M59` move itself made stale (still listing the moved reconciliation
terms) — a direct, checked consequence of my own change, not left for the researcher to notice
later.

Migration: `iba/app/migration/fix_cluster_anomalies_v2_20260917.py`, applied live, verified against
the DB afterward, not just trusted.

## What wasn't attempted

A full manual semantic read of every gloss in all 80 clusters (thousands of rows) — not done, and
saying so rather than implying the sweep was exhaustive at that level. The targeted method above
(homonym/collision-prone English words, checked against real lexical data) is a real, verified pass,
not a complete line-by-line audit. If you want that deeper pass, it's a real, separate piece of work
to scope, not something this sweep silently also did.
