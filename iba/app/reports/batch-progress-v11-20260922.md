# Batch progress monitor

> Generated 2026-09-22T18:24:30Z by `report.batch_progress`.

- currently running: **0**
- committed (this view): **157**
- failed (this view): **12**
- total spend (this view): **$47.6496**

## Contents

- [Summary](#summary)
- [Running now](#currently-running)
- [Recent failures](#recent-failures)
- [Recent committed](#recent-committed-batches)

<a id="summary"></a>
## Summary

0 running, 157 committed, 12 failed (view limited to the most recent 500 rows unless filtered)

<a id="currently-running"></a>
## Currently running

(none currently running)

<a id="recent-failures"></a>
## Recent failures

`lexical.meaning` / `M49` batch 1 -- run `RUN-20260922_191434_564-STAGE1-BATCH-M49`, failed at 2026-09-22T18:19:17Z (started 2026-09-22T18:14:40Z, after 4m37s): bad-model-response: model reply is not valid JSON: Expecting value: line 1 column 1 (char 0) -- first 300 chars: '```json\n{"observations": [\n{"strong": "H3034", "question_code": "M0.7.1", "tag": "answered-no-flag", "obs_text": "Isa.12.1: thanksgiving is the speech-act the speaker commits to give, its role being to name and complete the shift from God\'s anger to comfort -- it leads the person to voice acknowledg'
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_175511_121-VERSE-READING`, failed at 2026-09-22T16:56:09Z (started 2026-09-22T16:55:12Z, after 0m57s): bad-model-response: model reply is not valid JSON: Expecting value: line 1 column 1 (char 0) -- first 300 chars: '```json\n{"observations": [\n{"strong": "H6103", "question_code": "M0.7.1", "tag": "answered-no-flag", "obs_text": "Sloth here implies no positive purpose for the person; it functions as a negative disposition whose only stated effect is the roof\'s collapse, not any development the person is led towar'
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_140120_179-VERSE-READING`, failed at 2026-09-22T13:05:45Z (started 2026-09-22T13:01:21Z, after 4m24s): bad-model-response: model reply is not valid JSON: Expecting value: line 1 column 1 (char 0) -- first 300 chars: '```json\n{"observations": [\n{"strong": "G0091", "question_code": "M0.7.1", "tag": "not-related-to-meaningful-word", "obs_text": "The wrongdoer/sufferer party names are not the letter\'s purpose; the wrongdoing itself serves as backdrop occasion, not a stated purpose/role for the person who did it.", "'
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_132623_791-VERSE-READING`, failed at 2026-09-22T12:26:36Z (started 2026-09-22T12:26:25Z, after 0m11s): ConnectionError: HTTPSConnectionPool(host='api.anthropic.com', port=443): Max retries exceeded with url: /v1/messages (Caused by NameResolutionError("HTTPSConnection(host='api.anthropic.com', port=443): Failed to resolve 'api.anthropic.com' ([Errno 11001] getaddrinfo failed)"))
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922-FORCE-RECONCILE-TEST`, failed at 2026-09-22T04:32:05Z (started 2026-09-22T04:31:26Z, after 0m39s): OperationalError: ambiguous column name: cluster_code
`lexical.meaning` / `M67` batch 5 -- run `RUN-20260921_185641_674-VERSE-READING`, failed at 2026-09-21T18:04:02Z (started 2026-09-21T17:59:33Z, after 4m29s): bad-model-response: model reply is not valid JSON: Expecting value: line 1 column 1 (char 0) -- first 300 chars: '```json\n{"observations": [\n{"strong": "H2255", "question_code": "M0.1.1", "tag": "answered-no-flag", "obs_text": "H2255 names an action of hurting/destroying (Aramaic), signaling forceful ruin brought upon a structure or entity by an agent\'s decree.", "meaning_source": "strong_meaning_tree", "occurr'
`lexical.meaning` / `M67` batch 4 -- run `RUN-20260921_184205_441-VERSE-READING`, failed at 2026-09-21T17:55:10Z (started 2026-09-21T17:50:50Z, after 4m20s): bad-model-response: model reply is not valid JSON: Invalid control character at: line 235 column 610 (char 80464) -- first 300 chars: '```json\n{"observations": [\n{"strong": "G0684", "question_code": "M0.1.1", "tag": "answered-no-flag", "obs_text": "apoleia names destruction/ruin/perdition as its essential nature - a state of being utterly lost or wasted, here applied to the false teachers\' coming ruin.", "meaning_source": "strong_m'
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260921_183539_495-VERSE-READING`, failed at 2026-09-21T17:40:36Z (started 2026-09-21T17:35:41Z, after 4m55s): bad-model-response: model reply is not valid JSON: Unterminated string starting at: line 266 column 164 (char 89449) -- first 300 chars: '{"observations": [\n{"strong": "G1922", "question_code": "M0.1.1", "tag": "answered-no-flag", "obs_text": "ἐπίγνωσις (\'knowledge\') names deepened, applied recognition -- knowledge that has come to bear on a person\'s Christian life, not bare information.", "meaning_source": "strong_meaning_tree; stron'
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260921_182837_181-VERSE-READING`, failed at 2026-09-21T17:33:38Z (started 2026-09-21T17:28:38Z, after 5m00s): bad-model-response: model reply is not valid JSON: Expecting value: line 1 column 1 (char 0) -- first 300 chars: '```json\n{"observations": [\n{"strong": "G1922", "question_code": "M0.1.1", "tag": "answered-no-flag", "obs_text": "ἐπίγνωσις names full/deeper knowledge -- knowledge that has come to recognition, signalling a knowing that is thorough, applied, and personally realised rather than bare acquaintance.", '
`cluster.answer` / `M83|B_intensified_seeking` batch 1 -- run `RUN-20260918_133947_340-CLUSTER-ANSWER`, failed at 2026-09-18T12:49:02Z (started 2026-09-18T12:39:48Z, after 9m14s): Manually invalidated for a deliberate re-read (zero-grounding data-quality gap found live, escalation pending) -- the prior committed batch is NOT wrong/lost, this just lets already_committed() allow a genuine re-read instead of treating it as already-done
`cluster.reading` / `M49|D_yadah_praise_confess` batch 1 -- run `RUN-20260918_113859_216-CLUSTER-READING`, failed at 2026-09-18T10:39:37Z (started 2026-09-18T10:39:00Z, after 0m37s): bad-model-response: model reply is not valid JSON: Extra data: line 1 column 5413 (char 5412) -- first 300 chars: '{"observations": [{"strong": "H3034", "question_code": null, "tag": "verse-grouping", "tag_note": null, "obs_text": "Within this pass\'s surface set, the great majority of occurrences (e.g. Ps.106.1, Ps.111.1, Ps.44.8, Ps.86.12, Ps.28.7, 1Chr.16.35/16.8/16.41/16.34, Ps.105.1, Ps.54.6, Ps.75.1 (x2), P'
`cluster.reading` / `M49|C_thankful_disposition` batch 1 -- run `RUN-20260918_110541_573-CLUSTER-READING`, failed at 2026-09-18T10:05:53Z (started 2026-09-18T10:05:42Z, after 0m11s): ConnectionError: HTTPSConnectionPool(host='api.anthropic.com', port=443): Max retries exceeded with url: /v1/messages (Caused by NameResolutionError("HTTPSConnection(host='api.anthropic.com', port=443): Failed to resolve 'api.anthropic.com' ([Errno 11001] getaddrinfo failed)"))

<a id="recent-committed-batches"></a>
## Recent committed batches

`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_175846_762-VERSE-READING`, committed at 2026-09-22T16:59:45Z (started 2026-09-22T16:58:47Z, 0m58s), $0.1566
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_175716_237-VERSE-READING`, committed at 2026-09-22T16:57:57Z (started 2026-09-22T16:57:17Z, 0m40s), $0.1268
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_175609_817-VERSE-READING`, committed at 2026-09-22T16:57:15Z (started 2026-09-22T16:56:10Z, 1m05s), $0.1717
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_175430_694-VERSE-READING`, committed at 2026-09-22T16:55:10Z (started 2026-09-22T16:54:31Z, 0m39s), $0.1314
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_175338_632-VERSE-READING`, committed at 2026-09-22T16:54:30Z (started 2026-09-22T16:53:39Z, 0m51s), $0.1426
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_175235_111-VERSE-READING`, committed at 2026-09-22T16:53:38Z (started 2026-09-22T16:52:36Z, 1m02s), $0.2003
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_175159_777-VERSE-READING`, committed at 2026-09-22T16:52:34Z (started 2026-09-22T16:52:00Z, 0m34s), $0.1108
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_175020_502-VERSE-READING`, committed at 2026-09-22T16:51:59Z (started 2026-09-22T16:50:21Z, 1m38s), $0.2599
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_174855_063-VERSE-READING`, committed at 2026-09-22T16:50:20Z (started 2026-09-22T16:48:56Z, 1m24s), $0.3017
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_174650_540-VERSE-READING`, committed at 2026-09-22T16:48:54Z (started 2026-09-22T16:46:51Z, 2m03s), $0.3676
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_174422_659-VERSE-READING`, committed at 2026-09-22T16:46:50Z (started 2026-09-22T16:44:24Z, 2m26s), $0.3649
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_174215_319-VERSE-READING`, committed at 2026-09-22T16:44:22Z (started 2026-09-22T16:42:16Z, 2m06s), $0.3069
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_174034_165-VERSE-READING`, committed at 2026-09-22T16:42:15Z (started 2026-09-22T16:40:35Z, 1m40s), $0.2574
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_173841_172-VERSE-READING`, committed at 2026-09-22T16:40:33Z (started 2026-09-22T16:38:42Z, 1m51s), $0.2937
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_173707_224-VERSE-READING`, committed at 2026-09-22T16:38:40Z (started 2026-09-22T16:37:08Z, 1m32s), $0.2518
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_173526_529-VERSE-READING`, committed at 2026-09-22T16:37:06Z (started 2026-09-22T16:35:27Z, 1m39s), $0.3231
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_173334_344-VERSE-READING`, committed at 2026-09-22T16:35:26Z (started 2026-09-22T16:33:35Z, 1m51s), $0.3300
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_173155_683-VERSE-READING`, committed at 2026-09-22T16:33:34Z (started 2026-09-22T16:31:56Z, 1m38s), $0.2959
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_172949_928-VERSE-READING`, committed at 2026-09-22T16:31:55Z (started 2026-09-22T16:29:50Z, 2m05s), $0.4649
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_172712_650-VERSE-READING`, committed at 2026-09-22T16:29:49Z (started 2026-09-22T16:27:13Z, 2m36s), $0.4443
