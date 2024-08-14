DELETE FROM
	employees
WHERE 
	department_id in (1, 2)
;

SELECT 
	*
FROM 
	public.employees
ORDER BY
	id
;