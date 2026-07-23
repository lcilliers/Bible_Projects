# Review — escalation #304 findings, itemised for judgement (2026-07-23)

**Source:** `configmaint.validate` run `RUN-20260723_123556_579-CONFIGMAINT`, escalation id 304,
state `raised` (unanswered). Full question text on the escalation itself — this file pulls each
of the 13 items apart with its live DB row and (where relevant) actual code usage, so each can be
judged on its own rather than as one bundled yes/no.

**How to answer:** `Escalation.ps1 -Action Answer -RunId RUN-20260723_123556_579-CONFIGMAINT
-Answer <approve|reject|revise> [-Comment "..."]` — one answer covers the whole escalation (all 13
findings), so a `revise` comment is the way to give a per-item verdict if they don't all get the
same answer. See `GOVERNANCE.md` §9A point 2 for how orphan detection works, §15A/§15B for how
today's two new orphans got created.

---

## Part A — 6 orphan configs (not referenced anywhere in `iba/app/**/*.py`)

An "orphan" here means: `cfg_setting.key` or `cfg_enum.name` does not appear as a literal string
in any `.py` file under `iba/app/`, excluding `migration/*.py` (write-once bootstrap scripts don't
count as usage). Advisory, not an error — a setting can be legitimately pre-staged ahead of code
that doesn't exist yet, or (the case for all 6 below) can be a deliberate documentation-only
convention. The detector cannot tell those apart; that's the judgement call.

### 1. `cfg_setting 'governance.build_md_on_code_change'`
- **value:** `"any code change under iba/app/** must update iba/app/BUILD.md in the same unit of
  work — BUILD.md is the build record, not a one-time snapshot"`
- **use (stored rationale):** `researcher ruling 2026-07-22: BUILD.md/GOVERNANCE.md must stay
  current, not just be written once`
- **module:** `governance`
- **Pre-existing** — flagged as orphan since at least 2026-07-23 04:21 (escalation #265, same
  wording). Not new to this run.
- **What it actually is:** a process rule stated as a `cfg_setting` row so it lives in config
  rather than only in prose, but nothing in the app *reads* it to enforce anything — compliance is
  by convention (and by this session's own practice: BUILD.md/GOVERNANCE.md were in fact updated
  alongside every code change today).

### 2. `cfg_setting 'governance.governance_md_on_rule_change'`
- **value:** `"any governance/process rule change must be set in cfg_* first (via
  configmaint.propose), then GOVERNANCE.md updated to reflect it in the same unit of work —
  GOVERNANCE.md documents the config, it never holds a rule the config does not"`
- **use (stored rationale):** `researcher ruling 2026-07-22: no rule should exist only in
  GOVERNANCE.md; the config is the source of truth, GOVERNANCE.md is the overview of it`
- **module:** `governance`
- **Pre-existing**, same as #1 — flagged since 2026-07-23 04:21, unchanged.
- **What it actually is:** same shape as #1 — a self-referential meta-rule (this row's own
  existence is partly what it's describing) with no code consumer.

