SELECT 
	(REGEXP_MATCHES("River Information", '[0-9]{1,4}'))[1]  AS river_lenght
	--SUBSTRING("River Information", '[0-9]{1,4}') AS river_lenght
FROM
	view_river_info
;
