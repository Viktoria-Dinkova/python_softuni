UPDATE
	countries
SET
	country_name = 'Burma'
WHERE
	country_name = 'Myanmar'
;

INSERT INTO
	monasteries(monastery_name, country_code)
VALUES
	('Hanga Abbey', (SELECT country_code FROM countries WHERE country_name = 'Tanzania')),
	('Myin-Tin-Daik', (SELECT country_code FROM countries WHERE country_name = 'Myanmar'))
;

SELECT 
	cont.continent_name,
	c.country_name,
	count(m.id) AS monasteries_count
FROM
	continents AS cont
	JOIN countries AS c ON c.continent_code = cont.continent_code
	JOIN monasteries AS m ON m.country_code = c.country_code
WHERE
	c.three_rivers IS TRUE
GROUP BY
	cont.continent_name,
	c.country_name
ORDER BY
	monasteries_count DESC,
	country_name
;