"""
NOTES:
1) Needs real planet_description function
2) create_planet_name function is pretty basic right now
3) Needs inanimate objects creation functions (which need the requisite classes made)
"""

from planet_features_generation import *

# keeps track of players interactions with certain planets without needing to store the entire planet instance in
# memory, only those parts that changed based on the previous interactions
visited_planets = {}


# creates a name consisting of 3 to 8 alphanumeric characters
def create_planet_name():
    name = ''
    length = random.randint(3, 8)
    alphanums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'x', 'y', 'z']
    for i in range(length):
        if i == 0:
            choice = random.choice(alphanums[10:]).upper()
        else:
            choice = random.choice(alphanums)
        name += choice
    if name not in visited_planets:
        visited_planets[name] = {'visited': True, 'ruined bases': [], 'known organisms': [], 'known minerals': [],
                                 "alien artifacts found": []}
        return name
    else:
        return create_planet_name()


# assigns a prime number P to each alphanumeric character then multiplies it by the ith prime for a new number N.
# Each of these numbers are then summed to get a unique seed.
def get_seed_from_name(name):
    string_to_int = {'a': 103, 'b': 107, 'c': 109, 'd': 113, 'e': 127, 'f': 181, 'g': 191, 'h': 193, 'i': 197, 'j': 23,
                     'k': 29, 'l': 31, 'm': 37, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73,
                     'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101, '0': 131, '1': 137, '2': 139, '3': 149, '4': 151,
                     '5': 157, '6': 163, '7': 167, '8': 173, '9': 179}
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    seed = 0
    for index in range(len(name)):
        character_value = string_to_int[name[index].lower()]
        seed += primes[index] * character_value
    return seed


class Planet:

    def __init__(self, name=create_planet_name()):
        self.name = name
        self.planet_seed = get_seed_from_name(self.name)
        random.seed(self.planet_seed)
        self.gravity = random.randint(5, 20) / 10.0
        self.biodiversity = random.randint(1, 10)
        self.plants = self.create_objects(Tree) + self.create_objects(GroundCover)
        self.animals = self.create_objects(Animal)
        self.microbes = self.create_objects(Microbe)
        self.minerals = self.create_objects(Mineral)
        self.description = self.planet_description()
        self.past_interactions = visited_planets[name]

    def create_objects(self, object_class):
        objects = []
        for i in range(random.randint(200, 400) * self.biodiversity):
            objects.append(object_class(self.name))
        return objects

    def planet_description(self):
        return self.name
