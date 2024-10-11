ALTER TABLE public.countries_rivers
ADD CONSTRAINT fk_countries_rivers_rivers 
		FOREIGN KEY (river_id) 
			REFERENCES public.rivers (id)
				ON UPDATE CASCADE;

ALTER TABLE public.countries_rivers
ADD CONSTRAINT fk_countries_rivers_countries
		FOREIGN KEY (country_code) 
			REFERENCES public.countries (country_code)
				ON UPDATE CASCADE;

