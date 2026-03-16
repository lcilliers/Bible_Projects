# Claude Session Log: [Topic]

> **Copy this file to Google Drive `04_Claude_Research/sessions/YYYY-MM-DD_topic_NN.md`.**
> Keep the full session archive on Google Drive. Summarise key outputs in `research/notes/`.

---

## Session Metadata

| Field | Value |
|-------|-------|
| **Date** | YYYY-MM-DD |
| **Session number** | 01 (increment per topic per day) |
| **Topic** | |
| **Related project** | |
| **Related passage(s)** | |
| **Claude model** | claude-3-5-sonnet / claude-3-7-sonnet / etc. |
| **Session link** | (paste Claude.ai conversation URL if available) |

---

## Session Objective

*What was this session trying to achieve? What question was posed to Claude?*

---

## Prompts Used

*Paste or summarise the key prompts used in this session.*

### Prompt 1

```
[Paste prompt here]
```

### Prompt 2

```
[Paste prompt here]
```

---

## Claude Outputs

*Paste the key outputs from this session. Summarise where outputs are very long.*

### Output 1 — [brief label]

```
[Paste Claude output here, or summarise if very long]
```

### Output 2 — [brief label]

```
[Paste Claude output here]
```

---

## JSON Data Records Produced

*If Claude produced structured JSON records for import into SQLite, note them here.*

| Batch file | Table | Record count | Import status |
|------------|-------|-------------|--------------|
| `verse_notes_[topic]_[date]_01.json` | `verse_notes` | | Not imported / Imported |

**Import command:**
```bash
python analytics/bible_analytics.py --import-json data/imports/[filename].json --table verse_notes
```

---

## Key Insights

*What are the 3–5 most valuable things that emerged from this session?*

1.
2.
3.

---

## Follow-Up Actions

- [ ] Create / update research note in `research/notes/`
- [ ] Import JSON data if produced
- [ ] Schedule follow-up session on:
- [ ] Add sources to Zotero:

---

## Session Quality Assessment

| Criterion | Rating (1–5) | Notes |
|-----------|-------------|-------|
| Accuracy / reliability | | |
| Depth of analysis | | |
| Usefulness for research | | |
| Prompts could be improved | | |

---

## Notes

*Any other observations about this session — what worked, what didn't, what to try next time.*
