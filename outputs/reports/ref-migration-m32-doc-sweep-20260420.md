# Reference Migration M32 — Document Sweep Record — 2026-04-20

| Field | Value |
|---|---|
| Migration | M32 — `wa_vocab_set` + `wa_vocab_member` seed (5 vocabularies, 27 members) |
| Framework cycle step | 5 — Document sweep |
| Scope | Session_B instruction docs that duplicate/enumerate M32-scope vocabularies |
| Produced | 2026-04-20 |

---

## 1. Scope of this sweep

M32 migrated five vocabularies into the DB as the new single source of truth:

| Set code | Members | Governing doc |
|---|---:|---|
| `DIMENSION_LABEL` | 11 | wa-dimensionreview-instruction §7.7 |
| `DOMINANT_SUBJECT` | 5 | wa-dimensionreview-instruction §7.7 (Dim 11 note), DR-12 |
| `DIMENSION_CONFIDENCE` | 3 | wa-dimensionreview-instruction |
| `QA_FLAG` | 6 | wa-dimensionreview-instruction §6.3 + §7.3 |
| `MANUAL_OVERRIDE` | 2 | wa-dimensionreview-instruction + DR-8 |

**Sweep target:** Session_B instruction docs that **duplicate or declare** these vocabularies (not docs that merely *use* the values in analytical narrative — those stay intact).

**Docs with matches (grep pattern for M32 vocab values):**

- `wa-dimensionreview-instruction-v3_3-20260418.md` — declares the vocabularies
- `wa-reference-v5_7-20260420.md` — mirrors
- `wa-registry-management-guide-v5_10-20260418.md` — analytical narrative (uses values)
- `wa-registry-management-guide-v5.9-20260414.md` — older version; superseded
- `wa-sessionb-analysis-output-v1_1-20260418.md` — analytical narrative
- `wa-sessionb-analysis-readiness-v1_6-20260418.md` — analytical narrative
- `wa-global-readiness-sweep-instruction-v1_0-20260419.md` — analytical narrative (uses values)

---

## 2. Sweep actions taken

### 2.1 wa-reference-v5_7 §4.3 — CANONICAL SOURCE HEADER UPDATED

**Before:** "CANONICAL SOURCE: `wa-dimensionreview-instruction [current]` §7.7" — doc-to-doc pointer.

**After:** "CANONICAL SOURCE: DB `wa_vocab_set.DIMENSION_LABEL` (M32 2026-04-20)" — doc-to-DB pointer. Added: "AI sessions should consume this via the reference snapshot (`data/exports/reference/wa-reference-snapshot-{YYYYMMDD}.json`)". Mirrored table remains inline for reference but is marked as derived (DB wins on divergence).

### 2.2 wa-dimensionreview-instruction-v3_3 §7.7 — DB POINTER ADDED

**Before:** "*Derived from data. Working vocabulary as of v3.1.*" + inline dimension list.

**After:** Added paragraph at top of §7.7: "Canonical source (2026-04-20): DB `wa_vocab_set.DIMENSION_LABEL`. The authoritative list lives in the DB; consume via reference snapshot. Inline definitions describe what each dimension means (instructional narrative); the value strings themselves are whatever the DB returns. CC validator `apply_session_patch.py::_canonical_dimensions()` rejects any patch whose dimension label is not in the DB."

Inline dimension definitions preserved — they have instructional value (describing each dimension's *meaning* for analysts). Only the declaration-of-authority changed.

### 2.3 Other files — NO EDIT (intentional)

The remaining 5 docs use vocabulary values in analytical/instructional narrative (e.g., "when dominant_subject is HUMAN, proceed with X") rather than declaring them as authoritative lists. Per the sweep protocol, narrative USE is left intact; only DECLARATIONS are redirected to DB.

**Exception candidates for follow-up (if researcher wants tighter discipline):**

- `wa-registry-management-guide-v5.9-20260414.md` — older version, should be archived (superseded by v5_10). Not an M32 concern but tidy-up opportunity.

---

## 3. Validator rewire status

`scripts/apply_session_patch.py`:

- `CANONICAL_DIMENSIONS` back-compat alias retained pointing at `_FALLBACK_CANONICAL_DIMENSIONS` (pre-M32 safety net)
- New `_load_vocab_set(conn, set_code)` function — DB-first lookup
- New `_canonical_dimensions(conn)` function — DB-first with hardcoded fallback + [NOTE] logging
- Validator site for `wa_dimension_index.dimension` — now calls `_canonical_dimensions(conn)`
- Validator site for `wa_dimension_index.dominant_subject` — now calls `_load_vocab_set(conn, "DOMINANT_SUBJECT")` with hardcoded fallback
- Verified import-clean on live DB: 11 DIMENSION_LABEL + 5 DOMINANT_SUBJECT + 6 QA_FLAG members resolved

---

## 4. Reference snapshot — first run

`scripts/build_reference_snapshot.py --also-markdown` successfully emitted:

- `data/exports/reference/wa-reference-snapshot-20260420.json` — full snapshot
- `data/exports/reference/wa-reference-snapshot-20260420.md` — human-readable MD view

Snapshot reports:

- Vocabularies: 5 sets, 27 members
- Schema: 56 tables (live snapshot)
- Rules, patch_types, file_name_patterns, label_patterns, programme_prose_index: `_status: not-available` (awaiting M33–M35)

The MD view is suitable for AI session-start loading; JSON is suitable for programmatic consumption.

---

## 5. Outcomes

- **DB is now the single source of truth** for 5 vocabularies (dimensions, dominant_subject, dimension_confidence, QA flags, manual_override)
- **Validator enforces DB canonical** on patch apply — future patches with non-canonical values fail fast
- **Session-start snapshot available** — AI loads `wa-reference-snapshot-{date}.json` instead of (or alongside) the `wa-reference` document
- **Canonical source pointers updated** in wa-reference §4.3 and DimReview §7.7 — each now points to the DB as authoritative
- **Hardcoded fallback retained** — validator still works if snapshot is missing or empty; emits `[NOTE]` in that case

---

## 6. Remaining framework steps (M33–M35)

Per `outputs/investigations/reference-as-database-framework-execution-20260420.md` §2:

| Phase | Scope | Status |
|---|---|---|
| M33 | `wa_rule_registry` + seed from `wa-global-general-rules-v2_11-20260418.json` | pending approval |
| M34 | Prose-store `source_stage='programme'` + seed 6-10 section types | pending |
| M35 | `wa_patch_type_registry` + `wa_file_name_pattern` + `wa_label_pattern` | pending |
| Post-M35 | Populate programme prose (PROSE patches) + deprecate `wa-reference` | pending |

---

*Sweep complete — M32 cycle closed. Awaiting researcher approval to start M33.*
