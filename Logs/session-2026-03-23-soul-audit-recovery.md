# Session Recovery — 23 March 2026
**Recovered after crash.  Last work: Soul (registry 182) AUDIT_WORD + export.**

---

## What was completed before the crash

### 1. audit.py WR-05 downgrade (STOP → REVIEW)
Between the 05:35 and 05:37 runs, `engine/audit.py` WR-05 was changed from
`_fail_stop` to `_fail_review`. The comment recorded in-code reads:

> "Downgraded to REVIEW: gaps can arise from legitimate term restructuring
> (e.g. splitting a consolidated entry into sub-glosses) and are not evidence
> of a partial write. Partial-write detection is covered by WR-06/WR-07."

This is the only code change visible from the artefacts.

### 2. Soul term expansion (4 → 11 terms)
Between the 04:47 run (54 verses, 4 terms) and the 05:35 run (694 verses,
11 terms), Soul's `wa_term_inventory` was expanded to include the H5315 sub-gloss
variants: **H5315G, H5315H, H5315I, H5315J, H5315K, H5315L, H5315M, H5315N**
(in addition to the existing H4578, H5397, G5590, H5315).

### 3. AUDIT_WORD runs — Soul registry 182

| Time | Run ID | Outcome | Changes |
|------|--------|---------|---------|
| 04:47 | RUN-20260323_044721 | REVIEW | 4 terms, 54 verses (dry-run or early state) |
| 05:35 | RUN-20260323_053527 | STOP | Applied: 640 inserts, 24 ti field changes → 694 total verses |
| 05:37 | RUN-20260323_053724 | REVIEW | 0 changes — all 694 verses confirmed |

The 05:35 run got a STOP via WR-05 (ID gap check was still `_fail_stop` at that
point). WR-05 was then downgraded to REVIEW, and the 05:37 run completed cleanly.

### 4. JSON export
`data/exports/Soul_182_full_20260323.json` — generated at **05:40:26** from the
clean 05:37 run state. This is the authoritative export for this session.

---

## Current state of Soul (as at 05:40 export)

| Field | Value |
|-------|-------|
| `phase1_status` | In Progress |
| `phase1_term_count` | 11 |
| `phase1_verse_count` | 694 |
| `testament_coverage` | OT_only |
| `last_automation_run` | 2026-03-23T05:37:29 |
| `automation_run_id` | RUN-20260323_053724-AUDIT_WORD |

**Note on `testament_coverage = OT_only`:** G5590 (psychē, Greek/NT) has 0
verse records in the DB — it was consolidated by researcher decision (see
status_note on that term). Because no NT verse records exist, testament_coverage
reports OT_only. WR-09 PASSed with this value. This is consistent with the
data but should be noted for the researcher.

---

## Outstanding REVIEW items from latest run (RUN-20260323_053724)

### WR-05 REVIEW — ID gaps in wa_term_inventory
```
Gaps: [(491, 493), (493, 1530)]
```
IDs 491–493 are Soul's original 4 terms; 1530 is where the new H5315x sub-terms
were inserted (they got higher IDs). This is a structural artefact of adding terms
after-the-fact, not a data integrity issue.  WR-05 is now REVIEW-level; no action
required unless the researcher wants the terms renumbered (which would be a
significant migration task with no functional benefit).

### WR-08 REVIEW — G5590 verse/occurrence ratio = 0.0
```
G5590: verses=0, occurrences=825, ratio=0.0
```
G5590 has no DB verse records by design — its status_note records researcher
decision to consolidate the 5 STEP sub-glosses (G5590G–K) into a single entry
without separate verse records. The WR-08 flag is technically correct but
expected.  **Action needed:** add `"no separate verse record"` to the G5590
`status_note` field in `wa_term_inventory`. This suppresses the STEP verse fetch
in future AUDIT_WORD runs and would suppress WR-08's ratio check for this term.

Current G5590 status_note (from export):
> "STEP presents as 5 sub-glosses: soul, soul: animal, soul: life, soul: myself,
> soul: person — all resolving to G5590. STEP internal suffixed identifiers:
> G5590G, G5590H, G5590I, G5590J, G5590K. Consolidated as single entry per
> researcher decision."

Suggested addition: append ` No separate verse record.` so the phrase is
detected by audit_word.py A3's skip guard.

### WR-19 REVIEW — G5590 parse warnings without NOTE flag
```
Parse warnings without NOTE flag: ['G5590']
```
The meaning parser ran on G5590 and produced warnings, but G5590 does not have
a NOTE-type researcher flag in `wa_data_quality_flags`.  
**Action needed:** either add a NOTE flag to G5590, or investigate the parse warning
and fix the meaning text.

---

## What may have been in progress at the time of the crash

Based on the artefacts, the most likely next steps were:

1. **Reviewing the REVIEW items above** — the export was generated immediately
   after the 05:37 run, suggesting the researcher was about to examine the JSON
   to understand the outstanding checks.

2. **Word report** — `engine/report.py --mode=report --registry=182` would show
   the same data in human-readable form. This may have been the next step to
   verify the full Soul state before deciding on WR-08 / WR-19 actions.

3. **G5590 status_note patch** — to suppress WR-08 false-positive in future runs.

---

## Recommended next steps to resume

1. **Decide on G5590 `status_note`** — append `" No separate verse record."` 
   to suppress WR-08 and A3 verse fetch for this term. This can be done via a
   direct DB update or a small patch script.

2. **Investigate WR-19 (G5590 parse warning)** — run the meaning parser manually
   or check `wa_meaning_parsed` for G5590 to see what warning was generated.

3. **Re-run audit** after any patches to confirm WR-08 and WR-19 clear.

4. **Re-export** after a clean audit run to update `Soul_182_full_20260323.json`.

5. **Continue the batch audit sequence** — session log 2026-03-22 listed all
   remaining words. Soul was the word in progress at the crash point.
