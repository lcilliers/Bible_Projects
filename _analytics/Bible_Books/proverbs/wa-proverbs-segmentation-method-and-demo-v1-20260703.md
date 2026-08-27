# Proverbs — inner-being segmentation method + worked demo (v1)

> **Researcher direction (2026-07-03):** Proverbs is handled **segmentation-first**. Before any analysis, read a section and **split it into units** from an *inner-being characteristic* perspective. A unit is sometimes a **single verse**, sometimes a **whole series**; where **several characteristics operate together they are handled together**. The unit — not the chapter — is what then receives a Phase-2 inner-being reading.
>
> This doc: the proposed method + a worked demo on **Prov 1** (discourse) and **Prov 10:1–20** (sentence-collection), then the open design decisions to confirm before scaling to all 31 chapters.

## 1. Why Proverbs needs this (the two genres)
- **Chs 1–9 — connected discourses** (the father's appeals; Wisdom personified). These read like the Psalms: natural, mostly **contiguous** units of 5–30 verses. Chapter-driven segmentation is easy here.
- **Chs 10–31 — sentence-collections** (largely independent couplets). Here the **chapter is a weak unit**; the couplet is the atom. Inner-being coherence is often **thematic and scattered** — many couplets on one characteristic spread across a chapter. Segmentation must therefore allow both *contiguous runs* and *gathered threads*.

## 2. Unit types (emergent, not forced)
- **D — discourse unit:** a contiguous run in chs 1–9 (and set-pieces like 8:1–36, 31:10–31) developing one theme/appeal.
- **S — single saying:** a self-contained couplet that is its own inner-being unit (a gem that stands alone).
- **C — cluster (contiguous):** a short run of adjacent couplets on one characteristic.
- **T — thread (non-contiguous):** couplets *scattered* across a chapter/section, gathered by a shared characteristic and handled together.
- **F — frame/arena:** the pervasive righteous⇄wicked (or wise⇄fool) antithesis that runs under most of chs 10–15 — noted **once per section** as the arena, not re-tagged per verse (so it does not drown the specific findings).

Each unit carries: **id · verse range(s) · type · inner-being characteristic(s) · multi?(y/n) · one-line gist.** Provisional characteristics are named to *route* the later reading, not to pre-decide it.

## 3. Worked demo A — Proverbs 1 (discourse; clean contiguous units)

| unit | verses | type | characteristic(s) | multi | gist |
|---|---|---|---|---|---|
| PRO-01-A | 1:1–6 | D | **formation of the inner being** — the faculties wisdom builds (knowing, understanding, prudence, discretion, receiving instruction) | y | the stated *aims* of wisdom = what it does to the inner being |
| PRO-01-B | 1:7 | S | **the fear of the LORD as the beginning/root** | n | cornerstone motto (with Ps 111:10); the foundational inner posture — its own unit by weight |
| PRO-01-C | 1:8–19 | D | **filial receptivity** (hear/forsake-not instruction) + **the self-destructive greedy heart** (enticement resisted; ambushers who "lie in wait for their own blood") | y | two characteristics held together: receiving the father's word, and greed that recoils on itself |
| PRO-01-D | 1:20–33 | D | **the refusal of wisdom** — loving simplicity, delighting in scoffing, hating knowledge, ignoring counsel — vs. **the security of the one who listens** ("will dwell secure… without dread") | y | Wisdom's cry and the refusing heart; disposition-against-wisdom and its fatal end |

## 4. Worked demo B — Proverbs 10:1–20 (sentence-collection; single / cluster / thread)
- **Frame (F):** 10:1–20 runs on the **righteous⇄wicked / wise⇄fool antithesis** — the moral-poles *arena* (as in Ps 1). Noted once; the units below are the specific inner-being findings within it.

| unit | verses | type | characteristic(s) | multi | gist |
|---|---|---|---|---|---|
| PRO-10-v1 | 10:1 | S | **character produces others' inner state** | n | the wise/foolish son as gladness or sorrow to a parent's inner being |
| PRO-10-v3 | 10:3 | S | **desire / craving** | n | God "thwarts the craving of the wicked" (appetite thread, w/ Ps 106/145) |
| PRO-10-recept | 10:8, 10:17 (+ recurring 10:10b) | T | **receptivity / teachability** | n | the wise heart *receives* commandments; heeding instruction = "path to life" vs. rejecting reproof |
| PRO-10-v9 | 10:9 | S | **integrity** | n | "whoever walks in integrity walks securely" (integrity thread, w/ Ps 15/26) |
| PRO-10-v12 | 10:12 | S | **love vs. hate as relational drivers** | y | "hatred stirs up strife, but love covers all offenses" — a self-contained gem |
| PRO-10-speech | 10:11, 13–14, 18–20 | T | **the inner condition legible in speech** | y | mouth of the righteous = fountain of life; concealed hatred = lying lips; many words = transgression; restrained lips = prudent; tongue of righteous = silver / heart of wicked = worthless — a **thread gathered across the chapter**, handled together (w/ Ps 5:9, 12, 141:3) |

This one slice already yields **single sayings (S)**, a **contiguous-ish thread (T, receptivity)**, a **scattered thread (T, speech)**, a **self-contained gem (S, love/hate)**, and the **moral-poles frame (F)** — demonstrating the method across the sentence-collection's real texture.

## 5. Pipeline (proposed, after segmentation)
Segmentation → then, **per unit**: Phase-1 lexical (verse-by-verse, as for Psalms; the substrate is already verse-first) → **Phase-2 reading of the unit** (single or multi-characteristic), filed to `prose_section` as a new type **`lexical_prose_proverbs_unit`** (keyed by unit id / verse-range, not chapter). The cross-chapter synthesis later folds Proverbs' characteristics into the same emergent families as the Psalter (self-address, trust, fear-of-the-LORD, desire, integrity, speech-legibility, …), so the two books converge.

## 6. Open design decisions (for the researcher) — confirm before scaling
1. **Storage of units.** `verse.passage_id` fits **contiguous** units (D/S/C) cleanly (anchor = first verse). **Non-contiguous threads (T)** don't fit one passage_id. Options: (a) passage_id for contiguous + a separate `unit_id` label carried on `ve_lexical`/a small `proverbs_unit` table for threads; (b) a dedicated `proverbs_unit` + `proverbs_unit_verse` (M:N) table for *all* units (cleanest, handles threads natively); (c) keep threads as reading-level groupings only (map in the doc), verses tagged to their nearest contiguous unit. **Recommendation: (b)** — a small M:N unit table, DB-canonical, reusable for any sentence-collection book.
2. **Thread scope.** Gather threads **within a chapter** first (as demo B), or **across a section** (e.g. all of 10–15)? Within-chapter is more tractable and less speculative; cross-section threads can be a later synthesis pass. **Recommendation: within-chapter for now.**
3. **The moral-poles frame.** Confirm it is noted **once per section as arena** (not a per-verse finding) — avoids drowning the specific inner-being findings.
4. **Pacing.** Segment **1–9 first** (discourses, high inner-being density), review, then tackle **10–31** (sentences) section by section? Or a full segmentation pass first, then readings?

## 7. Recommendation
Approve the unit-type scheme (§2) and storage option **6.1(b)**; I then (i) backfill all 31 Proverbs chapters for complete text, (ii) segment **chs 1–9** and file the unit map, (iii) pause for your review before the sentence-collections. Nothing is filed to the corpus DB until the segmentation of a section is confirmed.

---
*Text backfilled for Prov 1 (3 vv.) and Prov 10 (complete) for this demo. Proverbs coverage in DB: 839/915 verses — full backfill needed before segmentation.*
