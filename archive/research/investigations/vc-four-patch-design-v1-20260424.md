# VC Session Output — Four-Patch Design (execution brief)

**Date:** 2026-04-24
**Approval basis:** researcher direction 2026-04-24 — "update both the instruction (to give full detail to preparing the 4 patches) and the prose (to include why and what to expect from the outputs) … and check the patch instruction (update if needed) to cater for these new patches."

This brief fixes the four-patch design and lists the execution steps for the researcher's approval of the direction before edits land.

---

## 1. The four patch types

A VC session (identified by `VCB-{nnn}` — same id across all artefacts of the session) produces up to four patches, one per output class. Each may be empty and therefore not produced.

| # | Type (new) | Covers | Primary table |
|---|---|---|---|
| 1 | **`VCNEW`** | (b) New VC data — first-time classifications for terms not yet seen | `verse_context_group` + `verse_context` (inserts) |
| 2 | **`VCREVISE`** | (a) Changes to existing VC data — revisions, reassignments, dissolves | `verse_context_group` + `verse_context` (updates, including `delete_flagged = 1`) |
| 3 | **`VCSBFLAGS`** | (c) Session B observations raised while reading verses | `wa_session_research_flags` (inserts, `session_target = 'Session B'`) |
| 4 | **`VCSDPOINTERS`** | (d) Cross-term / cross-registry pointers for Session D | `wa_session_research_flags` (inserts, `session_target = 'Session D'`, `cross_registry_id` populated) |

**Why four separate patches rather than one combined:**

- Clear scope per patch — the reviewer sees one type of output per file.
- Each patch is applied in its own transaction — a failure in (c) doesn't roll back (a)+(b).
- Matches existing programme pattern of type-specific patches (CLUSTERING, CATALOGUE_POPULATION, etc.).
- Patch archive has clean provenance per output type.
- Any patch may be absent from a session (e.g. a session that only re-evaluates — no new VC, just revisions — produces only VCREVISE).

The existing `VERSECONTEXT` patch type is retained (not removed) for backwards compatibility with prior VC patches; new VC sessions under v3_3 produce the four new types instead.

## 2. Apply order

All four carry `batch_id` (the session id) so Claude Code and auditors can correlate. Recommended apply order:

1. **`VCNEW`** first — new groups must exist before revisions can reference them
2. **`VCREVISE`** second — operates on existing rows (pre-session and newly created)
3. **`VCSBFLAGS`** third — independent of (1) and (2)
4. **`VCSDPOINTERS`** fourth — independent of (1) and (2)

Independence of (3) and (4) means they can run in either order; the convention is SB-before-SD for reading consistency.

## 3. `_patch_meta` per type

All four share the standard header (`patch_id`, `batch_id`, `produced_date`, `produced_by`, `session_b_status`: null, `description`). Additional required fields:

- **`VCNEW`** and **`VCREVISE`**: require `_patch_meta.terms_covered` — array of `mti_term_id`s this patch touches. For VCNEW this lists terms receiving first-time classification; for VCREVISE terms being revised. The applicator writes `mti_terms.vc_status = 'complete'` for terms in `terms_covered` on VCNEW apply (their first complete); for VCREVISE, `vc_status_updated_at` is bumped but `vc_status` stays `'complete'` (revising a term that was already complete).
- **`VCSBFLAGS`** and **`VCSDPOINTERS`**: `terms_covered` optional (the flags reference terms via `strongs_reference` on each row); `registry_affected` as an informational array of registry numbers touched by the flags.

## 4. Files to update

| Artefact | Current | New | Scope |
|---|---|---|---|
| Patch instruction | v2_4 | v2_5 | Add 4 new rows to §3.3 and §3.4 tables; pipeline sequence §3.6 updated; short §12.X per new type. |
| VC instruction | v3_2 | v3_3 | §7 completely rewritten for 4-patch output; §6.2 Step 6 updated; §6.6 deprecated (VCSBFLAGS replaces the `.md`); §13.3 resolved for A-01 (DB state is the gate); §7.9 new ("Session output taxonomy"). |
| `prog_instr_verse_context` prose | v2 | v3 | Expand the governance narrative to describe the four-type output and what each produces. |
| Applicator (`apply_session_patch.py`) | current | — | Add 4 new types to `sb_exempt_types`; extend the VC-2 handler (`_apply_versecontext_term_updates`) to trigger on VCNEW + VCREVISE (not just VERSECONTEXT). |
| `wa_patch_type_registry` (DB) | 17 types | 21 types | CATALOGUE_POPULATION patch inserts 4 rows. |

