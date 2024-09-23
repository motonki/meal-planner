import random
import fileoperations as fileio

def pick_delimiter():
    options = ['" ', '? ', '! ']
    return random.choice(options)

class Mealplan:
    
    def __init__(self):
        self.meals = []
        self.servings = 0
        self.schedule = [1, 2, 1, 2, 1, 2, 2, 2, 1, 2]
        self.extags = []
        self.syntags = []

    def addrecipe(self, recipe):
        self.meals.append(recipe)

    def get_required_servings(self):
        return sum(self.schedule)

    def get_servings(self):
        return self.servings

    def update_schedule(self, new_schedule):
        self.schedule = new_schedule

    def replacerecipe(self, recipe, index):
        self.meals[index] = recipe

    def __str__(self):
        s = ''
        for recipe in self.meals:
            s += recipe.__str__() + pick_delimiter()
        return s
        return ' '.join([recipe.__str__() for recipe in self.meals])
