import time, os

members = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# member class
class Member():
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}'

def add_member():
    clear_screen()
    name = input('Enter name: ')
    address = input('Enter address: ')
    phone = input('Enter phone number: ')
    members.append(Member(name, address, phone))
    member_manage()

def remove_member():
    clear_screen()
    print('Select a member to remove:')
    for m in range(0, len(members)):
        print(f'{m + 1}. {members[m].name}')
    member_number = int(input('please enter the number corresponding to the member:'))
    members.pop(member_number-1)
    clear_screen()
    print('Member has been removed')
    time.sleep(3)
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
    input('Press any key to return...')
    member_manage()

def update_member():
    clear_screen()
    print('Select a member to update:')
    for m in range(0, len(members)):
        print(f'{m + 1}. {members[m].name}')
    member_number = int(input('please enter the number corresponding to the member:'))
    new_name = input('Enter New Name:')
    new_address = input('Enter new Address:')
    new_phonenum = input('Enter new Phone Number:')
    members[member_number-1] = Member(new_name,new_address,new_phonenum)
    print('Member info has been updated...')
    time.sleep(3)
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
    elif(user_choice == '3'):
        if not members:
            clear_screen()
            print('There are no members yet!')
            time.sleep(3)
            member_manage()
        else:
            view_members()
    elif(user_choice == '2'):
        if not members:
            clear_screen()
            print('No members to update')
            time.sleep(3)
            member_manage()
        else:
            update_member()
    elif(user_choice == '4'):
        if not members:
            clear_screen()
            print('There are no members to remove.')
            time.sleep(3)
            member_manage()
        else:
            remove_member()
    elif(user_choice == '5'):
        return None
