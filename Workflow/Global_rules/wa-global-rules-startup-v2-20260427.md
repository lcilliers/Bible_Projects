# wa-global-rules-startup — Session Startup Rules (active)

_Source: `wa_rule_registry` (DB is source-of-truth post-M33) · category = `session_startup` · `obsolete=0` only · regenerated 2026-04-27 (GR-OBS-001 v2_2 → v2_3 — obslog destination folder added)._

**Active rules in this category: 2**

Per `GR-LOAD-001 v3_2`, these rules are loaded at every session start.

---

### `GR-LOAD-001` — Mandatory global rules load at every session start; familiarisation semantics; scope discipline at startup; help-forward bound at startup

- **Version:** 3_2  ·  **Applies to:** all sessions, all instructions, all phases
- **Added:** 20260421  ·  **Last modified:** 2026-04-21T07:08:02Z

**Rule text:**

> Claude AI reads this file in full at the start of every session, before reading any instruction document, extract, or data file. Session startup follows a three-step sequence, each step confirmed aloud in chat:
>
> (1) Rules loaded — state: "Global rules [filename] loaded — [n] rules across [n] categories."
>
> (2) Observations log initialised per GR-OBS-001.
>
> (3) Cadence discipline activated — state: "Cadence discipline M1+M4 active — self-check will precede every substantive response; present_files will follow every substantive write."
>
> Until all three confirmations are made, no substantive work may begin — no chat output of workings, no general conversation, no analytical work, no classification, no patch construction, no document production, no database operation. This rule is non-waivable.

**Rationale:**

> Claude AI forgets between sessions. This load gate exists to re-establish the full rule set at every session start, because the alternative — partial recall from memory, or proceeding without a load — is demonstrated to produce compliance failures. Non-compliance with the gate is a programme compliance failure, not a procedural oversight.

**Application notes:**

> Familiarisation semantics. When the researcher uses the verb 'familiarise' (or equivalents: 'read through', 'review the attached', 'load and hold', 'orient yourself'), the instruction has a bounded meaning. Familiarise means: (1) read every attached document in full — no skim, no sampling; (2) acknowledge the global rules and comply with session-start loading; (3) produce a feedback statement demonstrating the instruction was understood — what the task is, what scope it has, what the researcher has and has not asked for; (4) list what was read, including memory or project material loaded into context; (5) flag any compliance gaps (missing files, unclear scope, contradictions); (6) stop.
>
> Scope discipline at startup. Familiarise is read-and-acknowledge, not an invitation to analyse, propose, recommend, or structure the next step. Claude AI does not expand the scope of a familiarisation instruction by producing analytical observations, options, reflections, or other forward-motion content — even if the material invites it, and even if producing such content would demonstrate thorough reading. Demonstrating familiarisation is done through the feedback statement (step 3) and the list of what was read (step 4) — not through forward analysis.
>
> Help-forward at startup. Expanded or extensive help-forward is bounded at startup per GR-HF-001. Claude AI completes what the startup instruction asked for and stops until the next instruction arrives.

**Examples:**

> Familiarisation trigger phrases: 'familiarise yourself with the attached'; 'read through this'; 'review the attached'; 'load and hold'; 'orient yourself'.
>
> Specific failure mode countered: the trained pull to 'show the work of reading' by producing analysis of the attached material when only acknowledgement was asked for.

---

### `GR-OBS-001` — Observations log — write discipline, segmentation, and filename convention

- **Version:** 2_3  ·  **Applies to:** all sessions, all phases
- **Added:** 20260421  ·  **Last modified:** 2026-04-27 (v2_3 — destination folder added)

**Rule text:**

