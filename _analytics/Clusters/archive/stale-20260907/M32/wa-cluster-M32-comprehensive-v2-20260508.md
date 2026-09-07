# M32 Conscience and Self-Awareness — comprehensive term + verse exposure

**Generated:** 2026-05-08T03:21:43Z  
**Cluster:** `M32` (bucket=NAMED, status=Analysis - In Progress, version=v6)  
**Source:** `database/bible_research.db`  

**Scope of this report:** every database fact that connects to a term in this cluster, exposed by term and by verse. Items currently linked only at registry / collection level (not yet resolvable to a specific term) are listed in the appendix as candidates for future linkage. Numbered paragraphs are used throughout to make every item directly referenceable.

---

## §1. Cluster summary

1. Description: Conscience and Self-Awareness
2. Bucket / Status / Version: NAMED / Analysis - In Progress / v6
3. Last updated: 2026-05-08T03:20:43Z
4. Terms in cluster: **6** (Hebrew 1 · Greek 5)
5. Active OWNER verses (sum across terms): 17
6. Contributor registries: 5

**Verse status summary** (17 active verses)

| Status | Count | % | Meaning |
|---|---:|---:|---|
| G | 17 | 100.0% | group-assigned (analysed) |
| SA | 0 | 0.0% | set-aside (with reason) |
| NR | 0 | 0.0% | not-relevant (is_relevant=0) |
| P | 0 | 0.0% | pending (relevant but no group yet) |
| UT | 0 | 0.0% | untouched (no verse_context row) |
| **Total** | **17** | 100% | |

**By testament:** OT 7 · NT 10

7. Gloss list (6 entries — every distinct term currently in the cluster, disambiguated by transliteration):

be aware (suneidō), be conscious of (sunoida), heart-knower (kardiognōstēs), self-condemned (autokatakritos), to reflect on (enthumeomai), to set: consider (shit)

**Patch-authoring reference table:** integer values per term for the patch's `_patch_meta.terms_covered` (mti_id) and `_patch_meta.input_versions` (md_version). Sorted by Strong's.

| Strong's | Translit | mti_id | md_version | vc_status |
|---|---|---:|---:|---|
| G0843 | autokatakritos | 4848 | 1 | not_done |
| G1760 | enthumeomai | 3392 | 2 | vc_completed |
| G2589 | kardiognōstēs | 599 | 1 | not_done |
| G4894 | suneidō | 454 | 1 | not_done |
| G6083 | sunoida | 2739 | 1 | not_done |
| H7896K | shit | 3578 | 1 | not_done |

8. Sub-group breakdown (3 sub-groups, 6 terms assigned):

| Sub-group | Label | Terms | Description |
|---|---|---:|---|
| `M32-A` | Conscience | 2 | The faculty by which the person assesses their own moral state — inner knowing of one's own moral standing, complicity, or condition; operating under the awareness that God's judgment is the higher court |
| `M32-B` | Self-Awareness / Inner Attention | 1 | The directed inner act of setting attention — deliberate cognitive engagement and attending carefully to a matter, person, or situation; the attentiveness capacity that underlies conscience |
| `M32-BOUNDARY` | BOUNDARY | 3 | Supporting terms that contextualise the conscience and self-awareness characteristics without themselves being T1 characteristic-bearing: the reflective capacity (enthumeomai), the terminal conscience-state (autokatakritos), and the divine epistemological frame (kardiognōstēs) |

## §2. Verses by sub-group

All verses for cluster terms, grouped by the analytical sub-group the term belongs to. Within each sub-group the rows are sorted canonically (book · chapter · verse). The **Term** column shows the Strong's number and transliteration of the cluster term whose `wa_verse_records` row generated this entry; **Spans in verse** lists every term-span recorded at that verse location.

Status precedence: G = group-assigned (analysed) · SA = set-aside · NR = is_relevant=0 · P = pending in VC · UT = untouched (no VC row).

**ID columns:** `vr_id` is `wa_verse_records.id`; `mti_id` is `mti_terms.id` (also `wa_verse_records.mti_term_id` and `verse_context.mti_term_id`). Both are exposed so AI can author VCREVISE / VCNEW / VCVERSE patches directly from this report — no separate ID-resolver query needed. The `(vr_id, mti_id)` pair is the natural key for any `verse_context` operation.

### §2.1 `M32-A` — Conscience

_The faculty by which the person assesses their own moral state — inner knowing of one's own moral standing, complicity, or condition; operating under the awareness that God's judgment is the higher court_

1. Terms in sub-group (2): G4894 suneidō, G6083 sunoida
2. Verse rows (4, deduped by term × location):

| vr_id | mti_id | Reference | Term | Status | Group | Set-aside reason | Spans in verse | Verse text |
|---:|---:|---|---|---|---|---|---|---|
| 1177 | 454 | Act 5:2 | G4894 suneidō | G | 1643 |  | G4894 suneidō (be aware) [knowledge]; G3313 meros (part) [part]; G5342 ferō (to bear/lead) [brought] | Act 5:2 and with his wife’s knowledge he kept back for himself some of the proceeds and brought only a part of it and laid it at the apostles ’ feet . |
| 1178 | 454 | Act 12:12 | G4894 suneidō | G | 1643 |  | G4894 suneidō (be aware) [realized]; G4336 proseuchomai (to pray) [praying] | Act 12:12 When he realized this, he went to the house of Mary , the mother of John whose other name was Mark , where many were gathered together and were praying . |
| 1179 | 454 | Act 14:6 | G4894 suneidō | G | 1643 |  | G4894 suneidō (be aware) [learned] | Act 14:6 they learned of it and fled to Lystra and Derbe , cities of Lycaonia , and to the surrounding country , |
| 82337 | 2739 | 1Cor 4:4 | G6083 sunoida | G | 364 |  | G6083 sunoida (be conscious of) [aware]; G1344 dikaioō (to justify) [acquitted] | 1Cor 4:4 For I am not aware of anything against myself, but I am not thereby acquitted . It is the Lord who judges me . |

### §2.2 `M32-B` — Self-Awareness / Inner Attention

_The directed inner act of setting attention — deliberate cognitive engagement and attending carefully to a matter, person, or situation; the attentiveness capacity that underlies conscience_

1. Terms in sub-group (1): H7896K shit
2. Verse rows (7, deduped by term × location):

| vr_id | mti_id | Reference | Term | Status | Group | Set-aside reason | Spans in verse | Verse text |
|---:|---:|---|---|---|---|---|---|---|
| 132800 | 3578 | Exo 7:23 | H7896K shit | G | 1776 |  | H3820A lev (heart) [heart]; H7896K shit (to set: consider) [take] | Exo 7:23 Pharaoh turned and went into his house , and he did not take even this to heart . |
| 132798 | 3578 | 1Sa 4:20 | H7896K shit | G | 1776 |  | H4191 mut (to die) [death]; H3372G ya.re (to fear: revere) [afraid]; H3820A lev (heart) [pay attention]; H7896K shit (to set: consider) [pay attention]; H5324 na.tsav (to stand) [women attending] | 1Sa 4:20 And about the time of her death the women attending her said to her, “Do not be afraid , for you have borne a son .” But she did not answer or pay attention . |
| 132799 | 3578 | 2Sa 13:20 | H7896K shit | G | 1776 |  | H2790B cha.resh (be quiet) [peace]; H3820A lev (heart) [heart]; H7896K shit (to set: consider) [take] | 2Sa 13:20 And her brother Absalom said to her, “Has Amnon your brother been with you? Now hold your peace , my sister . He is your brother ; do not take this to heart .” So Tamar lived , a desolate woman , in her brother Absalom’s house . |
| 132803 | 3578 | Psa 13:2 | H7896K shit | G | 1776 |  | H3015 ya.gon (sorrow) [sorrow]; H3824 le.vav (heart) [heart]; H5315G ne.phesh (soul) [soul]; H7896K shit (to set: consider) [take]; H6098 e.tsah (counsel) [counsel]; H7311A rum (to exalt) [exalted]; H7311B ra.mam (be rotten) [exalted]; H0341 o.yev (enemy) [enemy] | Psa 13:2 How long must I take counsel in my soul and have sorrow in my heart all the day ? How long shall my enemy be exalted over me ? |
| 132804 | 3578 | Psa 48:13 | H7896K shit | G | 1776 |  | H4616 ma.an (because) [tell]; H7896K shit (to set: consider) [consider] | Psa 48:13 consider well her ramparts , go through her citadels , that you may tell the next generation |
| 132802 | 3578 | Pro 24:32 | H7896K shit | G | 1776 |  | H7896K shit (to set: consider) [considered] | Pro 24:32 Then I saw and considered it; I looked and received instruction . |
| 132801 | 3578 | Jer 31:21 | H7896K shit | G | 1776 |  | H1980G ha.lakh (to go: went) [went]; H7896K shit (to set: consider) [consider]; H5324 na.tsav (to stand) [up] | Jer 31:21 “Set up road markers for yourself; make yourself guideposts ; consider well the highway , the road by which you went . Return , O virgin Israel , return to these your cities . |

