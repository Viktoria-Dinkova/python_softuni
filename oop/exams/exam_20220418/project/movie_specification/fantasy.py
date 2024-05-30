from project.movie_specification.movie import Movie


class Fantasy(Movie):
    AGE_RESTRICTION = 6

    def __init__(self, title: str, year: int, owner, age_restriction: int = AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.AGE_RESTRICTION:
            raise ValueError(f"Fantasy movies must be restricted for audience under {self.AGE_RESTRICTION} years!")
        self.__age_restriction = value

    def details(self) -> str:
        return f"Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
