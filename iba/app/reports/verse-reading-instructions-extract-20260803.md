# Verse-reading instructions — extract, not synthesis

> Straight extraction of every existing IBA-app instruction, governance rule, build-record entry, and memory entry touching verse reading — governance, `BUILD.md`, `iba/docs/` method docs, `iba/app/config/CONFIG-REPORT.md`, and memory. Nothing here is blended into a new rule; each block is sourced and, where short enough, quoted in full. Excluded on purpose: memory files that turned out, on checking, to belong to the *other* system (`bible_research.db` / the main Bible-study programme's `ve_lexical`/`finding`/cluster model) — CLAUDE.md is explicit that the two are separate; conflating them would misrepresent what "this app" actually has on record.

---

## 1. The core finding, stated first

**A base-verse-reading technique document already exists, dated today, and I did not consult it before doing the Obadiah exercise earlier in this session.** `iba/docs/WA-verse-reading-technique-v2-2026-08-03.md` — eight numbered rules (T1-T8) for exactly the "read a verse lexically, in isolation, before any phenomenon/movement question" task this session has been designing from scratch. It is **DRAFT, marked explicitly unconfirmed** by the researcher, and — checked directly against `CONFIG-REPORT.md`'s `method.*` settings table (§5 below) — **it has no `cfg_setting` pointing to it and no report/handler consumes it**, unlike its two companion docs (`passage_read_guidance`, `interpretation_questions`), which are both wired in. It is written but not yet plumbed into the app.

This matches, exactly, an existing feedback memory on file: [`feedback_iba_record_rules_when_set_in_configs`](#6-memory) — a rule not recorded/wired at the point it's set gets rediscovered by archaeology instead of applied. That is what happened this session.

---

## 2. `iba/docs/WA-verse-reading-technique-v2-2026-08-03.md` — base lexical reading (T1-T8)

**Status:** Version 2, DRAFT, not yet confirmed by the researcher — "being tested against further passages before it is treated as settled." Supersedes v1 (archived same day). **Not yet config-registered.**

**Scope, as the document itself states it:** covers *only* the base reading — establishing what a clause actually says, lexically and grammatically — as its own complete, standalone pass, done **before** any phenomenon/movement question. Phenomenon and movement isolation is explicitly a separate step, under separate instructions, not described here. v1 was corrected into this shape because mixing the two "causes the analyst to start framing a clause in terms of the phenomenon/movement model before the plain reading is even settled, which drifts the reading itself."

**Input it assumes:** the verse-span-meaning extract's row — `# | surface | strong | morph | particle | meaning` (meaning = stepGloss + full meaning_tree).

**T1 — Work from the row, not the gloss.** Unit of analysis is the row, not the English translation printed above the table. Don't extract English clauses and match them against a keyword checklist.

**T2 — Pull the full lexical range before assigning a sense.** Read the whole meaning_tree, not just stepGloss or the one sense the translation uses. Record explicitly when a sense the translation doesn't use is already a standing lexical-range member (stated via the lexicon, not inferred), and when the range is genuinely ambiguous — name the live senses and reason which is operative, don't silently pick one.

**T3 — Let morph decide voice, person, and aspect — never English word order or tense.** Read every verb's morph code: perfect/imperfect/participle carry different aspectual force (a passive participle is durative — "is, continually" — not a future event); person/number decides the actual grammatical subject, not an inferred English pronoun; voice (Qal active / Niphal / Pual / Hiphil / passive participle) decides whether the subject acts or is acted upon.

**T4 — Separate the causing action from the resulting condition.** Where a verse has both (e.g. "I will make you small" → "you are despised"), record both as separate grammatical facts — who performs the action, who is in the resulting condition. Don't collapse them; don't report only the resultant term.

**T5 — Referent cruxes: name every grammatically live reading, adopt one explicitly, keep the rest on record.** For a genuinely ambiguous pronoun/party (e.g. Obad 1's "we"): (1) enumerate every grammatically/contextually live reading, (2) give textual grounds for each, (3) adopt one explicitly and state whether the choice is a directed/researcher call or the pass's own default, (4) keep the rejected alternatives on record.

**T6 — Unstated agents: record as genuinely open, not resolved either way.** A passive verb with no stated agent (e.g. "a messenger has been sent") gets recorded as "expected an agent, none given — genuinely open/underdetermined," not a guess in either direction.

**T7 — Record genre-conventional elements that are expected but textually absent.** Where the verse's form (vision report, call narrative, lament…) conventionally carries an element elsewhere in the corpus and it's absent here, record the absence explicitly. Don't fill it in from convention; don't pass over the comparison silently.

**T8 — Self-check before closing a verse.** Before moving to the next verse, confirm every output of *this* reading — sense (T2), grammatical call (T3/T4), referent (T5), open case (T6), absence (T7) — traces to a specific row/field (Strong's, morph, meaning_tree entry), not an English keyword match. Scoped only to the base reading's own outputs, not to any phenomenon/movement judgment (a separate step's own check).

---

## 3. `iba/docs/WA-passage-read-guidance-v1.5-2026-08-02.md` — phenomenon + operation identification (passage-level, per-verse)

**Status:** current, config-registered (`method.passage_read_guidance_path`). Supersedes v1.4. Restructured after the researcher found the Amos 1-3 debate had drifted from per-verse inner-being phenomena into general/textual patterns (a repeated oracle formula, a claimed "ring-composition," a book-wide "thesis") with operations constructed to fit them — a drift diagnosed as procedural, not just a caution.

**Three phases, strict sequence, run across the *whole* debated range before advancing:**

- **Phase 1 — phenomenon identification (every verse, completed for the whole range before Phase 2 starts).** Read the verse → does it bear on the IB, else set aside → for **every** inner being present, isolate the phenomenon (state/disposition/characteristic, possibly hidden behind a stated or refrained-from act) → record **why** it's regarded as such (the specific textual warrant, stated or inferred) in a **phenomena register**, written independently of and before any operation.
- **Phase 2 — operation generation (separate pass, only after Phase 1 is complete for the whole range).** For each registered phenomenon: state what the verse says about it as an operation (state/status, or a movement — come from / go to / impact on / emerge / go away / become evident); record subject / operation / source / target / action-type label. An operation may **only** originate from an already-registered Phase 1 phenomenon — Phase 2 must never invent a fresh one to make an operation work. If writing the operation reveals no genuine phenomenon underlies it, that's a signal the Phase 1 entry was mis-identified — go back and fix the register, don't paper over it.
- **Phase 3 — validation (closing pass, once the whole per-verse debate is assembled).** For each phenomenon (or a representative sample): is it genuinely an inner-being state/disposition/characteristic, not a textual/structural pattern in disguise? Does its Phase 1 justification actually warrant it? Does its Phase 2 operation track faithfully back to it? Record the outcome; **correct failures before the debate counts as filled** — not just logged for later.

**Key notes:**
- Step 1 note (a): a recorded operation always has subject (the inner being in focus) / operation (state of, happening in, impacting/impacted by) / source (another operation, human, non-human, object, or situation) / target (same options) — source/target may be singular, multiple, mixed, or absent.
- Step 2 note (a): multiple inner beings in one verse are each considered separately, plus the movement *between* them.
- Step 2 note (c): a collective (tribe, youths, nation, gentiles…) is a movement to/from a collection, not an individual.
- **Step 2 note (f) — the candidate rule:** "every human mentioned is a presumptive IB candidate. any human — named or collective, major or minor, however briefly mentioned — who performs an act, undergoes an act, thinks, speaks, refrains from acting, or is simply named as present, is a candidate operation." An outward/administrative/incidental-looking act does **not** license skipping it — "no phenomenon found, silent" is a valid *result* of running the check, never a valid *substitute* for running it. Every human in the passage should be traceable to a phenomena-register entry, even if the entry records silence.
- Step 3 note (d): phenomena may link to another phenomenon elsewhere in the passage — that's the Q7 interrogative's job, applied once operations exist, not Phase 1's.
- Step 5 note (a): every operation carries an action-type label (a short verb-based tag — "gave," "worshiped," "bound and cast" — not drawn from or building a fixed list) so the same action-type can be found and weighed together wherever it recurs.
- Step 5 note (b) / Step 6 (Phase 3, new in v1.5): validation should specifically watch for phenomena/justifications that read as describing the passage's own literary architecture (recurring formula, claimed compositional structure, book-wide argument) rather than a specific inner being's state — the exact failure the phase-separation exists to prevent. A genuine literary/structural observation, if noticed, is logged once as an emergent question, never built into the register or an operation.

---

## 4. `iba/docs/WA-interpretation-questions-v1.4-2026-08-02.md` — the interrogative (Q1-Q12) + guidance (Part B)

**Status:** current, config-registered (`method.interpretation_questions_path`). Companion to the guidance doc above; same 2026-08-02 Amos-1-3 review prompted the new Q12/Part B.12.

**Part A — applied to every human/human-act in a qualifying verse, once its phenomenon is registered and operation written. Every question is *considered* for every candidate; it need not resolve, but must be considered:**

- **Q1 Focused inner being** — is this person a focused IB in their own right even where only an outward act is stated?
- **Q2 Implied interior** — what interior state/disposition/intent/volition could underlie the stated act?
- **Q3 Stated vs inferred** — is the interior stated in text/span-data, or inferred? If inferred, name it as referential, never assert as fact.
- **Q4 Source (state vs enablement)** — source of the interior state, and *separately* source of the enablement to act (self/human/non-human/object-situation) — same source or different? Stated or inferred?
- **Q5 Target** — what does the operation impact?
- **Q6 State or movement** — which is it?
- **Q7 Linkage** — what links to other operations in the passage; surface absence, don't pass over it silently. (B.12: a Q7 linkage connects two specific, already-registered items — it is not license to narrate a pattern across a whole chapter range.)
- **Q8 Collective** — if the human is a collective, how does that reshape the operation as a movement to a collection?
- **Q9 Sufficiency** — does the document contain enough data to weigh this operation? If not, name the insufficiency; don't supply it from outside.
- **Q10 Emergent questions** — what new question does this verse raise that the instrument doesn't yet hold? Log and carry forward. (A genuine literary/structural observation is logged *here*, once — not built into the register/an operation as if it were content.)
- **Q11 Action-type** — a short, verb-based label for what was done, regardless of how Q1-Q9 resolved.
- **Q12 Divine mirroring** — where a human operation sits alongside or shares action-type/vocabulary with a stated divine operation, does it compare/differ/invert — recorded only where the text's own juxtaposition/wording/statement supports it; a merely-plausible resemblance is logged as Q10, not asserted.

**Part B guidance (numbered as in the doc):**
1. Consider, don't force-resolve — leaving a question open is fine; not considering it is not.
2. Referential debate is legitimate provided nothing inferred is imported as fact.
3. Inference is named as inference at the point it's made.
4. Silence is a finding — recorded as the result, not filled.
5. Source of state ≠ source of enablement — keep them separate; extending sourcing from outcome to interior is a flagged interpretive step, not assumed.
6. Observation / interpretation / reflection are distinguished and labelled.
7. Insufficiency is named, not papered over.
8. Emergent questions are carried forward.
9. Interpretive forks are tracked, not escalated — weighed against new data as the corpus grows, not settled in the abstract.
10. Action-type is a label, not a taxonomy — no controlled vocabulary/enum is being built by this note.
11. Mirroring is observed, not manufactured — anchored only in the text's own juxtaposition/wording/statement; no general theological elaboration.
12. **(new, v1.4) The phenomenon comes first, is registered before any operation, and batching does not license book-architecture narrative-building.** Identifying a general/textual phenomenon (recurring formula, structural pattern, book-wide "thesis") and constructing an operation to fit it is a named failure mode, not a shortcut — it produces a narrative about the text's own architecture, not about an inner being's operation.

**Part C — output directive**, per passage: one debate document (`WA-[passage]-debate-[version]-[date].md`) containing, in order — preliminaries; phenomena register (Phase 1); per-verse operations (Phase 2, with observation/operation-parts/Q1-Q12/referential debates/mirroring/decision); passage-level linkages (Q7); insufficiencies register; emergent-questions log (incl. interpretive forks and literary/structural observations); debate-quality validation (Phase 3, new); open decisions/next steps.

---

## 5. Config anchors (`iba/app/config/CONFIG-REPORT.md`)

| setting | value | note |
|---|---|---|
| `method.passage_read_guidance_path` | `iba/docs/WA-passage-read-guidance-v1.5-2026-08-02.md` | "the passage-debate scaffold and any AI applying it must follow this exact file; bump this setting (not the debates' memory) when the guidance revises" |
| `method.interpretation_questions_path` | `iba/docs/WA-interpretation-questions-v1.4-2026-08-02.md` | same requirement |
| `method.inner_being_narrative_guidance_path` | `iba/docs/WA-inner-being-narrative-guidance-v1-2026-07-28.md` | downstream of verse/passage reading — governs the book-narrative step, out of scope here |
| `method.narrative_hard_constraints_path` | `iba/docs/WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md` | same, downstream |
| `passage.debate_session_chapter_guideline` | `3` | advisory cap on chapters of `report.passage_debate` fill-in per Claude Code session, added after Micah+Hosea exhausted caps in one unbroken 21-chapter session |
| `report.auto_backfill_before_render` | `True` | `report.verse_span_meaning` auto-runs meaning backfill for any unregistered strong in the exact range before writing |
| `report.verse_analysis_output_dir` / `_pattern` | `iba/app/verse-analysis` / `{book}-{range}-verse-span-meaning.md` | base extract location/naming |
| `report.passage_debate_naming_pattern` | `WA-{book}-{range}-debate.md` | |
| `report.whole_book_read_naming_pattern` | `WA-{book}-whole-book-read.md` | |

**No `method.verse_reading_technique_path` setting exists.** `report.verse_span_meaning` — the step that produces the base extract `WA-verse-reading-technique-v2` is meant to operate on — is registered, but nothing reads or requires the technique doc. Both `report.passage_debate` and `report.book_narrative_generate` fail cleanly (`guidance-doc-missing`) if their `method.*` setting points to a missing file — there is no equivalent failure mode for the verse-reading-technique doc, because nothing currently points to it.

**From `BUILD.md` (verse-analysis / passage-debate build history):** *"The debate itself (applying Q1-Q10 to a verse, judging stated-vs-inferred, naming a subject/source/target) is analytical work an AI does against the method docs — no DB query produces it, the same reason `report.verse_span_meaning` only renders lexical data and never interprets it."* — i.e. the base extract step is architecturally scoped to rendering only; any actual *reading* (base-lexical or phenomenon-level) is AI work done against a method doc, not something the pipeline itself performs.

---

## 6. Memory

**`feedback_iba_record_rules_when_set_in_configs`** (memory, 2026-07-22) — "it has been defined, many times over, and is all over the docs and logs. The only problem is you update memory (sometimes) and never follow any of the rules of the app, partly because you do not record the rules when they are set in the configs." Directly the failure this session's Obadiah exercise reproduced.

**`project_movement_operation_definition_written`** (2026-07-26) — the "movement" operational definition (subject/operation/source/target) was signed off by the researcher, written into what is now `WA-passage-read-guidance`. Closes the "movement definition open" item specifically; does not mean the wider rollout is complete.

**`project_iba_output_spiderweb_process_locality_augment`** (2026-07-20) — IBA output is a spiderweb of linked concordances, not one; the real shift is **process** — away from bulk-update (one rule swept over everything) toward **locality** (build deeply for one unit, then back-fill/augment prior work on return). Named as the study's most-repeated failure mode when violated (method rebuilt 4-5×, each sweep discarding prior learning).

**`project_iba_verse_existence_gated_on_term_discovery`** (resolved 2026-07-29) — a verse only exists in `iba.db` if term-discovery onboarding surfaced a study-relevant word there (6.59% of canonical verses missing, concentrated in genealogy/list books, accepted as within tolerance). `governance.verse_gap_by_design` + `report.verse_gap_note`: both `report.verse_span_meaning` and `report.passage_debate` note a detected gap inline and skip to the next verse — applied live in this session's own Obadiah 1:19 record.

**`project_iba_passage_debate_no_separate_ai_chat_needed`** (2026-07-27) — passage-debate work (base extract + debate) is written directly in Claude Code via `report.passage_debate`; read the *current* `method.passage_read_guidance_path`/`method.interpretation_questions_path` docs from config, not memory, before applying them. The old separate Claude.ai upload-chat workflow is retired for this task.

**`project_iba_book_by_book_debate_phase`** — current status: books 1-6 (Daniel, Jonah, Joel, Obadiah, Micah, Hosea) done; pipeline split (2026-08-02) into three PS entry points (Chapter-Generate / WholeBookRead / Book-Narrative) plus the 3-chapters/session guideline, after Micah+Hosea exhausted caps in one session; Amos (book 7) not started.

---

## 7. What this extract does *not* cover

- `WA-inner-being-narrative-guidance` / `WA-inner-being-narrative-hard-constraints` — downstream, govern the book-narrative step, not verse/passage reading.
- The six-type (or seven-type, per this session's earlier correction) beings typology from the 2026-08-02 precursor-reading training session — that's step-2 (candidate/human-being) territory, not verse reading; not pulled in here since it wasn't asked for and pulling it in would be exactly the cross-doc self-synthesis this extraction is meant to avoid.
- Memory files matched by keyword search but confirmed (by checking for `bible_research.db`/`ve_lexical`/`cluster_subgroup`/`finding` references) to belong to the main Bible-study programme, not this app — excluded as out of scope for "this app."
