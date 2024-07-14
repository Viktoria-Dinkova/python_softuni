from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBER = {"ArcticClimber": ArcticClimber,
                     "SummitClimber": SummitClimber
                     }

    VALID_PEAK = {"ArcticPeak": ArcticPeak,
                  "SummitPeak": SummitPeak
                  }

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def find_climber(self, name) -> BaseClimber or None:
        try:
            return next(filter(lambda c: c.name == name, self.climbers))
        except StopIteration:
            pass

    def find_peak(self, name) -> BasePeak or None:
        try:
            return next(filter(lambda p: p.name == name, self.peaks))
        except StopIteration:
            pass

    def register_climber(self, climber_type: str, climber_name: str) -> str:

        if climber_type not in self.VALID_CLIMBER:
            return f"{climber_type} doesn't exist in our register."

        climber = self.find_climber(climber_name)
        if climber:
            return f"{climber_name} has been already registered."

        climber = self.VALID_CLIMBER[climber_type](climber_name)
        self.climbers.append(climber)

        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:

        if peak_type not in self.VALID_PEAK:
            return f"{peak_type} is an unknown type of peak."

        peak = self.VALID_PEAK[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]) -> str:
        climber = self.find_climber(climber_name)
        peak = self.find_peak(peak_name)

        required_gear = set(peak.get_recommended_gear())
        missing_gear = required_gear - set(gear)

        if not missing_gear:
            climber.is_prepared = True
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self.find_climber(climber_name)
        peak = self.find_peak(peak_name)

        if not climber:
            return f"Climber {climber_name} is not registered yet."

        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        # successfully_climbers = [c for c in self.climbers if c.conquered_peaks]
        sorted_successfully_climbers = sorted([c for c in self.climbers if c.conquered_peaks],
                                              key=lambda c: (-len(c.conquered_peaks), c.name))

        result = f"Total climbed peaks: {len(self.peaks)}\n**Climber's statistics:**\n"
        result += '\n'.join([str(s) for s in sorted_successfully_climbers])

        return result
