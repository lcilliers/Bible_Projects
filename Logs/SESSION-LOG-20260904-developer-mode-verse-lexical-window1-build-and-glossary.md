# Session log — 2026-09-04 (Developer Mode session)

**Scope, one line:** Entered Developer Mode; built #1444's catalogue-code-split migration and
#1383's full verse-lexical Window 1 Layer 1/Layer 2 build (schema, config, code, PS scripts,
552,353-row corpus backfill, 2 real bugs caught and fixed live); after researcher approval, closed
out #1383's own named leftover items (4 spawned escalations, the `ps tools worksheet.xlsx` fix once
Excel was closed) and built #1447's full T1–T9 glossary (18 entries, a stale `prose_section` FK bug
found and worked around, spawned as its own escalation); worked the automatic 4-item escalation-
backlog check to real completion, not just acknowledgement — including a genuine data-integrity fix
(824 verses' worth of orphaned `verse_lexical` rows) for #1441. Session ends here at the
researcher's initiative to clear context and start fresh for Window 1 outstanding tasks + Layer 2
testing.

## Escalations touched, by id, with outcome

- **#1444** — `re-assigned`/`ready_for_approval` (prior session) → v10 (mine): built and ran
  `migration/split_obs_catalogue_mechanical_interpretive_codes_v1_20260904.py` — splits the 5
  bundled catalogue codes (T0.1.2/T4.6.2/T4.6.3/T7.2.2/T1.4.1) into mechanical/interpretive `a`/`b`
  pairs, soft-deleting the old unified codes; idempotent, verified live (131 active rows). → v11
  (researcher): **completed**, "approved as implemented."
- **#1383** — `re-assigned`/`ready_for_approval` (prior session, full build specification filed) →
  v27 (mine): built the full spec — schema/config migration
  (`migration/build_verse_lexical_window1_layer1_layer2_v1_20260904.py`: `verse_lexical` +8
  columns, `passage` +2, 2 new tables, 28 enum values, 4 steps, 19 method rules, H0853 role fix
  on 10,521 rows, full corpus backfill), new `lib/lexicalenrich.py`, 4 handler functions,
  `VerseLexical.ps1`/`Build-Passages.ps1` extended, 28-row catalogue `review_note` writeback. Two
  real bugs caught live (an off-by-one `LIKE` pattern, a variant-suffix matching miss in the
  backfill), fixed, independently re-verified. → v28 (researcher): **completed**, "approved, ahead
  of testing and validating, and a few unfinished items - spawn escalations to complete the
  unfinished items. Do not drop anything silently."
  - Follow-on this session, after approval: fixed `ps tools worksheet.xlsx` (Excel closed by the
    researcher mid-session) for both scripts' new flags — drift check now clean. Spawned **#1448**
    (party_human/party_angelic lexicons unseeded), **#1449** (no `note_type` for "verb triggered-by/
    impacts"), **#1450** (run the filed test plan in a fresh session), **#1451** (found live:
    `passage.build`'s `no-hibs` gate still blocks Window-1-only boundary registration — a real,
    named, unfixed coupling with Window 2).
