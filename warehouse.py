class Warehouse:

    # Privatising the attributes and setting them to self.__
    def __init__(self, rows, cols,):
        self.rows = rows
        self.cols = cols
        self.grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(None)
            self.grid.append(row)

    
    # Adds location within the warehouse
    def add_location(self, location):
        self.grid[location.row][location.col] = location
    
    # Displays warehouse grid visually for user
    def display_grid(self):
        # Goes through every row and coloumn
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j]:
                    print("[X]", end = "") # This is for if the location is supplied with a product
                else:
                    print("[ ]", end = "") # This is for if the location is not supplied with a product
            print() # Not sure if /n works in this case so seperating with this

    # Searching warehouse for product
    def search_product(self, sku):
        # Goes through 2D array to find product
        for row in self.grid:
            for location in row:
                if location:
                    product = location.find_product(sku)
                    if product:
                        return product
        return None