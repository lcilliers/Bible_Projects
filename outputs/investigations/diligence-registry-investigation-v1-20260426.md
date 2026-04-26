# Registry 48 diligence — investigation

_Date: 2026-04-26 · prompted by: "verse_context_status reset — does diligence have other terms that cover it?"_

---

## Headline

**No — the current term inventory of registry 48 does not cover the concept of diligence.** Of 6 active OWNER terms, only one (`H0629 os.par.na — "diligently"`, 7 verses) is genuinely on-topic. The other five are high-frequency Hebrew/Aramaic function words (extraction anomalies on the same pattern as the PH2_DATA_ERROR series elsewhere in the programme).

The classic NT diligence-family (`G4710 spoudē`, literally glossed by STEP as "diligence") is **not in this registry at all** — it sits in registry 181 zeal.

---

## Current term inventory — registry 48

### Active OWNER terms

| Strong's | Translit | Gloss | Lang | Verses | Real diligence content? |
|---|---|---|---|---:|---|
| H0608 | an.tun | "you" | H (Aramaic) | 1 | **No — Aramaic 2nd-pers pronoun** |
| **H0629** | **os.par.na** | **"diligently"** | **H (Aramaic)** | **7** | **Yes — only on-topic term** |
| H3606 | kol | "all" | H (Aramaic) | 61 | **No — Aramaic "all/every"** |
| H3635A | ke.lal | "to complete" | H | 7 | Marginal — "complete" not "diligent" |
| H3644H | ke.mo | "[Geruth] Chimham" | H | 1 | **No — proper-noun fragment** |
| H3660 | ke.ne.ma | "thus" | H | 5 | **No — adverbial "thus"** |

Plus deduplication-pending duplicates (mti_terms rows with `delete_flagged=1`) — the `mti_terms` dedup is a known open OT ([OT-DBR-009] still pending Action R). Not specific to diligence.

### XREF terms

| Strong's | Gloss | Verses (active/del) | Notes |
|---|---|---:|---|
| H3644G ke.mo | "like" | 0 / 126 | All XREF verses already `delete_flagged` — correctly scoped down |

### Status fields

| Field | Value | Issue |
|---|---|---|
| `verse_context_status` | **Complete** | **Wrong** — 0 active groups across all OWNER terms |
| `session_b_status` | Verse Context Reset | Indicates VC needs to be redone |
| `phase1_status` | Complete | **Wrong if the Phase 1 inventory is anomalous as the data suggests** |

The session_b_status / verse_context_status pair is internally contradictory: SB says reset, VC says Complete. The reset should propagate — VC status should be NULL or `In Progress`, not Complete.

---

## What "diligence" SHOULD include — STEP cross-reference

Common diligence-semantic Strong's:

| Strong's | Translit | STEP gloss | Currently in project? | If so, where? |
|---|---|---|---|---|
| **H2742** | cha.ruts | "sharp" / diligent | **Not in MTI at all** | — |
| H4106 | ma.hir | "quick" / skilful, diligent | Yes | **reg 61 fear** (anomalous placement) |
| **H8104** | sha.mar | "to keep: obey" / diligently keep | **Not in MTI at all** | — |
| **G4710** | spoudē | **"diligence"** (STEP's literal gloss) | Yes | **reg 181 zeal** (OWNER), reg 211 being (XREF) |
| G4704 | spoudazō | "be eager" / be diligent | Yes | reg 181 zeal (OWNER), reg 211 being (XREF) |
| G4705 | spoudaios | "eager" / diligent | Yes | reg 181 zeal (OWNER), reg 211 being (XREF) |
| **G4709** | spoudaiōs | "diligently" | **Not in MTI at all** | — |
| **G1567** | ekzēteō | "to seek out" / seek diligently | **Not in MTI at all** | — |

**Three observations from this:**

1. **The spoudē family is in registry 181 zeal.** STEP's primary gloss for `G4710` is literally "diligence" — yet in the project it's owned by zeal. Either (a) zeal/diligence are conflated and the project decided to handle them under one registry, (b) the spoudē family should XREF into diligence, or (c) the registry boundary itself needs review. This is the dominant finding — over half of what English readers think of as "diligence" lives elsewhere.
2. **At least four diligence-semantic Strong's are not in the project MTI at all** (H2742, H8104, G4709, G1567). Phase 1 discovery missed them.
3. **One Hebrew diligence term (H4106 mahir) is mis-placed** in registry 61 fear.

---

## What this means practically

### Resetting verse_context_status is correct but insufficient

A VC reset gets the status field honest, but it does not solve the underlying problem. With only `H0629` (7 verses) genuinely on-topic, classifying those 7 verses produces a registry that **still doesn't represent diligence as a concept** — it represents the lone Aramaic adverb meaning "diligently".

### The actual remediation has three layers

| Layer | Action | Cost |
|---|---|---|
| **L1 — VC status correction** | Reset `verse_context_status` to NULL or `In Progress` to remove the Complete-with-no-groups inconsistency. | Trivial — single UPDATE. |
| **L2 — Term inventory cleanup** | Mark the 5 HFA / proper-noun OWNER terms (`H0608`, `H3606`, `H3635A`, `H3644H`, `H3660`) for delete or candidate_delete. Same precedent as the H4639H/I disposition just applied. | Small — one REPAIR-style patch. |
| **L3 — Phase 1 re-discovery + cross-registry decision** | Decide whether the spoudē family (`G4710`, `G4704`, `G4705`) and `H4106` belong in diligence (move/XREF) or stay where they are; pull missing terms (`H2742`, `H8104`, `G4709`, `G1567`); confirm registry coverage represents the concept. | Largest — a registry-design decision plus Phase 1 STEP pull. |

### Reasonable next step

**L1 + L2 immediately**, deferring **L3** until you've decided the diligence-vs-zeal boundary:

- **L1:** UPDATE `word_registry` SET `verse_context_status = NULL` (or `'In Progress'`) WHERE `no = 48`. Aligns the field with the Verse Context Reset session_b_status.
- **L2:** Mark `H0608`, `H3606`, `H3635A`, `H3644H`, `H3660` (all HFA / function / proper-noun) as `mti_terms.status = 'delete'` with documented reason — same pattern as today's H4639H/I disposition. After this, registry 48 has a single OWNER term (H0629).
- **L3:** Open question for researcher decision: where should the diligence concept live, and what's the relationship to zeal (181)? This is a registry-architecture question, not a data fix.

---

## Side-finding (not blocking)

The H3644 family is partially deduplicated:
- `H3644G ke.mo` "like" — XREF in 48 (correctly scoped, all 126 verses delete_flagged)
- `H3644H ke.mo` "[Geruth] Chimham" — OWNER in 48 (proper-noun fragment, recommend delete)

This pattern (suffix-letter sub-glosses from STEP) is identical to the H4639X case resolved earlier today.
