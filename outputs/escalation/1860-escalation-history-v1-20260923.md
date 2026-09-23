# Escalation deep history

## #1860 — Split word-level and relational into separate Stage 1 steps
type=issue source=researcher

**v1** (2026-09-23T09:31:12Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Split word-level and relational into separate Stage 1 steps
> **comment (set this version):** Researcher, verbatim, this chat: 'we must split the word questions and answers and the relational answers into separate processes. the relational process depends on the word work, and doing it in the same session can only result in errors.' Grounded in today's own evidence: the current single lexical.meaning call asks for fresh word-level answers and relational reasoning about those same words in the same pass, sometimes for the same verse -- relational judgments are being derived from word-level facts not yet established/confirmed, in the same breath they're being generated.
> **context (set this version):** Concrete plan, checked against live cfg_step (lexical.meaning: scope=cluster, one registered step covering both families today): (1) keep lexical.meaning as the word-level step only (M0.1/M0.5, M0.5.11); (2) new step lexical.relational for M0.6.5/M0.6.6/D7.7.1/M0.7/M0.8.1; (3) a real readiness gate -- lexical.relational refuses to run for a verse until every M-code word in it has a committed word-level observation, same shape as the existing lexical.readiness/spine-check hard-stops; (4) relational prompt reads COMMITTED word-level ib_observation rows as grounding, not raw meaning_sources_by_strong lexicon text directly; (5) versereadinggenerate.py's single assemble_batch_package splits into two; stage1coverage.py's coverage tracking splits or is parameterized by family. Not yet built -- larger than anything else this session except the span-grounding rework itself, wanted explicit confirmation before starting given how much has already changed in this same code today.

**v2** (2026-09-23T09:36:54Z, Claude) state=re-assigned next_action=ready_for_approval assigned_to=Researcher
> **comment (set this version):** Researcher, verbatim: 'the split is inevitable.' Decision made -- not building it this session (session ending here per researcher instruction, fresh start next session). Carried forward as the top open item.
> **resolution (set this version):** Decided, not built. Concrete plan already on record (this escalation's own context). Next session's starting point.

**v3** (2026-09-23T10:04:41Z, Researcher) state=completed next_action=approved assigned_to=Claude
> **comment (set this version):**  proceed with split. Ensure that you comply with every aspect of governance, and properly validate that steps taken is complete and achieve the objective.  The object is that the word observations is run corpus wide for all verses, and that the observations quality is correct for the relational phase. worse result would be that relational quality is compromised and the base data must in any case be included for relational phase to be successful. 
