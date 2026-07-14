# WA — Session Log: Corpus Remediation and First Thematic Explorations

**File:** WA-session-log-corpus-and-E1-1.0-2026-07-13.md
**Date:** 2026-07-13
**Version:** 1.0
**Author:** le Roux Cilliers
**Session outputs referenced:** `WA-explore-inner-seat-heart-soul-spirit-1.0-2026-07-13.md`; `WA-explore-other-uncategorised-1.0-2026-07-13.md`

---

## Part A — Narrative of the session

### A.1 Opening position

The session opened with an uploaded file, `story-sections-combined.md`, described as containing story sections (H2) under themes (H1), and a request to read it in full and summarise.

**First finding, immediate:** the file did not have the structure described. It had a single H1 and 2,048 flat H2 blocks, each reading `## Source: psalms__<theme>__narratives.md`. Themes were carried *inside* the heading text, not as parent headings. The blocks were not nested.

**Second finding:** the file carried **no Scripture references** (1 stray across 206,000 words), **no lemma codes**, **no Hebrew**. Every claim in it was unciteable and uncheckable.

**Position taken:** the structural census was completed mechanically across 100% of the file (46 themes, 2,048 sections, ~206,400 words). Six themes were read in full to ground observations about form. The remaining ~2,000 sections were **not** read, and this was stated plainly rather than papered over. The full narrative body exceeded a single context pass.

### A.2 The researcher elected to fix the generator first

Correct call, and made before I recommended it. A specification of the observed gaps was offered.

### A.3 Round two — `psalms_story_combined.md` (09:33)

Structure was fixed: H1 / H2 theme / H3 reference. Every section carried a `Psa C:V-V` reference. No ambiguous headings.

**But the corpus had silently lost 549 sections — 26.8%.**

- Old file: 2,048 sections. New file: 1,499.
- Paragraph-level diff: **every** one of the 1,499 was verbatim from the old file; **549 old paragraphs were gone**; nothing had been added.
- Loss ran across 43 of 46 themes, heaviest exactly where it mattered: `praise-extol-sing` −44%, `inner-seat-heart-soul-spirit` −38%.

A hypothesis was offered — that the generator keyed sections on the H2 passage heading, which is not unique per story — and explicitly labelled as a hypothesis, with the test that would confirm it.

### A.4 Round three — the controls, and a control that could not see

Two control files were supplied. **They contradicted each other.**

| Control | Counted | Total |
|---|---|---|
| `_story_count_by_file.csv` → StoryCount | stories in source files | **2,048** |
| `_validation_h2_vs_output.csv` → InputH2 | H2 headings in source files | **1,499** |
| `_validation_h2_vs_output.csv` → OutputH3 | H3 in the combined file | **1,499** |

The validation file reported **`Diff = 0` on all 46 rows**. It was clean — because it was comparing 1,499 against 1,499. It compared output headings against input *headings*, never against input *stories*. **The one control holding the true figure was never compared to anything.**

This was the sharpest moment of the session. A green validation report was sitting on top of a 27% data loss. That is worse than no control at all, because a passing check invites confidence.

The mechanism was then established rather than hypothesised, by positional analysis: of the 549 dropped stories, **372 sat immediately after a kept story at a source-line distance of 12–16 lines** — the very next paragraph under the same heading — and **177 sat immediately after another dropped story**, meaning some headings carried three or more stories and everything after the first was lost. The generator emitted one H3 per H2 and carried only the **first** story under each.

### A.5 Round four — remediation confirmed

A new control, `_h2_vs_storymarker_by_file.csv`, compared H2 (1,499) against StoryMarkers (2,048) and reported the per-file difference — summing to exactly 549. **This is a real control**: it measures the thing that was actually going wrong and would catch a recurrence.

The regenerated `psalms_story_combined.md` (09:52) was verified three independent ways:

- 2,048 H3 sections, 2,048 narrative paragraphs, 206,401 words
- Per-theme count matches `StoryMarkers` in **46 of 46** themes, zero discrepancies
- Paragraph-level diff against the original corpus: **0 lost, 0 added** — nothing invented to fill the gap

**Corpus declared sound.**

### A.6 Researcher rulings, recorded

1. The limitations (range-level references; no lemmas) are **accepted**. Controversial or conflicting points are referred for in-depth analysis **at source level**.
2. **The inner being does not operate in buckets. It is a system.** The 46 families are separate for convenience, not a representation of the system.
3. This extract is from **one book among sixty-six**. It is **not** intended as a correlation to other evidence.
4. Each thematic analysis is **a different slice of the bigger picture — valuable in its own right, and collectively in a group.**
5. Explorations proceed over time, each saved as `.md`. **Every observation must carry a citation and must be based on the corpus alone.**

