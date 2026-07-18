# IBA app — status report (2026-07-18)

> After the legacy registry migration + the automatic candidate-seed coupling. Verdict:
> **registry load substantially complete (176/180 built, 4 flagged)**; **candidate seeding
> complete and current** (steady state, +0 changes on re-run).

---

## 1. Registry load — 176 / 180 built

| status | words | meaning |
| --- | --- | --- |
| `raw-complete` | **176** | fully built (strongs + verses + spans + validation passed) |
| `approved` | 3 | approved but the raw build did not complete |
| `proposed` | 1 | approval never resolved |
| **total** | **180** | the legacy list, minus deleted/excluded |

**The 4 that did not finish — need a researcher decision (not app faults):**

| word | why | action |
| --- | --- | --- |
| `Slyness` | maps to **no Strong's** in STEP (no original-language term) | decide: drop, or a manual anchor |
| `vulnerability` | maps to **no Strong's** | decide: drop, or a manual anchor |
| `read-surfaced characteristics` | maps to **no Strong's** — a meta/placeholder entry, not a real word | likely drop from the registry |
| `blindness (spiritual` | **malformed name** (old entry was probably "blindness (spiritual)"; the "(" also broke the auto-approve answer) | fix the name, then re-run |

The migration correctly **paused rather than forced** these: its auto-approve only answers the
registration question, never a "maps to no strongs" question — those are left for you.

## 2. Raw layer volume

| table | rows |
| --- | --- |
| `word_strong` (word→strong links) | 4,333 |
| `strong` (unique strongs) | 2,998 |
| `verse` | 28,802 |
| `strong_verse` | 105,699 |
| `span` (L4a) | 530,982 |

`PRAGMA integrity_check` = **ok**. DB now runs in **WAL** mode.

## 3. Candidate seeding — complete & current

The new-word coupling re-ran `candidate.seed` after every word, and a fresh run now reports
**+0 added / +0 match-updates** — i.e. the seed is at steady state, fully reflecting all built words.

| candidate_seed | count |
| --- | --- |
| `lemma_inventory` (independent substrate) | 11,781 |
| `candidate` (potential) | **2,825** |
| `rejected` | 74 |
| candidates **covered** by a built registry word (`registry_match` set) | 2,340 |
| candidates **not** covered — the **double-control** (candidate missing registry words) | **485** |
| distinct registry words matched | 171 |

The 485 uncovered candidates are the point of the independent seed: inner-being lemmas the net
judged candidate that **no registry word yet carries** — a live list of *potential missing registry
words* to review, plus lemmas covered only by the 4 unbuilt words.

## 4. What is NOT done yet (the next step)

**Candidate *stamping* and *passages* are a separate, manual, per-book step** — not part of the
registry load or the seed coupling. Current base-layer rows exist **only for Prov + Ps** (my earlier
tests), not the corpus:

| table | rows | scope |
| --- | --- | --- |
| `span_candidate` (L4b stamp) | 617 | Prov + Ps only |
| `passage` | 143 | Prov + Ps only |
| `verse_passage` | 146 | Prov + Ps only |

To build the base layer across the corpus, run per book: `Set-Candidates.ps1 -Book <OSIS>` then
`Build-Passages.ps1 -Book <OSIS>`.

## 5. Notes / minor cleanups (not blocking)

- **Run-audit noise.** The `run` table holds many non-terminal rows: `failed` (81 — the "already
  built" skips from re-running the migration, correctly stopped), `running` (174 — the coupling
  invokes only `candidate.seed`, which is not its package's last step, so those run rows never close
  to `done`), `paused` (182 — the registration pauses, each resolved by a later resume run). These
  are audit rows, not data problems; a `run` housekeeping pass could tidy them.
- **`validation --word` "latest run" check.** It reports the word's *latest* run; a later "already
  built" skip (a `failed` stop) makes a fully-built word (e.g. `anger`) show FAIL. The word is fine
  — the check should ignore skip/stop runs. Small report refinement.
