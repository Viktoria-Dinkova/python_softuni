SELECT 
	e.employee_id,
	CONCAT(first_name, ' ',last_name) AS full_name,
	p.project_id,
	p.name
FROM
	employees AS e
	JOIN public.employees_projects AS ep ON ep.employee_id = e.employee_id
	JOIN projects AS p ON ep.project_id = p.project_id
WHERE
	p.project_id = 1
;