### §2.3 `M32-BOUNDARY` — BOUNDARY

_Supporting terms that contextualise the conscience and self-awareness characteristics without themselves being T1 characteristic-bearing: the reflective capacity (enthumeomai), the terminal conscience-state (autokatakritos), and the divine epistemological frame (kardiognōstēs)_

1. Terms in sub-group (3): G2589 kardiognōstēs, G1760 enthumeomai, G0843 autokatakritos
2. Verse rows (6, deduped by term × location):

| vr_id | mti_id | Reference | Term | Status | Group | Set-aside reason | Spans in verse | Verse text |
|---:|---:|---|---|---|---|---|---|---|
| 169907 | 3392 | Mat 1:20 | G1760 enthumeomai | G | 1290 |  | G5399 fobeō (to fear) [fear]; G0040G hagios (holy) [Holy]; G4151G pneuma (spirit/breath: breath) [Spirit]; G1760 enthumeomai (to reflect on) [considered] | Mat 1:20 But as he considered these things , behold , an angel of the Lord appeared to him in a dream , saying , “ Joseph , son of David , do not fear to take Mary as your wife , for that which is conceived in her is from the Holy Spirit . |
| 169908 | 3392 | Mat 9:4 | G1760 enthumeomai | G | 1290 |  | G2588 kardia (heart) [hearts]; G4190 ponēros (evil/bad) [evil]; G1761 enthumēsis (reflection) [thoughts]; G1760 enthumeomai (to reflect on) [think] | Mat 9:4 But Jesus , knowing their thoughts , said , “ Why do you think evil in your hearts ? |
| 9056 | 599 | Act 1:24 | G2589 kardiognōstēs | G | 2728 |  | G2589 kardiognōstēs (heart-knower) [hearts]; G4336 proseuchomai (to pray) [prayed] | Act 1:24 And they prayed and said , “ You , Lord , who know the hearts of all , show which one of these two you have chosen |
| 169906 | 3392 | Act 10:19 | G1760 enthumeomai | G | 1290 |  | G1760 enthumeomai (to reflect on) [pondering] | Act 10:19 And while Peter was pondering the vision , the Spirit said to him , “ Behold , three men are looking for you . |
| 9057 | 599 | Act 15:8 | G2589 kardiognōstēs | G | 2728 |  | G2589 kardiognōstēs (heart-knower) [heart] | Act 15:8 And God , who knows the heart , bore witness to them , by giving them the Holy Spirit just as he did to us , |
| 145652 | 4848 | Tit 3:11 | G0843 autokatakritos | G | 350 |  | G0843 autokatakritos (self-condemned) [self-condemned]; G0264 hamartanō (to sin) [sinful] | Tit 3:11 knowing that such a person is warped and sinful ; he is self-condemned . |

## §3. Per-term comprehensive detail

Each term gets numbered sections: identity • meaning • anchor-verse linkages • groups • findings • pointers • auxiliary data. Verses are not repeated here — they are listed by sub-group in §2. Items linked only by registry are summarised here; exhaustive lists are in the appendix §4.

---

### H7896K shit — to set: consider

**Identity & meaning**

1. Strong's: `H7896K` · Lang: Hebrew · Owner: OWNER
2. Registry: R112 mind · Legacy C-cluster: C01
3. Sub-group: `M32-B` (Self-Awareness / Inner Attention)
4. Term status: extracted · Evidential: research_not_required · Occurrences: 7
5. Patch-authoring refs: `mti_id=3578` · `md_version=1` · `vc_status=not_done`
7. Retention note: Legacy evidential_status=confirmed mapped to research_not_required (M29 remap 2026-04-20)

**Verses:** 7 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 1776 | 3578-001 | Term names the inner act of setting attention — directing the mind to consider, take to heart, or attend carefully to a matter or person |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `SHIT` (Hebrew): to set: consider

_Related words (16):_

1. H7896G shit → to set: make
2. H7896H shit → to set: put
3. H7896I shit → to set: appoint
4. H7896J shit → to set: accuse
5. H7897 shit → garment
6. H7898 sha.yit → thornbush
7. H8352 shet → Seth
8. H8356 shat → foundation
9. H7896G shit → to set: make
10. H7896H shit → to set: put
11. H7896I shit → to set: appoint
12. H7896J shit → to set: accuse
13. H7897 shit → garment
14. H7898 sha.yit → thornbush
15. H8352 shet → Seth
16. H8356 shat → foundation

_Data-quality flags (6):_

1. flag_id=3 · Low occurrence count: 7. Statistical patterns unreliable with fewer than 20 occurrences.
2. flag_id=4 · meaning field is null for H7896K. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for H7896K stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
4. flag_id=3 · Low occurrence count: 7. Statistical patterns unreliable with fewer than 20 occurrences.
5. flag_id=4 · meaning field is null for H7896K. STEP returned no word analysis block for this term.
6. flag_id=47 · Meaning for H7896K stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

### G4894 suneidō — be aware

**Identity & meaning**

1. Strong's: `G4894` · Lang: Greek · Owner: OWNER
2. Registry: R026 conscience · Legacy C-cluster: C13
3. Sub-group: `M32-A` (Conscience)
4. Term status: extracted · Evidential: — · Occurrences: 5
5. Patch-authoring refs: `mti_id=454` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: to share knowledge with; to be conscious (of oneself) aware

**Verses:** 3 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 1643 | 454-001 | Term names a conscious inner awareness — moral complicity or cognitive recognition — that informs volitional response |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Cross-references (1):_

1. 100 · knowledge · 

_Root family (1):_

1. `SUNOID` (None): 

_Related words (243):_

