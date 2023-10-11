from shared import clear_screen

class Item:
    def __init__(self, stock, price):
        self.stock = stock
        self.price = price
    
    def update(self, stock, price):
        self.stock = stock
        self.price = price

def item_manage():
    clear_screen()
    print('Item Management:')
    print('1. Update Item')
    print('Any other key to return to the main menu')
    user_choice = input('Enter Choice: ')
    if(user_choice == '1. Update Item'):
        pass