> The observations log — referred to as the obslog — is the authoritative record of every session's working trail. The obslog is initialised as step 2 of the session-startup sequence (GR-LOAD-001); no substantive work may begin until it exists. While the session is live, every finding, decision, gap, patch consequence, and open question is written to the obslog at the moment it is determined. Every substantive chat output also appears in the obslog. When a researcher message is received, the researcher's feedback is recorded verbatim in the obslog before a response is formulated. At every pass close, items requiring database persistence are written via a patch or directive, and a fresh extract confirming the write becomes the working source for the next pass. This discipline persists for the life of the session.
>
> The obslog and the session log are separate files with separate purposes. The obslog is the working paper, written continuously as defined above. The session log is the handoff record, produced at session close. A session that closes without a session log has not closed cleanly — the session log is always produced before the session ends.
>
> The obslog filename is version-incremented within the same session, at the end of a logical session batch, to keep the working file in manageable segments. The version bump is for size control, not for marking a new working scope: each new version continues the same logical obslog trail without loss of continuity. A version bump is not triggered by per-save writes within a batch, only by the close of a logical batch.
>
> The obslog filename follows the pattern `wa-obslog-[reference]-[session-name-abbreviated]-[version]-[date]`, where `reference` is declared at session startup (default `ref`), `session-name-abbreviated` is a short topic token (lowercase, hyphens only, maximum 16 characters), `version` follows GR-FILE-003 (`v1`, `v2`, …), and `date` follows GR-FILE-009 (`YYYYMMDD`). This pattern is a carve-out from GR-FILE-001's standard `[prefix]-[reference]-[short description]-[version]-[date]` order: for obslogs, the literal token `obslog` sits between the `wa-` prefix and the reference, so that all observation logs sort together regardless of their reference.
>
> The obslog and its companion session log are written to the folder that governs the work the session documents — not to a single global obslog folder. Destinations by session type:
>
> - Session B word-analysis sessions → `Sessions/Session_B/09_Analysis_output_logs/`
> - Verse Context (VC) classification sessions → `Sessions/Session_B/02_Verse_Context_logs/`
> - Dimension Review sessions → `Sessions/Session_B/05_Dimension_Review_logs/`
> - Programme prose authoring sessions → `data/imports/WA/Prose/logs/` (per file-organisation-rules §3.16 once that rule lands; presently the flat `Prose/` folder)
> - Methodology, rules-review, and Session-A discovery sessions → `Workflow/methodology/`
> - Database-review and programme-control sessions → `outputs/session-logs/`
> - Default when no specific folder applies → `outputs/session-logs/`
>
> The `Sessions/Patches/` folder is reserved for JSON patches and must not receive obslog or session-log files.
>
> This rule is non-waivable.

**Rationale:**

> Claude AI cannot rely on in-memory accumulation across a session. Sessions crash; context windows truncate; follow-up work depends on what was captured. The obslog exists so that the working trail survives these failure modes. Without continuous capture to disk, findings reach the researcher only through chat output — which is ephemeral and unaudited. Continuous write makes the work externally reviewable at every turn.

**Application notes:**

> Compliance test. A useful shorthand: if something is not in the observations log, it has not been received or done. This is not literal — the thought existed — but it captures the rule's operational meaning: nothing that is only in chat or in memory counts as work.
>
> Capture scope. The list of content types caught by continuous-write includes: findings, decisions, gaps, patch consequences, flags, open questions, clarification requests, and researcher feedback verbatim. New content types arising in a session are logged on the same discipline.
>
> Verbatim researcher capture. 'Verbatim' means the researcher's message is reproduced exactly, not paraphrased or summarised. If the message is long, the full text is still captured; summaries appear elsewhere in the log if needed.
>
> Logical batch boundary for version bumps. A logical batch is a coherent unit of work declared at startup or at the boundary itself — for example, processing batch 1 of N within a registry, or a clean Q&A round close. The bump is initiated at an explicit pause point, not by file size alone (file size is the reason the rule exists, but not the trigger — the trigger is the logical close).
>
> New session vs new batch. Crossing into a new session resets the obslog to a new file (new session-name-abbreviated, version reset to v1). Bumps within a single session continue under the same session-name-abbreviated and increment v1 → v2 → v3 …. The obslog never spans two sessions in the same file.
>
> Reference defaulting. If the researcher does not declare a reference at startup, the obslog filename uses `ref`. The reference identifies the working scope (e.g. a registry, a cluster, a programme-wide pass) and is set once per session.
>
> Session-name abbreviation. The token must be ≤ 16 characters, lowercase, hyphens only — chosen to keep total filename length short while preserving recognisability of the session topic. Examples: rules-review, flags-valid, vc-review, regmgmt, preamble. If a topic cannot be expressed in 16 characters, abbreviate aggressively rather than truncate (e.g. database-review → db-review).
>
> Forward-only application. Existing obslog files predating GR-OBS-001 v2_2 are not retro-renamed. The new pattern applies to all obslogs created from this rule's effective date onward.

---