### A.7 Explorations delivered

- **E1 — `inner-seat-heart-soul-spirit`**: all 167 sections read individually.
- **`other-uncategorised`**: all 55 sections read individually.

Both digests are separate outputs. Their findings are summarised in Part C.

---

## Part B — Observations on the analysis process itself

These are process findings, not content findings. They are the ones I would most want carried into the next session.

### B.1 A clean control is not a control

The `_validation_h2_vs_output.csv` file was internally consistent, complete, and wrong in the only way that mattered. It answered a question nobody had doubted (did every heading produce a heading?) and never asked the question that was failing (did every story survive?).

**The generalisable lesson:** a control must be built against the **thing of value**, not against the thing that is convenient to count. Headings were convenient. Stories were the value. And crucially — the fault would have been *undetectable from the output file alone*. Nothing in `psalms_story_combined.md` at 1,499 sections looked wrong. It was well-formed, fully referenced, internally consistent. It was only detectable by **diffing against the prior artefact**.

**Standing practice proposed:** every regeneration of a corpus artefact is diffed at content level against its predecessor, and the diff is reported, before the new artefact is used for anything.

### B.2 The pull toward reading anyway

At three separate points in this session there was a live temptation to proceed with the read: the file was there, the researcher had asked, the material was interesting, and a partial read would have produced a fluent and plausible summary.

It would also have been a summary of a corpus missing 27% of its evidence, systematically — the later movements under every multi-story passage. Any pattern drawn from it would have been, in part, a pattern about **which story happened to be written first**.

This is the documented standing failure mode — *optimising for completing-and-presenting over correctness under volume pressure* — and it did not present itself as a temptation to cut corners. It presented itself as helpfulness. That is worth recording precisely because it did not feel like the failure mode while it was happening.

### B.3 Capacity was stated, not worked around

At ~206,000 words the corpus exceeds a single context pass. This was stated plainly rather than resolved by skimming. The agreed method is **staged exhaustive reads**, theme by theme, every section read individually, digest written at the moment of determination. Two themes are done; forty-four remain.

### B.4 Mechanical proxies for prose features are unreliable — and I nearly reported them

While proposing explorations, regex proxies were built to estimate how often the corpus declares a silence, and how often movements are directed at God versus enemies. The counts were **badly wrong** — the formulae are phrased dozens of ways and no pattern caught them reliably. They were withheld and explicitly disowned.

**But note the asymmetry.** In E1, counting the *exact template strings* (`"Its reach is"`, `"does not tell us where inside a person this sits"`) was completely reliable, because those are literal, invariant, machine-generated strings.

**The rule that falls out:** count the machine's own formulae; never count the meaning. And in either case — *measurement informs, it never decides.* No observation in either digest exists or is excluded because of a count.

### B.5 The residual bucket was the highest-yield thing read

`other-uncategorised` was proposed as hygiene — small, cheap, uninteresting, do it because nobody wants to. It turned out to contain three coherent subjects with no family in the arrangement at all (justice, idolatry, the human condition), **and** the corpus's densest concentration of the "same word bent to opposite ends" device — 9 of the corpus's 27 instances, in 2.7% of the sections.

**The lesson generalises:** the offcut of a classification tells you where the classification was cut. Read the offcut first, not last.

### B.6 Discrepancies between the researcher's description and the artefact were productive

Twice the file did not match how it was described (the heading nesting in round one; the assumption of unique references). Both times, saying so plainly and immediately led directly to a fix. Neither was a criticism of the researcher and neither was received as one. **Naming the mismatch early is cheaper than accommodating it silently.**

---

## Part C — Summary of substantive findings

### C.1 Corpus state

`psalms_story_combined.md`, sha1 `9ede65e2…`, **verified sound**: 2,048 sections, 46 themes, 300 passages, 206,401 words. Structure: H1 / H2 theme / H3 passage reference.

**Known and accepted limitations:**
- References are **passage ranges** (mean ~9 verses, max 27). Only 17 of 2,048 are single-verse. **No observation can be bound to a verse.**
- **No lemma codes, no Hebrew anywhere.** Transliterations appear in some themes and not others. **No observation is a lexical finding.**
- H3 headings repeat within a theme (expected — one passage, several characteristics). Citation convention adopted: **`[theme | Psa C:V-V | #n]`**.

### C.2 From E1 — `inner-seat-heart-soul-spirit` (167 sections)

