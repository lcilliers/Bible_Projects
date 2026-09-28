# M47 — handoff after Batch H: synthesis next (v7)

**Date:** 2026-09-28
**Supersedes:** v6 (`archive/`). **v7 changes:**
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
| `M47-spirit-distinction-v1-20260927.md` + `M47-spirit-classification-v1-20260927.csv` | divine / human / other / undetermined, per verse |
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

- `research/investigations/cluster-M47-surface-forms-20260927.csv` (M47 verses)
- `research/investigations/cluster-M47-other-m-code-pairs-with-distance-20260927.csv` (pairs + distance; **UTF-8 with BOM** → read with `utf-8-sig`)
- **Cluster membership DB:** `iba/app/db/iba.db` (read-only):
  - `cluster` holds `cluster_code`, `short_name`, `description`
  - `cluster_strong` holds `strong`, `cluster_code`, `source`, `confidence`, `alt_clusters`, `review_flag`, `rationale`; filter `deleted=0`
- **Context verses:** `iba/app/db/iba.db` → `verse` (ESV, `reference` e.g. `1Sa 18:1`, column `text`).
  - Gen 8:22 and Pro 7:6, 7:9 are missing; fall back to the STEP server `http://localhost:8989` for any gap.
- The death words are **not M-coded** ("die" H4191 / G0599 in T3; "death" H4194 / G2288 in T10), so "Life & Death" pairs show only the life side.

## 4. Remaining work

| Item | Scope |
|---|---|
| **Cross-batch synthesis** (next; **discuss with the researcher first; not started**) | Candidates, with sources: |
| 1. Voices to the soul | Five self-address settings: praise, lament, rest, self-indulgence, battle (F §15). Also others addressing the soul (Psa 11:1) and God's oath by his own soul (H §7.8) |
| 2. Eating and drinking at inner thresholds | F §7 (incl. §7.6), G §14.6, H §7.6 |
| 3. One word, opposite value by object or component | tender (F §6); strong / hard (G §3.3); entice (G §10); *hāgâ* (F §12.2); *nāṣar*, *šāmar*, vengeance, fatness, *šāgâ*, kinship-flesh (H §7.4); the "lifted" heart (D) |
| 4. (new, for the researcher to decide) The inner seat as governed | rule, service, guarding and judgment turned inward (H §7.3) |

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
