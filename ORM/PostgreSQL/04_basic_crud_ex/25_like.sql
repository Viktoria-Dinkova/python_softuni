SELECT
	"name",
	"start_date"
FROM
	public.projects
WHERE
	"name" LIKE 'MOUNT%'
ORDER BY
	"id"
;