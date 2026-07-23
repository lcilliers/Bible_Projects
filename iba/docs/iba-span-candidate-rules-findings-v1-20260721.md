# `span_candidate` rule additions — findings before building anything (v1)

> Checked the live data before adding any rule, per the pattern this session established. Two of the
> three requested rules would conflict with the majority of existing data right now — not edge cases,
> the majority. Flagging before building rather than either silently blocking on this or silently
> deciding it's "informational only" myself.

---

## 1. `candidate_tag IS NOT NULL` — conflicts with 17.7% of rows today

`span_candidate`: 87,922 rows total. **15,541 (17.7%) already have `candidate_tag IS NULL`.**
`cfg_column` currently declares it nullable (`notnull=0`), matching reality.

**Why:** tracing where `candidate_tag` gets its value — `handlers/candidate.py`'s `set()` copies it
straight from `candidate_seed.tag`. That field is populated two different ways: `_set_decision()`
(the `seed()` step's synonym/accept/reject paths) always writes `tag=None`; only
`migration/import_seed.py`'s one-time migration populated it, with the lemma's **gloss** text. So
`candidate_tag` is null for every candidate whose decision came from the live `seed()` step rather
than the original migration — that's the *normal* path going forward, not a defect in old data.

## 2. "No special characters or transliteration" — conflicts with virtually all non-null values

Sample of the 72,381 non-null values, unfiltered:

```
'see (raah)'                              'to twist: tremble'
'stretch out the hands (shalach)'         'come before (bo)'
'into your hand I commit my spirit'       'to be incensed'
'profane / violate (chalal - he violated his covenant)'
"'God has forgotten, he won't see'"
```

These are literal dictionary gloss text (from `import_seed.py`'s migration of the old lemma
inventory) — parenthetical transliterations (`(raah)`, `(shalach)`, `(nabat)`, `(chalal)`), colons,
slashes, full sentences. **A "no special characters/transliteration" rule would fail on nearly every
non-null row that exists today.** Some values are already clean single words (`wrath`, `peace`,
`heart`, `violence`) — those look like what the rule wants; the messy majority are migration-carried
gloss text, not a formatting bug in new writes.

## 3. `lemma_key` must exist in `strong` — conflicts with 52.3% of rows, and may contradict a
   founding principle of the candidate system, not just be missing data

**46,003 of 87,922 rows (52.3%)** reference a `lemma_key` with no matching `strong.strongNumber` row —
including extremely high-frequency ones: `H0430` ("God"), `H3068` ("the LORD"), `H7200` ("to see").

**Why, and why this may not be a bug to fix:** `strong` is populated incrementally, one row per
Strong's number, only when some *registered word*'s `new-word` build actually fetches it
(`raw.detail`) — today, 3,463 rows. `candidate_seed`/`span_candidate` come from a much larger,
**independent** migration (2,086 distinct candidate lemmas) that was deliberately built *not* gated on
the registry or on `strong` being populated — this is the already-established "candidate seed is
independent of the registry, over-inclusive by design, the lexical stage is the real test" principle
(matches the existing `registry_match`-is-a-double-control pattern in `candidate.py`'s own `seed()`
step, not a hard block). Making `lemma_key ∈ strong` a **hard** rule would block `candidate.set()` for
over half of all real candidates, including "God" and "the LORD" — that's very likely not what's
wanted, but I'm asking rather than assuming.

---

## What I'd recommend, pending your confirmation

Treat all three as **validity/quality rules that report, not block** — this is exactly the gap `candidate.py`
was already flagged as missing (the earlier module audit: "quality: NONE" for candidate). Concretely:
a new check (in `configmaint.validate`, or a `candidate`-specific report) that flags, per book or
overall: candidates with null/messy `candidate_tag`, and candidates whose `lemma_key` has no `strong`
row yet (a **third double-control signal**, alongside the existing `registry_match` one — "this
candidate hasn't had its Strong's detail-fetched by any registered word yet").

If instead you want these as **hard, blocking rules** (reject a write rather than just report it), that
implies either backfilling/cleaning the existing data first (what should a null or messy tag become?)
or changing `candidate.set()`'s scope (only stamp candidates whose `strong` row already exists — a real
behavioural change to the over-inclusive design, not just a validation addition). Which do you want:
report-only (my lean), or hard-blocking (with the cleanup/scope question that implies)?
