---
name: project_l2_verse_read_meaning_live
description: LIVE (2026-06-09): the L2 verse-read=meaning pipeline is built, validated, and M01 is COMPLETE (1036/1036 own verses, all 85 terms). scripts/_apply_verse_read_meaning.py — verse-complete (one verse read once, every in-scope term's findings routed to its OWN cluster), engine-logged (engine_run_log + engine_stream_checkpoint per term, resumable/idempotent), Sonnet 4.6 API. Output per term-in-verse = ~14 separately-identifiable tier findings (provenance l2_api) + a MEANING PARAGRAPH (provenance l2_meaning) that collates them in verse context. ~14 USD + ~4.5h per first cluster; cross-cluster fan-out already seeded 47 clusters. Flagged-for-review = free-text-omission self-audit, ~5%.
metadata:
  type: project
---

**The verse-read = meaning layer is operational (2026-06-09).** This is the spine of the largest task of the
study. Plan: `research/investigations/wa-verse-read-meaning-plan-v1-20260609.md`.

**What it is.** For each verse (read ONCE, verse-complete), the Sonnet 4.6 API extracts the verse-level
record for every in-scope term in the verse and writes a **meaning paragraph** that collates the answered
tier questions in the verse's context. Mechanical-first; API does the synthesis CC cannot. STATE-not-induce
(NONE/SILENT/not-stated first-class). Each tier element is a **separately-identifiable `finding`**
(provenance `l2_api`, linked to its catalogue obs_id); the paragraph is its own VERSE finding (provenance
`l2_meaning`). Faculty + location are multi-select (per-term from meaning, [[feedback_faculty_must_be_per_term_not_per_cluster]]).

**Verse-complete + idempotent.** Term-by-term loop drives iteration/checkpointing, but the read unit is the
verse: `fetch_verse_block(ref)` gathers every clustered term at the reference lacking a meaning finding; each
term's findings route to its OWN cluster (`finding.mti_term_id/cluster_code`). Skips already-read (verse,term)
pairs, so cross-cluster terms are written once and NOT re-read when their cluster runs ([[project_l2_writer_verse_complete]]).

**Control.** `engine_run_log` (run) + `engine_stream_checkpoint` (per term: status complete/review/error,
timestamps, rows_written, resume). Per-verse self-audit (API semantic SELFAUDIT + CC free-text backstop) →
`flagged_for_review`; per-term self-audit gates `complete` vs `review`. Re-launch `--cluster M01 --live`
resumes cleanly.

**M01 result.** PASS ~4h23m, ~$14.4 (in 595k / out 838k Sonnet tokens). M01 own 1036/1036; 2750 paragraphs +
61k tier findings; cross-cluster fan-out seeded **47 clusters** (head start). Flag rate **~5%** (mostly
word-overlap artifacts). ra.gaz surfaced as grief/quarrel-not-fear (clustering signal).

**Open / next.** Subsequent clusters are cheaper (M01 already seeded their overlap). `cache_read=0` — the
system prompt is <1024 tokens so prompt-caching doesn't engage; pad it before the full-corpus run to cut
input cost (minor at single-cluster scale). The catalogue refit D1–D4 and verse-extraction-spec D1–D5 are
still pending researcher markup but the field set is in use. SYNTH tiers (roll-up over the verse records) are
the layer above, not yet built.
