# GR-OBS-001 Consolidation Draft

_Drafted: 2026-04-26 · Author: Claude Code · Status: **DRAFT — awaiting researcher approval**_

## Purpose

Fold the substance of `GR-OBS-003` (obslog vs session log) and `GR-OBS-004` (obslog version increment at named boundaries) into `GR-OBS-001`, producing a single observations-log rule under the `session_startup` category. After approval and application, `GR-OBS-003` and `GR-OBS-004` are marked obsolete with `superseded_by = GR-OBS-001 v2_2`.

## Source rules (current)

| rule_id | category | version | subject |
|---|---|---|---|
| GR-OBS-001 | session_startup | 2_1 | Observations log — continuous write, log authoritative, pass-close persistence |
| GR-OBS-003 | observation_discipline | 2_1 | Observations log vs session log — separate files, different purposes; session log mandatory at close |
| GR-OBS-004 | observation_discipline | 2_1 | Observations log version increment at named boundaries |

## Proposed consolidated rule — `GR-OBS-001 v2_2`

**Field changes vs v2_1:**

| field | v2_1 | v2_2 (proposed) |
|---|---|---|
| `category` | session_startup | session_startup _(unchanged)_ |
| `version` | 2_1 | **2_2** |
| `subject` | Observations log — continuous write, log authoritative, pass-close persistence | **Observations log — continuous write, log authoritative, pass-close persistence; obslog vs session log; version increment at named boundaries** |
| `applies_to` | all sessions, all phases | all sessions, all phases _(unchanged — already covers GR-OBS-004's narrower scope)_ |
| `rule_text` | _see below — current_ | _see below — proposed_ |
| `application_notes` | _see below — current_ | _see below — proposed_ |
| `last_modified` | 2026-04-21T08:47:50Z | **2026-04-26T<HH:MM:SS>Z** _(set on apply)_ |

### Proposed `rule_text`

> The observations log — referred to as the obslog — is the authoritative record of every session's working trail. The obslog is initialised as step 2 of the session-startup sequence (GR-LOAD-001); no substantive work may begin until it exists. While the session is live, every finding, decision, gap, patch consequence, and open question is written to the obslog at the moment it is determined. Every substantive chat output also appears in the obslog. When a researcher message is received, the researcher's feedback is recorded verbatim in the obslog before a response is formulated. At every pass close, items requiring database persistence are written via a patch or directive, and a fresh extract confirming the write becomes the working source for the next pass. This discipline persists for the life of the session.
>
> The obslog and the session log are separate files with separate purposes. The obslog is the working paper, written continuously as defined above. The session log is the handoff record, produced at session close and at any named batch boundary within a session. A session that closes without a session log has not closed cleanly — the session log is always produced before the session ends.
>
> The obslog filename is version-incremented when resuming work on the same registry or cluster in a new session — not on every file save within the same session. A named boundary is a new session start, not a mid-session write.
>
> This rule is non-waivable.

**Diff vs v2_1 rule_text:**
- Paragraph 1: unchanged from current v2_1 except the trailing "This rule is non-waivable." moves to the end of the rule (so it scopes the whole consolidated rule, not just the continuous-write clause).
- Paragraph 2 (new): absorbed verbatim from GR-OBS-003 v2_1, with one connective edit ("written continuously per GR-OBS-001" → "written continuously as defined above") since the rule no longer cross-references itself.
- Paragraph 3 (new): absorbed verbatim from GR-OBS-004 v2_1.
- Final line (re-positioned): "This rule is non-waivable." now applies to all three clauses.

### Proposed `rationale` _(unchanged from v2_1)_

> Claude AI cannot rely on in-memory accumulation across a session. Sessions crash; context windows truncate; follow-up work depends on what was captured. The obslog exists so that the working trail survives these failure modes. Without continuous capture to disk, findings reach the researcher only through chat output — which is ephemeral and unaudited. Continuous write makes the work externally reviewable at every turn.

_GR-OBS-003 and GR-OBS-004 had no rationale text; nothing to merge._

### Proposed `application_notes` _(unchanged from v2_1)_

> **Compliance test.** A useful shorthand: if something is not in the observations log, it has not been received or done. This is not literal — the thought existed — but it captures the rule's operational meaning: nothing that is only in chat or in memory counts as work.
>
> **Capture scope.** The list of content types caught by continuous-write includes: findings, decisions, gaps, patch consequences, flags, open questions, clarification requests, and researcher feedback verbatim. New content types arising in a session are logged on the same discipline.
>
> **Verbatim researcher capture.** 'Verbatim' means the researcher's message is reproduced exactly, not paraphrased or summarised. If the message is long, the full text is still captured; summaries appear elsewhere in the log if needed.

_GR-OBS-003 and GR-OBS-004 had no application_notes; nothing to merge. If you want operational notes for the absorbed clauses (e.g. what counts as a "named batch boundary", what the session-log filename convention is), flag and I'll draft._

## Knock-on actions after approval

1. **Edit source JSON** `data/imports/WA/Workflow/Framework_B/Session_B/wa-global-general-rules-v2_11-20260418.json` → produce `wa-global-general-rules-v2_12-20260426.json` (GR-FILE-003 minor bump). In the new file:
   - Replace `GR-OBS-001` block with the v2_2 content above.
   - Mark `GR-OBS-003` `obsolete=1`, `obsolete_reason="Substance folded into GR-OBS-001 v2_2 (obslog vs session log clause). Consolidated 2026-04-26."`, `superseded_by="GR-OBS-001 v2_2"`.
   - Mark `GR-OBS-004` `obsolete=1`, `obsolete_reason="Substance folded into GR-OBS-001 v2_2 (version increment clause). Consolidated 2026-04-26."`, `superseded_by="GR-OBS-001 v2_2"`.
2. **Reimport** to refresh `wa_rule_registry` from the v2_12 source.
3. **Verify** with a fresh active-only extract: GR-OBS-001 v2_2 present in `session_startup`; GR-OBS-003/004 present but `obsolete=1` and excluded from the default extract.
4. **Run** `python scripts/_check_doc_versions.py` to confirm version bump compliance.

## Outstanding questions for you

1. Are you happy with the three-paragraph rule_text structure, or do you want it more tightly woven into one paragraph?
2. Subject line as proposed is long. Acceptable, or shorten to e.g. _"Observations log — single end-to-end discipline (continuous write, session-log handoff, version increment)"_?
3. Should I draft the v2_12 JSON now (and you review the file diff), or wait until rule text is signed off?
4. Anything from GR-OBS-003/004 you want **dropped** rather than absorbed (e.g. you might want the "named batch boundary" carve-out reworded since it's been a source of ambiguity)?
