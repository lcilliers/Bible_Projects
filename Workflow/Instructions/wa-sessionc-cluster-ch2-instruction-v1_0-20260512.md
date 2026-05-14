# Session C Cluster — Chapter 2 Instruction

**Chapter:** 2 — The characteristics in this study
**Document type:** Chapter-specific writing instruction
**Audience:** Claude AI (the writer)
**Version:** v1.0
**Date:** 2026-05-12
**Loads alongside:** `wa-sessionc-cluster-style-method-v1_1-20260512.md` (shared)
**Reads:** the per-chapter input file (`wa-cluster-{CLUSTER}-ch2-input-v1-{YYYYMMDD}.md`)
**Writes:** the per-chapter draft file (`wa-cluster-{CLUSTER}-ch2-draft-v1-{YYYYMMDD}.md`)

---

## 1. What this chapter does

Chapter 2 **introduces each characteristic in the study** in turn — short, focused sections that give the reader a working sense of every characteristic before the deep dives begin. For every non-BOUNDARY characteristic, you write a single ~200–300 word section that answers:

- **What this characteristic is** — its name (in plain English, not by code), the central inner-life phenomenon it names.
- **What it looks like in Scripture** — anchored by one or two key verses that capture the characteristic most clearly.
- **How it differs from the others in this study** — what distinguishes this characteristic from its closest neighbours in the family.

There is also a final, shorter section acknowledging the **supporting characteristics** (BOUNDARY) — terms that appear in the verse evidence supporting the study but are not themselves inner-being characteristics.

The chapter is the reader's **map** for what follows. After Chapter 2, the reader should know which characteristics will be treated, in what order, and roughly what each one is.

---

## 2. Structure of the chapter

The chapter input file lays out the structure. You fill the AI-WRITE zones, in order:

1. **Chapter 2 opening (~50–80 words).** A brief framing sentence or two saying that the Bible's vocabulary for this inner-life domain organises into N characteristics, each a distinct way the inner person manifests this aspect of inner life.
2. **Per-characteristic sections, in order.** One per non-BOUNDARY characteristic. Each section header is provided; you write only the body prose.
3. **Supporting characteristics section (final).** A short acknowledgement of the BOUNDARY terms.

---

## 3. Per-characteristic section — what to write

For each characteristic's section (~200–300 words):

**Open** with the characteristic in plain English — name it the way a non-specialist would understand it, not the way the analytical record names it. (e.g. for M15-A: "Wisdom — the settled inner character that orients the whole person.")

**Develop** the characteristic in 2–3 sentences. Draw on the sub-group description provided in the evidence below — the description is your *source*, not your *output*. Rewrite into plain English; do not paste the description verbatim. Anchor with one key verse quoted briefly inline.

**Distinguish** the characteristic from its closest neighbours in the family in 1–2 sentences. (e.g. for M15-A: "Wisdom in this sense is wider than understanding — wisdom is the constituted character of the whole person, while understanding is the receptive faculty by which that character grasps what is offered.") This is the *positioning* sentence — what makes this characteristic this characteristic and not another.

**Close** with a key verse that captures the characteristic most clearly — quoted verbatim, briefly framed.

The 200–300 word target is a guide, not a cap. Some characteristics need more (Logos / the Word in M15 will probably need 300+ to establish its breadth). Some characteristics with sparse evidence may close at 200.

---

## 4. The supporting characteristics section

The final section (~150 words) acknowledges the BOUNDARY characteristics — supporting terms that appear in the verse evidence but are not themselves inner-being characteristics. Briefly:

- Name what they are at the family level (e.g. "translation, training, the office of teaching, the act of insisting").
- Say what role they play in the inner-life domain (they support the inner-life characteristics without being inner-life characteristics themselves).
- Note that they are **not treated at full depth** in the chapters that follow (chapters 4–7).

Draw on the BOUNDARY description in the evidence below. No verse citation is required for this section.

---

## 5. Length

