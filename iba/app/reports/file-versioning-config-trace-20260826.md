# File-versioning config — full trace, project-wide

> Extracted 2026-08-26 for escalation #857. Traced every live config setting and code path that
> touches file versioning — not just reports. Two real, live, config-driven mechanisms exist;
> neither covers "all files," and the broadest, original rule they both descend from has **no**
> config representation at all.

## 1. `report.version_on_regenerate` → `lib/reportkit.py:write_report()`

- **Config:** one `cfg_setting`, module `report`, boolean, default `true`.
- **Code:** read once, inside `write_report(conn, step, path, lines)`.
- **Filename it produces:** `{stem}-v{n}-{date}{suffix}` — `n` is NOT date-scoped, climbs forever
  across the report's whole lifetime; prior version moved to `cfg_report.archive_dir`; the
  plain-named `path` is also refreshed every time (escalation #702, see prior turn).
- **Scope — narrow:** only reports registered in `cfg_report` whose writer function calls
  `write_report()` directly. `escalation.list`/`escalation.history` were wired into this today;
  ~30+ other registered reports already used it (CONFIG-REPORT.md's own `-v148-`/`-v149-` sequence
  is this mechanism).

## 2. Four `governance.oneoff_*` settings → `lib/reportkit.py:oneoff_path()`

- **Config:** `governance.oneoff_report_dir` (`iba/app/reports/`), `governance.
  oneoff_report_naming_pattern` (`{topic}-{YYYYMMDD}.{format}`), `governance.oneoff_report_format`
  (`md`), `governance.oneoff_report_archive_dir` (`archive`).
- **Code:** read inside `oneoff_path(cfg, topic, ext)`. **Its own docstring names its source
  directly:** *"Same-day version bump on collision, per the Bible-study side's own established
  convention (`docs/file-organisation-rules.md §2.3`) rather than inventing a new one for this
  app."*
- **Filename it produces:** `{topic}-{YYYYMMDD}.md` normally; on a same-day collision,
  `{topic}-{YYYYMMDD}-v{n}.md` — here `n` **is** date-scoped (resets every day, unlike mechanism
  1). Prior live version archived first.
- **Scope — narrow, and different from mechanism 1:** only code that explicitly *calls*
  `oneoff_path()`. Confirmed live callers: `iba/app/handlers/configmaint.py`, `iba/app/lib/
  cfgquality.py`, `iba/app/lib/contentindex.py`, `iba/app/lib/manifest.py`, `iba/app/lib/
  cfgreport.py`. Not orphaned — genuinely used.

## 3. The rule these both descend from — `docs/file-organisation-rules.md §2.3` — has NO config representation

This is the **original, project-wide** rule (also restated in `CLAUDE.md` §9 item 4: "same-name =
version bump — `-v{n}`, no leading zero, applies even same-day"). Mechanism 2 above is a partial,
narrow implementation of it, scoped to one IBA subfolder. Searched exhaustively — **zero**
`cfg_setting` or `cfg_behaviour_rule` rows state this rule anywhere.** It exists only as prose in a
markdown file. Per `governance.rules_must_be_config_driven` ("no operational or process rule may
exist only in ... without a referenced cfg_* row recording it... any deviation discovered requires
escalation") — this is exactly the kind of gap that rule names, for the broadest and oldest
versioning convention the project has.

## 4. Not the same thing — flagged so it isn't confused with the above

`cfg_behaviour_rule` ids 48/49 (`record-change-log-choke-point`, `record-change-log-version-is-
pointer`) govern a **database row's** `version` column (`prose_section`/`prose_section_type`) —
that's DB-row versioning via `record_change_log`, unrelated to filenames or file versioning
entirely. Turned up in the same keyword search; not part of this trace's actual subject.

## 5. What is covered by NOTHING — including every report this session produced

Neither mechanism is a general file-versioning service anything can call — each is scoped to its
specific caller set. Concretely uncovered: every file under `Sessions-v2/`, `Workflow/`,
`outputs/`, `research/`, and most of `iba/docs/`; anything any handler writes via a raw
`path.write_text()` without calling either function. **Including, found on self-check, every
report this session's #857 investigation itself produced** — `escalation-review-action-config-
rules-20260826.md` and the other six filed today were all hand-typed with the Write tool, imitating
mechanism 2's `{topic}-{YYYYMMDD}` shape by convention, but never actually **calling**
`oneoff_path()` — no collision check, no archiving, no version bump ran for any of them. They
followed the pattern by habit, not by using the config that exists to enforce it.
