# IBA Session Log — v4, 2026-07-22

**Topic:** Continuation from `session-log-v3-20260722.md`. A long session: config-seed/README
audit, a hard ban on the unreliable `AskUserQuestion` tool, `GOVERNANCE.md`/`BUILD.md`/
`USER-GUIDE.md` all found badly stale and rewritten, a real registry-normalisation bug found and
fixed via a live word (`blindness`), the `candidate.load` JSON-batch tool designed, built, and
shipped with a real DB-corruption incident found by testing and fully recovered — and then, at the
very end, a **fundamental conceptual error in the candidate-seed's whole departure point**,
identified by the researcher after reviewing the tag-correction proposal this session produced.
**This stream of work (`candidate_seed`/`candidate.load` as currently designed) is closed here, by
the researcher's explicit instruction, to be restarted on a different method.**

**Outcome:** ✅ `iba/config/README.md` rewritten (was stale since 07-15, didn't match the
process/utility/wide restructure). ✅ `AskUserQuestion` permanently banned project-wide
(`.claude/settings.json` deny rule + `CLAUDE.md` + `docs/interaction-preferences.md` + memory) after
a third violation lost an answer entirely. ✅ `GOVERNANCE.md`/`BUILD.md` restructured and brought
current (were stale on real points: the "facts vs rules" boundary, the new-word approval mechanism).
✅ `USER-GUIDE.md` — found to have **zero** documentation for anything built since 07-18 (config
maintenance, candidate curation, quality checks, reports, retention) — fully rewritten. ✅
`lib/words.py:normalise()` bug fixed (a real qualifier like `blindness (spiritual)` was silently
truncated). ✅ `candidate.load` built: JSON-batch create/update/validate for `candidate_seed`, new
`sense_seq`/`step_status`/`ib_referent_type` schema, `lib/dbsnapshot.py` (the pre-run rollback
mechanism this app never had) built in direct response to a real incident found while testing.
**❌ Then closed**, per the researcher: the whole `candidate_seed` substrate — including
everything built for it today — starts from the wrong place. See §5.

---

## 1. Config-seed README + AskUserQuestion ban

