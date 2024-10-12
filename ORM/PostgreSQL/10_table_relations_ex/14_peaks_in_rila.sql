SELECT
	"mountain_range", 
	"peak_name", 
	"elevation"
FROM
	public.mountains AS m
	JOIN public.peaks AS p ON p.mountain_id = m.id
WHERE
	TRIM(m.mountain_range) IN ('Rila')
ORDER BY
	elevation DESC
;