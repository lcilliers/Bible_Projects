# Action Q — Path 1 Investigation Before Patch Assembly — 2026-04-20

| Field | Value |
|---|---|
| Purpose | Investigate the 179 Path 1 findings from programme scan 2026-04-19 before assembling a READINESSSWEEP patch |
| Discipline | Yesterday's investigation discipline (caught OT-DBR-010) applied to today's Path 1 candidates |
| Source scan | `outputs/reports/wa-global-readinesssweep-programme-scan-raw-20260419.json` |
| Scorecard | `outputs/reports/wa-global-readiness-scorecard-v2-20260419.md` |
| Produced | 2026-04-20 |

---

## Outcome

**DO NOT ASSEMBLE THE PATCH.** Both Path 1 finding classes are misclassifications by the pilot. Applying them blindly would (i) insert incorrectly-semantic quality flags into `wa_data_quality_flags` and (ii) attempt mechanical derivation of a field that requires semantic judgement.

**Effect on Q:** Q pivots from "build Path 1 remediation patch" to "fix pilot Path 1 classifiers (OT-DBR-011, OT-DBR-012), re-scan, then revisit".

**Effect on scorecard v2:** The "179 P1 items" figure is spurious. True P1 count is effectively 0 after reclassification. Programme-wide Path 1 burden is essentially clean post-DBR.

---

## The 179 Path 1 findings

| Breakdown | Count |
|---:|---|
| R.B `INSERT SMALL_VERSE_SAMPLE quality flag` | 135 |
| R.D `derive dominant_subject from context_description` | 44 |
| **Total** | **179** |

---

## Investigation — Finding class 1 (135 × SMALL_VERSE_SAMPLE)

### What the pilot emits

Pilot `scripts/readiness_sweep_pilot.py:243–254` emits:

```python
elif occ > 20 and active > 0 and active < occ * 0.2:
    # Check if SMALL_VERSE_SAMPLE flag already present
    ...
    if not has_flag:
        state.add(Finding("R.B", 1,
                          f"wa_data_quality_flags (term {t['strongs_number']})",
                          f"small verse sample: active={active}, occ={occ}",
                          "Path 1: INSERT SMALL_VERSE_SAMPLE quality flag"))
```

**Pilot's trigger:** `occ > 20 AND active < 20% of occ` — a ratio-based check.

### What the SMALL_VERSE_SAMPLE flag actually means

`engine/flag_engine.py:158–168` is the canonical writer of this flag:

```python
elif confirmed_verses < SMALL_VERSE_SAMPLE_THRESHOLD:
    ...
    _write_quality_flag(
        conn, file_id, strongs, "SMALL_VERSE_SAMPLE",
        f"Only {confirmed_verses} confirmed verse records for {strongs}. "
        f"Threshold is {SMALL_VERSE_SAMPLE_THRESHOLD}.",
    )
```

`SMALL_VERSE_SAMPLE_THRESHOLD = 5` in `engine/constants.py`. So the engine writes the flag when **absolute** confirmed verse count is `< 5`.

### Mismatch

| Context | Trigger |
|---|---|
| Engine (canonical writer) | `confirmed_verses < 5` (absolute) |
| Pilot (Path 1 emitter) | `occ > 20 AND active < occ * 0.2` (ratio, independent of absolute count) |

**Sample from r1 abomination term G0946:**
- `active=6`, `occ=117` → pilot flags SMALL_VERSE_SAMPLE
- But `active=6 >= 5` — engine would **not** set this flag
- Engine's rule would set HIGH_FREQUENCY_ANCHOR only if `occ >= 500` (not triggered for occ=117)

Applying the pilot's 135 "fixes" would **insert SMALL_VERSE_SAMPLE flags on terms that don't meet the flag's definition** — corrupting the semantic meaning of the flag.

### What the pilot's check actually detects

The pilot is detecting a real, different phenomenon: "high-occurrence term with low verse-capture ratio" — likely indicating span-filter-heavy terms where a large share of ESV occurrences weren't tagged at Strong's level (or were filtered out). This is a legitimate diagnostic, but it's NOT `SMALL_VERSE_SAMPLE`. Would need either:

- A new flag code (e.g. `LOW_CAPTURE_RATIO`) with its own threshold and documentation, or
- A diagnostic report (not a DB flag), or
- Reclassification as Path 4 (researcher review whether it matters for analysis)

### Verdict — class 1

**OT-DBR-011 raised.** All 135 items misclassified. No patch should be built from these findings.

---

## Investigation — Finding class 2 (44 × dominant_subject='NONE')

### What the pilot emits

Pilot `scripts/readiness_sweep_pilot.py:330–334`:

```python
if g["dominant_subject"] == "NONE":
    state.add(Finding("R.D", 1,
                      f"verse_context_group.id={g['id']}",
                      f"dominant_subject='NONE'",
                      "Path 1: derive from context_description"))
```

