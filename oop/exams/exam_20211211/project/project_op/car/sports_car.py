from project.car.car import Car


class SportsCar(Car):
    VALID_SPEED_RANG = [400, 600]

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)