- **#1447** — `re-assigned`/`ready_for_approval` (prior session, 3 open questions on record) → v4
  (researcher, during this session): **completed**, "approved, but to full scope of the glossary
  fix... all the variants of T1-T9 must be documented in the glossary." → built after approval: 18
  new `prose_section` rows (9× Verse Reading Technique T1–T9, 8× Tier Catalogue T0–T7, 1× bare "T1"
  disambiguator), the T0–T9/"DEPRECATED" range-discrepancy resolved by checking the source document
  directly (it's T0–T7, not deprecated — corrected in `1446-verse-word-analytic-methods-extract-v2`
  in place), the "T2 qualifiers" case dispositioned as already covered (no new entry needed). A real
  bug found applying the patch (`apply_session_patch.py`'s `prose_section` insert path fails against
  a stale FK, `prose_section_type_old`, which doesn't exist) — worked around by inserting the 18
  rows directly with the identical INSERT+audit-log shape, verified live. Since #1447 itself was
  already `completed` and could not be reopened, the build execution was recorded as **#1453**
  (`ready_for_approval`), and the FK bug itself spawned as **#1452** (raised `self_correctable`,
  reclassified to `decision_required` via `EscalateToDecision` — a live table rebuild needs the
  researcher's own call on timing, not decided unilaterally).
- **Automatic escalation-backlog Stop-hook check** (not a memory rule, `cfg_behaviour_rule
  claude-held-item-must-progress-or-bounce-back`) surfaced 4 items still `next_action_assigned_to=
  'Claude'`; all 4 progressed for real this turn, not just acknowledged:
  - **#1441** — genuinely fixed: 824 verses' worth of `verse_lexical` rows (13,621 total) found
    pointing at soft-deleted `span` rows from an earlier incomplete migration (a query correctly
    joining to only-live spans got zero results, even though the rows read as live). Soft-deleted
    the stale rows, re-ran the (now-extended) `lexical.build` for all 824 verses — 14,698 fresh
    rows, correctly pointed, all 8 new #1383 columns computed too. Verified: 0 remaining orphans
    corpus-wide, John.1.5 (the verse that surfaced this) now resolves 10/10. → `ready_for_approval`.
  - **#1442** — confirmed live: its own proposed fix (a dedicated same-gloss/different-code check)
    is exactly what #1383 built (`cross_lemma_shared_gloss` note_type + method rule + quality
    check). → `ready_for_approval`.
  - **#1378** — genuinely reviewed (its own instruction: "review... if not, prepare for approval").
    Not resolved: #1383 supplies the raw substrate this pipeline needs, but the actual ask (assemble
    a *finding* per verse/IB-word from that substrate) is real, undesigned work #1383's own
    definitional correction places outside Window 1 entirely. Handed back with that open question
    stated plainly, not forced closed. → `ready_for_approval`, open question for the researcher.
  - **#1379** — core ask (verse-lexical contextual enrichment) confirmed delivered via #1383. One
    leftover idea from its own history (tag HIB values at the verse-lexical read) now directly
    contradicts #1383's settled Window boundary — retired explicitly, not silently dropped, pointed
    at #1378 as where it would belong if still wanted. → `ready_for_approval`.

## Files created or changed

