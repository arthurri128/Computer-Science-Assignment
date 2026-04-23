from location import Location
from product import Product
from warehouse import Warehouse


## Test for program to check classes working correctly

# Creating a Warehouse
warehouse = Warehouse(5, 5)

# Creates a location
loc = Location(0, 0, 5)
warehouse.add_location(loc)

#Creating a test product
product = Product("Foil", "ABC123", 1.45, 50)

# Adding product to locaiton 
loc.add_product(product)

# Display the result
warehouse.display_grid()

# Search test
found = warehouse.search_product("ABC123")
if found:
    found.display()