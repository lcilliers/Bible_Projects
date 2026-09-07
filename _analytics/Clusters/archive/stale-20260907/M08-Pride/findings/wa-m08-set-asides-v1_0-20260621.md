# WA — M08 (Pride, Arrogance and Boasting): Set-Aside Candidates

**File:** wa-m08-set-asides-v1_0-20260621.md · **Version:** v1_0 · **Date:** 2026-06-21
**Prior output reference:** wa-m08-prov-char-list-v1_1-20260621.md; obslog wa-obslog-m08-distill-chars-v1-20260621.md.
**Source data:** wa-ve-lexical-extract-M08-20260621-b1of2.json + b2of2.json (extract v1_0, 2026-06-21).
**Status:** PROPOSAL only (GR-PROC-004). No item is excluded by this file.

## Governing disposition (researcher direction, 2026-06-21)

**Inclusion by default.** An item stays in the working analysis corpus until the evidence is **confirmed** not to support the item being *in any way involved in or supporting inner-being activity*. The bar for set-aside is high: residual doubt → keep in. This file documents the evidence so each exclusion can be confirmed (or overturned) on the verses, not asserted.

Three categories are distinguished:
- **(I) Relevance set-aside candidate** — the term, in its M08 occurrences, does not engage inner-being activity at all (GR-PROG-007 term-level filter fails).
- **(II) Cluster-ownership query** — the term *is* inner-being, but may belong to a different cluster, not M08 pride. (These are KEPT — they support inner-being activity — and flagged only for ownership.)
- **(III) Per-occurrence filter** — not a whole-term set-aside; individual occurrences are tested verse-by-verse in the detail phase.

---

## (I) Relevance set-aside candidates

### archō (G0757) — "be first / rule / begin" — 8 occurrences
**Verdict: recommend set-aside; CONFIRMED at term level across all 8; two residual-awareness flags. Keep in corpus until you confirm.**

Every occurrence read. In each, archō contributes only the **inceptive auxiliary** ("began/begins to") or denotes **ruler-status**, not an inner-being state of pride/boasting:

| Ref | Term's role in the verse | Inner-being pride carried by archō? |
|---|---|---|
| Matthew 16:22 | "Peter… **began** to rebuke him" | No — inceptive aux |
| Matthew 24:49 | "**begins** to beat his fellow servants" | No — inceptive aux (abuse carried by other terms) |
| Mark 8:32 | "Peter… **began** to rebuke him" | No — inceptive aux |
| Mark 10:41 | "the ten… **began** to be indignant" | No — affect carried by *aganakteō* |
| Mark 10:42 | "those considered **rulers** of the Gentiles lord it over them" | No — ruler-status; domination carried by *katakurieuō* ⚠ |
| Luke 3:8 | "do not **begin** to say… 'We have Abraham as our father'" | No — inceptive aux (lineage-pride is in the claim, not archō) ⚠ |
| Luke 11:53 | "scribes and Pharisees **began** to press him hard" | No — inceptive aux |
| Luke 12:45 | "**begins** to beat the male and female servants" | No — inceptive aux |

**Assessment:** Across all 8, the M08-relevant sense of archō ("be first / loves primacy") does not actually appear; the term carries no inner-being content in any of these uses. **Residual-awareness flags:** Mark 10:42 (lording-over) and Luke 3:8 (presumption of lineage) sit in verses with pride-adjacent themes, though the pride is carried by other terms. Recommend set-aside as a non-inner-being lemma here, subject to your confirmation.

### ro.hav (H7296) — glossed "pride" — 1 occurrence
**Verdict: recommend set-aside; CONFIRMED. Keep in corpus until you confirm.**
- Psalm 90:10 — "yet their **span** is but toil and trouble." The sense here is the *extent/span* of one's years, not pride. Gloss/sense mismatch (the lemma can mean pride/breadth, but this occurrence is "span"). No inner-being pride content. Setting it aside removes ro.hav from M08 entirely (sole occurrence).

---

## (II) Cluster-ownership query (KEPT — inner-being confirmed)

