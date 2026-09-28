# M47 — handoff for batches G–H (v5)

**Date:** 2026-09-28
**Supersedes:** v4 (`archive/`). **v5 changes the method** per researcher direction (2026-09-28): interaction first, §R demoted, and revisiting earlier batches is the rule. It records Batch F done and the revisits (C v3, D v2, E v2).
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
| `M47-x-willing-desiring-batchC-v3-20260928.md` | Batch C (Willing / Desiring / Orientation) — v3 revisits §1.6 (merry heart → F §7) and §8.4 / R3 (crushing → F §5) |
| `M47-x-moral-condition-batchD-v2-20260928.md` | Batch D (Moral condition) — v2 revisits §1.5 (Lev 26 → F §4);  §R rulings R1–R10 (all membership; no spirit-class item), §X; §7.1 = "Holy Spirit" pre-filter group (92 verses) |
| `M47-x-relating-to-god-batchE-v2-20260928.md` | Batch E (Relating to God, 19 clusters) — v2 revisits §2 (2Ki 2) and §7.1 (1Sa 18);  §R rulings R1–R11 (all membership; speech verbs left to B R1), §X; §1.9 = "declares the Lord" pre-filter group (38 verses); §13 flags *kāvôd* as a possible self-term |
| `M47-x-relating-to-others-batchF-v1-20260928.md` | Batch F (Relating to others: M51, M05, M06, M10, M33, M52, M84) — **first batch in the interaction-first format**; context read for about 30 passages; §R-V lists the revisits |

**§R items A–E** (A R1–R7, B R1–R4, C R1–R5, D R1–R10, E R1–R11) are **kept as a record and are not awaiting ruling**. Re-allocation is low priority (researcher, 2026-09-28). Nothing has been written to the DB.

## 2. Researcher rulings to carry forward

1. Keep all senses: wind, breath, body, meat, borderline. They are significant wherever they touch another aspect of the inner being.
2. **Not statistical.** Report both dominant relations and the fringe (marked ◆).
3. Distinguish divine, human and other spirits where the evidence is clear, and say explicitly where it is not. Use the CSV classes.
4. Exclude bones, kidneys, bowels, *nous* and "inner being" as separate study words for now.
5. The tag/surface misalignment note is sufficient.
6. "Heart as integrating centre" is to be explored later — not adopted yet.
7. Output always goes to `.md`; chat gets a short summary only.
8. **(2026-09-27, amended 2026-09-28)** Each batch file accompanies the analysis of the clusters it covers, so every batch keeps a short **§X** (cluster → sections). **§R option tables are dropped.** Misfiles get one line in §0, and only where a tag would mislead the reading.
9. **(2026-09-28) Interaction first.** Clusters are loose assemblies, and re-allocation is low priority. Focus on how components relate, why they relate here, why a word's meaning shifts between circumstances, and **what happened before and after**.
10. **(2026-09-28) Revisit as the rule.** When new reading bears on earlier batches, revise them: version bump, archive the prior version, and list the revisits in the new batch's §R-V.

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
| ~~F. Relating to others~~ **done** | M05, M51, M06, M10, M33, M52, M84 |
| **G. Life / body / condition** (next) | M25, M23, M73, M55, M77, M70, M71, M37 |
| **H. Setting / narrative** (scan for fringe only) | M72, M46, M78, M76, M74, M26 |

**Correction to v1:** "said in heart" (H0559 "to say") is in **T3 Operations**, not M42. It is **not in the pairs file**, so Batch E will not contain it. See Batch B R2 (recommendation: cover it from depiction v1 §2.1c).

**Pre-filters to report (not drop silently):**
- "Holy" inside "Holy Spirit" (M61) — done in Batch D §0.1 / §7.1
- "declares the Lord" (M42) — done in Batch E §0.1 / §1.9
- "Lord of hosts" (M72)
- misfiled cluster tags — list them in §0 of each batch, and raise membership questions in §R

## 5. Method per batch (revised 2026-09-28)

1. Filter the pairs file to the batch's `other_cluster_code`s. Group by cluster → verse, sorted by minimum distance.
   - The dump format is `M47code{spiritclass}[surface]~other_surface(gloss) dN | verse text`.
   - A reusable dump script sat in the session scratchpad (`dumpD.py` pattern) and has to be recreated each session.
2. Read every verse.
3. Identify the **recurring relations** — pairings or sequences of inner-seat components — and the **words whose sense shifts** by circumstance.
4. For the key passages in each relation, **read the context**: 2–3 verses either side, or the whole episode for narratives.
   - Source: `iba/app/db/iba.db` → `verse` (29,760 ESV verses, plain `text`, keyed by `reference`, e.g. `1Sa 18:1`).
   - Fall back to the STEP server (`http://localhost:8989`) if a verse is missing.
5. Write each relation up as:
   - what the relation is
   - why they are related here
   - how the meaning shifts
   - before / after (with the context verses quoted)
   - ◆ fringe
6. Keep §0 short: pre-filters, and misfiles only where they mislead. Keep §X short.
7. **§R-V:** list the earlier files or sections the new reading changes. Revise them in the same session (version bump, archive the prior version).
8. Save as `M47-x-<theme>-batch<X>-v1-<date>.md`, then commit and push.
