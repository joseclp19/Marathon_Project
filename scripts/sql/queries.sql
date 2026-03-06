-- Global BQ Success Rate and Totals for 2024
SELECT 
    COUNT(*) AS total_runners,
    SUM(CASE WHEN bq_qualifier = true THEN 1 ELSE 0 END) AS total_bq_qualifiers,
    ROUND((SUM(CASE WHEN bq_qualifier = true THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100)::numeric, 2) AS global_bq_rate,
    ROUND((AVG(finish) / 3600.0)::numeric, 2) AS avg_finish_hours
FROM results;

-- Performance Analysis by Age Bracket and Gender
SELECT 
    gender,
    "Age Bracket",
    COUNT(*) AS total_runners,
    ROUND((AVG(finish) / 3600.0)::numeric, 2) AS avg_time_hours,
    ROUND((SUM(CASE WHEN bq_qualifier = true THEN 1.0 ELSE 0.0 END) / COUNT(*) * 100)::numeric, 2) AS bq_rate
FROM results
WHERE "Age Bracket" IS NOT NULL
GROUP BY gender, "Age Bracket"
ORDER BY gender, "Age Bracket";

-- Identifying "Trap" Races: Massive events with 0% BQ Rate
SELECT 
    race,
    COUNT(*) AS total_runners,
    SUM(CASE WHEN bq_qualifier = true THEN 1 ELSE 0 END) AS bq_qualifiers
FROM results
GROUP BY race
HAVING SUM(CASE WHEN bq_qualifier = true THEN 1 ELSE 0 END) = 0
ORDER BY total_runners DESC
LIMIT 5;