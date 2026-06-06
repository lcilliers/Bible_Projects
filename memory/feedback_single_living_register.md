---
name: feedback_single_living_register
description: Update one living register in place and close items to completion; do not spawn parallel docs that restate the situation
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eae3184c-630b-48c2-9ac1-b0b494ccf689
---

Do not create a new document every time the situation changes or the researcher gives feedback. Update the **one** living register in place, and actually **close items to completion** before moving on.

**Why:** On 2026-05-31, when the researcher answered the §A policy questions that lived *inside* the open-items register, CC created a *separate* policy_decisions doc that re-stated the whole situation with the answers folded in — the third overlapping artefact in one session (register → cleanup summary → policy doc), none closed. Result: "a large range of half truths and half completed stuff all over the place." When focus lands on one point, everything else drifts because the content is scattered across parallel half-finished files.

**How to apply:**
- One canonical living register is the single source of truth. Answer questions, record decisions, and mark items done **in that file**, not in a new one.
- When the researcher answers a question that lives in a document, edit *that document* in place: record the ruling next to the question and mark it resolved with date.
- Closing an item means: do it, mark it complete (date + note), and remove/strike it from "open" — not leave it implied as done elsewhere.
- A new file is justified only for a genuinely new deliverable, not for re-stating an existing list with edits. If tempted to create a differently-*named* doc (e.g. `policy_decisions_...`), first ask whether the content belongs back in the existing register.
- **Versioning is in metadata, not the filename (2026-05-31 policy).** Per [[feedback_version_discipline]] rule 7 + file-org §2.3a, a living register keeps a **single stable filename**; its version lives in the metadata header (`Doc version:` + `Last updated:`) and git holds the history. Do NOT make `-vN` filename copies or archive copies for living docs — that churns files and breaks cross-references. (Earlier this session I wrongly used `-vN` copies; corrected to the metadata+git approach.)
- Finish the point in front of you before opening a new direction. Relates to [[feedback_review_via_files_not_chat]] and [[feedback_obslog_discipline_for_cc]].
