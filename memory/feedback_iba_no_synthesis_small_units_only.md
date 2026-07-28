---
name: feedback_iba_no_synthesis_small_units_only
description: "On IBA planning work, do not synthesize/interpret across documents on your own — assemble mechanically in small dictated units only."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a4164060-09e6-4212-b013-0c4e988a3f29
  modified: 2026-07-21T03:58:47.808Z
---

When working on IBA application planning/design docs (`iba/docs/`), do not independently reconstruct,
interpret, or synthesize a plan from multiple source documents on your own initiative — even when asked
to "prepare a planning document" or "capture the design elements." Work in **small units**, each one
explicitly directed, and check before combining/inventing structure across documents.

**Why:** On 2026-07-20/21 the researcher had, in a separate session/channel, already worked through most
of the open questions in `iba-config-rules-for-process-loop-v1-20260720.md` (D1-D6) — but that
resolution was never written to a file I could find (searched `iba/logs/`, `Workflow/Sessionlogs/`,
grepped the whole `iba/` tree — nothing newer than the source docs existed). Asked to "prepare a
planning document... to capture the design elements," I synthesized a fresh document (
`iba-db-schema-change-plan-v1-20260720.md`) that treated already-resolved questions as still open —
because my only inputs were the stale docs, and I filled gaps with my own reasoning rather than stopping
to ask where the resolution lived. The researcher's verdict: "you cannot recover from the point that you
lost... it seems to unpick your brain, versus doing it myself is a much larger exercise... you steal my
tokens because of all the rework you force me to do." They then began manually reconstructing the plan
themselves (`iba-application-plan-v3-reconstructed.md`) by literally copy-assembling sections from
multiple existing docs, explicitly to avoid my invention.

**How to apply:**
- When asked to consolidate/plan/capture design elements across multiple docs, do NOT default to writing
  a new synthesized document. First check explicitly whether more-recent resolving material exists
  (ask the researcher directly: "did this get resolved elsewhere since these docs were written?") before
  treating open questions in a doc as still open.
- Prefer literal extraction/assembly (copy the researcher's own words from named sections) over
  paraphrase or inferred structure, when the researcher is reconstructing/consolidating documents.
- Work in small, explicitly-scoped units and check in before moving to the next unit — do not chain
  multiple interpretive steps into one big deliverable unprompted, on this workstream specifically.
- This is IBA-workstream-specific guidance (ties to [[project_iba_output_spiderweb_process_locality_augment]]
  and the "learning lost in chat" failure the whole IBA app is designed to prevent — ironic that the
  planning process itself hit the same failure mode this session).
