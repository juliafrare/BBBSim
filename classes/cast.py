from .contestant import Contestant

class Cast:
    #constructor
    def __init__(self, size):
        self.size = size

        self.cast_list = []

        for i in range(size):
            self.cast_list.append(Contestant("a" + str(i), i))

    #prints the whole cast's name and age
    def print_cast(self):
        for i in range(self.size):
            print(self.cast_list[i].name + " " + str(self.cast_list[i].age))

    #eliminates a cast member
    def eliminate(self, cont_index):
        self.cast_list[cont_index].elim = True
        #return self.cast_list.pop(cont_index)