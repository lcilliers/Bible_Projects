# Inner-being narrative: source vs publication check — 2026-10-14

Researcher request (chat, 2026-10-14): compare `C:\learning4comfort\publication-inbox\the_inner_being` with the source, and check `C:\learning4comfort\content\books\the_inner_being`. *"I am not convinced that the process of pushing to public-inbox and the subsequent preparation of the content for publishing is accurate."*

## Result

No faults found. Every current source chapter reached the inbox byte for byte. Every published page carries the source text word for word, with only the working notes left out.

| Check | Result |
|---|---|
| Source folder (`_analytics/essay/spirit_soul_body/inner-being-narrative`, top-level `.md`) | 32 current chapter files |
| Inbox `publication-inbox\the_inner_being` | **Empty — by design.** The learning4comfort publish workflow (`.github/prompts/publish-inbox.prompt.md` step 5) copies each inbox file to `publication-archive\the_inner_being\<date>\`, checks the SHA-256 hash, then deletes the inbox copy. |
| Archive batch `2026-10-14` vs source | 32 of 32 files present with **identical bytes** (SHA-256). No source file is missing from the archive. |
| Published pages `content\books\the_inner_being\chapter-*` | 32 pages, one per source file; no page without a source, no source without a page. |
| Page text vs source text (word for word, after removing Markdown and HTML markup) | **32 of 32 identical.** |
| Working notes left out | 31 lines in 7 chapters (10.7, 10.12, 10.13, 11, 12, 13.1, 14). All of them are working notes or the *Held — not yet re-examined* sections. No narrative text was dropped with them (listed below). |
| Working-note text on the published pages | None. The only "held" hits are prose ("Held-in anger…", "Held anger comes out as a ledger", "held by the prophet"). |
| Opening-page contents | 32 entries, in chapter order, titles matching the source. |
| learning4comfort git | Book folder and tracker clean; last commit `a556ad1` 2026-10-14 09:34 *Publish Inner Being: Chapter 2 "Going down to Sheol"*; `main` level with `origin/main` (as of its last fetch). |

## Text left out as working notes

| Chapter | Source lines | What it is |
|---|---|---|
| 10.7 | 613–617 | *Working note, not part of the narrative text.* Further readings on choosing still to come |
| 10.12 | 251 | *Held (working note…)*: fear verses that cross into life and death, for Ch 2 |
| 10.13 | 484–487 | *Held (working note…)*: 2Ki 3:27; *ḥāmam* "to warm"; heart and spirit in the anger verses |
| 11 | 234 | *Working note…*: the first reading of authority (OT-100) |
| 12 | 148–156 | *Held — not yet re-examined* (the earlier chapter's material) |
| 13.1 | 321 | *Working note…*: the wider verses in which God chooses, not yet placed |
| 14 | 117–125 | *Held — not yet re-examined* (the earlier chapter's material) |

## Observations on the process (no fault)

1. **The inbox is emptied after each publish, so each copy run sends all 32 files again.** `narrativecopy.py` decides "unchanged" by comparing with the inbox, not with what has been published. The converter then rewrites only the pages whose text changed, so nothing is wrong on the site. But the archive keeps a full copy of unchanged chapters in each batch (for example, Ch 1 v4 is archived 10 times). This is harmless; it costs only disk space.
2. **A working note runs to the next `## ` heading.** The converter (`scripts/publish_book.py`, `HELD`) drops everything from a note marker to the next `## ` heading or the end of the file. Today every note sits at the end of a section or file, so nothing was lost. Narrative prose placed after a note but before the next `## ` heading would be silently left off the page.

## Limits of this check

- The comparison is text-level (word sequence). It does not test the page structure: list nesting, table cells, or which line is a heading.
- I did not run learning4comfort's converter in dry-run mode against the source; the session's permission check blocked it. Instead I compared with a read-only script that applies the same working-note rule (scratchpad `compare_pub.py`).
- I did not fetch the live site (https://learning4comfort.uk). The check covers the committed local pages, not what the server currently returns.
