# Response to your table review — `run`, `escalation`, `candidate_seed`

> 2026-07-22. Every point below was checked against the live code and `iba/app/db/iba.db` — none
> answered from assumption. Structure: **found** (what the data/code actually shows), then either
> a fix proposal awaiting your go-ahead, or a question back to you where I don't have enough to
> act.

## Part 1 — `run`

### 1.1 `config_version` — confirmed, you're right

It has been `"app-0.1.0"` on **every single row** since the first run (2026-07-18) through today,
across 12 bulk config reloads (`cfg_change_log`) and roughly 30 individual `configmaint.propose`
row-changes made yesterday/overnight. Root cause: `config_version` is a **manually-typed string
inside `config/rules.json`'s seed** (`cfgload.py:134` just copies whatever the seed file says into
`cfg_meta`) — nobody has ever incremented it by hand, and worse, **`configmaint.propose` never
touches it at all**, even though row-level propose changes are now the primary way config changes.
So `run.config_version` ("the config that ran, pinned before any work" — its whole stated purpose)
has been meaningless as an audit signal since 2026-07-21, when propose-driven editing began.

**Not fixed yet — needs a decision:** should `config_version` be (a) a hash of the live `cfg_*`
tables' content (auto-computed, always accurate, no human discipline required), or (b) still a
human string but auto-incremented by `configmaint.propose` on every applied change? (a) is more
work but never goes stale again; (b) is simpler but relies on the same discipline that's already
failed once.

### 1.2 Failure alerting — confirmed gap: none exists beyond the terminal, at that moment

`run.state='failed'` is set (`run.py:111`) and nothing else happens — no persisted report, no
notification. The PS wrapper prints that one line in red **at the moment it happens**; if you
weren't watching that terminal, there is currently no way to discover a run failed except querying
`run` directly (or now, `Export-Tables.ps1`). 89 rows are `state='failed'` today — I checked a
sample and most are deliberate self-tests from yesterday's build session (`TEST-BADMODULE-1` etc.,
proving `configmaint.propose` rejects bad input) rather than real accidental failures, but nothing
distinguishes the two today.

### 1.3 What's pausing `configuration-maintenance` this morning — **found a real bug, not a real pause**

Nothing is actually blocking it. I checked the specific runs: their escalations were already
answered, `outcome` was `'ok'`, but `run.state` is still `'paused'` — because of a bug in
`run.py`'s completion logic. `_ensure_run`/the dispatcher marks a run `'done'` only when the
*current* step is the **last step in its work package's `cfg_step` sequence**. That's correct for
a chained run (`new-word`, `set-candidates`) but wrong for `configuration-maintenance`
(`validate`=0, `propose`=1, `report`=2 — three **independently invoked** operations sharing one
registration, per its own design, GOVERNANCE.md §5A) and `reports` (`report.word`=0,
`validation.word`=1, `validation.book`=2, same shape). Running `configmaint.validate` alone —
which is the normal way to use it — can never reach `'done'`, because it's never the last step.
Live-verified:

| pattern | count |
|---|---:|
| runs stuck at `state IN (running, paused)` even though every escalation on them is fully `answered` (none still `raised`) | **185** |
| `configuration-maintenance` runs stuck `paused` at `configmaint.validate`, `outcome=NULL` | 8 (+ this morning's, +yesterday's test runs) |
| `reports` runs stuck `running` at `report.word`/`validation.word` | 3 |
| `set-candidates` runs stuck `running` at `candidate.seed` | 178 (likely a mix of real chained runs that failed to progress and older direct single-step test invocations — not yet separated) |

This is a real defect: `run.state` cannot be trusted as "is this actually blocked" for any
standalone-step work package. **Fix proposal:** the done-check should also close the run when the
step's `on_fail` resolution is `'ok'`/`'report-continue'` **and the work package is not a chained
sequence being run end-to-end** — simplest concrete fix: a work package flag (e.g.
`cfg_work_package.chained = 0/1`) so the dispatcher only applies "last-step-in-sequence" logic to
chained packages, and marks any standalone step `'done'` on its own `'ok'`. Want me to build that?

### 1.4 / log growth — confirmed gap: no retention routine exists

`run` (760 rows), `escalation` (215), and `validation_result` (15,460) have no pruning, archiving,
or size cap anywhere in the codebase — I grepped for any retention logic and found none. They will
grow unboundedly for as long as the app runs. Given §1.3's bug means **stuck rows never resolve
themselves even conceptually**, a retention routine is more urgent than it would otherwise be.

