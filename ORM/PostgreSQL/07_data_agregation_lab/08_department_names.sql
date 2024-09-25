SELECT
	e.id,
	first_name,
	last_name,
	salary :: decimal(10, 2),
	department_id,
	CASE department_id
		WHEN 1 THEN 'Management'
		WHEN 2 THEN 'Kitchen Staff'
		WHEN 3 THEN 'Service Staff'
		ELSE 'Other'
	END AS department_name

FROM
	employees AS e
	JOIN departments AS d ON d.id = e.department_id
ORDER BY
	e.id
;