1. G0050 agnoeō → be ignorant
2. G0052 agnoia → ignorance
3. G0056 agnōsia → ignorance
4. G0057 agnōstos → unknown
5. G0314 anaginōskō → to read
6. G0319 anagnōrizō → to recognize
7. G1097 ginōskō → to know
8. G1106 gnōmē → resolution
9. G1107 gnōrizō → to make known
10. G1108 gnōsis → knowledge
11. G1109 gnōstēs → expert in
12. G1110 gnōstos gnōrimos → acquainted with
13. G1231 diaginōskō → to decide
14. G1232 diagnōrizō → to report
15. G1492H eidō → to perceive: see
16. G1492I eidō → to perceive: know
17. G1921 epiginōskō → to come to know
18. G1922 epignōsis → knowledge
19. G2589 kardiognōstēs → heart-knower
20. G4267 proginōskō → to know/choose
21. G4268 prognōsis → foreknowledge
22. G4275 proeidon → to foresee
23. G4774 sungnōmē → concession
24. G4862 sun → with
25. G4893 suneidēsis → conscience
26. G4894 suneidō → be aware
27. G6083 sunoida → be conscious of
28. G1106 gnōmē → resolution
29. G4275 proeidon → to foresee
30. G1922 epignōsis → knowledge
31. G0057 agnōstos → unknown
32. G1110 gnōstos gnōrimos → acquainted with
33. G1231 diaginōskō → to decide
34. G6083 sunoida → be conscious of
35. G4267 proginōskō → to know/choose
36. G4893 suneidēsis → conscience
37. G1097 ginōskō → to know
38. G4268 prognōsis → foreknowledge
39. G0052 agnoia → ignorance
40. G0319 anagnōrizō → to recognize
41. G1492I eidō → to perceive: know
42. G4862 sun → with
43. G0050 agnoeō → be ignorant
44. G4774 sungnōmē → concession
45. G1107 gnōrizō → to make known
46. G4894 suneidō → be aware
47. G0314 anaginōskō → to read
48. G1109 gnōstēs → expert in
49. G2589 kardiognōstēs → heart-knower
50. G0056 agnōsia → ignorance
51. G1108 gnōsis → knowledge
52. G1232 diagnōrizō → to report
53. G1492H eidō → to perceive: see
54. G1921 epiginōskō → to come to know
55. G0050 agnoeō → be ignorant
56. G0052 agnoia → ignorance
57. G0056 agnōsia → ignorance
58. G0057 agnōstos → unknown
59. G0314 anaginōskō → to read
60. G0319 anagnōrizō → to recognize
61. G1097 ginōskō → to know
62. G1106 gnōmē → resolution
63. G1107 gnōrizō → to make known
64. G1108 gnōsis → knowledge
65. G1109 gnōstēs → expert in
66. G1110 gnōstos gnōrimos → acquainted with
67. G1231 diaginōskō → to decide
68. G1232 diagnōrizō → to report
69. G1492H eidō → to perceive: see
70. G1492I eidō → to perceive: know
71. G1921 epiginōskō → to come to know
72. G1922 epignōsis → knowledge
73. G2589 kardiognōstēs → heart-knower
74. G4267 proginōskō → to know/choose
75. G4268 prognōsis → foreknowledge
76. G4275 proeidon → to foresee
77. G4774 sungnōmē → concession
78. G4862 sun → with
79. G4893 suneidēsis → conscience
80. G4894 suneidō → be aware
81. G6083 sunoida → be conscious of
82. G0050 agnoeō → be ignorant
83. G0052 agnoia → ignorance
84. G0056 agnōsia → ignorance
85. G0057 agnōstos → unknown
86. G0314 anaginōskō → to read
87. G0319 anagnōrizō → to recognize
88. G1097 ginōskō → to know
89. G1106 gnōmē → resolution
90. G1107 gnōrizō → to make known
91. G1108 gnōsis → knowledge
92. G1109 gnōstēs → expert in
93. G1110 gnōstos gnōrimos → acquainted with
94. G1231 diaginōskō → to decide
95. G1232 diagnōrizō → to report
96. G1492H eidō → to perceive: see
97. G1492I eidō → to perceive: know
98. G1921 epiginōskō → to come to know
99. G1922 epignōsis → knowledge
100. G2589 kardiognōstēs → heart-knower
101. G4267 proginōskō → to know/choose
102. G4268 prognōsis → foreknowledge
103. G4275 proeidon → to foresee
104. G4774 sungnōmē → concession
105. G4862 sun → with
106. G4893 suneidēsis → conscience
107. G4894 suneidō → be aware
108. G6083 sunoida → be conscious of
109. G0050 agnoeō → be ignorant
110. G0052 agnoia → ignorance
111. G0056 agnōsia → ignorance
112. G0057 agnōstos → unknown
113. G0314 anaginōskō → to read
114. G0319 anagnōrizō → to recognize
115. G1097 ginōskō → to know
116. G1106 gnōmē → resolution
117. G1107 gnōrizō → to make known
118. G1108 gnōsis → knowledge
119. G1109 gnōstēs → expert in
120. G1110 gnōstos gnōrimos → acquainted with
121. G1231 diaginōskō → to decide
122. G1232 diagnōrizō → to report
123. G1492H eidō → to perceive: see
124. G1492I eidō → to perceive: know
125. G1921 epiginōskō → to come to know
126. G1922 epignōsis → knowledge
127. G2589 kardiognōstēs → heart-knower
128. G4267 proginōskō → to know/choose
129. G4268 prognōsis → foreknowledge
130. G4275 proeidon → to foresee
131. G4774 sungnōmē → concession
132. G4862 sun → with
133. G4893 suneidēsis → conscience
134. G4894 suneidō → be aware
135. G6083 sunoida → be conscious of
136. G0050 agnoeō → be ignorant
137. G0052 agnoia → ignorance
138. G0056 agnōsia → ignorance
139. G0057 agnōstos → unknown
140. G0314 anaginōskō → to read
141. G0319 anagnōrizō → to recognize
142. G1097 ginōskō → to know
143. G1106 gnōmē → resolution
144. G1107 gnōrizō → to make known
145. G1108 gnōsis → knowledge
146. G1109 gnōstēs → expert in
147. G1110 gnōstos gnōrimos → acquainted with
148. G1231 diaginōskō → to decide
149. G1232 diagnōrizō → to report
150. G1492H eidō → to perceive: see
151. G1492I eidō → to perceive: know
152. G1921 epiginōskō → to come to know
153. G1922 epignōsis → knowledge
154. G2589 kardiognōstēs → heart-knower
155. G4267 proginōskō → to know/choose
156. G4268 prognōsis → foreknowledge
157. G4275 proeidon → to foresee
158. G4774 sungnōmē → concession
159. G4862 sun → with
160. G4893 suneidēsis → conscience
161. G4894 suneidō → be aware
162. G6083 sunoida → be conscious of
163. G0050 agnoeō → be ignorant
164. G0052 agnoia → ignorance
165. G0056 agnōsia → ignorance
166. G0057 agnōstos → unknown
167. G0314 anaginōskō → to read
168. G0319 anagnōrizō → to recognize
169. G1097 ginōskō → to know
170. G1106 gnōmē → resolution
171. G1107 gnōrizō → to make known
172. G1108 gnōsis → knowledge
173. G1109 gnōstēs → expert in
174. G1110 gnōstos gnōrimos → acquainted with
175. G1231 diaginōskō → to decide
176. G1232 diagnōrizō → to report
177. G1492H eidō → to perceive: see
178. G1492I eidō → to perceive: know
179. G1921 epiginōskō → to come to know
180. G1922 epignōsis → knowledge
181. G2589 kardiognōstēs → heart-knower
182. G4267 proginōskō → to know/choose
183. G4268 prognōsis → foreknowledge
184. G4275 proeidon → to foresee
185. G4774 sungnōmē → concession
186. G4862 sun → with
187. G4893 suneidēsis → conscience
188. G4894 suneidō → be aware
189. G6083 sunoida → be conscious of
190. G0050 agnoeō → be ignorant
191. G0052 agnoia → ignorance
192. G0056 agnōsia → ignorance
193. G0057 agnōstos → unknown
194. G0314 anaginōskō → to read
195. G0319 anagnōrizō → to recognize
196. G1097 ginōskō → to know
197. G1106 gnōmē → resolution
198. G1107 gnōrizō → to make known
199. G1108 gnōsis → knowledge
200. G1109 gnōstēs → expert in
201. G1110 gnōstos gnōrimos → acquainted with
202. G1231 diaginōskō → to decide
203. G1232 diagnōrizō → to report
204. G1492H eidō → to perceive: see
205. G1492I eidō → to perceive: know
206. G1921 epiginōskō → to come to know
207. G1922 epignōsis → knowledge
208. G2589 kardiognōstēs → heart-knower
209. G4267 proginōskō → to know/choose
210. G4268 prognōsis → foreknowledge
211. G4275 proeidon → to foresee
212. G4774 sungnōmē → concession
213. G4862 sun → with
214. G4893 suneidēsis → conscience
215. G4894 suneidō → be aware
216. G6083 sunoida → be conscious of
217. G0050 agnoeō → be ignorant
218. G0052 agnoia → ignorance
219. G0056 agnōsia → ignorance
220. G0057 agnōstos → unknown
221. G0314 anaginōskō → to read
222. G0319 anagnōrizō → to recognize
223. G1097 ginōskō → to know
224. G1106 gnōmē → resolution
225. G1107 gnōrizō → to make known
226. G1108 gnōsis → knowledge
227. G1109 gnōstēs → expert in
228. G1110 gnōstos gnōrimos → acquainted with
229. G1231 diaginōskō → to decide
230. G1232 diagnōrizō → to report
231. G1492H eidō → to perceive: see
232. G1492I eidō → to perceive: know
233. G1921 epiginōskō → to come to know
234. G1922 epignōsis → knowledge
235. G2589 kardiognōstēs → heart-knower
236. G4267 proginōskō → to know/choose
237. G4268 prognōsis → foreknowledge
238. G4275 proeidon → to foresee
239. G4774 sungnōmē → concession
240. G4862 sun → with
241. G4893 suneidēsis → conscience
242. G4894 suneidō → be aware
243. G6083 sunoida → be conscious of

