from typing import List
from pokemon import Pokemon
# from dasdasdasd.pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon_name: Pokemon):
        if pokemon_name not in self.pokemons:
            self.pokemons.append(pokemon_name)
            return f"Caught {pokemon_name.pokemon_details()}"
        elif pokemon_name in self.pokemons:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        # except IndexError:
        #     return f"Pokemon is not caught"
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return f"Pokemon is not caught"

        self.pokemons.remove(pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        pokemons_data = '\n'.join(f"- {p.pokemon_details()}" for p in self.pokemons)
        return f"Pokemon Trainer {self.name}" \
               f"\nPokemon count {len(self.pokemons)}\n" + \
               f"{pokemons_data}"

# ############################################################
# Test_Code_1:
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
# -----------------------------------------------------------
# Output_1:
# Pikachu with health 90
# Caught Pikachu with health 90
# Caught Charizard with health 110
# This pokemon is already caught
# You have released Pikachu
# Pokemon is not caught
# Pokemon Trainer Ash
# Pokemon count 1
# - Charizard with health 110
# ############################################################
