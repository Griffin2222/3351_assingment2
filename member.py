# Importing time module for sleep function and custom clear_screen function from shared.py.
import time
from shared import clear_screen

# Initializing an empty list to store Member objects.
members = []

# Defining the Member class.
class Member():
    # Constructor to initialize a new member object.
    def __init__(self, name, address, phone, transactions=[]):
        self.name = name
        self.address = address
        self.phone = phone
        self.transactions = []  # Initializing an empty list to store transactions.

    # String representation for printing member details.
    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}'

    # Method to update member details.
    def update(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

# Function to display a message when no members are available.
def no_members():
    clear_screen()
    print('There are no members yet...')
    time.sleep(3)  # Pausing execution for 3 seconds.
    member_manage()  # Redirecting back to member management menu.

# Function to add a new member.
def add_member():
    duplicate = True
    while duplicate:
        clear_screen()
        print('Add Member')
        name = input('Enter name: ').capitalize()
        if name == '':
            continue
        elif(members):
            for member in members:
                if member.name == name:
                    clear_screen()
                    print(f'{name} is already in the system...')
                    time.sleep(2)
                    duplicate = True
                    break
                duplicate = False
        else:
            duplicate = False

    address = input('Enter address: ')
    phone = input('Enter phone number: ')
    members.append(Member(name, address, phone))  # Creating and appending a new Member object.
    member_manage()  # Redirecting back to member management menu.

# Function to display and select members.
def view_members():
    while True: # error handling
        clear_screen()
        print('Choose a member:')
        for m in range(0, len(members)):  # Looping through all members.
            print(f'{m + 1}. {members[m].name}')
        # Loop until a valid selection is made.
        try:
            user_input = int(input('Enter Choice: '))
            if user_input < len(members) + 1 and user_input > 0:
                return members[user_input - 1]  # Returning the selected member object.
        except ValueError:
            pass

# Function to display a selected member's details.
def member_details():
    member = view_members()  # Fetching the selected member.
    clear_screen()
    print('Member Details:')
    print(member)  # Printing member details.
    input('Enter any key to return...')  # Pause until user proceeds.
    member_manage()  # Redirecting back to member management menu.

# Function to update a member's details.
def update_member():
    member = view_members()  # Fetching the selected member.
    clear_screen()
    name = input('Enter name: ')
    address = input('Enter address: ')
    phone = input('Enter phone number: ')
    member.update(name, address, phone)  # Updating the member's details.
    member_manage()  # Redirecting back to member management menu.

# Function to remove a member.
def remove_member():
    members.remove(view_members())  # Removing the selected member.
    clear_screen()
    print('Member has been removed...')
    time.sleep(3)  # Pausing execution for 3 seconds.
    member_manage()  # Redirecting back to member management menu.

# Function to view purchase history of a member (commented out parts are placeholders for future code).
def purchase_history():
    sel_member = view_members()  # Fetching the selected member.
    clear_screen()
    if(not sel_member.transactions):
        print(f'{sel_member.name} has no transactions...')
        time.sleep(3)
        member_manage()
    else:
        print('Purchase History:')
        count = 1
        for purchase in sel_member.transactions:
            print(f'{count}: {purchase}')
            count += 1
        input('Enter any key to return: ')

# Main function for member management options.
def member_manage():
    clear_screen()
    # members.append(Member('Marcus', '123 Street', '41634234'))
    # members.append(Member('Gdf', '543 Street', '416314135'))
    print('Member Management:')
    print('1. Add Member')
    print('2. Update Member')
    print('3. View Member Details')
    print('4. Remove Member')
    print('5. View Purchase History')
    print('Any other key to return to the main menu')
    user_choice = input('Enter Choice: ')  # Getting user's choice.
    if user_choice == '1':
        add_member()
    elif user_choice == '2':
        if not members:  # Check if members list is empty.
            no_members()
        else:
            update_member()
    elif user_choice == '3':
        if not members:  # Check if members list is empty.
            no_members()
        else:
            member_details()
    elif user_choice == '4':
        if not members:  # Check if members list is empty.
            no_members()
        else:
            remove_member()
    elif user_choice == '5':
        if not members:  # Check if members list is empty.
            no_members()
        else:
            purchase_history()
