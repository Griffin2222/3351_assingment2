import time
from shared import clear_screen

members = []

# member class
class Member():
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}'
    
    def update(self, new_name, new_address, new_phone):
        self.name = new_name
        self.address = new_address
        self.phone = new_phone


def add_member():
    clear_screen()
    name = input('Enter name: ')
    address = input('Enter address: ')
    phone = input('Enter phone number: ')
    members.append(Member(name, address, phone))
    member_manage()

def view_members():
    clear_screen()
    print('Members List:')
    for m in range(0, len(members)):
        print(f'{m + 1}. {members[m].name}')
    while True:
        user_input = int(input('Enter Choice: '))
        if user_input < len(members) + 1 and user_input > 0:
            return members[user_input - 1]

def member_details():
    member = view_members()
    clear_screen()
    print('Member Details:')
    print(member)
    input('Press any key to return...')
    member_manage()

def update_member():
    clear_screen()
    member = view_members()
    name = input('Enter name: ')
    address = input('Enter address: ')
    phone = input('Enter phone number: ')
    member.update(name, address, phone)
    member_manage()

def remove_member():
    clear_screen()
    members.remove(view_members())
    member_manage()

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
    elif(user_choice == '2'):
        if not members:
            clear_screen()
            print('There are no members yet!')
            time.sleep(3)
            member_manage()
        else:
            update_member()
    elif(user_choice == '3'):
        if not members:
            clear_screen()
            print('There are no members yet!')
            time.sleep(3)
            member_manage()
        else:
            member_details()
    
    elif(user_choice == '4'):
        if not members:
            clear_screen()
            print('There are no members to remove.')
            time.sleep(3)
            member_manage()
        else:
            remove_member()