## 5. Detailed per-patch spec (goes into VC instruction v3_3 §7)

### 5.1 VCNEW

**Filename:** `wa-vcb-{batch_id}-patch-vcnew-v{n}-{date}.json`
**When produced:** when the session classifies any term for the first time (any `insert` on `verse_context_group` or `verse_context`).
**When absent:** when every term in the session has prior classifications and no new groups/verse_context rows are created.

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VCNEW-V1",
    "batch_id": "VCB-{nnn}",
    "terms_covered": [142, 187],
    "governing_instruction": "wa-versecontext-instruction-v3_3-{date}.md",
    "session_b_status": null,
    "description": "VC new classifications — VCB-{nnn}, {n} terms, {n} groups, {n} verse_context rows"
  },
  "operations": [
    { "op_id": "OP-001", "operation": "insert", "table": "verse_context_group", "record": { "mti_term_id": 142, "group_code": "142-001", "context_description": "…", "delete_flagged": 0 } },
    { "op_id": "OP-002", "operation": "insert", "table": "verse_context",       "record": { "verse_record_id": 4821, "mti_term_id": 142, "group_id": "142-001", "is_anchor": 1, "is_relevant": 1, "is_related": 0 } }
    /* … */
  ],
  "_patch_summary": {
    "total_operations": 0,
    "group_inserts": 0,
    "verse_context_inserts_anchor": 0,
    "verse_context_inserts_related": 0,
    "verse_context_inserts_set_aside": 0
  }
}
```

### 5.2 VCREVISE

**Filename:** `wa-vcb-{batch_id}-patch-vcrevise-v{n}-{date}.json`
**When produced:** when the session revises any existing `verse_context_group` or `verse_context` row — reclassifies a verse, promotes/demotes an anchor, revises a group description, dissolves a group (`delete_flagged = 1`).
**When absent:** on a pure first-time-classification session (no revisions).

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VCREVISE-V1",
    "batch_id": "VCB-{nnn}",
    "terms_covered": [142],
    "governing_instruction": "wa-versecontext-instruction-v3_3-{date}.md",
    "session_b_status": null,
    "description": "VC revisions — VCB-{nnn}, {n} terms, {n} groups revised, {n} verse_context rows revised, {n} groups dissolved"
  },
  "operations": [
    { "op_id": "OP-001", "operation": "update", "table": "verse_context_group", "match": { "id": 47 }, "set": { "context_description": "…", "notes": "revised 2026-04-24 under v3_3 re-evaluation" } },
    { "op_id": "OP-002", "operation": "update", "table": "verse_context_group", "match": { "id": 48 }, "set": { "delete_flagged": 1, "notes": "dissolved — all verses reassigned in re-evaluation" } },
    { "op_id": "OP-003", "operation": "update", "table": "verse_context",       "match": { "id": 892 }, "set": { "is_anchor": 1, "notes": "promoted" } }
  ],
  "_patch_summary": {
    "total_operations": 0,
    "group_updates": 0,
    "group_dissolves": 0,
    "verse_context_updates": 0,
    "anchor_promotions": 0,
    "anchor_demotions": 0
  }
}
```

### 5.3 VCSBFLAGS

**Filename:** `wa-vcb-{batch_id}-patch-vcsbflags-v{n}-{date}.json`
**When produced:** when the classifier raises any Session B observation during verse reading — analytical signals that need attention at Session B.
**When absent:** when no SB-worthy observation was raised.

Each row is a `wa_session_research_flags` insert:

```json
{
  "op_id": "OP-001",
  "operation": "insert",
  "table": "wa_session_research_flags",
  "record": {
    "registry_id": 62,
    "file_id": {resolved — CC fills from registry_id},
    "flag_code": "SB_FINDING",
    "flag_label": "one-line summary — terminal clause",
    "strongs_reference": "G2842",
    "cross_registry_id": null,
    "priority": "normal",
    "session_target": "Session B",
    "description": "Full observation text — what was noticed while reading verse(s) {ref}, why it matters for Session B analysis. Self-contained; survives session boundary.",
    "session_raised": "VCB-045",
    "raised_date": "2026-04-24T{time}Z",
    "resolved": 0
  }
}
```

