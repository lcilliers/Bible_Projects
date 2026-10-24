# #2188: the 8 instruction files and the iba/config JSON, mapped to config (v1, 2026-10-24)

Researcher 2026-10-24, on #2188 v7, verbatim: *"proceed with mapping"*. That is step 1 of the approach in
`outputs/escalation/2177-reset-backlog-plan-v1-20261021.md` §1: a mapping only. **Nothing in config or in the files is
changed until you approve this mapping.** Researcher 2026-10-21 (v5), verbatim: *"pause this work until the study is
restarted and the narration can be aligned between the rules"*. The study restarted on 2026-10-23
(`governance.study_status`), and the mapping is read against today's rules (B:1 to B:116).

Each instruction goes to one of:
- **(a)** already held by a cfg row (named), so the file line becomes a pointer;
- **(b)** a new rule, or an amendment to one, with draft wording;
- **(c)** history: the file, or the section, goes to `archive/` (rule B:96);
- **(d)** guide detail: worked method that stays in a guide file which a cfg row points to.

## 1. What changed since the plan of 2026-10-21

- **Nothing live reads any of the eight files.**
  - The book-narrative generator was retired (#2201 item 5). `method.inner_being_narrative_guidance_path` and
    `method.narrative_hard_constraints_path` are inactive.
  - The three passage-debate steps (`report.passage_debate`, `passage.debate_sync`, `chapter-generate`) are inactive.
    `method.passage_read_guidance_path` and `method.interpretation_questions_path` are still active, but no active
    step uses them.
  - `narrative.inner_being_style_guide_path` is active. No code reads it; B:86 points to it.
- **The JSON readers are archived:** `iba/scripts/archive/build_dbschema.py` and `probe_step_api.py`. Nothing live
  reads `iba/config/`.
- **So decision 1A of the plan** (whether the four code-read files stay as files or become rows) **falls away.**
  Decision 1B (the study hold) is settled by the restart.

## 2. Summary

| File | Size | Verdict |
|---|---|---|
| `Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md` | 15.9 KB | **live guide:** rules to cfg (b), stale parts out (c), detail stays (d) |
| `Workflow/Instructions/wa-verse-reading-by-role-guide-v2-20261019.md` | 18.0 KB | **live guide** behind B:73: stale references updated, otherwise (a)/(d) |
| `Workflow/Instructions/WA-inner-being-narrative-guidance-v1-2026-07-28.md` | 8.3 KB | **(c)**: carried into the style guide (§0, §7a, §10 item 6); its generator is retired |
| `Workflow/Instructions/WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md` | 8.2 KB | **(c)**: carried into the style guide (§0); its generator is retired |
| `Workflow/Instructions/WA-passage-read-guidance-v1.5-2026-08-02.md` | 13.2 KB | **(c)**: its rules are `cfg_method_rule` rows 1 to 43 (source_doc); its steps are inactive |
| `Workflow/Instructions/WA-interpretation-questions-v1.4-2026-08-02.md` | 14.9 KB | **(c)**: as above |
| `Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md` | 25.9 KB | **(c)**: the July lexical pipeline (`ve_lexical`, `segment_unit` in bible_research.db, B:67); its one live idea (§13b, §14: role per occurrence) is already in B:73 and the role guide |
| `Workflow/Instructions/wa-operational-governance-v1_0-20260614.md` | 6.6 KB | **(c)**: retired by its own banner on 2026-08-18 (#715); its content is in cfg rows |
| `iba/config/DBSchema/DBSchema.json` (+ `.md`), `iba/config/utility/DBSchema_maintenance.json`, `step.json` (+ `.md`) | | **(c)**: their readers are archived; nothing live reads them |

## 3. The style guide, section by section

| § | Instruction | Verdict | Where it lives |
|---|---|---|---|
| 0 | What the guide governs; its sources | (c) the source table; (a) the scope | scope: `narrative.inner_being_style_guide_path` (use text), B:86 |
| 1 | Let Scripture speak for itself; no joined patterns; "I read" only as restatement; quote and stop | (a) | B:69, B:90 |
| 1.5 | An insight found while writing goes to the record first | (a), wording now B:114 | B:114 (record, then synergise); B:112 |
| 2 | Five prohibited patterns | superlatives (a) B:36; literary framing, comparative claims, premature closure, claims that conflict with the data: **(b) N1** | |
| 3 | Voice: first person "I", testimony, plain, confident where plain and open where open, general reader | **(b) N2** | |
| 4 | Words never in chapter text (cluster, strand, observation, Strong's, "this study" and the rest); Hebrew or Greek with its gloss | **(b) N3**; gloss (a) B:100, M:111 (obs_text only, so N3 adds chapter text) | |
| 5 | Every claim on a cited verse; ESV checked; reference style (full book names, then chapter:verse alone); a lone occurrence stated as such; open threads and contradictions stand | claim (a) B:77; ESV (a) B:87 and `narrative_register.quote_check`; contradictions (a) B:77; reference style and lone occurrence **(b) N4** | |
| 6 | Silence named only when it carries weight | **(b) N4** | |
| 7 | Weave, don't fit; change of character; Held material; prose supported by bullets; titles name the subject only | weave (a) B:88; change of character (a) B:89; Held (a) B:87; bullets and titles **(b) N5** | |
| 7a | External parties: each dealt with in relation to the phenomenon, in its own terms, not watered down | routing (a) B:72; "in its own terms, not watered down" **(b) amend B:72 (N6)** | |
| 8 | Checks before a file is committed (reverse audit, let-Scripture-speak pass, quote check, external-party and format checks, self-review, records) | quote check (a) mechanical; reverse audit and records (a) Reading.ps1 gates 2 and 3; the reading passes (let-Scripture-speak, external party, format, self-review) **(d)**, kept as the guide's checklist under N1 to N6 | |
| 9 | Chapter drafts are files, not DB prose rows | **(c) stale**: the narrative is kept in iba.db blocks (`governance.narrative_home`, B:76); decisions to a `.md` and an escalation (a) B:16, B:18, B:21 | |
| 10, 11 | Differences between the guides; change history | (c) | `archive/` |

**Draft rules (for your wording):**
- **N1** `study_method.narrative-no-unsourced-framing`: "Chapter text does not frame a verse with a literary verdict, does
  not compare (the NT goes deeper than the OT) without the evidence, does not close a question the verses leave open,
  and never says what the data does not. The verse is rendered; the framing is dropped."
- **N2** `study_method.narrative-voice`: "Chapter text is written in the first person singular ('I', never 'we'), as
  testimony and not report: plain short sentences, confident where the verse is plain and open where it is open, for
  a general reader with no Hebrew, Greek or interest in how the work was done."
- **N3** `study_method.narrative-no-project-vocabulary`: "Chapter text never uses the study's working vocabulary
  (cluster, M-code, strand, observation, finding, Strong's number, ledger, 'this study', 'our analysis') or describes
  how the work was done. A Hebrew or Greek word always comes with its gloss."
- **N4** `study_method.narrative-citation-and-silence`: "References give the full book name first, then chapter:verse
  alone within that chapter, with several witnesses separated by semicolons. A lone occurrence is stated as such. A
  silence is named only where it carries weight: an expectation set and not met, or an absence that shapes the thing."
- **N5** `study_method.narrative-format`: "A passage opens in prose with its point, and bullets carry its different
  applications; a bullet list never stands without its prose introduction, and argument stays in the prose. A title
  names its subject only and never characterises it."
- **N6** amend **B:72** `llm_output.route-verses-hib-other-beings-data-only`, adding: "Any external party a verse
  brings in (God, the Spirit, other spirits, angels, another person, a crowd, the physical world) is dealt with in
  relation to the phenomenon, each in its own terms, and its role is not watered down."

With N1 to N6 in config, the style guide keeps §1 to §8 as worked guidance, with each rule replaced by a pointer
(rule B:3). §9 to §11 go to `archive/`.

## 4. The role guide, section by section

The guide is B:73's method (B:73 names it). It stays a guide (d), with these changes.

| § | Instruction | Verdict |
|---|---|---|
| 1 | What the reading is for | (a) B:72, B:89; glossary prose |
| 2 | The terms | (a) glossary prose (bible_research.db, the B:67 exception) and B:72; the role concept now cites the archived verse-analysis method |
| 3.1 | Use what is already extracted | (a) B:71 |
| 3.2 | The surface table | (a) B:110 |
| 3.3 | Earlier readings of the same verses | (a) stale wording: now `Verse-Collate.ps1` and Reading.ps1 Open give what is known for a scope (B:114) |
| 3.4 | Check `_analytics/cross-cluster-web/open-threads-register.md` | **(c) stale**: the register is in the escalation table (B:74), matched by Reading.ps1 at Open and Synergy |
| 3.5 | Filters are working aids | (a) B:111 |
| 4.0, 4.1 | Read outward from the verse; read it in its passage and genre | (a) B:116 (new), B:73 |
| 4.2 to 4.8 | Main operation, roles, relations, parties, original, face, record | (a) B:73 (the rule), (d) the method |
| 4.9 | Never close on "not X" | (a) B:73 (#2168 amendment) |
| 5.1 to 5.5 | Progressive reading; group by operation; one account per phenomenon; faces kept; faculty last | (a) B:91, B:89, B:88; (d) the method |
| 5.6 | Trial a few verses first; read, don't ask; don't hold; weave, don't fit | (a) B:109, B:92, B:88; "trial a few verses first" (d) |
| 6, 7, 8 | Worked cases; checks; sources | (d); sources updated (the `feedback_*` memory files are retired, #2184) |

## 5. The JSON in iba/config

- `DBSchema.json` (and its `.md`), `DBSchema_maintenance.json` and `step.json` (and their `.md`) are read only by archived
  scripts. Verdict **(c)**: they move to `iba/config/archive/`.
- Two live references follow:
  - `iba/app/lib/schemareport.py:190` tells the reader to see `DBSchema.json` and the archived `build_dbschema.py`.
    The pointer text is removed. That is a code change, with its BUILD.md entry.
  - `cfg_setting session_close.build_scope` lists `iba/config/*`. The entry is removed through configmaint.propose.

## 6. Found on the way (not in #2188's scope, for you to place)

- **`cfg_method_rule` rows 1 to 43** (the passage-debate method: `hib.set`, `phenomenon.set`, `operation.set`,
  `closing.set`, `passage.build`) are `active=1`, but the steps they govern are inactive. B:61 already keeps inactive
  steps out of use. Whether the rows should be made inactive with their steps is a question I have not raised.
- **Backups:** the operational governance file's §2 recorded the NAS backup schedule as "not yet cfg-resident". I have
  not checked whether that is still so.

## 7. What step 2 would do, once you approve

1. Propose N1 to N5 and the B:72 amendment (N6) through `configmaint.propose`, as worded or as you reword them.
2. Rewrite the style guide (v3), with the rules replaced by pointers and §9 to §11 archived. Update the role guide
   (§2 source, §3.3, §3.4, §8).
3. Move the five history files and the iba/config JSON to `archive/`.
4. Set `method.passage_read_guidance_path` and `method.interpretation_questions_path` inactive, and drop `iba/config/*`
   from `session_close.build_scope`. Both go through configmaint.propose.
5. Remove the stale `schemareport.py` pointer, with its BUILD.md entry.

## Your decision

1. The mapping, as above: ______
2. Rules N1 to N6: as worded, or reworded: ______
3. Section 6, the `cfg_method_rule` rows: raise as its own item, or leave: ______
