# Poetic-book lexical method (chapter-driven) + Psalm 1 plan — v1, 2026-07-02

> Researcher direction (2026-07-02): tackle the **specialised (poetic) books first — Psalms then Proverbs — chapter by chapter, starting Psalm 1.** The governing question for these verses is **"what do these verses tell us about the inner being?"** Method: run each verse to a base lexical (same pipeline as before **except the passage process does not apply**), then evaluate the whole chapter together — and that whole-chapter analysis is expected to tease out **different characteristics from different perspectives.** This is a plan for approval — **nothing built yet.**

## 1. What changes vs the prose (ruthlessness) pipeline
| | Prose (ruthlessness) | **Poetic (Psalm/Proverbs)** |
|---|---|---|
| **Driver** | TERM-driven (one owner term across its verses) | **CHAPTER-driven** (one chapter, all its verses) |
| **Unit batch** | the passage (maximal consecutive run) | **the chapter**; passage process **not applicable** — each verse stands as its own unit |
| **Phase 1 build** | per-passage, adjacent verses read together | **per-verse, independently** — no adjacent-verse load; **cross-verse items OFF** (source-across-verses / effect-across-verses / process-chain would be noise between poetic lines) |
| **Within-verse items** | on | **on** (sense, type, operation, seat, bearer, target, manner, coupling, intensity, prohibition — all verse-bounded) |
| **Phase 2** | single-term rollup → one focus characteristic | **whole-chapter reading → MULTIPLE characteristics**, read from different perspectives (contrast, simile, cause) |
| **Output** | one `lexical_prose` story per term | (proposed) one chapter reading — "what this chapter says about the inner being" — naming each characteristic it surfaces |

The infrastructure already supports Phase-1 poetic: the index-driven builder gates cross-verse derivation on `kind='prose'`; passing `kind='poetic'` turns source/effect/process off automatically. So no per-verse cross-verse leakage.

## 2. The two phases (poetic)
**Phase 1 — base lexical, verse by verse (mechanical draft, then sanity-check).**
For each verse of the chapter, independently:
- two-gate index-driven build on that verse's spans only (gate 1 = tagged non-T2 term → link `verse_context`; gate 2 = content span not yet a term → span-keyed, candidate);
- within-verse items only; cross-verse OFF; genre = `poetic/wisdom`;
- sanity-check each verse (evaluate every derived value against the verse; assign `role` = characteristic / process-qualifier / standalone / uncertain; bearer-quality → D11).
- mark `verse.process_marker`.

**Phase 2 — evaluate the chapter as a whole (the poem's reading).**
Read all the verses' lexicals together and tease out the inner-being characteristics. Unlike the prose rollup this is **multi-characteristic and multi-perspective**:
- a psalm presents several IB characteristics at once (Psalm 1: *delight*, *meditation*, the *moral condition* righteous-vs-wicked, *stability/rootedness*);
- it presents them from **different angles** — positive vs negative (the two ways), direct statement vs simile (the planted tree / the driven chaff), cause and consequence;
- so Phase 2 identifies the **set** of characteristics, each grounded in its verses, and reads how the poem frames each — rather than forcing one focus term.
- Output = a chapter-scoped reading answering "what does Psalm 1 tell us about the inner being," every inference tagged stated|inferred, tethered to the verse.

## 3. Psalm 1 — the evidence already in the DB (facts, not derived)
6 verses, genre `poetic/wisdom`, passage 1573 (ignored per method). No existing new-model lexical (clean). Tagged terms:

| verse | tagged terms (Strong's / cluster / gloss) |
|---|---|
| Psa 1:1 | H2400 M10 sinner · H6098 M17 counsel · H7563 M10 wicked |
| Psa 1:2 | **H2656 M04 delight/pleasure** · **H1897 M42 meditate/mutter** |
| Psa 1:3 | H5034B M24 wither · H5414 M12 give |
| Psa 1:4 | H7563 M10 wicked |
| Psa 1:5 | H2400 M10 sinner · H4941 M26 justice/judgement · H6662 M26 righteous · H7563 M10 wicked |
| Psa 1:6 | H6662 M26 righteous · H7563 M10 wicked |

~48 content spans across the 6 verses (gate-2 will lexicalise the untagged content — *blessed*, *walk/stand/sit*, *law*, *tree*, *water*, *fruit*, *chaff*, *perish*, *way*). The candidate characteristics: **delight** (M04, desire-orientation), **meditation** (M42, cognitive rumination), the **moral condition** wicked/sinner vs righteous (M10/M26), and **stability/rootedness** (the tree simile, likely gate-2).

## 4. What I propose to build
1. A **reusable** `scripts/_apply_poetic_chapter_lexical_v1_YYYYMMDD.py` — parameterised by book+chapter (so it runs Psalm 2, 3, … Proverbs 1, … next), Phase-1 only: per-verse two-gate build, `kind='poetic'`, sanity-check + role, `process_marker`. Backup + dry-run + verify, same safe pattern.
2. Run it on **Psalm 1**, produce the per-verse lexical view for your inspection (frequency + role, DB-only) — same read-back you signed off on for ruthlessness.
3. On your confirmation of Phase 1, do **Phase 2** — the whole-chapter reading — and file it to prose (proposed new type `lexical_prose_chapter`, or reuse `lexical_prose` keyed to the chapter; your call).

## 5. Decisions I need from you before building
- **(a)** Phase 1 approach above (per-verse, cross-verse OFF, sanity-check+role) — agreed?
- **(b)** Phase 2 as a **multi-characteristic** chapter reading (not one focus term) — agreed?
- **(c)** Build the reusable chapter-driven script now (vs a Psalm-1-only throwaway)? I recommend reusable.
- **(d)** Where the chapter reading is filed: new `lexical_prose_chapter` type, or reuse `lexical_prose`?
