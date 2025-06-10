# Recipe Manager App

A command-line application built with Python and SQLAlchemy to manage recipes in a MySQL database. Users can create, view, search, update, and delete recipes.

## 📦 Features

- Add new recipes with cooking time and ingredients
- Automatically calculates recipe difficulty
- View all recipes
- Search recipes by ingredients
- Edit existing recipes (name, ingredients, cooking time)
- Delete recipes from the database

## 🛠️ Tech Stack

- Python 3.x
- SQLAlchemy (ORM)
- MySQL
- PyMySQL

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/padmajapinnika/recipe-manager.git
cd recipe-manager
```

### 2. Create and Activate a Virtual Environment

python -m venv venv

# Windows:

venv\Scripts\activate

# macOS/Linux:

source venv/bin/activate

### 3. Install Dependencies

pip install sqlalchemy pymysql

### 4. Set Up the MySQL Database

CREATE DATABASE task_database;
The app will automatically create a table named final_recipes on the first run.

### 5. Run the Application

python recipe_app.py

### 🧪 Example Recipes to Try

## Chickpea Curry

Cooking Time: 35
Ingredients: Chickpeas, Onion, Tomato, Garlic, Garam masala, Salt

## Masala Dosa

Cooking Time: 25
Ingredients: Rice, Urad dal, Potato, Mustard seeds, Curry leaves, Salt

## Paneer Butter Masala

Cooking Time: 30
Ingredients: Paneer, Tomato, Butter, Cream, Garam masala, Onion

### 📝 License

This project is for educational purposes only.
