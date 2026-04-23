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