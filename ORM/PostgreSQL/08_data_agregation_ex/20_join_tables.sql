SELECT
	*
FROM
	departments AS d
	JOIN employees AS e ON e.department_id = d.id
;