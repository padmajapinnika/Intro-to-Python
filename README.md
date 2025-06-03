Recipe App Data Structures
Overview
This repository contains the implementation of basic data structures to store recipe information for a Recipe app. Each recipe includes attributes such as name, cooking time, and ingredients. Multiple recipes are stored sequentially to allow easy management and expansion.

Data Structure Choices
For storing individual recipe information, I chose a dictionary because it allows clear association of keys (name, cooking_time, ingredients) to their respective values. Dictionaries provide flexibility for modifying, adding, or removing attributes in the future, which is important as the app grows.

To store multiple recipes in an ordered fashion, I used a list named all_recipes. Lists preserve the order of insertion and allow easy addition, removal, or iteration through recipes. This sequential structure is ideal for handling collections of items like recipes, which may be accessed or updated frequently.

Summary
Individual Recipe: Dictionary — allows key-value pairing and flexibility.

Collection of Recipes: List — maintains order and supports dynamic modification.

This design balances readability, usability, and scalability for future app development.
