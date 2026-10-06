from recipe import Recipe
import json

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
    chosen_recipe = input("Enter the recipe name: ")
    input_string = chosen_recipe.replace(" ", "_")
    show_recipe(input_string)



        


