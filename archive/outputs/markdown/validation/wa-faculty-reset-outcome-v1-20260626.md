# Faculty reset — outcome (verse-grounded, live DB write)

- **File:** wa-faculty-reset-outcome-v1-20260626.md · **2026-06-26 · Author:** Claude Code.
- **What you asked:** faculty must appear on a verse only if explicitly mentioned/inferred ON THE VERSE, never via the lemma — and to proceed with the reset. **Done, live, reversible.**

## 1. What changed
- **Old (invalid) faculty removed:** 29,205 lemma-derived rows (the `faculty-map-v1` + `v2_engine_iter1` data — 100 % per-term constant, the mechanism your rule forbids) **soft-deleted** and snapshotted to table `ve_lexical_faculty_pre_reset_20260626`.
- **New verse-grounded faculty written:** **22,128 rows across 17,161 units**, in two honest tiers:
  - `faculty-verse-explicit-v1-20260626` — **20,636 rows**: a genuine faculty-word (1–3 faculties in the map) is in the verse; carries its own faculty.
  - `faculty-verse-inferred-seat-v1-20260626` — **1,492 rows**: a *seat* (heart/spirit, ≥4-faculty lemma) inherits only the faculties named by faculty-words co-present in the verse. Lower-confidence inference, **independently removable**.

## 2. Method (Variant C — see wa-faculty-reset-dryrun-v1-20260626.md)
- **Faculty-word (1–3 faculties):** carries its own faculty — the word is explicitly in the verse (e.g. *suneidesis*→conscience, *yetser*→volition).
- **Seat (≥4 faculties = the 8 heart/spirit lemmas):** no auto-dump; faculty inferred only from the verse's own faculty-words. Empty if none.
- **Non-faculty term:** empty (the *kol*/*raq* proximity noise of the naive verse-scan is excluded).

## 3. Validation (all pass)
- **Over-fire gone:** faculties-per-unit max 6 → 5; Mat 5:8 *kardia* (was all 6) → **empty**.
- Seats now read the verse: **Gen 6:5** *lev* → cognition/moral_evaluation/volition; **Deu 6:5** *levav* → affect/volition.
- Faculty-words preserved: **Heb 9:14** *suneidesis* → conscience/moral_evaluation.
- 0 orphan rows; integrity intact.

## 4. The one honest limit (your call if it bothers you)
Seat inference is proximity-based, not binding-proven. **Heb 9:14** *pneuma* picks up {conscience, moral_evaluation} from *suneidesis* in the same verse — but there the Spirit acts *on* the conscience, it doesn't operate *in* it. This is the ceiling. It is isolated in the `…-inferred-seat` tier (1,492 rows): I can **demote or delete that whole tier in one command** if you'd rather seats stay empty and defer to the depth pass.

## 5. IMPORTANT follow-up — l2_meaning is now stale on faculty
The `l2_meaning` narrations were generated in the 2026-06-26 corpus sweep **from the old over-fired faculty** ("…engaging the affect, cognition, volition, conscience, perception, moral_evaluation faculty"). The reset's benefit will not show in the narrated meanings until **l2_meaning is regenerated** against the new faculty. Not done here (regeneration is a corpus-wide step and you are mid-decision on the overall approach). Flagged for your go-ahead.

## 6. Reversibility / provenance
- DB backup before write: `backups/bible_research_pre-faculty-reset_20260626.db`.
- Snapshot of old faculty: table `ve_lexical_faculty_pre_reset_20260626` (29,203 rows) + old rows soft-deleted in place (recoverable).
- Scripts: `scripts/_apply_faculty_reset_verse_grounded_v1_20260626.py` (live) · `scripts/_probe_faculty_reset_dryrun_v1_20260626.py` (dry-run/compare).
- Diagnosis: `wa-faculty-state-diagnosis-v1-20260626.md` · Rule in memory: `feedback_faculty_only_if_explicit_or_inferred_on_verse`.
