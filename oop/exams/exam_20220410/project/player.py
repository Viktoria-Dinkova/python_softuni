class Player:
    STAMINA_UNITS = 100
    PLAYERS_NAMES = []

    def __init__(self, name: str, age: int, stamina: int = STAMINA_UNITS):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name not valid!")
        elif value in Player.PLAYERS_NAMES:
            raise Exception(f"Name {value} is already used!")
        Player.PLAYERS_NAMES.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self) -> bool:
        return self.__stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
