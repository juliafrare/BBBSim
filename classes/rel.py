import numpy

#relationship/affinity chart
class Rel:
    #constructor
    def __init__(self, size):
       self.affinity = numpy.zeros((size, size))

    #affinity system
    #-10 to -7 = high disaffection
    #-7 to -4 = medium disaffection
    #-4 to -2 = mild disaffection
    #-2 to 2 = neutral
    #2 to 4 = mild affinity
    #4 to 7 = medium affinity
    #7 to 10 = high affinity

    def is_neutral(self, c1, c2):
        if abs(self.affinity[c1][c2]) < 2:
            return True
        else:
            return False

    def mild_affinity(self, c1, c2):
        if self.affinity[c1][c2] > 2 and self.affinity[c1][c2] < 4:
            return True
        else:
            return False

    def medium_affinity(self, c1, c2):
        if self.affinity[c1][c2] > 4 and self.affinity[c1][c2] < 7:
            return True
        else:
            return False
    
    def high_affinity(self, c1, c2):
        if self.affinity[c1][c2] > 7:
            return True
        else:
            return False
    
    def mild_disaff(self, c1, c2):
        if self.affinity[c1][c2] < -2 and self.affinity[c1][c2] > -4:
            return True
        else:
            return False

    def medium_disaff(self, c1, c2):
        if self.affinity[c1][c2] < -4 and self.affinity[c1][c2] > -7:
            return True
        else:
            return False
    
    def high_disaff(self, c1, c2):
        if self.affinity[c1][c2] < -7:
            return True
        else:
            return False

    #finds the person with highest affinity with a contestant in the cast
    def find_highest_aff(self, c1):
        highest = (None, -10)
        for i in range(len(self.affinity[c1])):
            if i == c1:
                pass
            elif self.affinity[c1][i] >= highest[1]:
                highest = (i, self.affinity[c1][i])
        return highest

    #finds the person with lowest affinity with a contestant in the cast
    def find_lowest_aff(self, c1):
        lowest = (None, 10)
        for i in range(len(self.affinity[c1])):
            if i == c1:
                pass
            elif self.affinity[c1][i] <= lowest[1]:
                lowest = (i, self.affinity[c1][i])
        return lowest