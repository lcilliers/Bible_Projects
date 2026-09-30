# Session B v1.8 Stage 2c — CC Compliance Digest

**Date:** 2026-04-30
**Reviewed file:** [Workflow/Instructions/wa-sessionb-analysis-output-v1_8-20260430.md](../../Workflow/Instructions/wa-sessionb-analysis-output-v1_8-20260430.md) (1,520 lines)
**Reviewer:** Claude Code
**Purpose:** Confirm CC understanding of v1.8 Stage 2c rewrite, enumerate the six CC actions required, identify schema and code changes, and lay out an implementation plan.

---

## 1. What changed in v1.8

Stage 2c is no longer a prose-chapter-writing stage. It is a **structured analytical synthesis pass** that produces 28 mandatory entries per registry — 7 intra-tier (T1–T7) + 21 inter-tier pairs — recorded in the obslog as `**SYN-INTRA-{NNN}-{seq}**` and `**SYN-INTER-{NNN}-{seq}**` markers and written to `wa_session_b_findings` as new finding types `SYNTHESIS_INTRA_TIER` and `SYNTHESIS_INTER_TIER`. Session C reads these synthesis findings from the database and writes the reader-facing word story.

**T0 is excluded from Stage 2c entirely.** T0 findings from Stage 2b are held in the database for Session D cross-registry synthesis. Stage 2c covers T1–T7 only.

**Every entry carries one of three outcomes:**

| Outcome | Code | Required content |
|---|---|---|
| Described | D | Substantive synthesis finding citing ≥2 Q&A entries |
| Further research | F | Question that cannot be resolved from current evidence; SD pointer always written |
| Not applicable | N | One-sentence rationale required |

**21 inter-tier pairs** are exhaustive: T1×T2, T1×T3 ... T6×T7. CC's parser verifies the count is exactly 28 per registry; below 28 raises `DATA_ANOMALY_SYNTHESIS_INCOMPLETE`.

---

## 2. The six CC actions enumerated

### Action 1 — New finding_type values

Add to `wa_session_b_findings.finding_type` controlled vocabulary:

| Value | Use |
|---|---|
| `SYNTHESIS_INTRA_TIER` | Single-tier synthesis (T1, T2, ... T7) — 7 per registry |
| `SYNTHESIS_INTER_TIER` | Tier-pair synthesis (T1×T2, ... T6×T7) — 21 per registry |

**Schema check (verified 2026-04-30):** `wa_session_b_findings.finding_type` is `TEXT NOT NULL` with no CHECK constraint. The 28 existing values are documentary, not enforced. Adding the two new values requires no schema change for the column itself — they are immediately writable. Vocabulary registration in `wa_vocab_set` / `wa_vocab_member` is recommended for governance but not strictly required for the parser to work.

**Status: ready to implement** — column is permissive, no migration blocks the writes.

### Action 2 — New metadata fields on synthesis findings

Five new fields are required:

| Field | Type | Controlled values | Use |
|---|---|---|---|
| `synthesis_outcome` | TEXT | `D` / `F` / `N` | The outcome code per entry |
| `tiers_engaged` | TEXT | comma-separated `T{n}` codes (e.g. `T2` or `T2,T3`) | Which tier(s) the entry covers |
| `structural_relationship` | TEXT | `causal` / `enabling` / `sequential` / `constitutive` / `tension` / `parallel` / `N/A` | For inter-tier D entries; named relationship type |
| `session_c_chapter` | TEXT | comma-separated `Ch1`..`Ch5` or `N/A` | Routing hint for Session C extract builder |
| `sd_pointer_ref` | TEXT | `SP-{NNN}-{seq}` or NULL | Back-reference for F-outcome entries |

**CC recommendation: add as columns on `wa_session_b_findings`.** Reasoning:

- Schema is already wide (20 columns); 5 more is acceptable.
- Synthesis findings will be ~28 per registry × ~80 registries = ~2,240 rows. Linked-table approach would add ~2,240 join rows and a separate index — disproportionate.
- All 5 fields are NULL for non-synthesis findings (1,068 existing rows) which is a clean "feature-only-on-this-finding-type" pattern. SQLite stores NULL columns efficiently.
- Queries like `SELECT * FROM wa_session_b_findings WHERE synthesis_outcome IS NOT NULL` are immediately useful; equivalent JOIN queries would be less readable.

**Status: schema migration script needed** — will be run at the same time the first v1.8 obslog is captured.

### Action 3 — Parser extension for SYN markers

CC's obslog parser (today: `scripts/_pilot_parse_obslog_to_db_v1_20260427.py` and `scripts/_pilot_capture_obslog_to_db_v1_20260427.py`) must recognise:

- `**SYN-INTRA-{registry:03d}-{seq:03d}** | T{N} — {tier title}` block — writes one `wa_session_b_findings` row with `finding_type='SYNTHESIS_INTRA_TIER'` and the 5 new fields populated from the bullet metadata
- `**SYN-INTER-{registry:03d}-{seq:03d}** | T{N} × T{N}` block — writes one row with `finding_type='SYNTHESIS_INTER_TIER'`
- `Source Q&A:` field — comma-separated `Q&A-{seq:03d}` tokens — each token resolves to a `wa_finding_catalogue_links` row linking the synthesis finding to the source Q&A entry's existing finding row

