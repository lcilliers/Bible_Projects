# WA Global — Pass-Close Procedure

**Filename:** wa-global-pass-close-procedure-v1.1-20260414.md
**Date:** 20260414 | **Version:** 1.1
**Previous output ref:** wa-global-general-rules-v2-20260414.json
**Status:** Draft procedure for incorporation into the Session B instruction at its next revision.

## Change note
v1.1 (20260414): Filename and header dates updated to compact format per GR-FILE-009. Previous output ref updated to global rules v2. No substantive content changes.

---

## 1. Purpose

The pass-close procedure is the sequence of steps that an AI analyst must execute at the end of every Pass (Session B Pass 1 through Pass 6, Stage 1 audit, Dimension Review, and equivalent pass-level units in Session C and Session D). It ensures that:

1. All analytical content produced during the pass is made available for download before the next pass begins (GR-PASS-001).
2. All (b) observations produced during the pass are written to the database via a patch or directive, so the database is the authoritative store by the end of the pass (GR-PASS-002).
3. A fresh extract is pulled after the database write so subsequent pass work reads from the updated authoritative state.
4. All session actions generated during the pass are explicitly classified and either resolved within the pass, carried forward as session-level actions, or flagged for researcher decision.
5. Nothing is silently carried forward.

This procedure enforces the write-on-discovery discipline at pass boundaries. Within a pass, observations are written to the markdown observations log continuously on discovery (GR-OBS-001). At pass close, the analytical content flows from the markdown log into the database in structured form.

---

## 2. Prerequisites

Before a pass can close, the following must be true:

1. All analytical work defined as the pass's scope has been completed. A pass cannot close with scope incomplete unless the incomplete scope is escalated as a session action with a deferral reason.
2. The observations log is current (everything discovered during the pass is in the markdown log).
3. Any external inputs the pass depended on (researcher decisions, data from other processes) have been received and recorded.

---

## 3. The pass-close sequence

The procedure runs in strict order. Each step must complete before the next begins.

### Step 1 — Pass review

Read the pass's entries in the observations log in full. For each entry, classify it into exactly one of the four categories per GR-OBS-002:

- **(a) Drop** — the entry is a superlative, impression-making statement, or claim without analytical value. It has no database home. Note it in the pass-close record but do not carry it forward.
- **(b) Entity-linked observation** — the entry is an analytical comment keyed to one or more entities (verse, term, registry, group, dimension, xref, root). Queue it for database write in Step 3.
- **(c) Forward pointer** — the entry is a Session B pointer (to be resolved within Session B) or a Session D pointer (for cross-registry synthesis). Queue it for the appropriate pointer table write in Step 3.
- **Session action** — the entry is a data-quality finding, methodology note, sequencing decision, self-correction, verification record, or other non-analytical item. Handle per Step 4.

Each entry's classification is recorded in the pass-close record. An entry that does not cleanly fit one of these four categories is flagged for researcher review.

### Step 2 — Cross-pass consistency check

Before writing to the database, verify that the pass's new observations do not conflict with existing observations already in the database for this registry. Specifically:

- For each new (b) observation, retrieve any existing observations keyed to the same entity.
- Check for factual contradiction (two observations making incompatible claims about the same entity).
- If a contradiction is found, the new observation must either (i) supersede the existing one via the obsolete + superseded_by mechanism, or (ii) be withdrawn if the existing one is correct.
- If the contradiction cannot be resolved at the pass level (e.g., it requires researcher judgement or cross-registry comparison), it is escalated as a session action and the new observation is held in a staging state.

The purpose of this step is to prevent the database from accumulating contradictory observations silently. Per GR-OBS-005, obsolescence is always marked, never silent.

### Step 3 — Database write via patch

Produce a patch or CC directive that:

1. Writes each queued (b) observation to `observation_description` with its entity index rows.
2. Updates any obsoleted observations (from Step 2) with `delete = 1`, `obsolete_reason`, `obsolete_date`, and `superseded_by_id`.
3. Writes each queued (c) pointer to its appropriate table (`wa_session_b_findings`, `session_d.sd_pointer_flags`, or equivalent).
4. Updates any pointers that were resolved by the pass's work — the pointer record gets `resolved = 1` and the resolving (b) observation references it via `related_obser_id`.
5. Updates the registry's session progress fields (`session_b_status`, pass-level markers, or equivalent).

The patch follows the patch specification format established for the programme (plain-language directives for Claude Code, per GR-DIR-001).

The patch is delivered and confirmed as applied before moving to Step 4.

### Step 4 — Session action classification

For each session action identified in Step 1, decide:

- **Resolve within this pass.** The action can be completed before the pass closes. Complete it now. Examples: produce a required field-level patch and apply; run a verification spot-check; record a methodology note in the appropriate instruction document.
- **Carry forward to a later pass in the same session.** The action depends on later pass work. Add it to a session-action carry-forward list that will be revisited in subsequent pass-close procedures in the same session.
- **Escalate to session-level resolution.** The action cannot be resolved within any single pass but must be resolved before the session closes. Add it to the session-level action register that the final session log will summarise.
- **Flag for researcher decision.** The action requires researcher judgement. Add it to the pending researcher decisions list. The pass can close with the action deferred, provided the decision is carried into the session log.

No session action may be silently dropped. Per GR-OBS-003, all session actions must be resolved before the session closes or clearly summarised in the final session log.

### Step 5 — Fresh extract pull

