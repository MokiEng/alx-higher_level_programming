-- Import in hbtn_0c_0 database this table dump:
-- https://s3.amazonaws.com/intranet-projects-files/
-- +holbertonschool-higher-level_programming+/272/temperatures.sql
-- a script that displays the top 3 of cities temperature during
-- +July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
