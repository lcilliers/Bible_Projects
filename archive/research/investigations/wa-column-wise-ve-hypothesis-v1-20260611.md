# Column-wise VE extraction — hypothesis, timing, and the meaning-duplication diagnosis

> 2026-06-11. Working note developing le Roux's hypothesis that the verse-read should be reorganised from
> **row-wise** (read a verse, answer all 14 VE dimensions + write a meaning, per verse) to **column-wise**
> (answer each isolable VE question across the whole corpus as one focused pass). Includes the timing
> instrumentation finding and the evidence that the meaning paragraph duplicates-then-fabricates.

---

## 1. The hypothesis

- **Current (row-wise / verse-complete):** read a verse once → answer *all ~14 VE dimensions* for *all
  in-scope terms* → write a meaning paragraph. Process the corpus verse-by-verse. ~1 day per cluster,
  ~40 days outstanding. Every review surfaces errors and omissions.
- **Proposed (column-wise / question-complete):** answer each *isolable* VE question across the **whole
  corpus** as a single focused pass; only the genuinely interdependent questions stay as a per-verse read.

### Why it holds
- **Consistency (the larger win).** Row-wise re-derives 14 rubrics ~31,000 times → drift is structural;
  that is the "errors and omissions on every review." A single-question pass holds **one rubric stable** and
  makes review *tractable* (inspect all of one dimension at once — would have caught the `boulomai`=cognition
  and `ya.re` god-heuristic induces in one place). Proven precedent: faculty errors happened *because* faculty
  was decided per-cluster/per-verse; one per-term faculty rubric would have prevented them.
- **Time/cost.** Several dimensions are **mechanical** — answerable from STEP morphology / lexicon / book
  metadata with **no verse read** (sense-range, faculty per-term, type, literary setting, compound). Column-wise
  lets those be *scripted* and never touch the metered read. The M-vs-R work confirms the mechanical
  sense-range is **constant per term** — re-deriving per verse is waste.

### The guardrail
**Do not split the interdependent dimensions into separate column-passes.** If each needed a read and got its
own corpus pass, you would re-read every verse N times and *lose* time. Column-wise applies only to the
**isolable** dimensions; the irreducible core stays one grouped read.

### Three lanes (proposed; validate against the catalogue)
| lane | dimensions (proposed) | how | reads verse? |
|---|---|---|---|
| **A — mechanical / term-level** | sense-*range*, faculty, type, constitutional-location, literary-setting, compound | scripted corpus passes, one rubric each | **no** |
| **B — sense-application spine** | VE-01 sense *applied here* (+ meaning anchor) | one corpus-wide read pass; one question | yes, once |
| **C — interdependent core** | origin, mode, immediate-response, produces-effect, relational-implication, purpose, typology | grouped per-verse read against the *fixed* sense+meaning | yes, grouped |

Once sense+meaning is fixed (B), A+B cover **~9–10 of 14** ("most of them in isolation"). Lane C is exactly
the **cause/effect/relationship/dynamics** cluster — also the gap flagged on 2026-06-10 and the weakest data.
So this concentrates the expensive holistic read where it is actually needed.

### Risks (honest)
1. **Re-read multiplication** — mitigated by keeping Lane C grouped (the guardrail).
2. **Cross-dimension coherence** — Lane B must run before its dependents; final coherence check.
3. Workflow/sequencing change, **not** schema change — `finding` + `finding_question_link` already supports
   populating any single question corpus-wide (already done for obs-395 mechanically).

---

## 2. Can the engine time a/b/c/d? (initial-read / dimensions / meaning / write)

**No, not as it stands.** Instrumentation is coarse wall-clock only:
- `engine_stream_checkpoint`: `started_at`/`completed_at` per term-stream + `rows_written`.
- `engine_run_log`: run-level start/complete.
- Per-batch model-call seconds (`time.time()` around `call_api`) — **printed, not stored**.
- No timers around input-read or DB-write.

**(b) and (c) are physically inseparable today** because the 14 dimensions *and* the meaning are produced in
**one streamed model call**: the model emits the fields → `MEANING:` → `SELFAUDIT:` in one generation. No clock
boundary exists between "answering dimensions" and "compiling meaning". (a) and (d) are script-side I/O folded
into the inter-call gap, untimed.

**Proxy available now (generation time ∝ output tokens), measured across 8,367 records:**