**Appropriate `flag_code` values** (existing vocabulary — no new codes needed):

- `SB_FINDING` — generic analytical finding for Session B
- `SB_INNER_BEING` — the verse-reading surfaced an inner-being connection worth flagging
- `PH2_CROSS_REF_ENRICHMENT` — a cross-reference that would enrich Session B analysis
- `PH2_THEOLOGICAL_DEPTH_REQUIRED` — needs deeper theological engagement at Session B
- `PH2_EXEGETICAL_STUDY_REQUIRED` — needs structured exegesis
- `PH2_BOUNDARY_QUESTION` — boundary between this term and a neighbouring concept needs clarification

### 5.4 VCSDPOINTERS

**Filename:** `wa-vcb-{batch_id}-patch-vcsdpointers-v{n}-{date}.json`
**When produced:** when the classifier raises any cross-term or cross-registry observation during reading — signals that verse X on term Y in registry R points to something in term Y' / registry R' worth investigating in Session D.
**When absent:** when no cross-registry signal was raised.

Each row is a `wa_session_research_flags` insert:

```json
{
  "op_id": "OP-001",
  "operation": "insert",
  "table": "wa_session_research_flags",
  "record": {
    "registry_id": 62,
    "file_id": {resolved},
    "flag_code": "SD_POINTER",
    "flag_label": "one-line summary — terminal clause",
    "strongs_reference": "G2842",
    "cross_registry_id": 103,
    "priority": "normal",
    "session_target": "Session D",
    "description": "Observation at {ref} (vr_id={n}): the use of {strongs} in this verse parallels / contrasts with {other_term} in registry {cross_registry_id} ({other_word}). For Session D: {concrete question or angle}.",
    "session_raised": "VCB-045",
    "raised_date": "2026-04-24T{time}Z",
    "resolved": 0
  }
}
```

**Appropriate `flag_code` values:**

- `SD_POINTER` — standard cross-registry pointer
- `SD_CLUSTER` — implicates a whole cluster, not just one registry
- `PH2_CROSS_REGISTRY_REQUIRED` — analysis requires cross-registry work at Session B (precursor to Session D)
- `THEMATIC_LINK` — thematic connection worth carrying forward

## 6. Applicator extension

**Existing handler (v3_2 era):** `_apply_versecontext_term_updates` runs on patches where `patch_type == "VERSECONTEXT"`.

**v3_3 change:** the handler runs when `patch_type IN ('VERSECONTEXT', 'VCNEW', 'VCREVISE')`. VCSBFLAGS and VCSDPOINTERS carry only flag inserts — no per-term `vc_status` update; no registry aggregation. (The registry-aggregation check still runs after VCNEW/VCREVISE, reading the latest `mti_terms.vc_status` state.)

`sb_exempt_types` tuple — add the four new types.

## 7. Execution order (commits)

1. CATALOGUE_POPULATION patch — seed the 4 new types in `wa_patch_type_registry`. One commit.
2. Patch instruction v2_4 → v2_5 — add the 4 types to §3.3 / §3.4 / §3.6. v2_4 archived. One commit.
3. Applicator extension — `sb_exempt_types` + `_apply_versecontext_term_updates` gate widened. One commit.
4. VC instruction v3_2 → v3_3 — full 4-patch detail in §7; §6 / §13 updates; A-01 resolved. v3_2 archived. One commit.
5. `prog_instr_verse_context` v2 → v3 PROSE supersede — governance narrative updated with the four-type output. One commit.

Each commit self-contained and reviewable.

## 8. Researcher approval needed before I proceed

One question:

**Four new patch-type names — VCNEW, VCREVISE, VCSBFLAGS, VCSDPOINTERS — acceptable?** (They're short, discriminated, and fit the existing naming pattern of uppercase-no-separator. Alternative forms: VC-NEW / VC-REVISE / VC-SB-FLAGS / VC-SD-POINTERS with hyphens — also valid per existing precedent like DIMREVIEW-GRPDESC.)

On yes: I proceed through the five execution commits in order. On redirect: I adjust to whatever naming you prefer.

---

*Design brief produced 2026-04-24 from the researcher's four-patch direction. Ties to the output-model proposal in `vc-session-output-model-v1-20260424.md` and resolves A-01 (DB state as the gate, reported in `vc-v3_1-ambiguities-needing-researcher-decision-v1-20260424.md`).*
