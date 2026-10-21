# Config-maintenance + passage — live build inspection (v1)

> **Purpose:** answers your four comments on the gap list, from direct inspection of the actual code
> and DB — not from the design document. Nothing here is a fix; per your instructions, config-maintenance
> gets confirmed/fixed before any config changes, and the passage rule gets confirmed before any rebuild.
> This is the "did you actually look" pass.

---

## 1. Config-maintenance utility — NOT just "add row-level tracking." It's currently broken.

**What I did:** read `cfgload.py`, `cfg.py`, `cfgcheck.py`, `cfgreport.py` in full, then actually ran
`cfgcheck.py` and checked whether the files it depends on exist.

**Finding 1 — the load/validate pathway is broken right now, not merely incomplete.**
`cfgload.py` and `cfgcheck.py` both read their seed from 7 JSON files (`schema.json`, `step.json`,
`run.json`, `rules.json`, `report.json`, `reference.json`, `candidate.json`) at
`iba/app/config/<name>.json`. Those files no longer live there — commit `216314b9` ("config->configurator
restructure", 2026-07-19, a prior Claude Opus session) moved all seven to `iba/app/config/archive/` as a
pure rename (0 lines changed) and **never updated either module's path**. I ran `cfgcheck.py` directly:

```
FileNotFoundError: [Errno 2] No such file or directory: 'C:\Bible_study_projects\iba\app\config\schema.json'
```

Confirmed by `cfg_change_log`: the last successful load is `2026-07-18T17:41:53Z` — nothing has loaded
since the 07-19 restructure. **Right now, no config change — yours or anyone's — can be loaded into the
DB at all.** This is a harder blocker than "no row-level tracking"; it's why row-level tracking doesn't
matter yet either: there's no live loader to track.

**Finding 2 — a reporting/inspection tool exists, but it's dead code, not a working feature.**
`cfgreport.py` (added in the same 07-19 commit) generates a full markdown snapshot of every `cfg_*`
table — settings, work packages/steps, on-fail rules, write grants, status flow, schema, enums, change
log — to `iba/app/config/CONFIG-REPORT.md`. Its own docstring says it's "regenerated automatically at the
end of every accepted cfgload." I read `cfgload.py`'s `load()` function in full: **it never calls
`cfgreport.generate()`.** The claim in the docstring doesn't match the code. And no `CONFIG-REPORT.md`
file exists anywhere in the repo — it has never actually been run. So: yes, a config-inspection report
exists in principle, but today it is neither wired to anything nor has it ever produced output you could
have seen. This directly answers "I do not see any reporting method for inspection of the configs" — you
don't, because there effectively isn't one working yet, despite the code existing.

**Finding 3 — an example of exactly the "is the DB content correct" problem you asked about.**
I queried the live `cfg_candidate_rule` table: 289 rows, **all `kind='accept'`, zero `reject`, zero
`synonym`.** I then read the archived seed it should have come from, `archive/candidate.json`:

```json
{ "synonyms": [], "accept": [], "reject": [] }
```

All three arrays are **empty** — and the file's own `"note"` field says this is deliberate: *"Empty at
first — the migration imports the bulk of the seed; these are the ongoing manual adjustments."* So the
current seed-of-record says there should be **zero** `cfg_candidate_rule` rows of any kind right now
(candidacy comes from the separate `import_seed.py` migration into `candidate_seed`, a different table).
But the live DB has 289 stale `accept` rows — almost certainly left over from an **earlier** version of
`candidate.json` that did have entries, before it was edited down to empty. Because the loader has been
broken since 07-19, that edit was never applied to the DB. **This is a concrete, confirmed case of "the
existing config in the DB is not correct/current" — not a hypothetical.**

**So, to your question: is row-level change tracking the only fix needed for config-maintenance? No.**
At minimum, in priority order:
1. The loader's path is stale (`CONFIG` should resolve to `archive/`, or the seed files should move back
   — a call you'd need to make, not me).
2. The reporting tool is unwired and has never run — it needs either a call from `cfgload.load()` or a
   documented "run this after every change" step, and someone needs to actually generate a first
   `CONFIG-REPORT.md` so you have something to look at.
3. Once loadable again, the live `cfg_candidate_rule` table needs reconciling against the *current*
   (empty) seed — those 289 rows are stale relative to what the seed of record says should be there.
4. Row-level change tracking (the original A8 item 6) is real but is now the smallest of the four.

**Usability — no, not confirmed.** As it stands today you could not open a report and see current config
state (none exists), and if you tried to make an edit and reload it, the reload would fail outright.

---

## 2. Passage table — diagnosis from the actual algorithm, no rule confirmed, no fix proposed

**What I did:** read `handlers/passage.py`'s `build()` in full.

**What it actually does, exactly:** for a book, it walks candidate-bearing verses in canonical order and
extends the current run only when the next verse is (a) the **same chapter**, (b) the **immediately next
verse number**, and (c) shares **at least `passage.min_shared_strongs`** (currently `1`) candidate
base-Strong's with the *immediately preceding* verse — unless run with `-Rule maximal`, which drops
condition (c) and merges on adjacency alone. `passage.cross_chapter=false` means a chapter boundary
always breaks a run regardless of the other two conditions.

**A plausible mechanism, not a confirmed cause:** `span_candidate` is *deliberately over-inclusive* — its
own docstring in `candidate.py` says candidacy is meaning-based and broad, "the lexical stage is the real
test." So two narratively-adjacent verses very often carry **different, non-overlapping** candidate
lemmas — which is enough, under the default `char-continuity` rule, to break the run even inside what is
obviously one continuous reading unit. That is a plausible explanation for the 1.56-verse average, but I
have **not** run the query that would confirm it (e.g. characterising what fraction of breaks are
chapter-boundary vs. non-adjacent-verse vs. no-shared-Strong's) — I can run that as a next step if useful,
as a diagnostic only, not a fix.

**I am not proposing a rule.** The actual question — what should count as "this verse belongs with its
neighbour" for passage purposes — is a methodological choice about what a passage is *for* (per the
handler's own docstring: extending a characteristic's context to adjacent verses so movement can be read
"with that context"), not a bug. That's yours to confirm, per your instruction, before anything is
rebuilt.

---

## 3. "Is [item 3] the only rule missing?" — no, and the original framing of it was wrong

Re-reading `candidate.py`'s `seed()` in full: the code **already fully supports** three
`cfg_candidate_rule` kinds — `synonym`, `accept`, `reject` — all three are read and applied
(`ctx.cfg.candidate_rules("synonym"/"accept"/"reject")`). My earlier gap-list wording ("no `reject` kind
despite the column implying one") was **wrong** — the mechanism isn't missing a kind. What's actually
true, per §1 above: the live table has 289 `accept` rows and **zero** `reject`/`synonym` rows, and the
current seed-of-record (`archive/candidate.json`) says all three should currently be empty. So this
isn't a missing rule in the code — it's the same stale-content problem as §1, item 3. The original A8
item 5 should be corrected, not treated as still-standing as written.

---

## 4. Full compliance sweep (every config, every module, against §0's a–k and the rule sextet)

I now have real code read for the three built modules (`new-word` = `raw.py`+`registry.py`,
`set-candidates` = `candidate.py`, `build-passages` = `passage.py`) plus `report.py`, `cfgload.py`,
`cfg.py`, `cfgcheck.py`, `cfgreport.py`. That's enough to correct specific claims (done above) but **not
enough yet for the systematic module × principle matrix you're asking for** — that needs a deliberate
pass per module against all eleven items (a–k) and the full rule sextet (create/update/delete · data ·
relationships · output · validity · quality), checking each against the actual code the way §1–3 did
above, not against what the design document already claimed.

I'd rather scope that explicitly with you than run it unprompted. Two ways to take it:

- **Narrow first:** finish fixing config-maintenance (§1) so there's a working load/report cycle to
  audit *with*, then do the full sweep once configs are provably current — auditing against a broken,
  possibly-stale config store risks the same "confirmed X" mistake again.
- **Sweep now anyway:** do the module × principle matrix against the code as it stands, flagging
  everything, including the parts that depend on config content I can't yet fully trust.

I'd lean toward the first — fix and confirm config-maintenance, regenerate a real `CONFIG-REPORT.md` you
can actually look at, then sweep against a trustworthy base — but that's your call, not mine to make.
