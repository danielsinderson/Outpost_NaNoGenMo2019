from planet_generation import *
import math

first_names = ["Gork", "Snood", "Damien", "Arnold"]
last_names = ["Aran", "McCheese", "Floozenoodle"]


class Explorer:

    def __init__(self):
        self.location = "None"
        self.first_name = random.choice(first_names)
        self.last_name = random.choice(last_names)
        self.day = 1
        self.log = ""
        self.hp = 10
        self.attack = 8
        self.supplies = 0
        self.medicine = 0
        self.ammo = 0
        self.money = 1830
        self.mauler = ""

    def go_to_planet(self):
        random.seed()
        self.location = Planet()
        self.buy_resources()
        self.go_to_planet_log(self.location)
        self.day += 1

    def go_to_planet_log(self, planet):
        sentences = {"opening": [
            f"My next planet is {planet.name}. ",
            f"Tomorrow I leave for {planet.name}. ",
            f"The next mission is on a planet called {planet.name}, somewhere on the far side of this arm of the galaxy. ",
            f"They're sending me to {planet.name} next. ",
            f"Another planet, this one called {planet.name}. "],
            "supplies": [
                f"From what I set away from the last mission I've managed to purchase about {self.supplies} days' worth of supplies, including ammunition and the various medical treatments or tissue replacer I may need (god, here's hoping I don't this time). ",
                f"The ship's landing pod and portable base are already set up with the {self.supplies} days' worth of supplies I purchased. ",
                f"I've got {self.supplies} days' worth of supplies this time. Here's hoping the trip isn't cut short this time (here's hoping I don't lose another finger). ",
                f"The supplies are packed away -- about {self.supplies} days' worth -- and my accounts are in order. ",
                f"I've got supplies for {self.supplies} days. "],
            "life_report": [
                f"Initial scans have indicated at least {int(len(planet.plants) / random.randint(1, 4))} species of plants that are all potentially valuable, as well as {int(len(planet.animals) / random.randint(1, 4))} species of potentially valuable animals. ",
                f"Apparently this new planet is teeming with life. No fewer than {int((len(planet.plants) + len(planet.animals) + len(planet.microbes)) / random.randint(1, 4))} distinct candidate research species are outlined in the briefing. ",
                f"I've got the pod stacked high with transport containers. The briefing outlined {int((len(planet.plants) + len(planet.animals) + len(planet.microbes)) / random.randint(1, 4))} different types of organisms that initial scans seem to think will be worthwhile samples. "],
            "mineral_report": [
                f"In addition to the Life Signs Report the geologists on base here seem to think there's a high likelihood of valuable minerals -- at least {int(len(planet.minerals) / random.randint(1, 4))} were sampled by the initial probes. ",
                f"Supposedly this planet is also mineral rich. The probes found {int(len(planet.minerals) / random.randint(1, 4))} valuable mineral traces while they were there. "],
            "closing": [
                f"I guess I should try to get some sleep now. ",
                f"I guess I should try to get some sleep now. Tomorrow is going to be rough. ",
                f"I'm going to sign off now. My stomach is already turning thinking about the landing tomorrow. "]}
        self.log += "DAY 1:\n"
        options = [["opening", "supplies", "life_report", "mineral_report", "closing"]]
        for entry in random.choice(options):
            self.log += random.choice(sentences[entry])
        self.log += "\n\n\n"

    def buy_resources(self):
        spent = math.floor(self.money / 10)
        self.supplies += 2 * spent
        self.medicine += spent
        self.ammo += spent
        self.money = 0

    def explore(self):
        encountered_things = []
        num_objects_encountered = 1
        for i in range(num_objects_encountered):
            choice = random.randint(1, 11)
            if choice <= 3:
                encountered_things.append(random.choice(self.location.plants))
            elif choice <= 7:
                encountered_things.append(random.choice(self.location.animals))
            elif choice <= 9:
                encountered_things.append(random.choice(self.location.microbes))
            else:
                encountered_things.append(random.choice(self.location.minerals))
        for thing in encountered_things:
            self.interact(thing)
        self.supplies -= 1
        self.day += 1

    def interact(self, thing):
        if type(thing) is Tree:
            self.money += thing.monetary_value
            self.acquired_tree_log(thing)
        elif type(thing) is GroundCover:
            self.money += thing.monetary_value
            self.acquired_ground_cover_log(thing)
        elif type(thing) is Animal:
            if self.attack > thing.danger:
                self.money += thing.monetary_value
                self.ammo -= 1
                self.acquired_animal_log(thing)
            else:
                if random.randint(1, 8) < thing.aggression[0]:
                    if random.randint(1, 4) < 2:
                        self.hp -= thing.danger
                        self.ammo -= 1
                        if self.hp < 1:
                            self.hp = 1
                        self.mauler = thing
                        self.attacked_log(thing)
                    else:
                        self.ran_away_log(thing)
                else:
                    self.observed_animal_log(thing)
        elif type(thing) is Microbe:
            if random.randint(1, 8) < thing.contagious[1] and random.randint(0, 1) == 1:
                print("INFECTED!")
                self.hp -= thing.harm[1]
                if self.hp < 1:
                    self.hp = 1
                self.contracted_illness_log(thing)
            else:
                self.money += thing.monetary_value
                self.acquired_microbe_log(thing)
            return
        elif type(thing) is Mineral:
            self.money += thing.monetary_value
            self.acquired_mineral_log(thing)

    def acquired_tree_log(self, tree):
        sentences = {
            "discovery_neutral": [
                f"Found one of the organisms of interest today -- a tree, standing around {tree.height} meters tall and with a diameter of around {tree.diameter} meters.",
                "Got some samples from one of the trees of interest today.",
                "New samples taken today, this time from a tree.",
                f"Another tree discovered. It's {tree.height} meters tall and {tree.diameter} meters across."
                "More samples for the weird room. From a tree this time."
            ],
            "discovery_big": [
                f"Discovered one of the trees of interest today and holy shit it's impressive. The report makes note of the size but a {tree.height} meter tree isn't really experienced until your standing in front of it and hurting your neck trying (and failing) to see the top.",
                f"It's a big one today -- a {tree.height} meter tall tree.",
                f"Another one for the record books: {tree.height} meters tall and {tree.diameter} meters across.",
                f"Found a tree today must've been about {tree.height} meters tall. Truly a monster."
            ],
            "discovery_small": [
                f"A little guy today, a tree just {tree.height} meters tall and {tree.diameter} across.",
                f"I found one of the trees today, a fairly small one at around {tree.height} meters tall. Looks almost like an orchard of them."
            ],
            "bark": [f"The bark is {tree.bark_texture} and {tree.bark_color}.",
                     f"The bark has a subtle {tree.bark_color} color and is {tree.bark_texture}.",
                     f"The bark of this tree is {tree.bark_texture} and has a web of {tree.bark_color} veins across it.",
                     f"It's got {tree.bark_color} bark that's {tree.bark_texture} to touch."],
            "leaves": [f"The leaves are {tree.leaves['size']}, {tree.leaves['shape']}, and {tree.leaves['color']}."],
            "fruit_outside": [
                f"The fruit is a {tree.fruit['shape']} {tree.fruit['size']} with a {tree.fruit['skin/husk']} that is {tree.fruit['outside color']} on the outside."],
            "fruit_inside": [
                f"The inside of the fruit is no less alien. It's {tree.fruit['inside color']} and has a {tree.fruit['inside texture']} texture. The smell is {tree.fruit['smell']}."]
        }
        if tree.height > 68:
            choices = [random.choice(sentences["discovery_neutral"] + sentences["discovery_big"]),
                       random.choice(sentences["bark"]),
                       random.choice(sentences["leaves"]),
                       random.choice(sentences["fruit_outside"]),
                       random.choice(sentences["fruit_inside"])]
        elif tree.height < 12:
            choices = [random.choice(sentences["discovery_neutral"] + sentences["discovery_small"]),
                       random.choice(sentences["bark"]),
                       random.choice(sentences["leaves"]),
                       random.choice(sentences["fruit_outside"]),
                       random.choice(sentences["fruit_inside"])]
        else:
            choices = [random.choice(sentences["discovery_neutral"]),
                       random.choice(sentences["bark"]),
                       random.choice(sentences["leaves"]),
                       random.choice(sentences["fruit_outside"]),
                       random.choice(sentences["fruit_inside"])]
        self.log += f"DAY {self.day}:\n"
        self.log += ' '.join(choices)
        self.log += "\n\n\n"

    def acquired_ground_cover_log(self, gc):
        sentences = {
            "discovery": [f"Discovered a {gc.shape} today from the list of promising specimens.",
                          f"Took samples from a {gc.shape}.",
                          f"Found a {gc.shape} for the archives today."],
            "description": [f"It has a {gc.texture} texture."],
            "flower": [
                f"The {gc.shape} has a {gc.flower['color']} {gc.flower['shape']} flower that smells {gc.flower['smell']}."]
        }
        if gc.flower['color'] is not None:
            log = [random.choice(sentences["discovery"]),
                   random.choice(sentences["description"]),
                   random.choice(sentences["flower"])]
        else:
            log = [random.choice(sentences["discovery"]),
                   random.choice(sentences["description"])]
        self.log += f"DAY {self.day}:\n"
        self.log += ' '.join(log)
        self.log += "\n\n\n"

    def acquired_animal_log(self, animal):
        sentences = {}
        log = []
        self.log += f"DAY {self.day}:\n"
        self.log += ' '.join(log)
        self.log += "\n\n\n"

    def attacked_log(self, animal):
        locales = {
            "aquatic": ["a lake", "a glacial lake", "a river", "an inland sea", "a sea", "a channel"],
            "terrestrial": ["an alluvial valley", "a forest", "some woodland", "a highland desert", "a desert",
                            "some tundra"],
            "arboreal": ["a forest", "some woodland"],
            "subterranean": ["a cave", "a pit", "a fissure"],
            "aerial": ["an alluvial valley", "a forest", "a highland desert", "a desert", "some tundra", "a forest",
                       "some woodland"]
        }
        activities = {
            "aquatic": ["swimming in", "boating on", "crossing", "exploring"],
            "terrestrial": ["walking through", "hiking in", "crossing", "exploring"],
            "arboreal": ["walking", "hiking", "crossing", "exploring"],
            "subterranean": ["delving", "exploring"],
            "aerial": ["walking", "hiking", "crossing", "exploring"]
        }
        injury_types = {
            "bone": {
                "injury": ["fractured", "shattered", "broken", "cut", "sprained", "bruised"],
                "location": ["rib", "clavicle", "ulna", "radius", "humurus", "femur", "tibia", "fibula"]
            },
            "muscle": {
                "injury": ["cut", "sliced", "pulled", "pierced", "bruised", "battered"],
                "location": ["arm", "leg", "chest", "gut", "shoulder", "face", "back"]
            },
            "organ": {
                "injury": ["bruised"],
                "location": ["kidney", "liver", "lung"]
            }
        }
        injury_type_1 = random.choice(["bone", "muscle", "organ"])
        injury_type_2 = random.choice(["bone", "muscle", "organ"])
        injuries = [
            random.choice(injury_types[injury_type_1]["injury"]) + " " + random.choice(injury_types[injury_type_1]["location"]),
            random.choice(injury_types[injury_type_2]["injury"]) + " " + random.choice(injury_types[injury_type_2]["location"])]
        terror_adjectives = ["terrifying", "tremendous", "telling", "frightening"]
        place = random.choice(locales[animal.environmental_niche])
        activity = random.choice(activities[animal.environmental_niche])
        mouth_adjectives = ["large", "unsettling", "horrifying", "giant"]
        sentences = {
            "attack": [f"I was attacked today while {activity} {place}.",
                       f"Accidentally angered an animal today while {activity} {place}.",
                       f"I was {activity} {place} today and disturbed one of the local animals.",
                       f"I set out to {activity} {place} early this morning when I was attacked by a species of the local fauna."],
            "injury": [f"It seems to have given me a {injuries[0]} and a {injuries[1]}.",
                       f"Feels like I have a {injuries[0]} and a {injuries[1]}.",
                       f"I think I have a {injuries[0]} and a {injuries[1]}, I'll have to wait for the autodoc to finish it's analysis though.",
                       f"Back at the base now but it looks like I have a {injuries[0]} and a {injuries[1]}. Likely have to spend tomorrow resting as well."],
            "get away": ["Barely managed to get away. Not even sure how I did really.",
                         "I noticed something was off. Barely acted fast enough. I think I'm safe now though.",
                         "Not sure if it was a defensive attack or if it was hunting me. I'm lucky I'm not dead.",
                         "Had to retreat immediately. Don't know if I was unlucky or if this area is effectively off-limits. Leaving it be for now and moving on.",
                         "I'm leaving this area. Going back to the last known safe place to rest in the pod.",
                         "I'm not going back there. Not worth it. Not on a solo mission."],
            "sighting": [
                f"The creature was {animal.size_category}. I couldn't get a good look but I'd say it might've been {animal.max_mass} kg.",
                f"I got a decent look at the thing while retreating. It looked to have {animal.eyes['number']} {animal.eyes['type']} and {animal.color1} and {animal.color2} {animal.skin}. And it was {animal.size_category}. Easily {animal.min_mass} kg and possibly much much more.",
                f"Whatever it was that attacked me it was {animal.size_category}. I didn't ever see it but the effect it had on the {place.split(' ')[-1]} as it came towards me was {random.choice(terror_adjectives)}.",
                f"It was monstrous. Maybe {animal.min_mass} kg and possibly much much more. It had {animal.color1} and {animal.color2} {animal.skin} and a {random.choice(mouth_adjectives)} {animal.mouth}. So lucky to be here still."
                ]
        }
        log = [random.choice(sentences["attack"]),
               random.choice(sentences["injury"]),
               random.choice(sentences["get away"]),
               random.choice(sentences["sighting"])]
        self.log += f"DAY {self.day}:\n"
        self.log += ' '.join(log)
        self.log += "\n\n\n"

    def ran_away_log(self, animal):
        locales = {
            "aquatic": ["a lake", "a glacial lake", "a river", "an inland sea", "a sea", "a channel"],
            "terrestrial": ["an alluvial valley", "a forest", "some woodland", "a highland desert", "a desert",
                            "some tundra"],
            "arboreal": ["a forest", "some woodland"],
            "subterranean": ["a cave", "a pit", "a fissure"],
            "aerial": ["an alluvial valley", "a forest", "a highland desert", "a desert", "some tundra", "a forest",
                       "some woodland"]
        }
        activities = {
            "aquatic": ["swimming in", "boating on", "crossing", "exploring"],
            "terrestrial": ["walking through", "hiking in", "crossing", "exploring"],
            "arboreal": ["walking", "hiking", "crossing", "exploring"],
            "subterranean": ["delving", "exploring"],
            "aerial": ["walking", "hiking", "crossing", "exploring"]
        }
        terror_adjectives = ["terrifying", "tremendous", "telling", "frightening"]
        place = random.choice(locales[animal.environmental_niche])
        activity = random.choice(activities[animal.environmental_niche])
        sentences = {
            "attack": [f"I was attacked today while {activity} {place}.",
                       f"Accidentally angered an animal today while {activity} {place}.",
                       f"I was {activity} {place} today and disturbed one of the local animals.",
                       f"I set out to {activity} {place} early this morning when I was attacked by a species of the local fauna."],
            "get away": ["Barely managed to get away. Surprised the hell out of me.",
                         "I saw it coming from a ways away, thank god, and was able to retreat to a safe place.",
                         "Not sure if it was defensive or hungry but I'm lucky to have gotten away.",
                         "Had to retreat immediately. Don't know if I was unlucky or if this area is effectively off-limits. Leaving it be for now and moving on.",
                         "I'm going to leave this area for a different expedition.",
                         "I'm skipping this area this time around. Not worth it."],
            "sighting": [
                f"The creature was {animal.size_category}. I couldn't get a good look but I'd say it might've been {animal.max_mass} kg.",
                f"I got a decent look at the thing while retreating. It looked to have {animal.eyes['number']} {animal.eyes['type']} and {animal.color1} and {animal.color2} {animal.skin}. And it was {animal.size_category}. Easily {animal.min_mass} kg and possibly much much more.",
                f"Whatever it was that attacked me it was {animal.size_category}. I didn't ever see it but the effect it had on the {place.split(' ')[-1]} as it came towards me was {random.choice(terror_adjectives)}.",
                ]
        }
        log = [random.choice(sentences["attack"]),
               random.choice(sentences["get away"]),
               random.choice(sentences["sighting"])]
        self.log += f"DAY {self.day}:\n"
        self.log += ' '.join(log)
        self.log += "\n\n\n"

    def observed_animal_log(self, animal):
        locales = {
            "aquatic": ["a lake", "a glacial lake", "a river", "an inland sea", "a sea", "a channel"],
            "terrestrial": ["an alluvial valley", "a forest", "some woodland", "a highland desert", "a desert",
                            "some tundra"],
            "arboreal": ["a forest", "some woodland"],
            "subterranean": ["a cave", "a pit", "a fissure"],
            "aerial": ["an alluvial valley", "a forest", "a highland desert", "a desert", "some tundra", "a forest",
                       "some woodland"]
        }
        activities = {
            "aquatic": ["swimming in", "boating on", "crossing", "exploring"],
            "terrestrial": ["walking through", "hiking in", "crossing", "exploring"],
            "arboreal": ["walking", "hiking", "crossing", "exploring"],
            "subterranean": ["delving", "exploring"],
            "aerial": ["walking", "hiking", "crossing", "exploring"]
        }
        adverbs = ["truly", "very", "troublingly", "marvelously"]
        adjectives = ["bizarre", "unique", "impressive", "uncomfortable", "one of a kind", "new", "interesting",
                      "fucked up"]
        witness_nouns = ["sight", "occurrence", "thing", "creature", "animal", "event"]
        place = random.choice(locales[animal.environmental_niche])
        sentences = {
            "discovery1": [
                f"Came across a {random.choice(adjectives)} looking animal while {random.choice(activities[animal.environmental_niche])} {place} today."],
            "discovery2": ["Not sure if it just didn't notice me or didn't care.",
                           "Didn't appear to notice me.",
                           "Definitely noticed me but didn't care at all.",
                           "Looked right at me. Seemed more curious than wary. Lucky it didn't think I was a threat."],
            "sample": ["Thought about collecting a sample, but I really didn't want to provoke it.",
                       "No sample taken. Definitely too dangerous. Writing my observations in the log though for any future expedition.",
                       "Writing my observations in lieu of a sample. Any attempt to sample from this thing is going to need a full, and very well-prepared extraction team."],
            "size": [f"It was {animal.size_category}. Easily {animal.min_mass} kilograms."],
            "skin": [
                f"It appeared to have {animal.skin} that was {animal.color1}, {animal.color2} and {animal.pattern}."],
            "eyes_mouth_diet": [
                f"The thing appeared to be {animal.dietary_niche}. It had a {animal.mouth} and {animal.eyes['number']} {animal.eyes['type']}."],
            "locomotion": [
                f"It moved by {animal.locomotion} through the {' '.join(place.split(' ')[1:])}. A {random.choice(adverbs)} {random.choice(adjectives)} {random.choice(witness_nouns)}."],

        }
        log = [random.choice(sentences["discovery1"]),
               random.choice(sentences["discovery2"]),
               random.choice(sentences["sample"]),
               random.choice(sentences["size"]),
               random.choice(sentences["skin"]),
               random.choice(sentences["eyes_mouth_diet"]),
               random.choice(sentences["locomotion"])]
        self.log += f"DAY {self.day}:\n"
        self.log += ' '.join(log)
        self.log += "\n\n\n"

    def contracted_illness_log(self, microbe):
        organs = ["kidneys", "liver", "lungs", "immune system", "brain"]
        mild_symptoms = ["a rash", "some nausea", "a mild fever", "a slight cough", "the shits"]
        sentences = {
            "neutral": ["Feeling ill. Contracted something I think.",
                        "Must've contracted something today. Not feeling well at all."],
            "serious": [
                f"The {microbe.type} I came into contact today must've infected me. Running a fever and was getting delirious. In the autodoc now.",
                f"Started feeling strange during my expedition today. Getting treated at base right now and it looks like it was a {microbe.type} that I ran into that was attacking my {random.choice(organs)}."],
            "mild": [f"Got {random.choice(mild_symptoms)} from coming into contact with an alien {microbe.type} today.",
                     f"Something on this planet just gave me {random.choice(mild_symptoms)}. Lucky it wasn't something worse."]
        }
        log = []
        if microbe.harm[1] > 5:
            log.append(random.choice(sentences["serious"] + sentences["neutral"]))
        elif microbe.harm[1] < 4:
            log.append(random.choice(sentences["mild"] + sentences["neutral"]))
        else:
            log.append(random.choice(sentences["neutral"]))
        self.log += f"DAY {self.day}:\n"
        self.log += ' '.join(log)
        self.log += "\n\n\n"

    def acquired_microbe_log(self, microbe):
        sentences = {
            "discovery": [f"Found an interesting {microbe.shape} {microbe.type}. Samples taken."],
            "initial_tests": [f"Initial tests suggest that it might be {microbe.harm[0]}."]
        }
        log = [random.choice(sentences["discovery"]),
               random.choice(sentences["initial_tests"])]
        self.log += f"DAY {self.day}:\n"
        self.log += ' '.join(log)
        self.log += "\n\n\n"

    def acquired_mineral_log(self, mineral):
        sentences = {
            "discovery": [f"Found a {mineral.color1} and {mineral.color2} {mineral.form} to add to the samples.",
                          f"Found an interesting mineral today. It's a {mineral.form} banded with {mineral.color1} and {mineral.color2}.",
                          f"This mineral sample I took today is pretty wild. It's a {mineral.color1} {mineral.form} that appears {mineral.color2} if you hold it to the light just right."],
            "crystal": [f"It's a {mineral.transparency} {mineral.structure} crystal.",
                        f"Looks like a {mineral.transparency} {mineral.structure} crystalline structure."],
            "low_energy_low_material": [
                "Material doesn't appear to have any energy potential or interesting properties.",
                "Other than it's looks the sample seems like a dud."],
            "low_energy_good_material": [
                "Doesn't appear to have any energy potential but its material properties are worth looking into."],
            "high_energy_low_material": [
                "This mineral is basically humming with radiation. Lucky I'm wearing protection."],
            "high_energy_high_material": [
                "Interesting thing here. Appears to be almost physically indestructible and it's also glowing with some kind of energy."]
        }
        log = [random.choice(sentences["discovery"])]
        if mineral.form == "crystal":
            log.append(random.choice(sentences["crystal"]))
        if mineral.energy_production > 7:
            if mineral.material_properties > 6:
                log.append(random.choice(sentences["high_energy_high_material"]))
            else:
                log.append(random.choice(sentences["high_energy_low_material"]))
        elif mineral.energy_production < 3:
            if mineral.material_properties > 6:
                log.append(random.choice(sentences["low_energy_good_material"]))
            elif mineral.material_properties < 3:
                log.append(random.choice(sentences["low_energy_low_material"]))
        self.log += f"DAY {self.day}:\n"
        self.log += ' '.join(log)
        self.log += "\n\n\n"

    def rest(self):
        self.supplies -= 1
        self.medicine -= 1
        self.hp += 5
        self.rest_log()
        self.day += 1

    def rest_log(self):
        sentences = {
            "mildly injured": [
                f"After that encounter I need to take a day to recuperate a bit. Seems like every planet I go to I end up chewed on or infected by some fucking thing or another but at least I'm still well enough to complain about it. By tomorrow I'll be back out there. I still have {self.supplies} days' worth of supplies left.",
                f"I'm taking the day to rest up a bit. Thank the lord for the mobile base that I'm able to take days like this now and then. As it is I should be back out there tomorrow. Looks like I still have enough supplies for {self.supplies} days. Hopefully I don't need to spend them all hiding in here.",
                f"Taking the day to rest, read over the specimen logs, and drink another glass of the whiskey I brought along. It hasn't been as bad as it could be, but my body is feeling pretty beat up so hiding in the bubble for awhile seems like the best option. Just {self.supplies} days left before I fly the fuck outta here. Hopefully these specimens I've captured will be worth enough to float me for awhile."],
            "severely injured": [
                f"Barely holding on here. Taking a few days to try and not die. {self.last_name} out."
                f"In the autodoc. Barely made it but healing up okay now. I think I might ask the replicator to make a tombstone for me before my next trip out. Or maybe I should just spray paint {self.first_name} {self.last_name} on the side of the mobile base. Bigger than tombstone anyway."
                f"Severely injured. Made it to the pod. Need to rest. {self.medicine} packs of medicine left."
                f"I honestly might die on this planet. Managed to escape to the pod. In the autodoc now. {self.medicine} packs of medicine left."]
        }
        self.log += f"DAY {self.day}:\n"
        if self.hp > 2:
            self.log += random.choice(sentences["mildly injured"])
        else:
            self.log += random.choice(sentences["severely injured"])
        self.log += "\n\n\n"

    def leave_planet(self):
        self.leave_log()
        self.day = 1
        self.location = "None"

    def leave_log(self):
        sentences = {
            "intro": [
                f"Leaving {self.location.name} today after {self.day} days of exploring (and surviving) this place.",
                f"It's been {self.day} days already (or finally depending on my mood) but I'm leaving {self.location.name} today."],
            "middle": [
                f"I have {self.ammo} shells of ammunition left and {self.medicine} packs of medicine left and preliminary reports from base suggest my collection of specimens will be worth around {int(self.money)} credits. Not a bad haul. Possibly even worth the nightmares I've added to my brain's collection."],
        }
        self.log += f"DAY {self.day}:\n"
        self.log += random.choice(sentences["intro"])
        self.log += random.choice(sentences["middle"])
        self.log += "\n\n\n"

    def write_memoirs(self):
        filename = f"Explorer_Memoirs/{self.first_name}_{self.last_name}_Memoirs"
        file = open(filename, "w+")
        file.write(self.log)
        file.close()