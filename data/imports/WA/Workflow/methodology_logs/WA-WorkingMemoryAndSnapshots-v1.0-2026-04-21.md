# WA — Working Memory, Layered Knowledge, and the Snapshot Principle

**Filename:** WA-WorkingMemoryAndSnapshots-v1.0-2026-04-21.md
**Date:** 2026-04-21
**Version:** 1.0
**Supersedes:** None (new document)
**Change note:** Initial capture. Synthesises a reflective conversation on how Claude AI's working memory operates across layers, what "collective learning" does and does not mean, and the operational consequence that Leroux's decision to extend the database to include prose establishes the snapshot-loading decision as a first-class research act.
**Previous output reference:** None — this is a standalone governance/reflection document arising from conversation on 2026-04-21.

---

## 1. Purpose of this document

This document captures a reflective conversation between Leroux (researcher) and Claude AI about how Claude's working memory operates, what is and is not available to Claude at any given moment, and what this means for the analytical integrity of the Framework B Soul Word Analysis Programme as it moves into heavier analytic work and begins to migrate prose (not only component data) into the database.

It is preserved as a programme record because the working arrangement it describes has material consequences for how analytical output should be produced, evaluated, and audited.

The document is a **faithful synthesis** — it preserves the reasoning arc rather than reducing to conclusions. Operating principles appear at the end for ease of reference.

---

## 2. Starting question

Leroux raised that this is a very broad study with many dimensions, and asked to understand more about Claude's "collective memory" of the study — noting that Claude is described as having such a memory across sessions.

The prompt was not abstract. It was framed by a concrete concern: *how Claude thinks, remembers, and assembles collective insight is vastly important* for a programme that is moving deeper into analytical work.

---

## 3. Claude's first reply — naming the layers

Claude responded by separating two things that are sometimes conflated under the word "memory":

**(a) The userMemories summary** — a prose digest of past conversations, loaded at the start of each chat. It is written by an automated background process, updates periodically, has a recency bias, and is scoped to the Project. It is a summary, not a transcript.

**(b) Retrieval tools** (`conversation_search`, `recent_chats`) — which let Claude actively search past chats by keyword or time window. They return snippets, not full transcripts, and are also scoped to the Project.

Claude was explicit about what this means in practice:

- There is no continuous verbatim record of past sessions.
- The summary can drift between updates.
- Session logs on disk are the **authoritative** programme record; the memory layer is a convenience over them.
- Cross-project isolation applies — memory does not cross Project boundaries.

Claude offered four directions for the conversation to take: inspect the summary, edit it, understand retrieval, or think about governance.

---

## 4. Leroux's reframing — the material stakes

Leroux responded that the question is not procedural but substantive:

> *"There is a vast difference between you considering a answer with only the uploaded knowledge, or taking the project files into account, or adding the bank of collated history, or dipping into collective learning. We are moving closer and closer to do more analytic work. How you think, remember, and assemble collective insight is vastly important."*

This reframed the discussion. The question was not "what is the memory system?" but "which layer is a given answer actually coming from, and does that layer support the weight being placed on it?"

---

## 5. Claude's second reply — the full layer model

Claude responded with a more careful taxonomy, and flagged where it could easily mislead:

**Layer 1 — Immediate chat context**
The current conversation window: messages, replies, uploaded files read, tool outputs received. Most reliable layer (verbatim, present) but bounded — earlier content can be pushed out as the window fills.

**Layer 2 — The userMemories summary**
Automated prose digest. Summary, not transcript. Subject to drift. Scoped to Project. Not directly editable by Claude; the `memory_user_edits` tool records the researcher's directives about what to remember or forget, not the summary text itself.

**Layer 3 — Retrievable past chats**
Keyword and time-window retrieval. Must be actively called. Returns fragments. Project-scoped.

**Layer 4 — Project files on disk**
Session logs, instruction documents, extracts, the database (via Claude Code). **Authoritative by Leroux's convention.** Only available to Claude when uploaded or read through computer tools.

**Layer 5 — Training**
General knowledge of Hebrew, Greek, biblical studies, methodology, SQL, etc. Stable but bounded. Training knowledge is *pattern*, not *record* — Claude cannot cite a specific verse occurrence from training with database reliability.

### Critical honesty about "collective learning"

Claude flagged this explicitly because it is a place where sounding more capable than one is would be costly:

