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
            person = Contestant(name, age)
            self.cast_list.append(person)

    #prints the whole cast's name and age
    def print_cast(self):
        for i in range(self.size):
            name = self.cast_list[i].name
            age = str(self.cast_list[i].age)
            print(name + ", " + age)

    #eliminates a cast member
    def eliminate(self, cont_index):
        self.cast_list[cont_index].elim = True
        #return self.cast_list.pop(cont_index)