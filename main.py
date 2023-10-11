#Make sure to work within your own branch and merge after pulling from main to prevent merge conflicts

"""Retail Store Management System"""
import sys, member
from shared import clear_screen

# members.append(member.Member('Marcus', '123 street', '1234567890'))

def welcomePage():
    clear_screen()
    print('Welcome to the Retail Store Management Program!')
    print('1. Member Management')
    print('2. Item Management')
    print('3. Inventory Viewing')
    print('4. Transaction Processing')
    print('5. Exit')
    user_choice = input('Enter Choice: ')

    if(user_choice == '1'):
        member.member_manage()
        welcomePage()
    elif(user_choice == '2'):
        pass
    elif(user_choice == '3'):
        pass
    elif(user_choice == '4'):
        pass
    elif(user_choice == '5'):
        clear_screen()
        print('Goodbye! Thank you for using our Retail Store Management Program!')
        sys.exit()

welcomePage()