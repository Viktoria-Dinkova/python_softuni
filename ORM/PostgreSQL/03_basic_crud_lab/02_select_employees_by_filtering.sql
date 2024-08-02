SELECT 
	id,  
	CONCAT(first_name,' ', last_name) as "Full Name", 
	job_title, 
	salary 
FROM
	public.employees
WHERE
	salary > 1000.00
ORDER BY
	id
;