Request a fresh JSON extract of the registry from the database. The extract must include all observations and pointers written in Step 3. Verify the extract contains:

1. The new (b) observations with correct `study_segment` values and entity index rows.
2. The obsoleted observations with `delete = 1` and populated metadata.
3. The new/updated (c) pointers.
4. The updated registry session progress fields.

If any of the above is missing from the extract, Step 3 did not complete correctly. The pass cannot close until Step 3 is re-run and the extract is verified.

The fresh extract becomes the working source for the next pass. The previous extract is retained (per GR-FILE-004 — no overwrites) but is no longer the working source.

### Step 6 — Output preparation

Prepare all pass outputs for download:

1. The observations log (markdown) — updated with an explicit end-of-pass marker recording that the pass has closed, the patch has been applied, and the fresh extract has been pulled.
2. The pass-close patch or CC directive (whichever format was used in Step 3).
3. The fresh extract.
4. Any pass-specific working files (analytical briefs in draft, session C rendering drafts, session D synthesis drafts).

All files follow the filename rules in GR-FILE-001 through GR-FILE-006.

### Step 7 — Download and confirmation

All prepared outputs are made available for download at pass close. The researcher is notified that the pass has closed and the files are ready. No further pass work begins until confirmation.

The pass-close record (which is itself a small markdown document) is produced listing:

- Pass identity (which pass closed)
- Date and time
- Count of observations classified (a / b / c / session action)
- Count written to database
- Count of pointers resolved
- Count of session actions resolved / carried forward / flagged
- Fresh extract filename
- Outputs available for download

### Step 8 — Next pass readiness

The next pass does not begin until:

1. All files from Step 7 are confirmed downloaded.
2. The researcher has acknowledged the pass close (or the configured protocol permits auto-advance).
3. Any pending researcher decisions from Step 4 that are blocking the next pass have been received.

---

## 4. Session-level equivalent

At session close, a session-level close procedure runs that is structurally similar but operates across all passes of the session:

1. Review the session-level action register (accumulated from Step 4 of each pass-close).
2. Resolve or explicitly summarise each session-level action in the final session log.
3. Verify that no (b) observation from any pass was left in a staging state.
4. Verify that all (c) pointers raised in the session are written to the appropriate tables.
5. Produce the final session log (per GR-PASS-001 and the existing session log discipline).
6. Make all session outputs available for download.

The session-level close procedure is specified separately; this document covers the pass-level procedure only.

---

## 5. Failure modes and recovery

These are the ways the pass-close procedure can fail and how to recover:

**Failure A: Step 3 patch does not apply cleanly.**
The pass cannot close. Investigate the patch failure, produce a corrected patch, re-apply, and re-run from Step 5.

**Failure B: Fresh extract in Step 5 does not contain the expected new records.**
Indicates a patch application or database write failure. Do not close the pass. Investigate and re-apply.

**Failure C: Cross-pass contradiction found in Step 2 that cannot be resolved at the pass level.**
Escalate as a session action (Step 4, "escalate to session-level resolution"). The new observation is held in staging until the contradiction is resolved. The pass closes with the staging flagged in the pass-close record.

**Failure D: A researcher decision is required before the pass can close.**
If the decision is not blocking (the pass work is complete but awaits confirmation of an interpretation), the pass closes with the decision flagged. If the decision is blocking (the pass work cannot be classified without it), the pass cannot close — pause the pass and request the decision.

**Failure E: Context budget exhausted before the pass closes.**
Save the observations log and any partial outputs, produce a partial pass-close record stating exactly what was and was not completed, and defer the pass close to a new session with the partial record as the starting point.

---

## 6. Relationship to other procedures

- **GR-OBS-001 (write-on-discovery):** The pass-close procedure assumes write-on-discovery has been followed throughout the pass. If the observations log is missing content that was discovered during the pass, Step 1 will be incomplete and the pass cannot close cleanly.
- **GR-OBS-003 (session action resolution):** Step 4 of this procedure enforces GR-OBS-003 at the pass level.
- **Patch specification format:** Step 3's patch must follow the format established in the patch specification document (currently v1.10 per project files). Patches to `observation_description` and the entity index tables will require the schema to be implemented first.

---

## 7. Pre-schema-implementation interim mode

Until the observations schema (per Artefact 2) is implemented, the pass-close procedure operates in an interim mode:

- Steps 1 and 2 proceed as specified, operating on markdown content.
- Step 3 writes to the currently available tables (`wa_session_b_findings`, `session_d.sd_pointer_flags`, `word_registry`, etc.) and produces a **forward-staged patch specification** for the observations not yet writeable — analogous to Artefact 3 from the compassion session.
- Steps 4–7 proceed as specified.

When the schema is implemented, the forward-staged patches are applied and the interim mode ends.

---

## 8. Open items for incorporation into the Session B instruction

The next revision of the Session B instruction (v4.8 or v5.0) should incorporate:

1. A reference to this procedure, with the procedure itself either embedded or loaded as a project asset.
2. An update to the Stage 2 Pass structure to include an explicit "Pass N close" step after each pass.
3. A reference to GR-OBS-002 for the three-category classification.
4. A reference to GR-OBS-003 for session action discipline.
5. A reference to GR-PASS-001 and GR-PASS-002 in the instruction's rules section, with the inline rules removed (per SA-18 consolidation).

---

*Produced under GR-PASS-001, GR-PASS-002, GR-OBS-002, GR-OBS-003. For incorporation into the Session B instruction at its next revision.*
