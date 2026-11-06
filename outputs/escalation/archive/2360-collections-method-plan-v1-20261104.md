# Collections of surfaces by likeness of meaning, method plan for approval (#2360)

> Developer Mode session 325129d4, 2026-11-04. Nothing in this plan is built or run. It follows the researcher's instruction and decisions D1 to D3 of 2026-11-04 (recorded on #2360 v2 and v3). A new mechanism is designed here and comes to the researcher first (B:105, B:44). Every judgement the method makes is inferential (B:4) until the researcher confirms it.

## 1. What goes in (checked live in `outputs/escalation/2359-surfaces-and-bases-v1-20261104.xlsx`, sheet Surfaces)

- **3,850 surfaces**: 2,533 inner_being_state and 1,317 behaviour (corrected group, first-split-v4). 2,684 are single words and 1,166 are phrases.
- Each surface has a **combined base**. They give **2,481 distinct bases**: 699 bases hold more than one surface (largest 7: believe, break, condemn, sin) and 1,782 hold one.
- Base source: 2,217 own base, 1,246 from the structure methods, 387 from Ollama.
- Flagged items from #2359 that travel with the bulk (D2): 99 surfaces with a lead (opposite or other), 47 with a base found outside the list, and the held M1 pairs and failed words. They are carried as a flag column and never settled before the run.
- Judgement is on the surface text. Never the Strong's code, never the cluster (cluster work is a later cross-check).

## 2. The unit and the shape of a collection

- **The unit is the base, not the surface.** All surfaces of one base are one unit and always stay together; that is the "same base" part of your description. Behaviour and state surfaces are not separated: `group` stays as a column but no longer divides collections.
- A collection holds, for each member base, **why it is there**, one of: `root` (the seed itself), `same base` (already decided by the base column), `synonym` (same meaning by definition), `opposite` (D3: the contrary of a member, in the same collection), `associated` (related by meaning, but not a synonym).
- **A base sits in exactly one collection**; the runner-up collection, when the judge names one, is kept as a cross-link for the later rollup. (Decision 1 below.)
- **No target count** in this assembly (D1). The 250 to 300 is for a later rollup of collections into larger ones.
- **Nothing is written to the database** (D1). Results are files: one JSON line per judgement under `outputs/concept-mapping/collections/`, and a workbook for you to inspect.

## 3. The rounds

1. **Seed round.** Propose seed collections from the pool of all 2,481 bases, by two sources compared in the experiment: (a) embedding groups with no seed (method 1): bases whose meaning vectors are close form a proposed seed group; (b) model-listed words (method 4): from a core word the model lists words of like meaning, which are matched back to the pool. Each seed is a root base plus its first members. A seed needs at least 2 bases or one base with 2 or more surfaces to count.
2. **Attach round.** For each seed, a **shortlist** of the nearest remaining bases is taken by embedding (method 5, k set by the experiment). The judge then rules per (collection, candidate): relation `same meaning`, `opposite`, `associated`, or `none`, with a reason under 10 words (method 3). The judge sees the collection's current members (bases with their surfaces) and the candidate. `none` leaves the candidate in the pool.
3. **Inspect the remainder.** The pool left is embedded again and grouped afresh; the groups with 2 or more bases become new seeds (round 1 logic on a smaller pool) and are attached the same way.
4. **Repeat** rounds 2 and 3. **Stop** when a full round creates no new seed of 2 or more bases and attaches fewer than a set number of bases (starting value 10, to be settled by the pilot). What is left is the **long tail**, listed unassigned and handled later.
5. After each round the collections are exported for your inspection; a round does not start until the one before is exported.

## 4. The experiment before the full run (your five methods, two embedding models, with and without a frame)

Embedding models: `nomic-embed-text` and `qwen3-embedding` (both pulled on the server, not yet in `cfg_setting`; B:124 requires the settings and a check that the server has them before the first call). Frame: the bare word, against the word inside a one-line frame ("an English word as the ESV uses it, for a study of the human inner being").

- **Free test material, no hand marking needed**: the 699 multi-surface bases give known "same meaning" groups, and the 22 flagged opposites give known "opposite" pairs. For each model and frame, the test measures how many of those known partners land in the shortlist of the nearest k bases (k = 10, 20, 40). This is a measured recall, not an impression.
- **Judge check**: a pilot of 200 bases (a mix of multi-surface, opposite-flagged and singleton bases), run through seed, shortlist and judge, written out for you to read. The pilot is where you tell me whether the judge's `associated` is too wide or too narrow.
- The two embedding models and two frames give 4 runs; the report lists the recall of each and what it costs in time. The choice of model and frame is yours after you see it.

## 5. How it is built and run (B:124, B:125, CHARTER section 1)

- A routine inside the app: a new work package and step(s), a PowerShell wrapper in the style of `iba/app/ps/Surface-Judge.ps1`, reusing `iba/app/lib/surfacejudge.py` for the server check, the tunnel and the halt after consecutive failures. New settings (module `surface_judge`, plus the embedding model names under `ollama`): the collection prompt, the relation list, shortlist k, stop thresholds, the output folder.
- The server, the tunnel and the timeouts come from the existing `ollama.*` settings (host 192.168.83.114, model `qwen3:30b`, ssh tunnel). The judge is `qwen3:30b` unless you say otherwise.
- Any run longer than a few minutes starts through Windows' own process service with a log under `Logs/`, is resumable, and I report how to check, stop and resume it (B:125). Time per judge call is about 10 seconds (#2359 measure); the full number of calls depends on k and is estimated from the pilot before any full run.
- Code is tested in this session on a copy (never the live database), recorded in a BUILD.md entry and on #2360 (CHARTER section 4).

## 6. For you to decide

1. **One collection per base**, with the runner-up kept as a cross-link, or allow a base in two collections? (Default: one, cross-link kept.)
2. **Phrases in or out.** 1,166 of the 3,850 surfaces are phrases ("a sinner"). They are mostly their own base and mostly singletons. In the first assembly, include them with the single words, or hold them until the single-word collections exist and then attach them? (Default: hold them, attach them in a later round, because a phrase is easier to place once its collections exist.)
3. **Starting stop value** of 10 attached bases per round and the 200-base pilot: right, or other?
4. **Go ahead with the experiment of section 4** (settings added, models checked, pilot of 200 on a copy), on this plan?

When you answer these, the next step is the build of the experiment only. The full assembly is a separate approval after you have read the experiment report.
