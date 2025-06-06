Recipe App
Overview
This Recipe App is built using Object-Oriented Programming (OOP) principles in Python. It models recipes as objects, each containing details such as the recipe name, ingredients, cooking time, and difficulty level. The app also supports searching recipes by ingredients and tracks all unique ingredients across recipes.

Features
Create and manage recipes as objects with attributes and methods.

Calculate recipe difficulty based on cooking time and number of ingredients.

Add ingredients to existing recipes dynamically.

Search recipes by ingredient (case-insensitive).

Track all unique ingredients used in all recipes.

Use OOP concepts like encapsulation, inheritance, and polymorphism for clean and reusable code.

Installation
Make sure you have Python installed (version 3.x recommended).

Download or clone the repository:

bash
Copy code
git clone https://github.com/padmajapinnika/recipe-app.git
Navigate to the project folder:

bash
Copy code
cd recipe-app
Run the main Python script:

bash
Copy code
python recipe_app.py
Usage
The app defines a Recipe class. Create instances by providing the name, list of ingredients, and cooking time.

Use methods to add ingredients, calculate difficulty, or search for recipes by ingredient.

Example:

python
Copy code
tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
print(tea)
tea.add_ingredients("Lemon")
print(tea.search_ingredient("lemon")) # True
Reflection on Object-Oriented Programming
OOP organizes code by grouping data and behavior into objects created from classes.

Benefits include modularity, reusability, scalability, encapsulation, and abstraction.

The app demonstrates key OOP concepts: classes and objects, inheritance, polymorphism, and operator overloading.
