from .cast import Cast
from random import sample

class Challenge:
    #constructor: creates a challenge object with its description
    def __init__(self, description):
        self.description = description

    #generates the results of a challenge by shuffling the list
    def generate_results(self, cast_list, cast_size):
        self.chall_list = sample(cast_list, cast_size)  #shuffles the cast list into a new list
    
    #gets the winner from the shuffled list
    def get_winner(self):
        self.winner = self.chall_list[0] #gets the winner from first member of list

class HeadChallenge:
    pass

class VetoChallenge:
    pass