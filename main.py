import classes.cast as cst
from classes.challenge import Challenge

cast = cst.Cast(5)
rel = cst.Rel(5)

cast.print_cast()

chall = Challenge("new challenge")
chall.generate_results(cast.cast_list, 5)
chall.get_winner()
chall.winner.print_name()

#for i in range(5):
#    cast.append(part)
#    print(cast[i].name)