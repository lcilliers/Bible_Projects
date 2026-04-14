# WA-023 Compassion — Session Actions

**Filename:** wa-023-compassion-session-actions-v1-2026-04-13.md
**Date:** 2026-04-13
**Version:** 1.0
**Previous output ref:** wa-023-compassion-audit-patch-v1-2026-04-13.md; wa-global-general-rules-v1-2026-04-13.json; wa-global-obs-schema-v1-2026-04-13.md
**Status:** Session action list. Each item is marked with its resolution status at session close.

## Change note
Version 1.0. Initial list of session actions arising from the compassion word study audit session (2026-04-13). Produced under GR-OBS-003: session actions must be resolved before the session closes or clearly summarised in the final session log.

---

## 1. Purpose

This document lists session actions — items that do not belong in the analytical database (category (b) observations) or in the forward-pointer tables (category (c) pointers), but which require explicit attention before this session can close cleanly. Each action has a type (resolve / summarise / defer), an owner, and a resolution status.

The discipline from GR-OBS-003 is: **a session cannot close silently leaving work in an unresolved state.** Items marked "deferred" must be carried forward in the session log with sufficient handles for the next session to pick them up without loss of context.

---

## 2. Action register

| # | Type | Description | Status at session close |
|---|---|---|---|
| SA-01 | Resolve | Produce the general rules file (Artefact 1) | **Resolved** — file produced: `wa-global-general-rules-v1-2026-04-13.json` |
| SA-02 | Resolve | Produce the observations schema proposal (Artefact 2) | **Resolved** — file produced: `wa-global-obs-schema-v1-2026-04-13.md` |
| SA-03 | Resolve | Produce the compassion audit patch specification (Artefact 3) | **Resolved** — file produced: `wa-023-compassion-audit-patch-v1-2026-04-13.md` |
| SA-04 | Resolve | Produce the pass-close procedure draft (Artefact 5) | **Resolved** — file produced: `wa-global-pass-close-procedure-v1-2026-04-13.md` (on completion) |
| SA-05 | Resolve | Produce the Session C derive-from-observations rule draft (Artefact 6) | **Resolved** — file produced: `wa-global-sessionC-prose-rule-v1-2026-04-13.md` (on completion) |
| SA-06 | Defer | Rewrite the compassion brief v1 → v2 with corrections applied in place | **Deferred to next session.** Scoping decision by researcher (2026-04-13): no document rewrites in this session. Handle for next session: the patch specification in SA-03 is the authoritative list of corrections to apply. |
| SA-07 | Defer | Rewrite the compassion word study v3 → v4 with corrections applied in place | **Deferred to next session.** Same scoping decision. Same handle: SA-03. |
| SA-08 | Defer | Correct the observations log Pass 2 line 754 transcription error (the "~14/24" count that was misread as a prohibition count in the brief) | **Deferred to next session.** The correction is small but should land in an obsoleting observation under the new schema rather than a markdown edit. Handle for next session: Item 1 in the patch spec (SA-03). |
| SA-09 | Resolve | Reopen SD-019 in `session_d.sd_pointer_flags` (logically — the change is staged in the patch spec) | **Logically resolved** — staged in the patch spec (Item 15). Physical database update deferred until the patch spec can be applied. |
| SA-10 | Summarise | The `meaning_numbered` Pass 5 gap finding is a false positive per GR-DATA-004 | **Summarised here and in the patch spec (Item 17).** Retirement of the finding is staged via OBSOLETE-only operation. |
| SA-11 | Summarise | Rule to drop the four deprecated meaning fields from audit scope (meaning, meaning_numbered, also_spelled, lsj_entry) | **Summarised** — now captured as GR-DATA-004 in the general rules file. Future sessions should not flag these as gaps. |
| SA-12 | Summarise | The filename-structure addition (reference between prefix and short description) and the no-overwrite rule | **Summarised** — now captured as GR-FILE-001 and GR-FILE-004 in the general rules file. |
| SA-13 | Summarise | The term ownership rule (OWNER carries root/meaning/verses/classifications; XREF is a distribution marker only) | **Summarised** — now captured as GR-DATA-002 in the general rules file. This also clarifies the Stage 1 "SPLANCHN/OIKTEIRŌ/NICHUM/CHIN root family gap" investigation — they were artefacts of the XREF mechanism, not real gaps, per GR-DATA-003. |
| SA-14 | Summarise | Pass-close discipline (write-on-discovery to database, fresh extract after each pass, all outputs downloaded at pass close) | **Captured** as GR-PASS-001 and GR-PASS-002 in the general rules file; full procedure drafted in Artefact 5. |
| SA-15 | Summarise | Session C prose rule (derive from observations, gaps trigger patches, section-level linking via `study_segment`, caveat for writer-surfaced insights) | **Captured** as GR-OBS-006 in the general rules file; full rule drafted in Artefact 6. |
| SA-16 | Defer | Cluster-wide audit of other C17 briefs (mercy 111, grace 68, kindness 99) for the same class of correlation-mechanism and shared-anchor errors found in compassion | **Deferred.** The compassion audit revealed a *pattern* — Section 7 of the analytical brief was compiled from inference rather than direct JSON read, producing systematic misattributions of which verses and vocabulary are shared with which registries. This pattern is likely to exist in the other C17 briefs. A programme-wide audit of all completed Session B briefs against the correlation JSON should be scheduled. Handle for next session: apply the same verification procedure used in this session (JSON-direct check of xref_sharing, verse_cooccurrence, shared_anchor_verses, root_families) to each completed brief. |
| SA-17 | Defer | Implementation of the observations schema (DDL, write procedures, migration plan) | **Deferred.** Schema proposal is Artefact 2; implementation is the next design cycle. Handle: the schema proposal, plus the 16-item patch spec as migration test input. |
| SA-18 | Defer | Consolidation of rules currently duplicated between instructions and the new general rules file | **Deferred.** The existing instruction documents (Session A, Session B, Session C, Session D, Dimension Review, Verse Context, Patch Specification, Registry Management) currently carry many rules inline that should now be centralised in `wa-global-general-rules-v1-2026-04-13.json`. Consolidation pass is a programme-level cleanup that should happen after the schema is implemented. Handle for next session: grep each instruction for rules now in the general rules file and remove the duplicates. |
| SA-19 | Summarise | Session B instruction will need updating to reference the general rules file, add the pass-close procedure, and add the three-category classification model | **Summarised** — to be addressed when the Session B instruction reaches its next revision (v4.8 or v5.0). The draft of the pass-close procedure (Artefact 5) is ready to be incorporated. |
| SA-20 | Summarise | Session C instruction will need updating to reference the general rules file and add the derive-from-observations rule | **Summarised** — to be addressed when Session C instruction reaches its next revision. The draft rule (Artefact 6) is ready to be incorporated. |

