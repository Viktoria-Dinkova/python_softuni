SELECT
	CONCAT(a.address,' ', a.address_2) AS apartment_address,
	booked_for AS nights
FROM
	public.apartments AS a
	JOIN public.bookings AS b ON  b.booking_id = a.booking_id
ORDER BY
	a.apartment_id
;