from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE = {"Appaloosa": Appaloosa,
                   "Thoroughbred": Thoroughbred
                   }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int) -> str:
        horse = self._find_horse(horse_name)
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = self.VALID_HORSE[horse_type](horse_name, horse_speed)
        self.horses.append(horse)

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> str:
        jockey = self._find_jockey(jockey_name)
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str) -> str:
        horse_race = self._find_horse_race(race_type)
        if horse_race:
            raise Exception(f"Race {race_type} has been already created!")

        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str) -> str:
        jockey = self._find_jockey(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        available_horse = [ah for ah in self.horses if ah.__class__.__name__ == horse_type and not ah.is_taken]
        if not available_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if available_horse and jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        self.horses.remove(available_horse[-1])
        jockey.horse = available_horse[-1]
        available_horse[-1].is_taken = True

        return f"Jockey {jockey_name} will ride the horse {available_horse[-1].name}."


    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str) -> str:
        jockey = self._find_jockey(jockey_name)
        horse_race = self._find_horse_race(race_type)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str) -> str:
        horse_race = self._find_horse_race(race_type)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(horse_race.jockeys, key=lambda j: -j.horse.speed)[0]

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    ###################### helper

    def _find_horse(self, name):
        try:
            return next(filter(lambda h: h.name == name, self.horses))
        except StopIteration:
            pass

    def _find_jockey(self, name):
        try:
            return next(filter(lambda j: j.name == name, self.jockeys))
        except StopIteration:
            pass

    def _find_horse_race(self, race_type):
        try:
            return next(filter(lambda hr: hr.race_type == race_type, self.horse_races))
        except StopIteration:
            pass
