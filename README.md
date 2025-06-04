# Recipe Storage and Search App

This is a Python-based console application that allows users to input, save, and search recipes. Recipes are stored using Python’s `pickle` module for easy retrieval and persistence.

---

## Features

- Add new recipes with ingredients and cooking time
- Automatically calculate recipe difficulty
- Store all recipes and ingredients in a binary file
- Search for recipes by ingredient
- Handle file read/write errors gracefully

---

## File Descriptions

### `recipe_input.py`

- Allows the user to input one or more recipes.
- Stores recipe data in a binary `.dat` file using the `pickle` module.
- Automatically calculates and assigns a difficulty level based on the number of ingredients and cooking time.

### `recipe_search.py`

- Loads recipe data from the saved file.
- Displays all available ingredients and allows the user to search for recipes containing a selected ingredient.
- Displays matching recipes clearly using a `display_recipe()` function.

---

## How to Use

1. **Input Recipes**  
    Run the following command in your terminal to add recipes:
   ```bash
   python recipe_input.py
   ```
2. **Search Recipes**
   Run this command to search for recipes by ingredient:
   python recipe_search.py
3. **File Saving**
   When prompted, enter a filename (e.g., recipes.dat). The program will either create a new file or update an existing one.

Concepts Used

File handling (open, read, write)

Error handling (try-except)

Pickling with the pickle module

Functions and loops

User input handling
Author
Padmaja
Full-stack Web Developer
