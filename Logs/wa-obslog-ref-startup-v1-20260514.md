# Session obslog — startup / familiarisation

- **Session start:** 2026-05-14
- **Reference:** ref (no specific reference declared by researcher)
- **Session type:** startup / familiarisation
- **Session-name abbreviated:** startup
- **Operator:** Claude Code

---

## Startup sequence (GR-LOAD-001)

1. **Global rules loaded** — `wa-global-rules-all-v2-20260427.md` — 34 rules across 12 categories: cadence_discipline (1), data_discipline (5), database_discipline (1), document_discipline (2), file_format (1), file_naming (6), file_output (1), pass_close (1), process_discipline (5), programme_orientation (8), researcher_decision (1), session_startup (2).
2. **Obslog initialised** — this file, per GR-OBS-001 v2_3.
3. **Cadence discipline M1+M4 active** — self-check will precede every substantive response; present_files will follow every substantive write.

## Researcher message (verbatim)

> familiarise yourself with the project and start up

## Familiarisation reads

- `CLAUDE.md` (always loaded)
- `MEMORY.md` index + key memory entries (auto-loaded)
- `Workflow/Global_rules/wa-global-rules-startup-v2-20260427.md` (GR-LOAD-001, GR-OBS-001)
- `Workflow/Global_rules/wa-global-rules-all-v2-20260427.md` (category headers + rule count)
- `Workflow/Sessionlogs/wa-sessionlog-20260513-end-of-session-v1.md` (most recent end-of-session report)
- `Workflow/Instructions/wa-claudecode-instruction-v4_4-20260428.md` (first 100 lines — scope and Architecture v2 addendum)
- `tasks.md` (full)
- `memory/project_current_work.md` (flagged 25 days stale; treated as historical)

## Flags / compliance gaps

- `memory/project_current_work.md` is 25 days old and pre-dates the term-anchor reset (2026-05-04) and cluster-publication workflow. Schema in memory says 3.9.0; CLAUDE.md and engine constants say 3.17.0. Memory is stale and should not be trusted as live state.
- `wa-claudecode-instruction-v4_4-20260428.md` is from 2026-04-28 (pre-restructure to cluster model). It still describes Architecture v2 obslog-to-DB capture for per-word Session B — superseded in practice by the cluster instruction (`wa-sessionb-cluster-instruction-v1_7-20260513.md`). No conflict for startup, but worth noting if Session B work is invoked.
- Git working tree has many staged deletions (per the startup `git status` snapshot) — these appear to be moves under the Workflow folder restructure documented in the 2026-05-13 end-of-session report. Not a blocker; flagged for awareness.
