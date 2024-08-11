UPDATE 
	employees
SET	
	salary = salary + 1500,
	job_title = concat('Senior ', job_title)
WHERE
	hired BETWEEN('January 1 1998', 'January 5 2000')
;