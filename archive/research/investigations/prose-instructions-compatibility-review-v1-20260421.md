# Prose Lifecycle — Patch + Directive Instruction Compatibility Review

**Date:** 2026-04-21
**Scope:** confirm that [wa-patch-instruction-v2_3](../../data/imports/WA/Workflow/Framework_B/Session_B/wa-patch-instruction-v2_3-20260421.md) and [wa-directive-instruction-v1_2](../../data/imports/WA/Workflow/Framework_B/Session_B/wa-directive-instruction-v1_2-20260421.md) cleanly support (a) **adding new prose** and (b) **editing existing prose** — both at the section-type level (the stubs / handles) and at the prose-content level (the bodies).
**Verdict:** partial coverage. The documents recognise PROSE as a patch type but do not specify its operation catalogue or workflow. The applicator has most of the machinery but has two known gaps that blocked today's one-off execution. This review itemises what's missing, what's safe, and a minimal fix plan.

---

## 1. What today's work proved

The programme-prose session on 2026-04-21 tried the full flow end-to-end:

1. **Schema enablement directive** intended (DIR-20260421-002) — *delivered only as a submission wrapper; the directive body was never placed on disk*.
2. **CATALOGUE_POPULATION patch** — intended to add 7 new `prose_section_type` rows. The applicator supports `prose_section_type insert` (line 1473 of [apply_session_patch.py](../../scripts/apply_session_patch.py)). This would have worked through the standard applicator.
3. **PROSE patch** — intended to add 7 new `prose_section` rows. **Failed on two applicator details**:
   - `required = ("registry_id", "section_type_id", ...)` — the validator rejects `registry_id = NULL` even after the schema is relaxed.
   - `section_type_id_lookup: {"code": "..."}` — Claude AI used this pattern to resolve section_type_id by code within the same patch run (parallel to `group_id` resolution in verse_context patches §12.2). The applicator has no resolver for it.

We bypassed with a one-off script ([_apply_prose_programme_chapter01.py](../../scripts/_apply_prose_programme_chapter01.py)) and committed the results. Useful for audit, but not a repeatable path.

---

## 2. Adding new prose — coverage audit

### 2.1 Adding a new section type (a new stub / handle)

