UPDATE projects
SET end_date = start_date + INTERVAL '5 MONTHS'
WHERE
	end_date IS NULL;
	