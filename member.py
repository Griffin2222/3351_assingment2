# member class

class Member():
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}'

    
def add_member(self, name, address, phone):
    self.name = input('Enter name: ')
    self.address = input('Enter address: ')
    self.phone = input('Enter phone number: ')
