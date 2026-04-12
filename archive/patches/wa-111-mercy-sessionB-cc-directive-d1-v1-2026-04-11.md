# Session B — CC Directive D1
## Registry 111 — mercy
## Passes 1–3 Directives
## Version: v1 | 2026-04-11
## Governing instruction: WA-SessionB-Analysis-Instruction-v4.7-2026-04-11
## Delivery point: D1 — after Pass 3 PASS COMPLETE

---

## Context

This directive delivers all database operations generated during Passes 1, 2, and 3 of Stage 2 Session B for Registry 111 (mercy). Per the instruction's directive delivery discipline (Section 2.0b), delivery to Claude Code occurs only at D1 (after Pass 3) and D2 (after Pass 6). No other delivery points.

After these operations are applied and confirmed, Claude Code produces fresh extract R2. Pass 4 cannot begin until R2 is in hand and spot-checked.

---

## D1 Operations

### Operation D1-001 — GOD_AS_SUBJECT flag insertions (mti_term_flags)

Insert `mti_term_flags` records (flag_id = 1, GOD_AS_SUBJECT) for 13 terms where Pass 2 analysis confirmed God as the primary actor.

**SQL:**
```sql
-- flag_id 1 = GOD_AS_SUBJECT (confirmed from WA-Reference Section 13.3)
-- mti_term_id is the mti_terms.id value

INSERT OR IGNORE INTO mti_term_flags (mti_term_id, flag_id) VALUES
  (981,  1),  -- G1653 eleeō         — group 981-001 dominant_subject=GOD (Rom 9:15)
  (983,  1),  -- G1656 eleos         — group 983-001 dominant_subject=GOD (Eph 2:4)
  (3177, 1),  -- G2434 hilasmos      — group 3177-001 dominant_subject=GOD (1Jo 4:10)
  (3166, 1),  -- G2436 hileōs        — group 3166-001 dominant_subject=GOD (Heb 8:12)
  (992,  1),  -- G3628 oiktirmos     — group 992-001 God as Father of mercies (2Cor 1:3)
  (3158, 1),  -- G3629 oiktirmōn     — group 3158-001 "the Lord is compassionate" (Jam 5:11)
  (984,  1),  -- H2603A cha.nan      — group 984-001 God's gracious turning (Num 6:25)
  (982,  1),  -- H3727 kap.po.ret    — group 982-001 "I will meet with you" (Exo 25:22)
  (986,  1),  -- H3819 lo-ruhamah    — group 986-001 dominant_subject=GOD (Hos 1:6)
  (990,  1),  -- H5750 od            — group 990-002 dominant_subject=GOD (Hab 2:3)
  (988,  1),  -- H7359 ra.cha.min    — group 988-001 dominant_subject=GOD (Dan 2:18)
  (3169, 1),  -- H3722A kip.per      — group 3169-002 dominant_subject=GOD (Psa 78:38)
  (3173, 1);  -- H3722B ka.phar      — group 3173-002 dominant_subject=GOD (Eze 16:63)
```

**Verification:** After insert, confirm count:
```sql
SELECT COUNT(*) FROM mti_term_flags WHERE flag_id = 1
AND mti_term_id IN (981, 983, 3177, 3166, 992, 3158, 984, 982, 986, 990, 988, 3169, 3173);
-- Expected: 13
```

---

### Operation D1-002 — FRAMEWORK_SIGNAL phase2 flags (wa_term_phase2_flags)

Insert `wa_term_phase2_flags` records for terms where the divine-human relationship has direct implications for the spirit-soul-body classification. These terms receive `FRAMEWORK_SIGNAL` because the Pass 2 analysis identifies them as terms where mercy originates at the spirit level (received from God) or where the divine mechanism is the structural ground of mercy's operation.

**Terms:** G1656 eleos (mercy as divine attribute, ground of salvation), G2433 hilaskomai (divine provision of propitiation, direction reversal), G2434 hilasmos (Christ as the propitiation — divine provision), G2435 hilastērios (mercy seat / Christ as living propitiation), H3727 kap.po.ret (divinely designated meeting point).

