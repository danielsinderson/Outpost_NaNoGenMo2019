"""
NOTES:
1) still need methods for making names for most classes
2) still need methods for making descriptions for most classes
3) Characteristics completed for plants and animals, just need microbes, minerals, and alien salvage
"""

import random
import json


def open_json(filename):
    file = open(filename, "r")
    data = json.load(file)
    file.close()
    return data


colors = ["red", "pink", "orange", "yellow", "green", "tan", "teal", "purple", "blue", "white", "black", "brown",
          "iridescent", "maroon", "ochre", "opalescent", "prismatic"]
plant_types = open_json("data_files/plant_types")
animal_types = open_json("data_files/animal_types")
microbe_types = open_json("data_files/microbe_types")
mineral_types = open_json("data_files/mineral_types")


class Life:

    def __init__(self, planet_name):
        self.planet = planet_name
        self.nourishment = self.nourishment_level()
        self.toxicity = self.toxicity_level()
        self.psychoactivity = self.psychoactivity_level()
        self.addictivity = self.addiction_level()
        self.research_value = self.curiosity_level()
        self.beauty = self.beauty_level()
        self.monetary_value = self.overall_value()

    def nourishment_level(self):
        x = random.randint(0, 10)
        return x

    def toxicity_level(self):
        x = random.randint(0, 10)
        return x

    def psychoactivity_level(self):
        x = random.randint(-5, 5)
        return x

    def addiction_level(self):
        x = self.psychoactivity * random.randint(0, 1)
        return x

    def curiosity_level(self):
        x = random.randint(0, 10)
        return x

    def beauty_level(self):
        x = random.randint(0, 10)
        return x

    def overall_value(self):
        if self.toxicity < 2 and self.toxicity < self.nourishment:
            food_value = self.nourishment / 10.0
        else:
            food_value = 0

        if self.psychoactivity > 0:
            drug_value = self.psychoactivity + (10 * self.addictivity)
        else:
            drug_value = 0

        total = food_value + drug_value + self.research_value + self.beauty
        return total


class Tree(Life):

    def __init__(self, planet_name):
        super().__init__(planet_name=planet_name)
        self.fruit = {"outside color": random.choice(colors),
                      "inside color": random.choice(colors),
                      "inside texture": random.choice(plant_types["tree"]["fruit"]["inside texture"]),
                      "size": random.choice(plant_types["tree"]["fruit"]["size"]),
                      "shape": random.choice(plant_types["tree"]["fruit"]["shape"]),
                      "skin/husk": random.choice(plant_types["tree"]["fruit"]["skin/husk"]),
                      "smell": random.choice(plant_types["tree"]["fruit"]["smell"])}
        self.leaves = {"color": random.choice(colors),
                       "size": random.choice(plant_types["tree"]["leaves"]["size"]),
                       "shape": random.choice(plant_types["tree"]["leaves"]["shape"])}
        self.height = random.choice(plant_types["tree"]["height"])
        self.diameter = random.choice([x for x in plant_types["tree"]["diameter"] if x < self.height / 5.0])
        self.bark_texture = random.choice(plant_types["tree"]["bark"])
        self.bark_color = random.choice(colors)
        self.description = self.description()
        self.name = ""
        self.discovered = False

    def description(self):
        return f""

    def name(self):
        self.name = input("You're the first to discover this! Type in a name of 16 or less characters: ")
        if len(self.name) > 16:
            while len(self.name) > 16:
                self.name = input("Try again. Please type in a name of no more than 16 characters: ")
        print("You've just named this", self.name + ".")
        self.discovered = True


class GroundCover(Life):

    def __init__(self, planet_name):
        super().__init__(planet_name=planet_name)
        self.color = random.choice(colors)
        self.shape = random.choice(plant_types["ground cover"]["shape"])
        self.texture = random.choice(plant_types["ground cover"]["texture"])
        if "grass" in self.shape:
            self.flower = {"color": None,
                           "shape": None,
                           "smell": None}
        else:
            self.flower = {"color": random.choice(colors),
                           "shape": random.choice(plant_types["ground cover"]["flower"]["shape"]),
                           "smell": random.choice(plant_types["ground cover"]["flower"]["smell"])}
        self.description = self.description()
        self.name = ""
        self.discovered = False

    def description(self):
        return

    def name(self):
        self.name = input("You're the first to discover this! Type in a name of 16 or less characters: ")
        if len(self.name) > 16:
            while len(self.name) > 16:
                self.name = input("Try again. Please type in a name of no more than 16 characters: ")
        print("You've just named this", self.name + ".")
        self.discovered = True


