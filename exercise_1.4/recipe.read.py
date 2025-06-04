import pickle

recipe = {
    "Ingredient Name": "Tea",
    "Ingredients": ["Tea leaves", "Water", "Sugar"],
    "Cooking Time": 5,
    "Difficulty": "Easy"
}

with open("recipe_binary.bin", "wb") as my_file:
    pickle.dump(recipe, my_file)

with open("recipe_binary.bin","rb") as my_file:
    recipe = pickle.load(my_file)

print("---- Recipe details ----")
print("Name: " + recipe["Ingredient Name"])
print("Ingredients: " + ", ".join(recipe["Ingredients"]))
print("Cooking Time: " + str(recipe["Cooking Time"]) + " minutes")
print("Difficulty: " + recipe["Difficulty"])