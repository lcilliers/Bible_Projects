# Registry prompts — what the test exposed, and the fixes

> Triggered by the test run `New-Word.ps1 -Word [hypocrisy] -Source "testing: rerun existing word"`.
> The researcher asked: (a) the prompts are confusing — what does "mid-build" mean; (b) show what
> the engine recorded; (c) walk through what happens when an *existing* word is entered.

---

## 1. What the engine actually recorded

Straight from `iba/app/db/iba.db`:

**`word_registry`**

| id | word | status | source |
|----|------|--------|--------|
| 1 | `hypocrisy` | `raw-complete` | gap scan 2026-07-18 |
| 2 | `[hypocrisy]` | `proposed` | testing: rerun existing word |

**`escalation`** (id 2, the one your test raised)

- word `[hypocrisy]`, at `registry.create`, state `raised`, answer `null`
- preset: `maps_to_strongs: 5`, strongs `G0505, G5272, H2612, H2519, G4942`,
  **`already_held: [all 5]`**, `meanings_total: 17`

**`run`**

| run_id | word | state | resume_point |
|--------|------|-------|--------------|
| …033615… | hypocrisy | paused | registry.create |
| …033616… | hypocrisy | **running** | raw.validate |
| …035851… | `[hypocrisy]` | paused | registry.create |

### Three real problems this exposes

1. **The brackets were taken literally.** You typed `-Word [hypocrisy]` (the guide's `<word>`
   placeholder, entered verbatim), and the app stored a **new, different word** `[hypocrisy]` —
   distinct from `hypocrisy`. That is why it did not recognise it as existing. **The app does not
   normalise or validate the word** (trim, strip stray punctuation, case) before registering it.

2. **The near-duplicate was detected but not surfaced.** The escalation preset shows
   `already_held: [all 5 strongs]` — every Strong's this "new" word maps to is *already in the DB*
   from `hypocrisy`. That is a strong signal it is a duplicate/typo, but it is buried in the preset
   and the prompt said nothing about it.

3. **A completed run is left marked `running`.** Run `…033616…` finished (it built `hypocrisy`
   to `raw-complete`) yet its row still says `state=running`, no `ended_at`, no `outcome`. The
   dispatcher does not close the run row on completion.

---

## 2. What "mid-build" means — and why the prompt is wrong

The `registry.exists` handler only *stops* a word when it is fully built:

```python
BUILT = ("raw-complete", "signed-off")
def exists(ctx):
    row = get word_registry by word
    if row and not row["deleted"] and row["status"] in BUILT:
        return fail("word-exists", …already built…)
    return ok("word is new or mid-build")   # <-- everything else lands here
```

So **one vague message covers four genuinely different states**:

| the word is… | status | what the message says | what it should say |
|---|---|---|---|
| never seen | (no row) | "new or mid-build" | "not in the registry — will propose it" |
| awaiting your approval | `proposed` | "new or mid-build" | "already proposed — will resume its approval" |
| approved, not yet built | `approved` | "new or mid-build" | "approved — will build its raw layer" |
| previously rejected | `rejected` | "new or mid-build" | "was rejected before — proposing again" |
| already built | `raw-complete`/`signed-off` | (stops) "already built" | (stops) "already built" ✓ |

"mid-build" is internal shorthand for *"in the registry but not yet `raw-complete`"* — i.e. proposed
or approved. It is jargon, and worse, it is even printed for a **rejected** word (which is then
stopped one step later at `registry.create` — so the true state is known but not told at the point
it is known). **This is the confusing prompt you flagged.**

---

## 3. Walk-through — what happens when an *existing* word is entered

"Existing" is not one path. It forks on the word's **status**:

### (a) Already built — e.g. `hypocrisy` (status `raw-complete`)

```
registry.exists   report-stop   'hypocrisy' is already built (status raw-complete)
STOPPED — the word already exists; use a refresh run, not new-word
```

`exists` returns `fail("word-exists")`; the dispatcher resolves
`on_fail(registry.exists, word-exists)` → path **report-stop** (from `rules.json`) → exit code 3 →
PowerShell prints STOPPED and halts. **Nothing is re-built.** (There is no refresh run in this
slice yet — that is a later operation.)

### (b) Proposed — e.g. `[hypocrisy]` right now (status `proposed`)

