# Manual Test — Brief Meaning Router (100 pairs)

**Purpose:** test the simplified per-verse classifier contract using Claude AI (chat) s.

**Contract:** brief plain-English summary OR set-aside. **No** morphology essay, **no** unresolved pointers, **no** §3 framing — just enough to GROUP verses with similar meaning.

**output:** `wa-abbr-classify-test2-sonnet-4-6-20260504.json`

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
> The point of this pass is to GROUP verses with similar meaning. Brief and consistent matters more than exhaustive. Do NOT analyse morphology, do NOT cite parallels, do NOT speculate. If you can read the verse and see the gist, write it. If not, set aside.
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

The structured per-pair records — 100 (verse, term) pairs the programme has not yet classified. Open `outputs/markdown/manual-test-brief-input-100-20260504.json` and paste its contents (≈120 KB).

```
[paste the full contents of manual-test-brief-input-100-20260504.json here]
```

PowerShell helper to copy the file to the clipboard:

```powershell
Get-Content "outputs\markdown\manual-test-brief-input-100-20260504.json" -Raw | Set-Clipboard
```

---

## What to compare

For each pair, compare:

| Test | Pass condition |
|---|---|
| **Decision agreement** | Did Claude AI and the API agree on summary vs set_aside? |
| **Set-aside reason agreement** | When both set aside, did they pick the same category? |
| **Summary similarity** | When both summarised, do the summaries support the same grouping (semantically equivalent)? |
| **Brevity** | Are summaries ≤25 words and free of theology-essay drift? |
| **Discipline boundaries** | No grouping, no cross-references, no speculation — just the gist. |

Disagreements are the interesting cases — they identify where the contract is ambiguous or where one of the surfaces drifts. List those in a small comparison table at the bottom of `WA-manual-test-brief-100-20260504.md`.
