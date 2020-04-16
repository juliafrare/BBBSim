from .contestant import Contestant
from .rel import Rel

#event = something that happens outside challenges and eliminations
class Event:
    def __init__(self, prompt):
        self.prompt = f"prompt"
    
    def print_event(self):
        print(self.prompt)


#single event = something that happens with only one character
class SingleEvent(Event):
    def __init__(self, prompt, a):
        self.prompt = f"prompt"
        Event.print_event(self)

#interaction = event that involves two contestants and affects their relationship
class Interaction(Event):
    def __init__(self, prompt, a, b, rel, a_relcg, b_relcg):
        self.a = a
        self.b = b
        self.prompt = f"prompt"
        Event.print_event(self)

    def rel_check(self, rel, minrel, maxrel):
        if minrel < rel.affinity[self.a][self.b] and maxrel > rel.affinity[self.a][self.b]:
            return True
        return False

#outcome = one of the ways an event can turn out
class Outcome:
    def __init__(self, prompt, rel, a, b, a_relcg, b_relcg):
        self.prompt = f"prompt"
        rel.rel_change(a.index, b.index, a_relcg, b_relcg)
        self.print_outcome()
    
    def print_outcome(self):
        print(self.prompt)