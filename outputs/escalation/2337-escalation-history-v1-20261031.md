# Escalation deep history

## #2337 — Local LLM engine for verse analysis: redesign
type=task source=researcher

**v1** (2026-10-31T05:29:36Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Local LLM engine for verse analysis: redesign
> **comment (set this version):** Session bc4646d4, 2026-10-31. Researcher messages, verbatim, in order:
1. "i want to build a LLM / AI engine that read the database locally and perform all the analysis on the verses locally without having to resort to chat or cloud resources."
2. "recommend a mini computer that have the resources needed for local llm work"
3. "ollama is now active"
4. "qwen2.5:7b is installed"
5. "prepare a powershell so I can run the pilot in the terminal"
6. "it is obvious that I need to change to approach when using local llm. I will work on it."

What was done: hardware check (16 GB RAM, 4 GB Vega M GPU, CPU only); recommendation of a Strix Halo 128 GB mini PC (advice only, nothing bought); Ollama 0.40.13 confirmed running with qwen2.5:7b-instruct (the installed name) and qwen2.5-coder:3b; a read-only pilot written in iba/app/staging/pilot_local_llm/ (iba/app/staging/pilot_local_llm/Pilot-LocalLLM.ps1 and iba/app/staging/pilot_local_llm/export_pilot.py) that runs the model over the 39 m21-asking verses redone on 2026-10-30 and compares item counts with the Analysis_phase_1 observations. Test on Deut.10.12: JSON valid, copy rule held, operation present, 10 model observations against 31 reference (one per item), 237 s for one verse (about 2.5 h for 39). Nothing written to iba/app/db/iba.db.

Finding: given the whole verse in one pass and no meaning data, the 7B model gives one generic observation per item, far short of the per-characteristic depth. Researcher decided the approach must change and will design it. The pilot files are unregistered (iba/app/CHARTER.md section 1: nothing outside the app); they stay in staging as a throwaway until the new approach is designed.
