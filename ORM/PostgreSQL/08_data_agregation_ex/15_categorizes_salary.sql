SELECT
	e.job_title,
	CASE 
		WHEN e.avg_salary > 45800 THEN 'Good'
		WHEN e.avg_salary BETWEEN 27500 AND 45800 THEN 'Medium'
		WHEN e.avg_salary < 27500 THEN 'Need Improvement'
	END AS category
FROM
	(
	SELECT
		job_title,
		AVG(salary) AS avg_salary
	FROM
		employees
	GROUP BY
		job_title
	) AS e
ORDER BY
	category,
	job_title
;

