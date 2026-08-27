# Prose Edit — Programme — Chapter 6

<!-- Edit only the prose body below each chapter heading. Do not change markers. -->
<!-- This file is temporary and can be discarded after patch application. -->

<!-- PROSE_SECTION_ID: 67 -->
<!-- PROSE_SECTION_TYPE: prog_instr_session_b_readiness -->
<!-- PROSE_BOOK: Programme -->
<!-- PROSE_SECTION: Programme -->
<!-- PROSE_CHAPTER_NO: 6 -->
<!-- PROSE_CHAPTER_TITLE: Programme — Session B — Analysis Readiness -->
<!-- PROSE_SORT_ORDER: 120 -->
<!-- PROSE_VERSION: 2 -->
<!-- PROSE_SOURCE_FILE: programme-prose-v2-recommendations-v1-20260427.md -->

## Session B — Analysis Readiness

The Session B Analysis Readiness instruction governs the readiness phase of Session B — the stage that prepares a word for analytical work. Under Architecture v2 (effective 2026-04-27) this phase is owned end-to-end by Claude Code: AI's involvement is limited to receiving the readiness output and proceeding into Analysis Output.

Claude Code generates two paired artefacts per registry: a readiness `.md` (human-readable, structured into 14 sections covering registry overview, term inventory, lexical foundation, XREF terms, group landscape with dimensions, correlation signals, existing flags and findings, thin-evidence flags, verbatim verse text, legacy-VC notice, generic catalogue with embedded JSON, readiness verification, and open Session B items) and a readiness `.json` (machine-readable mirror). The structure is deterministic — same DB state produces byte-identical output modulo timestamp — and the generation can be re-run any time the database state changes.

The §N Open Session B Items section carries forward every `wa_session_b_findings` row at status `open` for the registry — Stage 2a observations from prior sessions that have not yet resolved, plus any anomalies CC raised during post-write validation of past obslogs. Each open item must reach one of four outcomes by the close of the upcoming analytical session: resolution via a Q&A pair, conversion to an SD pointer, raising as a new GAP catalogue question, or marking as no-longer-relevant with reason. The instruction treats §N as non-negotiable; an analytical session that closes leaving §N items open has not closed cleanly.

Pre-flight integrity checks run before the readiness output is issued. CC verifies anchor count consistency, dimension assignment coherence, term-status integrity, and group description versus dimension drift. When an inconsistency surfaces, CC writes a `wa_session_b_findings` row at status `open` with a `DATA_ANOMALY_*` finding type — making the anomaly visible to AI in the next session's §N. This bidirectional channel between CC's data validation and AI's analytical review is the mechanism by which the database and the analytical record stay coherent.

For revision sessions — when a registry has been analysed before and is being revisited — CC produces an additional artefact: the analytic status `.md`+`.json` companion, capturing lifecycle summary, resolved Q&A pairs, resolved SD pointers, not-relevant findings, prior chapters, anchor-verse analytical notes, and open items. AI for revision sessions reads both the readiness output (current data) and the analytic status (prior analysis) and produces an obslog reflecting any shifts.

Analysis Readiness is a discipline of preparation — under v2, it is the discipline of producing a data artefact that prompts AI to deal with every field it presents and to resolve every open item carried into the session. It does not itself produce analytical output; it produces the readiness state and the open-item agenda.

---
