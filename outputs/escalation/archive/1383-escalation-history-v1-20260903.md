# Escalation deep history

## #1383 — Approve verse-lexical Window 1 enrichment design/propose
type=task source=researcher

**v1** (2026-09-03T03:41:56Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Approve verse-lexical Window 1 enrichment design/propose
> **comment (set this version):** Spawned from #1376 per researcher instruction (2026-09-03, Developer Mode session) -- full objective: enrich verse_lexical to produce the results the prototype checklist demonstrated (Dan 1:8 / Ps 25:2 / Hos 2:4), with additional columns, the configs/controls governing them, an updated glossary, and every process properly registered per IBA app governance -- not a one-off script. Lineage traced live in the DB: #1376 (characteristic model cross-db inventory) -> #1377 (glossary, seeded from #1376) -> #1378 (lexical-to-finding pipeline purpose) -> #1379 (verse-lexical rework: scope reconciliation + prototype checklist, tested on Ps 25:2/Hos 2:4) -> this item. Design+propose document filed, following the plan-design-propose-testplan-buildplan-build cycle: answers open decisions A-G from #1379's scope doc with grounded recommendations (checked live against schema/code, not assumed), proposes schema (4 verse_lexical columns, passage.genre, new verse_lexical_note table), the config registrations that go with it, a found-live H0853 role-classification bug (10,521 affected rows) to root-fix in the same build, glossary terms confirmed missing, a build plan, and a test plan per test-plan-per-module-utility. Nothing built yet -- awaiting this approval. Separately found live: Escalation.ps1's -ShortDescription parameter is declared but never wired into the Raise action's flags -- the python CLI's short_description positional actually receives -Question's text instead (silently) -- worked around here by keeping -Question title-length; flagging for its own fix, not chasing it in this item.
> **context (set this version):** iba/docs/verse-lexical-enrichment-design-propose-v1-20260903.md

**v2** (2026-09-03T04:08:23Z, Claude) state=raised next_action=review assigned_to=Researcher
> **context (set this version):** iba/docs/1383-verse-lexical-enrichment-design-propose-v1-20260903.md
> **tried (set this version):** Filename corrected to carry its own escalation-id prefix (governance rule, researcher instruction 2026-09-03), same pass as fixing the same gap across #1007/#1376/#1377/#1379/#1380's own working files.
