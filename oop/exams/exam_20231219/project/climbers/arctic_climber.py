from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):

    @property
    def get_initial_strength(self):
        return 200.0

    @property
    def get_min_needed_strength(self):
        return 100.0

    def __init__(self, name: str):
        super().__init__(name, self.get_initial_strength)

    def can_climb(self) -> bool:
        return self.strength >= self.get_min_needed_strength

    def climb(self, peak: BasePeak) -> None:

        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2.0
        else:
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)