```
registry.exists   ok             (…in the registry, awaiting approval…)
registry.create   pause-continue …still waiting for your approval…
PAUSED
```

`exists` passes (not built); `registry.create` sees `proposed`, looks for an answer, finds none, and
re-raises the pause. Answering `yes` then re-running resumes and builds it.

### (c) Approved but not built (status `approved`)

```
registry.exists   ok             approved — will build its raw layer
registry.create   ok             '…' already approved (id N) — proceeding
raw.discover … raw.validate   ok
COMPLETE
```

`create` proceeds idempotently and the raw layer builds. This is the normal **resume-after-yes**
path.

### (d) Rejected (status `rejected`)

Today: `exists` says "new or mid-build" (wrong), then `registry.create` stops with
`word-rejected` → report-stop. The stop is correct; the earlier message is not.

---

## 4. Proposed fixes (for approval before I apply)

**A. Make `registry.exists` say the true state (messages only, low risk).** Replace the single
"word is new or mid-build" with the state-specific messages in the table in §2. No behaviour change —
same steps run — the operator just sees what is really going on.

**B. Surface the near-duplicate in the approval prompt (low risk).** When `already_held` covers
*all* of a word's strongs, add a line to the escalation question, e.g.
*"⚠ all 5 strongs are already held — is this a duplicate/typo of an existing word?"* So a stray
`[hypocrisy]` is caught by you at the gate.

**C. Normalise + validate the word at entry (needs your ruling).** Before registering, trim
whitespace and reject or strip stray characters. **Design decision for you:**
   - trim surrounding whitespace — yes (safe, always right);
   - strip surrounding brackets/quotes/punctuation — probably;
   - lower-case — ? (the registry is English inner-being words; case-insensitive dedup would have
     caught `Hypocrisy` vs `hypocrisy`, but changes stored form);
   - reject a word that is not letters/spaces/hyphen — ? (would have rejected `[hypocrisy]` outright
     with a clear error instead of registering it).

**D. Close the run row on completion (bug fix).** The dispatcher should set
`run.state=complete`, `ended_at`, `outcome` when the last step succeeds. Right now completed runs
stay `running`.

**E. Clean up the test residue.** `[hypocrisy]` (id 2) and its open escalation are test noise —
delete once you have seen this, so the registry is clean.

Fixes **A, B, D** are clearly correct and I recommend applying them together. **C** needs your
normalisation ruling. **E** is a one-line cleanup on your say-so.

---

## 5. APPLIED — 2026-07-18

The researcher approved all fixes and ruled on C: *"adding a new word should do a more sophisticated
validation to check if the word already exists or in fact is a true new word, if not sure, then ask
for confirmation. We definitely need a method to remove test data."* Update/delete operations are
later work, not now. All applied and verified end-to-end:

- **A — true-state messages.** `registry.exists` now reports the actual state (new / awaiting
  approval / approved-not-built / previously-rejected / already-built) instead of "new or mid-build".
  Verified: `[hypocrisy]`→already-built stop; `malice`→"not in the registry — a new word".
- **C — normalise + case-insensitive dedup.** New `lib/words.py::normalise` (config setting
  `registry.strip_ends_pattern`) strips surrounding stray characters and whitespace; all word
  matching is case-insensitive. Applied once at the dispatch boundary (`run.py`). `[hypocrisy]`
  now resolves to `hypocrisy` and is caught as the existing word. Case preserved in storage.
- **B + C-confirm — duplicate check.** `_possible_duplicates` finds existing words holding the same
  strongs; when an existing word holds ALL of them the approval becomes an explicit
  *"shares ALL N strongs with '<word>' — register as separate anyway?"* confirmation. Verified via
  unit test (hypocrisy's 5 strongs) and that `malice` (9 strongs, none held) gets no false warning.
- **D — run closes on completion.** The dispatcher marks the run `done` (+`ended_at`,`outcome`) when
  the last step in the sequence completes. Verified: `malice` run ended `state=done`.
- **E + "method to remove test data".** New `tools/purge_word.py` — dry-run by default, `--yes` to
  delete; matches the word **literally** (targets malformed residue), removes only the word's own
  rows, leaves the shared raw layer. The `[hypocrisy]` residue (id 2) was purged.

Rejected words are now **re-proposed** on an explicit re-add (a reconsideration still needs fresh
approval), rather than hard-stopped. Guide updated (§3–§5, §9).
