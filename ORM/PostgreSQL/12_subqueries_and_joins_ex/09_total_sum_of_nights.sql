SELECT
	a."name",
	SUM(b.booked_for)
FROM
	public.bookings AS b 
	JOIN public.apartments AS a USING(apartment_id)
GROUP BY
	a."name"
ORDER BY 
	a."name"
;