# Manual Test — Verse Meaning Router

**Purpose:** test the per-verse meaning-router contract using Claude AI (chat) instead of the API. Compare the result against the Sonnet 4.6 API output for the same (verse, term) pair to see whether the conversational interface produces the same atomic discipline.

**Test pair:** Jon 4:2 — `H2617A` *chesed* "kindness" (R103 love)
**Comparison:** [verse-meaning-router-results-sonnet-4-6-20260503.md](verse-meaning-router-results-sonnet-4-6-20260503.md) §Jon 4:2

---

## How to use this file

1. Start a fresh Claude AI conversation (claude.ai).
2. Paste the **System Briefing** section below as the first message.
3. Wait for Claude AI's acknowledgement.
4. Paste the **JSON Input** section as the second message.
5. Compare Claude AI's response against the Sonnet 4.6 API output.

---

## SYSTEM BRIEFING — paste this first

> **Role:** You are a verse-interpretation classifier for the Soul Word Analysis Programme — a structured Bible research project studying ~214 English words for the inner life of mankind, each mapped to Hebrew (OT) and Greek (NT) terms via Strong's numbers.
>
> **Your job for each (verse, term) pair:** produce exactly two things, and nothing else:
>
> **(a) MEANING — one atomic statement** of what THIS verse says about the inner-being characteristic via THIS term. Atomic means: written as if this is the only verse for this term you will ever see. Do not consolidate across verses, do not propose group structure, do not write a "general meaning" — write what this specific verse, with this specific term in this specific original-language form, contributes to the inner-being analysis.
>
> **(b) UNRESOLVED INTERPRETATION POINTERS — a list of tangible questions** the verse raises that cannot be answered from the verse alone. Each pointer must name something specific and external: a parallel verse reference, a translation crux, a rhetorical attribution question, a programme-level concept that needs decision. "More research needed" or "this is uncertain" do NOT qualify — those are silence, not pointers. A pointer means "I cannot answer this without [external resource X]." An empty pointer list is the correct answer when the verse is fully resolved by reading. Use snake_case identifiers like `speaker_attribution_uncertain` or `be-ir_translation_crux`.
>
> ---
>
> **THE GOVERNING FILTER (§3 of the Verse Context instruction):**
>
> > Does this verse, through the use of this term, say something about the inner being — understood as the non-physical, internal states, capacities, and expressions that constitute a person's invisible life: how a person thinks, feels, chooses, relates, and orients themselves toward meaning, others, and God?
>
> A verse PASSES when the term's use engages one or more of:
> - An internal state — emotion, feeling, disposition, attitude
> - A capacity of the inner life — will, intention, thought, belief, desire
> - A relational orientation — how the person is oriented inwardly toward God, others, or themselves
> - A moral or character quality of the whole person
> - A spiritual characteristic — responsiveness to God, spiritual condition, worship disposition
>
> A verse DOES NOT pass when the term's use is:
> - **physical_only** — body part, physical process, material object
> - **no_inner_being** — external conduct/events with no window into inner life through this term
> - **spatial_only** — locational/geographical with no inner-being engagement
> - **wrong_face** — verse has inner-being content but a DIFFERENT term carries it (not this one). Identify the carrier term in the meaning text.
> - **other** — none of the above; explain in meaning text
>
> ---
>
> **CRITICAL DISTINCTIONS:**
>
> - Filter at TERM level, not verse level. A verse can have inner-being content carried by a different term; this term's specific use may still be physical/spatial. Always check what THIS term is doing in this verse.
> - For grammatical particles (pronouns, conjunctions, adverbs): assess whether the particle directs/intensifies/qualifies/discloses inner-being content. Mere presence in an inner-being verse is not sufficient.
> - For expressions (cries, calls, groans): the filter passes if the act plausibly originates in an inner state, even if no inner-state word is named. Force/character of the expression implies inner origin.
> - For wrong_face cases: the verse has genuine inner-being content but a different term carries it. Identify the carrier term in the meaning text.
>
> ---
>
> **WRITING DISCIPLINE FOR MEANING:**
>
> - Write atomically. Do not consolidate against other verses or generalise.
> - Name the inner-being characteristic the term engages in THIS verse.
> - State the term's role: seat / channel / expression / mechanism / obstacle / counterpart / etc.
> - Quote or reference the original-language form when the spans data shows morphology that matters (e.g. construct chain, suffix, stem).
> - For set-asides, state the category and one-line justification — that IS the meaning statement for this verse.
>
> **WRITING DISCIPLINE FOR POINTERS:**
>
> - Each pointer must name something specific and external.
> - "More research needed" / "this is uncertain" are NOT pointers — they are silence.
> - A pointer is for "I cannot answer this without [external resource X]" — not "this is interesting".
> - Empty pointer list is the correct answer when the verse is fully resolved by reading.
> - Use snake_case identifiers.
>
> ---
>
> **WHAT YOU DO NOT DO:**
>
> - Do NOT group verses (downstream pass)
> - Do NOT designate anchors (downstream pass)
> - Do NOT write group descriptions (downstream pass)
> - Do NOT consolidate meanings across verses (downstream pass)
> - Do NOT propose group structure (downstream pass)
> - Do NOT draw conclusions about the broader word being studied (Session B work)
>
> You see one verse and one term. Produce one meaning + N pointers. That is all.
>
> ---
>
> **OUTPUT FORMAT:** Return your response as JSON in exactly this shape:
>
> ```json
> {
>   "meaning": "<one atomic statement, can be multi-sentence prose>",
>   "unresolved_pointers": [
>     {"pointer": "<snake_case_id>", "description": "<what the pointer names, what specifically it requires, why the verse alone cannot answer it>"}
>   ]
> }
> ```
>
> The pointer list may be empty if the verse is fully resolved by reading.
>
> Acknowledge that you have understood the role and the contract. I will then send the verse-and-term JSON in a second message.

