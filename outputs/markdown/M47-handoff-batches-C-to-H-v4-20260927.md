# M47 — handoff for batches F–H (v4)

**Date:** 2026-09-27
**Supersedes:** v3 (`archive/`). v4 records that Batch E is done. v3 recorded Batch D; v2 recorded Batch C, A–C v2 files with §R / §X, and the "said in heart" correction.
**Purpose:** let a fresh chat continue the M47 × other-cluster reading without re-deriving anything.
**Branch:** `main`. `claude/happy-mayer-nhz1mz` is behind `main` and not used since Batch C.

## 1. Done so far (all in `outputs/markdown/`)

| File | What it holds |
|---|---|
| `M47-inner-seat-stocktake-v2-20260927.md` | membership, counts, variant senses |
| `M47-inner-seat-depiction-v1-20260927.md` | how each component is depicted, and how they interrelate (full verse read); §2.1c = "said in heart" series |
| `M47-other-cluster-cooccurrence-assessment-v1-20260927.md` | assessment of the co-occurrence file; the batch plan (§5) |
| `M47-spirit-distinction-v1-20260927.md` + `M47-spirit-classification-v1-20260927.csv` | divine / human / other / undetermined, per verse |
| `M47-x-feeling-batchA-v2-20260927.md` | Batch A (Feeling) — §R rulings R1–R7 (R7 = process, all batches), §X |
| `M47-x-knowing-speaking-batchB-v2-20260927.md` | Batch B (Knowing / Speaking / Hearing) — §R rulings R1–R4, §X |
| `M47-x-willing-desiring-batchC-v2-20260927.md` | Batch C (Willing / Desiring / Orientation) — §R rulings R1–R5, §X |
| `M47-x-moral-condition-batchD-v1-20260927.md` | Batch D (Moral condition) — §R rulings R1–R10 (all membership; no spirit-class item), §X; §7.1 = "Holy Spirit" pre-filter group (92 verses) |
| `M47-x-relating-to-god-batchE-v1-20260927.md` | Batch E (Relating to God, 19 clusters) — §R rulings R1–R11 (all membership; speech verbs left to B R1), §X; §1.9 = "declares the Lord" pre-filter group (38 verses); §13 flags *kāvôd* as a possible self-term |

**Open researcher rulings:** A R1–R7, B R1–R4, C R1–R5, D R1–R10, E R1–R11 (a blank "Ruling" row in each). Nothing has been written to the DB.

## 2. Researcher rulings to carry forward

1. Keep all senses: wind, breath, body, meat, borderline. They are significant wherever they touch another aspect of the inner being.
2. **Not statistical.** Report both dominant relations and the fringe (marked ◆).
3. Distinguish divine, human and other spirits where the evidence is clear, and say explicitly where it is not. Use the CSV classes.
4. Exclude bones, kidneys, bowels, *nous* and "inner being" as separate study words for now.
5. The tag/surface misalignment note is sufficient.
6. "Heart as integrating centre" is to be explored later — not adopted yet.
7. Output always goes to `.md`; chat gets a short summary only.
8. **(2026-09-27)** Each batch file accompanies the analysis of the clusters it covers. So every batch needs:
   - **§R — items for researcher ruling:** one table per item, with cluster(s), Strong's, DB now, evidence, issue, options, recommendation, and a blank Ruling row
   - **§X — cluster cross-reference:** sections and flagged Strong's per cluster, with DB source and confidence

## 3. Inputs

- `research/investigations/cluster-M47-surface-forms-20260927.csv` (M47 verses)
- `research/investigations/cluster-M47-other-m-code-pairs-with-distance-20260927.csv` (pairs + distance; **UTF-8 with BOM** → read with `utf-8-sig`)
- **Cluster membership DB:** `iba/app/db/iba.db` (read-only):
  - `cluster` holds `cluster_code`, `short_name`, `description`
  - `cluster_strong` holds `strong`, `cluster_code`, `source`, `confidence`, `alt_clusters`, `review_flag`, `rationale`; filter `deleted=0`
  - A Strong's can have several rows (M-cluster + T-bucket).
  - `database/bible_research.db` does **not** hold these codes.

**Distance note:** positions are original-language word order [verify]. d0 = one token carries both tags.

## 4. Remaining batches (from assessment §5)

| Batch | Clusters |
|---|---|
| ~~D. Moral condition~~ **done** | M12, M58, M56, M14, M57, M62, M61, M10c, M08, M09 |
| ~~E. Relating to God~~ **done** | M13, M31, M19, M36, M22, M49, M42 ("speak" verbs H1696G/I, H0981 — see B R1), M21, M54, M44, M32, M35, M60, M50, M79, M59, M45, M80, M39 |
| **F. Relating to others** (next) | M05, M51, M06, M10, M33, M52, M84 |
| **G. Life / body / condition** | M25, M23, M73, M55, M77, M70, M71, M37 |
| **H. Setting / narrative** (scan for fringe only) | M72, M46, M78, M76, M74, M26 |

**Correction to v1:** "said in heart" (H0559 "to say") is in **T3 Operations**, not M42. It is **not in the pairs file**, so Batch E will not contain it. See Batch B R2 (recommendation: cover it from depiction v1 §2.1c).

**Pre-filters to report (not drop silently):**
- "Holy" inside "Holy Spirit" (M61) — done in Batch D §0.1 / §7.1
- "declares the Lord" (M42) — done in Batch E §0.1 / §1.9
- "Lord of hosts" (M72)
- misfiled cluster tags — list them in §0 of each batch, and raise membership questions in §R

## 5. Method per batch

1. Filter the pairs file to the batch's `other_cluster_code`s.
2. Group by cluster → verse, and sort verses by minimum distance.
3. Show each pair as `M47code{spiritclass}[surface]~other_surface(gloss) dN | verse text`. Take the spirit class from the classification CSV (join on reference + strong).
4. Read every verse.
5. Write it up by cluster: relation types, per-component profile, spirit classes, ◆ fringe, data notes, then cross-cutting observations.
6. For every flagged Strong's, query `cluster_strong` for all active rows. Write **§R** and **§X** (see §2.8).
7. Save as `M47-x-<theme>-batch<X>-v1-<date>.md`, then commit and push. Revisions bump `-v{n}` and archive the prior version.
