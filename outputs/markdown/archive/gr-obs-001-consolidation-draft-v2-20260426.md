# GR-OBS-001 Consolidation Draft — v2

_Drafted: 2026-04-26 · Author: Claude Code · Status: **DRAFT — awaiting researcher approval**_
_Supersedes: `gr-obs-001-consolidation-draft-v1-20260426.md` (archived)_

## Changes vs v1 draft

1. **Subject line shortened.**
2. **Version-increment rule rewritten** — bumps now happen *within* a session at batch boundaries (size control), not per-session. This reverses the prior GR-OBS-004 v2_1 semantic.
3. **New filename clause added** — pinning the obslog filename pattern to `wa-obslog-[reference]-[session-name-abbreviated]-[version]-[date]`, with `reference` declared at startup (default `ref-a`).

## Source rules absorbed

| rule_id | category | version | substance folded in |
|---|---|---|---|
| GR-OBS-001 v2_1 | session_startup | 2_1 | base — kept |
| GR-OBS-003 v2_1 | observation_discipline | 2_1 | obslog vs session log |
| GR-OBS-004 v2_1 | observation_discipline | 2_1 | version increment (semantic reversed) |

## Proposed consolidated rule — `GR-OBS-001 v2_2`

### Field changes vs v2_1

| field | v2_1 | v2_2 (proposed) |
|---|---|---|
| `category` | session_startup | session_startup _(unchanged)_ |
| `version` | 2_1 | **2_2** |
| `subject` | Observations log — continuous write, log authoritative, pass-close persistence | **Observations log — write discipline, segmentation, and filename convention** |
| `applies_to` | all sessions, all phases | all sessions, all phases _(unchanged)_ |
| `rule_text` | _see below — current_ | _see below — proposed_ |
| `application_notes` | _see below — current_ | _see below — proposed (small additions for the new clauses)_ |
| `last_modified` | 2026-04-21T08:47:50Z | **2026-04-26T<HH:MM:SS>Z** _(set on apply)_ |

### Proposed `rule_text`

> The observations log — referred to as the obslog — is the authoritative record of every session's working trail. The obslog is initialised as step 2 of the session-startup sequence (GR-LOAD-001); no substantive work may begin until it exists. While the session is live, every finding, decision, gap, patch consequence, and open question is written to the obslog at the moment it is determined. Every substantive chat output also appears in the obslog. When a researcher message is received, the researcher's feedback is recorded verbatim in the obslog before a response is formulated. At every pass close, items requiring database persistence are written via a patch or directive, and a fresh extract confirming the write becomes the working source for the next pass. This discipline persists for the life of the session.
>
> The obslog and the session log are separate files with separate purposes. The obslog is the working paper, written continuously as defined above. The session log is the handoff record, produced at session close and at any named batch boundary within a session. A session that closes without a session log has not closed cleanly — the session log is always produced before the session ends.
>
> The obslog filename is version-incremented within the same session, at the end of a logical session batch, to keep the working file in manageable segments. The version bump is for size control, not for marking a new working scope: each new version continues the same logical obslog trail without loss of continuity. A version bump is not triggered by per-save writes within a batch, only by the close of a logical batch.
>
> The obslog filename follows the pattern `wa-obslog-[reference]-[session-name-abbreviated]-[version]-[date]`, where `reference` is declared at session startup (default `ref-a`), `session-name-abbreviated` is a short token identifying the session topic, `version` follows GR-FILE-003 (`v1`, `v2`, …), and `date` follows GR-FILE-009 (`YYYYMMDD`). This pattern is a carve-out from GR-FILE-001's standard `[prefix]-[reference]-[short description]-[version]-[date]` order: for obslogs, the literal token `obslog` sits between the `wa-` prefix and the reference, so that all observation logs sort together regardless of their reference.
>
> This rule is non-waivable.

### Diff vs v2_1 rule_text

- **Paragraph 1** — unchanged from v2_1, except the trailing "This rule is non-waivable." moves to the end of the rule (so it now scopes the whole consolidated rule).
- **Paragraph 2** (new — from GR-OBS-003 v2_1) — verbatim with one connective edit: "written continuously per GR-OBS-001" → "written continuously as defined above" (the rule no longer cross-references itself).
- **Paragraph 3** (new — replaces GR-OBS-004 v2_1) — **semantic reversed:** previous rule said version bumps mark a new session; new rule says version bumps happen *within* a session at logical batch boundaries for size control. New sessions are addressed in `application_notes` (see below).
- **Paragraph 4** (new — no prior rule) — pins the obslog filename pattern. Flags the carve-out from GR-FILE-001.
- **Final line** repositioned to scope all four clauses.

### Proposed `rationale` _(unchanged from v2_1)_