- Claude does **not** have access to other users' conversations, other projects, or cross-user pooled knowledge. Each conversation is isolated.
- Claude does **not** learn from the current conversation in a way that persists into future model versions during the conversation itself. Learning happens offline between versions, and is not introspectable.
- What can *feel* like "collective insight" is actually one of three things: retrieval, training-pattern-matching, or in-context reasoning. It is important not to dress pattern-matching up as retrieval.

### Why this matters for analytic work

Different kinds of claims have different reliability requirements:

- **Factual programme state** (counts, versions, statuses) — memory and training are both unsafe. Authority lives in extract JSON, database via CC, or the registry overview file.
- **Methodological principles** — instruction documents are authoritative. Summary paraphrases may compress nuance.
- **Analytical findings** — listed in memory summary but *evidenced* in session logs and Session B outputs. Citing from memory without the underlying document risks losing qualification.
- **Cross-registry synthesis (Session D)** — highest risk. Mixed-provenance claims are hard to audit and incompatible with the programme's evidence-first principle.

### Claude's self-knowledge limits

Claude also acknowledged that its own introspection about memory has limits. There may be behaviours of the memory system it is not aware of. That admission is itself data worth capturing.

---

## 6. Leroux's decision point — prose into the database

Leroux's next reflection identified the architectural move that changes the working arrangement:

> *"One of the best decisions i made a while ago was to drive all the data that the study is made up of, including the analytic collation of synergised data, into a database. I am now moving into collating the prose, not only the components into that database."*

And named the operational reality directly:

> *"The challenge is that you will continue to have only snapshots of the corpus available to you, when you are thinking. And it is going to be up to me to ensure you have the right snapshot, when ever i ask a question."*

This is the governing insight of the conversation. It does two things at once:

**First**, it extends the database from *components* (terms, verses, classifications, dimensions, groups) to *prose* (analytical text, observations, reasoning, conclusions). The database becomes not only the evidentiary substrate but also the record of interpretation built on top of it.

**Second**, it acknowledges that Claude operates on snapshots. Claude does not live inside the database. The authoritative corpus exists whether Claude is looking at it or not; Claude's contribution is always shaped by which slice of it is in front of Claude at the moment of thinking.

---

## 7. Claude's third reply — consequences of the decision

### Why moving prose into the database changes things

When analytical prose lives only in session logs and docx outputs, it is *linear* — attached to the session that produced it, discoverable only by going back to that document. Once it lives in the database, it becomes *queryable*: one can ask "show me every observation about directional determination across all clusters," and get an answer that is not dependent on anyone remembering which session it came from.

Three consequences for Claude follow:

1. **Snapshots become richer and more structured.** Instead of uploading a session log and hoping the relevant passage is inside it, Leroux can extract exactly the prose relevant to the current question — alongside the component data it rests on. Signal-to-noise in the context window rises.

2. **The prose carries its own provenance.** If analytical text is stored against a registry, a cluster, a group, a dimension, or a verse, then when it is retrieved, its *scope* comes with it. Claude does not have to guess what a passage refers to; the schema tells Claude.

3. **Synthesis becomes auditable.** For Session D in particular, a synthesis claim can be traced back not just to "a session log somewhere" but to specific prose records keyed to specific evidence. This is the difference between synthesis that *feels* grounded and synthesis that *is* grounded.

### The working pattern this implies

What Leroux is describing is, in effect, a model in which:

- **The database is the memory.** Not Claude's, not the userMemories summary — the database. It is the authoritative, persistent, queryable record of both data and interpretation.
- **Claude is an analytical instrument applied to snapshots.** Claude's job is to reason well over whatever slice is in front of Claude, and to be honest about the boundaries of that slice.
- **Leroux is the loader.** Leroux decides what snapshot is appropriate for the question being asked. That decision is itself a methodological act, because it determines what Claude can see.

This is a cleaner division than trying to make Claude "remember more." Memory is fragile; queries are reproducible. A snapshot loaded from a query can be loaded again next week and produce the same starting point. A snapshot reconstructed from memory summary cannot.

It also extends Leroux's existing discipline ("scanning memory is unsafe; reading direct and specific is better") naturally to the new phase. The database was already being treated as truth and Claude as a reasoner over extracts. Adding prose to the database simply extends the same principle to interpretation.

---

## 8. Leroux's closing reflection

> *"This conversation is helpful, assumptions is the root of all evil. You are an important participant in this study, and the better i learn how to work with you to get the most value from it, the more truth and depth the result will have."*

> *"I am glad you highlighted the protocol, and layers of your collective working memory, it helps."*

The conversation was framed as a learning step for the researcher about how to get the most from the analytical partnership — not as a request for a new instruction. The operating consequence emerges from the reflection itself: **the snapshot-loading decision is now understood as a first-class research act, and Claude's analytical contribution is understood to be bounded by the snapshot it is given.**