| Element | Status | Notes |
|---|---|---|
| Patch type | ✓ `CATALOGUE_POPULATION` exists (v2_3 §3.3) | Also permitted as `PROSE` type per A.3 ("Prose section insert/supersede/approve") — choice is ambiguous today. |
| Applicator op | ✓ `insert` on `prose_section_type` | [apply_session_patch.py:1473](../../scripts/apply_session_patch.py#L1473), uses `INSERT OR IGNORE` so duplicate codes are skipped, not errored. |
| Instruction doc | ✗ **Not documented.** | v2_3 §4 (supported operation types) does not mention `prose_section_type`. The operation works but is not declared. |
| Worked example | ✗ None in v2_3. | Catalogue patch from today's session is a clean example but lives only in `archive/patches/`. |

**Gap:** the patch instruction needs a §4.x sub-section describing `insert on prose_section_type` — required fields (`code`, `label`, `source_stage`), optional fields (`lifecycle_tag`, `chapter_no`, `description`, `expected_length_min`, `expected_length_max`, `sort_order`), `INSERT OR IGNORE` semantics, and the recommended patch type (either CATALOGUE_POPULATION or a dedicated PROSE type — decide one).

### 2.2 Adding new prose content under an existing type

| Element | Status | Notes |
|---|---|---|
| Patch type | ✓ `PROSE` exists (v2_3 §3.3) | Null-exempt per §3.4. |
| Applicator op | ✓ `insert` on `prose_section` | [apply_session_patch.py:1323](../../scripts/apply_session_patch.py#L1323). |
| Field list | Partial | `registry_id` incorrectly in required list → rejects NULL post-schema-change. Needs fix. |
| `section_type_id_lookup: {code}` resolver | ✗ Missing | The natural pattern (parallel to verse_context §12.2) is not implemented; patches must supply integer ids, which requires splitting catalogue + content across two runs. |
| Programme-wide support | Partial — schema supports it, applicator does not | Schema fixed today; applicator needs the same relaxation. |
| Instruction doc | ✗ **Not documented.** | v2_3 has no PROSE operation section. v1_2 §10 covers the programme-wide case as a directive worked example but doesn't cover the general "add a prose body" flow. |

**Gap:** the patch instruction needs a §4.y sub-section for `insert on prose_section` — required fields (`section_type_id`, `body`, `status`, `author`), optional including `registry_id` (NULL = programme-wide), `heading`, `word_count` (auto-derived if omitted), `version` (default 1), `approved_at/by`, `metadata_json`, `source_file`. And a §12-style resolver section for `section_type_id_lookup`.

---

## 3. Editing existing prose — coverage audit

### 3.1 Editing a section type stub (label / description / sort_order)

| Element | Status | Notes |
|---|---|---|
| Applicator op | ✗ **No update handler** for `prose_section_type` | Only `insert` exists. To rename a stub or re-word its description, there is no patch route today. |
| Instruction doc | ✗ Not documented. | N/A until applicator supports. |

**Gap (blocking).** This came up today when we closed the sort_order gap in chapter 1 — had to go around the applicator with direct SQL. Also relevant when renaming M34 stubs per the structure design doc (7 of 8 M34 codes are flagged for rename).

**Fix:** add an `update` handler on `prose_section_type` matching on `id` or `code`, accepting any subset of mutable fields (label, description, chapter_no, sort_order, expected_length_min/max, lifecycle_tag). Mirror the `update` pattern used for `wa_rule_registry` in §13.4.2 of v2_3.

### 3.2 Editing existing prose content

The prose store has **two distinct edit semantics** by design:

| Operation | Applicator | Semantics | When to use |
|---|---|---|---|
| `supersede` | ✓ line 1350 | Creates a new row (v+1) and links it to the predecessor via `superseded_by_id`. Old row retained. | Substantive revisions, analytical restatement, any change worth versioning. |
| `session_a_replace` | ✓ line 1416 | In-place UPDATE. Restricted to `author = 'claude_code'` (Session A mechanical extracts only). | Session A auto-generated content only — NOT for narrative prose. |
| `approve` | ✓ line 1401 | Sets status → `approved`, stamps `approved_at` + `approved_by`. | Lifecycle transition from `in_review` to `approved`. |
| `delete` | ✓ line 1389 | Soft-deletes (`delete_flagged = 1`). | Retirement. |
| `bulk_supersede` | ✓ line 1437 | Systematic bulk revision via a target list + record template. | Programme-wide refactors. |
| `update` (in-place) | ✗ **Not implemented** | Would allow typo fixes without versioning. | Currently no route. |

**Gap (observational, not necessarily a bug).** There's no in-place update for narrative prose. Every correction, even a typo, has to go through `supersede`, which creates a new row. That may be intentional (full audit trail) but it means minor editorial passes proliferate `prose_section` rows.

**Decision needed.** Either:
- **(a)** Document the supersede-only discipline explicitly in v2_3, and accept that narrative prose is immutable at row level. Row count grows; every edit is audited; old versions stay discoverable.
- **(b)** Add a narrow `update_in_place` operation (or extend `session_a_replace` to drop the `author = 'claude_code'` constraint) — restricted to minor fixes where versioning is overkill. Risk: erodes audit guarantees.

My recommendation: **(a)**. The programme's soft-delete / no-destructive-edit discipline (GR-OBS-005, patch instruction §5.4) is consistent with supersede-only. Document it explicitly. If typo fixes become a real pain point later, revisit with (b).

### 3.3 Status lifecycle

Schema CHECK: `status IN ('draft','in_review','approved','archived')`. Applicator has explicit handlers for `approve`. There's no handler for:
- `draft → in_review` (submission for review)
- `approved → archived` (end-of-life, though `delete` may cover this)

**Gap (minor).** If `in_review` is a real checkpoint, a `transition` or `set_status` op would clarify the route. Or document that `in_review` is set at insert time and moves via direct update (which today doesn't exist — reinforces §3.1 gap above).

---

## 4. What's actually documented in v2_3 and v1_2

### v2_3 patch instruction
- §3.3 patch type registry lists PROSE as null-exempt, purpose "Prose section insert/supersede/approve"
- §2.4 programme-wide filename: `wa-prose-{section_code}-{action}-v{n}-{YYYYMMDD}.json`
- Appendix A.3: PROSE → "wa-reference [current] §13.14 (prose store)"
- **No §4 coverage of operations on prose_section / prose_section_type.**
- **No field catalogue for PROSE patches.**
- **No section on the section_type_id_lookup resolver.**

### v1_2 directive instruction
- §10.2 covers the one-time schema enablement directive (registry_id NOT NULL → nullable)
- **No coverage of editing-by-directive scenarios** for prose (there shouldn't be many — most edits should be patches, but e.g. bulk renames of section-type codes across content rows + type rows could be directive territory).

---

## 5. Minimal fix plan

### 5.1 Applicator (scripts/apply_session_patch.py)

1. **prose_section insert** — remove `registry_id` from the required list so NULL is accepted (2-line change around line 1326). The FK still enforces integrity if a non-null value is supplied.
2. **section_type_id_lookup resolver** — add a helper `_resolve_section_type_id(conn, record)` that accepts either `section_type_id` (integer) or `section_type_id_lookup: {"code": "..."}` (lookup in `prose_section_type.code`). Call at the top of the insert path before the `required` check. ~20 lines.
3. **prose_section_type update** — new handler similar to the rule_registry update pattern: match on `id` or `code`, set any subset of mutable fields, `last_modified` stamped. ~25 lines.
4. Optional: **prose_section status transition** — cleaner API than requiring researchers to call `approve` directly if the status is moving `draft → in_review`. Low priority.

### 5.2 v2_3 patch instruction — new §4 subsections

- **§4.13 `insert` on `prose_section_type`** — CATALOGUE_POPULATION patch format, INSERT OR IGNORE semantics, field catalogue.
- **§4.14 `update` on `prose_section_type`** — once the applicator support is added, document matching + mutable fields.
- **§4.15 `insert` on `prose_section`** — PROSE patch format, required vs optional fields, programme-wide with `registry_id = null`, `section_type_id` either numeric or via `section_type_id_lookup: {code}`.
- **§4.16 `supersede` / `approve` / `delete` / `bulk_supersede` on `prose_section`** — each with a worked example, immutability discipline noted.
- **§4.17 Prose revision discipline** — explicit rule: narrative prose uses `supersede` only; `session_a_replace` is restricted to Session A mechanical extracts by `author = 'claude_code'`; in-place updates are not supported by design.

### 5.3 v2_3 patch instruction — new §14 (parallel to §12 Verse Context and §13 Rules/Addenda)

**§14 Prose Updates** — worked patterns:
- Adding a new chapter: CATALOGUE_POPULATION patch with N `prose_section_type` inserts.
- Populating prose under existing types: PROSE patch with N `prose_section` inserts, using `section_type_id_lookup` resolver.
- Revising a prose body: PROSE patch with `supersede` operation.
- Retiring a section type (not deleting, just marking obsolete): apply `delete_flagged` via `update` on the type.

### 5.4 v1_2 directive instruction — §10.5 addition

Small addition to §10.5 (where the pattern recurs): note that adding columns to `prose_section` (e.g. a `tags` column later) uses the same schema-enablement pattern.

### 5.5 Sequencing the fix

Two reasonable orderings:

- **Doc-first** (safer): update instructions, get researcher agreement on the operation catalogue + revision discipline, then update the applicator to match. This lets v2_4 + v1_3 reach a stable state before we touch code. Downside: the gaps stay open for another day.
- **Code-first** (faster to unblock): patch the applicator (5.1 items 1–3, ~50 lines), then update v2_3 to reflect what the applicator now supports. Downside: docs lag until the next edit pass.

Recommendation: **code-first** — the applicator gaps blocked a real session today, and the doc updates fall naturally out of the code once it's nailed down.

---

## 6. Compatibility verdict

| Scenario | Works today? | Blocker |
|---|---|---|
| Add a new section type (stub) | Yes, via CATALOGUE_POPULATION or ad-hoc | Undocumented; works by happy accident. |
| Add prose content under existing type (registry-scoped) | Yes | Fine. |
| Add prose content under existing type (programme-wide, `registry_id = null`) | **No** | Applicator required-list rejects NULL. One-line fix. |
| Cross-patch `code → section_type_id` resolution | **No** | No resolver. Modest fix, parallel to verse_context group_id. |
| Edit a section type (rename, re-word description) | **No** | No update handler. Blocker for cleaning up M34 seed codes. |
| Revise prose content (new version, keep old) | Yes | Via `supersede`. Fine. |
| Fix a typo in prose (in-place, no new version) | By design: no | Use `supersede` or re-document the discipline. |
| Approve a draft | Yes | Via `approve`. Fine. |
| Retire prose | Yes | Via `delete` (soft). Fine. |

**Three concrete gaps** (items 3, 4, 5 in the table) are the blockers for cleanly supporting the programme-prose lifecycle. All three are in the applicator; documentation updates follow naturally.

---

## 7. Open questions for the researcher

1. **Edit-in-place vs supersede-only for narrative prose.** My read: supersede-only, documented explicitly. Confirm or redirect.
2. **Patch type for `prose_section_type` inserts** — keep using CATALOGUE_POPULATION, or move to PROSE? (Today's session used CATALOGUE_POPULATION — appropriate.)
3. **Revision authorship.** When Claude AI drafts a revision, should the author field flip to `claude_ai` even if the original was `claude_code` / `researcher`? Or retain the original? (My read: always reflect the author of the new row; provenance of the old row is preserved in `supersedes_id`.)
4. **Approval on programme-wide prose.** The programme prose currently sits at `status = 'draft'`. When you want these moved to `approved`, we'd use the `approve` op — does that need batch-style handling (approve all at once), or one-at-a-time per row?

---

*Review produced 2026-04-21; filename pattern `prose-instructions-compatibility-review-v1-20260421.md` per GR-FILE-001.*
