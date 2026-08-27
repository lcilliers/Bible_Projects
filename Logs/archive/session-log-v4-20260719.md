# IBA Session Log — v4, 2026-07-19

**Topic:** Romans inspection exposed the candidate-characteristic seed as incomplete and the
passage-build as unfit. Response: stop symptom-patching, reason from the study's outcome, run a
complete seed-quality review over the whole lemma inventory, confirm the inclusion criterion with
the researcher, and apply + validate the recall additions. (Passage method deliberately left parked.)

**Outcome:** ✅ Full judgement pass over all 11,781 lemmas → ~150 disposition misses + ~35 spiritual
agents + adversary/divine classes; criterion confirmed maximally inclusive; **candidate_seed
1,732 → 2,013 (+281)**, all 66 books re-stamped, **10/10 validation checks PASS**. Ready for the
targeted investigation the researcher will direct next.

---

## 1. Trigger

Researcher inspected Romans and reported: passage creation not fit for purpose (majority
single-verse), seeding not right, candidate-char assignment incomplete (a simple term like *thank*
missing) and not supporting the context of the characteristics. Deeper charge: the app's
"validations" check nothing about compliance / quality / fitness; and my check-find-patch reflex is
appalling — I had never asked what the *outcome* of seeding / characteristics / passages should be.

## 2. Reframe (outcome-first)

- **Owned the real failure:** the IBA validations test *mechanics* (schema, write-grants, hashes,
  "did every candidate verse get a row"), never *fitness* (is the char set complete/clean; does a
  unit carry a movement). Presenting green mechanical ticks as quality assurance was misleading.
- **The passage foundation is built on the wrong unit.** The study's own method
  (`Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md`) already worked out, book-type by
  book-type, that the contextual unit is a **movement-scoped segment** (§14 poetic chapter, §15
  wisdom segmentation, §15.1 prophetic oracle) — never a mechanical run. Romans (epistle) fell
  through to the untested "prose = consecutive run" default, and the IBA build implemented an even
  worse version (consecutive *candidate-bearing* verses broken by a repeated Strong's → 83%
  single-verse, 96% of those adjacent to context that was thrown away). Filed:
  `iba/app/docs/iba-foundation-outcome-and-unit-position-v1-20260719.md`,
  `romans-passage-seeding-diagnosis-v1-20260719.md`.
- **Researcher direction:** the digest/passage method is *not* settled — do **not** reopen it now.
  The **first door — the candidate chars — must be right first.** Root = a low-quality seed list.

## 3. Seed quality review (the judgement pass)

Read and judged **all 11,781 `lemma_inventory` glosses** against the criterion. Findings:

- The migrated basis (1,732) was **registry-derived → incomplete and inconsistent** — Hebrew *thanks*
  (*yadah/todah*) in, Greek *thanks* (*eucharisteo*) out; same concept, opposite fate.
- **~150 solid disposition misses**, in whole families, not a tail: self-control (*enkrateia*),
  piety/godliness (*eusebeia*), virtue (*arete*), the sluggard (*atsel*), the simple (*pethi*),
  craftiness (*ormah*), unfaithfulness/backsliding (*maal/meshubah*), bear-a-grudge (*natar*),
  discipline (*musar*), reproof (*tokechah*), and *thanks*.
- **Structural ceiling = lemma-vs-sense:** membership lives at the sense ("clean" = moral purity IN /
  ritual cleanness NOT; *sarx*, *tiqvah*, *chayil*), not the lemma. Filed + checkable:
  `iba/app/docs/seed-quality-review-greek-v1-20260719.md`,
  `seed-quality-review-hebrew-aramaic-v1-20260719.md`.

## 4. Criterion — confirmed by researcher

- **Other-being characteristics IN** (God, spirits) — Screen 0 decides human-vs-other later, at the
  read, never at the seed.
- **Imagery / analogy / allegory / idiom / verb-forms IN** ("to be devoted" = devotion). Ties to the
  2026-07-14 analogy qualifier-typing discourse.
- **Agents that act ON the inner being IN** — Satan, spirits, demons, idols/false gods, occult powers
  exist to tempt/deceive/torment/ensnare it; they are load-bearing nodes, not external referents.
  (Corrected my initial wrong "entity-name = drop"; Satan H7854 and jealousy H7065/67/72 were in fact
  already candidates.)
- **The seed IS the verse-selection gate** — it decides which verses enter the primary read; a false
  negative drops a whole *verse* (and every interaction in it) forever → bias hard to inclusion.
  Governing rule (config `char.seed-over-inclusive`): *false positive caught by a gate; false
  negative invisible forever.* Boundary calls (human adversaries, divine names) resolved **IN** —
  role is contextual, can't be pre-judged at the seed; scoping still holds because pure
  geography/objects/numbers/individual-names (~80%) never interact and stay out.

## 5. Apply

- Compiled the include-set (dry-run verified every lemma against its gloss — no typos): dispositions
  + agents (authored from the reviews) + adversary + divine classes (gloss-matched). **289 `accept`
  rules** written to `cfg_candidate_rule` (+ CSV for the record).
- Ran the config-governed path: `candidate.seed` (global) created the candidates →
  `candidate.set` re-stamped `span_candidate` across **all 66 books**.
- Result: **candidate_seed 1,732 → 2,013**; `ib-judgement` layer 202 → 489; span_candidate 87,922;
  candidate-bearing verses (primary read) **25,775 / 29,037**; Romans **363 → 382** verses recovered.

## 6. Validation — PASS 10/10

`iba/app/reports/seed-recall-validation-20260719.md`. All checks green incl. the integrity invariant
(`candidate-has-verse-record`, 0 violations), all-accepts-are-candidates, all-books-stamped, and
recall landing (*thanks* G2168 = 6 stamps in Romans; Satan, enemy, hospitality, flattery all present).

## 7. Carried forward

- **Divine-name footprint is heavy** — bare "God" (G2316) = 151 spans in Romans. Intentional
  (can-interact ruling); the read/Screen 0 must sort arena vs counterpart. Reversible lever if noisy:
  bare divine *names* (dispositions stay regardless).
- **Passage method still parked** — verse selection (seed) done; context scoping (passage/movement
  unit) remains the open foundation question, deliberately not reopened this session.
- **Next:** researcher will direct a targeted investigation (flagged interest in comments made during
  this session, incl. the divine-name interaction footprint and the lemma-vs-sense boundary).

## 8. Key files

- Diagnosis / reframe: `iba/app/docs/romans-passage-seeding-diagnosis-v1-20260719.md`,
  `iba-foundation-outcome-and-unit-position-v1-20260719.md`
- Seed reviews: `iba/app/docs/seed-quality-review-greek-v1-20260719.md`,
  `seed-quality-review-hebrew-aramaic-v1-20260719.md`
- Validation: `iba/app/reports/seed-recall-validation-20260719.md`
- Config input: `iba/app/config/cfg_candidate_rule.csv` (289 accept rules)
- Memory: `feedback_candidate_seed_independent_over_inclusive_control` (criterion + applied state)
