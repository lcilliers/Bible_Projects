# surfacejudge.py explained, as registered: what goes in, what is asked, what comes out (#2354, v2, 2026-11-02)

Replaces v1, which described the library before the first split was decided. Library `iba/app/lib/surfacejudge.py`, handlers `iba/app/handlers/surfacejudge.py`, front `iba/app/ps/Surface-Judge.ps1`. Usage: USER-GUIDE.md section 8.8. Build record: BUILD.md section 447. Test results: `outputs/escalation/2354-surface-judge-test-plan-v1-20261102.md`.

## 1. In one paragraph

The tool takes the distinct surfaces of `surface_subgroup`, asks the Ollama server one question about each ("is this English definitely a behaviour, a state of the inner being, a being, or otherwise?") and appends the answer to a batch file, one line per surface. It writes nothing to `iba.db`. A surface goes to behaviour, inner_being_state or being only when the model says it definitely belongs there; everything else is `other`, the list you will clean up in a later pass. Every answer is inferential until you confirm it.

## 2. What goes in

| Input | Where it comes from |
|---|---|
| The list | `SELECT surface, COUNT(*) FROM surface_subgroup WHERE deleted=0 AND surface IS NOT NULL AND trim(surface)<>'' GROUP BY surface ORDER BY COUNT(*) DESC, surface`: 6,069 distinct surfaces, most rows first. The 4 live rows with a blank surface are left out (nothing to ask). Recorded meaning of the column (`cfg_column.use`): "verse_lexical.surface, lower-cased and trimmed". |
| The server and limits | `cfg_setting` module `ollama`: host `http://192.168.83.114:11434`, model `qwen3:30b`, timeout 900 s, keep-alive 30m, context 4096, temperature 0. |
| The groups | `cfg_setting surface_judge.groups`: behaviour, inner_being_state, being, other. |
| The question | `cfg_setting surface_judge.word_prompt` (a config row now, not a code literal). `{surface}` is replaced by the English. |
| The batch file | `<surface_judge.batch_dir>/<-Batch>.jsonl`; `-Batch` is lower-case words, `-v{n}`, `-yyyymmdd`. |

Nothing else is sent: no verse, no Hebrew or Greek code, no gloss, no neighbouring word. Whatever the model knows of the word in Scripture it brings from its own training.

## 3. What is asked (the whole message, shown for "fear")

```
You classify one English word or phrase as the ESV Bible uses it, for a study of how Scripture describes the human inner being.
English: "fear"

Answer with exactly one group:
- behaviour: something a person does or undergoes, inwardly or outwardly (an act, feeling, thought, speech, choice)
- inner_being_state: a standing condition or characteristic of a person's inner being (righteous, wicked, wise, proud)
- being: an entity: a person, God, a spirit, an angel, or a part of a person such as the heart or the soul
- other: everything else

Give behaviour, inner_being_state or being only when the English definitely belongs there as the Bible uses it. If it does not definitely belong in one of those three, or you cannot tell, answer other. Words that only describe, locate or link something (pronouns, prepositions, adverbs, conjunctions, articles, numerals, degree words) and words with no bearing on a person's inner being are other.
Answer JSON only: {"group":"...","reason":null}
"reason" only for other, under 10 words (else null).
```

The call is `POST {host}/api/chat` with `stream: false`, `think: false`, `format: json`, temperature 0.

## 4. What comes back, what is checked, what is written

The model answers `{"group": ..., "reason": ...}`. The answer is accepted only if `group` is one of the four. If it is not, or the call fails (network, timeout, JSON that cannot be read), the call is made once more; after two failures the surface is recorded with `group` null and the errors listed.

One line is appended to the batch file as each surface finishes, and printed on the terminal:

```
{"surface": "fear", "group": "behaviour", "reason": "fear is an action or response", "judged_by": "qwen3:30b",
 "errors": [], "secs": 6.8, "out_tokens": 17, "prompt_tokens": ..., "tok_s": ...}
```

- **Restart:** a run reads the file first and skips every surface that has a group; a surface that failed is tried again. Ctrl+C stops after the surface in hand has been written.
- **Status:** `-Action Status -Batch <name>` reads the file against the list: judged per group, failed, left.
- **Database:** nothing is written. Loading confirmed groups into `surface_subgroup.surface_group` is a separate step that does not exist yet.

## 5. What it did on the three real pilot surfaces

First three of the live batch `outputs/concept-mapping/surface-group/first-split-v1-20261102.jsonl` (the most frequent surfaces): strong = inner_being_state (11.3 s), right = inner_being_state (11.0 s), desire = behaviour (7.1 s). The model gave a long reason for answers other than `other`, though the prompt asks for one only for `other`; it is recorded as given. The quality of the groups is yours to judge; the tests show the tool works, not that the groups are right.

## 6. What changed from v1

- The pair path (per Strong's code) is removed.
- The list is `surface_subgroup`'s 6,069 surfaces, not the 18,249 of `verse_lexical`.
- Four groups; no `use`, no `also`, no `qualifier`, no `not_allocated`.
- The prompt and groups are config rows.
- The answer check refuses anything outside the four groups.
