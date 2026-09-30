# VC Session Output Model — Four-Type Taxonomy (proposal)

**Date:** 2026-04-24
**Context:** Researcher framing (conversation 2026-04-24) — the VC session produces four distinct output types. The current instruction (v3_2 §7) documents types (a) and (b) via the VERSECONTEXT patch and handles (c) as a companion `.md` file (§6.6); (d) is implicit and currently captured at Session B time rather than at VC time. This proposal formalises all four into a single unified VC output model and resolves A-01 (DataPrep gate) as a consequence.

---

## 1. The researcher's taxonomy

| # | Output type | What it records |
|---|---|---|
| (a) | Changes to existing VC data | Revisions to prior classifications: group edits, group dissolves, verse reassignments, anchor promotions/demotions |
| (b) | New VC data | Fresh classifications for terms being seen for the first time: new groups, new verse_context rows (anchor / related / set-aside) |
| (c) | Session B observations | Analytical flags the classifier notices while reading verses — things that will need special attention during Session B analysis |
| (d) | Cross-term / cross-registry (Session D) observations | Signals the classifier notices that a verse's inner-being content relates to another term or another registry — material for Session D synthesis |

This is a clean taxonomy. Every meaningful thing a classifier produces while reading verses falls into one of the four.

---

## 2. Current state — how each type is handled today

| Type | Mechanism | Where it lands | Status |
|---|---|---|---|
| (a) | VERSECONTEXT patch, `update` operations on `verse_context_group` and `verse_context` (including `delete_flagged = 1` for dissolve) | DB tables `verse_context_group` + `verse_context` | **Covered.** v3_2 §7.3 documents the ops. |
| (b) | VERSECONTEXT patch, `insert` operations on `verse_context_group` and `verse_context` | DB tables `verse_context_group` + `verse_context` | **Covered.** v3_2 §7.3 documents the ops. |
| (c) | File: `wa-vcb-{batch_id}-sessionb-flags-v{n}-{date}.md` produced by Claude AI at end of session (§6.6) | File on disk in `data/imports/WA/Session_B_Verse_Context/` or similar | **Partly covered — file only.** Not currently written to the DB at VC time. Session B reads the `.md`. |
| (d) | DB: `wa_session_research_flags` with `flag_code = 'SD_POINTER'` and `session_target = 'Session D'`. Currently inserted via **SESSIONB** patches — not during VC. | DB table `wa_session_research_flags` | **Partly covered — wrong stage.** The observation is made during VC but not captured then. It's regenerated at Session B time, which risks loss of the VC classifier's context. |

### The gap

For (c): file-only means the DB does not hold the observation. Under the database-as-memory principle, this is a gap — Session B must load a file rather than query the DB.

For (d): cross-registry signals spotted during VC classification are not captured until Session B. This delays the observation's persistence by a whole stage, and relies on Session B analysis to re-surface what was seen earlier.

---

## 3. Proposed unification — one VERSECONTEXT patch carries all four

The applicator already supports `wa_session_research_flags` insert operations. No schema or applicator change needed — **this is a documentation/discipline change**: the VC instruction formalises that the VERSECONTEXT patch may carry SB and SD flag inserts alongside its verse_context operations. All four output types land in one patch, applied in one transaction.

