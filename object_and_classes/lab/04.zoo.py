class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammal = list()
        self.fish = list()
        self.bird = list()

    def add_animal(self, species, name):
        command = f"self.{species}.append('{name}')"
        eval(command)

    def get_info(self, species):
        command = f"\", \".join(self.{species})"
        if species == "fish":
            species = species.capitalize() + "es"
        else:
            species = species.capitalize() + "s"

        output = f"{species} in {name_of_zoo}: {eval(command)}"
        return output


name_of_zoo = input()
total_animals = int(input())
zoo = Zoo(name_of_zoo)

for _ in range(total_animals):
    current_animal = input().split()
    current_species = current_animal[0]
    current_name = current_animal[1]
    zoo.add_animal(current_species, current_name)

info_species = input()
print(zoo.get_info(info_species))
print(f"Total animals: {total_animals}")
