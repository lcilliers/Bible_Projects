# Base form by Ollama, plan for approval (#2359)

> Developer Mode session 5dc90923, 2026-11-04. Nothing in this plan has been built or run. It follows the researcher's instruction of 2026-11-04: ask Ollama for the base form of the remaining unmatched words, keeping the rule of similar root meaning. A new mechanism is designed here and comes to the researcher first (B:105).

## 1. What goes in

The single words still unmatched after the structure methods, from `outputs/concept-mapping/surface-group/surface-match-control-v3-20261104.json` (built on the corrected list `outputs/concept-mapping/surface-group/first-split-v4-20261104.jsonl`): **681 unmatched** and **26 whose base was found outside the input list** (707 in all). Phrases are not included. The word only, no verse, no Strong's code, no cluster.

## 2. The question put to the server (draft, one word per call)

```
You give the base form of one English word as the ESV Bible uses it, for a study of how Scripture describes the human inner being.
English: "{surface}"

Give a base word only when the English is an inflected or derived form of it AND the two share the same root meaning.
- Inflected forms count: tense, plural, participle, comparative, including irregular ones (sought: seek; wept: weep; grew: grow).
- Derived forms count only when the core meaning stays the same (wonderful: wonder).
- Not the same root meaning, so give the word itself: an opposite (unfaithful, faithless), a different word that only looks similar (lying is not lye), a word whose meaning has moved away from its base, and a word with no base.
Answer JSON only: {"base":"...","relation":"inflection|derivation|none","reason":null}
"reason" only when relation is none and the word looks derived: under 10 words (else null).
```

## 3. How the rule of similar root meaning is kept

1. The question above says it, with the cases that fail it.
2. The answer is accepted only when `relation` is inflection or derivation, the `base` is one lower-case word of letters, and it is not the word itself.
3. Every accepted answer is listed with the word, the base, the relation and the server's model; it is inferential (B:4). The answers are reported to the researcher with that data, and are not applied to the surface list before that.
4. A `none` answer leaves the word unmatched, with the server's reason if it gave one.
5. A check before the full run: a **pilot of 20 words** (10 known inflections, such as `sought` and `wept`, and 10 I expect to stay unmatched), shown to the researcher.

## 4. How it is built and run (B:124, B:125, CHARTER section 1)

- A routine inside the app, not a loose script: a new work package, a PowerShell wrapper like `iba/app/ps/Surface-Judge.ps1`, a library module and handlers, registered in `cfg_work_package` and `cfg_step`.
- The server, model, timeout, tunnel and halting come from the existing `ollama.*` settings. The question, the answer format and the batch folder are new `cfg_setting` rows (module `surface_judge`). It checks the server and the model before the first call and refuses at once if they do not answer, and halts after the configured number of calls in a row with no usable answer; it reuses `iba/app/lib/surfacejudge.py` for this.
- The answers go to a batch file, one JSON line per word, in `outputs/concept-mapping/surface-group/`; no table is written. It is resumable.
- At about 10 seconds a call, 707 words take about two hours. A job that long is started through Windows' own process service with its output in a log under `Logs/`, so it does not depend on this session (B:125).
- The code is tested in this session on a copy, not on the live database (CHARTER section 4, #2137), and recorded with a BUILD.md entry.

## 5. For the researcher to decide

1. Is the question in section 2 right, especially the cases listed as not the same root meaning?
2. Run on the 707 only, or also on the 98 words that the sibling method joined, as a check on that method? (Default: the 707 only.)
3. May a base the server gives be accepted even when it is not itself in the input list (for example `adulterer` for `adulterers`)? (Default: yes, listed as a computed base, as the sibling method does.)
4. Go ahead with the pilot of 20 first? (Default: yes.)
