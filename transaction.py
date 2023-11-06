from shared import clear_screen
import time, member
from item import Item
from inventory import Inventory, items

cart =  []
out_stock = []
class Transaction:
    def __init(self, member, cost, items=[]):
        self.member = member
        self.cost = cost
        self.items = items

def add_item(trans_member):
    clear_screen()
    if(all(getattr(item, 'stock')== 0 for item in items)):
        if(cart):
            print('The store is out of stock...')
            time.sleep(3)
            transaction_manage(trans_member)
        else:
            no_items()
    else:
        while True:
            clear_screen()
            print("Items: ")
            for i in range(0, len(items)):
                print(f'{i + 1}. {items[i].name}, Stock: {items[i].stock}, Price: ${items[i].price:.2f}')
            try:
                item_to_add = int(input("Please select the number of the item you would like: "))

                if(item_to_add <= len(items) and item_to_add > 0):
                    clear_screen()
                    if(items[item_to_add-1].stock == 0):
                        print('This item is out of stock...')
                    else:
                        cart.append(items[item_to_add-1])
                        items[item_to_add-1].stock -= 1
                        print(f"{items[item_to_add-1].name} has been added to your cart...")
                    break
            except:
                pass

        while True:
            search_again = input('Enter 1 to add another item or 2 to return to transaction processing: ')
            clear_screen()
            if search_again == '1' or search_again == '2':
                break
        if search_again == '1':
            add_item(trans_member)
        elif search_again == '2':
            transaction_manage(trans_member)

def remove_item(trans_member):
    clear_screen()
    if(not cart):
        no_cart(trans_member)
    else:
        while True:
            print('Items in cart: ')
            for i in range(0, len(cart)):
                if(cart[i].stock == 0):
                    pass
                print(f'{i+1}. {cart[i].name}, Price: ${cart[i].price:.2f}')
            try:
                item_to_remove = int(input('Please enter the number of the item to remove: '))
                if(item_to_remove <= len(cart) and item_to_remove > 0):
                    clear_screen()
                    print(f'{cart[item_to_remove-1].name} has been removed for your cart...')
                    cart[item_to_remove-1].stock += 1
                    del cart[item_to_remove-1]
                    break
            except ValueError:
                pass

        while True:
            search_again = input('Enter 1 to remove another item or 2 to return to transaction processing: ')
            clear_screen()
            if search_again == '1' or search_again == '2':
                break
        if search_again == '1':
            remove_item(trans_member)
        else:
            transaction_manage(trans_member)

def calculate_total(trans_member):
    if(not cart):
        no_cart(trans_member)
    else:
        clear_screen()
        cost = 0
        print('Your Cart:')
        for i in range(0, len(cart)):
            print(f"{i+1}. {cart[i].name}, Price: ${cart[i].price:.2f}" )
            cost += float(cart[i].price)
        print(f"Your total cost is: ${cost:.2f}")
        user_input = input('Enter yes to confirm or any other key to return: ').lower()
        if(user_input == 'yes'):
            clear_screen()
            purchased_items = ', '.join(item.name for item in cart)
            trans_member.transactions.append(f'Items: {purchased_items}, Total: ${round(cost, 2)}')
            cart.clear()
            print('Thank you for shopping!')
            time.sleep(3)
        else:
            transaction_manage(trans_member)

def sel_trans_member():
    if(not items):
        no_items()
    elif(all(getattr(item, 'stock')== 0 for item in items)):
        clear_screen()
        print('The store is out of stock...')
        time.sleep(3)
    elif(not member.members):
        member.no_members()
    else:
        trans_member = member.view_members()
        transaction_manage(trans_member)

def transaction_manage(trans_member):
    clear_screen()
    print('Transaction Processing:')
    print('1. Add An Item')
    print('2. Remove An Item')
    print('3. Checkout')
    print('Any other key to return to the main menu')
    user_choice = input('Enter Choice: ')
    if(user_choice == '1'):
        add_item(trans_member)
    elif(user_choice == '2'):
        remove_item(trans_member)
    elif(user_choice == '3'):
        calculate_total(trans_member)
    else:
        for item in items:
            for cart_item in cart:
                if cart_item.name == item.name:
                    item.stock += 1
        cart.clear()


def no_items():
    clear_screen()
    print('There are no items in the system...')
    time.sleep(3)

def no_cart(trans_member):
    clear_screen()
    print('There are no items in the cart...')
    time.sleep(3)
    transaction_manage(trans_member)