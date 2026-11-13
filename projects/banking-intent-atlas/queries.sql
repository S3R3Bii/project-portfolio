-- Retained evidence is keyed by query and model; totals must not multiply on joins.
SELECT model, COUNT(*) AS tested, SUM(correct) AS correct,
       SUM(accepted) AS accepted,
       SUM(CASE WHEN accepted=1 AND correct=0 THEN 1 ELSE 0 END) AS accepted_errors
FROM predictions GROUP BY model;

SELECT split, COUNT(*) AS rows, COUNT(DISTINCT fingerprint) AS distinct_texts
FROM queries GROUP BY split;

SELECT p.model, p.truth, p.prediction, COUNT(*) AS errors
FROM predictions p JOIN queries q USING(row_id)
WHERE q.split='test' AND p.correct=0
GROUP BY p.model,p.truth,p.prediction ORDER BY errors DESC;
