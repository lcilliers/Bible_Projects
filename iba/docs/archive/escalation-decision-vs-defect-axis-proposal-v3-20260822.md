# Escalation core model — decision-vs-defect axis (v3)

**Escalation #798** (`from_id=753`). Replaces v2. §1/§2 stay agreed, unchanged from v2 — not
repeated below except where they're affected. This version: full §3 review (no site left as
"needs review"), §4b/§4c fully re-specified per your correction, §5.4 answered with real examples,
and a build sequence with a test per stage. Still nothing built.

---

## §3 (revised) — every `escalate()` site, fully reviewed and classified

**The unifying rule, found doing this review, not assumed going in:** every one of the 9
handler-authored `escalate()` calls is, by construction, `decision_required` — with no exceptions.
A handler only calls `escalate()` when its own logic has already decided it *cannot* resolve the
situation itself; that is the definition of a decision point. None of the 9 represents "Claude got
the code wrong" — they're all "the running operation found something outside what's already
specified, needs a human read."

| Site | What it actually asks | Why `decision_required` |
|---|---|---|
| `candidate.py:288` (`candidate.validate`) | Quality findings across seed/span/gloss tables — "your call whether it's acceptable as-is or needs action" | Explicit acceptability judgment on data state |
| `candidate.py:416` (`candidate.curate`) | A proposed single-row correction to `candidate_seed` — "approve to apply, reject to decline" | A content decision, same shape as `configmaint.propose` but for a different table |
| `candidate.py:702` (`candidate.load`) | Exception rows — format failures, unresolved lemma matches, gloss mismatches | Nobody has decided how to handle these specific exceptions yet |
| `cluster.py:125` (`cluster.validate`) | Cluster-assignment exceptions (no-word-link, sibling conflicts) | Same — "neither is auto-resolved" |
| `configmaint.py:406` (`configmaint.validate`) | Coherence findings in `cfg_*` itself | Open questions about the config's own current state |
| `lexicon.py:214` (`lexicon.validate`) | Parse-coverage/value-quality gaps | Same shape |
| `narrative.py:187` (narrative generation) | Real-money API spend authorization | Spending a real, uncapped cost is always a decision — per this project's own standing cost-awareness rule, never auto-approved |
| `passage.py:332` (passage distribution) | "Is this distribution acceptable... an outlier?" | Pure judgment call |
| `raw.py:94` (word registration, zero strongs) | "Register anyway, or reject?" | Genuine edge-case judgment |

**Consequence for §2:** `resolution_kind` doesn't need to be threaded through these 9 call sites as
a *choice* — it can be hardcoded `decision_required` at each site, since the classification is
structural, not per-instance. Simpler than v2 implied.

### The one real exception: `reports.py:65` (`validation_word`/`validation_book`) — answering §5.4

You asked for concrete examples of what actually fires this, since it looked like it might be pure
notification. It genuinely is a mix — checked `iba/app/validation.py` directly, not assumed:

- **Looks like a real code bug (self_correctable-shaped):** `"data tables present"` — FAIL if a
  table `cfg_table` says should exist doesn't. `"latest run complete"` — FAIL if a run for this
  word never reached `state='done'`. These usually mean something in the build/dispatch pipeline
  didn't do what it was supposed to — an execution defect against an already-settled design, not a
  new judgment call.
- **Looks like a genuine open question (decision_required-shaped):** `"registry source set"` — WARN
  if `word_registry.source` is empty; this may just mean the word's source hasn't been filled in
  yet, not that anything is broken. `"passages needing review (> review_over verses)"` — WARN with
  its own comment *"a long run may be several passages — confirm the rule"*, explicitly asking for
  a judgment, not reporting a defect.
- **Genuinely ambiguous without more context:** `"span recovers strong_verse"` — FAIL if some verse
  spans weren't recovered by the parser. Could be a parser bug (self_correctable) or a legitimately
  hard passage the parser was never expected to handle (decision_required) — the check alone
  doesn't say which.

