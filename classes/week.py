from .challenge import Challenge
from .cast import Cast
from .elimination import Nomination
from .elimination import Elimination

class Week:
    def __init__(self, cast):
        #reset weekly flags
        cast.reset_weekly_flags()
        #wed(1): events
        #thu(2): head of house challenge
        self.chall = Challenge("new challenge")
        self.chall.generate_results(cast.cast_list, 5)
        self.chall.get_winner()
        self.chall.winner.print_name()
        #fri(3): events
        #sat(4): veto challenge/events
        #sun(5): nomination ceremony
        self.nm = Nomination(cast, self.chall.winner.index)
        #mon(6): events
        #tue(7): elimination ceremony
        self.el = Elimination(self.nm.nominees)