from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist,
                            "Drummer": Drummer,
                            "Singer": Singer,
                            }

    CONCERT_REQUIREMENTS = {
        "Rock": {"Drummer": "play the drums with drumsticks",
                 "Singer": "sing high pitch notes",
                 "Guitarist": "play rock"
                 },

        "Metal": {"Drummer": "play the drums with drumsticks",
                  "Singer": "sing low pitch notes",
                  "Guitarist": "play metal"
                  },

        "Jazz": {"Drummer": "play the drums with drum brushes",
                 "Singer": "sing high pitch notes and sing low pitch notes",
                 "Guitarist": "play jazz"
                 }
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        musician = self._find_musician(name)
        if musician:
            raise Exception(f"{name} is already a musician!")

        musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        band = self._find_band(name)
        if band:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = [c for c in self.concerts if c.place == place]
        if concert:
            raise Exception(f"{place} is already registered for {concert.gener} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._find_musician(musician_name)
        band = self._find_band(band_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        musician = self._find_musician(musician_name)
        band = self._find_band(band_name)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        if not [m for m in band.members if m.name == musician_name]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self._find_band(band_name)
        for _type in self.VALID_MUSICIAN_TYPES:
            if not [m for m in band.members if m.__class__.__name__ == _type]:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        concert_requirements = self.CONCERT_REQUIREMENTS[concert.genre]

        for m in band.members:
            musician_type = m.__class__.__name__
            if m.skills[0] != concert_requirements[musician_type]:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def _find_musician(self, name) -> Musician:
        try:
            return next(filter(lambda m: m.name == name, self.musicians))
        except StopIteration:
            pass

    def _find_band(self, name) -> Band:
        try:
            return next(filter(lambda b: b.name == name, self.bands))
        except StopIteration:
            pass

