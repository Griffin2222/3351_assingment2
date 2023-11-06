from shared import clear_screen
import time

# lists for items and categories
items = []
categoies = []

# Defining invetory class
class Inventory:
    def __init__(self, name, category, stock, price):
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price
        
def add_item():
    duplicate = True
    while duplicate: # error handling
        clear_screen()
        print('Add Item: ')
        name = input('Enter item name: ').capitalize()
        # error handling for empty item name or duplicate item
        if name == '':
            continue
        elif(items): 
            for item in items:
                if item.name == name or f'{item.name}s' == name:
                    clear_screen()
                    print(f'{name} is already in the system...')
                    time.sleep(2)
                    duplicate = True
                    break
                duplicate = False
        else:
            duplicate = False

    # makes sure category name is not empty
    category = input('Enter item category: ').capitalize()
    while category == '':
        clear_screen()
        print('Add Item: ')
        category = input('Enter item category: ').capitalize()

    while True:
        clear_screen()
        print('Add Item: ')
        try: # error handling for bad input
            price = float(input("Enter item price: "))  # Taking new price as input.
            if(price > 0):
                break
        except ValueError:
            pass

    while True: # error handling
        clear_screen()
        print('Add Item: ')
        try: # error handling for bad input
            stock = int(input("Please enter item stock: "))  # Taking new stock quantity as input.
            if(stock > 0):
                break
        except ValueError:
            pass
    
    # new item is added to inventory
    items.append(Inventory(name, category, stock, price))
    clear_screen()
    print(f'{name} has been added to the inventory...')
    time.sleep(3)
    inventory_manage()

# remove an item from the inventory
def remove_item():
    if(not items): # error handling for no items in the system
        no_inventory()
    else:
        while True: # error handling for value entered to remove
            clear_screen()
            for i in range(0, len(items)):
                print(f'{i + 1}. {items[i].name}')
            try: # error handling for bad input
                item_num = int(input('Enter item number to remove: '))
                if item_num < len(items)+1 and item_num > 0:
                    break
            except ValueError:
                pass
        # remove item from inventory
        del items[item_num-1]
        clear_screen()
        print('Item has been removed...')
        time.sleep(2)
        inventory_manage()

# search for item in the inventory
def item_search():
    if(not items): # error handling
        no_inventory()
    else:
        clear_screen()
        item = input('Enter item to search for: ').lower()
        # checks for empty item name
        while item == '':
            clear_screen()
            item = input('Enter item to search for: ').lower()
        # checks if item is in the system
        not_found = True
        for i in range(0, len(items)):
            if item.lower() == items[i].name.lower():
                print(f'{items[i].name} is currently in the system...')
                time.sleep(2)
                not_found = False
                break
        if not_found:
            print(f'{item.capitalize()} has not been found...')
            time.sleep(3)
        
        # allows user to search again or return
        while True:
            clear_screen()
            search_again = input('Enter 1 to search again or 2 to return to inventory management: ')
            if search_again == '1' or search_again == '2':
                break
        if search_again == '1':
            item_search()
        elif search_again == '2': 
            inventory_manage()
    
# print the categories stored in the system
def category_list():
    global items
    if(not items):
        no_categories()
    else:
        categories = []
        clear_screen()
        print(f'Category List:')
        count = 1
        for item in items:
            if item.category not in categories:
                categories.append(item.category)
                print(f'{count}. {item.category}')
                count += 1
        input('Enter any key to return to inventory management...')
        inventory_manage()

# prints transaction management menu options
def inventory_manage():
    clear_screen()
    print('Inventory Management:')
    print('1. Add Item')
    print('2. Remove Item')
    print('3: Item Search')
    print('4: Category List')
    print('Any other key to return to the main menu')
    user_choice = input('Enter Choice: ')
    if(user_choice == '1'):
        add_item()
    elif(user_choice == '2'):
        remove_item()
    elif(user_choice == '3'):
        item_search()
    elif(user_choice == '4'):
        category_list()

# no items in the system
def no_inventory():
    clear_screen()
    print('There are no items yet...')
    time.sleep(3)  # Pausing execution for 3 seconds.
    inventory_manage()  # Redirecting back to member management menu.

# no categories in the system
def no_categories():
    clear_screen()
    print('There are no categories yet...')
    time.sleep(3)
    inventory_manage() # Redirecting back to member management menu.