### Proposed extended VERSECONTEXT operations

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-{YYYYMMDD}-VCB{nnn}-VERSECONTEXT-V1",
    "batch_id": "VCB-{nnn}",
    "terms_covered": [142, 143, 187],
    "governing_instruction": "wa-versecontext-instruction-v3_3-20260424.md",
    "session_b_status": null,
    "description": "…"
  },
  "operations": [
    /* Type (a) revisions to existing VC */
    { "op_id": "OP-001", "operation": "update", "table": "verse_context_group", "match": {"id": 47}, "set": {...} },
    { "op_id": "OP-002", "operation": "update", "table": "verse_context", "match": {"id": 892}, "set": {...} },

    /* Type (b) new VC */
    { "op_id": "OP-003", "operation": "insert", "table": "verse_context_group", "record": {...} },
    { "op_id": "OP-004", "operation": "insert", "table": "verse_context", "record": {...} },

    /* Type (c) Session B observation */
    {
      "op_id": "OP-005",
      "operation": "insert",
      "table": "wa_session_research_flags",
      "record": {
        "registry_id": 62,
        "file_id": {resolved},
        "flag_code": "SB_FINDING",
        "flag_label": "short one-line summary",
        "strongs_reference": "G2842",
        "priority": "normal",
        "session_target": "Session B",
        "description": "Full observation from verse-reading — what was noticed, what verse(s), why it matters for Session B analysis.",
        "session_raised": "VCB-045",
        "raised_date": "2026-04-24T…",
        "resolved": 0
      }
    },

    /* Type (d) Session D cross-registry pointer */
    {
      "op_id": "OP-006",
      "operation": "insert",
      "table": "wa_session_research_flags",
      "record": {
        "registry_id": 62,
        "file_id": {resolved},
        "flag_code": "SD_POINTER",
        "flag_label": "short one-line summary",
        "strongs_reference": "G2842",
        "cross_registry_id": 103,
        "priority": "normal",
        "session_target": "Session D",
        "description": "Observation: at Col 1:9 (vr_id=…), the term's use points at a structural parallel with love (reg 103)'s term G25. Worth examining in Session D cross-registry synthesis.",
        "session_raised": "VCB-045",
        "raised_date": "2026-04-24T…",
        "resolved": 0
      }
    }
  ]
}
```

### What the instruction v3_3 would add

A new **§7.9 Session output taxonomy** (or equivalent), stating:

> A VC session's VERSECONTEXT patch carries up to four types of output, all landed in a single transaction:
>
> **(a) Changes to existing VC data.** `update` operations on `verse_context_group` (group description revision, dissolve via `delete_flagged = 1`) and `verse_context` (reclassification, group reassignment, anchor promotion/demotion).
>
> **(b) New VC data.** `insert` operations on `verse_context_group` (new groups for terms or new groups on existing terms) and `verse_context` (new anchor / related / set-aside rows).
>
> **(c) Session B observations raised during verse reading.** `insert` operations on `wa_session_research_flags` with `session_target = 'Session B'`. Appropriate `flag_code`s include `SB_FINDING`, `SB_INNER_BEING`, and — where the pattern fits — the `PH2_*` family (`PH2_CROSS_REF_ENRICHMENT`, `PH2_THEOLOGICAL_DEPTH_REQUIRED`, `PH2_EXEGETICAL_STUDY_REQUIRED`, `PH2_BOUNDARY_QUESTION`). The flag's `description` field carries the observation; `strongs_reference` names the term; `session_raised = 'VCB-{nnn}'` names the session; `resolved = 0` at raise time.
>
> **(d) Cross-term / cross-registry observations for Session D.** `insert` operations on `wa_session_research_flags` with `session_target = 'Session D'` and `flag_code = 'SD_POINTER'` (or `SD_CLUSTER` where a whole cluster is implicated). `cross_registry_id` names the other registry referenced; `description` names the concrete cross-reference (verse, term, nature of the connection).
>
> A patch may carry zero operations of any type. A session with only (a)+(b) is a pure classification session; a session that also raises (c) or (d) captures the analytical observations at the moment of reading, not at the downstream stage they feed.
>
> **The `sessionb-flags.md` file** (§6.6) becomes a companion **readable summary** of the (c) flags inserted in this session's patch, not the authoritative record. The DB row set is the authoritative record; the file is a view. Claude Code produces the `.md` from the `wa_session_research_flags` rows after the patch applies, or the classifier produces it as a reading summary — either way, the rows are the primary artefact.

And a companion update to §6.2 Step 6 (the per-term classification summary) — when the classifier notices an SB or SD-worthy observation during Step 1 (read) or Step 2 (filter), it records the flag to be included in the session's patch. No new mechanism — just explicit permission for SB/SD flags to ride in the VERSECONTEXT patch.

---

## 4. Consequences for A-01 (DataPrep gate)

With (c) and (d) written to the DB at VC time, the DB now carries **everything** the downstream stages need:

- Session B reads `wa_session_research_flags WHERE session_target = 'Session B' AND registry_id = N AND resolved = 0` for its pre-analysis observation set.
- Session D reads `wa_session_research_flags WHERE session_target = 'Session D' AND (registry_id = N OR cross_registry_id = N)` for its pointer set.
- Dimension Review reads `verse_context_group` + `verse_context` for its dimensional assignment.
- DataPrep reads `word_registry.verse_context_status = 'Complete'` as the trigger.

Nothing downstream needs to read a `.md` or a JSON file to function correctly. The DB state IS the state.

**Therefore A-01 resolves to option (a): DataPrep gate = DB state.** The full-word JSON re-export becomes an optional audit artefact, not a required step in the apply cycle. §13.3 is rewritten to state this unambiguously.

This is a cleaner resolution than if we only considered A-01 in isolation — the taxonomy forces the question of whether the DB has everything. Under the four-type model, it does.

---

## 5. Relationship to A-02 (`'approved'` semantics)

If SB and SD observations are captured at VC time as `resolved = 0` flags, the lifecycle of those flags (raise → triage → resolve) is distinct from `mti_terms.vc_status`. So A-02 stays about the term's VC state, not about the flags:

- `vc_status = 'complete'` — VC classification written; all four output types captured (where applicable)
- `vc_status = 'approved'` — something later confirms the classification stands (researcher, Dimension Review, or Session B)

A-02 remains a separate question. My earlier recommendation (DimReview writes `'approved'` on cluster stamp) is unchanged.

---

## 6. Implementation scope

**Instruction (v3_3) — edits needed:**

1. New §7.9 (or equivalent) documenting the four-type output taxonomy with the extended VERSECONTEXT patch example.
2. §6.2 Step 6 — add a note that SB/SD flags noticed during reading are recorded for inclusion in the session's patch.
3. §6.6 — reframe Session B flags: DB rows are authoritative; the `.md` is a companion readable summary.
4. §13.3 — resolve A-01 (DB state is the gate; JSON re-export optional).
5. §7.7 pre-submission validation — add a bullet: if the session's reading produced SB/SD-worthy observations, they are included as operations in this patch; verify no observations are left in the obslog without corresponding operations.

**Applicator:** no changes — `wa_session_research_flags` insert already supported. VERSECONTEXT patches carrying these ops will apply cleanly today.

**Session A `.md` renderer:** no changes.

**`prog_instr_verse_context` prose:** the description field still carries batch-era language; a prose-type description update should land alongside v3_3 (this is the E-02 item from the prior review).

**Session B / Session D / Dimension Review instructions:** each should be updated to note that their input now includes reading `wa_session_research_flags` from the DB, not just the `.md` files. Small edits — future work, can be scheduled separately.

---

## 7. Researcher decisions needed

1. **Accept the four-type taxonomy as the formalised VC output model?** (My recommendation: yes — it matches your framing and the applicator already supports it.)
2. **Accept the resolution of A-01 as DB-state-is-the-gate?** (Follows directly from (1).)
3. **Existing `flag_code` vocabulary sufficient?** Review the current codes in `wa_session_research_flags` — SB_FINDING, SB_DIMENSION, SB_INNER_BEING, SD_POINTER, SD_CLUSTER, PH2_* family — or propose additions. Current inventory: 15 distinct codes in use today.
4. **Proceed with instruction v3_3** applying the documentation changes above? Applicator and schema need no change.

On yes-to-all, v3_3 is a straightforward documentation update (not a structural rewrite). I can produce it as a supersede of v3_2.

---

*Proposal produced 2026-04-24 in response to the researcher's four-type framing of VC session output. Ties the output model to A-01 resolution and the database-as-memory principle. Approvals recorded at §7.*
