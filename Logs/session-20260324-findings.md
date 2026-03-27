# Session Findings — 24 March 2026

---

## Finding 1 — AUDIT_WORD REVIEW items: where they are captured

**Question:** Are the REVIEW items from A9 captured in the word-report JSON export?

**Answer:** Yes — but not in the quality flag tables.

### Where they live

The REVIEW items are written to `word_run_state.audit_detail` (a JSON blob) during A9 of every AUDIT_WORD run. The `export_word()` function queries `word_run_state` using `wrs.*`, so the full check-by-check breakdown is present in the export at:

```
data["run_history"][0]["audit_detail"]
```

Example structure (after JSON parsing):
```json
{
  "WR-04": { "r": "REVIEW", "d": "3 row(s) with null strongs_number" },
  "WR-05": { "r": "REVIEW", "d": "ID gaps detected in wa_term_inventory: [(69, 1554)]" },
  "WR-08": { "r": "REVIEW", "d": "Low verse/occurrence ratio: [...]" },
  "WR-13": { "r": "REVIEW", "d": "Undocumented nulls in API-derivable fields: ['G_mēnis.occurrence_count', ...]" },
  "WR-18": { "r": "REVIEW", "d": "Terms without parsed meaning: ['G_mēnis', 'G_enkotēma', 'G_cholos', 'H5945H']" },
  "WR-01": { "r": "PASS",   "d": null },
  ...
}
```

### Why they are NOT in the quality flag tables

`wa_data_quality_flags` contains semantic/data-quality flags only (DATA_COVERAGE, TERM_ANALYSIS, NOTE, IMPORT_STATUS group codes). The WR-XX audit checks are engine-run diagnostics — they are not written to the flag tables.

### Optional enhancement

The `audit_detail` blob is stored as a serialised JSON string inside `run_history`. If a top-level structured field (e.g. `audit_checks[]`) is preferred for easier downstream consumption by Claude.ai, that can be added to `export_word()` — researcher to direct.

---

## Finding 2 — anger (registry 4) AUDIT_WORD REVIEW items — 24 March 2026

**Run:** `RUN-20260324_070256-AUDIT_WORD` | Result: **REVIEW** (4 checks)

| Check | Detail |
|---|---|
| WR-04 | 3 rows with `null strongs_number`: `G_mēnis`, `G_enkotēma`, `G_cholos` (transliterated Greek terms with no Strong's number assigned) |
| WR-05 | ID gap `(69, 1554)` in `wa_term_inventory` — structural artefact from new terms being appended |
| WR-08 | 64 terms with low verse/occurrence ratio — primarily G2/G2r related terms with no separate verse records fetched (expected for high-frequency sub-glosses) |
| WR-13 | `occurrence_count` is NULL for the 3 transliterated Greek terms (`G_mēnis`, `G_enkotēma`, `G_cholos`) |
| WR-18 | 4 terms without parsed meaning: `G_mēnis`, `G_enkotēma`, `G_cholos`, `H5945H` |

**Root cause of WR-04 / WR-13 / WR-18:** The 3 transliterated Greek terms have no Strong's number and no meaning text — they were included in the Step 1 extract as cluster-related terms but carry no STEP data fields. Researcher to decide whether to assign placeholder Strong's numbers or exclude them.

**WR-05 / WR-08:** Expected structural artefacts — no action required unless researcher decides otherwise.

No action will be taken on any REVIEW item without explicit researcher instruction.
