Create OR REPLACE view "view_continents_countries_currencies_details"
AS
SELECT
	CONCAT_WS(': ', "continent_name", "continent_code") AS "continent_details",
	CONCAT_WS(' - ', "country_name", "capital", "area_in_sq_km", 'km2') AS "country_information",
	CONCAT( "description", CONCAT(' (',cur.currency_code,')')) AS "currencies"
FROM
	continents AS c
	INNER join public.countries AS ctr USING (continent_code)
	INNER join public.currencies  AS cur USING (currency_code)

ORDER by 
	"country_information",
	"currencies"
;
