-- #1978: every verse holding both an M64 (Will & Resolve) and an M47 (Inner Seat) word.
-- One row per verse, with the ESV text and each side's words (strong · gloss · surface @ position).
-- Same filters as quick-summary query v2: live cluster_strong, cluster and verse_lexical rows only.
-- Read-only against iba.db. Ordered in canonical book order (cfg_book_order), then chapter, verse.
WITH hits AS (
  SELECT DISTINCT vl.verse_id, cs.cluster_code, vl.position, vl.strong, vl.surface
  FROM verse_lexical vl
  JOIN cluster_strong cs ON cs.strong = vl.strong AND cs.deleted = 0
  JOIN cluster c ON c.cluster_code = cs.cluster_code AND c.deleted = 0
  WHERE vl.deleted = 0 AND cs.cluster_code IN ('M64', 'M47')
),
shared AS (
  SELECT verse_id FROM hits GROUP BY verse_id
  HAVING SUM(cluster_code = 'M64') > 0 AND SUM(cluster_code = 'M47') > 0
),
words AS (
  SELECT h.verse_id, h.cluster_code,
         COUNT(*) AS n,
         GROUP_CONCAT(h.strong || ' ' || COALESCE(s.stepGloss, '') || ' "' || h.surface || '" @' || h.position, ' | ') AS words
  FROM (SELECT * FROM hits ORDER BY verse_id, position) h
  LEFT JOIN strong s ON s.strongNumber = h.strong
  WHERE h.verse_id IN (SELECT verse_id FROM shared)
  GROUP BY h.verse_id, h.cluster_code
)
SELECT v.reference,
       m64.n AS m64_hits, m64.words AS m64_words,
       m47.n AS m47_hits, m47.words AS m47_words,
       v.text AS esv_text
FROM shared sh
JOIN verse v ON v.id = sh.verse_id AND v.deleted = 0
JOIN words m64 ON m64.verse_id = sh.verse_id AND m64.cluster_code = 'M64'
JOIN words m47 ON m47.verse_id = sh.verse_id AND m47.cluster_code = 'M47'
LEFT JOIN cfg_book_order bo ON bo.book = substr(v.osisId, 1, instr(v.osisId, '.') - 1)
ORDER BY bo.ordinal,
         CAST(substr(v.osisId, instr(v.osisId, '.') + 1,
              instr(substr(v.osisId, instr(v.osisId, '.') + 1), '.') - 1) AS INTEGER),
         CAST(substr(substr(v.osisId, instr(v.osisId, '.') + 1),
              instr(substr(v.osisId, instr(v.osisId, '.') + 1), '.') + 1) AS INTEGER);
