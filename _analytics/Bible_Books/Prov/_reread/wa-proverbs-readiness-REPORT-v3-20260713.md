# Book lexical-readiness — Proverbs (book_id=20, seg='Pro')

**VERDICT: READY-WITH-DEBT (amber)**  ·  preconditions: 12 green / 2 amber / 0 red


## A. DB integrity & traceability (I1-I11)
- [OK  ] **I1 Referential** (PRECONDITION): dangling: ve_lex.vctx=0, wvr.span=0, wvr.mti=0, wvr.reg=0
- [OK  ] **I2 Master-index coverage** (PRECONDITION): candidate spans with NO (verse,term) verse-record = 0/2123
- [OK  ] **I3 Traceability(char->span->verse)** (PRECONDITION): candidate spans whose verse_id does not resolve = 0
- [OK  ] **I4 Passage membership (Stage 0)** (PRECONDITION): all 799 char-verses belong to a passage
- [info] **I4b Read completeness** (READ-OUTPUT): covered candidate spans with no lexical yet = 40 (whole book pre-read; informational)
- [info] **I5 Ledger completeness** (READ-OUTPUT): candidate spans carrying any active lexical = 2083/2123 (baseline measures detail)
- [info] **I6 Role decidedness** (READ-OUTPUT): candidate spans with role=NULL = 40 (role is assigned BY the read; not a pre-read defect)
- [info] **I7 ib_char linkage** (READ-OUTPUT): candidate spans with ib_char_id=NULL = 2123/2123 (populated BY the read; empty pre-read is correct)
- [WARN] **I8 Pair endpoints (span-id rule)** (PRECONDITION): active pairs with STRONG'S-encoded endpoints (must be span-ids) = 2437  -> re-read must write integer span-id endpoints
- [info] **I10 Candidate/role relation** (READ-OUTPUT): role='characteristic' spans not seed-flagged char_candidate = 266 (candidate!=role is allowed; emergent chars get stamped + seed-fed during the read)
- [info] **I11 Char-on-master** (READ-OUTPUT): role='characteristic' spans with no characteristic word = 1708 (written BY the read)
- [OK  ] **D1 Role backfill** (PRECONDITION): spans with an active ve_lexical but role IS NULL = 0 (defect: back-fill role from the lexical)
- [WARN] **D2 Lexical only on characteristic** (PRECONDITION): non-characteristic spans carrying an active ve_lexical = 4117 (old-model debt; changeover: read rebuilds characteristic-only, old lexicals soft-deleted) by role: standalone=3119, qualifier=601, process-qualifier=397

## B. Isolation of superseded data
- [info] **Active-lexical provenance** (PRECONDITION): active ve_lexical by provenance: lexical-model-2026=22342; role-reassess-2026=1193; locus-derivation-v1-20260704=725
- [OK  ] **Legacy isolation** (PRECONDITION): ve_lexical_legacy rows joinable to book spans = 0 (archive; must not be read)
- [OK  ] **I13 mti-uniqueness** (PRECONDITION): candidate strongs with >1 active mti_terms row = 0 (unique)

## C. Seed sanity
- [OK  ] **Seed coverage** (PRECONDITION): candidate spans=2123/6918 (30%); role dist: standalone=3119, characteristic=1708, (null)=1093, qualifier=601, process-qualifier=397
- [OK  ] **Candidate tags present** (PRECONDITION): candidate spans with no char_candidate_tag = 0
- [info] **Role mix (info)** (READ-OUTPUT): roles present: standalone=3119, characteristic=1708, (null)=1093, qualifier=601, process-qualifier=397 (all of characteristic/qualifier/standalone are valid; assigned by the read)
- [OK  ] **Seed terms in mti_terms (OT-DBR-009)** (PRECONDITION): candidate base-Strong's with NO active mti_terms row = 0/325

## E. Config & tooling
- [OK  ] **Genre set** (PRECONDITION): genre: poetic/wisdom=915
- [OK  ] **Re-read tooling present** (PRECONDITION): all reusable scripts present
- [info] **Segment units** (PRECONDITION): segment_unit rows for 'Pro' = 323

## F. Baseline anchor
- [OK  ] **Baseline filed** (ANCHOR): baseline report(s): ['verse-analysis\\proverbs\\_reread\\wa-proverbs-reread-BASELINE-20260708.md', 'verse-analysis\\proverbs\\_reread\\wa-proverbs-reread-BASELINE-v2-20260709.md']

_Read-only. Per `wa-book-lexical-readiness-assessment-AUTHORITATIVE-v1-20260712.md`. Preconditions must be green/waived before Stage 0; READ-OUTPUT items are expected empty pre-read._
