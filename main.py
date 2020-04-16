import classes.cast as cst
from classes.challenge import Challenge
import classes.elimination as el
import classes.week as wk

cast = cst.Cast(5)

cast.print_cast()

week = wk.Week(cast)