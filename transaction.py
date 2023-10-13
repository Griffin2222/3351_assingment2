from shared import clear_screen
import time
from member import Member
from item import Item
from inventory import Inventory, items

cart =  []
class Transaction:
    def __init(self, member, cost, items):
        self.member = member
        self.cost = cost
        self.items = items


def add_item():
    clear_screen()
    print("items:")
    for i in range(0, len(items)):
        print(f'{i + 1}. {items[i].name}, Price: {items[i].price}')
    item_to_add = int(input("Please select the number of the item you would like: "))
    cart.append(items[item_to_add-1])
    print(f"Item {items[item_to_add-1].name} has been added to your cart")
    time.sleep(3)
    transaction_manage()

def remove_item():
    clear_screen()
    print("cart: ")
    for i in range(0, len(cart)):
        print(f"{i+1}. {cart[i].name}, Price: {cart[i].price}" )
    item_to_remove = int(input("Please enter the number of the item to remove: "))
    del cart[item_to_remove-1]
    print("item has been removed")
    time.sleep(3)
    transaction_manage()

def calculate_total():
    cost = 0
    for i in range(0, len(cart)):
        print(f"{i+1}. {cart[i].name}, Price: {cart[i].price}" )
        cost += int(cart[i].price)
    print(f"your total cost is: {cost}")
    input("Press any button to return to transaction manage page: ")

    transaction_manage()

def transaction_manage():
    clear_screen()
    print('Transaction Processing:')
    print('1. Add An Item')
    print('2. Remove An Item')
    print('3. Calculate Total')
    print('Any other key to return to the main menu')
    user_choice = input('Enter Choice: ')
    if(user_choice == '1'):
        add_item()
    elif(user_choice == '2'):
        remove_item()
    elif(user_choice == '3'):
        calculate_total()