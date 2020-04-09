from classes.contestant import Contestant
from classes.cast import Cast
from classes.challenge import Challenge

#part = Contestant("Ana", 26)
#part.print_name()
#part.print_age()

cast = Cast(5)

cast.print_cast()

chall = Challenge("new challenge")
chall.generate_results(cast.cast_list, 5)
chall.get_winner()
chall.winner.print_name()

#for i in range(5):
#    cast.append(part)
#    print(cast[i].name)