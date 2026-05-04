# Q&A Method — Triage Findings & Options

**Date:** 2026-04-28
**Author:** Claude Code (in response to researcher feedback on `wa-qa-quality-review-20260428.md`)
**Status:** For researcher review. No catalogue-wide action taken beyond the GAP-S migration described below.

---

## 1. What the researcher said

> "GAP-S2-002 is word specific. This should be answered in goodness, if not, it should be surfaced as to be researched further. some of the questions are unclear, badly worded, or should have a follow up question. many of these questions need to be re-asked. I don't think the QA method has achieved its objectives."

Three concerns are present:

1. **Mis-categorisation** — programme-level questions sitting in the generic catalogue. (Concrete: GAP-S2-002.)
2. **Question quality** — unclear, badly worded, or needing follow-up.
3. **Method effectiveness** — overall judgment that the catalogue has not delivered on its purpose.

I have acted only on (1), where the precedent and the right action were both unambiguous (matches the GAP-N migration of 2026-04-28). For (2) and (3), this document surfaces evidence and options without taking destructive action on the catalogue.

---

## 2. Action taken: GAP-S* migration

All eight `GAP-S*` rows were programme-level methodology questions raised during R067 goodness obslog v3 work and parked in the generic catalogue. The same mis-categorisation pattern as the earlier GAP-N triplet.

**Migrated** (transactionally, with backup `backups/bible_research_pre_gap_s_migrate_20260428.db`):

| obs_id | question_code | new SD pointer | answers on file pre-migration |
| ------ | ------------- | -------------- | ------------------------------ |
| 207 | GAP-S1-001 | SP-067-019 | R064/OBS-064-004, OBS-064-026, OBS-064-027 |
| 208 | GAP-S1-002 | SP-067-020 | R064/OBS-064-024, OBS-064-027, OBS-064-032 |
| 209 | GAP-S2-001 | SP-067-021 | R030/OBS-030-028, OBS-030-047 |
| 210 | **GAP-S2-002** | SP-067-022 | *none — unanswered, surfaced for further research as you requested* |
| 211 | GAP-S3-001 | SP-067-023 | none |
| 212 | GAP-S3-002 | SP-067-024 | none |
| 213 | GAP-S4-001 | SP-067-025 | none |
| 214 | GAP-S5-001 | SP-067-026 | none |

Each new `wa_session_research_flags` row has `flag_code='SD_POINTER'`, `priority='MEDIUM'`, `session_target='Session D'`. The original question text is preserved verbatim in the description with a migration prefix. Where pre-migration answers existed (S1-001, S1-002, S2-001), those answers remain in `wa_session_b_findings` accessible via their `finding_id` and the SD pointer description references them.

Catalogue rows soft-deleted (`deleted=1`); 17 finding-catalogue link rows soft-deleted.

**Catalogue status post-migration:** 212 active rows (was 220 pre-migration today, 223 total — 11 deleted = 3 GAP-N + 8 GAP-S).

Script: [scripts/archive/_apply_gap_s_migrate_to_sd_pointers_v1_20260428.py](../../scripts/archive/_apply_gap_s_migrate_to_sd_pointers_v1_20260428.py)

---

## 3. Surfacing: GAP-N migration silent-skip bug

While doing the GAP-S work I confirmed an issue with the earlier GAP-N migration that is worth flagging to you, but which I have **not** auto-fixed.

**What happened.** The 2026-04-28 GAP-N migration script soft-deleted catalogue rows 221/222/223 (GAP-N-001/002/003) with `review_note` claiming they were "migrated to SP-067-009/010/011 as SD pointer". But SP-067-009..011 were already populated with substantive R067 goodness pointers from the obslog (Jos 23:14 inner-being binding; Est 5:9 tov-lev shared anchor; G0018 distribution across R65). The script's idempotency check matched on `flag_label` only, found those labels present, and silently skipped its own inserts — but proceeded to soft-delete the catalogue rows anyway.

**Net effect.** GAP-N-001/002/003 catalogue rows are gone, but their content (programme-level questions about how the framework treats vocabulary divisions) was never carried forward into the SD pointer table. The `review_note` on those rows is misleading.

**Options if you want this fixed:** insert SP-067-027/028/029 with the GAP-N content, and update the misleading `review_note` on obs_ids 221–223 to point to the correct labels. This is reversible at any time. Awaiting your direction.

---

## 4. Question-quality concern — concrete samples

You said: *"some of the questions are unclear, badly worded, or should have a follow up question."* Sampling the 72 silent questions in Sections 1–5 (post-migration), I see three failure modes worth distinguishing — they ask for different remedies:

### 4.1 Presupposition opacity

> **Q051** *What reason does a key verse give for the extension of the word — in the recipient's actions, or in the character of the one who gives it?*

The phrase "the extension of the word" is not a defined construct in `wa-reference`. It presupposes a framework the analyst doesn't know is being invoked. A reader cannot answer because they cannot first parse the question.

**Likely remedy:** rewrite with explicit construct names, or replace with the framework concept it is gesturing at.

### 4.2 Excessive abstraction

> **Q057** *What spatial or directional language does a key verse use for the reality of the word's operation?*

Plausibly answerable but the abstraction collapses across very different phenomena (a verb of motion, a metaphor, a locative preposition…). Different analysts will produce non-comparable answers, so cross-word synthesis becomes impossible.

**Likely remedy:** split into 2–3 narrower questions with stated answer types.

### 4.3 Latent dependency

> **Q058** *Does any verse distinguish between the means of entry into the word and the condition the word produces?*

