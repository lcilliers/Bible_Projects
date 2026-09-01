# Word/term (lexical) — proposed `source` values

> Escalation #1007. Isolates the 16 live T-coded questions whose `scope = 'Word/term (lexical)'`
> (`T1.1.1`–`3`, `T6.4.1`–`3`, `T7.1.1`–`10`) and proposes a `source` value for each — a definitive
> statement of what the answer is derived from, not a hedge. Grounded in the already-verified
> table/field findings from
> [`tier-catalogue-iba-raw-data-mapping-v2-20260831.md`](tier-catalogue-iba-raw-data-mapping-v2-20260831.md)
> (Part 3), not re-derived from scratch — that document's own worked examples (Dan 1:8, `H3820A`
> leb) and live-data checks (`strong_related` has no relation-type column; `cluster_strong` has 77
> multi-cluster codes) are what each statement below rests on.
>
> Two shapes recur, both definitive on purpose: where the raw-data mapping found real structured
> or computable material, the statement names the exact table/field chain. Where it found none,
> the statement says so directly — "derived from interpretive reading/synthesis, not a stored
> field" — rather than leaving it blank or vague. Nothing here is written to the database yet;
> this is the proposal for your review before `obs_catalogue.update` runs.

| obs_id | Code | Question | Proposed `source` |
|---|---|---|---|
| 236 | `T1.1.1` | What is the characteristic called in the programme, and what does the name signal about its essential nature? | The name is derived from `word_registry.word` (the registered English word). What it signals about the characteristic's essential nature is derived from interpretive reading of that word's lexicon entries (`strong_meaning_parsed`/`strong_sense`), not a stored field. |
| 237 | `T1.1.2` | What do the primary Hebrew and Greek terms show at the definitional level? | The value is derived from `word_strong.strong` → `strong.stepGloss`/`strong.accentedUnicode`/`strong.stepTransliteration`, `strong_sense.head`, `strong_meaning_parsed`, `strong_meaning_tree`, `strong_lsj_parsed`, and `strong_mounce_parsed` — the full lexicon chain for every Hebrew/Greek code onboarded to the word via `word_strong`. |
| 238 | `T1.1.3` | What directional, relational, or constitutional implication does the name carry? | The value is derived from interpretive synthesis over the `T1.1.2` lexicon data — no field states a directional/relational/constitutional implication directly. |
| 379 | `T6.4.1` | Which vocabulary terms, if any, does this characteristic share with other characteristics in the programme? | The value is derived from `cluster_strong` (a Strong's code assigned to more than one `cluster_code` — 77 live cases) cross-checked against `strong_related` (STEP's root/cognate list per Strong's) — a computed proxy, not a stored "shared vocabulary" judgment. |
| 380 | `T6.4.2` | Does the sharing extend to root-level architecture — a shared root generating terms across two or more characteristics? | The value is derived from `strong_meaning_parsed.lemma_key` and `strong_related`'s root-form entries, grouped by shared root (e.g. `H3820A` leb related to `H3824` levav, `H3826` libbah) — a computed proxy; no field names "shared root architecture" directly. |
| 381 | `T6.4.3` | What does the vocabulary sharing show about the conceptual relationship between the characteristics? | The value is derived from interpretive synthesis over the `T6.4.1`/`T6.4.2` output — not itself stored. |
| 393 | `T7.1.1` | What are the primary Hebrew and Greek terms for this characteristic, and what do their root meanings show? | The value is derived from `word_strong.strong` → `strong.accentedUnicode`/`strong.stepGloss`/`strong.stepTransliteration`, `strong_meaning_parsed`, and `strong_meaning_tree`. |
| 394 | `T7.1.2` | What is the grammatical range of the primary term (noun, verb, adjective, participle), and what does that range show about how the characteristic operates? | The value is derived from `verse_lexical.strong` + `verse_lexical.morph_code`, aggregated across every occurrence of the term via `strong_verse` — the attested grammatical forms, computed directly from the parse data. |
| 395 | `T7.1.3` | What is the semantic range of the primary term — across what breadth of meaning does it operate? | The value is derived from `strong_meaning_parsed` (its `sense_code`/`gloss` rows) and `strong_meaning_tree`, keyed by `lemma_key` — the sense tree itself enumerates the term's semantic range. |
| 396 | `T7.1.4` | Does the vocabulary include terms distinguishing distinct aspects — disposition versus act, received versus given, condition versus quality? | The value is derived from a full manual read of `strong_meaning_parsed`'s glosses across the term's whole root family — no field tags this distinction; `strong_related` carries no relation-type column. |
| 397 | `T7.1.5` | Does the vocabulary include a term for the structural opposite or absence of this characteristic? | The value is derived from a full manual read of `strong_meaning_parsed`/`strong_related` across the term's whole root family — no field tags a structural-opposite relation. |
| 398 | `T7.1.6` | Does the vocabulary include a person-type term — one for the person who habitually possesses or exercises this characteristic? | The value is derived from a full manual read of `strong_meaning_parsed`/`strong_related` across the term's whole root family — no field tags a person-type/agent-noun relation. |
| 399 | `T7.1.7` | Does the vocabulary include a supplication or seeking term — one for the act of seeking this characteristic from another? | The value is derived from a full manual read of `strong_meaning_parsed`/`strong_related` across the term's whole root family — no field tags a supplication/seeking-term relation. |
| 400 | `T7.1.8` | What does the relationship between the OT Hebrew and NT Greek vocabulary show about continuity or development of the characteristic across the Testaments? | The value is derived from `word_strong.strong` filtered by `strong.language` (Hebrew vs. Greek), comparing the two vocabulary sets directly; judging what the comparison shows about continuity or development is interpretation on top of that raw comparison, not itself stored. |
| 401 | `T7.1.9` | Is there a term newly coined in the NT period for this characteristic; if so, what does the coinage show? | The value is derived from external Koine-Greek corpus comparison, outside IBA's data — `strong.created_at` records only when IBA fetched the code, not when the word entered the language, so it cannot answer this. |
| 402 | `T7.1.10` | What does the full vocabulary arc show about the characteristic's complete semantic range? | The value is derived from synthesis across `T7.1.1`–`T7.1.9`'s own answers — not itself a stored field. |

## What to decide

Each `source` above is a proposal, not yet written. Two shapes to confirm or correct:

1. **Table/field-backed** (`T1.1.2`, `T6.4.1`, `T6.4.2`, `T7.1.1`–`3`, `T7.1.8`) — these name exact
   tables/columns. If the phrasing needs to be tighter or a table/column is wrong, say which row.
2. **No stored field** (`T1.1.1`'s second half, `T1.1.3`, `T6.4.3`, `T7.1.4`–`7`, `T7.1.9`,
   `T7.1.10`) — these state plainly that the value comes from interpretive reading or external
   comparison, not a database field. If you'd rather these say something more specific (e.g. name
   *which* interpretive step or *which* external source), tell me and I'll sharpen them.

On your go-ahead I'll write these into `wa_obs_question_catalogue.source` for these 16 rows via
`obs_catalogue.update`, the same governed path used for `scope`.
