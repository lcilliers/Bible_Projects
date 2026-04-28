# WA-SessionD-Orientation-v3_0-2026-04-12

**Framework B — Soul Word Analysis Programme**
**Session D: Cross-Registry Synthesis**
Orientation and Process Instruction

Version 3.0 | April 2026 | Status: Active governing document

| **Document** | **Value** |
|---|---|
| Filename | WA-SessionD-Orientation-v3.0-2026-04-12.md |
| Supersedes | WA-SessionD-Orientation-v2.1-20260329.md |
| Status | Governing document — sufficient for conducting Session D runs against accumulated SD pointer data. Not yet a full instruction for the final programme synthesis pass. |
| Change note | v3.0 — Full rewrite. Pool architecture retired: all pool-based Session B, pool analysis dataset, and pool-level synthesis references removed. SD pointer mechanism formalised: `wa_session_research_flags` SD_POINTER records are now the concrete bridge from Session B to Session D. Section 1 boundary statement corrected: Session B raises SD pointers, Session D resolves them. Section 5 updated: capture mechanism now described through the concrete SD_POINTER database mechanism with field specifications. Section 6 updated: input model is per-registry word studies plus the SD pointer record, not pool analysis datasets. Section 7 updated: gate is researcher-declared based on sufficient SD pointer accumulation, not pool completion. Section 12 added: the Session D process — how a session actually runs from SD pointer clustering through database query requests to synthesis document production. Section 11 updated: items still undesigned now reflect current state. |
| Companion documents | WA-SessionB-Instruction-v4.7 │ WA-Registry-Management-Guide-v5.8 │ WA-Reference-v5.5 │ patch_specification-v1.10 |

---

## 1. What Session D Is

Session D is the cross-registry synthesis phase of the Framework B Soul Word Analysis Programme. It works in the opposite direction from Sessions A and B.

Sessions A and B are word-driven. They begin with a Hebrew or Greek term, extract its occurrences, analyse its semantic range, and build a structured account of what that word contributes to the biblical understanding of the inner life. The word is the entry point; the corpus follows.

Session D begins not with words but with questions about the inner life of the human person that the programme as a whole is trying to answer. It asks: when you lay the full body of word-study data alongside each other, what do you see? What patterns emerge that no single word study could produce? What concepts does the data illuminate that the biblical writers addressed without ever naming directly?

Session D is therefore the interpretive, synthetic, and constructive phase of the programme. It is where the research becomes a framework rather than a catalogue.

---

### 1a. The Session B / Session D Boundary

**Session B raises SD pointers. Session D resolves them.**

This boundary replaces the earlier formulation that "observations about how words relate belong in Session D, not Session B." That formulation was incomplete. Session B is now the place where cross-registry observations are made and captured — every verse is read through the cross-registry lens (Section 2.0a of the Session B instruction), and every observation that implicates another registry is immediately recorded as an SD pointer in the observations log and persisted to the database. Session B does not resolve these observations — it does not have the cross-word data to do so — but it raises them with precision and analytical detail.

Session D begins with this accumulated pointer record. Its work is to:
1. Group related pointers across registries
2. Formulate specific investigation questions
3. Request targeted database queries from Claude Code to retrieve evidence
4. Perform cross-registry analysis against that evidence
5. Produce synthesis findings

**What does not cross the boundary:** synthesis conclusions. An SD pointer is a structural observation and a question — not an answer. Session D is where the question is investigated. Session B is not permitted to answer it.

---

## 2. What Session D Is Not

It is not Session B. Session B performs word-level analysis and raises SD pointers. Session D investigates those pointers using cross-registry data. A Session D analysis that simply re-reads individual word studies without engaging the cross-registry pointer record has not done Session D work.

It is not a commentary. Session D does not interpret individual biblical passages; it synthesises patterns across the full dataset.

It is not a systematic theology. The governing method is that structural categories must emerge from the data, not be imported from existing theological frameworks. Session D holds to this even when the synthesis looks like familiar categories.

It is not premature. Session D investigations can begin when meaningful pointer accumulation exists for a thematic cluster — researcher-declared, not algorithm-triggered. But full programme synthesis waits until the dataset is substantially complete.

It is not confirmatory. The primary risk at Session D is fitting subsequent data to a narrative that hardened during early analyses. The methodology must remain genuinely open to revision.

---

## 3. The Stratigraphy Model

The programme operates as a stratigraphy — a layered accumulation of knowledge where each layer is both output and foundation.

### 3.1 The Layers

