from .contestant import Contestant
from .rel import Rel
import csv
import os

class Cast:
    #constructor
    def __init__(self, file_name):
        self.file_name = file_name
        self.cast_list = []

        size = self.get_cast_from_csv()

        self.size = size
        self.rel = Rel(size)

    #prints the whole cast's name and age
    def print_cast(self):
        for i in range(self.size):
            name = self.cast_list[i].name
            age = str(self.cast_list[i].age)
            print(name + ", " + age)
    
    #gets a Contestant by its index
    def get_cont_by_index(self, index):
        return self.cast_list[index]

    #eliminates a cast member
    def eliminate(self, cont_index):
        self.cast_list[cont_index].elim = True

    #resets weekly flags (nom and imn)
    def reset_weekly_flags(self):
        for i in range(self.size):
            self.cast_list[i].nom == False
            self.cast_list[i].imn == False

    #get cast from csv
    def get_cast_from_csv(self):
        line_count = 0
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    name = row[0]
                    age = row[1]
                    person = Contestant(name, age, line_count - 1)
                    print(f'\t{person.index}. {row[0]} is {row[1]} years old.')
                    self.cast_list.append(person)
                    line_count += 1
            print(f'Processed {line_count} lines.')
        return line_count - 1

    #gets traits from csv
    def get_traits_from_csv(self, traits_file):
        line_count = 0
        with open(traits_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    keys = ["extroversion", "temperament", "friendliness", "flirty", "romantic", "playfulness", "loyalty", "neatness"]
                    values = row
                    self.cast_list[line_count - 1].att.traits = dict(zip(keys, values))
                    person = self.cast_list[line_count - 1]
                    print(f'\t{person.index}. {person.name} has {row[0]} extroversion points.')
                    line_count += 1
            print(f'Processed {line_count} lines.')
        return line_count - 1

    #gets skills from csv
    def get_skills_from_csv(self, skills_file):
        line_count = 0
        with open(skills_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    keys = ["strategy", "strength", "stealth", "endurance", "intelligence", "charisma"]
                    values = row
                    self.cast_list[line_count - 1].att.skills = dict(zip(keys, values))
                    person = self.cast_list[line_count - 1]
                    print(f'\t{person.index}. {person.name} has {row[0]} strategy points.')
                    line_count += 1
            print(f'Processed {line_count} lines.')
        return line_count - 1
