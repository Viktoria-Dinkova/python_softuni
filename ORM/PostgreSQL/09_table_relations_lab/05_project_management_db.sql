CREATE TABLE
	clients
	(
		id INT PRIMARY KEY,
		name VARCHAR(100)
	)
;


CREATE TABLE
	employees
	(
		id INT PRIMARY KEY,
		first_name VARCHAR(30),
		ldst_name VARCHAR(30),
		project_id INT
		--CONSTRAINT fk_projects_id FOREIGN KEY (project_id) REFERENCES projects(id)
		
	)
;



CREATE TABLE
	projects
	(
		id INT PRIMARY KEY,
		client_id INT,
		project_lead_id INT,
		CONSTRAINT fk_clients_id FOREIGN KEY (client_id) REFERENCES clients("id"),
		CONSTRAINT fk_employees_id FOREIGN KEY (project_lead_id) REFERENCES employees("id")
	)
;


ALTER TABLE
	employees
ADD CONSTRAINT fk_projects_id FOREIGN KEY (project_id) REFERENCES projects("id")
;