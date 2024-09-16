SELECT 
	continent_name,
	TRIM(LEADING continent_name) AS "trim"
FROM
	continents
;