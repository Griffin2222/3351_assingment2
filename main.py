import sys;

# Retail Store Management System
print('Welcome to the Retail Store Management Program!')
print('1. Member Management')
print('2. Item Management')
print('3. Inventory Viewing')
print('4. Transaction Processing')
print('5. Exit')

user_choice = input('Enter choice: ')

if(user_choice == '5'):
    print('Goodbye!')
    sys.exit()