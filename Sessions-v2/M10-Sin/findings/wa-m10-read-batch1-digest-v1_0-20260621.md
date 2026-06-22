# WA M10 — Batch 1 Read Digest (Gen 4:7 → Num 5:6)

**File:** wa-m10-read-batch1-digest-v1_0-20260621.md · **Version:** v1_0 · **Date:** 2026-06-21
**Prev output:** `wa-m10-verse-workthrough-plan-v1_0-20260621.md` (the method this executes — Stage 1, batch 1 of 8)
**Backing data:** `wa-m10-read-batch1-v1_0-20260621.json` (210 per-occurrence records)
**Source:** `wa-ve-lexical-extract-M10-20260621-b1of8.json`
**Status:** Batch 1 read complete. Behaviour keys are batch-local and will be reconciled across all 8 batches at Stage 2. No collection committed; no finding generalised to the cluster.

---

## 1. Coverage

160 verses · **210 / 210 focus occurrences read** · 24 distinct focus terms · corpus span Gen 4:7 → Num 5:6 (Pentateuch, heavily cultic-legal). Every occurrence has a record in the backing JSON; nothing skipped or sampled.

**Running tracker: 210 / 1,462 occurrences read (14%).**

---

## 2. The headline — the extract's inner-being fields are heavily polluted here, and only reading caught it

This batch is the test case for why we read rather than trust the fields. The fields claim far more inner-being seating than the verses support.

- **`seat=soul` is almost always *nephesh* = "anyone / a person", not the soul-seat.** The Levitical sin laws open "If a *nephesh* sins…" (Lev 4:2, 4:27, 5:1, 5:2, 5:15, 5:17, 6:2, 19:8, Num 5:6). The engine read *nephesh* as the constitutional seat "soul." It is the legal idiom for *a person*. **Not an inner-being seating.**
- **`seat=flesh` is the sacrificial animal's literal meat** (Exo 29:14 "the *flesh* of the bull"; Lev 16:27 "their *flesh*… burned"). Not the inner-being "flesh."
- **`origin=received-from-outside` is spurious** on the cultic occurrences (Lev 4:8, 5:6, 5:16, 9:10, 7:18) — no external-source clause is present; it looks like a stray "from"-preposition in the compensation wording.

**Count: 28 seat-tags and 5 origin-tags in this batch alone are artefacts.** Carried forward unread, they would have populated a "sin seated in the soul" collection that the verses do not support. This is the single most important result of batch 1, and it directly affects the programme-wide SEATED sub-collection (152) — much of it may dissolve on reading. *Flagged for CC as a possible re-gloss/verify item; no DB change proposed here.*

---

## 3. The genuine inner-being operations the reading *did* find

Rare, but real — and they are the constructs you suspected. Three kinds surfaced:

**(a) Sin as an external agent/appetite to be mastered — 1 occ, but striking.**
Gen 4:7 — sin "crouching at the door, its desire is for you, and you must rule over it." Sin behaves as a quasi-personal force outside the person, pressing on the will, to be ruled. Nothing else in the batch behaves like this.

**(b) Sin coupled with the heart — 5 occ.**
The heart is where sin is *restrained* (Gen 20:6, "integrity of your heart… I kept you from sinning"), *hardened into* (Exo 9:34, "he sinned… and hardened his heart"), *incurred through* (Lev 19:17, "do not hate your brother in your heart, lest you incur sin"), and *remedied at* (Lev 26:41, "if their uncircumcised heart is humbled"; with Lev 26:43, "their soul abhorred my statutes"). Here the inner being is the *site* of sin's operation — but note the seat word attaches to the heart's act (hardening, humbling, hating), not to the sin-term itself.

**(c) The conscience sequence: realize-guilt → confess — 18 occ.**
The Levitical refrain "when he comes to know it… and realizes his guilt… and confesses the sin" (Lev 4:13, 4:22, 4:27, 5:1–5, 6:4–5, Num 5:6). This is a genuine inner-being *process* — awareness of guilt arising, then confession — and it recurs enough to be a candidate collection in its own right.

Everything else (186 of 210) is **silent on the inner being** — and that silence is a finding, not a gap: in this corpus sin is overwhelmingly a *cultic-legal fact* (an offering to bring, a liability to bear, a status named), with no interior content. That is itself the dominant behaviour of M10's Pentateuchal core.

---

## 4. The behaviour taxonomy that emerged from the read (batch-local)

Reading the 210 occurrences, they sort into these behaviours (counts are batch 1 only; keys will be reconciled across batches at Stage 2):

| Behaviour key | n | What binds it |
|---|---:|---|
| cultic.sin-offering | 54 | *chat.tat* as the prescribed offering; ritual designation |
| status.named-sin | 41 | sin/iniquity/transgression named as a fact or condition |
| act.commit-sin | 26 | the doing of sin (mostly cultic "the sin he committed") |
| liability.bear | 18 | "bear his iniquity/sin" — sin as a borne liability + consequence (death/cut-off) |
| guilt.realize-confess | 18 | conscience operation: come-to-know guilt → confess |
| treachery.breach-faith | 9 | *ma'al* / *bagad* — covenant unfaithfulness |
| rebellion.transgression | 7 | *pesha* — revolt/transgression |
| cultic.atonement | 6 | *kippurim* — the remedy |
| guilt.liability | 5 | *asham* / *ashmah* — becoming/being guilty |
| act.sin-against-God | 5 | sin as deed Godward (often self-confessed) |
| ritual.purify (privative) | 4 | *cha.ta* meaning de-sin/cleanse an object — opposite direction |
| perversion | 3 | *tevel* / *salaph* |
| generational.fathers | 2 | iniquity transmitted fathers→children |
| injustice.civil | 2 | *avel* — wrong in judgement |
| corruption/destruction | 2 | *mashchit* |
| act.sin-against-person | 2 | sin Manward |
| (the six inner-being singletons in §3) | 6 | agent-external / heart-coupled / soul-abhorred |

Two observations held open: **"liability.bear"** (sin as a weight carried, with lethal consequence) and the **"realize-guilt→confess"** conscience sequence are the two behaviours most likely to become genuine constructs once reconciled across the corpus — the first looks like a *status* (a standing one is under), the second like an *operation* (something the inner being does).

---

## 5. What the result tells us about the method

- The read-first approach earned its keep on batch 1: it caught a systematic field artefact (seat) that would have corrupted the inner-being collection, and it found the 24 genuine inner-being occurrences buried in 186 cultic-legal ones.
- The per-occurrence schema works; `ib_note` + `behaviour_key` carried the judgement; "silent on inner being" was used honestly (186×) for genuine absence, never as a dumping ground.
- Pace: batch 1 = 14% of the corpus. Seven batches remain.

---

## 6. For your review

This is the result of batch 1. Before I continue, tell me:
1. Is this read depth and the record schema what you want for the remaining seven batches?
2. The seat-artefact finding is significant — do you want it carried as a running CC verify-list as we go, or handled separately?
3. Continue to batch 2 at this same full-batch pace, or adjust?

*Batch 1 of 8 read. Behaviour keys batch-local, to be reconciled at Stage 2. No collections committed; no findings generalised to the cluster.*
