from shared import clear_screen
import time, member, inventory
from item import Item
from inventory import Inventory, items

# initializing list for cart
cart = []

# Defining transaction class
class Transaction:
    def __init(self, member, cost, items=[]):
        self.member = member
        self.cost = cost
        self.items = items

# adds an item to the member's cart
def add_item(trans_member):
    clear_screen()
    # checks if all items are out of stock or there are no items in the system
    if(all(getattr(item, 'stock') == 0 for item in items)):
        if(cart):
            print('The store is out of stock...')
            time.sleep(3)
            transaction_manage(trans_member)
        else:
            no_items()
    else:
        # prints items in the store and allows user to select one to add to cart
        while True: # error handling for bad input
            clear_screen()
            print("Items: ")
            for i in range(0, len(items)):
                print(f'{i + 1}. {items[i].name}, Stock: {items[i].stock}, Price: ${items[i].price:.2f}')
            try: # bad input handling
                item_to_add = int(input("Please select the number of the item you would like: "))
                if(item_to_add <= len(items) and item_to_add > 0):
                    clear_screen()
                    if(items[item_to_add-1].stock == 0):
                        print('This item is out of stock...')
                    else:
                        # adds item to cart and reduces stock in store
                        cart.append(items[item_to_add-1])
                        items[item_to_add-1].stock -= 1
                        print(f"{items[item_to_add-1].name} has been added to your cart...")
                    break
            except:
                pass

        # allows user to add another item or return
        while True:
            search_again = input('Enter 1 to add another item or 2 to return to transaction processing: ')
            clear_screen()
            if search_again == '1' or search_again == '2':
                break
        if search_again == '1':
            add_item(trans_member)
        elif search_again == '2':
            transaction_manage(trans_member)

# removes an item from the member's cart
def remove_item(trans_member):
    clear_screen()
    # checks if there are no items in the cart
    if(not cart):
        no_cart(trans_member)
    else:
        while True: # error handling
            # prints items in the cart
            print('Items in cart: ')
            for i in range(0, len(cart)):
                print(f'{i+1}. {cart[i].name}, Price: ${cart[i].price:.2f}')
            try: # error handling bad input
                item_to_remove = int(input('Please enter the number of the item to remove: '))
                if(item_to_remove <= len(cart) and item_to_remove > 0):
                    clear_screen()
                    print(f'{cart[item_to_remove-1].name} has been removed for your cart...')
                    # removes item from cart and increases stock
                    cart[item_to_remove-1].stock += 1
                    del cart[item_to_remove-1]
                    break
            except ValueError:
                pass
        
        # allows user to remove another item or return
        while True:
            search_again = input('Enter 1 to remove another item or 2 to return to transaction processing: ')
            clear_screen()
            if search_again == '1' or search_again == '2':
                break
        if search_again == '1':
            remove_item(trans_member)
        else:
            transaction_manage(trans_member)

# calculates total cost of member's cart
def calculate_total(trans_member):
    if(not cart): # no items in cart
        no_cart(trans_member)
    else:
        clear_screen()
        cost = 0
        # prints items in cart and total
        print('Your Cart:')
        for i in range(0, len(cart)):
            print(f"{i+1}. {cart[i].name}, Price: ${cart[i].price:.2f}" )
            cost += float(cart[i].price)
        print(f"Your total cost is: ${cost:.2f}")
        # allows user to confirm purchase
        user_input = input('Enter yes to confirm or any other key to return: ').lower()
        if(user_input == 'yes'):
            clear_screen()
            purchased_items = ', '.join(item.name for item in cart)
            # adds transaction to the member to be viewed in transaction history
            trans_member.transactions.append(f'Items: {purchased_items}, Total: ${round(cost, 2):.2f}')
            cart.clear()
            print('Thank you for shopping!')
            time.sleep(3)
        else:
            transaction_manage(trans_member)

# selects member for transaction
def sel_trans_member():
    if(not items): # no items in system
        no_items()
    elif(all(getattr(item, 'stock') == 0 for item in items)): # all items out of stock
        clear_screen()
        print('The store is out of stock...')
        time.sleep(3)
    elif(not member.members): # no members in system
        member.no_members()
    else:
        trans_member = member.view_members()
        transaction_manage(trans_member)

# transaction options select for specific member
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
    else: # if member exits then cart is cleared and items are restocked
        for item in items:
            for cart_item in cart:
                if cart_item.name == item.name:
                    item.stock += 1
        cart.clear()

# no items in the system
def no_items():
    clear_screen()
    print('There are no items in the system...')
    time.sleep(3)
    inventory.inventory_manage()

# no items in the carts
def no_cart(trans_member):
    clear_screen()
    print('There are no items in the cart...')
    time.sleep(3)
    transaction_manage(trans_member)