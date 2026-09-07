# wa-cluster-M05-dir-011-followup-v1-20260507

> Cluster-process directive — Follow-up resolution for DIR-004 through DIR-010 outstanding items
> Pattern: wa-directive-instruction-v1_4-20260506 §11.4
> Sequence: dir-011 in the M05 cluster directive sequence
> Produced by: Claude AI — Session B Phase 7 | 20260507
> Source: CC application report (DIR-004 through DIR-010) + wa-obslog-M05-love-compassion-kindness-v1-20260507 Phase 7

---

## DIRECTIVE ID

`DIR-20260507-M05-011`

---

## MOTIVATION

The application of DIR-004 through DIR-010 left four items requiring AI analytical input before they can be resolved. All four are now resolved and this directive applies them in a single pass:

1. **Group 1542 (agapē, mti=562)** — anchor 1Jo 4:8 did not resolve (mti=562 not present in DB for that verse). Alternative anchor provided: Rom 5:8 (vr=4943, mti=562, Group 1542, G-status).

2. **Group 1271 (an.vah, H6037, mti=188)** — anchor 2Sa 22:36 has no wa_verse_records row for mti=188. CC suggested parallel Psa 18:35 (vr=3741, mti=188). Confirmed correct.

3. **Group 3602 (anochē, G0463, mti=7502)** — mti=7502 has 0 rows in wa_verse_records. Group cannot have an anchor until extraction is run. Anchor left unset; any spurious verse_context rows in group 3602 that do not belong to mti=7502 should be investigated and reported.

4. **Group 1583 split (H2617A che.sed, mti=536)** — per-verse routing supplement provided for all 115 verses (59 → 1583-a, 56 → 1583-b). Full routing table in §SCOPE.

**Additional items from residual verse check:**
5. **Group 629 residual (5 verses)** — routing of Deu 13:8, Job 20:13, Pro 6:34, Isa 9:19, Zec 11:5 to 629-a or 629-b provided.
6. **Group 604 residual (1 verse)** — routing of 1Cor 4:13 (vr=59217) to 604-a or 604-b provided.

---

## SCOPE

**Cluster:** M05
**Tables:** `verse_context` (is_anchor updates; group_id updates for routing)
**No new group rows required.**
**wa_session_b_findings:** Not touched.

---

## OPERATION 1 — Anchor for Group 1542

**Action:** Set `is_anchor=1` on the verse_context row for vr=4943 (Rom 5:8, mti=562, group_id=1542).

Confirm that no other row in group 1542 has `is_anchor=1` before setting. Clear any existing stale anchor in group 1542 first.

**Rationale:** Rom 5:8 — "God shows his love for us in that while we were still sinners, Christ died for us" — uses the agapē noun (mti=562), is in Group 1542, has G-status, and is the most definitive statement of God's love as the ground and source: love demonstrated through the cross, directed toward the undeserving, the origin of all that follows.

---

## OPERATION 2 — Anchor for Group 1271

**Action:** Set `is_anchor=1` on the verse_context row for vr=3741 (Psa 18:35, mti=188 H6037 an.vah, group_id=1271).

Confirm mti=188 and group_id=1271 on vr=3741 before setting. Clear any stale anchor in group 1271 first.

