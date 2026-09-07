# WA-M05-patch-boundary-pverses-format-diff-v1-20260507

> Framework B Soul Word Analysis Programme
> Document type: Patch format correction record
> Cluster: M05 — Love, Compassion and Kindness
> Date: 20260507
> Original file: wa-cluster-M05-patch-boundary-pverses-v1-20260507.json
> Corrected file: wa-cluster-M05-patch-boundary-pverses-v2-20260507.json
> Standing rule: Claude AI patch format errors are not silently accommodated — a corrected sibling file is created and the diff documented rather than mutating the original.

---

## Summary

Three applicator-spec format errors were found in the v1 patch file. The v2 sibling corrects all three. No analytical content was changed — the verse assignments, group ids, mti_term_ids, verse_record_ids, notes text, input_versions, and operations_count are identical between v1 and v2.

The v1 file is retained as the historical record of the original Claude AI output. The v2 file is the submission to CC for application.

---

## Error 1 — `_patch_meta.terms_covered` wrong type

**Spec requirement (wa-patch-instruction-v2_11 §15, §3.3):** `terms_covered` must be a list of integer mti_term_ids.

**v1 (incorrect):**
```json
"terms_covered": {
  "6209": 2,
  "6845": 2
}
```

**v2 (corrected):**
```json
"terms_covered": [6209, 6845]
```

**Note:** The v1 value appears to have conflated `terms_covered` with `input_versions`. The version numbers (2, 2) belong in `input_versions` only. The `terms_covered` list carries mti_term_ids without version numbers. Both fields are present and correctly separated in v2.

---

## Error 2 — Operation field `values` → `set`

**Spec requirement (wa-patch-instruction-v2_11 §4, line ~325–334):** Each operation's update payload must be keyed `set`. The applicator dispatches on `set`; `values` is not a recognised key and would be silently ignored, causing a no-op application.

**v1 (incorrect) — both operations:**
```json
"values": {
  "is_relevant": 1,
  ...
}
```

**v2 (corrected) — both operations:**
```json
"set": {
  "is_relevant": 1,
  ...
}
```

**Impact of the error:** If applied as-is, the applicator would find no `set` key, treat the operations as empty updates, and write nothing — a silent no-op. The version gate would still fire and bump md_version, giving a false appearance of successful application. This is a high-severity format error.

---

## Error 3 — `op_id` missing from each operation

**Spec requirement (wa-patch-instruction-v2_11 §4, line ~325):** Each operation object must carry an `op_id` in `OP-NNN` format.

**v1 (incorrect) — both operations:** No `op_id` field present.

**v2 (corrected):**
- Operation 1 (Amo 5:21, mti=6209): `"op_id": "OP-001"`
- Operation 2 (2Pe 1:3, mti=6845): `"op_id": "OP-002"`

---

## Fields unchanged between v1 and v2

| Field | Value |
|---|---|
| `patch_type` | `VCREVISE` |
| `session_reference` | `wa-obslog-M05-love-compassion-kindness-v1-20260507 Phase 8 BOUNDARY` |
| `source_document` | `WA-M05-BOUNDARY-findings-v1-20260507.md` |
| `input_versions` | `{"6209": 2, "6845": 2}` |
| `operations_count` | `2` |
| Operation 1 `match` | `{"verse_record_id": 192566, "mti_term_id": 6209}` |
| Operation 1 payload content | `is_relevant=1, group_id=2148, set_aside_reason=null, notes=[verbatim]` |
| Operation 2 `match` | `{"verse_record_id": 215044, "mti_term_id": 6845}` |
| Operation 2 payload content | `is_relevant=1, group_id=2597, set_aside_reason=null, notes=[verbatim]` |

---

## Fields added in v2

| Field | Value | Reason |
|---|---|---|
| `_patch_meta.patch_id` | `wa-cluster-M05-patch-boundary-pverses-v2-20260507` | Version-bumped patch_id for the corrected file |
| `_patch_meta.supersedes` | `wa-cluster-M05-patch-boundary-pverses-v1-20260507` | Provenance link to the original |
| `_patch_meta.correction_note` | [see v2 file] | Brief statement of what was corrected and that no analytical content changed |

---

## CC instruction

Apply `wa-cluster-M05-patch-boundary-pverses-v2-20260507.json`. Do not apply v1. The v1 file is retained for the historical record only.

---

*WA-M05-patch-boundary-pverses-format-diff-v1-20260507*
*Cluster: M05 — Love, Compassion and Kindness*
*Correction of: wa-cluster-M05-patch-boundary-pverses-v1-20260507.json*
