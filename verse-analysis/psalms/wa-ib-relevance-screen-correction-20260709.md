# IB-relevance screen — method correction (God-chars → qualifiers)

**Date:** 2026-07-09 · **Status:** DECIDED — Option A (screen forward; done corpus left as-is) · embedded
**Raised by:** researcher (le Roux) · **Severity:** systemic (affects ~24% of reread chars)

> **Decision (2026-07-09, researcher):** **Option A.** The analysis already done is *not
> fundamentally wrong* — it only adds burden — so the done Psalms corpus (Ps 1–36, 78) is
> **left as-is, flagged not reworked**. The IB-relevance screen (Screen 0) is applied **forward
> from Ps 37** and **properly embedded** (below). **Reading-unit change:** because most verses
> carry no IB char once God-content is screened out, we do **not** read whole chapters or
> chapter-blocks — we anchor on each surviving **human IB char** and read **its passage** (its
> related verses) **together**. Expect to *not* read nearly every verse of Psalms.
>
> **Embedded in:** cycle instruction `wa-characteristic-role-lexical-cycle-authoritative-v1`
> (Screen 0 in §5, rule 0 in §11); `scripts/_reread_finish_v1` (loud `IB-SCREEN WARNING` on any
> God-bearer characteristic); memory `feedback_ib_screen_first_god_is_arena`; catalogue note.

---

## 1. The correction

The study's lens is the **human inner being (IB)**. God is the **arena**, not the subject —
he enters analysis as a **source**, a **target**, or as **qualities** bearing on the human
IB. God's own attributes and actions are **not** characteristics.

**The screening test — the FIRST assessment for every candidate char:**

> Is this candidate about the **human** inner being (a faculty, state, disposition, or
> inner-driven act of a human — the psalmist, the wicked, mankind)?
> - **Yes** → **characteristic** (full ledger).
> - **No — it is wholly God's** (his attribute / quality / action) → **qualifier**.
>   It gets no characteristic ledger; it enters the relevant human char as
>   **D3 source**, **D7 target**, or a **quality / manner**.

A purely hymnic verse about God may legitimately contain **no** characteristic at all.

### Examples

| Span | Old (wrong) | Corrected |
|---|---|---|
| God's `chesed` (steadfast love) | characteristic, bearer=God | **qualifier** — the thing the human *trusts in / hopes in* (D7 target / source of the human char) |
| `yasha` "God saves" | characteristic, bearer=God | **qualifier** — source of the human's rescue/joy |
| God's `kavod` / `hadar` glory | characteristic | **qualifier** — target of the human's worship |
| God's `aph` wrath | characteristic | **qualifier** — the human's *terror/dismay* is the IB char; God's wrath qualifies it |
| God's `tsedaqah` / `emunah` | characteristic | **qualifier** — quality the human appeals to / rests on |
| human `batach` trust, `yare` fear, `chasah` refuge, `nefesh`/`lev`, `samach` joy, `qavah` wait | characteristic (correct) | **characteristic** — the human response IS the IB; God is its target |
| the wicked's malice, deceit, corrupt heart, no-fear-of-God | characteristic (correct) | **characteristic** — the wicked's inner life is human IB (negative) |

This is a **restatement** of an existing principle
(memory `feedback_lens_is_inner_being_process_not_god_relation`,
`project_focus_points_scripture_as_data_source`), drifted from during the rapid re-read.

## 2. Scope of the drift

Diagnostic (`ve_lexical` reread rows, `ve_nr=105` bearer naming God/LORD, on
`role='characteristic'` spans):

- **221 char-spans** across the reread carry **God as bearer** — candidates to downgrade
  to qualifier. ≈ **24%** of the 930 reread characteristics.
- **Every chapter is affected** (1–36 + 78). Heaviest: Ps 78 (18), Ps 18 (15), Ps 25 (17),
  Ps 31 (13), Ps 22 (10), Ps 33 (9), Ps 36 (9), Ps 9 (8), Ps 19 (8).
- Note: 221 is a floor — God-attribute chars where I left bearer as "none"/other are not
  captured by the query, so the true count is somewhat higher.

## 3. Consequence for the gates

Add the **IB-relevance screen as gate 0** (before G10/G6): a span only qualifies for the
mandatory characteristic ledger if it passes the IB screen. God-bearer spans are
reclassified `role='qualifier'` and re-anchored as source/target/quality on the human
char they serve (or dropped to pure context where the verse has no human char).

## 4. Decision needed — how to fix the done corpus

| Option | What it does | Cost |
|---|---|---|
| **A. Screen forward only** | Apply the IB-screen from Ps 37 on; leave the 37 done chapters flagged for a later reclassification pass. | cheapest now; leaves 221 mis-coded spans in the corpus until later |
| **B. Reclassification pass now (recommended)** | Before continuing, sweep the 37 done chapters: flip God-bearer chars to qualifier, re-anchor each on its verse's human char. Semi-automated + per-chapter judgement. | moderate; corpus clean before proceeding |
| **C. Full re-read** | Re-read all 37 chapters with the corrected lens from scratch. | highest; most thorough |

**Recommendation: B** — the content is fresh, so re-anchoring is fast; it stops the drift
propagating and keeps the corpus coherent before the book grows further. In all cases the
IB-screen becomes a permanent gate 0 and is written into the cycle instruction + catalogue.
