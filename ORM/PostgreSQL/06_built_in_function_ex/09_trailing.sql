SELECT 
	continent_name,
	TRIM(TRAILING continent_name) AS "trim"
FROM
	continents
;