**Pilot's claim:** `dominant_subject='NONE'` is a Path 1 (mechanical) fix by deriving from `context_description` text.

### What "NONE" actually means and what derivation requires

Distribution of `wa_dimension_index.dominant_subject` (active):

| Value | Count |
|---|---:|
| NULL | 2,554 |
| 'HUMAN' | 772 |
| 'GOD' | 117 |
| **'NONE'** | **44** |
| 'OTHER_HUMAN' | 9 |
| 'UNSEEN' | 2 |

Spot sample (r23 compassion, 5 'NONE' groups):

| gid | group_code | dimension | context_description excerpt |
|---|---|---|---|
| 333 | 730-001 | Relational Disposition | Term names the visceral, inward movement of compassion… |
| 334 | 734-001 | Relational Disposition | Term names the inner capacity for fellow-feeling… |
| 337 | 3182-001 | Relational Disposition | Term describes pity and compassion as an inner disposition… |
| 338 | 3182-002 | Relational Disposition | Term names the withholding of pity as a judicial inner disposition… |
| 343 | 1635-001 | Divine-Human Correspondence | Term names the responsive quality of inner covenantal mercy… |

All 5 sampled describe **human inner dispositions**. The correct `dominant_subject` for these is `HUMAN` (or GOD for gid=343 depending on interpretation). The literal `'NONE'` value is a data error — it's neither the proper NULL (not yet set) nor one of the valid sentinels (HUMAN/GOD/OTHER_HUMAN/UNSEEN).

### Why this isn't mechanical

"Derive dominant_subject from context_description" requires:

1. **Reading** the context_description (prose)
2. **Classifying** the inner state it describes as belonging to HUMAN, GOD, OTHER_HUMAN, or UNSEEN
3. **Applying judgement** — e.g. gid=343 "responsive quality of inner covenantal mercy" could be HUMAN (receiver) or GOD (source) depending on the registry and dimension framing

This is semantic classification work — identical in nature to what Claude AI does in Dimension Review. No regex, string match, or dimension-to-subject lookup table can do it reliably.

### Correct classification

- **Path 2** (sub-process directive): re-run Dimension Review sub-step on the 44 NONE groups to reclassify them as HUMAN/GOD/etc. — or
- **Path 4** (RD): researcher dispositions each of 44 individually

Not Path 1.

### Verdict — class 2

**OT-DBR-012 raised.** All 44 items misclassified. No patch should be built from these findings.

---

## Programme-wide implications

After reclassification:

| Before (scorecard v2) | After | Change |
|---:|---:|---:|
| Path 1 findings: 179 | Path 1 findings: **0** | −179 |
| Path 2 findings: 1,361 | Path 2 findings: 1,405 | +44 |
| Path 4 findings: 5,422 | Path 4 findings: ~5,557 | +135 |

**Net effect on banking tiers:**

- **P1_REMEDIATION tier (9 registries) disappears.** Those 9 move to either STRUCTURALLY_CLEAN (if 0 P2) or SUBPROCESS_NEEDED (if P2 > 0).
- **BANKED tier (5) unchanged** — already at 0 across P1/P2/P4.

This is actually **good news**: the mechanical Path 1 burden across the programme is effectively zero post-DBR. All genuine remediation work is sub-process directive work (Path 2) or researcher-decision work (Path 4).

---

## Recommended next moves for Q

Q pivots to:

1. **Fix pilot R.B logic (OT-DBR-011):** either introduce a new flag code, downgrade to Path 4, or remove the check entirely
2. **Fix pilot R.D logic (OT-DBR-012):** promote `dominant_subject='NONE'` findings to Path 2 (DimReview sub-process)
3. **Re-run programme scan** with corrected pilot
4. **Publish scorecard v3** reflecting the true post-DBR state (expected: 0 P1 across the programme)
5. **Close Q** as "pilot fixed + re-scanned + scorecard v3; 0 P1 remediation needed"

**Estimated effort:** ~half-day (pilot edits ~20 lines + re-scan ~5 min + scorecard refresh).

**Savings:** avoids assembling and applying a 179-operation patch that would have done net harm.

---

## Why this matters beyond Q

Yesterday's OT-DBR-010 discovery (XREF join bug) and today's OT-DBR-011/012 discoveries follow the same pattern: **the pilot's Path 1 classifier has been emitting findings that don't meet the "mechanical" bar.** Three independent misclassifications now, all caught by investigation before application.

This argues for a pilot review sweep — go through every Path 1 emitter site and confirm the "mechanical" claim holds. Propose raising **OT-DBR-013 (pilot Path 1 classifier full audit)** as follow-on work.

---

*End of Action Q investigation record — 2026-04-20*
