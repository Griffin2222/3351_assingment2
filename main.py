#Make sure to work within your own branch and merge after pulling from main to prevent merge conflicts

"""Retail Store Management System"""
import sys, member, item, inventory, transaction
from shared import clear_screen

# members.append(member.Member('Marcus', '123 street', '1234567890'))

def welcomePage():
    clear_screen()
    print('Welcome to the Retail Store Management Program!')
    print('1. Member Management')
    print('2. Item Management')
    print('3. Inventory Viewing')
    print('4. Transaction Processing')
    print('Any other key to exit')
    user_choice = input('Enter Choice: ')

    if(user_choice == '1'):
        member.member_manage()
        welcomePage()
    elif(user_choice == '2'):
        item.item_manage()
        welcomePage()
    elif(user_choice == '3'):
        inventory.inventory_manage()
        welcomePage()
    elif(user_choice == '4'):
        transaction.transaction_manage()
        welcomePage()
    else:
        clear_screen()
        print('Goodbye! Thank you for using our Retail Store Management Program!')
        sys.exit()

welcomePage()