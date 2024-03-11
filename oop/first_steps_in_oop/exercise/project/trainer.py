"""
You are tasked to create two classes: a Pokemon class in the pokemon.py file and a Trainer class in the trainer.py file.
The Pokemon class should receive a username (string) and health (int) upon initialization. It should also have a method called pokemon_details that returns the information about the pokemon: "{pokemon_name} with health {pokemon_health}"
The Trainer class should receive a username (string). The Trainer should also have an attribute pokemons (list, empty by default). The Trainer has three methods:
-	add_pokemon(pokemon: Pokemon)
o	Adds the pokemon to the collection and returns "Caught {pokemon_name} with health {pokemon_health}". Hint: use the pokemon's details method.
o	If the pokemon is already in the collection, return "This pokemon is already caught"
o	Hint: to import the Pokemon class, you should add "from project.pokemon import Pokemon"
-	release_pokemon(pokemon_name: string)
o	Check if you have a pokemon with that username and remove it from the collection. In the end, returns "You have released {pokemon_name}"
o	If there is no pokemon with that username in the collection, return "Pokemon is not caught"
-	trainer_data()
o	The method returns the information about the trainer and his pokemon's collection in the format:
"Pokemon Trainer {trainer_name}
 Pokemon count {the amount of pokemon caught}
 - {pokemon_details1}
 ...
 - {pokemon_detailsN}"
"""
from typing import List
from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        for curr_pokemon in self.pokemons:
            if pokemon_name == curr_pokemon.username:
                self.pokemons.remove(curr_pokemon)
                return f"You have released {pokemon_name}"
                break

        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        result = f"Pokemon Trainer {self.name}\n Pokemon count {len(self.pokemons)}\n"
        for un_pokemon in self.pokemons:
            result += f" - {un_pokemon.pokemon_details()}\n"

        return result

