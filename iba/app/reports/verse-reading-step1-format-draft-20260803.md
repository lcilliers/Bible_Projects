# Step 1 format draft — verse reading (lexical, isolated) — Obad 1:1 worked example

> Draft only. Not written to DB. Format not yet approved. Source: `iba/app/verse-analysis/Obadiah/obad-1-verse-span-meaning.md` (the existing raw span-level extract — surface/strong/morph/meaning_tree per word). This record is one step further than that raw extract: a grounded, per-verse lexical reading built strictly from the span evidence, done in isolation from every other verse.

## Worked record

```json
{
  "osisId": "Obad.1.1",
  "book": "Obadiah",
  "chapter": 1,
  "verse": 1,
  "source_extract_path": "iba/app/verse-analysis/Obadiah/obad-1-verse-span-meaning.md",
  "span_count": 18,
  "lexical_reading": "A vision (H2377 — prophetic oracle, not a dream-image) belonging to/from Obadiah (H5662R). It is introduced as authoritative reported speech: 'thus says' (H0559 — a formal speech-act formula) the Lord God (H0136/H3069 — divine title/name pair) concerning Edom (H0123G). The speaker(s) — an unspecified 'we' — report having heard (H8085G) a report/tidings (H8052) from the Lord (H3068G, YHWH), and state that a messenger/envoy (H6735A) has been sent (H7971G) among the nations (H1471A). The verse closes with a quoted summons: 'rise' (H6965J, chosen sense: hostile/attack, not the neutral 'stand') — repeated twice — 'against her for battle' (H4421).",
  "span_trace": [
    { "span_idx": 0, "strong": "H2377", "chosen_sense": "vision, oracle, prophecy (divine communication)" },
    { "span_idx": 3, "strong": "H0559", "chosen_sense": "to say (Qal) — formal declarative speech-act" },
    { "span_idx": 8, "strong": "H8085G", "chosen_sense": "to hear (perceive by ear / report received)" },
    { "span_idx": 14, "strong": "H6965J", "chosen_sense": "to arise — hostile sense (not neutral 'stand')" },
    { "span_idx": 15, "strong": "H6965J", "chosen_sense": "to arise — hostile sense (not neutral 'stand')" }
  ],
  "unresolved_items": [
    "subject of 'we have heard' (v1) — not identified in this verse alone; candidate-determination question, not resolved here",
    "identity of the messenger (v1) — unspecified agent, no referent within this verse"
  ],
  "status": "draft",
  "read_at": null,
  "read_by": null
}
```

## Open questions for verification

1. **`lexical_reading` as prose vs. structured clauses** — right now it's one paragraph. Could instead be an array of clause-level readings (one per syntactic unit) if that serves step 2/3 better.
2. **`span_trace` scope** — currently only flags spans where a *choice* was made among variant senses (ambiguous/multi-variant Strong's). Should every span be traced, or only the disambiguation-relevant ones?
3. **`unresolved_items`** — deliberately *not* resolved here (that's the point of isolation — no reaching into v2+ or the passage debate to fill it in). Confirm this is the right boundary: step 1 names the gap, step 2 (human-beings) is where it gets resolved.
4. **Granularity** — this is whole-verse. Given multiple clauses/subjects can appear in one verse (as here — narrator, "we", the Lord, the messenger, the nations), does step 1 need a lower unit than "verse," or does that belong to step 2's candidate work?
5. **No DB table exists yet for this.** Confirming this shape is what step 1 should write is a precondition to building the table/column set — nothing built yet.
