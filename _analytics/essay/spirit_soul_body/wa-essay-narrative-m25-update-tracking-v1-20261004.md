# Inner-being narrative: tracking the life-and-death (M25) updates

**Date:** 2026-10-04 · **Author:** Claude Code · **Purpose:** to show where the M25 work landed in the narrative, and how to compare it with what was there before. Read-only; nothing in the chapters was changed.
**Researcher (chat, 2026-10-04):** *"I am trying to find the updates you did for M25 in the narrative to compare what you already done so far for M25 but find it difficult to find - can you show me how to track the updates."*

## 1. Where the record of M25 is kept

Five places. None of them, on its own, shows the changed text.

| # | Place | What it tells you | What it does not |
|---|---|---|---|
| 1 | `inner-being-narrative/00-index-and-status-v1-20260930.md`, **Structure log** (rows dated 2026-10-02 to 10-04, "life and death (M25)") | What each unit did to the structure: new sections, moves, renames | The text itself |
| 2 | The same index, **version map** (the "life and death (M25) … →" lines) | Which chapter files each unit bumped, and to which version | What changed inside them |
| 3 | Each unit ledger's **"Woven — where"** table (`_analytics/Clusters/M25 - life-death/`: unit 1 §238, unit 2 §316, unit 3 §328, unit 4 §167, Q2/Q3 §134) | Each observation (LD-nn) → chapter and section | It lists placements; it does not show the surrounding text |
| 4 | `_analytics/Clusters/M25 - life-death/life-death-linkage-map.md` | Each life-death link → where its account is carried, and where it is only pointed to | Units 3–4 and Q2/Q3 coverage not checked here |
| 5 | `wa-essay-spirit-soul-body-claim-register-v13-20261004.md` | Each changed claim, with its verdict | New text that is not a claim |

**The comparison you need is a side-by-side of each chapter before M25 and now.** Every earlier version is kept in `inner-being-narrative/archive/`, so this is always possible (§3).

## 2. What M25 changed, chapter by chapter (measured)

Baseline = the last version **before** the first life-and-death unit touched that file. Words are counted on the whole file. "Lines added" = paragraphs, bullets or headings that are new or changed.

| Ch | Before M25 (archive) | Now | Words before → now | Lines added / removed | New headings from M25 |
|---|---|---|---|---|---|
| 2 | v5 | v11 | 2,095 → 12,508 | +433 / −31 | Where life flows from; Life set before a person; Living before God; Life asked for; What death is (Death and sin; Death in the living); Sleep and waking; Life weighed; Facing death; Soul, spirit and heart at death; Made alive; Dying to the Lord; The body raised (Sown and raised; Christ first; Changed; Waited for); Life, and judgment; What follows |
| 4 | v7 | v10 | 1,973 → 2,207 | +6 / 0 | — |
| 6 | v4 | v6 | 1,893 → 2,039 | +4 / 0 | — |
| 10.1 | v8 | v11 | 5,230 → 5,715 | +17 / 0 | — |
| 10.2 | v7 | v9 | 2,081 → 2,253 | +4 / 0 | — |
| 10.3 | v2 | v5 | 1,002 → 1,348 | +9 / 0 | — |
| 10.4 | v4 | v6 | 3,396 → 3,628 | +7 / −1 | Thinking and life |
| 10.5 | v9 | v12 | 2,283 → 2,629 | +13 / 0 | The oath |
| 10.6 | v4 | v7 | 344 → 755 | +15 / −1 | — |
| 10.7 | v6 | v9 | 565 → 867 | +7 / −1 | — |
| 10.9 | v10 | v14 | 3,715 → 4,308 | +22 / 0 | Calling on God to wake; The living God |
| 10.10 | v8 | v11 | 2,426 → 3,036 | +22 / −1 | Loyalty and honour |
| 10.11 | v1 | v2 | 2,191 → 2,224 | +1 / 0 | — |
| 11 | v9 | v13 | 4,756 → 5,264 | +5 / 0 | — (additions inside §4) |
| 12 | v9 | v12 | 2,584 → 2,861 | +8 / 0 | — |
| 13 | v4 | v9 | 3,832 → 4,247 | +17 / −1 | — |
| 14 | v8 | v12 | 2,025 → 2,499 | +10 / −2 | — |

**What the figures show:** almost all of M25 went into Ch 2, which grew about sixfold. Every other chapter got short added passages, mostly a paragraph or a pointer back to Ch 2. They were added, not rewritten: other than in Ch 2, removed lines are 0–2 per file.

*(Ch 2's v5 figure is the chapter as it stood when it was still Ch 9, just after the move, #1936. Ch 1, 3, 5, 7, 8, 9, 10.0, 10.8 and 15 were not touched by M25.)*

## 3. How to see the actual changes

Open a side-by-side compare in VS Code. Run the command from `C:\Bible_study_projects\_analytics\essay\spirit_soul_body\inner-being-narrative`. Added text shows in green and removed text in red.

```
code --diff archive/02-life-breath-and-death-v5-20261002.md 02-life-breath-and-death-v11-20261004.md
code --diff archive/04-the-heart-v7-20261002.md 04-the-heart-v10-20261004.md
code --diff archive/06-the-spirit-v4-20261002.md 06-the-spirit-v6-20261004.md
code --diff archive/10-01-feeling-v8-20261002.md 10-01-feeling-v11-20261004.md
code --diff archive/10-02-knowing-and-hearing-v7-20261002.md 10-02-knowing-and-hearing-v9-20261004.md
code --diff archive/10-03-remembering-and-forgetting-v2-20261002.md 10-03-remembering-and-forgetting-v5-20261004.md
code --diff archive/10-04-thinking-v4-20261002.md 10-04-thinking-v6-20261004.md
code --diff archive/10-05-speaking-v9-20261002.md 10-05-speaking-v12-20261004.md
code --diff archive/10-06-wanting-v4-20261002.md 10-06-wanting-v7-20261004.md
code --diff archive/10-07-choosing-and-setting-direction-v6-20261001.md 10-07-choosing-and-setting-direction-v9-20261004.md
code --diff archive/10-09-relating-to-god-v10-20261002.md 10-09-relating-to-god-v14-20261004.md
code --diff archive/10-10-relating-to-others-v8-20261002.md 10-10-relating-to-others-v11-20261004.md
code --diff archive/10-11-hiding-and-disclosing-v1-20261002.md 10-11-hiding-and-disclosing-v2-20261003.md
code --diff archive/11-patterns-of-the-inner-life-v9-20261002.md 11-patterns-of-the-inner-life-v13-20261004.md
code --diff archive/12-when-the-inner-being-goes-wrong-v9-20261002.md 12-when-the-inner-being-goes-wrong-v12-20261004.md
code --diff archive/13-under-gods-anger-v4-20261001.md 13-under-gods-anger-v9-20261004.md
code --diff archive/14-made-new-v8-20261002.md 14-made-new-v12-20261004.md
```

To see a single unit only, compare the two versions on either side of it. The version map (§1, item 2) gives the numbers. For example, unit 3 in Ch 2 is v8 → v9:

```
code --diff archive/02-life-breath-and-death-v8-20261003.md archive/02-life-breath-and-death-v9-20261004.md
```

## 4. The gap this shows

There is no single view that says, for each passage of the narrative, which strand put it there. The chapter text carries no markers (deliberately, since it is reader-facing), and the version map stops at file level. If a running view would help, one option is a generated "strand changes" report per strand: the chapter diffs above, with each added passage listed under its chapter and section. It would be built from the archive and would not touch the chapters. **Not built. For your decision.**