- `iba/config/README.md` documented a flat file layout (`enums.json`, `dimensions.json`, ...) that
  no longer existed after the 07-16 `process/utility/wide` restructure — rewritten to match the
  live layout and to state plainly that this is the **designed, not-yet-loadable** configurator
  (distinct from the app's actual lightweight `cfg_*` runtime config), pointing to
  `iba/app/USER-GUIDE.md` as the real entry point.
- Asked to check the IBA session-startup routine: found no hooks, nothing auto-runs
  `Start-Iba.ps1`. Added a `CLAUDE.md` banner instructing it, and wired `init.py` to print a
  `BUILD.md`/`GOVERNANCE.md` orientation line on every startup.
- `AskUserQuestion` fired repeatedly this session despite two prior "hard stop" memory entries
  (2026-06-01, 2026-06-15) — and on one call, the researcher's typed answer never reached me at
  all, only a bare rejection. **Blocked at the config level**: `.claude/settings.json`
  `permissions.deny`, a `CLAUDE.md` top banner, a dedicated section in
  `docs/interaction-preferences.md`, and `feedback_review_via_files_not_chat.md` promoted to `★★`
  in `MEMORY.md`. This is now a technical block, not a reminder.

## 2. GOVERNANCE.md / BUILD.md / USER-GUIDE.md — all found stale, all rewritten

- `GOVERNANCE.md`: restructured (standing overview §1–§8, dated history §9A onward). Two real
  drifts corrected by checking live code, not the old prose: book order and `step.span_html` were
  claimed to be "facts, stay in code" — both are `cfg_*` rows now; the new-word approval was
  claimed "stubbed to auto-approve" — it's a real, live escalation.
- `BUILD.md`: added §3A (step tables for all 6 work packages built since the raw slice — only
  `new-word` had one), corrected §7 (base layer — candidate + passage — is built, not out of
  scope), brought the file list current.
- `USER-GUIDE.md`: found to have **zero** mention of `Config-Maintenance.ps1`, `Candidate-
  Curate.ps1` (either mode), `Candidate-Quality.ps1`, `Passage-Quality.ps1`, `Reports.ps1`,
  `Export-Tables.ps1`, or `Log-Retention.ps1` — the entire operational surface built since 07-18.
  Rewritten with a section per work package.

## 3. `lib/words.py:normalise()` — a real registry bug, found via a live word

Registering `blindness` surfaced a stale malformed row (`blindness (spiritual`, missing its
closing paren) from the legacy-registry migration. Root cause: `normalise()` stripped **any**
trailing non-letter run unconditionally, including a closing bracket that legitimately paired with
an opening one earlier in the word — so `blindness (spiritual)` would always lose its `)` on
re-entry too, not just once. Fixed: only strip trailing junk that doesn't leave an unmatched
opening bracket behind. Malformed row purged (dry-run then `--yes`), `blindness` re-registered
clean, paused correctly for approval (a real word decision, left for the researcher).

## 4. `candidate.load` — built, a real incident, fully recovered, then closed (see §5)

Escalation `#222`'s backlog led to an approved plan (`melodic-foraging-bunny`) for a JSON-batch
`candidate_seed` create/update/validate tool. Built: `handlers/candidate.py:load()`, new
`sense_seq`/`step_status`/`ib_referent_type` columns, `Candidate-Curate.ps1 -Mode Load`.

**Incident, found by testing before it could do more damage:** the shipped
`candidate.transliteration_pattern` default matched almost any clean single-word tag (`hearing`,
`heart`, `spirit`, ...) — running the empty-input revalidation pass once wrote
`decision='exception'` over **1029 of 1806** rows. **No rollback mechanism existed for `iba.db` at
all** — recovered via a same-morning `Export-Tables.ps1` CSV export, matched by stable row `id`
(1028/1029 exact; 1 by code-path reasoning). Two more real bugs found by then testing a small
batch before re-running against the full seed: unbounded substring matching (a gloss of `'I'`
matched inside `hearing`; a gloss of `'word'` matched inside a nonsense test string), and the
duplicate-check path mutating the pre-existing legitimate row instead of leaving it untouched. All
three fixed and verified; `lib/dbsnapshot.py` built in direct response (every new run now
snapshots `iba.db` first, pruned to the last 20 — the rollback point this app should have had "from
the word go," the researcher's words). Full account: `GOVERNANCE.md` §12.

Asked to propose clean tags for the resulting 244 genuinely-messy pre-existing rows (reading each
one's own captured `strong_sense`/`strong_meaning_tree` data — no guessing), I produced
`candidate-tag-corrections-v1-20260722.md`. **Reviewing that file is what surfaced the conceptual
error below.**

## 5. ★ CLOSED — the candidate-seed's departure point is wrong, and has been for days

**The researcher's correction, verbatim in substance:** the tag-correction proposal — and
everything under it (`candidate_seed`, `lemma_inventory`, `candidate.load`, `candidate.seed`,
`cfg_candidate_rule`) — treats **a Strong's/Hebrew-Greek lemma** as the primary unit: start from
`lemma_inventory` (already a Hebrew/Greek root list), decide per-lemma whether it's IB-relevant,
attach an English tag as a label on top. **That is backwards from the actual aim: a list of ALL
the words in the English dictionary that could possibly relate to the inner being.** English
vocabulary is the departure point; Strong's/Hebrew/Greek mapping is a *downstream* step applied
**after** an English word is already judged IB-relevant, not the anchor the whole seed is built on.

**This is not a mistake introduced today.** `lemma_inventory.lemma_key` and `candidate_seed.
lemma_key` are Strong's-keyed by schema, and every seed-building method used across the prior
sessions (`feedback_candidate_seed_independent_over_inclusive_control`, `project_candidate_
characteristic_seed_and_role_model` — both from 2026-07-07 through 07-19) already built the seed
as "an over-inclusive meaning net over lemma_inventory" — i.e. Hebrew/Greek-root-first. Today's
`candidate.load` faithfully extended that same pre-existing architecture; building a tool whose
whole job is "take an English word and resolve it to a lemma" is what finally made the mismatch
concrete and undeniable, rather than introducing a new one. The researcher's own words: **"I have
now gone around this block for days on end."**

**Consequence, per the researcher's explicit instruction:**
1. This stream of work — `candidate_seed`, `candidate.load`, `cfg_candidate_rule`'s accept/reject/
   synonym mechanism, the tag-correction proposal — is **closed**, not to be continued or
   incrementally repaired.
2. A **different method** is needed for arriving at the IB-relevant word list, departing from the
   **English dictionary**, not from `lemma_inventory`/Strong's. What that method is has not yet
   been designed — this log records the closure and the reason, not a replacement plan.
3. The researcher is clearing memory of this framing so it does not keep recurring across
   sessions — this file, and `BUILD.md`/`GOVERNANCE.md`'s existing `candidate_seed` sections, are
   the durable record of what was built and why it's now closed, kept for provenance even though
   the memory entries describing the old departure point are being retired.

**Filed artifacts from this stream, kept for reference, not for continuation:**
`iba/app/reports/candidate-tag-corrections-v1-20260722.md` (the proposal that surfaced this),
`iba/app/reports/candidate-load.md`, `iba/docs` plan `melodic-foraging-bunny` (the approved design
now superseded), `GOVERNANCE.md` §12 (the build + incident account).

---

## What's next

Not decided in this session — the researcher will set the new method's starting point (English
vocabulary first) in a future session, unencumbered by the old lemma-first framing this log
retires.
