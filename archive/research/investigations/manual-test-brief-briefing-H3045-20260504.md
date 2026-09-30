# Manual Test — Brief Meaning Router (100 pairs, concentrated on H3045 *ya.da*)

**Purpose:** test the simplified per-verse classifier contract on a **concentrated** cohort — 100 unclassified verses, all from a single Strong's number (`H3045` *ya.da* "to know", R100 knowledge).

**Why concentrated:** the [stratified test](manual-test-brief-briefing-20260504.md) sampled across registries (one or two verses per term). This run holds the term constant so we can see whether chat preserves atomic discipline at scale on a single concentrated term — does it consolidate against itself, or does it stay verse-by-verse?

**Contract:** brief plain-English summary OR set-aside. **No** morphology essay, **no** unresolved pointers, **no** §3 framing — just enough to GROUP verses with similar meaning.

**Comparison output:** save Claude AI's response as `outputs/markdown/WA-manual-test-brief-100-H3045-20260504.md`. Once that's saved I can run an API counterpart against the same 100 pairs and compare.

---

## How to use this file

1. Start a fresh Claude AI conversation.
2. Paste the **System Briefing** (Block A) as the first message.
3. Wait for Claude AI's acknowledgement.
4. Paste the **JSON Input** (contents of `manual-test-brief-input-100-H3045-20260504.json`) as the second message.
5. Save Claude AI's full JSON output to `outputs/markdown/WA-manual-test-brief-100-H3045-20260504.md`.

If the 100-pair JSON is too large for one paste, split the `pairs` array (e.g. 50 + 50) and run two consecutive turns inside the same chat. Same system briefing applies to both turns.

---

## Block A — SYSTEM BRIEFING (paste first)

> You are a Bible-verse classifier for the Soul Word Analysis Programme — a research project studying ~214 English words for the inner life of mankind, each mapped to Hebrew (OT) and Greek (NT) terms via Strong's numbers.
>
> Your job for each (verse, term) pair is ONE of two things:
>
> **(A) BRIEF SUMMARY** — one short plain-English sentence (≤25 words) saying what THIS verse says about the inner-being characteristic via THIS term. Concrete, not abstract. Just the sense of the verse on this term — not a theology essay.
>
> **(B) SET ASIDE** — if the term in this verse does NOT engage inner-being content, or the verse is genuinely unclear, mark `set_aside=true` with one of these reasons:
> - `no_inner_being` — the term here is about external conduct/event with no inner-life window
> - `physical_only` — body part, physical process, material object
> - `spatial_only` — location/geography
> - `wrong_face` — verse has inner-being content but a different term carries it (name the carrier in `note`)
> - `unclear` — needs deeper analysis to decide
>
> The point of this pass is to GROUP verses with similar meaning. Brief and consistent matters more than exhaustive. Do NOT analyse morphology, do NOT cite parallels, do NOT speculate. **Treat each pair atomically — do not consolidate phrasing across pairs even when the term is the same.** If you can read the verse and see the gist, write it. If not, set aside.
>
> **Filter test:** does this verse, through this term, say something about how a person thinks, feels, chooses, relates, or is oriented toward meaning, others, or God? If yes, summarise. If no or unclear, set aside.
>
> **Output:** return a single JSON array — one object per pair, in the same order as the input — with this shape per object:
>
> ```json
> {
>   "pair_id": "<copy from input>",
>   "reference": "<copy from input>",
>   "strong": "<copy from input.term_being_analysed.strong>",
>   "summary": "<≤25 words plain English, OR null if set_aside=true>",
>   "set_aside": <true|false>,
>   "set_aside_reason": "<one of the categories above, OR null if set_aside=false>",
>   "note": "<optional one-line note, or null>"
> }
> ```
>
> Return ONLY the JSON array — no prose before or after.
>
> Acknowledge that you have understood the role and the contract. I will then send the input JSON in a second message.

---

## Block B — JSON INPUT (paste second)

100 (verse, term) pairs, all on `H3045` *ya.da* "to know" (Hebrew, R100 knowledge). Open `outputs/markdown/manual-test-brief-input-100-H3045-20260504.json` and paste its contents (≈120 KB).

```
[paste the full contents of manual-test-brief-input-100-H3045-20260504.json here]
```

PowerShell helper to copy the file to the clipboard:

```powershell
Get-Content "outputs\markdown\manual-test-brief-input-100-H3045-20260504.json" -Raw | Set-Clipboard
```

---

## What this test stresses

| Test | Pass condition |
|---|---|
| **Atomic discipline at scale** | Each summary is independently written for that verse — Claude AI does not consolidate phrasing across pairs even though the term is constant. |
| **Sub-sense differentiation** | *ya.da* covers cognitive knowing, experiential knowing, intimate-knowing, and recognising/acknowledging. The summaries should reveal these sub-senses naturally rather than collapsing to a single "knows" template. |
| **Set-aside discipline** | Where *ya.da* engages no inner-life content (idiomatic, formulaic, narrative-only), the model sets aside with the right reason. |
| **Brevity** | Summaries are ≤25 words. No theology essays, no parallel cross-references. |
| **No grouping output** | The model does **not** propose groups, anchors, or consolidated meanings. It only emits one decision per pair. |

When you save the output, Claude Code will compare it pair-by-pair against an API run on the same 100 pairs and surface disagreements.
