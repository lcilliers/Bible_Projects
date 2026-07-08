# How verse · passage · master · term · lexical · verse-record tie together (linkage map)

> The complete, verified reference for how the study's core objects link — the substrate the characteristic→role→lexical cycle runs on. Every join key below is confirmed against the live DB (2026-07-08). Companion to `Workflow/Instructions/wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md`.

---

## 1. The objects and the ONE hub
Everything hangs off the **master index** (`verse_span_index`) — one row per morphological word, keyed by `id`. It is the hub; all other objects point **into** it or are reached **through** it.

```
                         passage
                            ▲  (verse.passage_id → passage.id)
                            │
            verse  ─────────┘         verse.id
              ▲                          ▲
              │ (verse_span_index.verse_id → verse.id)
              │
        ┌─────┴───────── MASTER: verse_span_index (id) ───────────┐
        │  columns: verse_id, primary_strong(=term/strong),       │
        │           role, char_candidate                          │
        └───▲───────────────▲───────────────────▲────────────────┘
            │               │                   │
   ve_lexical.        wa_verse_records.     primary_strong
   verse_span_id      verse_span_id         (string) → mti_terms
   → master.id        → master.id           .strongs_number
   [THE LEXICAL]      [THE VERSE-RECORD]     [THE TERM]
```

## 2. The join keys (all verified)
| link | from → to | key | status |
|---|---|---|---|
| passage ↔ verse | `verse.passage_id` → `passage.id` | FK | live |
| verse ↔ master | `verse_span_index.verse_id` → `verse.id` | FK | live |
| master ↔ lexical | `ve_lexical.verse_span_id` → `verse_span_index.id` | de-facto FK | **511,527 of 511,849 live rows linked; 322 unlinked = DEFUNCT** |
| master ↔ verse-record | `wa_verse_records.verse_span_id` → `verse_span_index.id` | de-facto FK | live (records with span set) |
| verse ↔ verse-record | `wa_verse_records.verse_id` → `verse.id` | FK | live |
| master ↔ term | `verse_span_index.primary_strong` → `mti_terms.strongs_number` | string match | partial (strong not unique; the study term) |
| verse-record ↔ term | `wa_verse_records.mti_term_id`/`term_id` → `mti_terms` | FK/id | live |

**Corollary — the strong is not a key.** It repeats within a verse and across the corpus. Nothing joins on the strong; everything joins on `verse_span_index.id` (or `verse_id,word_index`).

## 3. What lives on a single master span
A master span (one word occurrence) can simultaneously carry:
- a **role** and a **char_candidate** flag (columns on the master itself);
- **one lexical** (`ve_lexical` rows for its 16 dimensions) — *if* it is a characteristic;
- **one verse-record** (`wa_verse_records`) — *if* its term is a registered IB term;
- a **term** identity (`primary_strong`).

So the master span is the junction where **term, lexical, verse-record and role meet**. The verse groups spans; the passage groups verses.

## 4. Authoritative vs DEFUNCT (researcher rule 2026-07-08: anything not in the master referencing system is defunct)
- **Authoritative lexical** = a `ve_lexical` row whose `verse_span_id` resolves to a master span. **511,527 rows.** The live model is further marked by `pair_kind IS NOT NULL`.
- **DEFUNCT lexical** = `ve_lexical` with `verse_span_id` NULL / unresolved (**322 rows**), plus `ve_lexical_legacy` (507,651 archived rows). Excluded — no value.
- **DEFUNCT evidence** = `verse_evidence_index.evidence_type='lexical'` (423,968 rows): **0 resolve to a live `ve_lexical`** — they point at archived ids. This index is **not maintained for lexicals**; treat as defunct. (Its `span`→master rows are 100% live and its `unit`→verse-record rows 96% live, but the cycle does not depend on it — the master + `ve_lexical` give full forward/back tracking directly.)

## 5. verse_evidence_index — is it part of the process? (answer: no, for this cycle)
`verse_evidence_index` is a per-`verse_id` catalogue of `span` / `unit` (verse-record) / `lexical` / `finding` evidence. For **this cycle it is not load-bearing**: forward/back tracking is done directly on the master (`role`, `char_candidate`, `verse_span_id`) and `ve_lexical`. Its `lexical` rows are stale (§4). **The cycle does not read or maintain it.** If it is ever to be the canonical evidence ledger, it needs a rebuild against live `ve_lexical` — a separate decision, not part of this cycle.

## 6. Forward / backward tracking (how you traverse the web)
- **From a passage →** its verses (`verse.passage_id`) → their master spans (`verse_span_index.verse_id`) → each span's role, lexical (`ve_lexical.verse_span_id`), verse-record (`wa_verse_records.verse_span_id`), term (`primary_strong`).
- **From a lexical →** its master span (`verse_span_id`) → verse (`verse_id`) → passage (`verse.passage_id`); and → its verse-record and term off the same span.
- **From a term (strong) →** its master spans (`primary_strong`) → per occurrence: verse, passage, lexical, verse-record.
- **Completeness ledger:** a verse is fully read when every real-strong span carries a `role`; `role IS NULL` on any span ⇒ that verse is not yet accounted for.

## 7. The verse-record ↔ characteristic gap (bears on passage compilation)
The study intends that a **characteristic relates back to a verse-record** (the registered IB occurrence). Currently it does **not**, at scale:
- OT candidate spans **with** a verse-record: **6,284**
- OT candidate spans **without** a verse-record: **24,402**

So the seed (candidate characteristics) is far broader than the registered verse-records. The 24,402 are characteristics the registry never recorded — the **gate-1 completeness debt** (term not recorded / verses not pulled / links not built) from the per-book corrective method. Passage compilation "around characteristics that relate to verse-records" therefore has to treat the verse-record as the *anchor where it exists*, and flag the candidate-without-record spans as a per-book gate-1 gap to close — not silently assume every characteristic already has a record.

## 8. Object roll-call (authoritative / legacy / defunct)
| object | table | role in the cycle |
|---|---|---|
| verse | `verse` | the read unit; carries `passage_id`, `process_marker`, `genre` |
| passage | `passage` | reading-unit grouping of verses (anchor = first verse) |
| master span | `verse_span_index` | THE hub; `role`, `char_candidate` |
| lexical | `ve_lexical` (master-linked, `pair_kind` NOT NULL) | the 16-dimension decomposition of a characteristic |
| verse-record | `wa_verse_records` | registered IB-term occurrence; the intended anchor for a characteristic |
| term | `mti_terms` (+ `word_registry` for the seed) | the strong/lemma identity |
| verse_evidence_index | — | **not part of this cycle** (lexical entries defunct) |
| verse_context | `verse_context` | old per-verse classification — legacy, not used by this cycle |
| ve_lexical_legacy | `ve_lexical_legacy` | archived pre-M63 — defunct |

*Filed 2026-07-08. Verified against live DB. This is the substrate reference for the cycle instruction.*
