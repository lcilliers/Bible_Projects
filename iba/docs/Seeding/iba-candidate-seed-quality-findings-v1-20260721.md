# candidate_seed quality — gap + live findings

> Investigation, 2026-07-21. Triggered by the researcher's suspicion that `candidate_seed` (the
> L4b seed table) carries dirty `tag` values — special characters, multi-word phrases,
> transliterations — and that no config-driven report actually assesses it. Read-only inspection
> of live code (`handlers/candidate.py`, `migration/import_seed.py`) and the live DB
> (`iba/app/db/iba.db`). No changes made.

## 1. The gap, confirmed

There is **no work-package step, no `on_fail` rule, and no report path in config that targets
`candidate_seed` directly.** The only quality check in the system — `candidate.validate`
(`Candidate-Quality.ps1`, handler `handlers/candidate.py:validate`) — checks **`span_candidate`**
(the L4b *stamp*, one row per span), not `candidate_seed` (the L4b *seed decision*, one row per
lemma). `candidate.quality_report_path` in `CONFIG-REPORT.md` §2 is scoped the same way: "where
`candidate.validate` persists its findings" — i.e. span_candidate findings.

`span_candidate.candidate_tag` is a straight denormalised copy of `candidate_seed.tag`
(`handlers/candidate.py:128`), so today the two happen to look similar. But the coverage is
**incidental, not structural**: `span_candidate` only contains a lemma once `Set-Candidates.ps1`
has run for a book containing that lemma's spans. A candidate lemma seeded but not yet stamped
into any processed book is currently invisible to `candidate.validate` — checked below.

## 2. Root cause — where the dirt enters

`candidate_seed.tag` is written verbatim, with **no cleaning**, at two points in
`migration/import_seed.py`:

- line 91: `"tag": L.get("gloss")` — the raw gloss string from the old
  `lemma-inventory-master-no-particles-20260707.json`.
- line 112: `"tag": e.get("seed_word")` — the raw `seed_word` from a
  `char-seed-extension-read-emergent-*.json` file.

Neither is passed through `candidate.tag_clean_pattern` (`^[A-Za-z][A-Za-z' -]*$` — the rule that
*is* enforced, but only downstream, on `span_candidate.candidate_tag` via `candidate.validate`).
`handlers/candidate.py:seed()` (the live re-run step) never touches `tag` at all — it only sets it
on first insert (`_set_decision`, always `None`), so cleanup can't happen through a normal seed
refresh; it would need a dedicated fix at the source (the migration) or a new pass over the live
table.

## 3. Live measurement (`iba/app/db/iba.db`, 2026-07-21)

| metric | count |
| --- | --- |
| `candidate_seed` rows (not deleted) | 2,086 |
| of which `decision='candidate'` | 2,013 |
| candidates with `tag IS NULL` | 281 |
| candidates with a non-null `tag` | 1,732 |
| non-null tags **failing** `candidate.tag_clean_pattern` | **226** (13.0% of non-null) |
| — of which contain `:` (dual-gloss, e.g. `"to hear: hear"`) | 38 |
| — of which contain `/` (alt-gloss, e.g. `"spirit/breath: spirit"`) | 83 |
| — of which contain `(` / `)` (e.g. `"to trust (in)"`) | 121 |
| non-ASCII characters in any tag | 0 (none found — no raw transliteration glyphs) |
| tags that *pass* the clean pattern but are still a raw multi-word dictionary gloss (e.g. `"to hear"`, not an IB label) | 654 |
| distinct lemma_keys ever stamped into `span_candidate` | 2,013 — **currently equals candidate count**, so today every messy tag *is* reachable via `candidate.validate`'s span_candidate scan (0 messy rows were found "invisible") |

Sample of the 226 pattern failures:

```
H8085  [registry-direct]  'to hear: hear'
H7451  [registry-direct]  'bad: harmful'
G4100  [registry-direct]  'to trust (in)'
H0639  [registry-direct]  'face: anger'
H6942  [ib-judgement]     'to consecrate: consecate'   <- also a misspelling
H3477  [registry-direct]  'upright:right'
```

## 4. What this means

- Your suspicion is correct: `candidate_seed.tag` is dirty at the source. It was never meant to be
  the display label — it inherited the old inventory's `gloss` field wholesale.
- The dirt is **not currently invisible** (span_candidate coverage happens to be total right now),
  but the safety net is accidental: the day a new candidate lemma is seeded and stamped into a book
  before another book run touches it, or a lemma exists only in an as-yet-unprocessed book, its
  messy tag would sit unreported until that book's `set-candidates` run.
- No config setting documents an expectation for `candidate_seed.tag` cleanliness the way
  `candidate.tag_clean_pattern` documents it for the stamp. That's the literal gap you went
  looking for.

## 5. Open judgement calls (not decided here)

1. Should `candidate_seed.tag` get its **own** validate step/report (mirroring `candidate.validate`
   but scoped to the seed table, catching a lemma before it's ever stamped), or is checking it via
   `span_candidate` (once coverage is total) considered sufficient?
2. Should the **654** clean-pattern-passing-but-raw-gloss tags (e.g. `"to hear"`) be treated as a
   quality issue too? The pattern only rejects punctuation/special characters — it does not enforce
   that the value is an actual IB label rather than a dictionary gloss.
3. If yes to (1): this is a config change (a new `cfg_step`/`cfg_on_fail`/report-path row) —
   per GOVERNANCE.md §5A, goes through `Config-Maintenance.ps1 -Step Propose`, escalation-gated,
   not a silent edit.
