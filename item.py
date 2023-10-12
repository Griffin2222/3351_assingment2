from shared import clear_screen
from inventory import Inventory, items



class Item:
    def __init__(self,name, stock, price):
        self.stock = stock
        self.price = price
        Inventory.name = name
    
    def update(self, stock, price):
        self.stock = stock
        self.price = price

def item_manage():
    clear_screen()
    print('Item Management:')
    print('1. Update Item')
    print('2. View Stocks and Prices')
    print('Any other key to return to the main menu')
    user_choice = input('Enter Choice: ')
    if(user_choice == '1'):
        update_item()
    elif(user_choice == '2'):
        view_stock()


def update_item():
    print("items:")
    for i in range(0, len(items)):
        print(f'{i + 1}. {items[i].name}')
    selection = int(input('select a item to update...'))
    print(f"Please change the values for {items[selection-1].name}")
    price = input("Enter the new price: ")
    stock = input("Please enter new stock quantity: ")
    items[selection-1].price = price
    items[selection-1].stock = stock
    item_manage()


def view_stock():
    print("items")
    for i in range(0, len(items)):
        print(f'{i + 1}. {items[i].name}, Stock: {items[i].stock}, Price: ${items[i].price}')
    input('Press any key to return to item management...')
    item_manage()
