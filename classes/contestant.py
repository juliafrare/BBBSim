class Contestant:
    #constructor
    def __init__(self, name, age, index):
        self.name = name
        self.age = age
        self.index = index
        self.att = Attributes()
        #flags
        self.elim = False
        self.nom = False
        self.imn = False

    #prints name of contestant
    def print_name(self):
        print(self.name)

    #prints age of contestant
    def print_age(self):
        print(self.age)

    #prints index of contestant
    def print_index(self):
        print(self.index)

class Attributes:
    #constructor
    def __init__(self):
        #personality attributes
        self.extroversion = 0   #0 = introverted / 10 = extroverted
        self.temperament = 0    #0 = volatile / 10 = calm
        self.friendliness = 0   #0 = unfriendly / 10 = friendly
        self.flirty = 0 #0 = unflirty / 10 = casanova
        self.romantic = 0   #0 = detached / 10 = romantic
        self.playfulness = 0    #0 = serious / 10 = playful
        self.loyalty = 0    #0 = backstabber / 10 = devoted
        self.neatness = 0   #0 = sloppy / 10 = neat, organized

        #skills
        self.strategy = 0   #0 = not strategic / 10 = very strategic
        self.strength = 0   #0 = weak / 10 = strong
        self.stealth = 0    #0 = slow / 10 = quick
        self.endurance = 0 #0 = not resistant / 10 = very resistant
        self.intelligence = 0   #0 = dumb / 10 = smart
        self.charisma = 0   #0 = unlikeable / 10 = very likeable

    def set_attributes(self):
        print("Personality Attributes: ")
        self.extroversion = int(input("Extroversion: "))
        self.temperament = int(input("Temperament: "))
        self.friendliness = int(input("Friendliness: "))
        self.flirty = int(input("Flirtiness: "))
        self.romantic = int(input("Romance: "))
        self.playfulness = int(input("Playfulness: "))
        self.loyalty = int(input("Loyalty: "))
        self.neatness = int(input("Neatness: "))

        print("Skills: ")
        self.strategy = int(input("Strategy: "))
        self.strength = int(input("Strength: "))
        self.stealth = int(input("Stealth: "))
        self.endurance = int(input("Endurance: "))
        self.intelligence = int(input("Intelligence: "))
        self.charisma = int(input("Charisma: "))