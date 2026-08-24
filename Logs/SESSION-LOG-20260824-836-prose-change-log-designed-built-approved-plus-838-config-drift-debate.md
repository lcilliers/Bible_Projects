# Session log — 2026-08-24 (cont.) — #836: prose change log designed (9 rounds) → consolidated proposal (3 rounds) → approved → built and tested live; #834/#837 self-inflicted CLI crashes closed; #838 config-drift finding debated and closed

**Session start:** `start-project`. Git clean at session start (last commit `03eb6088`, the prior
session's #829 on-hold handoff). STEP already up. IBA bootstrap READY. 16 open escalations reviewed;
most relevant: #836 raised but not yet worked, #829 on-hold pending it, a fresh crash log (#834).

## What happened, in order

1. **#834 checked and closed as non-issue.** A self-inflicted escalation-CLI crash from the prior
   session — a `short_description` 3 chars over the 60-char title limit, raising #835. Same pattern
   as three earlier crashes this week (#830/#827/#819); resolved self-correctable, no code fix.
2. **#836 design — 9 rounds, each a fresh file per the versioning-discipline correction from the
   prior session.** Researcher's opening framing: sources of prose change (multi-table edit script,
   a not-yet-built flag-fix routine, direct `prose_section_type` updates, an unconceptualised
   findings-generator), whether full previous-version text needs to stay live, insert/update/delete
   scope, whether `version` becomes the change-log id, and a full column-relocation list.
   - **v1–v2:** objective + control scope + a survey of existing patterns (escalation's own
     current-state + delta-history table, IBA's `run` table as a different execution-tracking axis,
     three existing bare-incrementing-number instances). Then answered the five opening questions
     directly against live code and live data — found two real write paths already bypassing
     tracking (`session_a_replace`, `prose_section_type.update`), and a live bulk-bloat check
     (1,040 rows/14MB, only 91 ever superseded, but **every** row including superseded ones still
     live in the FTS search index — a real defect, found while checking, unrelated to the design
     question itself).
   - **v3 — scale correction.** Researcher: today's activity is a small early experiment, not a
     preview — prose stays actively worked for years across ~40k verses/66 books/50 clusters/~4k
     characteristics, essays composed as short extracts from many angles. Strengthened the
     retention-option recommendation and surfaced a fifth, likely volume-dominant change source
     (pure editorial/stylistic revision, no upstream data event) — real, but too early to design,
     parked as a placeholder per direct instruction.
   - **v4 — Model A adopted.** "No old versions live" resolved as mutate-in-place (matching
     `prose_section_type`'s and escalation's own shape), not insert-then-prune — recommended because
     Model B would leave every future citation/link table exposed to `prose_section.id` changing
     under it. Full column design worked through against Model A.
   - **v5 — researcher asked for outside research**, not this project's own precedent. Found: Model A
     is the textbook *system-versioned temporal table* pattern (SQL:2011), not a project invention;
     MediaWiki's diff+gzip revision storage is the real, proven answer to the bulk concern beyond
     just relocating history. Compression adopted now; diffing named and set aside.
   - **v6 — a single shared `record_change_log` table, dictated directly**, not the two
     differently-shaped history tables v4 had proposed. Worked out the one gap the dictated field
     list left open (where prior content actually lives — a `payload` column, proposed) and stated
     plainly, not silently built in: `version = record_change_log.id` means version stops being a
     per-item 1-2-3 counter and becomes a direct pointer — confirmed as the researcher's deliberate
     intent.
   - **v7 — scope confirmed project-wide** ("this is opening a big door, and I think we should
     consider it"). `change_type`/broadened `change_source` added. Checked live before naming
     anything: `cfg_change_log` already exists (unrelated, config-seed-load audit) — new table named
     to avoid the clash. Checked `bible_research.db` against the researcher's own findings
     forward-note, not waiting to be asked: `finding_revision` already exists, 0 rows, a genuinely
     different field-level-delta shape — surfaced now, not resolved, per instruction to wait for
     findings work.
   - **v8 — migration instruction given directly** (91 superseded rows → log, hard-deleted). Found a
     gap the instruction didn't cover (the 949 live rows + 108 types also need a baseline log entry,
     since `version` can't point at nothing) — flagged as an addition needing confirmation, not
     assumed. The payload question produced a genuine wrong turn: proposed "resulting state," which
     was backwards.
   - **v9 — correction, owned plainly.** Researcher: *"how it looks like after the change is in the
     prose... what is not retained is what it looked like before — maybe the confusion is in the
     naming."* Not a naming issue — a real mistake. Reverted to prior-state (what v4/v7 already had),
     traced the drift to v8 reasoning itself away from v5's own correct research while trying to make
     the migration instruction feel intuitive.
3. **Consolidated proposal — 3 rounds, each one a real gap the researcher caught, not a smooth
   handoff.**
   - **v1** filed as "ready for approval" — wrongly deferred config content to "next round."
     Researcher: *"why are you not including the config entries..."* Fixed as v2, citing the
     violated standing instruction (#784 v10) directly rather than defending the omission: literal
     `cfg_table`/`cfg_column`/`cfg_enum`/`cfg_write_grant`/4×`cfg_behaviour_rule` content, checked
     live first (found `cfg_write_grant`/`cfg_behaviour_rule` genuinely empty for both prose tables,
     matching what #829 already found), with a clear boundary drawn against #829's own still-pending
     proposal so nothing was duplicated.
   - **v2 → v3:** same class of mistake, caught the same way — a test plan and build sequence
     "required up front" but not actually included. Fixed: an 18-case test plan and an 11-step build
     sequence, both literal, in the document itself.
4. **Approved. Build executed live**, not just written up:
   - `iba/app/migration/prose_change_log_build_v1_20260824.py` — tested against a full copy of the
     live DB before touching it for real. Found two defects no design round anticipated: **4 of the
     91 superseded rows sit in 2-hop supersede chains**, not simple pairs — fixed by walking to each
     chain's *final* live row; **3 partial indexes** blocked the column drops outright (two of them
     filtered on the very column being removed) — dropped and rebuilt against `delete_flagged = 0`
     only.
   - `scripts/apply_session_patch.py` — all 8 write operations across both tables rewritten through
     one choke-point helper. `supersede`/`bulk_supersede` genuinely rewritten (in-place `UPDATE`, not
     insert-a-new-row). `session_a_replace`'s long-standing bug — silently touching `created_at` on
     every replace — fixed in the same pass.
   - **Beyond the approved plan's own file list:** `iba/app/lib/prosestore.py` (export/import/
     search/extract — everything `search_prose.py`/`export_prose_chapter_edit.py`/
     `import_prose_chapter_edit.py` depend on) referenced the columns being dropped and would have
     crashed on next use. Found by checking, not assumed clean; fixed anyway rather than left as a
     known regression, all 4 paths re-tested live afterward including a real edit→patch round-trip.
   - Migration run live: 91 rows logged and hard-deleted, 949 + 108 baseline-backfilled, 0 dangling
     version pointers, FTS row count fell 1,040→949 automatically (the search-bloat defect found in
     round 2 fixed as a side effect, not a separate task). All 18 test-plan cases run against real
     data, results recorded on the escalation, not asserted — one case (flag-driven `change_reason`)
     honestly flagged as mechanically wired but untestable until #835 exists.
   - `GOVERNANCE.md` §52 and `docs/prose-store-architecture.md` (5 locations) updated. `#829`
     unblocked — its own drafted rule text formally superseded, taken off hold (a manual `-State`
     override was needed; a plain `Update` alone didn't clear the on-hold state).
5. **#836 approval-cycle mechanics.** `ready_for_approval` required a filled `resolution` (a rule
   the researcher flagged before I hit the crash it would have caused). Approved, then closed —
   `state='completed'` confirmed directly against the DB when the tool's own confirmation message
   read ambiguously.
6. **#837 closed** — my own first `approved` attempt on #836, missing resolution; same
   self-correctable non-issue pattern as #834/#830/#827/#819.
7. **#838 — a real config-drift finding, debated properly, not waved off.** `configmaint.validate`
   flagged the 2 new `cfg_enum` groups as orphan (CHECK-enforced, never read via `cfg.enum()`).
   First pass reached for the #833 precedent and recommended Approve — **wrong**, caught by the
   researcher: *"maybe the pattern you now see... is not the pattern... maybe you are not explaining
   sufficiently why a control that was put in place for a good reason is no longer good."* Retracted
   the comparison on inspection, not defended: #833 was a table with *no writer at all*; #836's
   tables are actively written daily, so the orphan-check's real concern (nothing ties `cfg_enum`'s
   declared vocabulary to the `CHECK` constraint's actual one) is live and legitimate here. Laid out
   the fuller, honest facts (every `change_type`/`status` value is a hardcoded Python literal, never
   caller-supplied; `apply_session_patch.py` has zero existing dependency on `Cfg` at all) and three
   real options rather than one recommendation. The researcher's own escalation update ("noted...
   prepare for approval... likely to re-appear until the script is completed") crossed in transit
   with the deeper redo — reconciled, then closed directly per explicit instruction after the
   back-and-forth read as evasive rather than careful.

## What's actually built and live now

`bible_research.db`: `record_change_log` (new), `prose_section`
(`-supersedes_id/-superseded_by_id/-source_file`, `+updated_at`), `prose_section_type`
(`+version/+updated_at`), migration applied (949 + 108 + 91-logged rows), 3 indexes
dropped-and-rebuilt. `iba.db`: full `cfg_table`/`cfg_column`/`cfg_enum`/`cfg_write_grant`/
`cfg_behaviour_rule` registration for the above. Code: `scripts/apply_session_patch.py`,
`iba/app/lib/prosestore.py` both live-tested post-migration. Pre-op backup:
`backups/bible_research_pre_changelog_<timestamp>.db`.

## Escalations touched this session

`#834` closed (non-issue). `#836` raised → 9 design rounds → 3 proposal rounds → approved → built →
completed. `#829` unblocked, off hold (v19). `#837` closed (non-issue). `#838` raised (dispatcher,
`configmaint.validate`) → debated → closed per direct instruction.

## Files touched this session

**New:** `iba/docs/prose-change-log-design-v1` through `-v9-20260824.md`; `iba/docs/prose-change-log-
proposal-v1` through `-v3-20260824.md`; `iba/app/migration/prose_change_log_build_v1_20260824.py`.

**Modified:** `scripts/apply_session_patch.py`; `iba/app/lib/prosestore.py`; `iba/app/GOVERNANCE.md`
(§52); `docs/prose-store-architecture.md`.

## Researcher's own framing, worth carrying forward

*"the current prose (and change occurance) is not a reflection of what is going to happen in the
months (years) to come... just imagine the control challenge for this."* That single reframing
turned a cautious "leaning" recommendation into a settled design decision, and surfaced a change
source (stylistic revision) the original four-source list had missed entirely. And on #838: being
asked to actually justify a waived-off control, not just re-assert the same conclusion with a
borrowed precedent, is the same discipline as D7's "this is really important" from the prior session
— a shallow analogy is not an explanation, and the researcher will catch the difference.
