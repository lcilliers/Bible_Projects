# M47 — handoff for batches C–H (v1)

**Date:** 2026-09-27
**Purpose:** let a fresh chat continue the M47 × other-cluster reading without re-deriving anything.
**Branch:** `claude/happy-mayer-nhz1mz`

## 1. Done so far (all in `outputs/markdown/`)

| File | What it holds |
|---|---|
| `M47-inner-seat-stocktake-v2-20260927.md` | membership, counts, variant senses |
| `M47-inner-seat-depiction-v1-20260927.md` | how each component is depicted, and how they interrelate (full verse read) |
| `M47-other-cluster-cooccurrence-assessment-v1-20260927.md` | assessment of the co-occurrence file; the batch plan (§5) |
| `M47-spirit-distinction-v1-20260927.md` + `M47-spirit-classification-v1-20260927.csv` | divine / human / other / undetermined, per verse |
| `M47-x-feeling-batchA-v1-20260927.md` | Batch A (Feeling) |
| `M47-x-knowing-speaking-batchB-v1-20260927.md` | Batch B (Knowing / Speaking / Hearing) |

## 2. Researcher rulings to carry forward

1. Keep all senses: wind, breath, body, meat, borderline. They are significant wherever they touch another aspect of the inner being.
2. **Not statistical.** Report both dominant relations and the fringe (marked ◆).
3. Distinguish divine, human and other spirits where the evidence is clear, and say explicitly where it is not. Use the CSV classes.
4. Exclude bones, kidneys, bowels, *nous* and "inner being" as separate study words for now.
5. The tag/surface misalignment note is sufficient.
6. "Heart as integrating centre" is to be explored later — not adopted yet.
7. Output always goes to `.md`; chat gets a short summary only.

## 3. Inputs needed in the new chat (re-attach — uploads don't carry over)

- `cluster-M47-surface-forms-20260927.csv` (M47 verses)
- `cluster-M47-other-m-code-pairs-with-distance-20260927.csv` (pairs + distance)

**Distance note:** positions are original-language word order [verify]. d0 = one token carries both tags.

## 4. Remaining batches (from assessment §5)

| Batch | Clusters |
|---|---|
| **C. Willing / desiring / orientation** | M18, M64, M28, M69, M34, M68, M83, M11, M30, M75, M66, M67 |
| **D. Moral condition** | M12, M58, M56, M14, M57, M62, M61, M10c, M08, M09 |
| **E. Relating to God** | M13, M31, M19, M36, M22, M49, M42 (includes "say / speak in heart"), M21, M54, M44, M32, M35, M60, M50, M79, M59, M45, M80, M39 |
| **F. Relating to others** | M05, M51, M06, M10, M33, M52, M84 |
| **G. Life / body / condition** | M25, M23, M73, M55, M77, M70, M71, M37 |
| **H. Setting / narrative** (scan for fringe only) | M72, M46, M78, M76, M74, M26 |

**Pre-filters to report (not drop silently):**
- "Holy" inside "Holy Spirit" (M61)
- "declares the Lord" (M42)
- "Lord of hosts" (M72)
- misfiled cluster tags — list them in §0 of each batch, as in A and B

## 5. Method per batch (as used for A and B)

1. Filter the pairs file to the batch's `other_cluster_code`s.
2. Group by cluster → verse, and sort verses by minimum distance.
3. Show each pair as `M47code{spiritclass}[surface]~other_surface(gloss) dN | verse text`. Take the spirit class from the classification CSV (join on reference + strong).
4. Read every verse.
5. Write it up by cluster: relation types, per-component profile, spirit classes, ◆ fringe, data notes, then cross-cutting observations.
6. Save as `M47-x-<theme>-batch<X>-v1-<date>.md`, then commit and push.
