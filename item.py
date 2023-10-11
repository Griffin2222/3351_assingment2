class Item:
    def __init__(self, stock, price):
        self.stock = stock
        self.price = price
    
    def update(self, stock, price):
        self.stock = stock
        self.price = price