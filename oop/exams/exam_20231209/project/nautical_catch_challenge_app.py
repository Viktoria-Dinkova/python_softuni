from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPE = {"FreeDiver": FreeDiver,
                        "ScubaDiver": ScubaDiver
                        }

    VALID_FISH_TYPE = {"PredatoryFish": PredatoryFish,
                       "DeepSeaFish": DeepSeaFish
                       }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str) -> str:
        if diver_type not in self.VALID_DIVER_TYPE:
            return f"{diver_type} is not allowed in our competition."

        diver = self._find_diver(diver_name)
        if diver:
            return f"{diver_name} is already a participant."

        diver = self.VALID_DIVER_TYPE[diver_type](diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float) -> str:
        if fish_type not in self.VALID_FISH_TYPE:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self._find_fish(fish_name)
        if fish:
            return f"{fish_name} is already permitted."

        fish = self.VALID_FISH_TYPE[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool) -> str:
        diver = self._find_diver(diver_name)
        fish = self._find_fish(fish_name)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()

            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()

                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
                # diver.hit_info(fish)
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()

                return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()

            return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            # diver.hit_info(fish)

    def health_recovery(self):
        ill_divers = [d for d in self.divers if d.has_health_issue]

        for curr_diver in ill_divers:
            curr_diver.has_health_issue = False
            curr_diver.renew_oxy()

        return f"Divers recovered: {len(ill_divers)}"

    def diver_catch_report(self, diver_name: str):
        diver = self._find_diver(diver_name)
        result = [f"**{diver_name} Catch Report**"]
        for f in diver.catch:
            result.append(f.fish_details())

        return f"'\n'".join(result)

    def competition_statistics(self):
        health_divers = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(health_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = ["**Nautical Catch Challenge Statistics**"]
        for hd in sorted_divers:
            result.append(str(hd))

    # my methods
    def _find_diver(self, name) -> BaseDiver or None:
        try:
            return next(filter(lambda d: d.name == name, self.divers))
        except StopIteration:
            pass

    def _find_fish(self, name) -> BaseFish or None:
        try:
            return next(filter(lambda f: f.name == name, self.fish_list))
        except StopIteration:
            pass
