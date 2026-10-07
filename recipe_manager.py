from recipe import Recipe
import json
import os

def show_recipe(recipe):
    if os.path.exists(f"recipes\\{recipe}.txt"):
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
    else:
        print("Recipe does not exist!")

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
    quantity = input("Enter the amount: ")
    unit = input("Enter the unit (g, ml, etc): ")
    ingredient_template = {
        "item":ingredient, 
        "quantity":quantity, 
        "unit": unit}
    ingredients_list.append(ingredient_template)
    another = input("Add anorther ingredient? y/n ")
    if another =="y":
        return add_ingredients(ingredients_list)
    else:
        return ingredients_list

def add_method(method):
    print("Next, enter the method of the recipe")
    step = input("Enter the next step: ")
    method.append(step)
    another = input("Add another step? y/n ")
    if another =="y":
        return add_method(method)
    else:
        return method

def create_recipe():
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
    
    recipe_dump = json.dumps(recipe)

    if os.path.exists(f"recipes\\{new_recipe}.txt"):
        print("Recipe already exists!")
        main_menu()
    else:
        print(f"New recipe: {new_recipe} created!")
        with open(f"recipes\\{new_recipe}.txt", "x") as recipe:
            recipe.write(recipe_dump)

def delete_recipe(recipe):
    if os.path.exists(f"recipes\\{recipe}.txt"):
        os.remove(f"recipes\\{recipe}.txt")
        print(recipe, "deleted!")
        main_menu()
    else: 
        print("Recipe does not exist")
        main_menu()
    
def exit():
    print("Goodbye!")

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
7. Exit

"""))

    if choice == 1:
        chosen_recipe = input("Enter the recipe name: ").strip().lower()
        input_string = chosen_recipe.replace(" ", "_")
        show_recipe(input_string)
        menu = input("Go back to main menu? y/n")
        if menu == "y":
            main_menu()
        else: 
            exit()

    elif choice ==2:
        all_recipes = get_all_recipes()
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
            menu = input("Go back to main menu? y/n")
            if menu == "y":
                main_menu()
            else: 
                exit()

    elif choice ==4:
        all_recipes = get_all_recipes()
        print("\n".join(all_recipes))
        menu = input("Go back to main menu? y/n")
        if menu == "y":
            main_menu()
        else: 
            exit()

    elif choice ==5:
        create_recipe()
        main_menu()

    elif choice ==6:
        to_delete = input("Enter a recipe to delete: ").strip().lower()
        to_delete = to_delete.replace(" ", "_")
        confirm = input("Are you sure? y/n ").strip().lower()
        if confirm == "y":
            delete_recipe(to_delete)
            menu = input("Go back to main menu? y/n")
            if menu == "y":
                main_menu()
            else: 
                exit()
        else:
            main_menu()

    elif choice ==7:
        exit()


if __name__== "__main__":
    main_menu()



        


