from abc import ABC


class Car(ABC):
    VALID_SPEED_RANG = []

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        min_speed = self.VALID_SPEED_RANG[0]
        max_speed = self.VALID_SPEED_RANG[1]
        if not (min_speed <= value <= max_speed):
            raise ValueError(f"Invalid speed limit! Must be between {min_speed} and {max_speed}!")
        self.__speed_limit = value