class Animal(Life):

    def __init__(self, planet_name):
        super().__init__(planet_name=planet_name)
        self.environmental_niche = random.choice(animal_types["environmental niche"])
        self.dietary_niche = random.choice(animal_types["dietary niche"])
        self.size_category = random.choice(list(animal_types["size"]))
        self.min_mass = animal_types["size"][self.size_category][0]
        self.max_mass = animal_types["size"][self.size_category][1]
        self.avg_mass = (self.max_mass + self.min_mass) / 2
        self.skin = random.choice(animal_types["skin"])
        self.color1 = random.choice(colors)
        self.color2 = random.choice([x for x in colors if x != self.color1])
        self.pattern = random.choice(animal_types["pattern"])
        self.mouth = random.choice(animal_types["mouth"][self.dietary_niche])
        self.eyes = {"number": random.randint(animal_types["eyes"]["number"][0], animal_types["eyes"]["number"][1]),
                     "type": random.choice(animal_types["eyes"]["type"]),
                     "visible range": random.choice(animal_types["eyes"]["visible range"])}
        self.locomotion = random.choice(animal_types["locomotion"][self.environmental_niche])
        if random.randint(0, 1) == 0 or self.avg_mass < 100:
            self.poison = 0
        else:
            self.poison = random.randint(animal_types["poison"][0], animal_types["poison"][1])
        self.intelligence = random.randint(animal_types["intelligence"][0], animal_types["intelligence"][1])
        self.aggression = random.choice(animal_types["aggression"])
        self.description = self.animal_description()
        self.name = ""
        self.discovered = False
        self.danger = self.danger_level()

    def animal_description(self):
        return

    def name(self):
        self.name = input("You're the first to discover this! Type in a name of 16 or less characters: ")
        if len(self.name) > 16:
            while len(self.name) > 16:
                self.name = input("Try again. Please type in a name of no more than 16 characters: ")
        print("You've just named this", self.name + ".")
        self.discovered = True

    def danger_level(self):
        size_danger = animal_types["size"][self.size_category][2]
        poison_danger = self.poison
        return size_danger + poison_danger


class Microbe(Life):

    def __init__(self, planet_name):
        super().__init__(planet_name=planet_name)
        self.type = random.choice(microbe_types["type"])
        self.shape = random.choice(microbe_types["shape"][self.type])
        self.harm = random.choice(microbe_types["harm"])
        self.contagious = random.choice(microbe_types["contagious"])
        self.description = self.microbe_description()
        self.name = ""
        self.discovered = False

    def microbe_description(self):
        return

    def name(self):
        self.name = input("You're the first to discover this! Type in a name of 16 or less characters: ")
        if len(self.name) > 16:
            while len(self.name) > 16:
                self.name = input("Try again. Please type in a name of no more than 16 characters: ")
        print("You've just named this", self.name + ".")
        self.discovered = True


class BaseSalvage:

    def __init__(self, supplies, specimens, team_name, days):
        self.monetary_value = supplies + specimens
        self.salvage_level = 0
        self.name = team_name + " Base"
        self.description = f"The base of {team_name}. Abandoned after {days} days."


class AlienSalvage:

    def __init__(self):
        self.research_value = self.curiosity_level()
        self.beauty = self.beauty_level()
        self.salvage_level = self.research_value - self.beauty
        self.monetary_value = self.research_value + self.beauty
        self.description = self.alien_salvage_description()
        self.name = self.alien_salvage_name()

    def curiosity_level(self):
        x = random.randint(5, 20)
        return x

    def beauty_level(self):
        x = random.randint(5, 10)
        return x

    def alien_salvage_description(self):
        return

    def alien_salvage_name(self):
        return


class Mineral:

    def __init__(self, planet_name):
        # class attributes used by self
        self.planet = planet_name
        self.material_properties = random.randint(0, 10)
        self.energy_production = random.randint(0, 10)
        self.color1 = random.choice(colors)
        self.color2 = random.choice([x for x in colors if x != self.color1])
        self.structure = random.choice(mineral_types["structure"])
        self.form = random.choice(mineral_types["form"])
        self.transparency = random.choice(mineral_types["transparency"])

        # class attributes possibly used by other classes
        self.research_value = self.material_properties + self.energy_production
        self.beauty = self.beauty_level()
        self.monetary_value = self.research_value + self.beauty
        self.description = self.mineral_description()
        self.name = ""
        self.discovered = False

    def beauty_level(self):
        form_conversion = {"crystal": (3, 12), "metal": (2, 8), "rock": (0, 5)}
        colors_conversion = {"red": 2, "pink": 2, "orange": 2, "yellow": 2, "green": 2, "tan": 1, "teal": 2,
                             "purple": 2, "blue": 2, "white": 1, "black": 2, "brown": 1, "iridescent": 3, "maroon": 2,
                             "ochre": 1, "opalescent": 3, "prismatic": 4}
        color_beauty = colors_conversion[self.color1] + colors_conversion[self.color2]
        beauty = random.randint(form_conversion[self.form][0], form_conversion[self.form][1]) + color_beauty
        return beauty

    def mineral_description(self):
        return

    def name(self):
        self.name = input("You're the first to discover this! Type in a name of 16 or less characters: ")
        if len(self.name) > 16:
            while len(self.name) > 16:
                self.name = input("Try again. Please type in a name of no more than 16 characters: ")
        print("You've just named this", self.name + ".")
        self.discovered = True
