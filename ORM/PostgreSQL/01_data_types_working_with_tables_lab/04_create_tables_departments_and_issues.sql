CREATE TABLE IF NOT EXISTS public.departments
(
    id integer NOT NULL DEFAULT nextval('departments_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default",
    code character(3) COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    CONSTRAINT departments_pkey PRIMARY KEY (id)
);



CREATE TABLE IF NOT EXISTS public.issues
(
    id integer NOT NULL DEFAULT nextval('issues_id_seq'::regclass),
    description character varying(150) COLLATE pg_catalog."default",
    date date,
    start timestamp without time zone,
    CONSTRAINT issues_pkey PRIMARY KEY (id)
);