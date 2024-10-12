SELECT
	COUNT(*)
FROM
	public.countries AS c
	LEFT JOIN public.countries_rivers AS cr ON cr.country_code = c.country_code
WHERE
	cr.country_code IS NULL
;