import mysql.connector

# Create the connection object
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    password="password"
)

# Create cursor object
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Use the database
cursor.execute("USE task_database")

# Create the Recipes table if it doesn't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
''')

def main_menu(conn, cursor):
    choice = ""
    while choice.lower() != "quit":
        print("\n======================================================")
        print("\nMain Menu:")
        print("-----------------------------------------")
        print("Pick a choice:")
        print("   1. Create a new recipe")
        print("   2. Search for a recipe by ingredient")
        print("   3. Update an existing recipe")
        print("   4. Delete a recipe")
        print("   5. View all recipes")
        print("\n   Type 'quit' to exit the program.")
        choice = input("\nYour choice: ")
        print("\n======================================================\n")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            view_all_recipes(conn, cursor)
        elif choice.lower() == "quit":
            print("Exiting program. Goodbye!")
        else:
            print("Invalid choice. Please try again.")

def create_recipe(conn, cursor):
    name = input("\nEnter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (minutes): "))

    # Split ingredients by comma, strip spaces, and ignore empty strings
    ingredients_input = input("Enter the ingredients (comma separated): ")
    recipe_ingredients = [i.strip() for i in ingredients_input.split(",") if i.strip()]

    difficulty = calc_difficulty(cooking_time, recipe_ingredients)
    recipe_ingredients_str = ", ".join(recipe_ingredients)

    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (name, recipe_ingredients_str, cooking_time, difficulty)

    cursor.execute(sql, val)
    conn.commit()
    print("Recipe saved into the database.")

def calc_difficulty(cooking_time, recipe_ingredients):
    print("Run the calc_difficulty with: ", cooking_time, recipe_ingredients)

    if (cooking_time < 10) and (len(recipe_ingredients) < 4):
        difficulty_level = "Easy"
    elif (cooking_time < 10) and (len(recipe_ingredients) >= 4):
        difficulty_level = "Medium"
    elif (cooking_time >= 10) and (len(recipe_ingredients) < 4):
        difficulty_level = "Intermediate"
    elif (cooking_time >= 10) and (len(recipe_ingredients) >= 4):
        difficulty_level = "Hard"
    else:
        difficulty_level = "Unknown"  # fallback if conditions fail

    print("Difficulty level: ", difficulty_level)
    return difficulty_level

def search_recipe(conn, cursor):
    all_ingredients = []
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    for (recipe_ingredients,) in results:
        recipe_ingredient_split = [i.strip() for i in recipe_ingredients.split(",") if i.strip()]
        all_ingredients.extend(recipe_ingredient_split)

    # Remove duplicates preserving order
    all_ingredients = list(dict.fromkeys(all_ingredients))

    print("\nAll ingredients list:")
    print("------------------------")
    for idx, ingredient in enumerate(all_ingredients, 1):
        print(f"{idx}. {ingredient}")

    try:
        ingredient_searched_nber = input("\nEnter the number corresponding to the ingredient you want to select from the above list: ")
        ingredient_searched_index = int(ingredient_searched_nber) - 1
        ingredient_searched = all_ingredients[ingredient_searched_index]
        print("\nYou selected the ingredient: ", ingredient_searched)
    except (ValueError, IndexError):
        print("An unexpected error occurred. Make sure to select a valid number from the list.")
        return

    print("\nThe recipe(s) below include(s) the selected ingredient: ")
    print("-------------------------------------------------------")
    cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", ('%' + ingredient_searched + '%', ))
    results_recipes_with_ingredient = cursor.fetchall()

    for row in results_recipes_with_ingredient:
        print("\nID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking Time: ", row[3])
        print("Difficulty: ", row[4])

def update_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    try:
        recipe_id_for_update = int(input("\nPlease enter the ID of the recipe you want to update: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    column_for_update = input("\nPlease enter the column you want to update (name, ingredients, or cooking_time): ").lower()

    if column_for_update not in ["name", "ingredients", "cooking_time"]:
        print("Invalid column choice.")
        return

    updated_value = input("\nPlease enter the updated value: ")

    if column_for_update == "name":
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (updated_value, recipe_id_for_update))
        print("Recipe name updated successfully")

    elif column_for_update == "cooking_time":
        try:
            cooking_time_val = int(updated_value)
        except ValueError:
            print("Invalid cooking time. Must be a number.")
            return
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (cooking_time_val, recipe_id_for_update))

        cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id_for_update,))
        recipe = cursor.fetchone()

        if recipe:
            # Ingredients split and strip
            recipe_ingredients = [i.strip() for i in recipe[2].split(",") if i.strip()]
            updated_difficulty = calc_difficulty(cooking_time_val, recipe_ingredients)
            cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, recipe_id_for_update))
            print("Recipe cooking time and difficulty updated successfully")
        else:
            print("Recipe not found.")

    elif column_for_update == "ingredients":
        # Sanitize and split updated ingredients
        updated_ingredients_list = [i.strip() for i in updated_value.split(",") if i.strip()]
        updated_ingredients_str = ", ".join(updated_ingredients_list)
        cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (updated_ingredients_str, recipe_id_for_update))

        cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id_for_update,))
        recipe = cursor.fetchone()

        if recipe:
            cooking_time = recipe[3]
            updated_difficulty = calc_difficulty(cooking_time, updated_ingredients_list)
            cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, recipe_id_for_update))
            print("Recipe ingredients and difficulty updated successfully")
        else:
            print("Recipe not found.")

    conn.commit()

def delete_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    recipe_id_for_delete = input("\nPlease enter the ID of the recipe you want to delete: ")
    try:
        recipe_id_int = int(recipe_id_for_delete)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id_int,))
    conn.commit()
    print("Recipe deleted successfully")

def view_all_recipes(conn, cursor):
    print("\nAll recipes can be found below: ")
    print("-------------------------------------------")

    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    for row in results:
        print("\nID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking Time: ", row[3])
        print("Difficulty: ", row[4])

# Run main menu
main_menu(conn, cursor)
