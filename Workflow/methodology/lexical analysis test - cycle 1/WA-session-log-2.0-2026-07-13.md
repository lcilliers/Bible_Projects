# WA — Session Log (FINAL): Corpus Remediation, First Explorations, and the Rule-Base Reckoning

**File:** WA-session-log-2.0-2026-07-13.md
**Date:** 2026-07-13
**Version:** 2.0 — **final for this session. Supersedes v1.0 and v1.1** (both were written mid-session and are now substantially wrong; see Part C).
**Author:** le Roux Cilliers

**Outputs produced this session:**
| file | status |
|---|---|
| `WA-explore-inner-seat-heart-soul-spirit-1.0` | live — **but §2 must be split; see C2** |
| `WA-explore-other-uncategorised-1.0` | live |
| `WA-explore-E4-direction-target-prelim-1.0` | live — **recast; see C1** |
| `WA-assess-raw-source-json-1.1` | live |
| `WA-rulebase-reconciliation-1.0` | live — **the pivotal document of this session** |
| `WA-analytic-input-spec-2.0` | live — **the deliverable for CC** |
| `WA-projection-spec-1.0 / 1.1 / 1.2` | **superseded** by the above |
| `WA-session-log-1.0 / 1.1` | **superseded by this** |

---

## PART A — THE ARC OF THE SESSION

Four movements, each of which changed what the next one could be.

### A1. The corpus was broken, and its controls could not see it

The session opened with a request to read and summarise a 206,000-word narrative corpus. Instead it found:

- **The file's structure did not match its description** — flat H2 blocks, theme encoded in the filename, no Scripture references anywhere (1 stray in 206,000 words), no lemmas.
- After regeneration: **549 sections — 26.8% — had silently vanished.** Paragraph-level diff proved it was pure subtraction: every surviving paragraph verbatim from the source, 549 gone, nothing added. Loss ran across 43 of 46 themes, heaviest where it mattered most (`praise-extol-sing` −44%, `inner-seat` −38%).
- **The two supplied controls contradicted each other.** `StoryCount` = 2,048. `InputH2` = 1,499. The validation file reported **`Diff = 0` on all 46 rows** — because it compared output headings against input *headings*, never against input *stories*. **The one control holding the true figure was never compared to anything.**

The mechanism was then established, not hypothesised: of the 549 dropped stories, **372 sat immediately after a kept story at a source-line distance of 12–16 lines** — the next paragraph under the same heading. The generator emitted one H3 per H2 and carried only the **first** story under each.

**Resolved.** A new control (`StoryMarkers`) measured the right thing; the regenerated corpus verified sound three independent ways: 2,048 sections, per-theme match on 46 of 46, paragraph diff 0 lost / 0 added.

### A2. Two themes read exhaustively

**E1 — `inner-seat-heart-soul-spirit`, all 167 sections.** The corpus systematically declines to localise: **132 of 167** state the psalm does not say *where inside a person* the movement sits — in the theme named for the seats. Flesh, body and bones sit *inside* "inner-seat"; *"my heart and flesh sing for joy"* is recorded twice, once from each `[Psa 84:1-12 | #1, #2]`. No seat has a fixed function — spirit is right, willing and broken in one psalm.

**`other-uncategorised`, all 55 sections.** Not leftovers. Three coherent subjects with **no family in the arrangement at all**: justice-and-office, idolatry, the human condition. And the corpus's densest concentration of the *"same word bent to opposite ends"* device — 9 of the corpus's 28 instances in 2.7% of the sections.

*(The offcut of a classification tells you where the classification was cut. Read the offcut first, not last.)*

### A3. E4 preliminary — direction

Three transitive themes read exhaustively (`seeking-inquiring` 35, `lifting-bearing` 21, `being-heard-listening` 20). The corpus **states the principle outright**:

> *"The same rising motion that is beautiful when the soul reaches up to God becomes pride when it reaches up for itself"* `[lifting-bearing | Psa 131:1-3 | #1]`

One verb, two objects, opposite outcomes, marked as opposites *within a single psalm* `[Psa 63:1-11 | #2]`. The identical deliberate act — stopping one's own ears — righteous in `[Psa 38:1-20 | #1]`, damning in `[Psa 58:1-5 | #1]`.

**Hypothesis:** direction may not be one edge among nine but **the edge that constitutes the movement**.

### A4. The rule base arrived, and overturned four of my conclusions

The researcher supplied the authoritative instruction set. It falsified four structural claims I had drawn from the emitted artefacts — see Part C. Most importantly:

> **Direction was never missing. It is the pair — `from_span → to_span` — and the position in the pair is significant.**

The model already held the edge E4 had "discovered." The session's final act was to rebuild the analytic-input specification from the rule base rather than from the artefact.

---

## PART B — THE DEBATE, AND WHAT WAS ARGUED

### B1. Whether to read a corpus known to be 27% short

The pull to proceed was live at three separate points. The file was there, the researcher had asked, and a partial read would have produced a fluent, plausible summary.

It would also have been a summary of a corpus missing its later movements under every multi-story passage — so any pattern drawn from it would have been, in part, **a pattern about which story happened to be written first**.