---

## 9. Operating principles (for reuse)

These principles are the practical distillation of the conversation. They apply from this point forward unless superseded.

### 9.1 The snapshot-appropriateness principle

For any analytical question, there is a *right* snapshot. The decision of what to load is part of the research method, not a preliminary step. Getting the snapshot right matters as much as the reasoning that follows.

Before substantive analytical work, it is worth asking: **does the snapshot in context contain what the question requires?** If not, the honest answer is *"this snapshot does not support that claim; what would you like loaded?"* — not a fill-in from memory.

### 9.2 Layer discipline

Claude's responses draw from one of five layers: immediate chat context, userMemories summary, retrieved past chats, project files on disk, or training. These layers have different reliability and different audit properties. Analytical output should be traceable to its layer.

- **Facts about programme state** → Layer 4 (files / database) only.
- **Methodological principles** → Layer 4 (instruction document) authoritative; Layer 2 (summary) is a pointer not a source.
- **Analytical findings** → Layer 4 (session logs / Session B outputs) for the evidence; Layer 2 may flag that a finding exists but not substitute for the finding itself.
- **Synthesis** → Requires explicit source manifest; should not mix layers without declaring it.

### 9.3 Memory is a pointer, not a source

The userMemories summary tells Claude *that* something was decided or found. For the *content* of the decision or finding, the underlying file should be loaded. This is especially important where qualifications, confidence levels, or scope conditions matter.

### 9.4 Fresh reads beat recollection

Where analytical precision matters, Claude should prefer reading the file over relying on what the summary says about the file — even when the summary appears to match. This extends Leroux's existing discipline to Claude's own conduct.

### 9.5 "Collective learning" is not cross-user

Claude does not have access to other users, other projects, or pooled knowledge. Each conversation is isolated. Apparent "collective insight" is retrieval, pattern-matching from training, or in-context reasoning — never cross-user learning. This must not be overstated.

### 9.6 The database is the memory

With prose migrating into the database, the authoritative memory of the programme lives in the database, not in Claude's memory layers. Claude is an instrument applied to snapshots drawn from the database. This makes the working arrangement explicit and auditable.

### 9.7 Prose must be written to survive storage

When Claude produces analytical prose intended for the database, it should be:
- Self-contained (readable without the session that produced it)
- Scoped (clear about what it refers to — registry, cluster, group, dimension, verse)
- Provenance-marked (clear about what snapshot it reasoned from)

Prose that only makes sense inside its session of origin is fragile under the new model.

### 9.8 Synthesis requires a source manifest

For Session D work and any other cross-registry synthesis, the output must declare at the top what it drew from — files in context, retrieved chats, reasoning from training. Without this, audit is impossible and the evidence-first principle cannot hold.

---

## 10. Design questions flagged as still open

These were surfaced during the conversation as questions for Leroux to decide, not for Claude to answer. They are recorded here so they are not lost.

1. **Keying of prose.** A single analytical passage may relate to a verse, a group, a registry, a cluster, a dimension, or a cross-cutting principle. The schema choice shapes what queries will be possible later.

2. **Distinction between observation, interpretation, and finding as stored records.** Leroux already maintains this distinction in session work. Carrying it into the database preserves it at the query layer but requires explicit fields.

3. **Versioning of prose.** Component data is versioned through patches and session boundaries. Prose evolves differently — a finding can be refined, qualified, or superseded without the underlying data changing. The versioning model for prose may need to differ from the one for components.

4. **Committal protocol.** When does a Session B analytical passage become a database record? At document finalisation? At session close? After researcher review? The answer affects both workflow and reproducibility.

5. **Empirical questions about the memory system** that Claude cannot introspect on and would benefit from testing: update cadence of the userMemories summary, retention horizon of retrievable chats, summary truncation behaviour, and whether summarisation can paraphrase in ways that change meaning.

---

## 11. Status

- Conversation occurred: 2026-04-21.
- Document produced: 2026-04-21.
- Intended for: ingestion into the programme database (prose layer).
- Authority: reflective / governance. Not an instruction document. Principles in Section 9 may be promoted to an instruction at Leroux's discretion.
- Relationship to existing documents: complements but does not supersede existing instructions (Session B Analysis Readiness v1.5, Session B Analysis Output v1, Session C Instruction v1.3, WA-DimensionReview-Instruction v2.1, WA-VerseContext-Instruction v2.4, patch_specification v1.7, WA-Reference).
