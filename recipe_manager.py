from recipe import Recipe
import json
import re
import os

def show_recipe(recipe):
    with open(f"recipes\\{recipe}.txt", encoding="UTF-8") as string:
        fetched = json.loads(string.read())
        shown_recipe = Recipe(**fetched)
        print(f"Name: {shown_recipe.name}")
        print(f"Type: {shown_recipe.type}")
        print(f"Style: {shown_recipe.style}")
        for i in shown_recipe.ingredients:
            print(f"{i["item"]}: {i["quantity"]}{i["unit"]}")
        step = 0
        for m in shown_recipe.method:
            step +=1
            print(f"{step}. {m}")

def get_all_recipes():
    files = os.listdir("recipes\\")
    recipe_list = []
    for f in files:
        recipe = f.replace(".txt", "")
        recipe = recipe.replace("_", " ")
        recipe_list.append(recipe)
    return recipe_list

def add_ingredients(ingredients_list):
    ingredient = input("Enter an ingredient: ")
    quantity = int(input("Enter the amount: "))
    if type(quantity) != int:
        print("quantities must be numbers")
        quantity = int(input("Enter the amount: "))
    unit = input("Enter the unit (g, ml, etc): ")
    ingredient_template = {
        "item":ingredient, 
        "quantity":quantity, 
        "unit": unit}
    ingredients_list.append(ingredient_template)
    another = input("Add anorther ingredient? y/n ")
    if another =="y":
        add_ingredients()
    else:
        return ingredients_list

def add_method(method):
    print("Next, enter the method of the recipe")
    step = input("Enter the next step: ")
    method.append(step)
    another = input("Add another step? y/n ")
    if another =="y":
        add_method()
    else:
        return method

    

def create_recipe(recipe_name):
    ingredients_list = []
    method = []
    
    new_recipe = input("New recipe's name: ")
    new_recipe_type = input("Type of the recipe: ")
    new_recipe_style = input("Style of the recipe: ")

    finished_i = add_ingredients(ingredients_list)
    finished_m = add_method(method)
    
    
    recipe = {
        "name":new_recipe, 
        "type":new_recipe_type,
        "style":new_recipe_style,
        "ingredients":finished_i,
        "method":finished_m
        }

    with open(f"recipes\\{recipe_name}.txt", "x") as recipe:
        recipe.write(**recipe)

def delete_recipe(recipe):
    os.remove(f"recipes\\{recipe}")
    print(recipe, "deleted")


def main_menu():
    print("Welcome to Recipe Manager")

    choice = int(input(
"""What would you like to do? 

1. Pick a recipe by name    
2. Search for a recipe
3. Edit a recipe
4. See all recipes
5. Create a recipe
6. Delete a recipe

"""))

    if choice == 1:
        chosen_recipe = input("Enter the recipe name: ").strip().lower()
        input_string = chosen_recipe.replace(" ", "_")
        show_recipe(input_string)
    elif choice ==2:
        all_recipes = get_all_recipes()
        joined = " ".join(all_recipes)

        search_string = input("Enter a term to search for: ").strip().lower()
        while len(search_string) <3:
            print("Enter at least 3 characters: ")
            search_string = input("Enter a term to search for: ").strip().lower()

        matches = list(filter(lambda e: search_string in e, all_recipes))
        
        if len(matches) ==0:
            print("No matches found")
        else:
            print("Found matching recipes:")
            for m in matches:
                print(m)

    elif choice ==4:
        all_recipes = get_all_recipes()
        print("\n".join(all_recipes))

    elif choice ==5:
        recipe_name = input("Choose a name for the recipe: ")

    elif choice ==6:
        to_delete = input("Enter a recipe to delete: ").strip().lower()
        to_delete = to_delete.replace(" ", "_")
        confirm = input("Are you sure? y/n ").strip().lower()
        if confirm == "y":
            delete_recipe(to_delete)
        else:
            main_menu()


main_menu()



        


