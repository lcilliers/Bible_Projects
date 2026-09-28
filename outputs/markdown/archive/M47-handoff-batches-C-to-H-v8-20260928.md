# M47 — handoff after Batch H and the #1880 re-allocation (v8)

**Date:** 2026-09-28
**Supersedes:** v7 (`archive/`). **v8 changes (same day):**
- **Escalation #1880 applied** (BUILD.md §333). 72 re-allocation items from the M47 work were approved and applied to `cluster_strong`, and `verse_lexical.role` was refreshed.
- **The M47 input CSVs are now v2** (regenerated from `verse_lexical`). The v1 inputs are archived.
- **New investigations** (in `research/investigations/`):
  - `M47-seat-coverage-and-unseated-verses-v1-20260928.md` — only 10% of M-cluster verses name the seat. Its plan (§5) awaits your approval.
  - `M47-t-code-to-m-code-question-v1-20260928.md`
  - `M47-reallocation-register-v2-20260928.md`
- **Order agreed with you:** re-allocation (done) → delta revisit → seat-coverage tie-profile and pilot → synthesis, which may be redefined.

**v7 changes:**
- Batch H is done. **All batches A–H are complete.**
- F was revisited in the light of H (F v3). G was revisited in the light of H (G v2).
- The next step is the cross-batch synthesis, which is **to be discussed with the researcher before it starts**.
- The method is unchanged from v5.

**Purpose:** let a fresh chat continue M47 without re-deriving anything.
**Branch:** `main`.

## 1. Done so far (all in `outputs/markdown/`)

