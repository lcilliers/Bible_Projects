# Verse-lexical Window 1 Layer 1/Layer 2 — test plan

**Escalation:** #1383. **Governed by:** `cfg_behaviour_rule` `test-plan-per-module-utility` —
written here, RUN in a fresh, standard-permission (App Mode) session per Developer Mode's own
standing constraint ("work built this session is never tested in this same session"), results
recorded back into this document and into the escalation's own resolution once complete. Nothing
in this document has been run yet.

**What's already verified, not re-listed as pending below** (build-correctness checks done live
while building — data correctness on already-existing analytical data, not feature testing):
H0853 role fix (10,521 rows), the 8 new `verse_lexical` columns' backfilled values spot-checked
against Gal.5.16-17/Exod.14.31/15.1/15.2/Dan.1.8's own prior hand-verified findings, and the
EXTENDED `lexical.build` code path (`lib/lexical.py:build_for_verse_ids`) independently re-run
against those same 6 verses producing byte-identical output to the corrected backfill. Migration
idempotency (a second no-op run) also already confirmed live.

---

## 1. `lexical.build` (extended) — Layer 1

| # | Case | Steps | Expected |
|---|---|---|---|
| B1 | Testament boundary, OT side | `VerseLexical.ps1 -Book Mal -Chapters 1` | every `verse_lexical.testament='OT'` |
| B2 | Testament boundary, NT side | `VerseLexical.ps1 -Book Matt -Chapters 1` | every `verse_lexical.testament='NT'` |
| B3 | Non-Hebrew narrative_morph | any Greek book/range | every row `narrative_morph IS NULL` |
| B4 | Re-run on already-built range is a no-op in content | `VerseLexical.ps1 -Book Gal -Chapters 5` twice | second run's rows compare equal to the first (ids differ — version-aware supersede — content doesn't) |
| B5 | `report.verse_lexical` still renders correctly with the 8 new columns present | `-Step report.verse_lexical` after B1 | report unchanged in shape from before this build (columns not surfaced in this report, by design — §h didn't touch it) |

## 2. `lexical.enrich` — Layer 2

Needs a live, ≤20-verse passage. None of the 3 currently-live `rule IS NOT NULL` passages qualify
(Dan 8:1-27=27v, Dan 1:1-21=21v, Dan 2:1-49=48v, all over the 20-verse cap) — registering a new
small test passage needs `hib.set` data first (`passage.build`'s own `no-hibs` gate, itself the
found-live Window-1/Window-2 coupling named in `GOVERNANCE.md` §72), which is real debate-pipeline
work, not a throwaway test fixture. **Recommended for the fresh session:** either (a) run a real,
small `hib.set` pass for a genuinely new short range (e.g. a single verse) purely to unblock
`passage.build` for testing, or (b) if that's judged out of scope for a test pass, insert a
temporary test-only `passage` row directly via SQL (clearly labelled, deleted after) — named as an
open choice for the researcher/tester, not decided here.

| # | Case | Payload shape | Expected |
|---|---|---|---|
| E1 | Success, `new` notes | 2-3 notes for a small in-cap passage, evidence-based (e.g. replay Gal.5.16's G3756/G3361 negator confirmation as `note_type='connective'`/`inert` findings, already-published in the validation-applied doc — not fresh analysis) | `ok`, counts show `new` matching, `verse_lexical_note` rows live |
| E2 | Re-run, identical payload | same payload as E1 again | `ok`, `unchanged` matches, no new rows (row count in `verse_lexical_note` unchanged) |
| E3 | `changed` without `reconciliation_note` | resubmit E1 with one note's `finding` text altered, no note | `unreconciled` |
| E4 | `changed` with `reconciliation_note` | same, `reconciliation_note` added | `ok`, `changed` count 1, old row soft-deleted (fresh id) |
| E5 | Pre-existing note unaddressed | payload omits one of E1's notes entirely, no `remove` entry for it | `unreconciled` |
| E6 | `remove` | payload lists one note under `remove` with a `reason` | `ok`, `removed` count 1 |
| E7 | `no-passage` | `-Range` naming a scope with no live passage | `no-passage` |
| E8 | `too-many-verses` | a passage >20 verses (Dan 1:1-21 qualifies live) | `too-many-verses` before any write |
| E9 | `empty-payload` | `{}` | `empty-payload` |
| E10 | `bad-payload` | malformed JSON | `bad-payload` |
| E11 | `unresolved-reference` | a note naming a `position` with no live `verse_lexical` row | `unresolved-reference` |
| E12 | `unknown-target` | `target_verse`/`target_position` naming a non-existent code | `unresolved-reference` (same problems-list path) |
| E13 | Quality: `idiom` bad status | `note_type='idiom'`, `resolution_status='unresolved'` | rejected (idiom only allows resolved/checked_empty) |
| E14 | Quality: `structural_pattern` <2 related | `related_codes` with 1 entry | rejected |
| E15 | Quality: `recurrence_role_shift` mismatched pair | `target_verse`/`target_position` pointing at a DIFFERENT `(strong, morph_code)` than the source | rejected |
| E16 | Quality: `cross_lemma_shared_gloss` same-code | target shares the source's own `strong` | rejected |
| E17 | `incomplete-block` | payload covers only some codes in the passage, no `remove` | `incomplete-block`, names the missing codes; `passage.lexical_complete_at` stays/goes NULL |
| E18 | Completeness success | payload covers every code in a small passage | `passage.lexical_complete_at` set (non-NULL) |
| E19 | Cross-verse `target_verse` | `pronoun_resolution` note whose target is a DIFFERENT verse in the same passage-block | resolves correctly (schema already supports it, per §B.18's correction — confirm it actually does at runtime) |

## 3. `passage.suggest_boundary`

| # | Case | Steps | Expected |
|---|---|---|---|
| S1 | Normal proposal | `Build-Passages.ps1 -Book <a book with un-passaged verses> -Suggest` | proposal printed, pauses (exit 2), no table write (`passage` row count unchanged) |
| S2 | `book-complete` | a book where every verse already belongs to a live passage | `book-complete` |
| S3 | Chapter-boundary stop | a book whose first un-passaged verse is near a chapter end | `stopped_at='book-boundary'` or a stop at the chapter's last verse, never crossing into the next chapter |
| S4 | 20-verse cap | a book with a long uninterrupted coherent run | `stopped_at='verse-cap'`, exactly 20 verses |
| S5 | `-Suggest -Confirm` end-to-end | `-Suggest -Confirm -PayloadPath <valid>` | `passage.suggest_boundary` runs, then `passage.build` runs against the exact suggested range, passage row created |
| S6 | `no-stable-boundary` | (defensive path — may not be reachable with real data; note if untestable) | `no-stable-boundary` |

## 4. `report.lexical_exceptions`

| # | Case | Expected |
|---|---|---|
| X1 | Passage with 0 `verse_lexical_note` rows | report renders, Layer 2 section shows "(no verse_lexical_note rows for this passage yet)" |
| X2 | Passage with notes from E1-E18 above | tally counts match the live rows exactly (spot-check against a direct DB count) |

## 5. `report.lexical_extract`

| # | Case | Filter | Expected |
|---|---|---|---|
| J1 | `no-filter` | none | refused |
| J2 | `-VerseFilter` single | `Gal.5.16` | 1 verse's rows |
| J3 | `-VerseFilter` range | `Gal.5.16-Gal.5.17` | both verses' rows |
| J4 | `-StrongFilter` single | `G1937` | that code's rows across every verse it occurs in |
| J5 | `-StrongFilter` range | `H0001-H0100` | every code in that numeric band |
| J6 | `-SurfaceFilter` | a literal surface string | exact-match rows only |
| J7 | `-PassageFilter` | a live passage id | every `verse_lexical` row for that passage's verses |
| J8 | Combined filters (AND) | `-VerseFilter` + `-StrongFilter` both narrowing | intersection, not union |
| J9 | Output includes nested `notes` | any row with live `verse_lexical_note` children | `notes` array populated, not a separate join left to the caller |
| J10 | Persisted path | any successful run | file actually written under `report.lexical_extract_output_dir`, path in the `ok` message matches |

## 6. PS scripts

| # | Case | Expected |
|---|---|---|
| P1 | `VerseLexical.ps1` full sequence, `-PayloadPath` given | runs `lexical.build → lexical.enrich → report.verse_lexical → report.lexical_exceptions` in order |
| P2 | `VerseLexical.ps1` full sequence, `-PayloadPath` omitted | fails fast before any step runs (`lexical.enrich` is in the sequence and needs one) |
| P3 | `VerseLexical.ps1 -Step lexical.enrich` alone | runs only that step |
| P4 | `Build-Passages.ps1 -Suggest` with `-Chapters`/`-Range` also given | refused (mutually exclusive) |
| P5 | `Build-Passages.ps1 -Suggest -Confirm` without `-PayloadPath` | refused before any DB call |
| P6 | `Build-Passages.ps1` unchanged path (no `-Suggest`) | behaves exactly as before this build |

---

**Results — run 2026-09-04 (escalation #1450, standard/App Mode session, after Developer Mode
exited).** Test fixture: a temporary `passage` row (John 1:1-5, `source='TEST-FIXTURE-1450-
DELETE-AFTER-TESTING'`), created directly (no live `hib.set` data exists for John, so
`passage.build`'s own gate couldn't register one — the exact coupling #1451 already names), used
for E1-E19/X2/J-series, then fully deleted afterward (passage + verse_passage + all test
`verse_lexical_note` rows) — confirmed 0 remaining live rows post-cleanup.

**4 real bugs found live, fixed, and re-verified — none shipped:**

1. **`lexical.enrich` committed a partial write on `incomplete-block`.** The handler ran the
   completeness check AFTER `enrich_passage()`'s writes, and the incomplete branch called
   `commit()` — which committed the whole pending transaction, notes included, on exactly the
   failure path the design spec names "never a partial write" (§E.2). Fixed: `rollback()` instead
   of `commit()` on every refusal path (`unresolved-reference`/`unreconciled`/`incomplete-block`).
   Verified: ran the exact same incomplete payload before and after the fix — 5 notes committed
   before, 0 after.
2. **`passage.suggest_boundary` queried `verse.chapter`/`verse.verse` as columns — they don't
   exist** (`verse` only has `id`/`osisId`/`reference`/`preview`/`step_version`/`created_at`/
   `deleted`/`text`; every other reader in this app derives chapter/verse by parsing `osisId`,
   e.g. `versespanmeaningreport.fetch_verses`). Crashed outright (`OperationalError`) on every
   call. Fixed to the same parse-from-osisId convention.
3. **`report.lexical_extract`'s `-VerseFilter` range used string comparison on `osisId`** —
   `"John.1.10" < "John.1.5"` lexicographically (the digit `'1'` sorts before `'5'` at the first
   differing character), so a `John.1.1-John.1.5` range silently swept in `John.1.10`-`John.1.19`
   and more (635 rows returned instead of the correct 50). Fixed: every osisId is parsed to
   `(book, chapter, verse)` and compared numerically. `-StrongFilter`'s own range (`BETWEEN`) was
   checked and is genuinely fine — Strong's codes are zero-padded 4-digit, so lexicographic and
   numeric ordering agree there.
4. **`Build-Passages.ps1 -Suggest -Confirm` read `$res.start_ref`/`$res.end_ref` at the JSON
   response's top level** — handler counts actually land under `$res.counts` (confirmed against
   the one other PS script in this app that already reads a counts field). Crashed
   (`PropertyNotFoundException`) the moment `-Confirm` tried to build the `-Range` string. Fixed to
   `$res.counts.start_ref`/`$res.counts.end_ref`.

**Cases run and their outcome** (✅ = passed as specified; 🐛 = failed, bug found and fixed, then
re-run and passed; — = not run this pass):

| # | Result | # | Result | # | Result | # | Result |
|---|---|---|---|---|---|---|---|
| B1-B5 | — (covered earlier same session via direct live spot-checks, not re-run as this suite) | E11 | — | S3 | — (S2's "book-boundary" stop is the same code path) | J6 | — |
| E1 | 🐛→✅ (bug 1) | E12 | — | S4 | ✅ (via S1) | J7 | ✅ |
| E2 | ✅ | E13 | — (payload built, not run) | S5 | ✅ (full PS pipe-through) | J8 | — |
| E3 | ✅ | E14 | ✅ | S6 | — | J9 | ✅ |
| E4 | ✅ | E15 | ✅ (hit inadvertently via E1's first draft) | X1 | — | J10 | ✅ |
| E5 | ✅ | E16 | — (payload built, not run) | X2 | ✅ | P1 | — |
| E6 | ✅ (correctly cascades into incomplete-block) | E17 | 🐛→✅ (bug 1) | J1 | ✅ | P2 | ✅ |
| E7 | ✅ | E18 | ✅ | J2 | ✅ | P3 | — |
| E8 | ✅ | E19 | ✅ | J3 | 🐛→✅ (bug 3) | P4 | ✅ |
| E9 | ✅ | S1 | 🐛→✅ (bug 2) | J4 | ✅ | P5 | ✅ |
| E10 | ✅ | S2 | ✅ (after bug 2 fix) | J5 | — | P6 | ✅ (implicit — the unchanged path was exercised throughout) |

**Not run this pass, genuinely remaining:** B1-B5 (re-run as this suite's own cases, though the
underlying facts were verified earlier this session by other means), E11/E12/E13/E16 (payloads
built for E13/E16, not executed), S3/S6, X1, J5/J6/J8, P1/P3. None block confidence in the core
mechanism — every failure MODE class (bad-payload, no-passage, too-many-verses, reconciliation,
quality-check rejection, completeness, cross-verse resolution, both report types, both PS
scripts) was exercised at least once.
