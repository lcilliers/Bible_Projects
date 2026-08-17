# SESSION LOG — 2026-08-10 — `Incurability` repurposed to `Suffering`; `receive` created then fully rolled back on a relevance judgement call; a real corpus-wide span-parsing bug found (and, mid-session, un-fixed again by the rollback)

Researcher's own framing at close (paraphrased across the session): the `receive` build "created
chaos" and was done "without visibility of the impact" — procedural governance (write-grants,
`configmaint.propose` approval gates) was followed throughout, but the study's own substantive
test — is this Strong's/verse relevant to the **inner being** — was skipped, and STEP's raw
discovery was allowed to run unchecked. The session closed on a full DB rollback plus a mandate to
plan (not yet build) three follow-on fixes.

## What happened, in sequence

1. **`iba/app` bootstrapped clean** (`Start-Iba.ps1`) — config/DB/STEP all green.

2. **Investigated why `word_registry` id 177 ("Incurability") had 7 Strong's with no visible
   relation to the word.** Traced the origin precisely: the word itself is a legacy "verse-fanout
   orphan" from the main project (id 218 there), curated there to exactly ONE Strong's (`H0605`,
   *anash*, "be incurable" — `H0582` "enosh"/man explicitly excluded as non-target, researcher's
   own 2026-06-29 note). But in THIS app, `run` row `RUN-20260718_153954-NEW-WORD` shows the word
   was onboarded via `raw.discover` -> `Step.call1_meanings("Incurability")` — STEP's own bare
   English-string search — which returned 7 codes, 4 genuinely on-topic and 3 false positives
   (`G2983` *lambanō* "to take", `H2470I` *chalah* "be weak/grieved", `H5375J` *nasa* "to
   lift/bear") picked up only because one ESV verse span each happens to render with the English
   word "incur" ("will incur judgment", "lest you incur sin"), unrelated to the term's actual
   meaning. Read-only — no changes.

3. **Researcher instruction: repurpose the word.** Rename id 177 `Incurability` -> `Suffering`,
   with the researcher's own curated Hebrew list (`tsa.rah`/distress 70x, `o.ni`/affliction 36x,
   `qa.shah`/harden 28x, `makh.ov`/pain 16x, `ke.ev`/pain 6x, `ma.cha.luy`/suffering 1x [flagged —
   `strong.count`=4, 0 `strong_verse` rows, unambiguous by translit+gloss though], `e.nut`/
   affliction 1x, `ats.tse.vet`/injury 5x). Renaming needed a NEW `cfg_write_grant`
   (`migration` -> `word_registry`) — proposed via `configmaint.propose`, researcher-approved
   (`RUN-20260810_153409_045-CONFIGMAINT`), applied. `migration/repurpose_incurability_to_
   suffering_20260810.py` — retired the 7 old links, added the 8 new. **BUILD.md §94.**

4. **Correction, same session:** "the strong links of the old ones must be retained and the 8 new
   ones added" — the first pass had wrongly retired the 7 legacy links instead of keeping them
   alongside the new 8. `migration/restore_incurability_legacy_word_strong_20260810.py` restored
   all 7 to active; final state 15 active `word_strong` under `Suffering`. **BUILD.md §95.**

5. **`Suffering`'s raw layer completed** — `raw.detail`/`raw.verses` run directly against the
   existing word (skipping `registry.create`/`raw.discover` since strongs were already set by
   migration); pulled `H4251`'s one missing `strong_verse` row; `raw.write`/`raw.validate` both
   clean. `verse_lexical` checked across all 448 distinct verses the 15 strongs touch — already
   100% covered by a prior whole-Bible build, nothing to run. **BUILD.md §96.**

6. **Instructed: add a new word `receive`, move `G2983` to it, pull all related strongs.**
   `New-Word.ps1` proposed/approved/resumed normally — `raw.discover` seeded 64 strongs (STEP
   `masterSearch(meanings="receive")`; `G2983` was already one of them, discovered on its real
   meaning this time). `raw.verses` -> **`raw.validate` FAILED**: `G2192:2 missed`.

7. **Root-caused, not worked around: `step.span_html` regex bug.** STEP sometimes emits a content
   `<span strong='...'>` tag with NO `morph=` attribute at all (confirmed live, e.g. John 4:18's
   `G2192` "have") — the regex required `morph=` unconditionally, so these tags were silently
   dropped from `span` entirely, even though `strong_verse` correctly asserts the occurrence via a
   separate STEP call. Scanned the WHOLE DB: **824 verses / 1,077 spans / 24 Strong's codes**
   affected project-wide, not scoped to `receive`. Fixed via `configmaint.propose` (researcher-
   approved, `RUN-20260810_160133_776-CONFIGMAINT`): morph made optional in the regex, tested
   (John 4:18: 13 -> 16 tags recovered, zero regressions). A second bug found building the backfill:
   `span` carries an UNCONDITIONAL `UNIQUE(verse_id, position)` table constraint (not just the
   partial live-only index) — fixed by bumping old rows' position on soft-delete. New `migration`
   -> `span` write grant (researcher-approved, `RUN-20260810_160505_505-CONFIGMAINT`).
   `migration/backfill_morphless_span_fix_20260810.py` — 13,268 old span rows retired, 14,345
   inserted; re-scan clean (0 remaining). `receive` re-validated clean. **BUILD.md §97.**

