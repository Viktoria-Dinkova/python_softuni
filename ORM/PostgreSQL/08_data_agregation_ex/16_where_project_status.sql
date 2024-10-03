SELECT
	project_name,
	CASE 
		WHEN 
			COALESCE(start_date, '1900-01-01 00:00:00') = '1900-01-01 00:00:00' 
			AND COALESCE(end_date, '1900-01-01 00:00:00') = '1900-01-01 00:00:00' 
		THEN 'Ready for development'
		WHEN 
			COALESCE(start_date, '1900-01-01 00:00:00') <> '1900-01-01 00:00:00' 
			AND COALESCE(end_date, '1900-01-01 00:00:00') = '1900-01-01 00:00:00'
		THEN 'In Progress'
		ELSE 'Done'
	END AS project_status
FROM
	projects
WHERE
	project_name LIKE '%Mountain%'
;