- `iba/app/migration/split_obs_catalogue_mechanical_interpretive_codes_v1_20260904.py` — new,
  one-off, idempotent (#1444).
- `iba/app/migration/build_verse_lexical_window1_layer1_layer2_v1_20260904.py` — new, one-off,
  idempotent (#1383 schema/config/backfill).
- `iba/app/lib/lexical.py` — H0853 `classify_role` exception; `build_for_verse` computes all 8 new
  Layer-1 fields for every future build; `resolve_code` now returns `language` directly.
- `iba/app/lib/lexicalenrich.py` — new (Layer 2 engine).
- `iba/app/handlers/lexical.py` — `enrich`.
- `iba/app/handlers/passage.py` — `suggest_boundary`.
- `iba/app/handlers/reports.py` — `lexical_exceptions_report`, `lexical_extract`.
- `iba/app/ps/VerseLexical.ps1` / `iba/app/ps/Build-Passages.ps1` — extended (`-PayloadPath`,
  widened `-Step`; `-Suggest`/`-Confirm`).
- `iba/docs/ps tools worksheet.xlsx` — `VerseLexical`/`Build-Passages` tabs updated to match.
- `iba/app/GOVERNANCE.md` (§72), `iba/app/BUILD.md` (§225), `iba/app/USER-GUIDE.md` (§12b-ii/
  §12b-iii) — #1383's build record.
- `iba/docs/1383-window1-layer1-layer2-test-plan-v1-20260904.md` — new, 40 cases across 6 areas,
  not yet run (spawned as #1450).
- `iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md` — corrected in place: the
  T0–T9/"DEPRECATED" claim about the tier catalogue was wrong on both counts, checked directly
  against the source document and fixed (banner + §4 retitled).
- `iba/docs/1447-glossary-t-scheme-entries-build-patch-input.py` /
  `iba/docs/1447-glossary-t-scheme-entries-patch-v1-20260904.json` — new, provenance for the 18
  glossary rows (applied directly against `bible_research.db`, not tracked in git).
- `Workflow/Catalogue/obs-catalogue.md` (+ archived `-v2`, new `-v3`) — regenerated report reflecting
  the #1444 catalogue split + #1383's 28-row `review_note` writeback.
- `outputs/escalation/*.md` — routine `Escalation.ps1 -Action List` report regenerations across the
  session; not deliverables in their own right.
- **Database (not git-tracked, `iba/app/db/*.db` gitignored):** `iba.db` — the full #1383 schema/
  config/backfill above, the #1441 data-integrity fix (13,621 rows soft-deleted, 14,698 rebuilt).
  `bible_research.db` — the #1444 catalogue split (5 codes → 10), the 28-row `review_note`
  writeback, the 18 new glossary rows.

## Decisions made

**Researcher's own decisions**, not self-correctable:
- Declared Developer Mode for this session.
- Instructed completing #1383's and #1444's outstanding build work.
- Approved #1444 as implemented; approved #1383 "ahead of testing and validating" with instruction
  to spawn escalations for every unfinished item, none dropped silently; approved #1447 to full
  scope, not the narrower scope originally proposed.
- Confirmed Excel closed, prompting the `ps tools worksheet.xlsx` fix.

**My own judgement calls, made and documented at their own location, not silently assumed** (per
the build spec's own closing section naming these as open; researcher's approval taken as
authorization to proceed on recommended readings, not as answering each individually):
- `passage.max_verses` → `cfg_passage`, not the doc's generic `cfg_setting` (matches every sibling
  `passage.*` row).
- `passage.genre`/`lexical_complete_at` → `cfg_column` ordinals 20/21, not the doc's assumed 24/25
  (found `passage`'s `cfg_column` registration already 4 columns short of its live schema — flagged,
  not fixed, out of scope).
- `lexical.enrich` → its own new `lib/lexicalenrich.py` module, not appended to `lib/lexical.py`.
- `party_human`/`party_angelic` lexicons deliberately left unseeded (named as non-blocking).
- `verse_lexical_note` stays off `debate_change_detail`'s audit trail (no downstream FK dependent
  yet, matching `verse_lexical`'s own convention).
- No new `note_type` for "verb triggered-by/impacts" — left open, spawned as #1449.
- #1441's fix chosen as re-run (re-derive fresh) over manual span_id repoint — re-running the real
  build engine also backfills the 8 new columns in the same pass, not just fixing the pointer.
- #1452 (the stale `prose_section_type_old` FK) reclassified from `self_correctable` to
  `decision_required` mid-raise, on the grounds that the FIX itself (a live table rebuild) is a real
  action needing the researcher's own timing call, even though WHAT to fix is unambiguous.

**My own errors, caught and corrected on the record, not glossed over**:
- The `narrative_morph` backfill's first draft had a `LIKE` pattern with one wildcard too many
  (`'HV__w%'` checked `morph_code` index 4, not the real TAM index 3) — silently matched nothing
  against Exod.14.31/15.1's own already-hand-verified wayyiqtol cases. Caught by spot-checking the
  backfill's own output, not by review of the code alone.
- The `is_negator`/`party_kind` backfill's first draft compared `strong` to the seeded lexicon by
  exact string, missing every code carrying STEP's own optional variant-letter suffix (`H3068G`,
  `H0430G`) — every divine-name occurrence in the Exod.15 test verses silently came back
  unclassified. Same catch method.
- #1452 was initially raised as `resolution_kind=SelfCorrectable`, which on reflection understated
  what a live table rebuild actually needs (researcher approval on timing) — corrected via
  `EscalateToDecision` in the same round, not left standing.

## Open items carried into the next session

1. **#1448–#1451** (spawned from #1383) — `ready_for_approval`, none yet reviewed by the
   researcher: party lexicons, the note_type gap, the deferred test plan, the `passage.build`
   Window-1/Window-2 coupling.
2. **#1452** — `decision_required`: the stale `prose_section` FK, real fix (table rebuild) not yet
   applied, needs the researcher's own timing call.
3. **#1453** — `ready_for_approval`: the #1447 glossary build's own execution record, not yet
   reviewed.
4. **Test plan not run** (`iba/docs/1383-window1-layer1-layer2-test-plan-v1-20260904.md`, 40 cases)
   — deliberately deferred per Developer Mode's own standing constraint ("work built this session
   is never tested in this same session"). **Named by the researcher as the explicit next-session
   plan**: `/clear` and `/start-project` to finish any remaining Window 1 build items, then run the
   Layer 2 Window 1 tests.
5. Session ending by the researcher's own choice, not because any item above reached a natural
   stopping point — Developer Mode marker to be cleared by `/exit-developer-mode` as part of this
   close-out.

## Git state — this log's own completion trigger

_To be filled in after commit/push, per this project's own convention — not asserted ahead of the
actual command output._
