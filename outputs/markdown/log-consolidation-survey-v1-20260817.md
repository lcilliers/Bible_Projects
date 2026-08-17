# Log-location survey — before consolidating (2026-08-17)

> Grounding for a new escalation (researcher, 2026-08-17): *"create a new escalation to
> consolidate the location of all logs to one folder in /logs/, move the logs that is all over
> the place and bring the configs up to date."* Per the immediately-preceding lesson (a config
> row must exist before a format/location is treated as settled — `governance
> .past_precedent_investigation_signals_missing_config`), this is a survey of the REAL scatter,
> not an assumed one, filed before any escalation or config change.

## What actually exists, measured

| location | file count | content | category |
|---|---|---|---|
| `Logs/` (repo root, existing) | 31 | old main-project session logs — `.md`, `.docx`, one `.zip` | narrative session log (historical, pre-restructure per `CLAUDE.md`) |
| `archive/Logs/` | 22 | already-archived copies | narrative session log (archived) |
| `Workflow/Sessionlogs/` | 126 | **mixed** — `wa-*-sessionlog-*.md` narrative logs, but also `PATCH-*.json` files and a `.zip` | **not purely logs** — needs triage, not a blind move |
| `outputs/session-logs/` | 15 | `wa-sesslog-*.md`/`wa-obslog-*.md` | narrative session log (clean) |
| `iba/logs/` | 68 | `SESSION-LOG-*.md` (2026-07-22 → today) + older `session-log-v{1-4}-*.md` | narrative session log (IBA app) |
| repo root (loose) | 3 | `SESSION-LOG-20260803/0814/0815-*.md` | narrative session log (IBA app, stray) |
| `Sessions/Session_B/{02_Verse_Context,05_Dimension_Review,09_Analysis_output}_logs/` | not counted | pipeline-generated per-word processing artifacts | **different category — NOT a narrative session log**, do not fold in |

## Real complications found, not glossed over

1. **`Workflow/Sessionlogs/` is not a pure log folder.** It holds `PATCH-*.json` operational
   patches alongside narrative logs — a blind "move every file" would misfile live patch data as
   a log. Needs a per-file (or per-pattern: `*.json` stays, `*sessionlog*.md`/`*obslog*.md` moves)
   triage, not a directory-level move.
2. **Windows filesystem is case-insensitive.** `logs/` and the existing `Logs/` are the *same*
   directory on disk here — "one folder in /logs/" most plausibly means using the existing
   `Logs/` as the canonical location, not creating a same-named sibling. Flagged for confirmation,
   not assumed.
3. **`Sessions/Session_B/*_logs`** are pipeline output (verse-context/dimension-review/analysis
   logs per word), not "what happened this session" narrative — a different concept sharing the
   word "log." Excluded from this consolidation's scope unless told otherwise.
4. **Overlaps escalation #650** (on-hold: *"think through filing between the main project and
   IBA... dependent on a deeper review of the statement of affairs"*) — this could BE a concrete
   piece of that deeper review, or the researcher may want it kept separately gated. Not decided
   here.
5. **Overlaps the just-raised session-log-config-gap escalation**
   (`MANUAL-20260817_055806_658970` — no `governance.session_log_dir`/`_naming_pattern`/`_format`
   settings exist at all). This consolidation, once a location is confirmed, settles that
   escalation's open location question rather than leaving it separately unresolved.

## Not decided by this document

The actual target folder, the disposition of `Workflow/Sessionlogs/`'s non-log files, and whether
`archive/Logs/` (already archived) needs touching at all — all genuine researcher calls, raised as
the new escalation, not decided here.
