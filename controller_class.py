from explorer_class import *


class Controller:

    def __init__(self, num_of_explorers, day_limit):
        self.explorers = [Explorer() for x in range(num_of_explorers)]
        self.day_limit = day_limit
        self.day = 1

    def control_explorers(self):
        for explorer in self.explorers:
            if self.day == self.day_limit:
                explorer.leave_planet()
                print("leaving planet")
                explorer.write_memoirs()
                print("write memoirs")
            elif explorer.location == "None":
                explorer.go_to_planet()
                print(f"going to planet {explorer.location.name}.")
            elif explorer.supplies == 1 or explorer.medicine == 0 or explorer.ammo == 0:
                explorer.leave_planet()
                print("leaving planet")
            elif explorer.hp < 6:
                explorer.rest()
                print("resting")
            else:
                explorer.explore()
                print("exploring")
                print(f"HP at: {explorer.hp}.")
            self.day += 1


length = 2500
characters = 1
story = Controller(characters, length)
for i in range(length):
    story.control_explorers()
print(story.explorers[0].log)

