# WA M10 — Verse Work-Through Plan (how we read all the verses)

**File:** wa-m10-verse-workthrough-plan-v1_0-20260621.md · **Version:** v1_0 · **Date:** 2026-06-21
**Prev output:** `wa-m10-behaviour-map-v1_0-20260621.md` (behavioural scaffold — a set of *lenses*, not yet deep-dive units)
**Source:** `wa-ve-lexical-extract-M10-20260621-b{1..8}of8.json` (extract v1_0)
**Status:** PLAN for review. No verses read. No collections committed.

---

## 1. The problem this plan fixes

Last turn I offered collections (WRONG-status, SEATED, SELF-owned…) that *overlap*. As deep-dive units they fail two tests: a verse could land in several of them (so coverage double-counts), and they were drawn from the lexical fields *before* reading (so they pre-judge the shape). Committing to deep-dive collections now would be jumping to conclusions — the very thing we agreed not to do.

**The fix: read first, collect after.** We read every verse once, record what each sin-occurrence actually *does* in that verse, and let the collections form from the completed reads. The collection list becomes an **output** of the reading, not a precondition of it.

---

## 2. The principle

> One pass through the corpus. Every occurrence read exactly once. A compact, uniform behavioural record per occurrence, grounded in the verse text (not just the field). Collections assembled from those records afterward. Typing (characteristic / status / new construct) only after the collections are visible and their relationships clear.

This honours: verse-leads (GR-PROG-001), don't-impose-granularity (§0), read-don't-sample (§A1), don't-script-the-judgement (§A2), and full coverage (§4).

---

## 3. Unit of work and the coverage guarantee

- **Unit = the verse occurrence** (one focus term in one verse). There are **1,462** of them across **1,215** verses.
- **Read-once:** we move through the corpus in fixed batches; each occurrence is read in its batch and nowhere else. No occurrence is read twice; none is skipped.
- **Multi-membership is deferred, not lost:** an occurrence can later belong to several behavioural collections (e.g. *self-owned* **and** *seated in the soul* **and** *against God*). We capture all those facets *as tags on the single read*, so multi-membership is recorded without re-reading.
- **Running tracker:** every step reports cumulative coverage (e.g. "366 / 1,462 occurrences read") so we always know exactly where we are.

---

## 4. What we record per occurrence (the read schema)

A tight, uniform record so reads are comparable and clustering is possible afterward. Each field is confirmed against the **verse text**, with the lexical field as a starting hint only.

| Field | Values | Note |
|---|---|---|
| `ref` / `term` / `sense` | — | verse, Strong's+translit+gloss, the ESV sense here |
| `kind` | act / state / character | what the term *is* in this verse |
| `valence` | wrong / remedy / commanded / forbidden / neutral | confirmed from context |
| `whose` | self / other / addressed / impersonal | whose sin it is |
| `against` | God / person / community / abstract / none | the offence's target |
| `seat` | soul / heart / flesh / mind / conscience / none | inner-being seat, if the verse locates it |
| `entry` | within-person / from-outside / generational / none | how the sin arises/reaches the person, if shown |
| `God_role` | none / object / agent / giver / addressee | God's role toward the sin |
| `ib_note` | one line | what this verse shows about sin's *operation in the inner being* — or "silent on inner being" |
| `field_check` | ok / flag:<field> | if the verse contradicts a lexical field (FA-14 hygiene) |
| `behaviour_key` | short composite | e.g. `state·wrong·self·vsGod·heart` — the handle we cluster on later |

`ib_note` and `behaviour_key` are the two that carry the analytical judgement; everything else is confirmation. "Silent on inner being" is a legitimate, expected result for many occurrences (GR-PROG-007) — sin named as a legal/cultic fact with no interior content. Silence is recorded, never padded (§A7).

---

## 5. The end-to-end sequence

```
STAGE 1  READ  (this is the bulk of the work)
   8 batches, corpus order. Per batch:
     • read every verse; write one read-record per focus occurrence (§4 schema)
     • write batch read-file (json: records) + batch digest (md: what surfaced, field-flags)
     • update coverage tracker; obslog; present_files
   → ends when 1,462 / 1,462 read.            [no collections declared yet]

STAGE 2  ASSEMBLE  (collections emerge)
   • cluster the 1,462 records by behaviour_key / ib_note likeness
   • the collection list is written from the data; coverage reconciles to 1,462
   • DECISION POINT: you review the emergent collections.

STAGE 3  RELATE
   • map how collections sit to one another (which merge, which split,
     which are facets of one another, which are distinct)
   • surface the candidate inner-being constructs (e.g. "sin seated",
     "sin received from outside", "sin owned/borne").

STAGE 4  TYPE
   • only now: propose which collections are characteristics, which are
     statuses, which need a new construct — with the status precedent
     defined from the assembled evidence.
   • DECISION POINT: you decide the typing.
```

Deep-dive verse analysis **is** Stage 1 — it is not a later step applied to pre-chosen collections. We are deep-diving *all* the verses, once, in order.

---

## 6. Cadence options (how big each working step is)

The 8 source batches are ~150 verses / ~180 occurrences each. Choose the turn size:

- **Option F — one full batch per turn** (8 turns to finish Stage 1). Fewer turns; each turn is dense.
- **Option H — one half-batch (~75 verses) per turn** (16 turns). Lighter, easier to review as we go; slower.
- **Option S — a small pilot first**: I read the first ~40 verses (batch 1, part 1), you check the read-record quality and the schema against real output, we lock it, then proceed at F or H. *Recommended — this is the §4 "lock the template on one exemplar before mass-producing" discipline, and it lets you see a real read before committing to 1,462 of them.*

---

## 7. Decisions I need before reading

1. **Design:** confirm the read-first, collect-after sweep (Stage 1→4 above), rather than deep-diving pre-chosen collections.
2. **Schema:** confirm the §4 read record — or add/remove fields. (Is `ib_note` + `behaviour_key` the right place for the judgement? Any inner-being facet you want captured that isn't here?)
3. **Cadence:** F, H, or S. (I recommend S, then H.)

No reading starts until you've set these. On your go, I begin with the pilot (or your chosen cadence), batch 1, and write the first read-file.

---

*Plan only. No verses read; no collections committed; no findings.*
