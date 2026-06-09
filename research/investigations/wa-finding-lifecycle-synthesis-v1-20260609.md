# Finding lifecycle prototype — formulate → write → correct (synthesis)

> **Investigation · v1 · 2026-06-09 · CC.** Prototypes the next cycle the researcher asked for: **formulating
> findings, writing them, and correcting existing findings.** 8 (term, verse) pairs taken through the
> *complete* meaning stage into findings; written to a prototype store; then two clarification-driven
> corrections applied with full provenance. Artifacts: store
> [v1](wa-m01-findings-store-v1-20260609.json) → [v2](wa-m01-findings-store-v2-20260609.json) ·
> correction run [wa-finding-lifecycle-run-v1](wa-finding-lifecycle-run-v1-20260609.md) ·
> `scripts/_prototype_finding_lifecycle.py`. **Read-only prototype store — NOT the DB.**

---

## 1. Formulation — what a finding *is*

One finding per **(term, verse)** (characteristic = typed term-in-verse). Each carries the typed lexical
meaning + the **resolvable tier findings**, with **`stated-silent`** wherever the verse doesn't resolve a
tier (never induced). Examples from the batch:

- **Deu 28:67 `pa.chad`** — `ACTION · Qal · "to be in dread"`; **T2 = HEART** (a *direct* locus hit —
  "the dread your heart shall feel"); T3 = affect. A clean ACCEPT where the verse even fills T2.
- **Eze 12:18 `de.a.gah`** — `STATUS · "anxiety"`; T3 = affect; **T2 = stated-silent** (no locus in the
  verse — stated, not guessed).
- **1Ch 10:4 `ya.re`** — `ACTION · Qal · "to fear → dread"`; provenance = *clarification:threat-object→dread*
  (a signal genuinely read in the verse).

So the finding records: `term · verse · cluster · type · mode · lexical_meaning · tiers{T7.1,T1.2,T1.4,T2,T3,
T1.3} · triage · provenance · status · corrections[]`. The tier values are the **answer**, `stated-silent`
(verse doesn't resolve), or `stated-unresolved` (escalated).

## 2. Writing — per-term findings, saved to the cluster

A verse-read emits **one finding per in-scope term**; each is written to its term's cluster (a multi-term
verse populates several clusters from one read — verse-coverage / no double-work). The store is the prototype
of that table. Every finding carries **provenance** (mechanical / clarification:X / api / researcher) and a
**status** (`draft` → `corrected` / `confirmed`).

## 3. Correcting — the two cases that matter (both demonstrated)

**(a) A FORCED finding un-induced — `M01-0007` (1Sa 4:7 `ya.re`).** Initially ACCEPTed as *reverence* by the
induced `god-present→reverence` rule. The clarification is **revoked** (it induces) and replaced by reading
the verse's actual posture — "the Philistines were afraid … *Woe to us!* … who can deliver us from these
mighty gods?" = **dread of God-as-threat**. Finding corrected `to revere → to fear/dread`, provenance now
*reads a present signal*. This is **state-not-induce enforced as a correction.**

**(b) An ESCALATED finding resolved — `M01-0008` (1Ki 8:40 `ya.re`).** Initially escalated (the object, God
addressed as "*you*", wasn't detected → genuine *detection gap*, not silence). A new clarification —
*god-as-"you" in a covenant-obedience-life frame → reverence* — resolves it: `ESCALATE → ACCEPT`, shade =
reverence. This is **the clarification library raising the ACCEPT rate** over time.

Every change is recorded in the finding's `corrections[]` (`from / to / reason / clarification / date`), and
`status → corrected` — fully auditable and reversible in principle.

## 4. What the cycle reveals (design notes)

1. **Findings are drafts, sifted iteratively** (matches the documented finding lifecycle) — the store is
   append-and-correct, never overwrite-in-place; the history is the audit trail.
2. **Clarifications are the correction engine** and they **propagate**: revoking `god-present→reverence`
   should re-evaluate **every** finding that used it, not just this one. → the real schema needs a
   **clarification library** with back-references from findings (which clarification justified each), so a
   library change triggers targeted re-evaluation.
3. **state-not-induce is enforceable**: an induced finding was *flagged at formulation* ("INDUCED — flagged
   for review") and *corrected* later — the flag is the hook.
4. **Two correction triggers** seen: (i) a clarification is **revoked/added** (re-evaluate matching
   findings); (ii) a **detection gap** is fixed (escalate → resolved). A third (not shown) is a **new verse**
   changing a term's reading — handled the same way.

## 5. Refinements noted (for the real build)

- **Suppress no-op corrections** (the prototype logged a `triage ACCEPT→ACCEPT` non-change).
- **Reason at the directive level**, not duplicated per field.
- **Clarification library as a first-class store** (id, rule, signal-it-reads, validated?, supersedes) with
  finding↔clarification links, so corrections propagate by *clarification*, not by hand-listed ids.
- A **`flagged_for_review`** status distinct from `draft` for induced/low-confidence findings, so the audit
  surfaces them.

## Verdict
The **formulate → write → correct cycle works** and naturally carries provenance + correction history. The
key build pieces it implies: the **finding record** (§1), the **per-term write to cluster** (§2), and a
**clarification library** with finding back-links so corrections **propagate** (§4.2). With those, "augment +
correct" is mechanical and auditable, and **state-not-induce is enforced at both formulation and correction.**
