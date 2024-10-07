DROP TABLE mountains;
DROP TABLE peaks;

CREATE TABLE 
	mountains 
	(
		"id" INT PRIMARY KEY,
		"name" VARCHAR(50)
	)
;

CREATE TABLE 
	peaks 
	(
		"id" INT PRIMARY KEY,
		"name" VARCHAR(50),
		mountain_id INT,
		CONSTRAINT fk_mountain_id FOREIGN KEY (mountain_id) REFERENCES mountains("id")
	)
;

CREATE RULE 
	r_peaks_del 
AS ON DELETE TO 
	mountains
DO INSTEAD
	(
		DELETE FROM
			peaks
		WHERE 
			mountain_id = OLD.id
	)
;
	
