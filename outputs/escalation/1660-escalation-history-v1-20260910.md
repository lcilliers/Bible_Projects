# Escalation deep history

## #1660 — Lexicon-join meaning data: does it help characteristic work?
type=issue source=researcher

**v1** (2026-09-10T11:15:26Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Lexicon-join meaning data: does it help characteristic work?
> **comment (set this version):** Researcher, live, looking at a query joining strong + vw_strong_gloss + span + verse for G3004G (say/lego): "I am looking at the data, and analysed it with the following script. I am afraid, the parsing process does not make it any easier to digest meaning, it, it fact causes a significant layer of noise. as a method of driving better understanding, it is not really helpful. Feeding the meaning data into the lexicon actually does not help the analysis. that really leaves me with great doubt about how to approach the analysis of the characteristics."

Diagnostic confirmation (run live against iba.db this turn): G3004G has 1,314 span occurrences and 27 vw_strong_gloss rows (1 strong_meaning_parsed, 2 strong_mounce_parsed, 24 strong_lsj_parsed). A naive per-occurrence join (span x vw_strong_gloss) produces 1,314 x 27 = 35,478 rows for one word; 24 of the 27 gloss rows are LSJ classical-citation senses, largely irrelevant to Koine NT usage or even to the one active sense in a given verse.

This is the direct, predictable consequence of vw_strong_gloss's deliberate design (per its own docstring): a raw union of every sense from every table, no stem/voice narrowing, no ambiguity handling, no base-lemma fallback, explicitly "the raw join surface underneath any future resolution layer, not a replacement for one." Joining that 1:1 against span (one row per word occurrence in running text) multiplies every occurrence by every historical sense; that is structural noise, not a bug in the view or the join syntax.

Two related but separable questions for a researcher decision, not something for Claude to resolve unilaterally (design work is never self-correctable):
(1) Is lexicon-level meaning data (LSJ/Mounce/meaning-tree, however joined or parsed) fundamentally the wrong grain of input for characteristic analysis, i.e. should characteristic work rely on contextual/verse-level reading instead, with lexicon lookup only as an occasional targeted reference, not a bulk join?
(2) Or is the real gap a missing per-occurrence sense-resolution layer (something that picks the one active sense for a given span occurrence, e.g. via stem/voice/context narrowing) that would collapse the 27-senses-per-word noise down to something close to 1:1 with span, and if so, is that worth building, given resolve_code() was already ruled invalid and no design for its replacement exists yet?

Claude has not attempted to answer or prejudge this; flagging the researcher's own doubt back as a decision point, per standing instruction that any genuine open item/judgement call in chat gets its own escalation the same turn. Confirmed diagnostically only (span-row-count x vw_strong_gloss-row-count = 35,478 for G3004G, and the LSJ-vs-other-source 24/27 split causing most of the volume) -- no fix attempted.
> **context (set this version):** This is the same underlying question flagged when resolve_code()/lib/lexical.py was ruled invalid ("whatever is in lexical at the moment is no longer valid"): a real per-occurrence sense-resolution layer has never been built. Related: project_base_data_spine_verse_span_strong_parse memory (spine/parse work); escalations for vw_strong_gloss creation and the parse-grain fix (#1655/#1659, 2026-09-10).
