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
    user_choice = input('Enter Choice: ')
    if(user_choice == '1'):
        pass
    else:
        return None