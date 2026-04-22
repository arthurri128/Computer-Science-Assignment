# Location Class
class Location:
    def __init__(self, row, col, capacity):
        # The position of within the 2D grid
        self.row = row
        self. col = col

        # Max allotted capcity given by User
        self.capacity = capacity

        # Initial list of product/s being stored
        self.products = []

    # Adds the product into the given location and validation ensuring there is enough capactiy
    def add_product(self, product):
        if len(self.products) < self.capacity:
            self.products.append(product)
            print("Product has been added")
        else: 
            print("Location Full")

    # Removes a product via it's unique identifer (SKU)
    def remove_product(self, sku): 
        # Loops through all products to attempt to find a match
        for product in self.products:
            if product.sku == sku:
                self.products.remove(product)
                print("Product has been removed")
                return
        print("Product could not be found")

    # Searches for wether Product is in location
    def find_product(self, sku):
        for product in self.products:
            if product.sku == sku:
                return product # Shows product if it has been found in the location
        return None # Shows if product could not be found in lcoation
    
    # Displays all the products and product details in locaiton
    def display(self):
        print(f"Location: ({self.row}, {self.col})")

        # Loops for each product within location, showing details of all
        for product in self.products:
            product.display()