### 3. `cfg_setting 'governance.scripts_ps_dir'`
- **value:** `"iba/app/ps"`
- **use (stored rationale):** *(none recorded — `use` column is NULL)*
- **module:** `governance`
- **New this session** (§15A, escalation #271's follow-on) — first appears in escalation #285
  (2026-07-23 08:16), the run right after the script relocation was proposed/applied.
- **Confirmed by direct grep:** zero references in any `.py` file. No code resolves "where do
  PowerShell scripts for this app live" by reading this setting — the relocation in §15A moved
  files to `iba/app/ps/` directly; this row documents the destination after the fact, it did not
  drive it.
- **What it actually is:** the canonical-folder convention promoted from "just convention" to "a
  real `cfg_setting` row" per §15A's own wording — but promoting it to a DB row didn't also wire
  any code to read it.

### 4. `cfg_setting 'governance.scripts_python_dir'`
- **value:** `"iba/app/tools"`
- **use (stored rationale):** *(none recorded — `use` column is NULL)*
- **module:** `governance`
- **New this session**, same run/reasoning as #3 (its Python-script sibling).
- **Confirmed by direct grep:** zero references in any `.py` file. Same situation as #3.

### 5. `cfg_enum group 'escalation_answer'`
- **values:** `approve` (0), `reject` (1), `revise` (2)
- **Pre-existing** — created 2026-07-21 per `GOVERNANCE.md` §9A (the three-way answer rule), first
  flagged as orphan by 2026-07-23 04:21 (escalation #265), unchanged since.
- **What it actually is:** the controlled vocabulary is enforced procedurally — `configmaint.py`'s
  `validate()` branches on the literal strings `"approve"`/`"reject"` (see e.g.
  `handlers/configmaint.py:221,225`) and `escalation.answer` values are constrained by whatever
  writes them (`Escalation.ps1 -Action Answer`), not by a runtime `cfg_enum` lookup against this
  group. The enum row exists to make the vocabulary a governed, inspectable fact rather than a
  scattered set of string literals — but nothing queries `cfg_enum WHERE name='escalation_answer'`
  at runtime to validate an incoming answer.

### 6. `cfg_enum group 'escalation_state'`
- **values:** `raised` (0), `answered` (1), `paused` (2), `retracted` (3)
- **New this session** (§15B, built for the Edit/Pause/Resume/Retract lifecycle) — first appears
  in escalation #304 (this run), i.e. brand new.
- **Confirmed by direct grep:** zero references to `escalation_state` in any `.py` file.
  `lib/escalation.py`'s new `edit_question()`/`pause_run()`/`resume_run()`/`retract_run()` write
  the literal strings `"paused"`/`"retracted"`/etc. directly to `escalation.state`, the same
  pattern as #5 — the enum documents the vocabulary, nothing reads it back to validate a write.
- **Same class as #5**, just newly added rather than pre-existing.

**Summary of Part A:** 2 pre-existing (#1, #2 — accepted as orphans in every prior `validate` run
back to at least this morning, never actioned), 2 new from the script relocation (#3, #4), 2 enum
groups where the pattern is "governs vocabulary procedurally, not read back at runtime" (#5
pre-existing, #6 new). None of the 6 are dead/unused in the sense of "written once and forgotten"
— all 6 reflect real, current decisions; the question is only whether "declared in `cfg_*` but
enforced by convention/code-structure rather than a runtime lookup" is an acceptable shape for
this app's governance model, same as it already implicitly was for #1/#2/#5.

---

## Part B — 7 settings "needing justification" (module already has a dedicated table)

Trigger: `MODULE_DEDICATED_TABLE = {"candidate": "cfg_candidate_rule"}` in `lib/cfgquality.py:17-19`
— *any* `cfg_setting` row with `module='candidate'` is flagged, purely on the module tag, with no
check of whether the setting's actual shape resembles what `cfg_candidate_rule` holds. All 7 are
confirmed **actively read** in `handlers/candidate.py` (grep evidence below) — none are orphans;
this is a structural-placement question only.

**For contrast — what `cfg_candidate_rule` actually holds:** 289 rows, 2 columns (`kind`, `value`)
— per-item accept/reject rules, e.g. `{'kind': 'accept', 'value': 'G0037'}`. It is an enumerable
list of individual rule instances, not a place for scalar patterns, paths, or limits.

### 1. `candidate.lemma_base_pattern`
- **value:** `"^([HG]\\d+)([A-Z]?)$"`
- **use:** `capture group 1 = the base Strong's (sub-letters stripped) — the lemma key. The
  seed/stamp key on this.`
- **read at:** `handlers/candidate.py:32` — `re.match(ctx.cfg.setting("candidate.lemma_base_pattern", ...), code or "")`
- **shape:** a regex pattern (scalar) — not an enumerable list item.

### 2. `candidate.tag_clean_pattern`
- **value:** `"^[A-Za-z][A-Za-z' -]*$"`
- **use:** `a clean candidate_tag: letters/spaces/hyphens/apostrophe only — no parenthetical
  transliteration, punctuation, or multi-clause gloss text`
- **read at:** `handlers/candidate.py:643` — `re.compile(ctx.cfg.setting("candidate.tag_clean_pattern", ...))`
- **shape:** regex pattern (scalar).

### 3. `candidate.quality_report_path`
- **value:** `"iba/app/reports/candidate-quality.md"`
- **use:** `where candidate.validate persists its findings`
- **read at:** `handlers/candidate.py:208`; also referenced structurally by
  `lib/cfgquality.py:28` (`QUALITY_CHECK_REPORT_PATH["candidate.validate"]`).
- **shape:** a file path (scalar) — same category as every other module's `*_report_path` setting
  (`configmaint.report_path`, `passage.quality_report_path`, etc.), all of which live in
  `cfg_setting` uncontested. Singling this one out for `candidate`-module reasons would be
  inconsistent with how every other module's report path is stored.

### 4. `candidate.concept_delimiter_pattern`
- **value:** `"[:/]"`
- **use:** `a character in a candidate.load input word signalling more than one concept — split
  into one sub-item per piece before validating, rather than reject or guess which half is right`
- **read at:** `handlers/candidate.py:433`
- **shape:** regex pattern (scalar).

### 5. `candidate.tag_max_words`
- **value:** `5`
- **use:** `a candidate.load input word/tag longer than this many space-separated tokens is
  treated as a sentence, not a concept, and written as an exception row`
- **read at:** `handlers/candidate.py:644`
- **shape:** an integer threshold (scalar).

### 6. `candidate.transliteration_pattern`
- **value:** `"^[a-z]+'[a-z]+$"`
- **use:** `STARTER heuristic, tune via configmaint.propose as real cases are seen: a bare
  lowercase token with no space is a plausible transliteration (e.g. 'asah', 'halak') and gets
  written as an exception for a human read... conservative flag-for-review test, not a hard
  linguistic classifier`
- **read at:** `handlers/candidate.py:645`
- **shape:** regex pattern (scalar) — its own `use` text explicitly frames it as a tunable
  heuristic meant to be edited via `configmaint.propose` over time, which `cfg_setting` supports
  directly; `cfg_candidate_rule`'s `kind`/`value` shape has no field for "pattern."

### 7. `candidate.load_report_path`
- **value:** `"iba/app/reports/candidate-load.md"`
- **use:** `where candidate.load persists its per-run duplicates/exceptions report`
- **read at:** `handlers/candidate.py:663`
- **shape:** file path (scalar) — same reasoning as #3.

**Summary of Part B:** all 7 are scalar values (regex pattern, integer limit, or file path) that
configure *how `candidate.py`'s code behaves*, not per-item data rules like `cfg_candidate_rule`'s
289 `(kind, value)` accept/reject rows. The dedicated table and these 7 settings look like two
genuinely different shapes of config (enumerable rule-instances vs. scalar behaviour knobs) rather
than the same thing split across two homes — but that's exactly the call `MODULE_DEDICATED_TABLE`
is designed to force onto the researcher rather than assume, since the check itself has no concept
of "shape," only "module name."

---

## What's NOT in scope here

Escalation #304 also isn't the only open item — `GOVERNANCE.md` §15A flags this as the same class
as pre-existing orphans, and there are other, older open escalations unrelated to this run (see
`iba/app/reports/escalation-list.md`). This file covers only the 13 findings inside #304.
