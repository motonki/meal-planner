import fileoperations as fileio
from htmlwrapper import write_html
import recommendations
from mealplan import Mealplan
from recipe import Recipe
import os

def create_mealplan(recipes):
    defaultmp = input("Do you want to use default weekly schedule y/n?\n")
    mealplan = Mealplan()
    if defaultmp == "n":
        newmp = input("Please set new schedule (as list of ints, separated only by spaces)\n")
        newmp = [int(num) for num in newmp.split()]
        mealplan.update_schedule(newmp)
    req_servings = mealplan.get_required_servings()
    while mealplan.get_servings() < req_servings:
        new_recipe_file = recommendations.get_recipe(recipes)
        new_recipe = fileio.load_recipe("data/mains/" + new_recipe_file)
        mealplan.addrecipe(new_recipe)
        mealplan.servings += new_recipe.servings
    return mealplan

def reroll_meal(recipes, mealplan, pos):
    new_recipe = fileio.load_recipe("data/mains/" + recommendations.get_recipe(recipes))
    mealplan.replacerecipe(new_recipe, pos)
    return mealplan

def main():
    # recipes = fileio.read_data()
    next_command = "a"
    mealplan = []
    recipe_names = os.listdir("data/mains")
    print(recipe_names)
    while next_command != "q":
        print("Current mealplan is {}.\n List of available commands:\n n. Create mealplan\n s. Save mealplan\n e. Edit mealplan\n u. Update recipes from Google Drive\n q. Exit".format(mealplan.__str__()))
        next_command = input("What would you like to do?\n")
        if next_command == "n":
            mealplan = create_mealplan(recipe_names)
        elif next_command == "s":
            fname = input("Please enter the name for the mealplan\n")
            mpfile = open("{}.txt".format(fname), "w")
            mpfile.write(''.join(str(meal) for meal in mealplan))
            mpfile.close()
        elif next_command == "e":
            print(mealplan)
            posstr = input("Which meal you'd like to swicth?\n")
            pos = int(posstr)
            mealplan = reroll_meal(recipe_names, mealplan, pos)
            print("New mealplan is:")
            print(mealplan)
        elif next_command == "u":
            recipes = fileio.update_recipes()
        elif next_command == "w":
            fileio.write_to_file(mealplan.meals)
            write_html(mealplan.meals)


    

if __name__ == "__main__":
    main()