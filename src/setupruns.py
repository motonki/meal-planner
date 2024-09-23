import yaml

class Recipe:
    def __init__(self, recipe_data):
        self.link = recipe_data["url"]
        self.name = recipe_data["name"]
        self.type = recipe_data["type"]
        if "notes" in recipe_data:
            self.notes = recipe_data["notes"]
        else:
            self.notes = None
        # self.season = recipe_data[6]
        # self.extags = recipe_data[7]
        self.syntags = recipe_data["tags"]
        self.instructions = recipe_data["instructions"]
        self.ingredients = recipe_data["ingredients"]
        try:
            self.servings = recipe_data["servings"]
        except ValueError:
            self.servings = 4
        # self.recipefile = recipe_data[10]

        # self.link = recipe_data[0]
        # self.name = recipe_data[1]
        # self.type = recipe_data[2]
        # self.notes = recipe_data[4]
        # self.season = recipe_data[6]
        # self.extags = recipe_data[7]
        # self.syntags = recipe_data[8]
        # try:
        #     self.servings = int(recipe_data[9])
        # except ValueError:
        #     self.servings = 4
        # self.recipefile = recipe_data[10]
def create_yamls(reciperows):
    for row in [rows for rows in reciperows if rows[10] == "testi123.yml"]:
        towrite = {}
        towrite["url"] = row[0]
        towrite["name"] = row[1]
        towrite["instructions"] = ["PLACEHOLDER"]
        towrite["ingredients"] = ["PLACEHOLDER"]
        towrite["notes"] = ["PLACEHOLDER"]
        towrite["type"] = "PLACEHOLDER"
        towrite["tags"] = "PLACEHOLDER"
        towrite["type"] = row[2]
 
        accepted_types = ["Pääruoka", "pääruoka", "pie", "lisuke"]
        if row[2] in accepted_types:
            fname = "data/mains/" + row[1].replace(' ', '')[0:8] + ".yml"
            fhandle = open(fname, 'w')
            yaml.dump(towrite, fhandle)