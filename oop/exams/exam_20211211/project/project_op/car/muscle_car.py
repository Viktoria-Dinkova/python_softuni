from project.car.car import Car


class MuscleCar(Car):
    VALID_SPEED_RANG = [250, 450]

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)
    