**Note:** Psa 18:35 is the Psalter version of 2Sa 22:36 (David's song). Text: "You have given me the shield of your salvation, and your right hand supported me, and your gentleness made me great." Identical analytical content; vr=3741 is confirmed present in the DB.

---

## OPERATION 3 — Group 3602 (anochē) — anchor deferred

**Action:** No anchor operation. Leave group 3602 with `is_anchor=0` on all rows.

**CC pre-flight:** Query `SELECT id, vr_id, mti_term_id FROM verse_context WHERE group_id = 3602`. If any rows have `mti_term_id != 7502`, report them — they do not belong to this group and should be investigated. Do not delete them; report only.

**Next step (for researcher):** mti=7502 (G0463 anochē) requires a STEP extraction pass before an anchor can be set. This is deferred to a future session.

---

## OPERATION 4 — Group 1583 split: per-verse routing

**Action:** For each vr_id below, update `verse_context.group_id` from 1583 to the new group id:
- The new group created for 1583-a: CC to look up its id by `group_code = '536-001-a'` (or whatever code was assigned during DIR-004 application)
- The new group created for 1583-b: CC to look up its id by `group_code = '536-001-b'`

**Pre-flight:** Confirm group ids for 1583-a and 1583-b by querying `verse_context_group WHERE group_code IN ('536-001-a', '536-001-b')`.

**Set anchors after routing:**
- 1583-a anchor: vr=4097 (Lam 3:22, mti=536) → `is_anchor=1`
- 1583-b anchor: vr=3886 (Exo 15:13, mti=536) → `is_anchor=1`

**Full routing table — 115 verses (vr_id | reference | target group):**

| vr_id | Reference | Target |
|---|---|---|
| 3875 | Gen 19:19 | 1583-b |
| 3878 | Gen 24:12 | 1583-b |
| 3879 | Gen 24:14 | 1583-b |
| 3880 | Gen 24:27 | 1583-b |
| 3882 | Gen 32:10 | 1583-b |
| 3883 | Gen 39:21 | 1583-b |
| 3886 | Exo 15:13 | 1583-b |
| 3887 | Exo 20:6 | 1583-a |
| 3888 | Exo 34:6 | 1583-a |
| 3889 | Exo 34:7 | 1583-a |
| 3891 | Num 14:18 | 1583-a |
| 3892 | Num 14:19 | 1583-b |
| 3893 | Deu 5:10 | 1583-a |
| 3894 | Deu 7:9 | 1583-a |
| 3895 | Deu 7:12 | 1583-b |
| 3906 | 2Sa 2:6 | 1583-b |
| 3908 | 2Sa 7:15 | 1583-b |
| 3913 | 2Sa 15:20 | 1583-b |
| 3915 | 2Sa 22:51 | 1583-b |
| 3917 | 1Ki 3:6 | 1583-b |
| 3918 | 1Ki 8:23 | 1583-a |
| 3920 | 1Ch 16:34 | 1583-a |
| 3921 | 1Ch 16:41 | 1583-a |
| 3922 | 1Ch 17:13 | 1583-b |
| 3924 | 2Ch 1:8 | 1583-b |
| 3925 | 2Ch 5:13 | 1583-a |
| 3926 | 2Ch 6:14 | 1583-a |
| 3927 | 2Ch 6:42 | 1583-b |
| 3928 | 2Ch 7:3 | 1583-a |
| 3929 | 2Ch 7:6 | 1583-a |
| 3930 | 2Ch 20:21 | 1583-a |
| 3934 | Ezr 3:11 | 1583-a |
| 3935 | Ezr 7:28 | 1583-b |
| 3936 | Ezr 9:9 | 1583-b |
| 3937 | Neh 1:5 | 1583-a |
| 3938 | Neh 9:17 | 1583-a |
| 3939 | Neh 9:32 | 1583-a |
| 3941 | Neh 13:22 | 1583-b |
| 3945 | Job 10:12 | 1583-b |
| 3946 | Job 37:13 | 1583-a |
| 3947 | Psa 5:7 | 1583-a |
| 3948 | Psa 6:4 | 1583-b |
| 3949 | Psa 13:5 | 1583-a |
| 3950 | Psa 17:7 | 1583-b |
| 3951 | Psa 18:50 | 1583-b |
| 3952 | Psa 21:7 | 1583-b |
| 3953 | Psa 23:6 | 1583-a |
| 3954 | Psa 25:6 | 1583-a |
| 3955 | Psa 25:7 | 1583-b |
| 3956 | Psa 25:10 | 1583-a |
| 3957 | Psa 26:3 | 1583-a |
| 3958 | Psa 31:7 | 1583-b |
| 3959 | Psa 31:16 | 1583-b |
| 3960 | Psa 31:21 | 1583-b |
| 3961 | Psa 32:10 | 1583-a |
| 3962 | Psa 33:5 | 1583-a |
| 3963 | Psa 33:18 | 1583-a |
| 3964 | Psa 33:22 | 1583-b |
| 3965 | Psa 36:5 | 1583-a |
| 3966 | Psa 36:7 | 1583-a |
| 3967 | Psa 36:10 | 1583-b |
| 3968 | Psa 40:10 | 1583-b |
| 3969 | Psa 40:11 | 1583-a |
| 3970 | Psa 42:8 | 1583-a |
| 3971 | Psa 44:26 | 1583-b |
| 3972 | Psa 48:9 | 1583-a |
| 3973 | Psa 51:1 | 1583-b |
| 3974 | Psa 52:1 | 1583-a |
| 3975 | Psa 52:8 | 1583-a |
| 3976 | Psa 57:3 | 1583-b |
| 3977 | Psa 57:10 | 1583-a |
| 3978 | Psa 59:10 | 1583-b |
| 3979 | Psa 59:16 | 1583-a |
| 3980 | Psa 59:17 | 1583-a |
| 3981 | Psa 61:7 | 1583-b |
| 3982 | Psa 62:12 | 1583-a |
| 3983 | Psa 63:3 | 1583-a |
| 3984 | Psa 66:20 | 1583-b |
| 3985 | Psa 69:13 | 1583-b |
| 3986 | Psa 69:16 | 1583-b |
| 3987 | Psa 77:8 | 1583-a |
| 3988 | Psa 85:7 | 1583-b |
| 3989 | Psa 85:10 | 1583-a |
| 3990 | Psa 86:5 | 1583-a |
| 3991 | Psa 86:13 | 1583-b |
| 3992 | Psa 86:15 | 1583-a |
| 3993 | Psa 88:11 | 1583-a |
| 3994 | Psa 89:1 | 1583-a |
| 3995 | Psa 89:2 | 1583-a |
| 3996 | Psa 89:14 | 1583-a |
| 3997 | Psa 89:24 | 1583-b |
| 3998 | Psa 89:28 | 1583-b |
| 3999 | Psa 89:33 | 1583-b |
| 4000 | Psa 89:49 | 1583-b |
| 4001 | Psa 90:14 | 1583-b |
| 4002 | Psa 92:2 | 1583-a |
| 4003 | Psa 94:18 | 1583-b |
| 4084 | Isa 16:5 | 1583-a |
| 4086 | Isa 54:8 | 1583-b |
| 4087 | Isa 54:10 | 1583-a |
| 4088 | Isa 55:3 | 1583-b |
| 4090 | Isa 63:7 | 1583-b |
| 4092 | Jer 9:24 | 1583-a |
| 4094 | Jer 31:3 | 1583-b |
| 4095 | Jer 32:18 | 1583-a |
| 4096 | Jer 33:11 | 1583-a |
| 4097 | Lam 3:22 | 1583-a |
| 4098 | Lam 3:32 | 1583-b |
| 4099 | Dan 1:9 | 1583-b |
| 4100 | Dan 9:4 | 1583-a |
| 4101 | Hos 2:19 | 1583-b |
| 4107 | Joe 2:13 | 1583-a |
| 4109 | Jon 4:2 | 1583-a |
| 4111 | Mic 7:18 | 1583-a |
| 4112 | Mic 7:20 | 1583-b |

**Total: 115 verses (59 → 1583-a, 56 → 1583-b). Every row in Group 1583 must be routed. If CC finds any vr_ids in Group 1583 not listed in this table, halt and report them before proceeding.**

---

## OPERATION 5 — Group 629 residual verses (5 verses)

Route the following vr_ids from Group 629 to 629-a or 629-b:

| vr_id | Reference | Verse summary | Target |
|---|---|---|---|
| 1569 | Deu 13:8 | "shall not spare him" — commanded withholding of compassion toward the idolater; covenantal judicial context | 629-b |
| 59047 | Job 20:13 | "though he is loath to let it go" — cha.mal in the sense of unwillingness to relinquish something held; not a compassion-toward-person instance; context is Zophar's speech about the wicked hoarding sin | 629-b (judicial / not genuine compassion) |
| 59054 | Pro 6:34 | "he will not spare when he takes revenge" — cha.mal as the absence of mercy in the context of jealous anger; judicial/punitive context | 629-b |
| 59040 | Isa 9:19 | "the land is scorched and the people are like fuel for the fire; no one spares his brother" — cha.mal in a context of social breakdown; the absence of compassion as a symptom of judgment | 629-b |
| 59055 | Zec 11:5 | "those who buy them slaughter them and go unpunished, and those who sell them say 'Blessed be the Lord, I have become rich'; and their own shepherds do not spare them" — cha.mal withheld; shepherds without compassion for their flock | 629-b |

**All 5 residual verses → 629-b.** None evidences genuine positive human compassion toward a person in need.

---

## OPERATION 6 — Group 604 residual verse (1 verse)

| vr_id | Reference | Verse text | Target |
|---|---|---|---|
| 59217 | 1Cor 4:13 | "when slandered, we entreat (parakaleō). We have become, and are still, like the scum of the world" | 604-a |

**Rationale:** 1Cor 4:13 uses parakaleō in the sense of Paul's apostolic response to slander — he entreats rather than retaliates. This is the pastoral-apostolic inner disposition (suffering with grace, not coercing) and belongs with the pastoral register of 604-a, not the social-request register of 604-b.

---

## OUTCOME REQUIRED

1. Group 1542: exactly 1 anchor row (vr=4943, Rom 5:8); no other anchor in the group.
2. Group 1271: exactly 1 anchor row (vr=3741, Psa 18:35); no other anchor.
3. Group 3602: 0 anchor rows; any non-mti=7502 rows in the group reported (not deleted).
4. Groups 1583-a and 1583-b: all 115 vr_ids from Group 1583 redistributed per the table above; each new group has exactly 1 anchor row; Group 1583 (original) has 0 rows remaining.
5. Group 629 residuals: 5 vr_ids moved from 629 to 629-b; Group 629 has 0 rows remaining.
6. Group 604 residuals: vr=59217 moved from 604 to 604-a; Group 604 has 0 rows remaining.
7. wa_session_b_findings row count: unchanged.

---

## COMPLETION CONFIRMATION

```sql
-- Anchor check for Groups 1542 and 1271
SELECT vcg.id, vcg.group_code, vc.vr_id, vc.is_anchor
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id = vcg.id
WHERE vcg.id IN (1542, 1271, 3602)
AND vc.is_anchor = 1;
-- Expected: rows for 1542 (vr=4943) and 1271 (vr=3741); nothing for 3602

-- 1583 split confirmation
SELECT vcg.group_code, COUNT(vc.id) AS verse_count, SUM(vc.is_anchor) AS anchors
FROM verse_context_group vcg JOIN verse_context vc ON vc.group_id = vcg.id
WHERE vcg.group_code IN ('536-001-a', '536-001-b')
GROUP BY vcg.group_code;
-- Expected: 536-001-a → 59 verses, 1 anchor; 536-001-b → 56 verses, 1 anchor

-- Original Group 1583 emptied
SELECT COUNT(*) FROM verse_context WHERE group_id = 1583;
-- Expected: 0

-- 629 and 604 residuals cleared
SELECT COUNT(*) FROM verse_context WHERE group_id IN (629, 604);
-- Expected: 0

-- Group 3602 investigation (non-7502 rows)
SELECT id, vr_id, mti_term_id FROM verse_context WHERE group_id = 3602;
-- Report all rows; flag any where mti_term_id != 7502
```

Application report: `Sessions/Session_Clusters/M05/WA-M05-dir011-followup-applied-v1-20260507.md`

---

*wa-cluster-M05-dir-011-followup-v1-20260507 | Researcher approval required before CC executes*
