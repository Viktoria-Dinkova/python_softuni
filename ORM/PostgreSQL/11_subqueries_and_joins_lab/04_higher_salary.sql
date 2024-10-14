SELECT 
	COUNT(employee_id)
FROM
	employees
WHERE
	salary > 
	(
		SELECT
			AVG(salary)
		FROM
			public.employees
	)
;