| phase | avg chars | share of generation |
|---|---|---|
| the 14 dimensions | 397 | **~40%** |
| the meaning paragraph | 590 | **~60%** |

The **meaning paragraph costs more than all 14 dimensions combined.** Input-read is near-free (prompt cache-read);
write is small DB I/O.

**Tie to the hypothesis:** you can't measure dimensions-vs-meaning separately *because the architecture fuses
them*. Decomposing into separate passes makes each pass's wall-clock = that phase's cost, for free.

**Cheap option without restructuring:** add `t_read`, `t_api`, `t_write` timers per batch → pins (a), (d), and
total (b+c). Splitting (b) from (c) needs either the token-share proxy or two calls.

---

## 3. The meaning paragraph duplicates — then fabricates (evidence)

le Roux's diagnosis (2026-06-11): the meaning process *largely duplicates* the 14-dimension work; some
observations live *only* in the meaning; and re-reading the whole (partly incomplete) material each time forces
"making up some stuff because it's needed" or re-doing because it's incomplete — a 4-month vicious circle.

**Confirmed by the pipeline's own design.** The system prompt orders the meaning to reflect *every non-null
field* ("Every non-null field above must be reflected in the paragraph"); `SELFAUDIT` and `audit_paragraph()`
check **field → paragraph** only. There is **no paragraph → field** check, so duplication is *enforced* and
extra prose is *unaudited*.

**Three real M02 records show the three patterns:**

- **Mat 2:16 `thumoō` — pure duplication.** The meaning restates the dimensions, naming the faculty tags
  verbatim ("Engaging affect and agency… the order to kill all Bethlehem's male children"). Adds nothing
  structurally absent. ~60% of generation re-wrapping the 40%.
- **Mar 3:5 `orgē` — observation only in the meaning.** "fused with grief (sullupeō)… hardness of heart
  (pōrōsis)" — the anger-grief fusion and co-occurring Greek terms are *grounded and valuable* but sit in **no
  dimension**: unqueryable, unaudited, lost to the structured layer.
- **Rom 1:18 `orgē` — imported filler.** "Paul makes this revealed orgē the dark backdrop against which the
  gospel's righteousness shines" — synthesis pulled from Rom 1:16-17, *not in this verse* (the "make up some
  stuff" import). The dimension `origin=within-person` for the wrath *of God* is also wrong, and the prose
  smooths over it.

**Why this is the vicious circle.** The meaning is a **generative free-prose step**; free prose abhors a
vacuum. Where dimensions are incomplete it *invents* to fill (the gospel backdrop); where it notices something
with no slot it *adds prose* (the co-terms). Each re-read notices/imports *different* things → the meaning
differs every time → reads "inconsistent/incomplete" → re-do. It also **falsifies the premise** that "value is
safely mirrored as ~14 queryable findings" — value is in fact prose-locked in the meaning.

---

## 4. Structural fix — reverse the primacy

1. **Dimensions become PRIMARY** — disciplined, option-list, silence-valid, extracted **column-wise** with one
   stable rubric against **complete inputs**. Bounded + grounded ⇒ re-reading returns the *same* answer ⇒ the
   variation stops.
2. **The meaning becomes DERIVED** — a deterministic roll-up of the fixed dimensions. If it can only restate
   what is structurally present, it **cannot invent**; the import vector closes (cross-verse synthesis belongs in
   the SYNTH layer, not a verse meaning).
3. **Promote genuine meaning-only observations to dimensions** — the data names the missing fields: a
   *paired/fused-with* field, *key co-terms*, and the **cause→effect** dynamics. Capture the real value
   *structurally* (queryable, auditable), not as undisciplined prose.

Column-wise is therefore not only faster and more consistent — it is **the mechanism that breaks the circle**:
it separates *disciplined extraction* (must be stable) from *generative prose* (where invention and variation
enter), and stops paying ~60% of every read for prose that duplicates-then-fabricates.

---

## 5. Suggested next steps (no build yet)
- **Prototype one isolable dimension corpus-wide** (faculty — purely term-level, already burned us) and measure
  consistency + time vs a verse-complete slice. Cheap test of the whole hypothesis.
- **Formally classify all 14 VE fields into Lanes A/B/C** against the catalogue for validation.
- **Widen the duplication read** beyond 3 records if more evidence is wanted (read, not stats).
- Decide whether the derived-meaning roll-up is templated (deterministic) or a cheap constrained pass.
