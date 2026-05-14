# Session C Cluster — Shared Style and Method

**Document type:** Shared instruction loaded by every chapter run.
**Audience:** Claude AI (the writer)
**Version:** v1.1
**Date:** 2026-05-12
**Supersedes:** v1.0 (Chapter 4 test outcome: added on-completion reverse audit, on-completion self-review, sharpened silence principle)

This document defines voice, audience, language discipline, citation rules, the analytical lens vocabulary, and the on-completion checks used across every chapter of a cluster's published study. It is loaded **once per chapter run**, alongside that chapter's own instruction and that chapter's own input file.

---

## 1. What you are writing

A **plain-English published study** of a family of related inner-being characteristics from Scripture. The reader is an intelligent person who has no familiarity with this project's analytical vocabulary. They are reading the study as they would read any serious essay on the Bible's treatment of a theme.

Each chapter is a standalone unit of prose. Other chapters of the study will be written in separate runs — you write only the chapter you are given, into the AI-WRITE zones marked in that chapter's input file.

---

## 2. Voice and tone

- **Essayistic.** Continuous prose, not bullet points. Topic sentences carry the argument.
- **Evidential.** Every analytical claim is grounded by a quoted verse — never by appeal to general impression.
- **Reverent without being devotional.** This is a study of Scripture, not a sermon. Avoid liturgical phrasing.
- **Clear about what is shown and what is silent.** Where the verse evidence is silent on something meaningful, name it; where the silence is routine, do not.
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

## 6. The silence principle (sharpened in v1.1)

**Name a silence only when its absence is meaningful.** A silence is meaningful when one of two conditions holds:

1. **Expectation-then-absence.** Something in the evidence creates an expectation that is then not met — for example, the divine-image pattern holds across seven characteristics, and then one characteristic has no divine version. The contrast itself is a finding.
2. **Silence shapes the characteristic.** The absence is what gives the characteristic its shape — for example, meditative inner activity is largely silent on God's own meditation, which marks meditation as the characteristically creaturely mode.

**Routine absence needs no comment.** If a particular inner location (say, the kidneys) is not named in the evidence for a particular characteristic, that is the default rather than a finding. Do not list silences as inventory; surface only the silences that carry weight.

The analytical record's "silent" findings are the candidate pool — but not every silent finding deserves prose treatment. Use judgement: ask "does naming this silence add to the reader's understanding of the characteristic, or is it filler?" When in doubt, leave it out.

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

```text
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

---

## 10. On completion — reverse audit (NEW in v1.1)

Before you return the chapter, perform an explicit reverse audit. The audit confirms that the chapter has used the evidence it was given.

For each per-characteristic section (or for the chapter as a whole where there are no per-characteristic sections):

**A. Findings coverage.** Walk through every finding in every EVIDENCE block inside that section's scope. For each finding, confirm one of:

1. The finding's claim is present in the prose (it does not need to be paraphrased verbatim — the claim must be reflected).
2. The finding is a **routine silent** finding whose omission is justified under §6 (the silence principle).
3. The finding was redundant with a finding already covered.

If a finding falls outside (1)–(3), you missed it. Add prose that incorporates it.

**B. Anchor verse coverage.** Walk through every key verse listed for that section. Confirm each key verse is quoted verbatim at least once in the prose. If any is uncovered, add a sentence that uses it.

**C. Lens coverage.** For each tier in the section's scope (e.g. Ch 4 = T2 + T3; Ch 5 = T4 + T5 + T1), confirm the chapter actually engages with that lens. If a lens is wholly absent, ask whether the prose is too narrow.

The reverse audit happens **before** the self-review (§11). Audit first, then read.

---

## 11. On completion — self-review pass (NEW in v1.1)

After the reverse audit, read through the entire chapter from start to finish as a reader would. Look for and correct:

- **Repetition.** The same point made in two places. Pick the better location and remove the duplicate.
- **Overreach.** A claim that goes beyond what the cited verse(s) actually carry. Soften or remove; do not add an extra verse to prop it up unless the evidence is genuinely there.
- **Padding.** Sentences that add words but no content — throat-clearing, restating the section heading, signposting that the reader does not need.
- **Tonal drift.** Devotional phrasing creeping in; first-person plural; hedging language; jargon from §3 that slipped through.
- **Structural drift.** Section reading as a list of findings rather than essayistic prose; missing topic sentences; sentences that depend on a finding code the reader cannot see.

Edit in place. The output you return is the post-self-review version.

---

## 12. Order of operations on completion

1. Write the chapter.
2. Reverse audit (§10): findings coverage → anchor verse coverage → lens coverage.
3. Self-review pass (§11): repetition → overreach → padding → tonal drift → structural drift.
4. Return.
