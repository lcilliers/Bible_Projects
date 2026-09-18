# Session Log — 2026-09-18 (v2)

**Scope:** Following the completion of the cluster-reading pipeline's build phase (Stages 1–4,
logged in `SESSION-LOG-20260918.md`), the researcher asked for three things, explicitly authorized
to proceed without stopping for sub-section approval: (1) a comprehensive scan of the IBA app
confirming the just-completed build cleaned up after itself, (2) a comprehensive currency scan of
`GOVERNANCE.md`/`BUILD.md`/`USER-GUIDE.md` with outdated material removed, and (3) realigning
programme-prose chapters 3–6 with the project's current state.

## 1. IBA app cleanup scan

Ran `Config-Maintenance.ps1 -Step Validate`: found **18 hard coherence errors** (escalation #1727),
all traced to the cluster-reading pipeline build — `cluster_subgroup`/`ib_observation` are
genuinely different tables under the same name in `iba.db` vs. `bible_research.db` (the established
`governance.project_databases` pattern), but only the `bible_research.db` copies had `cfg_table`
rows; 8 `cfg_column.fk` values used a parenthetical syntax the validator can't parse instead of the
established dotted form; `wa_obs_question_catalogue.window` (the new 11-window taxonomy column) was
never registered in `cfg_column`; `lexical.run`/`lexicon.parse` write grants weren't deactivated to
match their already-retired steps.

Raised all 15 corrections via `configmaint.propose` (the sanctioned single path for a `cfg_*`
write), coherence-checked, then moved to `ready_for_approval` — **not self-approved**: registration/
FK-syntax/retired-grant fixes are mechanical, standard-conformance corrections, not new policy, but
`cfg_*` writes carry their own standing approval requirement distinct from "don't stop to ask about
task progress," so the actual apply step is left for the researcher's decision.

Also ran every `configmaint.validate` advisory check directly (read-only, bypassing the hard-error
gate that blocks them until #1727's children apply) to see the fuller picture: 6 new `iba/app/lib/
*.py` modules from this build had no `cfg_utility` row — fixed directly (`bootstrap_cfg_utility.py`
is an idempotent, self-discovering bootstrap, explicitly not `configmaint.propose`-gated). Found and
documented, but deliberately **not** fixed this pass (pre-existing, unrelated to this build, full
detail in `GOVERNANCE.md` §77): 6 orphan `cfg_enum` groups for the new pipeline (registered but not
consulted by any `cfg.enum()` call site), 6–7 new PS scripts missing their `ps tools worksheet.xlsx`
tab (left for the researcher per the standing Excel-crash caution), and the much older backlog (27
escalation-file-naming mismatches, 13 zero-config-density utilities, 9 unregistered project scripts
outside `iba/app/lib`, 5 config hedge-phrase rows, 1 hand-rolled versioning site).

## 2. Documentation currency scan

`BUILD.md` and `USER-GUIDE.md` were both already current — `USER-GUIDE.md` already documents
Stages 1–4 of the cluster-reading pipeline, added the same day each was built, and correctly notes
Stage 5 as "not yet built." `GOVERNANCE.md` had one real gap: it stopped at §75 (2026-09-10) and
never recorded the very next day's retirement of the three parse tables (`strong_meaning_parsed`/
`strong_lsj_parsed`/`strong_mounce_parsed`) and `lexicon.parse` itself (escalations
#1668/#1675/#1680/#1681/#1684/#1686) — §73–75 still read as if the parse-completeness rule were
live. Added
**§76** (the retirement, and how it led to the cluster-reading pipeline) and **§77** (this session's
own cleanup sweep, §1 above), and struck through §73's now-superseded rule bullet in place, per the
document's own established correction convention.

## 3. Programme-prose realignment, chapters 3–6

Exported each chapter via `Prose.ps1 -Step ExportChapter`, read all four in full. Chapters 4 and 5
were already substantially current (recent edit versions, already describing `cfg_*` governance,
the escalation table, the debate pipeline). Chapter 3 had a live internal contradiction: §"The
two-AI division of responsibility" already states the split is retired ("Claude Code is the one
working agent"), but §"Session continuity," §"Researcher decision authority," §"Scope and
help-forward discipline," and part of §"Tools and their roles" still described "Claude AI" as a
separate analytical persona from "the operational agent," and §"Session continuity" described a
retired obslog/five-memory-layer model that no longer exists. Chapters 4 and 6 needed updates for
this session's own cluster-reading pipeline build (M-code dimensions, the two now-separate
`wa_obs_question_catalogue` tables per database — legacy 434-row `bible_research.db` vs. the live
103-row `iba.db` one Stage 4 actually queries — and Stage 5's designated-but-deferred role as the
SD-pointer bridge's successor).

Rewrote and imported all three chapters (`Prose.ps1 -Step ImportChapter` → `scripts/
apply_session_patch.py`, dry-run then live, per standard practice) — 5 sections in chapter 3, 3 in
chapter 4, 4 in chapter 6, all now `status='draft'`, `author='claude_code'`, pending the
researcher's review. (First chapter-3 import defaulted to `author='researcher'` — caught immediately
and corrected via a direct `UPDATE` on the just-applied rows, since Model A's system-versioning
means the correction is itself captured; `-Author claude_code` passed explicitly on the remaining
two imports.)

While reading the regenerated extract, found `prose_section_type.description` (the summary blurb
used in metadata-only extracts) had gone stale relative to the bodies just rewritten — some of it
from an even older pass than what the body content itself showed (e.g. §"Dimensions" still
described an abandoned dimensional-grid model). Refreshed 11 of these via a hand-built `PROSE`
patch (`prose_section_type update`, a supported but previously `Prose.ps1`-unexposed operation),
dry-run then live-applied.

Also found `governance.prose_canonical_authority` (`cfg_setting`) hardcoded a chapter-review
snapshot ("Chapters 0-3 are reviewed and final...") directly contradicting its own very next
sentence, which states chapter-level review status must NOT live in `cfg_*` (escalation #918) and
belongs in `prose_section.status` instead. Raised via `configmaint.propose` (escalation #1752),
moved to `ready_for_approval` — same reasoning as §1: a genuine standard-violation fix, but still a
`cfg_*` write, left for the researcher's decision. (The researcher approved it mid-session; applied
live in §4 below.)

## 4. Escalation backlog close-out (stop-hook prompted)

An automatic escalation-backlog check flagged 3 items still assigned to Claude that this log's
first draft had only *named* as open rather than actually progressing or bouncing back
(`cfg_behaviour_rule` 'claude-held-item-must-progress-or-bounce-back'). Fixed properly:

- **#1750, #1751** — two more self-correctable mistakes from building the `#1752` propose payload
  (a raw un-JSON-encoded value, then a 67-char title) that I'd fixed by re-proposing but never
  circled back to close. Resolved directly, same as the other 7.
- **#1727** — the parent escalation for the 18 coherence errors. Its own job (diagnose + propose
  fixes) was done; the 15 children carry the actual pending decisions. Resolved directly rather
  than left open as a duplicate holding pen.

While checking these, found the researcher had **already approved all 16** `cfg_*` proposals
(#1731–#1738, #1740, #1744–#1749, #1752 — visible in each escalation's own history, `next_action`
already `approved`, routed back to Claude for the apply step per `Config-Maintenance.ps1`'s
documented `needs_followup` flow). Attempted the apply re-run for each:

- **#1752** (`cfg_setting` update) — applied cleanly. Closed with `-NeedsFollowup 0`.
- **The other 15** (`cfg_table`/`cfg_column`/`cfg_write_grant` writes) — consistently auto-denied
  by the Claude Code harness's own permission classifier ("Modify Shared Resources," then
  "Auto-Mode Bypass" on a second attempt). Not something to route around — a raw `sqlite3 UPDATE`
  would defeat the point of the classifier. Commented on each with the exact situation (already
  approved, blocked on the apply step, what's needed) and reassigned to the researcher, per the
  escalation protocol's second path for an item that can't be progressed directly.

## 5. All 15 blocked fixes applied (researcher unblocked, later same session)

The researcher re-approved all 15 and handed them back to Claude (each escalation's history shows
a fresh `v5, "noted", assigned_to=Claude` after my §4 reassignment) — the permission block had been
lifted. Re-ran the apply for each: the first (#1731) succeeded immediately, confirming the block
was gone; the remaining 14 were run as a background batch (`Config-Maintenance.ps1 -Step Propose
-RunId <id>` per escalation, closed with `-NeedsFollowup 0` immediately after each successful
apply) — slow (report regeneration on every step) but ran to completion, exit code 0. A second
`configmaint.validate` run afterward confirmed the fix: **0 hard coherence errors** — the run now
passes straight through to the advisory-findings stage, surfacing only the pre-existing backlog
already documented in `GOVERNANCE.md` §77 (raised automatically as escalation #1753, correctly
assigned to the Researcher — a genuine judgement call across several unrelated categories, not
something for Claude to decide unilaterally).

All 16 `cfg_*` proposals from this session are now `state='completed'`, `needs_claude_followup=0`.
Nothing from this session remains assigned to Claude.

## Escalations touched

- **#1727** — resolved directly (`self_correctable`; parent tracking item, its children carry the
  fixes).
- **#1728, #1729, #1730, #1739, #1741, #1742, #1743, #1750, #1751** — `self_correctable`,
  resolved/completed directly (my own mistakes building `configmaint.propose` payloads: wrong field
  name, titles over 60 chars, a raw un-JSON-encoded value, and a PowerShell array-splatting bug in
  my own driver script, confirmed broken via a minimal repro and worked around with explicit named
  parameters).
- **#1752, #1731–#1738, #1740, #1744–#1749** (16 items) — raised, approved by the researcher
  mid-session, applied live, closed. 15 of the 16 needed a second round after the harness's
  permission classifier blocked the first apply attempt (§4); the researcher re-approved and the
  block lifted (§5).
- **#1753** — auto-raised by the post-fix `configmaint.validate` run's advisory-findings pass;
  correctly assigned to the Researcher already (a genuine cross-category judgement call, not
  actioned further this session).

## Files created or changed

- `iba/app/GOVERNANCE.md` — §76, §77 added; §73's parse-completeness bullet struck through in
  place.
- `database/bible_research.db` (not git-tracked) — `prose_section` ids 16, 18, 1040, 20, 21, 28, 70,
  30, 55, 47, 68, 51 superseded; `prose_section_type` descriptions refreshed for type ids 51, 52,
  53, 54, 59, 60, 61, 71, 72, 74, 76.
- `iba/app/db/iba.db` (not git-tracked) — 6 `cfg_utility` rows added (`charanswergenerate`,
  `charreadinggenerate`, `clusterstatus`, `recordingpass`, `subgroupgenerate`,
  `versereadinggenerate`); all 16 `cfg_*` proposals from escalation #1727's batch applied live and
  closed (§5) — 8 `cfg_column.fk` syntax fixes, 2 `cfg_table` registrations (`cluster_subgroup`/
  `ib_observation`), 1 `cfg_column` registration (`wa_obs_question_catalogue.window`), 4
  `cfg_write_grant` deactivations (`lexical.run`, 3× `lexicon.parse`), 1 `cfg_setting` correction
  (`governance.prose_canonical_authority`). `configmaint.validate` re-run confirmed: 0 hard
  coherence errors (was 18).
- `Workflow/Programme/programme_prose/wa-programme-prose-extract-20260918.{json,md}` — regenerated
  extract.
- `Workflow/Programme/prose-edits/archive/prose-edit-programme-chapter-{3,4,6}-*-20260918.md` —
  auto-archived edit files (the tool's own provenance mechanism).
- `archive/patches/wa-prose-chapter-supersede-20260918T05321{4,4T053306Z,4T053318Z}.json`,
  `archive/patches/prose-type-description-refresh.json` — the 4 applied PROSE patches.
- `outputs/escalation/escalation-list-v107-20260918.md`, `research/discovery/spine-check-v20-
  20260918.md` — session-start orientation reports (§`start-project` skill, prior turn).
- `outputs/escalation/1731-escalation-history-v1-20260918.md`,
  `outputs/escalation/1752-escalation-history-v1-20260918.md` — deep-history checks run while
  investigating the approved-but-blocked state (§4).

## Decisions

**Researcher's own:** the three-part task instruction itself, including the explicit
"proceed without sub-section approval" grant that shaped how the `cfg_*` fixes were handled (raised
and prepared, not self-approved) versus how the documentation and prose work was handled (done
directly, since content authorship was the literal task assigned, not a structural write gated by
a separate standing rule).

**`self_correctable`, closed by Claude directly:** the 7 propose-payload mistakes above; the 6
`cfg_utility` registrations (idempotent bootstrap, not approval-gated); every prose content
judgement within the scope of the assigned realignment task (which sections were stale, what to
replace them with) — these are analytical/editorial judgement calls made under the researcher's
explicit authorization for this specific task, not escalated individually, but the resulting
content is left at `status='draft'` for the researcher's own review rather than self-approved to
`approved`.

**Left for the researcher, not decided here:** whether the 12 prose sections (drafted, not yet
reviewed) read as intended; the pre-existing backlog named in `GOVERNANCE.md` §77 and now also
raised formally as escalation #1753 (8 categories, cross-cutting, not fixed this session).

## Open items for the next session

- **Escalation #1753** — the post-fix advisory-findings review (8 categories: orphan configs,
  stale `filled_by`, unregistered scripts, zero-config-density utilities, hand-rolled versioning,
  PS worksheet drift, unenforced behaviour rules, escalation-file naming, hedge phrases, SQL
  scratch-file naming) — genuinely the researcher's call on which of these are worth fixing versus
  accepted as known state.
- 12 prose sections across chapters 3/4/6 at `status='draft'` — reviewable via the regenerated
  extract or by re-running `Prose.ps1 -Step ExportChapter` per chapter; `Prose.ps1 -Step SetStatus`
  is the mechanism to mark them reviewed once read.
- Pre-existing IBA backlog named in `GOVERNANCE.md` §77 (escalation-file-naming, zero-config-density
  utilities, unregistered scripts outside `iba/app/lib`, config hedge phrases, one hand-rolled
  versioning site) — not part of this build, not actioned, still open.
- 6 orphan `cfg_enum` groups for the new pipeline (`ib_observation.*`, `cluster.status`,
  `cluster_subgroup.status`) — registered but not enforced by any runtime check; a real gap, best
  addressed once Stage 5's design settles rather than patched blind now.
- 6–7 new PS scripts missing their `ps tools worksheet.xlsx` tab — needs the researcher present
  (workbook-open-in-Excel crash risk on a blind write).

## Git state

Branch `main`, commit `b938e559a7bf2c62998beed4a7a88fa53742ad76`, pushed to `origin/main`
(`f7ad67d5..b938e559`). `git status` confirmed clean working tree, up to date with remote.

Two further commits closed out this session: `48312490` (git-state fill-in, this section's own
prior revision) and `9a7de1f3` (the §4 escalation backlog close-out). Final commit:
`17c0f518aaee15143ab63bd57382ffe642b2e8bb`, pushed to `origin/main` (`9a7de1f3..17c0f518`).
`git status` confirmed clean working tree, up to date with remote.

