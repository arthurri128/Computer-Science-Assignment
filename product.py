# Product class
class Product:
    #Attributes that store the product information
    def __init__(self, name, sku, price, quantity):
        self.name = name        # Name of the product
        self.sku = sku          # Identifier of product
        self.price = price      # Price of product
        self.quantity = quantity # Current level of stock

    # Method that updates the quantity, including validation
    def update_quantity(self, amount):
        # This prevents a possible negative quantity being inputted
        if self.quantity + amount >= 0:
            self.quantity += amount
        else:
            print("Quantity cannot be negative, please choose a positive value")

    # Displays All Product Details
    def display(self):
        print(f"Product Name: {self.name}, SKU: {self.sku}, Price: ${self.price}, Quantity: {self.quantity}")