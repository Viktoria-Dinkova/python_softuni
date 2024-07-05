from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    @property
    def get_initial_strength(self):
        return 150.0

    @property
    def get_min_needed_strength(self):
        return 75.0

    def __init__(self, name: str):
        super().__init__(name, self.get_initial_strength)

    def can_climb(self) -> bool:
        return self.strength >= self.get_min_needed_strength

    def climb(self, peak: BasePeak) -> None:

        if peak.difficulty_level == "Extreme":
            self.strength -= 30 * 2.5
        else:
            self.strength -= 30 * 1.3

        self.conquered_peaks.append(peak.name)


