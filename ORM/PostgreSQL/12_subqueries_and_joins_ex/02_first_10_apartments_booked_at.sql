SELECT
	a."name",
	a.country,
	CAST(b.booked_at AS DATE)
FROM
	public.apartments AS a
	LEFT JOIN public.bookings AS b ON  b.booking_id = a.booking_id
;