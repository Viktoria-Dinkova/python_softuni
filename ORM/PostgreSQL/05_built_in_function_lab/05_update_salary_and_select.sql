UPDATE 
	employees
SET 
	salary = salary + 100
WHERE 
	job_title = 'Manager'
;

SELECT 
	*
FROM 
	public.employees
WHERE 
	job_title = 'Manager'
;