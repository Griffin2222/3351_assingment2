from shared import clear_screen
import time


items = []
class Inventory:
    def __init__(self, name, category, stock, price):
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price
        

def add_item():
    clear_screen()
    print('Add Item: ')
    name = input('Enter item name: ')
    category = input('Enter item category: ')
    items.append(Inventory(name, category, 0, 0))
    print(f'item {name} has been added...')
    time.sleep(3)
    inventory_manage()

def remove_item():
    clear_screen()
    for i in range(0, len(items)):
        print(f'{i + 1}. {items[i].name}')
    item_num = int(input('Enter item number to remove: '))  
    while item_num > len(items)+1:
        item_num = int(input('Enter item number to remove: '))
    del items[item_num-1]
    print('item has been removed...')
    time.sleep(2)
    inventory_manage()

def item_search():
    clear_screen()
    item = input('Enter item to search for: ').lower()
    for i in range(0, len(items)):
        ticker = False
        if item.lower() == items[i].name.lower():
            print(f'Item {items[i].name} is currently in the system...')
            time.sleep(2)
            ticker = True
    if ticker == False:
        print('item has not been found')
        time.sleep(2)
    search_again = int(input('enter 1 to search again or 2 to return to inventory management: '))
    while search_again != 1 and search_again != 2:
            search_again = int(input('enter 1 to search again or 2 to return to inventory management: '))
    if search_again == 1:
        item_search()
    elif search_again == 2:          
        inventory_manage()
    
       


def category_list():
    global items
    categories = {}
    for item in items:
        category = item.category
        if category not in categories:
            categories[category] = []
        categories[category].append(item)
    clear_screen()
    for category, items in categories.items():
        print(f"Category: {category}")
        for item in items:
            print(f"- {item.name}")
    input("press any button to return to inventory management...")
    inventory_manage()

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