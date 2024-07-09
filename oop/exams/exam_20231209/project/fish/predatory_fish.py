from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    
    @property
    def get_time_to_catch (self):
        return 90
    
    def __init__(self, name: str, points: float):
        super().__init__(name, points, self.get_time_to_catch)

    def fish_details(self):
        return f"{self.__class__.__name__}: " \
                f"{self.name} [Points: " \
                f"{self.points}, " \
                f"Time to Catch: {self.time_to_catch} seconds]"