class Contestant:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.elim = False

    #prints name of contestant
    def print_name(self):
        print(self.name)

    #prints age of contestant
    def print_age(self):
        print(self.age)