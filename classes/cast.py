from .contestant import Contestant
from .rel import Rel

class Cast:
    #constructor
    def __init__(self, size):
        self.size = size

        self.cast_list = []
        self.rel = Rel(size)

        for i in range(size):
            #self.cast_list.append(Contestant("a" + str(i), i))
            name = str(input())
            age = int(input())
            index = i
            person = Contestant(name, age, index)
            self.cast_list.append(person)

    #prints the whole cast's name and age
    def print_cast(self):
        for i in range(self.size):
            name = self.cast_list[i].name
            age = str(self.cast_list[i].age)
            print(name + ", " + age)
    
    def get_cont_by_index(self, index):
        return self.cast_list[index]

    #eliminates a cast member
    def eliminate(self, cont_index):
        self.cast_list[cont_index].elim = True

    def reset_weekly_flags(self):
        for i in range(self.size):
            self.cast_list[i].nom == False
            self.cast_list[i].imn == False