This is two questions glued together — and the second depends on a "yes" to the first. Forced into one row, it produces fence-sitting half-answers or `no_finding`.

**Likely remedy:** one parent + one follow-up question, with the follow-up only fired when the parent resolves.

A complete categorisation of all 72 silent rows along these axes is a substantial review pass — see Section 6 for proposed scope.

---

## 5. The method-effectiveness question — what the data actually says

You wrote: *"I don't think the QA method has achieved its objectives."* Two things are true at once, and they need to be held apart.

### 5.1 What the headline numbers say

Post-migration, Sections 1–5 (universal generic):

| Coverage | Count | % of 147 |
| -------- | -----:| --------:|
| 0 words answered  | 72 | 49% |
| 1 word answered   | 31 | 21% |
| 2 words answered  | 28 | 19% |
| 3 words answered  | 16 | 11% |
| **Total**         | **147** | **100%** |

### 5.2 Why those numbers under-represent the method

**Only 3 registries have been run through v2 to `Analysis Complete`** (R030 contrition, R064 forgiveness, R067 goodness). 111 registries have at least one Session B finding under the older architecture but not v2-with-catalogue.

So "0 words answered" most often means "none of contrition/forgiveness/goodness answered this question". For most generic questions, n=3 is too small to distinguish "the question is bad" from "this triplet of words doesn't happen to engage the question".

**This does not invalidate your concern.** It does mean the binary assessment ("method failed" vs "method succeeded") is premature. What the data does show clearly:

- Some questions are demonstrably broken regardless of n (Section 4.1, 4.3 above — *no* analyst could answer Q051 confidently because the construct is undefined).
- Questions that landed answers in all three of R030/R064/R067 (the 16 in §C of the prior report) are working, and they are diverse — so the method is not categorically broken.
- The catalogue is mixing three things that should not be mixed (see §6.1).

### 5.3 The real diagnostic

The right question is not "did the method work?" but **"what fraction of catalogue questions, with the current n=3, are: (a) intrinsically answerable but the words didn't engage it; (b) badly worded; (c) misplaced?"** That is a researcher-judgment review, not a SQL query. I can build a structured review surface for you (see §6.3) but I should not autonomously triage catalogue content.

---

## 6. Triage options for researcher decision

### 6.1 The three-tier separation

Today's catalogue conflates three things:

1. **Generic per-word analytical questions** (Sections 1–5, ~147 active) — fire on every word.
2. **Word-specific extensions** (Compassion / Forgiveness / Goodness / Love / Mercy Extensions, 53 active) — fire only on the named word.
3. **Programme-level methodology questions** — should not be in the catalogue at all; belong in `wa_session_research_flags` as SD pointers (this is what GAP-N and GAP-S were).

Your "approx 150–160 unique questions" intuition matches Tier 1 if Tiers 2 and 3 are extracted. Tier 1 currently sits at 147; that is the bucket on which any "method effectiveness" judgment should be made.

### 6.2 Three actionable options (any combination)

| Option | What it does | Reversibility | Researcher time |
| ------ | ------------ | ------------- | --------------- |
| **A. Targeted rewrite** | I list every Section 1–5 question with 0–1 answers. You mark each: keep / rewrite / split / delete. I apply patches. | Full (audit trail in `review_note`). | 2–4 hrs (about 100 rows). |
| **B. Defer until n grows** | Run 3–4 more words against the v2 catalogue first; revisit the silent set when n=6 or 7. Some will resolve naturally. | Status quo. | 0 hrs now. |
| **C. Re-foundation** | Pause v2 catalogue use. Rebuild from the questions that successfully landed cross-word (the 16 §C questions are the demonstrably-effective core). New catalogue inherits proven questions, drops the abstract layer. | Heavy. Discards the existing answer mappings on the 75 rows with at least one answer. | 1–2 days, plus re-running R030/R064/R067 against the new catalogue. |

### 6.3 If you want me to build a review surface

A single markdown file, one row per Section 1–5 question, columns: question text, count of answers, registries that answered, sample answer text, and a blank "researcher disposition" column. This makes Option A into a single-file pass. Estimate: 30 min to build, output ~150–200 KB.

I will only build it if you ask. I will not autonomously edit any catalogue row beyond the GAP-S migration documented in §2.

---

## 7. Open loops parked from this session

- (a) Decision on §3 GAP-N silent-skip fix (insert SP-067-027/028/029 with GAP-N content, correct misleading review_note).
- (b) Decision on §6 triage path (A / B / C, or composite).
- (c) Whether to add a question-quality validation layer to the obslog ingest pipeline so that obviously-broken questions surface earlier (Section 4.1 / 4.3 patterns are detectable; 4.2 needs human judgment).

None of these block continued v2 word work on mercy / love / compassion / fellowship / grace.

---

## 8. References

- Prior coverage report: [research/investigations/wa-qa-quality-review-20260428.md](wa-qa-quality-review-20260428.md)
- GAP-N migration script (with the silent-skip bug noted in §3): [scripts/archive/_apply_gap_n_migrate_to_sd_pointers_v1_20260428.py](../../scripts/archive/_apply_gap_n_migrate_to_sd_pointers_v1_20260428.py)
- GAP-S migration script (this session): [scripts/archive/_apply_gap_s_migrate_to_sd_pointers_v1_20260428.py](../../scripts/archive/_apply_gap_s_migrate_to_sd_pointers_v1_20260428.py)
- Backup taken before GAP-S migration: `backups/bible_research_pre_gap_s_migrate_20260428.db`
