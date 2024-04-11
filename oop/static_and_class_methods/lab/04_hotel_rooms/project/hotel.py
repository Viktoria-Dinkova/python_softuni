from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))

            if not room.take_room(people): # ако стаята е заета ще върне стринг и няма да е None
                self.guests += people

        except StopIteration:
            pass

    def free_room(self, room_number: int):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
            people = room.guests # взимаме гостите преди да освободим стаята иначе после са 0
            if not room.free_room():  # ако стаята е заета ще върне стринг и няма да е None
                self.guests -= people

        except StopIteration:
            pass

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"

        free_rooms = filter(lambda r: not r.is_taken, self.rooms)
        result += "Free rooms: " + ', '.join(str(fr.number) for fr in free_rooms) + '\n'

        taken_rooms = filter(lambda r: r.is_taken, self.rooms)
        result += "Taken rooms: " + ', '.join(str(tr.number) for tr in taken_rooms)

        return result