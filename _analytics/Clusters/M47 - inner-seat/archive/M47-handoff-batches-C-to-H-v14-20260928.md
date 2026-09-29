# M47 → cluster phenomena — handoff (v14)

**Date:** 2026-09-28 · **Supersedes:** v13 (`archive/`). The v1–v13 history is still valid background and is not repeated here. Read `archive/M47-handoff-batches-C-to-H-v13-20260928.md` only if you need it.
**Session log:** `Logs/SESSION-LOG-20260928-m47-filing-noseat-pilot-m20-phenomena.md`.
**Live tracking:** escalation **#1886**, "M02 Anger & Wrath: phenomenon-level reading" (raised, assigned to Claude, decision required).

## Where things stand

- **M20 is complete and approved.** Escalation #1885 was approved 2026-09-28 (v6). The finished reading is `../M20 - doubt-discouragement/wa-cluster-M20-phenomena-v3-20260928.md` (commit `906b25f7`). v2 is in that folder's `archive/`, and the ledger is `wa-cluster-M20-phenomena-ledger-v1-20260928.csv`.
- **#1885's approval comment reads "completed M20 and M02", but M02 had not been done.** The researcher then ruled, verbatim: **"2 — raise a new escalation for M02"**. That is #1886.
- **A parallel session also worked on #1885.** Its v4 comment (14:18) was written by another Claude session. The researcher stopped it with "claude AI already completed this". **Before starting, check that no other session is working on #1886** (`Escalation.ps1 -Action History -Id 1886`).

## NEXT STEP — M02 unit 1: human anger's phenomena

**M02 Anger & Wrath has 681 verses:** 66 carry an M47 seat word, and 615 do not. The plan, proposed in #1885 and M20 v3 §19, and recorded in #1886:

1. **Unit 1: human anger's phenomena.** This session.
2. **Unit 2: divine anger as borne by the human.** Only after the researcher has reviewed unit 1.

**Unit 1 needs:**

1. **A split of the 681 verses into human-subject and divine-subject anger,** made from the verses, not from a Strong's list. The split itself is a judgement.
   - Record every verse's side in the ledger.
   - Put the borderline cases in their own list, for example: a human speaking of God's anger; God's anger carried out by a human agent; "the anger of the Lord was kindled against Moses". **Don't decide them silently.**
   - Report the count on each side before reading unit 1 in full, so that the researcher can check the unit's size.
