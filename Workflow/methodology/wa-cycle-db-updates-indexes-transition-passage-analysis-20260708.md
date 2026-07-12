# Cycle instruction — DB updates, index maintenance, transition & passage cross-reference (analysis)

> Investigation feeding the additions to `Workflow/Instructions/wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md`. Answers the researcher's four asks: (1) transition processes, (2) does the cycle update all indexes, (3) other related DB updates, (4) cross-reference the passage instruction and make the two work together. 2026-07-08.
>
> **✅ RESOLVED & APPLIED 2026-07-08.** The researcher decided all three §6 decisions and the instruction is finalised: **(1)** `verse_evidence_index.lexical` = **deprecated/defunct** (option A). **(2)** read-vs-legacy roles marked by **`role_provenance = 'read-2026'`** (yes) — column already exists on the master (M64). **(3)** passage scope = **candidate characteristic** (the heart), verse-record = entry/anchor; and — stronger than the "union" proposed in §4 — **a `char_candidate` span with no verse-record is a DB integrity violation** that must be repaired (verse-record + term + relations) *before* the passage is read, not a scope union. Applied to: **§4A / §7A / §7B** of the cycle instruction, and **`wa-passage-completeness-rule-v2-20260708.md`** (supersedes v1). §2–§4 below record the original options; §6 is now closed.

---

## 1. What a verse read actually writes (the DB-update checklist)
There are **no triggers** on `ve_lexical`, `verse_span_index`, or `verse_evidence_index` — **all maintenance is manual and must be done by the cycle.** Per verse read:

| # | table / column | write | when |
|---|---|---|---|
| 1 | `ve_lexical` | create/revise the 16-dimension rows for each characteristic (+ its pairs) | core of the read |
| 2 | `verse_span_index.role` | write back **every** span's role (char/qualifier/standalone/undecided) | on completion (§7) |
| 3 | `verse.process_marker` | mark the verse read (completion ledger) | on completion |
| 4 | `verse_span_index.char_candidate` | re-stamp when the seed changes (self-learning) | Stage 3 feedback |
| 5 | `verse.passage_id` / `is_passage_anchor` / `genre` | **prerequisite** — set by the passage step *before* the read | Stage 0 (passage) |
| — | `verse_term_index`, `verse_morphology`, `verse_span_index` rows | **not touched** — derived from morphology, upstream of this cycle | — |

## 2. ⚠ DECISION 1 — `verse_evidence_index` is stale for lexicals
`verse_evidence_index` catalogues, per verse, its `span` / `unit` / `lexical` / `finding` evidence. **Its `lexical` entries are 100% stale:** 423,968 rows, **0** resolve to a live `ve_lexical.id` (they point at pre-M63 archived ids; `ve_lexical` live = 511,849, `ve_lexical_legacy` = 507,651). So either:
- **(A)** the evidence index is **deprecated for lexicals** — then the instruction says so, and the read does not maintain it; or
- **(B)** it is a **live index the cycle must maintain** — then the read must (re)write the `lexical` evidence rows to point at the new `ve_lexical` ids, and we need a rebuild of the 423,968 stale rows.

**Recommendation: (A) for now** — treat `verse_evidence_index.lexical` as deprecated/legacy, since nothing in the live cycle reads it and the master (`verse_span_index.role`/`char_candidate`) + `ve_lexical` already give full forward/back tracking. If it is meant to be the canonical evidence ledger, choose (B) and we schedule a rebuild. **Your call.**

## 3. ⚠ DECISION 2 — the transition (legacy → read-derived), for role AND lexical
Two legacy layers coexist and must change over cleanly:
- **Roles:** `verse_span_index.role` currently holds the **M64 backfill** (the old `ve_lexical` `ve_nr=115` roles, ~50% wrong). The read **overwrites** these verse-by-verse (§7). Until a verse is read, its role is the untrusted backfill.
- **Lexicals:** `ve_lexical` live (511,849) contains the **mechanical/legacy** rows (incl. the NULL-pair mechanical pass and the imperfect existing lexicals); `ve_lexical_legacy` (507,651) is the archived pre-M63 set. The read **revises** the live rows for a characteristic (or builds them where missing).

**Transition rule to state in the instruction:** a span/verse is in one of exactly two states — **legacy (untrusted)** until its verse is read, or **read-derived (authoritative)** once `process_marker` is set and roles written back. The completeness ledger (§7: `role IS NULL` ⇒ unread) is the transition tracker. **Question for you:** do we distinguish "read-derived" from "legacy-backfilled" on the master with a `role_provenance` value (e.g. `read-2026` vs the M64 tag), so a query can separate trusted from untrusted roles during the multi-book changeover? **I recommend yes** — otherwise mid-transition you cannot tell a trusted role from a backfilled one.

## 4. ⚠ DECISION 3 — passage instruction vs the cycle: the IB-relevance definitions diverge
The passage rule (`wa-passage-completeness-rule-v1-20260707.md`, step b) defines a passage's scope by **verse-records** ("every verse with an active `wa_verse_records` must be in a passage"). The new cycle defines IB-relevance by **`char_candidate`** (the seed). These are **different populations**:

- **1,051 verses have a `char_candidate` span but `passage_id IS NULL`** — they are **not in any passage**, so the cycle **cannot read them yet** (the read needs the passage). This is a live blocker.
- **10,202 verses have a verse-record but no `char_candidate` span** — the old rule passages them; the seed sees no candidate there.

**These two instructions do not currently agree on what makes a verse IB-relevant.** To make them work together, the **passage-determination scope must be driven by the same signal the cycle uses** — the candidate seed — not (only) by verse-records. Proposed reconciliation:

- **Passage scope becomes:** verses where `passage_id IS NULL` AND (`has a char_candidate span` **OR**, during transition, `has an active verse-record`). The union keeps the old verse-record coverage while adding the 1,051 candidate-only verses.
- The passage rule's mechanics (consecutive-run grouping, merge/prepend/extend/create, integrity gate) are unchanged — only its **scope test** is widened to include `char_candidate`.
- The passage step is **Stage 0** of this cycle (prerequisite): no verse is read before it is in a passage. The cycle instruction must cross-reference the passage rule and state this ordering.

**Your call on the scope union** (candidate-only, or candidate ∪ verse-record during transition).

## 5. Proposed instruction additions (once decisions are made)
- **New §: "Stage 0 — passage prerequisite"** — cross-references the passage rule; states no verse is read outside a passage; widens the passage scope test to `char_candidate` (Decision 3).
- **New §: "DB updates & index maintenance"** — the §1 checklist as a normative list; states no triggers exist so the read must write items 1–4 explicitly; resolves `verse_evidence_index` per Decision 1.
- **New §: "Transition & changeover"** — the two-state model (legacy-untrusted vs read-derived), the `role IS NULL` ledger, and the `role_provenance` distinction (Decision 2).
- **Passage rule doc** gets a reciprocal cross-reference back to the cycle instruction, and its scope test updated (Decision 3).

## 6. Summary of decisions blocking finalisation
1. `verse_evidence_index.lexical` — deprecate (A, recommended) or maintain+rebuild (B)?
2. Mark read-derived vs legacy roles with a `role_provenance` (recommended yes)?
3. Passage scope union — `char_candidate` only, or `char_candidate ∪ verse-record` during transition (recommended)?

*Filed 2026-07-08. No DB writes. Awaiting decisions 1–3 before editing the authoritative instruction.*