### akratēs (G0193) — "without self-control" — 1 occurrence
**Verdict: KEEP in M08 corpus; flag ownership only.**
- 2 Timothy 3:3 — in the vice list, "**without self-control**." The term *does* engage inner-being activity (volition / self-mastery), so by the governing bar it must be kept. But its own meaning is intemperance, not pride; it may properly belong to a self-control / temperance cluster rather than M08. **Not a relevance set-aside** — surfaced as a boundary/ownership question for the cluster analysis. It rides in the 2 Timothy 3:2–3 vice list alongside genuine pride terms (huperēfanos, alazōn, filautos), which is likely why it was seeded here.

---

## (III) Per-occurrence filter (whole-term retained; occurrences tested in detail)

### Height-nouns — ma.rom (H4791), qo.mah (H6967), ga.vo.ah (H1364), go.vah (H1363), rum (H7312)
**Verdict: retain the lemmas; filter occurrence-by-occurrence in the detail phase.**
These mix two uses that must be separated by reading each verse, not by lemma:
- **Literal / neutral height (set-aside the occurrence):** "the **height** of his stature" (1 Samuel 16:7); "the **heights** of the mountains… tallest cedars" (2 Kings 19:23; Isaiah 37:24); literal architectural/topographic height.
- **Pride-of-self (keep the occurrence):** "its **heart was proud** of its height" (Ezekiel 31:10); "the **lofty pride** of men" (Isaiah 2:11, 17); "in the **pride** of his heart" (Obadiah 3).

The split is real and per-occurrence; no whole-term exclusion is warranted. The literal-height occurrences are confirmed candidates for occurrence-level set-aside, to be marked verse-by-verse during detail work.

---

## Summary

| Item | Occ | Category | Recommendation | Confirmed? |
|---|---|---|---|---|
| archō (G0757) | 8 | I — relevance | Set aside (2 awareness flags) | Term-level confirmed; awaiting researcher |
| ro.hav (H7296) | 1 | I — relevance | Set aside | Confirmed |
| akratēs (G0193) | 1 | II — ownership | **Keep**; flag re-home | Inner-being confirmed |
| height-nouns (5 lemmas) | — | III — per-occ | Keep lemmas; filter occurrences | Per-occurrence, in detail phase |

**No item is excluded by this file.** Pending your confirmation of the category-I set-asides (archō, ro.hav), all items remain in the working corpus for detail-by-characteristic.

---

## Application outcome (researcher direction "proceed with set asides", 2026-06-21)

Applied by `scripts/_apply_m08_setasides_20260621.py` (occurrence-level `set_aside_reason`, reversible). **15 occurrences set aside**; M08 in-scope verses 253 → **241**.

| Item | Applied | Detail |
|---|---|---|
| archō (G0757) | **8** set aside (term-level) | All 8 in-scope occurrences — the inceptive-auxiliary / ruler-status uses (Mat/Mar/Luk). 55 were already set aside in a prior pass. |
| ro.hav (H7296) | **1** set aside | Psa 90:10 "span/extent" — gloss/sense mismatch, no pride content. |
| akratēs (G0193) | **0** (KEPT) | Category II — inner-being confirmed; left in-scope, ownership flag only (candidate re-home to a self-control cluster). |
| height-nouns | **6** set aside (occurrence-level) | Only the occurrences this file **names** as literal: `1Sa 16:7` ("height of his stature" — qo.mah + ga.vo.ah), `2Ki 19:23` & `Isa 37:24` ("heights of the mountains… tallest cedars" — ma.rom + qo.mah). |

**Kept in-scope (inclusion-by-default, residual doubt):** the remaining ~33 height-noun occurrences — all pride-of-self or pride-adjacent (e.g. Eze 31:10 "its heart was proud of its height"; Isa 2:11/2:17 "the lofty pride of men"; Obd 3, Pro 16:5/16:18, Psa 10:4, Jer 48:29, 2Ch 32:26). These were **not** set aside; per-occurrence detail confirmation of any further literal-height residue remains an open (low-priority) item.

**Consequence:** the M08 lexical extract (253 verses) is now **stale** (in-scope 241). Regenerate before any re-use as a Chat input (FA-11 will flag it). M08 findings + essay are already captured, so no re-run is required for the closed work.
