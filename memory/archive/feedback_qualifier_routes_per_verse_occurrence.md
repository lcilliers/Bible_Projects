---
name: feedback_qualifier_routes_per_verse_occurrence
description: For a QUALIFIER (T2 — qualifies a characteristic but isn't one), the unit of movement is the VERSE-OCCURRENCE, not the whole term. A qualifier's verse routes to the cluster of the characteristic it COMBINES with in that verse; verses with no co-occurring characteristic don't route; the same qualifier routes to DIFFERENT clusters in different verses.
metadata:
  type: feedback
---

**The rule (researcher, 2026-06-08):** a **qualifier** (T2 — a term that qualifies another term but is not a
characteristic in itself; a qualifier+T1 is still *one* characteristic) is routed **per verse-occurrence**,
**not** per term. Only the verses where the qualifier **combines with a characteristic** move, to **that
characteristic's cluster**. A qualifier may have **no related term** in a verse (→ doesn't route there) or
**different related terms** in different verses (→ routes to different clusters). **You cannot apply all of a
qualifier's verses to one cluster.**

**This refines [[feedback_term_is_the_unit_of_movement]]:** the term-is-the-unit rule holds for **faculties
(T1 / characteristics)** — the whole term moves, carrying its verses. For **qualifiers (T2)**, the **verse-
occurrence (the qualifier+characteristic combination)** is the unit.

**Grounded (2026-06-08, M01 T2-cleanup):** `G3788 ophthalmos` ("eye") — 85 verse-occurrences, only **44
(52%) co-occur with a characteristic**, and they spread across Truth / Wickedness / Repentance / Deceit /
Faith / Wisdom (different clusters per verse); 41 verses have "eye" with no characteristic → no route. Across
the 44 §D qualifier terms: 1,600 occurrences, **49% co-occur with a characteristic** (would route), ~51%
not.

**Implications:** (1) qualifiers (the T2 cleanup §C/§D) are **not** moved by a term-level `cluster_code`
change — they need a **per-verse-occurrence routing** mechanism (the verse-typing / span-pairing work, type-b
"T2+T1"). (2) This is the same mechanism the verse-aware L1/L2 needs (see
[[feedback_l1_must_be_verse_aware]]). (3) T1 vs T2 is therefore decided **in the verse read** (which term is
the faculty, which qualifies), per occurrence — not a fixed per-term tag. Detail:
`research/investigations/wa-t2-cleanup-dispositions-v1-20260608.md`.
