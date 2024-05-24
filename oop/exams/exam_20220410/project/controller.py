from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players: Player) -> str:
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplys: Supply) -> None:
        for supply in supplys:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str) -> str or None:
        supply = [s for s in self.supplies if s.__class__.__name__ == sustenance_type]
        player = [p for p in self.players if p.name == player_name]

        if sustenance_type not in ["Food", "Drink"] or not player:
            return None

        if not supply:
            if sustenance_type == "Food":
                raise Exception("There are no food supplies left!")
            raise Exception("There are no drink supplies left!")

        supply = supply[-1]
        player = player[0]
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        self.supplies.reverse()
        self.supplies.remove(supply)
        self.supplies.reverse()

        player.stamina += supply.energy
        if player.stamina > 100:
            player.stamina = 100

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str) -> str:
        first_player = next(filter(lambda p: p.name == first_player_name, self.players))
        second_player = next(filter(lambda p: p.name == second_player_name, self.players))

        if 0 in (first_player.stamina, second_player.stamina):
            result = []
            if first_player.stamina == 0:
                result.append(f"Player {first_player_name} does not have enough stamina.")
            if second_player.stamina == 0:
                result.append(f"Player {second_player_name} does not have enough stamina.")

            return '\n'.join(result)

        attacker = first_player if first_player.stamina < second_player.stamina else second_player
        defender = first_player if first_player.stamina > second_player.stamina else second_player

        defender.stamina -= attacker.stamina / 2
        if defender.stamina <= 0:
            defender.stamina = 0
            winner = attacker
            return f"Winner: {winner.name}"

        attacker.stamina -= defender.stamina / 2
        if attacker.stamina <= 0:
            attacker.stamina = 0
            winner = defender
            return f"Winner: {winner.name}"

        winner = attacker if attacker.stamina > defender.stamina else defender
        return f"Winner: {winner.name}"

    def next_day(self) -> None:
        for player in self.players:
            if player.stamina < player.age * 2:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = [str(p) for p in self.players]
        result.extend([s.details() for s in self.supplies])
        return "\n".join(result)