| **Layer** | **Description** |
|---|---|
| Layer 0 — Foundation | The two 100-page documents on spirit-soul-body and the Holy Spirit. The foundational layer. |
| Layer 1 — Scope | The 212-word registry. The discovery that the original 29-word frame was too narrow. |
| Layer 2 — Term inventory | Phase 1 extraction — all Hebrew and Greek terms associated with the 212 words. |
| Layer 3 — Verse Context | The full corpus filtered and structured — all OWNER terms classified, anchor verses designated. |
| Layer 4 — Word analysis with SD pointers | Session B — per-registry word analysis producing word studies and SD pointer records. The building blocks of synthesis. |
| Layer 5 — Cross-registry pointer record | The accumulated SD_POINTER records in `wa_session_research_flags` across all completed registries. The structural bridge layer. |
| Layer 6 — Synthesis | Session D analysis — cross-registry investigation of pointer clusters, producing synthesis documents. Not yet underway at scale. |

### 3.2 The Emergent Nature of the Layers

The layers were not designed top-down. They emerged through the work itself. The consequence for Session D: Session D categories must emerge from the Layer 4/5 data, not from the Layer 0 framework. The foundation shapes the questions; it does not determine the answers.

---

## 4. The Scope Model Correction

### 4.1 The Correction

The concentric circle model was at risk of being used as an explanatory framework rather than a scope instrument. The corrected position: the concentric circles define scope only. They answer the question of which entities and relationships are in scope for the programme. They do not describe how characteristics interact, how the inner being is structured, or how the four rings relate to each other. That is precisely what Session D is supposed to discover from the data.

| **⚠ Any Session D synthesis that uses the concentric circle model as an explanatory framework — rather than as a scope boundary — is repeating the error corrected in March 2026. The circles define what is in scope. What the structure of the inner being looks like is what the 212 words are supposed to reveal.** |
|---|

### 4.2 The Spirit-Soul-Body Caution

The spirit-soul-body framework is a working organisational frame from Layer 0, not a pre-determined answer. Session D must ask: does the data confirm, modify, or challenge the spirit-soul-body frame as a description of the inner being's structure? The framework is a hypothesis at Session D, not a given.

---

## 5. The SD Pointer Mechanism — The Bridge from Session B to Session D

### 5.1 What SD Pointers Are

SD pointers are the concrete bridge between Session B analysis and Session D synthesis. They are records in `wa_session_research_flags` with `flag_code = 'SD_POINTER'`.

Each pointer:
- Names a specific cross-registry observation arising from a word's Session B analysis
- Identifies the registries implicated
- States the analytical question that cannot be resolved within a single registry
- Carries a priority rating (HIGH / MEDIUM / LOW)
- Carries a `cross_registry_id` pointing to the primary partner registry where determinable

### 5.2 SD Pointer Field Specification

| **Field** | **Content** |
|---|---|
| `flag_code` | `SD_POINTER` |
| `flag_label` | `DIM-[nnn]-SD[nnn]` — sequential, unique per registry (e.g. `DIM-023-SD001`) |
| `registry_id` | The registry where this pointer was raised |
| `cross_registry_id` | Primary partner registry ID (or null if multiple/programme-level) |
| `priority` | `HIGH` — core structural question; `MEDIUM` — significant connection with clear evidence; `LOW` — noteworthy but secondary |
| `session_target` | `D` |
| `description` | Full analytical text: specific verse or data point, registries implicated, the question for Session D, why it cannot be resolved within the source registry |
| `session_raised` | Instruction version that produced it |
| `raised_date` | Date raised |
| `resolved` | `0` until Session D marks it resolved |

### 5.3 What Is Captured vs What Is Not

**Captured as SD pointers:**
- Any observation from Session B analysis that requires cross-registry data to investigate
- Verse-level co-occurrences between this registry and another that reveal a structural inner-being relationship
- Root family connections that span registry boundaries
- Dimensional patterns that appear in unexpected cross-cluster combinations
- Researcher-identified structural observations arising during any analytical pass

**Not captured as SD pointers:**
- Synthesis conclusions — these belong in Session D outputs, not pointer records
- Observations resolvable within the single registry's own data
- Thematic speculation without specific verse or term evidence

### 5.4 Querying the Pointer Record

Claude Code query — all unresolved HIGH priority pointers:
```sql
SELECT f.flag_label, f.registry_id, r1.word as source_word,
       f.cross_registry_id, r2.word as partner_word,
       f.description, f.raised_date
FROM wa_session_research_flags f
JOIN word_registry r1 ON r1.id = f.registry_id
LEFT JOIN word_registry r2 ON r2.id = f.cross_registry_id
WHERE f.flag_code = 'SD_POINTER'
  AND f.priority = 'HIGH'
  AND f.resolved = 0
ORDER BY f.raised_date, f.flag_label;
```

