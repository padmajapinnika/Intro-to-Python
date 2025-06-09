# 🧑‍🍳 Recipe Manager CLI App

A simple command-line interface (CLI) application written in Python that allows users to **create**, **search**, **update**, **delete**, and **view** recipes stored in a MySQL database. Each recipe includes a name, list of ingredients, cooking time, and a difficulty level automatically calculated.

## 📦 Features

- Add new recipes to a MySQL database
- View all saved recipes
- Search for recipes by ingredient
- Update recipe details (name, ingredients, cooking time)
- Automatically calculate difficulty level
- Delete recipes

## 🛠️ Technologies Used

- Python 3
- MySQL
- `mysql-connector-python` package

## 📋 Difficulty Calculation Logic

```python
if cooking_time < 10 and number_of_ingredients < 4:
    difficulty = "Easy"
elif cooking_time < 10 and number_of_ingredients >= 4:
    difficulty = "Medium"
elif cooking_time >= 10 and number_of_ingredients < 4:
    difficulty = "Intermediate"
else:
    difficulty = "Hard"
```

🧰 Prerequisites
Python 3 installed

MySQL Server running locally

mysql-connector-python installed

Install it using pip:
pip install mysql-connector-python

🚀 How to Run
1.Clone this repository or copy the script files.

2.Ensure your MySQL server is running with the correct credentials:

conn = mysql.connector.connect(
host="localhost",
user="cf-python",
password="password"
)
3.Run the script:
python recipe_app.py
Follow the interactive menu to:

Create new recipes

Search by ingredients

Update or delete recipes

View all recipes
📸 Example
Main Menu:

1. Create a new recipe
2. Search for a recipe by ingredient
3. Update an existing recipe
4. Delete a recipe
5. View all recipes
   Type 'quit' to exit the program.
   📁 Database Schema
   Table: Recipes

Column Type
id INT (PK, AI)
name VARCHAR(50)
ingredients VARCHAR(255)
cooking_time INT
difficulty VARCHAR(20)

🧑 Author
Padmaja – Full Stack Developer in training

Happy Cooking! 🍽️

---
