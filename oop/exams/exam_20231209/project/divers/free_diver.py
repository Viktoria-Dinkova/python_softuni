from math import floor, ceil

from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    @property
    def get_max_oxygen_level(self):
        return 120.0

    @property
    def get_oxygen_reduces(self):
        return 0.60

    def __init__(self, name: str):
        super().__init__(name, self.get_max_oxygen_level)

    def miss(self, time_to_catch: int):
        used_oxy = round(time_to_catch * self.get_oxygen_reduces)
        if self.oxygen_level < used_oxy:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used_oxy

    def renew_oxy(self):
        self.oxygen_level = self.get_max_oxygen_level