Claude Code query — pointers by partner registry (for cross-registry investigation):
```sql
SELECT f.flag_label, f.registry_id, r1.word as source_word,
       f.description
FROM wa_session_research_flags f
JOIN word_registry r1 ON r1.id = f.registry_id
WHERE f.flag_code = 'SD_POINTER'
  AND f.cross_registry_id = ?
  AND f.resolved = 0
ORDER BY f.priority DESC, f.flag_label;
```

---

## 6. The Packaging Architecture

### 6.1 The Division of Labour

| **Claude Code** | **Claude AI** |
|---|---|
| Queries `bible_research.db` for pointer records, verse evidence, and cross-registry data | Receives packaged data |
| Groups SD pointers by theme, partner registry, or cluster | Performs cross-registry analysis |
| Retrieves specific verse records, anchor verse sets, or dimension profiles on request | Asks targeted questions of the packaged data |
| Provides structured data packages | Produces synthesis documents |
| Does not interpret | Does not perform database operations |

### 6.2 The Fresh Eyes Principle

Session D synthesis is performed by a fresh Claude AI instance — one that receives packaged data without the accumulated recency bias of watching 212 words processed one by one. A fresh instance receiving the full SD pointer set and relevant word study extracts sees the cross-registry landscape with equal weight across the whole.

**The packaging must be neutral.** Claude Code's grouping of pointers (by theme, priority, partner registry) must not embed interpretive assumptions. The grouping is structural; the interpretation belongs to Claude AI in Session D.

### 6.3 Session D Input Package

A Session D investigation receives:
- The SD pointer records for the registries under investigation (from `wa_session_research_flags`)
- The word study publication documents for all implicated registries
- Specific verse records or anchor verse sets requested by Claude AI during the session
- Dimension index data for relevant groups where dimensional patterns are being investigated

The input package is assembled by Claude Code on researcher instruction. It is targeted — not the full programme corpus.

---

## 7. The Gate — When Session D Begins

Session D does not wait for the full programme to complete. Targeted investigations can begin as soon as meaningful SD pointer accumulation exists for a thematic cluster.

| **Gate condition** | **Description** |
|---|---|
| Minimum pointer base | At least 3–5 registries have reached Analysis Complete with SD pointers in the database for a thematic cluster. This provides cross-word visibility within a meaningful domain. |
| Pointer quality | The accumulated pointers include HIGH-priority records with specific verse evidence and clear analytical questions. Pointer accumulation without evidence is insufficient. |
| Researcher declaration | The decision to trigger a Session D investigation belongs to the researcher. Claude Code can surface candidate investigation clusters based on pointer density; the researcher decides when to proceed. |

**The gate is not programme completion.** The C17 cluster (compassion, mercy, grace) has 94 SD pointers in the database as of April 2026. A targeted C17 Session D investigation is possible now — before any other cluster has been worked.

**Full programme synthesis (Layer 6 Pass 3):** The final synthesis across all 212 words waits until the dataset is substantially complete. This is a researcher-declared threshold.

---

## 8. The Conceptual Word Register

The Conceptual Word Register captures modern inner-life vocabulary that has no direct Hebrew or Greek lexical equivalent but represents genuine inner-being realities the programme must account for.

### 8.1 The Three Categories

| **Category** | **Description** |
|---|---|
| Addressed narratively without a dedicated term | The biblical writers address the reality extensively — through narrative, theology — without a dedicated word. *Motive* is the clearest example. |
| Expressed through the semantic range of broader terms | The concept exists in the biblical world but is captured within broader terms. *Inspiration* (theopneustos, neshamah, ruach) is an example. |
| Modern analytical categories without direct biblical traction | Concepts that are modern organising tools rather than biblical realities — emotion, personality, self-awareness as named faculties. These require different handling at Session D. |

### 8.2 Home of the Register

The Conceptual Word Register is a Session D construct. It is not part of the main word registry and does not require Session A or Session B processing. Its research method is synthetic — drawing on multiple registries to map a concept that no single word names directly.

---

## 9. Methodological Commitments for Session D

These commitments were established during the March 2026 sessions and govern all Session D work:

**Data first.** Session D categories must emerge from the corpus data, not be imported from prior frameworks — including the Layer 0 documents.

**The concentric circles are scope only.** They do not explain interaction. What the inner being's structure looks like is what the data reveals.

**The spirit-soul-body framework is a hypothesis at Session D.** It may be confirmed, modified, or supplemented by the full corpus.

**Science engagement begins at Session D.** No scientific references appear in Session B analyses. When Session D engages neuroscience, psychology, or other fields, it does so as a comparative exercise — not as a framework into which biblical findings are fitted.

**Fresh eyes for synthesis.** Session D synthesis is performed by a fresh Claude AI instance receiving packaged data, not one that has accumulated recency bias across many word analyses.

