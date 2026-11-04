# surfacejudge.py explained: what goes in, what is asked, what comes out (#2354, 2026-11-02)

File: `iba/app/lib/surfacejudge.py` (263 lines). Written for the researcher, from the code as it stands (git 3e591fe9) and the recorded meaning of the tables it reads. Nothing in it has been changed for this document.

## 1. In one paragraph

The library takes English words as the ESV renders them (the `surface` of `verse_lexical`), asks the Ollama server one question about each ("what kind of word is this in the Bible?") and writes the answer to a file, one line per word. It never writes to `iba.db`. There are two paths in the file. The **per-word path** (from line 182) is the working one you asked for: one call per distinct English string, no Hebrew or Greek codes sent. The **pair path** (lines 1 to 180) judges each (Strong's code, English) pair; the 7-surface pilot showed it does not work, it is kept and unused. Every answer is inferential (B:4) until you confirm it.

## 2. What goes in (per-word path)

| Input | Where it comes from | What it is |
|---|---|---|
| The list of surfaces | `surface_list(conn)`: `SELECT lower(surface), COUNT(*) FROM verse_lexical WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>'' GROUP BY 1 ORDER BY 2 DESC, 1` | Every distinct live English string, lower-cased, most frequent first. 18,249 strings today. Top: lord (10,004), and (8,231), all (8,211), not (8,128), to (5,671). |
| Server and limits | `cfg_setting` module `ollama`: host `http://192.168.83.114:11434`, model `qwen3:30b`, timeout 900 s, keep-alive 30m, context 4096, temperature 0, codes per call 8 | Read by `settings()`. If any is missing, the run stops with `JudgeError`. |
| Allowed answers | `cfg_enum` `surface_pair_verdict.surface_group` (behaviour, inner_being_state, being, qualifier, not_allocated) and `surface_pair_verdict.use` (place, time, quantity, quality, manner, reason, negation, pronoun, article, conjunction, preposition, particle, other) | Read by `run_words()`. The model's answer is checked against these. |
| Output file | `out` path given by the caller; the setting `surface_judge.batch_dir` is `outputs/concept-mapping/surface-group` | Appended to, never overwritten. |

Recorded meaning of the column used (B:123): `verse_lexical.surface` is "span.surface, denormalized: the literal text at this span, independent of sense", filled by `lexical.build`, expectation blank. The recorded text is thin on one point: BUILD 428 and working log finding 28 say a multi-code span carries the span's whole English on every code, so a surface can be a phrase, and the list contains phrases as well as single words. `verse_lexical` is "one row per Strong's code within a span". Nothing about the verse, the Hebrew or Greek code, or the sense is sent on this path.

## 3. What is asked

One call per string, to `POST {host}/api/chat`, `stream: false`, `think: false`, `format: json`, `temperature 0`, context 4096. The whole message is the text below with the string and the 13 uses filled in (shown here for "made"):

```
You classify one English word or phrase as the ESV Bible uses it, for a study of how Scripture describes the human inner being.
English: "made"

Give the group of this English as it is used in the Bible:
- behaviour: something a person does or undergoes, inwardly or outwardly (an act, feeling, thought, speech, choice)
- inner_being_state: a standing condition or characteristic of a person's inner being (righteous, wicked, wise, proud)
- being: an entity: a person, God, a spirit, an angel, or a part of a person such as the heart or the soul
- qualifier: describes, locates or links something and is not itself a behaviour, state or being. This includes pronouns (who they name is settled when the verse is read), prepositions, adverbs, conjunctions, articles, numerals and degree words. For a qualifier give the use: place, time, quantity, quality, manner, reason, negation, pronoun, article, conjunction, preposition, particle, other.
- not_allocated: you cannot tell
Judge the English as it reads, by what kind of word it is and what it says. "also" gives a second group only if the English is commonly used in a second, different way (for example "long" as a time word and "long" as a desire).
Answer JSON only: {"group":"...","use":null,"also":null,"reason":null}
"use" only for qualifier (else null). "also" is another group from the list or null. "reason" only for qualifier and not_allocated, under 10 words (else null).
```

The group definitions and the question are literals in the code (`WORD_PROMPT`, line 183), not config. The model sees only the English and these definitions: no verse, no neighbouring words, no Hebrew or Greek, no gloss. Whatever it knows of "made" in Genesis 1:26 it brings from its own training.

## 4. What comes back and what is checked

The model must answer one JSON object: `{"group", "use", "also", "reason"}`. `check_word()` accepts it only if:
- `group` is one of the five groups;
- if `group` is `qualifier`, `use` is one of the 13 uses;
- `also` is empty or one of the five groups.

It does **not** reject a `use` given for a non-qualifier on this path, and does not check that `reason` is under 10 words. If the answer fails the check, or the call fails (network, timeout, JSON that cannot be parsed), the call is tried **once more**. After two failures the word is recorded with `group: null` and the errors listed.

## 5. What is written

One JSON line per word, appended and flushed as each word finishes:

```
{"surface": "made", "group": "...", "use": null, "also": null, "reason": null,
 "judged_by": "qwen3:30b", "errors": [], "secs": 12.3, "out_tokens": ..., "prompt_tokens": ..., "tok_s": ...}
```

`judged_by` is the model name when the answer was accepted, else null. The last three come from the server's own counts. Each word is also printed to the terminal as it finishes.

- **Restart:** `run_words` reads the file first and skips every word that already has a `group`. A word that failed (group null) is tried again on the next run. A stop at any point loses at most the word in progress.
- **Database:** nothing is written. `surface_pair_verdict` (empty) and `surface_subgroup.surface_group` are not touched by this library; loading verdicts is a separate step not yet built.
- **`also` has no home yet:** `surface_pair_verdict` has no column for it, so a second group lives only in the batch file until you decide where it goes.

## 6. The pair path (kept, not the working path)

For one string, `pairs_of()` lists the distinct Strong's codes the string translates, each with its `kind`:
- `particle`: code is H9xxx. Settled by a rule, no model call: group `qualifier`, use from `PARTICLE_USE` (a 13-entry table in the code; H9020 to H9049 are `pronoun`). `judged_by` is `rule:particle_code`.
- `own`: the code occurs in at least one span with a single non-particle code.
- `span_shared`: the code occurs only in spans with 2 or more non-particle codes, so the English is the unit's.

Own and span_shared pairs go to the model, up to 8 codes a call, with each code's `strong.stepGloss` (recorded meaning: "short English sense") and the same five groups, answered as a list of pairs. Same checking, same one retry. The 7-surface pilot of it (`outputs/concept-mapping/surface-group/pilot-2354-v1-20261102.jsonl`): "you" carries 123 codes (13 calls, 407 s), 29 of 253 rows had no group, and the model judged the code's gloss rather than the English. This is why you replaced it.

## 7. What has and has not been run

- The pair path ran for 7 surfaces. The per-word path was syntax-checked only and has **not been run** against the server (BUILD 446). A throwaway script `iba/app/staging/surface_judge_pilot_2354/temp_2354_pilot.py` exists to run 100 strings through `run_words`; it has not been run either.
- Time per call is not yet measured on the per-word path. For 18,249 strings the total depends on the measured seconds per word; I have not measured it, so I give no estimate.

## 8. Points where the code departs from the app's own standard

These are findings, not changes made. Each is a decision for you.
1. **Prompt text in code.** `WORD_PROMPT`, `PROMPT` and the group definitions are code literals. The standard (`governance.rules_must_be_config_driven`) wants a rule that decides something as a `cfg_*` row. The group definitions are the test itself.
2. **`PARTICLE_USE` table in code** (pair path only, 13 entries plus the pronoun range).
3. **`also` has no column** (section 5).
4. **No check on `use` for non-qualifiers or on `reason` length** on the per-word path (the pair path does check the first).
