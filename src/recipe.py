# import fileoperations as fileio

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
        if "servings" in recipe_data:
            try:
                self.servings = recipe_data["servings"]
            except ValueError:
                self.servings = 4
        else:
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




    def __str__(self):
        return "{}".format(self.name)