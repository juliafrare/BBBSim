from .cast import Cast
from .rel import Rel
import random as rd

class Nomination:
    #constructor
    def __init__(self, cast, head_index):
        self.get_head_nominee(cast, head_index)
        self.get_house_nominee(cast, cast.size)
        self.nominees = (self.head_nom, self.house_nom)
        self.print_nomination()

    #gets the nomination from the winner of head challenge
    def get_head_nominee(self, cast, head_index):
        nominee_index = cast.rel.find_lowest_aff(cast, head_index, True)[0]
        self.head_nom = cast.get_cont_by_index(nominee_index)
        self.head_nom.nom = True
        return self.head_nom

    #gets the house nominee with each contestant's vote
    def get_house_nominee(self, cast, cast_size):
        self.vote_count = [0] * cast_size   #vote count for each contestant is stored here
        nom_index = 0 #there is not a nominee yet
        for i in range(cast_size):
            vote = cast.rel.find_lowest_aff(cast, i, True)  #vote is defined by affinity
            self.vote_count[vote[0]] += 1
        for i in range(1, cast_size):
            if self.vote_count[nom_index] < self.vote_count[i]:
                nom_index = i
            self.house_nom = cast.get_cont_by_index(nom_index)
        self.house_nom.nom = True
        return self.house_nom

    def print_nomination(self):
        print(f"The head of the house has nominated {self.nominees[0].name}.")
        print(f"The house has nominated {self.nominees[1].name}.")

class Elimination:
    def __init__(self, nominees):
        self.nominees = nominees
        self.generate_votes()
        self.print_elimination()

    def generate_votes(self):
        self.votes = 50

        while self.votes == 50:
            self.votes = (rd.randrange(10001)) / 100
        
        if self.votes < 50:
            self.elim = self.nominees[0]
        else:
            self.elim = self.nominees[1]

        self.elim.elim = True
        return self.elim

    def print_elimination(self):
        if self.votes < 50:
            self.votes = 100 - self.votes
        print(f"{self.elim.name} is eliminated with {self.votes}% of the computed votes.")