_Data-quality flags (24):_

1. flag_id=3 · Only 3 confirmed verse records for G4894. Threshold is 5.
2. flag_id=4 · meaning field is null for G4894. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G4894 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
4. flag_id=3 · Only 3 confirmed verse records for G4894. Threshold is 5.
5. flag_id=4 · meaning field is null for G4894. STEP returned no word analysis block for this term.
6. flag_id=47 · Meaning for G4894 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
7. flag_id=3 · Only 3 confirmed verse records for G4894. Threshold is 5.
8. flag_id=4 · meaning field is null for G4894. STEP returned no word analysis block for this term.
9. flag_id=47 · Meaning for G4894 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
10. flag_id=3 · Only 3 confirmed verse records for G4894. Threshold is 5.
11. flag_id=4 · meaning field is null for G4894. STEP returned no word analysis block for this term.
12. flag_id=47 · Meaning for G4894 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
13. flag_id=3 · Only 3 confirmed verse records for G4894. Threshold is 5.
14. flag_id=4 · meaning field is null for G4894. STEP returned no word analysis block for this term.
15. flag_id=47 · Meaning for G4894 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
16. flag_id=3 · Only 3 confirmed verse records for G4894. Threshold is 5.
17. flag_id=4 · meaning field is null for G4894. STEP returned no word analysis block for this term.
18. flag_id=47 · Meaning for G4894 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
19. flag_id=3 · Only 3 confirmed verse records for G4894. Threshold is 5.
20. flag_id=4 · meaning field is null for G4894. STEP returned no word analysis block for this term.
21. flag_id=47 · Meaning for G4894 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
22. flag_id=3 · Only 3 confirmed verse records for G4894. Threshold is 5.
23. flag_id=4 · meaning field is null for G4894. STEP returned no word analysis block for this term.
24. flag_id=47 · Meaning for G4894 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

### G1760 enthumeomai — to reflect on

**Identity & meaning**

1. Strong's: `G1760` · Lang: Greek · Owner: OWNER
2. Registry: R085 imagination · Legacy C-cluster: C02
3. Sub-group: `M32-BOUNDARY` (BOUNDARY)
4. Term status: extracted · Evidential: — · Occurrences: 9
5. Patch-authoring refs: `mti_id=3392` · `md_version=2` · `vc_status=vc_completed`
6. Mounce short-def: to think, ponder, reflect

**Verses:** 3 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 1290 | 3392-001 | Term names the inner act of reflecting or considering — deliberate inner thought directed at a situation, a vision, or a moral question |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `ENTHUMĒ` (Greek): reflection

_Related words (6):_

1. G1722 en → in/on/among
2. G1761 enthumēsis → reflection
3. G2372 thumos → wrath
4. G1722 en → in/on/among
5. G1761 enthumēsis → reflection
6. G2372 thumos → wrath

_Data-quality flags (6):_

1. flag_id=3 · Only 3 confirmed verse records for G1760. Threshold is 5.
2. flag_id=4 · meaning field is null for G1760. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G1760 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
4. flag_id=3 · Only 3 confirmed verse records for G1760. Threshold is 5.
5. flag_id=4 · meaning field is null for G1760. STEP returned no word analysis block for this term.
6. flag_id=47 · Meaning for G1760 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

### G2589 kardiognōstēs — heart-knower

**Identity & meaning**

1. Strong's: `G2589` · Lang: Greek · Owner: OWNER
2. Registry: R183 heart · Legacy C-cluster: C01
3. Sub-group: `M32-BOUNDARY` (BOUNDARY)
4. Term status: extracted_thin · Evidential: — · Occurrences: 2
5. Patch-authoring refs: `mti_id=599` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: heart-knower of the heart

**Verses:** 2 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 2728 | 599-001 | Term names God as the one who knows hearts — the divine inner-being knowledge of every person's innermost reality |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `KARDIA` (None): 

_Related words (144):_

