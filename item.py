from shared import clear_screen  # Importing the clear_screen function to clear the console.
from inventory import Inventory, items  # Importing Inventory class and items list from another module.
import time

# Class definition for Item objects.
class Item:
    # Constructor for initializing new Item objects.
    def __init__(self, name, stock, price):
        self.stock = stock  # Stock quantity of the item.
        self.price = price  # Price of the item.
        Inventory.name = name  # Assigning the name to the Inventory's name attribute. 

    # Method to update stock and price of an item.
    def update(self, stock, price):
        self.stock = stock  # Updating the stock quantity.
        self.price = price  # Updating the price.

# Function to manage items.
def item_manage():
    if(not items):
        no_items()
    else:
        clear_screen()  # Clearing the console screen.
        print('Item Management:')
        print('1. Update Item')
        print('2. View Stocks and Prices')
        print('Any other key to return to the main menu')
        
        # Taking the user's choice as input.
        user_choice = input('Enter Choice: ')  
        
        # Redirecting based on user's choice.
        if user_choice == '1':
            update_item()
        elif user_choice == '2':
            view_stock()

# Function to update an existing item.
def update_item():
    while True: # error handling
        clear_screen()
        print("Items: ")
    
    # Displaying all items for the user to choose from.
        for i in range(0, len(items)):
            print(f'{i + 1}. {items[i].name}')
    
    # Taking the user's choice as input.
        try: # error handling
            selection = int(input('Select a item to update: '))
            if selection < len(items) + 1 and selection > 0:
                break
        except ValueError:
            pass
    
    # Prompting user for new values
    while True: # error handling
        clear_screen()
        print(f"Please change the values for {items[selection-1].name}")  
        try: # error handling
            price = float(input("Enter the new price: "))  # Taking new price as input.
            if(price > 0):
                break
        except ValueError:
            pass

    while True: # error handling
        clear_screen()
        print(f"Enter new values for {items[selection-1].name}:")  
        try: # error handling
            stock = int(input("Please enter new stock quantity: "))  # Taking new stock quantity as input.
            if(stock > 0):
                break
        except ValueError:
            pass

    category = input('Please enter the new category name: ').capitalize()
    
    # Updating the item based on user's input.
    items[selection-1].price = price  
    items[selection-1].stock = stock  
    items[selection-1].category = category
    item_manage()  # Redirecting back to item management menu.

# Function to view stock and price of all items.
def view_stock():
    clear_screen()
    print("Items: ")
    if(not items): # error handling
        no_items()
    # Looping through all items to display their details.
    else:
        for i in range(0, len(items)):
            print(f'{i + 1}. {items[i].name}, Stock: {items[i].stock}, Price: ${items[i].price:.2f}')
        
        # Waiting for the user's keypress to proceed.
        input('Enter any key to return to item management...')  
        item_manage()  # Redirecting back to item management menu.

def no_items():
    clear_screen()
    print('There are no items in the system...')
    time.sleep(3)  # Pausing execution for 3 seconds.
    # Redirecting back to main menu.