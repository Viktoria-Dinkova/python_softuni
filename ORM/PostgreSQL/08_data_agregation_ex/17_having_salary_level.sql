SELECT
	department_id,
	count("id") AS num_employees,
	CASE
		WHEN AVG(salary) > 50000 THEN 'Above average'
		WHEN AVG(salary) <= 50000 THEN 'Below average'
	END AS salary_level
FROM
	public.employees
GROUP BY
	department_id
HAVING
	AVG(salary) > 30000
ORDER BY
	1
;