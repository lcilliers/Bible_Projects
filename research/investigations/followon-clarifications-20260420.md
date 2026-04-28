# Follow-On Clarifications — 2026-04-20 End-of-Day

| Field | Value |
|---|---|
| Filename | followon-clarifications-20260420.md |
| Purpose | Elaborate on researcher-requested points (4 FLAG-016 audit scope; 5 validator DB-sourcing extension) |
| Status | INFORMATIONAL — for researcher decision |
| Produced | 2026-04-20 end-of-day |

---

## (4) FLAG-016 — programme-wide orphan audit

### 4.1 What FLAG-016 is

Raised during C01 Phase B (2026-04-20) when Directive DIR-20260420-001 executed on r183 group 577-005 and returned **0 surviving verses** for a group with 44 active `verse_context` classifications. Investigation showed: all 44 underlying `wa_verse_records` rows were `delete_flagged=1`. The verse_context records had been orphaned — classifications pointing at soft-deleted verse evidence.

**Analytical impact:** the group had a dimension assignment (MO=1) and an active classification history — but no verse evidence survived. Phase C would have made a dimension call on description alone, without the verse-level grounding Phase C normally requires.

**Likely cause:** historical audit_word re-runs or span-filter re-runs soft-deleted verses without cascading soft-delete to `verse_context`. A latent data-integrity gap.

The r183 patch cleaned this one case (delete_flagged vcg + cascade to 44 vc rows + annotated dim_index notes). FLAG-016 is raised to track the programme-wide question: **how many other groups are in the same state?**

### 4.2 The audit query (programme-wide)

One SQL query answers the scope question:

```sql
WITH group_vr_status AS (
  SELECT vcg.id AS group_id,
         vcg.group_code,
         vcg.mti_term_id,
         mt.owning_registry_fk,
         COUNT(vc.id) AS total_active_vc,
         SUM(CASE WHEN vr.delete_flagged = 0 THEN 1 ELSE 0 END) AS surviving_vr,
         SUM(CASE WHEN vr.delete_flagged = 1 THEN 1 ELSE 0 END) AS deleted_vr
    FROM verse_context_group vcg
    JOIN mti_terms mt ON mt.id = vcg.mti_term_id
    LEFT JOIN verse_context vc
      ON vc.group_id = vcg.id AND vc.delete_flagged = 0
    LEFT JOIN wa_verse_records vr
      ON vr.id = vc.verse_record_id
   WHERE vcg.delete_flagged = 0
   GROUP BY vcg.id
)
SELECT owning_registry_fk, group_id, group_code,
       total_active_vc, surviving_vr, deleted_vr
  FROM group_vr_status
 WHERE total_active_vc > 0
   AND surviving_vr = 0
 ORDER BY owning_registry_fk, group_code;
```

**Orphan condition:** `total_active_vc > 0 AND surviving_vr = 0` — group has classifications but no surviving verse evidence.

### 4.3 Expected findings

Unknown until the query runs. Candidates for why orphans might exist programme-wide:

- Historical audit_word re-runs that soft-deleted verses without cascade
- Span-filter re-extractions that discarded verses
- Test/development residue from early pipeline cycles
- Import corrections that didn't cascade

Likely a small-to-moderate set — if it were pervasive, the dimension review earlier would have surfaced more than one instance.

### 4.4 Action on findings

Per orphan group, three dispositions (same as used for r183 group 577-005):

- **(a) Restore** — re-run extraction to recover the verses (may not be possible if verses were never there)
- **(b) Soft-delete cascade** — delete_flag the vcg + cascade to 44+ vc rows + annotate dim_index notes (like r183 577-005)
- **(c) Convert to description-only** — keep the group's dim assignment on description evidence alone (risky)

For a mass cleanup: (b) by default; (a) only where re-extraction is tractable; (c) rarely.

### 4.5 Scope + effort

- **Run the audit query:** trivial — one SQL query, seconds
- **Produce the finding list:** small markdown report — minutes
- **Remediate:** depends on count. If <10, case-by-case. If 10-100, a REPAIR patch covering all (same pattern as M29 THIN_DATA dedup). If >100, a migration.

**When to run:** ideally **before starting DimReview on any other cluster** — same issue could surface during any Phase B. Cheap insurance.

### 4.6 Researcher decision point

Run the audit now (< 5 minutes) — get the scope, decide remediation approach. Or defer until the next cluster DimReview actually trips on an orphan (reactive approach).

CC recommendation: run the audit. Zero cost to get the data; high value if the orphan count is non-trivial.

---

## (5) Extending validator DB-sourcing

### 5.1 Current state (post M32-M35)

`apply_session_patch.py` has **2 validator sites** rewired to query DB (M32 cycle):

- `wa_dimension_index.dimension` → validates against `wa_vocab_set.DIMENSION_LABEL` via `_canonical_dimensions(conn)`
- `wa_dimension_index.dominant_subject` → validates against `wa_vocab_set.DOMINANT_SUBJECT` via `_load_vocab_set(conn, "DOMINANT_SUBJECT")`

