from abc import ABC
from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENTS = {"KneePad": KneePad,
                        "ElbowPad": ElbowPad
                        }

    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam,
                   "IndoorTeam": IndoorTeam
                   }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENTS:
            raise Exception("Invalid equipment type!")

        equipment = self.VALID_EQUIPMENTS[equipment_type]()
        self.equipment.append(equipment)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."

        team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next(filter(lambda t: t.name == team_name, self.teams), None)
        equipment = next(filter(lambda e: e.__class__.__name__ == equipment_type, reversed(self.equipment)), None)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next(filter(lambda t: t.name == team_name, self.teams), None)
        if team is None:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment_for_price_increase = [e.increase_price() for e in self.equipment if e.__class__.__name__ == equipment_type]
        # for eq in equipment_for_price_increase:
        #     eq.increase_price()

        return f"Successfully changed {len(equipment_for_price_increase)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next(filter(lambda t1: t1.name == team_name1, self.teams))
        team2 = next(filter(lambda t2: t2.name == team_name2, self.teams))

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        sum_of_protection1 = sum(e.protection for e in team1.equipment)
        sum_of_protection2 = sum(e.protection for e in team2.equipment)

        points1 = team1.advantage + sum_of_protection1
        points2 = team2.advantage + sum_of_protection2

        if points1 == points2:
            return "No winner in this game."

        elif points1 > points2:
            team1.win()
            return f"The winner is {team1.name}."
        else:
            team2.win()
            return f"The winner is {team2.name}."

    def get_statistics(self):
        result = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}", "Teams:"]
        for t in sorted(self.teams, key=lambda st: -st.wins):
            result.append(t.get_statistics())

        return '\n'.join(result)
