CREATE TABLE IF NOT EXISTS public.employees
(
    id integer NOT NULL DEFAULT nextval('employees_id_seq'::regclass),
    name character varying COLLATE pg_catalog."default",
    "salary " numeric(10,2),
    devices_number integer,
    CONSTRAINT employees_pkey PRIMARY KEY (id)
);