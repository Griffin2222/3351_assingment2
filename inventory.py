from shared import clear_screen
import time

items = []
class Inventory:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        

def add_item():
    clear_screen()
    print('Add Item:')
    name = input('Enter item name:')
    category = input('Enter item category:')
    items.append(Inventory(name, category))
    print(f'item {name} has been added...')
    time.sleep(3)
    inventory_manage()

def remove_item():
    clear_screen()
    for i in range(0, len(items)):
        print(f'{i + 1}. {items[i].name}')
    item_num = int(input('Enter item number to remove: '))
    if item_num < len(items)+1:
        del items[item_num-1]
    else:
        while item_num > len(items)+1:
            item_num = int(input('Enter valid item number to remove: '))
    print('item has been removed...')
    time.sleep(2)
    inventory_manage()

def item_search():
    clear_screen()
    item = input('Enter item to search for: ')

    inventory_manage()

def category_list():
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