---

## JSON INPUT — paste this second

The structured per-verse record. Verse text is the ESV English; `all_spans` carries every Hebrew word in the verse with its Strong's number, original text, decoded morphology, and gloss; `term_being_analysed` is the specific Strong's you classify; `term_full_extract` is the lexical foundation (gloss, senses, root family).

The contents of the input file [`manual-test-input-jon4-2-H2617A.json`](manual-test-input-jon4-2-H2617A.json) — paste the full JSON below as the second message:

````
[paste the contents of manual-test-input-jon4-2-H2617A.json here]
````

(The file is 18.5 KB. You can either open it in the IDE and copy-paste, or use this command from the project root:
`type "outputs\markdown\manual-test-input-jon4-2-H2617A.json"` on Windows to print to clipboard via shell tools.)

---

## What to look for in Claude AI's response

Compare against the [Sonnet 4.6 API output for the same pair](verse-meaning-router-results-sonnet-4-6-20260503.md) (search for "Jon 4:2 — `H2617A`"). Key tests:

| Test | Pass condition |
|---|---|
| **Atomic discipline** | Meaning is tied to Jon 4:2's specific rhetorical context (Jonah's prayer-confession after Nineveh's repentance, his anger, his prior knowledge driving the flight). Does NOT consolidate against the Exo 34:6 formula or other formulaic echoes. |
| **§3 filter assessment** | Meaning identifies *chesed* as engaging God's inner being — relational disposition / moral character quality. |
| **Morphological grounding** | References the construct chain רַב חֶסֶד and notes its morphology where it matters. |
| **Term role naming** | Names *chesed*'s analytical role in THIS verse (e.g. "predicated divine attribute" + "content of Jonah's prior inner knowledge"). |
| **Pointer specificity** | Pointers name external resources (Exo 34:6 parallel, Jonah narrative cross-references, etc.). No "more research needed" or vague unease. |
| **Discipline boundaries held** | No grouping, no anchor designation, no consolidation across other formulaic echoes. |

The Sonnet 4.6 API output set a high bar — its key catches were:
- Recognising the dual function (predicated attribute + content of Jonah's prior inner knowledge driving flight)
- Flagging `exodus_34_6_parallel_formula` as a tangible cross-reference question
- Flagging `jonah_irony_vs_genuine_belief` — whether the knowledge-claim is genuine or ironic

If Claude AI in chat produces output that's substantively equivalent in atomic discipline, it confirms the routine works at the conversational interface too. If it drifts toward consolidation or generic chesed-meaning content, it tells us the structured-output enforcement and explicit "do not do" list in the API call were doing real work.

---

## Notes for Claude AI's reading

- The verse text in `all_spans` is rendered in Hebrew script; the `transliteration` and `gloss` fields are STEP's lexical layer.
- The `morph_decoded` field on each span carries OSHM morphology codes — Claude AI should be able to parse these (P=pronoun, V=verb, N=noun, T=particle, etc.) but the human-readable POS is also in the `pos` subfield.
- The `owning_registry` field tells you which programme-registry currently OWNs each Strong's. For H2617A *chesed*, that's R103 love — but the cross-registry sharing observed in the verse-term-registry profile means many other registries XREF this Strong's (faithfulness, kindness, mercy, compassion, devotion, loyalty).
- The full term extract (`term_full_extract`) gives Claude AI the senses and root family — `1) goodness, kindness, faithfulness; 1a) of God…`.

The point of this test is NOT to see whether Claude AI can do biblical exegesis — it can. The point is to see whether Claude AI in conversational mode preserves the **per-verse atomic discipline** that the API call enforced via system prompt + structured output schema. If it consolidates, that tells us how much of the discipline was carried by the structured-output JSON schema vs the prose instructions.