---

## 3. Pending researcher decisions

Items that require a researcher decision before they can be resolved, per the established discipline:

| # | Decision needed | Where it lives |
|---|---|---|
| PRD-01 | Which shape do you want implemented for `observation_description`? The minimum (4 fields: id, obser_desc, delete, study_segment) or the recommended (4 + 7 audit fields)? | Artefact 2 Section 9 Q1 |
| PRD-02 | Promote xref and root to first-class entities (with stable ids) as part of the schema implementation, or use composite keys? | Artefact 2 Section 9 Q2 |
| PRD-03 | Add a `pass_batch` table to group observations written in each pass, or rely on per-observation origin metadata only? | Artefact 2 Section 9 Q3 |
| PRD-04 | Is the proposed `study_segment` initial controlled vocabulary acceptable, or should it be revised? | Artefact 2 Section 9 Q4 |
| PRD-05 | Rendering-verification procedure under GR-OBS-006: manual, automated, or both? | Artefact 2 Section 9 Q5 |
| PRD-06 | The four literary framings in Items 12, 13, 14, 16 of the patch spec (Lam 3:22 "defiant confession"; Gen 19:16 "mercy in the face of inadequacy"; Jon 4:11 "creatureliness"; chesed/shame "eschatological horizon"): the patch spec retires them pending review. Do you want them retained as author interpretations with explicit source tags, or dropped entirely? | Artefact 3 Items 12–16 |
| PRD-07 | Cluster-wide audit of other C17 briefs (SA-16): should this be the next session's priority, or should the schema implementation come first? | Artefact 4 SA-16 |

---

## 4. Discipline test at session close

Per GR-OBS-003, a session cannot close silently leaving work in an unresolved state. Walking the register:

- **Resolved items (SA-01 through SA-05, SA-09):** All produced or logically resolved. No action required at session close beyond confirming files are downloadable.
- **Deferred items (SA-06 through SA-08, SA-16 through SA-18):** All carry explicit handles for the next session. The handles are: (i) the patch specification (Artefact 3) as the authoritative correction list; (ii) the schema proposal (Artefact 2) as the implementation starting point; (iii) the session log (Artefact 9) as the narrative of decisions made in this session.
- **Summarised items (SA-10 through SA-15, SA-19, SA-20):** All captured in the general rules file (Artefact 1) or in the methodology drafts (Artefacts 5, 6). Future sessions will consume these rules automatically once the file is loaded as a project asset.
- **Pending researcher decisions (PRD-01 through PRD-07):** Each is explicitly listed. None blocks the session from closing cleanly; each is an input to the next session's scoping.

**The session closes cleanly provided:**
1. All artefacts in the produced list are made available for download at session close (per GR-PASS-001).
2. The session log (Artefact 9) carries forward the deferred items with their handles.
3. The researcher has an opportunity to answer PRD-01 through PRD-07 before the next session begins, or can defer them to the start of the next session.

---

*Produced under GR-OBS-003. Each item in the register has a status at session close; nothing is carried forward silently.*
