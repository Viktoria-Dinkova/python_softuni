SELECT
	SUM(deposit_amount::decimal(18,2)) AS total_amount
FROM
	wizard_deposits
;