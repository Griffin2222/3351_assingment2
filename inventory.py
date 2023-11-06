from shared import clear_screen
import time

items = []
categoies = []

class Inventory:
    def __init__(self, name, category, stock, price):
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price
        
def add_item():
    while True: # error handling
        duplicate = True
        while duplicate:
            clear_screen()
            print('Add Item: ')
            name = input('Enter item name: ').capitalize()
            if(items):
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

        category = input('Enter item category: ').capitalize()
        try: # error handling
            price = float(input("Enter item price: "))  # Taking new price as input.
            if(price > 0):
                break
        except ValueError:
            pass

    while True: # error handling
        clear_screen()
        print('Add Item: ')
        try: # error handling
            stock = int(input("Please enter item stock: "))  # Taking new stock quantity as input.
            if(stock > 0):
                break
        except ValueError:
            pass
    
    items.append(Inventory(name, category, stock, price))
    
    clear_screen()
    print(f'{name} has been added to the inventory...')
    time.sleep(3)
    inventory_manage()

def remove_item():
    if(not items): # error handling
        no_inventory()
    else:
        clear_screen()
        for i in range(0, len(items)):
            print(f'{i + 1}. {items[i].name}')
        item_num = int(input('Enter item number to remove: '))  
        while item_num > len(items)+1 or item_num <= 0:
            item_num = int(input('Enter item number to remove: '))
        del items[item_num-1]
        clear_screen()
        print('Item has been removed...')
        time.sleep(2)
        inventory_manage()

def item_search():
    if(not items): # error handling
        no_inventory()
    else:
        clear_screen()
        item = input('Enter item to search for: ').lower()
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
        
        while True:
            clear_screen()
            search_again = input('Enter 1 to search again or 2 to return to inventory management: ')
            if search_again == '1' or search_again == '2':
                break
        if search_again == '1':
            item_search()
        elif search_again == '2': 
            inventory_manage()
    
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

def inventory_manage():
    clear_screen()
    # items.append(Inventory('Apple', 'Fruit', 1, 4))
    # items.append(Inventory('Orange', 'Fruit', 1, 5))
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

def no_inventory():
    clear_screen()
    print('There are no items yet...')
    time.sleep(3)  # Pausing execution for 3 seconds.
    inventory_manage()  # Redirecting back to member management menu.

def no_categories():
    clear_screen()
    print('There are no categories yet...')
    time.sleep(3)
    inventory_manage() # Redirecting back to member management menu.