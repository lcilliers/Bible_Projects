# M47 — handoff for Batch H and synthesis (v6)

**Date:** 2026-09-28
**Supersedes:** v5 (`archive/`). **v6 changes:**
- Batches A and B were checked against Batch F and revised (A v3, B v3).
- Batch G is done.
- F was revisited in the light of G (F v2).
- The method is unchanged from v5.

**Purpose:** let a fresh chat continue the M47 × other-cluster reading without re-deriving anything.
**Branch:** `main`.

## 1. Done so far (all in `outputs/markdown/`)

| File | What it holds |
|---|---|
| `M47-inner-seat-stocktake-v2-20260927.md` | membership, counts, variant senses |
| `M47-inner-seat-depiction-v1-20260927.md` | how each component is depicted and how they interrelate (full verse read); §2.1c = "said in heart" series |
| `M47-other-cluster-cooccurrence-assessment-v1-20260927.md` | assessment of the co-occurrence file; the batch plan (§5) |
| `M47-spirit-distinction-v1-20260927.md` + `M47-spirit-classification-v1-20260927.csv` | divine / human / other / undetermined, per verse |
| `M47-x-feeling-batchA-v3-20260928.md` | Batch A (Feeling). **v3**: checked against F and G. Revisit notes throughout; new context for 1Sa 11:5–7 (§2.4: Spirit → anger, versus 1Sa 18 anger → spirit) |
| `M47-x-knowing-speaking-batchB-v3-20260928.md` | Batch B (Knowing / Speaking / Hearing). **v3**: checked against F and G. New context for Gen 45:25–28, 1Sa 1:7–18 and Judg 16:15–30; §9.5 qualified ("hearing sometimes needs seeing") |
| `M47-x-willing-desiring-batchC-v3-20260928.md` | Batch C (Willing / Desiring / Orientation) |
| `M47-x-moral-condition-batchD-v2-20260928.md` | Batch D (Moral condition); §7.1 = "Holy Spirit" pre-filter group |
| `M47-x-relating-to-god-batchE-v2-20260928.md` | Batch E (Relating to God); §1.9 = "declares the Lord" pre-filter group; §3.2 = *kāvôd* as a self-term (flag) |
| `M47-x-relating-to-others-batchF-v2-20260928.md` | Batch F (Relating to others). **v2**: revisited from G. §7 threshold pattern extended (Judg 19:5, 8; Uriah; Gen 27:25; Samson; the sad-heart counter-case); §3.4 despairing life-hatred; §4 Lev 26:36; §15 fifth self-address setting |
| `M47-x-life-body-condition-batchG-v1-20260928.md` | **Batch G** (Life / body / condition: M25, M23, M73, M55, M77, M70, M71, M37). 802 pairs / 547 verses, all read; context read for about 35 passages; §R-V lists the revisits |

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
10. **Revisit as the rule.** When new reading bears on earlier batches, revise them: version bump, archive the prior version, and list the revisits in the new batch's §R-V.

## 3. Inputs

- `research/investigations/cluster-M47-surface-forms-20260927.csv` (M47 verses)
- `research/investigations/cluster-M47-other-m-code-pairs-with-distance-20260927.csv` (pairs + distance; **UTF-8 with BOM** → read with `utf-8-sig`)
- **Cluster membership DB:** `iba/app/db/iba.db` (read-only):
  - `cluster` holds `cluster_code`, `short_name`, `description`
  - `cluster_strong` holds `strong`, `cluster_code`, `source`, `confidence`, `alt_clusters`, `review_flag`, `rationale`; filter `deleted=0`
- **Context verses:** `iba/app/db/iba.db` → `verse` (ESV, `reference` e.g. `1Sa 18:1`, column `text`).
  - Gen 8:22 is missing; fall back to the STEP server `http://localhost:8989` for any gap.
- **Note from Batch G:** the death words are **not M-coded**:
  - "die" (H4191, G0599) is in T3
  - "death" (H4194, G2288) is in T10

  So "Life & Death" pairs show only the life side.

## 4. Remaining work

| Item | Scope |
|---|---|
| **H. Setting / narrative** (next; scan for fringe only) | M72, M46, M78, M76, M74, M26. Pre-filter: "Lord of hosts" (M72) — report the group, not a silent drop. |
| Revisit pass after H | Apply rule 10 to A–G as H's reading requires. |
| Cross-batch synthesis (**discuss with the researcher first; not started**) | Three candidates: (1) self-address to the soul — five settings: praise, lament, rest, self-indulgence, battle; (2) eating and drinking at inner thresholds (F §7 + G §14.6); (3) one word with opposite moral value by object — tender (F §6), strong / hard (G §3.3), entice (G §10), *hāgâ* (F §12.2) |

## 5. Method per batch (unchanged from v5)

1. Filter the pairs file to the batch's `other_cluster_code`s. Group by cluster → verse, sorted by minimum distance.
   - The dump format is `M47code{spiritclass}[surface]~other_surface(gloss) dN | verse text`.
   - The scratchpad scripts `dumpG.py` (dump) and `ctx.py` (context reader: `python ctx.py "Judg 16:15-30" ...`) have to be recreated each session.
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
