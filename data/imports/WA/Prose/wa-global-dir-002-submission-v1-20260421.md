# Directive Submission to Claude Code

> Per wa-directive-instruction-v1_2-20260421 §5.5
> Session reference: prose
> Session date: 2026-04-21
> Researcher approval: PENDING (this submission statement is produced in anticipation of approval; CC acts only after the researcher has approved)

---

## DIRECTIVE SUBMISSION TO CLAUDE CODE

**Directive file:** `wa-global-dir-002-prose-reg-nullable-v1-20260421.md`

**Directive ID:** `DIR-20260421-002`

**Action required:** Execute per directive. Return completion confirmation per §5 (Completion confirmation) of the directive.

---

## Sequencing note — directive precedes patches

This directive is a **schema enablement directive** per wa-directive-instruction-v1_2 §10. It must be executed and confirmed before either of the two patches produced in the same session can apply. The full execution sequence for session `prose` is:

1. **Directive** `DIR-20260421-002` — this submission. CC executes; returns completion confirmation; researcher and Claude AI confirm outcome matches.
2. **CATALOGUE_POPULATION patch** `PATCH-20260421-CATALOGUE-PROSE-TYPES-V1` (file: `wa-prose-catalogue-chapter0-1-v1-20260421.json`). Applied via standard patch applicator. Separately approved by researcher before apply.
3. **PROSE patch** `PATCH-20260421-PROSE-PROGRAMME-CH01-V1` (file: `wa-prose-programme-chapter0-1-v1-20260421.json`). Applied via standard patch applicator. Separately approved by researcher before apply. Depends on steps 1 and 2.

Each step gates the next. If step 1 fails or is not confirmed, steps 2 and 3 do not proceed.

The two patches are submitted via the standard patch-application route (wa-patch-instruction-v2_3 §6) and do not require a §5.5-equivalent submission statement. Only the directive carries this submission statement.

---

*wa-global-dir-002-submission-v1-20260421 | Submission wrapper for DIR-20260421-002 per wa-directive-instruction-v1_2 §5.5*
