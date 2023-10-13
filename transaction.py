from shared import clear_screen

class Transaction:
    def __init(self, member, cost, items=None):
        self.member = member
        self.cost = cost
        items = []

def add_item():
    transaction_manage()

def remove_item():
    transaction_manage()

def calculate_total():
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
    