8. **Instructed: confirm the parse tables were generated for the new strongs.** Answer was
   honestly **no** — `new-word`'s step sequence has no `lexicon.parse`/`lexicon.related` step at
   all (only the book-scoped `raw-backfill` package auto-chains those). Ran `lexicon.parse`
   (full corpus rebuild, deterministic, no network) and a TARGETED `strong_related` fetch (3 new
   codes only, not the wasteful full-corpus version). Checking all 64 `receive` codes (not just the
   3 new) surfaced a SECOND, separate, pre-existing gap — 8 codes with no exact-variant
   `strong_meaning_tree` row of their own (same class already fixed once this session for
   `healing`) — backfilled via `migration/backfill_receive_exact_variant_meaning_20260810.py`,
   reusing that exact mechanism, no new grant. **BUILD.md §98.**

9. **Asked to wire the "complete cycle" into the `new-word` routine itself.** Wrote and unit-tested
   (against `receive`, not yet wired into any `cfg_step`): `lib/lexical.py:build_for_verse_ids()`
   (word-scoped `verse_lexical` rebuild, reusing the existing version-aware `build_for_verse`), and
   `handlers/raw.py:related()`/`lexical()` (new steps, both reusing already-granted writer
   identities — no new grants needed). Full-scale test against `receive`'s 7,336 verses: 261.5s,
   106,162 spans, 157,878 codes resolved, 152,651 superseded (stale entries from earlier in the
   session's own fixes, correctly caught and repaired). **Proposals for wiring these into
   `cfg_step` were drafted but never submitted** — the researcher's next question interrupted
   before they were.

10. **Researcher's challenge: "are you sure... is this 25% of the Bible really relevant?"**
    Broke `receive`'s 64 codes down by verse count: **79% of all 8,266 code-occurrences came from
    just 9 codes** — `bo` ("come," 1,753x), `natan` ("give," 1,187x), `shama` ("hear," 904x),
    `laqach` ("take," 734x), `echō` ("have/be," 615x — the SAME code whose missing spans triggered
    §97's bug discovery), `matsa` ("find," 425x), `didōmi` ("give," 375x), `laleō` ("speak," 265x),
    `lambanō` ("take," 238x) — basic high-frequency action verbs, not terms about receiving as an
    inner-being movement, pulled in only because STEP's bare English search matches "receive"
    against *any* buried sense in a lemma's full dictionary entry.

11. **Researcher's follow-up: is this actually following governance, or off the cuff — this
    "ran completely away."** Honest answer: procedural governance (write-grants,
    `configmaint.propose`, BUILD.md-per-change) was genuinely followed throughout. What was
    skipped was the study's OWN substantive test — inner-being relevance — which has never been an
    automated `cfg_*` gate in this app; it's always been a human curation step (matches the main
    project's own Phase 1 discover -> Phase 2 **decisions** shape, and `Suffering`'s own
    H0605-kept/H0582-excluded precedent, sitting right there in the same session). `raw.discover`'s
    64 raw seeds went straight into `detail`/`verses`/the full lexical build with no pause for
    relevance review.

12. **Instructed: roll back to before this started.** Rather than hand-reverse dozens of writes
    (real "chaos"/uncertain-impact risk in itself), used the app's own per-run pre-write snapshot
    mechanism (`lib/dbsnapshot.py`, found 2026-07-22). Took a safety snapshot of the messy state
    first (`iba-20260810T154548Z-pre-rollback-receive-mess.db` — nothing lost, just out of the live
    DB), then restored `iba.db` from `iba-20260810T145708Z-new-word-run-20260810-155707-659-
    new-wor.db` — the snapshot taken the instant before `receive`'s very first write. Verified
    clean: `receive` (word + 64 links) gone; `Suffering` (steps 3-5 above) fully intact; write
    grants back to pre-`receive` state; **`step.span_html` regex reverted to its UNFIXED state**
    (flagged explicitly — this un-does step 7's genuine, validated, `receive`-independent bug fix
    too, since the snapshot predates it; NOT silently re-broken, the researcher's separate call).
    Code files from steps 7-9 (2 migration scripts, `build_for_verse_ids`, `related()`/`lexical()`)
    left in place, inert — no config drift to undo since the `cfg_step` wiring from step 9 was
    never submitted. **BUILD.md §99.**

13. **Closing investigation (this session's actual end): quantified the span bug's REAL impact,
    not just its scope.** With the bug back (step 12), confirmed the SAME 824/1,077/24 figures as
    step 7 (as expected — the rollback is a pure revert). Found this is not hypothetical: the whole
    Bible already went through a bulk verse-lexical build+report pass on 2026-08-09 — **65
    book-level `.md` reports exist** in `verse-analysis/`, one per book of the Bible. Pulled up Joh
    4:18 directly in the filed `John/john-1-21-verse-lexical-v1-20260809.md`: the reading table
    silently skips exactly the 3 `G2192` rows ("you have had"/"you"/"have"), **no gap marker at
    all** — reads as complete. Since these `.md` files are a pure render of `verse_lexical` (never
    re-derive independently), the DB rows themselves are equally short, not a rendering artifact.
    Roughly 26 of the 65 filed book reports (every NT book + Psalms — the bug is almost entirely
    Greek/NT-concentrated) carry this same silent gap.

## Explicitly not done (queued, not forgotten)

**(a) Re-apply the span-parsing fix and propagate it.** The regex fix + the 824-verse
`migration/backfill_morphless_span_fix_20260810.py` are already written and were already proven
clean (zero regressions) before the rollback un-applied them. Needs: (1) re-propose the
`cfg_setting` change (fresh `configmaint.propose` run, researcher approval — the prior approval's
run is already resolved/superseded by the rollback), (2) re-run the backfill migration, (3) rebuild
`verse_lexical` for the same 824 verses (or their books), (4) **regenerate the ~26 affected filed
book-level verse-lexical reports** so the published record matches the corrected data — this last
step has no existing automation and needs a plan (probably `VerseLexical.ps1` re-run per affected
book).

**(b) Wire the full raw-data cycle into `new-word` (and design a genuine word/strong UPDATE
routine, which doesn't exist yet).** The 3 new steps from step 9 above are written and unit-tested;
just need `cfg_step`/`cfg_on_fail` wiring (5 approval-gated `configmaint.propose` calls, no new
write-grants — all three reuse already-granted writer identities). Separately, and not yet
designed at all: every word/strong-scoped CHANGE this session (`Suffering`'s repurpose, `receive`'s
`G2983` move) was a hand-written one-off migration script, not a routine operation — there is no
registered "update an existing word's strongs" work package the way `new-word` exists for creation.
That needs real design next session, plus a catalogue (via `cfg_report`) of which reports
(`report.word_registry_span`, `report.strong_verse`, `report.registry`, `report.verse_lexical` for
touched books) must be regenerated whenever a word's strongs change — recorded as an actual
`cfg_method_rule`, not just code behavior, per `governance.rules_must_be_config_driven`.

**(c) A config-driven inner-being-relevance gate on `raw.discover`'s output.** Not designed yet.
Leaning (stated to the researcher, not yet decided) toward a genuine approval gate on the
DISCOVERED STRONGS LIST itself (not just the word's existence, which is all `registry.create`
currently gates) — show glosses/counts, require explicit accept/reject per code or as a batch
BEFORE `raw.detail`/`verses` ever run, reusing the escalation mechanism already built. A
frequency-ceiling auto-flag (mirroring the main project's `HIGH_FREQ_THRESHOLD`) could supplement
it as an automatic "needs a closer look" signal, but the actual relevance call stays the
researcher's, matching how this project has always worked (Phase 1 discover -> Phase 2
**decisions**).

## Files touched (not yet committed — see below)

**New:** `iba/app/migration/repurpose_incurability_to_suffering_20260810.py`,
`restore_incurability_legacy_word_strong_20260810.py`,
`backfill_morphless_span_fix_20260810.py`, `move_g2983_suffering_to_receive_20260810.py`,
`backfill_receive_exact_variant_meaning_20260810.py` (all still present on disk — several now
describe DB states that step 12's rollback reverted; kept as historical record of what was found
and done, per the file's own docstring in each case — none should be re-run as-is without fresh
review).

**Modified:** `iba/app/lib/lexical.py` (+`build_for_verse_ids`), `iba/app/handlers/raw.py`
(+`related`, +`lexical`, +`StepUnavailable` import) — both inert, never wired into `cfg_step`.
`iba/app/BUILD.md` (§94-§99).

**DB:** net effect of the whole session, after the step-12 rollback, is exactly `Suffering`'s
repurpose (steps 3-5) — `receive` and the span-regex fix both ended the session reverted to their
pre-session state. Two DB snapshots retained: `iba-20260810T145708Z-new-word-run-20260810-155707-
659-new-wor.db` (the pre-`receive` restore point, now the live state) and `iba-20260810T154548Z-
pre-rollback-receive-mess.db` (everything from `receive` onward, preserved if any of it is wanted
later).

## Next

Pick up the three-part plan above (a/b/c) — the researcher asked for exactly this ordering
(summarise first, log it, THEN build) specifically so a fresh session can start from this file
without re-deriving today's reasoning. Suggest starting with (a) (small, already-built, already-
validated, purely mechanical) before (b)/(c) (real design work).
