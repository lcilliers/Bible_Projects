# FANOUT — Exo 1:13–14  (SAMPLE · illustrative)

> **This is a hand-built sample** to agree the shape before the generator is written. Values are pulled from the live DB (`verse_span_index`, `verse_term_index`); a few items marked «PENDING» await a prerequisite build (§9 of the architecture register). The real report will be generated, versioned `-vN`, bump-on-change.
>
> **Fanout = static lexicon only.** No findings, observations, narrations, logos or chat appear here (those live in the Passage_observation report). This is the stable substrate you read *from*.

- **Passage:** Exo 1:13–14 · group label `Exo 1:8-14` (from `wa_verse_records.verse_group` «PENDING DEC-1»)
- **Anchor verse:** Exo 1:13 (`verse_analysis_progress`)
- **Generated:** sample · **Version:** v1 · **Content-hash:** «set at build»

---

## 1. Passage text  ·  *source: `wa_verse_records` (reference = DB anchor)*
| ref | verse text |
|---|---|
| **Exo 1:13** | «verse text from verse record / STEP getBibleText» |
| **Exo 1:14** | «verse text from verse record / STEP getBibleText» |

*(Running text is pulled, not stored span-wise; shown here as the anchor line each datapoint traces back to.)*

## 2. Morphology — every span, by verse  ·  *source: `verse_span_index`*
**Exo 1:13** (`verse_id` 6542)

| # | surface | gloss | part | morphology | stem | lemma |
|---|---|---|---|---|---|---|
| 0 | they | the Egyptians | noun | HNpl | — | **H4713** *mitsri*, Egyptian |
| 1 | ruthlessly | with harshness | noun | HNcmsa HR | — | **H6531** *perek*, ruthlessness/harshness |
| 2 | people | sons/children | noun | HNcmpc HTo | — | **H1121** *ben*, son |
| 3 | Israel | Israel | noun | HNpl | — | **H3478** *yisrael* |
| 4 | work | made-to-serve | verb | HVhw3mp (Hiphil) | — | **H5647** *abad*, serve/enslave |

**Exo 1:14** (`verse_id` 6543)

| # | surface | gloss | lemma |
|---|---|---|---|
| 1 | bitter | to be bitter | **H4843** *marar*, be bitter |
| 2 | hard | hard/severe | **H7186** *qasheh*, hard |
| 3 | service | labour | **H5656** *abodah*, service |
| 4 | mortar | clay/mortar | **H2563** *chomer* |
| 5 | brick | brick | **H3843** *lebenah* |
| 8 | field | field | **H7704** *sadeh* |
| 11 | ruthlessly | with harshness | **H6531** *perek* |
| 12 | slaves | made-to-serve | **H5647** *abad* (Hiphil) |

*(Grammar-only spans — articles, conjunctions — omitted from this view; full span set retained in the DB.)*

## 3. Related verses by shared lemma  ·  *source: `verse_term_index` (primary lemma; DEC-2: index not census — anomalies accepted)*

> **Visualisation proposal for #12.** Lemmas differ wildly in spread (`perek` = 6 verses; `abad` = 260). A flat dump fails. Proposed rule:
> - **≤ 12 verses → list them all** (the small set *is* the story; show every one with anchor status).
> - **> 12 verses → show only the in-study subset** (verses already anchored / carrying observations) **+ a count of the remainder**, never the full list. The remainder is reachable on demand, not dumped.
> - Each related verse shows whether it **already has an anchor** — a verse with none is a **candidate the fanout raises** (DEC-3).

### `perek` H6531 — *ruthlessness* — **6 verses (full list)**
| verse | in this passage | has anchor? |
|---|---|---|
| Exo 1:13 | ● (anchor) | yes |
| Exo 1:14 | ● | yes (via passage) |
| Lev 25:43 | | yes |
| Lev 25:46 | | yes |
| Lev 25:53 | | **no → fanout raises anchor candidate (DEC-3)** |
| Eze 34:4 | | **no → fanout raises anchor candidate (DEC-3)** |

→ The complete `perek` story is 6 verses; 2 lack an anchor and would be queued for selection.

### `abad` H5647 — *serve/enslave* — **260 verses (in-study subset shown; 255 not listed)**
| verse | in this passage | has anchor? |
|---|---|---|
| Exo 1:13 | ● (anchor) | yes |
| Exo 1:14 | ● | yes |
| 2Ch 34:33 | | yes (worship pole — already in study) |
| Isa 43:23 | | **no → anchor candidate** |
| … | | **255 further verses — not dumped; reachable on demand** |

→ High-frequency lemma: the report shows *what the study already touches* + the count, not 260 rows. **This is the open visual you wanted to react to.**

### Other passage lemmas (frequency only — expand on demand)
*marar* H4843 (be bitter) = 13 · *abodah* H5656 (service) = 121 · *qasheh* H7186 (hard) = «count».

## 4. Coverage note  ·  *source: computed*
Content spans with no study lemma in this passage: *chomer* H2563 (mortar), *lebenah* H3843 (brick), *sadeh* H7704 (field) — material nouns, no inner-being relevance; flagged untracked, not errors.

---
*Static lexicon only. To act on meaning, open the Passage_observation report for Exo 1:8-14.*