**Bullet field parsing rules:**

| Bullet | Maps to |
|---|---|
| `Entry type:` | (validation only — must match marker) |
| `Tier:` (intra) / `Tiers:` (inter) | `tiers_engaged` (joined comma) |
| `Components considered:` (intra) | `study_segment` (reused — comma-joined components) |
| `Source Q&A:` | one `wa_finding_catalogue_links` row per Q&A token, linking finding to Q&A's question_id |
| `Outcome:` | `synthesis_outcome` |
| `Finding:` | `finding` (full text) |
| `Structural relationship:` (inter only) | `structural_relationship` |
| `Session C chapter:` | `session_c_chapter` |
| `SD pointer:` | `sd_pointer_ref` (`NONE` → NULL) |

**Status: parser extension needed when first v1.8 obslog arrives.** No v1.8 obslog has been produced yet — the 5 captured words used the v1.7 second-tier model without Stage 2c synthesis. Parser work can be deferred until then.

### Action 4 — 28-entry completeness audit

CC's post-parse audit must verify per registry:

- Intra-tier count = 7 (T1 through T7)
- Inter-tier count = 21 (all unique pairs within T1–T7)
- T0 absent
- Total = 28

A count below 28 raises `DATA_ANOMALY_SYNTHESIS_INCOMPLETE` for the registry. Implementation:

```sql
SELECT
  registry_id,
  SUM(CASE WHEN finding_type = 'SYNTHESIS_INTRA_TIER' THEN 1 ELSE 0 END) AS intra_count,
  SUM(CASE WHEN finding_type = 'SYNTHESIS_INTER_TIER' THEN 1 ELSE 0 END) AS inter_count,
  COUNT(*) AS total_synth
FROM wa_session_b_findings
WHERE finding_type LIKE 'SYNTHESIS_%'
  AND delete_flag = 0
GROUP BY registry_id
HAVING intra_count != 7 OR inter_count != 21
```

Plus a check that no synthesis entry's `tiers_engaged` mentions `T0`.

**Status: easy follow-on once schema is in place.**

### Action 5 — Session D routing for F-outcome entries

The instruction asks: is `sd_pointer_ref` (text field) sufficient to link an F-outcome synthesis finding to its SD pointer in `wa_session_research_flags`, or do we need an explicit FK column?

**Recommendation: text field is sufficient.** Reasoning:

- The text field carries the `flag_label` (e.g. `SP-067-T2-019`), which is `UNIQUE` on `wa_session_research_flags`. A look-up `JOIN wa_session_research_flags sf ON sf.flag_label = f.sd_pointer_ref` is cheap and unambiguous.
- Adding an FK column means an extra integer column + an index, for a relationship that is already 1-to-1 and easy to resolve via the unique label.
- The inverse direction (SD pointer → which synthesis finding raised me?) can be answered with the same JOIN reversed.

If governance wants stricter FK semantics later, the column can be added without breaking the text field's existing meaning.

**Status: no further action — text field is the chosen approach.**

### Action 6 — Extract builder update (`build_complete_extract.py`)

The `--scope=final` extract for Session C needs Stage 2c synthesis structure. Required changes:

| Section | Content |
|---|---|
| **Intra-tier D entries** | Grouped by tier (T1, T2, ... T7); each carrying `Session C chapter` tag |
| **Inter-tier D entries** | Grouped by primary tier combination; each carrying `Session C chapter` tag |
| **F-outcome entries** | Listed separately as open research questions, with SD pointer reference |
| **N-outcome entries** | **Omitted** from Session C extract (held in DB for programme record) |
| **T0 Q&A findings** | Surfaced **separately** for Session D extract — not in Session C |

**Status: `build_complete_extract.py` update needed before first Session C run that uses v1.8-derived data.** Defer until the first synthesis-pass obslog is captured (no Session C run is pending in the immediate term).

---

## 3. Implementation plan

### Phase 1 (now): schema migration — Actions 1 + 2

Add 5 columns to `wa_session_b_findings`:

```sql
ALTER TABLE wa_session_b_findings ADD COLUMN synthesis_outcome TEXT;
ALTER TABLE wa_session_b_findings ADD COLUMN tiers_engaged TEXT;
ALTER TABLE wa_session_b_findings ADD COLUMN structural_relationship TEXT;
ALTER TABLE wa_session_b_findings ADD COLUMN session_c_chapter TEXT;
ALTER TABLE wa_session_b_findings ADD COLUMN sd_pointer_ref TEXT;
```

Plus optional vocab registration in `wa_vocab_set` / `wa_vocab_member` for the controlled-vocabulary fields (`synthesis_outcome`, `structural_relationship`).

**Idempotent:** check for column presence before ALTER. **Transactional with backup.**

### Phase 2 (when first v1.8 obslog arrives): parser extension — Action 3

Extend the existing pilot parser (or build a successor) to:

