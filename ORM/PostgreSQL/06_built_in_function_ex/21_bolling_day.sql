ALTER TABLE bookings
ADD COLUMN billing_day TIMESTAMPTZ DEFAULT NOW()
;

SELECT
	TO_CHAR(billing_day, 
			'DD "Day" MM "Month" YYYY "Year" HH24:MI:SS')
FROM
	bookings
;