1. G0050 agnoeō → be ignorant
2. G0052 agnoia → ignorance
3. G0056 agnōsia → ignorance
4. G0057 agnōstos → unknown
5. G0314 anaginōskō → to read
6. G0319 anagnōrizō → to recognize
7. G1097 ginōskō → to know
8. G1106 gnōmē → resolution
9. G1107 gnōrizō → to make known
10. G1108 gnōsis → knowledge
11. G1109 gnōstēs → expert in
12. G1110 gnōstos gnōrimos → acquainted with
13. G1231 diaginōskō → to decide
14. G1232 diagnōrizō → to report
15. G1492H eidō → to perceive: see
16. G1492I eidō → to perceive: know
17. G1921 epiginōskō → to come to know
18. G1922 epignōsis → knowledge
19. G2588 kardia → heart
20. G4267 proginōskō → to know/choose
21. G4268 prognōsis → foreknowledge
22. G4275 proeidon → to foresee
23. G4774 sungnōmē → concession
24. G4894 suneidō → be aware
25. G0056 agnōsia → ignorance
26. G1097 ginōskō → to know
27. G4894 suneidō → be aware
28. G1231 diaginōskō → to decide
29. G0319 anagnōrizō → to recognize
30. G4774 sungnōmē → concession
31. G1108 gnōsis → knowledge
32. G1922 epignōsis → knowledge
33. G0050 agnoeō → be ignorant
34. G0314 anaginōskō → to read
35. G1492H eidō → to perceive: see
36. G1492I eidō → to perceive: know
37. G1107 gnōrizō → to make known
38. G2588 kardia → heart
39. G1110 gnōstos gnōrimos → acquainted with
40. G0052 agnoia → ignorance
41. G0057 agnōstos → unknown
42. G4267 proginōskō → to know/choose
43. G4275 proeidon → to foresee
44. G1109 gnōstēs → expert in
45. G1232 diagnōrizō → to report
46. G4268 prognōsis → foreknowledge
47. G1921 epiginōskō → to come to know
48. G1106 gnōmē → resolution
49. G0050 agnoeō → be ignorant
50. G0052 agnoia → ignorance
51. G0056 agnōsia → ignorance
52. G0057 agnōstos → unknown
53. G0314 anaginōskō → to read
54. G0319 anagnōrizō → to recognize
55. G1097 ginōskō → to know
56. G1106 gnōmē → resolution
57. G1107 gnōrizō → to make known
58. G1108 gnōsis → knowledge
59. G1109 gnōstēs → expert in
60. G1110 gnōstos gnōrimos → acquainted with
61. G1231 diaginōskō → to decide
62. G1232 diagnōrizō → to report
63. G1492H eidō → to perceive: see
64. G1492I eidō → to perceive: know
65. G1921 epiginōskō → to come to know
66. G1922 epignōsis → knowledge
67. G2588 kardia → heart
68. G4267 proginōskō → to know/choose
69. G4268 prognōsis → foreknowledge
70. G4275 proeidon → to foresee
71. G4774 sungnōmē → concession
72. G4894 suneidō → be aware
73. G0050 agnoeō → be ignorant
74. G0052 agnoia → ignorance
75. G0056 agnōsia → ignorance
76. G0057 agnōstos → unknown
77. G0314 anaginōskō → to read
78. G0319 anagnōrizō → to recognize
79. G1097 ginōskō → to know
80. G1106 gnōmē → resolution
81. G1107 gnōrizō → to make known
82. G1108 gnōsis → knowledge
83. G1109 gnōstēs → expert in
84. G1110 gnōstos gnōrimos → acquainted with
85. G1231 diaginōskō → to decide
86. G1232 diagnōrizō → to report
87. G1492H eidō → to perceive: see
88. G1492I eidō → to perceive: know
89. G1921 epiginōskō → to come to know
90. G1922 epignōsis → knowledge
91. G2588 kardia → heart
92. G4267 proginōskō → to know/choose
93. G4268 prognōsis → foreknowledge
94. G4275 proeidon → to foresee
95. G4774 sungnōmē → concession
96. G4894 suneidō → be aware
97. G0050 agnoeō → be ignorant
98. G0052 agnoia → ignorance
99. G0056 agnōsia → ignorance
100. G0057 agnōstos → unknown
101. G0314 anaginōskō → to read
102. G0319 anagnōrizō → to recognize
103. G1097 ginōskō → to know
104. G1106 gnōmē → resolution
105. G1107 gnōrizō → to make known
106. G1108 gnōsis → knowledge
107. G1109 gnōstēs → expert in
108. G1110 gnōstos gnōrimos → acquainted with
109. G1231 diaginōskō → to decide
110. G1232 diagnōrizō → to report
111. G1492H eidō → to perceive: see
112. G1492I eidō → to perceive: know
113. G1921 epiginōskō → to come to know
114. G1922 epignōsis → knowledge
115. G2588 kardia → heart
116. G4267 proginōskō → to know/choose
117. G4268 prognōsis → foreknowledge
118. G4275 proeidon → to foresee
119. G4774 sungnōmē → concession
120. G4894 suneidō → be aware
121. G0050 agnoeō → be ignorant
122. G0052 agnoia → ignorance
123. G0056 agnōsia → ignorance
124. G0057 agnōstos → unknown
125. G0314 anaginōskō → to read
126. G0319 anagnōrizō → to recognize
127. G1097 ginōskō → to know
128. G1106 gnōmē → resolution
129. G1107 gnōrizō → to make known
130. G1108 gnōsis → knowledge
131. G1109 gnōstēs → expert in
132. G1110 gnōstos gnōrimos → acquainted with
133. G1231 diaginōskō → to decide
134. G1232 diagnōrizō → to report
135. G1492H eidō → to perceive: see
136. G1492I eidō → to perceive: know
137. G1921 epiginōskō → to come to know
138. G1922 epignōsis → knowledge
139. G2588 kardia → heart
140. G4267 proginōskō → to know/choose
141. G4268 prognōsis → foreknowledge
142. G4275 proeidon → to foresee
143. G4774 sungnōmē → concession
144. G4894 suneidō → be aware

_Data-quality flags (18):_

1. flag_id=3 · Only 2 confirmed verse records for G2589. Threshold is 5.
2. flag_id=4 · meaning field is null for G2589. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G2589 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
4. flag_id=3 · Only 2 confirmed verse records for G2589. Threshold is 5.
5. flag_id=4 · meaning field is null for G2589. STEP returned no word analysis block for this term.
6. flag_id=47 · Meaning for G2589 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
7. flag_id=3 · Only 2 confirmed verse records for G2589. Threshold is 5.
8. flag_id=4 · meaning field is null for G2589. STEP returned no word analysis block for this term.
9. flag_id=47 · Meaning for G2589 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
10. flag_id=3 · Only 2 confirmed verse records for G2589. Threshold is 5.
11. flag_id=4 · meaning field is null for G2589. STEP returned no word analysis block for this term.
12. flag_id=47 · Meaning for G2589 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
13. flag_id=3 · Only 2 confirmed verse records for G2589. Threshold is 5.
14. flag_id=4 · meaning field is null for G2589. STEP returned no word analysis block for this term.
15. flag_id=47 · Meaning for G2589 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
16. flag_id=3 · Only 2 confirmed verse records for G2589. Threshold is 5.
17. flag_id=4 · meaning field is null for G2589. STEP returned no word analysis block for this term.
18. flag_id=47 · Meaning for G2589 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

_Term flags (6):_

1. mti_term_id=599, flag_id=1
2. mti_term_id=2731, flag_id=1
3. mti_term_id=3645, flag_id=1
4. mti_term_id=4307, flag_id=1
5. mti_term_id=5794, flag_id=1
6. mti_term_id=6106, flag_id=1

---

### G6083 sunoida — be conscious of

**Identity & meaning**

1. Strong's: `G6083` · Lang: Greek · Owner: OWNER
2. Registry: R026 conscience · Legacy C-cluster: C13
3. Sub-group: `M32-A` (Conscience)
4. Term status: extracted_thin · Evidential: — · Occurrences: 1
5. Patch-authoring refs: `mti_id=2739` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: to be conscious of, know

**Verses:** 1 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 364 | 2739-001 | Term names the act of inner self-awareness or conscience — the person's own consciousness of their moral state, which nonetheless remains subject to God's higher judgment |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Related words (8):_

1. G4662 skōlēkobrōtos → worm-eated
2. G4894 suneidō → be aware
3. G6063 oida → to know
4. G6083 sunoida → be conscious of
5. G4662 skōlēkobrōtos → worm-eated
6. G4894 suneidō → be aware
7. G6063 oida → to know
8. G6083 sunoida → be conscious of

_Data-quality flags (6):_

1. flag_id=3 · Only 1 confirmed verse records for G6083. Threshold is 5.
2. flag_id=4 · meaning field is null for G6083. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G6083 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.
4. flag_id=3 · Only 1 confirmed verse records for G6083. Threshold is 5.
5. flag_id=4 · meaning field is null for G6083. STEP returned no word analysis block for this term.
6. flag_id=47 · Meaning for G6083 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

### G0843 autokatakritos — self-condemned

**Identity & meaning**

1. Strong's: `G0843` · Lang: Greek · Owner: OWNER
2. Registry: R024 condemnation · Legacy C-cluster: C13
3. Sub-group: `M32-BOUNDARY` (BOUNDARY)
4. Term status: extracted · Evidential: — · Occurrences: 1
5. Patch-authoring refs: `mti_id=4848` · `md_version=1` · `vc_status=not_done`
6. Mounce short-def: self-condemned

**Verses:** 1 distinct locations (see §2 for the verse table grouped by sub-group).

**Group memberships (1)**

| Group ID | Code | Description | Notes |
|---|---|---|---|
| 350 | 4848-001 | Term names the condition of the inner person whose own beliefs or conduct become the instrument of their condemnation — the conscience turned against the self |  |

