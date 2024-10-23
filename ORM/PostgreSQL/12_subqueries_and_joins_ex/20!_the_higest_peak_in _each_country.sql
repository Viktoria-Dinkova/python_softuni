WITH "row_number"
AS
(
	SELECT
		rp.country_name,
		COALESCE(rp.peak_name, '(no highest peak)') AS highest_peak_name,
		COALESCE(rp.elevation, 0) AS highest_peak_elevation,
		COALESCE(rp.mountain_range, '(no highest peak)') AS mountain
	FROM
		(
			SELECT
				cm.country_name,
				cm.peak_name,
				cm.elevation,
				cm.mountain_range,
				ROW_NUMBER() OVER (PARTITION BY cm.country_name ORDER BY cm.elevation DESC) AS highest_peak
			FROM
				(
					SELECT
						c.country_name,
						p.peak_name,
						p.elevation,
						m.mountain_range
					FROM
						countries AS c
						LEFT JOIN mountains_countries AS mc ON mc.country_code = c.country_code
						lEFT JOIN mountains AS m ON m.id = mc.mountain_id
						LEFT JOIN peaks AS p ON p.mountain_id = m.id

				) AS cm
		) AS rp
	WHERE
		highest_peak = 1
	ORDER BY
		rp.country_name,
		highest_peak_elevation DESC
	)

SELECT * FROM "row_number";

	
	
	