**Position taken: refuse.** The documented failure mode — *optimising for completing-and-presenting over correctness under volume pressure* — does not announce itself as a temptation to cut corners. **It presents itself as helpfulness.**

### B2. Whether the residual bucket was worth reading

It was proposed as hygiene: small, cheap, uninteresting. It produced two of the session's best findings.

### B3. Whether to read the story or the evidence first

Settled on evidence: **CSV → technical narrative → story.** The story layer is a lossy and in places misleading derivative (C3). Reading it first anchors the analysis on its conclusions, including the unsound ones. **Where the layers diverge, that is a finding.** Two divergences from a single family, both substantive.

### B4. Technical narrative vs prose story — decided on measurement, not preference

Across 39 records of `psalms__wisdom-folly-teaching__narratives.json`:

| layer | **record** vocabulary (*"absent"*, *"no origin is booked"*) | **Scripture-silence** vocabulary (*"the passage never tells us"*) |
|---|---|---|
| `narrative` | **39 / 39** | **0 / 39** |
| `story` | 0 / 39 | **8 / 39** |

**The technical narrative is honest. The story launders design decisions into claims about Scripture.** Decision: work against the narrative.

---

## PART C — CORRECTIONS TO MY OWN CLAIMS (the substance of this log)

Five claims made this session were wrong. All were made by reading the emitted artefact without the rule that governs its production.

### C1. **"`direction` is never populated"** — WITHDRAWN

Cycle §3: *a dimension value is a VALUE, a **PAIR (`from_span → to_span`)**, an EVENT, or a FLAG.* **The pair is the directed edge.** I called it missing because the emission shows `to_span` on 49 of 176 rows and `from_span` on 4.

**Consequence:** E4 stops being a *proposal* and becomes a **validation** — *does the recorded pair structure bear out what the narratives assert about direction?* Answerable mechanically from the pairs, **provided both endpoints are emitted.**

### C2. **"`source`, `intensity`, `effect` were never recorded — the declared silence is unsupported"** — SPLIT IN THREE

- **`source` (103) and `effect` (111): WITHDRAWN.** Method §14 — for poetic genre, *"cross-verse items OFF (source-across-verses / effect / process would be noise between poetic lines)."* **Deliberate, reasoned, documented.** Not a gap.
- **`intensity` (109), `prohibition` (113), `specifier` (110): STANDS.** §14 has all three **ON** for poetic. All three are `present: false`. Real gap.
- **And the consequence is worse than my original claim.** Every `inner-seat` narrative closes with *"does not tell us how strong it was, or how it finally turned out."* **"How strong"** = intensity — never tested. **"How it turned out"** = effect — **deliberately not read.** The narrative reports a **methodological decision as a property of Scripture.**

**E1 §2 must be split:** seat-silence is evidenced and sound; intensity-silence is untested; effect-silence is a design decision misreported.

### C3. **"`type` may be a faculty bin under another name"** — WITHDRAWN
Cycle §3: `102 type` is *"✅ derivable (sub-gloss; POS)"*. Morphology-derived. Unfounded.

### C4. **"`H2603` is fragmented by English gloss"** — WITHDRAWN
§7D v3: lemma-keying merges meanings (halal → praise/boast/deride); stem alone is insufficient; the read-sense over-splits. **The ESV rendering is a validated proxy for meaning-in-context, cross-checked by stem/morph** — adopted after the alternatives were tried and found wanting. The evidence columns (`stems`, `morph_codes`, `esv_words`) are **already mandatory** in `ib_characteristic`; they are simply **not emitted**.

### C5. **"At least three generations of story"** — CORRECTED
**Two, radically lopsided.** A full marker map across all 46 themes: `inner-seat` alone (8%) has the structured template; **all 45 other themes have 0% of every marker.**

### C6. CONFIRMED and strengthened — **`seat: "none"` is a genuine reader determination**
P4 defines `none/silent` as the explicit *"looked for, found nothing"* state, distinct from `unresolved`. `seat` = `none`, `resolution: none`, **16 of 16**. **E1's headline finding has a rule-based warrant. It remains the strongest finding of the session.**

### C7. SHARPENED — **`discovery` (114) is not running as the emergence engine**
P8 requires *"discovery: none"* when nothing is flagged — *"so we know it was looked for, not skipped."* **Populated 16/16; `none` appears zero times.** Its content is a sense-seed. Meanwhile the technical narrative is doing the lookout's job in prose: *"the LORD's answering derision (v4) is not filed as this operation's effect."*

---

## PART D — THE PROCESS LESSON

Three times in one session I drew a structural conclusion from an emitted artefact without the rule that governs it. Each time the artefact **supported** my reading. Each time the rule base did not.

**The tendency is not carelessness with data. It is treating the emitted artefact as self-describing** — assuming what is visible in the file is the whole of what the model holds. **In this programme it systematically is not:**

| the model holds | the artefact shows |
|---|---|
| the verse (`Psa 37:21`) | the passage range (`Psa 37:14-40`) |
| the morphology, read from the STEP span | nothing — no morph field anywhere |
| a **directed pair** | one endpoint |
| `effect` deliberately out of scope | a claim that Scripture is silent |
| a span-keyed meaning distinction | `H2603:generou` — lemma plus an English word |

