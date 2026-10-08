# CLAUDE.md — Claude Code Project Reference

> **★ AUTHORITATIVE SOURCE (researcher decision, 2026-09-28).** `C:\Bible_study_projects` is the **only** authoritative source for the project. **Ignore all other copies by default:**
> - `G:\My Drive\Bible_study_projects` — an old copy, to be archived in full
> - `G:\My Drive\Claude_Research` — a working folder for other platforms. Anything there that duplicates this project or Zotero is to be archived.
> - study documents in `%USERPROFILE%\Zotero\storage`, `Documents`, `Desktop`, and elsewhere on `G:\My Drive`
>
> Use a file from those places **only** when the researcher names it explicitly. Even then, say that it is outside the authoritative source, and bring it into this project (with the researcher's approval) before relying on it. The inventory and planned moves are in `research/investigations/file-location-inventory-*` (in progress).

> **★ THE `AskUserQuestion` TOOL IS BANNED IN THIS PROJECT — NEVER USE IT (reinforced 2026-07-22).**
> Blocked at config level (`.claude/settings.json` → `permissions.deny`), stated in
> `docs/interaction-preferences.md`, and in memory — after two prior "hard stop" warnings
> (2026-06-01, 2026-06-15) it was violated again this session, and the tool proved unreliable on
> top of being against policy: a fired question came back with the researcher's actual answer lost,
> only a bare rejection notice. Instead: investigate and present facts for anything answerable from
> the DB/code; put a genuine judgement call in a `.md` review file and point to it in plain chat;
> ask a real clarifying question in plain chat text. See `docs/interaction-preferences.md` for the
> full protocol.
>
> **★ IBA APP — SESSION START (2026-07-22).** This repo also contains a second, separate
> application — the **IBA app** (`iba/app/`), its own DB (`iba/app/db/iba.db`), its own config
> (`cfg_*` tables), and its own rules — distinct from the Bible-study programme the rest of this
> file describes. **On opening this project, before any IBA work, run
> `iba\app\ps\Start-Iba.ps1`** — it bootstraps config/DB/STEP and prints an orientation pointer to
> `iba/app/BUILD.md` (what's built) and `iba/app/GOVERNANCE.md` (how config governs the code).
> **To use the app, start at [`iba/app/USER-GUIDE.md`](iba/app/USER-GUIDE.md)** — not
> `iba/config/README.md`, which documents a separate, not-yet-loadable configurator design (see
> `iba/app/GOVERNANCE.md` on the two-configurator gap). **Never assume an IBA rule from memory or
> from a doc alone** — the rule that actually governs behaviour lives in a `cfg_*` DB row; changing
> one goes through `iba\app\ps\Config-Maintenance.ps1 -Step Propose` (approval-gated), never a
> direct edit.
>
> **★ BASE LAYER MOVED TO IBA — §4/§5/§7/§8 SUPERSEDED (2026-08-17).** §4 (The Engine), §5 (STEP API
> Client), §7 (Word Study Pipeline), and §8 (Data Flow) below describe the OLD `engine/`/STEP-client
> pipeline for base-layer work (word initiation → verse-lexical). Per the 2026-08-15 architecture
> correction, that layer is now owned entirely by `iba.db`/`iba/app/` — these four sections are
> **provenance-only** (accurate history of how it used to be done), not live instruction. For current
> base-layer work, start at [`iba/app/USER-GUIDE.md`](iba/app/USER-GUIDE.md). Each section carries
> its own short pointer back to this banner. Originated as governance-alignment register item #1
> (`docs/governance-alignment-register.md`, now retired-for-provenance — see its own banner);
> live tracking of this item is escalation #687 (completed). Full record: `iba/app/BUILD.md`.
>
> **★ bible_research.db IS PROSE-ONLY — §3's "prose and findings" framing SUPERSEDED (2026-09-24).**
> Every §3 table-group description below that calls `bible_research.db` "the home for prose and
> findings" is now stale. Researcher ruling (verbatim): *"findings is the terminology in the old
> system that is replaced by observations... all the finding related tables in research DB should
> be inactive and... all the records in those table are no longer relevant and can be purged."*
> Findings/observations now live entirely in `iba.db`'s `ib_observation`/`ib_node` pipeline;
> `bible_research.db` retains only the prose store as live content. Full record, including which
> tables were corrected and which were deliberately excluded from the sweep:
> `iba/app/GOVERNANCE.md` §81. This is exactly the kind of scope decision this banner section
> exists to surface — don't let it go undocumented again.
>
> **★ FAN-OUT REPLACES CLUSTER-BY-CLUSTER ANALYSIS (researcher decision, 2026-09-30).** After the M47
> inner-seat work and the M02/M20 prototypes, future analysis is **fan-out / progressive-stream**,
> not cluster by cluster. Researcher, verbatim: *"Clusters were originally designed to allow for
> creating batches of similar words to be analysed. however the study of M02 and M20 shows that
> progressive stream analysis will provide better result without doing a large portion of
> unnecessary cluster based findings."* Do not start another cluster reading. **Method (researcher,
> 2026-09-30, #1900):** the inner being is a *web of interrelated activity*. A stream is a strand
> of that web, with no start and no finish. Each strand is taken in turn and explored. The fan-out
> follows as the picture of the web develops. A strand may be diverted, and a "distraction" may
> deserve a deeper look. All strands eventually merge into one whole. **M47 is the starting point**
> (already begun). Open items are **parked focus areas**. Cluster codes stay as **anchor points,
> not goals**. None of the prior work is irrelevant. Answers #1899.
> **Capture is focused (researcher, 2026-09-30):** nodes and observations are written per topic or
> strand, as that strand is explored. There is **no** generic, whole-scope task and **no** backfill
> of earlier work. The `ib_node` principle (verse · surface · strong · subgroup = association ·
> question = stream) remains the central linkage.
> **Prose is the researcher's:** it is built up by the researcher as each area of focus develops.
> Claude never writes prose without a specific instruction.
>
> **★ THE ESSAY IS REGENERATED AS THE INNER-BEING NARRATIVE (researcher decision, 2026-09-30,
> #1912/#1913).** The Framework B essay (`_analytics/essay/spirit_soul_body/`, a two- vs three-part
> argument) is **reset** by the new research. It is regenerated as chapter files in
> `_analytics/essay/spirit_soul_body/inner-being-narrative/`. Start at `00-index-and-status-*`.
> Its title is *Inner Being in Operation* (confirmed 2026-09-30, #1916).
>
> Researcher, verbatim:
> - *"to original must adjust to the new, not visa versa"*
> - *"new theme is the inner being in operation described through the voice of the bible"*
> - *"each unfounded claim must be checked and restated"*
> - the narrative is written in the first person, *"personal, direct, easy to read"*, *"without
>   reference to the project terminology"*
> - *"Each next stream of work will add further updates to the narrative."*
>
> M47 was the first reset. Each later strand:
> - updates the chapter files it touches (version bump, with the prior version archived)
> - updates `wa-essay-spirit-soul-body-claim-register-*` in the same pass
>
> Rules for the chapter text:
> - Unchecked original material stays in marked **Held** sections.
> - Quote wording is checked against the ESV text in iba.db `verse`.
> - Science chapters come later.
> - The Holy Spirit study is separate.
>
> **Weave, don't fit (researcher decision, 2026-09-30, #1918).** Researcher, verbatim: *"Adding
> additional items is not a process of where does the new item support the current narrative - this
> is the wrong way around - it must be wove the new item into the narrative - knowing there is more
> to come."* Rules that follow:
> - Every observation from a strand gets a recorded placement. "Does not fit" is never one; it means
>   the narrative's structure must change.
> - Each strand also re-reads the sections it touches, and they adjust to it.
> - Ch 10 (*The inner being at work*) is designed in advance to grow.
> - Method: `wa-essay-narrative-weave-method-and-ch10-structure-*` in `_analytics/essay/spirit_soul_body/`.
>
> **Change of character is a key discovery (researcher, 2026-10-01, #1919).** Researcher, verbatim:
> *"One of the key discoveries in the study is how the meaning or application of the same concept /
> word changes in different circumstances … explore in more depth on when and how it changes
> character, why is it different. This should not be lost … It must be built upon, not be set aside."*
> - Every strand records each word's or concept's faces, the circumstances that differ, and why.
> - A word's meaning is never taken from its cluster tag, because a tag shows one face only.
> - ~~Proposal (awaiting approval)~~ **Approved and built 2026-10-01 (#1919):** `_analytics/cross-cluster-web/origin-of-thought/origin-of-thought-change-of-character-*`. Ledger v2 §I; Ch 11 §4 "What changes the character" is the cross-cutting account.
>
> **Narrative structure (researcher, 2026-10-01, #1920: "approve 1920 as recommended, remembering after 10.2"):**
> - A strand is **woven by activity, never given a file or chapter of its own**. The anger strand is the first worked example.
> - **10.3 Remembering and forgetting** was inserted, so the old 10.3–10.9 are now **10.4–10.10**.
> - The new **Ch 13 "Under God's anger"** sits between "goes wrong" and "made new". The old Ch 13 is now **14**, and the old 14 is now **15**.
>   - **Superseded 2026-10-05 (#1977):** Ch 13 is folded into **10.13 "Anger"** (section *Living under God's anger*). The numbers of Ch 14 and 15 are unchanged.
>   - **Superseded again 2026-10-07 (#1982):** Ch 13 is now **"Other beings"** (13.0 to 13.4); see below.
> - Ch 11 §4, "What changes the character", is the cross-cutting account that every strand adds to.
> - **Ch 9 "Life, breath and death" became Ch 2** (researcher, 2026-10-02, #1936: *"Move Ch 9 to Ch 2"*). Old Ch 2–8 became **3–9**. 10.x–15 are unchanged.
>   - Ch 2 now **sets the scene** (#1937): *"the context of Ch 2 is that it sets the scene for discovering the working of the inner being within the context of what life is about and what death means"*.
>   - It uses the verses' own phrases, never "umbrella" (the researcher's picture only).
>   - Links run through `_analytics/Clusters/M25 - life-death/life-death-linkage-map.md`.
> - **Open threads register (#1935):** `_analytics/cross-cluster-web/open-threads-register.md`. It holds held items, researcher questions and signposts, each with a "comes back when" trigger.
>   - Check it before every unit pull.
>   - Add to it at every ledger approval.
> - **Strand queue (#1933):**
>   1. life and death (M25): units 1–4 and Q2–Q4 ledgers done and woven. **Narrative placement held, not reworked** (researcher, 2026-10-04: *"M25 is a particularly difficult section and I am not sure it is the right time to try and massage it … these will only become really understood once other sections of the study is further developed"*). See open threads OT-08, and #1943 and #1948 (on hold).
>   2. ~~fear units 3–4, before any new cluster. **Unit 3 ledger approved, weave held** (#1957, OT-10: *"we want to first do more work on and around it before writing into the narrative"*). **Unit 4 (Greek) next, ledger only**, then a cross-ledger analysis of units 1–4 before any weave.~~ **Done 2026-10-04:**
>      - unit 3 (#1957), unit 4 (#1958) and the H4172A addendum (#1960)
>      - the cross-ledger overview (#1959, #1960)
>      - the 10.1 comparison **not** done (OT-12)
>      - **10.12 "Fear"** written and approved (#1961, #1962)
>
>      Next (researcher): *"gathering similar studies of other key characteristics."*
>   2a. **anger (M02), the second key characteristic, taken through the fear process (researcher, 2026-10-05, #1963).** Plan: `_analytics/Clusters/M02 - anger-wrath/anger-key-characteristic-process-proposal-v1-20261005.md` (§3A builds in #1944–#1947; rulings §7). Five word-family unit ledgers → coverage check → cross-ledger overview → **10.13 "Anger"**. Rulings:
>      - other parties' roles in anger are as important as God's (6.2)
>      - Ch 13 "Under God's anger" is to be **consolidated into 10.13** after 10.13 is written in full (6.3, OT-13) — **done 2026-10-05 (#1977)**
>      - #1944–#1947 are anchors for the reading method; Ch 10 will be retuned, **not yet** (6.5, OT-14)
>
>      **Unit 1 (*ʾaph*) approved** (#1966). **Unit 2 (*ḥēmāh* and the heat words) approved** (#1967; OT-15 added). **Unit 3 (*ḥārāh*, *ḥārôn*, *kāʿas*) approved** (#1968). **Unit 4 (the rest of the Hebrew and Aramaic) approved** (#1969). **Unit 5 (the Greek) approved** (#1973): all 65 Strong's and 919 hits faced. **Recovery and steps 2–4 done (2026-10-05):**
>      - The previous session ran ahead of the process. Researcher: *"AI started to follow its own imagination instead of the governance and instructions"*.
>      - Recovery file: `wa-cluster-M02-recovery-consolidation-v1-20261005.md`. The roll-up is tested by ID; the M-code pairings are OT-16 to OT-90.
>      - **Overview v2 approved** (#1974).
>      - **Part M** (U1/U2 wording) corrected in place with dated notes.
>      - **10.13 "Anger" v2** written and approved (#1976), with Ch 13 folded in (#1977).
>      - **M47 step** done (Ch 4–8; OT-18 resolved).
>      - #1975 closed: no re-tagging; OT-15 stays open.
>      - Handoff: `anger-strand-handoff-v1-20261005.md` (same folder).
>      - **No re-tagging** (#1970: *"cluster allocation is a loose association for the purposes of analysis"*; cfg_behaviour_rule 70, GOVERNANCE.md §88).
>   3. ~~then M12 and M64 as candidates~~ **#1933 closed 2026-10-06. M64 Will & Resolve is the next strand, on its own escalation, #1978.** M12 is not started.
>      - **Focused, not broad brush** (researcher, verbatim, 2026-10-06): *"The approach to the analysis will differ from previous iterations.  It will be much more focussed that broad brush as the results for broad brush were not as expected."*
>      - Work so far, all in `_analytics/Clusters/M64 - will-resolve/`:
>        - the M64 × M47 shared verses (56), cross-referenced to the narrative and the open threads register
>        - **29 uncited verses marked for deeper analysis and reading** (`m64-m47-marked-verses-v1-20261006.md`; researcher: *"the 29 verses will be fed back into analysis"*)
>        - a pinpointed pull of H6942H *dedicate*, held for M61 as **OT-91**
>        - **2026-10-07, the "choose" set.** This covers H0977, H0972, H7148, G0138, G0140, G4401, G0830, and on the researcher's instruction also G1586, G1588 and G1589. Files: `m64-choose-reading-v3-20261007.md` and `.csv`.
>          - All 232 verses are read and placed in 17 groups, with the faces of choosing (#1919).
>          - The M-codes in the 222 uncited verses are extracted (`m64-choose-mcode-cooccurrence-v1-20261007.csv`).
>          - Every verse is routed under rule 72: 166 to Ch 13, 52 inner-being only (B), 14 data only (C), and 14 flagged for the researcher.
>          - Nothing is woven (OT-92). The researcher continues with this output next session.
>        - **2026-10-07 (later), the HIB/qualifier split and §2a read verse by verse.** The words co-occurring in the choose verses are split into HIB, DIV and QUAL (`m64-choose-mcode-hib-qualifier-v1-20261007.md`).
>          - A first pass on §2a used a fixed frame per verse (what led to the choice, the choice, the outcome). The researcher **rejected** it: *"it may be mechanically right, but the outcome is fragmented"*; *"the method of interpretation is too far from the truth"*.
>          - Researcher's rulings on that pass:
>            - F1: the Job speakers are **choices evaluated by another party**, so they get their own section.
>            - F2: Pro 8:10 is not HIB, because "choice" describes the gold.
>            - F3: Isa 7:15–16 is the paired act, refuse the evil and choose the good, with its consequences. *"refusing is an implicit choice"*.
>            - F4: Isa 1:29 is figurative speech in an oracle.
>          - **Method from here (researcher, verbatim):** *"maybe my error is in giving you a framework or prompts for the reading, maybe I must leave you alone to do your thing, and then work with the outcome."* Each verse is read in its whole passage, with no framework. The account grows from the readings; nothing is overlaid on them. Memory: `feedback_read_verse_for_inner_act_not_event_template`.
>          - Done: a test of 3 verses (*"all three redone verses make sense and is valuable"*), then batches 1–4 (18 verses), then **the account of choosing**, `m64-choosing-account-v1-20261007.md`, for review.
>          - ~~The account covers §2a only. It is not woven.~~ **Woven 2026-10-08:** the researcher ordered *"first build the 2a into the narrative 10.7.  you will need to reframe 10.7 to ensure 2a is part of a larger context of choosing and setting direction and not a disconnected list of paragraphs"*. The results:
>            - **10.7 v10** was reframed as one account, built around Joshua 24 (choose, incline the heart, held).
>            - §2a's five faces went into **Ch 11 §4** (v14).
>            - Wanting beside choosing went into **10.6** (v8).
>            - **13.1** got its first content (v2).
>        - **2026-10-08, §2b (those who are chosen).** Read in two batches (OT 7, NT 8): `m64-choose-2b-reading-batch1-chosen-ot-*`, `-batch2-chosen-nt-*`.
>          - The account is `m64-being-chosen-account-v1-20261008.md`.
>          - It is woven as the **10.7 v11** section *Being chosen*. It also feeds the Ch 11 §4 faces "Choosing a person" and "Holiness" (v15) and 13.1 v3.
>          - Correction: in Eph 1:4 the love is God's ("In love he predestined", v5).
>        - **2026-10-08, §2c (others around the choosing).** 31 verses were read in three batches, including Michal (2Sa 6:16) and Moses in the breach (Psa 106:23): `m64-choose-2c-reading-batch1-chosen-place-*`, `-batch2-others-ot-*`, `-batch3-others-nt-*`.
>          - The account is `m64-others-around-choosing-account-v1-20261008.md`.
>          - It is woven as the **10.7 v12** section *Others around a choice*. Moses goes into *Being chosen* as *Standing for others*.
>          - **Placements confirmed** (researcher, verbatim: *"confirm Moses and Levite placements as recommended"*): Moses in *Being chosen*, the Levite of Deu 18:6 in *Others around a choice*. 10.7 is now v13.
>          - **Ch 11 §4 (v16) and 13.1 (v4) were updated from §2c** on instruction. Ch 11 §4 gained the faces desire, despising and knowing a choice, and fear beside a choice. 13.1 gained God's answers to those set against his choosing.
>          - The 166 verses routed to 13.1 are still held. They are not placed, because they were grouped, not read in their passages.
>          - Claim register v24. All on #1978.
>        - **2026-10-08, verses with no other M-code parked.** 41 of the 232 choose verses carry no other M-code (40 uncited, plus Act 10:41, which keeps its Ch 2 citation): `m64-choose-no-other-mcode-v1-20261008.md`. Researcher, verbatim: *"these verses can all be parked, the have no significant additional bearing on the study"*. OT-93; they drop out of the OT-92 routing.
>        - **#1978 complete for the time being** (researcher, 2026-10-08), approved and completed (v35). Carried forward: the 29 marked M64 × M47 verses, the 166 Ch 13 verses (OT-92), H6942H (OT-91), #1979.
>        - **2026-10-08, the "will" terms, on their own escalation, #1986.** Researcher: *"Create a new escalation to focus on the 'will', 'willing' terms in this cluster"*. Pull: H0014, H6634, H5081G (gloss) plus G1014, G1013 (surface): 99 verses, `m64-will-verses-v1-20261008.csv` and `.md`. G2309/G2307 (*thelō*, *thelēma*) are M18, not pulled. No reading yet.
>        - **2026-10-08, the 27 verses read in full, and their impact (#1987, cross-referenced to #1979).** Scope is holistic: their impact on the narrative, accounts, open threads, #1986 and #1979, of which citation is one part. Researcher: *"assuming the verse is already in the narrative and therefore should be ignored, is wrong."* A narrative citation is verse-level, not word coverage. 27 verses that earlier #1978 work set aside because they were cited (9 choose, Act 10:41, 21 M64 × M47) were read in full: `m64-reopened-cited-verses-reading-v1-20261008.md`. 10 carried for their M64 word; 17 hold something not carried. Nothing woven.
>      - #1979 (decision): the M47 reset recorded no verse-by-verse placement, so other M47 sections may also have dropped verses.
> - **A key characteristic gets a full account as its own Ch 10 sub-chapter (researcher, 2026-10-04, #1961). This modifies #1920 for key characteristics.** Researcher, verbatim: *"encapsulate the full finding of fear, as it emerged from the ledgers, the cross ledger review and the co-existence review into a separate Ch10 sub chapter. Be careful not to be distracted by elements that are not inner being relevant, but don't cut out external factors impact on or related to the operation and the inner being.  This is the first step. then we will proceed with gathering similar studies of other key characteristics."*
>   - First case: **10.12 "Fear"** (after 10.11, with no renumbering).
>   - Built from the unit ledgers, a cross-ledger overview (`_analytics/Clusters/M01 - fear-awe/fear-cross-ledger-overview-*`; moved from `cross-cluster-web/fear/` 2026-10-06 under #1965, GOVERNANCE.md §87) and the co-existence review (its §F).
>   - **Fear units 1–4 are complete**, with a unit 3 addendum for H4172A. That clears strand queue item 2 below.
>   - The other chapters are **not** reworked in this first step. 10.1's "Fear" section overlaps 10.12, and the 10.1 "Feeling" frame is open (OT-12: no biblical word names "feeling" as a category; `_analytics/essay/spirit_soul_body/wa-essay-narrative-feeling-frame-question-v1-20261004.md`).
>   - Style guide v2 §7 still states #1920 unchanged. It needs updating in v3 (deferred; #1930 closed 2026-10-06, so v3 takes its own escalation when it is taken up).
> - **10.11 "Hiding and disclosing"** was added after 10.10, with no renumbering (NS-D1, researcher 2026-10-02: *"ns-d1: select A"*, #1931). It holds M20's concealment phenomena as one account, because they face both God and others. M20 is fully woven; the record is in `_analytics/Clusters/M20 - doubt-discouragement/wa-cluster-M20-narrative-digest-v1-20261002.md`.
>
> **Verses are routed; other beings get Ch 13 (researcher, 2026-10-07, #1982; GOVERNANCE.md §90).** It arose from the M64 "choosing" reading. Researcher, verbatim: *"The study and narration primary focus in the human inner being. The actions of God are only analysed in so far as defining / impacting the HIB."* Each verse is routed in the ledger:
> - **(A) Other beings in their own right:** God, angels, other spirits, nature. These go to **Ch 13 "Other beings"**, with **13.1 Divine, 13.2 Angels, 13.3 Other spirits, 13.4 Nature** (D2). For God, this includes how his character passed to the HIB through creation; the image question is parked (#1984).
> - **(B) Another being with the HIB:** fully in HIB scope.
> - **(C) No inner-being or other-being bearing:** assessed in the analysis, but not in the narrative (D1).
> - A verse may take A and B.
>
> Further rules:
> - **No correction pass.** Existing analysis is reset only on the researcher's individual instruction (D3).
> - **The choosing verses are routed when the researcher directs** (D5: *"we are still busy with pre-analysis"*).
> - Ch 13 "Under God's anger" (a pointer to 10.13 since #1977) is replaced. The note that "Chapter 13" for God's anger means 10.13 is kept in 13.0.
> - Rule: `cfg_behaviour_rule` id 72 `route-verses-hib-other-beings-data-only` (#1985, applied).
>
> **Let Scripture speak for itself (researcher, verbatim, 2026-10-01):** "you are bordering on imputing meaning that is not supported by the verses. don't drive synergy and phantom observations into the findings. Rather allow scripture to speak for itself." No joining of verses into patterns, mechanisms or divisions that no verse states, in findings, ledgers or narrative. Quote, and stop.
> **Weaving carries meaning, not lists (researcher, 2026-10-01, #1930).** Researcher, verbatim: *"We lost meaning and interpretation, it is starting to just become a list of quotes"*; *"weaving means applying into other sections appropriate parts - it does not say you must ignore all the work that was done and listed in the ledger. you are not writing with intelligence and interpretation, you just doing a machanical mix and match excercise"*.
> - "Let Scripture speak" forbids joining verses into patterns no verse states. It does **not** forbid saying what a verse means in its own setting. That interpretation is required.
> - A phenomenon gets one coherent account that answers: what does Scripture say it is? What are its forms, from the words themselves? Why do they differ? (Model: 10.1 "Fear".)
> - Other sections carry only the parts that belong to their activity, rewritten as prose with chosen verses and pointing back to the account. Full verse lists stay in the ledger.
> - A verse that says nothing about the inner being or the word stays in the data, not the narrative.
> - Readings beyond what a verse states are marked "I read".
> - Style guide v3 is still to be written to fix this in config (deferred; #1930 closed 2026-10-06, so v3 takes its own escalation when it is taken up).
> **Writing standard (config, 2026-10-01):** `cfg_setting narrative.inner_being_style_guide_path` → `Workflow/Instructions/wa-inner-being-narrative-style-guide-v2-20261001.md`, plus `cfg_behaviour_rule` 69 `let-scripture-speak-no-imputed-synthesis`. The guide holds the researcher's #1924 rulings: prose supported by bullets; titles name the subject only; any external party in the verses (God, the Spirit, other spirits, angels, people, the physical world) is dealt with per phenomenon and never watered down.
>
> These narrative drafts are written **on the researcher's specific instruction**. They are files,
> not the DB prose store (the prose rule above is unchanged).
>
> Compact reference loaded into every conversation. Authoritative detail lives in `Workflow/Instructions/` (the `[current]` versions — see §10). Last refresh: 2026-04-27 (folder restructure: paths updated for the new top-level layout; pre-restructure refresh was 2026-04-26).
>
> **Orientation (2026-06-14; entry point corrected 2026-08-18):** §3 (schema) and §10 (programme state) refreshed to live **v3.31.0** + the finding-centric model. `docs/project-orientation-core-memory-map.md` — the former session-start fan-out map named here — was **retired 2026-08-18** (escalation #715 cycle 3: it had drifted pre-reset and pre-IBA with no live reader). **Start each session via the `start-project` skill** (`iba/app/GOVERNANCE.md` + `iba/app/BUILD.md` for IBA, the `escalation` table for open items project-wide); the current-state reconstruction in [`outputs/markdown/project-reconstruction/`](outputs/markdown/project-reconstruction/) (01–04) and the reusable-scripts catalogue remain valid background reading, just no longer fanned out from that retired map. This compact file can still lag the written record; when in doubt, the reconstruction is authoritative.
>
> # ★ LIVE METHOD — 2026-07-02 — verse-first / passage / self-learning lexical (schema 3.35.0)
> **The lexical process has fundamentally shifted** to a **self-learning, self-checking, passage-anchored, term-driven** method. **Authoritative now:** [`Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md`](Workflow/Instructions/wa-verse-analysis-method-v1-20260702.md) (the method) + [`Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md`](Workflow/Catalogue/wa-ve-lexical-catalogue-v1-20260702.md) (the item list). Key points: the ve-lexical is **verse-first**; a **passage = a maximal run of consecutive verses** (`verse.passage_id`, anchor = first verse); processing is **term-driven** (owner term's anchor verse first, then all its verses, `verse.process_marker` tracks completion); **genre-aware** (`verse.genre` → prose = cross-verse items on, poetic = two-phase); dimensions **D1–D14** are ve-lexical items (D10 valence / D12 hidden / D13 cohabitation **dropped**; `related_tier` deprecated); items are **pairs / events / flags** (`ve_lexical.from_span/to_span/resolution/pair_kind`). **Read-back + sensibility + rule-adjustment is core.** Schema now **3.35.0** (M61). Memory: `project_term_driven_genre_aware_lexical_method`, `project_ve_lexical_is_verse_first`. §3/§10 below are pre-this-work (legacy substrate).
>
> **★ CYCLE + DIMENSION AUTHORITY — 2026-07-08.** On top of the method/catalogue: [`Workflow/Instructions/wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md`](Workflow/Instructions/wa-characteristic-role-lexical-cycle-authoritative-v1-20260708.md) — AUTHORITATIVE characteristic→candidate→role→lexical cycle (Stage 0 passage prereq §4A · DB-updates/integrity §7A · transition §7B · pipeline+completion §7C · derivation principles §3A). Passage rule now **v2** (candidate-driven; v1 archived). **Dimension authority = the VE-lexical catalogue** (`wa-ve-lexical-catalogue-v1-20260702.md`, now with a **ve_nr master list §9**, 101–116 incl. `specifier`110/`locus`116); cycle §3 cites it. **Key invariant:** a `char_candidate` span with no verse-record = **DB integrity violation** (repair first). `wa-lexical-analysis-rules-reset-v1` **CLOSED** (principles → cycle §3A, items → catalogue); `wa-synthesis-B-spec-reset-v1` kept (stale). Memory: `project_lexical_cycle_finalised_and_integrity_invariant`.
>
> # ★ METHOD RESET — 2026-06-25 — "Characteristics → Movements"
> **The study's object has changed.** It no longer *identifies, names, describes individual characteristics*; it analyses the **movements, associations, interlocking, and emergence** of the inner being — modelled as a **process / relational web** read off *what each verse does*, with patterns allowed to **emerge** (not sorted into a grid). **The live method = the two reset specs:** [`wa-lexical-analysis-rules-reset-v1`](Workflow/Instructions/wa-lexical-analysis-rules-reset-v1-20260624.md) (decomposition) + [`wa-synthesis-B-spec-reset-v1`](Workflow/Instructions/wa-synthesis-B-spec-reset-v1-20260624.md) (assembly). **Milestone (arc · lessons · DB triage · change-over · rework scope):** [`wa-RESET-baseline-review-and-changeover-v1`](Workflow/methodology/wa-RESET-baseline-review-and-changeover-v1-20260625.md). Consequently the **characteristic / object-type / faculty-ontology / tier-grid / logical-unit framing is CLOSED (provenance-only)**; all prior lexical analysis + **all M01–M11 "completed" + all in-progress work is LEGACY to be revisited**. **§3 and §10 below describe the *pre-reset* structure — read them as the legacy substrate the reset builds on/replaces** (per the DB triage in the milestone).

---

## 1. What This Project Is

A structured academic Bible research platform centred on **~214 English words** for the inner life of mankind. Each word maps to Hebrew (OT) and Greek (NT) terms via Strong's numbers, captured in a SQLite database processed by a custom Python automation engine.

**Owner:** le Roux Cilliers — sole researcher; final authority on scope and methodology.

**AI roles:**

- **Claude Code** — DB engine: patch application, JSON export, schema migrations, validation queries, programme state, Verse Context batch construction, pool dataset assembly.
- **Claude AI** — analytical: term classification, verse analysis, scope judgements, narrative production, JSON extraction, Verse Context classification.

**Governing documents:** `Workflow/Instructions/`. All operational cross-refs use `[current]` → resolve to highest-numbered version at read time. Authoritative CC instruction: `wa-claudecode-instruction [current]`.

---

## 2. Directory Map

```text
Bible_study_projects/             ← working dir (C:\Bible_study_projects — moved off Google Drive 2026-06-03)
├── CLAUDE.md, README.md, tasks.md, .gitignore, .env
├── engine/                       ← Python automation engine (`python -m engine.engine`)
├── scripts/                      ← Utility/maintenance scripts (see §6 for prefix conventions)
│   └── analytics/                ← STEP/Zotero clients, db_client, word_export
├── database/
│   ├── bible_research.db         ← SQLite (~766 MB, NOT in Git)
│   └── archive/file_manifest.json ← RETIRED 2026-08-18 (escalation #730), frozen 2026-08-15 snapshot — live manifest is IBA's `file_manifest` DB table, see §9 item 5
├── Sessions-v2/                  ← ~~per-cluster working tree~~ **SUPERSEDED 2026-09-28: folder no longer exists; cluster output → `_analytics/Clusters/{code} - {short name}/` per `cfg_setting report.cluster_folder_naming_convention` (GOVERNANCE.md §83, #1884)**
│   └── {CODE}-{Name}/            ← one folder per cluster (M01-Fear … M46-Abundance, FLAG, T2); see README + file-organisation-rules §3.0
├── Sessions/                     ← Session-staged inputs and outputs (now READ-ONLY cross-reference)
│   ├── Patches/                  ← JSON patches (per-session-stage); applied → archive/patches/
│   ├── Session_A/                ← STEP Extracts, terms, Word_Data, registry, Data_Prose
│   ├── Session_B/                ← 12 numbered sub-stages (01_Verse_Context_Process_input … 12_Session_B_Status)
│   ├── Session_C/                ← Session C and Session_C_Words (word studies)
│   └── Session_D/                ← Session_D_Synthesis + session_d (cluster outputs)
├── Workflow/                     ← Programme governance
│   ├── Instructions/             ← Authoritative instruction docs (wa-*-vN_M-YYYYMMDD.md)
│   ├── Global_rules/             ← wa-global-rules-all-vN, -startup-vN, extract.json
│   ├── Catalogue/                ← Observation question catalogue extracts
│   ├── reference/                ← Reference snapshots, file/label/patch patterns
│   ├── registry/                 ← Registry-management guide + overview
│   ├── schema/                   ← create_tables.sql + database-schema-v*.json
│   ├── Programme/                ← programme_prose, programme_analysis, Program_reports
│   ├── methodology/              ← Methodology session logs and design notes
│   ├── Sessionlogs/              ← Cross-stage session logs
│   └── archive/                  ← Superseded instruction-doc versions
├── outputs/                      ← Generated artefacts (docx, markdown, pdf, session-logs)
├── research/                     ← discovery/ (STEP raw output), investigations/, notes/, templates/
├── docs/                         ← file-organisation-rules.md, interaction-preferences.md, *_setup.md
├── Logs/                         ← Pre-restructure session logs (historical)
├── archive/                      ← patches/, scripts/, docs/, Sessions/, References/, Programme_prose/, Logs/
└── backups/                      ← DB snapshots (NOT in Git)
```

For exact file lookup use `iba\app\ps\Manifest-Search.ps1 -Query "..."` (`scripts/build_file_manifest.py` retired 2026-08-18, escalation #730 — see §9 item 5).

---

## 3. The Database — Schema v3.33.0

> **2026-06-15 grounding + normalisation (major):** schema → **3.33.0**. (a) **`ve_lexical`** created (M59) = the *items-in-verse-level* table: VE field-VALUES normalised here (one row per value: `verse_context_id · ve_nr · ve_label · related_tier · value · source_provenance`); the `finding` table is now **real findings only** (~11k: synthesis + meanings, was ~309k). (b) **`mti_terms` grounded** — unique per Strong's, status-clean, owned (2,402 active). (c) **`wa_verse_records` unique by `(reference, term_id)`** (58,966 active; XREF dups + orphans cleared). (d) **`word_registry_fk` bypass** (M58) on verse/term tables — **never join through legacy `wa_file_index`**. (e) Mode = `morph_code`/`stem` **columns** (not a finding); language is **morph-authoritative**. **All VE/lexical work is filed + indexed at [`research/VE-lexical/00-INDEX.md`](research/VE-lexical/00-INDEX.md)** (start there). See also `wa-xref-verse-duplication-blocker-*`, and memory `reference_file_index_legacy_use_bypass_fks`, `project_morph_is_source_of_truth`. The VE *values* are migrated as-is — a value rerun/validation is the next phase.

**File:** `database/bible_research.db` (SQLite, **~766 MB**, excluded from Git). Connection pattern: `sqlite3.connect('database/bible_research.db')`; set `row_factory = sqlite3.Row` for dict-like access.

> **Live schema (measured 2026-07-16, schema 3.40.0):** 110 tables · 1177 columns · 105 PK columns · 77 FKs · 6 CHECK constraints · 169 indexes · 4 triggers · 2 views. The full captured schema — every table, column, FK, check, index, trigger and view, each with a description derived from profiling the live data — is at [`iba/config/DBSchema/DBSchema.json`](iba/config/DBSchema/DBSchema.json), rebuilt by `python iba/scripts/build_dbschema.py --db bible_research`. It supersedes `Workflow/schema/database-schema-v*.json` (newest is 3.35.0, 5 versions stale) and `Workflow/schema/create_tables.sql` (stale since 2026-04-19) — both of which also lack PKs, FKs, checks and index columns entirely.

### Table Groups

> **Live model (2026-06):** the primary analytical object is the **`finding`** (one typed term-in-verse finding; 343k rows), organised under the **M-code cluster model** (`cluster` → `characteristic` → `cluster_subgroup` → VCG → verse). The registry is the lexical entry point, not the analytical unit. Full current-state + table-relevancy in [`outputs/markdown/project-reconstruction/`](outputs/markdown/project-reconstruction/) (01, 03).

| Group | Tables | Purpose |
| --- | --- | --- |
| **Finding model (LIVE primary)** | `finding`, `finding_question_link`, `finding_citation`, `finding_verse_link`, `finding_revision` | Universal finding store (M55). VERSE-level findings = L2 verse-read tier findings + meaning; the live unit (340k VERSE · 1.9k CLUSTER · 1k GLOBAL) |
| **Cluster model (M-codes)** | `cluster`, `characteristic`, `characteristic_subgroup`, `cluster_subgroup`, `cluster_finding`, `cluster_observation` | Cluster (M01–M47 + FLAG + T2) → characteristic → sub-group → VCG → verse; `cluster_finding` = catalogue-prompted findings; `cluster_observation` = write-on-discovery |
| **Term/VCG junctions** | `mti_term_subgroup`, `vcg_term` | M:N (M44/M45) — replaced `mti_terms.cluster_subgroup_id` and `verse_context_group.mti_term_id` |
| Registry | `word_registry` | Lexical entry point + **C-code dimension anchor** (`cluster_assignment` = C01–C22); scaffolding under the M-code model (C and M coexist). Carries `phase1_status`, `verse_context_status`, `session_b_status` |
| WA core (term/verse foundation) | `wa_file_index`, `wa_term_inventory`, `wa_term_related_words`, `wa_term_root_family` | Per-term metadata; `term_owner_type` = OWNER \| XREF. Stable foundation (last bulk write 2026-05-14) |
| MTI | `mti_terms`, `mti_term_flags`, `mti_term_cross_refs` | One row per Strong's; `owning_registry_fk` = canonical home; carries `cluster_code` (M-codes). ⚠ OT-DBR-009 duplication unresolved |
| Verse data | `wa_verse_records`, `wa_verse_term_links` | One row per term-in-verse (~230k rows); `span_strong_match` = authoritative usage; `morph_code`/`stem` backfilled |
| Verse Context | `verse_context`, `verse_context_group` | Per-verse classification + groups; `verse_context` carries the L1/L2 fields (`keywords`, `analysis_note`, `pole`, `triage_status`) |
| Meaning parse | `wa_meaning_parsed`, `wa_meaning_sense`, `wa_meaning_stem`, `wa_lsj_parsed` | Structured meaning text |
| Observation catalogue | `wa_obs_question_catalogue`, `wa_finding_catalogue_links`, `wa_flag_type_question_link` | 189-question catalogue; ⚠ being refactored to the two-layer VE/SYNTH catalogue (not yet in DB) |
| Prose store | `prose_section_type`, `prose_section`, `prose_section_fts` (FTS5), link tables | DB-canonical prose (publication parked) |
| Quality / research flags | `wa_quality_flag_types`, `wa_data_quality_flags`, `wa_session_research_flags` | Engine-derived evidence flags + researcher pointers (PH2_*, SD_POINTER) |
| Reference-as-DB registries | `wa_addendum_registry`, `wa_vocab_set`/`_member`, `wa_patch_type_registry`, `wa_file_name_pattern`, `wa_label_pattern` | Governance reference (M32–34). ⚠ stale (last written April), not yet reviewed |
| ~~`wa_rule_registry`~~ | — | **Superseded 2026-08-17** (researcher decision, escalation #696) — all 59 rows (34 previously active) marked `obsolete=1`, `superseded_by='iba.db cfg_* configuration system'`. No longer operational; rules now live in `cfg_*` (`iba/app/GOVERNANCE.md`, `iba\app\ps\Config-Maintenance.ps1 -Step Propose`), not this table. Full review: [`archive/outputs/markdown/wa-rule-registry-full-review-v1-20260817.md`](archive/outputs/markdown/wa-rule-registry-full-review-v1-20260817.md). |
| Engine control | `engine_run_log`, `engine_stream_checkpoint`, `word_run_state`, `term_fetch_log` | Audit trail |
| Reference (static) | `books`, `book_code_variants`, `themes`, `sources` | 66 books + aliases; `themes`/`sources` empty |
| Metadata | `schema_version` | Migration history (→ 3.31.0) |
| **Legacy / superseded** (retained) | `wa_session_b_dimensions`, `wa_session_b_findings`, `wa_finding_entity_links` (old per-word findings → migrate into `finding`); `wa_dimension_index`, `wa_dim_review_cluster_log` (dimension review, eliminated 2026-05-04); `wa_cross_registry_links`, `wa_crosslink_type` (pre-cluster links); `session_d_*` (Session D, **0 rows**) | Superseded by the cluster/finding model; data retained pending disposition (see reconstruction 03) |

### Key Relationships

```text
word_registry (lexical entry point; cluster_assignment = C-code)
  └─ wa_file_index ─ wa_term_inventory ─ wa_verse_records ─ verse_context
mti_terms (owning_registry_fk → word_registry; cluster_code = M-code)
  ├─ mti_term_subgroup ─→ cluster_subgroup ─ characteristic_subgroup ─ characteristic
  └─ vcg_term ─→ verse_context_group
cluster (M-code) ─ cluster_subgroup ─ characteristic ─ cluster_finding
finding (LIVE unit; level=VERSE → verse_context_id + mti_term_id + cluster_code)
  ├─ finding_question_link ─→ wa_obs_question_catalogue
  └─ finding_citation / finding_verse_link
```

### XREF Architecture

- One `mti_terms` row per Strong's, programme-wide.
- `wa_term_inventory.term_owner_type`: **OWNER** = canonical home (verses active, VC processed); **XREF** = cross-reference copy (verses delete_flagged; VC derived from OWNER).
- `verse_context.mti_term_id` is shared across OWNER/XREF copies.
- Scale: ~5,500 OWNER + ~1,500 XREF terms; ~133k active OWNER verses.

### Conventions

- **Strong's:** `H` Hebrew, `G` Greek; suffix letters (e.g. `H7965H`) = sub-entries.
- **Language:** `"Hebrew"` or `"Greek"` (capitalised).
- **Dates:** ISO-8601 UTC (`2026-03-19T18:08:49Z`).
- **Booleans:** INTEGER 1/0.
- **Soft deletes:** `delete_flagged = 1`; no physical deletes in automated flows.

---

## 4. The Engine

> **Superseded 2026-08-17 — provenance only, not live instruction.** Base-layer work moved to IBA;
> see the top-of-file banner and [`iba/app/USER-GUIDE.md`](iba/app/USER-GUIDE.md).

Invocation: `python -m engine.engine [options]`. Source: `engine/`. Audit pipeline runs `audit.py` (WR-01..WR-20: outcome PASS / REVIEW / STOP).

| Mode | Command | Purpose |
| --- | --- | --- |
| AUDIT_WORD | `--mode=audit_word --registry=N` | Unified pipeline: ingest Step 1 JSON, sync DB, run audit (new + existing words) |
| MIGRATE | `--migrate [--dry-run]` | Apply pending schema migrations |
| REGISTER | `--register --word="..." --source="..."` | Add new word to `word_registry` |
| REPORT | `--report --registry=N` | Word overview |
| EXPORT | `--export-word --registry=N` | Export full word JSON |
| EXPORT_REGISTRY | `--export-registry` | Export `word_registry` JSON |

**★ Adding / updating a term — THE authoritative pipeline:** [`Workflow/Instructions/wa-term-add-update-AUTHORITATIVE-pipeline-v1-20260711.md`](Workflow/Instructions/wa-term-add-update-AUTHORITATIVE-pipeline-v1-20260711.md) — read it before any term work; it enumerates every field written to every table. The whole flow is **3 commands**: `--register` (if new) → `word_study_extract.py --word X` → `--mode=audit_word --registry=N`. **`audit_word` auto-creates the `wa_file_index` stub** and inserts + span-links terms and verses in one pass. **`new_word.py` is RETIRED (deleted 2026-07-11); `gap_fill.py` superseded** — do not use either. (This corrects the old 2026-06-15 caveat that claimed audit_word does not create file_index — it now does.)

**Common flags:** `--dry-run`, `--force`, `--interactive`, `--skip-span-backpop`, `--extract-file=PATH`.

**Constants (`engine/constants.py`):** `EXPECTED_SCHEMA_VERSION = "3.33.0"` · `LOCK_SENTINEL = "In Progress"` (title case, matches stored data) · `HIGH_FREQ_THRESHOLD = 500` · `THIN_DATA_THRESHOLD = 20` · `BACKUP_RETENTION = 10` · `STALE_LOCK_SECONDS = 7200`.

Detailed engine architecture and audit-check enumeration: `docs/Session-A-v9-Architecture-*.md`.

---

## 5. STEP API Client

> **Superseded 2026-08-17 — provenance only, not live instruction.** Base-layer work moved to IBA;
> see the top-of-file banner and [`iba/app/USER-GUIDE.md`](iba/app/USER-GUIDE.md).

`scripts/analytics/step_client.py` against local STEP server (`http://localhost:8989`). Methods: `get_vocab_info`, `get_verse_records`, `get_verse_records_with_html`, `get_strongs_for_word`, `get_related_term_cluster`, `extract_word_data`. STEP caps results at 60; client uses canonical section splits (Torah/History/Poetry/Prophets/NT, halved if needed) for full coverage. Detail: `docs/step_setup.md`.

---

## 6. Script Conventions

| Prefix | Behaviour | Safe? |
| --- | --- | --- |
| `_assess_*`, `_check_*`, `_discover_*`, `_explore_*`, `_probe_*`, `verify_*`, `inspect_*` | Read-only diagnostics | Yes |
| `_apply_*`, `_repair_*`, `_realign_*`, `_reset_*`, `_extract_*`, `_batch_extract.py` | Modify DB | **No** |
| `_delete_*` | Remove rows | **No** (destructive) |
| `_tmp_*` | Throwaway ad-hoc | Varies |
| `apply_session_patch.py` | Apply Session/VC/REPAIR JSON patches | **No** |
| `build_*`, `generate_*`, `export_*`, `_produce_*`, `_generate_*`, `word_*_extract.py`, `_exploratory_*` | Read-only reports/exports | Yes |

For full file lookup: `iba\app\ps\Manifest-Search.ps1 -Query "..."` (`scripts/build_file_manifest.py` retired 2026-08-18, escalation #730).

---

## 7. Word Study Pipeline

> **Superseded 2026-08-17 — provenance only, not live instruction.** Base-layer work moved to IBA;
> see the top-of-file banner and [`iba/app/USER-GUIDE.md`](iba/app/USER-GUIDE.md).

Three-phase term workflow (Phase 1 discover → Phase 2 decisions → Phase 3 DB sync): `_discover_word_terms.py` → `_apply_term_decisions.py` → `_extract_word_terms.py`. For a quick STEP pull without the full pipeline: `word_study_extract.py --word <english> [--anchors H1234,G5678]`.

---

## 8. Data Flow

> **Superseded 2026-08-17 — provenance only, not live instruction.** Base-layer work moved to IBA;
> see the top-of-file banner and [`iba/app/USER-GUIDE.md`](iba/app/USER-GUIDE.md).

```text
Phase 1 (STEP + audit_word) → Verse Context → Session B (DataPrep → pool Analysis → Extraction) → Session C → Session D
```

All Claude AI output → JSON patch → `python scripts/apply_session_patch.py` (validates and writes). **Never import raw Claude output directly.**

**Patch types:** PREANALYSIS · SESSIONB · SESSIONB-COMPLETE · ANALYSIS · VERSECONTEXT · VCGROUP · VCVERSE · SDPOINTERS · REPAIR · SESSIOND · CLUSTERING · DIMREVIEW.

**Engine export** (STEP format): `python -m engine.engine --export-word --registry=N` → `Sessions/Session_A/STEP Extracts/...`.
**Complete extract** (Session B/C format, 9 layers): `python scripts/build_complete_extract.py --registry=N` → `Sessions/Session_C/Session C/...`. Scope `full` (pre-analysis) or `final` (post-analysis); version auto-increments per day.

Detail: `wa-patch-instruction [current]` (patch ops, REPAIR catalogue, failure protocol) · `wa-versecontext-instruction [current]` (VC batch construction, R1–R4 validation, status advancement) · `wa-sessionb-analysis-readiness [current]` and `wa-sessionb-analysis-output [current]` (Session B Stage 1/2) · `wa-registry-management-guide [current]` §7a (pool IDs and pool-readiness logic) · `wa-sessiond-orientation [current]`.

---

## 9. Interaction Protocols (`docs/interaction-preferences.md`)

1. **Instruction Confirmation:** Before non-trivial tasks — summarise, state approach, WAIT for approval.
2. **Output & Workings → `.md` Always.** All outputs and workings (analysis, plans, decisions, intermediate results, reports) must be written to a `.md` file in `docs/`, `outputs/`, or a relevant subfolder. Chat is for **alerts and brief summaries only** — every substantive deliverable in chat must include a link to the `.md` file that holds the full content. Never present final output only in chat.
3. **Factual Discipline:** Work with explicit facts. Don't guess. Stop and ask if unclear.
4. **File Organisation & Versioning:** Follow `docs/file-organisation-rules.md`. **Same-name = version bump:** if a file with the same base name already exists (regardless of date), the new file must carry an incremented `-v{n}` suffix (integer, no leading zero). This applies even within the same day — a revised report produced later the same day becomes `-v2-`, the next revision `-v3-`, and so on. Archive superseded versions promptly. Never overwrite a prior version in place.
5. **Manifest Maintenance:** Run `iba\app\ps\Manifest-Rebuild.ps1` after session-log processing or batch file moves — **retired 2026-08-18** (escalation #730): `scripts/build_file_manifest.py` → `archive/scripts/`; `database/file_manifest.json` → `database/archive/` (frozen 2026-08-15 snapshot). The live manifest is IBA's `file_manifest` DB table (`USER-GUIDE.md` §13a).
6. **Cost Awareness:** Cost is a real constraint. Where a task can be done more cheaply without sacrificing the outcome, advise the cheaper path **before** acting. Flag: (a) Opus on routine pipeline work; (b) whole-file reads when targeted Read/Grep would suffice; (c) subagents when a direct query is enough; (d) duplicate artefacts; (e) `--dry-run` then `--live` for routine patches; (f) ad-hoc scripts duplicating existing reports. Detail: [`outputs/markdown/cost management 20260426.md`](outputs/markdown/cost%20management%2020260426.md).

---

## 10. Document Architecture

Documents in `Workflow/Instructions/`. **All operational cross-references use the `[current]` token** — resolve to highest-numbered version at read time. Pin specific versions only for provenance (Supersedes fields, patch metadata). (Originally codified as `GR-REF-002` in `wa_rule_registry` — that table is superseded 2026-08-17, see §3; the convention itself is unaffected, defined here directly.)

| Document | Audience | Purpose |
| --- | --- | --- |
| wa-claudecode-instruction | Claude Code | CC responsibilities: patch/directive execution, VC batch ops, extracts |
| wa-patch-instruction | Claude Code | Patch preparation + execution: ops, REPAIR catalogue, failure protocol, validation |
| wa-directive-instruction | Both | Directive specification (5 required elements, validation, execution) |
| ~~wa-global-general-rules~~ | — | **Superseded 2026-08-17** — was the compiled export of `wa_rule_registry` (GR-REF-002, GR-FILE-003, GR-OBS-001, etc.), now entirely `obsolete=1`. Rules now live in `iba.db`'s `cfg_*` system (`iba/app/GOVERNANCE.md`). |
| wa-global-flags | Both | Standalone flag tracking (FLAG-010 = blocking gate) |
| wa-reference | Both | Controlled vocabulary, schema reference, file naming, validation standard |
| wa-registry-management-guide | Both | Registry structure, OWNER/XREF, dual status, clusters, pools (§7a) |
| wa-sessionb-analysis-readiness | Both | Session B Stage 1: data audit + remediation. Hard gates: VC/DimReview/B-target |
| wa-sessionb-analysis-output | Both | Session B Stage 2: 2a analysis · 2b Q&A + Type b patch · 2c analytic word output |
| wa-sessionc-instruction | Claude AI | *(superseded by cluster model — see wa-sessionc-cluster-overview)* Per-word Session C, retired 2026-05-12 |
| wa-sessionc-cluster-overview | Both | Session C cluster publication: end-to-end process, shared style, 7 chapter instructions, appendices instruction, assembler. Entry point for cluster publication |
| wa-sessiond-orientation | Both | Session D: pointer clustering, question formulation, evidence retrieval, analysis |
| wa-dimensionreview-instruction | Both | Dimension review (Phase A/B/C) |
| wa-versecontext-instruction | Both | Verse Context: batch construction, classification, validation, status advancement |
| wa-word-study-template | Claude AI | Word study output template |

### Current Programme State (2026-06-14)

> ⚠ This compact reference can lag the written record. The **authoritative current state** is the manifest-driven reconstruction in [`outputs/markdown/project-reconstruction/`](outputs/markdown/project-reconstruction/) (01 status · 02 failures · 03 table-relevancy · 04 open-loops) and the fan-out map [`docs/project-orientation-core-memory-map.md`](docs/project-orientation-core-memory-map.md). Live-model instruction docs (v3_2 rollup, verse-analysis methodology, tier catalogue, study foundations) are listed there.

- Schema **v3.31.0** (live; M55 L2-finding system, 2026-06-08).
- **Live model:** L1/L2 **"verse-read = meaning"** → `finding` (340k VERSE-level). L3–L8 synthesis/distillation **parked** until more clusters accumulate. The **v3_2 cluster-rollup instruction is DRAFT** (open item B3); the catalogue refit (two-layer VE/SYNTH) is approved but **not yet applied to the DB**.
- **215 registries** — session_b_status: 160 Verse Context Reset · 12 Analysis Complete · 43 NULL; verse_context_status: 172 Complete · 1 In Progress · 42 NULL.
- **49 clusters** (M01–M47 + FLAG + T2): 30 Not started · 13 Analysis Completed · 3 Analysis Completed (Terms Added) · 2 Structurally Ready · 1 Ready for re-analysis. M01 (Fear) + M15 (Wisdom) verse-read 100%. **128 characteristics.**
- ~~**Cluster-rework phase active from 2026-06-05** — new output → `Sessions-v2/{CODE}-{Name}/`~~ — **superseded 2026-09-28:** cluster output → `_analytics/Clusters/{code} - {short name}/` (`cfg_setting report.cluster_folder_naming_convention`, GOVERNANCE.md §83); old `Sessions/` read-only cross-reference.
- **DB loss 2026-06-03** recovered to a 2026-05-28 copy (~6 weeks lost); project off Google Drive, NAS + git backups (§13).
- Registry/cluster duality: `word_registry.cluster_assignment` = **C-codes** (C01–C22, dimension-review layer, retired but data retained); the live analytical layer is the **M-code `cluster` table**. Both coexist — C-codes are scaffolding, not dead.
- Open: **OT-DBR-009** (mti_terms dedup) unresolved; `wa-programme-open-items.md` (127 items) currency uncertain post-pivot; science extracts not yet in DB; ~12 docs silently superseded (reconstruction 04 §4).

---

## 11. Common Operations

```bash
# Engine
python -m engine.engine --db-status
python -m engine.engine --migrate
python -m engine.engine --check-locks
python -m engine.engine --clear-lock --registry=N
python -m engine.engine --mode=audit_word --registry=N
python -m engine.engine --report --registry=N
python -m engine.engine --export-word --registry=N
python -m engine.engine --export-registry

# Patches
python scripts/apply_session_patch.py [--dry-run] <patch.json>

# Reports & extracts (read-only)
python scripts/_generate_programme_report.py
python scripts/generate_registry_overview.py
python scripts/generate_programme_snapshot.py [--registry-only|--strongs-only] [--out PATH] [--date YYYYMMDD]
python scripts/build_complete_extract.py --registry=N [--complete-only|--owner-only]
python scripts/build_correlation_extract.py
python scripts/build_dimension_extract.py --cluster|--pointers|--rootfamily C17
python scripts/_exploratory_sessionb_export_v1_20260415.py --registry=N
python scripts/export_database_schema.py

# File manifest (rebuild + search) — retired 2026-08-18 (escalation #730), now IBA-governed
iba\app\ps\Manifest-Rebuild.ps1
iba\app\ps\Manifest-Search.ps1 -Query "grace"
iba\app\ps\Manifest-Search.ps1 -Query "registry:68"
iba\app\ps\Manifest-Search.ps1 -Query "type:observations"

# STEP discovery (no DB writes)
python scripts/word_study_extract.py --word anger --anchors H2734

# Integrity
python scripts/_integrity_full_check.py
```

DB connection pattern for ad-hoc scripts:

```python
import sqlite3, os
conn = sqlite3.connect(os.path.join('data', 'bible_research.db'))
conn.row_factory = sqlite3.Row
```

Programme-state SQL queries (Session B progress, VC progress, OWNER terms needing VC, pool readiness, cluster progress, ownership distribution): `wa-claudecode-instruction [current]` §6.6.

---

## 12. Git

- Excluded: `database/bible_research.db`, `backups/`.
- Committed: `Sessions/Patches/*.json`.
- **No direct GitHub publishing (2026-10-04, #1941; GOVERNANCE.md §86).** This project never publishes a site to GitHub. The inner-being narrative reaches learning4comfort only through `iba\app\ps\Copy-NarrativeToLearning4Comfort.ps1`, which copies the current files to `C:\learning4comfort\publication-inbox	he_inner_being`. Run it when a section of work is complete, on request, and at every `/session-close` (step 6a). `cfg_setting governance.no_direct_github_publish`.
- Commit message: `session YYYYMMDD: brief description`. Branch: `main`. Remote: `github.com/lcilliers/Bible_Projects`.
- **Standing pre-authorization (2026-07-23, scope widened 2026-08-10, widened again 2026-09-24):**
  completing a session log (any `SESSION-LOG-*.md`, including `iba/app/SESSION-LOG-*.md`) **OR**
  completing a `/session-close` cycle (`.claude/commands/session-close.md`, escalation #1875/#1876)
  means the full commit-and-push cycle happens in the same unit of work — write a proper commit
  message, commit, push, confirm `git status` clean/pushed. This is the standing exception to
  "never commit unless explicitly asked" (§ system instructions) — narrowly scoped to these two
  triggers, not a general license to commit proactively elsewhere. Mirrors
  `governance.build_md_on_code_change` in `iba/app/` (same shape of rule, same day it was first
  set). Config-driven: `governance.session_log_triggers_commit` (`cfg_setting`, module
  `governance`) is the live source of truth this text documents, per
  `governance.governance_md_on_rule_change` — applied via `Config-Maintenance.ps1 -Step Propose`,
  escalation #1876, researcher direct instruction this chat: *"ensure that the session-close will
  activate the commit rules also."*
  **Default scope, corrected 2026-08-10:** stage every outstanding change in the working tree at
  close, not only the changes made during the current session — a prior narrower reading (session-
  own changes only, everything else left for a separate pass) required a follow-up "(cont.)"
  catch-up commit twice (2026-08-09, 2026-08-10); the default is now the full diff. Still not a
  blanket `git add -A` performed blindly: read anything unfamiliar before staging it (per the
  standing "read before publishing/distributing" rule) and still exclude the standing binary/log
  paths above (`database/bible_research.db`, `backups/`) — but do not filter files down to "did I
  personally generate this" as a routine step.

---

## 13. Environment

- Windows 11; working directory `C:\Bible_study_projects` (moved off Google Drive 2026-06-03 after a Drive sync event corrupted the DB + `.git`; see `archive/outputs/markdown/wa-db-loss-incident-20260603.md`). Off-Drive backups to NAS `\\LSUK-SYNRACK\HomeMedia\bible_study_projects\`: (a) **DB** → `db_backups\` (daily 18:00 task `BibleResearch DB Backup to NAS`; `scripts/backup_db_to_nas.py`); (b) **full folder + memory mirror** → `mirror\` + `claude-backup\` (daily 18:30 task `BibleResearch Full Mirror to NAS`; `scripts/mirror_to_nas.ps1`, robocopy /MIR). Project memory is also committed to git under `memory/` (mirror of the `.claude` memory). Old `G:\My Drive\Bible_study_projects` retained as a fallback only.
- Python 3.14.0 · PowerShell 7+ (`$env:PYTHONUTF8="1"`).
- STEP Bible local server at `http://localhost:8989`.
- Secrets in `.env` (ZOTERO_API_KEY, ZOTERO_USER_ID, STEP_BASE_URL).

---

## 14. Controlled Vocabulary (most-referenced)

**`word_registry.session_b_status`:** NULL · `Verse Context Reset` · `Ready for Analysis` · `Pre-Analysis Complete` · `Analysis Complete` · `Session B Complete`.

**`word_registry.verse_context_status`:** NULL · `In Progress` · `Complete`.

**`wa_term_inventory.term_owner_type`:** `OWNER` | `XREF`.

**`mti_terms.status`:** `extracted` · `extracted_thin` · `extracted_theological_anchor` · `candidate_delete` · `delete` · `excluded` · NULL.

**`wa_session_research_flags.flag_code`:** `PH2_*` · `SB_FINDING` · `SB_DIMENSION` · `SB_INNER_BEING` · `SD_POINTER` · `SD_CLUSTER` · `CANDIDATE_REGISTRY_WORD` · `VOLUME_LIMITATION`.

**Evidence flags (post-M29, informational only):** `VERSE_EVIDENCE_MINIMAL` · `_CONCENTRATED` · `_HIGH` · `_BREADTH_NOTE`.

**Researcher-authored fields (pipeline must not overwrite):** `word_registry.inference_note` · `word_registry.word_synopsis`.

Full vocabulary, schema reference, evidential-status enum, dimensional-weight enum, dropped/retained-fields catalogue, full patch operation list: `wa-reference [current]` and `wa-patch-instruction [current]`.
