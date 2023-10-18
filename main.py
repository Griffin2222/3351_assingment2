# Make sure to work within your own branch and merge after pulling from main to prevent merge conflicts

"""Retail Store Management System"""  # Brief description of what the script does.

# Importing necessary modules and functions.
import sys  # For system functions like exiting the application.
import member, item, inventory, transaction  # Custom modules for different aspects of the retail management.
from shared import clear_screen  # Custom function to clear the console screen.

# Function to display the welcome page and navigation options.
def welcomePage():
    clear_screen()  # Clearing the console for better readability.
    
    # Displaying welcome message and options.
    print('Welcome to the Retail Store Management Program!')
    print('1. Member Management')
    print('2. Item Management')
    print('3. Inventory Viewing')
    print('4. Transaction Processing')
    print('Any other key to exit')
    
    # Taking user's choice for navigation.
    user_choice = input('Enter Choice: ')
    
    # Navigation based on user's choice.
    if user_choice == '1':  # Member Management
        member.member_manage()  # Call to function handling member management.
        welcomePage()  # Return to the welcome page after completion.
        
    elif user_choice == '2':  # Item Management
        item.item_manage()  # Call to function handling item management.
        welcomePage()  # Return to the welcome page after completion.
        
    elif user_choice == '3':  # Inventory Viewing
        inventory.inventory_manage()  # Call to function handling inventory management.
        welcomePage()  # Return to the welcome page after completion.
        
    elif user_choice == '4':  # Transaction Processing
        transaction.transaction_manage()  # Call to function handling transaction management.
        welcomePage()  # Return to the welcome page after completion.
        
    else:  # Any other key to exit the application.
        clear_screen()  # Clear the console.
        
        # Displaying the exit message.
        print('Goodbye! Thank you for using our Retail Store Management Program!')
        sys.exit()  # Exit the application.

# Initial call to welcomePage function to kickstart the application.
welcomePage()
