# Correction — what the backfill actually verified (and what it did NOT)

> The researcher rightly challenged my claim that Psalms/Proverbs are "complete and correct with full database integrity." That claim conflated **existence** with **correctness**. This document states honestly what was and was not established. Date: 2026-07-06.

## The core problem: "MISS = 0" is near-circular and coarse

- The backfill **creates** a verse-record for every uncovered master-index span, then I checked "does every characteristic span have a record?" → 0. **Of course it's 0 — I built the records to make it 0.** It proves the records now **exist**; it does **not** prove they are semantically right.
- The coverage check matches on **base strong** `(verse_id, base(strong))`. So a **wrong-sense** record satisfies it. Example: H2617 *chesed* has H2617A *kindness* (127 recs) and H2617B *shame* (57 recs); a characteristic span for *kindness* is counted "covered" by **either**. The check cannot tell them apart.

## What was NOT verified

1. **Sense correctness of ambiguous terms.** **137 Psalms base-strongs** have multiple OWNER sub-entries; I resolved each by a **dominant-sense heuristic** (the sub-entry with the most existing records) + a lowest-code tiebreak. Unverified. Some are certainly wrong (e.g. chesed A/B tied at 169 each — the tiebreak, not evidence, picked A).
2. **Tangled ownership.** H7307 *ruach/spirit* was linked to the **`anger`** registry (its pre-existing tangled owner) — semantically dubious ("spirit" under "anger"), chosen for expedience, not correctness.
3. **Role correctness.** The backfill does **not** touch roles. I **trusted** the `role-reassess-2026` layer; I did not re-verify it this session. Your own figure — only ~43% of *prior* roles survived that reassessment — is exactly why trusting any single role pass without independent check is risky.
4. **Proverbs has NO role layer at all** (0 `role-reassess-2026`). So for Proverbs I did **no** characteristic validation and made **no** valid completeness claim — I only backfilled *registered-term occurrences regardless of role*. Calling that "full integrity" was misleading; it meant only that the structural integrity **controls** (dup/orphan checks) showed no new breach — nothing about correctness.

## What WAS established (the honest, narrow claim)
- **Structural integrity controls** pass: no new duplicate-owner, no orphaned links, no out-of-corpus rise. (This is real but is *plumbing*, not *meaning*.)
- **Verse-records now exist** for every registered-term master-index occurrence in Psalms and Proverbs — with full FK scaffolding (term_inv_id, word_registry_fk, mti_term_id, verse_span_id).
- The Psalms **97 + 27 orphan onboarding** had a genuine, non-circular audit (the stamped collateral detector showed existing terms preserved, delta +0) — that part stands.

## Why your skepticism is correct
You said: largely the same logic that found Psalms roles only ~50% right cannot suddenly yield "everything correct." Right — because the backfill **never checked correctness**; it manufactured existence and I reported the existence check as if it were a correctness proof. The role layer's known unreliability is untouched by the backfill and, for Proverbs, entirely absent.

## What a real verification would require (proposed, before ANY rollout)
1. **Independent (non-circular) correctness sample**: draw N backfilled records, verify against the master-index morphology that the linked OWNER term is the *right sense* for that surface/morph — measure an error rate, don't assert 0.
2. **Quantify heuristic exposure** per book: fraction of records that depended on the ambiguous dominant-sense pick or a tangled owner; treat those as "provisional," not "correct."
3. **Separate the role question**: role correctness is an **analytical** layer the backfill does not address. Any "characteristic completeness" claim is only as good as the role pass beneath it — which for Proverbs does not exist.

**Recommendation: do not roll the backfill across 27 books on the current premise.** First agree what "correct" must mean and a non-circular way to measure it. I will not report existence as correctness again.

*Filed 2026-07-06 as a correction to the Step-e and Proverbs status claims.*
