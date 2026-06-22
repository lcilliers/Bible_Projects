# WA M10 / M10b / M10c — Per-Verse Evidencing Schema Spec (from the JSON meta)

**File:** wa-m10-perverse-schema-spec-v1_0-20260622.md · **Version:** v1_0 · **Date:** 2026-06-22
**Source:** the 15 lexical JSONs' `meta` (`ve_lexical` v2_engine_iter1 + verse-read API; morphology schema 3.34.0).
**Purpose:** fix exactly what "evidencing a verse" must cover, read off the meta — before any per-verse extract is built. Not synthesis; a reading of the source spec.

---

## 1. Scope (computed from the 15 files)
- **15 JSONs:** M10 ×8, M10b ×5 (4 batches + the H7563 recovery), M10c ×2.
- **1,904 unique verses** (dedup by reference): M10 1215, M10b 557, M10c 236, with cross-unit overlap (M10∩M10b 71, M10∩M10c 21, M10b∩M10c 17, all three 5; 1,805 in exactly one unit).
- **Terms per verse (full inventory, incl. co-terms):** 1–12, median 2, mean 2.5; 180 verses carry ≥5 terms, 10 carry ≥8.
- **Implication:** the deliverable is keyed to the **unique verse**; an overlapping verse is evidenced once, from its full term inventory (the fan-out lists every term regardless of which unit's extract it sits in).

## 2. Per-verse data structure (what each verse carries)
`verse`: reference · osis_id · testament · verse_text.
`term_occurrences[]`: **every active term in the verse** (focus + co-terms; `focus_cluster=true` marks the cluster's own). Each occurrence =
- `term`: strong · translit · gloss · language · cluster · focus_cluster
- `verse_report`: target_word · morph · stem
- `lexical`: the analytical parts (§3).

**Fan-out (central):** a term's `compound` lists its co-terms, and **each co-term is present as its own full record in the same verse.** The verse's inner-being reality is built by **relating the head term to its co-terms within the verse** — never by reading a term alone.

## 3. The lexical parts (canonical, per meta `fields`) — each must be evidenced
sense · lemma_meaning · type (action/status/quality) · mode (lang·POS·stem) · faculty · location · origin · how · object · object_type · cause · cause_clause · experiencer · divine_involvement · intensity · valence · immediate_response · relational · compound. *(~18 fields; the substantive analytical "parts" the researcher counts as 14 sit within these — to be confirmed against the canonical list.)*

## 4. Derivation rules that GOVERN the evidencing (from meta `why_each_element_is_derived`)
These are not optional notes — they dictate how a verse is read:
- **Measure, not English.** Every value derives from a named original-language measure (lemma · morphology · per-occurrence sense · co-occurring tagged terms) — **never the English string.** Evidence the term from the Hebrew/Greek, using *sense* as the contextual reading.
- **Silence = NONE, never imputed.** An absent field is genuine silence; the evidence must say "silent," not fill it.
- **`object_type` is authoritative; `object` text is a hint** (mechanical, ~13% imprecise — can grab a determiner/pronoun/addressee). When they disagree, trust `object_type`.
- **`faculty` is TERM-INTRINSIC only.** It is the faculty the term *itself* is; it is **not** the verse's faculty engagement. Co-occurring-faculty seating (R2) is *not-yet-implemented*. So a verse's faculty/seat picture is built from the **co-terms** (compound: *co-seated*, faculty co-terms), not from the head term's `faculty`. *(This is the correction to my Pass-1, which read the focus term's faculty as the verse's.)*
- **`location`** = a constitutional-seat lemma actually present in the verse, sense-gated (ruach/pneuma may be wind/disposition), de-duplicated per seat-level. Absent = not located.
- **`origin`** is partial — only the "from"-source preposition (→ received-from-outside) is implemented; within-person/generational are not. Sparse (≈140), so its silence is not evidence of "no origin."
- **`cause` is read-resolved** (the verse's argument after ki/hoti/gar); `cause_clause` is a superseded mechanical hint.
- **`valence`** is read-resolved (righteous/sinful/commanded/forbidden/neutral) — but **hold it open as a tag, not a verdict** (it over-applies "sinful," e.g. to *lev* "heart" and to ritual contact-uncleanness; the status-vs-characteristic question is not settled).
- **`divine_involvement`** = God's role toward the term (agent/possessor/giver/object/addressee), read-resolved.
- **`compound`** = the synergy web; roles are *partner* (co-T1, another inner-being term) · *qualifier* (T2 content) · *co-seated* (shares a seat). Fan out to each co-term's full record.
- Co-terms are already **T2-noise-filtered** (kept only for a recognised inner-being qualifier role) and **set-aside-honoured** (out-of-scope/homonym verses excluded). So the inventory present is the in-scope, meaningful set.

## 5. What "evidencing a verse" therefore means (corrected)
For each of the 1,904 unique verses: read the verse from the measure; for **every** term in it evaluate **all** its lexical parts per §3–4 (interpreting, honouring silence, trusting object_type, treating faculty as term-intrinsic); **relate the terms through the compound web** (partner/qualifier/co-seated) to show how they operate together; and draw the **inner-being reality** of the verse — neutrally, with the extract's own tags (valence/location) flagged where they over-reach. No architecture, no status/characteristic verdict, no cross-verse synthesis.

## 6. How this corrects Pass-1 (preserved, not inherited)
Pass-1 read **focus terms only**, leaned on the **English** target_word, took the **focus term's faculty** as the verse's, and used `compound` as **sin-ring touch-points**. The meta shows the unit is the **whole verse**, the read is from the **measure**, faculty is **term-intrinsic** (verse-faculty is built from co-terms), and `compound` is the **synergy web**. The per-verse pass follows the meta; Pass-1 stays a reference seed (manifest `wa-m10b-pass1-manifest-v1_0`).

---
*Open items before building: (1) confirm the canonical 14-part list (or "evidence all meta fields"); (2) confirm the Jer 4:14 sample format/depth, now to be re-grounded on §4 (measure-led, faculty-from-co-terms); (3) file organisation — one searchable file per unit (M10 / M10b / M10c) with overlaps evidenced once, or a single unified verse-keyed file.*
