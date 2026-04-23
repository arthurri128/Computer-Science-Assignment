from location import Location
from product import Product
from warehouse import Warehouse

# Main GUI of the program
def main():
    # Create the Warehouse on a 5 by 5 grid
    warehouse = Warehouse(5, 5)

    while True:
        # Menu User is intitally Shown
        print("\nInventory Management System")
        print("1. Add Location")
        print("2. Add Product")
        print("3. Remove Product")
        print("4, Update Quantity")
        print("5. Search Product")
        print("6. Display Warehouse")
        print("7. Exit")
        print()

        # User Choice
        decision = input("Enter choice: ")

        print()

        # 1. (Add Location)
        if decision == "1":
            try:
                # Allows for user to create locations
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
                capacity = int(input("Enter Capacity: "))

                # Boundary Check (Validation)
                if row < 0 or row >= warehouse.rows or col < 0 or col >= warehouse.cols:
                    print("Invalid Position")
                    continue

                # Check if location already exists
                if warehouse.grid[row][col] is not None:
                    print("Location already exists")
                    continue
                
                # Adding location
                loc = Location(row, col, capacity)
                warehouse.add_location(loc)

                print("Location has been added")
            except:
                print("Invalid Input")

        # 2. (Add Product)
        elif decision == "2":
            try:
                name = input("Enter Product Name: ")
                sku = input("Enter SKU: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter quantity: "))

                if quantity < 0:
                    print("Quantity cannot be negative")
                    continue

                # Choose location
                row = int(input("Enter location row: "))
                col = int(input("Enter location column: "))

                if row < 0 or row >= warehouse.rows or col < 0 or col >= warehouse.cols:
                    print("Invalid Location")
                    continue

                location = warehouse.grid[row][col]

                if location:
                    product = Product(name, sku, price, quantity)
                    location.add_product(product)
                else: print("No location exists in that area")
            except:
                print("Invalid Input")


main()