**So this one site can't take a hardcoded `resolution_kind`** — unlike the other 9, `overall !=
PASS` bundles checks from every category above into one escalation. Making this precise would mean
`_validation_outcome()` inspecting *which* specific checks fired (not just the pass/warn/fail
count) and classifying per-check — real code, not a config value. Flagging this as its own,
smaller open question rather than guessing a default (see §6.1 below).

### The 3 dispatcher-tied `raise_()`/`esc_raise()` sites in `run.py`

- **Line 192 (crash)** and **line 244 (report-stop)**: an uncaught exception or a hard `fail()`.
  Same ambiguity as the validation-check case — could be a genuine gap (decision_required) or
  Claude's own slip against settled logic (self_correctable) — the crash-wrapper itself has no way
  to know which. **Open question 6.2.**
- **Line 223 (pause-continue)**: carries whatever `resolution_kind` the handler's own `escalate()`
  call supplied — no separate decision needed here, it's a pass-through.

---

## §4c (settled) — what `decision_required` does to a run

Per your correction, precisely:

1. The run terminates immediately, `run.state = 'failed'`.
2. An escalation is auto-raised, **`type` forced to `issue`** regardless of what type the raising
   code would otherwise have picked (matches the existing type model: *"an issue is about
   exploring/debating/considering options"* — #6 v3) — with the full detail already gathered
   (question/context/report path) attached, same content as today's `escalate()` payload.
3. Nothing resumes this specific run. Verifying the fix means **starting a fresh run** once the
   issue escalation reaches a settled, approved answer — that fresh run **is** the test.

## §4b (re-specified) — `self_correctable` has no decision at all

Corrected understanding, replacing v2's wrong assumption that it reuses today's `AnswerRun`:

- **No `approve`/`reject`/`revise`/`hold`/`noted` vocabulary.** `AnswerRun` is never invoked for a
  `self_correctable` item — a researcher is structurally never the one who fixes code.
- **Flow:** raised → Claude applies the fix → Claude records what was wrong and what changed
  (the resolution) → escalation closes. No approval gate at any point.
- **If the escalation paused a run** (a crash mid-execution, judged `self_correctable`): once
  fixed, Claude re-runs the *same* command/`run_id` — this is the existing informal pattern from
  this session (#765, #769: fix, retry, succeeds) made into the formal mechanism, not something
  new. This is what distinguishes it from `decision_required`, which never resumes the same run.
- **The governing boundary, quoted precisely because it's the load-bearing rule:** *"if a config is
  already as per specification, there is no need for re-approval. an approved specification is the
  approval — on the condition that Claude is not allowed to make changes under the auspices of a
  specification where the item was never specifically specified."* Concretely: `self_correctable`
  is valid **only** when the fix makes reality match something *already, specifically* approved
  (my `key=NULL` mistake vs. the already-approved `prose.extractor_version` proposal is the
  textbook case). The moment a fix requires Claude to decide something the prior approval didn't
  cover, it is `decision_required`, unconditionally — this is not Claude's judgment call to make in
  the moment.

**Mechanism implication, new since v2:** `self_correctable` items need their own resolve-and-close
transaction (Claude-authored, no researcher-facing decision step) — not a repurposed `AnswerRun`.
Likely a small new function alongside `raise_()`/`answer_for_run()` — naming/shape not yet decided,
flagged in §6.

---

## §6. Open questions — narrowed since v2

1. **`reports.py`'s `validation_word`/`validation_book`** (the one call site needing real per-check
   logic, not a hardcoded default) — build this now as part of the same pass, or treat it as a
   follow-on once the core mechanism exists and can be exercised against it?
2. **Crash/report-stop default** (`run.py` lines 192/244) — same ambiguity as validation checks.
   Proposal: default `decision_required` (the safe, "don't assume it's fixable" choice) at raise
   time; if Claude's own investigation afterward shows it's genuinely `self_correctable`, that
   becomes the *resolution* recorded on the (still `decision_required`, still `type=issue`) item —
   i.e. don't retroactively change the classification, just resolve it fast once investigated.
   Confirm or correct this default.
3. The `self_correctable` resolve-and-close mechanism's exact shape (new function name/CLI verb) —
   not designed yet, deliberately, until §4b's model itself is confirmed.

---

## §7. Build sequence and tests — staged, per your instruction

**Stage 1 — pure config, no code.** `cfg_behaviour_rule` (§1, unchanged from v2), `cfg_enum
resolution_kind`, the `cfg_escalation_requirement` row.
*Test:* `configmaint.validate` runs clean; a scratch-DB manual raise without `-ResolutionKind`
is correctly refused with the new requirement's message.

**Stage 2 — `escalation.py` internals.** `raise_new()`/`raise_()` require and store
`resolution_kind`; `decision_required` forces `type='issue'` at creation; the new
`self_correctable` resolve-and-close function (per §6.3's decision) built; `Update()`'s dispatcher
refusal gets the `decision_required` carve-out from §4b of v2 (unchanged).
*Test:* scratch-DB round trip for both kinds — raise each, resolve each through its own path,
confirm state/type land correctly; confirm `AnswerRun` is refused (or simply irrelevant) for a
`self_correctable` item.

**Stage 3 — `run.py`.** Pause-continue/crash/report-stop branch on `resolution_kind`:
`decision_required` → terminate `failed` + auto-raise the `issue` (§4c); `self_correctable` →
stays retryable via same-`run_id` re-invocation after Claude's fix.
*Test:* two real work-package runs — one forced into each path — confirm the run table and the
escalation both land in the states §4b/§4c describe.

**Stage 4 — the 9 `escalate()` sites + `reports.py`.** The 9 structural sites get
`resolution_kind='decision_required'` hardcoded (§3's table). `reports.py` gets the per-check
classification, if §6.1 says build it now.
*Test:* re-run each affected step live against real data, confirm the escalation it raises carries
the right `resolution_kind` and (for the 9) lands as `type='issue'`.

**Stage 5 — CLI/PS surface + docs, same unit of work as whichever stage a mechanism lands in** (not
a separate stage — matches the existing standing rule that docs update alongside the code, not
after it). `-ResolutionKind` on `Escalation.ps1 -Action Raise`; `--resolution-kind` on the Python
CLI; `GOVERNANCE.md`/`USER-GUIDE.md`/`BUILD.md` updated as each stage above lands, not batched to
the end.
