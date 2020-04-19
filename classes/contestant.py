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
        traits = {
            "extroversion" : 0,   #0 = introverted / 10 = extroverted
            "temperament" : 0,    #0 = volatile / 10 = calm
            "friendliness" : 0,   #0 = unfriendly / 10 = friendly
            "flirty" : 0, #0 = unflirty / 10 = casanova
            "romantic" : 0,   #0 = detached / 10 = romantic
            "playfulness" : 0,    #0 = serious / 10 = playful
            "loyalty" : 0,    #0 = backstabber / 10 = devoted
            "neatness" : 0   #0 = sloppy / 10 = neat, organized
        }

        skills = {
            "strategy" : 0, #0 = not strategic / 10 = very strategic
            "strength" : 0,   #0 = weak / 10 = strong
            "stealth" : 0,    #0 = slow / 10 = quick
            "endurance" : 0, #0 = not resistant / 10 = very resistant
            "intelligence" : 0,   #0 = dumb / 10 = smart
            "charisma" : 0   #0 = unlikeable / 10 = very likeable
        }