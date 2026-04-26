# wa_rule_registry — session_startup + observation_discipline

_Source: `data/bible_research.db` · table `wa_rule_registry` · generated 2026-04-26 06:12Z_

Filter: `category IN ('session_startup','observation_discipline')`  ·  Rows: **7**

## observation_discipline  (5 total — 2 active, 3 obsolete)

### `GR-OBS-003` — Observations log vs session log — separate files, different purposes; session log mandatory at close  _[active]_

- **Version:** 2_1  ·  **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:47:50Z
- **Source document:** wa-global-general-rules-v2_11-20260418.json
- **Applies to:** all sessions, all phases

**Rule text:**

> The observations log (obslog) and the session log are separate files with separate purposes. The obslog is the working paper, written continuously per GR-OBS-001. The session log is the handoff record, produced at session close and at any named batch boundary within a session. A session that closes without a session log has not closed cleanly — the session log is always produced before the session ends.

---

### `GR-OBS-004` — Observations log version increment at named boundaries  _[active]_

- **Version:** 2_1  ·  **Added:** 20260414  ·  **Last modified:** 2026-04-21T08:48:04Z
- **Source document:** wa-global-general-rules-v2_11-20260418.json
- **Applies to:** Session B, Dimension Review, Verse Context instructions

**Rule text:**

> The observations log (obslog) filename is version-incremented when resuming work on the same registry or cluster in a new session — not on every file save within the same session. A named boundary is a new session start, not a mid-session write.

---

### `GR-OBS-002` — Observations log classification categories  _[OBSOLETE]_

- **Version:** 2.0  ·  **Added:** 20260414  ·  **Last modified:** _(none)_
- **Source document:** wa-global-general-rules-v2_11-20260418.json
- **Applies to:** Session B, Dimension Review, Verse Context instructions
- **Obsolete reason:** Retired in v2_9. Four-category pass-close classification subsumed by consolidated observations-log discipline in GR-OBS-001 v2_0 and GR-OBS-003 v2_0.
- **Superseded by:** GR-OBS-001 v2_0 and GR-OBS-003 v2_0

**Rule text:**

> Every entry in the observations log is classified into exactly one of four categories at the pass-close review: (a) Drop — no analytical value, no database home; (b) Entity-linked observation — analytical comment keyed to one or more entities, queued for database write; (c) Forward pointer — Session B pointer or Session D pointer, queued for pointer table write; (d) Session action — data quality finding, methodology note, sequencing decision, self-correction, verification record. An entry that does not fit one of these four categories is flagged for researcher review using the RESEARCHER_DECISION format (GR-RD-001).

---

### `GR-OBS-005` — No physical deletion — flag and mark only  _[OBSOLETE]_

- **Version:** 2.0  ·  **Added:** 20260414  ·  **Last modified:** _(none)_
- **Source document:** wa-global-general-rules-v2_11-20260418.json
- **Applies to:** all sessions, all phases
- **Obsolete reason:** Migrated to addendum_patch_directive ADD-PATCHDIR-004 in v2_8. Rule text preserved in addendum item; consolidation session will incorporate into target instruction.

**Rule text:**

> No database record is ever physically deleted. Records that are superseded, incorrect, or out of scope are marked with delete_flagged = 1, obsolete_reason, and obsolete_date. The original record is retained for audit. This applies to all tables across all phases. CC must never execute DELETE statements against analytical records.

---

### `GR-OBS-006` — All observations return to the database  _[OBSOLETE]_

- **Version:** 2.0  ·  **Added:** 20260414  ·  **Last modified:** _(none)_
- **Source document:** wa-global-general-rules-v2_11-20260418.json
- **Applies to:** all sessions, all phases
- **Obsolete reason:** Migrated to addendum_instructions ADD-INSTR-011 in v2_8. Rule text preserved in addendum item; consolidation session will incorporate into target instruction.

**Rule text:**

> Every analytical observation produced during any phase must be persisted to the database before the session closes. Session C and Session D read from the database only — they do not read observations logs or session logs as source material. An observation that exists only in a markdown file has not been recorded for the programme.

---

## session_startup  (2 total — 2 active, 0 obsolete)

### `GR-LOAD-001` — Mandatory global rules load at every session start; familiarisation semantics; scope discipline at startup; help-forward bound at startup  _[active]_

- **Version:** 3_2  ·  **Added:** 20260421  ·  **Last modified:** 2026-04-21T07:08:02Z
- **Source document:** wa-global-general-rules-v2_11-20260418.json
- **Applies to:** all sessions, all instructions, all phases

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

### `GR-OBS-001` — Observations log — continuous write, log authoritative, pass-close persistence  _[active]_

- **Version:** 2_1  ·  **Added:** 20260421  ·  **Last modified:** 2026-04-21T08:47:37Z
- **Source document:** wa-global-general-rules-v2_11-20260418.json
- **Applies to:** all sessions, all phases

**Rule text:**

> The observations log — referred to as the obslog — is the authoritative record of every session's working trail. The obslog is initialised as step 2 of the session-startup sequence (GR-LOAD-001); no substantive work may begin until it exists. While the session is live, every finding, decision, gap, patch consequence, and open question is written to the obslog at the moment it is determined. Every substantive chat output also appears in the obslog. When a researcher message is received, the researcher's feedback is recorded verbatim in the obslog before a response is formulated. At every pass close, items requiring database persistence are written via a patch or directive, and a fresh extract confirming the write becomes the working source for the next pass. This discipline persists for the life of the session. This rule is non-waivable.

**Rationale:**

> Claude AI cannot rely on in-memory accumulation across a session. Sessions crash; context windows truncate; follow-up work depends on what was captured. The obslog exists so that the working trail survives these failure modes. Without continuous capture to disk, findings reach the researcher only through chat output — which is ephemeral and unaudited. Continuous write makes the work externally reviewable at every turn.

**Application notes:**

> Compliance test. A useful shorthand: if something is not in the observations log, it has not been received or done. This is not literal — the thought existed — but it captures the rule's operational meaning: nothing that is only in chat or in memory counts as work.
> 
> Capture scope. The list of content types caught by continuous-write includes: findings, decisions, gaps, patch consequences, flags, open questions, clarification requests, and researcher feedback verbatim. New content types arising in a session are logged on the same discipline.
> 
> Verbatim researcher capture. 'Verbatim' means the researcher's message is reproduced exactly, not paraphrased or summarised. If the message is long, the full text is still captured; summaries appear elsewhere in the log if needed.

---
