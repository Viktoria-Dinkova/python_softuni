SELECT
	c.country_name,
	r.river_name
FROM
	countries AS c
	JOIN continents AS con ON con.continent_code = c.continent_code
	LEFT JOIN countries_rivers AS cr ON cr.country_code = c.country_code
	LEFT JOIN rivers AS r ON r.id = cr.river_id
WHERE 
	LOWER(TRIM(con.continent_name)) = 'africa'
ORDER BY
	c.country_name
LIMIT 5
;