> Claude AI cannot rely on in-memory accumulation across a session. Sessions crash; context windows truncate; follow-up work depends on what was captured. The obslog exists so that the working trail survives these failure modes. Without continuous capture to disk, findings reach the researcher only through chat output — which is ephemeral and unaudited. Continuous write makes the work externally reviewable at every turn.

### Proposed `application_notes`

_v2_1 notes preserved; new notes added for the two new clauses._

> **Compliance test.** A useful shorthand: if something is not in the observations log, it has not been received or done. This is not literal — the thought existed — but it captures the rule's operational meaning: nothing that is only in chat or in memory counts as work.
>
> **Capture scope.** The list of content types caught by continuous-write includes: findings, decisions, gaps, patch consequences, flags, open questions, clarification requests, and researcher feedback verbatim. New content types arising in a session are logged on the same discipline.
>
> **Verbatim researcher capture.** 'Verbatim' means the researcher's message is reproduced exactly, not paraphrased or summarised. If the message is long, the full text is still captured; summaries appear elsewhere in the log if needed.
>
> **Logical batch boundary for version bumps.** A logical batch is a coherent unit of work declared at startup or at the boundary itself — for example, processing batch 1 of N within a registry, or a clean Q&A round close. The bump is initiated by the researcher or by an explicit pause point, not by file size alone (file size is the *reason* the rule exists, but not the *trigger* — the trigger is the logical close).
>
> **New session vs new batch.** Crossing into a new session resets the obslog to a new file (new `session-name-abbreviated`, version reset to `v1`). Bumps within a single session continue under the same `session-name-abbreviated` and increment `v1 → v2 → v3 …`. The obslog never spans two sessions in the same file.
>
> **Reference defaulting.** If the researcher does not declare a `reference` at startup, the obslog filename uses `ref-a`. The reference identifies the working scope (e.g. a registry, a cluster, a programme-wide pass) and is set once per session.

## Knock-on actions after approval

1. **Edit source JSON** `data/imports/WA/Workflow/Framework_B/Session_B/wa-global-general-rules-v2_11-20260418.json` → produce `wa-global-general-rules-v2_12-20260426.json` (GR-FILE-003 minor bump). In v2_12:
   - Replace `GR-OBS-001` with v2_2 content above.
   - Mark `GR-OBS-003` `obsolete=1`, `obsolete_reason="Substance folded into GR-OBS-001 v2_2 (obslog vs session log clause). Consolidated 2026-04-26."`, `superseded_by="GR-OBS-001 v2_2"`.
   - Mark `GR-OBS-004` `obsolete=1`, `obsolete_reason="Substance folded into GR-OBS-001 v2_2 (version increment clause; semantic reversed from new-session to in-session batch boundary). Consolidated 2026-04-26."`, `superseded_by="GR-OBS-001 v2_2"`.
2. **Reimport** to refresh `wa_rule_registry` from the v2_12 source.
3. **Verify** with a fresh active-only extract: `GR-OBS-001 v2_2` present in `session_startup`; `GR-OBS-003 / GR-OBS-004` `obsolete=1` and excluded from default extract.
4. **Run** `python scripts/_check_doc_versions.py` to confirm GR-FILE-003 compliance.
5. **Cross-check** — `GR-FILE-001 v2_1` does *not* currently mention an obslog carve-out. Decide whether to:
   - leave the carve-out only inside `GR-OBS-001 v2_2` (status quo of this draft), or
   - also add a forward-pointer in `GR-FILE-001` ("Obslogs follow a special pattern — see `GR-OBS-001`."). Recommend the forward-pointer for discoverability.

## Outstanding questions for you

1. **Subject line** — _"Observations log — write discipline, segmentation, and filename convention"_. Acceptable, or trim further (e.g. _"Observations log — discipline and naming"_)?
2. **`session-name-abbreviated`** — is this declared by the researcher at startup, derived from the topic, or pulled from a controlled vocabulary? Current draft says "short token identifying the session topic" without further constraint. Want a max-length cap (e.g. ≤ 24 chars, lowercase, hyphens only)?
3. **`reference` default `ref-a`** — what does "ref-a" semantically denote? "Reference A" of an A/B/C series? A placeholder when no specific reference applies? Worth pinning the meaning in the rule so future readers don't have to guess.
4. **Carve-out from GR-FILE-001** — happy with the carve-out being declared inside `GR-OBS-001`, or do you want a small accompanying edit to `GR-FILE-001 v2_1 → v2_2` adding the forward-pointer? (My recommendation: yes, add the forward-pointer.)
5. **Existing obslog files** that don't match the new pattern (26 files in `data/imports/WA/Workflow/Sessionlogs/` and elsewhere — see prior search) — leave alone (historical), rename in place, or rename only when next touched? The new rule applies forward only unless you say otherwise.
6. **Draft v2_12 JSON now** (so you can review the full diff against v2_11), or wait until rule-text is signed off?
