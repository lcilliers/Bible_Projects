# M11 — Park notice (methodology review pending)

**Date parked:** 2026-05-26
**Parked by:** researcher
**Cluster status:** `Parked - Methodology Review`
**Pre-park work preserved in DB:** Phase 1 (vc_status advancement, 14 terms → vc_completed) + Phase 2 (Pass A meanings + keywords, 288/288 verses)

---

## Why parked

M11 surfaced a programme-level architectural question that needs to be resolved before further work on this cluster can proceed.

### Trigger

The Phase 3 constitution-debate verdict from the AI flagged one term (H5749A ud, 1V, Psa 119:61) as a marginal STAYS via §6.3.2 structural-opposite reading. Researcher review of that verdict opened a deeper inquiry.

### What the deeper inquiry revealed

1. **Zero keyword overlap between ud's verse and the M11 corpus** — the verse's keywords (`loyalty holding`, `will steadfast`, `pressure external`, `law remembered`, `faithfulness persisting`) appear in M11 only in this single verse. They are M30/M34/M13 vocabulary, not M11 vocabulary.

2. **More importantly, the broader pattern** — searching the database for verses containing the English word "forgive" returned **421 verses** programme-wide. Only **103** sit in M11. The other **246** are anchored to non-M11 terms in 30+ other clusters (M10 88, M05 19, M38 17, M45 10, M21 7, etc.) — because the verses' anchor Strong's numbers are sin/love/prayer/etc., not forgiveness verbs.

### The architectural diagnosis

The programme is term-anchored: each verse belongs to the cluster owning its Strong's number. The analytical work since v2_6 is characteristic-anchored: findings author at characteristic scope. The two models cohabit, but the tension surfaces when a characteristic's verse evidence is highly distributed across anchor-terms.

Three distinct cluster types now visible across the programme:

1. **Type 1 — Clusters that fit one characteristic cleanly** (the term-grouping aligns with one inner-being faculty). Candidates: M07 Shame, M02 Sorrow, M10c Defilement post-split. The v2_8 pipeline was designed for this case.
2. **Type 2 — Clusters that are status-aspects** (the cluster captures aspects/dimensions of one larger status). Explicit case: M10 (`char_structure='aspect_based'`, 22 aspect-characteristics around the single status "sin"). Other candidates the researcher named: life, atonement.
3. **Type 3 — Clusters with characteristic-legs in many other clusters** (the cluster captures only some of its characteristic's verses; the rest are anchored elsewhere). **M11 is the canonical example.**

Memory entry recording the diagnosis: [[feedback-three-cluster-types]].

---

## What's preserved in the DB

Phase 1 + Phase 2 work remains intact. If a future decision restores M11 in some form, these are starting material; if M11 is dissolved or restructured, these data are still valid analytical inputs for whichever clusters absorb M11's terms.

| Phase | Artefact | DB State |
|---|---|---|
| 1 | UT review | 0 UT verses; 14 of 15 mti_terms.vc_status advanced to `vc_completed` |
| 2 | Pass A meanings + keywords | 288/288 is_relevant=1 verses have `analysis_note` and `keywords` populated. §5.6 hard gate PASS. |
| 3 | Constitution debate verdicts (AI) | Verdicts file authored but NOT applied to DB (Phase 3 is analytical only — verdicts inform Phase 4/5, no direct DB writes). 15/15 STAYS recommended; 1 marginal (ud). |

Inherited VCGs (26) from the pre-cluster-pivot era are still present in the DB; they would be silently dissolved at Phase 8 per v2_9 *if* the cluster reaches that phase.

---

## Phase 3 AI verdicts file (reference, not applied)

`Sessions/Session_Clusters/M11/wa-cluster-M11-phase3-constitution-verdicts-v1-20260526.md`

The AI recommended 15/15 STAYS (12 clear + 2 with cross-register flag + 1 marginal). CC has not endorsed or rejected these verdicts at the DB level — no Phase 4 work was done.

---

## What needs to be resolved before un-parking

The researcher needs to decide on the programme-architecture question raised. Possible directions:

1. **Accept the current architecture as-is.** M11 captures the term-anchored subset of forgiveness/atonement/repentance/restoration vocabulary. Cross-cluster characteristic analytics (Phase 9 T6, Session D) integrate verses anchored elsewhere. M11 stays as one cluster spanning 4 sub-registers.

2. **Contract M11** to its M11-dominant core (atonement + forgiveness as priestly-mediated sin-release). Transfer turning/reconciliation/marginal terms to their dominant clusters (M10/M06/M30/M34/M44). M11 ends as ~7-8 terms, ~220V.

3. **Dissolve M11 entirely.** Each term TRANSFERS to its dominant-partner cluster. M11 ceases to exist. Apply the principle "a cluster should have a dominant characteristic that's also dominant only in itself" strictly.

4. **Restructure programme-wide** — reconsider Type-3 clusters generally, possibly adopting a different cluster-anchor model. Most invasive but most architecturally clean.

The decision is the researcher's; CC's role is to apply whichever direction is chosen.

---

## How to un-park

1. Researcher specifies the direction (one of the four above, or a different framing).
2. CC builds the corresponding directive(s) — typically Phase 4 TRANSFERS for options 2/3, or a "resume Phase 3 with revised verdicts" directive for option 1.
3. cluster.status returns to `Data - In Progress` (or `Not started` if the cluster is being dissolved).

---

## Reference

- **Phase 1+2 obslog:** `wa-cluster-M11-obslog-phase1-phase2-v1-20260526.md`
- **Phase 3 brief:** `wa-cluster-M11-phase3-constitution-brief-v1-20260526.md`
- **Phase 3 AI verdicts:** `wa-cluster-M11-phase3-constitution-verdicts-v1-20260526.md`
- **Constitution report:** `wa-cluster-M11-constitution-v1-20260526.md`
- **Keyword analytics v1:** `wa-cluster-M11-keyword-analytics-v1-20260526.md`
- **Memory entry on the three cluster types:** `feedback-three-cluster-types`

---

*Park notice — M11 — 2026-05-26. Awaiting researcher direction.*
