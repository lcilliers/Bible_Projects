"""Force-onboard H7854 (Satan) into the 'spiritual powers' registry (195) as a third-party
evil-agent reference. STEP auto-excludes it as a proper noun (F1: is_proper_noun -> G3), so we
fetch its verses via the same fetch_verses machinery and flip action->include, then let
audit_word --add-terms ingest it. Per the researcher: Satan (the evil one / evil spirits) is a
third party with major influence on the inner being and MUST be included.
"""
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from analytics.step_client import StepClient
from word_study_extract import fetch_verses

SRC = 'research/discovery/195_spiritual powers_step_data_20260706.json'
OUT = 'research/discovery/195_spiritual_powers_satan_curated.json'

d = json.load(open(SRC, encoding='utf-8'))
h = [t for t in d['terms'] if t['code'] == 'H7854'][0]
# force include + fetch verses
h['action'] = 'include'
h['decision_group'] = 'G1'
h['decision_reason'] = 'FORCED: third-party evil agent (researcher directive 2026-07-06)'
client = StepClient()
fetch_verses(client, [h], {'H7854': h})
print(f"H7854 verses fetched: {h.get('verse_count')}  span-matched: {sum(v['span_strong_match'] for v in h['verses'])}")

d['terms'] = [h]
d['meta']['include_codes'] = ['H7854']
d['meta']['anchor_codes'] = ['H7854']
d['meta']['curated_note'] = 'FORCED onboarding: Satan H7854 as third-party evil agent (spiritual powers)'
json.dump(d, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('curated ->', OUT)