- Recognise `## Stage 2c — Synthesis Entries` section header
- Parse `**SYN-INTRA-{NNN}-{seq}**` and `**SYN-INTER-{NNN}-{seq}**` blocks
- Walk bullet fields (`Tier:`, `Tiers:`, `Components considered:`, `Source Q&A:`, `Outcome:`, `Finding:`, `Structural relationship:`, `Session C chapter:`, `SD pointer:`)
- Write one `wa_session_b_findings` row per block with `finding_type='SYNTHESIS_*'` and the 5 new columns populated
- For each `Q&A-{seq}` token in `Source Q&A:`, write a `wa_finding_catalogue_links` row linking the new synthesis finding to the source Q&A's question_id (looked up via the existing finding for that Q&A)

### Phase 3 (immediately after parser): completeness audit — Action 4

Add to CC's post-parse audit:

- Per-registry synthesis-count check (7 intra + 21 inter = 28)
- T0-not-present check
- F-outcome → SD pointer existence check
- D-outcome inter-tier → `structural_relationship` populated check
- Raise `DATA_ANOMALY_SYNTHESIS_INCOMPLETE` for anomalies

### Phase 4 (before next Session C run): extract builder — Action 6

Update `scripts/build_complete_extract.py` `--scope=final` path:

- Add new sections for intra/inter/F-outcome/T0 groupings
- Surface `session_c_chapter` tags
- Filter out N-outcome from Session C view
- Surface T0 separately for Session D

### Phase 5 (cosmetic, can land any time): vocab registration

Add controlled-vocab entries:

- `wa_vocab_set('finding_type — SYNTHESIS')` with members `SYNTHESIS_INTRA_TIER`, `SYNTHESIS_INTER_TIER`
- `wa_vocab_set('synthesis_outcome')` with members `D`, `F`, `N`
- `wa_vocab_set('structural_relationship')` with members `causal`, `enabling`, `sequential`, `constitutive`, `tension`, `parallel`, `N/A`

---

## 4. Concerns and open questions

### 4.1 Existing finding_id format for synthesis entries

The instruction's marker is `**SYN-INTRA-{registry:03d}-{seq:03d}**`. CC's writer should produce `finding_id` values in the form `SYN-INTRA-{NNN}-{seq:03d}` and `SYN-INTER-{NNN}-{seq:03d}`. These are distinct from existing patterns (`OBS-NNN-MMM`, `OBS-NNN-T2-MMM`, `DIM-NN-NNN`, `ANOMALY-NNN-NNN`). No collision risk — confirmed.

### 4.2 The `seq` numbering for Stage 2c

The instruction says: *"`{seq}` is sequential across both intra- and inter-tier entries within a registry (001..NNN)"*. So a registry might have:

- SYN-INTRA-067-001 (T1)
- SYN-INTRA-067-002 (T2)
- SYN-INTRA-067-003 (T3)
- ...
- SYN-INTRA-067-007 (T7)
- SYN-INTER-067-008 (T1×T2)
- ...
- SYN-INTER-067-028 (T6×T7)

Total 28 sequential numbers. **CC's parser should not enforce a specific tier-order**, only that the count and tier coverage are correct.

### 4.3 Session C chapter tags reuse the legacy chapter labels

The `session_c_chapter` field uses `Ch1`..`Ch5`, which are the legacy Stage 2c chapter codes. Under v1.8, Stage 2c no longer writes prose chapters — but Session C still produces chapters by these codes. The tag is a routing hint for Session C, not a Stage-2c output target. **No conflict.**

### 4.4 Deprecation of `prose_section` `sb_s2c_ch1`..`sb_s2c_ch6` rows

Existing programme has `prose_section` rows for the old six chapters — including the goodness corpus prose (R067) which is a real prior session's output. **These are not deleted.** They remain as historical record. Session C, going forward, reads from synthesis findings (in `wa_session_b_findings`) rather than producing fresh `sb_s2c_ch*` prose rows. The legacy prose rows can be superseded individually under §7 prose-revision discipline if a revision session touches them.

### 4.5 `study_segment` reuse for `Components considered:`

For SYN-INTRA entries, the instruction says `Components considered:` lists all component codes in the tier (e.g. `T2.1, T2.3, T2.6, T2.8, T2.10`). I propose storing this in the existing `study_segment` column (which today carries the catalogue v2 component code on per-Q&A findings). Reusing `study_segment` keeps the schema lean. Alternative: a new `tier_components` column. Recommend reuse.

### 4.6 Backwards compatibility with existing 725 v2 findings

The 725 catalogue-v2 findings already in the DB (5 words × ~150 each, finding_type='OBSERVATION') are unaffected by the schema additions — the 5 new columns will be NULL for those rows, which is correct. They continue to be queryable as Stage 2b Q&A-derived OBSERVATION findings.

---

## 5. Confirmation

I have understood v1.8 §Stage 2c, §8 markers, §9 citation discipline, §Closure Domain F, and SB-29. I can comply with all six CC actions. The schema migration (Actions 1+2) is safe to run now — it adds columns, no data migration needed, no risk to existing rows. Actions 3, 4, and 6 are deferred until the first v1.8-format obslog arrives. Action 5 is a no-op (text field is sufficient).

Phase 1 schema migration is the immediate next step.
