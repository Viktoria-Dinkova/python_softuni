SELECT
	COUNT(c.id) AS countries_without_mountains
FROM
	countries AS c
	LEFT JOIN mountains_countries AS mc ON mc.country_code = c.country_code
WHERE
	mc.country_code IS NULL
;