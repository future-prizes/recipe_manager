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
        number = 0
        for m in shown_recipe.method:
            number +=1
            print(f"{number}. {m}")

def get_all_recipes():
    files = os.listdir("recipes\\")
    recipe_list = []
    for f in files:
        recipe = f.replace(".txt", "")
        recipe = recipe.replace("_", " ")
        recipe_list.append(recipe)
    return recipe_list



print("Welcome to Recipe Manager")

choice = int(input(
"""What would you like to do? 

1. Pick a recipe by name
2. Search for a recipe
3. Edit a recipe
4. See all recipes
5. Delete a recipe


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

    matches = filter(lambda e: search_string in e, all_recipes)
    for m in matches:
        print(m)
    if len(matches) ==0:
        print("No matches found")
    else:
        print("Found matching recipes:")
elif choice ==4:
    get_all_recipes()




        