| File | What it holds |
|---|---|
| `M47-inner-seat-stocktake-v2-20260927.md` | membership, counts, variant senses |
| `M47-inner-seat-depiction-v1-20260927.md` | how each component is depicted and how they interrelate (full verse read); §2.1c = "said in heart" series |
| `M47-other-cluster-cooccurrence-assessment-v1-20260927.md` | assessment of the co-occurrence file; the batch plan (§5) |
| `M47-spirit-distinction-v1-20260927.md` + `M47-spirit-classification-v2-20260928.csv` (v2: Psa 106:33 → U, #1880 C-R4) | divine / human / other / undetermined, per verse |
| `M47-x-feeling-batchA-v3-20260928.md` | Batch A (Feeling); checked against F and G |
| `M47-x-knowing-speaking-batchB-v3-20260928.md` | Batch B (Knowing / Speaking / Hearing); checked against F and G |
| `M47-x-willing-desiring-batchC-v3-20260928.md` | Batch C (Willing / Desiring / Orientation) |
| `M47-x-moral-condition-batchD-v2-20260928.md` | Batch D (Moral condition); §7.1 = "Holy Spirit" pre-filter group |
| `M47-x-relating-to-god-batchE-v2-20260928.md` | Batch E (Relating to God); §1.9 = "declares the Lord" pre-filter group |
| `M47-x-relating-to-others-batchF-v3-20260928.md` | Batch F (Relating to others). **v3**: revisited from H — §7.6 threshold extended (Esther, Daniel, the servant, Luk 21:34, Rom 14:17); §15 voices addressed to the soul |
| `M47-x-life-body-condition-batchG-v2-20260928.md` | Batch G (Life / body / condition). **v2**: revisited from H — §4.5 God's oath by his soul and the Ish-bosheth oath; §5.4 the price of a life qualified; §14.3 pointer |
| `M47-x-setting-narrative-batchH-v1-20260928.md` | **Batch H** (Setting / narrative: M72, M46, M78, M76, M74, M26). 717 pairs / 452 verses, all read; context read for about 30 passages; §1.9 = "Lord of hosts" pre-filter group; §7 cross-cutting; §R-V revisits |

**§R items A–E** are kept as a record and are **not awaiting ruling** (researcher, 2026-09-28). Nothing has been written to the DB.

## 2. Researcher rulings to carry forward

1. Keep all senses: wind, breath, body, meat, borderline. They are significant wherever they touch another aspect of the inner being.
2. **Not statistical.** Report both dominant relations and the fringe (marked ◆).
3. Distinguish divine, human and other spirits where the evidence is clear, and say explicitly where it is not. Use the CSV classes.
4. Exclude bones, kidneys, bowels, *nous* and "inner being" as separate study words for now.
5. The tag/surface misalignment note is sufficient.
6. "Heart as integrating centre" is to be explored later — not adopted yet.
7. Output always goes to `.md`; chat gets a short summary only.
8. Each batch keeps a short **§X** (cluster → sections). **No §R option tables.** Misfiles get one line in §0, and only where a tag would mislead the reading.
9. **Interaction first.** Clusters are loose assemblies, and re-allocation is low priority. Focus on:
   - how components relate
   - why they relate here
   - why a word's meaning shifts between circumstances
   - **what happened before and after**
10. **Revisit as the rule.** When new reading bears on earlier batches, revise them: version bump, archive the prior version, and list the revisits in the new file's §R-V.

## 3. Inputs

- `research/investigations/cluster-M47-surface-forms-v2-20260928.csv` (M47 verses; identical to v1)
- `research/investigations/cluster-M47-other-m-code-pairs-with-distance-v2-20260928.csv` (pairs + distance, **after #1880**; **UTF-8 with BOM** → read with `utf-8-sig`)
- `research/investigations/cluster-M47-delta-new-pairs-after-1880-v1-20260928.csv` — **155 genuinely new pair rows in 115 verses**: "die" / "death" now in M25, plus 1 *splanchna* (M50). **This is the delta to read.**
- The batch files A–H were read on the v1 pairs. After #1880 the same word pairs mostly sit under corrected codes. The 367 pairs that dropped out were all already flagged as misfiles.
- **Regenerating the CSVs:** the method (verse_lexical tokens whose `role` contains M47 × tokens with any other M role in the same verse; distance = |position difference|) reproduces the 2026-09-27 files exactly. See BUILD.md §333.
- **Cluster membership DB:** `iba/app/db/iba.db` (read-only):
  - `cluster` holds `cluster_code`, `short_name`, `description`
  - `cluster_strong` holds `strong`, `cluster_code`, `source`, `confidence`, `alt_clusters`, `review_flag`, `rationale`; filter `deleted=0`
- **Context verses:** `iba/app/db/iba.db` → `verse` (ESV, `reference` e.g. `1Sa 18:1`, column `text`).
  - Gen 8:22 and Pro 7:6, 7:9 are missing; fall back to the STEP server `http://localhost:8989` for any gap.
- **Since #1880** "die" (H4191, G0599) and "death" (H4194, G2288) also carry **M25** (the T3 / T10 rows are kept). Life & Death now shows both sides.

## 4. Remaining work (in order)

| # | Item | Scope |
|---|---|---|
| 1 | **Delta revisit** | Read the 155 new pairs (115 verses) with context; the death side of Life & Death. Batch G → v3, with §R-V and any consequential revisits |
| 2 | **Seat-coverage tie-profile** (Step 1 of the seat-coverage plan) | **Needs your approval** of that plan's §6 decisions (tie classes, body-seat list, pilot clusters) |
| 3 | Pilot reading of the no-seat verses | Two clusters (suggested M02 Anger, M20 Doubt) |
| 4 | Cross-batch synthesis | Discuss first; may be redefined by 2–3. Candidates: voices to the soul; eating and drinking at thresholds; one word with opposite value; the inner seat as governed |

**Open side items from #1880:**
- M67 gained H7423B and H5647I; its readiness check must run before its reading resumes.
- E-R6 (the faith family across M13 / M31 / M19) awaits a cluster-structure review.
- `cluster-M47-other-m-code-cooccurrence-20260927.csv` is stale.

## 5. Method per batch (unchanged from v5; kept for any further reading)

1. Filter the pairs file to the batch's `other_cluster_code`s. Group by cluster → verse, sorted by minimum distance.
   - The dump format is `M47code{spiritclass}[surface]~other_surface(gloss) dN | verse text`.
   - The scratchpad scripts `dump.py` (dump: `python dump.py M72,M46 out.txt`) and `ctx.py` (context reader: `python ctx.py "Judg 16:15-30" ...`) have to be recreated each session. Copies from earlier sessions may survive in older scratchpad folders.
2. Read every verse.
3. Identify the **recurring relations** and the **words whose sense shifts** by circumstance.
4. For the key passages, **read the context**: 2–3 verses either side, or the whole episode for narratives.
5. Write each relation up as:
   - what it is
   - why it is related here
   - how the meaning shifts
   - before / after (with quotes)
   - ◆ fringe
6. Keep §0 short: pre-filters, and misleading tags only. Keep §X short.
7. **§R-V:** list the earlier files or sections the new reading changes. Revise them in the same session (version bump, archive the prior version).
8. Save as `M47-x-<theme>-batch<X>-v1-<date>.md`, then commit and push.

**Re-allocation register and apply:** `iba/docs/m47-cluster-reallocation-spec-v3-20260928.json`, `iba/app/migration/apply_m47_reallocation_1880_v1_20260928.py`, DB backup `iba/app/db/iba.db.pre-1880-m47-reallocation-20260928.bak`.
