from shared import clear_screen
import time

class Inventory:
    def __init__(self):
        pass

def add_item():
    clear_screen()
    print('Add Item')
    name = input('Item Name: ')
    category = input('Item Category: ')
    inventory_manage()

def remove_item():
    clear_screen()
    item = input('Enter item to remove: ').lower()
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