**Not built yet — needs a decision:** what should retention mean here — archive-and-delete after N
days, keep-last-N-per-work-package, or just a size/age report that flags when it's time for you to
decide by hand? I'd lean toward the last one first (a report, no automatic deletion of DB history
that might matter for audit) — deletion policy is your call, not mine to assume.

---

## Part 2 — `escalation`

### 2.1 Include in the log maintenance routine

Noted — folded into §1.4 above; whatever retention mechanism gets built should cover `run` +
`escalation` (+ `validation_result`) together, since they're all append-only audit trails with the
same growth shape.

### 2.2 Write-grant extract — which routines write to `escalation`

```
cfg_write_grant WHERE table_name='escalation':
  writer = 'escalation'          -- lib/escalation.py's own answer_for_word/answer_for_run
  writer = 'registry.create'     -- legacy, explained below
  writer = 'run'                 -- the dispatcher itself
```

Every step that can pause (`candidate.validate`, `configmaint.propose`, `passage.validate`,
`registry.create`, `raw.detail`, `raw.discover`, `raw.verses`) escalates through **one centralised
path**: `run.py`'s dispatcher writes the `escalation` row under the `'run'` grant on any
`pause-continue` outcome — a step's handler never writes `escalation` directly (confirmed by
reading `handlers/registry.py:create`, which also just returns `escalate(...)` for the dispatcher
to act on). So the short answer to "which steps write, which don't" is: **all of them route
through the same centralised writer (`run`); none write it directly** — except:

**Found while checking this: `registry.create`'s own grant is dead code.** It's listed in
`cfg_write_grant` but nothing in the codebase ever checks `cfg.may_write('registry.create')` for
the `escalation` table — the actual write goes through `cfg.may_write('run')` in the dispatcher, as
above. It's a leftover from before escalation-raising was centralised (BUILD.md dates the raw
slice to 2026-07-17, before the dispatcher's centralised handling existed). Harmless, but an
orphaned grant row — worth a `configmaint.propose` delete when you're doing general cleanup, not
urgent.

### 2.3 A report of all open items — confirmed gap, you're right to assume it should exist but it doesn't

`Escalation.ps1 -Action List` → `python -m iba.app.lib.escalation list` only **prints to the
terminal**. It never writes a persisted file. This is exactly the standard this session already
enforced everywhere else (`governance.reports_must_persist` — every quality-check/status view must
persist to a report path, not live only in a terminal print) — and this one was simply never
brought in line with it. **Fix proposal:** add a `lib/escalation.py` report writer
(`open-escalations.md`, listing every `state='raised'` row — id, run_id/word, at_step, question,
raised_at) wired the same way `candidate.quality_report_path` etc. are — want me to build it?

### 2.4 How can you manually add an item for later resolution — confirmed gap, doesn't exist yet

`lib/escalation.py:raise_()` exists but is only ever called *by a running step* (needs a `run_id`
and `at_step` to know where to resume) — there's no CLI path for you to raise your own ad hoc item
outside of a governed run. **Fix proposal:** a small `Escalation.ps1 -Action Raise -Question "..."`
that writes a manually-raised row (a sentinel `run_id` like `MANUAL-<timestamp>`, no `at_step` since
nothing resumes it, `type='interactive'`) into the same table, so it shows up in the same open-items
list (§2.3) and gets "answered" the same way, purely as your own tracked note/decision — not tied
to resuming any run. Want this built alongside §2.3?

---

## Part 3 — `candidate_seed`

### 3.1 Tag dirt — confirmed, matches the existing worklist

Your examples (`"to call:call to"`, `"to trust (in)"`, `"will/desire"`,
`"be at rest / settle (shakan - and be at rest)"`, `` `Terror on Every Side` ``) are all already
in `candidate-quality.md`'s worklist (225 rows). No new discovery here — confirms the worklist is
accurate.

### 3.2 `registry_match` blank AND `tag` blank = false row — confirmed, and precisely scoped

