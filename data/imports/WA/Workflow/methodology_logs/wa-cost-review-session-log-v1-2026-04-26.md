# WA-Cost-Review-Session-Log-v1-2026-04-26

**File:** WA-cost-review-session-log-v1-2026-04-26.md  
**Date:** 2026-04-26  
**Session type:** Reflective / strategic review  
**Previous outputs:** VCB-008, VCB-010, VCB-011, VCB-013 session logs  

---

## 1. Purpose

Review of cost drivers across the last four working sessions (VCB-008, VCB-010, VCB-011, VCB-013), followed by a broader strategic conversation about the root cause of waste and the direction of architectural change.

---

## 2. Cost Pattern Analysis

### Patterns identified from session review

| Pattern | Cost Impact | Finding |
|---|---|---|
| Overlapping global rules reads (4–6 per session) | High | Same ranges read multiple times per session — directly wasteful |
| Full instruction reads every session | Medium | Required by rules but long files; version-check protocol proposed as alternative |
| Chat used as working surface instead of obslog | Medium | Pre-VCB-013 pattern; VCB-013 improved but not fully resolved |
| GR-CAD-001 self-checks | Low | Audit function — no change recommended |
| Natural-breakpoint session logs | Low | Correctly applied |

---

## 3. Root Cause — Researcher Assessment

**Researcher stated directly:**

The elaborate instruction architecture, the repetitive reads, the compensating rules — all are symptoms of Claude's failure to follow instructions consistently across sessions. The cost is not the reads themselves. The cost is the error, the correction, the instruction update, and the re-run that precede each new compensating rule.

Every instruction added to the global rules traces back to an actual execution failure.

---

## 4. Key Observations from the Conversation

### 4.1 Instruction documents written by Claude have not held
Not one instruction-type output produced by Claude has survived without requiring correction and revision. This is an established pattern, not an isolated finding.

### 4.2 Memory is unreliable by architecture
Claude does not persist between sessions. Every session begins from whatever is placed in the context window. The "whole" of the programme exists only in the researcher's mind and in the documents. Claude sees only a fragment at any time.

### 4.3 Where Claude adds genuine value
- **Thinking together** — exploratory, reflective, connective reasoning (this session is an example)
- **Coherent expression** — taking a concept and giving it clear, well-formed language

### 4.4 Where Claude consistently fails
- Sustained judgement across many steps in a session
- Self-directed procedure
- Consistency over time — paragraphs do not form a coherent whole because Claude does not carry the whole

### 4.5 The prose component insight
The researcher identified that pre-forming database output as markdown snippets — rather than asking Claude to assemble from raw tables — works. This is already partially implemented. The direction is correct. The scale problem (4000 verse context classifications) makes the current session overhead unviable.

### 4.6 The obslog failure pattern
Claude defaults to the chat as its natural output surface. Writing to the obslog is an additional deliberate act that erodes under task load. The instruction to write obslog-first competes with task content and does not win consistently. The solution is not a stronger instruction — it is removing the chat as a viable working surface by design.

### 4.7 The atomisation direction
The researcher has identified the architectural response:
- Global rules: already atomised in the database; needs an index to allow subset delivery
- Global rules prose: strip the fluff — deliver rule statements only
- Instructions: split into three distinct layers:
  - Process management (what happens in what order)
  - Context understanding (what the programme is and why)
  - Filter application (the actual classification or analytical rule)
- Obslog: the bible for all working content — not a record, the active surface

### 4.8 System prompt vs project files — structural distinction
**System prompt:** Processed before anything else. Ambient — Claude operates inside it before beginning work. Strongest constraint lever available.

**Project files:** Read via tool calls. Enter context as content. Compete with task content under load. Lose salience.

**Open question requiring empirical verification:** Whether project files in the Claude.ai project setup are injected at system-prompt precedence or content precedence. This is structurally important and should not be assumed — test empirically before designing around it.

---

## 5. Decisions and Direction

| Decision | Status |
|---|---|
| Researcher will not ask Claude to write its own instructions | Confirmed — established pattern of failure |
| Atomise session inputs — right information for right task | Direction confirmed |
| Extend prose component approach deliberately | Direction confirmed |
| Test system prompt precedence empirically | Open — researcher to experiment |
| Strip global rules prose; add index for subset delivery | Direction confirmed |
| Split instructions into three layers | Direction confirmed |
| Obslog enforcement by design, not instruction | Direction confirmed |

---

## 6. Open Questions

1. **System prompt precedence:** Does the Claude.ai project file injection operate at system-prompt level or content level? Requires empirical testing.
2. **Atomisation scope:** What is the right unit size for instruction subsets? 500 words was named as a target — needs validation against actual task types.
3. **Sequencing logic:** In an atomised architecture, what holds the sequencing between task atoms? This logic must live outside Claude.

---

## 7. Next Steps (Researcher-owned)

1. Digest this conversation
2. Experiment with system prompt as constraint lever
3. Progress atomisation of global rules — index for subset delivery
4. Strip prose from global rules — rule statements only
5. Design the three-layer instruction split
6. Extend prose component approach to instruction inputs, not just database outputs

---

## 8. Session Character

This was a thinking-together session. No classification work, no patch construction, no file operations beyond this log. The value was in the conversation itself — grounded in session evidence, honest about failure patterns, directed toward structural rather than symptomatic solutions.

---

*Session log produced at researcher's indication of session close.*  
*No deferred items. No in-flight work.*