**SQL:**
```sql
-- flag_code for FRAMEWORK_SIGNAL must be confirmed from phase2_flag_types table
-- If not present, use DIVINE_HUMAN_PARALLEL or THEOLOGICAL_ANCHOR as available alternatives

-- First confirm the flag_code exists:
SELECT id, flag_code, description FROM phase2_flag_types WHERE flag_code = 'FRAMEWORK_SIGNAL';

-- If confirmed, insert (term_inv_id from wa_term_inventory):
INSERT OR IGNORE INTO wa_term_phase2_flags (term_inv_id, flag_id, description, source, raised_date)
SELECT pt.id, pft.id, 
  'Divine-human relationship directly shapes spirit-soul-body classification for this term.',
  'Session B v4.7 Pass 2',
  '2026-04-11'
FROM wa_term_inventory ti
JOIN phase2_flag_types pft ON pft.flag_code = 'FRAMEWORK_SIGNAL'
WHERE ti.term_id IN ('G1656', 'G2433', 'G2434', 'G2435', 'H3727')
  AND ti.file_id = (SELECT id FROM word_registry WHERE no = 111);
```

**Note to CC:** If `FRAMEWORK_SIGNAL` is not in the `phase2_flag_types` table, substitute `DIVINE_HUMAN_PARALLEL` or `THEOLOGICAL_ANCHOR` and report which was used so Claude AI can update the observations log.

---

### Operation D1-003 — meaning_numbered update for G2433 hilaskomai

**Basis (DIR-MEAN-001 from Pass 1):** The current `meaning_numbered` for G2433 is null (prose-only). Pass 1 identified two structurally distinct senses that warrant explicit numbering: (1) the middle-voice sense (human act of making atonement/propitiation) and (2) the passive-voice sense (receiving mercy/being forgiven). Additionally, the classical-to-NT direction reversal is analytically significant and should be captured.

**Target table:** `wa_parsed_meaning` / `wa_meaning_senses` — or wherever `meaning_numbered` content is stored.

**CC Investigation required first:** Confirm which table stores `meaning_numbered` content and how it is structured. Then apply the following sense structure:

```
Sense 1 (middle voice): to make atonement for; to propitiate — the human act of providing the 
means for forgiveness, resulting in reconciliation (Heb 2:17: "to make propitiation for the sins 
of the people")

Sense 2 (passive voice): to receive mercy; to be forgiven; to have propitiation applied 
(Luk 18:13: "God, be merciful to me, a sinner" — the sinner's cry for propitiation to be turned 
toward him)

Classical note: In classical Greek, hilaskomai meant "to appease the gods" — always the human's 
act directed toward the divine. The NT radically inverts this direction: in 1Jo 4:10, it is God 
who sends the propitiation. The human passive of Luk 18:13 ("be propitious toward me") and the 
NT's attribution of the atoning act to God both reflect this inversion.
```

**SQL approach:** Query `wa_parsed_meaning` for `term_inv_id = 3311` (G2433) to see current structure, then update or supplement as appropriate.

```sql
SELECT * FROM wa_parsed_meaning WHERE term_inv_id = 3311;
-- Review current structure, then apply sense update per CC's best practice
```

---

## R2 Extract Request

After D1-001 through D1-003 are applied and confirmed, produce fresh extract R2:

```
CC DIRECTIVE — FRESH EXTRACT R2
Registry: 111 — mercy
Action: Produce fresh complete export
Filename: wa-111-mercy-complete-2026-04-11-r2.json
Reason: D1 directives (Passes 1–3) applied and confirmed. Pass 4 requires updated term data.
Confirm: 
  - mti_term_flags: 13 new GOD_AS_SUBJECT records present
  - wa_term_phase2_flags: FRAMEWORK_SIGNAL (or equivalent) records present for 5 terms
  - G2433 meaning_numbered: updated with middle/passive sense distinction
  - All other fields unchanged from R1
```

---

## D1 Delivery Summary

| Op | Type | Target | Count |
|---|---|---|---|
| D1-001 | SQL insert — mti_term_flags | 13 terms | flag_id=1 (GOD_AS_SUBJECT) |
| D1-002 | SQL insert — wa_term_phase2_flags | 5 terms | FRAMEWORK_SIGNAL (confirm flag_code first) |
| D1-003 | meaning_numbered update | G2433 hilaskomai | Middle/passive sense structure + classical note |

**Return to Claude AI:** Results of D1-001 and D1-002 confirmation queries, the FRAMEWORK_SIGNAL flag_code resolution, and filename of R2 extract.

---
