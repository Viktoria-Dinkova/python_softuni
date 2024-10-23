CREATE VIEW continent_currency_usage
AS
SELECT
	vrank.continent_code,
	vrank.currency_code,
	vrank.currency_usage
FROM

	(
		SELECT
			ccr.continent_code,
			ccr.currency_code,
			ccr.currency_usage,
			DENSE_RANK() OVER (
								PARTITION BY 
										ccr.continent_code
								ORDER BY 
										ccr.currency_usage DESC
								) AS currency_rank
		FROM	
			(
				SELECT
					continent_code,
					currency_code,
					COUNT(currency_code) AS currency_usage
				FROM
					countries
				GROUP BY
					continent_code,
					currency_code
				HAVING
					COUNT(*) > 1
			) AS ccr
	) AS vrank
WHERE
	vrank.currency_rank = 1
ORDER BY
		vrank.currency_usage DESC,
		vrank.continent_code,
		vrank.currency_code
;