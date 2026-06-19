# Obslog — Tier Catalogue Rewrite (full T0–T7) — v1 — 2026-06-19

**Reference:** tier-rewrite · **Session topic:** tier-rewrite · **Started:** 2026-06-19

## Governing decisions (researcher, this session)

**Source confirmed authoritative:** `WA-tier-catalogue-current-state-v1-20260617.md` — 173 active questions, T0–T7.

**Researcher convention answers (2026-06-19):**
- **Q-a — Freed slots:** mark obsolete so CC can soft-delete (`deleted=1`). NOT repurposed, NOT retained-live. This overturns the `′`-repurpose and "code retained" approach used in the attached draft `WA-tier-catalogue-rewrite-v1_0-2026-06-18.md` (T0–T2).
- **Q-b — [V]/[S] tags:** strip. Every rewritten question is a synthesis of verse data; lexical vs read-synthesis source varies but is not tagged at question level.
- **Q-c — Consolidation level:** remove bias and repetition; lose no aspect to consider. Expect level-3 (`.1/.2/.3`) questions to SURVIVE where each asks something genuinely distinct; fold only true redundancy (the explicit "note silence" rows; exact-duplicate reveals; the six identical T2 location-level grids).

**Internal consistency:** researcher confirmed (2026-06-19) the full T0–T7 must be re-issued under ONE convention set. The attached T0–T2 draft (retain/`′`) is superseded by this build.

**Output purpose:** a document CC can use to update the database. Each original code carries an explicit disposition: `keep` (with rewritten text) or `obsolete` (folded into a primary, soft-delete). Where folded, the primary names the absorbed codes so no aspect is lost. The actual JSON patch is CC's to build (two-AI split, GR-PROG-005); this document is the analytical/decision source.

## De-biasing rules applied (carried from attached draft, retained)
- Ask what the evidence shows / which items are present and how they behave — never "does it have property P?" or "what does it reveal about Y?" framed to expect a yes.
- Remove expected-answer verbs: equip, receive, give, enable/deepen/bypass/impair.
- Silence is first-class: every kept question can record absence, so dedicated "note silence explicitly" rows become obsolete.

## Disposition model for CC
- **keep** — code remains active (`deleted=0`); question_text updated to rewritten form.
- **obsolete** — code folded into a named primary (`deleted=1`); its distinct content is named in the primary's `absorbs:` line so scope is preserved and the merge is reversible.

## Build complete — v2_0 produced

**Output:** wa-tier-catalogue-rewrite-v2_0-20260619.md (dual-written: /home/claude/work + /mnt/user-data/outputs).
**Disposition counts (verified by per-tier enumeration):** 173 → keep 126, obsolete 47.
Per-tier: T0 9/3 · T1 18/2 · T2 6/22 · T3 33/0 · T4 18/6 · T5 9/9 · T6 13/5 · T7 20/0.

**Self-audit note:** first draft of the disposition ledger contained two conflicting count tables (T2 stated 7/21 then a restatement gave total 128/45). Caught on review, re-counted from source by enumeration, corrected to single verified ledger 126/47. T2 corrected to keep 6 / obsolete 22 (T2.1.1 and T2.1.2 kept-and-repurposed; all other location-grid codes obsolete).

**Decisions recorded for researcher visibility:**
- T1.3.2 and T1.3.3 KEPT as distinct (excludes/resists vs where-it-ends) rather than folded — judged genuinely distinct under Q-c "lose no aspect". Flag for researcher: this is an authorship call; if a tighter T1.3 single-question is preferred, say so.
- T3 retains all 33 codes (no silence rows existed to retire); the .2 effect-question de-biased by removing enable/deepen/bypass/impair.
- T2.9.1 carries the [proposed: from other spirits] origin option already present in the v1_0 draft — left as proposed, not confirmed.

**Open for researcher before CC patch:** confirm the keep/obsolete ledger is the intended DB action set; confirm T1.3 granularity; then CC builds the JSON patch (text-update for keep, deleted=1 for obsolete).

## Researcher instruction (verbatim, 2026-06-19)

"T2.9.1 was added as a question as the original questions silently ignored other spirits, which it should not. Can you ensure that this aspect is included in the questions."

## Interpretation + scope decision

The "other spirits" aspect (influence/origin/operation of non-divine, non-human spiritual beings — adversarial or angelic — on the inner being) was a known gap: the original 173-question catalogue only surfaced it at T4.6 (Spiritual Beings Interface) and was retro-patched into T2.9.1 (origin). The researcher wants the aspect carried wherever it legitimately bears, not isolated.

Discipline check (GR-PROG-001 verse-first; do not invent): the aspect must be ADDED as a possibility the question can record, NOT asserted as present. Each touch must keep silence first-class ("or record none / not stated"). I must not imply other-spirit involvement is expected — that would re-introduce bias, the very thing the rewrite removes.

Where it legitimately bears (proposing — for researcher confirmation, not assuming):
- T2.9.1 origin — ALREADY carries [proposed: from other spirits]. Promote from [proposed] to a settled option per this instruction.
- T2.10.1 constitutional movement — "onto the person from outside" should explicitly name other spirits as one possible external source of movement onto/within the inner being.
- T1.7.2 conditions under which the characteristic is blocked/distorted — distortion by an external spirit is a recognised mode; name it as one possible source without asserting it.
- T0.1.1 / T0.4 — God-relation and typology: NOT other-spirits scope. Leave.
- T3 faculties — the faculty triads ask what the CHARACTERISTIC does to the faculty; adversarial action on a faculty is really T4.6 territory. Do NOT bloat every T3 triad. Leave T3 to its own scope.
- T4.6 Spiritual Beings Interface — already the dedicated home; de-biased wording already records absence. Confirm it remains the primary locus.
- T5/T6 — formation and inter-characteristic structure: other-spirits is not a native axis there. Leave.

Net proposed edits: T2.9.1 (promote), T2.10.1 (name external-spirit source), T1.7.2 (name external-spirit distortion). Minimal, targeted, silence-preserving. Flag T4.6 as the existing primary home.

## Three edits applied + CC update document produced

**Edits to catalogue (now v2_1):**
- T2.9.1 — other-spirit origin promoted from [proposed] to settled option ("introduced by another spirit (angelic or adversarial)").
- T2.10.1 — external spirit named as a possible source of movement onto the person.
- T1.7.2 — distortion/interference by another spirit named as a possible blocking condition.
All three keep silence first-class (recordable, not expected). T4.6 unchanged (remains dedicated home). No disposition changed.

**Catalogue renamed:** wa-tier-catalogue-rewrite-v2_1-20260619.md (supersedes v2_0; stale v2_0 removed from outputs).

**CC update document produced:** wa-tier-catalogue-cc-update-v1_0-20260619.md.
- Operation A: 126 TEXT-UPDATE (keep codes, full rewritten question_text quoted).
- Operation B: 47 SOFT-DELETE (deleted=1, each with → primary fold target and reason).
- Verified by script: 126 + 47 = 173, zero overlap between keep and obsolete sets.
- Post-run verification steps for CC included. Per GR-PROG-005/GR-PROC-004, CC builds the JSON patch from this and presents for researcher review.

**All three files dual-written** (/home/claude/work + /mnt/user-data/outputs).

**Outstanding for researcher:** (a) confirm the operation set is the intended DB action; (b) the T1.3.2/T1.3.3 granularity call still stands open from prior turn (kept distinct, not folded). Then CC proceeds to patch build.