**Counter-discipline, stated so it can be enforced:**
> *Before drawing any structural conclusion from an artefact, ask what governs its production — and read that first.*

The researcher framed this generously as a supply problem (*"perhaps the biggest shortcoming was to provide you with the absolute rule base"*). **It is also mine: I should have asked.**

**A companion lesson, from A1:** the 1,499-section corpus was well-formed, fully referenced, internally consistent, and **passed its own validation**. The fault was undetectable from the output alone. Only the diff against the prior artefact exposed it.
> *Every regeneration is diffed at content level against its predecessor, and the diff is reported, before the new artefact is used for anything.*

**And a third, from B4:** count the machine's own invariant strings — that is 100% reliable. **Never count meaning.** Every regex-on-prose attempt this session produced garbage and was disowned. *Measurement informs; it never decides.*

---

## PART E — SUBSTANTIVE FINDINGS THAT SURVIVE

1. **The corpus systematically declines to localise the inner movement in a part of the person.** `seat: none`, 16/16 at source; 132 of 167 in the narratives. Rule-based warrant (P4). **The strongest finding of the session.**
2. **The theme crosses the spirit/body line freely.** Flesh, bones and body sit inside "inner-seat". If a boundary is drawn, it is not spirit/body but **what man can reach vs what God can reach** `[Psa 64:1-6 | #1]`.
3. **No seat has a fixed function.** Spirit right/willing/broken in one psalm; heart created clean and broken in the same.
4. **The inner being is at least as often patient as agent** — created, restored, redeemed, cut off, turned, bowed, gladdened by wine.
5. **Direction may constitute the movement.** Stated outright by the corpus `[Psa 131:1-3 | #1]`; demonstrated in `seeking-inquiring` and `being-heard-listening`. **Now recastable as a validation against the pair structure.**
6. **`other-uncategorised` holds three subjects with no family** — justice-and-office, idolatry, the human condition.

**Standing caveat on all six:** 298 of 2,048 sections read (14.6%), from 5 of 46 themes, **three of them selected for the property under test**. The adversarial test — `faint-despair-languishing`, `shame-confusion`, `rest-stillness-peace`, where direction is *not* structurally obvious — has not been run.

---

## PART F — DECISIONS TAKEN

1. Corpus remediated and verified sound (2,048 sections). Prior versions superseded.
2. Citation convention: **`[theme | Psa C:V-V | #n]`**.
3. Limitations (range refs, no lemmas in the narrative layer) **accepted**; conflicts referred to source level.
4. **The inner being is a system, not buckets.** The 46 families are a convenience of arrangement, not a representation of the system.
5. Psalms is **one book of sixty-six**; not a correlation to other evidence.
6. Each thematic exploration is a standalone `.md`, valuable in its own right and collectively in a group.
7. **Working order fixed:** compute → CSV evidence → technical narrative → story. **Divergence between layers is a finding.**
8. Analytic input to be built per book to **`WA-analytic-input-spec-2.0`**.

---

## PART G — NEXT STEPS

**Researcher, when CC is available:**
1. Generate the Psalms projection to `WA-analytic-input-spec-2.0` and resubmit for testing.
2. **Open items, in priority order** (spec Part 6):
   - **`discovery` (114) is not running as the emergence engine.** Highest leverage — fixing it cuts the analytic read load ~7× and restores the mechanism by which new dimensions are found.
   - **The `story` silence-vocabulary.** 8 of 39 records launder a design decision into a claim about Scripture. **This misleads the researcher, not just the AI.**
   - **`intensity` / `prohibition` / `specifier` not written**, though §14 has them ON for poetic.
   - **Is `from_span` implicit or absent?** Determines whether direction is recoverable from the current emission.
   - **`coupling` ↔ `locus` swapped** in 10 of 16 sample rows.
   - **Is `object-type` recorded on `target`?** §5 step 2 calls for it. E4 needs it; it may already exist.

**Analysis, on receipt of the projection:**
3. **E4 as validation** — does the pair structure bear out what the narratives assert about direction?
4. **The adversarial test** — `faint-despair-languishing`, `shame-confusion`, `rest-stillness-peace`. If direction is constitutive *there*, in movements that look like states rather than acts, the claim holds. If not, it narrows honestly to transitive movements.
5. **E1 §2 to be reissued** with the intensity/effect silence split out.
6. **41 themes remain unread.**

**Untouched this session:** the D3 assembly-model fork (recognise-then-attach vs fragment-stitch).

---

## Change control

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-13 | First issue — corpus remediation + first two explorations. |
| 1.1 | 2026-07-13 | Corrected §C.4 (generations: three → two). |
| **2.0** | 2026-07-13 | **Final for session. Major.** Adds E4 preliminary, the raw-source assessment, and the rule-base reckoning. **Records five corrections to my own claims (Part C)**, the process lesson that produced them (Part D), and the decisions and next steps arising. Supersedes 1.0 and 1.1 in full. |

*Session closed 2026-07-13. Resumes on delivery of the Psalms projection.*
