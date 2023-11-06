from inventory import categories

# Defining category class
class Category:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = []

def add_category(name, item): # adds a new category and appends the new item
    new_category = Category(name)
    new_category.items.append(item)
    categories.append(new_category)

def remove_category(name):  # removes a category
    for catagory in categories:
        if catagory.name == name:
            categories.remove(catagory)