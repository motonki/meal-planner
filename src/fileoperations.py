import csv
from datetime import datetime
import time
import os
import urllib.request
from recipe import Recipe
import yaml
from setupruns import create_yamls

def load_recipe(fname):
    with open(fname, 'r') as rfile:
        try:
            recipe = yaml.safe_load(rfile)
            print(recipe)
            return Recipe(recipe)
        except yaml.YAMLError as exc:
            print(exc)

# Updates data from Google Sheets. Can be deprecated after migration to local recipes has been completed
def update_recipes():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ3qOJ0urI-6fFjCB974ulH9YcFBzQHbqCXcBOo5TmQSfpdY2eTHF9pwXv0zI0kbSPDfisifX-TeP9o/pub?gid=0&single=true&output=csv"
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)
    lines = [l for l in cr]

    local_recipe_f = open("local_recipes.csv", "w+")
    writer = csv.writer(local_recipe_f)
    writer.writerows(lines)
    local_recipe_f.close()
    # recipe_data = [Recipe(line) for line in lines if line[2] == "Pääruoka" or line[2] == "pääruoka"]

    create_yamls(lines)

    # return recipe_data
    return []

# Reads data from Google Sheets. Can be deprecated after migration to local recipes has been completed
def read_data():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ3qOJ0urI-6fFjCB974ulH9YcFBzQHbqCXcBOo5TmQSfpdY2eTHF9pwXv0zI0kbSPDfisifX-TeP9o/pub?gid=0&single=true&output=csv"

    if os.path.exists("local_recipes.csv"):
        mtime = os.path.getmtime("local_recipes.csv")
    else:
        mtime = 0

    if time.mktime(datetime.now().timetuple()) - mtime > 604800:
        response = urllib.request.urlopen(url)
        lines = [l.decode('utf-8') for l in response.readlines()]
        cr = csv.reader(lines)
        lines = [l for l in cr]

        local_recipe_f = open("local_recipes.csv", "w+")
        writer = csv.writer(local_recipe_f)
        writer.writerows(lines)
        local_recipe_f.close()
    else:
        response = open("local_recipes.csv")
        lines = response.readlines()
        cr = csv.reader(lines)
        lines = [l for l in cr]
        response.close()
    
    recipe_data = [Recipe(line) for line in lines if line[2] == "Pääruoka" or line[2] == "pääruoka"]
    recipe_data = [Recipe(line) for line in lines]
    
    return recipe_data

def write_to_file(recipes):
    with open("meals.txt", "w") as output:
        towrite = ""
        for recipe in recipes:
            towrite += recipe.__str__() + "\n\n"

            # raw_recipe = load_recipe(recipe.recipefile)

            # towrite += raw_recipe['name'] + "\n\n"
            towrite += recipe.name + "\n\n"
            towrite += "Huomiot:\n"
            # towrite += "\n".join(raw_recipe['notes']) + "\n\n"

            if isinstance(recipe.ingredients, dict):
                for k, v in recipe.ingredients.items():
                    if isinstance(v, list):
                        towrite += k + "\n"
                        for i in v:
                            towrite += i + "\n"
                        towrite +="\n"
                    else:
                        towrite += v + "\n"
            else:
                for i in recipe.ingredients:
                    towrite += i + "\n"
                towrite +="\n"

            if isinstance(recipe.instructions, dict):
                for k, v in recipe.instructions.items():
                    if isinstance(v, list):
                        towrite += k + "\n"
                        for i in v:
                            towrite += i + "\n"
                        towrite +="\n"
                    else:
                        towrite += v + "\n"
            else:
                for i in recipe.instructions:
                    towrite += i + "\n"
                towrite +="\n"
            towrite += "\n#############\n"

        output.write(towrite)