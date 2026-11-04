# Session log 2026-11-04: concept building from surface assessment, base forms of the surfaces (#2359), families raised (#2360)

Session id: 5dc90923-c91d-49ea-bb95-5a05766d55a3 (Developer Mode, started 2026-11-04, closed 2026-11-04).

## 1. Scope
Developer Mode on #2359 (concept building from surface assessment, raised this session). Input: the #2354 surface judging (`first-split-v3-20261103.jsonl`, judge `qwen3:30b`), collection a) only (groups `behaviour` and `inner_being_state`, 3,850 surfaces after correction). The researcher dropped cluster and cluster-subgroup data as the basis (checked at row level, not workable) and directed word-association by similar meaning, starting with word structure. Done: the two perspectives of surfaces against their groups (the second dropped by the researcher's change of direction); word-structure matching with control lists (v1 to v3); the repoint of 56 base words in a corrected copy (v4); a registered tool that asks the Ollama server for the base form of the 707 words still unmatched (BUILD 455), pilot twice, amended once, full run finished (676 answered, 31 failed); two embedding models pulled on zeta-assist for the later comparison; one workbook of all 3,850 surfaces with their bases. The researcher judged the workbook "reasonable" and asked for the families escalation. Nothing from the Ollama base-form run or the structure leads was applied to any list. Judged groups and Ollama answers are inferential (B:4).

## 2. Escalations
- #2359 (Concept building from surface assessment): raised and updated v2 to v15; v15 carries the researcher's messages of the session verbatim; assigned to Claude, in-progress, next action review; not completed. It stays open as parent for the review of the base-form results, the 52 held M1 pairs and the flagged opposites.
- #2360 (Families from surface bases, concept building stage 2): raised at close; first step is a plan for the five-method experiment, for the researcher's approval before any build.
- #2354 (Reset narrative): its judging run finished earlier; its record is in the 2026-11-04 session log of 7631fc39, not changed here.
- #2357 (open config advisories): with the Researcher, not touched.

