ALTER TABLE 
	public.countries
ADD CONSTRAINT fk_countries_currencies 
		FOREIGN KEY (currency_code) 
			REFERENCES public.currencies (currency_code)
				ON DELETE CASCADE;

ALTER TABLE 
	public.countries
ADD CONSTRAINT fk_countries_continents 
		FOREIGN KEY (continent_code) 
			REFERENCES public.continents (continent_code)
				ON DELETE CASCADE;
