UPDATE public.employees
SET salary = salary + 2500,
	job_title = CONCAT('Senior ', COALESCE(job_title, ''))
WHERE
	hire_date < '2015-01-16'
;

UPDATE public.employees
SET salary = salary + 1500,
	job_title = CONCAT('Mid-', COALESCE(job_title, ''))
WHERE
	hire_date >= '2015-01-16' AND hire_date < '2020-03-04' 
;