# Session log — 2026-07-27 — passage-debate method baked into the app, corrected, and made trackable

**Session closed deliberately 2026-07-27, at the researcher's request** — not a token-limit
pause. Work is at a clean stopping point: the passage-debate pipeline is fully mechanised and
config-governed, the method itself has been corrected twice on direct researcher feedback, and
completion is now trackable in the DB. Nothing here depends on this conversation's memory to
continue — the next session starts cold, reads this log, and picks up from "Where to start"
below.

---

## What this session did, in order

### 1. Read `WA-dan-1-1-7-debate` cold, listed its IB characteristics/states
Starting point: no prior context. Read the existing Dan 1:1–7 passage debate in full and produced
a plain listing of every retained/referential IB operation it found, verse by verse. Purely
informational — no artifact beyond the chat response.

### 2. Produced Dan 2:17–30 (base extract + debate) — first live application of the established method
Ran `VerseSpanMeaning-Report.ps1` then hand-wrote the debate, applying the two method docs as they
stood at the time (`WA-passage-read-guidance-v1.1` — see item 7, that filename never actually
existed as a file until this session; `WA-interpretation-questions-v1.0`). Produced
`WA-dan-2-17-30-debate-v1.0-2026-07-27.md` (now superseded, see item 4).

### 3. Corpus-review assessment — four debates checked against isolate-operations / isolate-parts / ask-the-right-questions / stay-on-brief
Reviewed `WA-dan-1-1-7`, `WA-dan-1-7-21`, `WA-dan-2-1-16` (researcher-authored, not by this
session), `WA-dan-2-17-30` against `Passage read guidance.md` and `WA-interpretation-questions-
v1.0`. First pass concluded the interrogative discipline was strong but the four documents used
inconsistent Subject/Operation/Source/Target formatting and had drifted EQ logs. **The researcher
pushed back directly**: the first pass graded the wrong layer — it never checked whether step 2's
gate was letting human-bearing clauses through to the interrogative in the first place. Re-scanned
on that basis and found a real, recurring pattern: verses naming a human doing something were
dismissed as "outward"/"administrative" *before* Q1/Q2 ever ran. Worst instance: Dan 2:13's
condemned wise men (facing execution, a party who had spoken at length two verses earlier) got no
interior treatment at all. Full findings, verdict, and priority-ordered fixes:
[`reports/dan-debate-method-assessment-20260727.md`](../app/reports/dan-debate-method-assessment-20260727.md).

### 4. All four debates redone as v1.1; the guidance doc corrected to v1.2 (step 2 note (f))
`WA-passage-read-guidance-v1.2-2026-07-27.md` (supersedes an "v1.1" every debate had been citing
that never existed as a file) adds step 2 note (f): every human mentioned is a presumptive IB
candidate; step 2's exit applies only where no human, or only an unrelated non-human, is present.
All four debates rewritten to v1.1: the seven missed operations from the assessment added as
retained operations or explicit named silences (never invented), every operation reformatted to
the `WA-dan-2-1-16`-style Subject/Operation/Source/Target block, and the false "Nebuchadnezzar's
interior stated for the first time" claim in `WA-dan-2-17-30` corrected against `WA-dan-2-1-16`'s
actual record. The EQ-log-merge recommendation from the assessment was **withdrawn** — not a real
defect; EQ logs are per-passage by design (see item 7). Old v1.0 files archived, not deleted.

