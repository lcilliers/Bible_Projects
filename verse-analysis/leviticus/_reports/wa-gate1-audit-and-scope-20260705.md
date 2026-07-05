# Gate-1 audit — what it is, where it was not in operation, and the Leviticus fix

> Prompted by the researcher (2026-07-05) after the `gaal` "redeem" miss: *"Gate 1 is supposed to scan through the spans of all the verses in focus and identify a span that is inner-being-like but not picked up. It is important for me to know for how long (which other books) the gate was not in operation."* This report gives a straight account.

---

## 1. What Gate 1 is (and what I actually did)

**Gate 1** in the live ve-lexical model is the **index-driven span scan**: it works off `verse_span_index` (the *full word-level index of every word in the text*) and identifies **inner-being-like spans that the curated term inventory did not pick up** — the "span-orphan audit." The infrastructure exists for exactly this: migration **M62** made `ve_lexical` span-keyable precisely because *"verse_context_id was NOT NULL, forcing every lexical to hang off a pre-tagged term — which is exactly why untagged content spans were skipped."* The `gate` column marks `1-primary` vs `2-relevant`.

**What my Leviticus study did instead:** my custom loader (`_apply_lev_study_v1`) worked off **`wa_verse_records`** — the *curated inner-being term subset* (the ~214-soul-word registry cascade). That subset is a **seed/index, not a census** (this is a known principle: *registry→terms = index not census; span-orphan audit* required). So any inner-being word that was **never registered as a term** — like `gaal` — was invisible to my study. **I bypassed Gate 1.** That is the root cause, not a bug in the ve-lexical script.

---

## 2. Where Gate 1 was — and was NOT — in operation (the scope you asked for)

Counting `ve_lexical.gate='1-primary'` spans per book (where the real Gate-1 index scan ran):

| Ran (Wisdom / Poetry / Prophets) | gate-1 spans |
|---|---|
| Psalms | 19,477 |
| Isaiah | 11,805 |
| Jeremiah | 10,652 |
| Proverbs | 7,583 |
| Ezekiel | 7,317 |
| Job | 5,704 |
| Daniel, Ecclesiastes, Hosea, Zechariah, Lamentations, Amos, Micah, and the rest of the Twelve | hundreds–thousands each |

| **NOT run (Torah / narrative)** | gate-1 spans |
|---|---|
| **Genesis** | **0** |
| **Exodus** | 120 (residual old-model rows, not a full scan) |
| **Leviticus** | 111 (residual, not a full scan) |
| Numbers, Deuteronomy | 0 |

**The finding:** Gate 1 ran thoroughly across the **Wisdom/Poetry/Prophets**, but **never ran on the Torah.** And critically — **my span-depth work all sits in the Torah and all bypassed Gate 1:**

- **Genesis** narrative readings (prose_section type 108) — built from `wa_verse_records` non-T2 spans via the probe script. **Gate 1 not in operation.**
- **Exodus** narrative readings (type 108) — same. **Gate 1 not in operation.**
- **Leviticus** terminology study (ve_lexical) — built from `wa_verse_records`. **Gate 1 not in operation** (now fixed — see §3).

So the honest answer: **for my span-depth work in the TORAH (Genesis, Exodus narrative; Leviticus terminology), Gate 1 was not in operation** — all three were built from the curated `wa_verse_records` seed.

### Were the prophets skipped? — NO (verified)

I checked, rather than assumed. Gate 1 (the `lexical-model-2026` index scan) **ran** on the Wisdom/Poetry/Prophets, and the recovered vocabulary **is** captured there — e.g. `ahev` "love" is coded **207×** in Psalms, 150× in Proverbs, 53× in Isaiah, 86× in Hosea, drawn straight from the index (Psalms `wa_verse_records` registers `ahev` only once, so the gate demonstrably caught the orphans). And my **poetic/prophetic reading method itself queries `verse_span_index`** (the full word index), not just the seed. So the prophets/wisdom were **index-driven and are sound** at the lexical level. (Their *prose* was written at movement-depth; a span-depth pass for them is a separately-logged debt — `project_prophets_wisdom_read_at_movement_depth_debt` — but that is a granularity choice, not a missing-word gap.)

### The actual blast radius (quantified)

The gap is therefore confined to the **Torah narrative + Leviticus.** Running the same span-orphan candidate scan:

| Book | status | genuine missed inner-being terms | headline misses |
|---|---|---|---|
| **Genesis** | span-depth read | ~6–8 (of 31 candidates) | **`ahev` LOVE (14 tokens** — Isaac/Esau, Jacob/Rachel, Israel/Joseph), `ruach` spirit (10), `abaq` **wrestle** (Peniel!), forget, be-willing |
| **Exodus** | span-depth read | ~6–8 (of 38 candidates) | `barak` **bless** (6), `ashaq` **oppress** (3 — the bondage), `chamad` desire (3), `chuphshah` free, `ruach` spirit-of-wisdom |
| **Leviticus** | FIXED | 13 recovered, coded | love, liberty, vow, redeem, oppress… (see §3) |

So it is **bounded and specific** — a handful of genuine terms per book, concentrated in identifiable passages (love in the patriarchal narratives; oppression in the bondage; wrestle at Peniel; spirit-of-wisdom in the tabernacle) — **not "all the prose."**

---

## 3. The Leviticus fix — Gate 1 properly run

I ran a proper Gate-1 scan for Leviticus: **every `verse_span_index` content-word Strong's** (858 distinct) diffed against the registered set (203) → **659 un-registered**; filtered by lexicon gloss for inner-being relevance → **46 candidates**; judged individually → **13 genuine inner-being terms** that had been missed. All are now coded into `ve_lexical` (keyed to their `verse_span_index` spans), coverage still **688/688**:

| Term | where | axis |
|---|---|---|
| `ahev` — **LOVE** ("love your neighbour as yourself") | 19:18, 19:34* | SELF (the-great-command) |
| `naqam` — **vengeance** ("you shall not avenge") | 19:18, 26:25 | SELF / BLESS_CURSE |
| `deror` — **liberty** ("proclaim liberty," Jubilee) | 25:10 | REDEEM |
| `chaphash`/`chuphshah` — **freedom** | 19:20 | REDEEM |
| `gaal`/`geullah` — **kinsman-redemption** (found earlier) | ch25, ch27 | REDEEM |
| `neder`/`nadar` — **vow** (the will's commitment) | 7:16; 22:18,21,23; 23:38; 27:2,8 | SELF |
| `barak` — **bless** (the priestly blessing verb) | 9:22, 23 | BLESS_CURSE |
| `ashaq`/`yanah`/`osheq` — **oppress / oppression** | 6:2,4; 25:14,17 | SIN_GUILT |
| `zimmah` — **depravity / lewdness** | 18:17, 19:29 | SIN_GUILT |
| `panah` — **turn** (to idols; and God's favourable turning) | 19:4,31; 20:6; 26:9 | SIN_GUILT / BLESS_CURSE |
| `chesed` (homonym) — **disgrace** (20:17; note: Leviticus has **no** `chesed`=steadfast-love) | 20:17 | SIN_GUILT |

*(\*19:34 "love the sojourner" is a `wa_verse_records` T2-only verse; its `ahev` span is in the index and now coded.)*

The single most important recovery is **`ahev` at 19:18** — *"you shall love your neighbour as yourself,"* the verse Jesus names the second great commandment, which my study had represented only obliquely (via `natar` "grudge"). The moral axis of Leviticus is materially richer for it: it now carries **love, liberty, vow, and freedom** — the *volitional and relational* vocabulary the curated seed had omitted.

REDEEM axis: 3 → **19 spans**. Total Leviticus coding rows: 6,839 → **7,142**.

---

## 4. Recommendations

1. **Genesis and Exodus need a Gate-1 pass.** The narrative readings were built from the same curated subset; a `verse_span_index`-vs-`wa_verse_records` diff (as run here) should be done for both, the missed inner-being terms identified, and the affected readings revised. `ahev` "love" alone will touch many passages. **This is a real debt, flagged for the researcher's decision** (it is a revision of already-filed readings).
2. **Bake Gate 1 into the method.** Any future book's span-depth work should begin with the index-scan span-orphan audit *before* reading, so un-registered inner-being terms are surfaced up front — not caught after the fact.
3. **Consider onboarding the recovered terms into `mti_terms`** (love, redeem, liberty, vow, oppress…) so they are registered for all books, not re-discovered book by book.

---

*Filed 2026-07-05. The Leviticus recovery is committed (coding JSONs + DB `ve_lexical`); the Genesis/Exodus exposure is documented here and in memory as an open debt.*
