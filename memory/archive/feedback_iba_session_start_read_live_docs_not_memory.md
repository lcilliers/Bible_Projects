---
name: feedback_iba_session_start_read_live_docs_not_memory
description: "At the start of any IBA-touching session, actually Read GOVERNANCE.md/BUILD.md/CONFIG-REPORT.md before making governance or build-state claims — don't answer from cross-session memory summaries alone."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 369238a5-4a30-4a96-85b6-138d1738a129
  modified: 2026-07-23T05:25:46.928Z
---

The CLAUDE.md pointer to `iba/app/BUILD.md`/`GOVERNANCE.md` (via `Start-Iba.ps1`) persists across
`/clear` automatically — the user never needs to re-paste or re-load those docs. But the pointer
only names where to look; it doesn't inject the content into context. Answering an IBA governance
question from memory-level familiarity (cross-session memory summaries, or the CLAUDE.md digest)
without actually opening the current files is not good enough — 2026-07-23 session: gave a
governance-compliance answer from memory first, only actually read `GOVERNANCE.md`/`BUILD.md` when
the researcher asked "are you sure you have this in memory" as a direct check.

**Why:** these docs are rewritten frequently and explicitly self-correct ("§5 corrected", "§6
corrected", "CORRECTED 2026-07-23") — a memory snapshot from even one session back can misstate the
current mechanism (e.g. table counts, what's enforced vs. stubbed, whether an escalation answer
shape is yes/no or three-way). This is the same discipline as
[[feedback_iba_gap_analysis_requires_live_build_inspection]] and
[[feedback_source_of_truth_is_written_record]], applied specifically to session-start orientation,
not only to gap-analysis tasks.

**How to apply:** before asserting any IBA rule, current build state, or compliance claim in a
fresh session, actually Read `iba/app/GOVERNANCE.md`, `iba/app/BUILD.md`, and (for specific rule
values) `iba/app/config/CONFIG-REPORT.md` — don't rely on memory's summary of them, and don't wait
to be asked twice.