**Pliability.** The methodology must remain genuinely open to revision at every stage. Session D should hold its conclusions lightly until the full corpus supports them.

**SD pointers are questions, not answers.** A Session D session that simply affirms the question in the pointer without investigating it has not done Session D work. The pointer is the entry point; the investigation is the work.

---

## 10. The Session D Process — How a Session Runs

### 10.1 Overview

A Session D investigation is triggered by a specific cluster or thematic question. It proceeds in four phases:

1. **Pointer clustering** — Claude Code groups the relevant SD pointers by theme, partner registry, and priority
2. **Question formulation** — Claude AI reads the pointer cluster and formulates specific investigation questions
3. **Database evidence retrieval** — Claude Code responds to Claude AI's targeted data requests
4. **Analysis and synthesis** — Claude AI performs the cross-registry analysis and produces the synthesis document

### 10.2 Phase 1 — Pointer Clustering

Claude Code assembles the pointer package:
- Query all unresolved SD pointers for registries in scope
- Group by: (a) shared partner registry, (b) thematic keyword in description, (c) priority
- Present as a structured cluster map showing: how many pointers implicate each partner, which pointers share common verses or terms, where the highest-priority observations concentrate

Claude Code does not interpret the clusters — it presents them structurally. Claude AI reads them fresh.

### 10.3 Phase 2 — Question Formulation

Claude AI reads the pointer cluster and determines:
- Which questions are most productive to investigate first (HIGH priority, most registries implicated, clearest verse evidence)
- What data would resolve or deepen each question
- Which questions may already be answerable from the word study documents in scope

Claude AI states its investigation plan explicitly before requesting data.

### 10.4 Phase 3 — Database Evidence Retrieval

Claude AI requests specific data; Claude Code retrieves it. Requests may include:
- Anchor verses for a specific group across multiple registries
- All verses where two specific Strong's numbers co-occur
- The dimension profile of a set of registries
- SD pointers from a partner registry that point back to the source registry
- The full context record set for a specific thematic group

Data requests are targeted, not bulk. Claude AI does not receive the full programme corpus in one pass — it asks for what the investigation requires.

### 10.5 Phase 4 — Analysis and Synthesis

Claude AI performs cross-registry analysis against the retrieved data. The analysis:
- States what the data shows — observations grounded in specific verses or term records
- Identifies structural patterns that no single word study could reveal
- Notes where the data confirms, complicates, or contradicts the pointer's question
- Raises new questions generated by the analysis (which become new SD pointers or Session D sub-questions)
- Does not import theological frameworks to fill gaps in the data

The output is a synthesis document:
- Filename: `wa-sd-[theme]-synthesis-v1-[date].md`
- One document per investigation cluster
- Contains: the investigation question, the data examined, the findings, the open questions, the new pointers generated

### 10.6 Marking Pointers Resolved

After a Session D investigation, Claude Code updates `wa_session_research_flags`:
- Set `resolved = 1` for pointers that were fully investigated
- Leave `resolved = 0` for pointers partially addressed or generating new sub-questions
- Insert new SD pointers for questions that arose during the investigation

---

## 11. What Still Needs to Be Designed

The following aspects of Session D require further development:

- The exact format and structure of synthesis output documents — currently specified in outline only (Section 10.5)
- The science engagement protocol — how neuroscience and psychology are introduced at Session D without importing their categories
- The relationship between Session D outputs and the Layer 0 framework documents — how new findings are integrated with or corrected against the foundational research
- The visualisation approach — how the inner-being framework that emerges is represented and communicated
- The final programme output — what the completed Framework B programme produces as its deliverable
- The protocol for the full programme synthesis pass — when all 212 words are complete

---

## 12. Current SD Pointer State — April 2026

As of the production of this document, the SD pointer record stands as follows:

| Registry | Cluster | SD Pointers | HIGH | MEDIUM | LOW |
|---|---|---|---|---|---|
| Grace (68) | C17 | 50 | 26 | 19 | 5 |
| Mercy (111) | C17 | 15 | 4 | 9 | 2 |
| Compassion (23) | C17 | 29 | 13 | 12 | 4 |
| **C17 total** | | **94** | **43** | **40** | **11** |

The C17 cluster is the first cluster with sufficient pointer density for a meaningful Session D investigation. The 43 HIGH-priority pointers across the three words represent the programme's current best candidates for first investigation. A targeted C17 Session D run is the next Session D priority when the researcher determines the time is right.

---

*WA-SessionD-Orientation-v3.0 | 20260412 | Supersedes v2.1-20260329 | Pool architecture retired; SD pointer mechanism formalised; Session D process specified; C17 pointer state documented*
