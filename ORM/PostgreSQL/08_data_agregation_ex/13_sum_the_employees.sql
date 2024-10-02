SELECT
	COALESCE(SUM(CASE When department_id = 1 then 1 END ), 0) AS "Engineering",
	COALESCE(SUM(CASE When department_id = 2 then 1 END ), 0) AS "Tool Design",
	COALESCE(SUM(CASE When department_id = 3 then 1 END ), 0) AS "Sales",
	COALESCE(SUM(CASE When department_id = 4 then 1 END ), 0) AS "Marketing",
	COALESCE(SUM(CASE When department_id = 5 then 1 END ), 0) AS "Purchasing",
	COALESCE(SUM(CASE When department_id = 6 then 1 END ), 0) AS "Research and Development",
	COALESCE(SUM(CASE When department_id = 7 then 1 END ), 0) AS "Production"

FROM
	public.employees
;