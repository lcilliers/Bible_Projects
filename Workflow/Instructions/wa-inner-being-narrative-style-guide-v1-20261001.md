# Inner-being narrative: style, format and evidence guide (v1)

**Date:** 2026-10-01 · **Author:** Claude Code, compiled for the researcher · **Status:** authoritative for all IBA-line narrative writing (escalation #1921). Config pointer: `cfg_setting narrative.inner_being_style_guide_path` (proposed via Config-Maintenance, approval-gated).
**Researcher direction (verbatim, 2026-10-01):** *"A while ago we compiled a guide for style and format for narratives - check the workflow folder for the instructions to write prose/essay/publish etc - you may need to re-introduce those guidelines for iba writing and include it in the configs."*

## 0. What this governs, and where it came from

It governs every piece of reader-facing prose in the IBA line:
- the chapter files of *Inner Being in Operation* (`_analytics/essay/spirit_soul_body/inner-being-narrative/`)
- any later book narrative, strand write-up or published essay

It does **not** govern working files (ledgers, registers, investigations), which may use project terms.

It re-introduces the earlier guides and reconciles them with the researcher's later rulings. **Where an earlier guide and a later ruling differ, the later ruling governs**, and the difference is shown in §10.

| Source | Date | What is carried forward |
|---|---|---|
| `Instructions/archive/wa-global-sessionc-prose-rule-v1_1-20260414.md` | 2026-04-14 | Derive only from the evidence; the gap corollary; the insight caveat; the five prohibited patterns |
| `Instructions/archive/wa-sessionc-cluster-style-method-v1_1-20260512.md` | 2026-05-12 | Voice and tone; words to avoid; citation discipline; the silence principle; reverse audit; self-review |
| `Instructions/archive/wa-cc-cluster-essay-style-template-v1_0-20260620.md` | 2026-06-20 | Completeness ("do not omit findings for simplicity"); plain quantifiers; no project superlatives |
| `Instructions/wa-narrative-style-instruction-v1-20260702.md` | 2026-07-02 | Testimony, not report; every clause grounded; "a claim with no citable ground is not written"; convergence as warrant |
| `Instructions/WA-inner-being-narrative-guidance-v1-2026-07-28.md` | 2026-07-28 | The three channels (non-human, human, physical world) |
| `Instructions/WA-inner-being-narrative-hard-constraints-v1-2026-07-30.md` | 2026-07-30 | Nothing invented; open threads stay open; contradictions stand; no forced unity; general-reader language; no self-reference |
| Researcher rulings, 2026-09-30 to 2026-10-01 (CLAUDE.md banners; #1912, #1913, #1916, #1918, #1919, #1921) | | The current frame, voice, weave and change-of-character rules, and *let Scripture speak for itself* |

## 1. The governing rule: let Scripture speak for itself

**Researcher, verbatim (2026-10-01):** *"you are bordering on imputing meaning that is not supported by the verses. don't drive synergy and phantom observations into the findings. Rather allow scripture to speak for itself."*

The same rule appears in every earlier guide:
- "must not introduce new analytical claims at the writing stage" (prose rule, 04-14)
- "no imported meaning that is not in the data" (07-02)
- "Nothing invented" (07-30)

**What it means in practice:**
1. A sentence may **state what a verse or passage says**, quote it, and set it beside another verse that says something related.
2. A sentence may **not** join verses into a pattern, mechanism, division of labour, cycle, or "what this shows" that no verse states. Examples withdrawn on 2026-10-01:
   - "spirit for the rising, heart for the keeping"
   - "the path is a circle"
   - "anger is what happens in the place of breath"
   - "the hand does not change, only where a person stands"
3. A narrator's reading ("I read this as…") is allowed **only** where it restates or paraphrases what the cited text itself says. It is **not** a licence for synthesis.
4. **When in doubt, quote and stop.** Let the reader see the verses side by side.
5. **A new insight found while writing is not written as prose.** It goes into the strand ledger as an observation for the researcher to see. Only then may it be written, and only as the verses carry it. (This is the insight caveat of 04-14.)

## 2. The five prohibited patterns (04-14, still in force)

| Pattern | Example of the fault | What to do instead |
|---|---|---|
| **Literary framing without source** | "Lam 3:22 is not optimistic sentiment but defiant confession" | Render the verse; drop the framing |
| **Superlatives not counted** | "the clearest picture", "the feeling Scripture traces most fully", "most often" | Omit, or state the count you actually made and its scope |
| **Comparative claims without evidence** | "the NT develops this more deeply than the OT" | Omit the comparative half |
| **Premature closure** | "this verse settles the question" | Present it as evidence; the question stays open |
| **Claims that conflict with the data** | wrong verse, wrong word, wrong sense | Check against the ESV in iba.db `verse` and the strand ledger; correct the source first |

## 3. Voice

- **First person, personal, direct, easy to read** (researcher, 2026-09-30). "I", not "we".
- **Testimony, not report** (07-02): grounded and morally serious, never clinical. Reverent without being devotional; no sermon, no liturgical phrasing.
- **Plain, short declaratives.** No padding, no throat-clearing, no signposting the reader does not need.
- **Confident where the verse is plain, and open where it is open.** Do not hedge plain evidence ("perhaps", "it could be argued"). Do not resolve what the text leaves open: say "the text does not say", "we are not told why".
- **General reader** (07-30): someone who has never studied Hebrew or Greek, and has no interest in how the work was done.

## 4. Words and terms

**Never in chapter text:**
- cluster, M-code, characteristic code, tier, phase, batch, strand, stream, ledger, node, observation, finding, Strong's number, VCG, sub-group, seat-sense, "this study found", "the debates", "our analysis"
- anything describing how the work was done

| Instead of | Write |
|---|---|
| finding, observation | "the verses show", "Scripture says" |
| seat, inner seat | "heart", "soul", "spirit", or "the inner word" |
| valence | "commanded", "forbidden", "good", "evil", in plain terms |
| raw counts ("973 of 975") | plain quantifiers ("in almost every instance", "the single exception"), **and only if counted** |

**Hebrew and Greek words** always appear with their gloss (cfg_method_rule `translit-never-without-gloss`), e.g. *ʾaph*, "nostril, anger".

## 5. Evidence and citation

- **Every claim rests on a cited verse.** "A claim with no citable ground is not written" (07-02).
- **Quotations are ESV.** Every quotation is checked mechanically against iba.db `verse` before a file is committed. Note the gaps by design (#1891).
- **Reference style:**
  - the full book name in chapter text ("Proverbs 15:1")
  - verse numbers alone after the first reference to a chapter ("(15:18)")
  - several witnesses separated by semicolons
- **A lone occurrence is stated as such.** Convergence across verses is what lets a point stand as a point (07-02).
- **Open threads stay open, and contradictions stand side by side** (07-30). Where two passages pull opposite ways, both are shown.

## 6. Silence

Name a silence **only when it carries weight**: an expectation set and then not met, or an absence that gives the thing its shape. A routine absence needs no comment. Silences are not listed as an inventory (05-12).

## 7. Structure and format

- **The book's shape follows the evidence**, not a template:
  - weave, don't fit (#1918)
  - a strand is woven through the chapters it touches and never given a chapter of its own (#1920)
  - Part 10 is organised by activity; Ch 11 holds patterns, and §4 holds the account of what changes a word's character (#1919)
- **No fixed sub-headings** in an activity section. The shape of each comes from its verses (weave method §3.2). Each activity file ends with **Connections**.
- **Change of character** is recorded and woven for every word or concept with more than one face, with the circumstances and the *why* as the verses give them (#1919). It is never taken from a cluster tag.
- **Held material** stays in a marked *Held* working note at the foot of a chapter until it is checked.
- **Lists:** bullets are used today for lists of verses and short parallel items. See §10, item 1: open for the researcher.

## 8. Before a file is committed: the checks

1. **Reverse audit (coverage).** Every ledger observation the file is meant to carry is present, or its absence is justified. For each strand: every observation's key verse is present somewhere in the narrative.
2. **Let-Scripture-speak pass.** Read every "I read / I take / I find / I notice", every "so", "therefore", "this shows", every superlative, and every sentence that joins two verses into a claim. Keep it only if a cited verse says it. Otherwise cut it back to the verses.
3. **Quote check.** Every quotation is matched against the ESV text in iba.db.
4. **Self-review** (05-12):
   - repetition
   - overreach (a claim that goes beyond what the cited verse carries)
   - padding
   - tonal drift (devotional phrasing, project words)
5. **Records:**
   - version bump (prior version to `archive/`)
   - claim register entry for every changed statement of the narrative
   - index Structure log and version map
   - escalation updated

## 9. Where things go

- **Chapter drafts** are files, not DB prose rows. The DB prose store's rule is unchanged: Claude does not write prose to the DB without a specific instruction (CLAUDE.md).
- **Working material** goes beside its sources (weave method §2.1): strand ledgers, the claim register, change-of-character tables.
- **Anything to be decided** goes in a `.md` file and an escalation, in plain chat. Never AskUserQuestion.

## 10. Differences between the guides, and how they are settled

| # | Earlier guide said | Later ruling / current practice | Settled? |
|---|---|---|---|
| 1 | "Essayistic, continuous prose, not bullet lists" (05-12, 06-20) | The chapters use many bulleted verse lists | **Open, for the researcher.** Current practice continues until you rule. Option: keep bullets only for verse lists, and write argument as prose |
| 2 | Third person; avoid "we" (05-12) | "Voice is first person, personal, direct" (researcher, 2026-09-30) | **Settled by the later ruling:** first person singular; still no "we" |
| 3 | Structure by the eight tier lenses (06-20) | Fan-out and weave by activity (#1900, #1918) | **Settled by the later ruling** |
| 4 | "The view from outside Scripture": bring in general science (06-20) | "Science chapters will be done later" (researcher, 2026-09-30) | **Settled:** no science in the current chapters |
| 5 | The story is saved to the prose tables (07-02) | Narrative drafts are files; no DB prose without instruction (CLAUDE.md) | **Settled by the later ruling** |
| 6 | Every narrative closes with a three-channel "Scope self-check" (07-28) | Written for book narratives generated from passage debates; the chapters have no such section | **Open, for the researcher.** Option: run the three-channel check on each **strand ledger** (non-human, human, physical world), not as a section in the chapter text |
| 7 | "Confident, not hedging" (05-12) | "Open threads stay open" (07-30) | Compatible: confident where the verse is plain, open where it is open (§3) |
| 8 | Insights found while writing become database observations through patches (04-14) | Observations live in iba.db `ib_observation` (#1912 banner); strand work is captured in ledgers per strand | **Settled:** an insight goes to the strand ledger first (§1.5). Capture to `ib_observation` follows the focused-capture rule |

## 11. Change history

- v1, 2026-10-01: compiled from the six earlier guides and the researcher's rulings (#1921).