**Findings — direct (Strong's mention) (0)**

(none)

**Findings — via anchor verse (0 unique)**

(none)

**SD pointers — direct (0)**

(none)

**Auxiliary data**

_Root family (1):_

1. `KATAKRINŌ` (Greek): to condemn

_Related words (4):_

1. G0178 akatakritos → uncondemned
2. G2631 katakrima → condemnation
3. G2632 katakrinō → to condemn
4. G2633 katakrisis → condemnation

_Data-quality flags (3):_

1. flag_id=3 · Only 1 confirmed verse records for G0843. Threshold is 5.
2. flag_id=4 · meaning field is null for G0843. STEP returned no word analysis block for this term.
3. flag_id=47 · Meaning for G0843 stored as single prose block. STEP medium_def contains no structured sense numbering. No further subdivision available.

---

## §4. Appendix — items linked at registry or collection level

### §4.1 Findings from contributor registries with no term-level link (24)

These findings sit on a registry that contributes terms to this cluster, but their text and anchor verses don't resolve to any specific cluster term. Candidates for term-level enrichment.

| Finding ID | Type | Registry | Anchor verses | Excerpt |
|---|---|---|---|---|
| 112-F001 | TERM_BEHAVIOUR | R112 mind | Gen 8:1, Exo 2:24, Deu 5:15, Deu 8:2, Joh 14:26 | Memory in biblical vocabulary is an active, covenantal, morally significant act — not passive cognitive retrieval. God's remembering produces redemptive action; Israel's commanded remembering constitutes covenant identity; forgetting is moral defection. |
| 112-F002 | THEOLOGICAL_NOTE | R112 mind | Rom 1:28, Rom 12:2, Eph 4:17, Col 1:21, 1Cor 2:16 | The mind is a moral organ before it is an intellectual one. It can be debased, blinded, corrupted, renewed, and transferred (mind of Christ). Romans 12:2 presents renewal of the nous as the locus of personal transformation. |
| 112-F003 | ETYMOLOGY | R112 mind | Gen 6:5, Gen 8:21, Isa 26:3 | The ye.tser (formed inclination) is the OT anthropology's closest approach to a foundational moral disposition. Gen 6:5 and 8:21 establish it as bent toward evil from youth — the dispositional substrate generating particular thoughts and plans. |
| 112-F004 | VERSE_PATTERN | R112 mind | Pro 12:5, Pro 15:26, Jer 29:11, Ps 140:2 | The cha.shav root documents that the same mental faculty produces artistic design, moral reasoning, and malicious plotting — there is no separate creative vs rational faculty in Hebrew anthropology. God's planning uses the same root as wicked scheming. |
| 112-F005 | THEOLOGICAL_NOTE | R112 mind | Rom 8:5, Rom 8:6, Rom 8:7 | Fronēma (the set mindset) in Romans 8:5-7 is the determinative factor for life or death, peace or enmity with God — making the mind's fundamental orientation soteriologically significant, not merely morally relevant. |
| 112-F006 | THEOLOGICAL_NOTE | R112 mind | Rom 2:15, 1Cor 8:7, Heb 9:14, 1Tim 4:2 | Suneidēsis (conscience) is the NT's distinctive contribution with no direct Hebrew equivalent. The conscience can be weak, clear, seared, or purified (Heb 9:14), and functions as a bridge between inner life and relational/covenantal domains. |
| 112-F007 | VERSE_PATTERN | R112 mind | Deu 4:9 | Deu 4:9 functionally links the sha.mar attentiveness cluster with the za.khar memory cluster: vigilant attentiveness is the means by which memory is maintained; forgetting is the product of failed attentiveness. |
| 112-F008 | TERM_BEHAVIOUR | R112 mind | 1Cor 14:14, 1Cor 14:15 | The 1 Cor 14:14-15 nous/pneuma distinction is the sharpest NT terminological boundary between mind-level and spirit-level inner operation — directly relevant to the Framework B spirit-soul-body boundary investigation. |
| 112-F009 | VERSE_PATTERN | R112 mind | Jas 1:8, Jas 4:8, Psa 119:113 | Double-mindedness (dipsuchos/se.eph) documents inner division as a cross-testament pathology. James presents inner unity as a condition for receiving from God and for effective action; Ps 119:113 makes it a moral stance. |
| 112-F010 | THEOLOGICAL_NOTE | R112 mind | Heb 8:10, Heb 10:16 | The Hebrews new covenant quotation (Heb 8:10; 10:16) names both dianoia (mind) and kardia (heart) as sites of internalized law — anticipating the structural relationship between Registries 112 and 183 for Session D investigation. |
| DIM-112-001 | DIMENSION_REVIEW | R112 mind |  | sha.mar family (H8104) spans four dimensions across Registry 112: Volitional/Will (G, covenantal obedience), Theological/Divine-Human (H, God's guarding), Moral/Conscience (H subset self-guarding; I attentive observation), Character/Disposition (J, vigilance). Session B: map the full sha.mar semantic range across all inner-being functions. |
| DIM-112-002 | DIMENSION_REVIEW | R112 mind |  | se.eph (4198-001, H5588) and dipsuchos (1398-001, G1374) form an OT/NT pair documenting inner division as a cross-testament moral pathology. Both assigned Moral/Conscience. Session B: analyse together as witnesses to the same inner-being phenomenon — the split allegiance that makes the person unstable before God. |
| DIM-112-003 | DIMENSION_REVIEW | R112 mind |  | ye.tser (936-001/936-002, H3336) spans Moral/Conscience (formed moral inclination toward evil or good) and Theological/Divine-Human (creaturely formation known and addressed by God). The OT's closest approach to a foundational moral disposition is simultaneously a moral reality and a creaturely-relational one. Session B: the ye.tser as the dispositional substrate of moral life. |
| DIM-112-004 | DIMENSIONAL_PATTERN | R112 mind |  | Covenant-renewal convergence across registries — Dimension 11 cluster. Five groups across r112 and r183 describe God's inner-being covenant act renewing the human person: dianoia law-writing (995-003, Heb 8:10/10:16), mnaomai non-remembrance (4413-003, Heb 8:12/10:17), le.vav circumcision/renewal (179-009, Deut 30:6), qe.rev new covenant writing (577-003, Jer 31:33), enkainizō inaugural renewal (602-001, Heb 10:20). Coordinated Dimension 11 event across multiple inner-being terms and registries. |
| DIM-112-005 | DIMENSIONAL_PATTERN | R112 mind |  | sha.mar root family dimensional breadth. Five sense-splits in r112 occupy five different dimensions: 4379-001 (obedience) → 04 Volition; 4380-001 (divine guarding) → 11 D-H Correspondence GOD; 4380-002 (self-guarding) → 11 D-H Correspondence HUMAN; 4381-001 (moral observation) → 03 Cognition; 4382-001 (vigilance) → 05 Moral Character. Illustrates directionally-determined inner-faculty principle. |
| DIM-112-006 | DIMENSIONAL_PATTERN | R112 mind |  | Divine reckoning and divine remembrance as paired Dimension 11 patterns. cha.shav 3335-001 (imputation, Gen 15:6/Rom 4) and mnaomai 4413-002 (divine remembrance producing effect) both name divine inner acts determining human standing. Both Dimension 11 GOD. Foundational pair for Session B studies of reckoning/imputation vocabulary. |
| DIM-112-007 | DIMENSIONAL_PATTERN | R112 mind |  | Memorial vocabulary as Dimension 11. Three AZKARAH groups (3498-001 zikkaron institutional, 3498-002 zikkaron priestly, 3499-001 az.ka.rah memorial portion) plus anamnēsis 4426-001 (eucharistic) all engage divine-human correspondence. The memorial is a structure of mutual remembrance between God and community — unifies OT offering vocabulary and NT eucharist vocabulary on the dimension axis. |
| DIM-183-001 | DIMENSION_REVIEW | R183 heart |  | qe.rev (H7130H) spans five groups across five dimensions: Theological/Divine-Human (God's indwelling in the midst), Moral/Conscience (seat of moral character; seat of hostile intent; location of false prophets' lies), Theological/Divine-Human (location of new covenant renewal). Session B: the inner parts as the site of both divine indwelling and moral corruption — a structural inner-being tension at the heart of the heart registry. |
| DIM-183-002 | DIMENSIONAL_PATTERN | R183 heart |  | Divine knowledge of the inner person — three-group cluster in r183 plus one in r112. 579-003 le.vav (known by God, 1 Sam 16:7), 598-004 kardia (known by God, multiple NT), 599-001 kardiognōstēs (heart-knower, Acts 1:24/15:8). All Dimension 11 with NONE or GOD dominant. Structural pattern: human heart as object of divine cognitive-searching act. Hebrew and Greek vocabulary naming the same structural relationship. Foundational for any word study of inner-knowledge vocabulary. |
| DIM-183-003 | DIMENSIONAL_PATTERN | R183 heart |  | Covenant-renewal pattern in heart vocabulary — four r183 members of the wider Dimension 11 covenant-renewal cluster. 579-009 le.vav (circumcised/renewed, Deut 30:6), 577-003 qe.rev (new covenant writing in inner parts, Jer 31:33 context), 581-008 lev (covenantal), 602-001 enkainizō (inaugural renewal, Heb 10:20). Together with r112 members 995-003 dianoia and 4413-003 mnaomai, forms an eight-term cluster where divine covenant act operates on the human inner-being. Pattern foundational for any word study of these terms. |
| DIM-183-004 | DIMENSIONAL_PATTERN | R183 heart |  | Somatic-to-figurative continuum in heart/bowel vocabulary. Six r183 groups (577-001 qe.rev midst, 585-001/002 cha.la.tsa.yim loins, 588-001 na.val withering, 590-003 splagchnon body, 1801-003 meim body) carry the somatic-physical sense of the inner organ/region, distinct from affective-moral-cognitive senses. Same roots engage both registers (e.g., splagchnon 590-001/002 affective vs 590-003 physical; meim 1801-001 yearning vs 1801-003 physical). Confirms biblical Hebrew and Greek retain physical-interior meaning alongside figurative inner-being. Word studies should acknowledge embodied register rather than reading all usage as metaphorical. |
| DIM-183-005 | DIMENSIONAL_PATTERN | R183 heart |  | Heart as site of divine indwelling — pattern distinct from divine knowing or covenant-writing. 598-007 kardia (Christ dwelling by faith Eph 3:17; Spirit poured out Rom 5:5; Father's word abiding) names a Dimension 11 structure where divine *presence* is in the human interior. Related to but distinct from 577-003 (covenant writing — act upon heart) and 579-009 (circumcision renewal — act upon heart). Indwelling is continued presence within, not a transformative act. Important distinction for systematic word study. |
| DIM-24-001 | DIMENSION_REVIEW | R024 condemnation |  | H4941H mish.pat appears in both Reg 24 (condemnation) and Reg 98 (justice) — three groups each. Session B must read both registries' mish.pat groups together to form a complete inner-being profile of this term. |
| DIM-26-001 | DIMENSION_REVIEW | R026 conscience |  | The conscience (suneidesis/sunoida) groups in Reg 26 show a consistent pattern: moral self-awareness operating under divine authority — conscience as inner witness that remains subordinate to God's judgment. Session B should examine the relationship between conscience-as-moral-witness and divine judgment as the higher court. |

### §4.2 SD pointers from contributor registries with no term-level link (31)

| Pointer | Priority | Strong's ref | Description |
|---|---|---|---|
| 112-SD001 | MEDIUM | G3340 | G3340 metanoeō, G3341 metanoia, G3338 metamellomai, and H5162H na.cham (relent) all present in Reg 112 and Reg 135 (repentance). Structural overlap at intersection of cognitive reorientation and mind-change. |
| 112-SD002 | MEDIUM | H5162G | H5162G na.cham (comfort) likely shared with Reg 071 (grief) and Reg 135. Na.cham root operates across mind-change (112), comfort of the grieving (071), and divine relenting (135). |
| 112-SD003 | MEDIUM | H5068 | H5068 na.dav (willing) likely shared with desire and will registries. Volitional inner movement of na.dav borders desire and will clusters. |
| 112-SD004 | MEDIUM | G4893 | G4893 suneidēsis has no Hebrew counterpart in this registry. Intersection with heart (183) and spirit (184) registries for Session D investigation of conscience as NT/Hellenistic category. |
| 112-SD005 | MEDIUM | H8104G | H8104G sha.mar/obey (195v) has significant overlap with will/obedience registries. Cross-registry boundary review recommended — may belong primarily to a different cluster. |
| 112-SD006 | MEDIUM | G1271 | Heb 8:10 and 10:16 name both dianoia (mind) and kardia (heart) as sites of new covenant law-writing. Structural overlap between Reg 112 and Reg 183. |
| 112-SD007 | MEDIUM | H2142 | H2142 za.khar operates across memory, worship, and ritual domains. Possible overlap with worship or praise registries (1 Chr 16:4 Levitical invoke/remember; Ps 38/70 memorial offering context). |
| 112-SD008 | MEDIUM | G3340 | Spirit-mind distinction in 1 Cor 14:14-15 is the sharpest NT terminological boundary between nous and pneuma. Session D: map against Reg 184 (spirit). |
| 112-SD009 | MEDIUM | H3336 | Ye.tser (formed inclination) in Gen 6:5 and 8:21 is the OT closest equivalent to fundamental moral disposition. Session D: relationship between ye.tser and will cluster. |
| 112-SD010 | MEDIUM | G5426 | 1 Cor 2:16 and Phil 2:5 present mind-orientation as transferable through participation in Christ. Key integration point for transformation of inner being across soul/mind/heart registries. |
| 182-SD005 | MEDIUM | G1374 | G1374 dipsuchos shared with mind registry (112). Inner division documented in both soul and mind vocabularies — double-minded (soul) and double-minded (nous). Cross-registry pattern of inner unity vs division. |
| DIM-112-SD001 | MEDIUM |  | C01 Theological/Divine-Human density: 62 of 297 groups (21%) reflect a structural reality — the primary inner-being terms are constitutively relational to God. Session D: the structural vocabulary of the inner being is a theo-relational construct, not a neutral anthropological one. This pattern should be tested against all 22 clusters. |
| DIM-112-SD002 | MEDIUM |  | Absence of Sin & Vice from all six C01 structural registries. The inner-being structural terms (mind, soul, heart, spirit, flesh, being) name the capacity and theatre of sin — not sin itself. Session D: structural vocabulary vs characterological vocabulary as an analytical distinction across the programme. |
| DIM-103-SD021 | MEDIUM | G5384 | Joh 15:15 — friendship with Christ defined by shared knowledge of the Father's purposes. 'I have called you friends, for all that I have heard from my Father I have made known to you.' Love takes the form of disclosure: God's inner purposes made known. Cross-registry: love (103), knowledge/thought (160), mind (112), calling (19). Question: is there a structural link between love and knowledge in the programme — does love require knowing and being known, not merely feeling? |
| DIM-112-SD003 | MEDIUM |  | CHASHAV root family cross-registry structural pattern. Hebrew root chashav spans Reg 112 (mind), Reg 126 (purpose), Reg 160 (thought). Functions split: act of devising/thinking/counting (mind), plan as product (purpose), calculation/explanation (thought). r112 groups predominantly 03 Cognition + 04 Volition. Session D synthesis should test dimensional profile of r126 and r160 groups. |
| DIM-112-SD004 | MEDIUM |  | BOUL root family Greek counterpart to CHASHAV. Spans Reg 32 (counsel) and Reg 112 (mind). bouleuō G1011 (mind) vs boulē G1012, epiboulē G1917, sumboulion G4824, sumboulos G4825 (counsel). Same mental-act/product/relational-noun pattern as CHASHAV. Cross-language CHASHAV/BOUL convergence is a possible structural universal for Hebrew-Greek mental-act vocabulary. |
| DIM-112-SD005 | MEDIUM |  | Inner-division theme across Greek and Hebrew vocabularies. dipsuchos G1374 (1398-001), se.eph H5588 (4198-001), dianoia-corrupted (995-002), nous-corrupted (994-002), isopsuchos G2473 (1402-001 — positive counterpart). Multiple terms from different roots/languages naming divided loyalty / split mind / darkened understanding. Distribution across 05 Moral Character, 03 Cognition, 06 Relational Disposition. Session D should trace across C17 and C22. |
| DIM-112-SD006 | MEDIUM |  | Spiritual/God-ward vocabulary gap — potential Dimension 12 (DR-13). Phase A identified 25 C01 groups with legacy 'Spiritual/God-ward' label having no clean current-vocabulary counterpart. r112 Phase C resolved these mostly to Dimension 11 (where divine-human correspondence structure was present) or 03/04/06. No r112 group required new dimension. But the label may indicate distinct 'God-ward Orientation' dimension — human's directedness toward God without correspondence structure. 995-001 dianoia 'love God with all your mind' is clearest candidate. Will be more significant for r183 where 581-006 lev God-ward orientation is UNCLASSIFIED. |
| DIM-112-SD007 | MEDIUM |  | False-positive cross-registry roots — CC rootfamily extract pipeline observation. Three of five 'cross-registry' roots for C01 appear to be string-match false positives: AT (root_code None, personal pronouns vs mutterer); YATSA (offspring vs come-out homonym); TAAM (perceive vs be-double homonym). Researcher may wish to refine tool's matching logic to exclude None-root and zero-semantic-overlap pairs. Pipeline observation, not dimension finding. |
| 182-SD007 | MEDIUM | G5590G | 1Th 5:23 tripartite statement (spirit, soul, body) and Heb 4:12 (soul-spirit division) are the primary structural cross-registry verses linking soul (182), heart (183), and spirit (184). The soul's place in the triad cannot be fully mapped without all three registries. |
| DIM-183-SD001 | MEDIUM |  | Repentance vocabulary spans Registries 112 (na.cham, metanoia, metanoeo, metamellomai), 182 (na.cham soul-level), and 183 (le.vav circumcision/renewal, kardia renewal). Session D: map the full cross-registry repentance network against Registries 135 (repentance) and 134 (renewal). The inner-being act of turning is distributed across all three C01 structural terms. |
| DIM-183-SD002 | MEDIUM |  | God-ward orientation pattern — four groups across three roots and two registries name the characteristic of human inner-being oriented toward God without divine-act structure. 581-006 lev, 579-010 le.vav, 598-008 kardia (all r183), plus 995-001 dianoia (r112 — 'love God with all your mind'). All assigned Dimension 11 under the 'operates across the boundary' clause. Question for Session D: is this genuinely Dimension 11 (cross-boundary operation), or a distinct 'God-ward Orientation' Dimension 12 that current §7.7 does not name? Linked to DIM-112-SD006. The answer determines how Dimension 11's scope is drawn programme-wide. |
| DIM-183-SD003 | MEDIUM |  | Yearning correspondence — meim 1801-001 names divine yearning (Jer 31:20) and human yearning (Song of Songs 5:4) using the same term. Splagchnon in NT has similar divine-human pattern (Luke 1:78 Christ's tender mercy; Phil 1:8 Paul's affection in Christ). Session D question: is yearning a distinct Dimension 11 pattern (parallel to knowing, remembering, reckoning) or does it sit within 06 Relational Disposition with divine-human examples? Empirical question for cross-testament synthesis. |
| DIM-183-SD004 | MEDIUM |  | Somatic-figurative dimensional split within root families — pattern observed at Phase C r183. Multiple roots show dimensional breadth determined by the somatic/figurative distinction: splagchnon (06, 06, 07); meim (06, 02, 07); qe.rev (05, 04, 07, 11, delete_flagged). Pattern raises question: should dimension-assignment rules explicitly address somatic-senses of inner-being vocabulary as a first-order distinction (not subsidiary to semantic sense-splits)? Session D candidate. |
| DIM-183-SD005 | MEDIUM |  | H3820A lev + H3824 le.vav synthesis candidate. lev cluster: 8 sense-splits covering §7.7 dimensions 02, 03, 04, 05, 05, 11, 11, 11. le.vav cluster: 10 senses covering 03, 05, 11, 04, 06, 05, 02, 02, 11, 11. Widest single-term dimensional spreads in C01. Together the two lemmas cover the heart-vocabulary analytical ground. Session D should consider whether these two lemmas warrant synthesis-level treatment as a single analytical unit with two grammatical forms (vs. separate treatment). |
| SP-067-009 | MEDIUM |  | Jos 23:14 ('you know in your hearts and souls, all of you, that not one word has failed of all the good things the Lord your God promised') explicitly names heart and soul as the site of covenantal knowing. God's good word (R67 Group 884-005) is received and registered in the inner being. Session D should examine whether Jos 23:14 establishes a structural link between R67 (goodness) and R183 (heart) / R182 (soul) — specifically whether the reception of covenantal goodness is a heart-and-soul event that connects the goodness and anthropological registries. |
| DIM-24-SD001 | MEDIUM |  | The polarity structure of condemnation (verdict/no-verdict) is the governing framework of Reg 24 and maps onto the no-condemnation freedom of Romans 8. Session D should examine the condemnation/no-condemnation polarity as the judicial frame within which the guilt-repentance-justification arc operates across C13. |
| DIM-73-SD001 | HIGH |  | The inner-being movement from guilt-incurred (Reg 73) through repentance (Reg 135) to freedom from condemnation (Reg 24) and justification (Reg 98) constitutes the governing arc of C13. Session D should examine whether this four-registry trajectory (guilt → repentance → no-condemnation → justification) maps a complete inner-being soteriology visible in Scripture. |
| DIM-98-SD001 | HIGH |  | Reg 98 (justice) shows repeated convergence between inner moral quality (Moral/Conscience) and divine action (Theological/Divine-Human) — particularly in justification/righteousness terminology. Session D should examine the relationship between the justice cluster and the condemnation registry (Reg 24) as structurally complementary: condemnation and justification are the negative and positive poles of the same judicial framework. |
| DIM-26-SD001 | MEDIUM |  | Reg 26 includes G4267 proginōskō (Identity/Selfhood) alongside conscience terms — this brings together the epistemic cluster (knowing, perception) with the identity-constituting dimension of divine foreknowing. Session D should examine whether being-known-by-God and knowing-oneself-morally form a coherent inner-being pairing that constitutes a distinct dimension of conscience. |
| DIM-180-SD002 | MEDIUM |  | The water groups ([6836-001] through [6836-008]) cluster around inner transformation, inner thirst/satisfaction, and conscience cleansing. Session D should examine whether the water imagery vocabulary belongs in the yielding registry or has stronger affinity with inner transformation vocabulary in Reg 26 (conscience, C13) and the guilt/repentance registries. |

### §4.3 Prose sections from contributor registries (0)

(none)

### §4.4 Cluster-internal verse_context_group rows (6)

Deduplicated list of all `verse_context_group` rows whose `mti_term_id` belongs to this cluster.

| Group ID | Code | mti_term_id | Strong's | Description | Notes |
|---|---|---|---|---|---|
| 364 | 2739-001 | 2739 | G6083 | Term names the act of inner self-awareness or conscience — the person's own consciousness of their moral state, which nonetheless remains subject to God's higher judgment |  |
| 1290 | 3392-001 | 3392 | G1760 | Term names the inner act of reflecting or considering — deliberate inner thought directed at a situation, a vision, or a moral question |  |
| 1776 | 3578-001 | 3578 | H7896K | Term names the inner act of setting attention — directing the mind to consider, take to heart, or attend carefully to a matter or person |  |
| 1643 | 454-001 | 454 | G4894 | Term names a conscious inner awareness — moral complicity or cognitive recognition — that informs volitional response |  |
| 350 | 4848-001 | 4848 | G0843 | Term names the condition of the inner person whose own beliefs or conduct become the instrument of their condemnation — the conscience turned against the self |  |
| 2728 | 599-001 | 599 | G2589 | Term names God as the one who knows hearts — the divine inner-being knowledge of every person's innermost reality |  |

### §4.5 Cross-cluster orphan findings/pointers

Findings + SD pointers that mention M-cluster vocabulary but originate from registries that do NOT contribute terms to this cluster — see [wa-cluster-m32-finding-orphans-v1-…](../../../outputs/markdown/) for the full scan.

