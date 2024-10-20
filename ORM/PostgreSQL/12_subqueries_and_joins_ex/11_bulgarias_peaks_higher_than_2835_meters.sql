SELECT
	mc.country_code,
	mountain_range, 
	peak_name, 
	elevation
FROM
	mountains AS m 
	JOIN peaks AS p ON m.id = p.mountain_id
	JOIN mountains_countries AS mc ON mc.mountain_id = m.id
WHERE
	p.elevation > 2835
	AND mc.country_code = 'BG'
ORDER BY
	p.elevation DESC
;
	