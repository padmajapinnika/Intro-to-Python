class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)

    def view_list(self):
        if self.shopping_list:
            print(f"{self.list_name}:")
            for item in self.shopping_list:
                print(f"- {item}")
        else:
            print("Your shopping list is empty.")

    def merge_lists(self, obj):
        # Creating a name for our new, merged shopping list
        merged_lists_name = 'Merged List - ' + self.list_name + " + " + obj.list_name

        # Creating a new ShoppingList object
        merged_lists_obj = ShoppingList(merged_lists_name)

        # Add items from the first list
        merged_lists_obj.shopping_list = self.shopping_list.copy()

        # Add unique items from the second list
        for item in obj.shopping_list:
            if item not in merged_lists_obj.shopping_list:
                merged_lists_obj.shopping_list.append(item)

        return merged_lists_obj


# Create shopping lists
pet_store_list = ShoppingList("Pet Store Shopping List")
grocery_store_list = ShoppingList("Grocery Store List")

# Add items to pet store list
for item in ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']:
    pet_store_list.add_item(item)

# Add items to grocery store list
for item in ['fruits', 'vegetables', 'bowl', 'ice cream']:
    grocery_store_list.add_item(item)

# Merge the two lists and store in a new object
merged_list = pet_store_list.merge_lists(grocery_store_list)

# Update pet store list
pet_store_list.remove_item("flea collars")
pet_store_list.add_item("frisbee")  # Will not be added again if it already exists

# View both lists
print("\nPet Store List:")
pet_store_list.view_list()

print("\nMerged List:")
merged_list.view_list()