2. **Read the human-subject verses in canonical order, and let the phenomena emerge** as M20 v3 did. For each phenomenon:
   - answer the five questions: what it is, what it does, where it comes from, how it co-exists, what it leads to
   - add a **Seat block** in the M20 v3 form: whose seat (the bearer's own, the other party's, the offender's, or none); the seat-sense check (genuine, life-sense, or spurious); and where the seat arrives in the next verse or the passage
   - **cite, don't redo, the M47 reading** (see Inputs)
3. **Account for every verse in a ledger CSV,** using the M20 ledger's columns plus a `side` column (human / divine / borderline): `n, reference, m02_words, seat_word_in_verse, side, phenomenon, text`.
4. **Read the context verses yourself before quoting them.** M20 v3 §21 had to be closed afterwards because the DB reader was blocked. Don't leave context seats unread.
5. **Then:** file as `../M02 - anger-wrath/wa-cluster-M02-phenomena-v1-20260928.md` (dated on the day), plus a ledger. Commit and push. Set #1886 to **ready_for_approval, assigned to Researcher**, with `-AssignedTo Researcher` passed explicitly. **Unit 2 does not start until the researcher has reviewed unit 1.**

## Inputs — cite these, don't redo them

- **The pattern:** `../M20 - doubt-discouragement/wa-cluster-M20-phenomena-v3-20260928.md`. Follow its §0.1 (the seat-sense mapping), its Seat blocks, the §20 seat-sense map and the §21 context-verse table.
- **The M02 no-seat pilot:** `../M02 - anger-wrath/wa-cluster-M02-noseat-observations-v1-20260928.md`, and its verse CSV (615 no-seat verses):
  - §1.1 *thumos* never seated
  - §1.2 *aganakteō* indignation
  - §1.3 the NT anger verbs
  - §1.4 human rage with a bodily face ("face fell", sullen)
  - §1.5 strife words
  - §1.6 smoke, Meribah and single-verse words
  - §2 the implicit-seat words: §2.1 human anger narratives (*aph, charah, chemah, qatsaph*); §2.2 wisdom sayings; §2.3 the human vessel of divine anger
  - §3 the carriers of inner being where there is no seat
- **Batch A v3 §2, "Anger & Wrath (M02)"** (`M47-x-feeling-batchA-v3-20260928.md`). It read the seated M02 verses:
  - §2.1 human anger in the inner seat
  - §2.2 God's anger and the human heart
  - §2.3 ◆ anger, breath and nose (H0639G "face: anger" is correctly dual, M02 + T14)
  - §2.4 ◆ the divine Spirit followed by human anger
  - §2.5 anger and grief together
- **The seated pairs:** `cluster-M47-other-m-code-pairs-with-distance-v2-20260928.csv` (this folder, UTF-8 with BOM), filtered to `other_cluster_code = M02`. That gives 66 verses. Some are also read in other batches: grep the `M47-x-*batch*.md` files for each reference, as was done for M20.
- **Revisit pointers carried forward:**
  - Job 3:10, 3:16, 14:13 and Jon 4 → Batch G v3 §16 (the death side)
  - 1Ki 21:5 and 1Sa 1:15 → Batch F v4

## Rules for the reading (all carried forward)

- **Phenomenon level, emergent.** Phenomena come from the verses, never from a preset list or a tick-box. Every claim is anchored to a verse. Quote a context verse only after reading it. Account for every verse. **Do not brush over detail or make general statements.** (Memory: `feedback_phenomenon_level_emergent_reading`.)
- **Do not use the 12-method table** (`wa-cluster-M47-ib-operation-modes-consideration-v1-20260928.md`) as a checklist.
- **Inner-being definition:** from config: `cfg_prose_concept.inner_being_definition` → prose section 5 ("Defining Inner Being"). The subject is the human inner being (prose sections 1089/1090; `cfg_method_rule` `hib.set`). Where God is the actor, analyse the human side. That is unit 2's whole subject, and it applies to borderline verses in unit 1. `phenomenon.set` hidden-behind-act applies.
- **Revisit as the rule; interaction first** (memories `feedback_revisit_as_rule`, `feedback_interaction_over_reallocation`). If M02 shows something that bears on M20 or the M47 batches, record it in an §R-V section.
- **Filing:** `_analytics/Clusters/{code} - {short name}/`, per `cfg_setting report.cluster_folder_naming_convention` (GOVERNANCE.md §83). Prior versions go in `archive/`. Same base name means a version bump.
- **Data:** read directly from `iba/app/db/iba.db` (read-only): `verse_lexical.role` (a JSON list of cluster codes; a seat is a token whose role has `"M47"`), `verse` (`reference`, `text`), `strong`, `cluster`, `cfg_book_order`. bible_research.db plays no part.
- **Scratch scripts** (recreate in the session scratchpad, `temp_` prefix, not registered):
  - an extract of all M02 verses in canonical order, with their M02 words and seat words
  - a context reader (reference ± n verses from `verse`, canonical order via `cfg_book_order`)
  - a batch reader that takes a list of references and writes a CSV

  Write them as `.py` files and run them with `python <file>`. `Bash(python -c ' *)` was removed from the allow list on 2026-09-28, so inline `python -c` now prompts every time.
- **Cost:** work in units, with a review between them. 681 verses is 2.5 times M20.

## Session notes from 2026-09-28

- **Permission mode:** in auto mode, every shell command failed the server-side safety check with "no verdict", not a refusal. After 10 in a row the turn ended. File tools were unaffected. The researcher switched out of auto mode and the shell worked at once. **If the shell is blocked, say so straight away and give the researcher the query to run** (they can export a CSV from the VS Code SQLite extension), rather than writing around the gap.
- **Uncommitted files left for session close:** `outputs/escalation/escalation-list-v133-20260928.md` (and v132 in `archive/`) and `research/discovery/spine-check-v34-20260928.md` (and v33 in `archive/`), plus `spine-check.md` modified. They come from the project's report scripts, not from this work.

## Other open items (not blocking)

- The loose pre-rule files at the `_analytics/Clusters` root have not been moved into cluster folders.
- #1881 (session.close stale transcript) is still open.
