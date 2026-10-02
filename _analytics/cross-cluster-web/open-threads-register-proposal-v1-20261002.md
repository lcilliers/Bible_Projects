# Keeping open observations alive without leaving the main flow: proposal

**Date:** 2026-10-02 · **Status:** proposal, for the researcher's decision · **Raised by:** researcher, after the life-death unit 1 ledger (verbatim): *"worth pondering on how to keep these observations open for further resolution without getting distracted by the main flow, and not loosing sight of it."*

## 1. What happens now

Open items are recorded, but each kind sits in a different place:

| Kind | Example | Where it sits now |
| --- | --- | --- |
| A held observation in a ledger | LD-30 (Eze 20:11 against 20:25, with Gal 3:21); FE-85 (Lam 4:6); the anger ledger §M | inside each strand's ledger, marked **H** |
| A researcher question carried through a strand | Q1–Q4 (death; spirit and soul at death; the heart after death; body and resurrection) | candidate v2 §7, and §D of each unit ledger |
| A signpost waiting for a trigger | #1893 (God's hand: resume when the hands are studied) | an escalation, plus one memory file |
| Held text in the narrative | "Held" sections in the chapters | the chapter files |

**The risk.** Each item is safe where it was written. But nothing brings it back at the moment a later strand reaches the same verses or words. A held item is only found again if someone re-reads that ledger.

## 2. Proposal: one living register, checked at the start of every unit

**One file:** `_analytics/cross-cluster-web/open-threads-register.md`. It is a single living document, updated in place, with resolved rows struck through, not deleted.

**One row per open thread:**

| Field | Content |
| --- | --- |
| id | OT-nn |
| thread | the question or tension, in one line, with the verses (quoted, unresolved) |
| raised | where and when (ledger id or escalation, date) |
| **comes back when** | the trigger: the Strong's numbers, clusters or topic whose reading would bear on it, e.g. "H2706 statute; M54; Galatians 3" |
| status | open · touched (a unit added evidence: ledger id) · resolved (the resolution, and the researcher's ruling) |

**Two light touch points. No new process steps.**

1. **Before each unit's pull:** compare the unit's Strong's numbers and clusters with the "comes back when" column. Matching threads are listed in the unit ledger's front matter as *"threads this unit may bear on"*. The unit then records anything it finds, as ordinary observations.
2. **At ledger approval:** new held items, and new researcher questions, go into the register as well as the ledger. This adds one line to the ledger's §F ("register: OT-nn added").

**What the register is not:**
- It is not a task list. Nothing on it is worked on directly; threads move only when a strand reaches them (focused capture, #1900).
- It does not replace the escalation for a *decision* (e.g. LD-30's "held pending direction"). The escalation records the decision; the register records the thread.
- Its threads do not appear in the narrative. The narrative keeps its own "Held" marking for unchecked text. A thread reaches the narrative only once it is resolved and woven.

## 3. First entries (if approved)

| id | thread | comes back when |
| --- | --- | --- |
| OT-01 | Statutes "by which … he shall live" (Eze 20:11) and "by which they could not have life" (Eze 20:25); "if a law had been given that could give life" (Gal 3:21). LD-30 | Torah and Obedience (M54); righteousness (M12, next candidate) |
| OT-02 | Q1 What is death? | life-death unit 2; Sheol / sleep words |
| OT-03 | Q2 What happens to the spirit and soul at death? | soul and spirit with the death words (focused pull) |
| OT-04 | Q3 Is anything said about the heart after death? (unit 1: no verse) | heart with die, death or Sheol (focused pull) |
| OT-05 | Q4 Body and resurrection; the glorified body | body, resurrection, transform, incorruptible (focused pull) |
| OT-06 | God's hand: the fuller pass and a scan of special clusters (#1893) | the inner being acting through the hands |
| OT-07 | Held items in the earlier ledgers (FE-85; anger §M) | to be carried over one by one when the register is set up |

## 4. Why this shape

- It is **one living register** (memory `feedback_single_living_register`), not a file per thread.
- It is **trigger-based**, like #1893, which already works this way for one item.
- It adds **two small checks**, not a new stage. This keeps to "simple steps, not engineered designs".
- Revisiting stays the rule (`feedback_revisit_as_rule`): a thread that a unit touches goes back into that unit's ledger.

## 5. Optional later step (not proposed now)

The overview script could print the matching threads automatically, by reading the "comes back when" column. This is worth doing only if the manual check proves to be forgotten.
