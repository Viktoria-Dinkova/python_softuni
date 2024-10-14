SELECT 
	employee_id, 
	CONCAT(first_name, ' ', last_name) AS full_name,
	d.department_id, 
	"name" AS department_name
FROM
	public.employees e
	JOIN public.departments d ON d.manager_id = e.employee_id

ORDER BY
	1
LIMIT
	5
;