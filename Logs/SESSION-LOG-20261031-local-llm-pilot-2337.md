# Session log 2026-10-31: local LLM engine, first pilot (#2337)

Session id: bc4646d4-fb8c-44c2-9458-ccd5cae37828 (standard session; `/start-project` was not run, see the compliance file).

## 1. Scope

2026-10-31: the researcher asked for a local LLM engine that reads the database and analyses verses without chat or cloud resources. Done: a hardware check (16 GB RAM, 4 GB Vega M GPU, CPU only) and advice on a mini PC (Ryzen AI Max+ 395 with 128 GB, advice only, nothing bought); Ollama confirmed running with `qwen2.5:7b-instruct`; a read-only pilot over the 39 `m21-asking` verses redone on 2026-10-30, tested on one verse (Deut.10.12). Not done: the pilot on the other 38 verses. The researcher decided the approach must change and will design it.

## 2. Escalations

- #2337 (Local LLM engine for verse analysis: redesign): raised at close with the six researcher messages verbatim, the work done and the finding. Assigned to the researcher; the design is theirs.

## 3. Files

- `iba/app/staging/pilot_local_llm/export_pilot.py` and `iba/app/staging/pilot_local_llm/Pilot-LocalLLM.ps1` (new, unregistered, read-only on `iba/app/db/iba.db`).
- `iba/app/staging/pilot_local_llm/runs/pilot-20261031_052026/` (the one test run: input export, the verse result, `summary.csv`); an earlier failed call wrote nothing.
- `iba/app/BUILD.md` (entry 436).
- `Logs/compliance/COMPLIANCE-20261031-bc4646d4.md`, this log, and the session-close reports under `iba/app/reports/`.

## 4. Decisions

Researcher's own:
- "it is obvious that I need to change to approach when using local llm. I will work on it.": the one-pass approach is dropped and the researcher designs the next one, recorded in #2337 v1.

Claude's, within the request:
- The pilot is kept as a throwaway in staging, unregistered, until the new approach exists: `iba/app/BUILD.md` entry 436 and #2337 v1.
- The model name is `qwen2.5:7b-instruct`, as installed (the short name failed): `iba/app/staging/pilot_local_llm/Pilot-LocalLLM.ps1`.

## 5. Open items

- #2337 (researcher): the new approach to local analysis. The test showed one generic observation per item (10 against 31) and 237 s per verse; per-characteristic passes with the meaning data from the database are the direction suggested, not decided.

## 6. Git

_(written after the first commit)_
