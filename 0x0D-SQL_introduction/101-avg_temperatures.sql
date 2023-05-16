-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Import in hbtn_0c_0 database this table dump: download
SELECT city, AVG(temperature) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
