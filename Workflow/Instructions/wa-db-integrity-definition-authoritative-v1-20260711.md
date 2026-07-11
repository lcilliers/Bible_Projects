# DB integrity — AUTHORITATIVE DEFINITION (v1)

> **Why this exists:** "DB integrity" was used repeatedly (including by me) without ever being defined — which let ledger-completeness be reported as "full integrity" when 261 characteristic spans were master-index orphans and 18 had no passage. This document **defines** integrity for the verse-analysis / reread data, derived from the **schema** (declared FKs + the bypass-link model) and the **stated expectations** (per-book corrective method step (e); passage-completeness-rule-v2). It is the target that step (e) and any "integrity-clean" claim must be measured against. **v1 — open to researcher correction; version-bump on change.**
>
> Grounding facts (verified 2026-07-11): declared FKs — `ve_lexical.verse_span_id→verse_span_index.id`, `ve_lexical.verse_context_id→verse_context.id`, `wa_verse_records.{verse_id→verse, book_id→books, term_inv_id→wa_term_inventory, file_id→wa_file_index}`. `verse_span_index` and `verse` declare no FKs (bypass-link model, memory `reference_file_index_legacy_use_bypass_fks`). Master index = `wa_verse_records` (term ↔ span ↔ verse).

## The invariants (a book/dataset has integrity iff ALL hold)

| # | Invariant | Grounded in | Check (per book, scope `v.book_id`) |
|---|---|---|---|
| **I1 Referential** | Every active `ve_lexical.verse_span_id` resolves to a `verse_span_index` row; every `verse_context_id` resolves; every `wa_verse_records` FK resolves. No dangling references. | declared FKs | LEFT JOIN each FK; expect 0 unresolved |
| **I2 Master-index backlink** | Every `role='characteristic'` span has a live `wa_verse_records` row (`verse_span_id`) tying it to its term (`mti_term_id`/`term_inv_id`) and verse (`verse_id`). **A characteristic span with no verse-record is a violation.** | passage-rule-v2; memory `project_lexical_cycle_finalised_and_integrity_invariant` | char-spans with `NOT EXISTS(wa_verse_records …)` = 0 |
| **I3 Forward/backward tracking** | For every characteristic span both directions resolve **by index/FK, never text-scan**: master-index → passage → lexical → verse, and verse → span → lexical → characteristic. | per-book method (b),(e) | trace both directions; 0 breaks |
| **I4 Passage membership** | Every verse carrying a characteristic span has a `passage_id` resolving to a `passage` row. | per-book method (b) | char-spans whose verse has NULL/dangling `passage_id` = 0 |
| **I5 Ledger completeness** | Every characteristic span carries its full genre-mandatory ledger (M set + 114 discovery + 115 role + 116 locus); every mandatory dimension **explicitly stated** (`none` written, not omitted). | reread process doc §2; G10 | missing-dim chars = 0; ZERO-dim = none |
| **I6 Role screen** | `role ∈ {characteristic, qualifier, standalone}` with `role_provenance` stamped; **no characteristic span has God as bearer (105)** (IB-screen). | Screen 0; `wa-ib-relevance-screen-correction` | God-bearer chars = 0; unroled candidates = 0 |
| **I7 Characteristic-model linkage** | Every characteristic span links to a **defined characteristic** in the characteristic table (the many-instances → one-defined-characteristic connection). | current direction (2026-07-11): "working towards defined characteristics" | char-spans not linked to a characteristic = 0 · ***clause + structure finalised with the characteristic-table restructure (see the (b) plan); until that is approved this invariant is DECLARED-PENDING, not yet enforceable*** |
| **I8 Soft-delete consistency** | `delete_flagged` applied consistently; no active row depends on a soft-deleted parent; pair endpoints (`from_span`/`to_span`) reference live spans. | soft-delete model; `_check_softdelete_integrity` | 0 active-on-deleted |
| **I9 Provenance** | Provenance stamps present + consistent per dataset (`role_provenance`, `ve_lexical.source_provenance`, `verse.process_marker`). | reread process doc §3 | 0 missing/mismatched |

## Rules of use
1. **"Integrity-clean" means ALL of I1–I9 pass** for the scope claimed. A subset (e.g. I5+I6, the step-(c) ledger gates) is **not** integrity — name it precisely ("ledger-clean", not "full integrity").
2. **Book-close (step e) requires I1–I9 = pass.** No book is "done" on the ledger read (step c) alone.
3. **One check runs them all:** a single per-book integrity script (extend `_integrity_full_check.py` → `_check_book_integrity_v1`) reports each invariant's violation count. Every write that is "integrity-gated" runs it pre + post and expects no new violation.
4. **Report violations with counts, never a bare "clean."** (2026-07-11 baseline for Psalms: I2 = 261, I4 = 18, I7 = 2,168-unlinked, others pass.)

*Filed 2026-07-11. Authoritative for what "DB integrity" means. Subordinate only to the researcher's direction. I7's enforceable form depends on the characteristic-table restructure being approved.*
