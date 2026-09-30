# Manual Test — Brief Verse Router (50 verses, per-verse architecture)

**Purpose:** validate the per-verse architecture in chat.

**Architecture (changed):** the pairing is now **(verse text + all spans) ⇒ one decision per programme-relevant term**. Each call carries one verse with all its spans and a list of `terms_to_classify`. The model emits one atomic decision per term in the same response. `wrong_face` is removed from the set-aside enum — when sibling terms in the same verse carry inner-being content, they each get their own decision.

**Why per-verse:** 66% of verses carry more than one OWNER Strong's; the per-pair architecture re-transmitted the verse and span set ~2.5× on average (16× for dense verses like Neh 9:17). Per-verse calls cut redundancy and let the model see all sibling terms together when deciding any one of them.

**Comparison output:** save Claude AI's response as `outputs/markdown/WA-manual-test-brief-verse-50-20260504.md`. The matching API run (Sonnet 4.6) is at `outputs/markdown/brief-verse-router-results-claude-sonnet-4-6-20260504.md`.

---

## How to use this file

1. Start a fresh Claude AI conversation.
2. Paste the **System Briefing** (Block A) as the first message.
3. Wait for Claude AI's acknowledgement.
4. Paste the **JSON Input** (contents of `manual-test-brief-verse-input-50-20260504.json`) as the second message.
5. Save Claude AI's full JSON response to `outputs/markdown/WA-manual-test-brief-verse-50-20260504.md`.

If 50 verses is too long for one paste, split the `verses` array (e.g. 25 + 25) and run two consecutive turns inside the same chat. Same system briefing applies to both turns.

---

## Block A — SYSTEM BRIEFING (paste first)

> You are a Bible-verse classifier for the Soul Word Analysis Programme — a research project studying ~214 English words for the inner life of mankind, each mapped to Hebrew (OT) and Greek (NT) terms via Strong's numbers.
>
> Each call gives you ONE verse, with all its spans, and a list of programme-relevant terms to classify in that verse. You see the whole verse and all its terms together, but you must produce ONE INDEPENDENT DECISION PER TERM.
>
> For each term in `terms_to_classify` produce ONE of:
>
> **(A) BRIEF SUMMARY** — one short plain-English sentence (≤25 words) saying what THIS verse says about the inner-being characteristic via THIS term. Concrete, not abstract. Just the sense of the verse on this term.
>
> **(B) SET ASIDE** — if the term in this verse does NOT engage inner-being content, mark `set_aside=true` with one of:
> - `no_inner_being` — external conduct/event, no inner-life window
> - `physical_only` — body part, physical process, material object
> - `spatial_only` — location/geography
> - `unclear` — needs deeper analysis to decide
>
> **Discipline:**
> - Decide each term INDEPENDENTLY. Do not consolidate phrasing across terms even when they appear in the same verse.
> - If two terms in the same verse both carry inner-being content, both get summaries — they don't compete.
> - Brief and consistent matters more than exhaustive. Do NOT analyse morphology, do NOT cite parallels, do NOT speculate.
> - Filter test per term: does this verse, through THIS term, say something about how a person thinks, feels, chooses, relates, or is oriented toward meaning, others, or God?
>
> **Output:** return a single JSON array — one object per **verse**, in the same order as the input — with this shape per object:
>
> ```json
> {
>   "reference": "<copy from input>",
>   "decisions": [
>     {
>       "verse_record_id": <int from input>,
>       "mti_term_id": <int from input>,
>       "strong": "<copy from input>",
>       "summary": "<≤25 words plain English, OR null if set_aside=true>",
>       "set_aside": <true|false>,
>       "set_aside_reason": "<one of the categories above, OR null if set_aside=false>",
>       "note": "<optional one-line note, or null>"
>     }
>   ]
> }
> ```
>
> The `decisions` array MUST contain exactly one entry per term in `terms_to_classify`, in the same order. Return ONLY the JSON array — no prose before or after.
>
> Acknowledge that you have understood the role and the contract. I will then send the input JSON in a second message.

---

## Block B — JSON INPUT (paste second)

50 verses with 63 terms-to-classify total. Open `outputs/markdown/manual-test-brief-verse-input-50-20260504.json` and paste its contents (≈120 KB).

```
[paste the full contents of manual-test-brief-verse-input-50-20260504.json here]
```

PowerShell helper to copy the file to the clipboard:

```powershell
Get-Content "outputs\markdown\manual-test-brief-verse-input-50-20260504.json" -Raw | Set-Clipboard
```

---

## What this test stresses

| Test | Pass condition |
|---|---|
| **Multi-decision discipline** | When a verse has multiple terms-to-classify, each gets its own atomic decision — no consolidated/comparative phrasing across terms. |
| **No `wrong_face` drift** | The model produces summaries (or set-asides) for each term independently rather than deferring inner-being content to a sibling term. |
| **Verse-level coherence** | Decisions in a single verse should be internally consistent (e.g. if shame is the topic, both shame-terms should reflect it independently). |
| **Set-aside discipline** | Where a term genuinely engages no inner-life content, the model sets aside with the right reason from the reduced enum. |
| **Brevity** | Summaries are ≤25 words. No theology essays, no parallel cross-references. |

When you save the chat output, Claude Code will compare it verse-by-verse against the API run on the same 50 verses and surface any disagreements.