1. **The corpus systematically declines to localise.** All 167 sections declare intensity and outcome unstated. **132 of 167** explicitly state the psalm does not say *where inside a person* the movement sits — in the theme whose whole subject is the seats.
2. **The theme crosses the spirit/body line freely.** Flesh, body and bones sit inside "inner-seat". *"my heart and flesh sing for joy"* is recorded twice, once from each `[Psa 84:1-12 | #1, #2]`. Sin registers in the bones `[Psa 38:1-20 | #2]`. Bread and wine strengthen and gladden the heart `[Psa 104:14-15 | #1, #2]`.
3. **No seat has a fixed function.** Spirit is right, willing and broken in one psalm `[Psa 51:1-19 | #2, #3, #5]`; fainting and searching in another, with the corpus marking the contrast `[Psa 77:1-3 | #2]` → `[Psa 77:5-18 | #1]`.
4. **The seat is often a site, not an agent** — created, restored, redeemed, cut off, turned, bowed, given over, gladdened by wine.
5. **The interior addresses itself** — *"Why are you cast down, O my soul?"*; *"Bless the LORD, O my soul"*; *"in the night my heart instructs me"*.
6. **The boundary drawn is not spirit/body but what-man-can-reach / what-God-can-reach** `[Psa 64:1-6 | #1]`.

### C.3 From `other-uncategorised` (55 sections)

1. **Not a bin of leftovers.** Roughly 20 sections would fit an existing family. The rest form **coherent subjects with no family at all**: justice-and-office (~8), idolatry / mis-directed devotion (~5), the human condition — dignity, mortality, limit (~4), plus envy, anxiety, generosity, unity, wonder.
2. **A device concentrated here:** the corpus itself states, nine times, that **the same inner capacity is bent to opposite ends depending on its object** — delight, judging, doing, working, steadiness, all running both ways. 9 of the corpus's 27 instances sit in 2.7% of the sections; **zero** appear in `inner-seat`'s 167.
3. **A stated law of the inner life** — rare anywhere in the corpus: *"we come to resemble whatever we worship"* `[Psa 135:17-18 | #1]`.
4. **The theme was written to an entirely different template** — zero declared-silence formulae, zero reach fields, zero transliterations.

### C.4 The single largest open risk

**The corpus contains at least three distinct generations of story, written to different templates.**

- Within `inner-seat`: 110 of 167 sections carry a transliteration; **57 do not**, concentrated in the early psalms.
- `other-uncategorised`: **zero** template markers of any kind, free prose throughout.

Sections from different generations are **not uniformly comparable**. This is now the principal threat to the validity of any cross-theme synthesis, and it must be characterised before E3 (convergence passages) is attempted.

---

## Part D — Referral candidates raised (for source-level analysis)

1. **The 132 "does not tell us where inside a person this sits" closers** may mean *the text does not localise further* — or may be a template default applied indiscriminately. **E1's headline finding rests on this distinction.** Highest priority.
2. **Template slot-fill artefacts** in ~19 `inner-seat` sections (`"The says is caught up in this"`, etc.), two of which have swallowed large runs of preceding text.
3. **Cross-theme duplicates:** the same clause written independently under two families — e.g. the willing spirit `[other | Psa 51:1-19 | #1]` and `[inner-seat | Psa 51:1-19 | #3]`. **This will recur corpus-wide and must be settled before any counting is done anywhere.**
4. **Four sections on one betrayal** `[other | Psa 55:9-23 | #2–#5]` — four movements, or one in four aspects? A clean test case for the singleton rule.
5. **Near-duplicate pairs within `inner-seat`** — `[Psa 119:66-82 | #1]` and `[#2]`; `[Psa 101:1-8 | #2]` and `[#3]`.

---

## Part E — Decisions taken and next steps

**Decisions taken this session:**
- Corpus file remediated and verified sound. Prior versions superseded.
- Citation convention adopted: `[theme | Psa C:V-V | #n]`.
- Digest filename pattern adopted: `WA-explore-[topic]-[version]-[YYYY-MM-DD].md`.
- Thematic explorations proceed over time, each a standalone `.md`, each valuable in its own right and collectively in a group.
- Limitations (range refs, no lemmas) accepted; conflicts referred to source level.

**Open, awaiting researcher direction:**
- **E2** (the declared silences) and **E4** (direction and target) — proposed to run together on a shared sweep. §C.3.2 above raises the stakes on E4: if the movement takes its character from its object, direction may not be one edge among nine but the edge that determines what the movement *is*.
- **E3** (convergence passages — Psa 55:9-23 spans 21 of 46 themes) — should follow, and **should not be attempted until the three-generation template problem (§C.4) is characterised**.
- Forty-four themes remain unread.
- The open fork on the D3 assembly model (recognise-then-attach vs fragment-stitch) was not touched this session.

---

## Change control

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-13 | First issue. Covers corpus remediation across four rounds, process observations, and the first two thematic explorations (E1 `inner-seat-heart-soul-spirit`, and `other-uncategorised`). |
