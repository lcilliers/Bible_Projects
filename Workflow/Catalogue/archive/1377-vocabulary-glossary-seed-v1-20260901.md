# Vocabulary/glossary — seed list

> New escalation. Seeded from the now-closed #1007 (catalogue exploration) and the open #1376
> (characteristic-model cross-db reconciliation). Purpose: pull together every project term that
> has come up loose/ambiguous/undefined across that work into one candidate list — **not** to
> define each one here. Whether this becomes its own mechanism or folds into `cfg_enum` is the
> open question this escalation exists to settle (see "Open question" below); nothing here decides
> that.

## Terms already given a working definition (carried over from #1376's own glossary)

[`1376-characteristic-tables-cross-db-inventory-v2-20260901.md`](1376-characteristic-tables-cross-db-inventory-v2-20260901.md)
started a "Terminology (growing list)" section as it went. Reproduced here as-is, not redefined:

| Term | As used in that study |
|---|---|
| **inner-being characteristic** | The programme's own filter-concept — what qualifies a word for the registry at all. |
| **HIB** | Human Inner Being — a named or implicit *human* narrative subject (`iba.db hib`). A non-human being can never be registered as a HIB. |
| **phenomenon** | IBA's live term for a characteristic *in operation* — one HIB's state/disposition, evidenced in one verse (`iba.db phenomenon`). A per-occurrence reading, not a catalog entry. |
| **operation** | The movement/behaviour registered against one phenomenon (`iba.db operation`). |
| **cluster** | A top-level thematic grouping, keyed on an M-code (or T2/T3/FLAG). |
| **cluster_code** | The stable string key for a cluster (e.g. `M04`, `T3`, `FLAG`). |
| **characteristic** (Model A sense) | A named, hand-defined trait belonging to a cluster — an abstract catalog entry, not tied to a verse (`bible_research.db characteristic`). |
| **family** (Model B sense) | `ib_characteristic`'s own grouping concept, derived by book, not by cluster. |
| **cluster_subgroup / characteristic_subgroup** | An abandoned sub-division attempt — built on lemma, not span. |
| **T2 (Supplementary)** | Strong's codes assigned to a cluster process but carrying no inner-being relation. |
| **T3 (Operations)** | Strong's codes for a human operation/movement not tied to one cluster, or applying across many. |
| **FLAG** | Flagged for review — deliberately rare. |
| **HIGH / MEDIUM / LOW** | Confidence tiers from the Model A cluster-allocation process. |
| **descriptor** | A T2 item reading as inner-being content but rarely analysed alone. |

## Candidate terms with NO settled definition yet (surfaced under #1007)

Pulled from the catalogue exploration's own documents and this session's discussion. Each of
these has been *used* — sometimes with conflicting senses across documents — but never pinned
down in one place.

| Term | Where it came up | Why it needs a definition |
|---|---|---|
| **scope** (`wa_obs_question_catalogue.scope`) | #1007, #1374/#1375 | Just repurposed from an old universal/Leviticus-marker meaning to the new Scope-focus bucket meaning — the two meanings coexisted confusingly until #1375's correction; the word itself still gets used loosely for both the column and the general English sense. |
| **Scope focus** (the 8 buckets) | `1007-tier-catalogue-scope-focus-v3-20260831.md` | Word/term (lexical), Characteristic (HIB behaviour), Characteristic relational, Characteristic (what it is) [proposed, unconfirmed], The HIB, Verse-context, Other non-human beings, The verse, Science — bucket boundaries were revised three times (v1→v2→v3) precisely because the working definitions weren't fixed going in. |
| **source** (`wa_obs_question_catalogue.source`) | `1007-word-term-lexical-source-v1-20260831.md` | New column, distinct from `scope` — "what the answer is derived from." Not yet stated as a formal definition anywhere outside that one doc's own framing. |
| **tier / T-code** | Whole catalogue (T0–T7) | Used throughout without one canonical statement of what a "tier" *is* as opposed to a cluster, a component, or a bucket. |
| **span** | `span` table, `verse_lexical.span_id` | One verse-position's row — distinct from "term" and from "surface." |
| **surface** | `span.surface` | The literal word/phrase text at a span — distinct from the Strong's-coded term it resolves to. |
| **term** | Used everywhere, loosely | Sometimes means a Strong's-coded lexical entry, sometimes means `word_registry.word` (the English registry word), sometimes used interchangeably with "word" or "span" — the three are not the same object. |
| **word** (as distinct from span/term) | Throughout | Same ambiguity as "term" — needs its own boundary stated against span and term. |
| **content / function** (`verse_lexical.role`) | Live schema | A linguistic classification (content word vs. function word/particle) — easy to mistake for an inner-being-relatedness judgment, which it is NOT. |
| **resolved / unregistered / content_resolved** (`verse_lexical.status`) | Live schema | Whether a span is lexically matched/onboarded — again easy to conflate with "has this been analysed for IB relevance," which it does not track. |
| **inner-being-related (IB-related)** | This session's discussion | Used constantly in conversation; **no field anywhere in the schema currently represents it** — confirmed gap, not yet even a defined term, let alone a mechanism. |
| **Layer A / Layer B** | `1007-tier-catalogue-iba-raw-data-mapping-v2-20260831.md` Part 2 | Layer A = the base lexical layer (word/Strong's-keyed); Layer B = the debate/phenomenology layer (HIB/passage-keyed, minimally populated) — a real, useful distinction coined in that doc, not yet a project-wide term. |
| **Phase 1 / Phase 2** | This session's chat only | Phase 1 = surface/word-level analysis; Phase 2 = characteristic-rollup, verse-context analysis. Coined live this session (2026-09-01), not written up anywhere durable yet. |
| **verse-context** | Ambiguous across two databases | Used as (a) a Scope-focus bucket label (this catalogue work) AND (b) `bible_research.db`'s actual `verse_context`/`verse_context_group` tables (a pre-existing, different mechanism) — same phrase, two different referents, real collision risk. |
| **model** (Model A/B/C/D) | `1376-characteristic-tables-cross-db-inventory-v2` | Informal labels invented for this one document to distinguish the four characteristic mechanisms — not project-standard names; worth deciding whether they graduate to real names or stay document-local shorthand. |

## Open question (not resolved here — the reason this is its own escalation)

Whether this vocabulary work belongs inside `cfg_enum` (`governance.project_lookups_and_naming_convensions`
— "project-specific naming in lookups, stages, and terms with specific meaning must be defined in
`cfg_enum`... a missing definition must be escalated") or is a genuinely separate mechanism.
Researcher's own framing: initially assumed it would intersect with `cfg_enum`, but now sees a
case for keeping it separate. `cfg_enum` as it exists today governs **column-value vocabularies**
(e.g. a status/state enum with a fixed set of legal values) — most of the terms above are not
column values at all; they're **concepts used in prose, code comments, and conversation**
(`characteristic`, `phenomenon`, `span` vs `term` vs `word`, `Phase 1/2`). Whether that distinction
is enough to justify a separate mechanism, or whether `cfg_enum` should simply be widened to cover
both, is the actual decision this escalation is for.
