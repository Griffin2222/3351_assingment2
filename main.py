"""Retail Store Management System"""
import sys, os, member;



members = []
members.append(member.Member('Marcus', '123 street', '1234567890'))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_member():
    clear_screen()
    name = input('Enter name: ')
    address = input('Enter address: ')
    phone = input('Enter phone number: ')
    members.append(member.Member(name, address, phone))
    member_manage()

def view_members():
    clear_screen()
    print('Members List:')
    for m in range(0, len(members)):
        print(f'{m + 1}. {members[m].name}')
    while True:
        user_input = int(input('Enter Choice: '))
        if user_input < len(members) + 1 and user_input > 0:
            break
    clear_screen()
    print('Member Details:')
    print(members[user_input - 1])

def member_manage():
    clear_screen()
    print('Member Management:')
    print('1. Add Member')
    print('2. Update Member')
    print('3. View Member Details')
    print('4. Remove Member')
    print('5. Main Menu')
    user_choice = input('Enter Choice: ')
    if(user_choice == '1'):
        add_member()
    elif(user_choice == '3'):
        view_members()
    elif(user_choice == '5'):
        welcomePage()


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
        member_manage()
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



