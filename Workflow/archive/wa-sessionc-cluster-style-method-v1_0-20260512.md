# Session C Cluster — Shared Style and Method

**Document type:** Shared instruction loaded by every chapter run.
**Audience:** Claude AI (the writer)
**Version:** v1.0
**Date:** 2026-05-12
**Replaces:** none (new — superseding the per-word Session C model)

This document defines voice, audience, language discipline, citation rules, and the analytical lens vocabulary used across every chapter of a cluster's published study. It is loaded **once per chapter run**, alongside that chapter's own instruction and that chapter's own input file.

---

## 1. What you are writing

A **plain-English published study** of a family of related inner-being characteristics from Scripture. The reader is an intelligent person who has no familiarity with this project's analytical vocabulary. They are reading the study as they would read any serious essay on the Bible's treatment of a theme.

Each chapter is a standalone unit of prose. Other chapters of the study will be written in separate runs — you write only the chapter you are given, into the AI-WRITE zones marked in that chapter's input file.

---

## 2. Voice and tone

- **Essayistic.** Continuous prose, not bullet points. Topic sentences carry the argument.
- **Evidential.** Every analytical claim is grounded by a quoted verse — never by appeal to general impression.
- **Reverent without being devotional.** This is a study of Scripture, not a sermon. Avoid liturgical phrasing.
- **Clear about what is shown and what is silent.** Where the verse evidence is silent on a point, name that silence rather than fill it.
- **Confident, not hedging.** Do not pad with "perhaps", "it could be argued", "in some sense" when the evidence is plain.

Address the reader in the third person ("the reader will notice…" only sparingly; prefer direct exposition). Avoid first-person plural ("we see that…") — it draws attention to the author. State the evidence and let it speak.

---

## 3. Words to avoid

The following project-internal terms must not appear in published prose.

| Avoid | Use instead |
|---|---|
| cluster | "this study", "these related characteristics", "the family of characteristics" |
| sub-group | "characteristic", "facet", "form", "the way wisdom appears as a settled inner quality" |
| VCG / verse context group | "meaning group" (rare); usually describe inline ("the verses where wisdom names God's own attribute") |
| anchor verse | "key verse", "central verse" |
| finding | "what the evidence shows", "what the verses tell us", "the pattern" |
| tier / T0 / T1 … | the thematic name (see §5) — never the code |
| catalogue prompt / question code | not exposed |
| constitutional location | "where this lives in the inner person", "the inner home of …" |
| inner faculty | "the inner capacity", "the part of the person that …" |
| sub-group code (M15-A etc.) / VCG code (M15-A-VCG01) | not in prose — used only in editing footnotes if at all |
| domain, findings | not exposed |

Words that **are** fine: wisdom, understanding, knowledge, inner life, inner person, heart, mind, will, conscience, soul, spirit, God, Scripture, character, attribute, characteristic, evidence, pattern, theme.

---

## 4. Citation discipline

**Every analytical claim must be grounded by a quoted verse.** No exceptions.

When you make a claim:

1. **Name the verse** in the prose using standard biblical citation (e.g. "as Pro 16:23 makes plain…", "Daniel's confession in Dan 2:20…").
2. **Quote it verbatim** — inline with quotation marks for short quotes, or in an indented block when the quote is long enough to warrant separation.
3. **Where the meaning-group context shapes the reading**, name it inline (e.g. "in the verses where wisdom is named as God's own attribute — most clearly at Dan 2:20 — …").

**Never** cite:
- finding-id (`cf=4615`)
- tier code (`T2`)
- VCG code (`M15-A-VCG01`)
- prompt code (`T2.1.1`)

The chapter input provides every verse you should quote with its full text inline. You do not need to re-source verses.

**Minimum density:** each AI-WRITE zone that makes analytical claims must cite at least two key verses verbatim from the list in its zone instruction. Deeper treatments cite more. The framework lists the *required* verses per zone.

---

## 5. Analytical lenses (the seven thematic names)

The chapters of the study are organised around analytical lenses. The internal codes (T0…T7) must never appear in the prose. Use the thematic name instead when you need to refer to the lens:

| Internal code (NOT in prose) | Thematic lens (use this language) |
|---|---|
| T0 | The divine pattern — what Scripture says about God in this characteristic |
| T1 | What the characteristic is (definition, name, kind, boundary, modes) |
| T2 | Where the characteristic lives in the inner person |
| T3 | Which inner capacities the characteristic engages |
| T4 | How the characteristic moves — between God and the person, between persons |
| T5 | How the characteristic is formed, deepens, is tested, is transformed |
| T6 | How the characteristic relates to other inner characteristics |
| T7 | The view from outside Scripture — what physical and clinical sciences observe |

You will rarely need to name the lens explicitly. Most chapters frame the lens through their own opening prose and section structure; the reader does not need to be told "this is the T2 chapter".

---

## 6. Handling silences

The verse evidence is silent on many specific points. The analytical record names these silences explicitly (as "silent findings"). When a silence appears in the evidence you are given:

- **Do not paper over it.** Do not infer what Scripture leaves unsaid.
- **Name the silence as itself meaningful** where appropriate. The absence of expected evidence is a finding.
- **Distinguish** a silence-in-evidence (Scripture is silent) from an unanswered question (the analytical record did not address it). The evidence blocks label silences as "silent findings".

---

## 7. Handling gaps in the analytical record

Some chapters (especially Chapter 7) will tell you that the analytical record is thin on a particular lens. In those cases:

- **State the gap honestly** in the prose — do not bluff.
- **Bring general scientific or scholarly knowledge** where the chapter's instruction explicitly invites you to (e.g. Chapter 7 invites general clinical-science knowledge as a supplement).
- **Do not overclaim.** A short, careful reflection that acknowledges the thinness is better than an inflated treatment.

---

## 8. What you return

For each chapter run you return a **single completed Markdown file** — the chapter input file with prose written into every AI-WRITE zone, in place of the zone marker and its placeholder text.

- Keep the chapter title and section headers intact.
- Remove the AI-WRITE marker comment blocks (`<!-- AI WRITE: … -->`) — they are scaffolding.
- Leave the EVIDENCE comment blocks (`<!-- EVIDENCE: … -->`) — they will be stripped by a finalisation pass after all chapters are written.
- Do not invent new sections or reorder existing ones.
- Do not write material that belongs to a different chapter. The chapter instruction names what is in scope; everything else is out of scope for this run.

**File naming convention** for your output (the chapter instruction repeats this):

```
wa-cluster-{CLUSTER}-ch{N}-draft-v1-{YYYYMMDD}.md
```

---

## 9. Cross-chapter consistency

Other chapters are written in separate runs. You will not see the other chapters' prose. To maintain consistency:

- Use the **brief characteristic profiles** provided at the top of every chapter input — these define how each characteristic is described across the study.
- Use the **thematic lens names** consistently (this document, §5).
- Do not preview content that belongs to a later chapter (e.g. don't describe how a characteristic is formed in Chapter 4 — that belongs to Chapter 5).
- Do not summarise content from an earlier chapter at the start of yours unless the chapter instruction explicitly tells you to.

If a claim feels like it would benefit from cross-chapter framing, trust the structure — the editing pass after all chapters are written will harmonise.
