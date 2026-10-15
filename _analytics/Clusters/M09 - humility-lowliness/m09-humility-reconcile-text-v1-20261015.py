"""M09 humility claims reconciliation (#2152): two existing statements on humbling restated to their
verses (rule 77). Researcher, 2026-10-15: "reconcile the existing claims for the concepts that is being
updated, for instance in this case humility and related". Exact replacements; refuses unless each
matches once. Writes 10.7 v30 and Ch 14 v19 beside v29 / v18.
"""
import pathlib, sys
D = pathlib.Path('_analytics/essay/spirit_soul_body/inner-being-narrative')
PLAN = {
 ('10-07-choosing-and-setting-direction-v29-20261015.md', '10-07-choosing-and-setting-direction-v30-20261015.md'): [
  ('The humbling of the soul was not wrong in itself. It stood beside oppression in the same people, and it was not what he chooses.',
   'The humbling stood beside oppression in the same people, and it was not what he chooses.')],
 ('14-made-new-v18-20261015.md', '14-made-new-v19-20261015.md'): [
  ('God\'s reason is tender: "I will not contend forever', 'God gives the reason: "I will not contend forever')],
}
outs = {}
for (src, out), eds in PLAN.items():
    t = (D / src).read_text(encoding='utf-8')
    for a, b in eds:
        if t.count(a) != 1: sys.exit(f'REFUSED {src}: {t.count(a)} matches for {a[:60]!r}')
        t = t.replace(a, b)
    if (D / out).exists(): sys.exit(f'REFUSED exists {out}')
    outs[out] = t
for out, t in outs.items():
    (D / out).write_text(t, encoding='utf-8'); print('wrote', out)
