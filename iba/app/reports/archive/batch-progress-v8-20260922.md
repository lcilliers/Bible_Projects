# Batch progress monitor

> Generated 2026-09-22T16:02:57Z by `report.batch_progress`.

- currently running: **1**
- committed (this view): **123**
- failed (this view): **10**
- total spend (this view): **$37.6108**

## Contents

- [Summary](#summary)
- [Running now](#currently-running)
- [Recent failures](#recent-failures)
- [Recent committed](#recent-committed-batches)

<a id="summary"></a>
## Summary

1 running, 123 committed, 10 failed (view limited to the most recent 500 rows unless filtered)

<a id="currently-running"></a>
## Currently running

`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_170215_672-VERSE-READING`, running 0m41s (started 2026-09-22T16:02:16Z)

<a id="recent-failures"></a>
## Recent failures

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

`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_170101_590-VERSE-READING`, committed at 2026-09-22T16:02:15Z (started 2026-09-22T16:01:02Z, 1m13s), $0.1955
`lexical.meaning` / `M67` batch 17 -- run `RUN-20260922_165235_253-STAGE1-BATCH-M67`, committed at 2026-09-22T15:55:32Z (started 2026-09-22T15:53:58Z, 1m34s), $0.3421
`lexical.meaning` / `M67` batch 16 -- run `RUN-20260922_165235_253-STAGE1-BATCH-M67`, committed at 2026-09-22T15:53:58Z (started 2026-09-22T15:52:39Z, 1m19s), $0.2909
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_164910_679-VERSE-READING`, committed at 2026-09-22T15:50:41Z (started 2026-09-22T15:49:14Z, 1m27s), $0.3065
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_141708_273-VERSE-READING`, committed at 2026-09-22T13:18:02Z (started 2026-09-22T13:17:09Z, 0m53s), $0.1797
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_141453_407-VERSE-READING`, committed at 2026-09-22T13:16:54Z (started 2026-09-22T13:14:54Z, 2m00s), $0.3508
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_141230_050-VERSE-READING`, committed at 2026-09-22T13:14:36Z (started 2026-09-22T13:12:31Z, 2m05s), $0.5801
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_141106_826-VERSE-READING`, committed at 2026-09-22T13:12:18Z (started 2026-09-22T13:11:08Z, 1m10s), $0.2713
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_140714_599-VERSE-READING`, committed at 2026-09-22T13:08:35Z (started 2026-09-22T13:07:15Z, 1m20s), $0.2340
`lexical.meaning` / `M67` batch 2 -- run `RUN-20260922_132649_784-VERSE-READING`, committed at 2026-09-22T12:34:05Z (started 2026-09-22T12:31:15Z, 2m50s), $0.5072
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_132649_784-VERSE-READING`, committed at 2026-09-22T12:31:15Z (started 2026-09-22T12:26:50Z, 4m25s), $0.9334
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_131653_779-VERSE-READING`, committed at 2026-09-22T12:19:06Z (started 2026-09-22T12:16:54Z, 2m12s), $0.5867
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_131537_122-VERSE-READING`, committed at 2026-09-22T12:15:41Z (started 2026-09-22T12:15:38Z, 0m03s), $0.2901
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_123045_892-VERSE-READING`, committed at 2026-09-22T11:32:39Z (started 2026-09-22T11:30:47Z, 1m52s), $0.5558
`lexical.meaning` / `M67` batch 1 -- run `RUN-20260922_121833_420-VERSE-READING`, committed at 2026-09-22T11:19:09Z (started 2026-09-22T11:18:34Z, 0m35s), $0.3857
`lexical.meaning` / `M67` batch 15 -- run `RUN-20260922_081007_151-STAGE1-BATCH-M67`, committed at 2026-09-22T07:12:20Z (started 2026-09-22T07:12:12Z, 0m08s), $0.0571
`lexical.meaning` / `M67` batch 5 -- run `RUN-20260922_081007_151-STAGE1-BATCH-M67`, committed at 2026-09-22T07:12:11Z (started 2026-09-22T07:10:45Z, 1m26s), $0.3262
`lexical.meaning` / `M67` batch 4 -- run `RUN-20260922_081007_151-STAGE1-BATCH-M67`, committed at 2026-09-22T07:10:45Z (started 2026-09-22T07:10:10Z, 0m35s), $0.3780
`lexical.meaning` / `M67` batch 16 -- run `RUN-20260922-WHOLEVERSE-M07SKIP-TEST`, committed at 2026-09-22T07:03:31Z (started 2026-09-22T07:02:21Z, 1m10s), $0.2197
`lexical.meaning` / `M67` batch 5 -- run `RUN-20260922-WHOLEVERSE-M07SKIP-TEST`, committed at 2026-09-22T07:02:21Z (started 2026-09-22T07:01:46Z, 0m35s), $0.3565