**169 rows**, `decision='candidate'`, `registry_match IS NULL AND tag IS NULL` — and **all 169 are
`layer='ib-judgement'`** (the researcher-force-included list from the old study, migrated via
`import_seed.py`'s explicit-reject/accept lists). None are `registry-direct`, `curated-synonym`, or
`read-emergent` — those three layers always got *some* tag or registry_match at migration time.
This is a clean, well-defined target: every `ib-judgement` candidate that never received a tag or a
registry match. I agree this looks like dead weight, not a live candidate — but per your own
standing rule that data judgement calls need your sign-off, I haven't touched these; see §3.6,
same disposition (delete) likely applies to these too, and could be handled in one pass together.

### 3.3 Blank `lemma_key` — not found; I likely misread your point, please clarify

`candidate_seed.lemma_key` is `NOT NULL`+`UNIQUE` in the schema and **0 rows** are blank/empty —
same for `lemma_inventory.lemma_key`. So either you meant a different column (`registry_match`,
which genuinely is blank in 190 `decision='candidate'` rows — the "candidate missing a registry
word" completeness signal already tracked and reported), or you're looking at a specific row I
should look at directly — if you can point me at one, I'll check it exactly rather than guess.

### 3.4 Sub-strong tracking — confirmed, and this is a real, previously-unnoticed structural gap

You're right, and it's bigger than a couple of examples: **173 of 3,178 base lemma_keys (5.4%)**
have multiple sub-lettered `strong` variants with **genuinely different glosses** — e.g. `G0769G`
"weakness: weak" vs `G0769H` "weakness: ill"; `G0039G` "Holy Place" vs `G0039H` "Most Holy Place".
`candidate_seed.lemma_key` is base-only (`candidate.lemma_base_pattern` strips the sub-letter on
purpose, "the lemma key" per its own `use` text) — there is genuinely **no table anywhere that
records which specific sub-strong a `candidate_seed`/`lemma_inventory` row's gloss/tag actually
came from.** This plausibly explains *some* of the "dual concept" dirty tags (a tag trying to hold
two sub-senses at once) — though I want to be precise: I have not yet proven that connection
row-by-row, only that the structural gap is real and large enough to matter. Confirmed this needs a
new column (e.g. `candidate_seed.strong_variant` or a small new mapping table) — this is a schema
change, not a config-content change, so it needs your explicit go-ahead on the design before I
build it. Do you want it as (a) a new column directly on `candidate_seed` (one row still = one
lemma, but now records which specific variant the tag reflects), or (b) a proper one-to-many table
(`candidate_seed_variant`: lemma_key, strong_variant, tag) so a single base lemma can carry multiple
clean, single-concept tags — one per sub-sense — which sounds closer to what your tag-cleanliness
principle (§3.5) actually requires?

### 3.5 Tag cleanliness principle — understood, will bake into the curation method doc

Recorded precisely: a seed tag must be (a) a single concept — a compound like "to call: call to" or
"will/desire" is two rows, not one; (b) searchable as it would actually appear in verse text — "to
trust (in)" fails this; (c) never a sentence; (d) never a transliteration; (e) never carry special
characters; (f) stripped of surplus words down to the term that carries the actual inner-being
sense. I'll fold this exact wording into
`iba-candidate-seed-curation-method-v1-20260721.md` as the formal cleanliness standard once §3.4's
schema question is settled (since "one concept, one row" directly implies the sub-strong/one-to-many
design in 3.4 — these two points are the same underlying fix).

### 3.6 Blank tags — confirmed, 281 rows, agree these are invalid as-is

`decision='candidate' AND tag IS NULL` = 281 rows (unchanged since first audit). You've said these
must be deleted, not just flagged. Two notes before I do that: (1) `candidate.curate` (built
yesterday) currently only supports **updating** `tag`/`decision` on an existing row — it has no
delete/purge operation, so this needs a small extension first; (2) per this app's soft-delete
convention (every data table carries `deleted`, no physical deletes anywhere else in the app), I'd
soft-delete (`deleted=1`) rather than hard-delete, so the migration history stays inspectable and
reversible — confirm that's what you want before I build the delete path and run it across all 281
(plus the 169 from §3.2, if those get the same disposition).

### 3.7 Anger/spirit overlap — logged as an open methodological issue, no action taken

Recorded as you framed it: a lemma whose seed match spans two valid IB concepts at once (spirit +
anger) raises a real question about how `candidate.set`'s stamp should represent dual-characteristic
verses, and I haven't seen this addressed anywhere else in the existing method docs. Not actioning
this — flagging it in
[`iba-candidate-seed-curation-method-v1-20260721.md`](iba-candidate-seed-curation-method-v1-20260721.md)
as an open item for when you're ready to work through it, alongside §3.4 since they're related (a
sub-strong-aware model may be part of the eventual answer, but I'm not assuming that).

---

## What I'm waiting on before doing anything further

Nothing above has been fixed or deleted — this is the findings pass only. Decisions needed from
you: 1.1 (version scheme), 1.3/1.4 (whether I build the `run.py` fix + a retention report), 2.3/2.4
(whether I build the escalation report + manual-raise), 3.2/3.6 (confirm soft-delete + scope), 3.3
(what you actually meant), 3.4 (column vs. one-to-many table design).