**~200–300 words per characteristic section** (with the flex described above). **~150 words for the supporting characteristics section.** **~50–80 words for the chapter opening.**

For M15 (9 characteristics including supporting), the chapter lands around 2,000–2,700 words total.

Length never constrains comprehensiveness. The characteristic must be establishable from this section alone — a reader who reads only Chapter 2 should come away with a working sense of each characteristic, not a placeholder.

---

## 6. Citation rules for this chapter

- **Each per-characteristic section quotes at least one key verse verbatim** (the required minimum is listed inside the AI-WRITE zone in the input file). Two is better where they help establish the characteristic.
- The first verse you quote should be the one that most clearly establishes the characteristic.
- No quotation is required for the chapter opening or the supporting characteristics section.

Never use VCG codes, tier codes, or finding-ids in the prose.

---

## 7. How to read the evidence in the input

For each characteristic, the chapter input gives you:

- **The sub-group description from the analytical record** (one paragraph). Your *source* for what the characteristic is.
- **All key verses for the characteristic**, quoted verbatim with their meaning-group context description.

For the BOUNDARY (supporting characteristics) section, you get the BOUNDARY description.

You do not receive T1–T7 findings in the Chapter 2 input — those belong to the deep-dive chapters. Chapter 2's job is the **introduction**, not the analysis. If you find yourself wanting more material, you are drifting into Chapter 4–7 territory.

---

## 8. Avoiding overlap with later chapters

- **Where the characteristic lives in the person** is the subject of Chapter 4. You may name the inner location briefly when establishing the characteristic ("wisdom seated in the heart…"), but do not unfold the topography here.
- **How the characteristic works** (movement, formation) is the subject of Chapter 5. You may hint at how the characteristic operates ("given by God, expressed through speech"), but do not develop the dynamics.
- **How it relates to other characteristics** is the subject of Chapter 6. Use the "distinguish from neighbours" sentence to *position* the characteristic against the family; do not catalogue the relationships.
- **The view from outside Scripture** is the subject of Chapter 7. No clinical-science framing here.

The general principle: Chapter 2 is the **introduction**. Every claim should serve the reader's working sense of the characteristic, not the depth of analysis that will come later.

---

## 9. Output

Return the chapter input file with prose written into every AI-WRITE zone:

- Replace each `<!-- AI WRITE: … -->` marker block AND the placeholder underneath it with the finished prose. Remove the marker block entirely.
- Leave each `<!-- EVIDENCE: … -->` block exactly as it is.
- Keep the chapter title and all section headers intact.
- Save your output as: `wa-cluster-{CLUSTER}-ch2-draft-v1-{YYYYMMDD}.md`

---

## 10. Quality bar

Chapter 2 passes the quality bar when:

1. The chapter opening names the inner-life domain and the number of characteristics in plain English.
2. Each per-characteristic section opens with the characteristic in plain English (not analytical-record phrasing).
3. Each per-characteristic section quotes at least one key verse verbatim.
4. Each per-characteristic section includes a distinguishing sentence that positions the characteristic against its neighbours.
5. The supporting characteristics section acknowledges the BOUNDARY terms briefly and notes they are not treated at full depth in chapters 4–7.
6. The sub-group description from the analytical record is used as a *source*, never pasted verbatim — the prose is your synthesis.
7. No content has crossed into chapters 4–7 territory.
8. No jargon from the shared instruction's avoid-list appears in the prose.

---

## 11. Completion procedure

Per shared style §12, on completion you:

1. **Write** the chapter.
2. **Reverse audit** (shared §10): walk every per-characteristic section; confirm each characteristic is named, distinguished, and verse-anchored. Walk every required-cite verse in each section's instruction; confirm each is quoted verbatim at least once. Confirm the supporting characteristics section is present.
3. **Self-review pass** (shared §11): repetition → overreach → padding → tonal drift → structural drift. Chapter 2 is particularly prone to **distinguishing-sentence repetition** (the same neighbour distinction made in two sections from opposite sides) — read for it.
4. **Return** the finished chapter file.
