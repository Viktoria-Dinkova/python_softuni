CREATE View
	"view_river_info" 
AS
SELECT
	CONCAT('The river', ' ', river_name, ' ', 'flows into the', ' '
			, outflow, ' ', 'and is', ' ', "length", ' ', 'kilometers long.') AS "River Information"
FROM
	public.rivers
ORDER BY
	river_name
;