class Recipe:
    def __init__(self, **recipe:dict):
        self.name = recipe["name"]
        self.type = recipe["type"]
        self.style = recipe["style"]
        self.ingredients = recipe["ingredients"]
        self.method = recipe["method"]
        self.rating = recipe["rating"]

if __name__ == "__main__":
    print("Use recipe_manager!")
