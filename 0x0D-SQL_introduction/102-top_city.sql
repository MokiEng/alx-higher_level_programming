-- Import in hbtn_0c_0 database this table dump:
-- https://s3.amazonaws.com/intranet-projects-files/
-- +holbertonschool-higher-level_programming+/272/temperatures.sql
-- a script that displays the top 3 of cities temperature during
-- +July and August ordered by temperature (descending)
SELECT city, MAX(temperature) AS max_temperature
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY max_temperature DESC
LIMIT 3;