## 3. Files
Index of the outputs (everything below is tracked by this log; #2359 and #2360 name the key ones).

Escalation deliverables, `outputs/escalation/` (id-prefixed, B:60/B:64):
- `2359-base-form-ollama-plan-v1-20261104.md`: the plan and question for the Ollama base-form step (approved: "Approve, run pilot", "Amend, then run").
- `2359-base-form-results-v1-20261104.xlsx`: results of the full run (tabs Accepted with a flag column, None, Failed, Notes).
- `2359-surfaces-and-bases-v1-20261104.xlsx`: the single inspection workbook, 3,850 surfaces, structure base, Ollama base, combined base and source, Columns tab. Starting point of #2360.

Working data, `outputs/concept-mapping/surface-group/`:
- `first-split-v4-20261104.jsonl`: first-split-v3 with 56 base words repointed (changed lines carry `original_group`, `corrected_by`, `correction_basis`); v3 untouched. Corrected counts: behaviour 1,317, inner_being_state 2,533, being 716, other 1,503.
- `surface-repoint-m1-v1-20261104.xlsx`: applied changes, and the 52 pairs (39 bases) held for the researcher.
- `surface-match-control-v1-20261104.json/.xlsx`, `-v2-`, `-v3-` (v3 is the current control: input list, constructs, hits, normalised list, sibling groups; 681 single words unmatched plus 26 leads).
- `base-form-pilot-v1-20261104-input.json` / `.jsonl`, `base-form-pilot-v2-20261104-input.json` / `.jsonl`: the two 20-word pilots (before and after the amended question).
- `base-form-v1-20261104-input.json`, `base-form-v1-20261104.jsonl`: the 707-word run and its answers (676 answered, 31 failed; run log `Logs/surface-base-run-20261104.log`).
- `surface-group-rows-v1-20261104.xlsx` (9,632 rows at row level, with Columns and Notes tabs), `surface-groups-vs-classes-v1-20261104.md`, `subgroup-surface-classes-v1-20261104.csv`: the first perspective, cluster-based, shown unusable by the researcher.
- `surface-families-v1-20261104.xlsx`: stemmer-based families, superseded as a method, kept as history.
- `first-split-v3-20261103.jsonl` and `.progress.json`: the #2354 batch, committed in the state the finished cycle left them.

Code and config:
- `iba/app/lib/surfacebase.py`, `iba/app/handlers/surfacebase.py`, `iba/app/ps/Surface-Base.ps1` (work package `surface-base`, steps `surface_base.status` and `surface_base.run`).
- Migrations, `iba/app/migration/archive/`: `surface_base_2359_v1_20261104.py` (14 cfg writes), `surface_base_prompt_2359_v2_20261104.py` (the amended question).
- Test: `iba/app/tools/temp_2359_surface_base_test_run.py` (38 cases, all pass on a copy).
- `iba/app/db/iba.db`: cfg rows through `apply_logged` (settings `surface_judge.base_prompt`, `base_relations`, `base_form_pattern`, `base_input_suffix`, the work package, steps, on_fail and utility rows).
- Documents: `iba/app/BUILD.md` (section 455), `iba/app/USER-GUIDE.md` (section 8.9), `iba/docs/ps tools worksheet.xlsx` (tab Surface-Base and an Index row).
- Server: `nomic-embed-text` and `qwen3-embedding` pulled on zeta-assist (log `~/ollama-pull-embed-20261104.log` there); not yet in cfg_setting.
- Generated: `Logs/compliance/COMPLIANCE-20261104-5dc90923.md`, config reports `outputs/configs/CONFIG-REPORT-v690-20261104.md` (earlier ones archived), `outputs/escalation/escalation-list-v235-20261104.md`, `iba/app/reports/session-close-*.md`.

## 4. Decisions
- The researcher: the work is on collection a) only; b) and c) assessed by the researcher after the surface work; recorded in #2359 v15.
- The researcher: no judgement rooted back to the Strong's code; cluster and subgroup data are not the basis for concept groups, only a later cross-check; recorded in #2359 v15.
- The researcher: concepts are isolated by word association on similar meaning, starting with word structure (derivatives, prefix, suffix, tense); families and synonyms come later; recorded in #2359 v15 and #2360.
- The researcher: the control lists (input, each base-match construct, normalised beside original) in one JSON, with what is unmatched visible; recorded in outputs/concept-mapping/surface-group/surface-match-control-v3-20261104.json and #2359 v15.
- The researcher: base words found outside the input list are repointed into a) or b) in the surface list; recorded in outputs/concept-mapping/surface-group/first-split-v4-20261104.jsonl and #2359 v15.
- The researcher: Ollama is asked the base form of the remaining words, keeping the rule of similar root meaning; the question amended and run; recorded in iba/app/BUILD.md section 455 and `cfg_setting surface_judge.base_prompt`.
- The researcher: the two embedding models are compared, pulled on the server, which is dedicated to the task; recorded in #2359 v15 and #2360.
- The researcher: the workbook of surfaces and bases is reasonable, errors will settle later; families get their own escalation and a session log; recorded in outputs/escalation/2359-surfaces-and-bases-v1-20261104.xlsx and #2359 v15.
- Self-corrected by Claude: the repoint rule's regex slip (replaced by an explicit list), bell-character escapes in the PS script and guide, the WAL-missing test copy; recorded in iba/app/BUILD.md section 455.

## 5. Open items
- #2359, with Claude, next action review: the Ollama base-form results are the model's and unapplied; 22 derivations flagged as possible opposites (`unfaithful` to `faithful`, `unholy` to `holy`), the meaning-shifted bases (`grateful` to `grate`, `lazy` to `laze`, `undoing` to `undo`), 31 failed words, 289 "none" answers not yet checked; 52 held M1 pairs; the researcher's choice on how to treat them.
- #2360, with Claude: the plan for the five-method experiment (embedding groups with no seed, seed words, judge per surface, model-listed words, shortlist then judge; `nomic-embed-text` against `qwen3-embedding`, with and without a context frame); the embedding models and server routes need cfg_setting rows first (B:124).
- Where the judge put surfaces in `other` or `being` that belong to a) is the researcher's later assessment of b) and c) (recorded in #2359).
- #2357 (config advisories) remains with the Researcher.

## 6. Git
Branch: main. Commit 4cadd943f5bd54ccd41bc3baf8555e3389f12979, `session 20261104: concept building from surface assessment (#2359), base-form tool and run (BUILD 455), surfaces-and-bases workbook, repoint v4, match controls v1-v3, families raised (#2360), session log, compliance file and close reports`.
Push output: `To https://github.com/lcilliers/Bible_Projects.git   fd61f59e..4cadd943  main -> main`.
