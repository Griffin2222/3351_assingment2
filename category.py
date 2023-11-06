from inventory import categories

class Category:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = []

def add_category(name, item):
    new_category = Category(name)
    new_category.items.append(item)
    categories.append(new_category)

def remove_category(name):
    for catagory in categories:
        if catagory.name == name:
            categories.remove(catagory)