### 5. The passage-debate method baked into the app as `report.passage_debate`
Researcher's request: config items, report format/destination/naming/content in config, a leading
PS script, "all the other requirements... for incorporating a new method." Built on the exact
precedent `report.verse_span_meaning` set: new `lib/passagedebatereport.py` (writes a SCAFFOLD —
front-matter citing the resolved current method-doc paths, per-verse Subject/Operation/Source/
Target + Q1-Q9 placeholders, standard closing sections — analytical content stays an AI's job, not
mechanised), new work package `passage-debate-report` → step `report.passage_debate` →
`handlers/reports.py:passage_debate_report`, new PS wrapper `PassageDebate-Report.ps1`. New
`cfg_setting`s `method.passage_read_guidance_path`/`method.interpretation_questions_path` (new
module `method`) — the CURRENT method-doc version is now a config fact, not something an AI or a
debate's own front-matter has to remember correctly (the exact gap item 4 found and fixed).
Registered via direct migration (`migration/bootstrap_passage_debate_report.py`, idempotent — 15
rows incl. a new `cfg_enum(config_module)` value), not `configmaint.propose` row-by-row, per the
established infrastructure-registration carve-out. Two failure conditions
(`base-extract-missing`, `guidance-doc-missing`) tested live through the real dispatcher, incl. a
deliberate config-break-and-restore test. `USER-GUIDE.md` §12b and `BUILD.md` §27 written (the
former also backfilled `report.verse_span_meaning`'s own missing documentation).

### 6. Dan 2:31–49 produced live through the new pipeline — a real DB gap found and flagged
Ran the new two-step pipeline for real. Found **Dan 2:33 does not exist in the DB at all** — no
`verse` row for `Dan.2.33` (chapter runs 1-32, 34-49) — confirmed by direct query, flagged in the
debate's insufficiencies register and reported to the researcher, not silently worked around or
fixed (out of scope for a debate-writing pass). The debate itself is the corpus's richest data
point yet for the passage-level "does divine sourcing reach disposition or only circumstance"
question (Dan 2:37-38 — God gives Nebuchadnezzar kingdom/power/might/glory/dominion, uniformly
circumstantial, never dispositional), plus a real unresolved textual tension surfaced (2:47 credits
Daniel personally for what Daniel himself denied any personal credit for at 2:30).

### 7. Scope-fork framing corrected — tracked, not a researcher ruling
Researcher's direct correction, quoted in full: *"it is not a researcher decision. It will either
emerge from the broader study or not."* Every debate had been describing the disposition-vs-
circumstance fork as "still awaiting the researcher" / "a researcher decision, not resolved here."
Wrong framing. Fixed at the source, not just patched in the debates: `WA-interpretation-questions-
v1.1-2026-07-27.md` adds Part B.9 — an interpretive fork this instrument raises is tracked exactly
like an emergent question (Q10/B.8), answered or left open by what the growing corpus shows, never
escalated for an up-front ruling; "the researcher should decide" is reserved for genuine
resourcing/data-curation calls (name etymologies, a DB gap), not interpretive questions the study
itself exists to answer. All four debates' "Scope fork" bullets reworded to match. The `method.
interpretation_questions_path` config update (v1.0 → v1.1) was proposed via `configmaint.propose`
(approval-gated, **not self-approved**), the researcher answered it themselves via
`Escalation.ps1 -Action AnswerRun` from the repo root (an earlier `.\Escalation.ps1` snippet was
wrong — not runnable from where the researcher actually was; corrected to the full
`iba\app\ps\Escalation.ps1` path), and the proposal was applied — confirmed live by
`PassageDebate-Report.ps1`'s own printed method-doc path switching to v1.1.

### 8. `passage`/`verse_passage` repurposed as the completion-tracking record
Researcher's framing: the passage tables become the record of what's been processed — extract
filename, debate filename, cross-referenced to the verse table, so book completion is queryable
and any verse is traceable back to its passage/outcome. Explicitly out of scope, in the same
message: digesting the debate's analytical *content* into the DB — "still emerging," not designed
here. Repurposed the tables §23 retired (candidate-driven system, 18,504/24,763 rows soft-deleted,
kept for provenance, "no new passage design proposed... yet"), now decided. **A real blocker found
first**: `verse_passage.verse_id` had a hard inline `UNIQUE` constraint, and the retired rows
already occupied nearly every verse_id in the Bible — any new insert would be blocked by dead rows.
Fixed by rebuilding the table (one dependent view dropped/recreated, one explicit transaction with
a row-count check) with a partial unique index (`WHERE deleted=0`) instead — every retired row
preserved exactly, "one live passage per verse" enforced going forward.
`migration/repurpose_passage_tracking.py` (idempotent): 6 new nullable `passage` columns
(`book_label`, `verse_span_meaning_path`/`_written_at`, `debate_path`/`_written_at`,
`debate_status` — new `cfg_enum(passage_debate_status)`: `scaffold`|`filled`, a **mechanical**
placeholder-scan only, explicitly not a content model, per the researcher's stated boundary), a
partial unique index on the range identity, `cfg_column`/`cfg_unique`/`cfg_write_grant` rows. New
`lib/passagetrack.py` (`record_extract`/`record_debate`) called from both report handlers
immediately after a successful write — linked into the run, not a separate step, per the
researcher's explicit requirement. Backfilled for the five real Daniel ranges already completed
(`migration/backfill_passage_tracking_daniel.py`) — a real bug caught in the process (`Cfg.close()`
does not commit, only `Db.close()` does; the live dispatcher path was unaffected since it shares
one connection through `Db`, but the standalone backfill script needed an explicit commit).
Verified end-to-end (Dan 3:1-7, safe to regenerate — scaffold-only) and via the backfill: all five
real ranges show `debate_status='filled'`; Dan 1:7, the shared boundary between two debates,
correctly resolved to a single current owner. `configmaint.validate` clean throughout. Full detail:
`BUILD.md` §28.

### 9. This close
Asked whether clearing/a new session was necessary before the next passage. Answer given: not
necessary (nothing lives only in conversation memory — DB, config, and files carry everything
forward), but recommended anyway given this session's accumulated size, since none of it is needed
to write the next debate. Researcher agreed; this log is the resulting cold-start entry point.

---

## Where to start a fresh session

1. **Next passage to debate.** `WA-dan-3-1-7-debate.md` currently exists only as an
   auto-generated **scaffold** (`debate_status='scaffold'` in the `passage` table, id `37414`) —
   every `<!-- fill in -->` placeholder is still unreplaced. Confirm with the researcher whether
   Dan 3:1-7 is the intended next range (it was chosen this session purely as a safe test target,
   not deliberately as "the next passage to read") before writing real analytical content into it.
2. **Dan 2:33 is missing from the DB** (no `verse` row for `Dan.2.33`) — flagged in the Dan
   2:31-49 debate's insufficiencies register, not yet reported through any other channel or fixed.
   Raise it with the researcher; do not silently backfill from an external translation.
3. **The four pre-registration debate files use the old ad-hoc naming**
   (`WA-dan-{range}-debate-v1.1-2026-07-27.md`), not the new stable-name scheme
   `report.passage_debate` writes (`WA-dan-{range}-debate.md`, archive-on-write, no version in the
   name). Explicitly left unreconciled (BUILD.md §27's own closing note) — do not rename or merge
   them without asking.
4. **How the debate's analytical content gets digested into the DB is still undecided** — `passage.
   debate_status` is a coarse scaffold-vs-filled signal only. Do not design or scaffold a content
   model pre-emptively; the researcher is still working this out.
5. **The scope fork (disposition vs. circumstance) and its related EQ items are still open** by
   design — they are not waiting on a researcher ruling (item 7). Continue treating them as
   evidence accumulates; do not force a resolution.
6. `git status` after this log should show a clean tree (this session's work committed and pushed
   in the same unit of work, per `governance.session_log_triggers_commit`) — if not, something
   changed between this log being written and being read; investigate before assuming continuity.

## Artifacts this session

**Method docs** (`iba/docs/`): `WA-passage-read-guidance-v1.2-2026-07-27.md` (new, step 2 note
(f)), `WA-interpretation-questions-v1.1-2026-07-27.md` (new, Part B.9); both v1.0/v1.1 predecessors
archived, not deleted.

**Debates** (`iba/app/verse-analysis/Daniel/`): `WA-dan-1-1-7-debate-v1.1`, `WA-dan-1-7-21-debate-
v1.1`, `WA-dan-2-1-16-debate-v1.1`, `WA-dan-2-17-30-debate-v1.1` (all rewritten this session),
`WA-dan-2-31-49-debate.md` (new), `WA-dan-3-1-7-debate.md` (scaffold, test artifact). Matching
`dan-*-verse-span-meaning.md` extracts for 2:17-30, 2:31-49, 3:1-7. Old versions archived.

**App code** (`iba/app/`): `lib/passagedebatereport.py` (new), `lib/passagetrack.py` (new),
`handlers/reports.py` (extended — `passage_debate_report` handler, `passagetrack` wiring in both
report handlers), `ps/PassageDebate-Report.ps1` (new), `migration/bootstrap_passage_debate_report.py`
(new), `migration/repurpose_passage_tracking.py` (new), `migration/backfill_passage_tracking_daniel.py`
(new).

**Config**: `report.passage_debate_naming_pattern`, `method.passage_read_guidance_path`,
`method.interpretation_questions_path` (the last bumped v1.0→v1.1 via `configmaint.propose`,
researcher-approved, not self-approved), `cfg_enum(config_module, method)`,
`cfg_enum(passage_debate_status)`, `cfg_write_grant` rows for both report steps → `passage`/
`verse_passage` — all via the infrastructure-registration carve-out except the one propose-gated
setting bump.

**Data**: `passage`/`verse_passage` schema repurposed (6 new `passage` columns, `verse_passage`
rebuilt to drop a blocking inline `UNIQUE` constraint); 6 live `passage` rows now exist for Daniel
(5 real + 1 test scaffold), cross-referenced to 76 `verse_passage` rows.

**Reports**: `reports/dan-debate-method-assessment-20260727.md` (new, revised in place per B.9's
correction — one living document, per standing convention).

**Docs**: `BUILD.md` §27–§28, `USER-GUIDE.md` §12b — all updated in the same unit of work as their
triggering code/config change, per `governance.build_md_on_code_change`/`governance_md_on_rule_change`.