### 5.2 What extension means

Take the same pattern and apply it to other fields / checks, pulling vocabularies / patterns / registries from DB at validation time rather than hardcoding.

### 5.3 Candidate extensions (available; not yet implemented)

| # | Site | Field / check | DB source |
|---|---|---|---|
| 5-1 | `wa_dimension_index` update | `dimension_confidence` | `wa_vocab_set.DIMENSION_CONFIDENCE` (3 values) |
| 5-2 | `wa_dimension_index` update | `manual_override` value (0 or 1 only) | `wa_vocab_set.MANUAL_OVERRIDE` (2 values) |
| 5-3 | `_patch_meta.patch_type` | patch type exists + status-exempt check | `wa_patch_type_registry` (15 types) |
| 5-4 | Finding insert ops | `finding_id` format matches `DIM-{nnn}-{NNN}` or `PH2-{nnn}-{NNN}` | `wa_label_pattern` — regex validation |
| 5-5 | SD pointer insert ops | `flag_label` format matches `DIM-{nnn}-SD{NNN}` | `wa_label_pattern` — regex validation |
| 5-6 | Patch filename on disk | matches `wa_file_name_pattern` entry | `wa_file_name_pattern` — regex validation |
| 5-7 | Rule-cited compliance | when a patch carries a rule_id reference, verify it exists in `wa_rule_registry` and is not obsolete | `wa_rule_registry` |
| 5-8 | Observation log section types | validate against `prose_section_type` where `source_stage='programme'` | `prose_section_type` |

### 5.4 Value proposition

Currently a patch can be produced with (for example):

- Undocumented `dimension_confidence` value (e.g. `CLAUDE_AI_STRONG`) — silently accepted
- Malformed `finding_id` like `112-DIM-004` instead of `DIM-112-004` — accepted
- Patch type `DIMREV` (typo for `DIMREVIEW`) — accepted if `session_b_status` fallback triggers
- `flag_label` referencing a rule ID that was retired in a prior version — accepted

With DB-sourced validation, each of the above fails fast at apply time with a clear error pointing at the canonical source.

### 5.5 Cost

| Extension | Lines of code | Complexity | Value |
|---|---|---|---|
| 5-1 DIMENSION_CONFIDENCE | ~5 | trivial | medium — catches typos |
| 5-2 MANUAL_OVERRIDE | ~5 | trivial | low — rarely wrong |
| 5-3 patch_type | ~10 | low | high — centralises the now-scattered exempt logic |
| 5-4/5-5 label format | ~15-20 each | medium (regex derivation) | high — today's r112/r183 patches had label-format nuances |
| 5-6 filename pattern | ~15 | medium | low-medium — filename is producer-side, not apply-side |
| 5-7 rule compliance | ~15 | medium | situational — only when patches cite rules |
| 5-8 prose section types | ~10 | low | low — PROSE patches are rare |

**Total if all 8 implemented:** ~80-100 lines of straightforward validation code.

### 5.6 Options

- **(A) Implement all 8 now.** One focused sitting. Comprehensive DB-validator coverage from here on.
- **(B) Implement the high-value subset (5-3 patch_type, 5-4/5-5 label format).** Addresses the specific defects we hit today in r112/r183 patches (OP-075 schema mismatch class).
- **(C) Lazy — add each as a specific issue surfaces.** Minimises upfront work; accepts occasional regressions.

CC recommendation: **(B) — the high-value subset now.** Patch-type validation (5-3) and label-format validation (5-4/5-5) would have caught real issues in today's DimReview patches. The others are nice-to-have; can be added as needed.

### 5.7 What each extension looks like (5-3 example)

```python
# In _validate() pre-apply path:
ptype = meta.get("patch_type", "")
if ptype:
    registered = _load_patch_type(conn, ptype)  # new helper
    if registered is None:
        errors.append(
            f"_patch_meta.patch_type {ptype!r} not in wa_patch_type_registry — "
            f"reject. Valid types: {sorted(_load_all_patch_types(conn))}"
        )
    elif not registered["session_b_status_exempt"] and not meta.get("session_b_status"):
        errors.append(
            f"_patch_meta.session_b_status required for patch_type {ptype!r} "
            f"(per wa_patch_type_registry)"
        )
```

Similar pattern for label-format regex validation (5-4, 5-5).

### 5.8 Researcher decision point

Choose (A), (B), or (C). Each extension is small. Recommend (B) — implement 5-3 + 5-4 + 5-5 in next working session; defer the rest until specific need surfaces.

---

## Researcher response expected

- **(4)** — run the orphan audit now, or defer?
- **(5)** — (A) / (B) / (C) for validator extension scope?

Neither is blocking. Both are programme-hygiene follow-ons.

---

*End of follow-on clarifications.*
