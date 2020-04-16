import numpy

#relationship/affinity chart
class Rel:
    #constructor
    def __init__(self, size):
       self.affinity = numpy.zeros((size, size))

    #affinity system
    #-100 to -70 = high disaffection
    #-70 to -40 = medium disaffection
    #-40 to -20 = mild disaffection
    #-20 to 20 = neutral
    #20 to 40 = mild affinity
    #40 to 70 = medium affinity
    #70 to 100 = high affinity

    def is_neutral(self, c1, c2):
        if abs(self.affinity[c1][c2]) < 20:
            return True
        else:
            return False

    def mild_affinity(self, c1, c2):
        if self.affinity[c1][c2] > 20 and self.affinity[c1][c2] < 40:
            return True
        else:
            return False

    def medium_affinity(self, c1, c2):
        if self.affinity[c1][c2] > 40 and self.affinity[c1][c2] < 70:
            return True
        else:
            return False
    
    def high_affinity(self, c1, c2):
        if self.affinity[c1][c2] > 70:
            return True
        else:
            return False
    
    def mild_disaff(self, c1, c2):
        if self.affinity[c1][c2] < -20 and self.affinity[c1][c2] > -40:
            return True
        else:
            return False

    def medium_disaff(self, c1, c2):
        if self.affinity[c1][c2] < -40 and self.affinity[c1][c2] > -70:
            return True
        else:
            return False
    
    def high_disaff(self, c1, c2):
        if self.affinity[c1][c2] < -70:
            return True
        else:
            return False

    #finds the person with highest affinity with a contestant in the cast
    def find_highest_aff(self, c1):
        highest = (None, -100)
        for i in range(len(self.affinity[c1])):
            if i == c1:
                pass
            elif self.affinity[c1][i] >= highest[1]:
                highest = (i, self.affinity[c1][i])
        return highest

    #finds the person with lowest affinity with a contestant in the cast
    def find_lowest_aff(self, c1):
        lowest = (None, 100)
        for i in range(len(self.affinity[c1])):
            if i == c1:
                pass
            elif self.affinity[c1][i] <= lowest[1]:
                lowest = (i, self.affinity[c1][i])
        return lowest

    #triggers relationship change between two contestants
    def rel_change(self, a_index, b_index, a_change, b_change):
        if self.rc_boundary_check(a_change, a_index, b_index) == True:
            self.affinity[a_index][b_index] = 100
        else:
            self.affinity[a_index][b_index] += a_change

        if self.rc_boundary_check(b_change, b_index, a_index) == True:  
            self.affinity[b_index][a_index] = 100
        else:
            self.affinity[b_index][a_index] += b_change

    #checks if relationship change is inside the boundaries
    def rc_boundary_check(self, a_change, a_index, b_index):
        if a_change == 0 and self.affinity[a_index][b_index] > 100:
            return True
        elif a_change == 0 and self.affinity[a_index][b_index] < -100:
            return True
        elif a_change > 0 and a_change > (100 - self.affinity[a_index][b_index]):
            return True
        elif a_change < 0 and a_change < (-100 - self.affinity[a_index][b_index]):
            return True
        return False

    #checks if relationship is inside the boundaries (-100 <= aff <= 100) and corrects to 100
    def boundary_check_correct(self, a_index, b_index):
        if self.affinity[a_index][b_index] > 100:
            self.affinity[a_index][b_index] = 100
        elif self.affinity[a_index][b_index] < -100:
            self.affinity[a_index][b_index] = -100

        if self.affinity[b_index][a_index] > 100:
            self.affinity[b_index][a_index] = 100
        elif self.affinity[b_index][a_index] > -100:
            self.affinity[b_index][a_index] = -100