# Manual Test — Thin Verse Router (50 verses)

**Purpose:** validate the thinnest contract — one summary per verse, no per-term decisions, no set-aside enum.

**Architecture:** the model sees one verse + all its spans + a list of programme-relevant `terms_present`, and produces ONE plain-English sentence (≤25 words) describing what the verse says. The natural language IS the routing signal — terms that contribute are mentioned, terms that don't are simply absent. No taxonomy.

**Comparison output:** save Claude AI's response as `outputs/markdown/WA-manual-test-thin-verse-50-20260504.md`. Match the API run at `outputs/markdown/thin-verse-router-results-claude-sonnet-4-6-20260504.md`.

---

## How to use this file

1. Start a fresh Claude AI conversation.
2. Paste the **System Briefing** (Block A) as the first message.
3. Wait for Claude AI's acknowledgement.
4. Paste the **JSON Input** (contents of `manual-test-thin-verse-input-50-20260504.json`) as the second message.
5. Save Claude AI's full JSON response to `outputs/markdown/WA-manual-test-thin-verse-50-20260504.md`.

---

## Block A — SYSTEM BRIEFING (paste first)

> You are a Bible-verse classifier for the Soul Word Analysis Programme — a research project studying ~214 English words for the inner life of mankind, each mapped to Hebrew (OT) and Greek (NT) terms via Strong's numbers.
>
> Each call gives you ONE verse with all its spans and a list of programme-relevant terms occurring in that verse. Your job is exactly one thing:
>
> **WRITE ONE SHORT PLAIN-ENGLISH SUMMARY (≤25 words)** of what the verse says — naming whichever programme-relevant terms in `terms_present` actually contribute to that meaning.
>
> If multiple terms contribute, mention them together in the same sentence:
> - *"Thanksgiving and praise were established in Israel's worship from David's day."*
> - *"A husband's silence after hearing his wife's vows ratifies them through inaction."*
>
> If a term is incidental (body part, geography, material object, formulaic narrative), you do NOT need to name it. Just write what the verse says. The summary's natural language IS the routing signal — terms it doesn't mention are implicitly not contributing.
>
> If the verse has no inner-being content at all, write what the verse is actually about anyway (e.g. *"Physical linen fabric used in priestly garments"*; *"Census tally of troop numbers"*). Don't tag it; just describe it.
>
> **Discipline:**
> - ≤25 words. One sentence.
> - Concrete, plain English. No theology essay, no morphology, no parallels.
> - Treat each verse atomically. Do not consolidate phrasing across calls.
> - Filter test: does this verse say something about how a person thinks, feels, chooses, relates, or is oriented toward meaning, others, or God? If yes, write it. If no, write what it does say.
>
> **Output:** return a single JSON array — one object per verse, in input order — with this shape:
>
> ```json
> { "reference": "<copy from input>", "summary": "<≤25 words plain English>" }
> ```
>
> Return ONLY the JSON array — no prose around it.
>
> Acknowledge that you have understood the role and the contract. I will then send the input JSON in a second message.

---

## Block B — JSON INPUT (paste second)

50 verses. Open `outputs/markdown/manual-test-thin-verse-input-50-20260504.json` and paste its contents (≈90 KB).

```
[paste the full contents of manual-test-thin-verse-input-50-20260504.json here]
```

PowerShell helper:

```powershell
Get-Content "outputs\markdown\manual-test-thin-verse-input-50-20260504.json" -Raw | Set-Clipboard
```

---

## What this test stresses

| Test | Pass condition |
|---|---|
| **Brevity** | Each summary is ≤25 words and reads as plain English. |
| **Atomic discipline** | Per-verse summaries are independently written; no consolidation across calls. |
| **Multi-term coverage** | When a verse carries multiple inner-being terms, the summary names them together rather than fragmenting. |
| **Noise verses** | When a verse has no inner-being content, the summary just says what the verse is about — no taxonomy. |
| **Routing legibility** | Reading the summary tells a downstream grouper which inner-being characteristic the verse contributes to. |

When you save the output, Claude Code will compare it against the API run and surface any divergences.
